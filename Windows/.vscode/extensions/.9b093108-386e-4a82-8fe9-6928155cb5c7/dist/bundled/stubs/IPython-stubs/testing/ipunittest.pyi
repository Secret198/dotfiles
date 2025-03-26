"""
This type stub file was generated by pyright.
"""

import unittest

"""Experimental code for cleaner support of IPython syntax with unittest.

In IPython up until 0.10, we've used very hacked up nose machinery for running
tests with IPython special syntax, and this has proved to be extremely slow.
This module provides decorators to try a different approach, stemming from a
conversation Brian and I (FP) had about this problem Sept/09.

The goal is to be able to easily write simple functions that can be seen by
unittest as tests, and ultimately for these to support doctests with full
IPython syntax.  Nose already offers this based on naming conventions and our
hackish plugins, but we are seeking to move away from nose dependencies if
possible.

This module follows a different approach, based on decorators.

- A decorator called @ipdoctest can mark any function as having a docstring
  that should be viewed as a doctest, but after syntax conversion.

Authors
-------

- Fernando Perez <Fernando.Perez@berkeley.edu>
"""
def count_failures(runner):
    """Count number of failures in a doctest runner.

    Code modeled after the summarize() method in doctest.
    """
    ...

class IPython2PythonConverter:
    """Convert IPython 'syntax' to valid Python.

    Eventually this code may grow to be the full IPython syntax conversion
    implementation, but for now it only does prompt conversion."""
    def __init__(self) -> None:
        ...
    
    def __call__(self, ds):
        """Convert IPython prompts to python ones in a string."""
        ...
    


class Doc2UnitTester:
    """Class whose instances act as a decorator for docstring testing.

    In practice we're only likely to need one instance ever, made below (though
    no attempt is made at turning it into a singleton, there is no need for
    that).
    """
    def __init__(self, verbose=...) -> None:
        """New decorator.

        Parameters
        ----------

        verbose : boolean, optional (False)
          Passed to the doctest finder and runner to control verbosity.
        """
        ...
    
    def __call__(self, func): # -> Type[Tester]:
        """Use as a decorator: doctest a function's docstring as a unittest.
        
        This version runs normal doctests, but the idea is to make it later run
        ipython syntax instead."""
        class Tester(unittest.TestCase):
            ...
        
        
    


def ipdocstring(func):
    """Change the function docstring via ip2py.
    """
    ...

ipdoctest = ...
ip2py = ...
