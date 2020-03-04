from reachy import Reachy
from time import sleep
import json

class Robot:
  def __init__(self):
    config_path = '/home/seb/reachy/software/reachy/configuration/reachy-force-gripper.json'
    self.reachy = Reachy(config=config_path)
    # self.reachy = Reachy()
    # self.reachy.force_gripper.offset = 4
    # self.reachy.force_gripper.scale = 10000

    # Load tic tac to position
    with open("tictacto.json", "r") as f:
      self.all_positions = json.load(f)

  def open_gripper(self):
    self.reachy.r_gripper.compliant = False
    self.reachy.r_gripper.goal_position = -100


  def close_gripper(self, threshold=10):
    self.reachy.r_gripper.compliant = False
    self.reachy.r_gripper.goal_position = 100
    
    # while abs(r.force_gripper.load) < threshold:
    #     time.sleep(.01)
        
    # r.r_gripper.goal_position = r.r_gripper.present_position + 1.5

  def goto(self, x, y):
    for motor in self.reachy.motors:
      motor.compliant = False
    position = self.all_positions[x + y * 3]
    # Move to position
    for motor in self.reachy.motors:
      motor.goal_position = position[motor.name]
    # Wait 2 s
    sleep(2)


def main():
  r = Robot()
  r.open_gripper()
  sleep(2)
  r.goto(0, 0)
  # r.close_gripper()
  sleep(10)

if __name__ == "__main__":
  main()
