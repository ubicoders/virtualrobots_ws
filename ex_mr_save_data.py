from ubicoders_vrobots import System, Multirotor
import numpy as np

# Create a multirotor object that contains states (euler angles, angular velocities, sensors, actuators, etc.)
mr = Multirotor()
# Open a file to save the data
file = open('multirotor_data.json', 'w')
# Write the first line of the file
file.write('[\n')


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
        print("states: ", states)

        # Write the data to the file
        file.write(str(states) + ',\n')

        # Set the PWM values to the motors! between 1100 to 2000
        mr.set_pwm(m0=1250, m1=1250, m2=1250, m3=1250)

if __name__ == "__main__":
    sys = System(mr, UbicodersMain())
    sys.start()

    # Close the file
    file.write(']')
    file.close()