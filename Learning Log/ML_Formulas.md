# ML Cheat Sheet - Key Formulas

## 1. Linear Regression
- **Hypothesis**: \( h_\theta(x) = \theta_0 + \theta_1 x \)
- **Cost Function (MSE)**:  
  

\[
  J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
  \]



## 2. Logistic Regression
- **Sigmoid Function**:  
  

\[
  \sigma(z) = \frac{1}{1 + e^{-z}}
  \]


- **Hypothesis**: \( h_\theta(x) = \sigma(\theta^T x) \)
- **Cost Function**:  
  

\[
  J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log h_\theta(x^{(i)}) + (1-y^{(i)}) \log (1-h_\theta(x^{(i)})) \Big]
  \]



## 3. Gradient Descent
- **Update Rule**:  
  

\[
  \theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
  \]


- Where \( \alpha \) = learning rate.

## 4. K-Means Clustering
- **Objective**: Minimize within-cluster variance:  
  

\[
  J = \sum_{k=1}^{K} \sum_{i \in C_k} \| x^{(i)} - \mu_k \|^2
  \]


- Iteratively update cluster centroids \( \mu_k \).

## 5. Neural Networks
- **Activation Functions**:
  - Sigmoid: \( \sigma(z) = \frac{1}{1+e^{-z}} \)
  - ReLU: \( f(z) = \max(0, z) \)
- **Forward Propagation**:  
  

\[
  a^{(l)} = f(W^{(l)} a^{(l-1)} + b^{(l)})
  \]

# Supervised Learning
# Linear Regression

## 1. Error & Cost Functions
- **Error (single sample)**:  
  

\[
  e^{(i)} = h_\theta(x^{(i)}) - y^{(i)}
  \]



- **Mean Squared Error (MSE)**:  
  

\[
  J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \big(h_\theta(x^{(i)}) - y^{(i)}\big)^2
  \]



- **Cross-Entropy Loss (Classification)**:  
  

\[
  J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log h_\theta(x^{(i)}) + (1-y^{(i)}) \log (1-h_\theta(x^{(i)})) \Big]
  \]



---

## 2. Gradient Descent
- **Update Rule**:  
  

\[
  \theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
  \]



- Where:
  - \( \alpha \) = learning rate  
  - \( J(\theta) \) = cost function  
  - \( \theta_j \) = parameter being updated  

---

## 3. Convergence Theorem (Gradient Descent)
- If the cost function \( J(\theta) \) is **convex** and differentiable, gradient descent is guaranteed to converge to the **global minimum
