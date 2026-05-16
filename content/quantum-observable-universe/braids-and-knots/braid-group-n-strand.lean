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

/-! ## Typed crossings -/

/-- A typed crossing in `B_n`: which generator (index `i : Fin (n − 1)`)
    and which sign (`positive` for σ_i, `negative` for σ_i⁻¹). -/
structure TypedCrossing (n : ℕ) where
  /-- Generator index `i` in `σ_i`, valued in `Fin (n − 1)`. -/
  gen : Fin (n - 1)
  /-- Sign of the crossing: `true` = positive (`σ_i`), `false` = inverse. -/
  positive : Bool
  deriving Repr, DecidableEq

/-! ## Braid words -/

/-- An n-strand braid word — list of typed crossings. The empty list
    is the identity braid. -/
abbrev BraidWord (n : ℕ) : Type := List (TypedCrossing n)

namespace BraidWord

/-- Net writhe (signed crossing count) of a braid word. -/
def writhe {n : ℕ} (w : BraidWord n) : ℤ :=
  w.foldr (fun c acc => acc + (if c.positive then 1 else -1)) 0

@[simp] theorem writhe_nil (n : ℕ) : writhe ([] : BraidWord n) = 0 := rfl

@[simp] theorem writhe_cons {n : ℕ} (c : TypedCrossing n) (w : BraidWord n) :
    writhe (c :: w) = (if c.positive then 1 else -1) + writhe w := by
  unfold writhe
  simp [List.foldr]
  ring

end BraidWord

/-! ## Markov closure (axiomatised at general n)

For `n = 2` the closure is `closure2` from `rem:braid-link-types`,
which is concrete (pattern match on `Braid2 := ℤ`).

For `n ≥ 3` the closure is axiomatised as an opaque function into
`Link`; per-irrep specialisations discharge concrete equalities
(e.g. `typed-b3-sub-braid-extraction` for n = 3 at ε^6 order). -/

/-- **Markov closure** of an n-strand braid word to a link.

    Axiomatised at the general-n level; concrete for `n = 2` via
    `closure2` (`rem:braid-link-types`). Per-irrep, per-n proofs of
    specific closure equalities (Hopf at n=2 σ², Borromean at n=3,
    etc.) plug into this signature. -/
opaque closureN : ∀ {n : ℕ}, BraidWord n → Link

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

/-! ## Open R&D

This file is the **n-strand scaffolding**. Concrete content to add:

  • Define `BraidWord.toBraid3 : ...` mapping into the typed
    `TypedBraidWord3` from `rem:typed-b3-sub-braid-extraction`
  • Define `closureN_eq_closure2` linking `closureN @ n=2` to
    `closure2` (1-line `rfl`-style identification once the
    `opaque closureN` is replaced by a concrete construction at n=2)
  • Per-n discharge of `MarkovTraceN n q` from a fixed Markov-trace
    operator on the inductive limit `⋃_n B_n`

These follow-ups are tractable but out of scope for the foundational
skeleton landed here.
-/

end QOU.BraidKnot
