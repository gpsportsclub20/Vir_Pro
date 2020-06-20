import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [5.216570, 100.435071]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 16)

m_tooltip_label = "Site Location"
m_tooltip = folium.Marker(Site_Coord, 
                          tooltip = m_tooltip_label).add_to(m_folium)

# Activating the 'folium.plugins' to include a minimap at the bottomright of the main map
m_minimap_Batu_Kawan = plugins.MiniMap(toggle_display = True, 
                                       zoom_level_offset = -1, 
                                       width=200, 
                                       height=200, 
                                       zoom_level_fixed=12,)
m_folium.add_child(m_minimap_Batu_Kawan)

# Outputting the 'm_folium' object on Jupyter Notebook
m_folium

# Saving the 'Leaflet' map generated in html format
m_folium.save('Batu_Kawan.html')