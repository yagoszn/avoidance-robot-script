# obstacle-avoidance-robot-script
Winter '23/24 Obstacle Avoidance Robot python code. Uses several libraries to to program the Raspberry Pi.
By Yoseph Tamene and Diego Sanchez

Abstract
The aim of our project is to implement a robot on DC-motor-powered wheels that can detect
obstacles in front of it and avoid them using an ultrasonic sensor. We want the robot to constantly
display information on its current state of movement, distance from the obstacle in front of it,
and the direction it is going using an OLED display and a visual LED signal.
The outcome of our project was an OLED that generally worked well in avoiding obstacles and
displaying information about its movement, but lacked some accuracy due to the position of the
ultrasonic sensor we used as a measuring device of distance.

Project Description
Our obstacle avoidance uses one Raspberry Pi and breadboard to implement the functionality of an
obstacle avoidance robot using a single HC-SR04 finder, an OLED display, an RGB-compatible
common cathode LED, and DC motors powered by an external battery. At the robot’s core, we
have programmed it to keep moving forward and to stop, then move backwards left or right
(depending on a count) when an obstacle is detected. In addition, we have provided visual
components on both an OLED display and an LED to provide further information for the user.

Project Objectives
Goals:
1.   Implement a method of movement via DC motors
2.   Calculate when the robot should turn using an ultrasonic sensor (Decided on 20cm before the robot stops moving forward)
3.   Implement an RGBLED component that provides a visual of the current state of movement of the robot
4.   Implement an OLED module to the rear of the robot to display a constant message detailing state of movement, direction,
     and the distance to the obstacle in front of the robot.
5.   Implement all necessary components and provide a program that can guide the robot to safely move in another direction when it detects an obstacle. This keeps the robot from completely stopping once an obstacle is met.
