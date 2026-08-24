/-
# `trM4` cyclicity from the generators alone — no Gram chain

The elements that commute with everything under the trace form a
**subalgebra**: if `x` and `x'` each satisfy `tr(x·y) = tr(y·x)` for all `y`,
then so does `x·x'`, by associativity alone —

    tr((x x') y) = tr(x (x' y)) = tr((x' y) x) = tr(x' (y x))
                 = tr((y x) x') = tr(y (x x'))

So cyclicity has to be checked only on generators. Since every normal-form
basis word is a shorter word times a generator, and the trace is linear,
that single observation replaces the residual finite content the Gram route
leaves behind: the 576 entries `tr(b_i·b_j) = tr(b_j·b_i)` of `gram_symm`,
which cost ~15 GB and over an hour held as one module and is why the ASCII
chain is split across eight.

What is checked here instead is 72 identities — 24 words against each of the
three generators. Each is two rewrites onto an explicit at-most-two-term
vector (`H4WordAction`, `H4GeneratorAction`) followed by `ring` on the
24-entry trace table.

## Provenance

This file and `H4WordAction` were emitted by a generator script rather than
typed by hand. **That emitter was not committed and no longer exists**, so the
checkable form of its provenance claim is
[`computations/h4_cyclicity_generator_route_check.py`](../../../../../../computations/h4_cyclicity_generator_route_check.py),
which re-derives the same content from the same single source of truth.

It *parses* — never transcribes — `mulσ₀/₁/₂` and `TRM4` out of
`HeckeH4StabilizationRung` and the 24 words out of `wordAction`, then checks:
the Hecke presentation re-derived from the parsed actions alone; all 72
identities symbolically over `ℚ[z, h]`; the structural fact the induction rests
on — for every tree edge `σᵢ · b_inner = b_j` on the nose, a single term with no
quadratic fold, so `b_j = b_inner · σᵢ` really is a shorter word times a
generator (23 edges); and the 72 `mulσᵢ_e₄_j` statements of `H4GeneratorAction`
re-checked against the parsed tables.

What that adds is narrow, and worth stating: Lean already machine-checks every
statement here, so the script cannot make the theorem more true. It checks the
layer Lean cannot see — that the committed statements are *about* the tables
these modules claim to be about, computed by an independent implementation. A
sorry-free file enumerating the wrong 72 facts is the failure mode it closes.

## Relation to the route this replaced

The ASCII basis carried the only `n = 4` cyclicity proof, `trM_cyclic`, off
`gram_symm`'s 576 computed entries in `MarkovTraceH4Gram0..7`. `H4BasisBridge`
then transported it to the subscript basis, so the Gram chain — 6604 generated
lines and the tree's build pole — was load-bearing.

This file proves the subscript statement directly and imports none of it, which
**reverses that arrow**: the bridge now derives the ASCII `trM_cyclic` from
`trM4_cyclic` here, and the Gram chain is deleted.
-/
import QOU.Machinery.H4WordAction

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-! ## The three generators, as word actions

`b_1 = σ₀`, `b_2 = σ₁`, `b_6 = σ₂`; each is definitionally its own generator
action. -/

theorem wordAction_gen₀ (h : R) (u : Fin 24 → R) :
    wordAction h (1 : Fin 24) u = mulσ₀ h u := rfl

theorem wordAction_gen₁ (h : R) (u : Fin 24 → R) :
    wordAction h (2 : Fin 24) u = mulσ₁ h u := rfl

theorem wordAction_gen₂ (h : R) (u : Fin 24 → R) :
    wordAction h (6 : Fin 24) u = mulσ₂ h u := rfl

/-- `trM4` commutes with finite sums — the form the basis expansion needs. -/
theorem trM4_sum (z h : R) (s : Finset (Fin 24)) (f : Fin 24 → (Fin 24 → R)) :
    trM4 z h (∑ j ∈ s, f j) = ∑ j ∈ s, trM4 z h (f j) := by
  induction s using Finset.induction with
  | empty => simp [trM4]
  | @insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, trM4_add, ih]


/-! ## Every basis word is a shorter word times a generator

`b_j = b_inner · σᵢ`, on the nose — the product never folds. -/

theorem e₄_zero_eq_unit : e₄ (0 : Fin 24) = (unitNF₄ : Fin 24 → R) := by
  funext i; fin_cases i <;> simp [e₄, unitNF₄]

theorem e₄_eq_mul_1 (h : R) :
    e₄ (1 : Fin 24) = mulNF₄ h (e₄ (0 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_0]

theorem e₄_eq_mul_2 (h : R) :
    e₄ (2 : Fin 24) = mulNF₄ h (e₄ (0 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_0]

theorem e₄_eq_mul_3 (h : R) :
    e₄ (3 : Fin 24) = mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_2]

theorem e₄_eq_mul_4 (h : R) :
    e₄ (4 : Fin 24) = mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_1]

theorem e₄_eq_mul_5 (h : R) :
    e₄ (5 : Fin 24) = mulNF₄ h (e₄ (4 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_4]

theorem e₄_eq_mul_6 (h : R) :
    e₄ (6 : Fin 24) = mulNF₄ h (e₄ (0 : Fin 24)) (e₄ (6 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₂, mulσ₂_e₄_0]

theorem e₄_eq_mul_7 (h : R) :
    e₄ (7 : Fin 24) = mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (6 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₂, mulσ₂_e₄_2]

theorem e₄_eq_mul_8 (h : R) :
    e₄ (8 : Fin 24) = mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_6]

theorem e₄_eq_mul_9 (h : R) :
    e₄ (9 : Fin 24) = mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_6]

theorem e₄_eq_mul_10 (h : R) :
    e₄ (10 : Fin 24) = mulNF₄ h (e₄ (4 : Fin 24)) (e₄ (6 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₂, mulσ₂_e₄_4]

theorem e₄_eq_mul_11 (h : R) :
    e₄ (11 : Fin 24) = mulNF₄ h (e₄ (3 : Fin 24)) (e₄ (6 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₂, mulσ₂_e₄_3]

theorem e₄_eq_mul_12 (h : R) :
    e₄ (12 : Fin 24) = mulNF₄ h (e₄ (7 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_7]

theorem e₄_eq_mul_13 (h : R) :
    e₄ (13 : Fin 24) = mulNF₄ h (e₄ (8 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_8]

theorem e₄_eq_mul_14 (h : R) :
    e₄ (14 : Fin 24) = mulNF₄ h (e₄ (9 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_9]

theorem e₄_eq_mul_15 (h : R) :
    e₄ (15 : Fin 24) = mulNF₄ h (e₄ (5 : Fin 24)) (e₄ (6 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₂, mulσ₂_e₄_5]

theorem e₄_eq_mul_16 (h : R) :
    e₄ (16 : Fin 24) = mulNF₄ h (e₄ (10 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_10]

theorem e₄_eq_mul_17 (h : R) :
    e₄ (17 : Fin 24) = mulNF₄ h (e₄ (11 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_11]

theorem e₄_eq_mul_18 (h : R) :
    e₄ (18 : Fin 24) = mulNF₄ h (e₄ (12 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_12]

theorem e₄_eq_mul_19 (h : R) :
    e₄ (19 : Fin 24) = mulNF₄ h (e₄ (13 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_13]

theorem e₄_eq_mul_20 (h : R) :
    e₄ (20 : Fin 24) = mulNF₄ h (e₄ (15 : Fin 24)) (e₄ (2 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₁, mulσ₁_e₄_15]

theorem e₄_eq_mul_21 (h : R) :
    e₄ (21 : Fin 24) = mulNF₄ h (e₄ (16 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_16]

theorem e₄_eq_mul_22 (h : R) :
    e₄ (22 : Fin 24) = mulNF₄ h (e₄ (17 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_17]

theorem e₄_eq_mul_23 (h : R) :
    e₄ (23 : Fin 24) = mulNF₄ h (e₄ (20 : Fin 24)) (e₄ (1 : Fin 24)) := by
  rw [mulNF₄_e_right, wordAction_gen₀, mulσ₀_e₄_20]

/-! ## The 72 generator identities

`tr(b_g · b_j) = tr(b_j · b_g)` for each word `j` and generator `g`.

**Diagonal entries are absent by design** (removed 2026-08-21; vacuity
ledger, `proof-no-trivial-true` / `reflexive-tautology`).  At `j = g` the
cyclicity instance degenerates to `tr(b_g · b_g) = tr(b_g · b_g)` — the two
sides are *syntactically* identical, so `trM4_cyc_1_1`, `trM4_cyc_2_2` and
`trM4_cyc_6_6` were `X = X := rfl`, asserting nothing falsifiable while
reading, from their names, like three more entries of a proved table.  The
`traceCentral_e₄_*` case splits that consumed them now discharge those
branches with `rfl` inline, where the triviality is visible at the point of
use.  The table's real content is the off-diagonal cases. -/

theorem trM4_cyc_0_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (0 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (0 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_0_1, wordAction_gen₀,
    mulσ₀_e₄_0]

theorem trM4_cyc_2_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (2 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_2_1, wordAction_gen₀,
    mulσ₀_e₄_2]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_3_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (3 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (3 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_3_1, wordAction_gen₀,
    mulσ₀_e₄_3]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_4_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (4 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (4 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_4_1, wordAction_gen₀,
    mulσ₀_e₄_4]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_5_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (5 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (5 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_5_1, wordAction_gen₀,
    mulσ₀_e₄_5]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_6_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (6 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_6_1, wordAction_gen₀,
    mulσ₀_e₄_6]

theorem trM4_cyc_7_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (7 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (7 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_7_1, wordAction_gen₀,
    mulσ₀_e₄_7]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_8_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (8 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (8 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_8_1, wordAction_gen₀,
    mulσ₀_e₄_8]

theorem trM4_cyc_9_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (9 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (9 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_9_1, wordAction_gen₀,
    mulσ₀_e₄_9]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_10_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (10 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (10 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_10_1, wordAction_gen₀,
    mulσ₀_e₄_10]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_11_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (11 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (11 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_11_1, wordAction_gen₀,
    mulσ₀_e₄_11]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_12_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (12 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (12 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_12_1, wordAction_gen₀,
    mulσ₀_e₄_12]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_13_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (13 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (13 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_13_1, wordAction_gen₀,
    mulσ₀_e₄_13]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_14_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (14 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (14 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_14_1, wordAction_gen₀,
    mulσ₀_e₄_14]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_15_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (15 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (15 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_15_1, wordAction_gen₀,
    mulσ₀_e₄_15]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_16_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (16 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (16 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_16_1, wordAction_gen₀,
    mulσ₀_e₄_16]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_17_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (17 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (17 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_17_1, wordAction_gen₀,
    mulσ₀_e₄_17]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_18_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (18 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (18 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_18_1, wordAction_gen₀,
    mulσ₀_e₄_18]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_19_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (19 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (19 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_19_1, wordAction_gen₀,
    mulσ₀_e₄_19]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_20_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (20 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (20 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_20_1, wordAction_gen₀,
    mulσ₀_e₄_20]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_21_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (21 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (21 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_21_1, wordAction_gen₀,
    mulσ₀_e₄_21]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_22_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (22 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (22 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_22_1, wordAction_gen₀,
    mulσ₀_e₄_22]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_23_1 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (23 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (23 : Fin 24)) (e₄ (1 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_23_1, wordAction_gen₀,
    mulσ₀_e₄_23]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_0_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (0 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (0 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_0_2, wordAction_gen₁,
    mulσ₁_e₄_0]

theorem trM4_cyc_1_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (1 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_1_2, wordAction_gen₁,
    mulσ₁_e₄_1]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_3_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (3 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (3 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_3_2, wordAction_gen₁,
    mulσ₁_e₄_3]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_4_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (4 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (4 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_4_2, wordAction_gen₁,
    mulσ₁_e₄_4]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_5_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (5 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (5 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_5_2, wordAction_gen₁,
    mulσ₁_e₄_5]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_6_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (6 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_6_2, wordAction_gen₁,
    mulσ₁_e₄_6]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_7_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (7 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (7 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_7_2, wordAction_gen₁,
    mulσ₁_e₄_7]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_8_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (8 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (8 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_8_2, wordAction_gen₁,
    mulσ₁_e₄_8]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_9_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (9 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (9 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_9_2, wordAction_gen₁,
    mulσ₁_e₄_9]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_10_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (10 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (10 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_10_2, wordAction_gen₁,
    mulσ₁_e₄_10]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_11_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (11 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (11 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_11_2, wordAction_gen₁,
    mulσ₁_e₄_11]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_12_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (12 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (12 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_12_2, wordAction_gen₁,
    mulσ₁_e₄_12]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_13_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (13 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (13 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_13_2, wordAction_gen₁,
    mulσ₁_e₄_13]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_14_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (14 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (14 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_14_2, wordAction_gen₁,
    mulσ₁_e₄_14]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_15_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (15 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (15 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_15_2, wordAction_gen₁,
    mulσ₁_e₄_15]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_16_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (16 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (16 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_16_2, wordAction_gen₁,
    mulσ₁_e₄_16]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_17_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (17 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (17 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_17_2, wordAction_gen₁,
    mulσ₁_e₄_17]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_18_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (18 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (18 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_18_2, wordAction_gen₁,
    mulσ₁_e₄_18]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_19_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (19 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (19 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_19_2, wordAction_gen₁,
    mulσ₁_e₄_19]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_20_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (20 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (20 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_20_2, wordAction_gen₁,
    mulσ₁_e₄_20]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_21_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (21 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (21 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_21_2, wordAction_gen₁,
    mulσ₁_e₄_21]

theorem trM4_cyc_22_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (22 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (22 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_22_2, wordAction_gen₁,
    mulσ₁_e₄_22]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_23_2 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (23 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (23 : Fin 24)) (e₄ (2 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_23_2, wordAction_gen₁,
    mulσ₁_e₄_23]

theorem trM4_cyc_0_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (0 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (0 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_0_6, wordAction_gen₂,
    mulσ₂_e₄_0]

theorem trM4_cyc_1_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (1 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (1 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_1_6, wordAction_gen₂,
    mulσ₂_e₄_1]

theorem trM4_cyc_2_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (2 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (2 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_2_6, wordAction_gen₂,
    mulσ₂_e₄_2]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_3_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (3 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (3 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_3_6, wordAction_gen₂,
    mulσ₂_e₄_3]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_4_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (4 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (4 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_4_6, wordAction_gen₂,
    mulσ₂_e₄_4]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_5_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (5 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (5 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_5_6, wordAction_gen₂,
    mulσ₂_e₄_5]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_7_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (7 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (7 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_7_6, wordAction_gen₂,
    mulσ₂_e₄_7]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_8_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (8 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (8 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_8_6, wordAction_gen₂,
    mulσ₂_e₄_8]

theorem trM4_cyc_9_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (9 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (9 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_9_6, wordAction_gen₂,
    mulσ₂_e₄_9]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_10_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (10 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (10 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_10_6, wordAction_gen₂,
    mulσ₂_e₄_10]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_11_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (11 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (11 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_11_6, wordAction_gen₂,
    mulσ₂_e₄_11]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_12_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (12 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (12 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_12_6, wordAction_gen₂,
    mulσ₂_e₄_12]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_13_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (13 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (13 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_13_6, wordAction_gen₂,
    mulσ₂_e₄_13]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_14_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (14 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (14 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_14_6, wordAction_gen₂,
    mulσ₂_e₄_14]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_15_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (15 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (15 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_15_6, wordAction_gen₂,
    mulσ₂_e₄_15]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_16_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (16 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (16 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_16_6, wordAction_gen₂,
    mulσ₂_e₄_16]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_17_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (17 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (17 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_17_6, wordAction_gen₂,
    mulσ₂_e₄_17]
  simp [trM4_e₄', TRM4]

theorem trM4_cyc_18_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (18 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (18 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_18_6, wordAction_gen₂,
    mulσ₂_e₄_18]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_19_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (19 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (19 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_19_6, wordAction_gen₂,
    mulσ₂_e₄_19]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_20_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (20 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (20 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_20_6, wordAction_gen₂,
    mulσ₂_e₄_20]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_21_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (21 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (21 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_21_6, wordAction_gen₂,
    mulσ₂_e₄_21]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]

theorem trM4_cyc_22_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (22 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (22 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_22_6, wordAction_gen₂,
    mulσ₂_e₄_22]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]
  ring

theorem trM4_cyc_23_6 (z h : R) :
    trM4 z h (mulNF₄ h (e₄ (6 : Fin 24)) (e₄ (23 : Fin 24)))
      = trM4 z h (mulNF₄ h (e₄ (23 : Fin 24)) (e₄ (6 : Fin 24))) := by
  rw [mulNF₄_e_right, mulNF₄_e_right, wordAction_e₄_23_6, wordAction_gen₂,
    mulσ₂_e₄_23]
  simp [trM4_add, trM4_smul, trM4_e₄', TRM4]


/-! ## Trace-centrality is a subalgebra -/

/-- `x` commutes with everything under the Markov trace. -/
def TraceCentral (z h : R) (x : Fin 24 → R) : Prop :=
  ∀ y, trM4 z h (mulNF₄ h x y) = trM4 z h (mulNF₄ h y x)

theorem traceCentral_zero (z h : R) : TraceCentral z h (0 : Fin 24 → R) := by
  intro y; rw [mulNF₄_zero_left, mulNF₄_zero_right]

theorem traceCentral_add {z h : R} {x x' : Fin 24 → R}
    (hx : TraceCentral z h x) (hx' : TraceCentral z h x') :
    TraceCentral z h (x + x') := by
  intro y
  rw [mulNF₄_add_left, mulNF₄_add_right, trM4_add, trM4_add, hx y, hx' y]

theorem traceCentral_smul {z h : R} {x : Fin 24 → R} (c : R)
    (hx : TraceCentral z h x) : TraceCentral z h (c • x) := by
  intro y
  rw [mulNF₄_smul_left, mulNF₄_smul_right, trM4_smul, trM4_smul, hx y]

/-- **The subalgebra step.** Associativity alone; no table, no basis. -/
theorem traceCentral_mul {z h : R} {x x' : Fin 24 → R}
    (hx : TraceCentral z h x) (hx' : TraceCentral z h x') :
    TraceCentral z h (mulNF₄ h x x') := by
  intro y
  rw [mulNF₄_assoc, hx (mulNF₄ h x' y), mulNF₄_assoc, hx' (mulNF₄ h y x),
    mulNF₄_assoc]

theorem traceCentral_sum (z h : R) (s : Finset (Fin 24)) (f : Fin 24 → (Fin 24 → R))
    (hf : ∀ j ∈ s, TraceCentral z h (f j)) : TraceCentral z h (∑ j ∈ s, f j) := by
  induction s using Finset.induction with
  | empty => simpa using traceCentral_zero z h
  | @insert a s ha ih =>
      rw [Finset.sum_insert ha]
      exact traceCentral_add (hf a (by simp)) (ih fun j hj => hf j (by simp [hj]))

/-- Linearity in the second argument: centrality need only be tested on the
basis. -/
theorem traceCentral_of_basis (z h : R) (x : Fin 24 → R)
    (hb : ∀ j, trM4 z h (mulNF₄ h x (e₄ j)) = trM4 z h (mulNF₄ h (e₄ j) x)) :
    TraceCentral z h x := by
  intro y
  conv_lhs => rw [basis_decomp₄ y]
  conv_rhs => rw [basis_decomp₄ y]
  rw [mulNF₄_sum_right, mulNF₄_sum_left, trM4_sum, trM4_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [mulNF₄_smul_right, mulNF₄_smul_left, trM4_smul, trM4_smul, hb j]


/-! ## Every basis word is trace-central -/

theorem traceCentral_e₄_1 (z h : R) : TraceCentral z h (e₄ (1 : Fin 24)) := by
  refine traceCentral_of_basis z h _ fun j => ?_
  fin_cases j
  · exact trM4_cyc_0_1 z h
  · rfl  -- diagonal j = 1: LHS ≡ RHS, no content (see note above)
  · exact trM4_cyc_2_1 z h
  · exact trM4_cyc_3_1 z h
  · exact trM4_cyc_4_1 z h
  · exact trM4_cyc_5_1 z h
  · exact trM4_cyc_6_1 z h
  · exact trM4_cyc_7_1 z h
  · exact trM4_cyc_8_1 z h
  · exact trM4_cyc_9_1 z h
  · exact trM4_cyc_10_1 z h
  · exact trM4_cyc_11_1 z h
  · exact trM4_cyc_12_1 z h
  · exact trM4_cyc_13_1 z h
  · exact trM4_cyc_14_1 z h
  · exact trM4_cyc_15_1 z h
  · exact trM4_cyc_16_1 z h
  · exact trM4_cyc_17_1 z h
  · exact trM4_cyc_18_1 z h
  · exact trM4_cyc_19_1 z h
  · exact trM4_cyc_20_1 z h
  · exact trM4_cyc_21_1 z h
  · exact trM4_cyc_22_1 z h
  · exact trM4_cyc_23_1 z h

theorem traceCentral_e₄_2 (z h : R) : TraceCentral z h (e₄ (2 : Fin 24)) := by
  refine traceCentral_of_basis z h _ fun j => ?_
  fin_cases j
  · exact trM4_cyc_0_2 z h
  · exact trM4_cyc_1_2 z h
  · rfl  -- diagonal j = 2: LHS ≡ RHS, no content (see note above)
  · exact trM4_cyc_3_2 z h
  · exact trM4_cyc_4_2 z h
  · exact trM4_cyc_5_2 z h
  · exact trM4_cyc_6_2 z h
  · exact trM4_cyc_7_2 z h
  · exact trM4_cyc_8_2 z h
  · exact trM4_cyc_9_2 z h
  · exact trM4_cyc_10_2 z h
  · exact trM4_cyc_11_2 z h
  · exact trM4_cyc_12_2 z h
  · exact trM4_cyc_13_2 z h
  · exact trM4_cyc_14_2 z h
  · exact trM4_cyc_15_2 z h
  · exact trM4_cyc_16_2 z h
  · exact trM4_cyc_17_2 z h
  · exact trM4_cyc_18_2 z h
  · exact trM4_cyc_19_2 z h
  · exact trM4_cyc_20_2 z h
  · exact trM4_cyc_21_2 z h
  · exact trM4_cyc_22_2 z h
  · exact trM4_cyc_23_2 z h

theorem traceCentral_e₄_6 (z h : R) : TraceCentral z h (e₄ (6 : Fin 24)) := by
  refine traceCentral_of_basis z h _ fun j => ?_
  fin_cases j
  · exact trM4_cyc_0_6 z h
  · exact trM4_cyc_1_6 z h
  · exact trM4_cyc_2_6 z h
  · exact trM4_cyc_3_6 z h
  · exact trM4_cyc_4_6 z h
  · exact trM4_cyc_5_6 z h
  · rfl  -- diagonal j = 6: LHS ≡ RHS, no content (see note above)
  · exact trM4_cyc_7_6 z h
  · exact trM4_cyc_8_6 z h
  · exact trM4_cyc_9_6 z h
  · exact trM4_cyc_10_6 z h
  · exact trM4_cyc_11_6 z h
  · exact trM4_cyc_12_6 z h
  · exact trM4_cyc_13_6 z h
  · exact trM4_cyc_14_6 z h
  · exact trM4_cyc_15_6 z h
  · exact trM4_cyc_16_6 z h
  · exact trM4_cyc_17_6 z h
  · exact trM4_cyc_18_6 z h
  · exact trM4_cyc_19_6 z h
  · exact trM4_cyc_20_6 z h
  · exact trM4_cyc_21_6 z h
  · exact trM4_cyc_22_6 z h
  · exact trM4_cyc_23_6 z h

theorem traceCentral_e₄_0 (z h : R) : TraceCentral z h (e₄ (0 : Fin 24)) := by
  rw [e₄_zero_eq_unit]
  intro y; rw [mulNF₄_one_left, mulNF₄_one_right]

theorem traceCentral_e₄_3 (z h : R) : TraceCentral z h (e₄ (3 : Fin 24)) := by
  rw [e₄_eq_mul_3 h]
  exact traceCentral_mul (traceCentral_e₄_2 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_4 (z h : R) : TraceCentral z h (e₄ (4 : Fin 24)) := by
  rw [e₄_eq_mul_4 h]
  exact traceCentral_mul (traceCentral_e₄_1 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_5 (z h : R) : TraceCentral z h (e₄ (5 : Fin 24)) := by
  rw [e₄_eq_mul_5 h]
  exact traceCentral_mul (traceCentral_e₄_4 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_7 (z h : R) : TraceCentral z h (e₄ (7 : Fin 24)) := by
  rw [e₄_eq_mul_7 h]
  exact traceCentral_mul (traceCentral_e₄_2 z h) (traceCentral_e₄_6 z h)

theorem traceCentral_e₄_8 (z h : R) : TraceCentral z h (e₄ (8 : Fin 24)) := by
  rw [e₄_eq_mul_8 h]
  exact traceCentral_mul (traceCentral_e₄_6 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_9 (z h : R) : TraceCentral z h (e₄ (9 : Fin 24)) := by
  rw [e₄_eq_mul_9 h]
  exact traceCentral_mul (traceCentral_e₄_6 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_10 (z h : R) : TraceCentral z h (e₄ (10 : Fin 24)) := by
  rw [e₄_eq_mul_10 h]
  exact traceCentral_mul (traceCentral_e₄_4 z h) (traceCentral_e₄_6 z h)

theorem traceCentral_e₄_11 (z h : R) : TraceCentral z h (e₄ (11 : Fin 24)) := by
  rw [e₄_eq_mul_11 h]
  exact traceCentral_mul (traceCentral_e₄_3 z h) (traceCentral_e₄_6 z h)

theorem traceCentral_e₄_12 (z h : R) : TraceCentral z h (e₄ (12 : Fin 24)) := by
  rw [e₄_eq_mul_12 h]
  exact traceCentral_mul (traceCentral_e₄_7 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_13 (z h : R) : TraceCentral z h (e₄ (13 : Fin 24)) := by
  rw [e₄_eq_mul_13 h]
  exact traceCentral_mul (traceCentral_e₄_8 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_14 (z h : R) : TraceCentral z h (e₄ (14 : Fin 24)) := by
  rw [e₄_eq_mul_14 h]
  exact traceCentral_mul (traceCentral_e₄_9 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_15 (z h : R) : TraceCentral z h (e₄ (15 : Fin 24)) := by
  rw [e₄_eq_mul_15 h]
  exact traceCentral_mul (traceCentral_e₄_5 z h) (traceCentral_e₄_6 z h)

theorem traceCentral_e₄_16 (z h : R) : TraceCentral z h (e₄ (16 : Fin 24)) := by
  rw [e₄_eq_mul_16 h]
  exact traceCentral_mul (traceCentral_e₄_10 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_17 (z h : R) : TraceCentral z h (e₄ (17 : Fin 24)) := by
  rw [e₄_eq_mul_17 h]
  exact traceCentral_mul (traceCentral_e₄_11 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_18 (z h : R) : TraceCentral z h (e₄ (18 : Fin 24)) := by
  rw [e₄_eq_mul_18 h]
  exact traceCentral_mul (traceCentral_e₄_12 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_19 (z h : R) : TraceCentral z h (e₄ (19 : Fin 24)) := by
  rw [e₄_eq_mul_19 h]
  exact traceCentral_mul (traceCentral_e₄_13 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_20 (z h : R) : TraceCentral z h (e₄ (20 : Fin 24)) := by
  rw [e₄_eq_mul_20 h]
  exact traceCentral_mul (traceCentral_e₄_15 z h) (traceCentral_e₄_2 z h)

theorem traceCentral_e₄_21 (z h : R) : TraceCentral z h (e₄ (21 : Fin 24)) := by
  rw [e₄_eq_mul_21 h]
  exact traceCentral_mul (traceCentral_e₄_16 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_22 (z h : R) : TraceCentral z h (e₄ (22 : Fin 24)) := by
  rw [e₄_eq_mul_22 h]
  exact traceCentral_mul (traceCentral_e₄_17 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄_23 (z h : R) : TraceCentral z h (e₄ (23 : Fin 24)) := by
  rw [e₄_eq_mul_23 h]
  exact traceCentral_mul (traceCentral_e₄_20 z h) (traceCentral_e₄_1 z h)

theorem traceCentral_e₄ (z h : R) (j : Fin 24) : TraceCentral z h (e₄ j) := by
  fin_cases j
  · exact traceCentral_e₄_0 z h
  · exact traceCentral_e₄_1 z h
  · exact traceCentral_e₄_2 z h
  · exact traceCentral_e₄_3 z h
  · exact traceCentral_e₄_4 z h
  · exact traceCentral_e₄_5 z h
  · exact traceCentral_e₄_6 z h
  · exact traceCentral_e₄_7 z h
  · exact traceCentral_e₄_8 z h
  · exact traceCentral_e₄_9 z h
  · exact traceCentral_e₄_10 z h
  · exact traceCentral_e₄_11 z h
  · exact traceCentral_e₄_12 z h
  · exact traceCentral_e₄_13 z h
  · exact traceCentral_e₄_14 z h
  · exact traceCentral_e₄_15 z h
  · exact traceCentral_e₄_16 z h
  · exact traceCentral_e₄_17 z h
  · exact traceCentral_e₄_18 z h
  · exact traceCentral_e₄_19 z h
  · exact traceCentral_e₄_20 z h
  · exact traceCentral_e₄_21 z h
  · exact traceCentral_e₄_22 z h
  · exact traceCentral_e₄_23 z h

/-- Everything is trace-central: expand in the basis. -/
theorem traceCentral_all (z h : R) (x : Fin 24 → R) : TraceCentral z h x := by
  rw [basis_decomp₄ x]
  exact traceCentral_sum z h _ _ fun j _ => traceCentral_smul _ (traceCentral_e₄ z h j)

/-- **(M2) Cyclicity of the level-4 Markov trace**, from the three
generators and associativity — no Gram matrix. -/
theorem trM4_cyclic (z h : R) (u v : Fin 24 → R) :
    trM4 z h (mulNF₄ h u v) = trM4 z h (mulNF₄ h v u) :=
  traceCentral_all z h u v


end QOU.Machinery.H4
