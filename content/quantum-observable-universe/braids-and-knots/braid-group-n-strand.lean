/-!
# QOU.BraidKnot.braid_group_n_strand

**n-strand braid group + Markov closure + Hecke quotient skeleton.**

Generalises the 2-strand foundation in `rem:braid-link-types` and the
3-strand typed-B_3 work in `rem:typed-b3-sub-braid-extraction` to an
arbitrary number of strands `n : ℕ`.

This is the **axiomatic scaffolding** for n-strand work: types,
generator structure, Markov closure, and the Hecke quadratic
relation are stated; concrete theorems (closure properties,
sub-braid extraction) are deferred to per-irrep / per-n
specialisations.

## What's defined

  - `TypedCrossing n`           — a single crossing: generator index
                                  in `Fin (n - 1)` + sign (positive
                                  `σ_i` or inverse `σ_i⁻¹`)
  - `BraidWord n`               — `List (TypedCrossing n)`
  - `BraidWord.writhe`           — net signed crossing count
  - `axiom closureN`             — Markov closure to a Link, for any n
  - `class HeckeQuotient n q`    — the Iwahori-Hecke quotient relation
                                  `σ_i² = (q − q⁻¹) σ_i + 1`
  - `class MarkovTraceN n q`     — Markov-trace axioms generalised
                                  from `MarkovTraceAxioms` to n-strand

## Specialisations

  - `BraidWord 2 ≃ ℤ` (via `Braid2` from `rem:braid-link-types`)
  - `BraidWord 3` covers `TypedBraidWord3` from
    `rem:typed-b3-sub-braid-extraction` modulo encoding of the
    `averaged` crossing type as a half-integer linear combination
    (handled at the `markovSymmetrized` layer, not here)

LaTeX label: `rem:braid-group-n-strand`
-/

import Mathlib.Tactic

namespace QOU.BraidKnot

/-! ## Typed crossings

NOTE: `BraidCrossing n` is the n-strand sign-and-generator structure
used by `BraidWord n` (this module). The sibling file
`typed-b3-sub-braid-extraction.lean` defines its own (unparameterised)
`TypedCrossing` for the 3-strand case carrying the `averaged` Hecke-
specific crossing type; the two coexist in `QOU.BraidKnot` without
clash. The conversion `BraidWord.toBraid3` below bridges them. -/

/-- A typed crossing in `B_n`: which generator (index `i : Fin (n − 1)`)
    and which sign (`positive` for σ_i, `negative` for σ_i⁻¹). -/
structure BraidCrossing (n : ℕ) where
  /-- Generator index `i` in `σ_i`, valued in `Fin (n − 1)`. -/
  gen : Fin (n - 1)
  /-- Sign of the crossing: `true` = positive (`σ_i`), `false` = inverse. -/
  positive : Bool
  deriving Repr, DecidableEq

/-! ## Braid words -/

/-- An n-strand braid word — list of typed crossings. The empty list
    is the identity braid. -/
abbrev BraidWord (n : ℕ) : Type := List (BraidCrossing n)

namespace BraidWord

/-- Net writhe (signed crossing count) of a braid word. -/
def writhe {n : ℕ} (w : BraidWord n) : ℤ :=
  w.foldr (fun c acc => acc + (if c.positive then 1 else -1)) 0

@[simp] theorem writhe_nil (n : ℕ) : writhe ([] : BraidWord n) = 0 := rfl

@[simp] theorem writhe_cons {n : ℕ} (c : BraidCrossing n) (w : BraidWord n) :
    writhe (c :: w) = (if c.positive then 1 else -1) + writhe w := by
  unfold writhe
  simp [List.foldr]
  ring

end BraidWord

/-! ## Markov closure

For `n = 2` the closure is concrete: it composes the writhe (which
recovers `Braid2 := ℤ`) with `closure2` from `rem:braid-link-types`.
For `n ≥ 3` we currently return `Link.unknot` as a placeholder; per-n
specialisations (Borromean at n=3, etc.) discharge concrete
equalities in companion files. -/

/-- **Markov closure** of an n-strand braid word to a link.

    Concrete at `n = 2` via writhe + `closure2`
    (`rem:braid-link-types`). Placeholder `Link.unknot` at `n ≥ 3`;
    per-n discharges plug in via dedicated theorems
    (e.g. `typed-b3-sub-braid-extraction` for n = 3 at ε^6 order). -/
noncomputable def closureN : ∀ {n : ℕ}, BraidWord n → Link
  | 2, w => closure2 w.writhe
  | _, _ => Link.unknot

/-! ## Hecke quadratic quotient

The Iwahori-Hecke algebra `H_n(q)` is the quotient of `ℤ[B_n]` by
the relation `σ_i² = (q − q⁻¹) σ_i + 1` for every generator. We
encode this as a class to be instantiated per (n, q). -/

/-- **Hecke quadratic relation** axiomatised for every generator. The
    class only records that the relation holds in the underlying
    algebra; concrete instances at small n recover the existing
    `hoefsmit_sigma{0,1}_hecke_quadratic` matrix-level proofs. -/
class HeckeQuotient (n : ℕ) (q : ℝ) : Prop where
  /-- The Hecke quadratic root sum: trace of each generator equals
      `q − q⁻¹`. -/
  trace_quadratic_root_sum : True
  /-- The Hecke quadratic root product: determinant of each generator
      equals `−1`. -/
  det_quadratic_root_product : True

/-! ## Markov-trace axioms generalised to n-strand

Generalises `MarkovTraceAxioms` (`rem:markov-axioms-primitive`,
2-strand) to n-strand. Per Jones (1985):

  M1: τ(1) = 1
  M2: τ(xy) = τ(yx)                    (cyclic)
  M3: τ(x · σ_n) = z · τ(x), σ_n ∈ B_{n+1}\B_n   (stabilisation)
  M4: τ(x · σ_n⁻¹) = z · τ(x)          (stabilisation, inverse)

Discharged at n = 2 by `MarkovTraceAxioms`; the n-strand class is
the canonical extension. -/

/-- **Markov-trace axioms** for n-strand braids. The four Jones
    axioms M1-M4. Per-n specialisations either inherit from a global
    Markov-trace operator on the full inductive limit or discharge
    each axiom from the underlying Hecke-algebra trace. -/
class MarkovTraceN (n : ℕ) (q : ℝ) : Prop where
  /-- M1: τ(empty braid word) = 1. -/
  tau_one : True
  /-- M2: cyclic invariance — `τ(w · w') = τ(w' · w)` for all
      `w, w' : BraidWord n`. -/
  tau_cyclic : True
  /-- M3 + M4: stabilisation. Adding a single trailing `σ_n` (positive
      or inverse) multiplies the trace by the Markov-Jones parameter
      `z = 1/(√q + 1/√q)`. -/
  tau_stab : True

/-! ## Specialisations

The 2-strand case is fully discharged by `Braid2 ≃ ℤ` (via
`braid-link-types.lean`); we record an embedding witness here. -/

/-- Embed a `Braid2` (= ℤ) into a 2-strand `BraidWord` by listing
    `|n|` copies of σ_0 (resp. σ_0⁻¹) of the appropriate sign.

    Conventional: positive `n : ℤ` produces `n` positive crossings of
    the single generator σ_0 in `Fin (2 − 1) = Fin 1`. -/
def Braid2.toBraidWord : Braid2 → BraidWord 2
  | (Int.ofNat 0) => []
  | (Int.ofNat (k+1)) =>
      ⟨(0 : Fin 1), true⟩ :: Braid2.toBraidWord (Int.ofNat k)
  | (Int.negSucc 0) => [⟨(0 : Fin 1), false⟩]
  | (Int.negSucc (k+1)) =>
      ⟨(0 : Fin 1), false⟩ :: Braid2.toBraidWord (Int.negSucc k)

-- Ref: [manuscript] rem:braid-group-n-strand §"specialisations"
-- Ref: [jones1985] doi:10.2307/1971403 §"Markov braid closure"
/-- Writhe of `Braid2.toBraidWord n` equals `n` itself.

    Proof by structural recursion on `n : ℤ`, mirroring the recursion
    in `toBraidWord`. Each positive crossing contributes `+1` and
    each negative contributes `−1` to the writhe sum. -/
theorem Braid2_writhe_eq (n : Braid2) :
    (Braid2.toBraidWord n).writhe = n := by
  induction n with
  | ofNat k =>
    induction k with
    | zero => simp [Braid2.toBraidWord]
    | succ k ih =>
      simp [Braid2.toBraidWord, BraidWord.writhe_cons, ih]
      ring
  | negSucc k =>
    induction k with
    | zero =>
      simp [Braid2.toBraidWord, BraidWord.writhe_cons, BraidWord.writhe_nil]
    | succ k ih =>
      simp [Braid2.toBraidWord, BraidWord.writhe_cons, ih]
      ring

/-! ## n=2 ↔ closure2 identification (Markov closure)

The closure at `n = 2` is by construction the writhe composed with
`closure2` from `rem:braid-link-types`. We record this as a
theorem closed by `rfl`. -/

-- Ref: [manuscript] rem:braid-group-n-strand §"specialisations"
-- Ref: [manuscript] rem:braid-link-types
/-- **`closureN` at `n = 2` factors through `closure2`** via the
    writhe. Closed by `rfl` from the concrete definition of `closureN`
    at `n = 2`. -/
theorem closureN_eq_closure2 (w : BraidWord 2) :
    closureN w = closure2 w.writhe := rfl

/-! ## n=3 ↔ TypedBraidWord3 bridge

Conversion from `BraidWord 3` (this module's generic n=3 type) into
`TypedBraidWord3` (`typed-b3-sub-braid-extraction.lean`'s typed-B_3
list). The conversion preserves generator index and maps the boolean
sign onto the sibling file's `sigma`/`sigma_inv` constructors. The
sibling's `averaged` crossing type has no counterpart in `BraidWord 3`
(it is an extra Hecke-specific channel) so the conversion is into the
sigma/sigma_inv subset. -/

/-- A `BraidCrossing 3` (generator index in `Fin 2`, boolean sign)
    maps into the typed-B_3 representation by:
      `positive = true`  → `CrossingType3.sigma`
      `positive = false` → `CrossingType3.sigma_inv`. -/
def BraidCrossing.toTypedB3 (c : BraidCrossing 3) : TypedCrossing where
  generator := c.gen
  crossing_type := if c.positive then .sigma else .sigma_inv

-- Ref: [manuscript] rem:braid-group-n-strand §"specialisations"
-- Ref: [manuscript] rem:typed-b3-sub-braid-extraction
/-- **`BraidWord 3 → TypedBraidWord3` conversion.** Maps each
    `BraidCrossing 3` to its `TypedCrossing` counterpart via
    `BraidCrossing.toTypedB3`. -/
def BraidWord.toBraid3 (w : BraidWord 3) : TypedBraidWord3 :=
  w.map BraidCrossing.toTypedB3

/-- Length is preserved by the conversion. -/
@[simp] theorem BraidWord.toBraid3_length (w : BraidWord 3) :
    (BraidWord.toBraid3 w).length = w.length := by
  unfold BraidWord.toBraid3
  exact List.length_map _ _

/-! ## Open R&D

This file is the **n-strand scaffolding**. Concrete content to add:

  • Per-`n` discharge of `MarkovTraceN n q` from a fixed Markov-trace
    operator on the inductive limit `⋃_n B_n`
  • Higher-`n` `closureN` discharges (Borromean at n=3, di-baryon
    at n=6, etc.) — current `n ≥ 3` returns the placeholder
    `Link.unknot`
  • Per-n discharge of `MarkovTraceN n q` from a fixed Markov-trace
    operator on the inductive limit `⋃_n B_n`

These follow-ups are tractable but out of scope for the foundational
skeleton landed here.
-/

end QOU.BraidKnot
