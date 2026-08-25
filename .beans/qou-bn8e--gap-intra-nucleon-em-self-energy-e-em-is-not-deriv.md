---
# qou-bn8e
title: 'GAP: intra-nucleon EM self-energy E_EM is not derived — the pion sets the length scale but not the magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:36:54Z
updated_at: 2026-08-25T13:01:19Z
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



---

**2026-08-25, second pass — the Coulomb localisation is wrong twice, and this
TIGHTENS the bean rather than closing it.**

Chasing the localisation claim in `rem:isospin-mass-split-em-localisation`
turned up two independent defects. The second is the larger and was **not mine**.

**1. The trace-tower premise is false at the substrate.** New file
`QOU/MassTheory/TraceSignFlipRegime.lean` (sorry-free, axiom-clean). The Hecke
relation forces $\sigma^{-1} = \sigma - (q - q^{-1})$, so a generator flip moves
any linear functional by exactly $(q - q^{-1})\,\mathrm{tr}(1)$, vanishing iff
$q^2 = 1$ — by `double_braiding_eq_one_iff`, exactly the symmetric-braiding
locus. **The trace tower is sign-flip blind precisely where the braiding is
symmetric, and QOU sits off it.** At $q_0$ the flip moves the trace by
$0.209\,\mathrm{tr}(1)$ (mpmath: 0.20906 against the repo's own $q_0$).

No contradiction with `prop:crystal-isospin-degeneracy`, a $q \to 0$ statement
that stays true there. The defect is a **regime conflation** — a crystal-limit
invariance licensing a claim about the functional at $q_0$.

**2. The Coulomb term has the wrong sign — found in the block's own `.qa.json`.**
A `trap-superlative` finding by whichever agent swept the block already carried
this, and I would have missed it. Verified independently in exact mpmath rather
than taken on trust:

    m(3H) - m(3He) = (m_n - m_p) - (B(3H) - B(3He))
                   =    +1.2933   -    +0.7638      = +0.5296 MeV

The Coulomb-driven binding difference enters with the **opposite sign** at 1.44x
the split's magnitude; the free-nucleon difference at 2.44x. **Acting alone the
Coulomb term gives the wrong sign.** That agent's finding and proposed fix were
both correct. The answer was in the sidecar — a place the corpus-grep checklist
does not name and I had not thought to look.

**Why this tightens rather than closes this bean.** The surviving constraint is
that the split lives outside the involution-invariant sector. That complement
holds **both** the nuclear Coulomb term **and** $m_n - m_p$, and the second
dominates. The intra-nucleon EM self-energy is carried in the **free-nucleon
masses**, not in the binding difference (which is what
`mirror_split_s3_em_functional_probe.py` §(A1) says, and what made C2 a genuine
correction). So the mirror split is **not a route around $E_{\mathrm{EM}}$ — it
requires it.** The bean's target is now load-bearing for a second observable
rather than isolated.

Block re-scoped per AGENTS.md §"Before declaring refuted": the observation
stands, only the localisation onto Coulomb goes.

**Still open, unchanged:** $E_{\mathrm{EM}}$ itself. No magnitude here.
