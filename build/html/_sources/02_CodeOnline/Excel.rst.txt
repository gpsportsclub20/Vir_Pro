.. VBA_Excel documentation master file, created by
   sphinx-quickstart on Sat May 23 11:47:32 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

VBA Excel
============

.. contents:: :local:

Conventions Used
^^^^^^^^^^^^^^^^
.. note:: 
    
   It is conventional for code blocks to be displayed in boxed section as below for ease of reference::

      print("Hello world")

      >>> Hello world

Data Types
^^^^^^^^^^^^^^^^^^
Numeric Data Types 
------------------
.. list-table::  
   :widths: 5 5 25 
   :header-rows: 1

   * - Data Type
     - Number Type
     - Range of Values

   * - Boolean
     - Integer
     - True = -1, False = 0
   
   * - Integer
     - Integer
     - -32,768 to 32,767

   * - Long
     - Integer
     - -2,147,483,648 through 2,147,483,647

   * - Single
     - Real
     - Single-Precision Floating Point (with 4 Byte memory required)
   
   * - Double
     - Real
     - Double-Precision Floating Point (with 8 Byte memory required)

Variable Data Types 
--------------------

.. list-table::  
   :widths: 5 25 
   :header-rows: 1

   * - Data Type
     - Range of Values
     
   * - String
     - 0 to approximately 2 billion Unicode characters

   * - Byte
     - 0 through 255 (unsigned)

   * - Variant
     - 0 through 65,535 (unsigned)