# Linear Algebra for Machine Learning — companion code

Companion Jupyter notebooks for the Kindle book **Linear Algebra for Machine Learning: Spaces, Operators, Matrix Analysis and the Mathematics of Learning** by Rajesh Ranjan Mahapatra.

Every program in the book is here, chapter by chapter, with its output and figures already rendered. The boxes marked *computed* in the book are the output of these notebooks, and every figure in the book is drawn by the code in them.

## Quick start

```bash
git clone https://github.com/rajesh1008/linear-algebra-for-machine-learning.git
cd linear-algebra-for-machine-learning
python -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt                     # or: pip install numpy scipy matplotlib sympy jupyter
jupyter lab notebooks/
```

Open any chapter notebook and run the cells top to bottom (Run → Run All Cells). Each notebook stands on its own; the only shared file is **`notebooks/lafp.py`**, the book's small plotting toolkit (`from lafp import *`). Keep it in the same folder as the notebooks.

You can also open the notebooks in Google Colab: upload the notebook together with `lafp.py`.

Requirements: Python 3.10 or newer, NumPy 2.x, SciPy, Matplotlib (and SymPy for chapter 13). Nothing else.

## Contents

| Notebook | Chapter |
|---|---|
| [00_laboratory](notebooks/00_laboratory.ipynb) | L. The Laboratory |
| [ch01_vectors_and_vector_spaces](notebooks/ch01_vectors_and_vector_spaces.ipynb) | 1. Vectors and Vector Spaces |
| [ch02_span_independence_basis_and_dimension](notebooks/ch02_span_independence_basis_and_dimension.ipynb) | 2. Span, Independence, Basis and Dimension |
| [ch03_linear_maps](notebooks/ch03_linear_maps.ipynb) | 3. Linear Maps |
| [ch04_matrices_and_the_ways_to_multiply_them](notebooks/ch04_matrices_and_the_ways_to_multiply_them.ipynb) | 4. Matrices and the Ways to Multiply Them |
| [ch05_elimination_lu_and_the_four_fundamental_subspaces](notebooks/ch05_elimination_lu_and_the_four_fundamental_subspaces.ipynb) | 5. Elimination, LU and the Four Fundamental Subspaces |
| [ch06_invertibility_isomorphism_and_change_of_basis](notebooks/ch06_invertibility_isomorphism_and_change_of_basis.ipynb) | 6. Invertibility, Isomorphism and Change of Basis |
| [ch07_products_quotients_and_duality](notebooks/ch07_products_quotients_and_duality.ipynb) | 7. Products, Quotients and Duality |
| [ch08_polynomials](notebooks/ch08_polynomials.ipynb) | 8. Polynomials |
| [ch09_eigenvalues_invariant_subspaces_and_the_minimal_po](notebooks/ch09_eigenvalues_invariant_subspaces_and_the_minimal_po.ipynb) | 9. Eigenvalues, Invariant Subspaces and the Minimal Polynomial |
| [ch10_triangular_and_diagonal_forms](notebooks/ch10_triangular_and_diagonal_forms.ipynb) | 10. Triangular and Diagonal Forms |
| [ch11_generalized_eigenvectors_jordan_form_and_trace](notebooks/ch11_generalized_eigenvectors_jordan_form_and_trace.ipynb) | 11. Generalized Eigenvectors, Jordan Form and Trace |
| [ch12_inner_products_and_orthonormal_bases](notebooks/ch12_inner_products_and_orthonormal_bases.ipynb) | 12. Inner Products and Orthonormal Bases |
| [ch13_orthogonal_projection_least_squares_and_the_pseudo](notebooks/ch13_orthogonal_projection_least_squares_and_the_pseudo.ipynb) | 13. Orthogonal Projection, Least Squares and the Pseudoinverse |
| [ch14_adjoints_normal_operators_and_the_spectral_theorem](notebooks/ch14_adjoints_normal_operators_and_the_spectral_theorem.ipynb) | 14. Adjoints, Normal Operators and the Spectral Theorem |
| [ch15_positive_operators_isometries_qr_and_cholesky](notebooks/ch15_positive_operators_isometries_qr_and_cholesky.ipynb) | 15. Positive Operators, Isometries, QR and Cholesky |
| [ch16_the_singular_value_decomposition](notebooks/ch16_the_singular_value_decomposition.ipynb) | 16. The Singular Value Decomposition |
| [ch17_low_rank_approximation_pca_and_rayleigh_quotients](notebooks/ch17_low_rank_approximation_pca_and_rayleigh_quotients.ipynb) | 17. Low-Rank Approximation, PCA and Rayleigh Quotients |
| [ch18_norms_of_vectors_functions_and_matrices](notebooks/ch18_norms_of_vectors_functions_and_matrices.ipynb) | 18. Norms of Vectors, Functions and Matrices |
| [ch19_bilinear_and_quadratic_forms](notebooks/ch19_bilinear_and_quadratic_forms.ipynb) | 19. Bilinear and Quadratic Forms |
| [ch20_alternating_forms_and_determinants](notebooks/ch20_alternating_forms_and_determinants.ipynb) | 20. Alternating Forms and Determinants |
| [ch21_tensor_products_and_tensor_factorizations](notebooks/ch21_tensor_products_and_tensor_factorizations.ipynb) | 21. Tensor Products and Tensor Factorizations |
| [ch22_majorization_and_doubly_stochastic_matrices](notebooks/ch22_majorization_and_doubly_stochastic_matrices.ipynb) | 22. Majorization and Doubly Stochastic Matrices |
| [ch23_variational_principles_for_eigenvalues](notebooks/ch23_variational_principles_for_eigenvalues.ipynb) | 23. Variational Principles for Eigenvalues |
| [ch24_symmetric_gauge_functions_and_unitarily_invariant](notebooks/ch24_symmetric_gauge_functions_and_unitarily_invariant.ipynb) | 24. Symmetric Gauge Functions and Unitarily Invariant Norms |
| [ch25_singular_value_inequalities](notebooks/ch25_singular_value_inequalities.ipynb) | 25. Singular Value Inequalities |
| [ch26_the_field_of_values](notebooks/ch26_the_field_of_values.ipynb) | 26. The Field of Values |
| [ch27_stable_matrices_and_inertia](notebooks/ch27_stable_matrices_and_inertia.ipynb) | 27. Stable Matrices and Inertia |
| [ch28_kronecker_products_and_linear_matrix_equations](notebooks/ch28_kronecker_products_and_linear_matrix_equations.ipynb) | 28. Kronecker Products and Linear Matrix Equations |
| [ch29_the_hadamard_product](notebooks/ch29_the_hadamard_product.ipynb) | 29. The Hadamard Product |
| [ch30_functions_of_matrices](notebooks/ch30_functions_of_matrices.ipynb) | 30. Functions of Matrices |
| [ch31_operator_monotone_and_operator_convex_functions](notebooks/ch31_operator_monotone_and_operator_convex_functions.ipynb) | 31. Operator Monotone and Operator Convex Functions |
| [ch32_matrix_inequalities](notebooks/ch32_matrix_inequalities.ipynb) | 32. Matrix Inequalities |
| [ch33_spectral_variation_of_normal_matrices](notebooks/ch33_spectral_variation_of_normal_matrices.ipynb) | 33. Spectral Variation of Normal Matrices |
| [ch34_perturbation_of_spectral_subspaces](notebooks/ch34_perturbation_of_spectral_subspaces.ipynb) | 34. Perturbation of Spectral Subspaces |
| [ch35_nonnormal_matrices_and_perturbation_of_matrix_func](notebooks/ch35_nonnormal_matrices_and_perturbation_of_matrix_func.ipynb) | 35. Nonnormal Matrices and Perturbation of Matrix Functions |
| [ch36_numerical_linear_algebra](notebooks/ch36_numerical_linear_algebra.ipynb) | 36. Numerical Linear Algebra |
| [ch37_randomized_linear_algebra_and_matrix_concentration](notebooks/ch37_randomized_linear_algebra_and_matrix_concentration.ipynb) | 37. Randomized Linear Algebra and Matrix Concentration |
| [ch38_low_rank_sparsity_and_compressed_sensing](notebooks/ch38_low_rank_sparsity_and_compressed_sensing.ipynb) | 38. Low Rank, Sparsity and Compressed Sensing |
| [ch39_fourier_circulant_and_toeplitz_matrices](notebooks/ch39_fourier_circulant_and_toeplitz_matrices.ipynb) | 39. Fourier, Circulant and Toeplitz Matrices |
| [ch40_graphs_laplacians_and_clustering](notebooks/ch40_graphs_laplacians_and_clustering.ipynb) | 40. Graphs, Laplacians and Clustering |
| [ch41_probability_and_statistics_through_matrices](notebooks/ch41_probability_and_statistics_through_matrices.ipynb) | 41. Probability and Statistics through Matrices |
| [ch42_optimization](notebooks/ch42_optimization.ipynb) | 42. Optimization |
| [ch43_deep_neural_networks](notebooks/ch43_deep_neural_networks.ipynb) | 43. Deep Neural Networks |
| [ch44_random_matrices_and_the_spectra_of_learning](notebooks/ch44_random_matrices_and_the_spectra_of_learning.ipynb) | 44. Random Matrices and the Spectra of Learning |
| [ch45_interpolation_implicit_bias_and_kernels](notebooks/ch45_interpolation_implicit_bias_and_kernels.ipynb) | 45. Interpolation, Implicit Bias and Kernels |
| [ch46_the_linear_algebra_of_transformers](notebooks/ch46_the_linear_algebra_of_transformers.ipynb) | 46. The Linear Algebra of Transformers |
| [ch47_preconditioners_orthogonalized_optimizers_and_low](notebooks/ch47_preconditioners_orthogonalized_optimizers_and_low.ipynb) | 47. Preconditioners, Orthogonalized Optimizers and Low Precision |

## Errata and questions

Found a mistake or a result that does not match the book? Please open an issue.

## License

The code in this repository is released under the [MIT License](LICENSE). Copyright (c) 2026 Rajesh Ranjan Mahapatra.
