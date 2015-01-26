slid
====

* Get a list of all the functions and their instructions for the binary you want to reverse as well as all the libraries that you think may be part of it. Before running this script, make sure you have the binary you want
to reverse as well as all the libraries you think are a part of the binary in the *"C:\data\IDBstore"* directory.

   For the code I used I put the *test* binary as well as all the files from the *libc.a* archive into the directory      *"C:\data\IDBstore"*. The *libc.a* archive was found on my system at */usr/lib/x86_64-linux-gnu/libc.a*. The files     from this archive can be extracted by using the command *ar x /usr/lib/x86_64-linux-gnu/libc.a*

   **FOR %x IN ("C:\data\IDBstore\*") do idaw64 -A -L"C:\data\log.txt" -S"C:\data\save_disasm.py" "%x"**
  
   The result of running this script will store the disassembly of the binary to be reversed and a lot of the
   associated libraries in a folder called *input*.
   
   Look at *1.png* for the result of this script.

* Compare functions of the binary with the functions of all the libraries. In the example below, the output of the statically linked binary is test_mnem.txt. The -m option compares only the mnemonics of all the functions.

  **python function_compare.py test_mnem.txt -m**
  
  The result of running this script will be stored in a new file called *input_to_rename_function.txt*.
  
  Look at *2.png* for the result of this script.

* Use the output obtained from the previous script to accordingly rename functions inside IDA.

   Look at *3.png* and *4.png* before running this script. The line numbers show the starting (1039) and 
   ending line numbers(1159) for *sub_* functions. This means there are *120* functions.
   
   *5.png* is a screenshot that shows how to run this script.
   
  **idaw64 -A -L""C:\data\log.txt" -S"C:\data\rename.py" test**
  
  The result of running this script is that all the functions that started with *sub_* inside the binary to be reversed
  AND found a match with some library somewhere will be renamed. Open up the saved IDB as usual - you will see that
  a number of functions have been renamed.
  
   Look at *6.png* and *7.png* for the result of this script. The line numbers show the starting (1120) and 
   ending line numbers(1159) for *sub_* functions. This means that there are now *39* functions. This means that *81*
   functions were renamed because they matched *some function* inside *libc.a*.
   
   Look at *8.png* and *9.png* for examples of how the names of the functions look once they have been renamed. The
   functions whose names start with **single** are named because only a single match was found in libc.a. The
   functions whose names start with **multiple** are named because multiple matches were found in libc.a.
