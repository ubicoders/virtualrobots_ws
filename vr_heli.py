from ubicoders_vrobots import System, Helicopter2D
import numpy as np

# Create a multirotor object that contains states (euler angles, angular velocities, sensors, actuators, etc.)
heli = Helicopter2D()

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
        states = heli.states
        print("States: ", states)

        # Set up-force to the helicopter
        heli.force = 20

if __name__ == "__main__":
    sys = System(heli, UbicodersMain())
    sys.start()
