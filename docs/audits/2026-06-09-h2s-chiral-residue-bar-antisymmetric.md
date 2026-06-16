# The H₂S +2.1° is the bar-anti-symmetric (chiral) residue

**Date:** 2026-06-09. **Status:** identification clean; exact magnitude open
(S³ curvature integral). **Compute:**
[`h2s_chiral_residue_bar_antisymmetric.py`](../../computations/h2s_chiral_residue_bar_antisymmetric.py).

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

## The chiral channel, pinned exactly (S³ holonomy)

The framework's chirality machinery
([`chirality-residue-mass-term.md`](../../content/quantum-observable-universe/mass-theory/chirality-residue-mass-term.md),
[`residue-as-braid-holonomy.md`](../../content/quantum-observable-universe/mass-theory/residue-as-braid-holonomy.md))
pins the chiral channel exactly. A Wedderburn block is a **chirality cell** iff
its signed Young content `c_λ = Σ_{(i,j)∈λ}(j−i) = 0`, equivalently the q-Dirac
curvature `D_q²(λ) = [c_λ]_q² = 0`. For H₃:

| block | `c_λ` | `D_q² = [c_λ]_q²` | chirality cell? |
|---|---|---|---|
| sym (3) | +3 | 9.26 | no |
| **std (2,1)** | **0** | **0** | **yes** ← |
| alt (1,1,1) | −3 | 9.26 | no |

So the chiral channel is **exactly the (2,1) standard block** — the q-Dirac
kernel — the same block the chiral p-orbital occupies (defect 2). And the
residue is the **holonomy ρ(β) of the braid loop around the singular fibre**
`ζ_ℓ` — the q-deformed **Chern–Simons holonomy of a Wilson loop in S³** around
the obstruction divisor.

Therefore the H₂S +2.1° **is** the S³ braid-holonomy of the chiral p-lone on the
`c_λ=0` (2,1) cell. The exact angle is the **monodromy phase around `ζ_ℓ`** — the
one remaining compute. Channel and mechanism are now exactly identified;
compute: [`h2s_chirality_residue_s3_holonomy.py`](../../computations/h2s_chirality_residue_s3_holonomy.py).
