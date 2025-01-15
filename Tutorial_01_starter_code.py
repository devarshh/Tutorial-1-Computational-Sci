import numpy as np
import matplotlib.pyplot as plt
from bisection import *
from dist import *

# Define a function witha root where the horizontal distanc equals R.
def F(theta):
    return dist(theta, c, g, v0) - R

v0 = 100
c = 0.01
g = 9.81
R = 85
eps_x = 1e-6    # The maximal error is stated in the assignment!
eps_f = 1e-6
kMax = 100
# First task: solution(s) for R=85.0 (m).
theta, err1, res1, conv1 = bis(F, 0, np.pi/4, eps_x, eps_f, kMax)
if conv1:
    print("First solution: R=%f, theta=%f +/- %f." % (R,theta,err1))
else:
    print("Bisection did not converge!")
theta2, err2, res2, conv2 = bis(F, 0, np.pi/4, eps_x, eps_f, kMax)
if conv2:
    print("Second solution: R=%f, theta=%f +/- %f." % (R,theta,err2))
else:
    print("Bisection did not converge!")

# Second task: find solutions in a range of values for R and plot the solution vs. R.
# First, let us get an impression of the maximal value of R:
angles = np.linspace(0,np.pi/2,100)
dists = dist(angles,c,g,v0)
plt.plot(angles,dists,'-*')
plt.xlabel('angle')
plt.ylabel('distance travelled')
plt.show()
# It seems the maximal reach is about 201(m). Let's try to automatically find the angles:
RMax =   201
nPoints = 50 # Compute nPoints solutions on each "branch" (low and fast vs. high and looping).
split = np.pi/4 # By the eye, this is the angle that separates the branches.
Rs = np.linspace(0,RMax,nPoints)
# Complete two loops, one for each branch. For the first run, the initial interval is [0,split],
# for the second it is [split,pi/2].
result = [[0,0]]
for i in range(1,nPoints):
    R = Rs[i] # Note, that R is a global variable in this script.
    theta, err, res, conv = bis(F, 0, split, eps_x, eps_f, kMax)
    if conv:
        result.append([R, theta])
    else:
        print("Bisection did not converge for R=%f." % (R))
for i in range(nPoints-1,0,-1):
    R = Rs[i]
    theta, err, res, conv = bis(F, split, np.pi/2, eps_x, eps_f, kMax)
    if conv:
        result.append([R,theta])
    else:
        print("Bisection did not converge for R=%f." % (R))
result = np.array(result)
plt.plot(result[:,0],result[:,1],'-*')
plt.show()
# As you can see, there is an issue near the maximal value of R. Can you explain why?
