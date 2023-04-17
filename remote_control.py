import os
import time

import keyboard


class RemoteControl:

    def __init__(self, room, brand):
        self.room = room
        self.brand = brand
        self.channel = 0

    def next_channel(self):
        self.channel += 1
        print(f'Advanced to channel: {self.channel}')

    def previous_channel(self):
        if self.channel > 0:
            self.channel -= 1
            print(f'Back to channel: {self.channel}')
        else:
            print(f'Current channel: {self.channel}')

    def choose_channel(self):
        channel = int(input('Choose a channel: '))
        if channel != self.channel:
            self.channel = channel
            print(f'Changed to channel: {self.channel}')
        else:
            print(f'Current channel: {self.channel}')

    def power_off(self):
        print('Turning off the TV!')

    def get_channel(self):
        print(f'Current channel: {self.channel}')


if __name__ == "__main__":

    remote_control = RemoteControl('Sala', 'Samsung')

    os.system('cls')

    print('-= Remote Control Menu =-')
    print(' ')
    print('[F5] To advance channel')
    print('[F6] To previous channel')
    print('[F7] To show current channel')
    print('[F8] To choose a channel')
    print('[F12] To turn off the TV')
    print('[F1] To show the brand TV')
    print('[F2] To show the room')
    print(' ')
    print('-= Console Log =-')
    print(' ')

    while True:
        try:
            if keyboard.is_pressed('F1'):
                print(remote_control.brand)
                time.sleep(0.5)
            elif keyboard.is_pressed('F2'):
                print(remote_control.room)
                time.sleep(0.5)
            elif keyboard.is_pressed('F5'):
                remote_control.next_channel()
                time.sleep(0.5)
            elif keyboard.is_pressed('F6'):
                remote_control.previous_channel()
                time.sleep(0.5)
            elif keyboard.is_pressed('F7'):
                remote_control.get_channel()
            elif keyboard.is_pressed('F8'):
                remote_control.choose_channel()
                time.sleep(0.5)
            elif keyboard.is_pressed('F12'):
                remote_control.power_off()
                break

        except Exception as e:
            print(e)
