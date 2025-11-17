# Python Advanced Level Questions

  1. Multithreading v/s Multiprocessing
    
  - **Multithreading : One person doing many tasks at the same time by switching very fast.**
     
    Multithreading allows multiple threads to run inside a single process. They share the same memory.  

  - **Multiprocessing : Many person doing one-one task each at the same time.**

    Multiprocessing creates multiple processes, each with its own Python interpreter and memory space.

---

  2. What is GIL?

     GIL = Global Interpreter Lock = It is a mutex that allows only one thread to run python code at a time. Ensure memory safety.

---

  3. What is Namespace and it's types?

     Namespace is a container that holds the name of the variables, function and classed to avoid conflicts.

     Types :  
       1. Build-in  :  print(), len()
       2. Global    :  x=10
       3. Local     :  def fun(): y=10
       4. Enclosing :  def outer(): def inner(): z=10
    
     Order :  LEGB : Local, enclosing, global, builtin

---

  4. Monkey Patching

     Dynamically modifying / extending a class / module at runtime. It allows adding/changing methods without change the original source code.

     Code:

     ```
       class Robot:
          def walk(self):
             print("Walking")

       r = Robot()
       r.walk()

       def dance(self):
           print("Dancing")

       Robot.dance = dance
       r.dance()
     ```

    
