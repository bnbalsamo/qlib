import unittest
import qlib
from random import shuffle


class Tests(unittest.TestCase):
    def setUp(self):
        self.q = qlib.Queue("testApp", "localhost")

    def tearDown(self):
        for x in self.q._gen_queue_keys():
            self.q.redis.delete(x)
        del self.q

    def test_block_false(self):
        self.assertEqual(
            self.q.retrieve_identifier(block=False),
            None
        )

    def test_block_delay_finishes(self):
        self.assertEqual(
            self.q.retrieve_identifier(block=3),
            None
        )

    def test_add_retrieve(self):
        self.q.add_identifier("abcd")
        self.assertEqual(
            self.q.retrieve_identifier(),
            "abcd"
        )

    def test_block_equals_true(self):
        self.q.add_identifier("abcd")
        self.assertEqual(
            self.q.retrieve_identifier(block=True),
            "abcd"
        )

    def test_block_false_return(self):
        self.q.add_identifier("abcd")
        self.assertEqual(
            self.q.retrieve_identifier(block=False),
            "abcd"
        )

    def test_bad_priority(self):
        with self.assertRaises(ValueError):
            self.q.add_identifier("abcd", "foobar")
        with self.assertRaises(ValueError):
            self.q.add_identifier("abcd", 10)
        with self.assertRaises(ValueError):
            self.q.add_identifier("abcd", 0)
        with self.assertRaises(ValueError):
            self.q.add_identifier("abcd", -1)

    def test_priorities_respected(self):
        priorities = [1,2,3,4,5,6,7,8,9]
        shuffle(priorities)
        for x in priorities:
            self.q.add_identifier(str(x), x)
        for x in range(1, 10):
            self.assertEqual(
                self.q.retrieve_identifier(),
                str(x)
            )


if __name__ == "__main__":
    unittest.main()
