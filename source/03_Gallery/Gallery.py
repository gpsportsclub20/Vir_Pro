import os
import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

''' *************************************** Generating Folium Base Map **************************************'''

# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [5.216570, 100.435071]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 15)

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
                                          icon = folium.Icon(color='black',icon='info-sign'),
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
                                          icon = folium.Icon(color='orange',icon='info-sign'),
                                          popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group_2020)


''' *************************************** Activating LayerControl in Folium Base Map **************************************'''

folium.LayerControl().add_to(m_folium)


''' *************************************** Saving Folium Base Map as HTML **************************************'''

# Saving the 'Leaflet' map generated in html format
m_folium.save('Batu_Kawan.html')
