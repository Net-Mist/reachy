import time
from reachy import Reachy


def main():
  reachy = Reachy()
  for motor in reachy.motors:
    motor.compliant = True

  while True:
    print(30*'\n')
    for motor in reachy.motors:
      print(f"The motor \"{motor.name}\" is in position: {motor.present_position}")
    time.sleep(1)


if __name__ == "__main__":
  main()
