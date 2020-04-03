from Event import Event, EventMode
from onEnable import OnEnable, OnDisable


@Event("PlayerMoveEvent", EventMode.NormalHookMode)
def event(obj):
    print(obj.getPlayer)


@OnEnable()
def onEnable():
    print("Example plugin load!")


@OnDisable()
def onDisable():
    print("Example plugin unload!")
