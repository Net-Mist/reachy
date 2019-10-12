# Reachy

This repo is a collection of small tools to start with [Reachy](https://github.com/pollen-robotics/reachy)

## Installation

These scripts were tested on linux with Python 3.6. To install Reachy's framework follow the [official readme](https://github.com/pollen-robotics/reachy#installation) or run :
```bash
sudo apt install liblapack-dev gfortran libblas-dev
git clone https://github.com/pollen-robotics/reachy.git
pip3 install -e ./reachy/software
```

On a Raspberry Pi you can start the scripts by running `python3`. On Ubuntu, you need more permissions, so you need to run `sudo python3`


## Scripts

### check_motor.py
This script set Reachy's motor to compliant mode and display every second the positions of the motors.

### move_memory.py
The script allows a user to move Reachy freely. Hitting `return` save the current position of the arm in a new key point. You can save as many key point 
as you want. When you're finished type "save" and the list of the key points will be saved in a json file. Then the are will iterate other the list of key points to redo the same moves.  

This script has 2 parameters :
- file_path: path of a json file where it will store the key points
- record : boolean. If true then record key points, else only read the json file and move


