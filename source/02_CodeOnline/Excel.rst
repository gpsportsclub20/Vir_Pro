.. VBA_Excel documentation master file, created by
   sphinx-quickstart on Sat May 23 11:47:32 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##########
VBA Excel
##########

.. contents:: :local:

*************
VBA Terminal
*************

Conventions Used
================
It is conventional for code snippets to be displayed in boxed section as below for ease of reference.

.. note::

   .. code-block:: python
    
      MsgBox "Hello world"
      >>> Hello world

******************
1. Inputs
******************

1.1 Numeric Data Type  
======================
The following data types have been ranked according to the size of computer memory required. ([#Input]_)

.. list-table::  
   :widths: 3 3 15 3
   :header-rows: 1

   * - Data Type
     - Number Type
     - Range of Values
     - Memory Usage


   * - Byte
     - Integer
     - 0 through 255
     - 1 byte
   
   * - Integer
     - Integer
     - -32,768 to 32,767
     - 1 byte

   * - Boolean
     - Integer
     - **True** or **False**
     - 2 bytes

   * - Long
     - Integer
     - -2,147,483,648 through 2,147,483,647
     - 2 bytes

   * - Single
     - Real
     - Single-Precision Floating-Point 
     - 4 bytes
   
   * - Double
     - Real
     - Double-Precision Floating-Point 
     - 8 bytes

1.2 Variable Data Type
=======================
You can also introduce data type with variable storage size to fit the purpose of your algorithm.

.. list-table::  
   :widths: 3 15 3
   :header-rows: 1

   * - Data Type
     - Range of Values
     - Memory Usage
     
   * - String
     - 0 to approximately 2 billion Unicode characters
     - Varies

   * - Variant 
     - 0 through 65,535 
     - Varies

*************
2. Process
*************

2.1 Declaration of Variables 
=============================
Declaring an input or variable can be done in the VBA terminal as such:

.. note::
   .. code-block:: 
    
      Dim <Variable Name> as <Type>


.. hint::

   .. code-block:: 

      Dim <Pile_Diameter> as <Integer>                   ' Declaring Pile_Diameter as an interger

2.2 Functions
=========================
Formulating a user-defined VBA function follows steps as below:

.. note::

   .. code-block:: 
    
      [Public Function] <Function_Name> ([Argument 1], [Argument 2], ..) [As<Type>]

         <Function_Name> = <Function_Results>

      End Function

.. hint::

   .. code-block:: 

      [Public Function] Sum(x, y) As Single

         ' Expressing the summation operator
         Sum = x + y
      
      End Function

*************
3. Decisions
*************
3.1 Conditional Statements
===========================
You can introduce nested 'if' statements as below to improve readibility of code ([#Ifs]_): 

.. note::

   .. code-block:: 
    
      If <Condition 1> Then

         [Statement 1]

      ElseIf <Condition 2> Then

         [Statement 2]

      Else 

         [Statement 3]
      
      End If

.. hint::

   .. code-block:: 

      If Pile_Diameter = 0.45 Then

         ' Assigning pile working load of 1,900 kN to pile of diameter 0.45 m
         PWL = 1,900

      ElseIf Pile_Diameter = 0.50 Then

         ' Assigning pile working load of 2,300 kN to pile of diameter 0.50 m      
         PWL = 2,300

      Else 

         ' Assigning pile working load of 3,000 kN to pile of diameter 0.60 m      
         PWL = 3,000
      
      End If

3.2 Looping Operations
===========================

Automate your code with 'For...Next' statements. ([#Fors]_)

.. note::

   .. code-block:: 
    
      For counter = start To end [Step step]
      
      [Statement 1]

      [Exit for]

      [Statement 2]

      Next [counter]

      
.. hint::

   .. code-block:: 

      For counter = 1 To 100 [Step 1]                    'Setting up 100 repetitions
      
      Pile_Number = Pile_Number + 1                      ' Adding 1 to Pile_Number

      [Exit for]

      MsgBox "Total Number of Piles is" & Pile_Number    ' Displaying the total number of piles

      Next [counter]

**************
4. References
**************
.. [#Input] 

`Microsoft Data Type Summary <https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/data-type-summary>`_ 

.. [#Ifs]

`Microsoft Using If...Then...Else Statements <https://docs.microsoft.com/en-us/office/vba/language/concepts/getting-started/using-ifthenelse-statements>`_

.. [#Fors]

`Microsoft For...Next Statement <https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/fornext-statement>`_