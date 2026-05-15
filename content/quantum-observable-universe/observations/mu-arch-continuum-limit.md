**Conjecture ($\mu_{\mathrm{arch}}$ integral-match, post-resolution
of strict match).**
*The strict-match version of this conjecture (kernel equality
$G \equiv \mathcal{L}_{\mathrm{CFS}}$ as functions) has been **refuted**
by [prop:mu-arch-strict-match-fails-at-n2](#prop:mu-arch-strict-match-fails-at-n2):
the QOU Frobenius Gram kernel and the Finster causal Lagrangian
differ at the unit pair $(1, 1) \in H_2(R, q) \times H_2(R, q)$
already at $n = 2$. The residual conjecture is the **integral-match**
version: on the shared free-probability spectral limit
$(\mathcal{F}_\infty, \rho_\infty)$, the QOU continuum kernel
$G(x, y) = \mathrm{tr}_M(x \cdot y)$
([prop:qou-continuum-kernel-is-frobenius-gram](#prop:qou-continuum-kernel-is-frobenius-gram))
and the Finster causal Lagrangian
$\mathcal{L}_{\mathrm{CFS}}(x, y) = f(\mathrm{spec}(x \cdot y))$
([`finster2024`, §2]) integrate to the same value against
$\rho_\infty \otimes \rho_\infty$:*
$$
  \iint_{\mathcal{F}_\infty\times\mathcal{F}_\infty}
    G(x, y) \,d\rho_\infty(x)\,d\rho_\infty(y)
  \;\stackrel{?}{=}\;
  \iint_{\mathcal{F}_\infty\times\mathcal{F}_\infty}
    \mathcal{L}_{\mathrm{CFS}}(x, y) \,d\rho_\infty(x)\,d\rho_\infty(y).
$$

**What this version makes precise.** The previous statement of
$\mu_{\mathrm{arch}}$ asked vaguely whether the Finster Lagrangian
matched QOU's Plancherel-weighted character functional. The latter
is actually identical to $\mathrm{tr}_M$ by the Plancherel identity,
so the right comparison object on the QOU side is *not* the trace
itself but the *quadratic kernel* of the LP-duality action — which
is the Frobenius Gram matrix $G$ promoted to continuum
([prop:qou-continuum-kernel-is-frobenius-gram](#prop:qou-continuum-kernel-is-frobenius-gram)).
The conjecture is now between two named quadratic kernels integrated
against the same measure.

**The two kernels, side by side.**

| | QOU kernel $G$ | CFS kernel $\mathcal{L}_{\mathrm{CFS}}$ |
|---|---|---|
| Form | Bilinear in $(x, y)$ | Non-linear, extremal in $\mathrm{spec}(x\cdot y)$ |
| Definition | $G(x, y) = \mathrm{tr}_M(x \cdot y)$ | $\mathcal{L}_{\mathrm{CFS}} = \max(0, \ldots)$-style functional of eigenvalues of $x \cdot y$ |
| Source | LP-duality + Frobenius positivity ([`prop:operator-selection-lp`](#prop:operator-selection-lp)) | Causal-action variational principle [`finster2024`] |
| Behaviour under free-probability scaling | Bilinearity preserved | Extremal structure generically not preserved |

The structural asymmetry — bilinear vs extremal — is the source of
the bifurcation. Bilinearity passes through free-probability limits
cleanly (Voiculescu); extremal functionals generally pick up
non-trivial dependence on the limit measure's specific shape.

**Bifurcation, post strict-match refutation.**

- ~~*Strict match outcome.*~~ — **Refuted** by
  [prop:mu-arch-strict-match-fails-at-n2](#prop:mu-arch-strict-match-fails-at-n2).
  The kernels are *not* equal as functions: $G(1, 1) = 1$ while
  $\mathcal{L}_{\mathrm{CFS}}(1, 1) = 0$ in any Finster variant in
  the difference-of-eigenvalues class.

- *Integral-match outcome (residual conjecture).* The kernels differ
  as functions, but the integrals
  $\iint G(x, y)\,d\rho_\infty(x)\,d\rho_\infty(y)$ and
  $\iint \mathcal{L}_{\mathrm{CFS}}(x, y)\,d\rho_\infty(x)\,d\rho_\infty(y)$
  could *still* coincide by cancellation — if the pointwise
  difference $G - \mathcal{L}_{\mathrm{CFS}}$ lies in the null space
  of $\rho_\infty \otimes \rho_\infty$. This would require positive
  and negative contributions to balance exactly. The unit pair
  $(1, 1)$ contributes $+1$; the integral-match outcome therefore
  requires sufficient compensating negative contributions elsewhere
  in $\mathcal{F}_\infty^2$. Whether this cancellation holds is the
  open piece of the conjecture.

- *Mismatch outcome (no coincidence).* If even the integrals
  disagree, QOU and CFS predict different continuum actions and
  therefore different physics on the same operator algebra. Given
  the established functional-class mismatch (bilinear vs
  extremal-difference) and the explicit pointwise disagreement at
  $(1, 1)$, this is the **most likely a priori outcome**: there is
  no algebraic reason for the kernel difference to integrate to
  zero against a generic free-probability measure.

**Generic prior: mismatch.** With the strict-match outcome refuted,
the conjecture is reduced to asking whether the (now-established)
kernel-difference $G - \mathcal{L}_{\mathrm{CFS}}$ has zero integral
against $\rho_\infty \otimes \rho_\infty$. Given the bilinear-vs-
extremal asymmetry and the explicit non-zero pointwise difference at
$(1, 1)$, generic cancellation would require a special algebraic
relationship between the QOU substrate's spectrum and Finster's
Lagrangian normalisation. There is no known mechanism for such
cancellation — the most likely a priori outcome is the *mismatch*
case, in which case QOU and CFS describe distinct continuum theories
of the same operator-algebra substrate.

**Which outcome holds determines the QOU-CFS relationship.** Either
way the conjecture resolves, the result is informative:
- *Strict match* (least likely *a priori*) — QOU and CFS coalesce as
  the same continuum theory; the substrate parameter $q_0$ is the
  CFS parameter.
- *Integral match* (intermediate likelihood) — QOU and CFS have the
  same total action at equilibrium but different local dynamics;
  experimentally distinguishable through correlator measurements.
- *Generic mismatch* — QOU has its own continuum theory, with the
  Frobenius-Gram kernel $G$ as its quadratic action kernel; CFS is a
  different continuum theory of the same operator-algebra substrate.
  QOU's specific predictions (q-Gaussian wash-out, knot-mass formulas,
  LP active-set dynamics) are the QOU continuum theory's outputs;
  CFS's specific predictions (Dirac dynamics, baryogenesis,
  holographic mixing) are CFS's outputs. Both can be tested
  empirically.

**Concrete falsifiability check.** At the free-probability level, the
free moments of $G(x, y)$ against the limit measure are computable
from the spectral cumulants of the q-Gaussian / semicircle. Finster's
Lagrangian moments are computable from the cited literature.
Numerical comparison at $q_0 \approx 1.110$ is a witness-level check
that the QOU compute infrastructure can carry out, distinguishing the
three outcomes above.

**Lean encoding.** Stated as a class with a single
`kernelMatchOnSupport` field — the integral-equality identity — plus
provable structural conditions on the carrier algebra and the limit
measure. Downstream Lean theorems requiring the match carry the
class as an explicit hypothesis, per CLAUDE.md §3b-cond.

**Distinction from $\tau_{\mathrm{arch}}$.** As before,
$\tau_{\mathrm{arch}}$ is scalar-valued (Kashaev volumes, dilogarithm
periods). The measure-valued $\mu_{\mathrm{arch}}$, after this
revision, is *almost entirely provable* — it factors as
$\Pi_{\mathrm{tr}}$ (provable) followed by the kernel-match
(the residual conjecture).
