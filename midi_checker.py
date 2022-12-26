import rtmidi
import rtmidi.midiutil
import mido

if __name__ == '__main__':
    prt = mido.open_input()
    while True:
        for msg in prt:
            print(msg)
            print(msg.type)
        # if msg.control == 56:
        #     print('fader #9')



