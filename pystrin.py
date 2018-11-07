try:
	import re
except ImportError:
	del re
	re = None
	i_regex = False
else:
	i_regex = True


def _eval(s):
	return eval(s)


def _f_find(s):
	ret = str(s)
	end = 0
	while end < len(ret):
		start = ret[end:].find('{') + 1
		end = ret[start:].find('}') + start
		param = ret[start:end]
		try:

			arg = _eval(str(param))
		except (SyntaxError, NameError, TypeError, ZeroDivisionError, ValueError) as e:
			return s
		else:
			ret = ret[:(start - 1)] + arg + ret[(end + 1):]
			end += 1
	return ret
		


def _f_regex(s):
	reg = '{(.*?)}'
	ret = str(s)
	params = re.findall(reg, ret)
	for param in params:
		try:
			arg = _eval(str(param))
		except (SyntaxError, NameError, TypeError, ZeroDivisionError, ValueError):
			return s
		else:
			reg = '{%s}' % param
			ret = re.sub(reg, str(arg), ret)
	return ret


def f(s):
	if i_regex:
		return _f_regex(s)
	return _f_find(s)


def printf(s):
	print(f(s))
