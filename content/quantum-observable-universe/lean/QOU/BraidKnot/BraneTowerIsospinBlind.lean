import Mathlib.Data.Fintype.Card
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Brane-tower (R-side) is isospin-blind — a structural (b)-exclusion

The six-term mass formula
(`content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.md`)
requires every term to be a **Markov-invariant trace**.  Terms 2 and 3 (the
brane tower) are trace-invariant in the **R-side algebraic form**
`∑_S z^{|S|} Vol_q^{(S)}(β)`, where each `Vol_q^{(S)}` is a Markov trace over
the transfer-matrix chain supported on `S`.

This file formalises the **(b) structural exclusion** flagged in
`docs/audits/2026-06-26-t2t3-trace-invariance-status-synthesis.md`:

> In the trace-invariant R-side form, the single-generator stratum `T₂`
> depends **only on the strand count** `n = 3A` (one `z²` per adjacent
> generator position, by the Markov axiom `tr_M(σᵢ) = z`, which is
> *reduced-word independent*).  Hence two isobars (same `A`, same `n`) receive
> *identical* `T₂` — the brane tower carries **zero** mirror-nucleus splitting.

The cited invariant is the **Markov axiom** (`prop:markov-pair-z2`): the trace
of a single generator is the constant `z`, independent of which generator and
of the surrounding braid word.  That word-independence is exactly what makes
the closed form a function of `n` alone, and it is carried here as the
explicit hypothesis field `markov_gen`, from which the closed form is
*derived* (not assumed).

**Consequence for the open question.** Any *trace* reformulation of `T₂/T₃`
puts the entire T/³He mirror split in `T₁` (descended `tr_M`) and `T₅`
(chirality), never in the brane tower.  This is a search-pruning negative, not
a refutation of the formula; the production `Φ_q(|V̂ᵢ|)` specialisation *does*
carry a split, but at the cost of Markov-invariance (and with inverted sign,
`docs/audits/2026-06-18-he3-brane-tower-structural-gap.md`).

Base ring: generic `[CommRing R]` per AGENTS.md §7c — no archimedean construct
appears (the `z`, `z²` values are purely algebraic; the substrate
specialisation `z ≈ 0.499` lives downstream over `ℝ`).

The pair stratum `T₃ = (C(n-1,2)) • z⁴` is isospin-blind by the identical
argument (constant `z²` per position pair); only `T₂` is formalised here to
keep the witness tight, and the corollary transfers verbatim.
-/

namespace QOU.BraidKnot

open scoped BigOperators

variable {R : Type*} [CommRing R] {n : ℕ}

/-- R-side single-generator brane-tower datum on an `n`-strand braid over a
generic base ring `R`.  `trGen i` is the Markov trace of the `i`-th adjacent
generator; the field `markov_gen` records the Markov axiom `tr_M(σᵢ) = z`
(word-independent), the cited invariant of the (b)-exclusion. -/
structure MarkovTowerT2 (n : ℕ) (R : Type*) [CommRing R] where
  /-- Markov parameter `z = 1/(q^{1/2}+q^{-1/2})`. -/
  z : R
  /-- Markov trace of each adjacent generator. -/
  trGen : Fin (n - 1) → R
  /-- Markov axiom: every generator trace equals `z`, independent of the word. -/
  markov_gen : ∀ i, trGen i = z

/-- The R-side single-generator stratum `T₂ = ∑_i z · tr_M(σᵢ)`. -/
def MarkovTowerT2.value (M : MarkovTowerT2 n R) : R :=
  ∑ i, M.z * M.trGen i

/-- **Closed form.** `T₂ = (n-1) • z²` — a function of the strand count `n`
alone, derived from the Markov axiom.  No reference to the braid word survives. -/
theorem MarkovTowerT2.value_eq (M : MarkovTowerT2 n R) :
    M.value = (n - 1 : ℕ) • M.z ^ 2 := by
  simp only [MarkovTowerT2.value, M.markov_gen, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, pow_two]

/-- **Isospin-blindness (the (b)-exclusion).** Two isobars with the same strand
count `n` and the same Markov parameter `z` receive *identical* `T₂`.  Read
with `n = 3A`: tritium `(Z=1,N=2)` and ³He `(Z=2,N=1)` both have `n = 9`, so
the brane tower contributes the same value to each — zero to their
difference. -/
theorem t2_isobar_invariant (M M' : MarkovTowerT2 n R) (hz : M.z = M'.z) :
    M.value = M'.value := by
  rw [M.value_eq, M'.value_eq, hz]

/-- The brane tower contributes **zero** to the mirror-nucleus split. -/
theorem t2_mirror_split_zero (M M' : MarkovTowerT2 n R) (hz : M.z = M'.z) :
    M.value - M'.value = 0 := by
  rw [t2_isobar_invariant M M' hz, sub_self]

end QOU.BraidKnot
