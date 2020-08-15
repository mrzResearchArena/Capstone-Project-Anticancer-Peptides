# Python-based-Flask-Framework-website-with-Machine-Learning-Model
Back-end  python, Front-end HTML, CSS, JavaScript, Bootstrap. Framework : Flask. Runs Machine learning model with great visual of ouput.

### Installation Process :
    Install Flask: 
    user@machine:~$ pip install flask
    
    Required Python Packages:
    
    Install: python (version >= 3.5)
    Install: sklearn (version >= 0.19.0)
    Install: numpy (version >= 1.13.0)
    Install: pandas (version >= 0.21.0)
    Install: matplotlib (version >= 2.1.0)
    Install: pickle

    pip install < package name >
    example: pip install sklearn

    or
    We can download from anaconda cloud.


### Code Description :
- **Features Extraction :**
  ```console
  user@machine:~$ python extractionFeatures.py
  ```
  Note #1: It will provide a dataset named **fullDataset.csv** from FASTA sequences.
  ([fullDataset.csv](https://drive.google.com/file/d/1-DHKnHMcVDZATUYZ8BwQzdLUAWQJRxyg/))

  Note #2: **readXY.py** ( This file will fetch data from **hotSpot.fasta** and **coldSpot.fasta** files. )


- **Features Selection :**
  ```console
  user@machine:~$ python selectionFeatures.py
  ```
  Note #1: It will provide a dataset named **selectedDataset.csv** from **fullDataset.csv**.


- **Training Model :**
  ``` console
  user@machine:~$ python modelDump
