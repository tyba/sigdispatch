# sigdispatch

A simple events library for Python.

[![image](https://readthedocs.org/projects/sigdispatch/badge/?version=latest)](http://sigdispatch.readthedocs.org/) [![Build Status](https://travis-ci.org/Tyba/sigdispatch.svg)](https://travis-ci.org/Tyba/sigdispatch)

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

See [the documentation](http://sigdispatch.readthedocs.org/).