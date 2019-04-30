#Terminology
"""
data file: 
    Extension:      .dfx || .dfb
    Definition:     the file containing the data

associated file: 
    Extension:      .dfd
    Definition:     the file containing titles for the data
"""

##############################################################################################################################
# INPUT:    a single dfd file
# RETURN:   dfd_fields          - titles for the data
#           dfb_fields          - data
#           additionnal_fields  - list of data that does't match the title in dfb_fields
#           errorcode           - specifies error type if there's any
#           error               - number of total errors
def dfd_dfb_parsing(dfd_file):
    
    # variable defining
    # *********************************************************
    dfd_fields          = [] # the titles of data from associated files
    dfb_fields          = [] # the data
    additionnal_fields  = [] # the abnormal data

    errorcode           = 0
    error               = 0

    difference          = 0 
    # the length difference between a line from .dfd and a line from .dfx
    
    first_fields        = [] 
    # the first few fields of the final .csv file
    # the data of these fields is in .dfd rather than .dfx
    # so we need an extra list to store them

    filetype            = "" 
    # either dfb or dfx, two possible types for data
    # but we don't know which we have yet

    # file existense checking
    # *********************************************************
    try:
        dfd = open(dfd_file, "r", encoding=('latin-1'))
        # print("dfd_file: ",dfd_file)
    except:
        print("An error occured while trying to open : " + dfd_file)
        errorcode = 1

    # trying to open the associated file
    # i.e., the .dfd files containing the data title
    if errorcode == 0:
        try:
            dfb = open(dfd_file.split('.')[0]+".dfb","r", encoding=('latin-1'))
            filetype = "dfb"
        except:
            errorcode = 2
        # the associated file is not .dfb
        # then check whether it's .dfx
        if errorcode == 2:
            try:
                dfb = open(dfd_file.split('.')[0]+".dfx","r", encoding=('latin-1'))
                filetype = "dfx"
                errorcode = 0
            except: # no associated files are found
                print("An error occured while trying to open : "+dfd_file.split('.')[0]+".dfb or .dfx")
                errorcode = 3
    # print("The error code is " + str(errorcode))
    # print(dfd)

    if errorcode == 0: # no error happened
        # parsing dfd, getting the titles
        # *********************************************************
        """
        dfd_fields will look like 
        [   "K1001", 
            "K1002", 
            ......, 
            "C_052 SM Position befor joining stator TD1 - Actual value", 
            "Attribute", 
            "Date/Time",
            "Event 1", 
            "Event 2", 
            "Event 3", 
            "Event 4", 
            "Batch Number", 
            "Nest Number", 
            "C_052 SM Position before joining stator TD1 - difference value", 
            "Attribute", 
            "C_052 SM Position befor joining stator TD2 - Actual value", 
            "Attribute", 
            ......  
        ]
        """
        
        # there are more lines than we need in the .dfd file
        # in most cases, only the lines starting with "K2002" contain the data title
        
        K2142_1_FOUND = False 
        # this parameter helps us to format the .csv file
        # by locating where to insert additional columns

        for lines in dfd:
            # replace '\n' with ' '
            line = lines.replace(chr(10),' ')
            # replace '\r' with ' '
            line = line.replace(chr(13),' ')
            if line[0:2] == "K1":
                if line[0:5] == "K1222":
                    # this title doesn't appear in the example file
                    # plus, some .dfx files don't have this data title
                    # so we just skip it
                    continue
                dfd_fields.append(line[0:5])
                first_fields.append(line[6:-1])
                difference = difference + 1
                # these data should be in the final .csv file
                # but they only appears in the associated file
                # so each appearance of these data can cause a difference of 1 
                # in the length of dfd_fields and dfb_fields
            if line[0:5] == "K2002":
                index = line.find(' ')
                dfd_fields.append(line[index+1:])
                # dfd_fields.append(line)
                dfd_fields.append("Attribute")
            if line[0:8] == "K2001/2 ":
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
        #if not found insert it at the end
        if K2142_1_FOUND == False:
            dfd_fields.append("Date/Time")
            dfd_fields.append("Event 1")
            dfd_fields.append("Event 2")
            dfd_fields.append("Event 3")
            dfd_fields.append("Event 4")
            difference = difference + 3
            dfd_fields.append("Batch Number")
            dfd_fields.append("Nest Number")
        # print("K2142_1_FOUND: ", K2142_1_FOUND)
        # print("first_fields: ",first_fields)


        # parsing dfb, getting data matching the titles
        # *********************************************************
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
                # skip lines like "K0097/0 b2e1408c-7029-46b4-9a2c-716e3de27458", starting with "K0097"
                # those lines are useful only to QsStat softwares

            # the lengths of dfb_fields and dfd_fields should match
            # each data corresponds to one title
            # print("len(tmp) = ",len(tmp),"; len(dfd_fields) = ",len(dfd_fields))
            # print("difference: ", difference)
            if len(tmp) + difference == len(dfd_fields):
                # print("len(tmp) == len(dfd_fields)")
                lis = first_fields[:]
                lis.extend(tmp[0:3])
                event_lis = parse_event(tmp[3])
                # print("event_lis: ",event_lis)
                lis.extend(event_lis)
                lis.extend(tmp[4:])
                dfb_fields.append(lis)
            else:
                # print("len(tmp) != len(dfd_fields)")
                additionnal_fields.append(tmp)
        dfd.close
        dfb.close

        # after this step, we've collected 
        #       1). the fields names from .dfd
        #       2).  the data in .dfx/dfb
        # hopefully they will match

        # plausibility check
        # *********************************************************
        # check the format of some fields
        # to know whether we have the correct data in the correct field
        # for example, if we have #12345678 in datetime field
        # it's wrong
        # what's expected is something like 2019/03/05
        for i in range(0,len(dfd_fields),1):
            if dfd_fields[i] == "Date/Time":
                for items in dfb_fields:
                    if len(items[i].split('/'))<2:
                        error+=1
                        print("error in datetime : ")
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
        if error > 0:
            errorcode = 4
            print("errors in file parsing : ", str(error))
    else: # this else corresponds to "if errorcode == 0: " at line 78
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