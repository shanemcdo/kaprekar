#!/usr/bin/env python3

import sys

# https://en.wikipedia.org/wiki/Kaprekar's_routine
KAPREKAR = 6174

def sort_digits(number: int, reverse: bool = False) -> int:
	return int(''.join(sorted(str(number).zfill(4), reverse=reverse)))

def desc_asc_diff(number: int) -> int:
	desc = sort_digits(number, True)
	asc = sort_digits(number)
	print(f'\n {desc}\n-{asc:04d}\n ----')
	return desc - asc

def main():
	'''Driver Code'''
	if len(sys.argv) > 1:
		number = sys.argv[1]
	else:
		number = input('Enter a number: ')
	number = number.zfill(4)
	if len(number) > 4 or not number.isdigit():
		print(f'{number} must be a 4 digit number')
		return
	while number != KAPREKAR:
		number = desc_asc_diff(number)
		print(f' {number}')

if __name__ == '__main__':
	main()
