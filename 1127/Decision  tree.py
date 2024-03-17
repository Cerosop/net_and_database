from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
tree.plot_tree(clf) 
print (clf.predict([[2., 2.], [0., 0.], [-2., -2.]]))
