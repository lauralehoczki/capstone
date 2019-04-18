# a utility file written by me
# containing some useful variables or functions
# import utils

##############################################################################################################################
# INPUT:    a single dfd file
# RETURN:   dfd_fields - titles for the data
#           dfb_fields - data
#           additionnal_fields - list of data that does't match the title in dfb_fields
#           errorcode - specifies error type if there's any
#           error - number of total errors
def dfd_dfb_parsing(dfd_file):
    
    dfd_fields          = [] # the title of data
    dfb_fields          = [] # the data
    additionnal_fields  = [] # not sure what this is used for 
    first_fields        = [] # the first few fields of dfd
                             # the data is in dfd rather than dfx
    errorcode           = 0
    error               = 0
    difference          = 0 # the length difference between dfb_fields and dfd_fields

    # filetype specifies the associated file type, either dfx or dfb
    # ##########################################################################################
    # associated file means the title file
    # ##########################################################################################

    filetype            = "" 
    #trying to open dfd and dfx or dfb associated file
    try:
        dfd = open(dfd_file, "r", encoding=('latin-1'))
        # print("dfd_file: ",dfd_file)
    except:
        print("An error occured while trying to open : " + dfd_file)
        errorcode = 1
    # execution not end here

    # trying to open dfx or dfb associated file
    # file like dfx and dfb contains the column titles of the dfd file
    if errorcode == 0:
        try:
            dfb = open(dfd_file.split('.')[0]+".dfb","r", encoding=('latin-1'))
            filetype = "dfb"
        except:
            errorcode = 2
        # the associated file is not a dfb one
        # then let's check whether it's dfx or not
        if errorcode == 2:
            try:
                dfb = open(dfd_file.split('.')[0]+".dfx","r", encoding=('latin-1'))
                filetype = "dfx"
                errorcode = 0
            except:
                print("An error occured while trying to open : "+dfd_file.split('.')[0]+".dfb or .dfx")
                errorcode = 3
    # in the two cases above, no associated files are found

    # if files are ready
    # which means both dfd and dfx/dfb files are ready
    # print("The error code is " + str(errorcode))
    # print(dfd)
    if errorcode == 0:
        K2142_FOUND = False 
        # the end of a list of titles belonging to a certain part
        # the dfd files contains titles for parts
        # even for the same parameter of different parts, e.g., MSN number for part No.4 and No.6
        # the machine on the production line will save it into differnt titles
        # for example, MSN_part_4 and MSN_part_6
        # so each part will have a list of titles in the dfd file
        # K2142 marks the end of this title list of a certain part

        # to find certain titles from the dfd file
        for lines in dfd:
            # replace '\n' with ' '
            line = lines.replace(chr(10),' ')
            # replace '\r' with ' '
            line = line.replace(chr(13),' ')
            if line[0:2] == "K1":
                if line[0:5] == "K1222":
                    # this field doesn't appear in the example file
                    # plus, some dfx files don't have this field
                    # so we just discard it
                    continue
                dfd_fields.append(line[0:5])
                first_fields.append(line[6:-1])
                difference = difference + 1
            if line[0:5] == "K2002":
                index = line.find(' ')
                dfd_fields.append(line[index+1:])
                # dfd_fields.append(line)
                dfd_fields.append("Attribute")
            if line[0:8] == "K2142/1 ":
                K2142_1_FOUND = True
                dfd_fields.append("Date/Time")
                dfd_fields.append("Event 1")
                dfd_fields.append("Event 2")
                dfd_fields.append("Event 3")
                dfd_fields.append("Event 4")
                difference = difference + 3
                # this is only one field in dfx file
                # and no corresponding field in the dfd file
                # we split it into 4 in the final csv file
                # i.e., Event1, Event2, Event3, Event4
                dfd_fields.append("Batch Number")
                dfd_fields.append("Nest Number")

        #if not found insert it at default position
        if K2142_1_FOUND == False:
            dfd_fields.append("Date/Time")
            dfd_fields.append("Event 1")
            dfd_fields.append("Event 2")
            dfd_fields.append("Event 3")
            dfd_fields.append("Event 4")
            difference = difference + 3
            dfd_fields.append("Batch Number")
            dfd_fields.append("Nest Number")

        # print("first_fields: ",first_fields)

        # dfd_fields will look like [("K2002", "K2004", )"K9000/1 ", "datetime", "status", "MSN", "nest"]

##############################################################################################################################
#       P1 --> the problem might be here
#       while writing the code, I found the there's a difference between the format of 
#       1). the data files sent to us by MR.Mangonot
#       2). the files that the Python file is designed to process (the Python file MR.Mangonot sent us)

#       so that we'll have a super long dfd_fields but a short dfb_fields
##############################################################################################################################

        # lines extracted from dfb according to dfd files
        # dfb is an associated file!
        for lines in dfb: 
            # replace 'si' (Shift In / X-Off) with 'dc4' (Device Control 4)
            tmp = lines.replace(chr(0x0F),chr(0x14))
            # replace '\n' with ' '
            tmp = tmp.replace(chr(0x0A),' ')
            # replace '\r' with ' '
            tmp = tmp.replace(chr(0x0D),' ')
            # split with 'dc4' (Device Control 4)
            tmp = tmp.split(chr(0x14))
            if (len(tmp) == 1):
                continue 
                # skip the K0097 lines like "K0097/0 b2e1408c-7029-46b4-9a2c-716e3de27458"
                # those lines are useful only to QsStat softwares
##############################################################################################################################
#       P1 (cont.)
#       because we didn't do well with the formatting issue
#       the lengths of dfb_fields and dfd_fields will not match
##############################################################################################################################
            # print("len(tmp) = ",len(tmp),"; len(dfd_fields) = ",len(dfd_fields))
            if len(tmp) + difference == len(dfd_fields):
                # print("len(tmp) == len(dfd_fields)")
                lis = first_fields[:]
                lis.extend(tmp[0:3])
                event_lis = parse_event(tmp[3])
                # print("event_lis: ",event_lis)
                lis.extend(event_lis)
                lis.extend(tmp[4:])
                # if (utils.once == 1):
                #     utils.once = utils.once + 1
                #     print(lis)
                dfb_fields.append(lis)
##############################################################################################################################
#       the problem happens because we didn't enter enough info into dfb
#       the K1*** fields
##############################################################################################################################
            else:
                # print("len(tmp) != len(dfd_fields)")
                additionnal_fields.append(tmp)
        dfd.close
        dfb.close

        # print("K2142_FOUND: ", K2142_FOUND)


        # after this step, I collected the fields names from dfd
        # and the data in dfx
        # hopefully they will match

        # plausibility check based on supposed field description
        # that means to check whether we have the correct data in the correct field
        # for example, if we have #12345678 in datetime field
        # it's wrong
        # what's expected is something like 2019/03/05
        for i in range(0,len(dfd_fields),1):
            if dfd_fields[i] == "Date/Time":
                for items in dfb_fields:
                    if len(items[i].split('/'))<2:
                        error+=1
                        print("error in datetime : ")
##############################################################################################################################
##############################################################################################################################
                # no field is called status in our case
#             if dfd_fields[i] == "status":
#                 for items in dfb_fields:
#                     if len(items[i].split(','))<2 and len(items[i])>3:
#                         error+=1
#                         print("error in status : ")
            if dfd_fields[i] == "Batch Number":
                for items in dfb_fields:
                    if items[i][0] != '#':
                        error+=1
                        print("error in MSN : ")
            # removing "Not measured" lines of the file
            # if dfd_fields[i][0:5] == "K2004" and filetype == "dfb":
            #     items = 0
            #     while items <len(dfb_fields):
            #         if dfb_fields[items][i] == "255":
            #             del(dfb_fields[items])
            #             items = 0
            #         else:
            #             items+=1
##############################################################################################################################
##############################################################################################################################
        if error > 0:
            errorcode = 4
            print("errors in file parsing : ", str(error))
    else:
        # in case dfd file was ok and no dfx and dfb was found
        if errorcode == 2 or errorcode == 3:
            dfd.close           
    return dfd_fields, dfb_fields, additionnal_fields, errorcode, error

##############################################################################################################################
# INPUT:    a comma seperated string extracted from dfx files, containing event info for up to 4 events
# RETURN:   a list of values for event 1 though 4
def parse_event(event):
    lis = event.split(',')
    if (len(lis) > 4):
        return lis[0:4]
    for i in range(4-len(lis)):
        lis.append("null")
    return lis