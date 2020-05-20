class KeyNotSetError(Exception):
	pass


class RegionNotSetError(Exception):
	pass


class KeyNotValidError(Exception):
	pass


class MaxRetryError(Exception):
	pass


class NotReachableError(Exception):
	"""
	You should not reach this error.
	"""
	pass
