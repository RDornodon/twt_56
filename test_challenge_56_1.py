from itertools import zip_longest
from pprint import pprint
import sys
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from test_cases_ch_56_1 import test_inp, test_out


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


@mock.patch('builtins.input', side_effect=["1011"] + test_inp)
def test_challenge_56_1(input: Callable) -> None:
    
    with Capturing() as output:
        start = perf_counter()
    
        import twt_56_1_roll  # change name to your file with solution name without extension
        
        end = perf_counter()
        
    passed = i = ii = oi = 0
    for i in range(1, 1012):
        c = int(test_inp[ii].split()[0])
        inp = test_inp[ii: ii + c + 1]
        out, exp = output[oi:oi + c], test_out[oi:oi + c]
        ii += c + 1
        oi += c
        if out != exp:
            print(f'Test nr:{i}\n    inp:')
            pprint(inp)
            print('Your output:')
            pprint(out)
            print('expected:')
            pprint(exp)
        else:
            passed += 1

    print(f"Passed: {passed}/{i} tests")
    print(f"Finished in: {end - start} seconds")


if __name__ == "__main__":
    test_challenge_56_1()

