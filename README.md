# fit-GPS-repair
<b>Preposition:</b>
- You have a bike computer (wow!) 
- You have a speed sensor
- Installed Python 3
  
<b>Main idea of code:</b>
<br>During the period of GPS issues, the sports device log jumps to the other side of our planet. 
Splitting these fragments and deleting damaged sections is a good idea, but it doesn't save any other data, such as pulse, cadence, power, and distance.
So, use smart delete - any GPS data with a negative value must be excluded, and save other data at the same time.

<b>Steps:</b>
1. Go to https://developer.garmin.com/fit/download/
2. Download FitSDKRelease.zip and unzip it
3. Go to /java directory and copy your .fit file
4. Rename it to <code>input.fit</code>
5. Convert from .fit to .csv 
<br><code>java -jar FitCSVTool.jar -b input.fit output.csv</code>
6. Run Python script
<br>Move clean.py in the /java folder and run it
- Linux:<br><code>python3 clean.py</code>
- Windows:<br><code>py clean.py</code>
7. After the Python script fixes the data, convert to .fit
<br><code>java -jar FitCSVTool.jar -c cleaned.csv ready.fit</code>

<b>Troubleshooting:</b>
When the speed sensor is available, the bike computer gives it priority over GPS speed data.
If the sensor doesn’t detect movement (e.g., when the rider stops), it temporarily shuts down.
At that point, the bike computer switches back to unstable GPS, which may result in incorrect speed readings.
<b>Solution:</b> During periods of GPS instability, always use the Pause button on your bike computer. This prevents false speed “noise” from being recorded in the log.

<b>Why we need FIT conversion</b>
FIT format saves speed data from the speed sensor in a separate field, but conversion to GPX by Strava is deleting this data.
