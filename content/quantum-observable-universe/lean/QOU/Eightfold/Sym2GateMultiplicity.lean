import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic

/-!
# QOU.Eightfold.Sym2GateMultiplicity — the `Sym²` gate forces EVEN dimension

Companion to `QOU.Eightfold.Sym2Gate` and `QOU.Eightfold.Sym2GateParity`.
Bean `qou-60o2`, under `qou-8pl3` (routes to `N = 3`) and epic `qou-8lxd`.

## The gap this closes

`Sym2GateParity.gate_fails_iff_odd_dim` decides the gate for a **single
irreducible** `SU(2)` representation: `Sym²(V_j)` contains a singlet exactly
when `dim V_j = 2j + 1` is odd.  The eightfold chapter and
`docs/audits/2026-08-07-eightfold-live-surface-collapse.md` then conclude that
no *odd-dimensional summand* of any `V^{⊗n}` can pass the gate.

**That does not settle the chapter's question.**  The `N = 3` problem asks for a
three-dimensional **object** `W`, and an object need not be irreducible.  The
irrep criterion is silent on, for instance,

    W  =  V_{1/2} ⊕ V_0        (dim 2 + 1 = 3)

which is a perfectly good 3-dimensional object of the tensor category generated
by the 2-dimensional fibre — `V_0` occurs in `V^{⊗2}`, `V_{1/2}` in `V` — and is
*not* an irrep, so `adjoint_fails_gate` says nothing about it.  Until the
reducible case is covered, "no 3-dimensional object passes the gate" is an
extrapolation from the irreducible case, not a theorem.

## What is proved here

The multiplicity form of the criterion, and the invariant it yields.

Write `W ≅ ⨁_j m_j · V_j`, indexed by `twoJ = 2j` so the arithmetic stays in
`ℕ`.  The count of singlets in `Sym²(W)` is the standard Frobenius–Schur
multiplicity count: each irrep `V_j` carries an invariant bilinear form, which
is **symmetric** when `2j` is even (orthogonal type, `FS = +1`) and
**antisymmetric** when `2j` is odd (symplectic type, `FS = −1`).  A multiplicity
space of dimension `m` therefore contributes its symmetric square
`C(m+1, 2) = m(m+1)/2` in the orthogonal case and its exterior square
`C(m, 2) = m(m−1)/2` in the symplectic case:

    singlets in Sym²(W)  =  Σ_{2j even} C(m_j + 1, 2)  +  Σ_{2j odd} C(m_j, 2)

* `sym2SingletCount_eq_zero_iff` — the gate passes **iff** every
  even-`2j` multiplicity is `0` and every odd-`2j` multiplicity is `≤ 1`.
  So a passing `W` is a sum of *pairwise distinct* even-dimensional irreps.
* `even_dimOfMult_of_gate` — **the invariant.**  A passing `W` has
  **even dimension**, since it is a sum of distinct even numbers.
* `dimOfMult_ne_three_of_gate` — hence no `W` of dimension `3` passes, whether
  or not it is irreducible.
* `gate_fails_of_odd_dim` — the contrapositive, for any odd dimension.

## Why this is the strengthening the chapter needs

`gate_fails_iff_odd_dim` is a statement about the *summands*; parity of
`dim W` is a statement about the *object*, and it is the form the exclusion has
to take to be a scope-(b) invariant in the sense of `AGENTS.md`
§"Before declaring 'refuted'".  With it, the exclusion of the single-fibre
category as a source of the flavour fundamental is complete rather than
extrapolated: **every** object built from one 2-dimensional fibre that passes
the `Sym²` gate has even dimension, and `3` is odd.

`reducible_three_fails_gate` is the concrete witness that this is new content
and not a restatement: a 3-dimensional object that the irrep criterion cannot
reach, and which the multiplicity criterion excludes.

## Why the count has no cross terms

`Sym²(⨁_i m_i V_i)` also contains the mixed pieces `(V_i ⊗ V_j)^{m_i m_j}` for
`i ≠ j`, and each contributes `dim Hom(1, V_i ⊗ V_j) = [V_j ≅ V_i^*]` singlets.
For `SU(2)` every irrep is **self-dual**, so `V_i^* ≅ V_i`, and distinct
summands are by definition non-isomorphic — hence `V_j ≇ V_i^*` and the mixed
pieces contribute **nothing**.  The two-term count above is therefore complete
for `SU(2)`, and it is self-duality that makes it so.  Over a group with a
non-self-dual irrep the cross terms would have to be carried, and the parity
conclusion would not follow.

## Scope

This is the **combinatorial / multiplicity shadow** of the Frobenius–Schur
count, in the same register as its two companion files: the Clebsch–Gordan
decomposition and the `FS = (−1)^{2j}` indicator for `SU(2)` are *cited*
(standard), not formalised — Mathlib has no `SU(2)` representation type.  What
is formalised is the consequence: given that count, the gate forces even
dimension.  The count itself is the model, stated as a definition and labelled
as such.

**Two boundaries, stated so the exclusion is not read wider than it is.**

1. **Multi-fibre structure is untouched.**  Nothing here bears on whether a
   genuinely groupoid-level construction can supply `N = 3`; that remains open
   (`qou-8pl3` Route A).  The result excludes the single-fibre tensor category
   and nothing beyond it — and in that respect it *sharpens* Route A rather
   than competing with it, since the requirement "not a subobject of any
   `V^{⊗n}`" is now proved for arbitrary subobjects and not merely for
   summands.
**A sibling result, resolved the OTHER way — the two are not precedent for each
other.**  `QOU.BraidKnot.HeckeStableScalarCascade` (PR #5766) met the same shape
of question one chapter over: an exclusion stated over *irreducible*
representations, being read as though it covered arbitrary ones.  There the
answer went the opposite direction.  Its load-bearing hypothesis is a
centralizer/Schur condition, which a reducible representation fails outright —
so reducible objects **escape** that exclusion, and `existsNonscalar_heckeGenerators`
exhibits one that does.  Here reducible objects are **also excluded**, because
the multiplicity count reaches them.

The shared lesson is only that an irrep-level criterion does not transfer to
objects without a separate argument.  The *direction* of the resolution is not
shared, so neither file licenses assuming the other's outcome.

2. **Generic `q` only; root-of-unity truncation is NOT covered.**  The count
   uses the classical fusion data, which the Drinfeld–Jimbo quantisation
   preserves at generic `q` (same fusion rules, same orthogonal/symplectic
   type), so it applies to the framework's fibre as long as `q` is generic.  At
   a **root of unity** the category is truncated to the tilting quotient and is
   a different category; whether the same parity argument survives there is
   *not* settled by this file.  That matters, because root-of-unity truncation
   is the chapter's own candidate mechanism (§8, *Truncation mechanism*), so
   this is a live escape route from the exclusion and is named here rather than
   silently closed.

## Base ring (§7c)

Pure combinatorics over `ℕ` — no ring, no ordering beyond `ℕ`, no archimedean
content.

-- Ref: [fulton-harris1991] §11 (Clebsch–Gordan for `sl₂`); the Frobenius–Schur
-- indicator `(−1)^{2j}` for the spin-`j` irrep of `SU(2)`, and the count of
-- invariant bilinear forms on an isotypic component.
-/

namespace QOU.Eightfold.Sym2GateMultiplicity

open Finset

/-! ## 1. Multiplicity data

An object `W ≅ ⨁_j m_j · V_j` is recorded by a finite index set `S` of
occurring values of `twoJ = 2j` together with a multiplicity function `m`. -/

/-- `dim W = Σ_j m_j · (2j + 1)`, since `dim V_j = 2j + 1`. -/
def dimOfMult (S : Finset ℕ) (m : ℕ → ℕ) : ℕ := ∑ j ∈ S, m j * (j + 1)

/-- The number of singlets in `Sym²(W)`, by the Frobenius–Schur count.

An orthogonal irrep (`2j` even, `FS = +1`) has a **symmetric** invariant form,
so its isotypic component contributes `Sym²` of the multiplicity space,
`C(m+1, 2)`.  A symplectic irrep (`2j` odd, `FS = −1`) has an **antisymmetric**
one, contributing `Λ²`, `C(m, 2)`.

This definition *is* the model: the Clebsch–Gordan decomposition and the
indicator are cited from the literature, not derived here. -/
def sym2SingletCount (S : Finset ℕ) (m : ℕ → ℕ) : ℕ :=
  ∑ j ∈ S, if Even j then (m j + 1).choose 2 else (m j).choose 2

/-! ## 2. When a binomial contribution vanishes -/

/-- An orthogonal isotypic component contributes no singlet exactly when it is
absent. -/
theorem choose_two_succ_eq_zero_iff (k : ℕ) : (k + 1).choose 2 = 0 ↔ k = 0 := by
  rw [Nat.choose_eq_zero_iff]; omega

/-- A symplectic isotypic component contributes no singlet exactly when its
multiplicity is at most one — two copies of a symplectic irrep already pair up
to a singlet in `Sym²`. -/
theorem choose_two_eq_zero_iff (k : ℕ) : k.choose 2 = 0 ↔ k ≤ 1 := by
  rw [Nat.choose_eq_zero_iff]; omega

/-! ## 3. The gate criterion in multiplicity form -/

/-- **The gate, for an arbitrary object.**  `Sym²(W)` has no singlet exactly
when `W` contains no orthogonal (odd-dimensional) irrep at all, and contains
each symplectic (even-dimensional) irrep at most once.

Equivalently: a passing `W` is a direct sum of **pairwise distinct
even-dimensional** irreps. -/
theorem sym2SingletCount_eq_zero_iff (S : Finset ℕ) (m : ℕ → ℕ) :
    sym2SingletCount S m = 0 ↔
      ∀ j ∈ S, (Even j → m j = 0) ∧ (¬ Even j → m j ≤ 1) := by
  unfold sym2SingletCount
  rw [Finset.sum_eq_zero_iff]
  constructor
  · intro h j hj
    have hz := h j hj
    refine ⟨fun he => ?_, fun ho => ?_⟩
    · rw [if_pos he] at hz
      exact (choose_two_succ_eq_zero_iff _).mp hz
    · rw [if_neg ho] at hz
      exact (choose_two_eq_zero_iff _).mp hz
  · intro h j hj
    obtain ⟨he, ho⟩ := h j hj
    by_cases hc : Even j
    · rw [if_pos hc, he hc]; decide
    · rw [if_neg hc]
      exact (choose_two_eq_zero_iff _).mpr (ho hc)

/-! ## 4. The invariant: a passing object has even dimension -/

/-- Every term of `dim W` is even once the gate passes: the orthogonal terms
vanish outright, and the symplectic ones carry the even factor `2j + 1` with
`2j` odd. -/
theorem two_dvd_dimOfMult_of_gate {S : Finset ℕ} {m : ℕ → ℕ}
    (h : sym2SingletCount S m = 0) : 2 ∣ dimOfMult S m := by
  unfold dimOfMult
  refine Finset.dvd_sum ?_
  intro j hj
  obtain ⟨he, ho⟩ := (sym2SingletCount_eq_zero_iff S m).mp h j hj
  by_cases hc : Even j
  · rw [he hc]; simp
  · have h2 : 2 ∣ (j + 1) := by
      rcases Nat.even_or_odd j with hE | hO
      · exact absurd hE hc
      · obtain ⟨k, hk⟩ := hO
        exact ⟨k + 1, by omega⟩
    exact h2.mul_left (m j)

/-- **The invariant, stated as parity.**  Any object passing the `Sym²` gate has
even dimension. -/
theorem even_dimOfMult_of_gate {S : Finset ℕ} {m : ℕ → ℕ}
    (h : sym2SingletCount S m = 0) : Even (dimOfMult S m) := by
  obtain ⟨c, hc⟩ := two_dvd_dimOfMult_of_gate h
  exact ⟨c, by omega⟩

/-- **The exclusion the chapter needs.**  No three-dimensional object of the
single-fibre category passes the `Sym²` gate — irreducible or not. -/
theorem dimOfMult_ne_three_of_gate {S : Finset ℕ} {m : ℕ → ℕ}
    (h : sym2SingletCount S m = 0) : dimOfMult S m ≠ 3 := by
  intro hd
  have hev := even_dimOfMult_of_gate h
  rw [hd, Nat.even_iff] at hev
  omega

/-- The contrapositive, for any odd dimension: odd-dimensional objects fail the
gate. -/
theorem gate_fails_of_odd_dim {S : Finset ℕ} {m : ℕ → ℕ}
    (h : Odd (dimOfMult S m)) : sym2SingletCount S m ≠ 0 := by
  intro hz
  have hev := even_dimOfMult_of_gate hz
  rw [Nat.even_iff] at hev
  rw [Nat.odd_iff] at h
  omega

/-! ## 5. Agreement with the irreducible criterion, and the new content -/

/-- The count on a single isotypic component. -/
theorem sym2SingletCount_single (twoJ mult : ℕ) :
    sym2SingletCount {twoJ} (fun _ => mult)
      = if Even twoJ then (mult + 1).choose 2 else mult.choose 2 := by
  simp [sym2SingletCount]

/-- **Consistency with `Sym2GateParity`.**  On a single irrep with multiplicity
one, the multiplicity criterion reproduces
`Sym2GateParity.zero_mem_sym2Indices_iff`: the gate passes exactly when `2j` is
odd, i.e. exactly when `dim V_j` is even.  So this file extends the companion
criterion rather than competing with it. -/
theorem single_irrep_gate_iff_not_even (twoJ : ℕ) :
    sym2SingletCount {twoJ} (fun _ => 1) = 0 ↔ ¬ Even twoJ := by
  rw [sym2SingletCount_single]
  by_cases h : Even twoJ
  · rw [if_pos h]
    exact iff_of_false (by decide) (not_not_intro h)
  · rw [if_neg h]
    exact iff_of_true (by decide) h

/-- **The new content.**  `W = V_{1/2} ⊕ V_0` has dimension `3` and is
**reducible**, so `Sym2GateParity.adjoint_fails_gate` — a statement about a
single irrep — does not apply to it.  It fails the gate all the same: the
trivial summand `V_0` is orthogonal, and its own symmetric square is a singlet.

This is the case the irrep-level argument left open, and the reason the
multiplicity form is needed. -/
theorem reducible_three_dim : dimOfMult {0, 1} (fun _ => 1) = 3 := by decide

theorem reducible_three_fails_gate : sym2SingletCount {0, 1} (fun _ => 1) ≠ 0 := by
  decide

/-- **Even dimension is necessary, not sufficient.**  `W = V_{1/2}^{⊕2}` has
even dimension `4`, yet fails the gate: two copies of a symplectic irrep pair
into a singlet of `Sym²`.  Recorded so the parity invariant is not read as a
characterisation. -/
theorem two_copies_dim_four : dimOfMult {1} (fun _ => 2) = 4 := by decide

theorem two_copies_fails_gate : sym2SingletCount {1} (fun _ => 2) ≠ 0 := by decide

/-- The smallest object that does pass: the 2-dimensional fibre itself,
`W = V_{1/2}`.  Consistent with `Sym2GateParity.fundamental_passes_gate`. -/
theorem fundamental_passes_gate : sym2SingletCount {1} (fun _ => 1) = 0 := by decide

end QOU.Eightfold.Sym2GateMultiplicity
