# from dataset import Dataset
import dataset
import sys, os

class Read:

   global verbose
   global fileRange
   global skipFiles
   global dataSets # List of dataset objects, each representing the data from one input file (corresponding to one set of excel data)


   def __init__(self):
      verbose = False
      fileRange = [1, 6]
      skipFiles = []
      dataSets = []
      for i in range(fileRange[0], fileRange[1]+1):
         if i in skipFiles:
            continue
         dir = os.path.dirname(sys.argv[0])
         # print "DIR", dir
         filePath =  os.path.join(dir, "../../data/FormattedDataFiles/T"+str(i)+".txt")
         dataSets.append(self.readFile(filePath)) # Read and store data as Dataset object
         for d in dataSets:
            print "-----------------------TITLES:", d.getTitles()
            print d.toString(),"\n"

   
   def readFile(self, filePath):
      f = open(filePath,'r')
      title = ""
      subtitle = ""
      columnRange = ""
      dataDictionary = {}
      line = f.readline()

      if "<TITLE>" in line:
         line = f.readline() 
         while not "<SUBTITLE>" in line:
            title += line
            line = f.readline()

      if "<SUBTITLE>" in line:
         line = f.readline() 
         while not "<EXCEL COLUMN RANGE>" in line:
            subtitle += line
            line = f.readline()

      if "<EXCEL COLUMN RANGE>" in line:
         line = f.readline() 
         while not "<VECTOR LABELS>" in line:
            columnRange+=line
            line = f.readline()

      labels = []
      if "<VECTOR LABELS>" in line:
         line = f.readline()
         while not "<DATA>" in line:
            labels.append(line)
            line = f.readline()

      labelIndex = 0

      if "<DATA>" in line:
         line = f.readline()
         while not line == "":
            line = line.strip()
            lineSplit = line.split("\t")
            dataVector = []
            for s in lineSplit:
               dataVector.append(self.parseNumber(s))
            dataDictionary[labels[labelIndex]]=dataVector
            labelIndex+=1
            line = f.readline()

      if not (len(dataDictionary)==len(labels)):
         print "ERROR 1"

      # Finally, make Dataset object
      return dataset.Dataset(title, subtitle, columnRange, dataDictionary)


   def parseNumber(self, s):
      number = 0
      try:
         number = float(s)
         return number
      except:
         try: # Try removing a comma
            number = float(s.replace(",",""))
            return number
         except:
            return -1.0

   def getDataSets(self):
      return self.dataSets