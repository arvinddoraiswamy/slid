import idaapi
import idautils

def save_disasm_functions_ida():
  for segAddress in Segments():
    segName = SegName(segAddress)
    if segName == ".text":
      funcs = Functions(SegStart(segAddress), SegEnd(segAddress))
      for i in funcs:
        funcBoundaries = Chunks(i)
        for j in funcBoundaries:
          if GetFunctionName(i) == "exit":
            start=j[0]
            end=j[1]
            
            while (start < end):
              current = GetDisasm(start)
              print str(start) + "\t" + str(ItemSize(start)) + "\t" + GetDisasm(start)

              #Not good as instruction size > 1 almost always and tracking that is going to be hard
              start+=ItemSize(start)

#Wait for analysis to complete
idaapi.autoWait()

#Get existing functions from IDA
save_disasm_functions_ida()

#Exit IDA
idc.Exit(0)
