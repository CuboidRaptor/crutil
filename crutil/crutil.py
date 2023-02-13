# imports?
import inspect
import binascii
import pickle

def test():
    """just needed to test that the program is running"""
    print("yo")

def get_sid(topic, callback):
    """Gets an sid from a topic/callback for subscribing/unsubscribing in pubsub."""
    return binascii.hexlify(topic.encode("utf-8") + pickle.dumps(callback)).decode("utf-8")

class pubsub:
    def __init__(self):
        # cache of listeners
        self.cache = {}

    def publish(self, topic, args, kwargs):
        """Publish to a channel, run all callbacks listed with args and kwargs as list/dict. Slashes are used for tiered publishing."""
        # Slashes are tiered, e.g subscribing to foo/bar/baz will callback when foo or foo/bar or foo/bar/baz are published.
        try:
            # retrieve listeners
            subs = self.cache[topic]

        except KeyError:
            # no listeners, don't waste performance than
            return

        for subscriber in reversed(subs):
            # callback listeners
            subscriber(*args, **kwargs)

    def subscribe(self, topic, callback):
        try:
            # retrieve listeners
            subs = self.cache[topic]

        except KeyError:
            # no listeners, don't waste performance than
            return

        subs.append(callback)

def find_args(func):
    """Attempt to list all arguments of a callable function"""
    try:
        return list(
            map(
                str,
                str(
                    inspect.signature(
                        func
                    )
                )[1:-1].split(
                    ", "
                )
            )
        )

    except ValueError:
        # couldn't find signature
        return None
