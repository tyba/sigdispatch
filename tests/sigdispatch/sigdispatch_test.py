import contextlib
import doctest
import unittest

import mock

import sigdispatch


class ModuleTest(unittest.TestCase):
    def test_doc(self):
        fails, tested = doctest.testmod(sigdispatch)
        if fails > 0:
            self.fail('Doctest failed!')

    def test_default_observe(self):
        self._test_default_func('observe')

    def test_default_emit(self):
        self._test_default_func('emit')

    def test_default_on_exceptions(self):
        self._test_default_func('on_exceptions')

    def _test_default_func(self, f):
        with self._mock_dispatcher() as dispatcher:
            getattr(dispatcher, f).return_value = 'expected'

            got = getattr(sigdispatch, f)('foo', 'bar', 'baz')

            self.assertEquals(got, 'expected')
            getattr(dispatcher, f).assert_called_with('foo', 'bar', 'baz')

    @contextlib.contextmanager
    def _mock_dispatcher(self):
        prev = sigdispatch.default_dispatcher
        d = mock.Mock()
        sigdispatch.default_dispatcher = d
        yield d
        sigdispatch.default_dispatcher = prev
