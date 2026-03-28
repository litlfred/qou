The $R$-matrix of the braided tensor category is unitary:
$\beta_{V,V}$ is an isomorphism with $\beta_{V,V} \circ
\beta_{V,V}^{-1} = \mathrm{id}_{V \otimes V}$, and the eigenvalues
$q$ and $-q^{-1}$ satisfy $|q \cdot (-q^{-1})| = 1$.  This is
not a conjecture — it is a proved property of the braiding.

**Proposition (Unitarity $\Rightarrow$ $q$-critical line).**
*Assume the spectral identification: the non-trivial zeros of the
dynamical zeta function $Z_q(s)$
([$q$-logarithmic zeta](#def:q-logarithmic-zeta)) are eigenvalues
of a Ruelle transfer operator $\mathcal{L}_s$ acting on
$L^2(J(f_q), \mu_q)$, and this operator is unitarily equivalent to
the $R$-matrix braiding on $V^{\otimes n}$.  Then all non-trivial
zeros satisfy*

$$
  \operatorname{Re}(s) \;=\; \sigma_q
  \;:=\; \frac{d_H(q)}{2}
  \;=\; \frac{(2q-1)^2}{2q^3},
$$

*where $d_H(q) = (2q-1)^2/q^3$ is the Hausdorff dimension of the
Julia set ([operational entropy](#def:operational-entropy)).*

**Proof sketch.**

1. **$R$-matrix unitary $\Rightarrow$ $\mathcal{L}_s$
   self-adjoint.**  The spectral identification maps $\mathcal{L}_s$
   to the $R$-matrix action.  Since $\beta_{V,V}$ is an isomorphism
   with inverse $\beta_{V,V}^{-1}$, the operator $\mathcal{L}_s$ is
   self-adjoint on $L^2(J(f_q), \mu_q)$.

2. **Self-adjoint $\Rightarrow$ real spectrum.**  The eigenvalues of
   $\mathcal{L}_s$ — which are the zeros $\rho$ of $Z_q$ — have
   $\operatorname{Im}(\rho)$ constrained by self-adjointness.

3. **$q$-functional equation pins the real part.**  The functional
   equation $\zeta_q(s) = \chi_q(s)\,\zeta_q(d_H(q) - s)$ pairs
   each zero $\rho$ with $d_H(q) - \bar{\rho}$.  Self-adjointness
   forces $\rho = d_H(q) - \bar{\rho}$, i.e.,
   $\operatorname{Re}(\rho) = d_H(q)/2 = \sigma_q$.  $\square$

**What is assumed vs. what is proved.**

| Status | Statement |
|--------|-----------|
| **Proved** (Lean) | $\beta_{V,V}$ is an isomorphism; Yang–Baxter holds |
| **Proved** (algebraic) | $d_H(q) = (2q-1)^2/q^3$ from Manning–McCluskey + $G_{\mathrm{Planck}} = 1$ |
| **Assumed** | Spectral identification: zeros of $Z_q \leftrightarrow$ eigenvalues of $\mathcal{L}_s \leftrightarrow$ $R$-matrix spectrum |
| **Follows** | All non-trivial zeros have $\operatorname{Re}(s) = \sigma_q$ |

The single assumption is the Hilbert–Pólya step: that the zeros of
$Z_q$ correspond to eigenvalues of an operator unitarily equivalent
to the $R$-matrix braiding.  Everything else is forced.

**Consistency checks.**

| Check | Result |
|-------|--------|
| $q \to 1$ | $d_H(1) = 1$, so $\sigma_1 = 1/2$ — recovers classical RH |
| $q = \varphi^2$ | $d_H(\varphi^2) = 1$, so $\sigma_{\varphi^2} = 1/2$ — golden threshold preserves the classical critical line |
| $q = 1.1097$ | $d_H \approx 1.088$, so $\sigma_q \approx 0.544$ — an $8.8\%$ shift from $1/2$ |
| $q \to \infty$ | $d_H \to 0$, so $\sigma_q \to 0$ — all zeros collapse to the imaginary axis |

**The two fixed points.**  The critical line equals $1/2$ at exactly
two values: $q = 1$ (classical limit) and $q = \varphi^2$ (golden
threshold).  Between these points ($1 < q < \varphi^2$), the critical
line is strictly above $1/2$ — zeros are displaced rightward.
Beyond $\varphi^2$, the critical line descends below $1/2$ and
approaches the imaginary axis as $q \to \infty$ (Big Bang).

**The $d_H(q)$ closed form is load-bearing.**  The entire argument
rests on the exact formula $d_H(q) = (2q-1)^2/q^3$.  This is
derived from two independent constraints:

1. The Manning–McCluskey formula $d_H = \eta_q / \chi_q$ with the
   $q$-deformed Lyapunov exponent $\chi_q = 1/(2q-1)$.
2. The gravitational self-consistency condition
   $G_{\mathrm{Planck}} = 1$, which algebraically forces
   $\eta_q = (2q-1)/q^3$.

If either ingredient is wrong — if $\chi_q$ has corrections, or if
$G_{\mathrm{Planck}} = 1$ admits perturbative deviations — then
$\sigma_q$ shifts and the critical line prediction changes.  The
closed form for $d_H(q)$ must be exact, not approximate.
