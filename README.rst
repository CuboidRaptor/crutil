======
Crutil
======

This is a random library I made with random garbage I made that occasionally can help with programming.
It's just the must random code crammed into one poopy doopy thing maintained by a dumbo octopus, so use this at your own risk.

Docs...?
========

- crutil.recursion() ; A context manager that lets you temporarily set your recursion depth. Use::

    with crutil.recursion(<some recursion limit here>):
        <do something here>
	  
  Your recursion limit will be reset after.
  
- crutil.suppress() ; A suppression context manager, use it with the "with" keyword like crutil.recursion(). This will
  temporarily suppres stdout and stderr, preventing anything from being printed to console, even with sys.stderr.write.
  This will, however, not silence error messages, although that's probably a good thing.
  
- crutil.pubsub() ; Class that lets you use a publish subscribe model. You can create an instance, then publish/subscribe to that instance.::
	
    ps = crutil.pubsub()
	
	def foo(bar):
	    return bar + 1
	
	sid = ps.subscribe("baz", foo)
	
	print(ps.publish("baz", [7]))
	
	ps.unsubscribe(sid)
	
  This will print [8]. There is also crutil.pubsub().clear(), which clears all subscribers and crutil.pubsub().view(), which will pretty print the cache.
  
- crutil.find_args(func) ; Tries, *tries*, to return a list of all arguments of function.

- crutil.test() ; idfk figure it out