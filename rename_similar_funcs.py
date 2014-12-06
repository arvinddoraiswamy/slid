import idaapi
import idautils
import sys

def get_similar_functions():
  func_library_map={}
  with open('similar_functions','rU') as f:
    l2=[line[:-1] for line in f.readlines()]

  for i in l2:
    t1= i.split('-')
    func_library_map[t1[0][:-1]]= t1[1]
    
  return func_library_map

def rename_functions_ida(func_library_map):
  print func_library_map.keys()
  #Repeat for list of segments
  for n in xrange(idaapi.get_segm_qty()):
    #Get number of segments
    seg = idaapi.getnseg(n)
    if seg:
      #Get list of functions in that segment
      funcs=idautils.Functions(seg.startEA, seg.endEA)
      for funcaddress in funcs:
        name=GetFunctionName(funcaddress)
        if func_library_map.has_key(name):
          MakeNameEx(funcaddress,func_library_map[name][1:]+"_"+name,SN_NOWARN)

#Wait for analysis to complete
idaapi.autoWait()

#Load functions list present in library sources
func_library_map= get_similar_functions()

#Get existing functions from IDA
rename_functions_ida(func_library_map)

#Exit IDA
idc.Exit(0)
