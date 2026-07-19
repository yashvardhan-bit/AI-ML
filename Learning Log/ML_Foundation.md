# Machine Learning Foundations

## 1. What is Machine Learning?
- Field of AI where systems learn patterns from data.
- Goal: improve performance on tasks without explicit programming.

## 2. Types of Learning
- **Supervised Learning**: Train with labeled data (e.g., regression, classification).
- **Unsupervised Learning**: Find hidden structure in unlabeled data (e.g., clustering, dimensionality reduction).
- **Reinforcement Learning**: Agent learns by interacting with environment and receiving rewards.

## 3. Key Concepts
- **Model**: Mathematical representation of a system (e.g., linear regression).
- **Training**: Process of fitting the model to data.
- **Loss Function**: Measures error between predictions and actual values.
- **Optimization**: Adjusting parameters to minimize loss (e.g., gradient descent).

## 4. Common Algorithms
- Linear Regression
- Logistic Regression
- Decision Trees
- K-Means Clustering
- Neural Networks

## 5. Applications
- Image recognition
- Natural language processing
- Recommendation systems
- Predictive analytics

# Learning Log - July 8, 2026

Today was all about digging deeper into ML foundations.  
I went beyond the basics and explored:

## Types of ML
- Supervised Learning: training with labeled data.
- Unsupervised Learning: finding hidden patterns.
- Reinforcement Learning: reward-driven learning.

## Supervised Learning Details
- Regression: predicting continuous values (like house prices).
- Classification: predicting discrete labels (spam vs. not spam).

## Errors & Cost Functions
- Error = difference between prediction and actual.
- Cost Function = average error across dataset (MSE, cross-entropy).

## Gradient Descent
- Iterative optimization to minimize cost.
- Learning rate controls step size.
- Convergence Theorem: guarantees reaching a minimum under certain conditions.

# 📘 Machine Learning Learning Log

This log tracks my progress and key takeaways while working on supervised and unsupervised ML projec

## 🔎 Supervised Learning
- **Minor Project** → Applied supervised ML on a small dataset.
- Key algorithms explored:
  - Linear Regression
  - Logistic Regression
  - Decision Trees
  - Random Forests
- **Learning Points:**
  - Importance of labeled data.
  - Evaluation using accuracy, precision, recall, F1-score.
  - Overfitting vs. generalization.

---

## 🌐 Unsupervised Learning
### Algorithms Implemented
- **KMeans.ipynb**
  - Learned clustering by minimizing intra-cluster variance.
  - Applied to synthetic datasets.
- **KMeansForIris.ipynb**
  - Used Iris dataset to visualize clustering performance.
  - Compared clusters with actual species labels.
- **DBSCAN.ipynb**
  - Density-based clustering.
  - Strength: finds arbitrary-shaped clusters.
  - Weakness: sensitive to parameter choice (eps, minPts).
- **hierarchical_clustering.ipynb**
  - Built dendrograms to visualize cluster merging.
  - Explored single-link vs. complete-link methods.

### Key Insights
- Unsupervised ML reveals hidden structures without labels.
- Choice of algorithm depends on dataset characteristics:
  - KMeans → spherical clusters, scalable.
  - DBSCAN → noise handling, non-linear shapes.
  - Hierarchical → visualization of cluster hierarchy.

---

## 📝 Reflections
- Supervised ML feels more straightforward due to labeled data, but unsupervised ML is powerful for exploratory analysis.
- Keeping `.ipynb_checkpoints` organized avoids clutter.
- Next steps:
  - Add PCA for dimensionality reduction.
  - Explore clustering evaluation metrics (Silhouette Score, Davies–Bouldin Index).
  - Document minor project results in detail.

