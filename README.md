# Wave-Sensor-Using-the-Raspberry-Pi
 a wave sensor is in internet of things device that use the raspberry 3+ connected to a light dependent resistor via MCP300, the MCP300 is an analog digital converter chip that use serial peripheral interface to communicate with the raspberry pi3+. The wave sensor uses the LDR to sense changes in light caused by a waving hand that frequently blocks the light when a person waves his/her hand, it then stores the data about changes in light caused by the waving. Data captured is send to a central sever via Transmission Control Protocol/Internet Protocol python sockets. the data sent to the server via internet contains information about how fast the hand is waving, the number of times the hand waves, the speed at which the hand is waving and the value of luminosity of the light.
 
 Requirements
 ---
 
The the MCP300 intergreated circuit

Raspberrypi 3+

Python version 3

RPI.GPIO library

How tow run
---
1. Initialize ther server first by running "server.py"
2. then run wave "sensor.py"
