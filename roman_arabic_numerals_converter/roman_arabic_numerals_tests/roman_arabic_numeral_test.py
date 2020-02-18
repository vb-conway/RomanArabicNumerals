import unittest
from roman_arabic_numerals_converter.roman_arabic_numerals import RomanArabicNumeral
from roman_arabic_numerals_converter.roman_arabic_error_handlers.roman_arabic_errors import (NumberOutOfRangeError,
                                                                                             NumberNotAnIntegerError,
                                                                                             NotAValidRomanNumeralError)


class RomanNumeralTest(unittest.TestCase):
    
    def setUp(self):
        
        # A map with correct arabic/numerals test values
        self.arabic_roman_numerals_map = [(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'),
                                          (8, 'VIII'), (9, 'IX'), (10, 'X'), (31, 'XXXI'), (50, 'L'), (100, 'C'),
                                          (500, 'D'), (1000, 'M'), (252, 'CCLII'), (546, 'DXLVI'), (621, 'DCXXI'),
                                          (784, 'DCCLXXXIV'), (862, 'DCCCLXII'), (999, 'CMXCIX')]
        
        # An list of invalid repetitions of the Roman Patterns
        self.invalid_roman_repetitions = ['MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII']
        
        # A list of invalid roman pairs
        self.invalid_roman_pairs = ['CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV']
        
        # A list of invalid precedence examples
        self.invalid_romans_with_higher_before_lower = ['IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC']
    
    # Convert To Roman Tests
    def test_convert_to_roman_raises_NumberOutOfRangeError_when_arabic_numerals_out_of_range(self):
        """Convert To Roman is only valid for Arabic Numerals between 1 and 1000 (inclusive).
           Any larger than 1000 and smaller than 1 will raise NumberOutOfRangeError
        """
        self.assertRaises(NumberOutOfRangeError, RomanArabicNumeral.convert_to_roman, 1001)
    
    def test_convert_to_roman_raises_NumberOutOfRangeError_when_arabic_numerals_are_negative(self):
        """Convert To Roman is only valid for Arabic Numerals between 1 and 1000 (inclusive).
           Any -ve values will raise NumberOutOfRangeError
        """
        self.assertRaises(NumberOutOfRangeError, RomanArabicNumeral.convert_to_roman, -1)
    
    def test_convert_to_roman_raises_NumberNotAnIntegerError_when_arabic_numerals_are_decimal_values(self):
        """Convert To Roman is only valid for Integer Arabic Numerals.
           Non Integer values should raise NumberOutOfRangeError.
        """
        self.assertRaises(NumberNotAnIntegerError, RomanArabicNumeral.convert_to_roman, 0.5)
    
    def test_convert_to_roman_raises_NumberNotAnIntegerError_when_arabic_numerals_are_strings(self):
        """Convert To Roman is only valid for Integer Arabic Numerals.
           String(Non Integer) values should raise NumberOutOfRangeError.
        """
        self.assertRaises(NumberNotAnIntegerError, RomanArabicNumeral.convert_to_roman, '1')
    
    def test_convert_to_roman_return_correct_roman_numerals_from_arabic(self):
        """Convert To Roman should return correct roman numerals from valid arabic numerals."""
        for numeral, roman in self.arabic_roman_numerals_map:
            self.assertEqual(roman, RomanArabicNumeral.convert_to_roman(numeral))
    
    # Convert From Roman Tests
    def test_convert_from_roman_raises_NotAValidRomanNumeralError_when_too_many_repetitions(self):
        """Convert From Roman raises NotAValidRomanNumeralError
           When invalid Roman Numeral Repetitions e.g. 'MMMM'.
        """
        for roman in self.invalid_roman_repetitions:
            self.assertRaises(NotAValidRomanNumeralError, RomanArabicNumeral.convert_from_roman, roman)
    
    def test_convert_from_roman_raises_NotAValidRomanNumeralError_when_empty_string_as_roman(self):
        """Convert From Roman raises NotAValidRomanNumeralError
           When empty string e.g. ''
        """
        self.assertRaises(NotAValidRomanNumeralError, RomanArabicNumeral.convert_from_roman, '')
    
    def test_convert_from_roman_raises_NotAValidRomanNumeralError_when_invalid_roman_pairs(self):
        """Convert From Roman raises NotAValidRomanNumeralError
           When invalid Roman Numeral Pairs e.g. 'IVIV'
        """
        for roman in self.invalid_roman_pairs:
            self.assertRaises(NotAValidRomanNumeralError, RomanArabicNumeral.convert_from_roman, roman)
    
    def test_convert_from_roman_raises_NotAValidRomanNumeralError_when_higher_roman_numeral_precede_lower(self):
        """Convert From Roman raises NotAValidRomanNumeralError
           When a higher Roman Numeral Precedes a lower Numeral e.g. "XCX"
        """
        for roman in self.invalid_romans_with_higher_before_lower:
            self.assertRaises(NotAValidRomanNumeralError, RomanArabicNumeral.convert_from_roman, roman)
    
    def test_convert_from_roman_return_correct_arabic_numerals(self):
        """Convert From Roman validates all the Arabic Roman Numeral Pairs"""
        for arabic_n, roman_n in self.arabic_roman_numerals_map:
            self.assertEqual(arabic_n, RomanArabicNumeral.convert_from_roman(roman_n))
    
    # Symmetry Test
    def test_validate_symmetry_to_from_arabic_numerals(self):
        """Validates all the Arabic Numerals between 1 and 1000 (inc)
           return a correct Roman (convert_to_roman) and the Roman
           converted back to the correct Arabic Numeral (convert_from_roman) proving symmetry
           between 2 operations.
        """
        for arabic_n in range(1, 1001):
            roman = RomanArabicNumeral.convert_to_roman(arabic_n)
            numeral = RomanArabicNumeral.convert_from_roman(roman)
            self.assertEqual(arabic_n, numeral)


if __name__ == '__main__':
    unittest.main()
