from Command import Command
from Event import Event, EventMode
from onEnable import OnEnable, OnDisable

server = None

@Event("PlayerJoinEvent", EventMode.NormalHookMode)
def onEvent(obj):
    server.getLogger().info("listen the the PlayerJoin")


@OnEnable()
def starting():
    print("Example Plugins load!")

@OnDisable()
def unloading():
    print("Example Plugins unload!")

@Command("test")
def cmd(args, player):
    print(args)
    print(player)

def getServer(server_):
    global server
    server = server_
    server.getLogger().info("get Server")