import json
import time
from distribute_config import Config
from reachy import Reachy

Config.define_str("file_path", "", "path of the file to write the different positions")
Config.define_bool("record", True, "if true then record and run. Else only run ")


def main():
  Config.load_conf()
  config = Config.get_dict()

  reachy = Reachy()
  for motor in reachy.motors:
    motor.compliant = True

  if config["record"]:
    # First part of the script : the user can move the arm and hit return to save the arm position
    all_positions = []
    action = input("> ")
    while action != "save":
      # Save the position of the motors
      position = {}
      for motor in reachy.motors:
        print(f"The motor \"{motor.name}\" is currently in position: {motor.present_position}")
        position[motor.name] = motor.present_position
      all_positions.append(position)
      action = input("> ")
    # Save the list of position in a file
    with open(config["file_path"], "w") as f:
      json.dump(all_positions, f)
  else:
    # If this first part was not executed, then we need to read the json file to load the key points
    with open(config["file_path"], "r") as f:
      all_positions = json.load(f)

  # Move the arm
  for motor in reachy.motors:
    motor.compliant = False

  for position in all_positions:
    # Move to position
    for motor in reachy.motors:
      motor.goal_position = position[motor.name]

    # Wait 2 s
    time.sleep(2)

  for motor in reachy.motors:
    motor.compliant = True


if __name__ == "__main__":
  main()
