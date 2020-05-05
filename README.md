# WordToDigits Package

Author: Abhishek Rawat

This package is used to convert the numbers present in word form in an input passage to the traditional numeric (digits) form. The word representation of numbers could be anywhere in the passage. It works from zero to nine hundred and ninety nine million nine  hundred and ninety nine thousand and nine hundred and ninety nine. It also takes care of the decimal part, if present.

An example on how to use the package is shown below:- 

import wordtodigits

text1 = 'A car accelerates for five point two one seconds for a distance of one hundred and ten meters. '
print(wordtodigits.convert(text1))
#A car accelerates for 5.21 seconds for a distance of 110 meters.

text2 = 'three thousand and fifty three point five is the final score'
print(wordtodigits.convert(text2))
#3053.5 is the final score

If you find any bugs, or have any suggestions for improvement, contact me at abhishek18.official@gmail.com


