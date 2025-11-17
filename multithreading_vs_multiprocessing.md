# Multithreading

   One person doing many tasks at the same time by switching very fast.  

  ### Definition:  

  Multithreading allows multiple threads to run inside a single process. They share the same memory.  

  In Python, because of the GIL (Global Interpreter Lock), threads cannot run CPU tasks truly in parallel — but they work great for I/O-bound tasks (network calls, file I/O, waiting tasks).

# Multiprocessing

  Many person doing one-one task each at the same time.

  ### Definition:

  Multiprocessing creates multiple processes, each with its own Python interpreter and memory space.  

  It bypasses the GIL — meaning CPU tasks can run in true parallel. Best for CPU-bound tasks (heavy calculations, image processing, data crunching).  
