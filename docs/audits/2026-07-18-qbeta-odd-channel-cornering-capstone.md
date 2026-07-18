# Q_β odd-channel (c₃ swing) — the cornering capstone

**Date:** 2026-07-18 · **Branch:** `claude/faddeev-phi-b-construction-wwblhu` ·
**Tier:** synthesis / campaign state (no new claim; consolidates the session's
landed results). No `c_k` wired; scope-(a) throughout.

## The problem

L2 (per-observable 100×) fails for Q_β because the c₃ bar-odd "S" quantity swings
2.44 % between the two q₀ anchors while q₀ itself moves ~1e-8 — a ~3.84×10⁶
representational amplification. `S = A/u³` with `A(q)` smooth crossing zero at q*
and `A′(q*) ≈ 2.37` (`BarOddLadderShape`, #3621/#3660). The question this
campaign has driven: **is that swing carried by any smooth geometric or resurgent
object, or is it intrinsically the 1/u³ inversion of a smooth numerator, pinned
by experimental Q_β?**

## What is now closed (this session + siblings)

**Every geometric route on 4₁ is closed:**

| Route | Result | Ref |
|-------|--------|-----|
| Deformed median resummation | smooth / anchor-blind (∝ δ) | #3813 |
| Classical CS / Stokes constant | anchor-invariant (Lean-proved prune `no_anchor_invariant_realizes_swing`) | #3813 |
| 5₂ σ1 quantum volume 𝔙_q | anchor-smooth, max \|d𝔙/dq\|=1.47 (~6 orders short) | #3902 |
| Substrate-meridian branch point | generic — 0.11 from nearest 4₁/5₂ branch point (~8.6e6× the anchor gap); det J(q₀)=4.37 | #3902 |

**The resurgent 4₁ lane is complete:**

| Result | Ref |
|--------|-----|
| Exact Ohtsuki κ-ladder κ₁..κ₇ (state-integral fluctuation invariants) | #3606/#3628/#3683 |
| Bar-parity = the √3-grading of the 4₁ cusp trace field ℚ(√3); bar-odd b-dictionary = closed-form √3-subladder {κ₁,κ₃,κ₅,κ₇}; F1's odd-k D-ladder is √3-dominated (unifies #3861's G2 2-adic grading) | #3916 |
| d↔κ bridge pruned: the one-instanton Borel action is **Vol(4₁)/π** (shared across κ-ladder, C1 even channel, corpus tower — A₆=0.6303 vs tower Re 0.6310); the bridge needs no new action | #3916 |
| Stokes constant = **integer 3** (GGM-proved #3872), confirmed from the κ amplitude (2πC_n→3); the amplitude is **parity-blind** (√3 is the rung grading, not a separate odd Stokes constant) | #3916 |
| 4₁ deformed Stokes amplitude is **real** — the odd-phase null; A_ω is not a 4₁ Stokes phase at any level | #3923 |
| ħ↔2πi/N wall is load-bearing: Kashaev fluctuation tower ≠ b-tower phase law term-by-term (a campaign category-error guard) | #3938 |

**Synthesis of the closed part.** On 4₁, the swing is carried by no smooth
geometric object and no resurgent Stokes datum. Both the substrate→geometry map
(branch-point generic) and the resurgent transseries (odd-phase null, real
amplitude) exclude a 4₁ source. The swing is **representational** — the 1/u³
inversion of the smooth N_odd, pinned by experimental Q_β. This is a
scope-(a)/(b) result: (a) no 4₁ construction *alone* reproduces the swing; (b)
the 4₁ odd-phase null is a *proved* structural exclusion (amphichirality ⇒ real
deformed amplitude) of a 4₁-Stokes source.

## The one live frontier — the 5₂ σ3-pair

The 4₁ null explicitly points elsewhere: "the odd channel must source from
non-amphichiral (5₂-class) geometry" (#3923). The 5₂ port (#3930,
`FiveTwoSaddleCurve.lean` Lean-proved) makes this concrete and **falsifiable**:

- 5₂ is chiral (CS ≠ 0): the u=0 singularities already include the genuinely
  complex ι₁₃ = −0.39349 − 0.65852i (vs 4₁'s real ι).
- **Deformed prediction:** the σ1-pair stays kinematic (ι̃₁₂ arg−kinematic =
  −8e-53, like 4₁), but the **σ3-pairs carry a NONZERO intrinsic phase** —
  ι̃₁₃: −2.127 rad, ι̃₂₃: −2.683 rad — vs the 4₁ null floor 9.2e-9. This is the
  bar-odd carrier the 4₁ null excluded. Falsifiable target for the #3892 5₂
  ladder: measuring ~0 kills the non-amphichiral-carrier hypothesis.

## The decisive remaining test (this branch, item 2)

A nonzero intrinsic *phase* is necessary but not sufficient for the swing — the
σ3-pair must also be **anchor-dependent** at the ~3.84×10⁶ scale. Every geometric
object tested so far (including the 5₂ σ1 quantum volume, #3902) is anchor-smooth
(O(1)). The open question: **is the 5₂ σ3-pair datum ι₁₃ anchor-smooth too, or
does it carry the swing?** If anchor-smooth, the odd-channel geometric search
closes entirely (representational confirmed on every front, chiral included); if
swing-carrying, the σ3-pair is the long-sought non-amphichiral carrier. This is
the one test that decides whether the 5₂-class lane can close the odd channel.

## Discipline

No `c_k` wired; registry untouched; scope-(a)/(b) with cited invariants; the 4₁
odd-phase null is a proved exclusion (b), the anchor-smoothness results are
scope-limited negatives (a). ħ↔2πi/N: perturbative objects only; μ never fixed
from QOU data.
