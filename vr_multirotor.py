from ubicoders_vrobots import System, Multirotor
import numpy as np

# Create a multirotor object that contains states (euler angles, angular velocities, sensors, actuators, etc.)
mr = Multirotor()

class UbicodersMain:
    def __init__(self) -> None:
        # Define the variables here!
        pass
    
    def setup(self):
        # This API will be released soon!
        # mr.mass = 2 #kg
        pass

    def loop(self):
        # Print the multirotor states from the simulator!
        states = mr.states
        print("States: ", states)

        # Set the PWM values to the motors! between 1100 to 2000
        mr.set_pwm(m0=1250, m1=1250, m2=1250, m3=1250)

if __name__ == "__main__":
    sys = System(mr, UbicodersMain())
    sys.start()
