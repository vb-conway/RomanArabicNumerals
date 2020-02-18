class NumberOutOfRangeError(ValueError):
    """NumberOutOfRangeError is raised When Arabic Numeral is < 1 and > 1000"""
    pass


class NumberNotAnIntegerError(ValueError):
    """NumberNotAnIntegerError is raised When Arabic Numeral is decimal or string"""
    pass


class NotAValidRomanNumeralError(ValueError):
    """NotAValidRomanNumeralError is raised When Roman Numeral is:
       Empty String
       Invalid Pattern (Preceding / Repetition scenarios)
    """
    pass

#
# class TooManyRepetitionsError(NotAValidRomanNumeralError):
#     """TooManyRepetitionsError raised when Roman Numerals are repeated more than Permitted"""
#     pass
#
#
# class RomanPrecedenceError(NotAValidRomanNumeralError):
#     """RomanPrecedenceError raised when Higher Roman Numerals Precedes Lower"""
#     pass
#
#
# class InvalidRomanPairsError(NotAValidRomanNumeralError):
#     """InvalidRomanPairsError raised when Invalid Roman Pairs"""
#     pass
