# test_xstatemanager.py
"""
Tests for XStateManager module.
"""

import unittest
from xstatemanager import XStateManager

class TestXStateManager(unittest.TestCase):
    """Test cases for XStateManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XStateManager()
        self.assertIsInstance(instance, XStateManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XStateManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
