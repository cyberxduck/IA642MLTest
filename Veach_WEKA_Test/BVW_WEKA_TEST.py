#Imports the WEKA tools used bellow
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier

#Starts the JVM with an allocated 512 megabytes of ram
jvm.start(max_heap_size="512m")

#Lists where the working data directory is, change this to reflect your working path
data_dir = "C:\\Users\\Credu\Desktop\\School\\DataProject\\Processed_CSV\\"

#Establishes the file loader from WEKA, currently targeting ARFF files    
loader = Loader(classname="weka.core.converters.ArffLoader")
iris_inc = loader.load_file(data_dir + "iris.arff", incremental=True)
iris_inc.class_is_last()

#Outputs the data inside the ARFF
print(iris_inc)

#Builds the naiveBayes model
cls = Classifier(classname="weka.classifiers.bayes.NaiveBayesUpdateable")
cls.build_classifier(iris_inc)

#Outputs Model
print(cls)

#Turns off JVM
jvm.stop()
