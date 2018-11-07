# pystrin
A small Python library for string interpolation.

### Installing
With **pip** this package can be installed as follows:
```
pip install pystrin
```

### Usage
Use the `f` method on a string with a literal for string interpolation. Use `printf` instead to directly print the result. An example is:
```
name = 'campoe'
printf('Hello {name}')

# --- Output ---
# Hello campoe
```

In fact, it can be used with any expression:
```
x = 3
printf('5 * {x} = {5 * x}')

# --- Output ---
# 5 * 3 = 15
```
