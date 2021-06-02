from itertools import zip_longest
import sys
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from test_cases_ch_56_2 import test_inp, test_out


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


@mock.patch('builtins.input', side_effect=["1000"] + test_inp)
def test_challenge_56_2(input: Callable) -> None:
    
    with Capturing() as output:
        start = perf_counter()
    
        import challenge_56_2  # change name to your file with solution name without extension
        
        end = perf_counter()
        
    passed = i = ii = 0
    for i, (out, exp) in enumerate(zip_longest(output, test_out), 1):
        c = int(test_inp[ii])
        inp = test_inp[ii: ii + c + 1]
        ii += c + 1
        if out != exp:
            print(f'Test nr:{i}\n    inp1: "{inp}"')
            print(f'    Your output: "{out}", expected: "{exp}"\n')
        else:
            passed += 1

    print(f"Passed: {passed}/{i} tests")
    print(f"Finished in: {end - start} seconds")


if __name__ == "__main__":
    test_challenge_56_2()
