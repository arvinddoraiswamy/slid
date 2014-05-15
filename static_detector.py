import subprocess
import re
import sys

binary_name = './static_hello'
glibc_sources_dir = 'glibc-2.15'

def main():
  get_idapro_symbols()
  get_glibc_version()
  is_binary_stripped = check_if_binary_stripped()

  if is_binary_stripped == 'not stripped':
    #list_of_symbols = get_symbols_from_binary()
    #library_symbols = search_library_for_symbols(list_of_symbols)
    library_symbols = search_library_for_symbols()

    f=open('libraryfuncs','w')
    for i in library_symbols:
      f.write(i+'\n')
    f.close()

def get_idapro_symbols():
  global idapro_symbols

  f=open('ida_functions.txt','rU')
  t1=f.read()
  f.close()

  idapro_symbols = t1.split('\n')

#def search_library_for_symbols(list_of_symbols):
def search_library_for_symbols():
  global idapro_symbols
  library_symbols = []
  #for symbol in list_of_symbols:
  for symbol in idapro_symbols:
    p1 = subprocess.Popen(["grep","-nr",symbol,glibc_sources_dir], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep","-iv","changelog"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(["wc","-l"], stdin=p2.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    p2.stdout.close()
    t1 = p3.communicate()[0][:-1]

    if int(t1,10) > 10:
      library_symbols.append(symbol)
  
  return library_symbols

def get_symbols_from_binary():
  list_of_symbols=[]
  count=0

  p1 = subprocess.Popen(["nm",binary_name], stdout=subprocess.PIPE)
  t1 = p1.communicate()[0]
  t2=t1.split('\n')

  #Last line is blank - ignore it
  while count<len(t2)-1:
    t3=[]
    t3=t2[count].split()
    if not t2[count].startswith(" "):
      list_of_symbols.append(t3[2])
    else:
      list_of_symbols.append(t3[-1])
    count+=1
  
  return list_of_symbols

def get_glibc_version():
  p1 = subprocess.Popen(["apt-cache","show","libc6"], stdout=subprocess.PIPE)
  p2 = subprocess.Popen(["grep","Version"], stdin=p1.stdout, stdout=subprocess.PIPE)
  p1.stdout.close()
  glibc_version_output= p2.stdout.read()
  print glibc_version_output
  print "Ensure that you download the sources of the glibc version displayed here and place them in the directory given above.\n"

def check_if_binary_stripped():
  strip_pattern = '(,\s*)(not stripped)(\s*)$'
  p1 = subprocess.Popen(["file",binary_name], stdout=subprocess.PIPE)
  file_cmd_output= p1.stdout.read()
  
  regex=re.compile(strip_pattern)
  m1=regex.search(file_cmd_output)

  if m1:
    return m1.group(2)
  
main()
