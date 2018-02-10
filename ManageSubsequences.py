from difflib import SequenceMatcher
import unittest

class ManageSubsequence:
    def __init__(self):
        pass

    def minAdded(self, S, A, B):
        def min_added():
            stack = list()
            stack.append(S)
            memory = {S: 0}
            while stack:
                s = stack.pop()
                if A in s and B not in s:
                    yield memory[s]
                else:
                    match = SequenceMatcher(None, s, A).find_longest_match(0, len(s), 0, len(A))
                    match_index_A = match.b
                    match_index_s = match.a
                    match_len = match.size
                    if match_index_A != 0:
                        new_s = s[:match_index_s] + A[match_index_A-1] + s[match_index_s:]
                        if new_s not in memory:
                            memory[new_s] = memory[s] + 1
                    if match_index_A != len(A) - match_len:
                        new_s = s[:match_index_s + match_len] + A[match_index_A + match_len] + s[match_index_s + match_len:]
                        if new_s not in memory:
                            memory[new_s] = memory[s] + 1

        options = list(min_added())
        print(options)
        if options:
            return min(options)
        else:
            return -1

class MSTest(unittest.TestCase):
    def setUp(self):
        self.ms = ManageSubsequence()

    def test_min_added(self):
        self.assertEquals(2, self.ms.minAdded("ABXBCA", "ABCD", "XD"))
        self.assertEquals(2, self.ms.minAdded("BXC", "BOCZ", "DSFHDS"))
        self.assertEquals(-1, self.ms.minAdded("BXC", "BOCZ", "BZ"))
        self.assertEquals(3, self.ms.minAdded("ABC", "CDE", "ABCE"))
        self.assertEquals(-1, self.ms.minAdded("BANANA", "APPLE", "ANNA"))
        self.assertEquals(6, self.ms.minAdded("BANANA", "ANANAS", "BS"))
        self.assertEquals(3, self.ms.minAdded("BANANA", "ANANAS", "BNNS"))


if __name__ == "__main__":
    unittest.main()
