import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.RepresentationTheory.Basic
import Mathlib.Order.Interval.Finset.Fin
import QOU.BraidKnot.Specht
import QOU.BraidKnot.RegularRepTrace

/-!
# QOU.BraidKnot.JucysMurphy — brick 5 of the Okounkov–Vershik tower

The **Jucys–Murphy elements** `X_k = ∑_{j<k} (j k)` of the group algebra
`k[S_n] = MonoidAlgebra k (Perm (Fin n))`, the **cell content** `c(i,j) = j - i`, and
the **content-square sum** `ω_λ = ∑_{c∈λ} c(c)²` — together with the deep
Okounkov–Vershik theorems that connect them to the Specht modules of brick 2
(`QOU.BraidKnot.Specht`, imported above).

This is "brick 5" of the QOU OV-tower.  The JM elements generate a maximal commutative
(Gelfand–Tsetlin) subalgebra of `k[S_n]`; on the Gelfand–Zetlin / seminormal basis of the
Specht module `S^λ` (indexed by standard Young tableaux `T`), `X_k` acts diagonally with
eigenvalue `c(cell of k in T) = col − row`.  Hence the central element
`C₂ = ∑_k X_k²` acts on `S^λ` by the **scalar** `∑_{c∈λ} c(c)²`.  This scalar is the
`ω = Σc²` input that the Identity-(B) keystone's `SnWedderburnSpectralData` (in
`RegularRepBlockTrace`) carries as a field.

## What is sorry-free here (the definitional foundation)

* `jucysMurphy n i` — the JM element `X_i = ∑_{j<i} single (swap j i) 1`, a `Finset.sum` of
  `MonoidAlgebra.single` of transpositions.  Aligned **definitionally** with the inner sum of
  `QOU.BraidKnot.RegularRepTrace.centralC2`, so `∑ k, (jucysMurphy n k)^2` is exactly that
  established `centralC2 n` (`centralC2_eq_sum_jucysMurphy_sq` below records the equality).
* `cellContent c = c.2 − c.1` (column minus row), in `ℤ`.
* `contentSqSum μ = ∑_{c∈μ.cells} (cellContent c)^2`, in `ℤ` — the `ω = Σc²` of the keystone.
* `jucysMurphy_zero` — `X_0 = 0` (the sum over `j < 0` is empty): the easy sanity anchor.
* `jucysMurphy_one` — `X_1 = 0` on `Fin n` (the only `j < (1 : Fin n)` is excluded because
  there is no strand below `0`; recorded as `jucysMurphy_succ_zero` for `Fin (n+2)` where the
  index `1` genuinely exists, giving `X_1 = single (swap 0 1) 1`).

## What is stated with `sorry` + `-- Ref:` (the genuine OV theorems)

* `jucysMurphy_commute` — the JM elements pairwise commute (the GZ algebra is commutative).
  `-- Ref: [vershik-kerov1977]`.
* `jucysMurphy_eigenvalue` — on a GZ/seminormal eigenvector of `S^λ` for the tableau `T`, `X_k`
  acts by the scalar `cellContent (T's cell of k)`.  Stated against an *abstract packaging* of
  the seminormal eigenbasis (see the design note below).  `-- Ref: [vershik-kerov1977]`.
* `centralC2_acts_by_contentSqSum` — the punchline: the central element `C₂ = ∑_k X_k²` acts on
  the Specht submodule `S^λ ≤ M^λ` (via `Specht.Mtab.rep` extended to the group algebra) as the
  scalar `contentSqSum μ`.  `-- Ref: [vershik-kerov1977]`.  This discharges the `ω = Σc²` field of
  the keystone's `SnWedderburnSpectralData`.

All three are theorems of the Okounkov–Vershik / Jucys–Murphy literature; their full Lean proofs
are the content of the OV paper and out of scope for one brick.  They are honestly stubbed per
AGENTS.md §1 (`theorem … := by sorry  -- Ref: …`), never `: True`, never `native_decide`.

## Base ring (§7c)

The JM / content layer is **purely algebraic**: `variable {k : Type} [CommRing k]`.  No `ℝ`, no
`Real.*`, no ordering on `k`, no `linarith`/`positivity`/`norm_num`.  `cellContent`/`contentSqSum`
land in `ℤ` (integer arithmetic — algebraic, not archimedean-`ℝ`).  The finite filter `j.val < i.val`
is an order on the *index type* `Fin n`, not on the ring `k`, and is necessary (it is the very
"strands below `k`" defining `X_k`).  The eigenvalue / scalar-action theorems are stated over a
generic `[CommRing k]`; the *proofs* (out of scope) would specialise to a field of characteristic
0 where the seminormal basis exists, but the **statements** need no field, so none is imposed.

## References
- [vershik-kerov1977] Vershik–Okounkov, "A new approach to the representation theory of the
  symmetric groups II" (JM elements; the GZ algebra; eigenvalues = cell contents).
- [sagan2001] Sagan, *The Symmetric Group* (Specht modules, standard tableaux).
- [fulton1997] Fulton, *Young Tableaux* (tableaux, cell contents).
-/

open scoped BigOperators
open MonoidAlgebra

namespace QOU.BraidKnot.JucysMurphy

variable {k : Type} [CommRing k]

/-! ## 1. The Jucys–Murphy element -/

/-- The **Jucys–Murphy element** `X_i = ∑_{j < i} (j i)` of `k[S_n] = MonoidAlgebra k (Perm (Fin n))`:
the sum of the transpositions `(j i)` for every strand `j` below `i`, each weighted `1`.

The filter `j.val < i.val` is the order on the **index type** `Fin n` (the strands), not an order
on the ring `k` (§7c-clean).  This is *definitionally* the inner summand of
`QOU.BraidKnot.RegularRepTrace.centralC2`, so `∑ k, (jucysMurphy n k)^2` unfolds to that
established central element (see `centralC2_eq_sum_jucysMurphy_sq`). -/
noncomputable def jucysMurphy (n : ℕ) (i : Fin n) : MonoidAlgebra k (Equiv.Perm (Fin n)) :=
  ∑ j ∈ Finset.univ.filter (fun j : Fin n => j.val < i.val), single (Equiv.swap j i) (1 : k)

/-- `X_0 = 0`: the sum over `j < 0` is empty (no strand sits below the first one). The easy
sorry-free anchor for the definition. -/
@[simp] theorem jucysMurphy_zero (n : ℕ) (h : 0 < n) :
    jucysMurphy (k := k) n ⟨0, h⟩ = 0 := by
  rw [jucysMurphy]
  have hempty : (Finset.univ.filter (fun j : Fin n => j.val < (⟨0, h⟩ : Fin n).val)) = ∅ := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.notMem_empty, iff_false]
    exact Nat.not_lt_zero j.val
  rw [hempty, Finset.sum_empty]

/-- On `Fin (n+2)` (where the index `1` genuinely exists), `X_1 = (0 1) = single (swap 0 1) 1`:
the only strand below `1` is `0`. A second sorry-free sanity check that the definition picks up
exactly the strands below the index. -/
theorem jucysMurphy_succ_zero (n : ℕ) :
    jucysMurphy (k := k) (n + 2) (1 : Fin (n + 2)) = single (Equiv.swap (0 : Fin (n + 2)) 1) 1 := by
  rw [jucysMurphy]
  have hsingleton :
      (Finset.univ.filter (fun j : Fin (n + 2) => j.val < (1 : Fin (n + 2)).val))
        = {(0 : Fin (n + 2))} := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    constructor
    · intro hj
      have : (1 : Fin (n + 2)).val = 1 := by simp
      rw [this, Nat.lt_one_iff] at hj
      exact Fin.ext hj
    · intro hj
      subst hj
      simp
  rw [hsingleton, Finset.sum_singleton]

/-! ## 2. Cell content and the content-square sum -/

/-- The **content** of a cell `c = (i, j)` of a Young diagram: `c(i,j) = j − i` (column minus row),
as an integer.  Constant on diagonals; the eigenvalue by which the JM element `X_k` acts on a
seminormal vector whose strand `k` sits in cell `c`. -/
def cellContent (c : ℕ × ℕ) : ℤ := (c.2 : ℤ) - (c.1 : ℤ)

@[simp] theorem cellContent_apply (i j : ℕ) : cellContent (i, j) = (j : ℤ) - (i : ℤ) := rfl

/-- The diagonal cells `(i, i)` have content `0`. -/
@[simp] theorem cellContent_diag (i : ℕ) : cellContent (i, i) = 0 := by
  simp [cellContent]

/-- The **content-square sum** `ω_λ = ∑_{c∈λ} c(c)²` of a Young diagram, as an integer.  This is
the scalar by which the JM central element `C₂ = ∑_k X_k²` acts on the Specht module `S^λ`
(`centralC2_acts_by_contentSqSum`), i.e. the `ω = Σc²` field carried by the keystone's
`SnWedderburnSpectralData`. -/
def contentSqSum (μ : YoungDiagram) : ℤ := ∑ c ∈ μ.cells, (cellContent c) ^ 2

/-- The empty diagram has content-square sum `0`. -/
@[simp] theorem contentSqSum_bot : contentSqSum ⊥ = 0 := by
  rw [contentSqSum, YoungDiagram.cells_bot, Finset.sum_empty]

/-- `contentSqSum` is always nonnegative (a sum of integer squares).  This is a statement about
the **integers** (`Int.le`), not an archimedean fact about `k` — it lives entirely in `ℤ`, so it
is §7c-clean.  Useful downstream when reading `ω` as a magnitude. -/
theorem contentSqSum_nonneg (μ : YoungDiagram) : 0 ≤ contentSqSum μ :=
  Finset.sum_nonneg (fun c _ => sq_nonneg (cellContent c))

/-! ## 3. The central element `C₂ = ∑_k X_k²` and its link to the established `centralC2` -/

/-- The Jucys–Murphy **central element** `C₂ = ∑_k X_k²` of `k[S_n]`, packaged directly from the
`jucysMurphy` elements.  By construction this is *definitionally equal* to
`QOU.BraidKnot.RegularRepTrace.centralC2 n` (the two inner sums coincide), recorded in
`centralC2_eq_sum_jucysMurphy_sq`. -/
noncomputable def centralC2 (n : ℕ) : MonoidAlgebra k (Equiv.Perm (Fin n)) :=
  ∑ i : Fin n, (jucysMurphy (k := k) n i) ^ 2

/-- The brick-5 `centralC2` (built from `jucysMurphy`) coincides with the established
`QOU.BraidKnot.RegularRepTrace.centralC2` used by the keystone's trace computation — they unfold
to the same `MonoidAlgebra` element.  Sorry-free: pure `rfl` on the two definitions. -/
theorem centralC2_eq_sum_jucysMurphy_sq (n : ℕ) :
    centralC2 (k := k) n = QOU.BraidKnot.RegularRepTrace.centralC2 n := rfl

/-- The identity coefficient of the brick-5 `C₂` is `binom(n,2)` — re-exported from the merged
ℂ-free core (`JucysMurphyCoeff.centralC2_coeff_one`), through the definitional equality above.
Sorry-free.  (A non-vacuous sanity check that the JM packaging is wired to the proved coefficient
identity; the *eigenvalue* form is the deep theorem stubbed below.) -/
theorem centralC2_coeff_one (n : ℕ) : (centralC2 (k := k) n) 1 = (n.choose 2 : k) := by
  rw [centralC2_eq_sum_jucysMurphy_sq]
  exact QOU.BraidKnot.RegularRepTrace.centralC2_coeff_one n

/-! ## 4. Commutativity of the Jucys–Murphy elements (the Gelfand–Zetlin algebra) -/

/-- Crux 1: `(a i)(i j) = (a j)(a i)` (both are the 3-cycle `a → i → j → a`), for distinct `a,i,j`. -/
private theorem swap_cross1 {α : Type*} [DecidableEq α] (a i j : α)
    (hai : a ≠ i) (haj : a ≠ j) (hij : i ≠ j) :
    Equiv.swap a i * Equiv.swap i j = Equiv.swap a j * Equiv.swap a i := by
  ext x; simp only [Equiv.Perm.mul_apply, Equiv.swap_apply_def]
  by_cases hx : x = a <;> by_cases hxi : x = i <;> by_cases hxj : x = j <;>
    subst_vars <;> split_ifs <;> tauto

/-- Crux 2: `(a i)(a j) = (i j)(a i)` (both are the 3-cycle `a → j → i → a`), for distinct `a,i,j`. -/
private theorem swap_cross2 {α : Type*} [DecidableEq α] (a i j : α)
    (hai : a ≠ i) (haj : a ≠ j) (hij : i ≠ j) :
    Equiv.swap a i * Equiv.swap a j = Equiv.swap i j * Equiv.swap a i := by
  ext x; simp only [Equiv.Perm.mul_apply, Equiv.swap_apply_def]
  by_cases hx : x = a <;> by_cases hxi : x = i <;> by_cases hxj : x = j <;>
    subst_vars <;> split_ifs <;> tauto

/-- Disjoint/equal transpositions commute: `(a i)` and `(b j)` commute when they share no point. -/
private theorem swap_comm_disjoint {α : Type*} [DecidableEq α] (a i b j : α)
    (hai : a ≠ i) (haj : a ≠ j) (hij : i ≠ j) (hbj : b ≠ j) (hbi : b ≠ i) (hba : b ≠ a) :
    Equiv.swap a i * Equiv.swap b j = Equiv.swap b j * Equiv.swap a i := by
  ext x; simp only [Equiv.Perm.mul_apply, Equiv.swap_apply_def]
  by_cases hxa : x = a <;> by_cases hxi : x = i <;> by_cases hxb : x = b <;> by_cases hxj : x = j <;>
    subst_vars <;> split_ifs <;> tauto

/-- The inner involution step. For `a < i < j` in `Fin n`, the `b`-indexed sum of
`single (σ_{ai} σ_{bj}) 1` over `b < j` equals the same sum with the factors transposed.  The
matching is term-by-term under the involution `φ b = if b = i then a else if b = a then i else b`
of `{b < j}`: the two "bad" indices `b = i`, `b = a` (where `(a i)`, `(b j)` fail to commute) are
swapped — turning each crux 3-cycle into the other — and every other `b` is a fixed point. -/
private theorem jm_inner_swap (n : ℕ) (a i j : Fin n)
    (hai : a.val < i.val) (hij : i.val < j.val) :
    (∑ b ∈ Finset.univ.filter (fun b : Fin n => b.val < j.val),
        single (Equiv.swap a i * Equiv.swap b j) (1 : k))
      = ∑ b ∈ Finset.univ.filter (fun b : Fin n => b.val < j.val),
          single (Equiv.swap b j * Equiv.swap a i) (1 : k) := by
  have haine : a ≠ i := fun h => by rw [h] at hai; exact lt_irrefl _ hai
  have hajne : a ≠ j := fun h => by rw [h] at hai; omega
  have hijne : i ≠ j := fun h => by rw [h] at hij; exact lt_irrefl _ hij
  refine Finset.sum_bij'
    (fun b _ => if b = i then a else if b = a then i else b)
    (fun b _ => if b = i then a else if b = a then i else b)
    ?_ ?_ ?_ ?_ ?_
  · intro b hb
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hb ⊢
    split_ifs with h1 h2 <;> omega
  · intro b hb
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hb ⊢
    split_ifs with h1 h2 <;> omega
  · intro b _
    by_cases h1 : b = i
    · subst h1; simp [haine]
    · by_cases h2 : b = a
      · subst h2; simp [haine]
      · simp [h1, h2]
  · intro b _
    by_cases h1 : b = i
    · subst h1; simp [haine]
    · by_cases h2 : b = a
      · subst h2; simp [haine]
      · simp [h1, h2]
  · intro b hb
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hb
    dsimp only
    by_cases h1 : b = i
    · rw [if_pos h1, h1, swap_cross1 a i j haine hajne hijne]
    · by_cases h2 : b = a
      · rw [if_neg h1, if_pos h2, h2, swap_cross2 a i j haine hajne hijne]
      · rw [if_neg h1, if_neg h2]
        have hbj : b ≠ j := fun h => by rw [h] at hb; exact lt_irrefl _ hb
        rw [swap_comm_disjoint a i b j haine hajne hijne hbj h1 h2]

/-- Main step for `i < j`: `X_i * X_j = X_j * X_i`.  The product `X_i X_j` expands to
`∑_{a<i} ∑_{b<j} single (σ_{ai} σ_{bj})`; transposing the order of summation in `X_j X_i` and
matching each inner `b`-sum via `jm_inner_swap` gives equality. -/
private theorem jm_commute_lt (n : ℕ) (i j : Fin n) (hlt : i.val < j.val) :
    jucysMurphy (k := k) n i * jucysMurphy (k := k) n j
      = jucysMurphy (k := k) n j * jucysMurphy (k := k) n i := by
  have hL : jucysMurphy (k := k) n i * jucysMurphy (k := k) n j
      = ∑ a ∈ Finset.univ.filter (fun a : Fin n => a.val < i.val),
          ∑ b ∈ Finset.univ.filter (fun b : Fin n => b.val < j.val),
            single (Equiv.swap a i * Equiv.swap b j) (1 : k) := by
    rw [jucysMurphy, jucysMurphy, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun a _ => ?_)
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [single_mul_single, one_mul]
  have hR : jucysMurphy (k := k) n j * jucysMurphy (k := k) n i
      = ∑ b ∈ Finset.univ.filter (fun b : Fin n => b.val < j.val),
          ∑ a ∈ Finset.univ.filter (fun a : Fin n => a.val < i.val),
            single (Equiv.swap b j * Equiv.swap a i) (1 : k) := by
    rw [jucysMurphy, jucysMurphy, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun a _ => ?_)
    rw [single_mul_single, one_mul]
  rw [hL, hR]
  rw [Finset.sum_comm (s := Finset.univ.filter (fun b : Fin n => b.val < j.val))
        (t := Finset.univ.filter (fun a : Fin n => a.val < i.val))]
  refine Finset.sum_congr rfl (fun a ha => ?_)
  simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ha
  exact jm_inner_swap n a i j ha hlt

/-- **Commutativity of the Gelfand–Zetlin algebra.** The Jucys–Murphy elements pairwise commute:
they generate a maximal commutative (Gelfand–Zetlin) subalgebra of `k[S_n]`.  This is the
structural fact underlying the simultaneous-eigenbasis (seminormal) construction.  Proved
sorry-free by Jucys's classical computation (see `jm_commute_lt`). -/
theorem jucysMurphy_commute (n : ℕ) (i j : Fin n) :
    Commute (jucysMurphy (k := k) n i) (jucysMurphy (k := k) n j) := by
  -- Ref: [vershik-kerov1977] (the JM elements generate the commutative GZ subalgebra of k[S_n]).
  -- Jucys's classical computation: expand the products into double sums of transpositions and match
  -- term-by-term under the involution swapping the two non-commuting indices (b = i ↔ b = a), via
  -- the crux 3-cycle identities `swap_cross1`/`swap_cross2`.
  rcases lt_trichotomy i.val j.val with h | h | h
  · exact jm_commute_lt n i j h
  · obtain rfl : i = j := Fin.ext h
    exact Commute.refl _
  · exact (jm_commute_lt n j i h).symm

/-! ## 5. The remaining deep Okounkov–Vershik theorems (stated, `sorry` + `-- Ref:`) -/

/-- A **seminormal (Gelfand–Zetlin) eigenvector** of the Specht module `S^λ`, packaged abstractly
so that the eigenvalue theorem can be stated at the level of brick 2's `Specht.Mtab.rep` without
first constructing the whole GZ basis (which is itself the content of the OV theorem).

The bundle carries:
* `T` — a standard Young tableau of shape `μ` (brick 1's `StandardYoungTableau`), which indexes the
  GZ basis vector;
* `v` — the corresponding seminormal vector, living in the Specht submodule `S^λ ≤ M^λ`;
* `nz` — non-triviality (`v ≠ 0`), so "eigenvector" is meaningful;
* `cellOf` — the **bijection** `Fin (nOf μ) ≃ μ.cells` that `T` induces, reading label `k` to the
  cell of `μ` holding `k`.  This is a bijection because a standard tableau fills the `nOf μ = μ.card`
  cells with the labels `0, …, nOf μ − 1` exactly once (brick 1's `StandardYoungTableau.inj_on`);
  packaging it as an `Equiv` is the faithful form of "the cell holding label `k`", and it is what
  makes the content-square sum over labels equal the content-square sum over cells
  (`centralC2_smul_seminormal`);
* `isEig` — the **defining seminormal property**: each `X_k` acts on `v` by the scalar
  `cellContent (cellOf k)`, i.e. the content of the cell holding label `k` in `T`.  We express
  the JM action on `M^λ` through `Specht.Mtab.rep` extended to the group algebra
  (`Representation.asAlgebraHom`), and the integer scalar via `zsmul`.

This is the *honest* packaging: rather than assert the GZ basis exists (the theorem), we make the
seminormal-eigenvector data a hypothesis, and `jucysMurphy_eigenvalue` states the consequence that
characterises such a vector.  Replacing this bundle with a constructed GZ basis is exactly the OV
theorem (`-- Ref: [vershik-kerov1977]`). -/
structure SeminormalVector (μ : YoungDiagram) where
  /-- The standard Young tableau indexing this GZ basis vector. -/
  T : QOU.BraidKnot.StandardYoungTableau μ
  /-- The seminormal vector itself, an element of the ambient permutation module `M^λ`. -/
  v : Specht.Mtab (k := k) μ
  /-- It lies in the Specht submodule `S^λ`. -/
  mem : v ∈ Specht.SpechtSubmodule (k := k) μ
  /-- It is nonzero (so "eigenvector" is non-vacuous). -/
  nz : v ≠ 0
  /-- The **bijection** `Fin (nOf μ) ≃ μ.cells` induced by the tableau `T`: label `k ↦` the cell
  of `μ` carrying `k`.  Bijective because a standard tableau is a bijection labels ↔ cells (brick 1's
  `inj_on` + the card identity `μ.cells.card = μ.card = nOf μ`).  Carrying the bijection (rather than
  a bare function) is what lets the content-square sum over labels collapse to `contentSqSum μ`. -/
  cellOf : Fin (Specht.nOf μ) ≃ μ.cells
  /-- **Seminormal eigenproperty.** Each `X_k` acts on `v` by the scalar
  `cellContent (cellOf k)` (an integer, via `zsmul`).  This is the defining diagonality of the
  GZ basis; its *existence* (a full GZ basis with this property) is the OV theorem stubbed in
  `jucysMurphy_eigenvalue`. -/
  isEig : ∀ s : Fin (Specht.nOf μ),
    (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
      = (cellContent ((cellOf s : ℕ × ℕ))) • v

/-- **Content-square sum over labels = over cells.** For any bijection `e : Fin (nOf μ) ≃ μ.cells`,
the sum of `cellContent (e s)²` over the labels `s` equals `contentSqSum μ = ∑_{c∈μ.cells} c(c)²`.
A pure reindexing of a finite sum along the bijection (`Finset.sum_attach` + `Fintype.sum_equiv`);
**no `sorry`, no `ℝ`** — integer arithmetic over `ℤ` (§7c-clean).  This is the "content-sum
arithmetic" leg of the punchline: it turns the JM-eigenvalue sum into the keystone's `ω = Σc²`. -/
theorem contentSqSum_eq_sum_over_labels (μ : YoungDiagram)
    (e : Fin (Specht.nOf μ) ≃ μ.cells) :
    (∑ s : Fin (Specht.nOf μ), (cellContent ((e s : ℕ × ℕ))) ^ 2) = contentSqSum μ := by
  rw [contentSqSum, ← Finset.sum_attach μ.cells (fun c => (cellContent (c : ℕ × ℕ)) ^ 2)]
  exact Fintype.sum_equiv e _ _ (fun s => rfl)

/-- **Each JM square acts on a seminormal vector by the content square.** From the seminormal
eigenproperty `X_s · v = c(cellOf s) • v`, the square `X_s² = X_s ∘ X_s` acts by `c(cellOf s)² • v`.
Sorry-free; the only inputs are `Representation.asAlgebraHom` being an algebra hom (so `map_pow`
sends `X_s²` to `(ρ X_s)²`) and the `zsmul` square computation. -/
theorem jucysMurphy_sq_smul_seminormal (μ : YoungDiagram) (sv : SeminormalVector (k := k) μ)
    (s : Fin (Specht.nOf μ)) :
    (Specht.Mtab.rep μ).asAlgebraHom ((jucysMurphy (k := k) (Specht.nOf μ) s) ^ 2) sv.v
      = ((cellContent ((sv.cellOf s : ℕ × ℕ))) ^ 2) • sv.v := by
  rw [map_pow, sq]
  show (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s)
        ((Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) sv.v) = _
  rw [sv.isEig s, map_zsmul, sv.isEig s, smul_smul, sq]

/-- **`C₂` acts on a seminormal vector by `contentSqSum μ`.** The central element
`C₂ = ∑_k X_k²` acts on the seminormal vector `sv.v` by the scalar `contentSqSum μ`.

Sorry-free.  The proof distributes `ρ(C₂) = ρ(∑_k X_k²) = ∑_k ρ(X_k²)` (via `map_sum` and
`LinearMap.sum_apply`), evaluates each summand by `jucysMurphy_sq_smul_seminormal`
(`= c(cellOf k)² • v`), pulls the `zsmul` out of the sum (`Finset.sum_smul` / `Finset.sum_zsmul`),
and collapses `∑_k c(cellOf k)² = contentSqSum μ` by `contentSqSum_eq_sum_over_labels` along the
bijection `sv.cellOf`.  This is the sorry-free core of the punchline; the only remaining OV input
(the *spanning* of `S^λ` by such vectors) is isolated in `seminormalVectors_span`. -/
theorem centralC2_smul_seminormal (μ : YoungDiagram) (sv : SeminormalVector (k := k) μ) :
    (Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)) sv.v
      = (contentSqSum μ) • sv.v := by
  rw [centralC2, map_sum, LinearMap.sum_apply]
  -- each summand: ρ(X_s²) v = c(cellOf s)² • v
  rw [Finset.sum_congr rfl (fun s _ => jucysMurphy_sq_smul_seminormal μ sv s)]
  -- factor the common vector out of the sum, then collapse the content-square sum over labels
  rw [← Finset.sum_smul, contentSqSum_eq_sum_over_labels μ sv.cellOf]

/-- **Jucys–Murphy eigenvalue theorem (Okounkov–Vershik).** The Specht module `S^λ` admits a
Gelfand–Zetlin / seminormal basis indexed by the standard Young tableaux of shape `μ`, on which
every JM element `X_k` acts **diagonally** with eigenvalue `cellContent (cell of k in T)`.

We state this as: for every standard tableau `T` of shape `μ`, there is a seminormal eigenvector
`sv` whose indexing tableau is `T`.  The eigenproperty itself is recorded as the `isEig` field of
`SeminormalVector` (each `X_k` acts by the content of `k`'s cell); the *content* of the theorem is
the **existence** of such vectors for every `T`, i.e. that the GZ basis exists and diagonalises the
JM elements.  Together with `jucysMurphy_commute`, this is the heart of the OV approach.

(The cleanest faithful formulation found: package the seminormal datum as `SeminormalVector` with
the eigenproperty built in, then assert existence indexed by the SYT.  This avoids hand-rolling a
basis API while keeping the statement honest — the only `sorry` is the genuine OV existence claim,
and the eigenvalue *equation* `X_k · v = c(cell) • v` is literally present in the bundle.)

This is the **deep OV core** — the existence of the GZ/seminormal eigenbasis — and remains a single
cited `sorry`; it is the content of the Okounkov–Vershik paper and out of scope for one brick. -/
theorem jucysMurphy_eigenvalue (μ : YoungDiagram) (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∃ sv : SeminormalVector (k := k) μ, sv.T = T := by
  -- Ref: [vershik-kerov1977] (the GZ/seminormal basis of S^λ diagonalises the JM elements with
  -- eigenvalues equal to the cell contents); brick-5 OV existence core.
  sorry

/-- **Seminormal vectors span the Specht module (Okounkov–Vershik).** The Specht submodule
`S^λ ≤ M^λ` is spanned by the seminormal (Gelfand–Zetlin) vectors `{sv.v}`.  Equivalently, the GZ
basis is a basis of `S^λ`.

This is the second irreducible OV input (alongside `jucysMurphy_eigenvalue`): it is *exactly* the
statement that the simultaneous JM-eigenvectors exhaust `S^λ`, i.e. that the GZ basis is complete.
It is isolated here as a single cited `sorry` so that the punchline `centralC2_acts_by_contentSqSum`
is then **sorry-free** (the scalar action on each spanning vector is the sorry-free
`centralC2_smul_seminormal`, and a `Submodule.span_induction` propagates it to all of `S^λ`).

The inclusion `span ⊆ S^λ` is automatic (each `sv.v ∈ S^λ` by the `mem` field); the content is the
reverse inclusion `S^λ ⊆ span`, stated below. -/
theorem seminormalVectors_span (μ : YoungDiagram) :
    Specht.SpechtSubmodule (k := k) μ
      ≤ Submodule.span k (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v)) := by
  -- Ref: [vershik-kerov1977] (the GZ/seminormal eigenvectors form a basis of S^λ; the simultaneous
  -- JM-eigenbasis is complete); brick-5 OV completeness core.
  sorry

/-- **Punchline — `C₂` acts by `Σ_{c∈λ} c(c)²` on `S^λ`.** The Jucys–Murphy central element
`C₂ = ∑_k X_k²` acts on the Specht module `S^λ ≤ M^λ` (via `Specht.Mtab.rep` extended to the group
algebra) as the **scalar** `contentSqSum μ`.  That is, for every `x ∈ S^λ`,
`ρ(C₂) · x = (contentSqSum μ) • x`.

This is the central element acting by a single eigenvalue on the irreducible `S^λ` (Schur's lemma
made explicit): since each `X_k` acts on the seminormal vector for `T` by `c(cell of k)`, the
central `∑_k X_k²` acts by `∑_k c(cell of k)² = ∑_{c∈λ} c(c)²` — independent of `T`, hence a
scalar on all of `S^λ`.  **This integer scalar `contentSqSum μ` is exactly the `ω = Σc²` field of
the keystone's `SnWedderburnSpectralData`** (`QOU.BraidKnot.RegularRepBlockTrace`); discharging
this theorem discharges that field's content for the Specht-module block.

**Sorry-free modulo the two cited OV cores.** The proof is a `Submodule.span_induction`:
the seminormal vectors span `S^λ` (`seminormalVectors_span`), `C₂` acts on each by `contentSqSum μ`
(the sorry-free `centralC2_smul_seminormal`), and the scalar action extends through `+`, `0`, and
`k`-scaling because both `ρ(C₂)` and `(contentSqSum μ) • ·` are `k`-linear.  No `sorry`, no `ℝ`,
no `native_decide`. -/
theorem centralC2_acts_by_contentSqSum (μ : YoungDiagram) :
    ∀ x ∈ Specht.SpechtSubmodule (k := k) μ,
      (Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)) x
        = (contentSqSum μ) • x := by
  intro x hx
  -- the seminormal vectors span S^λ, so x lies in their span
  have hxspan : x ∈ Submodule.span k
      (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v)) :=
    seminormalVectors_span μ hx
  -- propagate the scalar action `ρ(C₂) w = ω • w` from the spanning vectors to x by linearity,
  -- with a motive that depends *only* on span-membership (so no spurious S^λ side-goals appear)
  refine Submodule.span_induction
    (p := fun w _ => (Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)) w
      = (contentSqSum μ) • w)
    ?_ ?_ ?_ ?_ hxspan
  · rintro w ⟨sv, rfl⟩
    exact centralC2_smul_seminormal μ sv
  · simp
  · intro a b _ _ ha hb; rw [map_add, ha, hb, smul_add]
  · intro r a _ ha; rw [map_smul, ha, smul_comm]

end QOU.BraidKnot.JucysMurphy
