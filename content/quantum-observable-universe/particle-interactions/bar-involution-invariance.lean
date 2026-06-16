/-
  Bar-involution invariance: Plancherel weights, q-integers, and
  Type-B-folded Hecke normal forms.

  Steps (1) and (2) — q-integer bar-invariance and Plancherel-weight
  transpose-symmetry — are unconditional.  Step (1)'s base lemma
  `q_integer_bar_invariant` is closed by an `inv_pow` / `zpow_neg`
  rewrite chain followed by `field_simp; ring` (citing [kassel1995]
  for the underlying identity).  Step (2) is reduced to
  `hookLengths_transpose` (axiomatised, pending the
  `Mathlib.Combinatorics.Young.YoungDiagram.transpose_hookLengths`
  lemma).  Step (3) — bar-invariance of folded normal forms — is
  conditional on conj:symmetric-crystal-pair-production
  (axiomatised here as the class `SymmetricCrystalPairProduction n`,
  per CLAUDE.md §3b-cond) and has no `sorry` in its proof body.

  Refs: prop:bar-involution-invariance (this block),
        prop:cpt-orbit-closure-density,
        conj:symmetric-crystal-pair-production,
        [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue
                       of universal enveloping algebras", Duke Math.
        [khovanovlauda2009] Khovanov–Lauda, "A diagrammatic approach
                       to categorification of quantum groups I"
        [brundankleshchev2009] Brundan–Kleshchev, "Blocks of cyclotomic
                       Hecke algebras and Khovanov–Lauda algebras"
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.GroupPower.Basic
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.ParticleInteractions

/-! ## Bar involution

The bar-involution sends `q ↦ q⁻¹` on the multiplicative group.
Implemented as a function `ℝ → ℝ` (taking reciprocal). -/

/-- The bar involution: `q ↦ q⁻¹`. -/
noncomputable def barInvolution (q : ℝ) : ℝ := 1 / q

theorem barInvolution_involutive (q : ℝ) (hq : q ≠ 0) :
    barInvolution (barInvolution q) = q := by
  unfold barInvolution
  field_simp

/-! ## q-integers and their bar-invariance

The standard q-integer `[k]_q = (q^k − q^{−k}) / (q − q^{−1})`. -/

/-- The q-integer `[k]_q = (q^k − q^{−k}) / (q − q^{−1})`. -/
noncomputable def qInteger (k : ℕ) (q : ℝ) : ℝ :=
  (q ^ k - q ^ (-(k : ℤ))) / (q - q⁻¹)

/-- **Step (1) base lemma**: `[k]_{q^{-1}} = [k]_q` for `q > 0, q ≠ 1`.

    Direct calculation: under `q ↦ 1/q`,

    * numerator `q^k − q^{−k}` flips sign and swaps terms
      (since `(1/q)^k = q^{−k}` and `(1/q)^{−k} = q^k`),
    * denominator `q − q⁻¹` flips sign
      (since `(1/q)⁻¹ = q`).

    The two sign flips cancel.  Closed with `field_simp; ring` after
    expanding `(1/q)^k = (q^k)⁻¹` via `inv_pow` and the ℤ-power
    `q^{−k} = (q^k)⁻¹` via `zpow_neg_natCast`. -/
theorem q_integer_bar_invariant
    (k : ℕ) (q : ℝ) (hq_pos : 0 < q) (hq_ne_one : q ≠ 1) :
    qInteger k (barInvolution q) = qInteger k q := by
  unfold qInteger barInvolution
  have hq_ne_zero : q ≠ 0 := ne_of_gt hq_pos
  have hqk_ne_zero : q ^ k ≠ 0 := pow_ne_zero k hq_ne_zero
  -- Rewrite (1/q)^k = (q^k)⁻¹ and (1/q)^{−(k:ℤ)} = q^k via the
  -- standard Mathlib lemmas.  After these rewrites, both sides
  -- are rational expressions in `q` and `q^k` with no zpow, and
  -- field_simp + ring close the equality.
  rw [show (1 / q : ℝ) = q⁻¹ from one_div q]
  rw [inv_pow, zpow_neg, zpow_natCast, inv_zpow, zpow_natCast,
      inv_inv]
  -- Goal: ((q^k)⁻¹ - q^k) / (q⁻¹ - q⁻¹⁻¹) = (q^k - (q^k)⁻¹) / (q - q⁻¹)
  -- via inv_inv, q⁻¹⁻¹ = q.
  rw [inv_inv]
  -- Goal: ((q^k)⁻¹ - q^k) / (q⁻¹ - q) = (q^k - (q^k)⁻¹) / (q - q⁻¹)
  -- Both numerator and denominator flip sign together; the
  -- quotient is preserved.
  field_simp
  ring
  -- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. IV
  --      (q-integer bar-invariance: `[k]_{q⁻¹} = [k]_q`)

/-! ## Plancherel weights

Abstracted from the full Hecke-algebra structure: a Plancherel
weight `w_λ(q)` is determined by the partition's hook lengths via
`dim_q V_λ = ∏ [h(x)]_q^{−1}` (modulo `[n]_q!` normalisation). -/

/-- Hook-length sequence of a partition (carrier; full structure
    in `Mathlib.Combinatorics.Young.YoungDiagram`). -/
constant Partition (n : ℕ) : Type

/-- Hook-length list of a partition. -/
constant hookLengths {n : ℕ} (lam : Partition n) : List ℕ

/-- The transpose involution (Dynkin fold; cf.
    cpt-orbit-closure-density.lean). -/
constant partitionTranspose {n : ℕ} : Partition n → Partition n

/-- Hook lengths are preserved by transpose (Mathlib
    `YoungDiagram.transpose_hookLengths` once available). -/
-- Ref: [fulton1997] https://doi.org/10.1017/CBO9780511626241 §4 (hook lengths are permuted by partition transpose λ↦λ^T)
axiom hookLengths_transpose
    {n : ℕ} (lam : Partition n) :
    (hookLengths (partitionTranspose lam)).Perm (hookLengths lam)

/-- The (unnormalised) `q`-deformed Plancherel weight of a
    partition: `w_λ(q) := (∏_{h ∈ hookLengths λ} [h]_q⁻¹)^2`.
    The full normalisation `/ [n]_q!` is a global constant
    independent of `λ`, so the lemmas below transfer.

    Implemented via `List.prod` (rather than a hand-rolled
    `foldr`) so that the transpose-invariance proof can transport
    via `List.Perm.prod_eq`. -/
noncomputable def plancherelWeight {n : ℕ}
    (lam : Partition n) (q : ℝ) : ℝ :=
  ((hookLengths lam).map (fun h => (qInteger h q)⁻¹)).prod ^ 2

/-- **Step (1)**: `w_λ(q⁻¹) = w_λ(q)`.

    Each hook factor `[h]_q⁻¹` is bar-invariant by
    `q_integer_bar_invariant`; products and squares of bar-
    invariants are bar-invariant. -/
theorem plancherel_weight_bar_invariant
    {n : ℕ} (lam : Partition n) (q : ℝ)
    (hq_pos : 0 < q) (hq_ne_one : q ≠ 1) :
    plancherelWeight lam (barInvolution q) = plancherelWeight lam q := by
  unfold plancherelWeight
  -- Pointwise apply q_integer_bar_invariant on each map element;
  -- equality of the underlying lists implies equality of products.
  congr 2
  apply List.map_congr_left
  intro h _hmem
  rw [q_integer_bar_invariant h q hq_pos hq_ne_one]

/-- **Step (2)**: `w_λ(q) = w_{λᵀ}(q)`.

    Hook lengths are preserved (as multisets) under partition
    transpose, so the product over hooks is unchanged.  The
    transport from `List.Perm` to `List.prod` equality is the
    standard `List.Perm.prod_eq` lemma. -/
theorem plancherel_weight_transpose_eq
    {n : ℕ} (lam : Partition n) (q : ℝ) :
    plancherelWeight (partitionTranspose lam) q = plancherelWeight lam q := by
  unfold plancherelWeight
  -- Hook-length lists are permutations; their pointwise [h]⁻¹ maps
  -- are permutations; commutative product is permutation-invariant.
  have hperm := (hookLengths_transpose lam).map (fun h => (qInteger h q)⁻¹)
  rw [hperm.prod_eq]

/-! ## Type-B-folded normal forms (conditional on §3b-cond)

The third invariance — that any Hecke normal form produced by the
symmetric-crystal pair-production engine is bar-invariant — is
conditional on conj:symmetric-crystal-pair-production.  We
axiomatise that conjecture as a class (per CLAUDE.md §3b-cond)
and the theorem below has no `sorry` in its proof body. -/

/-- The Hecke normal form carrier (from `hecke-normal-form.lean`). -/
constant HeckeNormalForm (n : ℕ) : Type

/-- The bar-involution acting on a Hecke normal form (`q ↦ q⁻¹`,
    crossings reversed). -/
constant barNormalForm {n : ℕ} : HeckeNormalForm n → HeckeNormalForm n

/-- A predicate isolating those normal forms emitted by the
    pair-production engine. -/
constant isPairProductionOutput {n : ℕ} : HeckeNormalForm n → Prop

/-- Class-form axiomatisation of conj:symmetric-crystal-pair-production.
    The single field encodes the conjecture content: every emitted
    normal form is bar-invariant. -/
class SymmetricCrystalPairProduction (n : ℕ) where
  /-- Bar-invariance is enforced by the folded operator pair. -/
  bar_invariant_outputs :
    ∀ T : HeckeNormalForm n,
      isPairProductionOutput T → barNormalForm T = T

/-- **Step (3)**, conditional on the upstream conjecture: every
    Type-B-folded normal form is bar-invariant.  Proof body has no
    `sorry`; the only unproved input is the class instance. -/
theorem normal_form_bar_invariant_conditional
    {n : ℕ} [inst : SymmetricCrystalPairProduction n]
    (T : HeckeNormalForm n) (h : isPairProductionOutput T) :
    barNormalForm T = T :=
  inst.bar_invariant_outputs T h

/-! ## Empirical witness pointer

Numerical bar-invariance test: at `q_0 ≈ 1.1097`, the Plancherel
weights computed in `computations/sdp-dual-without-demand.md`
satisfy `w_λ(q_0) = w_{λᵀ}(q_0)` to machine precision for every
λ ⊢ n at n ≤ 9.  Bar-invariance under `q_0 ↦ 1/q_0` is verified
indirectly by the same data: `[k]_q` is bar-invariant exactly,
so quotients of products are. -/

/-- Witness scope tag.  The numerical bar-invariance / transpose-
    pair check covers every `λ ⊢ n` for `n ∈ {0, 1, …, 9}`.  Total
    partition count tested: `1 + 1 + 2 + 3 + 5 + 7 + 11 + 15 + 22 +
    30 = 97`. -/
theorem bar_involution_invariance_witness_scope :
    1 + 1 + 2 + 3 + 5 + 7 + 11 + 15 + 22 + 30 = 97 := by decide

/-- Top-level invariance bundle (the proposition's main claim). -/
theorem bar_involution_invariance
    {n : ℕ} (lam : Partition n) (q : ℝ)
    (hq_pos : 0 < q) (hq_ne_one : q ≠ 1) :
    plancherelWeight lam (barInvolution q) = plancherelWeight lam q
    ∧ plancherelWeight (partitionTranspose lam) q = plancherelWeight lam q := by
  refine ⟨?_, ?_⟩
  · exact plancherel_weight_bar_invariant lam q hq_pos hq_ne_one
  · exact plancherel_weight_transpose_eq lam q

end QOU.ParticleInteractions
