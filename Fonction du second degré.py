#!/usr/bin/env python
# coding: utf-8

def racine2(a, b, c):
	delta = b**2 - 4 * a * c
	if delta < 0:
		sol = f"pas de solution"
	elif delta == 0:
		sol = f"une solution réelle{-b/2*a}"
	else:
		sol = f"deux solutions réelles {(-b-delta**0.5)/(2*a)} , {(-b+delta**0.5)/(2*a)}"
	return sol


a = float(input("a?"))
b = float(input("b ?"))
c = float(input("c ?"))
print(racine2(a, b, c))
