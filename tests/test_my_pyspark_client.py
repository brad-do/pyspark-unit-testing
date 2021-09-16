#!/usr/bin/env python3
__author__ = 'brad'
"""
Class to test PySpark client
"""

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import pytest
from pyspark.sql import SparkSession
import my_pyspark_client as mpc

spark = SparkSession.builder.appName('com.dadoverflow.mypysparkclient.tests').getOrCreate()

def test_parse_xml():
    test_file = './tests/test.xml'
    test_df = mpc.parse_xml(test_file)
    
    assert test_df is not None, 'Expected a dataframe of data to be returned from function'
    assert test_df.count() == 12, 'Received unexpected count from test data'
    assert len(test_df.columns) == 7, 'Expected 7 columns in the test data'

def test_something_else():
    # some other test
    assert True
