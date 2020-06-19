.. VBA_Excel documentation master file, created by
   sphinx-quickstart on Sat May 23 11:47:32 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##########
Python
##########
.. contents:: :local:

****************
Python Terminal
****************
Online Python Interpreter
=========================
You may get your first hands-on coding experience with Python using the interpreter below:

.. raw:: html

    <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/repls/ConventionalDopeyParallelprocessing?lite=true">
   
    </iframe>

Conventions Used
================
It is conventional for code snippets to be displayed in boxed section for ease of reference.

.. note::

   .. code-block:: python
    
      print("Hello world")
      >>> Hello world

******************
1. Inputs
******************

1.1 Built-in Data Types
==========================
The following built-in data types illustrate the extent of data manipulation that Python can execute. [[#PyInput]_]


.. list-table::  
   :widths: 4 5 12 
   :header-rows: 1

   * - Built-in Types
     - Examples
     - Notes

   * - Text Type
     - str
     - String
         
   * - Numeric Types
     - int, float, complex
     - Integers, floating point numbers and complex numbers

   * - Sequence Types
     - list, tuple, range
     - List, tuples and range objects

   * - Mapping Types
     - dict
     - Dictionary that stores key-value pairs

*************
2. Process
*************

2.1 Assignment Statements for Variables 
=======================================
Assigning a data type for a variable can be done in the Python terminal as such:

.. note::
   .. code-block:: 
    
      <Variable Name> = <Type>

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python

         ' Assigning an integer value of 1.0 m to the variable Pile_Diameter
         Pile_Diameter =  1.0 


2.2 Functions
=========================
Formulating a user-defined Python function follows steps as below:

.. note::

   .. code-block:: Python
    
      def <Function_Name> ([Argument 1], [Argument 2], ..):

         Function_Results = [Operation]

      return Function_Results

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: 

         def R_Pile(Q_Base, Q_Shaft):

            ' Expressing pile resistance as a function of
            ' Base resistance, Q_Base
            ' Shaft resistance, Q_Shaft

            Pile_Resistance = Q_Base + Q_Shaft
         
         return Pile_Resistance

*************
3. Decisions
*************
3.1 Conditional Statements
===========================
You can introduce nested 'if' statements as below to improve readibility of code [[#PyIfs]_]:

.. note::

   .. code-block:: 
    
      if <Condition 1>:

         [Statement 1]

      elif <Condition 2>:

         [Statement 2]

      else:

         [Statement 3]

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: 

         if Pile_Diameter == 0.45:

            ' If pile diameter is 0.45 m, then define pile working load as 1,900 kN
            PWL = 1900

         elif Pile_Diameter == 0.50:

            ' Else if pile diameter is 0.50 m, then define pile working load as 2,300 kN     
            PWL = 2300

         else:

            ' Else, define pile working load as 3,000 kN
            PWL = 3000
      
3.2 Looping Operations
===========================

Automate your code with 'for' statements. [[#PyFors]_]

.. note::

   .. code-block:: 
    
      for counter in list:
      
          [Statement 1]

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down  

   .. hint::

      .. code-block:: 

         'Setting up a `for` statement to count the number of piles
         'in a piling log
         for counter in Pile_Log                   
         
            ' Adding 1 to Pile_Number for every iteration
            Pile_Number = Pile_Number + 1                      

******************
4. Debugging Tips
******************
.. tip::

   You can introduce **Python breakpoints** to pause the execution of code

      Code execution by Python stops at the designated breakpoints.
      
      Therefore,you can examine your code if there is any obvious error such as syntactic mistakes.



**************
5. References
**************
.. [#PyInput] 

`Python Built-In Types <https://docs.python.org/3/library/stdtypes.html#>`_ 

.. [#PyIfs]

`Python More Control Flow Tools <https://docs.python.org/3/tutorial/controlflow.html#>`_

.. [#PyFors]

`Python for Statements <https://docs.python.org/3/tutorial/controlflow.html#for-statements>`_
