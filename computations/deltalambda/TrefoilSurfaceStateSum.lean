/-
  TrefoilSurfaceStateSum.lean  —  Mathlib-FREE (core Lean 4 only, no imports).

  PROOF-TIER support for the deuteron symbolic closed-form attempt
  (docs/audits/2026-08-02-deuteron-symbolic-closed-form-trefoil-qinvariant.md).

  All declarations sorry-free, no trivial-true, no native_decide, no axiom.

  ─────────────────────────────────────────────────────────────────────────
  RESULT.  The σ₁³ trefoil scalar channel is NULL for a *structural* reason,
  not a numerical accident: the trefoil braid lives in the 2-strand Hecke
  algebra H₂(q), which is COMMUTATIVE (one generator σ₁).  Hence every
  commutator [x,y] = 0 identically, so the surface-ordering / handle-
  commutator correction (a product of commutators — sibling #4619's
  `tr[A,B] = 0`) vanishes on the trefoil by abelianness, independent of q₀.

  This is the independent, structural second confirmation of #4619's numerical
  null (writhe-normalized Jones = 0.136× ≠ 5.853×) AND of this branch's
  scan negative (no 0-parameter scalar q-invariant hits 5.853): the scalar
  H₂ channel *cannot* carry a mixed-sign chirality charge, because it is a
  single commutative scalar algebra.  The real object (an eigenphase-weighted
  per-block handle-commutator charge, naturally mixed-sign / sum-to-zero) can
  only be non-zero in the NON-abelian H₆ interface braid — the trefoil H₂ is
  abelian ⇒ handles collapse.

  We formalize (1) the surface-state-sum closed-form SHAPE aₙ(s), proving the
  trefoil coefficient, and (2) H₂(q) commutativity ⇒ every commutator is 0.
-/

namespace QOU.MassTheory.TrefoilSurfaceStateSum

/-! ## Part 1 — the surface state-sum closed-form shape (Chebyshev in `s`).

`σⁿ = aₙ(s)·σ + aₙ₋₁(s)·1` in H₂(q) with `σ² = s·σ + 1`, skein `s = √q − 1/√q`.
The closed form EXISTS (Lean-proved) but is a pure function of `s` with NO free
normalization scalar. -/

def a : Nat → Int → Int
  | 0,     _ => 0
  | 1,     _ => 1
  | (n+2), s => s * a (n+1) s + a n s

theorem a_two (s : Int) : a 2 s = s := by simp [a]

/-- The TREFOIL T(2,3): σ³ has σ¹-coefficient `s² + 1`. -/
theorem a_three (s : Int) : a 3 s = s * s + 1 := by simp [a]

/-- σ⁴ σ¹-coefficient `s³ + 2s` — independent cross-check of the recursion. -/
theorem a_four (s : Int) : a 4 s = s * (s * s + 1) + s := by simp [a]

/-- The closed form is genuinely knot-dependent (not the trivial sequence). -/
theorem a_nonconstant : a 2 1 ≠ a 3 1 := by decide

/-! ## Part 2 — H₂(q) is commutative ⇒ handle-commutator charge is null.

Model an element `c₀·1 + c₁·σ` of H₂(q) as a pair `(c₀, c₁) : Int × Int`.
Multiplication uses `σ² = s·σ + 1`:

  `(a₀+a₁σ)(b₀+b₁σ) = (a₀b₀+a₁b₁) + (a₀b₁+a₁b₀+s·a₁b₁)·σ`. -/

abbrev H2 := Int × Int

/-- H₂(q) product at skein parameter `s`. -/
def mul (s : Int) (x y : H2) : H2 :=
  (x.1 * y.1 + x.2 * y.2,
   x.1 * y.2 + x.2 * y.1 + s * (x.2 * y.2))

/-- **H₂(q) is commutative** for every skein parameter `s`. -/
theorem mul_comm (s : Int) (x y : H2) : mul s x y = mul s y x := by
  simp only [mul, Prod.mk.injEq]
  refine ⟨?_, ?_⟩
  · rw [Int.mul_comm x.1 y.1, Int.mul_comm x.2 y.2]
  · rw [Int.mul_comm y.1 x.2, Int.mul_comm y.2 x.1, Int.mul_comm y.2 x.2,
        Int.add_comm (x.1 * y.2) (x.2 * y.1)]

/-- The commutator, `[x,y] = xy − yx` componentwise. -/
def commutator (s : Int) (x y : H2) : H2 :=
  ((mul s x y).1 - (mul s y x).1, (mul s x y).2 - (mul s y x).2)

/-- **Every commutator in H₂(q) is identically zero.**  Structural reason the
    trefoil handle-commutator charge (sibling #4619's `tr[A,B]`) is null: the
    2-strand Hecke algebra is abelian, so there is no non-zero mixed-sign charge
    to supply the deuteron's `C_knot = 5.853`.  A non-zero such charge requires
    the non-abelian H₆ interface braid. -/
theorem commutator_zero (s : Int) (x y : H2) : commutator s x y = (0, 0) := by
  simp only [commutator, mul_comm s x y, Prod.mk.injEq]
  refine ⟨?_, ?_⟩ <;> omega

end QOU.MassTheory.TrefoilSurfaceStateSum

-- Verified sorry-free (lean-direct exit 0, v4.24.0, Mathlib-free):
--   #print axioms commutator_zero  ⇒  [propext, Quot.sound]   (no sorryAx)
--   #print axioms a_three          ⇒  [propext]               (no sorryAx)
