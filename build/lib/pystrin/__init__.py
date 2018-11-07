try:
	from pystrin import f, printf
except ImportError:
	from pystrin.pystrin import f, printf


__all__ = ['f', 'printf']
