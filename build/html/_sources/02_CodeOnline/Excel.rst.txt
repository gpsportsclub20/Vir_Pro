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
It is conventional for code snippets to be displayed in boxed section for ease of reference.

.. note::

   .. code-block:: python
    
      MsgBox "Hello world"
      >>> Hello world

******************
1. Inputs
******************

1.1 Numeric Data Type  
======================
The following data types have been ranked according to the size of computer memory required. [[#Input]_]

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

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: 

         ' Declaring Pile_Diameter as an interger
         Dim Pile_Diameter as Integer                   

2.2 Functions
=========================
Formulating a user-defined VBA function follows steps as below:

.. note::

   .. code-block:: 
    
      [Public Function] <Function_Name> ([Argument 1], [Argument 2],..) [As<Type>]

         <Function_Name> = <Function_Results>

      End Function

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: 

         [Public Function] R_Pile(Q_Base, Q_Shaft) As Single

            ' Expressing pile resistance, R_Pile as a function of 
            ' Base resistance, Q_Base
            ' Shaft resistance, Q_Shaft
            
            R_Pile = Q_Base + Q_Shaft
         
         End Function

*************
3. Decisions
*************
3.1 Conditional Statements
===========================
You can introduce nested 'if' statements as below to improve readibility of code [[#Ifs]_]: 

.. note::

   .. code-block:: 
    
      If <Condition 1> Then

         [Statement 1]

      ElseIf <Condition 2> Then

         [Statement 2]

      Else 

         [Statement 3]
      
      End If

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

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

Automate your code with 'For...Next' statements. [[#Fors]_]

.. note::

   .. code-block:: 
    
      For counter = start To end [Step step]
      
      [Statement 1]

      [Exit for]

      [Statement 2]

      Next [counter]

.. dropdown:: Click Me for an Example!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down     

   .. hint::

      .. code-block:: 

         'Setting up 100 repetitions with step count of 1
         For Piling_Log = 1 To 100 Step 1                    
         
         ' Adding 1 to Pile_Number
         Pile_Number = Pile_Number + 1                      

         ' Displaying the total number of piles
         MsgBox "Total Number of Piles is" & Pile_Number    

         Next Piling_Log

******************
4. Debugging Tips
******************
.. tip::

   Introduce **VBA breakpoints** to pause the execution of code

      Code execution by VBA stops at the designated breakpoints.
      
      Therefore, you can examine your code if there is any obvious error such as syntactic mistakes.

.. important::

   You can evaluate your function in the **VBA Intermediate Window**

      VBA Intermediate Window allows you to preview and evaluate outputs generated from user-defined functions.

      Previewing outputs allows you to debug before introducing functions into spreadsheets.
      
.. caution::

   Avoid preventable bug such as **overflow** during variable declaration.
      
   Overflow occurs when the variables that are explicitly declared have greater value than that can be stored by the data type.

      .. code-block:: 

         Dim <Variable_Name> as Integer

         <Variable_Name> = 50,000

         >>> "Overflow"

         ' Since the value of <Variable_Name> is greater than 32,767 
         ' which is the maximum value that the Integer data type can hold, "overflow" occurs.
         
         ' This error is preventable by assigning the <Variable_Name> to Long data type,
         ' as Long data type has a range of 2,147,483,647 
         ' that it can store (which is greater than 50,000).

         Dim <Variable_Name> as Long



**************
5. References
**************
.. [#Input] 

`Microsoft Data Type Summary <https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/data-type-summary>`_ 

.. [#Ifs]

`Microsoft Using If...Then...Else Statements <https://docs.microsoft.com/en-us/office/vba/language/concepts/getting-started/using-ifthenelse-statements>`_

.. [#Fors]

`Microsoft For...Next Statement <https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/fornext-statement>`_