##############################################################################################################################
# as specified, the input is a single dfd file
def dfd_dfb_parsing(dfd_file):
    
    dfb_fields          = []
    dfd_fields          = []
    additionnal_fields  = []
    errorcode           = 0
    error               = 0
    # filetype specifies the associated file type, either dfx or dfb
    # ##########################################################################################
    #  associated file seems to mean data file
    # ##########################################################################################
    filetype            = "" 
    #trying to open dfd and dfx or dfb associated file
    try:
        dfd = open(dfd_file, "r", encoding=('latin-1'))
    except:
        print("An error occured while trying to open : " + dfd_file)
        errorcode = 1
    # execution not end here

    # trying to open dfx or dfb associated file
    # file like dfx and dfb contains the column titles of the dfd file
    if errorcode == 0:
        try:
            dfb = open(dfd_file.split('.')[0]+".dfb","r")
            filetype = "dfb"
        except:
            errorcode = 2
        # the associated file is not a dfb one
        # then let's check whether it's dfx or not
        if errorcode == 2:
            try:
                dfb = open(dfd_file.split('.')[0]+".dfx","r")
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
        # useful lines extracted from dfd files 
        for lines in dfd:
            # replace '\n' with ' '
            line = lines.replace(chr(10),' ')
            # replace '\r' with ' '
            line = line.replace(chr(13),' ')
            if line[0:5] == "K2002":
                dfd_fields.append(line)
            if line[0:5] == "K2004":
                dfd_fields.append(line)
            if line[0:5] == "K2142":
                K2142_FOUND = True
                dfd_fields.append("datetime")
                dfd_fields.append("status")
                dfd_fields.append("MSN")
                dfd_fields.append("nest")

        #if not found insert it at default position
        if K2142_FOUND == False:
            dfd_fields.insert(2,"*datetime")
            dfd_fields.insert(3,"*status")
            dfd_fields.insert(4,"*MSN")
            dfd_fields.insert(5,"*nest")

        # dfd_fields will look like [("K2002", "K2004", )"K9000/1 ", "datetime", "status", "MSN", "nest"]

##############################################################################################################################
#       the problem might be here
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
            if len(tmp) == len(dfd_fields):
                dfb_fields.append(tmp)
            else:
                additionnal_fields.append(tmp)
        dfd.close
        dfb.close

        # print("K2142_FOUND: ", K2142_FOUND)


        # after this step, I collected the fields names from dfd
        # hopefully they match the fields in dfx

        #plausibility check based on supposed field description
        for i in range(0,len(dfd_fields),1):
            if dfd_fields[i] == "datetime":
                for items in dfb_fields:
                    if len(items[i].split('/'))<2:
                        error+=1
                        print("error in datetime : ")
            if dfd_fields[i] == "status":
                for items in dfb_fields:
                    if len(items[i].split(','))<2 and len(items[i])>3:
                        error+=1
                        print("error in status : ")
            if dfd_fields[i] == "MSN":
                for items in dfb_fields:
                    if items[i][0:1] != '#':
                        error+=1
                        print("error in MSN : ")
            # removing "Not measured" lines of the file
            if dfd_fields[i][0:5] == "K2004" and filetype == "dfb":
                items = 0
                while items <len(dfb_fields):
                    if dfb_fields[items][i] == "255":
                        del(dfb_fields[items])
                        items = 0
                    else:
                        items+=1
                
        if error > 0:
            errorcode = 4
            print("errors in file parsing : ", str(error))
    else:
        # in case dfd file was ok and no dfx and dfb was found
        if errorcode == 2 or errorcode == 3:
            dfd.close           
    return dfd_fields,dfb_fields,additionnal_fields,errorcode,error