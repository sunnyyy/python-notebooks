error = "{0} not installed. Need help? Post to Piazza, talk to your classmates, or come to office hours."
success = "{0} is installed. Yay!"

try:
    import numpy
    print success.format('NumPy')
except:
    print error.format('NumPy')

try:
    import scipy
    print success.format('SciPy')
except:
    print error.format('SciPy')

try:
    import matplotlib
    print success.format('Matplotlib')
except:
    print error.format('Matplotlib')

try:
    import sklearn
    print success.format('Scikit-learn')
except:
    print error.format('Scikit-learn')


