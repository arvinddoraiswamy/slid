"""
References:
http://clalance.blogspot.com/2011/01/exiting-python-program.html
"""

import subprocess
import re
import sys
import os

#binary_name = './static_hello'
binary_name = './static_blank'
glibc_sources_dir = 'glibc-2.15'

def main():
  """
  First function that is called.
  """
  try:
    get_idapro_symbols()
    get_glibc_version()
    is_binary_stripped = check_if_binary_stripped()

    if is_binary_stripped == 'not stripped':
      list_of_symbols = get_symbols_from_binary()
      #library_symbols = search_library_for_symbols(list_of_symbols)
      library_symbols = search_library_for_symbols()

      with open('libraryfuncs','w') as f:
        for i in library_symbols:
          f.write(i+'\n')
      #f.close()
  except:
    print 'Oops something went wrong. Dunno what. Go debug.' 

def get_idapro_symbols():
  """
  Get IDA PRO's saved function list and store for future use.
  """
  global idapro_symbols
  try:
    with open('ida_functions.txt','rU') as f:
      t1=f.read()
      idapro_symbols = t1.split('\n')
  except IOError:
    print 'Did you run IDA and save its functions as mentioned in the ReadMe? :)'
    os._exit(1)
    #f.close()

#def search_library_for_symbols(list_of_symbols):
def search_library_for_symbols():
  """
  Search for IDA symbols in glibc source code.
  """
  global idapro_symbols
  library_symbols = []
  #for symbol in list_of_symbols:
  try:
    if os.path.isdir(glibc_sources_dir):
      for symbol in idapro_symbols:
          p1 = subprocess.Popen(["grep","-nr",symbol,glibc_sources_dir], stdout=subprocess.PIPE)
          p2 = subprocess.Popen(["grep","-iv","changelog"], stdin=p1.stdout, stdout=subprocess.PIPE)
          p3 = subprocess.Popen(["wc","-l"], stdin=p2.stdout, stdout=subprocess.PIPE)
          p1.stdout.close()
          p2.stdout.close()
          t1 = p3.communicate()[0][:-1]

          if int(t1,10) > 0:
            library_symbols.append(symbol)
    else:
      print "Sources directory does not exist. Check name and copy sources into it."
  except OSError:
    print "Error grepping through sources. Are you sure grep and wc exist on your system? And you copied the sources in?\n"
    os._exit(1)
  
  return library_symbols

def get_symbols_from_binary():
  """
  Get symbols from current binary and store them.
  """
  list_of_symbols=[]
  count=0

  p1 = subprocess.Popen(["nm",binary_name], stdout=subprocess.PIPE)
  t1 = p1.communicate()[0]
  t2=t1.split('\n')

  #Last line is blank - ignore it
#  while count<len(t2)-1:
#    t3=[]
#    t3=t2[count].split()
#    if not t2[count].startswith(" "):
#      list_of_symbols.append(t3[2])
#    else:
#      list_of_symbols.append(t3[-1])
#    count+=1
#  
#  for count in range(len(t2)-1):
#    t3=t2[count].split()
#    if not t2[count].startswith(" "):
#      list_of_symbols.append(t3[2])
#    else:
#      list_of_symbols.append(t3[-1])
#
  t3 = [symbol.split() for symbol in t2]
  for count,symbol in enumerate(t2):
    if symbol:
      if not symbol.startswith(" "):
        list_of_symbols.append(t3[count][2])
      else:
        list_of_symbols.append(t3[count][-1])

  return list_of_symbols

def get_glibc_version():
  """
  Get version of glibc running on current system.
  """
  print "Glibc version detection using apt-cache\n"
  try:
    p1 = subprocess.Popen(["apt-cache","show","libc6"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep","Version"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    glibc_version_output= p2.stdout.read()
    print glibc_version_output
    print "\n"
  except OSError:
    print "Are you sure you're on a Debian system? If not comment the apt-cache detection out and rerun.\n"
    os._exit(1)

  try:
    print "Glibc version detection using ldd\n"
    p1 = subprocess.Popen(["ldd","--version"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep","ldd"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    glibc_version_output= p2.stdout.read()
    print glibc_version_output
    print "\n"
    print "Ensure that you download the sources of the glibc version displayed here and place them in the directory given above.\n"
  except OSError:
    print "Ha. No ldd either? Manually identify your glibc version and copy the correct sources in.\n"
    os._exit(1)

def check_if_binary_stripped():
  """
  Check if binary stripped and return a result.
  """
  try:
    strip_pattern = '(,\s*)(not stripped)(\s*)$'
    p1 = subprocess.Popen(["file",binary_name], stdout=subprocess.PIPE)
    file_cmd_output= p1.stdout.read()
    
    regex=re.compile(strip_pattern)
    m1=regex.search(file_cmd_output)

    if m1:
      return m1.group(2)
  except:
    print "Does the file binary exist on your system?\n"
  
if __name__ == '__main__':
  main()
