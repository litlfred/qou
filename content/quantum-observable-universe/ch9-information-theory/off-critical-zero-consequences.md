The $R$-matrix is unitary — that's proved.  The intuition that
unitarity should force zeros onto $\sigma_q$ is compelling.  But
as the gap analysis shows
([$q$-critical line](#conj:q-critical-line)), there is no direct
logical path from unitarity to the critical line yet.  This remark
catalogues what an off-critical zero would contradict and what
remains to be built.

**What unitarity gives us (proved).**

- $\beta_{V,V} \circ \beta_{V,V}^{-1} = \mathrm{id}$ — braiding
  is exactly invertible.
- Eigenvalues $q$ and $-q^{-1}$ with $|q \cdot (-q^{-1})| = 1$.
- Yang–Baxter holds: $\sigma_1\sigma_2\sigma_1 =
  \sigma_2\sigma_1\sigma_2$.

**What unitarity does NOT directly give us.**

- A Hilbert space on which a transfer operator acts.
- A spectral identification connecting $R$-matrix eigenvalues to
  zeta zeros.
- Meromorphic continuation of $Z_q$ past its convergence boundary.
- A $q$-functional equation.

**Contrapositive (hypothetical).**

If we *could* build the spectral identification, an off-critical
zero $\rho = \beta + i\gamma$ with $\beta \neq \sigma_q$ would
require the spectral operator to be non-self-adjoint, contradicting
the unitarity of the $R$-matrix.  The pathologies:

| Pathology | Mechanism |
|-----------|-----------|
| Orbit-counting anomaly | $\Pi_q(N)$ fluctuates as $q^{(\beta - \sigma_q)N}$ |
| Information loss in braiding | $\beta \circ \beta^{-1} \neq \mathrm{id}$ |
| Gravity fluctuations | $G_{\mathrm{Planck}} \neq 1$ at scale $|\gamma|$ |
| Entropy bound violation | $\Delta\eta \neq 0$ oscillations |

But this argument is conditional on the spectral identification
existing.  Without it, unitarity and the zeta zeros live in
different worlds.

**The $d_H(q)$ closed form.**

Even granting the spectral identification, the critical line
location depends on $d_H(q) = (2q-1)^2/q^3$.  The derivation:

$$
  G_{\mathrm{Planck}} = 1
  \;\Rightarrow\;
  \eta_q = \frac{2q-1}{q^3}
  \;\xRightarrow{\chi_q = 1/(2q-1)}\;
  d_H(q) = \frac{(2q-1)^2}{q^3}
  \;\Rightarrow\;
  \sigma_q = \frac{(2q-1)^2}{2q^3}.
$$

The $3.9\%$ discrepancy with the transfer-operator numerical
value ($1.047$ vs. $1.088$) is an open problem.  Possible
resolutions:

1. The cardioid parameterization $c(q)$ in the numerical
   computation is not the correct map from the substrate to the
   quadratic family.
2. The $q$-deformed Lyapunov exponent $\chi_q = 1/(2q-1)$ is
   approximate.
3. The QOU dynamics genuinely differs from classical conformal
   dynamics in a way the transfer operator does not capture.

**What would close the gaps.**

| Gap | What's needed |
|-----|---------------|
| 1. $Z_q$ analytic | Meromorphic continuation of the Ruelle product (Ruelle–Pollicott theory for the specific family $f_q$) |
| 2. Hilbert space | A field-independent spectral framework — possibly via Berkovich spaces ($p$-adic) or étale cohomology (finite fields) instead of $L^2$ |
| 3. Spectral identification | An explicit isometry from $V^{\otimes n}$ to the function space carrying $\mathcal{L}_s$ — or a categorical substitute that avoids Hilbert spaces entirely |
| 4. $d_H$ numerics | Either fix the parameterization $c(q)$, or derive the closed form without Manning–McCluskey |

**Classical RH as a special case.**
At $q = 1$: $d_H(1) = 1$, $\sigma_1 = 1/2$, $\chi_1 = 1$, and
the $R$-matrix collapses to the symmetric group (trivially
unitary).  Classical RH is the statement that the classical limit
of the substrate preserves unitarity.

**Falsifiability.**
For prime-power $q$, the Weil conjectures (Deligne) guarantee
zeros at $\operatorname{Re}(s) = 1/2$.  The $q$-critical line
prediction gives $\sigma_q = 1/2$ only when $d_H(q) = 1$
($q = 1$ or $q = \varphi^2$).  For other prime-power values,
the dynamical and arithmetic zeta functions must disagree — a
computable test.
