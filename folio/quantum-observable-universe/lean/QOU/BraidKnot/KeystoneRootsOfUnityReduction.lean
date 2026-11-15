import QOU.BraidKnot.PolynomialShadowRigidity

/-!
# The keystone's `q₀` step reduces to a root-of-unity statement

`bwS0_eq_hecke` — the keystone's open core — asks that the Beasley–Witten
`S³/2I` path-integral vacuum row equal the Hecke modular datum `d_q(λ)/D` at the
substrate anchor `q₀ ≈ 1.10998`. The standing framing treats the `q₀` step as an
**archimedean continuation** of a root-of-unity object, and that framing is what
`HabiroDomainVanishing.lean` (#4957/#4962) showed cannot be carried out for a
Habiro element: the `(q;q)_k`-adic completion diverges at real `q > 1`.

This file records the reduction that makes the continuation step unnecessary.

## The statement

If both sides are **rational functions of `q`** — each presented as a ratio of
polynomials — then agreement at **all roots of unity** already forces agreement
at `q₀`. No continuation, no completion, no analytic input:
`eq_of_eval_eq_on_rootsOfUnity` (proved in `PolynomialShadowRigidity.lean`) does
the work, because the roots of unity are an infinite test set and a polynomial
identity holding on an infinite set holds identically.

So the keystone's `q₀` obligation is not a *separate* archimedean obligation. It
is discharged the moment the root-of-unity match is, which is where the RT/WRT
machinery natively lives.

## The hypotheses, and which one is open

The Hecke side is manifestly rational: `d_q(λ)` is a Laurent polynomial (bean
`qou-2v7k`, item (i)), so `d_λ²/Σ_μ d_μ²` is a ratio of polynomials after
clearing the pole at `q = 0`.

**The load-bearing hypothesis is that the BW / path-integral side is also
rational.** That is *not* proved here and is not assumed to be true — it is an
explicit hypothesis of every theorem below, supplied by the caller. It is
precisely the open construction tracked as `bwse`. Per AGENTS.md
§"Axiomatization is NOT a Proof", stating it as a hypothesis is not progress on
proving it; the content of this file is only that *given* rationality, the `q₀`
step is free.

The theorems are stated for arbitrary `F G : ℂ → ℂ` with explicit rational
presentations, so nothing about the specific keystone data is smuggled in — the
conclusion is derived from the hypotheses, not projected out of a field carrying
it (§3b-cond item 5).

## What this does NOT claim

* It does **not** prove `bwS0_eq_hecke`, at roots of unity or anywhere else.
* It does **not** show the BW side is rational; that is the open input.
* It does **not** supply the root-of-unity match. `PolynomialShadowRigidity.lean`'s
  companion probe measures how far the *available* fibre data is from pinning the
  Hecke side by interpolation alone: for the n=5 vacuum row
  `S_0λ² = d_λ²/Σd²` with `d_q = ([1]_q, [4]_q, [5]_q, [4]_q[3]_q/[2]_q)`, the
  reduced degrees demand **25..33** values while Σ(2,3,5) supplies **5**. The
  reduction below needs agreement at *every* root of unity, which is a structural
  statement to be proved, not a finite table to be extended.

Scope-(a): a conditional reduction. It excludes no ingredient and refutes no route.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/

namespace QOU.BraidKnot.Keystone

open Polynomial

/-- `F` is presented as the rational function `num/den` wherever `den` does not
vanish. This is data supplied by the caller, not an assertion that any particular
object admits such a presentation. -/
structure RationalPresentation (F : ℂ → ℂ) where
  /-- Numerator polynomial. -/
  num : Polynomial ℂ
  /-- Denominator polynomial. -/
  den : Polynomial ℂ
  /-- `F` agrees with `num/den` away from the zeros of `den`. -/
  eq_ratio : ∀ z : ℂ, den.eval z ≠ 0 → F z = num.eval z / den.eval z

/-- **The reduction.** Two functions with rational presentations whose
denominators are nonvanishing on the roots of unity, and which agree at every
root of unity, agree at **every** point where both denominators are nonzero — the
substrate anchor `q₀` included.

The archimedean step is therefore not an extra obligation: it is a consequence of
the root-of-unity match together with rationality. -/
theorem eq_of_rational_and_agree_on_rootsOfUnity {F G : ℂ → ℂ}
    (pF : RationalPresentation F) (pG : RationalPresentation G)
    (hdF : ∀ z : ℂ, IsRootOfUnity z → pF.den.eval z ≠ 0)
    (hdG : ∀ z : ℂ, IsRootOfUnity z → pG.den.eval z ≠ 0)
    (hagree : ∀ z : ℂ, IsRootOfUnity z → F z = G z)
    {x : ℂ} (hxF : pF.den.eval x ≠ 0) (hxG : pG.den.eval x ≠ 0) :
    F x = G x := by
  have hratio : ∀ z : ℂ, IsRootOfUnity z →
      pF.num.eval z / pF.den.eval z = pG.num.eval z / pG.den.eval z := by
    intro z hz
    rw [← pF.eq_ratio z (hdF z hz), ← pG.eq_ratio z (hdG z hz)]
    exact hagree z hz
  have hmul : pF.num * pG.den = pG.num * pF.den :=
    mul_eq_of_ratio_agree_on_rootsOfUnity hdF hdG hratio
  rw [pF.eq_ratio x hxF, pG.eq_ratio x hxG]
  exact ratio_eval_eq_of_mul_eq hmul hxF hxG

/-- The keystone reading, with the substrate anchor named. `q₀` enters only as a
point at which both denominators are nonzero — an explicit, checkable side
condition on the concrete polynomials, not an assumption about `q₀` itself. -/
theorem keystone_q0_step_is_free {F G : ℂ → ℂ}
    (pF : RationalPresentation F) (pG : RationalPresentation G)
    (hdF : ∀ z : ℂ, IsRootOfUnity z → pF.den.eval z ≠ 0)
    (hdG : ∀ z : ℂ, IsRootOfUnity z → pG.den.eval z ≠ 0)
    (hagree : ∀ z : ℂ, IsRootOfUnity z → F z = G z)
    (q₀ : ℂ) (hF : pF.den.eval q₀ ≠ 0) (hG : pG.den.eval q₀ ≠ 0) :
    F q₀ = G q₀ :=
  eq_of_rational_and_agree_on_rootsOfUnity pF pG hdF hdG hagree hF hG

/-- **Non-vacuity.** `RationalPresentation` is inhabited by a genuine rational
function — the identity, presented as `X / 1`. This witnesses that the theorems
above are not statements about an empty structure; it is not a model of either
side of `bwS0_eq_hecke`. -/
noncomputable example : RationalPresentation (fun z : ℂ => z) where
  num := Polynomial.X
  den := 1
  eq_ratio := by intro z _; simp

/-- The reduction is not vacuous either: applied to two presentations of the same
function it returns the expected equality. A shape check, not evidence. -/
example (q₀ : ℂ) :
    (fun z : ℂ => z) q₀ = (fun z : ℂ => z) q₀ := by
  refine keystone_q0_step_is_free
    (F := fun z : ℂ => z) (G := fun z : ℂ => z)
    ⟨Polynomial.X, 1, by intro z _; simp⟩ ⟨Polynomial.X, 1, by intro z _; simp⟩
    (by intro z _; simp) (by intro z _; simp) (fun _ _ => rfl) q₀ ?_ ?_ <;> simp

end QOU.BraidKnot.Keystone
