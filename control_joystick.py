import pygame, sys
import keyboard


def getAxis(number, joystick):
    # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
    # so this is used not "if joystick value not zero"
    if number == 0 and joystick.get_axis(0) < -0.3:  # 왼쪽 방향
        keyboard.PressAndReleaseKey(0x25)
    if number == 0 and joystick.get_axis(0) > 0.3:  # 오른쪽 방향
        keyboard.PressAndReleaseKey(0x27)
    if number == 1 and joystick.get_axis(1) < -0.3:  # 위쪽 방향
        keyboard.PressAndReleaseKey(0x26)
    if number == 1 and joystick.get_axis(1) > 0.3:  # 아래쪽 방향
        keyboard.PressAndReleaseKey(0x28)


def getButton(number, joystick):
    # returns 1 or 0 - pressed or not
    if joystick.get_button(number):
        if number == 0:
            keyboard.PressAndReleaseKey(0x20)
        if number == 1:
            keyboard.PressAndReleaseKey(0x11)
        if number == 2:
            keyboard.PressAndReleaseKey(0x12)


def getHat(number, joystick):
    if joystick.get_hat(number) == (-1, 0):  # 왼쪽 방향
        # returns tuple with values either 1, 0 or -1
        keyboard.PressAndReleaseKey(0x25)
    if joystick.get_hat(number) == (1, 0):  # 오른쪽 방향
        # returns tuple with values either 1, 0 or -1
        keyboard.PressAndReleaseKey(0x27)
    if joystick.get_hat(number) == (0, 1):  # 위쪽 방향
        # returns tuple with values either 1, 0 or -1
        keyboard.PressAndReleaseKey(0x26)
    if joystick.get_hat(number) == (0, -1):  # 아래쪽 방향
        # returns tuple with values either 1, 0 or -1
        keyboard.PressAndReleaseKey(0x28)
    if joystick.get_hat(number) == (0, 0):
        return


if __name__ == '__main__':
    # setup the pygame window
    pygame.init()
    window = pygame.display.set_mode((200, 200), 0, 32)

    # how many joysticks connected to computer?
    joystick_count = pygame.joystick.get_count()
    print("There is " + str(joystick_count) + " joystick/s")

    if joystick_count == 0:
        # if no joysticks, quit program safely
        print("Error, I did not find any joysticks")
        pygame.quit()
        sys.exit()
    else:
        # initialise joystick
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    print(joystick)
    axes = joystick.get_numaxes()
    buttons = joystick.get_numbuttons()
    hats = joystick.get_numhats()

    while True:
        for event in pygame.event.get():
            # loop through events, if window shut down, quit program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if axes != 0:
            for i in range(axes):
                getAxis(i, joystick)
        if buttons != 0:
            for i in range(buttons):
                getButton(i, joystick)
        if hats != 0:
            for i in range(hats):
                getHat(i, joystick)
