import os
import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

''' *************************************** Generating Folium Base Map **************************************'''

# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [5.216570, 100.435071]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 16)

m_tooltip_label = "Site Location: Warehouse of Jabil Circuit Sdn. Bhd."
m_tooltip = folium.Marker(Site_Coord, 
                          tooltip = m_tooltip_label).add_to(m_folium)

''' *************************************** Adding FeatureGroup onto Folium Base Map **************************************'''

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group = folium.FeatureGroup("Trailblazers")
# Collecting in Python tuples the coordinates of places with historical significance to the development of computer science
# Blethchley Park (51.997779, -0.740697)

lat_CS = [51.997779, 28.606028, 60.185062, 33.321936, 32.064053,29.433293, 59.857012]
long_CS = [-0.740697, -80.653095, 24.932134, 44.347653, 118.792634,  106.915184, 30.254356]
m_tooltip_label = ["Alan Turing: Bletchley Park, England", "Margaret H. Hamilton: Kennedy Space Centre, USA", "Linus Torvalds: Helsinki, Finland", "Muhammad ibn Musa al-Khwarizmi: Baghdad, Iraq", "Zu Chongzhi: Nanjing, China","Xia Peisu: Chongqing, China", "Grigori Perelman: Leningrad, Russia"]


for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_CS, long_CS, m_tooltip_label):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                          icon = folium.Icon(color='red',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group)

''' *************************************** Adding Minimap onto Folium Base Map **************************************'''

# Activating the 'folium.plugins' to include a minimap at the bottomright of the main map
m_minimap_Batu_Kawan = plugins.MiniMap(toggle_display = True, 
                                       width=200, 
                                       height=200, 
                                       zoom_level_fixed=None)

m_folium.add_child(m_minimap_Batu_Kawan)

''' *************************************** Adding Polygon Overlay onto Folium Base Map **************************************'''

# Importing the polyline coordinates for the site boundary from Geojason.io
local_CPath ="source/03_Gallery/"
overlay = os.path.join(local_CPath,'GeoJason.json')

# Defining a function to style the 'GeoJson' overlay for site boundary
def style_function_GeoJson(feature):
    
    return { 'fillColor': '#black'
    }

folium.GeoJson(
    overlay, 
    name='Site Boundary',
    style_function = style_function_GeoJson
).add_to(m_folium)



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
                                          icon = folium.Icon(color='green',icon='info-sign'),
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
                                          icon = folium.Icon(color='green',icon='info-sign'),
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
                                          icon = folium.Icon(color='purple',icon='info-sign'),
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
                                          icon = folium.Icon(color='beige',icon='info-sign'),
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
                                          icon = folium.Icon(color='pink',icon='info-sign'),
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
                                          icon = folium.Icon(color='black',icon='info-sign'),
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
                                          icon = folium.Icon(color='white',icon='info-sign'),
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
                                          icon = folium.Icon(color='lightblue',icon='info-sign'),
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
                                          icon = folium.Icon(color='lightgreen',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2017)


''' ******************************************** 2018  **************************************************************'''


# Data extraction for projects secured in year 2018
DATA_2018 = np.array(DATA.sheet_by_name('2018'))
lat_2018 = np.ndarray.tolist(DATA_2018[1:,1])
lgn_2018 = np.ndarray.tolist(DATA_2018[1:,0])
pgn_2018 = np.ndarray.tolist(DATA_2018[1:,3])


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
                                          icon = folium.Icon(color='lightred',icon='info-sign'),
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
                                          icon = folium.Icon(color='lightgray',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2020)


''' *************************************** Activating LayerControl in Folium Base Map **************************************'''

folium.LayerControl().add_to(m_folium)


''' *************************************** Saving Folium Base Map as HTML **************************************'''

# Saving the 'Leaflet' map generated in html format
m_folium.save('Batu_Kawan.html')