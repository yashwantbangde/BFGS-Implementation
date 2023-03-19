import streamlit as st
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define the function to optimize
def f(x):
    return x[0]**2 + x[1]**2 + 2 * np.sin(x[0]) * np.sin(x[1])

# Define the gradient of the function
def gradient(f, x, h=1e-6):
    n = len(x)
    grad = np.zeros(n)
    for i in range(n):
        xh = np.copy(x)
        xh[i] += h
        grad[i] = (f(xh) - f(x)) / h
    return grad

# Define the BFGS optimizer function
def bfgs(f, x0, max_iter=100, tol=1e-6):
    n = len(x0)
    Bk = np.eye(n)
    xk = x0
    gk = gradient(f, xk)
    k = 0
    xs = [x0]
    while k < max_iter and np.linalg.norm(gk) > tol:
        pk = -np.dot(Bk, gk)
        alpha = line_search(f, xk, pk)
        xkp1 = xk + alpha * pk
        gkp1 = gradient(f, xkp1)
        sk = xkp1 - xk
        yk = gkp1 - gk
        rho_k = 1 / np.dot(yk, sk)
        A_k = np.eye(n) - rho_k * np.outer(sk, yk)
        Bk = np.dot(A_k, np.dot(Bk, A_k.T)) + rho_k * np.outer(sk, sk)
        xk = xkp1
        gk = gkp1
        k += 1
        xs.append(xk)
    return xk, np.array(xs)

# Define the line search function
def line_search(f, xk, pk):
    alpha = 1.0
    rho = 0.5
    c = 1e-4
    fk = f(xk)
    gk = np.dot(gradient(f, xk), pk)
    while f(xk + alpha * pk) > fk + c * alpha * gk:
        alpha *= rho
    return alpha

# Define the function to plot the convergence
def plot_convergence(xs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = xs[:, 0]
    y = xs[:, 1]
    z = [f(xi) for xi in xs]
    ax.plot(x, y, z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x,y)')
    st.pyplot(fig)

# Define the Streamlit app
st.title('BFGS Optimizer')
st.sidebar.title('Input Variables')
x0 = np.array([st.sidebar.slider('x0', -10.0, 10.0, 1.0), st.sidebar.slider('x1', -10.0, 10.0, 1.0)])
max_iter = st.sidebar.slider('Max Iterations', 10, 1000, 100)
tol = st.sidebar.slider('Tolerance', 1e-8, 1e-3, 1e-6)
st.write('### Input Variables')
st.write('Initial Guess:', x0)
st.write('Max Iterations:', max_iter)
st.write('Tolerance:', tol)

# Call the BFGS optimizer
x_opt, xs = bfgs(f, x0, max_iter=max_iter, tol=tol)

# Print the optimal solution
st.write('### Results')
st.write('Optimal Solution:', x_opt)

# Plot the convergence
plot_convergence(xs)
