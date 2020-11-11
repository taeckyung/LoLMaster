class LoLMasterException(Exception):
	pass


class KeyNotSetError(LoLMasterException):
	pass


class RegionNotSetError(LoLMasterException):
	pass


class KeyNotValidError(LoLMasterException):
	pass


class MaxRetryError(LoLMasterException):
	pass


class NotReachableError(LoLMasterException):
	"""
	You should not reach this error.
	"""
	pass
