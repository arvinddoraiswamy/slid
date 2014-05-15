import idaapi
import idautils

def get_functions_ida():
  #Repeat for list of segments
  for n in xrange(idaapi.get_segm_qty()):
    #Get number of segments
    seg = idaapi.getnseg(n)
    if seg:
      #Get list of functions in that segment
      funcs=idautils.Functions(seg.startEA, seg.endEA)
      for funcname in funcs:
        name = GetFunctionName(funcname)
        print name

#Wait for analysis to complete
idaapi.autoWait()

#Get existing functions from IDA
get_functions_ida()

#Exit IDA
idc.Exit(0)
