### SETTING UP ENVIRONMENT (macOS)

We will be using following as our development environment:
- Anaconda Python 3
- Tensorflow
- Apache Spark 2.1.0
- Pycharm 2017.1

## Installing Python
## -----------------
1) Download Anaconda python from
   https://repo.continuum.io/archive/Anaconda3-4.3.1-MacOSX-x86_64.pkg

   OR
   get the latest version from
   https://www.continuum.io/DOWNLOADS

2) Install using above downloaded package

## Installing Tensorflow (CPU only)
## --------------------------------
1) Create a conda environment named tensorflow by invoking the following command:

   $ conda create -n tensorflow python=3.5

2) Activate the conda environment by issuing the following command:

   $ source activate tensorflow
   (tensorflow)$  # Your prompt should change

3) Issue a command of the following format to install TensorFlow inside your conda environment:

   (tensorflow)$ pip install --ignore-installed --upgrade $TF_PYTHON_URL

   where TF_PYTHON_URL is the URL of the TensorFlow Python package.

   we are using :
   https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl

## Installing Spark
## ----------------

NOTE : Spark requires python and java be installed already

1) Download Spark 2.1.0 from
   http://spark.apache.org/downloads.html

2) untar the downloaded file as :

   $ tar -xzvf spark-2.1.0-bin-hadoop2.7.tgz

3) I generally keep all binaries art /usr/local

   $ mv spark-2.1.0-bin-hadoop2.7 /usr/local/spark

4) Setup SPARK_HOME and PATH environment variables in .bash_profile

   export SPARK_HOME=/usr/local/spark
   export PATH=$PATH:$SPARK_HOME/bin

##_____________________________________________________________________________

Now that we have everything installing we will set up Pycharm with Pyspark

1) We will use python from conda environment we created while installing
   tensorflow as project interpreter in Pycharm.

2) Project interpreter can be set at :

   preferences-->project-->project interpreter

3) Next we will enable Pycharm to be able to read py4j, so that we can "import pyspark"

   For the project interpreter above add following interpreter paths:

   /usr/local/spark/python
   /usr/local/spark/python/lib/py4j-0.10.4-src.zip

##_____________________________________________________________________________

THIS BRINGS US TO THE END OF SETTING UP THE ENVIRONMENT !!
