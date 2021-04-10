For your first coding assignment, you'll be producing a hash collision in a new hash function we'll call `MD1.25`.

`MD1.25` is just **MD5 truncated to the first 4 bytes (the first 8 digits in hex)**. Thus, `MD1.25` only has a digest size of 32 bits. You should be able to produce a collision in no more than a couple seconds.

To prove that you generated the hash collision yourself, **you must prefix your preimages with the string** "`nakamoto`". Your code should **return a tuple of the two colliding preimages as strings**.

Complete the assignment in `main.py`. Then hit the Run button to automatically run the test suite. (You can inspect the test suite yourself in `tests.py`). Once all the tests are passing, you're ready to move on. 

You can also check out the canonical solution [here](https://repl.it/@nakamoto/HashFunction-Solution#README.md).