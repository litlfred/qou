The Markov trace factorization
([factorization theorem](#thm:markov-trace-factorization)) gives
an exact product $\prod_i \hat{V}_i$ that grows exponentially with
$A$.  The **physical energy** is not the product itself but its
**logarithm** — the quantum dilogarithm volume of the nuclear link.

**Three volumes of a knot.**

| Volume | Formula | Scaling | Used for |
|--------|---------|---------|----------|
| Hyperbolic | $\text{Vol}(S^3 \setminus K)$ | $O(1)$ per knot | Single-particle mass |
| Hecke weight | $\sum \lVert c_w\rVert \cdot \ell(w)$ | $O(e^A)$ | Gröbner--Shirshov energy (algebraic) |
| Quantum dilogarithm | $\Phi_q(z) = \sum_i \log \hat{V}_i$ | $O(A)$ | **Nuclear binding energy** |

The hyperbolic volume is the classical ($q \to 1$) limit of
$\Phi_q$.  The Hecke weight is the exponential of $\Phi_q$.  The
quantum dilogarithm $\Phi_q$ is the intensive, physical volume.
