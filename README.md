# fit-GPS-repair
# bash
1. Go to https://developer.garmin.com/fit/download/
2. Download FitSDKRelease.zip and unzip it
3. Go to /java directory and copy there your .fit file
4. Convert from .fit to .csv
java -jar FitCSVTool.jar -b input.fit output.csv
5. After fix data by python script, convert to .fit
java -jar FitCSVTool.jar -c cleaned.csv ready.fit
