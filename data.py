#install module pip install -U scikit-learn
# sudo apt-get install python-scipy
# pip install scipy

from sklearn import tree

#Created a variable X that contains[height, weight, shoe size]
X = [[181, 80, 44], [177,70,43], [160,60,38], [154, 54, 37], [175,64,39], [177,70,40],
    [159,55, 33], [166,65,40],[190,90,47], [175,64,39],[177,70,40]]

#Created a variable Y that contains [male and female]
Y = ['male', 'female', 'female', 'female','male', 'female','male', 'female','male',
 'female', 'male']

#create a classify vairiable
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)


prediction = clf.predict([[190,70,43]])

#print the variable prediction
print prediction

#To test the application open the terminal and python data.py
