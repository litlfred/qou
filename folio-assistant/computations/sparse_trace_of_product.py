"""
Sparse trace of a product of matrices — avoids densification.

For a chain of sparse matrices M_1, ..., M_k of size dim × dim,
the standard `prod = M_1 @ M_2 @ ... @ M_k; trace(prod)` densifies
the running product and costs O(dim^3) per multiplication once
densified.

Instead: use that tr(prod) = Σ_i (prod)_{ii}, and compute each
diagonal entry by iterative matrix-vector products on a basis
vector e_i:

    v = e_i
    for l in 1..k:  v = M_l @ v
    diag_i = v[i]

After ~log_2(dim) sparse-by-sparse multiplications, v becomes
dense; subsequent multiplications are O(nnz(M)) = O(dim) per step.
Total per i: O(dim · k). Total trace: O(dim² · k).

For dim=6500, k=70: ~3e9 ops, but with scipy.sparse C kernels
this takes ~seconds, not minutes.

Used by `schur_weyl_q_hecke_v2.chi_lambda_atomic` to bypass the
matrix-product densification at A=12+ partition dimensions.
"""
from __future__ import annotations

import numpy as np
from scipy import sparse as sp_sparse


def sparse_trace_of_product(matrices, dim, *, dtype=None):
    """tr(M_1 @ M_2 @ ... @ M_k) without forming the full product.

    Args:
        matrices: list of dim × dim matrices (sparse or dense).
        dim: shared dimension.
        dtype: numpy dtype for the basis vectors (default: float64).

    Returns:
        Sum of diagonal entries of the product, as a Python float.
    """
    if not matrices:
        return float(dim)
    if dtype is None:
        dtype = np.float64
    total = 0.0
    for i in range(dim):
        v = np.zeros(dim, dtype=dtype)
        v[i] = 1.0
        # Apply matrices in REVERSE order: (M_1 ... M_k) e_i = M_1 (M_2 (... (M_k e_i)))
        # Standard convention: M_1 acts first when reading product left-to-right,
        # but for matrix multiplication M_1 @ M_2 @ ... @ M_k @ v, the rightmost
        # matrix is applied first.
        for M in reversed(matrices):
            v = M @ v
            # If v becomes a sparse intermediate, convert back to dense
            if sp_sparse.issparse(v):
                v = np.asarray(v.todense()).flatten()
        total += float(v[i])
    return total
