try:
	import re
except ImportError:
	del re
	re = None
	i_regex = False
else:
	i_regex = True


import inspect
import copy


glob, loc = {}, {}
_init = False


def _eval(s):
	global glob, loc
	ret = eval(s, glob, loc)
	
	global _init
	_init = False

	return ret


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
		except (SyntaxError, NameError, TypeError, ZeroDivisionError, ValueError) as e:
			return s
		else:
			reg = '{%s}' % param
			reg = re.escape(reg)
			ret = re.sub(reg, str(arg), ret)
	return ret


def f(s):
	global _init
	if not _init:
		glob = inspect.stack()[1][0].f_globals
		loc = inspect.stack()[1][0].f_locals
	if i_regex:
		return _f_regex(s)
	return _f_find(s)


def printf(s):
	global glob, loc
	glob = inspect.stack()[1][0].f_globals
	loc = inspect.stack()[1][0].f_locals
	
	global _init
	_init = True

	print(f(s))
