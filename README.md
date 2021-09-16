### Overview
I write a fair amount of Spark applications that run on Hadoop platforms and do lots of data parsing, transformation, and loading to HDFS, Hive, or other data repositories.  When I code my applications in Scala, I usually use Eclipse and the [ScalaTest framework](https://www.scalatest.org/user_guide/using_scalatest_with_eclipse) to test my work.  

However, I like to write PySpark solutions, too, but haven't found a great way to test my solutions in an editor like [VS Code](https://code.visualstudio.com/).  Recently, though, it occurred to me that maybe I could just test my code in a ready-made Hadoop environment, like a Docker image for Hadoop.  This project is a simple starter app for developing a PySpark application that you can easily test in a Docker container running Spark.

### Setup
#### Set up a local, virtual environment
To keep this project nice and isolated from my other Python projects, I like to setup a virtual environment for it.
1. In my WSL2 command shell, navigate to my development folder: cd /mnt/c/Users/brad/dev
1. Create a directory for my project: mkdir ./pyspark-unit-testing
1. Enter the new project folder: cd pyspark-unit-testing
1. Create a subdir for my tests: mkdir ./tests
1. Create my virtual environment (note: I initially had some issues doing this in WSL2 and found [this blog post](https://newbedev.com/installing-venv-for-python3-in-wsl-ubuntu) helpful in overcoming them): python3 -m venv app-env
1. Start the new virtual environment: source app-env/bin/activate
1. Install the [pytest package](https://docs.pytest.org/en/6.2.x/): pip3 install pytest --trusted-host `pypi.org` --trusted-host `files.pythonhosted.org`
1. (Optional) Create a requirements doc of your development environment: pip3 freeze -> requirements-dev.txt
1. Leave the virtual environment: deactivate
1. Now, fire up VS Code: code .

#### The Databricks Spark-XML dependency
As an added bonus, this project demonstrates how to code and test against third party APIs.  In this case, I'm leveraging [Databricks' Spark-XML API](https://github.com/databricks/spark-xml).  For simplicity, I just downloaded the JAR file directly into my project from [its Maven repository](https://mvnrepository.com/artifact/com.databricks/spark-xml_2.11/0.11.0).

#### Set up the Docker container
For most of my Spark needs, I like to use the [Jupyter "all-spark-notebook" image](https://hub.docker.com/r/jupyter/all-spark-notebook).
1. Download the image (I like to use the "spark-2" version, but I'm sure the latest will work just fine, too): docker pull /jupyter/all-spark-notebook:spark-2
1. Use my Dockerfile to build my own image: docker build -t my_spark_image:v1 .

### Running the Docker container and testing
When I start my Docker container, I like to include several commands that are not necessary for unit testing but helpful with other uses of the container like its Jupyter Notebook capabilities.  Here's the command I normally use:
```
docker run -d -p 9000:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v /mnt/c/Users/brad/dev/pyspark-unit-testing:/home/jovyan/work my_spark_image:v1
```

Next, open a bash shell into your container: docker exec -it <container pid> bash

Finally, run your pytest unit tests with this command:
```
pytest tests/ -s --disable-pytest-warnings
```

As an aside, if you're interested in the container's Jupyter Notebook capabilities, this command is helpful: jupyter notebook list