# fit-GPS-repair
Prepositon:
- you have bike computer (wow!) 
- you have speed sensor (bluetooth or wired)
- DISABLE auto-pause at your device

Steps:
1. Go to https://developer.garmin.com/fit/download/
2. Download FitSDKRelease.zip and unzip it
3. Go to /java directory and copy there your .fit file
4. Rename it to <code>input.fit</code>
5. Convert from .fit to .csv
<br><code>java -jar FitCSVTool.jar -b input.fit output.csv</code>
6. After fix data by python script, convert to .fit
<br><code>java -jar FitCSVTool.jar -c cleaned.csv ready.fit</code>

Troubleshooting:
When the speed sensor is available, the bike computer gives it priority over GPS speed data.
However, when the sensor doesn't detect movement (e.g. the rider is stopped), it temporarily shuts down.
But the GPS signal is chaotic at that moment, and the bike computer switches back to GPS and show incorrect speed data.

Solution: Disable the auto-start function
