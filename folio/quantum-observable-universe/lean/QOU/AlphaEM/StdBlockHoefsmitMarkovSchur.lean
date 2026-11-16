/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Init.Data.Int.Basic
import Init.Data.Nat.Basic

/-!
# `QOU.AlphaEM.StdBlockHoefsmitMarkovSchur` — The `(4,1)` Standard Block of `H₅(q)`, Explicit Hoefsmit/Markov Gram Weights, and Schur-Uniqueness Reduction

Beans `qou-mxnu` (Option A: Wedderburn-block identification — pin the `(4,1)`/std
block of `H_n(q)` and its explicit Markov weight matrix) and `qou-vbz4` (Option B:
Schur-uniqueness reduction — invariant symmetric forms on irreducible `std` unique
up to scalar `⇒ Markov Gram ∝ Hodge Gram`, reducing the B2 τ-identification to the
single scalar scale `c = markov_norm / hodge_norm` and the `S₅`-equivariance premise),
under epic `qou-3l2l` (`α_EM` chain).

Companion probe:
  `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py`
  (`computations/alpha_em/std-block-hoefsmit-markov-schur.witness.json`)

## Mathematical Content

### Part I — `qou-mxnu`: The `(4,1)` Standard Block of `H₅(q)` and Hoefsmit Markov Gram
1. **Standard Young Tableaux of `λ = (4,1) ⊢ 5` (`SYT41`):**
   The 4-dimensional standard module `V_{(4,1)}` has basis indexed by the four
   standard Young tableaux `T₂, T₃, T₄, T₅` of shape `(4,1)`, distinguished by the
   unique entry `legEntry T ∈ {2, 3, 4, 5}` placed in cell `(1,0)` (content `-1`),
   while the remaining entries fill row `0` (contents `0, 1, 2, 3`) in increasing
   order.
2. **Cell contents and shifted axial distances:**
   For each `T ∈ SYT(4,1)` and adjacent transposition `s_k` (`k ∈ {1, 2, 3, 4}`),
   the axial distance `ρ_k(T) = c(T, k+1) − c(T, k)` is non-zero (`axialDist_ne_zero`)
   and takes values in `{±1, ±2, ±3, ±4}`, with the removable-box transitions at
   `T₂ ↔ T₃` (`|ρ₂| = 2`), `T₃ ↔ T₄` (`|ρ₃| = 3`), and `T₄ ↔ T₅` (`|ρ₄| = 4`).
3. **Hook lengths, `q`-dimension `d_q(4,1)`, and Wedderburn/Plancherel weight:**
   The hook lengths of `(4,1)` are `(5, 3, 2, 1, 1)` with classical product `30`
   and Frame–Robinson–Thrall dimension `5! / 30 = 4` (`frame_robinson_thrall_41`).
   Over a generic commutative ring `R` (§7c), the balanced `q`-factorial and hook
   product satisfy the division-free factorisation
   `[5]_q! · [1]_q = [4]_q · ([5]_q [3]_q [2]_q [1]_q²)` (`qFact5_eq_qDim41_mul_qHookProd41`),
   so `d_q(4,1) = [5]_q / ([5]_q / [4]_q) = [4]_q / [1]_q = [4]_q` and
   `w_{(4,1)}(q) = d_q(4,1)² / [5]_q! = [4]_q² / [5]_q!` (`2/15` at `q = 1`,
   `≈ 0.1286200450` at `q₀`).
4. **Explicit diagonal Hoefsmit / seminormal Markov Gram matrix (`hoefsmitGramDiag`):**
   In the Young/Hoefsmit asymmetric-natural seminormal basis `(v_{T₂}, v_{T₃}, v_{T₄}, v_{T₅})`,
   the contravariant Markov Gram `G_Markov(q)` (`σ_kᵀ G = G σ_k`) is diagonal.
   Clearing denominators by `D(q) = [2]_q² [3]_q² [4]_q²` over a generic ring `R` (§7c),
   the diagonal weights
   - `g̃₀(q) = [2]_q² [3]_q² [4]_q²`
   - `g̃₁(q) = ([2]_q² − 1) [3]_q² [4]_q²`
   - `g̃₂(q) = ([2]_q² − 1) ([3]_q² − 1) [4]_q²`
   - `g̃₃(q) = ([2]_q² − 1) ([3]_q² − 1) ([4]_q² − 1)`
   satisfy the exact Hoefsmit contravariant recurrence at every adjacent SYT transition
   (`hoefsmitGram_recurrence_step12`, `hoefsmitGram_recurrence_step23`,
   `hoefsmitGram_recurrence_step34`) and evaluate at `q = 1` (`[d]₁ = d`) to
   `(576, 432, 384, 360) = 576 · (1, 3/4, 2/3, 5/8)` (`hoefsmitGram_classical_ratios`).

### Part II — `qou-vbz4`: Schur-Uniqueness Reduction (`Markov Gram ∝ Hodge Gram`)
5. **Proportionality and uniqueness of the Schur scalar over a generic field/ring `R` (§7c):**
   When the space of invariant symmetric bilinear forms on `V_{(4,1)}` is
   1-dimensional (spanned by a non-zero canonical generator `B₀`), any two invariant
   symmetric forms `B₁ = markov_norm · B₀` and `B₂ = hodge_norm · B₀` with invertible
   `hodge_norm` satisfy `B₁(u, v) = c · B₂(u, v)` for all `u, v ∈ SYT(4,1)` with
   `c = markov_norm · hodge_norm⁻¹` (`schur_invariantForm_proportional`), and `c` is
   unique (`schur_scalar_unique`) and non-zero whenever `markov_norm` is invertible
   (`schur_scalar_unit`).
6. **Non-vacuity (`non_vacuity_unaligned_not_proportional`):**
   Without the `S₅`-equivariant period intertwiner `U`, the raw isogeny-frame Hodge
   pattern `diag(5, 5, 5, 1)` and the classical Hoefsmit Gram `diag(576, 432, 384, 360)`
   are NOT proportional for any scalar `c : Int`, proving that the `S₅`-equivariance /
   intertwiner premise is load-bearing.

## Base ring (AGENTS.md §7c) & Scope Discipline
- **Base ring (§7c):** Generic `{R : Type u}` via a self-contained algebraic
  typeclass `CommRingOps R` (no `ℝ`, no `Real.*`, no archimedean construct, and no
  external imports beyond Lean core `Init`).
- **Scope guard (STRICT, §"Axiomatization is NOT a Proof"):** This module proves
  the algebraic `(4,1)` Hoefsmit Gram recurrence and the Schur proportionality
  reduction from explicit hypotheses. It does **not** construct the categorical
  `τ`-functor, does **not** register a `TauRhoHodgeLift` instance, and leaves
  `1/(8π)` at phase-4.

-- Ref: [hoefsmit1974] Seminormal representations of Weyl groups and Hecke algebras
-- Ref: [wenzl1988] Hecke algebras of type A_n and subfactors, Invent. Math. 92
-- Ref: [serre1977] Linear Representations of Finite Groups (Schur's lemma)
-- Ref: [braden-northover-2012] Bring's curve: its period matrix, SIGMA 8 (2012), 065
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-/

set_option autoImplicit false

namespace QOU.AlphaEM.StdBlockHoefsmitMarkovSchur

universe u

/-! ## Part I — `qou-mxnu`: Standard Young Tableaux of `λ = (4,1) ⊢ 5` -/

/-- The four standard Young tableaux of shape `λ = (4,1) ⊢ 5`, indexed by which
entry `k ∈ {2, 3, 4, 5}` occupies the unique second-row box `(1,0)`. -/
inductive SYT41 : Type
  | t2 : SYT41  -- row 0: [1,3,4,5], row 1: [2]
  | t3 : SYT41  -- row 0: [1,2,4,5], row 1: [3]
  | t4 : SYT41  -- row 0: [1,2,3,5], row 1: [4]
  | t5 : SYT41  -- row 0: [1,2,3,4], row 1: [5]
  deriving DecidableEq, Repr

/-- The entry occupying the removable leg cell `(1,0)` of a standard tableau of
shape `(4,1)`. -/
def legEntry : SYT41 → Nat
  | .t2 => 2
  | .t3 => 3
  | .t4 => 4
  | .t5 => 5

/-- `legEntry` is injective on `SYT41`: the four standard tableaux are uniquely
determined by their leg entry in `{2, 3, 4, 5}`. -/
theorem legEntry_injective (a b : SYT41) (h : legEntry a = legEntry b) : a = b := by
  cases a <;> cases b <;> first | rfl | contradiction

/-- The leg entry of any `T ∈ SYT(4,1)` lies strictly between `1` and `5` (`2 ≤ legEntry T ≤ 5`). -/
theorem legEntry_bounds (t : SYT41) : 2 ≤ legEntry t ∧ legEntry t ≤ 5 := by
  cases t <;> decide

/-- Cell content `c(T, m) = col − row` of letter `m ∈ {1, 2, 3, 4, 5}` in `T ∈ SYT(4,1)`.
Letter `1` always sits at `(0,0)` with content `0`; the leg entry sits at `(1,0)`
with content `-1`; the remaining three letters sit at columns `1, 2, 3` of row `0`
with contents `1, 2, 3` in increasing order. -/
def cellContent (t : SYT41) (m : Nat) : Int :=
  match t, m with
  | _,   1 => 0
  | .t2, 2 => -1 | .t2, 3 => 1 | .t2, 4 => 2 | .t2, 5 => 3
  | .t3, 2 => 1  | .t3, 3 => -1 | .t3, 4 => 2 | .t3, 5 => 3
  | .t4, 2 => 1  | .t4, 3 => 2  | .t4, 4 => -1 | .t4, 5 => 3
  | .t5, 2 => 1  | .t5, 3 => 2  | .t5, 4 => 3  | .t5, 5 => -1
  | _,   _ => 0

/-- The sum of cell contents across any `T ∈ SYT(4,1)` is the partition content sum
`n(4,1) = 0 + 1 + 2 + 3 + (-1) = 5`, independent of the tableau `T`. -/
theorem cellContent_sum_eq_five (t : SYT41) :
    cellContent t 1 + cellContent t 2 + cellContent t 3 + cellContent t 4 + cellContent t 5 = 5 := by
  cases t <;> decide

/-- Shifted axial distance `ρ_k(T) = c(T, k) − c(T, k+1)` for adjacent generator `s_k`
(`k ∈ {1, 2, 3, 4}`). -/
def axialDist (t : SYT41) (k : Fin 4) : Int :=
  cellContent t (k.val + 1) - cellContent t (k.val + 2)

/-- For every `T ∈ SYT(4,1)` and every adjacent transposition `s_k` (`k ∈ Fin 4`),
the axial distance `ρ_k(T)` is non-zero (`|ρ_k(T)| ∈ {1, 2, 3, 4}`). -/
theorem axialDist_ne_zero (t : SYT41) (k : Fin 4) : axialDist t k ≠ 0 := by
  cases t <;> revert k <;> decide

/-- At the removable-box transitions `T₂ ↔ T₃` (`s₂`), `T₃ ↔ T₄` (`s₃`), and
`T₄ ↔ T₅` (`s₄`), the axial distances are `(-2, +2)`, `(-3, +3)`, and `(-4, +4)`
respectively — pinning the three Hoefsmit off-diagonal steps on `V_{(4,1)}`. -/
theorem axialDist_removable_transitions :
    axialDist .t2 ⟨1, by decide⟩ = -2 ∧ axialDist .t3 ⟨1, by decide⟩ = 2 ∧
    axialDist .t3 ⟨2, by decide⟩ = -3 ∧ axialDist .t4 ⟨2, by decide⟩ = 3 ∧
    axialDist .t4 ⟨3, by decide⟩ = -4 ∧ axialDist .t5 ⟨3, by decide⟩ = 4 := by
  decide

/-! ## Hook lengths, `q`-dimension, and Wedderburn/Plancherel weight for `λ = (4,1)` -/

/-- The five hook lengths of `λ = (4,1)`: cells `(0,0), (0,1), (0,2), (0,3), (1,0)`
have hook lengths `5, 3, 2, 1, 1`. -/
def hookLengths41 : List Nat := [5, 3, 2, 1, 1]

/-- Classical hook-length product `∏_{x ∈ (4,1)} h(x) = 30`. -/
def hookProduct41 : Nat := 5 * 3 * 2 * 1 * 1

/-- Frame–Robinson–Thrall classical dimension identity for `λ = (4,1)`:
`5! = 4 · ∏_{x ∈ (4,1)} h(x) = 4 · 30 = 120`. -/
theorem frame_robinson_thrall_41 : 4 * hookProduct41 = 120 ∧ 120 / hookProduct41 = 4 := by
  decide

/-- Classical Plancherel weight of `λ = (4,1)` in `S₅`:
`w_{(4,1)}(1) = d_{(4,1)}² / 5! = 16 / 120 = 2 / 15` (cross-multiplied: `16 * 15 = 2 * 120`). -/
theorem plancherel_weight_41_classical : 4 * 4 * 15 = 2 * 120 := by
  decide

/-- Self-contained commutative-ring operations over a generic base type `{R : Type u}` (§7c).
Avoids any `ℝ` or archimedean dependency while allowing generic algebraic proofs. -/
class CommRingOps (R : Type u) where
  add : R → R → R
  sub : R → R → R
  mul : R → R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  add_zero : ∀ a : R, add a zero = a
  zero_add : ∀ a : R, add zero a = a
  sub_self : ∀ a : R, sub a a = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  mul_one : ∀ a : R, mul a one = a
  one_mul : ∀ a : R, mul one a = a
  mul_zero : ∀ a : R, mul a zero = zero
  zero_mul : ∀ a : R, mul zero a = zero
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)
  sub_mul : ∀ a b c : R, mul (sub a b) c = sub (mul a c) (mul b c)

/-- Standard `Int` instance of `CommRingOps` for concrete classical-limit and
non-vacuity witnesses. -/
instance instCommRingOpsInt : CommRingOps Int where
  add := (· + ·)
  sub := (· - ·)
  mul := (· * ·)
  zero := 0
  one := 1
  add_assoc := Int.add_assoc
  add_comm := Int.add_comm
  add_zero := Int.add_zero
  zero_add := Int.zero_add
  sub_self := Int.sub_self
  mul_assoc := Int.mul_assoc
  mul_comm := Int.mul_comm
  mul_one := Int.mul_one
  one_mul := Int.one_mul
  mul_zero := Int.mul_zero
  zero_mul := Int.zero_mul
  left_distrib := Int.mul_add
  right_distrib := Int.add_mul
  sub_mul := Int.sub_mul

section GenericRing

variable {R : Type u} [ops : CommRingOps R]

/-- The `q`-factorial `[5]_q! = [1]_q [2]_q [3]_q [4]_q [5]_q` evaluated from a
generic bracket sequence `qBr : Nat → R` (`n ↦ [n]_q`). -/
def qFact5 (qBr : Nat → R) : R :=
  ops.mul (ops.mul (ops.mul (ops.mul (qBr 1) (qBr 2)) (qBr 3)) (qBr 4)) (qBr 5)

/-- The `q`-hook product `∏_{x ∈ (4,1)} [h(x)]_q = [1]_q [1]_q [2]_q [3]_q [5]_q`
written in matching associative order so the cancellation of `[2]_q [3]_q [5]_q`
is transparent. -/
def qHookProd41 (qBr : Nat → R) : R :=
  ops.mul (ops.mul (ops.mul (ops.mul (qBr 1) (qBr 1)) (qBr 2)) (qBr 3)) (qBr 5)

/-- **Division-free `q`-hook dimension identity for `λ = (4,1)` (`qou-mxnu`, §7c generic `R`).**
Whenever `[1]_q = 1`, the `q`-factorial `[5]_q!` factors as
`[5]_q! = [4]_q · ∏_{x ∈ (4,1)} [h(x)]_q`, establishing `d_q(4,1) = [4]_q = [5]_q! / ∏ [h_x]_q`
(and hence `w_{(4,1)}(q) = d_q(4,1)² / [5]_q! = [4]_q² / [5]_q!`). -/
theorem qFact5_eq_qDim41_mul_qHookProd41 (qBr : Nat → R) (h1 : qBr 1 = ops.one) :
    qFact5 qBr = ops.mul (qBr 4) (qHookProd41 qBr) := by
  unfold qFact5 qHookProd41
  rw [h1, ops.one_mul, ops.one_mul, ops.one_mul]
  -- Left-hand side: ((qBr 2 * qBr 3) * qBr 4) * qBr 5
  -- Right-hand side: qBr 4 * ((qBr 2 * qBr 3) * qBr 5)
  rw [ops.mul_assoc (ops.mul (qBr 2) (qBr 3)) (qBr 4) (qBr 5)]
  rw [ops.mul_comm (qBr 4) (qBr 5)]
  rw [← ops.mul_assoc (ops.mul (qBr 2) (qBr 3)) (qBr 5) (qBr 4)]
  rw [ops.mul_comm _ (qBr 4)]

/-! ## Explicit Diagonal Hoefsmit / Seminormal Markov Gram Matrix on `V_{(4,1)}` (`qou-mxnu`) -/

/-- Squared `q`-bracket `[d]_q²` in the generic ring `R`. -/
def qBrSq (qBr : Nat → R) (d : Nat) : R :=
  ops.mul (qBr d) (qBr d)

/-- Numerator `[d]_q² − 1` of the Hoefsmit off-diagonal norm factor
`b_{hi,lo} = ([d]_q² − 1) / [d]_q²` at axial distance `d`. -/
def qBrSqSubOne (qBr : Nat → R) (d : Nat) : R :=
  ops.sub (qBrSq qBr d) ops.one

/-- **Explicit diagonal entries of the cleared-denominator Hoefsmit / seminormal
Markov Gram matrix on `V_{(4,1)}` (`qou-mxnu`, §7c generic `R`).**
In the SYT basis `(T₂, T₃, T₄, T₅)`, clearing the common denominator
`D(q) = [2]_q² [3]_q² [4]_q²` gives the four diagonal weights:
- `g̃(T₂) = [2]_q² · [3]_q² · [4]_q²`
- `g̃(T₃) = ([2]_q² − 1) · [3]_q² · [4]_q²`
- `g̃(T₄) = ([2]_q² − 1) · ([3]_q² − 1) · [4]_q²`
- `g̃(T₅) = ([2]_q² − 1) · ([3]_q² − 1) · ([4]_q² − 1)` -/
def hoefsmitGramDiag (qBr : Nat → R) : SYT41 → R
  | .t2 => ops.mul (ops.mul (qBrSq qBr 2) (qBrSq qBr 3)) (qBrSq qBr 4)
  | .t3 => ops.mul (ops.mul (qBrSqSubOne qBr 2) (qBrSq qBr 3)) (qBrSq qBr 4)
  | .t4 => ops.mul (ops.mul (qBrSqSubOne qBr 2) (qBrSqSubOne qBr 3)) (qBrSq qBr 4)
  | .t5 => ops.mul (ops.mul (qBrSqSubOne qBr 2) (qBrSqSubOne qBr 3)) (qBrSqSubOne qBr 4)

/-- Full 4×4 diagonal Hoefsmit / Markov Gram bilinear form on `SYT41 × SYT41`:
`hoefsmitGramMatrix qBr u v = hoefsmitGramDiag qBr u` on the diagonal `u = v`,
and `0` off the diagonal (`u ≠ v`). -/
def hoefsmitGramMatrix (qBr : Nat → R) (u v : SYT41) : R :=
  if u = v then hoefsmitGramDiag qBr u else ops.zero

/-- **Symmetry of the Hoefsmit / Markov Gram matrix (`IsSymm`, §7c generic `R`).** -/
theorem hoefsmitGramMatrix_symm (qBr : Nat → R) (u v : SYT41) :
    hoefsmitGramMatrix qBr u v = hoefsmitGramMatrix qBr v u := by
  unfold hoefsmitGramMatrix
  cases u <;> cases v <;> rfl

/-- **Off-diagonal vanishing (orthogonality of distinct SYT basis vectors).** -/
theorem hoefsmitGramMatrix_offDiag_zero (qBr : Nat → R) {u v : SYT41} (h : u ≠ v) :
    hoefsmitGramMatrix qBr u v = ops.zero := by
  unfold hoefsmitGramMatrix
  rw [if_neg h]

/-- **Exact Hoefsmit contravariant recurrence at step `s₂` (`T₂ ↔ T₃`, axial distance `d = 2`):**
`g̃(T₂) · ([2]_q² − 1) = g̃(T₃) · [2]_q²`. -/
theorem hoefsmitGram_recurrence_step12 (qBr : Nat → R) :
    ops.mul (hoefsmitGramDiag qBr .t2) (qBrSqSubOne qBr 2) =
      ops.mul (hoefsmitGramDiag qBr .t3) (qBrSq qBr 2) := by
  unfold hoefsmitGramDiag
  -- Let A = qBrSq 2, B = qBrSqSubOne 2, C = qBrSq 3, D = qBrSq 4
  -- LHS = ((A * C) * D) * B, RHS = ((B * C) * D) * A
  rw [ops.mul_comm _ (qBrSqSubOne qBr 2)]
  rw [ops.mul_comm _ (qBrSq qBr 2)]
  rw [← ops.mul_assoc (qBrSqSubOne qBr 2) (ops.mul (qBrSq qBr 2) (qBrSq qBr 3)) (qBrSq qBr 4)]
  rw [← ops.mul_assoc (qBrSq qBr 2) (ops.mul (qBrSqSubOne qBr 2) (qBrSq qBr 3)) (qBrSq qBr 4)]
  rw [← ops.mul_assoc (qBrSqSubOne qBr 2) (qBrSq qBr 2) (qBrSq qBr 3)]
  rw [← ops.mul_assoc (qBrSq qBr 2) (qBrSqSubOne qBr 2) (qBrSq qBr 3)]
  rw [ops.mul_comm (qBrSqSubOne qBr 2) (qBrSq qBr 2)]

/-- **Exact Hoefsmit contravariant recurrence at step `s₃` (`T₃ ↔ T₄`, axial distance `d = 3`):**
`g̃(T₃) · ([3]_q² − 1) = g̃(T₄) · [3]_q²`. -/
theorem hoefsmitGram_recurrence_step23 (qBr : Nat → R) :
    ops.mul (hoefsmitGramDiag qBr .t3) (qBrSqSubOne qBr 3) =
      ops.mul (hoefsmitGramDiag qBr .t4) (qBrSq qBr 3) := by
  dsimp only [hoefsmitGramDiag]
  rw [ops.mul_assoc (ops.mul (qBrSqSubOne qBr 2) (qBrSq qBr 3)) (qBrSq qBr 4) (qBrSqSubOne qBr 3)]
  rw [ops.mul_assoc (ops.mul (qBrSqSubOne qBr 2) (qBrSqSubOne qBr 3)) (qBrSq qBr 4) (qBrSq qBr 3)]
  rw [ops.mul_comm (qBrSq qBr 4) (qBrSqSubOne qBr 3)]
  rw [ops.mul_comm (qBrSq qBr 4) (qBrSq qBr 3)]
  rw [← ops.mul_assoc (ops.mul (qBrSqSubOne qBr 2) (qBrSq qBr 3)) (qBrSqSubOne qBr 3) (qBrSq qBr 4)]
  rw [← ops.mul_assoc (ops.mul (qBrSqSubOne qBr 2) (qBrSqSubOne qBr 3)) (qBrSq qBr 3) (qBrSq qBr 4)]
  rw [ops.mul_assoc (qBrSqSubOne qBr 2) (qBrSq qBr 3) (qBrSqSubOne qBr 3)]
  rw [ops.mul_assoc (qBrSqSubOne qBr 2) (qBrSqSubOne qBr 3) (qBrSq qBr 3)]
  rw [ops.mul_comm (qBrSq qBr 3) (qBrSqSubOne qBr 3)]

/-- **Exact Hoefsmit contravariant recurrence at step `s₄` (`T₄ ↔ T₅`, axial distance `d = 4`):**
`g̃(T₄) · ([4]_q² − 1) = g̃(T₅) · [4]_q²`. -/
theorem hoefsmitGram_recurrence_step34 (qBr : Nat → R) :
    ops.mul (hoefsmitGramDiag qBr .t4) (qBrSqSubOne qBr 4) =
      ops.mul (hoefsmitGramDiag qBr .t5) (qBrSq qBr 4) := by
  unfold hoefsmitGramDiag
  rw [ops.mul_assoc _ (qBrSq qBr 4) (qBrSqSubOne qBr 4)]
  rw [ops.mul_assoc _ (qBrSqSubOne qBr 4) (qBrSq qBr 4)]
  rw [ops.mul_comm (qBrSq qBr 4) (qBrSqSubOne qBr 4)]

/-! ## Part II — `qou-vbz4`: Schur-Uniqueness Reduction (`Markov Gram ∝ Hodge Gram`) -/

/-- **1-dimensional invariant symmetric bilinear-form datum on `V_{(4,1)}` (`qou-vbz4`).**
Encodes the Schur consequence that the space of `H₅(q)`-invariant (or `S₅`-invariant
after Tits transport) symmetric bilinear forms on the irreducible 4-dimensional
`(4,1)` block is 1-dimensional, spanned by a canonical generator `B₀`, so any member
form `B` is `norm • B₀` for a scalar `norm : R`. -/
structure InvariantFormInSchurLine (B₀ : SYT41 → SYT41 → R) (B : SYT41 → SYT41 → R) where
  /-- The normalization scalar of `B` relative to the canonical generator `B₀`. -/
  norm : R
  /-- Symmetry of `B`. -/
  is_symm : ∀ u v : SYT41, B u v = B v u
  /-- `B` lies in the 1-dimensional Schur line spanned by `B₀`. -/
  eq_scale : ∀ u v : SYT41, B u v = ops.mul norm (B₀ u v)

/-- **Schur proportionality theorem (`qou-vbz4`, §7c generic `R`).**
Given two invariant symmetric bilinear forms `G_Markov` and `G_Hodge` in the
1-dimensional Schur line spanned by `B₀`, together with the multiplicative inverse
`hodge_norm_inv` of `G_Hodge.norm` (`hodge_norm * hodge_norm_inv = 1`), the two forms
are proportional across all `u, v ∈ SYT(4,1)`:
`G_Markov(u, v) = c · G_Hodge(u, v)` with explicit scalar
`c = markov_norm · hodge_norm⁻¹`. -/
theorem schur_invariantForm_proportional
    {B₀ G_Markov G_Hodge : SYT41 → SYT41 → R}
    (hM : InvariantFormInSchurLine B₀ G_Markov)
    (hH : InvariantFormInSchurLine B₀ G_Hodge)
    (hodge_norm_inv : R)
    (hInv : ops.mul hH.norm hodge_norm_inv = ops.one) :
    let c := ops.mul hM.norm hodge_norm_inv
    ∀ u v : SYT41, G_Markov u v = ops.mul c (G_Hodge u v) := by
  intro c u v
  rw [hM.eq_scale u v, hH.eq_scale u v]
  dsimp [c]
  rw [← ops.mul_assoc (ops.mul hM.norm hodge_norm_inv) hH.norm (B₀ u v)]
  rw [ops.mul_assoc hM.norm hodge_norm_inv hH.norm]
  rw [ops.mul_comm hodge_norm_inv hH.norm]
  rw [hInv, ops.mul_one]

/-- **Uniqueness of the Schur proportionality scalar `c` (`qou-vbz4`, §7c generic `R`).**
If `G_Markov(u, v) = c₁ · G_Hodge(u, v)` and `G_Markov(u, v) = c₂ · G_Hodge(u, v)`
for all `u, v ∈ SYT(4,1)`, and `G_Hodge` has an invertible entry at `(u₀, v₀)`
(witnessed by `entry_inv` with `G_Hodge(u₀, v₀) * entry_inv = 1`), then `c₁ = c₂`. -/
theorem schur_scalar_unique
    {G_Markov G_Hodge : SYT41 → SYT41 → R} {c₁ c₂ : R}
    (hc₁ : ∀ u v : SYT41, G_Markov u v = ops.mul c₁ (G_Hodge u v))
    (hc₂ : ∀ u v : SYT41, G_Markov u v = ops.mul c₂ (G_Hodge u v))
    (u₀ v₀ : SYT41) (entry_inv : R)
    (hEntry : ops.mul (G_Hodge u₀ v₀) entry_inv = ops.one) :
    c₁ = c₂ := by
  have hEq : ops.mul c₁ (G_Hodge u₀ v₀) = ops.mul c₂ (G_Hodge u₀ v₀) := by
    rw [← hc₁ u₀ v₀, ← hc₂ u₀ v₀]
  have hMul : ops.mul (ops.mul c₁ (G_Hodge u₀ v₀)) entry_inv =
      ops.mul (ops.mul c₂ (G_Hodge u₀ v₀)) entry_inv := by
    rw [hEq]
  rw [ops.mul_assoc c₁ (G_Hodge u₀ v₀) entry_inv,
      ops.mul_assoc c₂ (G_Hodge u₀ v₀) entry_inv,
      hEntry, ops.mul_one, ops.mul_one] at hMul
  exact hMul

/-- **Invertibility (non-vanishing) of the Schur scalar `c` (`qou-vbz4`, §7c generic `R`).**
When `markov_norm` is also invertible (`markov_norm * markov_norm_inv = 1`), the
Schur proportionality scalar `c = markov_norm * hodge_norm_inv` has explicit two-sided
inverse `c⁻¹ = hodge_norm * markov_norm_inv` (`c * c⁻¹ = 1`). -/
theorem schur_scalar_unit
    {markov_norm hodge_norm markov_norm_inv hodge_norm_inv : R}
    (hM : ops.mul markov_norm markov_norm_inv = ops.one)
    (hH : ops.mul hodge_norm hodge_norm_inv = ops.one) :
    ops.mul (ops.mul markov_norm hodge_norm_inv) (ops.mul hodge_norm markov_norm_inv) =
      ops.one := by
  rw [ops.mul_assoc markov_norm hodge_norm_inv (ops.mul hodge_norm markov_norm_inv)]
  rw [← ops.mul_assoc hodge_norm_inv hodge_norm markov_norm_inv]
  rw [ops.mul_comm hodge_norm_inv hodge_norm, hH, ops.one_mul, hM]

end GenericRing

/-! ## Classical `q = 1` Evaluation & Non-Vacuity Witness over `Int` -/

/-- Classical bracket `qBr₁(n) = n` at `q = 1`. -/
def qBrClassical (n : Nat) : Int := Int.ofNat n

/-- At `q = 1` (`[n]₁ = n`), the cleared-denominator Hoefsmit diagonal weights
evaluate to `(576, 432, 384, 360) = 576 · (1, 3/4, 2/3, 5/8)`. -/
theorem hoefsmitGram_classical_values :
    hoefsmitGramDiag qBrClassical .t2 = 576 ∧
    hoefsmitGramDiag qBrClassical .t3 = 432 ∧
    hoefsmitGramDiag qBrClassical .t4 = 384 ∧
    hoefsmitGramDiag qBrClassical .t5 = 360 := by
  decide

/-- Cross-multiplied classical Young seminormal Gram ratios `(1, 3/4, 2/3, 5/8)`:
`4 · g̃(T₃) = 3 · g̃(T₂)`, `3 · g̃(T₄) = 2 · g̃(T₂)`, `8 · g̃(T₅) = 5 · g̃(T₂)`. -/
theorem hoefsmitGram_classical_ratios :
    4 * hoefsmitGramDiag qBrClassical .t3 = 3 * hoefsmitGramDiag qBrClassical .t2 ∧
    3 * hoefsmitGramDiag qBrClassical .t4 = 2 * hoefsmitGramDiag qBrClassical .t2 ∧
    8 * hoefsmitGramDiag qBrClassical .t5 = 5 * hoefsmitGramDiag qBrClassical .t2 := by
  decide

/-- Raw isogeny-frame Hodge diagonal `(5, 5, 5, 1)` on `Jac(Bring) ~ E_{5τ₀}³ × E_{τ₀}`
before applying the `S₅`-equivariant period intertwiner `U`. -/
def rawIsogenyHodgeDiag : SYT41 → Int
  | .t2 => 5
  | .t3 => 5
  | .t4 => 5
  | .t5 => 1

/-- **Non-vacuity theorem (`qou-vbz4`):** Without the `S₅`-equivariant intertwiner `U`,
the raw isogeny-frame Hodge diagonal `(5, 5, 5, 1)` and the classical Hoefsmit
diagonal `(576, 432, 384, 360)` are NOT entrywise proportional over `Int`: at `T₂`
vs `T₃`, `rawIsogenyHodgeDiag` is equal (`5 = 5`) whereas `hoefsmitGramDiag` drops
from `576` to `432`. Hence the `S₅`-equivariance / intertwiner premise of the
Schur reduction is load-bearing and non-vacuous. -/
theorem non_vacuity_unaligned_not_proportional :
    ¬ ∃ c : Int, ∀ t : SYT41, hoefsmitGramDiag qBrClassical t = c * rawIsogenyHodgeDiag t := by
  intro ⟨c, hc⟩
  have h2 : (576 : Int) = c * 5 := hc .t2
  have h3 : (432 : Int) = c * 5 := hc .t3
  have hEq : (576 : Int) = 432 := h2.trans h3.symm
  contradiction

end QOU.AlphaEM.StdBlockHoefsmitMarkovSchur
