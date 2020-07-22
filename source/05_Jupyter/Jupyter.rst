####################
Python Workbook
####################

****************
Python Terminal
****************

Online Python Interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Attempt on this workbook using the Python interpreter below:

.. raw:: html

    <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/repls/CostlyMiserlyAssembler?lite=true">
   
    </iframe>


**************************
Inputs and Data Types
**************************

Text Type
~~~~~~~~~

String <*str*>
^^^^^^^^^^^^^^

.. code:: ipython3

    # Declaring the pile type as <str>
    Pile_type = "API RC Pile"    

Numeric Types
~~~~~~~~~~~~~

Integer <*int*>
^^^^^^^^^^^^^^^

Assigning integer data type to Python variable

.. code:: ipython3

    # Declaring the exposed height of retaining wall as <int>
    H_exposed = 4

Floating points <*float*>
^^^^^^^^^^^^^^^^^^^^^^^^^

Assigning floating point number to Python variable

.. code:: ipython3

    # Declaring the pile length as <float>
    L_pile = 23.5


Sequence Type
~~~~~~~~~~~~~

List <*list*>
^^^^^^^^^^^^^

Compiling data into a Python list which is - ordered - changeable

.. code:: ipython3

    # Storing the diameter of piles as a <list>
    Dia_pile = [0.3,0.45,0.50,1.00]

Mapping Type
~~~~~~~~~~~~

Dictionary <*dict*>
^^^^^^^^^^^^^^^^^^^

Stores a set of key-value pairs which is - unordered - changeable -
indexed

In the following example for piling catalogue, the key-value pair is as
such - **key**: API RC 300 - **value**: 300mm

.. code:: ipython3

    # Storing the pile types and their corresponding diameter as a <dict>
    Pile_Catalogue = {"API RC300": "300mm",
                      "API RC450": "400mm",
                      "API RC450": "600mm"}
    

**************************
Process Design
**************************

User-Defined Function
~~~~~~~~~~~~~~~~~~~~~

The following example illustrates how Python functions can be formulated
to solve geotechnical engineering problems.

Rankine Theory of Lateral Earth Pressure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will try to write a simple Python expression to calculate the active
thrust on a retaining wall


.. math::
   
      K_{a} = \frac{1 - sin (\phi)} {1 + sin (\phi)}
      

where

:math:`c'` = 0

:math:`\phi'` = 37 :math:`^o`


.. dropdown:: Click Me for the Code Snippet!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python
        
        import math
        
        phi = 37
        theta_rad = phi/180*math.pi
        sin_phi = math.sin(theta_rad)
        
        K_active = (1-sin_phi)/ (1 + sin_phi)
        
   

Settlement of Rigid Piles - Randolph & Wroth Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you are familiar with the syntax of Python, more advanced formulation can be attempted.

Let's try to compute the settlement of rigid piles using the Randolph and Wroth method.

Soil Shaft Stiffness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. math::

    K_{si} = \frac{2\pi L_{si} \bar{G_{si}}}{ln \frac{2 r_m}{D_o}}


where,

:math:`K_{si}` = Soil shaft stiffness

:math:`L_{s}` = Effective length of under-reamed pile shaft

:math:`G_{si}` = Average shear modulus

:math:`r_{m}` = Radius of influence

:math:`D_{o}` = Pile shaft diameter

.. dropdown:: Click Me for the Code Snippet!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python
            
        import math 
        
        def K_shaft(L_si_eff, G_si_ave, r_m, D_0):
            
            K_si = (2*math.pi*L_si_eff*G_si_ave)/(math.log(2*r_m/D_0))
            
            return K_si
        
        k_shaft_Randolph = K_shaft(17,9.25,21.5,1.5)
        

Soil Base Stiffness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

    K_{bi} = 2 \frac{D_{o} G}{1 - \nu}

where,

:math:`K_{bi}` = Soil base stiffness

:math:`D_{o}` = Pile base diameter

:math:`G` = Soil shear modulus at the bottom of the under-reamed pile

:math:`\nu` = Poisson’s ratio of soil

.. dropdown:: Click Me for the Code Snippet!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python
            
        def K_base(D_base, G_base, v_nu):
            
            K_base = 2*(D_base*G_base)/(1-v_nu)
            
            return K_base
        
        k_bi_Randolph = K_base(2.5, 15.75, 0.2)



Settlement of Rigid Piles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::
    
    s_{r} = \frac{Q}{K_{bi} + K_{si}}

where,

:math:`s_{r}` = settlement of rigid pile

:math:`K_{si}` = Soil shaft stiffness

:math:`K_{bi}` = Soil base stiffness


.. dropdown:: Click Me for the Code Snippet!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python

        def s_rigid(Q_pile, K_si_input, K_bi_input):
            
            s_rigid = (Q_pile*1e3)/(K_si_input + K_bi_input)
            
            return s_rigid
        
        s_rigid_Randolph = s_rigid(5,k_bi_Randolph,k_shaft_Randolph)

    
**************************
Decision Controls
**************************

The following section demonstrates the usage of ‘for’ loops to automate
iterative calculations. 

Fibonacci Sequence
~~~~~~~~~~~~~~~~~~

.. math::

    F_{n} = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144


User-defined functions for Fibonacci Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. math::

    F_{n} = F_{n-2} + F_{n-1}


.. code:: ipython3

    def fib_N_function(f_N_2, f_N_1):
        
        fib_N_function = f_N_2 + f_N_1
        
        return fib_N_function
    
    fib_N_function_term = fib_N_function(233,377)

We will try to use a 'for' loop to automate the calculation of the recursive Fibonacci sequence.

.. dropdown:: Click Me for the Code Snippet!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python
  
        def fib_N(n_fib):
            
            'Defining the first 2 terms in the Fibonacci sequence
            fib_N_2 = 0
            fib_N_1 = 1
            
            'Formulating the Fibonacci numbers
            fib_N = fib_N_2 + fib_N_1
            
            for i in range(1,n_fib-1):
                
                # Formulating the Fibonacci numbers
                fib_N = fib_N_2 + fib_N_1
                
                # Updating the Fibonacci series
                fib_N_2 = fib_N_1
                fib_N_1 = fib_N     
                
            return fib_N


**************************
Tutorial
**************************

The tutorial involves using ‘for’ loop and ‘if’ statement to approximate the sine value of an angle using the MacLaurin series.

MacLaurin Sine Series Expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

    sin (x) = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k + 1)!} x^{2k+1}


.. math::

    sin (x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - ...


.. dropdown:: Click Me for the Solution!
   :title: bg-light text-center text-secondary
   :animate: fade-in-slide-down

   .. hint::

      .. code-block:: Python

        import math
    
        'Setting the number of interation to 10
        N_MacLaurin = 10

        'Initialising the first term of MacLaurin series to be zero
        sin_MacLaurin = 0

        'Assigning the coefficient pi
        pi = math.pi

        'Setting the angle of interest to be 60 degrees
        theta = 60

        'Calculating the radian of the angle of interest
        theta_rad = (theta/180)*pi
        
        'Initialising the <for> loop
        for k in range(0,N_MacLaurin):
            
            'Formulating the recursive equation of MacLaurin series
            sin_MacLaurin = sin_MacLaurin + (((-1))**k)/(math.factorial(2*k+1))*(theta_rad**(2*k+1)) 
