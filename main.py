#!/usr/bin/env python3

import sys

# https://en.wikipedia.org/wiki/Kaprekar's_routine
KAPREKAR = 6174
WIDTH = 4

def sort_digits(number: int, reverse: bool = False) -> int:
	return int(''.join(sorted(str(number).zfill(WIDTH), reverse=reverse)))

def desc_asc_diff(number: int, verbose = True) -> int:
	desc = sort_digits(number, reverse = True)
	asc = sort_digits(number)
	if verbose:
		print(f' {desc}\n-%0{WIDTH}d\n ----' % asc)
	return desc - asc

def perform_kaprekars_routine(number: int, verbose: bool = True) -> int:
	'''
	https://en.wikipedia.org/wiki/Kaprekar's_routine
	:number: the value on which to perform the routine on
	:verbose: print the operations as they occur
	:return: steps needed to reach constant
	'''
	if len(set(str(number).zfill(WIDTH))) <= 1:
		return -1
	steps = 0
	while number != KAPREKAR:
		steps += 1
		if verbose:
			print(f'step {steps}')
		number = desc_asc_diff(number, verbose = verbose)
		if verbose:
			print(f' %0{WIDTH}d\n' % number)
	return steps

def main():
	'''Driver Code'''
	if len(sys.argv) > 1:
		number = sys.argv[1].zfill(WIDTH)
		if len(number) > WIDTH or not number.isdigit():
			print(f'{number} must be a {WIDTH} digit number')
			return
		number = int(number)
		perform_kaprekars_routine(number, True)
	else:
		all_steps = []
		for i in range(0, 10 ** WIDTH):
			steps = perform_kaprekars_routine(i, False)
			if steps == -1:
				print(f'{i} would never reach the constant')
			else:
				all_steps.append(steps)
				print(f'{i} took {steps} to reach the constant')
		print(f'min: {min(all_steps)}')
		print(f'max: {max(all_steps)}')
		s = sum(all_steps)
		print(f'sum: {s}')
		print(f'average: {s / len(all_steps)}')

if __name__ == '__main__':
	main()
