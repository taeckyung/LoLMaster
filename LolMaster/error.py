class LolMasterException(Exception):
	pass


class KeyNotSetError(LolMasterException):
	pass


class RegionNotSetError(LolMasterException):
	pass


class KeyNotValidError(LolMasterException):
	pass


class MaxRetryError(LolMasterException):
	pass


class NotReachableError(LolMasterException):
	"""
	You should not reach this error.
	"""
	pass
