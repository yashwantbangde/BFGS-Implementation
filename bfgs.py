import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


def quadratic_function(x):
    """Quadratic function to be optimized."""
    return x[0]**2 + 10*x[1]**2


def gradient_quadratic_function(x):
    """Gradient of the quadratic function."""
    return np.array([2*x[0], 20*x[1]])


def bfgs(quadratic_function, gradient_quadratic_function, x0, epsilon=1e-5, max_iterations=1000):
    """BFGS algorithm for minimizing a function."""
    x = x0
    H = np.identity(len(x0))
    g = gradient_quadratic_function(x)
    for i in range(max_iterations):
        d = -np.linalg.solve(H, g)
        alpha = 1
        while quadratic_function(x + alpha*d) > quadratic_function(x) + alpha*epsilon*np.dot(g, d):
            alpha *= 0.5
        x_new = x + alpha*d
        g_new = gradient_quadratic_function(x_new)
        y = g_new - g
        s = x_new - x
        H = H + np.outer(y, y)/np.dot(y, s) - np.outer(H@s, H@s)/np.dot(s, H@s)
        if np.linalg.norm(g_new) < epsilon:
            break
        x, g = x_new, g_new
    return x


def plot_quadratic_function():
    """Plot the quadratic function."""
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = quadratic_function([X, Y])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    st.pyplot(fig)


if __name__ == '__main__':
    x0 = np.array([2, 2])
    x_min = bfgs(quadratic_function, gradient_quadratic_function, x0)
    st.write(f"The minimum of the quadratic function is {quadratic_function(x_min)} at {x_min}.")
    plot_quadratic_function()
