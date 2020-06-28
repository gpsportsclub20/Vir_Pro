import os
import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [40,0]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 2,
                      )

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group = folium.FeatureGroup("Coding Trailblazers")
# Collecting in Python tuples the coordinates of places with historical significance to the development of computer science
lat_CS = [51.997779, 28.606028, 60.185062, 29.433293]
long_CS = [-0.740697, -80.653095, 24.932134, 106.915184]
m_tooltip_label = ["Alan Turing: Bletchley Park, England", "Margaret H. Hamilton: Kennedy Space Centre, USA", "Linus Torvalds: Helsinki, Finland", "Xia Peisu: Chongqing, China"]


for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_CS, long_CS, m_tooltip_label):
    
    if lat_tooltip == lat_CS[0]:

        color_tooltip = 'darkblue'

        tooltip_Coord = [lat_tooltip, long_tooltip]
        feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                            icon = folium.Icon(color=color_tooltip,icon='user'),
                                            popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

    elif lat_tooltip == lat_CS[2]:

        color_tooltip = 'darkblue'

        tooltip_Coord = [lat_tooltip, long_tooltip]
        feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                            icon = folium.Icon(color=color_tooltip,icon='user'),
                                            popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

    else:

        color_tooltip = 'red'

        tooltip_Coord = [lat_tooltip, long_tooltip]
        feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                            icon = folium.Icon(color=color_tooltip,icon='user'),
                                            popup = folium.Popup(m_tooltip_label, max_width=200, min_width=200)))

m_folium.add_child(feature_group)

# Activating the 'folium.plugins' to include a minimap at the bottomright of the main map
m_minimap_CS = plugins.MiniMap(toggle_display = True, 
                                       width=100, 
                                       height=100, 
                                       zoom_level_fixed=None)

m_folium.add_child(m_minimap_CS)

folium.LayerControl().add_to(m_folium)

# Saving the 'Leaflet' map generated in html format
m_folium.save('CS.html')