import folium
import geopandas as gpd

directory = '/Users/hwheelen/Dropbox/Mahrud/OpenPrecinctsProgress/'
prog_map = directory + 'Progress_11_15.shp'
df =  gpd.read_file(prog_map)
m = folium.Map(location=[48, -102], zoom_start=3, tiles='Mapbox bright')
print(df.columns.values)

m.choropleth(
    geo_data=df,
    columns=['COUNTYFP', 'progress'],
    threshold_scale=[0,1,2,3,4,5],
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Progress'
)


folium.LayerControl().add_to(m)

m.save(outfile=directory + 'map.html')
# If you look inside the map.html source code you will see that Folium has been able to generate HTML,
# Javascript and CSS and these three render the map on the browser.
# You can serve this HTML as a static file  in a basic webserver,
# but you can also go more advanced and create a Python application and have Folium dynamically
# generate such Leaflet maps on demand.
