**Conjecture ($\mu_{\mathrm{arch}}$ kernel-match — Frobenius Gram vs. Finster causal Lagrangian).**
*On the shared free-probability spectral limit
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

**Bifurcation, sharpened.**

- *Match outcome (kernel-equality).* If $G(x, y) =
  \mathcal{L}_{\mathrm{CFS}}(x, y)$ as functions of $(x, y) \in
  \mathcal{F}_\infty^2$ — equivalently, if the Finster max-of-pair-
  products functional reduces to the bilinear trace
  $\mathrm{tr}_M(x \cdot y)$ on the free-probability limit — then
  $\mu_{\mathrm{arch}}$ is a theorem and CFS is exactly the continuum
  realisation of QOU's traceful projection
  ([prop:cfs-as-traceful-projection-of-qou](#prop:cfs-as-traceful-projection-of-qou)).

- *Weaker-match outcome (integral-equality only).* If the kernels
  differ as functions but the integrals against $\rho_\infty$ happen
  to coincide — i.e., the kernel difference $\mathcal{L}_{\mathrm{CFS}} -
  G$ is in the null space of $\rho_\infty \otimes \rho_\infty$ — then
  the *action values* of QOU and CFS coincide at the optimum even
  though the local dynamics differ. The two theories would predict
  the same total energies but different field configurations.

- *Mismatch outcome (no coincidence).* If even the integrals
  disagree, QOU and CFS predict different continuum actions and
  therefore different physics on the same operator algebra. This is
  the most informative outcome: QOU's natural continuum theory
  *differs* from Finster's CFS even though both are well-defined on
  the same carrier.

**Generic prior: mismatch.** A bilinear functional and a max-of-pair-
products functional are different objects; coincidence would require
either (a) a specific choice of $\rho_\infty$ that intertwines them,
or (b) a hidden algebraic identity reducing the extremal structure
to a bilinear sum. Neither is automatic. The strict-match outcome
(first bullet) is the strongest version of the conjecture; the
integral-match outcome (second bullet) is a fallback that would
still rescue $\mu_{\mathrm{arch}}$ as a "weak" theorem about action
values; the mismatch outcome (third bullet) is the most likely
*a priori*.

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
