from sigdispatch import SignalDispatcher, default_dispatcher
from sigdispatch.observers import Observer, AlreadyRegisteredException
import sigdispatch.observers
import unittest
import mock
import doctest


class ObserverTest(unittest.TestCase):
    def setUp(self):
        self.sd = SignalDispatcher()

    def test_doc(self):
        fails, tested = doctest.testmod(sigdispatch.observers)
        if fails > 0:
            self.fail('Doctest failed!')

    def test_basic(self):
        called = []

        def callback(code, payload):
            called.append((code, payload))

        o = MyObserver(callback)
        o.register(self.sd)

        self.sd.emit('foo', 123)
        self.sd.emit('bar')

        self.assertEquals([
            ('foo', 123),
            ('bar', None),
        ], called)

    def test_uses_default_dispatcher(self):
        m = mock.Mock()
        o = MyObserver(m)
        o.register()

        default_dispatcher.emit('foo', 123)
        m.assert_called_with('foo', 123)

    def test_already_registered(self):
        m = mock.Mock()
        o = MyObserver(m)
        o.register()

        with self.assertRaises(AlreadyRegisteredException) as e:
            o.register()

        self.assertEquals(
            'observer object %r already registered in signal dispatcher.' % o,
            str(e.exception))

        default_dispatcher.emit('foo', 123)
        m.assert_called_with('foo', 123)

    def test_unregister(self):
        m = mock.Mock()
        o = MyObserver(m)
        o.register()

        o.unregister()
        default_dispatcher.emit('foo', 123)
        self.assertFalse(m.called)

        o.register()
        default_dispatcher.emit('foo', 123)
        m.assert_called_with('foo', 123)

    def test_unregister_several_times(self):
        m = mock.Mock()
        o = MyObserver(m)
        o.register()
        o.unregister()
        o.unregister()
        default_dispatcher.emit('foo', 123)
        self.assertFalse(m.called)


class MyObserver(Observer):
    def __init__(self, callback):
        super(MyObserver, self).__init__()
        self.callback = callback

    def on_foo(self, payload):
        self.callback('foo', payload)

    def on_bar(self, payload):
        self.callback('bar', payload)
