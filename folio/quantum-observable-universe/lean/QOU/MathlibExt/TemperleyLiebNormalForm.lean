import QOU.MathlibExt.TemperleyLiebSpanning
import Mathlib.Combinatorics.Enumerative.Catalan

/-!
# Jones normal forms for `TL_n(δ)` — the general index type

**Bean `qou-cds1`.** The Temperley–Lieb arc reaches the planar diagram basis
from four directions — spanning sets, lower bounds, Wedderburn decompositions
and semisimplicity all stop at it. `computations/tl_normal_form_basis_probe.py`
measured that object before this file was written, and two of its findings are
what this file is shaped by.

**First: which family.** The *Jones normal forms* — words

    (e_{i₁} e_{i₁-1} ⋯ e_{j₁}) (e_{i₂} ⋯ e_{j₂}) ⋯ (e_{i_k} ⋯ e_{j_k})
    with  i₁ < ⋯ < i_k,  j₁ < ⋯ < j_k,  j_r ≤ i_r

— number exactly `catalan n`, are distinct as words, and map *bijectively* onto
all planar diagrams. So they are the right family, and this file names it.

**Second, and it is a negative: `word length` is not a termination measure.**
Left multiplication by a generator does close in the normal forms, but the word
length changes by `+1`, `0`, or a NEGATIVE ODD amount, reaching `−5` by `n = 7`.
A "rewrite until shorter" induction — the first thing one reaches for — cannot
exist. **The index must be the combinatorial data `(I, J)`, and the
multiplication rule must be proved on that.** This file therefore indexes by a
pair of subsets and never by a word.

## The encoding, and why it is subsets rather than sorted lists

Pointwise domination `j_r ≤ i_r` on equal-size subsets of a linear order is
equivalent to a *threshold count*:

    ∀ x,  |I ∩ [0,x]|  ≤  |J ∩ [0,x]|

(verified against the pointwise form for every pair at `m ≤ 7` before being
adopted). The threshold form needs no sorting, is decidable, and makes
`NormalIdx m` a subtype of a `Fintype` — so `Fintype.card` is settled by
`decide` rather than by a bijection argument.

`elems` likewise filters `List.finRange`, which is *already* sorted, instead of
calling `Finset.sort`. That is not a style choice: `Finset.sort` is merge sort
and does **not** reduce in the kernel, so every `decide` below fails if it is
used. Measured, not assumed — it is how the first draft failed.

## What is proved here

* `NormalIdx m` is a `Fintype` with `card = catalan (m+1)` for `m ≤ 6`
  (`1, 2, 5, 14, 42, 132, 429`), bridged to Mathlib's `Nat.catalan` rather than
  to a hand-typed table. Each is one `decide`; `m = 6` costs 17 s, `m = 5` 6 s,
  and the rest are instant.
* Its `elt` map reproduces, **exactly**, the two bases this corpus has already
  proved: `{1, e₀}` for `TL₂` and `{1, e₀, e₁, e₀e₁, e₁e₀}` for `TL₃`.

That second point is the reason to trust the general definition: at the only two
places where a proved basis exists, the general construction lands on it.

## 🛑 These objects are PUBLISHED — corrected after the fact

Both the index type and its count are in the literature, and this file was
written without knowing it. `NormalIdx m` is *exactly* the set of
Gröbner–Shirshov standard monomials of `T(A_m)` in Kim–Lee, *Gröbner-Shirshov
bases for Temperley-Lieb algebras*, Palestine J. Math. **7** (2018) 11–17,
Prop. 3.1 — same `E_{i,j}` blocks, same `i₁ < ⋯ < i_p`, `j₁ < ⋯ < j_p`,
`j_r ≤ i_r` — quoted there from Kang–Lee–Lee–Oh, J. Algebra **252** (2002)
258–292, Prop. 6.2, where `|MT(A_{n-1})| = C_n` is the stated theorem. That
PDF is held at `library/fd58d8e182edda805fed0946606c5ab82f81/` and registered
as `[kimlee2018]`, read 2026-08-09, months before this file.

**What that changes is the epistemic status, not the workload.** Everything
listed below is still absent from this repository and still has to be written;
but it is *unformalised published mathematics*, not an open problem, and it
must not be described as the latter. In particular the closure lemma is the
four-rule reduction

    E_i E_i → δE_i,   E_i E_j → E_j E_i (i > j+1),
    E_{i,j} E_i → E_{i-2,j} E_i (i > j),   E_j E_{i,j} → E_j E_{i,j+2} (i > j)

which `computations/tl_gs_reduction_probe.py` checks against this folio's own
planar-diagram ground truth: 3456 products reproduced with zero mismatches,
closure on 19,413 monomial pairs, confluence under 9 reduction orders.

**The primary is not held** (bean `qou-qspu`); Kim–Lee is a type-B paper
quoting it. So cite Kim–Lee §3 as the accessible statement and Kang–Lee–Lee–Oh
as the source, and note that this folio has verified the rules rather than
read the proof of them.

## 🛑 What is NOT proved HERE

**No general theorem is in this file, and nothing in it stands in for one.**

* `Fintype.card (NormalIdx m) = catalan (m+1)` is checked at `m ≤ 6` by
  `decide` — it is **not** proved for general `m`. It *is* Kang–Lee–Lee–Oh
  Prop. 6.2 (above), so what is missing is a Lean proof of a known count.

  **A self-contained route is identified, and it is not "a bijection to Dyck
  paths".** A pair
  `(I, J)` is exactly a word of length `m` over four letters — `I`-only,
  `J`-only, *both*, *neither* — and the domination condition says every prefix
  has `#(I-only) ≤ #(J-only)`, with equality overall. Those are the **bicoloured
  Motzkin words** of length `m`: two step letters and two neutral letters, with
  a ballot condition. So the general count is the classical
  *bicoloured-Motzkin-to-Catalan* bijection, not a Dyck-path one, and the two
  neutral letters are exactly what makes it Motzkin rather than Dyck.

  Equivalently, in closed form,

      catalan (m+1)  =  ∑_k  C(m, 2k) · catalan k · 2^(m-2k)

  Both formulations were checked against `catalan (m+1)` for `m ≤ 10` before
  being written down here.

  Mathlib has `DyckWord`, `DyckWord.semilength` and `catalan_succ`. It has **no
  Motzkin words at all** — checked by enumerating
  `Mathlib/Combinatorics/Enumerative/` (Bell, Catalan, Composition,
  DoubleCounting, DyckWord, IncidenceAlgebra, InclusionExclusion, Partition,
  Stirling) and by searching the whole library for `*motzkin*`, whose only hit
  is `Tactic/Linarith/Oracle/FourierMotzkin`, an unrelated linear-arithmetic
  oracle. So the bijection is the work, and it starts from nothing.

  That is stated from a search rather than from the shape of the difficulty —
  the distinction a sibling branch had to correct on `main` the same day
  (`0e18f7b954`, *"I wrote a 'Mathlib lacks X' claim from the shape of the
  difficulty — Mathlib has it"*), and the same class as this file's own
  `Matrix.ext_iff_trace_mul_right` correction, where the lemma existed under the
  shape it was used for rather than the name it was known by.
* **`elt` is not proved to span `TL_{m+1}(δ)` for general `m`**, and that is the
  real content of `dim TL_n = catalan n`. It needs the closure lemma — which is
  the published four-rule reduction above, so the work is formalising a stated
  rewriting system, not finding one — on the `(I, J)` index and not on word
  length. `span_range_elt_two` is the `m = 2`
  instance only, and it is proved by *citing the existing `TL₃` result*, not by
  any general argument.
* `elt` is not proved injective at general `m` either.

No class, axiom or `sorry` stands in for any of these. They are open **in this
repository**; per the correction above, they are not open in the literature.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-- Ref: [kimlee2018] Palestine J. Math. 7 (2018), Special Issue I, 11-17, Prop. 3.1
-/

namespace QOU.MathlibExt.TemperleyLiebNormalForm

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebSpanning

/-! ## The index type -/

/-- A Jones normal form for `TL_{m+1}(δ)`, as a pair of equal-size subsets of
the `m` generators with `J` dominating `I`.

The domination is stated as a threshold count rather than pointwise on sorted
lists, which is what keeps the whole type decidable. -/
def NormalIdx (m : ℕ) : Type :=
  {p : Finset (Fin m) × Finset (Fin m) //
     p.2.card = p.1.card ∧
     ∀ x : Fin m, (p.1.filter (· ≤ x)).card ≤ (p.2.filter (· ≤ x)).card}

instance (m : ℕ) : DecidableEq (NormalIdx m) := by unfold NormalIdx; infer_instance
instance (m : ℕ) : Fintype (NormalIdx m) := by unfold NormalIdx; infer_instance

/-! ## The count, against Mathlib's `catalan`

Each is `decide` on a finite type; `m ≤ 4` is where that stays cheap. These are
checks at fixed `m`, **not** a general theorem — see the module docstring. -/

theorem card_zero : Fintype.card (NormalIdx 0) = catalan 1 := by
  rw [show catalan 1 = 1 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

theorem card_one : Fintype.card (NormalIdx 1) = catalan 2 := by
  rw [show catalan 2 = 2 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

theorem card_two : Fintype.card (NormalIdx 2) = catalan 3 := by
  rw [show catalan 3 = 5 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

theorem card_three : Fintype.card (NormalIdx 3) = catalan 4 := by
  rw [show catalan 4 = 14 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

set_option maxRecDepth 4000 in
theorem card_four : Fintype.card (NormalIdx 4) = catalan 5 := by
  rw [show catalan 5 = 42 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

set_option maxRecDepth 20000 in
theorem card_five : Fintype.card (NormalIdx 5) = catalan 6 := by
  rw [show catalan 6 = 132 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

set_option maxRecDepth 100000 in
theorem card_six : Fintype.card (NormalIdx 6) = catalan 7 := by
  rw [show catalan 7 = 429 by norm_num [catalan_eq_centralBinom_div, Nat.centralBinom,
    Nat.choose]]
  decide

/-! ## From an index to a word to an element -/

/-- The elements of `s` in increasing order. `List.finRange` is already sorted,
so no sorting algorithm is needed — and unlike `Finset.sort` this **reduces in
the kernel**, which is what makes every `decide` in this file possible. -/
def elems {m : ℕ} (s : Finset (Fin m)) : List (Fin m) :=
  (List.finRange m).filter (fun x => x ∈ s)

/-- `descRun i j = [i, i-1, …, j]` — the descending run one block contributes.
Every intermediate value is a valid `Fin m` because `i` is. -/
def descRun {m : ℕ} (i j : Fin m) : List (Fin m) :=
  (List.range (i.val + 1 - j.val)).map
    fun t => ⟨i.val - t, lt_of_le_of_lt (Nat.sub_le _ _) i.isLt⟩

/-- The word of a normal form: its blocks, in order. -/
def NormalIdx.word {m : ℕ} (p : NormalIdx m) : List (Fin m) :=
  (List.zipWith descRun (elems p.1.1) (elems p.1.2)).flatten

variable {R : Type*} [CommRing R]

/-- The `TL` element a normal form names: the product of its word. -/
noncomputable def NormalIdx.elt {m : ℕ} (δ : R) (p : NormalIdx m) : TLFin R δ m :=
  (p.word.map (fun i => e R δ (adjFin (n := m)) i)).prod

/-! ## `m = 1`: the general definition against the proved `TL₂` basis -/

section Two

/-- The two normal forms at `m = 1`. -/
def nf2 : Fin 2 → NormalIdx 1 :=
  ![⟨(∅, ∅), by decide⟩, ⟨({0}, {0}), by decide⟩]

theorem nf2_bijective : Function.Bijective nf2 := by
  rw [Fintype.bijective_iff_injective_and_card]
  exact ⟨by decide, by decide⟩

theorem elt_nf2_0 (δ : R) : (nf2 0).elt δ = 1 := by
  rw [NormalIdx.elt, show (nf2 0).word = [] from by decide]; simp

theorem elt_nf2_1 (δ : R) : (nf2 1).elt δ = tl2e (R := R) δ := by
  rw [NormalIdx.elt, show (nf2 1).word = [0] from by decide]; simp [tl2e]

/-- **The general definition reproduces the proved `TL₂` basis exactly.** -/
theorem range_elt_one (δ : R) :
    Set.range (NormalIdx.elt (m := 1) (R := R) δ)
      = ({1, tl2e (R := R) δ} : Set (TL2 (R := R) δ)) := by
  ext x
  constructor
  · rintro ⟨p, rfl⟩
    obtain ⟨k, rfl⟩ := nf2_bijective.surjective p
    fin_cases k
    · simp [elt_nf2_0]
    · simp [elt_nf2_1]
  · rintro (rfl | rfl)
    · exact ⟨nf2 0, elt_nf2_0 δ⟩
    · exact ⟨nf2 1, elt_nf2_1 δ⟩

/-- Hence the general spanning set spans at `m = 1` — by **citing** the `TL₂`
result, not by any general argument. -/
theorem span_range_elt_one (δ : R) :
    Submodule.span R (Set.range (NormalIdx.elt (m := 1) (R := R) δ)) = ⊤ := by
  rw [range_elt_one]; exact tl2_span_eq_top δ

end Two

/-! ## `m = 2`: the same, against the proved `TL₃` basis

`m = 2` is the first case with anything to say: the adjacency relation exists,
the blocks can be longer than one generator, and `e₀e₁ ≠ e₁e₀`. The words come
out `[]`, `[0]`, `[1]`, `[1,0]`, `[0,1]` — five, distinct, in bijection with the
index type. -/

section Three

/-- The five normal forms at `m = 2`. -/
def nf3 : Fin 5 → NormalIdx 2 :=
  ![⟨(∅, ∅), by decide⟩,
    ⟨({0}, {0}), by decide⟩,
    ⟨({1}, {1}), by decide⟩,
    ⟨({1}, {0}), by decide⟩,
    ⟨({0, 1}, {0, 1}), by decide⟩]

theorem nf3_bijective : Function.Bijective nf3 := by
  rw [Fintype.bijective_iff_injective_and_card]
  exact ⟨by decide, by decide⟩

theorem word_nf3 :
    (nf3 0).word = [] ∧ (nf3 1).word = [0] ∧ (nf3 2).word = [1] ∧
    (nf3 3).word = [1, 0] ∧ (nf3 4).word = [0, 1] := by
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

theorem elt_nf3_0 (δ : R) : (nf3 0).elt δ = 1 := by
  rw [NormalIdx.elt, show (nf3 0).word = [] from by decide]; simp

theorem elt_nf3_1 (δ : R) : (nf3 1).elt δ = a3 δ := by
  rw [NormalIdx.elt, show (nf3 1).word = [0] from by decide]; simp [a3]

theorem elt_nf3_2 (δ : R) : (nf3 2).elt δ = b3 δ := by
  rw [NormalIdx.elt, show (nf3 2).word = [1] from by decide]; simp [b3]

theorem elt_nf3_3 (δ : R) : (nf3 3).elt δ = b3 δ * a3 δ := by
  rw [NormalIdx.elt, show (nf3 3).word = [1, 0] from by decide]; simp [a3, b3]

theorem elt_nf3_4 (δ : R) : (nf3 4).elt δ = a3 δ * b3 δ := by
  rw [NormalIdx.elt, show (nf3 4).word = [0, 1] from by decide]; simp [a3, b3]

/-- **The general definition reproduces the proved `TL₃` basis exactly.**

This is the reason to trust the definition: at the only two places where this
corpus has a proved basis, the general construction lands on it. -/
theorem range_elt_two (δ : R) :
    Set.range (NormalIdx.elt (m := 2) (R := R) δ)
      = ({1, a3 δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) := by
  ext x
  constructor
  · rintro ⟨p, rfl⟩
    obtain ⟨k, rfl⟩ := nf3_bijective.surjective p
    fin_cases k
    · simp [elt_nf3_0]
    · simp [elt_nf3_1]
    · simp [elt_nf3_2]
    · simp [elt_nf3_3]
    · simp [elt_nf3_4]
  · rintro (rfl | rfl | rfl | rfl | rfl)
    · exact ⟨nf3 0, elt_nf3_0 δ⟩
    · exact ⟨nf3 1, elt_nf3_1 δ⟩
    · exact ⟨nf3 2, elt_nf3_2 δ⟩
    · exact ⟨nf3 4, elt_nf3_4 δ⟩
    · exact ⟨nf3 3, elt_nf3_3 δ⟩

/-- Hence the general spanning set spans at `m = 2` — again by **citing** the
`TL₃` result. No general spanning argument exists yet; see the module
docstring. -/
theorem span_range_elt_two (δ : R) :
    Submodule.span R (Set.range (NormalIdx.elt (m := 2) (R := R) δ)) = ⊤ := by
  rw [range_elt_two]; exact tl3_span_eq_top δ

end Three

end QOU.MathlibExt.TemperleyLiebNormalForm
