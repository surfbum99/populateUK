# populateUK

The `populateUK` project visualises the population density of UK regions using a choropleth map. The project combines geographical data of UK regions (kaggle UK dataset) with population data to create an interactive map that displays population density variations across the country.

Kaggle:

https://www.kaggle.com/datasets/dorianlazar/uk-regions-geojson

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Output](#output)
- [License](#license)

## Overview

This project generates an interactive map that uses Folium to visualize population density across different regions of the UK. The population data is merged with geographical data to show how population density varies by region. The map is saved as an HTML file that can be opened in any web browser.

## Requirements

You need Python version 3.x and the following libraries installed:

- `pandas` for data manipulation
- `geopandas` for working with geographical data (GeoJSON)
- `folium` for generating the choropleth map

## Installation

Follow these steps to set up and run the project on your local machine.

1. Clone the repository:
    ```bash
    git clone https://github.com/surfbum99/populateUK.git
    cd populateUK
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv populateUK
    ```

3. Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source populateUK/bin/activate
      ```
    - On Windows:
      ```bash
      populateUK\Scripts\activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary data files in the project directory:
    - `uk_regions.geojson`: The GeoJSON file containing the UK region boundaries.
    - `population.csv`: The CSV file containing population data for each region.

2. Run the Python script:
    ```bash
    python populate.py
    ```

    This will generate a choropleth map and save it as `uk_population_map.html` in your project directory.

## Dependencies

This project requires the following Python packages:

- `pandas` - A powerful library for data manipulation.
- `geopandas` - An extension of pandas for working with geographical data.
- `folium` - A library to generate interactive maps using Leaflet.js.

Install the required dependencies by running:
```bash
pip install pandas geopandas folium
