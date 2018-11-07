# pystrin
A small Python library for string interpolation.

### Usage
Use the `f` method with a string containing a literal for string interpolation. Use `printf` to directly print the result. An example is:
```
name = 'campoe'
printf('Hello {name}')

# --- Output ---
# Hello campoe
```

It can also be used to evaluate an expression:
```
x = 3
printf('5 * {x} = {5 * x}')

# --- Output ---
# 5 * 3 = 15
```
