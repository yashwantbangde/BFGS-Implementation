# BFGS Optimization Algorithm Implementation from scratch
BFGS stands for Broyden–Fletcher–Goldfarb–Shanno, which is a quasi-Newton optimization algorithm used to find the minimum of a function. It is an iterative algorithm that belongs to the family of quasi-Newton methods, which are a class of optimization methods that use an approximation of the Hessian matrix of the objective function.

The BFGS algorithm approximates the Hessian matrix using information from the gradient of the objective function. It updates the approximation of the Hessian matrix in each iteration and uses it to determine the search direction. The algorithm also performs a line search to find the step size that minimizes the objective function along the search direction.

The BFGS algorithm is a quasi-Newton method for optimizing a function. It is an iterative algorithm that starts with an initial guess for the minimum and then updates the guess using the gradient of the function and an estimate of the inverse Hessian matrix. Here are the steps of the BFGS algorithm:

1. Choose an initial guess for the minimum, x0.
2 .Compute the gradient of the function at x0, g0.
3. Initialize the Hessian approximation to the identity matrix, H0 = I.
4. For each iteration k:
a. Compute the search direction, d_k = -H_k^(-1) * g_k.
b. Compute the step size alpha_k that minimizes f(x_k + alpha_k * d_k).
c. Update the guess for the minimum: x_{k+1} = x_k + alpha_k * d_k.
d. Compute the new gradient, g_{k+1}.
e. Compute y_k = g_{k+1} - g_k and s_k = x_{k+1} - x_k.
f. Update the Hessian approximation using the BFGS update formula:
H_{k+1} = H_k + (y_k y_k^T) / (y_k^T s_k) - (H_k s_k s_k^T H_k) / (s_k^T H_k s_k).
g. Check for convergence: if ||g_{k+1}|| < epsilon, stop iterating.
5. Output the final guess for the minimum, x_{k+1}.
