import sys
import socket

def main():
    print("Python version:")
    print(sys.version)
    print('\n')

    hostname = socket.gethostname()
    print("hostname: ", hostname)

    x=7
    y=3
    print(f'{x} + {y} = {x+y}')

if __name__ == '__main__':
    main()