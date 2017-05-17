import sys
from common_string_build import longestSubstringFinder


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(longestSubstringFinder("apple pie available", "apple pies"))
    
