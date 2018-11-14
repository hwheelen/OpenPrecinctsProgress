import folium
import geopandas as gpd

prog_map = './Progress_Map.shp'
df =  gpd.read_file(prog_map)
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')

df.columns.values


map.save(outfile='map.html')
# If you look inside the map.html source code you will see that Folium has been able to generate HTML,
# Javascript and CSS and these three render the map on the browser.
# You can serve this HTML as a static file  in a basic webserver,
# but you can also go more advanced and create a Python application and have Folium dynamically
# generate such Leaflet maps on demand.
