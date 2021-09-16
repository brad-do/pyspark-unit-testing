#!/usr/bin/env python3
__author__ = 'brad'
"""
My PySpark client
"""

import sys
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import StructField, StructType, StringType
from pyspark.sql.functions import current_timestamp, input_file_name


spark = SparkSession.builder.appName('com.dadoverflow.mypysparkclient').getOrCreate()
log4jLogger = spark._jvm.org.apache.log4j
LOGGER = log4jLogger.LogManager.getLogger(__name__)


def parse_xml(xml_file):
    """Simple function using the Databricks Spark-XML API to parse XML documents into dataframes"""
    df = spark.read.format('com.databricks.spark.xml').\
        option('rootTag', 'catalog').\
        option('rowTag', 'book').load(xml_file)
    return df


def main(argv):
    LOGGER.info('Starting application')
    parse_xml(argv[0])
    LOGGER.info('Completing application')


if __name__ == "__main__":
    main(sys.argv[1:])
