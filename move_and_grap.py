from reachy import Reachy, parts

PORT = "/dev/ttypACM0"

reachy = Reachy(
    right_arm=parts.arm.RightArm(
        luos_port=PORT,
        hand='force_gripper',
    ),
    # head=parts.head.Head(
    #     luos_port=PORT,
    #     camera_id=0,
    # ),
)