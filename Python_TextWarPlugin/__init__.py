from Command import Command
from Event import Event, EventMode
from onEnable import OnEnable, OnDisable

server = None

@Event("PlayerJoinEvent", EventMode.NormalHookMode)
def onEvent(obj):
    server.getLogger().info("listen the the PlayerJoin")


@OnEnable()
def starting():
    server.getLogger().info("Example Plugins load!")

@OnDisable()
def unloading():
    server.getLogger().info("Example Plugins unload!")

@Command("test")
def cmd(args, player):
    server.getLogger().info(str(args))
    server.getLogger().info(str(player))

def getServer(server_):
    global server
    server = server_
    server.getLogger().info("get Server")