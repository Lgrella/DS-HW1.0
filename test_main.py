"""
Created on Tue Sep 19 2023
@author: lillygrella
"""
import unittest
import pandas as pd

class TestMain(unittest.TestCase):
    """
    evoke unit testing to confirm readin and sumstats work correctly
    """

    def test_readin(self):
        """
        test that the readin function correctly populates df as a pd.dataframe datatype
        """
        diabetes = pd.read_csv("diabetes.csv")
        self.assertIsNotNone(diabetes)
        self.assertIsInstance(diabetes, pd.DataFrame)

# Run the tests
if __name__ == "__main__":
    unittest.main()