# BFGS Optimization Algorithm Implementation from scratch
BFGS stands for Broyden–Fletcher–Goldfarb–Shanno, which is a quasi-Newton optimization algorithm used to find the minimum of a function. It is an iterative algorithm that belongs to the family of quasi-Newton methods, which are a class of optimization methods that use an approximation of the Hessian matrix of the objective function.

The BFGS algorithm approximates the Hessian matrix using information from the gradient of the objective function. It updates the approximation of the Hessian matrix in each iteration and uses it to determine the search direction. The algorithm also performs a line search to find the step size that minimizes the objective function along the search direction.

The Flow of the Algorithm code :
1. The necessary packages are imported: streamlit, numpy, mpl_toolkits.mplot3d, and matplotlib.pyplot.
2. A function f(x) is defined to be optimized.
3. A function gradient(f, x, h) is defined to calculate the gradient of the function f(x) using the central difference method.
4. A function bfgs(f, x0, max_iter, tol) is defined to optimize the function f(x) using the Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm. This function takes the function to be optimized f(x), the initial guess x0, the maximum number of iterations max_iter, and the tolerance tol.
5. A function line_search(f, xk, pk) is defined to perform the line search during each iteration of the BFGS algorithm.
6. A function plot_convergence(xs) is defined to plot the convergence of the BFGS algorithm.
7. A Streamlit app is created with a title and a sidebar to input variables.
8. The initial guess x0, maximum number of iterations max_iter, and tolerance tol are obtained from the sidebar input.
9. The BFGS optimizer function bfgs(f, x0, max_iter, tol) is called with the obtained input variables to obtain the optimal solution x_opt and the sequence of points xs.
10. The optimal solution x_opt is displayed on the app.
11. The sequence of points xs is plotted to show the convergence of the BFGS algorithm.
