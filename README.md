slid
====

* Get a list of all the functions and their instructions for the binary you want to reverse as well as all the libraries that you think may be part of it.

  FOR %x IN ("C:\data\IDBstore\*.i64") do idaw64 -A -L"C:\data\log.txt" -S"C:\data\save_disasm.py" "%x"

* Compare functions of the binary with the functions of all the libraries. The aim  here is to identify a match. Save the output of this comparison. In the example below, the output of the statically linked binary is driver.txt

  python function_compare.py driver.txt

* Use the output obtained from the previous step to accordingly rename functions inside IDA. All complete matches
must be renamed directly. This code is nearly done, but I haven't finalized exactly how I want the renaming to happen. Will do that soon.

  idaw64 -A -L""C:\data\log.txt" -S"C:\data\rename_funcs.py" driver

-----------------------------------------------------------------------------------------------------------------------

OLD CONTENT. IGNORE FOR NOW. WILL CLEAN SOON.

1. Get a list of the functions that are displayed inside IDA. The aim is to identify as many functions as possible that are part of some
   standard library. As of now, we're only looking at glibc. 
   
   "C:\Program Files (x86)\IDA 6.4\idaw64" -c -o"C:\Users\arvind\Desktop\static" -L"C:\Users\arvind\Desktop\static\batch_log.txt" -A -S"C:\Users\arvind\Desktop\static\get_vuln_functions_list.py" "C:\Users\arvind\Desktop\static\static_hello"

   Copy the output of the script into the folder where the file static_detector.py is.

2. Now identify which of these symbols are present in the glibc sources.

   python static_detector.py
   
3. Copy the output of this script into the folder where the file rename_functions.py is.

   "C:\Program Files (x86)\IDA 6.4\idaw64" -o"C:\Users\arvind\Desktop\static" -L"C:\Users\arvind\Desktop\static\batch_log.txt" -A -S"C:\Users\arvind\Desktop\static\rename_funcs.py" "C:\Users\arvind\Desktop\static\static_hello"
   
4. Open the IDA64 file (IDA database) and notice that a number of functions have been renamed.
