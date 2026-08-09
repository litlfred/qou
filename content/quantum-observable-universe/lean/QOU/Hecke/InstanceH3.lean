import QOU.Hecke.FullRank
import QOU.Mathlib.HeckeAlgebra
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# `QOU.Hecke.InstanceH3` — the three-strand Hecke algebra, with the braid relation

`QOU.Hecke.InstanceH2` supplied `H₂(q)` and said plainly that it "is not evidence
for `n ≥ 3`": at `n = 2` the braid relation is vacuous. This file supplies `n = 3`,
where it is not.

## Where the content comes from

`QOU.Mathlib.HeckeAlgebra` already carried the concrete six-dimensional carrier
`H3Carrier R = R⁶`, the two generator-action maps `H3.mulSigma1` / `H3.mulSigma2`,
the full multiplication `H3.mul`, and machine-checked proofs of the quadratic and
braid relations *in generator-action form*. What it lacked — and what blocked the
`HeckeAlgebra` instance, since the class demands `[Ring A] [Algebra R A]` — was
**associativity of `H3.mul`**.

`H3.mul_assoc` below closes it. Every coefficient of `H3.mul` is polynomial in the
six components and the single scalar `q - q⁻¹`, so associativity is a polynomial
identity in 18 variables and `ring` discharges it componentwise. That it *is* an
identity is the real content: it says `H3.mulSigma1` and `H3.mulSigma2` are a
faithful transcription of left multiplication in `H₃(q)`.

## Why a type synonym

`H3Carrier R` is an `abbrev` for `R × R × R × R × R × R`, so it already carries
`Prod`'s **componentwise** `CommRing`. Putting the Hecke multiplication on it
directly would collide with that instance. `H3Alg R q` is a `def`, opaque to
instance search, so it takes the additive structure from the product (which is
correct — `H₃(q)` really is `R⁶` as a module) and the multiplication from `H3.mul`.

## What this establishes that `H2` did not

At `n = 3` there are two generators, `Generator.adjacent` is satisfiable, and
`braid` has to be discharged with actual content: `σ₁σ₂σ₁ = σ₂σ₁σ₂`. It also has
full Iwahori rank `6 = 3!` (`instIsHeckeOfFullRankH3`), so it is not one of the
degenerate models `QOU.Hecke.not_isHeckeOfFullRank_rankOne` rules out.
-/

namespace QOU.Hecke.InstanceH3

open QOU.Mathlib.HeckeAlgebra

universe u

variable {R : Type u} [Field R] {q : R}

/-! ## Carrier-level ring laws

Everything here is stated on `H3Carrier R` with the product's `+`, `0` and the
standalone `H3.mul`, so that the `Ring` instance below can take each field by
`rfl`-transfer through the type synonym. -/

section Carrier

variable (q)

/-- **Associativity of `H3.mul`** — the lemma the whole H3 instance was waiting
on. Each of the six output coefficients is a polynomial in the eighteen input
coefficients and `q - q⁻¹`, so `ring` settles it componentwise.

This is a genuine fact about `H3.mulSigma1` / `H3.mulSigma2`: it fails for an
arbitrary pair of `6 × 6` matrices, and holds here because those two maps encode
left multiplication by `σ₁` and `σ₂` subject to the Hecke and braid relations. -/
theorem H3.mul_assoc (x y z : H3Carrier R) :
    H3.mul q (H3.mul q x y) z = H3.mul q x (H3.mul q y z) := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  obtain ⟨c1, c2, c3, c4, c5, c6⟩ := z
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- `x · 1 = x`. The companion `H3.one_mul` is already in
`QOU.Mathlib.HeckeAlgebra`; this side needs the six generator-action maps to send
`1` to the right basis vector, which is exactly what makes the basis ordering
correct. -/
theorem H3.mul_one (x : H3Carrier R) : H3.mul q x (H3.one R) = x := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  simp only [H3.mul, H3.one, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add,
    Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

theorem H3.mul_add (x y z : H3Carrier R) :
    H3.mul q x (y + z) = H3.mul q x y + H3.mul q x z := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  obtain ⟨c1, c2, c3, c4, c5, c6⟩ := z
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.mk_add_mk,
    Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

theorem H3.add_mul (x y z : H3Carrier R) :
    H3.mul q (x + y) z = H3.mul q x z + H3.mul q y z := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  obtain ⟨c1, c2, c3, c4, c5, c6⟩ := z
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.mk_add_mk,
    Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

theorem H3.zero_mul (y : H3Carrier R) : H3.mul q 0 y = 0 := by
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  show H3.mul q ((0 : R), (0 : R), (0 : R), (0 : R), (0 : R), (0 : R)) _
      = ((0 : R), (0 : R), (0 : R), (0 : R), (0 : R), (0 : R))
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

theorem H3.mul_zero (x : H3Carrier R) : H3.mul q x 0 = 0 := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  show H3.mul q _ ((0 : R), (0 : R), (0 : R), (0 : R), (0 : R), (0 : R))
      = ((0 : R), (0 : R), (0 : R), (0 : R), (0 : R), (0 : R))
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- Scalars pass through the left argument. -/
theorem H3.smul_mul (r : R) (x y : H3Carrier R) :
    H3.mul q (r • x) y = r • H3.mul q x y := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.smul_mk,
    smul_eq_mul, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- …and through the right argument. -/
theorem H3.mul_smul (r : R) (x y : H3Carrier R) :
    H3.mul q x (r • y) = r • H3.mul q x y := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.smul_mk,
    smul_eq_mul, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-! ### The Hecke relations at carrier level

`QOU.Mathlib.HeckeAlgebra` proves these over `ℝ` in *generator-action* form
(`H3.mulSigma1 q (H3.sigma1 ℝ) = …`). Restated here over an arbitrary field as
equations in `H3.mul`, which is the form `HeckeQuadratic` and `BraidRelation`
ask for once the ring structure exists. -/

theorem H3.sigma1_sq_carrier :
    H3.mul q (H3.sigma1 R) (H3.sigma1 R)
      = (q - q⁻¹) • H3.sigma1 R + H3.one R := by
  simp only [H3.mul, H3.sigma1, H3.one, H3.mulSigma1, H3.mulSigma2, H3.smul,
    H3.add, Prod.smul_mk, smul_eq_mul, Prod.mk_add_mk, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

theorem H3.sigma2_sq_carrier :
    H3.mul q (H3.sigma2 R) (H3.sigma2 R)
      = (q - q⁻¹) • H3.sigma2 R + H3.one R := by
  simp only [H3.mul, H3.sigma2, H3.one, H3.mulSigma1, H3.mulSigma2, H3.smul,
    H3.add, Prod.smul_mk, smul_eq_mul, Prod.mk_add_mk, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- **The braid relation at carrier level**: both sides are the longest element
of `S₃`, basis position 6. -/
theorem H3.braid_carrier :
    H3.mul q (H3.mul q (H3.sigma1 R) (H3.sigma2 R)) (H3.sigma1 R)
      = H3.mul q (H3.mul q (H3.sigma2 R) (H3.sigma1 R)) (H3.sigma2 R) := by
  simp only [H3.mul, H3.sigma1, H3.sigma2, H3.mulSigma1, H3.mulSigma2, H3.smul,
    H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

end Carrier

/-! ## The algebra -/

/-- **`H₃(q)`** — the carrier `R⁶` with `H3.mul` as its multiplication.

A `def`, not an `abbrev`: `H3Carrier R` reduces to `R × R × R × R × R × R`, whose
`Prod` `CommRing` instance multiplies componentwise. Opacity is what keeps that
instance from being found in place of the Hecke one. -/
def H3Alg (R : Type u) [Field R] (_q : R) : Type u := H3Carrier R

namespace H3Alg

instance : AddCommGroup (H3Alg R q) := inferInstanceAs (AddCommGroup (H3Carrier R))

instance : Module R (H3Alg R q) := inferInstanceAs (Module R (H3Carrier R))

instance : Mul (H3Alg R q) := ⟨fun x y => H3.mul q x y⟩

instance : One (H3Alg R q) := ⟨H3.one R⟩

instance instRing : Ring (H3Alg R q) where
  __ := inferInstanceAs (AddCommGroup (H3Alg R q))
  mul_assoc := H3.mul_assoc q
  one_mul := H3.one_mul q
  mul_one := H3.mul_one q
  left_distrib := H3.mul_add q
  right_distrib := H3.add_mul q
  zero_mul := H3.zero_mul q
  mul_zero := H3.mul_zero q

instance instAlgebra : Algebra R (H3Alg R q) :=
  Algebra.ofModule (H3.smul_mul q) (H3.mul_smul q)

/-- The generator `σ₁`. -/
def sigma1 : H3Alg R q := H3.sigma1 R

/-- The generator `σ₂`. -/
def sigma2 : H3Alg R q := H3.sigma2 R

end H3Alg

/-! ## The Hecke relations, in ring form

Each is the corresponding carrier lemma transported through the type synonym:
`H3Alg R q` is definitionally `H3Carrier R`, `*` is `H3.mul q`, `1` is `H3.one R`,
and `+`/`•` are the product's — so the transport is `rfl`, and the mathematical
content stays where it was proved. -/

open H3Alg

/-- `σ₁² = (q − q⁻¹)·σ₁ + 1`. -/
theorem sigma1_sq : (sigma1 : H3Alg R q) * sigma1 = (q - q⁻¹) • sigma1 + 1 :=
  H3.sigma1_sq_carrier q

/-- `σ₂² = (q − q⁻¹)·σ₂ + 1`. -/
theorem sigma2_sq : (sigma2 : H3Alg R q) * sigma2 = (q - q⁻¹) • sigma2 + 1 :=
  H3.sigma2_sq_carrier q

/-- **The braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂` — the thing `n = 2` could not see. -/
theorem braid : (sigma1 : H3Alg R q) * sigma2 * sigma1 = sigma2 * sigma1 * sigma2 :=
  H3.braid_carrier q

/-! ## The basis, and that the generators reach all of it -/

/-- `σ₁σ₂` is basis position 4. -/
theorem sigma1_mul_sigma2 :
    (sigma1 : H3Alg R q) * sigma2 = H3.sigma1Sigma2 R := by
  show H3.mul q (H3.sigma1 R) (H3.sigma2 R) = _
  simp only [H3.mul, H3.sigma1, H3.sigma2, H3.sigma1Sigma2, H3.mulSigma1,
    H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- `σ₂σ₁` is basis position 5. -/
theorem sigma2_mul_sigma1 :
    (sigma2 : H3Alg R q) * sigma1 = H3.sigma2Sigma1 R := by
  show H3.mul q (H3.sigma2 R) (H3.sigma1 R) = _
  simp only [H3.mul, H3.sigma1, H3.sigma2, H3.sigma2Sigma1, H3.mulSigma1,
    H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- `σ₁σ₂σ₁` is basis position 6 — the longest element of `S₃`. -/
theorem sigma1_mul_sigma2_mul_sigma1 :
    (sigma1 : H3Alg R q) * sigma2 * sigma1 = H3.sigma1Sigma2Sigma1 R := by
  show H3.mul q (H3.mul q (H3.sigma1 R) (H3.sigma2 R)) (H3.sigma1 R) = _
  simp only [H3.mul, H3.sigma1, H3.sigma2, H3.sigma1Sigma2Sigma1, H3.mulSigma1,
    H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-- **Every element is an `R`-combination of words in the generators.** This is
what `spans` needs: the six basis vectors are `1`, `σ₁`, `σ₂`, `σ₁σ₂`, `σ₂σ₁`,
`σ₁σ₂σ₁`, so any `x` lies in the subalgebra generated by `{σ₁, σ₂}`. -/
theorem decompose (x : H3Alg R q) :
    x = x.1 • (1 : H3Alg R q) + x.2.1 • sigma1 + x.2.2.1 • sigma2
      + x.2.2.2.1 • (sigma1 * sigma2) + x.2.2.2.2.1 • (sigma2 * sigma1)
      + x.2.2.2.2.2 • (sigma1 * sigma2 * sigma1) := by
  rw [sigma1_mul_sigma2_mul_sigma1, sigma1_mul_sigma2, sigma2_mul_sigma1]
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  show (_ : H3Carrier R)
      = a1 • H3.one R + a2 • H3.sigma1 R + a3 • H3.sigma2 R
        + a4 • H3.sigma1Sigma2 R + a5 • H3.sigma2Sigma1 R
        + a6 • H3.sigma1Sigma2Sigma1 R
  simp only [H3.one, H3.sigma1, H3.sigma2, H3.sigma1Sigma2, H3.sigma2Sigma1,
    H3.sigma1Sigma2Sigma1, Prod.smul_mk, smul_eq_mul, Prod.mk_add_mk,
    Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩

/-! ## The `HeckeAlgebra` instance at `n = 3` -/

/-- The generator embedding: `Generator 3` carries `idx : Fin 2`, so index `0` is
`σ₁` and index `1` is `σ₂`. -/
def embed3 (g : Generator 3) : H3Alg R q :=
  if g.idx.val = 0 then sigma1 else sigma2

@[simp] theorem embed3_zero : embed3 (R := R) (q := q) ⟨0⟩ = sigma1 := rfl

@[simp] theorem embed3_one : embed3 (R := R) (q := q) ⟨1⟩ = sigma2 := rfl

/-- Every `Generator 3` is `⟨0⟩` or `⟨1⟩`. -/
theorem generator_three_cases (g : Generator 3) : g = ⟨0⟩ ∨ g = ⟨1⟩ := by
  obtain ⟨⟨v, hv⟩⟩ := g
  interval_cases v
  · exact Or.inl rfl
  · exact Or.inr rfl

/-- **`H₃(q)` is a Hecke algebra**, braid relation and all.

Unlike `InstanceH2.instHeckeAlgebraH2`, `braid` here is not vacuous: `Generator 3`
has two indices, they are adjacent, and the relation is discharged by `braid`
above — the first non-vacuous braid relation anywhere in the tree. -/
instance instHeckeAlgebraH3 : HeckeAlgebra R 3 q (H3Alg R q) where
  embed := embed3
  quadratic := by
    intro i
    rcases generator_three_cases i with rfl | rfl
    · simpa using sigma1_sq (R := R) (q := q)
    · simpa using sigma2_sq (R := R) (q := q)
  braid := by
    intro i j _
    rcases generator_three_cases i with rfl | rfl <;>
      rcases generator_three_cases j with rfl | rfl <;>
      simp only [embed3_zero, embed3_one]
    · exact braid
    · exact braid.symm
  farCommute := by
    intro i j hij
    obtain ⟨hne, hadj⟩ := hij
    exact absurd
      (by
        rcases generator_three_cases i with rfl | rfl <;>
          rcases generator_three_cases j with rfl | rfl
        · exact absurd rfl hne
        · exact Or.inl rfl
        · exact Or.inr rfl
        · exact absurd rfl hne)
      hadj
  spans := by
    refine le_antisymm le_top ?_
    rintro x -
    have hs1 : (sigma1 : H3Alg R q) ∈ Algebra.adjoin R (Set.range (embed3 (R := R) (q := q))) :=
      Algebra.subset_adjoin ⟨⟨0⟩, rfl⟩
    have hs2 : (sigma2 : H3Alg R q) ∈ Algebra.adjoin R (Set.range (embed3 (R := R) (q := q))) :=
      Algebra.subset_adjoin ⟨⟨1⟩, rfl⟩
    rw [decompose x]
    exact Subalgebra.add_mem _
      (Subalgebra.add_mem _
        (Subalgebra.add_mem _
          (Subalgebra.add_mem _
            (Subalgebra.add_mem _
              (Subalgebra.smul_mem _ (Subalgebra.one_mem _) _)
              (Subalgebra.smul_mem _ hs1 _))
            (Subalgebra.smul_mem _ hs2 _))
          (Subalgebra.smul_mem _ (Subalgebra.mul_mem _ hs1 hs2) _))
        (Subalgebra.smul_mem _ (Subalgebra.mul_mem _ hs2 hs1) _))
      (Subalgebra.smul_mem _ (Subalgebra.mul_mem _ (Subalgebra.mul_mem _ hs1 hs2) hs1) _)

/-! ## …and it has the full Iwahori rank -/

instance : Module.Free R (H3Alg R q) := inferInstanceAs (Module.Free R (H3Carrier R))

instance : Module.Finite R (H3Alg R q) := inferInstanceAs (Module.Finite R (H3Carrier R))

/-- `H₃(q)` is six-dimensional over `R`. -/
theorem finrank_H3Alg : Module.finrank R (H3Alg R q) = 6 := by
  show Module.finrank R (H3Carrier R) = 6
  simp [Module.finrank_prod, Module.finrank_self]

/-- **`H₃(q)` has the full Hecke rank** `6 = 3!`, so it is not one of the
degenerate models `QOU.Hecke.not_isHeckeOfFullRank_rankOne` excludes. Together
with `instHeckeAlgebraH3` this is the first object in the tree that is honestly
`H_n(q)` at a level where the braid relation has content. -/
instance instIsHeckeOfFullRankH3 : IsHeckeOfFullRank R 3 (H3Alg R q) where
  free := inferInstance
  finrank_eq := by rw [finrank_H3Alg]; rfl

/-! ## The rung to `n = 4`

`isHeckeOfFullRank_succ` reduces "H₄ has rank 24" to "H₄ is free of rank 4 over
H₃" — four cosets, not a twenty-four-dimensional structure-constant computation.
The remaining work is the multiplication itself (bean qou-jr3k → H4), reconciled
with `QOU.Machinery.MarkovTraceH4`'s normal form. -/

end QOU.Hecke.InstanceH3
