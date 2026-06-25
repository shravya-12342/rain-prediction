---
license: unknown
language:
- en
size_categories:
- 1K<n<10K
---
# Weather Dataset README

## Overview
This dataset contains weather data for Ankara, Turkey, from 2016-04-01 to 2022-04-01. The dataset is composed of weather-related measurements and information, such as temperature, precipitation, wind speed, and other relevant parameters.

## Dataset Description
Each row in the dataset represents a single day's weather data. The columns in the dataset are as follows:

- **name** (string): Name of the location (Ankara)
- **datetime** (string): Date in the format "YYYY-MM-DD"
- **tempmax** (float64): Maximum temperature in Celsius
- **tempmin** (float64): Minimum temperature in Celsius
- **temp** (float64): Average temperature in Celsius
- **feelslikemax** (float64): Maximum "feels like" temperature in Celsius
- **feelslikemin** (float64): Minimum "feels like" temperature in Celsius
- **feelslike** (float64): Average "feels like" temperature in Celsius
- **dew** (float64): Dew point temperature in Celsius
- **humidity** (float64): Humidity percentage
- **precip** (float64): Precipitation amount in millimeters
- **precipprob** (int64): Precipitation probability percentage
- **precipcover** (float64): Precipitation coverage percentage
- **preciptype** (null): Precipitation type (should be null in the dataset, otherwise an error)
- **snow** (float64): Snowfall amount in centimeters
- **snowdepth** (float64): Snow depth in centimeters
- **windgust** (float64): Maximum wind gust speed in kilometers per hour
- **windspeed** (float64): Average wind speed in kilometers per hour
- **winddir** (float64): Wind direction in degrees (0-360)
- **sealevelpressure** (float64): Sea-level pressure in millibars
- **cloudcover** (float64): Cloud coverage percentage
- **visibility** (float64): Visibility distance in kilometers
- **solarradiation** (float64): Solar radiation in Watts per square meter
- **solarenergy** (float64): Solar energy in kilojoules per square meter
- **uvindex** (int64): UV index value
- **severerisk** (float64): Severe weather risk percentage
- **sunrise** (string): Sunrise time in the format "YYYY-MM-DDTHH:mm:ss"
- **sunset** (string): Sunset time in the format "YYYY-MM-DDTHH:mm:ss"
- **moonphase** (float64): Moon phase value (0 to 1)
- **conditions** (string): General weather conditions
- **description** (string): Detailed weather description
- **icon** (string): Weather icon identifier
- **stations** (string): Comma-separated list of weather station IDs

## Notes
Please note that there are some errors in the dataset, such as non-null values in the "preciptype" column. Be sure to handle these cases appropriately when processing the data.