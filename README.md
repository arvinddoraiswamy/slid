slid
====

* Get a list of all the functions and their instructions for the binary you want to reverse as well as all the libraries that you think may be part of it.

  FOR %x IN ("C:\data\IDBstore\*.i64") do idaw64 -A -L"C:\data\log.txt" -S"C:\data\save_disasm.py" "%x"

* Compare functions of the binary with the functions of all the libraries. The aim  here is to identify a match. Save the output of this comparison. In the example below, the output of the statically linked binary is driver.txt

  python function_compare.py driver.txt

* Use the output obtained from the previous step to accordingly rename functions inside IDA. All complete matches
must be renamed directly. This code is nearly done, but I haven't finalized exactly how I want the renaming to happen. Will do that soon.

  idaw64 -A -L""C:\data\log.txt" -S"C:\data\rename_funcs.py" driver
