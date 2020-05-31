Getting Started
===============
To get started, kindly refer to the workshop materials below:

This is an introductory course for programming to automate calculations with VBA Excel and Python.
It is conventional for code blocks to be displayed in boxed section as below for ease of reference::


   Sub List_All_The_Files_Within_Path()
   
   Dim Row_No As Interger
   Dim No_Of_Files As Interger
   Row_No = 34

   MsgBox ("The number of rows in this file is", Row_No)
   
   >> The number of rows is 34

As for codes in Python, they shall typically be presented in the following form, where the imported modules precede the main code blocks::

   import numpy as np
   import matplotlib.pyplot as plt 

   x = np.linspace(0,2*np.pi,100)
   y = np.sin(x)
   z = 2

.. note:: 
    This function is not compatible with the Python interpreter

.. warning:: 
    Your computer has insufficient random access memory to run this application

Data Types
^^^^^^^^^^
Common data types that constitute a code block in Excel VBA are as follows:

==========     ============
Keyword        Range
==========     ============
Boolean        a) True
               b) False

Integer        a) -32,768
               b) 32,767
==========     ============

Additional Data Types
^^^^^^^^^^^^^^^^^^^^^
Some other data types that are also commonly used are as listed below:

.. list-table::  
   :widths: 5 25 
   :header-rows: 1

   * - Keyword
     - Range

   * - Long
     - -2,147,483,648 to 2,147,483,647
   
   * - Double
     - Double-Precision Floating Point (with 8 Byte memory required)

   * - Single
     - Single-Precision Floating Point (with 4 Byte memory required)
     
   * - String
     - Variable-length and Fixed-length String
       

     
       

     
       

     
      


