import os

msg = "Hello line follower from %s!"%os.environ['VEHICLE_NAME']
print(msg)
