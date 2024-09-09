import folium

# Create a map centered on South Africa
south_africa_map = folium.Map(location=[-30.5595, 22.9375], zoom_start=5)

# Save the map as an HTML file
south_africa_map.save('map.html')
