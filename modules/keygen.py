"""Public key generator """
import random, sys, os, primes


def main():
	# Create a public/private key pair with keysize of 1024 bytes
	print("Making Key ...")
	makeKeyFiles('moresh', 2048)
	print('Key files generated')


def generateKey(keySize):
	# Creats publi/private keys keySize bits in size
	p = 0
	q = 0
	# Step 1: Create two prime numbers p and q. calulate n = p * q
	print("Generating p prime...")
	while p == q:
		p = primes.generateLargePrime(keySize)
		q = primes.generateLargePrime(keySize)
	n = p*q

	# Step 2: Create a number e that is (p-1)*(q-1)
	print("Generating e that is relatively prime...")
	while True:
		# Keep trying random numbers for e until one is valid
		e = random.randrange(2**(keySize - 1), 2**(keySize))
		if primes.gcd(e, (p - 1) * (q - 1)) == 1:
			break

	# Step 3: Calculate d, the modular inverse of e
	print("Calculating d that is modular inverse of e")
	d = primes.findModInverse(e, n)

	publicKey = (n, e)
	privateKey = (n, d)

	print("Public key:", publicKey)
	print("Private key:", privateKey)

	return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
	# Create two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
	# is the value in name) with the n,e and d,e integers written in
	# them, delimited by a comma.

	# Our safety check will prevent us from overwriting our old key files:
	if os.path.exists("%s_pubkey.txt"%(name)) or os.path.exists("%s_privkey.txt"%(name)):
		sys.exit("WARNING: The filees %s_pubkey.txt and %s_privkey.txt already exists! Use a different file name or delete the files and rerun this program." %(name, name))

	publicKey, privateKey = generateKey(keySize)

	print()
	print("The public key is a {} and {} digit number.".format(len(str(publicKey[0])), len(str(publicKey[1]))))

	print("Writing public key to file {}_pubkey.txt".format(name))

	with open(f"{name}_pubkey.txt", 'w') as fo:
		fo.write("{}, {}, {}".format(keySize, publicKey[0], publicKey[1]))

	print()
	print("The private key is a {} and {} digit number.".format(len(str(privateKey[0])), len(str(privateKey[1]))))

	print("Writing public key to file {}_pubkey.txt".format(name))

	with open(f"{name}_privkey.txt", 'w') as fo:
		fo.write("{}, {}, {}".format(keySize, privateKey[0], privateKey[1]))



# If keygen.py is run (instead of imported as a module)
# call the main() function
if __name__ == "__main__":
	main()