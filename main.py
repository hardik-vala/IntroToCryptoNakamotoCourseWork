import random, string

from hashlib import md5

PREIMAGE_PREFIX = "nakamoto"
MAX_RANDOM_STR_LEN = 10

def md125(s: str) -> str: # this is the hash function you'll use
  return md5(s.encode()).hexdigest()[:8]

def generate_md125_collisions() -> (str, str):
  def random_str():
    l = random.randint(1, MAX_RANDOM_STR_LEN)
    return ''.join((random.choice(string.ascii_letters) for _ in range(l)))

  digests = {}

  while True:
    preimage = PREIMAGE_PREFIX + random_str()
    digest = md125(preimage)
    if digest in digests and digests[digest] != preimage:
      return (preimage, digests[digest])
    else:
      digests[digest] = preimage