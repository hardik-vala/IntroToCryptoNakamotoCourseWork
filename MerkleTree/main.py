#######################################
#              PART 1                 #
#######################################

import math
from collections import deque
from hashlib import sha256

def sha2(s):
  return sha256(s.encode()).hexdigest()

def merkleize(sentence: str) -> str:
  words = sentence.split()
  word_hashes = [sha2(w) for w in words]
  padding_len = 2 ** math.ceil(math.log2(len(words))) - len(words)
  blocks = deque(word_hashes + (['\x00'] * padding_len))
  while len(blocks) > 1:
    blocks.append(sha2(blocks.popleft() + blocks.popleft()))
  return blocks.pop()

#######################################
#              PART 2                 #
#######################################

from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
  hash = sha2(data)
  for sibling, side in proof:
    if side == Side.LEFT:
      hash = sha2(sibling + hash)
    else:
      hash = sha2(hash + sibling)
  return hash == root
