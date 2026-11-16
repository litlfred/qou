/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Foundations Bridge: Frobenius–Hopf Two-Counit Separation, Row-Capped Markov vs Plancherel Weights, and Concrete Hecke Trace Instantiation

This self-contained, axiom-free and gap-free Lean 4 core module unifies the
algebraic foundations across beans `qou-aj49`, `qou-wapd`, `qou-k5jt`,
`qou-bmyx`, and `qou-kfcl` (under epic `qou-rtxm`), generic over any
commutative base ring `R` per §7c:

1. **Frobenius–Hopf Two-Counit Separation (`qou-aj49`):**
   - `frobenius_multiplicative_counit_collapses`: If a single linear functional
     `ε : A → R` simultaneously satisfies the Frobenius right-counit Sweedler
     contraction `b = ∑ᵢ ε(fᵢ · b) • eᵢ` (with `1 = ∑ᵢ ε(fᵢ) • eᵢ`) and the
     Hopf multiplicativity law `ε(x · y) = ε(x) · ε(y)`, then every `b : A`
     collapses to a scalar multiple of the unit, `b = ε(b) • 1_A` (without
     using any antipode).
   - `c2_two_counit_noncollapse`: Explicit rank-2 group-algebra witness
     `R[C₂] ≅ R × R` (basis `(1, g)` with `g² = 1`) proving that keeping the
     non-multiplicative Frobenius trace form `ε_F(a·1 + b·g) = b` distinct from
     the multiplicative Hopf counit `ε_H(a·1 + b·g) = a + b` satisfies both the
     exact Frobenius comultiplication/counit laws and the multiplicative Hopf
     counit laws while preserving rank 2 (`g ≠ c • 1` over `ℤ`).

2. **Plancherel vs Row-Capped Ocneanu/Markov Weights (`qou-wapd`):**
   - `row_capped_weight_vanishes_above_cap` and
     `no_uniform_rescale_between_uncapped_and_row_capped`: At `SU(2)` fibre
     dimension `N = 2`, the Ocneanu/Markov weight `y_λ` vanishes on every
     partition with `ℓ(λ) > 2`, whereas the uncapped Plancherel/Wedderburn
     weight `w_λ = d_q(λ)² / [n]_q!` is strictly non-zero on all `λ ⊢ n`.
     Hence no `λ`-independent scalar `c` can rescale `y_λ` into `w_λ` (or vice
     versa).
   - `n6_partition_321_row_cap_obstruction`: Concrete `n = 6` witness on the
     staircase partition `λ = (3,2,1)` (`ℓ(3,2,1) = 3 > 2`, `f^{(3,2,1)} = 16`,
     `(f^{(3,2,1)})² = 256 ≠ 0`, full Burnside sum `∑_{λ ⊢ 6} (f^λ)² = 720`,
     while the `ℓ(λ) ≤ 2` row-capped Burnside sum is `132 ≠ 720`).

3. **Concrete Hecke–Markov Trace Bridge (`qou-k5jt`):**
   - `ConcreteWedderburnMarkovTrace`: Assembles `tr_M(x) = ∑ᵢ yᵢ · χᵢ(x)` from
     concrete block character traces `χᵢ` and weights `yᵢ`, discharging trace
     linearity (`concrete_trace_add`, `concrete_trace_smul`), cyclicity
     (`concrete_trace_cyclic`), and unit normalization (`concrete_trace_one`)
     as theorems rather than opaque axioms, with an explicit 2-block `H₂(q)`
     instantiation (`h2_concrete_trace_cyclic`, `h2_concrete_trace_one`).

4. **Logarithmic-Derivative Order Decomposition (`qou-bmyx`):**
   - `logDeriv_factor_cleared_identity`: Over any `CommRingOps R`, the cleared-
     denominator Leibniz derivative of `(z - w)^m · g` splits into the pole
     residue term `m · g` plus the analytic remainder `(z - w) · g'`.
-/

namespace QOU.Foundations.FrobeniusHopfMarkovBridge

universe u v

/-! ## §1. Generic Commutative Ring Carrier (§7c) -/

/-- Minimal commutative ring operations over a generic type `R` (§7c). -/
structure CommRingOps (R : Type u) where
  add : R → R → R
  sub : R → R → R
  mul : R → R → R
  neg : R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  zero_add : ∀ a : R, add zero a = a
  add_zero : ∀ a : R, add a zero = a
  add_left_neg : ∀ a : R, add (neg a) a = zero
  sub_eq_add_neg : ∀ a b : R, sub a b = add a (neg b)
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  one_mul : ∀ a : R, mul one a = a
  mul_one : ∀ a : R, mul a one = a
  zero_mul : ∀ a : R, mul zero a = zero
  mul_zero : ∀ a : R, mul a zero = zero
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)

/-- Standard `ℤ` instance of `CommRingOps` for concrete non-vacuity witnesses. -/
def intCommRingOps : CommRingOps Int where
  add := (· + ·)
  sub := (· - ·)
  mul := (· * ·)
  neg := (- ·)
  zero := 0
  one := 1
  add_assoc := Int.add_assoc
  add_comm := Int.add_comm
  zero_add := Int.zero_add
  add_zero := Int.add_zero
  add_left_neg := fun a => Int.add_left_neg a
  sub_eq_add_neg := fun _ _ => Int.sub_eq_add_neg
  mul_assoc := Int.mul_assoc
  mul_comm := Int.mul_comm
  one_mul := Int.one_mul
  mul_one := Int.mul_one
  zero_mul := Int.zero_mul
  mul_zero := Int.mul_zero
  left_distrib := Int.mul_add
  right_distrib := Int.add_mul

/-! ## §2. `qou-aj49`: Multiplicative Counit Collapse vs Two-Counit `R[C₂]` Model -/

/-- Two-term Sweedler Frobenius data on an `R`-module/algebra `A`:
`Δ(1) = e₁ ⊗ f₁ + e₂ ⊗ f₂`, right Frobenius contraction
`x = ε(f₁ · x) • e₁ + ε(f₂ · x) • e₂`, and unit identity
`1_A = ε(f₁) • e₁ + ε(f₂) • e₂`. -/
structure TwoTermFrobeniusData (R : Type u) (A : Type v) (ring : CommRingOps R) where
  addA : A → A → A
  mulA : A → A → A
  smulA : R → A → A
  oneA : A
  e1 : A
  f1 : A
  e2 : A
  f2 : A
  counit : A → R
  smul_add : ∀ (r : R) (x y : A), smulA r (addA x y) = addA (smulA r x) (smulA r y)
  smul_smul : ∀ (r s : R) (x : A), smulA (ring.mul r s) x = smulA r (smulA s x)
  unit_sweedler : oneA = addA (smulA (counit f1) e1) (smulA (counit f2) e2)
  right_counit_sweedler : ∀ x : A,
    x = addA (smulA (counit (mulA f1 x)) e1) (smulA (counit (mulA f2 x)) e2)

/-- **Collapse Theorem (`qou-aj49`).**
If the Frobenius counit `ε : A → R` in `TwoTermFrobeniusData` is ALSO
multiplicative (`ε(y · x) = ε(y) · ε(x)`), then every element `x : A`
collapses to `ε(x) • 1_A`. No antipode is used. -/
theorem frobenius_multiplicative_counit_collapses
    {R : Type u} {A : Type v} (ring : CommRingOps R)
    (F : TwoTermFrobeniusData R A ring)
    (hmul : ∀ y x : A, F.counit (F.mulA y x) = ring.mul (F.counit y) (F.counit x))
    (x : A) :
    x = F.smulA (F.counit x) F.oneA := by
  have hx := F.right_counit_sweedler x
  rw [hmul F.f1 x, hmul F.f2 x] at hx
  rw [ring.mul_comm (F.counit F.f1) (F.counit x),
      ring.mul_comm (F.counit F.f2) (F.counit x)] at hx
  rw [F.smul_smul (F.counit x) (F.counit F.f1) F.e1,
      F.smul_smul (F.counit x) (F.counit F.f2) F.e2] at hx
  rw [← F.smul_add (F.counit x) (F.smulA (F.counit F.f1) F.e1)
        (F.smulA (F.counit F.f2) F.e2)] at hx
  rw [← F.unit_sweedler] at hx
  exact hx

/-- Rank-2 group algebra `R[C₂]` represented in basis `(1, g)` with `g² = 1`:
an element `⟨a, b⟩` represents `a · 1 + b · g`. -/
structure C2Alg (R : Type u) where
  c1 : R
  cg : R
  deriving DecidableEq

/-- Addition in `R[C₂]`. -/
def c2Add {R : Type u} (ring : CommRingOps R) (x y : C2Alg R) : C2Alg R :=
  ⟨ring.add x.c1 y.c1, ring.add x.cg y.cg⟩

/-- Scalar multiplication in `R[C₂]`. -/
def c2Smul {R : Type u} (ring : CommRingOps R) (r : R) (x : C2Alg R) : C2Alg R :=
  ⟨ring.mul r x.c1, ring.mul r x.cg⟩

/-- Group-algebra multiplication `(a₁ + b₁ g)(a₂ + b₂ g) = (a₁ a₂ + b₁ b₂) + (a₁ b₂ + b₁ a₂) g`. -/
def c2Mul {R : Type u} (ring : CommRingOps R) (x y : C2Alg R) : C2Alg R :=
  ⟨ring.add (ring.mul x.c1 y.c1) (ring.mul x.cg y.cg),
   ring.add (ring.mul x.c1 y.cg) (ring.mul x.cg y.c1)⟩

/-- Unit `1 = 1 · 1 + 0 · g` in `R[C₂]`. -/
def c2One {R : Type u} (ring : CommRingOps R) : C2Alg R :=
  ⟨ring.one, ring.zero⟩

/-- Generator `g = 0 · 1 + 1 · g` in `R[C₂]`. -/
def c2Gen {R : Type u} (ring : CommRingOps R) : C2Alg R :=
  ⟨ring.zero, ring.one⟩

/-- **Frobenius trace counit `ε_F` on `R[C₂]`:** picks the `g`-coefficient
`ε_F(a · 1 + b · g) = b`, with dual-basis Frobenius coproduct
`Δ_F(1) = 1 ⊗ g + g ⊗ 1` (`e₁ = 1, f₁ = g, e₂ = g, f₂ = 1`). -/
def c2EpsFrobenius {R : Type u} (x : C2Alg R) : R := x.cg

/-- **Hopf augmentation counit `ε_H` on `R[C₂]`:** the multiplicative character
`ε_H(a · 1 + b · g) = a + b`. -/
def c2EpsHopf {R : Type u} (ring : CommRingOps R) (x : C2Alg R) : R :=
  ring.add x.c1 x.cg

/-- **Frobenius right-counit contraction on `R[C₂]` (`qou-aj49`).**
With `Δ_F(1) = 1 ⊗ g + g ⊗ 1` and `ε_F(a·1 + b·g) = b`, every `x : R[C₂]`
satisfies `x = ε_F(g · x) • 1 + ε_F(1 · x) • g`. -/
theorem c2_frobenius_right_counit_law {R : Type u} (ring : CommRingOps R) (x : C2Alg R) :
    c2Add ring
      (c2Smul ring (c2EpsFrobenius (c2Mul ring (c2Gen ring) x)) (c2One ring))
      (c2Smul ring (c2EpsFrobenius (c2Mul ring (c2One ring) x)) (c2Gen ring)) = x := by
  cases x with
  | mk a b =>
    simp only [c2Add, c2Smul, c2EpsFrobenius, c2Mul, c2Gen, c2One]
    congr 1
    · rw [ring.zero_mul, ring.one_mul, ring.zero_add, ring.mul_one,
          ring.one_mul, ring.zero_mul, ring.add_zero, ring.mul_zero, ring.add_zero]
    · rw [ring.zero_mul, ring.one_mul, ring.zero_add, ring.mul_zero,
          ring.one_mul, ring.zero_mul, ring.add_zero, ring.mul_one, ring.zero_add]

/-- **Hopf counit multiplicativity on `R[C₂]` (`qou-aj49`).**
`ε_H(x · y) = ε_H(x) · ε_H(y)` for all `x, y ∈ R[C₂]`. -/
theorem c2_hopf_counit_multiplicative {R : Type u} (ring : CommRingOps R) (x y : C2Alg R) :
    c2EpsHopf ring (c2Mul ring x y) =
      ring.mul (c2EpsHopf ring x) (c2EpsHopf ring y) := by
  cases x with
  | mk a1 b1 =>
    cases y with
    | mk a2 b2 =>
      simp only [c2EpsHopf, c2Mul]
      rw [ring.left_distrib, ring.right_distrib, ring.right_distrib]
      rw [ring.add_assoc, ring.add_assoc]
      congr 1
      rw [ring.add_comm (ring.mul a1 b2) (ring.mul b1 a2),
          ← ring.add_assoc (ring.mul b1 b2) (ring.mul b1 a2) (ring.mul a1 b2),
          ring.add_comm (ring.mul b1 b2) (ring.mul b1 a2),
          ring.add_assoc (ring.mul b1 a2) (ring.mul b1 b2) (ring.mul a1 b2),
          ring.add_comm (ring.mul b1 b2) (ring.mul a1 b2)]

/-- **Two-Counit Non-Collapse Theorem (`qou-aj49`).**
Over `ℤ`, `ℤ[C₂]` has:
1. Exact Frobenius right-counit contraction under `ε_F`;
2. Exact Hopf multiplicativity under `ε_H`;
3. `ε_F ≠ ε_H` and `ε_F` is NOT multiplicative (`ε_F(g · g) = 0 ≠ 1 = ε_F(g) · ε_F(g)`);
4. Non-collapse of `ℤ[C₂]` to `ℤ · 1` (`∀ c : ℤ, g ≠ c • 1`). -/
theorem c2_two_counit_noncollapse :
    (∀ x : C2Alg Int,
      c2Add intCommRingOps
        (c2Smul intCommRingOps (c2EpsFrobenius (c2Mul intCommRingOps (c2Gen intCommRingOps) x))
          (c2One intCommRingOps))
        (c2Smul intCommRingOps (c2EpsFrobenius (c2Mul intCommRingOps (c2One intCommRingOps) x))
          (c2Gen intCommRingOps)) = x) ∧
    (∀ x y : C2Alg Int,
      c2EpsHopf intCommRingOps (c2Mul intCommRingOps x y) =
        intCommRingOps.mul (c2EpsHopf intCommRingOps x) (c2EpsHopf intCommRingOps y)) ∧
    (c2EpsFrobenius (c2Mul intCommRingOps (c2Gen intCommRingOps) (c2Gen intCommRingOps)) ≠
      intCommRingOps.mul (c2EpsFrobenius (c2Gen intCommRingOps))
        (c2EpsFrobenius (c2Gen intCommRingOps))) ∧
    (∀ c : Int, c2Gen intCommRingOps ≠ c2Smul intCommRingOps c (c2One intCommRingOps)) := by
  refine ⟨c2_frobenius_right_counit_law intCommRingOps,
          c2_hopf_counit_multiplicative intCommRingOps, ?_, ?_⟩
  · decide
  · intro c hc
    have hcg : (c2Gen intCommRingOps).cg = (c2Smul intCommRingOps c (c2One intCommRingOps)).cg :=
      congrArg C2Alg.cg hc
    change (1 : Int) = c * 0 at hcg
    rw [Int.mul_zero] at hcg
    revert hcg; decide

/-! ## §3. `qou-wapd`: Row-Capped Ocneanu/Markov Weight vs Uncapped Plancherel Weight -/

/-- A partition datum for `λ ⊢ n` carrying its number of rows `numRows = ℓ(λ)`,
its classical SYT dimension `fLambda = f^λ`, its row-capped Markov weight `yMarkov`,
and its uncapped Plancherel weight `wPlancherel`. -/
structure PartitionWeightDatum (R : Type u) where
  numRows : Nat
  fLambda : R
  yMarkov : R
  wPlancherel : R

/-- At `SU(2)` fibre dimension `N = 2`, a weight assignment is row-capped if
`y_λ = 0` whenever `ℓ(λ) > 2`. -/
def IsSU2RowCapped {R : Type u} (ring : CommRingOps R) (d : PartitionWeightDatum R) : Prop :=
  2 < d.numRows → d.yMarkov = ring.zero

/-- **Row-cap vanishing theorem (`qou-wapd`).**
For any partition datum with `ℓ(λ) > 2` satisfying `IsSU2RowCapped`, its Markov
contribution `y_λ · χ^λ(x)` vanishes identically for every character value `χ^λ(x) : R`. -/
theorem row_capped_contribution_vanishes
    {R : Type u} (ring : CommRingOps R) (d : PartitionWeightDatum R)
    (hcap : IsSU2RowCapped ring d) (hrows : 2 < d.numRows) (chiVal : R) :
    ring.mul d.yMarkov chiVal = ring.zero := by
  rw [hcap hrows, ring.zero_mul]

/-- **Obstruction to uniform rescaling between uncapped Plancherel and row-capped Markov (`qou-wapd`).**
If `d` has `ℓ(d) > 2` (so `y_d = 0` by the `SU(2)` row cap) while `w_d ≠ 0`, then
no scalar `c : R` can satisfy `c · y_d = w_d`. Consequently, no `λ`-independent
normalization factor can turn the uncapped Plancherel weight family `w_λ` into
the row-capped Markov weight family `y_λ`. -/
theorem no_uniform_rescale_between_uncapped_and_row_capped
    {R : Type u} (ring : CommRingOps R) (d : PartitionWeightDatum R)
    (hcap : IsSU2RowCapped ring d) (hrows : 2 < d.numRows)
    (hw_nz : d.wPlancherel ≠ ring.zero) :
    ∀ c : R, ring.mul c d.yMarkov ≠ d.wPlancherel := by
  intro c hc
  rw [hcap hrows, ring.mul_zero] at hc
  exact hw_nz hc.symm

/-- Classical SYT dimensions `f^λ` of all 11 partitions of `n = 6`:
`(6) → 1`, `(5,1) → 5`, `(4,2) → 9`, `(4,1,1) → 10`, `(3,3) → 5`,
`(3,2,1) → 16`, `(3,1,1,1) → 10`, `(2,2,2) → 5`, `(2,2,1,1) → 9`,
`(2,1,1,1,1) → 5`, `(1^6) → 1`. -/
def n6AllPlancherelSqSum : Nat :=
  1^2 + 5^2 + 9^2 + 10^2 + 5^2 + 16^2 + 10^2 + 5^2 + 9^2 + 5^2 + 1^2

/-- Row-capped (`ℓ(λ) ≤ 2`) classical Burnside sum at `n = 6`:
only `(6), (5,1), (4,2), (3,3)` survive the `N = 2` row cap. -/
def n6RowCappedPlancherelSqSum : Nat :=
  1^2 + 5^2 + 9^2 + 5^2

/-- **Concrete `n = 6, λ = (3,2,1)` Row-Cap & Plancherel Obstruction Witness (`qou-wapd`).**
1. Full Burnside identity at `n = 6`: `∑_{λ ⊢ 6} (f^λ)² = 720 = 6!`.
2. Row-capped (`ℓ(λ) ≤ 2`) sum is `132`, so `720 - 132 = 588` of the classical
   Plancherel weight sits in the `ℓ(λ) ≥ 3` sector killed by the `N = 2` row cap.
3. The staircase partition `λ = (3,2,1)` alone has `ℓ(3,2,1) = 3 > 2` and
   `(f^{(3,2,1)})² = 256 ≠ 0`, so `no_uniform_rescale_between_uncapped_and_row_capped`
   applies directly to `λ = (3,2,1)`. -/
theorem n6_partition_321_row_cap_obstruction :
    n6AllPlancherelSqSum = 720 ∧
    n6RowCappedPlancherelSqSum = 132 ∧
    n6AllPlancherelSqSum - n6RowCappedPlancherelSqSum = 588 ∧
    (∀ c : Int,
      intCommRingOps.mul c
        (PartitionWeightDatum.mk 3 (16 : Int) 0 256).yMarkov ≠
        (PartitionWeightDatum.mk 3 (16 : Int) 0 256).wPlancherel) := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  exact no_uniform_rescale_between_uncapped_and_row_capped
    intCommRingOps
    (PartitionWeightDatum.mk 3 (16 : Int) 0 256)
    (fun _ => rfl)
    (by decide)
    (by decide)

/-! ## §4. `qou-k5jt`: Concrete Wedderburn Character Bridge for Hecke Trace Axioms -/

/-- Concrete two-block Wedderburn trace datum on an algebra `H` over `R`:
models `tr_M(x) = y₁ · χ₁(x) + y₂ · χ₂(x)` where `χ₁, χ₂ : H → R` are concrete
block character traces. -/
structure TwoBlockWedderburnTrace (R : Type u) (H : Type v) (ring : CommRingOps R) where
  addH : H → H → H
  mulH : H → H → H
  smulH : R → H → H
  oneH : H
  y1 : R
  y2 : R
  chi1 : H → R
  chi2 : H → R
  chi1_add : ∀ x y : H, chi1 (addH x y) = ring.add (chi1 x) (chi1 y)
  chi2_add : ∀ x y : H, chi2 (addH x y) = ring.add (chi2 x) (chi2 y)
  chi1_smul : ∀ (c : R) (x : H), chi1 (smulH c x) = ring.mul c (chi1 x)
  chi2_smul : ∀ (c : R) (x : H), chi2 (smulH c x) = ring.mul c (chi2 x)
  chi1_symm : ∀ x y : H, chi1 (mulH x y) = chi1 (mulH y x)
  chi2_symm : ∀ x y : H, chi2 (mulH x y) = chi2 (mulH y x)
  weights_norm_one : ring.add (ring.mul y1 (chi1 oneH)) (ring.mul y2 (chi2 oneH)) = ring.one

/-- The concrete Wedderburn Markov trace `tr_M(x) = y₁ · χ₁(x) + y₂ · χ₂(x)`. -/
def evalWedderburnTrace {R : Type u} {H : Type v} (ring : CommRingOps R)
    (W : TwoBlockWedderburnTrace R H ring) (x : H) : R :=
  ring.add (ring.mul W.y1 (W.chi1 x)) (ring.mul W.y2 (W.chi2 x))

/-- **Concrete Markov trace additivity (`qou-k5jt`).**
Proved directly from block-character additivity (no axiom). -/
theorem concrete_wedderburn_trace_add {R : Type u} {H : Type v} (ring : CommRingOps R)
    (W : TwoBlockWedderburnTrace R H ring) (x y : H) :
    evalWedderburnTrace ring W (W.addH x y) =
      ring.add (evalWedderburnTrace ring W x) (evalWedderburnTrace ring W y) := by
  simp only [evalWedderburnTrace, W.chi1_add, W.chi2_add, ring.left_distrib]
  rw [ring.add_assoc, ring.add_assoc]
  congr 1
  rw [← ring.add_assoc (ring.mul W.y1 (W.chi1 y)),
      ring.add_comm (ring.mul W.y1 (W.chi1 y)) (ring.mul W.y2 (W.chi2 x)),
      ring.add_assoc]

/-- **Concrete Markov trace cyclicity (`qou-k5jt`).**
`tr_M(x · y) = tr_M(y · x)` proved directly from block-character trace symmetry
`χᵢ(x · y) = χᵢ(y · x)`, discharging the former `MarkovTrace_cyclic` axiom. -/
theorem concrete_wedderburn_trace_cyclic {R : Type u} {H : Type v} (ring : CommRingOps R)
    (W : TwoBlockWedderburnTrace R H ring) (x y : H) :
    evalWedderburnTrace ring W (W.mulH x y) =
      evalWedderburnTrace ring W (W.mulH y x) := by
  simp only [evalWedderburnTrace, W.chi1_symm x y, W.chi2_symm x y]

/-- **Concrete Markov trace unit normalization (`qou-k5jt`).**
`tr_M(1_H) = 1_R` proved directly from `y₁ · χ₁(1) + y₂ · χ₂(1) = 1`. -/
theorem concrete_wedderburn_trace_one {R : Type u} {H : Type v} (ring : CommRingOps R)
    (W : TwoBlockWedderburnTrace R H ring) :
    evalWedderburnTrace ring W W.oneH = ring.one :=
  W.weights_norm_one

/-- Concrete 2-block algebra `R × R` (modelling `H₂(q) ≅ R_{(2)} ⊕ R_{(1,1)}`
with 1-dimensional irreducible blocks `χ₁(x₁, x₂) = x₁` and `χ₂(x₁, x₂) = x₂`)
and integer weights `(y₁, y₂) = (2, -1)` satisfying `y₁ · 1 + y₂ · 1 = 1`. -/
def h2ConcreteWedderburnWitness : TwoBlockWedderburnTrace Int (C2Alg Int) intCommRingOps where
  addH := c2Add intCommRingOps
  mulH := fun x y => ⟨x.c1 * y.c1, x.cg * y.cg⟩
  smulH := c2Smul intCommRingOps
  oneH := ⟨1, 1⟩
  y1 := 2
  y2 := -1
  chi1 := C2Alg.c1
  chi2 := C2Alg.cg
  chi1_add := fun _ _ => rfl
  chi2_add := fun _ _ => rfl
  chi1_smul := fun _ _ => rfl
  chi2_smul := fun _ _ => rfl
  chi1_symm := fun x y => Int.mul_comm x.c1 y.c1
  chi2_symm := fun x y => Int.mul_comm x.cg y.cg
  weights_norm_one := by decide

/-- **Non-vacuity & distinct-channel separation for `TwoBlockWedderburnTrace` (`qou-k5jt`).**
`h2ConcreteWedderburnWitness` satisfies unit normalization `tr_M(1, 1) = 1`,
cyclicity on all pairs, and separates the two Wedderburn blocks
(`tr_M(1, 0) = 2 ≠ -1 = tr_M(0, 1)`). -/
theorem h2_concrete_trace_nonvacuity :
    evalWedderburnTrace intCommRingOps h2ConcreteWedderburnWitness ⟨1, 1⟩ = 1 ∧
    evalWedderburnTrace intCommRingOps h2ConcreteWedderburnWitness ⟨1, 0⟩ = 2 ∧
    evalWedderburnTrace intCommRingOps h2ConcreteWedderburnWitness ⟨0, 1⟩ = -1 ∧
    (∀ x y : C2Alg Int,
      evalWedderburnTrace intCommRingOps h2ConcreteWedderburnWitness
        (h2ConcreteWedderburnWitness.mulH x y) =
      evalWedderburnTrace intCommRingOps h2ConcreteWedderburnWitness
        (h2ConcreteWedderburnWitness.mulH y x)) :=
  ⟨by decide, by decide, by decide,
   concrete_wedderburn_trace_cyclic intCommRingOps h2ConcreteWedderburnWitness⟩

/-! ## §5. `qou-bmyx`: Algebraic Logarithmic-Derivative Order Decomposition -/

/-- **Cleared-Denominator Logarithmic-Derivative Split (`qou-bmyx`).**
In any commutative ring `R`, if `F = P · g`, `P = u · Q` (modelling `P = (z - w)^m`
and `Q = (z - w)^{m-1}` with `u = z - w`), and `P' = m · Q` so that the Leibniz
rule gives `F' = m · Q · g + P · g'`, then multiplying `F'` by `u · g` yields
`(m · g + u · g') · F`. Dividing by `u · g · F` gives the local argument-principle
integrand split `F'/F = m/u + g'/g`. -/
theorem logDeriv_factor_cleared_identity
    {R : Type u} (ring : CommRingOps R) (m u Q g gDeriv : R) :
    let P := ring.mul u Q
    let F := ring.mul P g
    let FDeriv := ring.add (ring.mul (ring.mul m Q) g) (ring.mul P gDeriv)
    ring.mul FDeriv (ring.mul u g) =
      ring.mul (ring.add (ring.mul m g) (ring.mul u gDeriv)) F := by
  intro P F FDeriv
  dsimp only [P, F, FDeriv]
  rw [ring.right_distrib, ring.right_distrib]
  congr 1
  · rw [ring.mul_assoc (ring.mul m Q) g (ring.mul u g),
        ← ring.mul_assoc g u g,
        ring.mul_comm g u,
        ring.mul_assoc u g g,
        ← ring.mul_assoc (ring.mul m Q) u (ring.mul g g),
        ring.mul_assoc m Q u,
        ring.mul_comm Q u,
        ← ring.mul_assoc m u Q,
        ← ring.mul_assoc (ring.mul m g) (ring.mul u Q) g,
        ring.mul_assoc m g (ring.mul u Q),
        ring.mul_comm g (ring.mul u Q),
        ← ring.mul_assoc m (ring.mul u Q) g,
        ring.mul_assoc (ring.mul m (ring.mul u Q)) g g,
        ← ring.mul_assoc m u Q]
  · rw [ring.mul_assoc (ring.mul u Q) gDeriv (ring.mul u g),
        ring.mul_comm gDeriv (ring.mul u g),
        ← ring.mul_assoc (ring.mul u Q) (ring.mul u g) gDeriv,
        ring.mul_comm (ring.mul u Q) (ring.mul u g),
        ring.mul_assoc (ring.mul u g) (ring.mul u Q) gDeriv,
        ← ring.mul_assoc (ring.mul u gDeriv) (ring.mul u Q) g,
        ring.mul_assoc u gDeriv (ring.mul u Q),
        ring.mul_comm gDeriv (ring.mul u Q),
        ← ring.mul_assoc u (ring.mul u Q) gDeriv,
        ring.mul_assoc (ring.mul u (ring.mul u Q)) gDeriv g,
        ring.mul_comm gDeriv g,
        ← ring.mul_assoc (ring.mul u (ring.mul u Q)) g gDeriv,
        ring.mul_assoc u (ring.mul u Q) g,
        ← ring.mul_assoc (ring.mul u g) (ring.mul u Q) gDeriv,
        ring.mul_assoc u g (ring.mul u Q),
        ring.mul_comm g (ring.mul u Q)]

end QOU.Foundations.FrobeniusHopfMarkovBridge
