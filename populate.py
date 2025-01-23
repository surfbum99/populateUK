import pandas as pd
import geopandas as gpd
import folium

# Path to your GeoJSON file
geojson_path = "uk_regions.geojson"

# Load the GeoJSON file into a GeoDataFrame
regions = gpd.read_file(geojson_path)

# Check the columns in the GeoDataFrame
print("Regions GeoDataFrame columns:", regions.columns)

# Load population data
population_data = pd.read_csv("population.csv")
print("Population DataFrame columns:", population_data.columns)

# Standardize column names for merging
regions['rgn19nm'] = regions['rgn19nm'].str.strip().str.lower()
population_data['Region Name'] = population_data['Region Name'].str.strip().str.lower()

# Merge population data with GeoJSON
merged = regions.merge(population_data, left_on="rgn19nm", right_on="Region Name")
print("Merged DataFrame columns:", merged.columns)

# Initialize Folium Map
uk_map = folium.Map(location=[55.3781, -3.4360], zoom_start=6)

# Add choropleth layer
folium.Choropleth(
    geo_data=merged,
    data=merged,
    columns=["rgn19nm", "2021 people per sq. km"],  # Corrected column name
    key_on="feature.properties.rgn19nm",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population Density (people per km²)"
).add_to(uk_map)

# Save map as HTML
uk_map.save("uk_population_map.html")
print("Map saved as uk_population_map.html")
