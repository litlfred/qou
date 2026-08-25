import Mathlib.Tactic

/-!
# QOU.BraidsAndKnots.MilnorTripleLinkingMagnus — a computable `μ̄₁₂₃`, nonzero on Borromean

Bean `qou-bhfg` (front 4-B). Companion to
`QOU.BraidsAndKnots.BorromeanPairwiseLinking` and to
`docs/audits/2026-08-25-4b-pairwise-linking-prune.md`.

## Why this file exists

The pairwise prune next door shows every pairwise linking number vanishes on the
proton braid, so an `E_EM` ansatz built from pairwise data cannot separate it
from the unlink. The unique first-order candidate left is the **Milnor triple
linking number** `μ̄₁₂₃`.

The corpus did **not** have one. It has
`electroweak-triplet-charge-spin-from-involution.lean`'s
`evenTwistTripleLinking (_k : ℕ) : ℤ := 0` — correct, but defined only on the
**two**-component carrier `T(2,2k)`, where a triple linking number is `0` by
definition — and `KnotTheory/Vassiliev/MilnorVassilievBridge.lean`, which is
honest conjecture classes. Neither computes anything for three components. This
file supplies the computation, and it is the corpus's first **nonzero** triple
linking value.

## What is computed

Milnor's `μ̄₁₂₃` is the coefficient of `X₁X₂` in the Magnus expansion of the
longitude of the third component, read in the free group on the meridians
`x₁, x₂`. Degree 2 suffices, so the whole thing is a finite computation:

    x₁ ↦ 1 + X₁       x₁⁻¹ ↦ 1 − X₁ + X₁²
    x₂ ↦ 1 + X₂       x₂⁻¹ ↦ 1 − X₂ + X₂²

`Deg2` carries the seven coefficients of `1, X₁, X₂, X₁X₁, X₁X₂, X₂X₁, X₂X₂`,
and `Deg2.mul` is the truncated product. Everything below is `decide`.

## The coherence check worth noticing

The **degree-1** coefficients of a Magnus expansion are the linking numbers. So
`magnus_commutator`'s `c1 = c2 = 0` is the Magnus-side shadow of
`BorromeanPairwiseLinking.borromean_crossSum_zero`, computed by a completely
different route — a braid-word crossing simulation there, a free-group series
here. That they agree is a real consistency check on both files, not a
restatement.

It also matters mathematically: `μ̄₁₂₃` is only well-defined (indeterminacy-free)
when the pairwise linking numbers vanish. The vanishing degree-1 part is
*precisely* that hypothesis, verified rather than assumed.

## Scope — two topological inputs are CONSUMED, not proved

1. **Milnor's identification** of `μ̄₁₂₃` with the `X₁X₂` coefficient of the
   longitude. That is Milnor's theorem, cited, not re-derived here.
2. **That the Borromean longitude is the commutator `[x₁, x₂]`.** This is the
   standard presentation and is consumed exactly as the braid word
   `(σ₀σ₁⁻¹)³` is consumed next door.

What this file adds is the *computation* those inputs feed, which the corpus
lacked. It does **not** derive `E_EM`, and it does not supply the map from a
triple linking number to an energy — that gap is untouched and is the second of
the two objects 4-B still needs.

-- Ref: [milnor1957] (link groups; `μ̄` invariants as Magnus coefficients);
-- [kawauchi1996] (Borromean longitude as a commutator of meridians).
-/

namespace QOU.BraidsAndKnots.MilnorTripleLinkingMagnus

/-- A Magnus series truncated at degree 2, in two noncommuting variables:
coefficients of `1, X₁, X₂, X₁X₁, X₁X₂, X₂X₁, X₂X₂`. -/
structure Deg2 where
  c : ℤ
  c1 : ℤ
  c2 : ℤ
  c11 : ℤ
  c12 : ℤ
  c21 : ℤ
  c22 : ℤ
deriving DecidableEq, Repr

namespace Deg2

def one : Deg2 := ⟨1, 0, 0, 0, 0, 0, 0⟩

/-- Truncated product. `X₁X₂ ≠ X₂X₁`, so `c12` and `c21` are tracked separately —
which is the whole point: `μ̄₁₂₃` lives in the difference. -/
def mul (a b : Deg2) : Deg2 :=
  { c   := a.c * b.c
    c1  := a.c * b.c1 + a.c1 * b.c
    c2  := a.c * b.c2 + a.c2 * b.c
    c11 := a.c * b.c11 + a.c1 * b.c1 + a.c11 * b.c
    c12 := a.c * b.c12 + a.c1 * b.c2 + a.c12 * b.c
    c21 := a.c * b.c21 + a.c2 * b.c1 + a.c21 * b.c
    c22 := a.c * b.c22 + a.c2 * b.c2 + a.c22 * b.c }

end Deg2

/-- A free-group letter: generator index (`1` or `2`) and whether it is inverted. -/
abbrev Gen := ℕ × Bool

/-- Magnus image of a single letter. -/
def genImage : Gen → Deg2
  | (1, false) => ⟨1, 1, 0, 0, 0, 0, 0⟩
  | (1, true)  => ⟨1, -1, 0, 1, 0, 0, 0⟩
  | (2, false) => ⟨1, 0, 1, 0, 0, 0, 0⟩
  | (2, true)  => ⟨1, 0, -1, 0, 0, 0, 1⟩
  | _          => Deg2.one

/-- Magnus expansion of a word, truncated at degree 2. -/
def magnus : List Gen → Deg2
  | [] => Deg2.one
  | g :: w => Deg2.mul (genImage g) (magnus w)

/-- Milnor's `μ̄₁₂₃`: the coefficient of `X₁X₂` in the longitude's expansion. -/
def mubar123 (longitude : List Gen) : ℤ := (magnus longitude).c12

/-- The Borromean longitude `[x₁, x₂] = x₁x₂x₁⁻¹x₂⁻¹`. -/
def borromeanLongitude : List Gen := [(1, false), (2, false), (1, true), (2, true)]

/-- The unlink: trivial longitude. -/
def unlinkLongitude : List Gen := []

/-- The full degree-2 expansion of the commutator is `1 + X₁X₂ − X₂X₁`.

Note `c1 = c2 = 0`: the degree-1 part vanishes. Those coefficients are the
linking numbers, so this reproduces `BorromeanPairwiseLinking.borromean_crossSum_zero`
by an entirely different route — and it is exactly the hypothesis under which
`μ̄₁₂₃` is indeterminacy-free. -/
theorem magnus_commutator :
    magnus borromeanLongitude = ⟨1, 0, 0, 0, 1, -1, 0⟩ := by decide

/-- **`μ̄₁₂₃ = 1` on the Borromean braid** — the corpus's first nonzero triple
linking value, and the invariant the pairwise prune leaves standing. -/
theorem mubar_borromean_eq_one : mubar123 borromeanLongitude = 1 := by decide

/-- `μ̄₁₂₃ = 0` on the unlink, so the invariant separates the two links that
pairwise linking could not. -/
theorem mubar_unlink_eq_zero : mubar123 unlinkLongitude = 0 := by decide

/-- **The separation the prune asked for.** Pairwise linking assigns the
Borromean braid and the unlink the same data;
`μ̄₁₂₃` does not. -/
theorem mubar_separates_borromean_from_unlink :
    mubar123 borromeanLongitude ≠ mubar123 unlinkLongitude := by decide

/-- **Control on the hypothesis.** The non-commutator word `x₁x₂` also has
`X₁X₂`-coefficient `1`, but its degree-1 part is nonzero — so it does *not*
satisfy the vanishing-linking condition, and reading a `μ̄₁₂₃` off it would be
reading an indeterminate quantity.

This is here so the `= 1` above is not mistaken for "any word gives 1": the
value is meaningful for the commutator *because* its degree-1 part vanishes. -/
theorem noncommutator_degree_one_nonzero :
    (magnus [(1, false), (2, false)]).c1 ≠ 0 ∧
    (magnus [(1, false), (2, false)]).c2 ≠ 0 := by decide

end QOU.BraidsAndKnots.MilnorTripleLinkingMagnus
