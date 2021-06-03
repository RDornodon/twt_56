from itertools import zip_longest
import sys
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO

sample_input = ("6\n"
                "0 0\n"
                "4 6\n"
                "1 2 q w 3 4\n"
                "4 5 e r 6 7\n"
                "7 8 t z 9 0\n"
                "a b u i c d\n"
                "1 5\n"
                "1 2 3 4 5\n"
                "5 1\n"
                "1\n"
                "2\n"
                "3\n"
                "4\n"
                "5\n"
                "3 7\n"
                "q w e r t z u\n"
                "a 1 2 3 4 5 j\n"
                "y x c v b n m\n"
                "7 3\n"
                "q w e\n"
                "r 1 t\n"
                "z 2 u\n"
                "i 3 o\n"
                "a 4 s\n"
                "d 5 f\n"
                "g h j").splitlines()

test_out = ("\n"
            "4 1 2 q w 3\n"
            "7 e r 6 9 4\n"
            "a 5 8 t z 7\n"
            "b u i c d 0\n"
            "5 1 2 3 4\n"
            "5\n"
            "1\n"
            "2\n"
            "3\n"
            "4\n"
            "a q w e r t z\n"
            "y 2 3 4 5 1 u\n"
            "x c v b n m j\n"
            "r q w\n"
            "z 2 e\n"
            "i 3 t\n"
            "a 4 u\n"
            "d 5 o\n"
            "g 1 s\n"
            "h j f").splitlines()

class Capturing(list):
  def __enter__(self):
    self._stdout = sys.stdout
    sys.stdout = self._stringio = StringIO()
    return self

  def __exit__(self, *args):
    self.extend(self._stringio.getvalue().splitlines())
    del self._stringio  # free up some memory
    sys.stdout = self._stdout


@mock.patch('builtins.input', side_effect=sample_input)
def test_challenge_55_2(input: Callable) -> None:
  with Capturing() as output:
    start = perf_counter()

    import twt_56_1  # change name to your file with solution name without extension

    end = perf_counter()

  passed = i = 0
  for i, (out, exp) in enumerate(zip_longest(output, test_out), 1):
    if out != exp:
      print(f'Test nr:{i}\n    inp1: ')
      print(f'    Your output: "{out}", expected: "{exp}"\n')
    else:
      passed += 1

  print(f"Passed: {passed}/{i} tests")
  print(f"Finished in: {end - start} seconds")


if __name__ == "__main__":
  test_challenge_55_2()