#Imports the WEKA tools used bellow
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import PredictionOutput, KernelClassifier, Kernel
from weka.classifiers import Evaluation
from weka.core.classes import Random
from weka.classifiers import FilteredClassifier
from weka.filters import Filter
from weka.classifiers import Classifier

#Starts the JVM with an allocated 512 megabytes of ram
jvm.start(max_heap_size="512m")


#Establishes the file loader from WEKA, currently targeting CSV files    
loader = Loader(classname="weka.core.converters.CSVLoader")

#Load the data here
data = loader.load_file("logs/wekaPlz.csv")
data.class_is_last()

#Cleans the data for WEKA and processes it
remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-R", "1-3"])
cls = Classifier(classname="weka.classifiers.bayes.NaiveBayes")
fc = FilteredClassifier()
fc.filter = remove
fc.classifier = cls
evl = Evaluation(data)
evl.crossvalidate_model(fc, data, 10, Random(1))

#Displays WEKA's findings establishing the model
print(evl.percent_correct)
print(evl.summary())
print(evl.class_details())

#Load the new data

#Use's test datasets to see efficacy

#Turns off JVM
jvm.stop()

