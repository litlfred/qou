**Conjecture (physical role of Im(q)).**
*The substrate parameter $q$ admits a complex extension
([prop:q-zero-complex-extension](q-zero-complex-extension.md)).
The current QOU framework's observables (categorical masses
$\mathfrak{m}_{q,\mathcal{K}} = |\mathrm{tr}_M|$ and per-braid
mass tower) are real-valued and **insensitive to $\mathrm{Im}(q)$
at leading order** under modulus projection ($\mathrm{Im}(q)$
shifts both numerator and denominator of mass ratios in tandem
via the modulus operation). The physical role of $\mathrm{Im}(q)$
— if any — must therefore be sought in observables not currently
in the framework.*

*This conjecture catalogues three candidate roles, each
testable against a specific observable class. Identifying
which (if any) is the correct physical interpretation is open
work.*

## What Im(q) is NOT

Per [`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md), Im(q) is **NOT**:
- The EM / $P_{\mathrm{skew}}$ channel (that's a real-q mechanism)
- A fourth calibration input (the 3-CAL count is cohomologically forced)
- An observable in the current framework (mass formula uses $|\cdot|$)
- Equal to $\mathrm{Im}(\mathrm{tr}_M(\rho(\beta)))$ — Im(q) is a parameter; Im(tr_M) is the value induced

## Three candidate physical roles

### Candidate (i) — chirality / orientation parameter

In the Kashaev regime ($q$ a root of unity, $q = e^{2\pi i/N}$),
the q-deformed Hecke algebra produces N-fold quantum symmetries
whose Markov traces give hyperbolic volumes (Kashaev volume
conjecture). For complex $q = |q| e^{i \arg q}$ near the unit
circle, $\arg q$ is naturally a **chirality coordinate** —
positive arg gives clockwise braid orientation; negative arg
gives counterclockwise. The categorical mass formula is invariant
under $q \mapsto \bar q$ (complex conjugation under modulus
projection), consistent with mass being chirality-invariant.

**Testable**: does the framework's prediction for an explicitly
chirality-sensitive observable (e.g., parity-violating decay
asymmetry; CP violation in $K^0$-$\bar K^0$ mixing) require
$\arg q \neq 0$?

### Candidate (ii) — phase coordinate dual to CAL-2

CAL-2 ($m_\mu/m_e = 206.7682830$) gives **one real equation** on
two real unknowns ($\mathrm{Re}(q), \mathrm{Im}(q)$). The solution
set is an **Apollonius circle** in the complex q-plane (center
$\approx 1.010$, radius $\approx 0.100$ per `q_beta_complex_q_test1_phaseA_v2.py`).
The framework's real-axis solution $q_0 \approx 1.10998$ is one
point on this circle; Im(q) is the arc coordinate parametrizing
the other admissible q values.

**Testable**: does another CAL-2-like independent constraint
(a second real equation from $m_\tau/m_e$, or from a different
observable) fix a unique complex $q_0$? If only real solutions
exist, candidate (ii) is closed; if a complex solution is needed,
the framework has missed an Im(q)-coupled measurement.

### Candidate (iii) — non-Hermitian deformation / open-system parameter

The Hoefsmit seminormal Hecke representation has real-coefficient
matrices for $q > 0$ real, giving **unitary** $H_n(q)$ representations.
For complex $q$ with $|q| \neq 1$, unitarity breaks: representations
become non-unitary; eigenvalues become complex. In quantum mechanics,
non-Hermitian operators arise in **open systems** (decay, dissipation,
resonance widths).

**Testable**: do decay widths (Γ for unstable particles — W, Z,
top, resonances) correlate with the Im(q) needed to make Hecke
representations describe their non-Hermitian dynamics? Most decay
widths in the Standard Model have categorical interpretations open
in the QOU framework.

## Why none is currently proved

Each candidate requires an observable the framework does not yet
provide:
- (i) needs explicit chirality-sensitive observables (CP violation, parity asymmetry)
- (ii) needs a second independent CAL-2-like constraint
- (iii) needs a categorical formula for decay widths $\Gamma$

The framework's mass formula explicitly **projects away** Im(q)
content via $|\cdot|$, so no mass observable can detect Im(q)
directly. The candidate roles are all in **non-mass observables**.

## Connection to other conjectures

- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) F_ℓ
  — the canonical lepton-mass formula is Im(q)-robust (modulus projection
  invariance); F_ℓ does NOT distinguish the three candidate Im(q) roles.
  Hence the F_ℓ conjecture is consistent with ALL three candidates.
- [`prop:rho-k-pair-gen-canonical-form`](conj-rho-k-pair-gen-canonical-form.md) —
  similarly Im(q)-robust at LO.
- The complex-q machinery is **decoupled** from the mass-formula closure;
  closing the $\mathfrak{Q}_\beta$ residual or deriving F_ℓ does **not** require resolving
  Im(q)'s role.

## Default value: Im(q) = 0

In the absence of an Im(q)-sensitive observable, the framework's
canonical choice is **$\mathrm{Im}(q_0) = 0$** (real q). This is:
- **Computationally simple**: real Hecke arithmetic, real
  $\mathrm{tr}_M$, real masses.
- **Empirically sufficient**: all known mass observables fit
  with real $q_0$ to the precision documented in `per-observable-100x-status.witness.json`.
- **NOT structurally forced**: nothing in the QOU framework's
  cohomological discipline requires $\mathrm{Im}(q) = 0$; it's a
  convention pending an Im-sensitive measurement.

## Cross-references

- [`prop:q-zero-complex-extension`](q-zero-complex-extension.md) — substrate polymorphism
- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — involution split for complex q
- [`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md) — the distinction from P_skew
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — modulus projection
- Audit: [`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding
- Audit: [`docs/audits/-complex-q-historical-trajectory.md`](../../../docs/audits/-complex-q-historical-trajectory.md) — historical context
- Audit: [`docs/audits/-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md) §Q3 — Apollonius parametrization
