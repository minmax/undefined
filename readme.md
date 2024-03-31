# Undefined

## Code examples

Use as default to help with None:

```
from undefined import Undefined, undefined

mapping: dict[str, object | Undefined] = {}

if value := mapping.get(key, undefined) is undefined:
    assert_type(value, Undefined)
else:
    assert_type(value, object) # 'value' May be None
```

Or use as pre-defined immutable function argument.

```
def foo(nullable: object | None | Undefined = undefined):
    if nullable is undefined:
        nullable = ...
```

## Long read

Ever needed a global object that act as `None` but not quite ?

Like for example key-word argument for function, where `None` make sens, so you need a default value.

One solution is to create as singleton object:

```
mysingleton = object()
```

Though it becomes difficult to track the singleton across libraries,
and teach users where to import this from.

It's also relatively annoying use this singleton across library.


Introducing `undefined`:

```
>>> from undefined import undefined, Undefined
>>> undefined is Undefined
True
```

# behavior

`undefined` - is for runtime 'is' operation

`Undefined` - is for type hinting

It work mostly like a singleton object

Though it's neither truthy not falsy

```
>>> if undefined: print(True)
raise NotImplementedError
```

# Why not `None`, difference with `None`

`undefined` is likely slower, and as it is a regular Python object there are a few  on purpose (or not difference).

### Unlike `None`, you can assign to it

```
>>> None = 3
SyntaxError: can't assign to keyword
```

```
>>> undefined = 3
>>> undefned
3
```

### Unlike `None`, `undefined` is neither true not false.

If you test for boolean value of `undefind` if will raise.
That is to say: the following will fail:

```
value = undefined
if value:
   pass # will raise before reaching here.
```

You have to check for identity:

```
value = undefined
other = 1
if value is undefined:
    pass # will execute
```

for info, undefined is not `True`,`False`, not undefined with respect to identity

```
>>> undefined is True
False

>>> undefined is False
False

>>>: undefined is None
False
```

### String form

`str(undefined)` raises. `repr(undefined)` is the unicode string `'Undefined'`
