#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Basic import test to ensure the package can be imported correctly.
"""

def test_import_ccda():
    """Test that CCDA can be imported from the package."""
    try:
        from pyCCDA import CCDA
        assert CCDA is not None
    except ImportError as e:
        assert False, f"Failed to import CCDA from pyCCDA: {e}"

def test_import_bluebutton():
    """Test that BlueButton can be imported from the package."""
    try:
        from pyCCDA import BlueButton
        assert BlueButton is not None
    except ImportError as e:
        assert False, f"Failed to import BlueButton from pyCCDA: {e}"

def test_ccda_equals_bluebutton():
    """Test that CCDA and BlueButton are the same class."""
    from pyCCDA import CCDA, BlueButton
    assert CCDA is BlueButton, "CCDA should be the same class as BlueButton" 