import doctest
import unittest

import mock

import sigdispatch

SignalDispatcher = sigdispatch.SignalDispatcher


class SignalDispatcherTest(unittest.TestCase):
    def setUp(self):
        self.sd = SignalDispatcher()

    def test_emit_with_no_observers(self):
        self.sd.emit('foo')

    def test_emit_two_signals_with_observers(self):
        obs = mock.Mock()
        obs2 = mock.Mock()

        self.sd.observe('foo', obs)
        self.sd.observe('bar', obs)
        self.sd.observe('bar', obs2)

        self.sd.emit('foo')
        obs.assert_called_with(None)
        self.assertFalse(obs2.called)

        self.sd.emit('bar', 123)
        obs.assert_called_with(123)
        obs2.assert_called_with(123)

    def test_emit_catching_exceptions(self):
        obs1, obs2, obs3 = mock.Mock(), mock.Mock(), mock.Mock()
        obs1.side_effect = Exception('a')
        obs2.side_effect = Exception('b')
        self.sd.observe('foo', obs1)
        self.sd.observe('foo', obs2)
        self.sd.observe('foo', obs3)

        exc_handler_called = [0]

        def exc_handler(code, payload, exceptions):
            self.assertEquals(code, 'foo')
            self.assertEquals(payload, 123)
            self.assertEquals(
                set(exceptions),
                {obs1.side_effect, obs2.side_effect})
            exc_handler_called[0] += 1

        self.sd.on_exceptions(exc_handler)

        self.sd.emit('foo', 123)

        obs1.assert_called_with(123)
        obs2.assert_called_with(123)
        obs3.assert_called_with(123)

        self.assertEquals(exc_handler_called[0], 1)

    def test_several_exception_handlers(self):
        exc1, exc2 = mock.Mock(), mock.Mock()
        exc1.side_effect = Exception('a')
        exc2.side_effect = Exception('b')

        e = Exception('failed')

        def failer(*args):
            raise e

        self.sd.on_exceptions(exc1)
        self.sd.on_exceptions(exc2)
        self.sd.observe('foo', failer)
        self.sd.emit('foo')

        exc1.assert_called_with('foo', None, [e])
        exc2.assert_called_with('foo', None, [e])

    def test_unobserve(self):
        obs = mock.Mock()
        obs2 = mock.Mock()

        self.sd.observe('bar', obs)
        unobs = self.sd.observe('bar', obs2)
        unobs()

        self.sd.emit('bar', 123)
        obs.assert_called_with(123)
        self.assertFalse(obs2.called)
