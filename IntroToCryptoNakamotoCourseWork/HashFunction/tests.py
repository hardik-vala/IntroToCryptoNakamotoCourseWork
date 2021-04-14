import unittest
from hashlib import md5
from main import generate_md125_collisions

def md125(s: str) -> str:
  return md5(s.encode()).hexdigest()[:8]

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
      self.result = generate_md125_collisions()

    def test_correct_return_type(self):
      self.assertIsInstance(self.result, tuple, "Must return a tuple")

    def test_valid_collision(self):
        a, b = self.result
        self.assertEqual(md125(a), md125(b), "md1.25 values must collide")

    def test_not_identical(self):
        a, b = self.result
        self.assertNotEqual(a, b, "Values cannot be identical")

    def test_valid_prefix(self):
        a, b = self.result
        self.assertTrue(
          a.startswith('nakamoto') and b.startswith('nakamoto'),
          "Both strings must have the 'nakamoto' prefix"
        )

if __name__ == '__main__':
    unittest.main(failfast=True)