# obstacle-avoidance-robot-script
Winter '23/24 Obstacle Avoidance Robot python code. Uses several libraries to to program the Raspberry Pi.
By Yoseph Tamene and Diego Sanchez

## Abstract
The aim of our project is to implement a robot on DC-motor-powered wheels that can detect
obstacles in front of it and avoid them using an ultrasonic sensor. We want the robot to constantly
display information on its current state of movement, distance from the obstacle in front of it,
and the direction it is going using an OLED display and a visual LED signal.
The outcome of our project was an OLED that generally worked well in avoiding obstacles and
displaying information about its movement, but lacked some accuracy due to the position of the
ultrasonic sensor we used as a measuring device of distance.

## Project Description
Our obstacle avoidance uses one Raspberry Pi and breadboard to implement the functionality of an
obstacle avoidance robot using a single HC-SR04 finder, an OLED display, an RGB-compatible
common cathode LED, and DC motors powered by an external battery. At the robot’s core, we
have programmed it to keep moving forward and to stop, then move backwards left or right
(depending on a count) when an obstacle is detected. In addition, we have provided visual
components on both an OLED display and an LED to provide further information for the user.

## Project Objectives
### Goals:
1.   Implement a method of movement via DC motors
2.   Calculate when the robot should turn using an ultrasonic sensor (Decided on 20cm before the robot stops moving forward)
3.   Implement an RGBLED component that provides a visual of the current state of movement of the robot
4.   Implement an OLED module to the rear of the robot to display a constant message detailing state of movement, direction,
     and the distance to the obstacle in front of the robot.
5.   Implement all necessary components and provide a program that can guide the robot to safely move in another direction when it detects an obstacle. This keeps the robot from completely stopping once an obstacle is met.

## Project Approach
To physically implement the AROD robot’s required components into the Raspberry Pi device,
we followed the provided Obstacle Avoidance Robot guide. Most notably, in the guide, there
were details on how to implement the ability to power two DC motors at once natively through
the use of an H-Bridge IC chip (the specific IC chip being the L293D chip). We also followed the
recipe for the HC-SR04 Finder exactly how the guide did so, which left the HC-SR04 Finder to
detect the right-hand side of the car when moving. The associated recipes were Chapter 12.5:
Controlling the Direction of a DC Motor and Chapter 14.19: Measuring Distance Using
Ultrasound.

To implement the code and circuit we followed the following two methods, for the motors and
the ultrasonic sensor we followed the code and circuit diagram provided to us in the same
Obstacle Avoidance Robot guide. We used the Raspberry Pi recipes Chapter 15.4 and Chapter
11.1 for the OLED display and RGB LED respectively to figure out the necessary code and
circuit diagrams needed. One major thing we had to learn for the coding implementation is that
when moving backward right however the right wheel should move backward faster than the left
and vice versa for moving backward left. The speed of the wheel is determined by a number 0 to
1 which sets the PWM the closer to 1 the speed is set to the faster the motor/wheel will move.
Another thing we learned is that if you start a new line in your string via \n when displaying to
the OLED it will display a new line which was a really helpful discovery because we could not
figure out how to display more than 2 lines as the cookbook only shows how to display two
lines.

A challenge we faced when physically implementing the AROD robot’s required components
was figuring out how to provide a 5V output from the Raspberry Pi to all required
implementations, since the modules that needed them exceeded the physical pins of the device.
As a solution, we found a way to provide power using a single rail of the breadboard and
connecting all power to it.

We also faced a challenge in that some of the components we used were not working correctly,
which caused us to constantly reevaluate the code we wrote when it was a hardware issue. In
particular, the HC-SR04 finder was difficult to get working due to hardware issues and it
signaled to us that it may be the component that would give us the most trouble when meeting
our project goals. However, we got it to work after going through many HC-SR04 finders and
finding a suitable one.

All recipes used in the implementation of the AROD robot followed the project proposal we
submitted. We did not need to change them from our original idea.
We did not have to abandon certain features that we discussed in our project proposal.

## Conclusion
Overall, the project was a very interesting and enriching experience. While nothing is perfect, we
are overall satisfied with our version of the obstacle avoidance robot. To be able to implement a
more sophisticated project in a group environment a mere two months after starting from scratch
was a challenging, but fun feat. Overall, the class introduced us to new concepts in and outside
the scope of the Raspberry Pi and we hope to apply the universal concepts taught to us beyond
CSC 299.
