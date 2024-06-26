from ubicoders_vrobots import System, GeneralRobot
import numpy as np
from vr_realtimeplot import RealtimePlot

# Create a multirotor object that contains states (euler angles, angular velocities, sensors, actuators, etc.)
halfdrone = GeneralRobot()
plotter = RealtimePlot(ylabels="Angle (degrees)", title="Angle vs Time")

class UbicodersMain:
    def __init__(self) -> None:
        # Define the variables here!
        pass
    
    def setup(self):
        # This API will be released soon!
        pass

    def loop(self):
        # State Observer
        states = halfdrone.states        
        ts = states.timestamp
        theta = states.euler.x # the angle of the half drone
        theta_dot = -states.ang_vel.x # the angular velocity of the half drone
        throttle = states.pwm[0] # the current throttle of the half drone

        plotter.update(ts, theta)
        print(f"timestamp: {ts}, theta: {theta}, theta_dot: {theta_dot}, throttle: {throttle}")

        # Set the PWM values to the motors! between 1100 to 2000
        halfdrone.set_pwm(m0=1234, m1=1234, m2=0, m3=0)

if __name__ == "__main__":
    sys = System(halfdrone, UbicodersMain())
    sys.start()
