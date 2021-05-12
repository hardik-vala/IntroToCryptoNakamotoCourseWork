import argparse
import binascii
import math


def main():
	passphrase = b"SOLUTION TEXT GOES HERE"
	encrypted_prog_assign_soln_input_path = "prog_assign_soln.encrypted"
	decrypted_prog_assign_soln_out_path = "prog_assign_soln.py"

	key_hex = binascii.hexlify(passphrase)
	with open(encrypted_prog_assign_soln_input_path, 'r') as f:
		ciphertext_hex = f.read()

	expanded_key_hex_prefix = key_hex * int(math.floor(len(ciphertext_hex) / float(len(key_hex))))
	expanded_key_hex = expanded_key_hex_prefix + key_hex[:(len(ciphertext_hex) - len(expanded_key_hex_prefix))]

	plaintext_hex = "0" + hex(int(ciphertext_hex, 16) ^ int(expanded_key_hex, 16))[2:]
	plaintext = bytes.fromhex(plaintext_hex).decode()

	with open(decrypted_prog_assign_soln_out_path, 'w') as f:
		f.write(plaintext)


if __name__ == '__main__':
	main()
