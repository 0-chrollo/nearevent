import folium
from folium import Map, CircleMarker
from folium.map import LayerControl

# Create a map centered on South Africa
south_africa_map = folium.Map(
    location=[-30.5595, 22.9375],
    zoom_start=5,
    control_scale=True,  # Add scale control to the map
    zoom_control=False  # Disable the default zoom control
)

# Add custom zoom control at the bottom left using JavaScript
south_africa_map.get_root().html.add_child(folium.Element("""
    <script>
    var map = L.map('map').setView([-30.5595, 22.9375], 5);
    L.control.zoom({
        position: 'bottomleft'
    }).addTo(map);
    </script>
"""))

# List of South African provinces with coordinates
provinces = {
    "Eastern Cape": [-32.2968, 26.4194],
    "Free State": [-28.4541, 26.7968],
    "Gauteng": [-26.2708, 28.1123],
    "KwaZulu-Natal": [-29.0000, 31.0000],
    "Limpopo": [-23.4013, 29.4179],
    "Mpumalanga": [-25.5653, 30.5273],
    "Northern Cape": [-29.0467, 21.8569],
    "North West": [-27.1254, 25.7551],
    "Western Cape": [-33.2278, 21.8569]
}

# Add circle markers for each province with a popup
for province, coordinates in provinces.items():
    folium.CircleMarker(
        location=coordinates,
        radius=10,
        color='blue',
        fill=True,
        fill_color='green',
        fill_opacity=0.6,
        popup=province
    ).add_to(south_africa_map)

# Add layer control (optional)
folium.LayerControl().add_to(south_africa_map)

# Save the map as an HTML file
south_africa_map.save('map.html')
