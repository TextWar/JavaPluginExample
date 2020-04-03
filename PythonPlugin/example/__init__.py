from Event import Event, EventMode
from onEnable import OnEnable

print("example!!")
aa = " c"


@Event("PlayerFightEvent", EventMode.NormalHookMode)
def exevent(obj):
    print("aaaaaaaaaaaaaaaa")


@OnEnable()
def test():
    print("Example Plugins load2!")
# exec("event.append(exevent)")
