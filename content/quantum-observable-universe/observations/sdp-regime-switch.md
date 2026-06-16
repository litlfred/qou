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

**Observed sign-flip pattern** (computed at $q = q_0 \approx 1.11$,
$k$-cap $= 5$, pairs at $H_4(q) \oplus H_5(q)$):

See [Table](#tbl:sdp-regime-switch-table-data).

*Key features observed*:

1. **Sign flips**: each coupling changes sign multiple times across
   the isotope chain.  The zero-crossings (marked $\approx 0$)
   correspond to specific isotopes.

2. **Shell-closure signatures**: ${}^{3}\mathrm{He}$, ${}^{11}\mathrm{B}$, and ${}^{40}\mathrm{Ca}$ all sit at
   near-zero couplings — these are the SDP's markers for N=1
   (trivial shell), N=6 (closed $p_{3/2}$), and Z=N=20 (double-
   magic $s\text{-}d$ shell closure).

3. **Isoscalar vs isovector structure**: the $(3,1)$$\leftrightarrow$$(2,1,1)$
   pair changes sign most frequently (sensitive to N vs Z parity);
   the $(3,2)$$\leftrightarrow$$(2,2,1)$ pair varies most smoothly (less sensitive
   to individual-nucleon structure).

**Physical interpretation** (conjectural — awaiting Lean
formalisation and experimental comparison):

- The SDP couplings $c_{\lambda\lambda'}$ are the categorical
  analogues of **density-matrix coherence elements** between
  Wedderburn sectors.
- Zero couplings mark nuclear configurations where the atom's
  projection loses phase coherence between $\lambda$ and $\lambda'$
  — equivalent to the appearance of a conserved quantum number
  (shell closure, pairing gap, spin saturation).
- As $q$ is held fixed at $q_0$ (the substrate parameter from
  SnapPy $\mathrm{Vol}(4_1)$ and CODATA $m_\mu/m_e$), the
  $(Z, N)$ scan is a categorical probe of the Standard Model's
  discrete nuclear-structure hierarchy.

$\square$

**Witness.**  `computations/sdp_cross_channel.py`
with `sdp_with_atom_observables(Z, N, partition_entries,
pair_couplings)` using the `cvxpy` SDP solver; falls back to
scalar LP if `cvxpy` unavailable.

**Related**:
- Complementary to the LP-dual shadow prices
  ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)),
  which give only scalar per-partition variables.
- The $q$-dependence of the couplings $c_{\lambda\lambda'}(q)$
  (varying $q$ at fixed $Z, N$) detects SUBSTRATE regime switches
  — cosmological transitions, Big-Bang to heat-death across the
  $q$-time coordinate ([$q$-heat equation](#def:q-heat-equation)).
  This extension is deferred to a future commit.
