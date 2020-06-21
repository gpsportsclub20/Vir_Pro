import os
# Importing the Earth Engine API to include Google custom basemaps into folium
# import ee
# Importing folium
import folium
# Importing explicitly the module from 'folium' - 'folium.plugins'
import folium.plugins as plugins

'''
# Authenticating and initialising access to the Earth Engine server
ee.Authenticate()

# Initialising the library.
ee.Initialize()

# Add custom basemaps to folium
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = True,
        control = True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}

'''
# Generating a 'Leaflet' map for the location in interest by passing through the coordinates 
# Calling the 'folium.folium.Map' object
Site_Coord = [0,0]
m_folium = folium.Map(location = Site_Coord,
                      zoom_start = 2,
                      )

# Calling the class folium.map.FeatureGroup to group the places of interest in the LayerControl panel
feature_group = folium.FeatureGroup("Coding Trailblazers")
# Collecting in Python tuples the coordinates of places with historical significance to the development of computer science
# Blethchley Park (51.997779, -0.740697)

lat_CS = [51.997779]
long_CS = [-0.740697]
m_tooltip_label = ["Alan Turing"]

'''
for lat_tooltip, long_tooltip, name_tooltip in zip(lat_CS, long_CS, m_tooltip_label):

    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group.add_child(folium.Marker(location = tooltip_Coord, 
                            popup = name_tooltip))

m_folium.add_child(feature_group)

'''
'''
for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_CS, long_CS, m_tooltip_label):

    tooltip_Coord = [lat_tooltip, long_tooltip]
    m_tooltip = folium.Marker(tooltip_Coord, 
                            tooltip = m_tooltip_label).add_to(m_folium)
'''

for (lat_tooltip, long_tooltip, m_tooltip_label) in zip(lat_CS, long_CS, m_tooltip_label):
    
    tooltip_Coord = [lat_tooltip, long_tooltip]
    feature_group.add_child(folium.Marker(location = tooltip_Coord,
                                          popup = m_tooltip_label))

m_folium.add_child(feature_group)

# Activating the 'folium.plugins' to include a minimap at the bottomright of the main map
m_minimap = plugins.MiniMap(toggle_display = True, 
                                       width=200, 
                                       height=200, 
                                       zoom_level_fixed=None)

m_folium.add_child(m_minimap)

# Activating the control panel for map layers 
folium.LayerControl().add_to(m_folium)

# Saving the 'Leaflet' map generated in html format
m_folium.save('CS.html')