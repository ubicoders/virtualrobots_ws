from ubicoders_vrobots import System, InertialSensor
import numpy as np

# Create a multirotor object that contains states (euler angles, angular velocities, sensors, actuators, etc.)
imu = InertialSensor()

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
        states = imu.states
        print("States: ", states)

        

if __name__ == "__main__":
    sys = System(imu, UbicodersMain())
    sys.start()
