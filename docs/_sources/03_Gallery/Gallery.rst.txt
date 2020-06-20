################
Project Gallery
################

********************************************************************************
Investigative Project at Batu Kawan, Pulau Pinang, Malaysia
********************************************************************************


.. raw:: html

    <iframe frameborder="0" width="100%" height="600px" src="Batu_Kawan.html">
   
    </iframe>

*****************
Project Summary
*****************

.. list-table::  
   :widths: 6 15
   :header-rows: 0

   * - **Client**
     - Chuan Un Chye (M) Sdn. Bhd. (*hereafter referred to as CUC*)

   * - **Role of G&P Geotechnics**
     - Geotechnical Consultant for 
            * Independent Investigation
            * Expert Opinions
        
   * - **Scope of Investigation**
     - On the probable causes of pile deviations observed from jack-in RC square piles
            * | Installed for the warehouse of Jabil Circuit Sdn. Bhd. 
              | (as depicted in the Map)

   * - **Problem Statement**
     - Discrepency in pile deviations (up to 300 mm and more) were identified between:
            * First as-built survey by CUC 
                  * Taken from Jan 2019 to March 2019
                  * Simultaneously conducted with ongoing piling and earthworks on-site 
            * Second joint survey by CUC and Building Main Contractor 
                  * Taken in June 2019 
                  * Conducted after the end of piling and earthworks

   * - **General Site Geology** [[#GMPP]_]
     - The site is underlain by alluvium of Quaternary age which consists of
            * Inter-layered sands, silts and clays
            * From the fluviatile deposits in the main river valleys

   * - **Project Challenges**
     - Massive data analysis and intepretation
            * Pilelogs from 6,248 jack-in RC pilepoints
            * Pile Test Reports for more than 300 pilepoints (PIT, HSDPLT, MLT)

   * - **Programming Tools Used**
     - Python was predominantly used in
            * Pile deviation data visualisation 
            * | Analysis on theoretical radial soil displacement from pile driving
              | (Sagaseta & Whittle, 2001) [[#SSPM]_]
   
   * - **Project Team Members**
     - Team Structure 
            * Ir. Liew Shaw Shong (Project Director)
            * Chee Fong Wah (Project Engineer)
            * Teo Yow Yang (Engineer)
            * Ch'ng Wei En (Engineer)
            * Neoh Xiao Binn (Engineer)

**********************************
Data Visualisation with Python
**********************************
As-built Pile Deviation Data
==============================
Leveraging on Python's exceptional data processing and visualisation capabilities, the as-built pile deviations were    
      * visualised in a spatial manner to assist the project team in
      * understanding the mechanisms that contributed to excessive pile movements.

First As-built Pile Survey by CUC (Taken from Jan to March 2019)
==========================================================================================

.. figure:: CUC.png
      :align: center 
      :width: 1000 px
      :height: 500 px
      :class: no-scaled-link

Second Joint As-built Pile Survey (Taken in June 2019)
==========================================================================================

.. figure:: Joint.png
      :align: center 
      :width: 1000 px
      :height: 500 px
      :class: no-scaled-link

Inferences
==========================================================================================
From the figures above, the following observations can be summarised as below:

      * Significant outward pile deviation for large clusters of column group piles relative to smaller clusters of column group piles.
      * Internal column group piles were observed to have less deviation in Joint Survey.
      * External clusters of column group piles tend to have more outwards pile movements.

These observations were crucial to illustrate that the discrepancies in as-built pile deviation surveys were influenced by:
      
      **Spatial Factor**
            * Radial soil displacement from pile driving
      **Temporal Factor**
            * Timing of as-built pile deviation survey taken (at least 3 months apart)

***************************************
Theoretical Analysis with Python
***************************************

Radial Soil Displacement from Pile Driving
============================================================
The phenomenon of radial soil displacement was further studied using Python with reference to
      * Sagaseta & Whittle (2001) [[#SSPM]_].

This theoretical study provided the project team insights into 
      * the expected soil displacement due to the pile driving process for circular piles.

The radial soil displacement of a 350mm circular pile that is driven 30m into ground can be determined from the 
      * Small Strain Path Method 
      * Pioneered by the authors cited.

.. figure:: Radial.png
      :align: center 
      :width: 700 px
      :height: 700 px
      :class: no-scaled-link

****************
Recommendations
****************
Facing an avalanche of piling data from over 6,000 piles, the use of Python assisted the project team greatly in 
      * accelerating engineering analysis
      * automating data visualisation.

However, it is should be stressed that Python and any programming languages should only be used as a 
      * **complementary tool** to automate repetive work flows.

Manual review of automated coding results **must be carried out** to ensure 
      * sound and sensible engineering outputs.


**************
References
**************
.. [#GMPP]

| Geological Map of Pulau Pinang and Butterworth Area, New Series L7010 Sheet 28, Pulau Pinang (2014)
| Director General, Minerals and Geoscience Department of Malaysia

.. [#SSPM]

| Sagaseta, C. & Whittle, A. J. (2001), Prediction of Ground Movement due to Pile Driving in Clay,
| J. Geotech. Geoenviron. Eng., 127 (1), pp 55-66.