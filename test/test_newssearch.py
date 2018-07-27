import unittest
from newssearch.newssearch import newssearch

class testNS(unittest.TestCase):

    def setUp(self):
        with open('./test/data/hscic-news.txt') as f:
            self._content = f.readlines()
            self._ns = newssearch(self._content)

    def test_orquery(self):
        self.assertEqual(
            self._ns.orquery('Care Quality Commission'),
            {0,1,2,3,4,5,6}
        )
        self.assertEqual(
            self._ns.orquery('September 2004'),
            {9}
        )
        self.assertEqual(
            self._ns.orquery('general population generally'),
            {6,8}
        )

    def test_orquerybadinput(self):
        self.assertEqual(
            self._ns.orquery('Care Quality Commission September3'),
            {0,1,2,3,4,5,6}
        )
        self.assertEqual(
            self._ns.orquery('September 2004 Commission4'),
            {9}
        )
        self.assertEqual(
            self._ns.orquery('general population generally generally2'),
            {6,8}
        )

    def test_andquery(self):
        self.assertEqual(
            self._ns.andquery('Care Quality Commission admission'),
            {1}
        )
        self.assertEqual(
            self._ns.andquery('general population Alzheimer'),
            {6}
        )

    def test_andquerybadinput(self):
        self.assertEqual(
            self._ns.andquery('Care Quality Commission admission4'),
            set()
        )
        self.assertEqual(
            self._ns.andquery('general population Alzheimer1'),
            set()
        )


if __name__ == '__main__':
    unittest.main()
