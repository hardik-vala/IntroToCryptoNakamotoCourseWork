##################################
#            PART 1              #
##################################

from hashlib import sha256

def sha2(s: str):
  return sha256(s.encode()).hexdigest()

def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
  token_elements = token.split(":")

  if len(token_elements) != 4:
    return False

  leading_0s = binary_leading_0s(sha2(token))

  return token_elements[0] == "1" and \
    token_elements[1] == date and \
    token_elements[2] == email and \
    len(token_elements[3]) == 16 and \
    leading_0s >= difficulty


##################################
#            PART 2              #
##################################

import random

NONCE_UPPER_BOUND = 2**64

def gen_nonce():
  return hex(random.randint(0, NONCE_UPPER_BOUND))

def mint(date: str, email: str, difficulty: int) -> str:
  while True:
    nonce = gen_nonce()[2:]
    token = "1:{}:{}:{}".format(date, email, nonce)
    leading_0s = binary_leading_0s(sha2(token))
    if leading_0s >= difficulty:
      return token
