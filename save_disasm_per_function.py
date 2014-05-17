import idaapi
import idautils
import xml.etree.cElementTree as ET

disassembly_file = 'disasm.txt'

def save_disasm_functions_ida():
  global funcDisassList

  funcDisassList = {}
  disasm_per_function = ""
  
  for segAddress in Segments():
    segName = SegName(segAddress)
    if segName == ".text":
      funcs = Functions(SegStart(segAddress), SegEnd(segAddress))
      for i in funcs:
        disasm_per_function = ""
        start=0
        end=0
        
        funcBoundaries = Chunks(i)
        for j in funcBoundaries:
          if not GetFunctionName(i).startswith("sub_"):
            start=j[0]
            end=j[1]
            
            while (start < end):
              disasm_per_function = disasm_per_function + "^^^" + GetDisasm(start)
              start+=ItemSize(start)

            funcDisassList[GetFunctionName(i)] = disasm_per_function

  f=open(disassembly_file, 'w')
  for key in funcDisassList.keys():
    f.write('+'*10+key+''+'+'*10+"\n\n"+funcDisassList[key]+"\n\n")
  f.close()

def write_xml_file():
  root = ET.Element("root")

  for key in funcDisassList.keys():
    k1 = ET.SubElement(root, key)
    v1 = ET.SubElement(k1, "value")
    v1.set("name", funcDisassList[key])
    
  tree = ET.ElementTree(root)
  tree.write("filename.xml")

#Wait for analysis to complete
idaapi.autoWait()

#Save disassembly of binary to a file
save_disasm_functions_ida()

#Write results to an XML file
write_xml_file()

#Exit IDA
idc.Exit(0)
