from unittest import TestCase
from Big_Integer import *


class TestBigInteger(TestCase):
    def setUp(self):
        self.bigint_1 = BigInteger('1')
        self.bigint_1234 = BigInteger('1234')
        self.bigint_odd1234 = BigInteger('-1234')
        self.bigint_555555 = BigInteger('555555')
        self.bigint_50505_11 = BigInteger(str(50505 * 11))
        self.bigint_odd555555 = BigInteger('-555555')

    def tearDown(self):
        self.setUp()

    def test_str(self):
        self.assertEqual(str(self.bigint_1), '1')
        self.assertEqual(str(self.bigint_1234), '1234')
        self.assertEqual(str(self.bigint_odd1234), '-1234')
        self.assertEqual(str(self.bigint_555555), '555555')
        self.assertEqual(str(self.bigint_50505_11), '555555')
        self.assertEqual(str(self.bigint_odd555555), '-555555')

    def test_lt(self):
        self.assertEqual(self.bigint_1 < BigInteger('0'), False)
        self.assertEqual(self.bigint_1 < BigInteger('3'), True)
        self.assertEqual(self.bigint_555555 < BigInteger('220'), False)
        self.assertEqual(self.bigint_555555 < BigInteger('99995'), True)
        self.assertEqual(self.bigint_odd1234 < BigInteger('3'), True)
        self.assertEqual(self.bigint_odd1234 < self.bigint_odd555555, False)

    def test_le(self):
        self.assertEqual(self.bigint_1 <= BigInteger('-2'), False)
        self.assertEqual(self.bigint_1234 <= self.bigint_555555, True)

        self.assertEqual(self.bigint_odd555555 <= self.bigint_1234, True)
        self.assertEqual(self.bigint_555555 <= self.bigint_50505_11, True)

        self.assertEqual(self.bigint_odd555555 <= self.bigint_1, True)

    def test_gt(self):
        self.assertEqual(self.bigint_1 > BigInteger('-1'), True)
        self.assertEqual(self.bigint_1234 > self.bigint_odd1234, True)
        self.assertEqual(self.bigint_odd555555 > self.bigint_555555, False)
        self.assertEqual(self.bigint_1234 > self.bigint_555555, False)

    def test_ge(self):
        self.assertEqual(self.bigint_1 >= BigInteger('0'), True)
        self.assertEqual(self.bigint_1234 >= self.bigint_odd1234, True)
        self.assertEqual(self.bigint_odd1234 >= BigInteger('0'), False)
        self.assertEqual(self.bigint_555555 >= self.bigint_50505_11, True)

    def test_eq(self):
        self.assertEqual(self.bigint_1 == BigInteger('0'), False)
        self.assertEqual(self.bigint_1234 == self.bigint_555555, False)
        self.assertEqual(self.bigint_odd1234 == self.bigint_1234, False)
        self.assertEqual(self.bigint_50505_11 == self.bigint_555555, True)

    def test_ne(self):
        self.assertEqual(self.bigint_1 != BigInteger('0'), True)
        self.assertNotEqual(self.bigint_1 != BigInteger('0'), False)
        self.assertNotEqual(self.bigint_1234 != self.bigint_555555, False)
        self.assertNotEqual(self.bigint_odd1234 != self.bigint_1234, False)
        self.assertNotEqual(self.bigint_555555 != self.bigint_50505_11, True)

    def test_add(self):
        self.assertEqual(self.bigint_1234 + self.bigint_1, BigInteger('1235'))
        self.assertEqual(self.bigint_1 + BigInteger('0'), BigInteger('1'))
        self.assertEqual(str(self.bigint_555555 + self.bigint_1234), '556789')
        self.assertEqual(self.bigint_odd1234 + self.bigint_1234, BigInteger('0'))
        self.assertEqual(self.bigint_odd1234 + self.bigint_555555, BigInteger('554321'))

    def test_sub(self):
        self.assertEqual(self.bigint_1234 - self.bigint_1, BigInteger('1233'))
        self.assertEqual(self.bigint_1 - self.bigint_1234, BigInteger('-1233'))
        self.assertEqual(self.bigint_555555 - self.bigint_1234, BigInteger('554321'))
        self.assertEqual(self.bigint_odd1234 - self.bigint_1234, BigInteger('-2468'))
        self.assertEqual(self.bigint_odd1234 - self.bigint_odd1234, BigInteger('0'))

    def test_mul(self):
        self.assertEqual(self.bigint_1234 * self.bigint_1, BigInteger('1234'))
        self.assertEqual(self.bigint_1 * BigInteger('0'), BigInteger('0'))
        self.assertEqual(self.bigint_50505_11 * self.bigint_1234, BigInteger('685554870'))
        self.assertEqual(self.bigint_odd1234 * self.bigint_1234, BigInteger('-1522756'))
        self.assertEqual(self.bigint_50505_11 * self.bigint_odd1234, BigInteger('-685554870'))

    def test_floordiv(self):
        self.assertEqual(self.bigint_1234 // self.bigint_1, BigInteger('1234'))
        self.assertEqual(self.bigint_1 // self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 // self.bigint_1234, BigInteger('0'))
        self.assertEqual(self.bigint_odd1234 // self.bigint_1234, BigInteger('-1'))
        with self.assertRaises(ZeroDivisionError):
            self.bigint_1 // BigInteger('0')

    def test_mod(self):
        self.assertEqual(self.bigint_1234 % self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 % self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 % self.bigint_1234, BigInteger('1'))
        self.assertEqual(self.bigint_555555 % self.bigint_1234, BigInteger('153'))
        self.assertEqual(self.bigint_odd1234 % self.bigint_1234, BigInteger('0'))

    def test_pow(self):
        self.assertEqual(self.bigint_1234 ** self.bigint_1, BigInteger('1234'))
        self.assertEqual(self.bigint_1 ** self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 ** self.bigint_1234, BigInteger('1'))
        self.assertEqual(self.bigint_555555 ** BigInteger('8'),
                         BigInteger('9074370031829775794654076990628972899875390625'))

    def test_xor(self):
        self.assertEqual(self.bigint_1234 ^ self.bigint_1, BigInteger('1235'))
        self.assertEqual(self.bigint_1 ^ self.bigint_1, BigInteger('0'))
        # self.assertEqual(self.bigint_1 ^ self.bigint_1234, BigInteger('1235'))
        self.assertEqual(self.bigint_555555 ^ self.bigint_1234, BigInteger('556785'))

    def test_rshift(self):
        self.assertEqual(self.bigint_1 >> self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 >> self.bigint_1234, BigInteger('0'))

    def test_lshift(self):
        self.assertEqual(self.bigint_1234 << self.bigint_1, BigInteger('2468'))
        self.assertEqual(self.bigint_1 << self.bigint_1, BigInteger('2'))
        self.assertEqual(self.bigint_1234 << BigInteger('3'), BigInteger('9872'))

    def test__to_bin(self):
        self.assertEqual(self.bigint_1._to_binary(), BigInteger('1'))
        self.assertEqual(self.bigint_1234._to_binary()._to_decimal(), BigInteger('1234'))

    def test_or(self):
        self.assertEqual(self.bigint_1234 | self.bigint_1, BigInteger('1235'))
        self.assertEqual(self.bigint_1 | self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 | self.bigint_1234, BigInteger('1235'))
        self.assertEqual(self.bigint_555555 | self.bigint_1234, BigInteger('556787'))

    def test_and(self):
        self.assertEqual(self.bigint_1234 & self.bigint_1, BigInteger('0'))
        self.assertEqual(self.bigint_1 & self.bigint_1, BigInteger('1'))
        self.assertEqual(self.bigint_1 & self.bigint_1234, BigInteger('0'))
        self.assertEqual(self.bigint_555555 & self.bigint_1234, BigInteger('2'))