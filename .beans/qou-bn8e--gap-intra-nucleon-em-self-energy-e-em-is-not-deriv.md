---
# qou-bn8e
title: 'GAP: intra-nucleon EM self-energy E_EM is not derived — the pion sets the length scale but not the magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:36:54Z
updated_at: 2026-08-25T11:15:23Z
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



---

**Progress 2026-08-25 — the localisation argument is now proved, and measured.
The magnitude gap survives, unchanged.**

Applying the discipline that worked on `qou-s4h6`: ask what the structure permits
before hunting a formula. The corpus already argues that an EM-sector quantity is
*where* a splitting must live —
[`rem:isospin-mass-split-em-localisation`](content/quantum-observable-universe/mass-theory/isospin-mass-split-em-localisation.md)
concludes the mirror-isobar split *"must therefore be entirely sourced by the
Coulomb term"* because *"the trace tower, co-Casimir, chirality, and
shell-correction functionals all respect these structural involutions."* It is a
`remark` with no Lean.

New file `QOU/MassTheory/InvolutionSelectionRule.lean`, sorry-free, axiom-clean
(two of three depend on `propext` alone), §7c-generic:

- `split_invariantSector_eq_zero` — an $\iota$-invariant sector contributes
  **zero** to the $\iota$-split. The valid core.
- `split_sum_eq_split_remainder` — a sum over a **`List`** of invariant sectors
  plus a remainder splits exactly like the remainder. The enumeration is a
  `List` *in the type* deliberately, so the arity cannot be lost between the
  proposition and the prose.
- `omitted_sector_breaks_localisation` — **the enumeration is load-bearing.**
  Omit one non-invariant sector and the conclusion is false: the argument reports
  "the split is entirely $G$'s, hence zero" while the true split is 2.

**Measured, and this is the part worth keeping.** Of the four sectors the remark
names, **one** has a proved sign-flip invariance in this corpus
(`prop:crystal-isospin-degeneracy`, itself conditional on
`CrystalEigenlineSignBlind`). No theorem asserts it for the trace tower, the
co-Casimir, or chirality. The nearest chirality result,
`QOU.Resurgence.chiral_sign_cancels`, **does not help and should not be cited
here**: it concerns a *different* involution (diagram conjugation, not the
generator sign-flip) and states **anti**-invariance,
$\mathrm{sign}(\bar\mu) = -\mathrm{sign}(\mu)$. An anti-invariant sector is the
one that *survives* a split, not one that drops out.

So the remark's *"all respect these structural involutions"* is one proved case
generalised to four, across at least two distinct involutions — the
`da-arity-conflation` shape. Scope-**(a)**: the localisation is very plausibly
true and is **not** refuted; as supported, it does not follow. The fix is to
prove the two missing invariances, not to weaken the remark.

**The bean's own gap is untouched.** A selection rule says *where* a quantity may
live, never how big it is. $E_{\mathrm{EM}}$ is still not derived, here or
anywhere in this corpus.
