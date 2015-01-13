# sigdispatch

A simple events library for Python.

```python
>>> import sigdispatch
>>> def on_foo(payload):
...     print 'Received %s.' % payload
...
>>> def another_on_foo(payload):
...     print 'Received %s too.' % payload
...
>>> sigdispatch.observe('foo', on_foo)
<function unobserve at 0x...>
>>> sigdispatch.observe('foo', another_on_foo)
<function unobserve at 0x...>
>>> sigdispatch.emit('foo', [1, 2, 3])
Received [1, 2, 3].
Received [1, 2, 3] too.
```
