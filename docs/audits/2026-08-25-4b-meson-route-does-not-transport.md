# 4-B: the meson/pion route to the intra-nucleon EM self-energy

**Bean:** `qou-bhfg`. **Date:** 2026-08-25. **Trigger:** owner, this session —
*"derive intra nucleon.. we have some meson pion in corpus"*.

**Verdict up front: the meson route does not transport, and I have not derived
`E_EM`.** Two candidate bridges from the meson sector both fail, each for a
proved reason, and a third structural constraint survives and narrows what a
successful derivation must look like. That is a redirect, not the answer asked
for.

## The corpus does have a meson EM mechanism

[`meson-em-sinh-closed-form.md`](../content/quantum-observable-universe/braids-and-knots/meson-em-sinh-closed-form.md)
carries an electromagnetic correction in the meson sector:

    m_K² / m_π²  =  [3]_q·[4]_q  +  (α_em/π)·(1 + log(1 + ℏ_q))

with the strong fusion supplying ≈ 99.98 % and the EM term a ≈ 203 ppm
correction. (Note that block's own caveats: the pair `(3,4)` was found by
scanning, and `α_em` is derived *conditionally* on an open Witten-κ `sorry`.
AGENTS.md red-teams this result. None of that matters for what follows — the
question here is only whether the *mechanism* moves to the nucleon.)

## Bridge 1 — transport the term itself. Fails, trivially.

As written the correction is a function of `q` alone. The proton and the
neutron are evaluated at the same substrate `q`, so transporting it as-is
assigns them **the same value** and contributes **nothing** to their splitting —
which is the entire quantity 4-B needs. No computation required; it is immediate
from the shape of the expression, and is recorded here rather than in Lean
because there is nothing to prove.

## Bridge 2 — transport along the linking invariant. Fails, proved.

The two carriers differ in exactly the invariant at issue:

| carrier | components | pairwise linking |
|---|---:|---|
| meson (`q q̄`, Hopf-bound `T(2,2k)`) | 2 | `lk = k ≠ 0` — the corpus's own `evenTwistLinkingNumber` |
| nucleon (Borromean) | 3 | **all zero** — `borromean_crossSum_zero` |

`meson_mechanism_vanishes_on_nucleon` makes the consequence formal: for any `F`
vanishing at zero linking, if `F` is nonzero on the meson carrier then it is
zero on **every** pair of the nucleon carrier. A mechanism carried by pairwise
linking is active on the meson and identically inactive inside the nucleon.

## Bridge 3 — "there is a pion inside the nucleon". A braid-word artifact.

This is the tempting one, and the corpus material invites it.
[`brunnian-property-of-borromean.md`](../content/quantum-observable-universe/knots-particles-confinement/brunnian-property-of-borromean.md)
records that deleting the 0-th strand of `(σ₀σ₁⁻¹)³` leaves `(σ₀⁻¹)³ ∈ B₂`,
whose closure is the negative trefoil. The trefoil is `T(2,3)`, which
[`lepton-meson-torus-knot-dictionary.md`](../content/quantum-observable-universe/knots-particles-confinement/lepton-meson-torus-knot-dictionary.md)
assigns to the **generation-1 meson — the pion**. So: a pion, sitting inside the
nucleon, available to carry its EM self-energy.

**It does not survive a component count.** Deleting one component from a
3-component link must leave **two**. The naively deleted braid word closes to
**one** (`deleted_word_perm_is_swap`: the permutation is a transposition, a
single 2-cycle). So naive braid-word deletion is not sublink deletion, and its
trefoil is a feature of the *word*, not of the *link*. This is exactly why the
corpus block says topological equivalence to `U₂` "requires an explicit sequence
of Reidemeister moves". The true sublink is the unlink, and the unlink carries
no pion.

Proved (`deleted_word_not_two_components`) rather than argued, so the inference
cannot be re-derived from the same material later.

## What survives, and what it says a derivation must look like

Combining with the two earlier prunes on this front:

1. **The input must be `μ̄₁₂₃`** — pairwise linking cannot see the Borromean
   carrier at all (`pairwise_functional_cannot_separate`).
2. **The map must be even in `μ̄₁₂₃`** — an odd map that is symmetric under
   exchanging the two like-charged components vanishes
   (`odd_symmetric_functional_vanishes`), which kills the linear ansatz.
3. **And `μ̄₁₂₃ = 1` on the Borromean carrier** (`mubar_borromean_eq_one`), so
   any even function of it evaluates to a **constant** there.

Point 3 is the sharp one and it is new. The topological factor cannot supply a
*shape* for the proton — it supplies a number. So a successful `E_EM` derivation
has the form

    E_EM  =  (scale)  ×  (constant fixed by an even function of μ̄₁₂₃ = 1)

and **all** of the content is in the scale. Deriving `E_EM` therefore reduces to
deriving that scale — which is a different and better-posed question than
"find the topological invariant", and it is *not* answered by anything above.

## The other front, checked — and it refutes a hypothesis of mine

The same invariant gates the ³He mirror residual, so the mirror data is a
second constraint on one unknown. I went looking for a specific agreement and
**did not find it**; recording that because a hoped-for confirmation that fails
is worth as much as one that lands.

**The hypothesis.** Point 3 above says the topological factor contributes a
*constant*. `mirror-nuclei-coulomb-systematics.witness.json` describes its
ratio as *"≈constant across A=3–39"*, `0.84 ± 0.06`, from a canonical
uniform-sphere Coulomb with no free parameter. Two independent routes both
saying "constant" would have been a real cross-check.

**It is not constant.** Re-reading the witness's own eight rows
([`mirror_ratio_a_trend_probe.py`](../computations/audits/mirror_ratio_a_trend_probe.py),
exact `Fraction` arithmetic, read-only):

| statistic | value |
|---|---|
| Pearson `r` (ratio vs `A`) | **0.830** |
| `t`, 6 dof | **3.65** (crit 2.447 ⇒ **p < 0.05**) |
| slope | `+0.0044` per unit `A` |
| line at `A=3` → `A=39` | `0.774` → `0.934` |
| rms about the line | `0.0329` |
| rms about the mean | `0.0589` — **44 % worse** |

The ratio rises monotonically with `A`. The scatter the witness reports as
`± 0.06` is not noise about a constant; it is a trend, and a straight line
describes the eight points substantially better than their mean does.

**Two consequences.**

1. **The cross-check does not land.** The mirror data does *not* corroborate
   "the correction is a constant". It does not refute the Lean either — the
   mirror ratio is an *inter*-nucleon Coulomb comparison across a nucleus,
   while `E_EM` is *intra*-nucleon, and the `A`-trend is at least as likely to
   be the uniform-sphere model improving with `A` as anything about `E_EM`.
   **Do not read the trend as evidence that `E_EM` is `A`-dependent.** What is
   established is only that the hoped-for agreement is absent.
2. **The `A=3` number is not the quoted one**, and `A=3` is exactly the case
   4-B needs. Anyone reaching for the chain mean for the ³He case is off by
   ~1.15 sd.

### Follow-up (same day): the witness is numerically stale, and the trend survives it

Correcting the numbers above, and adding a finding the first pass missed.

`coulomb_energy.mirror_displacement_mev` **has changed on `main`** since the
witness was computed (2026-07-11). The committed `coulomb_canonical` column no
longer reproduces — and the change is an **exactly uniform rescale**, factor
`1.178176504688906`, identical across all eight pairs to 19 significant figures.
A normalisation change, not a model change.

| | committed (stale) | live recompute |
|---|---|---|
| chain mean | 0.8376 | **0.9868** |
| `A=3` (³H/³He) | 0.7650 | **0.9013** |
| Pearson `r` | 0.83049 | **0.83049** |
| `t` (6 dof) | 3.6520 | **3.6520** |

**The trend finding is untouched.** Pearson `r` and `t` are invariant under
rescaling one variable, so they are *identical* on the stale and live numbers —
the monotone trend is real either way. What moves is only the absolute level.

**But the witness's interpretation is now stale too**, and that is new. Its
narrative explains "the ~0.8 factor" as *"the known uniform-sphere
over-estimate"*. At the live normalisation the mean is **0.987** — there is no
over-estimate left to explain.

**The producer was also broken.** It raised `TypeError: unsupported format
string passed to mpf.__format__` and could not run **at all**, on `main`,
before this branch — a third instance of the mpf-formatting class fixed in
PR #5615. Fixed here, along with the "≈constant" wording and a trend block that
puts per-`A` statistics into the witness so no consumer has to take a mean on
trust.

### What the rescale actually is — the pion IS the nuclear length scale

Traced, because "the witness is stale" is the uninteresting half. The factor
`1.178176504688906` decomposes exactly into two **de-empiricisations** in
[`coulomb_energy.py`](../computations/coulomb_energy.py), neither a regression:

| change | factor | what it removes |
|---|---|---|
| `r₀ = 1.2 fm` → `λ̄_π = ℏc/m_π` (CAL-3 derived) | `1.1781808` | the empirical saturation length |
| `α_EM` CODATA → framework-derived | `3.6` ppm | an experimental input from a *predicted* observable |

`R0_FM = LAMBDA_BAR_PI_FM`, with `R0_FM_EMPIRICAL = 1.2` retained "for
comparison; NOT the default". The α residual is the module's own figure — its
comment states *"derived 1/α_EM = 137.035935094 vs CODATA 137.035999177, i.e.
468 ppb apart, shifting E_C by 3.6 ppm"*, which is the residual measured here to
the digit.

**And this is the owner's meson/pion pointer, already realised in the corpus.**
The nuclear Coulomb radius is the **pion Compton wavelength**. The consequence is
not cosmetic:

| length scale | chain mean `split/ΔE_C` | reading |
|---|---:|---|
| empirical `r₀ = 1.2 fm` | `0.838` | ~19 % over-prediction, excused as "the known uniform-sphere over-estimate" |
| derived `λ̄_π = ℏc/m_π` | **`0.987`** | ~1.3 %, **with no empirical length constant anywhere** |

Removing the fitted length made the agreement *better* by an order of magnitude
in the residual. The witness's "over-estimate" narrative was an artifact of
`r₀ = 1.2`, and there is now essentially nothing for it to explain.

**Do not over-read it.** The model is still a classical uniform-sphere Coulomb
energy compared against AME binding differences; what is derived is the *length
scale*, not the mechanism. And the `A`-trend survives at `r = 0.830` — the
*level* improved dramatically, the *structure* did not go away. Whatever produces
that trend is still open.

**The witness is deliberately NOT regenerated on this branch.** Regenerating
moves every number by the factor above, and that is an upstream `coulomb_energy`
change this branch has not audited. Baking it into an SM-front PR would
misattribute it. Whoever regenerates should audit that change and say so.

## Honest status

`E_EM` is **not derived**. What this session added is: one invariant identified
as the only possible input, one constraint on the map's parity, two meson-route
bridges closed with proofs, and the observation that the topology contributes a
constant so the remaining problem is entirely a scale. No value is claimed and
nothing is wired.
