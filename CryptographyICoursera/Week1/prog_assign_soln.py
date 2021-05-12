
from collections import Counter
from itertools import combinations


CIPHERTEXTS = [
	"315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e",
	"234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f",
	"32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb",
	"32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa",
	"3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070",
	"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4",
	"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce",
	"315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3",
	"271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027",
	"466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83",
	"32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
]

DECRYPT_KEY_ADJUSTMENTS = [
	(CIPHERTEXTS[10], 14, 'r'),
	(CIPHERTEXTS[10], 50, 'e'),
	(CIPHERTEXTS[8], 70, 's'),
	(CIPHERTEXTS[7], 172, 'e'),
	(CIPHERTEXTS[0], 174, 't'),
	(CIPHERTEXTS[0], 176, 'h'),
	(CIPHERTEXTS[3], 178, 'e'),
	(CIPHERTEXTS[3], 180, 'd'),
	(CIPHERTEXTS[7], 182, 'e'),
	(CIPHERTEXTS[7], 184, 'r'),
	(CIPHERTEXTS[5], 186, 'e'),
	(CIPHERTEXTS[5], 188, 'r'),
	(CIPHERTEXTS[4], 190, 'n'),
	(CIPHERTEXTS[4], 192, 'b'),
	(CIPHERTEXTS[4], 194, 'e'),
	(CIPHERTEXTS[4], 196, 'r'),
	(CIPHERTEXTS[4], 198, 'g'),
	(CIPHERTEXTS[6], 200, 'o'),
	(CIPHERTEXTS[6], 202, 'd'),
	(CIPHERTEXTS[6], 204, 'e'),
	(CIPHERTEXTS[5], 206, 'a'),
	(CIPHERTEXTS[5], 208, 't'),
	(CIPHERTEXTS[5], 210, ' '),
	(CIPHERTEXTS[8], 212, 'e'),
	(CIPHERTEXTS[3], 214, 'r'),
	(CIPHERTEXTS[3], 216, 'y'),
	(CIPHERTEXTS[3], 218, 'p'),
	(CIPHERTEXTS[3], 220, 't'),
	(CIPHERTEXTS[3], 222, 'i'),
	(CIPHERTEXTS[3], 224, 'o'),
	(CIPHERTEXTS[3], 226, 'n'),
	(CIPHERTEXTS[7], 228, ' '),
	(CIPHERTEXTS[8], 230, 'r'),
	(CIPHERTEXTS[8], 232, 'y'),
	(CIPHERTEXTS[8], 234, 'p'),
	(CIPHERTEXTS[8], 236, 't'),
	(CIPHERTEXTS[3], 238, 'r'),
	(CIPHERTEXTS[3], 240, 'i'),
	(CIPHERTEXTS[3], 242, 't'),
	(CIPHERTEXTS[3], 244, 'h'),
	(CIPHERTEXTS[3], 246, 'm'),
	(CIPHERTEXTS[6], 248, 'e'),
	(CIPHERTEXTS[6], 250, 's'),
	(CIPHERTEXTS[5], 252, 'e'),
	(CIPHERTEXTS[5], 254, 't'),
	(CIPHERTEXTS[5], 256, 's'),
	(CIPHERTEXTS[8], 258, ' '),
	(CIPHERTEXTS[6], 260, ' '),
	(CIPHERTEXTS[5], 262, 'a'),
	(CIPHERTEXTS[5], 264, 'f'),
	(CIPHERTEXTS[5], 266, 'e'),
	(CIPHERTEXTS[6], 268, 'e'),
	]

SPACE_CHARACTER_HEX_DIGITS = "20"


def main():
	inferred_decrypt_key = infer_decrypt_key()
	decrypt_key = adjust_decrypt_key(inferred_decrypt_key)
	print("decrypt key: %s" % decrypt_key)

	for i, ciphertext in enumerate(CIPHERTEXTS):
		plaintext_hex = decrypt(decrypt_key, ciphertext)
		print("\n(%d) plaintext (hex): %s" % (i, plaintext_hex))

		plaintext = str_hex_to_ascii(plaintext_hex)
		print("(%d) plaintext: %s" % (i, plaintext))


def infer_decrypt_key():
	key_hex_digit_pairs = [] 
	key_len = get_longest_cipher_text_len()
	for pair_start_index in range(0, key_len, 2):
		key_digit_pair = infer_decrypt_key_hex_digit_pair(pair_start_index)
		if key_digit_pair:
			key_hex_digit_pairs.append(key_digit_pair)

	return "".join(key_hex_digit_pairs)


def adjust_decrypt_key(decrypt_key):
	decrypt_key_hex_digits = list(decrypt_key)

	for ciphertext, pair_start_index, plaintext_char in DECRYPT_KEY_ADJUSTMENTS:
		some_adjusted_key_hex_digits = get_adjusted_decrypt_key_hex_digit_pair(
			ciphertext,
			pair_start_index,
			plaintext_char)
		decrypt_key_hex_digits[pair_start_index] = \
			some_adjusted_key_hex_digits[0]
		decrypt_key_hex_digits[pair_start_index + 1] = \
			some_adjusted_key_hex_digits[1]

	return "".join(decrypt_key_hex_digits)


def decrypt(key, text):
	return strxor(key, text)


def str_hex_to_ascii(str_hex):
	return bytes.fromhex(str_hex).decode('ascii', 'ignore')


def get_longest_cipher_text_len():
	return max([len(ct) for ct in CIPHERTEXTS])


def infer_decrypt_key_hex_digit_pair(pair_start_index):
	space_hits_per_ciphertext = Counter()

	for ciphertext_1, ciphertext_2 in iter_ciphertext_pairs():
		if pair_start_index + 2 >= len(ciphertext_1) or \
			pair_start_index + 2 >= len(ciphertext_2):
			continue

		ciphertext_hex_digit_pair_1 = \
			ciphertext_1[pair_start_index : pair_start_index + 2]
		ciphertext_hex_digit_pair_2 = \
			ciphertext_2[pair_start_index : pair_start_index + 2]

		result_hex_digit_pair = strxor(ciphertext_hex_digit_pair_1,
			ciphertext_hex_digit_pair_2)

		if is_letter(result_hex_digit_pair):
			space_hits_per_ciphertext[ciphertext_1] += 1
			space_hits_per_ciphertext[ciphertext_2] += 1

	if len(space_hits_per_ciphertext) == 0:
		return ""

	ciphertext_with_most_space_hits = \
		space_hits_per_ciphertext.most_common(1)[0][0]
	hex_digit_pair = \
		ciphertext_with_most_space_hits[pair_start_index : pair_start_index + 2]
	key_hex_digit_pair = strxor(hex_digit_pair, SPACE_CHARACTER_HEX_DIGITS)
	
	if len(key_hex_digit_pair) == 1:
		return "0" + key_hex_digit_pair
	return key_hex_digit_pair


def get_adjusted_decrypt_key_hex_digit_pair(
	ciphertext,
	pair_start_index,
	plaintext_char):
	ciphertext_hex_digit_pair = \
		ciphertext[pair_start_index : pair_start_index + 2]
	adjusted_key_hex_digits = strxor(
		ciphertext_hex_digit_pair,
		char_to_hex_digit_pair(plaintext_char))
	if len(adjusted_key_hex_digits) == 1:
		return "0" + adjusted_key_hex_digits
	return adjusted_key_hex_digits


def iter_ciphertext_pairs():
	for i, j in combinations(range(len(CIPHERTEXTS)), 2):
		yield (CIPHERTEXTS[i], CIPHERTEXTS[j])


def is_letter(hex_digit_pair):
	ord_val = int(hex_digit_pair, 16)
	return (ord('A') <= ord_val and ord_val <= ord('Z')) or \
		(ord('a') <= ord_val and ord_val <= ord('z'))


def char_to_hex_digit_pair(char):
	return hex(ord(char))[2:]


# xor two strings of different lengths, i.e. a^b
def strxor(a, b):
    if len(a) > len(b):
       return hex(int(a[:len(b)], 16) ^ int(b, 16))[2:]
    else:
       return hex(int(a, 16) ^ int(b[:len(a)], 16))[2:]


if __name__ == '__main__':
	main()
