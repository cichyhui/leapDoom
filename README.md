![leapdoom](https://user-images.githubusercontent.com/84254704/198024572-8b087ea8-11bd-42c0-b11a-f5bf862fd2f2.png)


------

**LeapDoom** is a simple Python script that interprets Leap Motion hand data into keyboard presses that allow you to play Doom (*or other games*)

------
## Controls
	* Left hand
		* movement - WASD
		* grab - use Space
	* Right hand
		* left and right aiming - J and L
		* grab - fire I

## Running
**Prerequisites**:
* Python
* Leap Motion Orion Drivers (v4)


**Running the script:**

* Install python (3.11.0) from

  https://www.python.org/downloads/
* Leap Motion Orion Drivers from:

  https://developer.leapmotion.com/releases/leap-motion-orion-400

> **Note:** Make sure that **Allow Web Apps** is ticked on in the Leap Motion Control Panel

* Install dependencies, by running the following in a command prompt:
```
pip install -r requirements.txt
```

* Start LeapDoom
```
python main.py
```


## Additional configuration
Here are some additional options in the script


* **Sensitivity** (changes the threshold to activate)
 ```
sensitivity = 50
```

* PunchOut Mode (changes the fire condition to "*grab and throw a punch with the right hand*")
```
punchout = False
```


-----
indeed a very "*handy*" script
