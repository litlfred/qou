import QOU.BraidKnot.KeystoneHeckeRootsForceTwist

/-!
# General `λ`: the Jucys–Murphy route to `θ_λ = q^{c(λ)}`

`KeystoneHeckeRootsForceTwist.lean` discharged the `KeystoneModularTwist` header's
*"(up to convention)"* hedge for the **one-dimensional** blocks `[n]` and `(1ⁿ)`, by the two roots
of the Hecke relation.  A character argument reaches no further: for `dim V_λ > 1` the generator
is not a scalar, so its twist cannot be read off a root.

This file builds the infrastructure for the general case and carries it as far as is honest.

## What is PROVED here, unconditionally

The combinatorial heart, and the reason the twist is well defined on a block at all:

* `cells` — the Young diagram of `λ` as a `Finset (ℕ × ℕ)`, with `contentSum_eq_cells_sum`
  identifying the corpus's nested-`foldl` `contentSum` with a single sum over that set.
* `sum_content_of_equiv` — **tableau-independence**.  A standard tableau of shape `λ` is, at
  minimum, a bijection between the `n` entries and the cells of `λ`.  Summing the content of each
  entry's cell gives `c(λ)` **for every such bijection**.  This is a reindexing along the
  bijection, so it holds with no hypothesis about Hecke algebras at all.

Tableau-independence is exactly what makes the Jucys–Murphy product a *scalar on the block* rather
than a per-tableau quantity: the JM elements act diagonally on the seminormal basis, and a
diagonal operator is a scalar precisely when its eigenvalues agree across basis vectors.

## What is ASSUMED, and why it is not proved here

`JucysMurphySpectrum` carries **one** hypothesis: that the central full twist's scalar on `V_λ` is
the product over entries of `q^{2·content}` — i.e. that the JM elements act on the seminormal
basis with eigenvalue `q^{2·content}` and that their product is the full twist.

That is a genuine theorem of Hecke-algebra representation theory, and it is **not proved in this
corpus**.  Proving it needs the seminormal form of `H_n(q)` — Young's orthogonal/seminormal basis,
the JM recursion `L_{i+1} = q^{-1} σ_i L_i σ_i`, their commutativity, and the identification of
`∏ᵢ Lᵢ` with `Δ²` — none of which Mathlib or this corpus carries.  Per §"Axiomatization is NOT a
Proof", **this class does not make the general case proved.**  It makes it *conditional*, in the
§3b-cond sense: the class supplies a **hypothesis**, and `fullTwistScalar_eq_theta_sq` **derives**
the conclusion from it using the unconditional combinatorics above.

The honest reading: the hedge in `KeystoneModularTwist.lean` remains **open for `dim V_λ > 1`**.
What this file removes is the *combinatorial* part of the gap, leaving the representation-theoretic
part named, isolated in one class field, and cited.

## The falsifiability check

`fullTwistScalar_single_row` specialises the conditional general result to `λ = [n]` and lands on
`q^{n(n−1)}` — which `theta_single_row_sq` proves **unconditionally** from the Hecke root.  So the
assumed spectrum is not free to be anything: on the blocks where the answer is already known
without it, it reproduces that answer.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1 (content, conjugate).
- [wenzl1988] Hecke algebra representations (seminormal form).
-/

namespace QOU.BraidKnot.Keystone

open Finset QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

variable {R : Type*} [Field R]

/-! ## Infra: the Young diagram as a `Finset` of cells -/

/-- The **cell set** of a Young diagram: `(i, j)` with `i` a row index and `j < λᵢ`. -/
def cells (l : Partition) : Finset (ℕ × ℕ) :=
  (Finset.range l.length).biUnion fun i =>
    (Finset.range (l.getD i 0)).image fun j => (i, j)

theorem mem_cells {l : Partition} {c : ℕ × ℕ} :
    c ∈ cells l ↔ c.1 < l.length ∧ c.2 < l.getD c.1 0 := by
  unfold cells
  simp only [Finset.mem_biUnion, Finset.mem_range, Finset.mem_image]
  constructor
  · rintro ⟨i, hi, j, hj, rfl⟩; exact ⟨hi, hj⟩
  · rintro ⟨h1, h2⟩; exact ⟨c.1, h1, c.2, h2, rfl⟩

/-- The row-blocks of the cell set are pairwise disjoint (they differ in the row coordinate). -/
theorem cells_rows_disjoint (l : Partition) :
    (Finset.range l.length : Finset ℕ).toSet.PairwiseDisjoint
      fun i => (Finset.range (l.getD i 0)).image fun j => ((i, j) : ℕ × ℕ) := by
  intro a _ b _ hab
  simp only [Function.onFun, Finset.disjoint_left, Finset.mem_image, Finset.mem_range]
  rintro c ⟨j, _, rfl⟩ ⟨j', _, hc⟩
  exact hab (congrArg Prod.fst hc).symm

/-- **`contentSum` as a single sum over the cell set.**  Bridges the corpus's nested-`foldl`
definition to a form a reindexing argument can use. -/
theorem contentSum_eq_cells_sum (l : Partition) :
    contentSum l = ∑ c ∈ cells l, cellContent c.1 c.2 := by
  rw [contentSum_eq_finset]
  unfold cells
  rw [Finset.sum_biUnion (cells_rows_disjoint l)]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.sum_image (by intro a _ b _ h; exact (Prod.mk.injEq _ _ _ _ ▸ h).2)]

/-! ## Tableau-independence — the unconditional heart -/

/-- **The content of a tableau's entries sums to `c(λ)`, for every tableau.**

A standard tableau of shape `λ` with `n` entries is in particular a bijection `Fin n ≃ cells λ`.
Summing `content` over the entries reindexes along that bijection to a sum over the cell set, which
is `c(λ)` by `contentSum_eq_cells_sum`.  **No Hecke hypothesis is used** — this is why the
Jucys–Murphy product is a scalar on the block rather than a per-tableau quantity. -/
theorem sum_content_of_equiv {l : Partition} {n : ℕ} (e : Fin n ≃ {c // c ∈ cells l}) :
    ∑ i : Fin n, cellContent (e i).1.1 (e i).1.2 = contentSum l := by
  rw [contentSum_eq_cells_sum]
  rw [Equiv.sum_comp e fun c : {c // c ∈ cells l} => cellContent c.1.1 c.1.2]
  exact Finset.sum_coe_sort (cells l) fun c => cellContent c.1 c.2

/-- A tableau pins the entry count to the number of cells. -/
theorem card_eq_of_tableau {l : Partition} {n : ℕ} (e : Fin n ≃ {c // c ∈ cells l}) :
    n = (cells l).card := by
  simpa using Fintype.card_congr e

/-- `∏ q^{f i} = q^{∑ f i}` over a finite index set, for `q ≠ 0`. -/
theorem prod_zpow_eq_zpow_sum {ι : Type*} (s : Finset ι) (q : R) (hq : q ≠ 0) (f : ι → ℤ) :
    ∏ i ∈ s, q ^ (f i) = q ^ (∑ i ∈ s, f i) := by
  classical
  induction s using Finset.induction with
  | empty => simp
  | insert a s ha ih =>
      rw [Finset.prod_insert ha, Finset.sum_insert ha, ih, zpow_add₀ hq]

/-! ## The Jucys–Murphy hypothesis (§3b-cond) and the conditional general theorem -/

/-- **The Jucys–Murphy spectrum hypothesis for the block `V_λ`.**

`fullTwistScalar` is the scalar by which the central full twist `Δ²` acts on `V_λ` (Schur: it is a
scalar because `Δ²` is central).  `tableau` is a standard tableau, as a bijection between the `n`
entries and the cells of `λ`.

The single assumed field is `fullTwistScalar_eq`: that this scalar is the product over entries of
`q^{2·content}`.  **This is the deep input and it is NOT proved in this corpus** — it packages the
seminormal-form facts (JM elements act diagonally with eigenvalue `q^{2·content}`; their product
is `Δ²`).  See the module docstring.

Non-degeneracy (§3b-cond item 5).  `fullTwistScalar` is a **parameter**, not a field: it is
supplied by whatever exhibits the twist action, and the class *constrains* it.  An earlier draft of
this file made it a field, which was degenerate — the class could then be satisfied for any `λ` by
simply *defining* the scalar to be the product, so it constrained nothing.  As a parameter, an
instance exists only when the supplied scalar really is the JM product.

`fullTwist_eq_theta_sq` **derives** `θ_λ²` from that hypothesis via the unconditional
tableau-independence result — the content-sum identification is not assumed anywhere. -/
-- Ref: [wenzl1988] Hecke algebra representations (seminormal form; JM spectrum)
class JucysMurphySpectrum (R : Type*) [Field R] (q : R) (l : Partition) (n : ℕ)
    (fullTwistScalar : R) : Prop where
  /-- A standard tableau of shape `λ`, as a bijection entries ≃ cells. -/
  tableau : Nonempty (Fin n ≃ {c // c ∈ cells l})
  /-- **Assumed**: the given scalar is the product of the JM eigenvalues `q^{2·content}`. -/
  fullTwistScalar_eq : ∀ e : Fin n ≃ {c // c ∈ cells l},
    fullTwistScalar = ∏ i : Fin n, q ^ (2 * cellContent (e i).1.1 (e i).1.2)

/-- **The general-`λ` twist, conditional on the Jucys–Murphy spectrum.**

Given the assumed JM spectrum, the full twist acts on `V_λ` by `θ_λ² = q^{2c(λ)}` — for **every**
partition, not only the one-dimensional blocks.

The derivation is the unconditional part: the product of `q^{2·content}` over entries collapses to
`q` raised to the *sum* of contents (`prod_zpow_eq_zpow_sum`), and that sum is `c(λ)` for any
tableau (`sum_content_of_equiv`).  Neither step assumes anything about Hecke algebras.

**This does not prove the general case** — it reduces it to the one named, cited hypothesis. -/
theorem fullTwist_eq_theta_sq (q : R) (hq : q ≠ 0) (l : Partition) (n : ℕ) (s : R)
    [J : JucysMurphySpectrum R q l n s] : s = (theta q l) ^ 2 := by
  obtain ⟨e⟩ := J.tableau
  rw [J.fullTwistScalar_eq e, prod_zpow_eq_zpow_sum _ q hq]
  have hsum : ∑ i : Fin n, 2 * cellContent (e i).1.1 (e i).1.2 = 2 * contentSum l := by
    rw [← Finset.mul_sum, sum_content_of_equiv e]
  rw [hsum]
  unfold theta
  rw [← zpow_natCast (q ^ contentSum l) 2, ← zpow_mul]
  congr 1
  push_cast
  ring

/-! ## Falsifiability check against the unconditional one-dimensional results -/

/-- **The conditional general result reproduces the unconditional one-row answer.**

On `λ = [n]` the Hecke-root argument already gives `θ² = q^{n(n−1)}` with no JM input
(`theta_single_row_sq`).  The JM route must land on the same value — and does.  So the assumed
spectrum is constrained by an independently-proved case rather than free. -/
theorem fullTwist_single_row (q : R) (hq : q ≠ 0) (n : ℕ) (s : R)
    [JucysMurphySpectrum R q [n] n s] : s = q ^ fullTwistLength n := by
  rw [fullTwist_eq_theta_sq q hq [n] n s, theta_single_row_sq]

/-- The same check on the one-column block, whose unconditional value comes from the **sign** root. -/
theorem fullTwist_single_col (q : R) (hq : q ≠ 0) (n : ℕ) (s : R)
    [JucysMurphySpectrum R q (conj [n]) n s] : s = (q ^ fullTwistLength n)⁻¹ := by
  rw [fullTwist_eq_theta_sq q hq (conj [n]) n s, theta_single_col_sq]

/-! ## Non-degeneracy: the hypothesis PINS the scalar, and is satisfiable -/

/-- **The hypothesis determines the scalar uniquely.**  Two instances for the same block must agree,
because each forces the scalar to `θ_λ²`.  So `JucysMurphySpectrum` is not satisfiable by an
arbitrary `s` — which is what makes the conditional results above non-vacuous. -/
theorem jm_scalar_unique (q : R) (hq : q ≠ 0) (l : Partition) (n : ℕ) (s s' : R)
    [JucysMurphySpectrum R q l n s] [JucysMurphySpectrum R q l n s'] : s = s' := by
  rw [fullTwist_eq_theta_sq q hq l n s, fullTwist_eq_theta_sq q hq l n s']

/-- The single-cell diagram has exactly one cell, `(0,0)`. -/
theorem cells_one : cells [1] = {(0, 0)} := by decide

/-- **The hypothesis is satisfiable.**  On the one-cell diagram `λ = (1)` the JM product is `q⁰ = 1`,
and the class instance exists with scalar `1`.  Together with `jm_scalar_unique` this shows the
class is a genuine constraint: inhabited, but only at the right value.

This is a consistency witness, not evidence for the general spectrum -- see the module docstring. -/
instance jmSingleCell (q : R) : JucysMurphySpectrum R q [1] 1 1 where
  tableau := ⟨Fintype.equivOfCardEq (by simp [cells_one])⟩
  fullTwistScalar_eq := by
    intro e
    have h := (e 0).2
    rw [mem_cells] at h
    have h1 : ((e 0 : {c // c ∈ cells [1]}) : ℕ × ℕ).1 = 0 := by
      have hb : ((e 0 : {c // c ∈ cells [1]}) : ℕ × ℕ).1 < 1 := h.1
      omega
    have h2 : ((e 0 : {c // c ∈ cells [1]}) : ℕ × ℕ).2 = 0 := by
      have hb := h.2
      rw [h1] at hb
      have hb' : ((e 0 : {c // c ∈ cells [1]}) : ℕ × ℕ).2 < 1 := hb
      omega
    rw [Fin.prod_univ_one, h1, h2]
    simp [cellContent]

end QOU.BraidKnot.Keystone
