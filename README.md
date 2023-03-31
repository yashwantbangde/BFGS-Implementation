# BFGS Optimization Algorithm Implementation from scratch
BFGS stands for Broyden–Fletcher–Goldfarb–Shanno, which is a quasi-Newton optimization algorithm used to find the minimum of a function. It is an iterative algorithm that belongs to the family of quasi-Newton methods, which are a class of optimization methods that use an approximation of the Hessian matrix of the objective function.

The BFGS algorithm approximates the Hessian matrix using information from the gradient of the objective function. It updates the approximation of the Hessian matrix in each iteration and uses it to determine the search direction. The algorithm also performs a line search to find the step size that minimizes the objective function along the search direction.

