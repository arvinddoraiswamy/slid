import idaapi
import idautils

def ascii_to_hex(string):
  t1=list(string)
  t2=''
  for i in t1: 
    t3=re.sub('0x','',str(hex(ord(i))))
    t3=t3.zfill(2)
    t2+=t3

  t2=re.sub('0x','',t2)
  return t2

def save_mnemonics_functions_ida(f1):
  filename= f1
  mnemonics = {}
  flag= 0

  for segAddress in Segments():
    segName = SegName(segAddress)
    if segName == ".text":
      funcs = Functions(SegStart(segAddress), SegEnd(segAddress))
      for address in funcs:
        t1= GetFunctionName(address)
        f1= idautils.FuncItems(address)
        t2=''
        for i in f1:
          t2+= GetMnem(i)
          t2+= '^^^'
        mnemonics[filename+'>'+t1]= t2+'<'+str(address)
        
  return mnemonics

def write_to_file(mnemonics):        
  #Write results to output file
  output_dir="input\\"
  
  output_mnemonics_filename=str(idc.GetInputFile())+'_mnem.txt'
  with open(output_dir+output_mnemonics_filename,'w') as f:
    for key, value in mnemonics.iteritems():
      f.write(key)
      f.write('$$$')
      f.write(value)
      f.write("\n")

#Wait for analysis to complete
idaapi.autoWait()

#Save mnemonics of all the functions of a binary to a file
mnemonics= save_mnemonics_functions_ida(str(idc.GetInputFile()))

write_to_file(mnemonics)

idc.Exit(0)
