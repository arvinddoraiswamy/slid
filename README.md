slid
====

* Get a list of all the functions and their instructions for the binary you want to reverse as well as all the libraries that you think may be part of it.

  FOR %x IN ("C:\data\IDBstore\*.i64") do idaw64 -A -L"C:\data\log.txt" -S"C:\data\save_disasm.py" "%x"

* Compare functions of the binary with the functions of all the libraries. The aim  here is to identify a match. Save the output of this comparison. In the example below, the output of the statically linked binary is driver.txt. The -m option compares only the mnemonics and will have better accuracy.

  python function_compare.py test_mnem.txt -m
  
  It's also possible to run it *without* the -m option. That isn't as accurate as I'd like it to be, because of the way IDA disassembles files and names its variables. I'm still searching for a fix here. :)

* Use the output obtained from the previous script to accordingly rename functions inside IDA. All complete matches
will be renamed directly.

  idaw64 -A -L""C:\data\log.txt" -S"C:\data\rename.py" test
