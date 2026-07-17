import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.RepresentationTheory.Basic
import Mathlib.Order.Interval.Finset.Fin
import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtStandardBasis
import QOU.BraidKnot.RegularRepTrace
import QOU.BraidKnot.SpechtFinrankWired
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Dimension.Free
import Mathlib.LinearAlgebra.LinearIndependent.Basic

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

## What is proved sorry-free beyond the definitional layer

* `jucysMurphy_commute` — the JM elements pairwise commute (the GZ algebra is commutative);
  Jucys's classical double-sum computation.
* `conj_jucysMurphy_self` / `conj_jucysMurphy_other` / `pair_shift_comm` (§4b) — the JM
  **conjugation recursion** `s·X_a·s = X_{a+1} − s` (adjacent swap `s`), fixing every other
  `X_m`; generic `[CommRing k]`.
* `end_conj_shift_eigenvector_pair` / `end_conj_fix_eigenvector` /
  `end_involution_eigenvector_ne` (§4c) — the classical **2×2 seminormal block**: on a joint
  eigenvector `v` of the recursion pair, `w = S v − (c_b − c_a)⁻¹ • v` is again a joint
  eigenvector with the swapped eigenvalues, nonzero when `(c_b − c_a)² ≠ 1`.
* `rep_polytabloid` / `rep_mem_spechtSubmodule` (§4d) — `σ · e_t = e_{σ·t}`; the Specht
  submodule is a **subrepresentation**.
* `seminormalVector_data_step` — the seminormal **induction step**: transport of the full
  seminormal eigenvector datum along any admissible adjacent swap (`AdjacentSwapStep`).
* `seminormalVector_data_exists` — the all-`T` eigenvector existence, **assembled sorry-free**
  from the two cited cores below by walking the swap chain from the base tableau.
* `jucysMurphy_eigenvalue`, `exists_indep_seminormal_family`, `seminormalVectors_span`,
  `centralC2_acts_by_contentSqSum` — the completeness chain and the `ω = Σc²` punchline,
  sorry-free modulo the cores below.

## What is stated with `sorry` + `-- Ref:` (the residual OV cores)

* `seminormalVector_base_exists` — existence of the seminormal eigenvector for **one**
  distinguished (base) tableau.  `-- Ref: [vershik-kerov1977]`.
* `syt_adjacentSwap_connected` — any two standard tableaux of a shape are connected by
  admissible adjacent swaps (pure combinatorics).  `-- Ref: [sagan2001]`.
* `syt_content_tuple_injective` — the content tuple determines the standard tableau (the GZ
  spectrum is simple; pure combinatorics).  `-- Ref: [vershik-kerov1977]`.

All three are strictly smaller than the previously carried all-`T` existence `sorry`; they are
honestly stubbed per AGENTS.md §1 (`theorem … := by sorry  -- Ref: …`), never `: True`, never
`native_decide`.

## Base ring (§7c)

The JM / content layer is **purely algebraic**: `variable {k : Type} [CommRing k]`.  No `ℝ`, no
`Real.*`, no ordering on `k`, no `linarith`/`positivity`/`norm_num`.  `cellContent`/`contentSqSum`
land in `ℤ` (integer arithmetic — algebraic, not archimedean-`ℝ`).  The finite filter `j.val < i.val`
is an order on the *index type* `Fin n`, not on the ring `k`, and is necessary (it is the very
"strands below `k`" defining `X_k`).  Most of the layer is stated over generic `[CommRing k]`.  The
**seminormal-form** results — `seminormalVector_data_exists`, `jucysMurphy_eigenvalue`, the
`seminormalVectors_span` completeness chain (`exists_indep_seminormal_family` + `seminormalSpan_le` +
`numSYT_le_finrank_seminormalSpan`), and the punchline `centralC2_acts_by_contentSqSum` — are stated
over `[Field k] [CharZero k]` instead.  This is a correctness restriction (not an archimedean `ℝ` leak —
char-0 field, no ordering, no `Real.*`): the seminormal/GZ eigenbasis is genuinely a char-0 fact, and
over a general commutative ring the relevant claims are *false* — completeness `S^λ ⊆ span` fails over
`ℤ` (denominators), and simultaneous-eigenvector existence fails over `ℤ/pℤ` (cell-contents collide
modulo `p`).  See those lemmas' docstrings.

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

/-! ## 4b. The Jucys–Murphy conjugation recursion (sorry-free, generic `CommRing`)

The engine of every inductive seminormal argument: conjugating by the adjacent
transposition `s = (a, a+1)` sends `X_a ↦ X_{a+1} − s` (`conj_jucysMurphy_self`)
and fixes every other `X_k` (`conj_jucysMurphy_other`).  Together with the pure
noncommutative-ring cancellation `pair_shift_comm`, these are the classical
Jucys relations.  All sorry-free, over the file-wide generic `[CommRing k]`. -/

/-- Conjugating one transposition by another: `(ab)·(ij)·(ab) = (σi, σj)` with `σ = (ab)`. -/
private theorem swap_conj_swap {n : ℕ} (a b i j : Fin n) :
    Equiv.swap a b * Equiv.swap i j * Equiv.swap a b
      = Equiv.swap (Equiv.swap a b i) (Equiv.swap a b j) := by
  have h := Equiv.swap_apply_apply (Equiv.swap a b) i j
  rw [Equiv.swap_inv] at h
  exact h.symm

private theorem conj_single_swap {n : ℕ} (a b i j : Fin n) :
    single (Equiv.swap a b) (1 : k) * single (Equiv.swap i j) 1 * single (Equiv.swap a b) 1
      = single (Equiv.swap (Equiv.swap a b i) (Equiv.swap a b j)) 1 := by
  rw [single_mul_single, single_mul_single, one_mul, one_mul, swap_conj_swap]

/-- **The Jucys–Murphy recursion (algebra form).** `s·X_a·s = X_b − s` for the adjacent swap
`s = (a b)`, `b = a + 1`: conjugation sends each `(j a)` (`j < a`) to `(j b)`, and
`X_b = ∑_{j<a} (j b) + (a b)`.  Sorry-free, generic `[CommRing k]`. -/
theorem conj_jucysMurphy_self {n : ℕ} (a b : Fin n) (hab : (a : ℕ) + 1 = (b : ℕ)) :
    single (Equiv.swap a b) (1 : k) * jucysMurphy (k := k) n a * single (Equiv.swap a b) 1
      = jucysMurphy (k := k) n b - single (Equiv.swap a b) 1 := by
  have hFb : Finset.univ.filter (fun j : Fin n => j.val < b.val)
      = insert a (Finset.univ.filter (fun j : Fin n => j.val < a.val)) := by
    ext j
    simp only [Finset.mem_insert, Finset.mem_filter, Finset.mem_univ, true_and,
      ← Fin.val_eq_val]
    omega
  have haF : a ∉ Finset.univ.filter (fun j : Fin n => j.val < a.val) := by simp
  simp only [jucysMurphy]
  rw [Finset.mul_sum, Finset.sum_mul, hFb, Finset.sum_insert haF, add_sub_cancel_left]
  refine Finset.sum_congr rfl (fun j hj => ?_)
  rw [Finset.mem_filter] at hj
  have hja : j ≠ a := Fin.ne_of_val_ne (by omega)
  have hjb : j ≠ b := Fin.ne_of_val_ne (by omega)
  rw [conj_single_swap, Equiv.swap_apply_of_ne_of_ne hja hjb, Equiv.swap_apply_left]

/-- **The other Jucys–Murphy elements are fixed** by conjugation with an adjacent swap:
`s·X_m·s = X_m` for `m ∉ {a, b}` — the swap permutes the index set `{j : j < m}`.
Sorry-free, generic `[CommRing k]`. -/
theorem conj_jucysMurphy_other {n : ℕ} (a b m : Fin n) (hab : (a : ℕ) + 1 = (b : ℕ))
    (hma : m ≠ a) (hmb : m ≠ b) :
    single (Equiv.swap a b) (1 : k) * jucysMurphy (k := k) n m * single (Equiv.swap a b) 1
      = jucysMurphy (k := k) n m := by
  have hma' : (m : ℕ) ≠ (a : ℕ) := fun h => hma (Fin.ext h)
  have hmb' : (m : ℕ) ≠ (b : ℕ) := fun h => hmb (Fin.ext h)
  have hmem : ∀ j : Fin n, (j : ℕ) < (m : ℕ) → ((Equiv.swap a b j : Fin n) : ℕ) < (m : ℕ) := by
    intro j hjm
    rcases eq_or_ne j a with rfl | hja
    · rw [Equiv.swap_apply_left]; omega
    · rcases eq_or_ne j b with rfl | hjb
      · rw [Equiv.swap_apply_right]; omega
      · rw [Equiv.swap_apply_of_ne_of_ne hja hjb]; exact hjm
  simp only [jucysMurphy]
  rw [Finset.mul_sum, Finset.sum_mul]
  have hstep : ∀ j ∈ Finset.univ.filter (fun j : Fin n => j.val < m.val),
      single (Equiv.swap a b) (1 : k) * single (Equiv.swap j m) 1 * single (Equiv.swap a b) 1
        = single (Equiv.swap (Equiv.swap a b j) m) 1 := by
    intro j _
    rw [conj_single_swap, Equiv.swap_apply_of_ne_of_ne hma hmb]
  rw [Finset.sum_congr rfl hstep]
  refine Finset.sum_nbij' (fun j => Equiv.swap a b j) (fun j => Equiv.swap a b j)
    ?_ ?_ ?_ ?_ ?_
  · intro x hx
    rw [Finset.mem_filter] at hx ⊢
    exact ⟨Finset.mem_univ _, hmem x hx.2⟩
  · intro x hx
    rw [Finset.mem_filter] at hx ⊢
    exact ⟨Finset.mem_univ _, hmem x hx.2⟩
  · intro x _; exact Equiv.swap_apply_self a b x
  · intro x _; exact Equiv.swap_apply_self a b x
  · intro x _; rfl

/-- Abstract ring fact: if `s² = 1` and `s·Y·s = Z − s`, then `s` commutes with `Y² + Z²`.
The pure noncommutative-ring core of the Jucys–Murphy centrality argument: from the
hypotheses, `s·Y = Z·s − 1` and `s·Z = Y·s + 1`, and the cross terms cancel. -/
theorem pair_shift_comm {A : Type*} [Ring A] (s Y Z : A) (hs : s * s = 1)
    (hA : s * Y * s = Z - s) :
    s * (Y ^ 2 + Z ^ 2) = (Y ^ 2 + Z ^ 2) * s := by
  have h1 : s * Y = Z * s - 1 := by
    calc s * Y = s * Y * (s * s) := by rw [hs, mul_one]
    _ = s * Y * s * s := by rw [← mul_assoc]
    _ = (Z - s) * s := by rw [hA]
    _ = Z * s - 1 := by rw [sub_mul, hs]
  have h2 : s * Z = Y * s + 1 := by
    have hZ : s * Y * s + s = Z := by rw [hA, sub_add_cancel]
    calc s * Z = s * (s * Y * s + s) := by rw [hZ]
    _ = s * s * Y * s + s * s := by noncomm_ring
    _ = Y * s + 1 := by rw [hs, one_mul]
  calc s * (Y ^ 2 + Z ^ 2)
      = s * Y * Y + s * Z * Z := by noncomm_ring
    _ = (Z * s - 1) * Y + (Y * s + 1) * Z := by rw [h1, h2]
    _ = Z * (s * Y) + Y * (s * Z) - Y + Z := by noncomm_ring
    _ = Z * (Z * s - 1) + Y * (Y * s + 1) - Y + Z := by rw [h1, h2]
    _ = (Y ^ 2 + Z ^ 2) * s := by noncomm_ring

/-! ## 4c. The classical 2×2 seminormal block (sorry-free linear algebra)

The module-level engine of Young's seminormal form: on a simultaneous eigenvector
`v` of two operators `A, B` intertwined by an involution `S` via the JM recursion
`S·A·S = B − S`, the vector `w = S v − (c_B − c_A)⁻¹ • v` is again a simultaneous
eigenvector — with the **swapped** eigenvalues (`end_conj_shift_eigenvector_pair`);
operators fixed by the conjugation keep their eigenvalue (`end_conj_fix_eigenvector`);
and `w ≠ 0` whenever `(c_B − c_A)² ≠ 1` (`end_involution_eigenvector_ne`).  No Specht
content — pure `Module.End` algebra. -/

/-- **The 2×2 seminormal block, eigenvalue-swap half.** If `S² = 1`, `S·A·S = B − S`
(the Jucys–Murphy recursion, abstractly), and `v` is an `A`-eigenvector with value `ca`
and a `B`-eigenvector with value `cb ≠ ca`, then `w = S v − (cb − ca)⁻¹ • v` is an
`A`-eigenvector with value `cb` and a `B`-eigenvector with value `ca` (the swapped pair).
Sorry-free. -/
theorem end_conj_shift_eigenvector_pair {k : Type} [Field k] {V : Type*}
    [AddCommGroup V] [Module k V]
    (S A B : Module.End k V) (hS2 : S * S = 1) (hconj : S * A * S = B - S)
    {v : V} {ca cb : k} (hA : A v = ca • v) (hB : B v = cb • v) (hne : cb - ca ≠ 0) :
    A (S v - (cb - ca)⁻¹ • v) = cb • (S v - (cb - ca)⁻¹ • v)
      ∧ B (S v - (cb - ca)⁻¹ • v) = ca • (S v - (cb - ca)⁻¹ • v) := by
  have hAS : A * S = S * B - 1 := by
    calc A * S = (S * S) * (A * S) := by rw [hS2, one_mul]
      _ = S * (S * A * S) := by noncomm_ring
      _ = S * (B - S) := by rw [hconj]
      _ = S * B - 1 := by rw [mul_sub, hS2]
  have hBS : B * S = S * A + 1 := by
    have hB' : B = S * A * S + S := by rw [hconj, sub_add_cancel]
    calc B * S = (S * A * S + S) * S := by rw [← hB']
      _ = (S * A) * (S * S) + S * S := by noncomm_ring
      _ = S * A + 1 := by rw [hS2, mul_one]
  have hASv : A (S v) = cb • S v - v := by
    have h := congrArg (fun f : Module.End k V => f v) hAS
    simp only [Module.End.mul_apply, LinearMap.sub_apply, Module.End.one_apply] at h
    rw [h, hB, map_smul]
  have hBSv : B (S v) = ca • S v + v := by
    have h := congrArg (fun f : Module.End k V => f v) hBS
    simp only [Module.End.mul_apply, LinearMap.add_apply, Module.End.one_apply] at h
    rw [h, hA, map_smul]
  constructor
  · have hsc : cb * (cb - ca)⁻¹ = (cb - ca)⁻¹ * ca + 1 := by
      field_simp
      ring
    rw [map_sub, map_smul, hA, hASv, smul_sub, smul_smul, smul_smul, hsc, add_smul, one_smul]
    abel
  · have hsc : ca * (cb - ca)⁻¹ = (cb - ca)⁻¹ * cb - 1 := by
      field_simp
      ring
    rw [map_sub, map_smul, hB, hBSv, smul_sub, smul_smul, smul_smul, hsc, sub_smul, one_smul]
    abel

/-- **The 2×2 seminormal block, fixed-operator half.** An operator `C` fixed by the
conjugation (`S·C·S = C`, `S² = 1`) commutes with `S`, so it keeps its eigenvalue on
`w = S v − r • v` for any shift `r`.  Sorry-free, generic `[CommRing k]`. -/
theorem end_conj_fix_eigenvector {k : Type} [CommRing k] {V : Type*}
    [AddCommGroup V] [Module k V]
    (S C : Module.End k V) (hS2 : S * S = 1) (hfix : S * C * S = C)
    {v : V} {c : k} (hC : C v = c • v) (r : k) :
    C (S v - r • v) = c • (S v - r • v) := by
  have hCS : C * S = S * C := by
    calc C * S = (S * S) * (C * S) := by rw [hS2, one_mul]
      _ = S * (S * C * S) := by noncomm_ring
      _ = S * C := by rw [hfix]
  have hCSv : C (S v) = c • S v := by
    have h := congrArg (fun f : Module.End k V => f v) hCS
    simp only [Module.End.mul_apply] at h
    rw [h, hC, map_smul]
  rw [map_sub, map_smul, hC, hCSv, smul_sub, smul_smul, smul_smul, mul_comm r c]

/-- **The 2×2 seminormal block, non-vanishing half.** If `S² = 1`, `v ≠ 0`, and
`(cb − ca)² ≠ 1`, then `w = S v − (cb − ca)⁻¹ • v ≠ 0`: from `w = 0` the vector `v`
would be an `S`-eigenvector with eigenvalue `r = (cb − ca)⁻¹`, forcing `r² = 1` by the
involution — i.e. `(cb − ca)² = 1` (with the degenerate `cb = ca` giving `r = 0`,
`r² = 0 ≠ 1`, also excluded).  Sorry-free. -/
theorem end_involution_eigenvector_ne {k : Type} [Field k] {V : Type*}
    [AddCommGroup V] [Module k V]
    (S : Module.End k V) (hS2 : S * S = 1) {v : V} (hv : v ≠ 0)
    {ca cb : k} (hsq : (cb - ca) ^ 2 ≠ 1) :
    S v - (cb - ca)⁻¹ • v ≠ 0 := by
  intro hw
  have hSv : S v = (cb - ca)⁻¹ • v := by rwa [sub_eq_zero] at hw
  have hSS : S (S v) = v := by
    have h := congrArg (fun f : Module.End k V => f v) hS2
    simpa only [Module.End.mul_apply, Module.End.one_apply] using h
  have hv2 : ((cb - ca)⁻¹ * (cb - ca)⁻¹) • v = v := by
    calc ((cb - ca)⁻¹ * (cb - ca)⁻¹) • v = (cb - ca)⁻¹ • (cb - ca)⁻¹ • v := by rw [mul_smul]
      _ = (cb - ca)⁻¹ • S v := by rw [← hSv]
      _ = S ((cb - ca)⁻¹ • v) := (map_smul S _ v).symm
      _ = S (S v) := by rw [← hSv]
      _ = v := hSS
  have hz : ((cb - ca)⁻¹ * (cb - ca)⁻¹ - 1) • v = 0 := by
    rw [sub_smul, one_smul, hv2, sub_self]
  have hrr : (cb - ca)⁻¹ * (cb - ca)⁻¹ = 1 := by
    rcases smul_eq_zero.mp hz with h | h
    · exact sub_eq_zero.mp h
    · exact absurd h hv
  apply hsq
  have hinv : ((cb - ca) * (cb - ca))⁻¹ = 1 := by
    rw [mul_inv]
    exact hrr
  rw [sq]
  exact inv_eq_one.mp hinv

/-! ## 4d. The Specht submodule is a subrepresentation (sorry-free)

`σ · e_t = e_{σ·t}`: the group action permutes the polytabloids, so the span `S^λ`
is invariant under every `rep μ σ`.  This is the membership leg of the seminormal
transport (the swapped vector `S v − r • v` stays inside `S^λ`). -/

/-- The conjugation equivalence `C_t ≃ C_{σ·t}` between column stabilizers,
`π ↦ σ π σ⁻¹`.  Membership transports along `colPattern (σ • t) = σ • colPattern t`. -/
private def colStabConj {μ : YoungDiagram} (σ : Equiv.Perm (Fin (Specht.nOf μ)))
    (t : Specht.Tableau μ) : ↥(Specht.colStab t) ≃ ↥(Specht.colStab (σ • t)) where
  toFun π := ⟨σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹, by
    have hπ := Specht.mem_colStab.mp π.2
    rw [Specht.mem_colStab, Specht.colPattern_smul]
    simp [mul_smul, hπ]⟩
  invFun π := ⟨σ⁻¹ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ, by
    have hπ := Specht.mem_colStab.mp π.2
    rw [Specht.colPattern_smul] at hπ
    rw [Specht.mem_colStab]
    simp only [mul_smul]
    rw [hπ]
    simp⟩
  left_inv π := by
    ext
    simp [mul_assoc]
  right_inv π := by
    ext
    simp [mul_assoc]

/-- **The group action permutes polytabloids**: `rep σ (e_t) = e_{σ·t}`.  Reindex the
column-stabilizer sum along the conjugation `π ↦ σπσ⁻¹` (`colStabConj`); signs are
conjugation-invariant and `(σπσ⁻¹)·(σ·t) = σ·(π·t)`.  Sorry-free. -/
theorem rep_polytabloid {μ : YoungDiagram} (σ : Equiv.Perm (Fin (Specht.nOf μ)))
    (t : Specht.Tableau μ) :
    Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) t)
      = Specht.polytabloid (k := k) (σ • t) := by
  classical
  rw [Specht.polytabloid, Specht.polytabloid, map_sum]
  refine Fintype.sum_equiv (colStabConj σ t) _ _ (fun π => ?_)
  rw [map_zsmul, Specht.Mtab.rep_of]
  have hsg : Equiv.Perm.sign (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹)
      = Equiv.Perm.sign (π : Equiv.Perm (Fin (Specht.nOf μ))) := by
    rw [map_mul, map_mul, map_inv, mul_comm (Equiv.Perm.sign σ), mul_assoc,
      mul_inv_cancel, mul_one]
  have harg : (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹) • (σ • t)
      = σ • (π : Equiv.Perm (Fin (Specht.nOf μ))) • t := by
    simp [mul_smul]
  show (Equiv.Perm.sign (π : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ)
        • Specht.Mtab.of (k := k) (σ • (π : Equiv.Perm (Fin (Specht.nOf μ))) • t)
      = (Equiv.Perm.sign ((colStabConj σ t π : Equiv.Perm (Fin (Specht.nOf μ)))) : ℤ)
        • Specht.Mtab.of (k := k)
            ((colStabConj σ t π : Equiv.Perm (Fin (Specht.nOf μ))) • σ • t)
  rw [show ((colStabConj σ t π : Equiv.Perm (Fin (Specht.nOf μ))))
        = σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹ from rfl, hsg, harg]

/-- **`S^λ` is invariant under the `S_n`-action** (a subrepresentation): `rep μ σ`
maps the Specht submodule into itself.  Span induction over the polytabloid
generators via `rep_polytabloid`.  Sorry-free, generic `[CommRing k]`. -/
theorem rep_mem_spechtSubmodule {μ : YoungDiagram} (σ : Equiv.Perm (Fin (Specht.nOf μ)))
    {v : Specht.Mtab (k := k) μ} (hv : v ∈ Specht.SpechtSubmodule (k := k) μ) :
    Specht.Mtab.rep (k := k) μ σ v ∈ Specht.SpechtSubmodule (k := k) μ := by
  have hv' : v ∈ Submodule.span k (Set.range (Specht.polytabloid (k := k) (μ := μ))) := hv
  refine Submodule.span_induction
    (p := fun w _ => Specht.Mtab.rep (k := k) μ σ w ∈ Specht.SpechtSubmodule (k := k) μ)
    ?_ ?_ ?_ ?_ hv'
  · rintro w ⟨t, rfl⟩
    rw [rep_polytabloid]
    exact Specht.polytabloid_mem_specht _
  · simp only [map_zero]
    exact zero_mem _
  · intro x y _ _ hx hy
    rw [map_add]
    exact add_mem hx hy
  · intro c x _ hx
    rw [map_smul]
    exact Submodule.smul_mem _ _ hx

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

/-- **The cell-bijection of a standard tableau (constructed sorry-free).** For a standard Young
tableau `T` of shape `μ`, the bijection `Fin (nOf μ) ≃ μ.cells` reading label `k` to the unique
cell of `μ` holding `k`.  This is **brick 4's** `SpechtStandardBasis.sytToTableau`: the inverse of
the cell→label map `cellLabel T` (an injection between two finite types of equal cardinality
`μ.cells.card = μ.card = nOf μ`, hence a bijection — `cellLabel_bijective`).  Carrying it here lets
us *construct* the `cellOf` field of a `SeminormalVector` explicitly, so the only OV input that
remains in `jucysMurphy_eigenvalue` is the seminormal eigenvector itself (not its indexing
bijection).  No `sorry`, no `ℝ`, no `k`-dependence (it is tableau data only). -/
noncomputable def tableauCellEquiv (μ : YoungDiagram) (T : QOU.BraidKnot.StandardYoungTableau μ) :
    Fin (Specht.nOf μ) ≃ μ.cells :=
  QOU.BraidKnot.SpechtStandardBasis.sytToTableau T

/-- **An admissible adjacent-swap step between standard tableaux**, recorded at the level of
their content vectors (all the seminormal transport needs).  `T'` is obtained from `T` by an
adjacent swap `(a, b)` (`b = a + 1`) when: the content vectors of `T'` and `T` agree away from
`{a, b}` and are swapped at `{a, b}`; and the content gap `d = c_T(b) − c_T(a)` satisfies
`d ≠ 0` and `d² ≠ 1`.  The two gap conditions are the classical admissibility: for a standard
tableau, consecutive labels never sit on the same diagonal (`d ≠ 0`), and `|d| = 1` exactly when
they are row- or column-adjacent — the case in which the swapped filling is *not* standard.  So
an `AdjacentSwapStep` is precisely "swap `a, a+1` in `T`, landing on another standard tableau". -/
def AdjacentSwapStep (μ : YoungDiagram)
    (T T' : QOU.BraidKnot.StandardYoungTableau μ) : Prop :=
  ∃ a b : Fin (Specht.nOf μ), (a : ℕ) + 1 = (b : ℕ) ∧
    cellContent ((tableauCellEquiv μ T' a : ℕ × ℕ))
      = cellContent ((tableauCellEquiv μ T b : ℕ × ℕ)) ∧
    cellContent ((tableauCellEquiv μ T' b : ℕ × ℕ))
      = cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) ∧
    (∀ s : Fin (Specht.nOf μ), s ≠ a → s ≠ b →
      cellContent ((tableauCellEquiv μ T' s : ℕ × ℕ))
        = cellContent ((tableauCellEquiv μ T s : ℕ × ℕ))) ∧
    cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))
      - cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) ≠ 0 ∧
    (cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))
      - cellContent ((tableauCellEquiv μ T a : ℕ × ℕ))) ^ 2 ≠ 1

/-- **Seminormal transport along an admissible adjacent swap (sorry-free).** If a nonzero
`v ∈ S^λ` is a simultaneous JM eigenvector with the content tuple of `T`, and
`AdjacentSwapStep μ T T'`, then `w = ρ(s)·v − (c_b − c_a)⁻¹ • v` (with `s = (a, a+1)` and
`c_a, c_b` the contents of `a, a+1` in `T`) is a nonzero simultaneous JM eigenvector in `S^λ`
with the content tuple of `T'`.

This is the classical induction step of Young's seminormal form, machine-checked end-to-end:
* the JM recursion `s·X_a·s = X_b − s` / `s·X_m·s = X_m` (`conj_jucysMurphy_self` /
  `conj_jucysMurphy_other`) is pushed through `asAlgebraHom` to `Module.End`;
* the eigenvalue swap is `end_conj_shift_eigenvector_pair`, the fixed operators are
  `end_conj_fix_eigenvector`, non-vanishing is `end_involution_eigenvector_ne`
  (using `d ≠ 0`, `d² ≠ 1` cast into `k` by `CharZero`);
* membership is the subrepresentation property `rep_mem_spechtSubmodule`. -/
theorem seminormalVector_data_step {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    {T T' : QOU.BraidKnot.StandardYoungTableau μ}
    (hstep : AdjacentSwapStep μ T T')
    (h : ∃ v : Specht.Mtab (k := k) μ,
        v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
          ∀ s : Fin (Specht.nOf μ),
            (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
              = (cellContent ((tableauCellEquiv μ T s : ℕ × ℕ))) • v) :
    ∃ v : Specht.Mtab (k := k) μ,
      v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
        ∀ s : Fin (Specht.nOf μ),
          (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
            = (cellContent ((tableauCellEquiv μ T' s : ℕ × ℕ))) • v := by
  classical
  obtain ⟨a, b, hab, hca', hcb', hother, hne, hsq⟩ := hstep
  obtain ⟨v, hmem, hnz, heig⟩ := h
  -- the k-cast eigen equations
  have heigk : ∀ s : Fin (Specht.nOf μ),
      (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
        = ((cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) : ℤ) : k) • v := by
    intro s
    rw [heig s]
    exact (Int.cast_smul_eq_zsmul k _ _).symm
  -- the representation of the adjacent swap, as an endomorphism
  have hS2 : ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k)))
      * ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k))) = 1 := by
    rw [← map_mul, single_mul_single, one_mul, Equiv.swap_mul_self, ← MonoidAlgebra.one_def,
      map_one]
  -- the JM recursion at the endomorphism level
  have hconjE : ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k)))
        * ((Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) a))
        * ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k)))
      = ((Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) b))
        - ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k))) := by
    rw [← map_mul, ← map_mul, conj_jucysMurphy_self a b hab, map_sub]
  have hfixE : ∀ s : Fin (Specht.nOf μ), s ≠ a → s ≠ b →
      ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k)))
          * ((Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s))
          * ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k)))
        = (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) := by
    intro s hsa hsb
    rw [← map_mul, ← map_mul, conj_jucysMurphy_other a b s hab hsa hsb]
  -- the content gap, cast into k
  have hcast : ((cellContent ((tableauCellEquiv μ T b : ℕ × ℕ)) : ℤ) : k)
      - ((cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) : ℤ) : k)
      = ((cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))
          - cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) : ℤ) : k) := by
    push_cast
    ring
  have hnek : ((cellContent ((tableauCellEquiv μ T b : ℕ × ℕ)) : ℤ) : k)
      - ((cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) : ℤ) : k) ≠ 0 := by
    rw [hcast]
    exact_mod_cast hne
  have hsqk : (((cellContent ((tableauCellEquiv μ T b : ℕ × ℕ)) : ℤ) : k)
      - ((cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) : ℤ) : k)) ^ 2 ≠ 1 := by
    rw [hcast]
    exact_mod_cast hsq
  -- the transported vector
  refine ⟨((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k))) v
      - (((cellContent ((tableauCellEquiv μ T b : ℕ × ℕ)) : ℤ) : k)
          - ((cellContent ((tableauCellEquiv μ T a : ℕ × ℕ)) : ℤ) : k))⁻¹ • v, ?_, ?_, ?_⟩
  · -- membership: ρ(s)·v ∈ S^λ (subrepresentation) and S^λ is a submodule
    refine sub_mem ?_ (Submodule.smul_mem _ _ hmem)
    have hSv_eq : ((Specht.Mtab.rep (k := k) μ).asAlgebraHom (single (Equiv.swap a b) (1 : k))) v
        = Specht.Mtab.rep (k := k) μ (Equiv.swap a b) v := by
      rw [Representation.asAlgebraHom_single, one_smul]
    rw [hSv_eq]
    exact rep_mem_spechtSubmodule _ hmem
  · -- non-vanishing
    exact end_involution_eigenvector_ne _ hS2 hnz hsqk
  · -- the swapped eigen equations
    intro s
    have hblock := end_conj_shift_eigenvector_pair _ _ _ hS2 hconjE (heigk a) (heigk b) hnek
    rcases eq_or_ne s a with rfl | hsa
    · rw [hca', ← Int.cast_smul_eq_zsmul k]
      exact hblock.1
    · rcases eq_or_ne s b with rfl | hsb
      · rw [hcb', ← Int.cast_smul_eq_zsmul k]
        exact hblock.2
      · rw [hother s hsa hsb, ← Int.cast_smul_eq_zsmul k]
        exact end_conj_fix_eigenvector _ _ hS2 (hfixE s hsa hsb) (heigk s) _

/-- **OV existence core 1 (base seminormal vector — the residual cited debt).** For *some*
standard tableau `T₀` of shape `μ` there is a nonzero simultaneous JM eigenvector in `S^λ`
with the content tuple of `T₀`.  Classically this is the explicit seminormal vector of the
column-superstandard tableau (or, in Okounkov–Vershik, the highest weight of the GZ chain);
its construction needs the polytabloid straightening machinery not yet built here.  Strictly
smaller than the previous all-`T` existence core: existence for a *single* tableau, with the
propagation to every `T` now machine-checked (`seminormalVector_data_step` +
`syt_adjacentSwap_connected`).

**Base ring `[Field k] [CharZero k]`** — see `seminormalVector_data_exists`. -/
theorem seminormalVector_base_exists {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    ∃ T₀ : QOU.BraidKnot.StandardYoungTableau μ,
      ∃ v : Specht.Mtab (k := k) μ,
        v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
          ∀ s : Fin (Specht.nOf μ),
            (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
              = (cellContent ((tableauCellEquiv μ T₀ s : ℕ × ℕ))) • v := by
  -- Ref: [vershik-kerov1977] (Young's seminormal form, base vector: the explicit seminormal
  -- eigenvector of one distinguished — e.g. column-superstandard — tableau; the OV highest
  -- weight of the Gelfand–Zetlin chain).
  sorry

/-- **`AdjacentSwapStep` is symmetric (sorry-free).** Swapping `a, a+1` back in `T'` returns `T`:
the content-swap conditions are visibly symmetric in `T ↔ T'`, and the content gap only changes
*sign* under the swap (`c'_b − c'_a = c_a − c_b = −(c_b − c_a)`), so the admissibility conditions
`d ≠ 0` and `d² ≠ 1` survive (`omega` / `(a−b)² = (b−a)²`). -/
theorem adjacentSwapStep_symm (μ : YoungDiagram)
    {T T' : QOU.BraidKnot.StandardYoungTableau μ}
    (h : AdjacentSwapStep μ T T') : AdjacentSwapStep μ T' T := by
  obtain ⟨a, b, hab, hTa, hTb, hoff, hne, hsq⟩ := h
  refine ⟨a, b, hab, hTb.symm, hTa.symm, fun s hsa hsb => (hoff s hsa hsb).symm, ?_, ?_⟩
  · rw [hTb, hTa]; omega
  · rw [hTb, hTa]
    have hflip :
        (cellContent ((tableauCellEquiv μ T a : ℕ × ℕ))
            - cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))) ^ 2
          = (cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))
              - cellContent ((tableauCellEquiv μ T a : ℕ × ℕ))) ^ 2 := by ring
    rw [hflip]; exact hsq

/-- **The admissible-adjacent-swap chain relation is symmetric (sorry-free).** Immediate from
`adjacentSwapStep_symm` by induction on the chain (reverse each step). Hence
`Relation.ReflTransGen (AdjacentSwapStep μ)` is an equivalence relation on `SYT(μ)`. -/
theorem reflTransGen_adjacentSwap_symm (μ : YoungDiagram)
    {T T' : QOU.BraidKnot.StandardYoungTableau μ}
    (h : Relation.ReflTransGen (AdjacentSwapStep μ) T T') :
    Relation.ReflTransGen (AdjacentSwapStep μ) T' T := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih => exact Relation.ReflTransGen.head (adjacentSwapStep_symm μ hstep) ih

/-- **OV existence core 2 (adjacent-swap connectivity — reduced to the one-directional base walk).**
There is a distinguished standard tableau `T₀` (the row-superstandard tableau) to which *every*
standard tableau of shape `μ` is connected by a chain of admissible adjacent swaps. This is the
genuine combinatorial content of Young's exchange argument (§3.10 of Sagan): any standard tableau
is walked toward the row-superstandard one by repeatedly swapping some `(k, k+1)` whose labels are
neither row- nor column-adjacent (contents differ by `≥ 2`, giving the `d ≠ 0`, `d² ≠ 1` gap
conditions), decreasing an inversion measure at each step. The full "any two are connected"
statement (`syt_adjacentSwap_connected`) is derived from this **sorry-free** via the symmetry
lemmas above — so the residual cited debt is now the strictly smaller *one-directional, single-base*
walk, not the two-directional connectivity. -/
theorem syt_all_connect_to_some (μ : YoungDiagram) :
    ∃ T₀ : QOU.BraidKnot.StandardYoungTableau μ,
      ∀ T : QOU.BraidKnot.StandardYoungTableau μ,
        Relation.ReflTransGen (AdjacentSwapStep μ) T T₀ := by
  -- Ref: [sagan2001] (The Symmetric Group, §3.10 / the exchange argument: every SYT walks to the
  -- row-superstandard tableau under admissible adjacent transpositions, by inversion induction).
  sorry

/-- **OV existence core 2 (adjacent-swap connectivity of standard tableaux — combinatorial).**
Any two standard Young tableaux of the same shape are connected by a chain of admissible
adjacent swaps (`AdjacentSwapStep`).

**De-abstraction (this proof is sorry-free).** Both `T` and `T'` connect to the common base `T₀`
(`syt_all_connect_to_some`, core 2); reverse the second leg by symmetry
(`reflTransGen_adjacentSwap_symm`) and compose (`T ⤳* T₀ ⤳* T'`). The residual cited debt is thus
the strictly smaller one-directional base walk, with the two-directional plumbing proved here. -/
theorem syt_adjacentSwap_connected (μ : YoungDiagram)
    (T T' : QOU.BraidKnot.StandardYoungTableau μ) :
    Relation.ReflTransGen (AdjacentSwapStep μ) T T' := by
  obtain ⟨T₀, hbase⟩ := syt_all_connect_to_some μ
  exact (hbase T).trans (reflTransGen_adjacentSwap_symm μ (hbase T'))

/-- **The Okounkov–Vershik existence theorem (Young's seminormal vector), de-abstracted.** For
every standard Young tableau `T` of shape `μ`, there exists a nonzero vector `v` in the Specht
submodule `S^λ` on which **each** Jucys–Murphy element `X_s` acts diagonally with eigenvalue
`cellContent (c)`, where `c = tableauCellEquiv μ T s` is the cell of `μ` holding label `s` in `T`.

**De-abstraction (this proof is sorry-free; its inputs are the two named cores).** Take the base
seminormal vector (`seminormalVector_base_exists`, core 1), walk the admissible-adjacent-swap
chain from its tableau to `T` (`syt_adjacentSwap_connected`, core 2), transporting the
eigenvector along each step by the machine-checked classical 2×2 seminormal block
(`seminormalVector_data_step`: the JM recursion `s·X_a·s = X_b − s` + the eigenvalue-swap /
fixed-operator / non-vanishing linear algebra + `S^λ`-invariance — all sorry-free).  The cited
debt is thus reduced from "all-`T` eigenvector existence" to {base-tableau existence,
adjacent-swap connectivity} — each strictly more atomic.

**Base ring `[Field k] [CharZero k]` (§7c over-generality fix).** Stated over a char-0 field, NOT
the file-wide `[CommRing k]`: over a general commutative ring the integer cell-contents can collide
modulo the characteristic (e.g. `ℤ/pℤ` with `c_i ≡ c_j` but `c_i ≠ c_j`), so the cast JM eigenvalues
`↑c_s` stop being distinct, the eigenspaces merge, and a simultaneous eigenvector with the
*prescribed* content tuple need not exist in `S^λ` — the `[CommRing k]` form is over-general (false at
`ℤ/pℤ`).  Young's seminormal form is genuinely a char-0 fact (it inverts the content differences
`c_i − c_j`, exactly as the transport step does). -/
theorem seminormalVector_data_exists {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∃ v : Specht.Mtab (k := k) μ,
      v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
        ∀ s : Fin (Specht.nOf μ),
          (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
            = (cellContent ((tableauCellEquiv μ T s : ℕ × ℕ))) • v := by
  obtain ⟨T₀, hbase⟩ := seminormalVector_base_exists (k := k) μ
  have hchain : Relation.ReflTransGen (AdjacentSwapStep μ) T₀ T :=
    syt_adjacentSwap_connected μ T₀ T
  induction hchain with
  | refl => exact hbase
  | tail _ hstep ih => exact seminormalVector_data_step μ hstep ih

/-- **Jucys–Murphy eigenvalue theorem (Okounkov–Vershik).** The Specht module `S^λ` admits a
Gelfand–Zetlin / seminormal basis indexed by the standard Young tableaux of shape `μ`, on which
every JM element `X_k` acts **diagonally** with eigenvalue `cellContent (cell of k in T)`.

We state this as: for every standard tableau `T` of shape `μ`, there is a seminormal eigenvector
`sv` whose indexing tableau is `T`.  The eigenproperty itself is recorded as the `isEig` field of
`SeminormalVector` (each `X_k` acts by the content of `k`'s cell); the *content* of the theorem is
the **existence** of such vectors for every `T`, i.e. that the GZ basis exists and diagonalises the
JM elements.  Together with `jucysMurphy_commute`, this is the heart of the OV approach.

**Reduction (sorry-free here, modulo the named eigenvector core).** This theorem no longer carries
the `sorry` directly.  Its `cellOf` field is *constructed* from `T` by the sorry-free brick-4
bijection `tableauCellEquiv μ T` (= `sytToTableau T`), and the eigenvector data `(v, mem, nz, isEig)`
is supplied by `seminormalVector_data_exists` — the single cited core that isolates exactly Young's
seminormal-vector existence.  `sv.T = T` then holds by `rfl`.  So the genuine OV debt is now named
precisely (`seminormalVector_data_exists`) and the *bijection* part — historically bundled into the
same `sorry` — is genuinely closed.

**Base ring `[Field k] [CharZero k]`** — inherited from `seminormalVector_data_exists` (the
seminormal eigenvector is a char-0 fact; the `[CommRing k]` form is over-general, false at `ℤ/pℤ`). -/
theorem jucysMurphy_eigenvalue {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∃ sv : SeminormalVector (k := k) μ, sv.T = T := by
  obtain ⟨v, hmem, hnz, hisEig⟩ := seminormalVector_data_exists (k := k) μ T
  exact ⟨{ T := T
           v := v
           mem := hmem
           nz := hnz
           cellOf := tableauCellEquiv μ T
           isEig := hisEig }, rfl⟩

/-- The span of the seminormal vectors, as a submodule of `M^λ` (local abbreviation; the public
`seminormalVectors_span` below uses the inline `Submodule.span …` form for splice-compatibility). -/
noncomputable abbrev seminormalSpan {k : Type} [Field k] (μ : YoungDiagram) :
    Submodule k (Specht.Mtab (k := k) μ) :=
  Submodule.span k (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v))

/-- **Easy direction (sorry-free).** The seminormal span sits inside `S^λ` — every seminormal vector
lies in `S^λ` (the `mem` field of `SeminormalVector`). -/
theorem seminormalSpan_le {k : Type} [Field k] (μ : YoungDiagram) :
    seminormalSpan (k := k) μ ≤ Specht.SpechtSubmodule (k := k) μ := by
  rw [seminormalSpan, Submodule.span_le]
  rintro _ ⟨sv, rfl⟩
  exact sv.mem

/-- **(L1) Joint eigenvectors with pairwise-distinct eigenvalue tuples are linearly independent.**
Generic linear algebra (no tableau/Specht content, sorry-free): a family `v : ι → V` of nonzero
vectors, each a simultaneous eigenvector of every operator `A s` with eigenvalue tuple
`c i : S → k`; if the tuple map `c` is injective, the family is independent.

Proof: `linearIndependent_iff'` + strong induction on the support `t` of a finite dependency.  For
`j ∈ t`: if `t = {j}`, then `g j • v j = 0` forces `g j = 0` (`v j ≠ 0`); otherwise pick `i₀ ∈ t`
with `i₀ ≠ j` and a separator `s₀` with `c i₀ s₀ ≠ c j s₀` (tuple injectivity), apply `A s₀` and
subtract `c i₀ s₀ ·` the original relation — the `i₀` term dies, and the inductive hypothesis on
`t.erase i₀` gives `g j · (c j s₀ − c i₀ s₀) = 0`, whence `g j = 0`.

Note the operators need **not** commute and no diagonalisability is assumed — only the given
family's eigen-structure is used.  This is the entire linear-algebra content of the OV
"distinct content-tuples ⇒ independent" step, factored out of the citation. -/
theorem linearIndependent_of_joint_eigenvectors {k : Type} [Field k]
    {V : Type*} [AddCommGroup V] [Module k V] {ι S : Type*}
    (A : S → V →ₗ[k] V) (v : ι → V) (c : ι → S → k)
    (hnz : ∀ i, v i ≠ 0)
    (heig : ∀ i s, A s (v i) = c i s • v i)
    (hinj : Function.Injective c) :
    LinearIndependent k v := by
  classical
  rw [linearIndependent_iff']
  intro t
  induction t using Finset.strongInduction with
  | _ t IH =>
    intro g hrel j hj
    by_cases hcard : t.card ≤ 1
    · -- singleton support: g j • v j = 0 with v j ≠ 0
      have ht : t = {j} := Finset.eq_singleton_iff_unique_mem.mpr
        ⟨hj, fun x hx => Finset.card_le_one.mp hcard x hx j hj⟩
      rw [ht, Finset.sum_singleton] at hrel
      exact (smul_eq_zero.mp hrel).resolve_right (hnz j)
    · push_neg at hcard
      -- a second support element i₀ ≠ j
      obtain ⟨i₀, hi₀t, hi₀j⟩ : ∃ i₀ ∈ t, i₀ ≠ j := by
        obtain ⟨a, ha, b, hb, hab⟩ := Finset.one_lt_card.mp hcard
        rcases eq_or_ne a j with rfl | haj
        · exact ⟨b, hb, fun h => hab h.symm⟩
        · exact ⟨a, ha, haj⟩
      -- a separating operator index
      obtain ⟨s₀, hs₀⟩ := Function.ne_iff.mp (fun h : c i₀ = c j => hi₀j (hinj h))
      -- apply A s₀ to the relation
      have h1 : ∑ i ∈ t, (g i * c i s₀) • v i = 0 := by
        have h := congrArg (A s₀) hrel
        rw [map_sum, map_zero] at h
        calc ∑ i ∈ t, (g i * c i s₀) • v i
            = ∑ i ∈ t, A s₀ (g i • v i) := by
              refine Finset.sum_congr rfl fun i _ => ?_
              rw [map_smul, heig, smul_smul]
          _ = 0 := h
      -- scale the relation by c i₀ s₀
      have h2 : ∑ i ∈ t, (g i * c i₀ s₀) • v i = 0 := by
        calc ∑ i ∈ t, (g i * c i₀ s₀) • v i
            = c i₀ s₀ • ∑ i ∈ t, g i • v i := by
              rw [Finset.smul_sum]
              refine Finset.sum_congr rfl fun i _ => ?_
              rw [smul_smul, mul_comm]
          _ = 0 := by rw [hrel, smul_zero]
      -- subtract: the i₀ coefficient is killed
      have hrel2 : ∑ i ∈ t, (g i * (c i s₀ - c i₀ s₀)) • v i = 0 := by
        calc ∑ i ∈ t, (g i * (c i s₀ - c i₀ s₀)) • v i
            = ∑ i ∈ t, ((g i * c i s₀) • v i - (g i * c i₀ s₀) • v i) := by
              refine Finset.sum_congr rfl fun i _ => ?_
              rw [mul_sub, sub_smul]
          _ = (∑ i ∈ t, (g i * c i s₀) • v i) - ∑ i ∈ t, (g i * c i₀ s₀) • v i :=
              Finset.sum_sub_distrib _ _
          _ = 0 := by rw [h1, h2, sub_zero]
      have hrel3 : ∑ i ∈ t.erase i₀, (g i * (c i s₀ - c i₀ s₀)) • v i = 0 := by
        have h := Finset.add_sum_erase t (fun i => (g i * (c i s₀ - c i₀ s₀)) • v i) hi₀t
        rw [hrel2] at h
        simpa [sub_self] using h
      -- inductive hypothesis on the smaller support, read off at j
      have hIH := IH (t.erase i₀) (Finset.erase_ssubset hi₀t)
        (fun i => g i * (c i s₀ - c i₀ s₀)) hrel3 j
        (Finset.mem_erase.mpr ⟨Ne.symm hi₀j, hj⟩)
      rcases mul_eq_zero.mp hIH with h | h
      · exact h
      · exact absurd (sub_eq_zero.mp h).symm hs₀

/-! #### L2 helpers: entries strictly increase along diagonals; the row-count formula

The proof of L2 below avoids diagram-removal entirely.  In a standard tableau the entries
strictly increase along each **diagonal** (`row_strict` + `col_strict` + up-left-closedness), the
diagonal-`d` cells of `μ` form a contiguous row range starting at row `(−d)⁺`, and therefore

  `row(s) = (−content s)⁺ + #{s' < s with the same content}`

— the row of a label is determined by the content **tuple** alone.  Two tableaux with the same
content tuple then agree cell-by-cell (columns follow from rows + contents), hence are equal. -/

private lemma entry_lt_diag_succ {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) {i j : ℕ}
    (hmem : (i + 1, j + 1) ∈ μ) : T.entry i j < T.entry (i + 1) (j + 1) :=
  lt_trans
    (T.row_strict i j (μ.up_left_mem (Nat.le_succ i) le_rfl hmem))
    (T.col_strict i (j + 1) hmem)

/-- Entries strictly increase along a diagonal: same content, strictly smaller row ⇒ strictly
smaller entry.  Induction on the row of the lower cell, stepping through the diagonal
predecessor `(y₁ − 1, y₂ − 1)` (in `μ` by up-left-closedness). -/
private lemma entry_lt_of_diag_row_lt {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∀ (r : ℕ) {x y : ℕ × ℕ}, x ∈ μ → y ∈ μ → y.1 = r →
      (x.2 : ℤ) - (x.1 : ℤ) = (y.2 : ℤ) - (y.1 : ℤ) → x.1 < y.1 →
      T.entry x.1 x.2 < T.entry y.1 y.2 := by
  intro r
  induction r with
  | zero => intro x y _ _ hy1 _ hlt; omega
  | succ r IH =>
    rintro ⟨x1, x2⟩ ⟨y1, y2⟩ hx hy hy1 hd hlt
    simp only at hy1 hd hlt ⊢
    subst hy1
    rcases eq_or_lt_of_le (Nat.lt_succ_iff.mp hlt) with heq | hlt'
    · -- x is the immediate diagonal predecessor: y = (x1+1, x2+1)
      subst heq
      have hy2 : y2 = x2 + 1 := by omega
      subst hy2
      exact entry_lt_diag_succ T hy
    · -- step through z = (r, y2 − 1)
      have hzmem : (r, y2 - 1) ∈ μ :=
        μ.up_left_mem (Nat.le_succ r) (Nat.sub_le y2 1) hy
      have hstep : T.entry r (y2 - 1) < T.entry (r + 1) y2 := by
        have h1 : y2 - 1 + 1 = y2 := by omega
        have := entry_lt_diag_succ T (i := r) (j := y2 - 1) (by rw [h1]; exact hy)
        rwa [h1] at this
      refine lt_trans (IH (x := (x1, x2)) (y := (r, y2 - 1)) hx hzmem rfl ?_ hlt') hstep
      have : ((y2 - 1 : ℕ) : ℤ) = (y2 : ℤ) - 1 := by omega
      simp only [this]
      omega

private lemma cellLabel_tableauCellEquiv {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    QOU.BraidKnot.SpechtStandardBasis.cellLabel T (tableauCellEquiv μ T s) = s :=
  Equiv.apply_symm_apply
    (Equiv.ofBijective _ (QOU.BraidKnot.SpechtStandardBasis.cellLabel_bijective T)) s

private lemma tableauCellEquiv_cellLabel {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (c : μ.cells) :
    tableauCellEquiv μ T (QOU.BraidKnot.SpechtStandardBasis.cellLabel T c) = c :=
  Equiv.symm_apply_apply
    (Equiv.ofBijective _ (QOU.BraidKnot.SpechtStandardBasis.cellLabel_bijective T)) c

/-- The entry at the cell of label `s` is `s` itself. -/
private lemma entry_tableauCellEquiv {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    T.entry ((tableauCellEquiv μ T s : ℕ × ℕ)).1 ((tableauCellEquiv μ T s : ℕ × ℕ)).2
      = s.val := by
  have h := congrArg Fin.val (cellLabel_tableauCellEquiv T s)
  simpa [QOU.BraidKnot.SpechtStandardBasis.cellLabel] using h

private lemma tableauCellEquiv_mem {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    ((tableauCellEquiv μ T s : ℕ × ℕ)) ∈ μ := by
  have := (tableauCellEquiv μ T s).2
  rwa [YoungDiagram.mem_cells] at this

/-- **The row-count formula.** The row of the cell holding label `s` equals
`(−content)⁺ + #{s' < s with the same content}` — determined by the content tuple alone. -/
private lemma row_eq_offset_add_count {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    ((tableauCellEquiv μ T s : ℕ × ℕ)).1
      = (-(cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)))).toNat
        + (Finset.univ.filter (fun s' : Fin (Specht.nOf μ) =>
            cellContent ((tableauCellEquiv μ T s' : ℕ × ℕ))
              = cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) ∧ s' < s)).card := by
  classical
  set x : ℕ × ℕ := ((tableauCellEquiv μ T s : ℕ × ℕ)) with hxdef
  have hxmem : x ∈ μ := tableauCellEquiv_mem T s
  set d : ℤ := cellContent x
  have hd : d = (x.2 : ℤ) - (x.1 : ℤ) := rfl
  -- the count is the size of the row range [(−d)⁺, x.1)
  have hcard : (Finset.univ.filter (fun s' : Fin (Specht.nOf μ) =>
        cellContent ((tableauCellEquiv μ T s' : ℕ × ℕ)) = d ∧ s' < s)).card
      = (Finset.Ico (-d).toNat x.1).card := by
    refine Finset.card_bij'
      (fun s' _ => ((tableauCellEquiv μ T s' : ℕ × ℕ)).1)
      (fun i hi => QOU.BraidKnot.SpechtStandardBasis.cellLabel T
        ⟨(i, ((i : ℤ) + d).toNat), by
          rw [YoungDiagram.mem_cells]
          rw [Finset.mem_Ico] at hi
          have hx' : (x.1, x.2) ∈ μ := by rwa [Prod.mk.eta]
          refine μ.up_left_mem (le_of_lt hi.2) ?_ hx'
          rw [Int.toNat_le]
          omega⟩)
      ?_ ?_ ?_ ?_
    · -- forward well-defined: row(s') ∈ Ico (−d)⁺ x.1
      intro s' hs'
      obtain ⟨-, hc, hlt⟩ := Finset.mem_filter.mp hs'
      have hymem : ((tableauCellEquiv μ T s' : ℕ × ℕ)) ∈ μ := tableauCellEquiv_mem T s'
      have hcy : ((((tableauCellEquiv μ T s' : ℕ × ℕ)).2 : ℤ))
          - (((tableauCellEquiv μ T s' : ℕ × ℕ)).1 : ℤ) = d := by
        simpa [cellContent] using hc
      show ((tableauCellEquiv μ T s' : ℕ × ℕ)).1 ∈ Finset.Ico (-d).toNat x.1
      rw [Finset.mem_Ico]
      constructor
      · -- (−d)⁺ ≤ row(s') since the column is a natural number
        rw [Int.toNat_le]
        omega
      · -- row(s') < x.1: not equal (else same cell ⇒ s' = s), not greater (entry monotone)
        rcases lt_trichotomy ((tableauCellEquiv μ T s' : ℕ × ℕ)).1 x.1 with h | h | h
        · exact h
        · -- same row + same content ⇒ same cell ⇒ s' = s, contra s' < s
          exfalso
          have hy2 : ((tableauCellEquiv μ T s' : ℕ × ℕ)).2 = x.2 := by omega
          have hcell : (tableauCellEquiv μ T s') = (tableauCellEquiv μ T s) := by
            apply Subtype.ext
            rw [← hxdef]
            exact Prod.ext h hy2
          have hss := congrArg (QOU.BraidKnot.SpechtStandardBasis.cellLabel T) hcell
          rw [cellLabel_tableauCellEquiv, cellLabel_tableauCellEquiv] at hss
          exact absurd hss (ne_of_lt hlt)
        · -- row(s') > x.1 ⇒ entry x < entry(s'-cell) ⇒ s < s', contra
          exfalso
          have hmono := entry_lt_of_diag_row_lt T ((tableauCellEquiv μ T s' : ℕ × ℕ)).1
            hxmem hymem rfl (by omega) h
          rw [hxdef] at hmono
          rw [entry_tableauCellEquiv, entry_tableauCellEquiv] at hmono
          exact absurd (Fin.lt_def.mpr hmono) (not_lt.mpr (le_of_lt hlt))
    · -- backward well-defined: the constructed label is in the filter
      intro i hi
      rw [Finset.mem_Ico] at hi
      have h0 : (0 : ℤ) ≤ (i : ℤ) + d := by
        have h1 := hi.1
        rw [Int.toNat_le] at h1
        omega
      rw [Finset.mem_filter]
      refine ⟨Finset.mem_univ _, ?_, ?_⟩
      · -- content of its cell = d
        rw [tableauCellEquiv_cellLabel]
        show ((((i : ℤ) + d).toNat : ℤ)) - (i : ℤ) = d
        rw [Int.toNat_of_nonneg h0]
        ring
      · -- the constructed label < s: its entry is on the diagonal at a smaller row
        have hcmem : ((i, ((i : ℤ) + d).toNat) : ℕ × ℕ) ∈ μ := by
          have hx' : (x.1, x.2) ∈ μ := by rwa [Prod.mk.eta]
          refine μ.up_left_mem (le_of_lt hi.2) ?_ hx'
          rw [Int.toNat_le]
          omega
        have hmono := entry_lt_of_diag_row_lt T x.1
          (x := (i, ((i : ℤ) + d).toNat)) (y := x) hcmem hxmem rfl
          (by
            show ((((i : ℤ) + d).toNat : ℤ)) - (i : ℤ) = (x.2 : ℤ) - (x.1 : ℤ)
            rw [Int.toNat_of_nonneg h0]
            omega) hi.2
        rw [Fin.lt_def]
        show T.entry i (((i : ℤ) + d).toNat) < s.val
        rw [← entry_tableauCellEquiv T s, ← hxdef]
        exact hmono
    · -- left inverse: reconstructing from the row gives back s'
      intro s' hs'
      obtain ⟨-, hc, -⟩ := Finset.mem_filter.mp hs'
      have hcy : ((((tableauCellEquiv μ T s' : ℕ × ℕ)).2 : ℤ))
          - (((tableauCellEquiv μ T s' : ℕ × ℕ)).1 : ℤ) = d := by
        simpa [cellContent] using hc
      have key : ∀ (c : μ.cells), (c : ℕ × ℕ) = ((tableauCellEquiv μ T s' : ℕ × ℕ)) →
          QOU.BraidKnot.SpechtStandardBasis.cellLabel T c = s' := by
        intro c hcv
        rw [Subtype.ext hcv, cellLabel_tableauCellEquiv]
      apply key
      refine Prod.ext rfl ?_
      show (((((tableauCellEquiv μ T s' : ℕ × ℕ)).1 : ℤ) + d).toNat)
          = ((tableauCellEquiv μ T s' : ℕ × ℕ)).2
      omega
    · -- right inverse: the row of the constructed cell is i
      intro i hi
      simp only [tableauCellEquiv_cellLabel]
  rw [hcard, Nat.card_Ico]
  -- x.1 ≥ (−d)⁺ since the column is a natural number
  have hle : (-d).toNat ≤ x.1 := by
    rw [Int.toNat_le]
    omega
  omega

/-- **(L2) The seminormal simple-spectrum core (combinatorial): the content tuple determines the
standard tableau — PROVED.** If two standard Young tableaux of shape `μ` assign the same
cell-content to every label, they are equal.

Proof (no diagram-removal): entries strictly increase along each diagonal
(`entry_lt_of_diag_row_lt`), so the **row** of the cell holding label `s` is
`(−content s)⁺ + #{s' < s with the same content}` (`row_eq_offset_add_count`) — a function of the
content tuple alone, hence shared by `T` and `T'`.  The **column** then follows from
row + content, so the label→cell maps coincide; inverting, the cell→label maps (`cellLabel`)
coincide, i.e. all entries agree on `μ` (and off `μ` both are pinned to `0`), so `T = T'`. -/
theorem syt_content_tuple_injective (μ : YoungDiagram)
    (T T' : QOU.BraidKnot.StandardYoungTableau μ)
    (h : ∀ s : Fin (Specht.nOf μ),
      cellContent ((tableauCellEquiv μ T s : ℕ × ℕ))
        = cellContent ((tableauCellEquiv μ T' s : ℕ × ℕ))) :
    T = T' := by
  classical
  -- the label→cell maps agree
  have hcell : ∀ s : Fin (Specht.nOf μ),
      ((tableauCellEquiv μ T s : ℕ × ℕ)) = ((tableauCellEquiv μ T' s : ℕ × ℕ)) := by
    intro s
    have hrow : ((tableauCellEquiv μ T s : ℕ × ℕ)).1
        = ((tableauCellEquiv μ T' s : ℕ × ℕ)).1 := by
      rw [row_eq_offset_add_count T s, row_eq_offset_add_count T' s, h s]
      congr 2
      apply Finset.filter_congr
      intro s' _
      rw [h s']
    refine Prod.ext hrow ?_
    -- columns: (col : ℤ) = row + content on both sides
    have h1 : ((((tableauCellEquiv μ T s : ℕ × ℕ)).2 : ℤ))
        - (((tableauCellEquiv μ T s : ℕ × ℕ)).1 : ℤ)
        = ((((tableauCellEquiv μ T' s : ℕ × ℕ)).2 : ℤ))
        - (((tableauCellEquiv μ T' s : ℕ × ℕ)).1 : ℤ) := by
      simpa [cellContent] using h s
    omega
  -- hence the cell→label maps agree, i.e. the entries agree on μ
  ext i j
  by_cases hij : (i, j) ∈ μ
  · have hc : ((i, j) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells _).mpr hij
    set c : μ.cells := ⟨(i, j), hc⟩
    set s : Fin (Specht.nOf μ) := QOU.BraidKnot.SpechtStandardBasis.cellLabel T c with hsdef
    have h1 : (tableauCellEquiv μ T s : ℕ × ℕ) = ((i, j) : ℕ × ℕ) := by
      rw [hsdef, tableauCellEquiv_cellLabel]
    have h2 : (tableauCellEquiv μ T' s : ℕ × ℕ) = ((i, j) : ℕ × ℕ) := by
      rw [← hcell s, h1]
    -- entries at (i,j): both equal s.val
    have e1 : T.entry i j = s.val := by
      have := entry_tableauCellEquiv T s
      rw [h1] at this
      exact this
    have e2 : T'.entry i j = s.val := by
      have := entry_tableauCellEquiv T' s
      rw [h2] at this
      exact this
    rw [e1, e2]
  · rw [T.zero_off i j hij, T'.zero_off i j hij]

/-- **The atomic OV completeness core (Young's seminormal form, independence half) — now assembled,
not cited.** The seminormal (Gelfand–Zetlin) vectors form a **linearly independent** family indexed
by **all** standard Young tableaux of shape `μ` — i.e. `#SYT(μ) = dim S^λ`-many independent
simultaneous JM-eigenvectors.

**De-abstraction (this proof is sorry-free; its only cited input is the existence core).** The
family is built by choice from `seminormalVector_data_exists` (the eigenvector existence core);
independence is the generic joint-eigenvalue argument `linearIndependent_of_joint_eigenvectors`
(L1, proved) applied to the operators `ρ(X_s)` with eigenvalue tuples the cast content vectors
`s ↦ ((cellContent (cell of s in T) : ℤ) : k)`, whose injectivity is `Int.cast_injective`
(`CharZero`) + the combinatorial simple-spectrum fact `syt_content_tuple_injective` (L2 —
**proved**, via the diagonal row-count formula).  So the entire cited debt of this statement is
`seminormalVector_data_exists` — both the linear algebra and the spectrum combinatorics are
machine-checked.

This is strictly more atomic than the old `seminormalVectors_span` cited `sorry`: that cited the
whole inclusion `S^λ ⊆ span`; the *spanning* is a sorry-free dimension corollary
(`seminormalVectors_span` below), and the independence is now itself assembled from more atomic
parts.

**Base ring `[Field k] [CharZero k]`** (not over-general): in positive characteristic the cell
contents collide mod `p`, merging eigenspaces and breaking distinctness, so the `[CommRing k]` form
would be false at its generality. -/
theorem exists_indep_seminormal_family {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    ∃ b : QOU.BraidKnot.StandardYoungTableau μ → SeminormalVector (k := k) μ,
      LinearIndependent k (fun T => (b T).v) := by
  -- build the family by choice from the existence core
  choose v hmem hnz hisEig using
    fun T : QOU.BraidKnot.StandardYoungTableau μ => seminormalVector_data_exists (k := k) μ T
  refine ⟨fun T => { T := T, v := v T, mem := hmem T, nz := hnz T,
                     cellOf := tableauCellEquiv μ T, isEig := hisEig T }, ?_⟩
  -- independence via L1: operators ρ(X_s), tuples the cast content vectors
  refine linearIndependent_of_joint_eigenvectors
    (fun s : Fin (Specht.nOf μ) =>
      (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s))
    (fun T => v T)
    (fun T s => ((cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) : ℤ) : k))
    hnz ?_ ?_
  · intro T s
    rw [hisEig T s]
    exact (Int.cast_smul_eq_zsmul k _ _).symm
  · intro T T' hTT'
    apply syt_content_tuple_injective μ T T'
    intro s
    have hs : ((cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) : ℤ) : k)
        = ((cellContent ((tableauCellEquiv μ T' s : ℕ × ℕ)) : ℤ) : k) := congrFun hTT' s
    exact_mod_cast hs

/-- **Plumbing (sorry-free): `#SYT(μ) ≤ dim_k(span)`.** The span of the independent `#SYT(μ)`-family
already has dimension `#SYT(μ)` (`finrank_span_eq_card`), and it is contained in `seminormalSpan`
(`Submodule.finrank_mono`). -/
theorem numSYT_le_finrank_seminormalSpan {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    numSYT μ ≤ Module.finrank k (seminormalSpan (k := k) μ) := by
  obtain ⟨b, hb⟩ := exists_indep_seminormal_family (k := k) μ
  have hsub : Submodule.span k (Set.range (fun T => (b T).v)) ≤ seminormalSpan (k := k) μ := by
    rw [seminormalSpan]
    apply Submodule.span_mono
    rintro _ ⟨T, rfl⟩
    exact ⟨b T, rfl⟩
  have hcard : Module.finrank k (Submodule.span k (Set.range (fun T => (b T).v)))
      = Fintype.card (QOU.BraidKnot.StandardYoungTableau μ) := finrank_span_eq_card hb
  have hnum : numSYT μ = Fintype.card (QOU.BraidKnot.StandardYoungTableau μ) := by
    rw [numSYT, Nat.card_eq_fintype_card]
  rw [hnum, ← hcard]
  exact Submodule.finrank_mono hsub

/-- **Seminormal vectors span the Specht module (Okounkov–Vershik) — sorry-free modulo the single
independence core `exists_indep_seminormal_family`.** The Specht submodule `S^λ ≤ M^λ` is contained in
the span of the seminormal (Gelfand–Zetlin) vectors; with the automatic reverse inclusion
`seminormalSpan_le`, the GZ vectors span `S^λ`.  This is the OV completeness consumed by the punchline
`centralC2_acts_by_contentSqSum` (the scalar action propagates from the spanning vectors by
`Submodule.span_induction`).

**De-abstraction.** `span ≤ S^λ` (`seminormalSpan_le`) plus `dim S^λ = #SYT(μ) ≤ dim(span)` (the
counting plumbing over the independence core) force `span = S^λ` on the finite-dimensional `M^λ`
(`Submodule.eq_of_le_of_finrank_le`); take `.ge`.  So the cited debt is now *independence of the
seminormal family* only — strictly more atomic than the old whole-inclusion `sorry`.

**Base ring — `[Field k] [CharZero k]` (§7c over-generality fix).** Completeness is false over `ℤ`
(seminormal vectors carry denominators ⇒ the integral vectors span only a proper finite-index
sublattice) and the independence is false in positive characteristic (contents collide mod `p`), so
the char-0 field is the honest generality.  The `[CommRing k]` form would be an over-general cited
claim — the same anti-pattern as `DominanceData.dom_colStab`; the capstone consumes the punchline at a
char-0 field `R`, so the restriction costs nothing downstream. -/
theorem seminormalVectors_span {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    Specht.SpechtSubmodule (k := k) μ
      ≤ Submodule.span k (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v)) := by
  have hle : seminormalSpan (k := k) μ ≤ Specht.SpechtSubmodule (k := k) μ :=
    seminormalSpan_le μ
  have hfr : Module.finrank k (Specht.SpechtSubmodule (k := k) μ)
      ≤ Module.finrank k (seminormalSpan (k := k) μ) := by
    rw [SpechtFinrankWired.specht_finrank_eq_numSYT_wired]
    exact numSYT_le_finrank_seminormalSpan μ
  exact (Submodule.eq_of_le_of_finrank_le hle hfr).ge

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
no `native_decide`.

**Base ring `[Field k] [CharZero k]`** — inherited from `seminormalVectors_span` (the completeness it
consumes is false over `ℤ`; see that lemma).  The capstone uses this at `k := R` with
`[Field R] [CharZero R]`. -/
theorem centralC2_acts_by_contentSqSum {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
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
