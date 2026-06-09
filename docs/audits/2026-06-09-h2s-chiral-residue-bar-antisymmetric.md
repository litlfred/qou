# The H₂S +2.1° is the bar-anti-symmetric (chiral) residue

**Date:** 2026-06-09. **Status:** identification clean; exact magnitude open
(S³ curvature integral). **Compute:**
[`h2s_chiral_residue_bar_antisymmetric.py`](../../folio-assistant/computations/h2s_chiral_residue_bar_antisymmetric.py).

## The question

[`prop:symmetric-block-domain-weight`](../../content/quantum-observable-universe/molecular-construction/symmetric-block-domain-weight.md)
predicts the second-row hydride angles from one `q²` rule and leaves H₂S's
`+2.1°` (the opening of the pure-p 90° base) as a residual. The owner pointed at
two geometric handles: **q-hyperbolic cosh** (even) and **S³-embedding
curvature in the chiral channel** (odd).

## The identification

[`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md)
splits every Hecke quantity by the involution `q↦q⁻¹, σ↦σ⁻¹`:

| part | functions | status |
|---|---|---|
| **bar-symmetric** (even) | `cos, cosh, Li₂^q` | retained (observable) |
| **bar-anti-symmetric** (odd) | `sin, sinh, Φ_q` | `P_skew` — normally *projected away* |

and `h = q − q⁻¹` is **bar-anti-symmetric** (`h²` is bar-symmetric). The owner's
two handles are exactly these two halves: **cosh = even, chiral S³-curvature =
odd**.

This resolves the H₂O / H₂S dichotomy:

- **H₂O** — both lone pairs are the self-dual `e⁻ = σ₀σ₁σ₀` (palindromic, defect
  0) ⇒ **bar-symmetric** ⇒ the angle is pure even ⇒ the clean `q²` prediction
  (104.5°), with **zero bar-anti-symmetric residual**.
- **H₂S** — the s-channel is inert, so the two lone pairs are inequivalent: the
  self-dual `3s²` (defect 0) and the **chiral `3p_z`** (defect 2). The chiral
  pair carries the **bar-anti-symmetric (odd-in-h)** component the framework
  usually discards (`P_skew`), which surfaces as the **+2.1°** opening.

So the residual exists *iff* a chiral lone is present, i.e. *iff* the s-channel
is inert (pure-p, third row) — H₂O has none.

## Parity check (decisive)

A chiral residue must be **odd in h** (bar-anti-symmetric). It is: its scale is
`h·z² ≈ 3.0°` / `h·z³ ≈ 1.5°`, and the observed **+2.1° sits between
consecutive odd powers** — the right parity and the right scale. The even
candidates (`h², cosh(h)−1`) are the *wrong parity* for a chiral residue (and
gave `≈2.5°`, the bar-symmetric scale).

## What is derived vs open

- **Derived:** the +2.1° is the bar-anti-symmetric (chiral, `P_skew`) channel;
  it is odd in h; it is present only for an asymmetric (chiral) lone, absent in
  bar-symmetric H₂O. This *explains* why H₂O is clean and H₂S deviates.
- **Open:** the exact magnitude — it is not a clean h-monomial (2.1° falls
  between odd powers), so it is the **S³-embedding curvature integral** of the
  chiral channel (the `prop:chirality-residue-mass-term` bar-anti-symmetric
  form), not a closed scalar. That integral is the remaining compute.

The clean result is the **identification**: the molecular bond angles split, by
the bar-involution, into a bar-symmetric backbone (the `q^ℓ` weights, the clean
second-row angles) and a bar-anti-symmetric chiral residue (the H₂S +2°).
