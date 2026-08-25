---
# qou-bn8e
title: 'GAP: intra-nucleon EM self-energy E_EM is not derived — the pion sets the length scale but not the magnitude'
status: todo
type: task
priority: normal
created_at: 2026-08-25T10:36:54Z
updated_at: 2026-08-25T10:37:23Z
---

**Where this stands (2026-08-25, PR #5744, branch `claude/standard-panel-qou-derivation-ixuolx`).**

The owner asked to derive the intra-nucleon EM contribution using the corpus's
meson/pion material. **What came out is a length scale, not an energy.** Stating
the negative plainly rather than dressing the partial result as a closure.

**What IS established.**

The empirical rescale factor `1.178176504688906` sitting in
`computations/mirror_nuclei_coulomb_systematics.py` traces to $r_0 = 1.2$ fm,
and $r_0$ is the reduced pion Compton wavelength
$\bar\lambda_\pi = \hbar c / m_\pi$. So **the pion sets the nuclear Coulomb
length scale**, and the factor is not a free fit. Substituting
$\bar\lambda_\pi$ for the empirical $r_0$ moves the chain mean
$0.838 \to 0.987$ with **no empirical length left in the expression** — the
strongest form of the result, since it removes an input rather than tuning one.

**What is NOT established — the gap.**

$E_{\mathrm{EM}}$ itself. A length scale fixes the $1/r$ in a Coulomb energy;
it does not fix the charge distribution, the exchange term, or the overall
normalisation. Nothing here derives the magnitude of the intra-nucleon
self-energy, and no probe in this branch claims to.

**Do not conflate this with the inter-nucleon front.** They are different
objects, and a retraction on this branch was caused by exactly that conflation
(`docs/audits/2026-08-25-4b-corrections-duplication-and-two-fronts.md`). The
binding-energy derivation `(A1)` shows the *self*-terms cancel in the binding
energy, so 4-B's EM-linking invariant does **not** gate this, and this does not
gate 4-B.

**Next honest step.** Either (i) derive the charge distribution from the
Borromean/color-tube geometry already in the corpus and integrate, or (ii) find
the categorical object whose archimedean evaluation *is* the self-energy. Route
(ii) is the framework-native one. Do not fit a normalisation to the mirror-pair
residuals — that reproduces the anti-fit failure mode the corpus is full of.
