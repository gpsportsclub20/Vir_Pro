import os
import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

''' *************************************** Generating Folium Base Map **************************************'''

# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [4.145825, 108.3035]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 5)


''' *************************************** Adding Minimap onto Folium Base Map **************************************'''

# Activating the 'folium.plugins' to include a minimap at the bottomright of the main map
m_minimap_Batu_Kawan = plugins.MiniMap(toggle_display = True, 
                                       width=200, 
                                       height=200, 
                                       zoom_level_fixed=None,
                                       minimized=True)

m_folium.add_child(m_minimap_Batu_Kawan)

''' ***************************** Extracting G&P Geotechnics Project with Coordinates *******************************'''
import pyexcel as pyex
import numpy as np


DATA = pyex.get_book(file_name = '2020_Gallery.xlsx')


''' ******************************************** 2008  **************************************************************'''
# Data extraction for projects secured in year 2008
DATA_2008 = np.array(DATA.sheet_by_name('2008'))
lat_2008 = np.ndarray.tolist(DATA_2008[1:,1])
lgn_2008 = np.ndarray.tolist(DATA_2008[1:,0])
pgn_2008 = np.ndarray.tolist(DATA_2008[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2008 = folium.FeatureGroup("2008 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2008, lgn_2008, pgn_2008):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2008.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='black',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2008)





''' ******************************************** 2009  **************************************************************'''

# Data extraction for projects secured in year 2009
DATA_2009 = np.array(DATA.sheet_by_name('2009'))
lat_2009 = np.ndarray.tolist(DATA_2009[1:,1])
lgn_2009 = np.ndarray.tolist(DATA_2009[1:,0])
pgn_2009 = np.ndarray.tolist(DATA_2009[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2009 = folium.FeatureGroup("2009 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2009, lgn_2009, pgn_2009):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2009.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='black',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2009)

''' ******************************************** 2010  **************************************************************'''

# Data extraction for projects secured in year 2010
DATA_2010 = np.array(DATA.sheet_by_name('2010'))
lat_2010 = np.ndarray.tolist(DATA_2010[1:,1])
lgn_2010 = np.ndarray.tolist(DATA_2010[1:,0])
pgn_2010 = np.ndarray.tolist(DATA_2010[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2010 = folium.FeatureGroup("2010 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2010, lgn_2010, pgn_2010):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2010.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='black',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2010)

''' ******************************************** 2011  **************************************************************'''
# Data extraction for projects secured in year 2011
DATA_2011 = np.array(DATA.sheet_by_name('2011'))
lat_2011 = np.ndarray.tolist(DATA_2011[1:,1])
lgn_2011 = np.ndarray.tolist(DATA_2011[1:,0])
pgn_2011 = np.ndarray.tolist(DATA_2011[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2011 = folium.FeatureGroup("2011 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2011, lgn_2011, pgn_2011):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2011.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='orange',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2011)

''' ******************************************** 2012  **************************************************************'''
# Data extraction for projects secured in year 2012
DATA_2012 = np.array(DATA.sheet_by_name('2012'))
lat_2012 = np.ndarray.tolist(DATA_2012[1:,1])
lgn_2012 = np.ndarray.tolist(DATA_2012[1:,0])
pgn_2012 = np.ndarray.tolist(DATA_2012[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2012 = folium.FeatureGroup("2012 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2012, lgn_2012, pgn_2012):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2012.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='orange',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2012)

''' ******************************************** 2013  **************************************************************'''
# Data extraction for projects secured in year 2013
DATA_2013 = np.array(DATA.sheet_by_name('2013'))
lat_2013 = np.ndarray.tolist(DATA_2013[1:,1])
lgn_2013 = np.ndarray.tolist(DATA_2013[1:,0])
pgn_2013 = np.ndarray.tolist(DATA_2013[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2013 = folium.FeatureGroup("2013 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2013, lgn_2013, pgn_2013):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2013.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='orange',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2013)

''' ******************************************** 2014  **************************************************************'''
# Data extraction for projects secured in year 2014
DATA_2014 = np.array(DATA.sheet_by_name('2014'))
lat_2014 = np.ndarray.tolist(DATA_2014[1:,1])
lgn_2014 = np.ndarray.tolist(DATA_2014[1:,0])
pgn_2014 = np.ndarray.tolist(DATA_2014[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2014 = folium.FeatureGroup("2014 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2014, lgn_2014, pgn_2014):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2014.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='orange',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2014)

''' ******************************************** 2015  **************************************************************'''
# Data extraction for projects secured in year 2015
DATA_2015 = np.array(DATA.sheet_by_name('2015'))
lat_2015 = np.ndarray.tolist(DATA_2015[1:,1])
lgn_2015 = np.ndarray.tolist(DATA_2015[1:,0])
pgn_2015 = np.ndarray.tolist(DATA_2015[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2015 = folium.FeatureGroup("2015 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2015, lgn_2015, pgn_2015):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2015.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='orange',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2015)


''' ******************************************** 2016  **************************************************************'''

# Data extraction for projects secured in year 2016
DATA_2016 = np.array(DATA.sheet_by_name('2016'))
lat_2016 = np.ndarray.tolist(DATA_2016[1:,1])
lgn_2016 = np.ndarray.tolist(DATA_2016[1:,0])
pgn_2016 = np.ndarray.tolist(DATA_2016[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2016 = folium.FeatureGroup("2016 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2016, lgn_2016, pgn_2016):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2016.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='red',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2016)



''' ******************************************** 2017  **************************************************************'''
# Data extraction for projects secured in year 2017
DATA_2017 = np.array(DATA.sheet_by_name('2017'))
lat_2017 = np.ndarray.tolist(DATA_2017[1:,1])
lgn_2017 = np.ndarray.tolist(DATA_2017[1:,0])
pgn_2017 = np.ndarray.tolist(DATA_2017[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2017 = folium.FeatureGroup("2017 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2017, lgn_2017, pgn_2017):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2017.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='red',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2017)


''' ******************************************** 2018  **************************************************************'''
# Data extraction for projects secured in year 2018
DATA_2018 = np.array(DATA.sheet_by_name('2018'))
lat_2018 = np.ndarray.tolist(DATA_2018[1:,1])
lgn_2018 = np.ndarray.tolist(DATA_2018[1:,0])
pgn_2018 = np.ndarray.tolist(DATA_2018[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2018 = folium.FeatureGroup("2018 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2018, lgn_2018, pgn_2018):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2018.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='red',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2018)

''' ******************************************** 2019  **************************************************************'''

# Data extraction for projects secured in year 2019
DATA_2019 = np.array(DATA.sheet_by_name('2019'))
lat_2019 = np.ndarray.tolist(DATA_2019[1:,1])
lgn_2019 = np.ndarray.tolist(DATA_2019[1:,0])
pgn_2019 = np.ndarray.tolist(DATA_2019[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2019 = folium.FeatureGroup("2019 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2019, lgn_2019, pgn_2019):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2019.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='red',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2019)

''' ******************************************** 2020  **************************************************************'''
# Data extraction for projects secured in year 2020
DATA_2020 = np.array(DATA.sheet_by_name('2020'))
lat_2020 = np.ndarray.tolist(DATA_2020[1:,1])
lgn_2020 = np.ndarray.tolist(DATA_2020[1:,0])
pgn_2020 = np.ndarray.tolist(DATA_2020[1:,3])

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group_2020 = folium.FeatureGroup("2020 Projects")

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_2020, lgn_2020, pgn_2020):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group_2020.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='red',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2020)


''' *************************************** Activating LayerControl in Folium Base Map **************************************'''

folium.LayerControl().add_to(m_folium)


''' *************************************** Saving Folium Base Map as HTML **************************************'''

# Saving the 'Leaflet' map generated in html format
m_folium.save('20200627_G&P_ALL.html')
