import sys
sys.path.append('/home/tim/hackathon/app')
from sensor_server.server import SensorServer


failed = True
count = 0
port = 5557
while failed:
    try:
        sensor_server = SensorServer('0.0.0.0', port)
        sensor_server.start()
    except Exception as e:
        count += 1
        port += 1
        if count > 10:
            sys.exit(1)
    else:
        print("USING PORT %d" % (port))
        failed = False


def get_sensor_server():
    return sensor_server
