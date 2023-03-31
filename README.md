# BFGS Optimization Algorithm Implementation from scratch
BFGS stands for Broyden–Fletcher–Goldfarb–Shanno, which is a quasi-Newton optimization algorithm used to find the minimum of a function. It is an iterative algorithm that belongs to the family of quasi-Newton methods, which are a class of optimization methods that use an approximation of the Hessian matrix of the objective function.

The BFGS algorithm approximates the Hessian matrix using information from the gradient of the objective function. It updates the approximation of the Hessian matrix in each iteration and uses it to determine the search direction. The algorithm also performs a line search to find the step size that minimizes the objective function along the search direction.

First, we define the quadratic function quadratic_function and its gradient gradient_quadratic_function. These functions will be used by the BFGS algorithm to optimize the function.

Next, we define the BFGS algorithm itself in the function bfgs. The algorithm takes four arguments: the quadratic function to be optimized, its gradient, the starting point x0, and two optional parameters epsilon and max_iterations. The algorithm uses the BFGS update formula to update the Hessian approximation H at each iteration, and solves for the descent direction d using the updated Hessian and gradient. The algorithm then performs a line search to determine the step size alpha along the descent direction. If the step size is too large and results in an increase in the function value, the algorithm reduces the step size by a factor of 0.5 and repeats the line search. Once a suitable step size is found, the algorithm updates the current point x and gradient g, and continues to the next iteration. The algorithm terminates when the norm of the gradient falls below the epsilon threshold or the maximum number of iterations is reached.

Finally, we define the function plot_quadratic_function to create a 3D plot of the quadratic function using Matplotlib. This function is called by the Streamlit app to display the plot to the user.

In the main block of the code, we set the starting point x0 and use the BFGS algorithm to find the minimum of the quadratic function. We then print the minimum and its location to the console, and call the plot_quadratic_function function to display the 3D plot in the Streamlit app.
