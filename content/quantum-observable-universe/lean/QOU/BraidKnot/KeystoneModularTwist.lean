import QOU.BraidKnot.KeystoneC2QDimTranspose

/-!
# Keystone modular data (ii): the ribbon twist / modular `T`-matrix `θ_λ = q^{c(λ)}`

`KeystoneVerlindeSMatrixBridge.lean` equips the keystone (Beasley–Witten localization) modular tensor
category with the **first** genuine piece of modular data: the **vacuum `S`-matrix row** `S_{0λ}`
(`VerlindeModularData`, weighting the Verlinde measure `μ(λ) = S_{0λ}²`).  A modular tensor category
carries *two* pieces of modular data: the `S`-matrix and the diagonal **modular `T`-matrix** / **ribbon
twist** `θ_λ`.  This file adds the **second**: the twist on a simple object.

In a ribbon / modular category the twist on the simple `V_λ` is the topological framing anomaly
`θ_λ = q^{κ_λ}`, and for the Hecke MTC the exponent is (up to convention) the **content sum**
`κ_λ = c(λ) = Σ_{(i,j)∈λ} (j − i)` — the quadratic-Casimir eigenvalue on `V_λ`.  We build, sorry-free:

* `theta q λ := q ^ (c(λ))` — the twist, as a `zpow` over a generic `{R : Type*} [GroupWithZero R]`
  (§7c: purely algebraic — no ordering, no `Real.sqrt`, no `ℝ`; strictly weaker base ring than the
  `S`-matrix side, which needed `ℝ` for `D = √(Σ d_q²)`).
* `theta_conj` — the **`C2`-analogue for the twist**: `θ_{λ'} = θ_λ⁻¹`, the twist's chirality /
  bar-parity behaviour, complementing the `S`-matrix's `qDim_conj` (`d_q(λ') = d_q(λ)`).  It follows
  from the **signed** content flip `c(λ') = − c(λ)` (transpose negates content), which this file
  proves in general — the corpus previously carried only the *squared* content invariance
  (`KeystoneC2ContentTranspose.sumSqContents_conj`) and the single `[2] ↔ [1,1]` instance
  (`KeystoneChiralityInvolution.conjugate_two_content_flip`), never the signed general statement.
* `ModularTwistData` — a structure carrying the abstract twist datum `theta` + `theta_conj`, and
  `heckeTwistData`, the Hecke instance `θ_λ = q^{c(λ)}` mirroring `heckeVerlindeData` (note: needs
  **no** positivity hypothesis `1 < q`, unlike the `S`-matrix data — another sign the twist is the
  purely-algebraic half of the modular data).
* Consistency lemmas: the twist is **trivial on the vacuum** (`theta q [] = 1`, `c(∅) = 0`), and on
  the trivial / one-row rep `[n]` it is `q^{c([n])}` with `c([n]) = Σ_{j<n} j = \binom{n}{2}`
  (`two_mul_contentSum_single_row`, the triangular number — the symmetric-rep framing anomaly).

**Honest scope.**  This is a genuine formalize-first *extension of the Verlinde MTC modular data* —
it makes the `T`-matrix explicit and proves its transpose law from the content-sum combinatorics.  It
does **not** prove the physics that the BW localization of `S³/2I` *yields* this modular category:
that category identification is still owner-gated (`bwS0_eq_hecke` in
`KeystoneVerlindeSMatrixBridge.lean`; narrow Subgoal-2 reversal #2503/#2524).  No fit, no physics
claim — only the algebra of the twist and its chirality behaviour.

Refs:
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (`S`, `T` modular data).
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1 (content, conjugate).
-/

namespace QOU.BraidKnot.Keystone

open Finset QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

/-! ## The signed content sum is transpose-antisymmetric: `c(λ') = − c(λ)`

The corpus proves the *squared* content sum is transpose-INVARIANT (`sumSqContents_conj`); the twist
needs the *signed* content sum, which is transpose-ANTISYMMETRIC.  Both use the same `cell_fubini`
row/column transpose of `IdentityIContentDecomposition`; here squaring is dropped, so the per-cell
content sign survives and the sum negates. -/

/-- A multiplicative-analogue-free additive `foldl` over `range n` is the `Finset.sum` (the additive
twin of `KeystoneC2QDimTranspose.foldl_mul_range`; used to unfold `contentSum`'s nested `foldl`). -/
theorem foldl_add_range (n : ℕ) (f : ℕ → ℤ) :
    (List.range n).foldl (fun acc i => acc + f i) 0 = ∑ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.foldl_append, ih, Finset.sum_range_succ]
    simp

/-- **`contentSum` as a `Finset` double sum.**  Unfold the nested `foldl` into the row×column cell
double sum `Σ_i Σ_{j<λ_i} c(i,j)`, matching the shape `cell_fubini` transposes. -/
theorem contentSum_eq_finset (l : List ℕ) :
    contentSum l = ∑ i ∈ Finset.range l.length,
      ∑ j ∈ Finset.range (l.getD i 0), cellContent i j := by
  unfold contentSum
  simp only [foldl_add_range]

/-- **Column form of `contentSum`** (via `cell_fubini`): the row-indexed cell sum equals the
column-indexed one, `Σ_i Σ_{j<λ_i} c(i,j) = Σ_j Σ_{i<colLen j} c(i,j)`. -/
theorem contentSum_col (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    contentSum l = ∑ j ∈ Finset.range (l.headD 0),
      ∑ i ∈ Finset.range (colLen l j), cellContent i j := by
  rw [contentSum_eq_finset]
  exact cell_fubini l hl cellContent

/-- **Column form of `contentSum (conj l)`**: rows of the merged conjugate `conj l` are the column
lengths `colLen l r` (`conj_getD` / `conj_length`), so its cell double sum is the column-indexed one
over `l`'s diagram — with cell `(r,c)` carrying content `c(r,c) = c − r`. -/
theorem contentSum_conj_col (l : List ℕ) :
    contentSum (conj l) = ∑ r ∈ Finset.range (l.headD 0),
      ∑ c ∈ Finset.range (colLen l r), cellContent r c := by
  rw [contentSum_eq_finset, conj_length]
  apply Finset.sum_congr rfl
  intro r hr
  rw [conj_getD l r (Finset.mem_range.mp hr)]

/-- **`C2` for the signed content sum (Σ-level): `c(λ') = − c(λ)`.**  Content negates under transpose
(`cellContent_transpose_neg`: `c(r,c) = − c(c,r)`); the two column forms above index the *same* cell
set, so the sum negates.  This is the signed companion of the corpus's `sumSqContents_conj` (squared,
invariant), and the general statement behind the single `conjugate_two_content_flip` instance. -/
theorem contentSum_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    contentSum (conj l) = - contentSum l := by
  rw [contentSum_conj_col l, contentSum_col l hl, ← Finset.sum_neg_distrib]
  apply Finset.sum_congr rfl
  intro r _
  rw [← Finset.sum_neg_distrib]
  apply Finset.sum_congr rfl
  intro c _
  unfold cellContent
  ring

/-- **`C2` on the canonical `Partition.conjugate`.**  Bridge `contentSum_conj` (stated on the merged
`conj`) to the `QPartitionCombinatorics` conjugate via `conjugate_eq_conj`. -/
theorem contentSum_conjugate (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    contentSum (Partition.conjugate l) = - contentSum l := by
  rw [conjugate_eq_conj l hl]; exact contentSum_conj l hl

/-! ## The ribbon twist / modular `T`-matrix `θ_λ = q^{c(λ)}` -/

variable {R : Type*} [GroupWithZero R]

/-- **The ribbon twist / modular `T`-matrix eigenvalue on the simple `V_λ`**: `θ_λ = q^{c(λ)}`, the
topological framing anomaly, with exponent the content sum `c(λ) = Σ_{(i,j)∈λ}(j−i)` (the
quadratic-Casimir eigenvalue).  A `zpow` (the exponent is a possibly-negative `ℤ`), over a generic
`GroupWithZero` (§7c — purely algebraic, no `ℝ`). -/
def theta (q : R) (l : List ℕ) : R := q ^ (contentSum l)

/-- **The twist's chirality / bar-parity law (the `C2`-analogue for the `T`-matrix): `θ_{λ'} = θ_λ⁻¹`.**
The transpose negates the content sum (`contentSum_conjugate`), and `q^{−c(λ)} = (q^{c(λ)})⁻¹`
(`zpow_neg`, valid in any `GroupWithZero`).  Complements the `S`-matrix's `qDim_conj`
(`d_q(λ') = d_q(λ)`): the `S`-datum is transpose-INVARIANT, the `T`-datum transpose-INVERTS. -/
theorem theta_conjugate (q : R) (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    theta q (Partition.conjugate l) = (theta q l)⁻¹ := by
  unfold theta
  rw [contentSum_conjugate l hl, zpow_neg]

/-- **The twist is trivial on the vacuum**: `θ_∅ = 1` (`c(∅) = 0`, the empty diagram has no cells). -/
@[simp] theorem theta_nil (q : R) : theta q [] = 1 := by
  unfold theta; rw [contentSum_nil]; exact zpow_zero q

/-! ## The trivial / one-row rep `[n]`: content sum is the triangular number `\binom{n}{2}` -/

/-- The content sum of the one-row shape `[n]` is `Σ_{j<n} j` (its cells are `(0,0),…,(0,n−1)` with
content `j − 0 = j`). -/
theorem contentSum_single_row (n : ℕ) :
    contentSum [n] = ∑ j ∈ Finset.range n, (j : ℤ) := by
  rw [contentSum_eq_finset]
  simp only [List.length_singleton, Finset.sum_range_one, List.getD_cons_zero]
  apply Finset.sum_congr rfl
  intro j _
  simp [cellContent]

/-- **The one-row (trivial / symmetric) rep has content sum `\binom{n}{2}`**: `2·c([n]) = n(n−1)`, the
triangular number (`two_mul_sum_range_int`).  So its framing anomaly is `θ_{[n]} = q^{\binom n2}`. -/
theorem two_mul_contentSum_single_row (n : ℕ) :
    2 * contentSum [n] = (n : ℤ) * ((n : ℤ) - 1) := by
  rw [contentSum_single_row, two_mul_sum_range_int]

/-- The twist on the one-row rep `[n]`, exponent made explicit: `θ_{[n]} = q^{Σ_{j<n} j} = q^{\binom n2}`. -/
theorem theta_single_row (q : R) (n : ℕ) :
    theta q [n] = q ^ (∑ j ∈ Finset.range n, (j : ℤ)) := by
  unfold theta; rw [contentSum_single_row]

/-! ## `ModularTwistData` — the abstract `T`-matrix datum, and its Hecke instance -/

/-- **Modular `T`-matrix / ribbon-twist data** of the keystone modular category — the *second* piece
of modular data, complementing `VerlindeModularData`'s vacuum `S`-matrix row.  Carries the simple
objects (Hecke blocks), the transpose involution, and the diagonal twist `theta` with its chirality
law `theta (λ') = theta(λ)⁻¹`.  Generic `GroupWithZero` (the twist is purely multiplicative — no
positivity / `ℝ` needed, unlike the `S`-matrix side). -/
structure ModularTwistData (R : Type*) [GroupWithZero R] where
  /-- Partition index for the Hecke block `λ ⊢ n`. -/
  Part : Type*
  /-- The finite set of Hecke partition blocks. -/
  parts : Finset Part
  /-- The transpose involution `λ ↦ λ′`. -/
  conj : Part → Part
  /-- Blocks closed under transpose. -/
  conj_mem : ∀ p ∈ parts, conj p ∈ parts
  /-- The ribbon twist / modular `T`-matrix eigenvalue `θ_λ`. -/
  theta : Part → R
  /-- **The twist's chirality law** `θ_{λ′} = θ_λ⁻¹` (the `C2`-analogue for the `T`-matrix). -/
  theta_conj : ∀ p ∈ parts, theta (conj p) = (theta p)⁻¹

/-- **The Hecke twist `θ_λ = q^{c(λ)}` realizes `ModularTwistData`** on any conjugate-closed set `P`
of weakly-decreasing blocks.  `theta_conj` is discharged by `theta_conjugate` (`θ_{λ'} = θ_λ⁻¹` from
the content flip).  Mirrors `heckeVerlindeData`, but needs **no** `1 < q` hypothesis — the twist is
the algebraic half of the modular data.  Given the (owner-gated) category identification, this is the
`T`-matrix of the keystone MTC, alongside `heckeVerlindeData`'s `S`-matrix. -/
def heckeTwistData (q : R) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P) :
    ModularTwistData R where
  Part := List ℕ
  parts := P
  conj := Partition.conjugate
  conj_mem := hconj
  theta := theta q
  theta_conj := fun p hp => theta_conjugate q p (hsorted p hp)

/-- **Non-vacuity — `ModularTwistData` is inhabited** (the transpose pair `{[2], [1,1]}` over `ℝ`),
so the structure and `heckeTwistData` are not vacuous.  Here `θ_{[2]} = q`, `θ_{[1,1]} = q⁻¹`, and
`[2]' = [1,1]` exhibits `θ_{λ'} = θ_λ⁻¹`. -/
noncomputable example : ModularTwistData ℝ :=
  heckeTwistData (3 / 2) {[2], [1, 1]}
    (by decide)
    (by decide)

end QOU.BraidKnot.Keystone
