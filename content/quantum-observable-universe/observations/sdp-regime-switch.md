**Proposition.**
*The semidefinite-programming (SDP) extension of the LP-dual
operator-selection framework
([BW coefficient shadow price](#prop:mass-coefficient-shadow-price))
introduces matrix-valued cross-block couplings
$c_{\lambda\lambda'}$ between conjugate-partition pairs in the
Wedderburn decomposition of $H_n(q)$.  These couplings vary
discretely as $(Z, N)$ varies at fixed substrate parameter $q_0$,
with isolated zeros that mark nuclear-structure regime switches —
shell closures, pairing transitions, and jet-level crossings.*

*At each $(Z, N)$, the atom braid word $W_{\mathrm{atom}}$ has
a YSN character $\chi_\lambda(W)$ in every irrep $\lambda$.
These characters serve as primal OBSERVABLES driving the SDP:*

$$
  \Phi_{\lambda\lambda} \;=\; \frac{|\chi_\lambda(W)|^2}{\lVert W \rVert^2}
$$

*The SDP dual has a $2 \times 2$ PSD block per conjugate pair
$(\lambda, \lambda')$:*

$$
  \begin{pmatrix}
    \mu_\lambda - y_0 - y_\lambda & c_{\lambda\lambda'} \\
    c_{\lambda\lambda'} & \mu_{\lambda'} - y_0 - y_{\lambda'}
  \end{pmatrix}
  \;\succeq\; 0
$$

*where $\mu_\lambda$ is the $q$-Laplacian eigenvalue
([$q$-heat kernel Peter-Weyl](#prop:q-heat-kernel-peter-weyl))
and $c_{\lambda\lambda'}$ is the coupling, determined by the atom
observables.*

*A **regime switch** occurs at $(Z, N)$ values where
$c_{\lambda\lambda'} \to 0$: the PSD block drops from rank 2 to
rank 1, the active-constraint set of the SDP jumps, and the
atom's density matrix loses coherence between $\lambda$ and
$\lambda'$.*

$\square$

**Witness.**  `computations/sdp_cross_channel.py`
with `sdp_with_atom_observables(Z, N, partition_entries,
pair_couplings)` using the `cvxpy` SDP solver; falls back to
scalar LP if `cvxpy` unavailable.
