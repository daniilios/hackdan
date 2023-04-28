import lirc

client = lirc.Client()
client.send_once("my-remote-name", "23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23")

# Go to channel "33"
client.send_once("my-remote-name", "232,323,232,323,232,32,323,232,323,232,323,232", repeat_count=1)
