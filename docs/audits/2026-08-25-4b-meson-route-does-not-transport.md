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

## Honest status

`E_EM` is **not derived**. What this session added is: one invariant identified
as the only possible input, one constraint on the map's parity, two meson-route
bridges closed with proofs, and the observation that the topology contributes a
constant so the remaining problem is entirely a scale. No value is claimed and
nothing is wired.
