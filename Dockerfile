# Dockerfile to build docker image used to test my PySpark client

# from https://hub.docker.com/r/jupyter/all-spark-notebook
FROM jupyter/all-spark-notebook:spark-2

WORKDIR /home/jovyan/work/

# from https://mvnrepository.com/artifact/com.databricks/spark-xml_2.11/0.11.0
COPY ./spark-xml_2.11-0.11.0.jar /usr/local/spark/jars/.
COPY ./requirements-dev.txt /home/jovyan/work/.
RUN pip install -r requirements-dev.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
