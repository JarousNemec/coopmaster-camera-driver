import server
from config import Config

if __name__ == '__main__':
    print(Config.hello_msg)
    server.run()