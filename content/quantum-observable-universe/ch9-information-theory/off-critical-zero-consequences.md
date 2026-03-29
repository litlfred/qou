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

- A spectral arena on which a transfer operator acts.
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

**The $d_{H,q}$ closed form.**

The critical line location depends on the **$q$-deformed Hausdorff
dimension** $d_{H,q} = (2q-1)^2/q^3$
([operational entropy](#def:operational-entropy)).  This is exact
within the $q$-deformed framework — a rational function of $q$,
not an approximation.  The derivation:

$$
  G_{\mathrm{Planck}} = 1
  \;\Rightarrow\;
  \eta_q = \frac{2q-1}{q^3}
  \;\xRightarrow{\chi_q = 1/(2q-1)}\;
  d_{H,q} = \frac{(2q-1)^2}{q^3}
  \;\Rightarrow\;
  \sigma_q = \frac{(2q-1)^2}{2q^3}.
$$

Each step is algebraic — no approximations, no numerics, no
fitting.  The $3.9\%$ difference from the classical
transfer-operator value ($d_H \approx 1.047$) is not a discrepancy:
$d_{H,q}$ and $d_H$ are **different quantities**.  The classical
$d_H$ uses $h_{\mathrm{top}} = \ln 2$ (transcendental, $\mathbb{C}$-only);
$d_{H,q}$ uses $\eta_q = (2q-1)/q^3$ (rational, field-independent).
They agree at $q = 1$ and at $q = \varphi^2$ but diverge elsewhere.

**What would close the gaps.**

| Gap | What's needed |
|-----|---------------|
| 1. $Z_q$ analytic | Meromorphic continuation of the Ruelle product (Ruelle–Pollicott theory for the specific family $f_q$) |
| 2. Spectral arena | A field-independent framework — possibly categorical (via the braided tensor category directly) rather than analytic ($L^2$ on the Julia set) |
| 3. Spectral identification | An explicit map from $V^{\otimes n}$ to the spectral arena, or a categorical substitute that avoids Hilbert spaces entirely |

**Classical RH as a special case.**
At $q = 1$: $d_{H,q} = 1$, $\sigma_1 = 1/2$, $\chi_1 = 1$, and
the $R$-matrix collapses to the symmetric group (trivially
unitary).  Classical RH is the statement that the classical limit
of the substrate preserves unitarity.

**Falsifiability.**
For prime-power $q$, the Weil conjectures (Deligne) guarantee
zeros at $\operatorname{Re}(s) = 1/2$.  The $q$-critical line
prediction gives $\sigma_q = 1/2$ only when $d_{H,q} = 1$
($q = 1$ or $q = \varphi^2$).  For other prime-power values,
the dynamical and arithmetic zeta functions must disagree — a
computable test.
