import idaapi
import idautils

def get_all_strings():
    """
    Get a list of strings stored in that segment
    """
    list_of_strings = idautils.Strings()
    for string in list_of_strings:
        if not str(string).endswith("\n"):
            f.write(str(string)+'\n')
        else:
            f.write(str(string))

#Wait for analysis to complete
idaapi.autoWait()

#Write results to output file
output_dir="C:\data\output\\"
output_filename=str(idc.GetInputFile())+'.txt'
with open(output_dir+output_filename,'a') as f:
    get_all_strings()

#Exit program
idc.Exit(0)
