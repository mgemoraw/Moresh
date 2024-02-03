"""prime_nubers MOdule"""
import math
import random


# Euclidean algorithm for finding gcd of two numbers
# gcd - greatest common divisor
def gcd(a, b):
	# Returns the gcd of a and b
	while a != 0:
		a, b = b%a, a
	return b

def findModInverse(a, m):
	# Returns the modular inverse of (a % m) which is
	# the number x such that (a * x) % m = 1

	if gcd(a, m) != 1:
		return None 	# No mode inverse if a and m aren't relatively prime

	# Calculate using extended Euclidean Algorithm
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, m
	while v3 != 0:
		q = u3 // v3 	# note // is for integer division to find the quotient
		v1,v2,v3, u1, u2, u3 = (u1 - q*v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

	return u1 % m


# tests if the number is prime
def isPrimeTrialDiv(n):
	# tests if the number n is prime or not
	# works efficiently for smaller integers

	if n < 2:
		return False

	for i in range(2, int((math.sqrt(n)) + 1)):
		if (n % i == 0):
			return False
		
	return True



def primeSieve(sieveSize):
	# Returns a list of prime numbers calculated using
	# the Sieve of Eratosthenes algorithm
	# Recommended for small integers

	sieve = [True] * sieveSize

	sieve[0] = False	# 0 is not prime
	sieve[1] = False	# 1 is not prime

	# create the sieve
	for i in range(2, int(math.sqrt(sieveSize)) + 1):
		pointer = i * 2
		while pointer < sieveSize:
			sieve[pointer] = False
			pointer += i

	# Compile the list
	primes = []
	for i in range(sieveSize):
		if sieve[i]  == True:
			primes.append(i)

	return primes

def rabinMiller(num):
	# Returns True if num is prime number
	if num % 2 == 0 or num < 2:
		return False 	# Rabin Miller dosen't work on even integers

	if num == 3:
		return True

	s = num - 1
	t = 0
	while s % 2 == 0:
		# keep halving s until it is odd (and use t
		# to count howmany times we halved s)
		s = s // 2
		t += 1
	for trials in range(5):
		# try to falsify nums primality 5 times
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1:	# this test doesn't apply if v is 1
			i = 0
			while v != (num - 1):
				if (i == t - 1):
					return False
				else:
					i = i + 1
					v = (v ** 2) % num
	return True


# prime numbers below 100
LOW_PRIMES = primeSieve(100)

def isPrime(num):
	# Return True if num is prime.
	if (num < 2):
		return False  # 0, 1 and negative numbers are not prime

	for prime in LOW_PRIMES:
		if (num % prime == 0):
			return False

	# if all above tests returned true then
	# use rabinMiller to check primality
	return rabinMiller(num)

def generateLargePrime(keysize = 1024):
	# Generates large prime number
	while True:
		num = random.randrange(2**(keysize-1), 2**keysize)
		if isPrime(num):
			return num

# print(generateLargePrime(1048))

