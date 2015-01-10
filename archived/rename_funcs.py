import idaapi
import idautils
import sys

def get_library_functions():
  global functions_in_library
  f=open('libraryfuncs','rU')
  t1 = f.read()
  f.close()

  functions_in_library = t1.split('\n')

def rename_functions_ida():
  #Repeat for list of segments
  for n in xrange(idaapi.get_segm_qty()):
    #Get number of segments
    seg = idaapi.getnseg(n)
    if seg:
      #Get list of functions in that segment
      funcs=idautils.Functions(seg.startEA, seg.endEA)
      for funcaddress in funcs:
        name=GetFunctionName(funcaddress)
        if name in functions_in_library:
          MakeNameEx(funcaddress,"glibc_"+name,SN_NOWARN)

#Wait for analysis to complete
idaapi.autoWait()

#Load functions list present in library sources
get_library_functions()

#Get existing functions from IDA
rename_functions_ida()

#Exit IDA
idc.Exit(0)
