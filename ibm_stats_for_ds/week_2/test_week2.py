"""Module for Testing and Executing Week 2 code"""
import pytest

import week2 as MUT


@pytest.mark.dev_test
def test_main():
    """Wrapper for executing main"""
    MUT.main()
