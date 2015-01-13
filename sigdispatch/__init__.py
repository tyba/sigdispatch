"""
sigdispatch
~~~~~~~~~~~

Sigdispatch is a simple events library.

    >>> import sigdispatch
    >>> def on_foo(payload):
    ...     print('Received %s.' % payload)
    ...
    >>> def another_on_foo(payload):
    ...     print('Received %s too.' % payload)
    ...
    >>> sigdispatch.observe('foo', on_foo) #doctest: +ELLIPSIS
    <function unobserve at 0x...>
    >>> sigdispatch.observe('foo', another_on_foo) #doctest: +ELLIPSIS
    <function unobserve at 0x...>
    >>> sigdispatch.emit('foo', [1, 2, 3]) #doctest: +ELLIPSIS
    Received ...
    Received ...

This library implements a signal dispatcher between components of your
application, so that they can send messages (signals) to each other
in a decoupled fashion; emitters don't know which components are receiving
their signals.

See :py:class:`SignalDispatcher` for details of the intrinsics.

.. data:: default_dispatcher

   An instance of :py:class:`SignalDispatcher`. Calls to
   :py:func:`sigdispatch.observe`, :py:func:`emit` and
   :py:func:`on_exceptions` are method invocations of this object.

.. automodule:: sigdispatch.SignalDispatcher
   :members:
"""

__version__ = '0.0.1'

from .signal_dispatcher import SignalDispatcher


default_dispatcher = SignalDispatcher()


def observe(*args, **kwargs):
    """
    Calls ``default_dispatcher.observe``.
    See :py:meth:`.SignalDispatcher.observe`.
    """
    return default_dispatcher.observe(*args, **kwargs)


def emit(*args, **kwargs):
    """
    Calls ``default_dispatcher.emit``.
    See :py:meth:`.SignalDispatcher.emit`.
    """
    return default_dispatcher.emit(*args, **kwargs)


def on_exceptions(*args, **kwargs):
    """
    Calls ``default_dispatcher.observe``.
    See :py:meth:`.SignalDispatcher.on_exceptions`.
    """
    return default_dispatcher.on_exceptions(*args, **kwargs)
