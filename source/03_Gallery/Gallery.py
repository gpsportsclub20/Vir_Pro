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
feature_group = folium.FeatureGroup("Easter Eggs")
# Collecting in Python tuples the coordinates of places with historical significance to the development of computer science
# Blethchley Park (51.997779, -0.740697)

lat_CS = [51.997779, 28.606028, 60.185062, 33.321936, 32.064053,29.433293, 59.857012,51.502738]
long_CS = [-0.740697, -80.653095, 24.932134, 44.347653, 118.792634,  106.915184, 30.254356,-0.177698]
m_tooltip_label = ["Alan Turing: Bletchley Park, England", "Margaret H. Hamilton: Kennedy Space Centre, USA", "Linus Torvalds: Helsinki, Finland", "Muhammad ibn Musa al-Khwarizmi: Baghdad, Iraq", "Zu Chongzhi: Nanjing, China","Xia Peisu: Chongqing, China", "Grigori Perelman: Leningrad, Russia", "Hyde Park, London, England"]


for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_CS, long_CS, m_tooltip_label):

    if lat_tooltip == 51.502738:
            tooltip_Coord = [lat_tooltip, long_tooltip]
            feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                                icon = folium.Icon(color='green',icon='ok'),
                                                popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))
    
    else:
            tooltip_Coord = [lat_tooltip, long_tooltip]
            feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                                icon = folium.Icon(color='red',icon='user'),
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


''' *************************************** Activating LayerControl in Folium Base Map **************************************'''

folium.LayerControl().add_to(m_folium)


''' *************************************** Saving Folium Base Map as HTML **************************************'''

# Saving the 'Leaflet' map generated in html format
m_folium.save('Batu_Kawan.html')
