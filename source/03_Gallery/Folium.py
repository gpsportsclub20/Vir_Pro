import os
import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [5.216570, 100.435071]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 16)

m_tooltip_label = "Site Location: Warehouse of Jabil Circuit Sdn. Bhd."
m_tooltip = folium.Marker(Site_Coord, 
                          tooltip = m_tooltip_label).add_to(m_folium)

# Activating the 'folium.plugins' to include a minimap at the bottomright of the main map
m_minimap_Batu_Kawan = plugins.MiniMap(toggle_display = True, 
                                       width=200, 
                                       height=200, 
                                       zoom_level_fixed=None)

m_folium.add_child(m_minimap_Batu_Kawan)

# Importing the polyline coordinates for the site boundary from Geojason.io
local_CPath ="source/03_Gallery/"
overlay = os.path.join(local_CPath,'GeoJason.json')
folium.GeoJson(overlay, name='Site Boundary').add_to(m_folium)

# Outputting the 'm_folium' object on Jupyter Notebook
#m_folium

# Saving the 'Leaflet' map generated in html format
m_folium.save('Batu_Kawan.html')