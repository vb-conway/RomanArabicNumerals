from roman_arabic_numerals_converter.roman_arabic_error_handlers.roman_arabic_errors import (NumberOutOfRangeError,
                                                                                             NumberNotAnIntegerError,
                                                                                             NotAValidRomanNumeralError)

import re


class RomanArabicNumeral:
    
    # A well defined map of Roman Arabic Numerals reduces code complexity when converting numerals.
    roman_arabic_numerals_map = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
                                 ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

    # roman_arabic_numerals_map = [('M', 1000, 3), ('CM', 900, 1), ('CD', 400, 1), ('D', 500, 1), ('C', 100, 3),
    #                             ('XC', 90, 1), ('XL', 40, 1), ('L', 50, 1), ('X', 10, 3), ('IX', 9, 1), ('IV', 4, 1),
    #                             ('V', 5, 1), , ('I', 1, 3)]

    # Using Regex instead of Tuples above to validate Roman Numerals Patterns.
    # This approach is very extensible following O of SOLID
    roman_numeral_pattern_regex = re.compile(r"""
                                             ^                  # Start of string
                                             M{0,1}             # thousands - 1000 (M) - 0 to 1M
                                             (CM|CD|D?C{0,3})   # hundred -  900 (CM), 400 (CD), 0-300 (0 to 3Cs),
                                                                 #    or 500-800 (D, followed by 3Cs)
                                             (XC|XL|L?X{0,3})   # tens - 90 (XC), 40 (XL),
                                                                 #    or 50-80 (L followed by 0 to 3 Xs)
                                             (IX|IV|V?I{0,3})   # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is)
                                                                 #    or 5-8 ( V, followed by 0 to 3 Is)
                                             $                   # end of string
                                             """, re.VERBOSE)
    
    @classmethod
    def convert_to_roman(cls, numeral: int) -> str:
        """Convert From Arabic Numerals to Roman"""
        if int(numeral) != numeral:
            raise NumberNotAnIntegerError(f'Number {numeral} should be of type int')
        if not (0 < numeral < 1001):
            raise NumberOutOfRangeError(f'Number {numeral} should be between 1 and 1000')
        
        result = ''
        for roman_n, arabic_n in cls.roman_arabic_numerals_map:
            while numeral >= arabic_n:
                result += roman_n
                numeral -= arabic_n
                # print(f'Substituting Roman Numeral {roman_n} Arabic {arabic_n} result {result}')
        return result
    
    @classmethod
    def convert_from_roman(cls, roman: str) -> int:
        """Convert From Roman To Arabic Numerals"""
        if not roman:
            raise NotAValidRomanNumeralError(f'Roman numeral should be a valid non-empty string')
        if not cls.roman_numeral_pattern_regex.search(roman):
            raise NotAValidRomanNumeralError(f'Roman numeral {roman} should be a in a valid format')
        
        arabic_numeral = 0
        index = 0
        for roman_n, arabic_n in cls.roman_arabic_numerals_map:
            while roman[index:index + len(roman_n)] == roman_n:
                arabic_numeral += arabic_n
                index += len(roman_n)
                # print(f'Generating {arabic_numeral} from {roman_n}')
        return arabic_numeral


if __name__ == "__main__":

    while True:
        numeral = input("\nPlease Enter Roman/Arabic Numeral: ")
        try:
            if numeral.isdigit():
                print(RomanArabicNumeral.convert_to_roman(int(numeral)))
            else:
                print(RomanArabicNumeral.convert_from_roman(numeral))
        except (NumberOutOfRangeError, NumberNotAnIntegerError, NotAValidRomanNumeralError) as e:
            print(f'{e}')
            pass
