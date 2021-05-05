# run using this command:
"""
spark-submit \
    --master yarn\
    --deploy-mode client\
    pyspark/count_glass.py
"""

if __name__ == '__main__':
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .master("local") \
        .appName("Word Count") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    df_glass = spark.read\
        .option("header", "true")\
        .csv("file:///root/lab/datasets/retail-data/all/online-retail-dataset.csv")\
        .repartition(2)\
        .selectExpr("instr(Description, 'GLASS') >= 1 as is_glass")\
        .groupBy("is_glass")\
        .count()

    df_glass.write\
        .format('csv')\
        .option('mode', 'overwrite')\
        .save('file:///root/lab/outputs/count_glass')
