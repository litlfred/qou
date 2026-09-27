/-
# γγ-produced braid words, and what the confinement SDP selects

Bean `qou-ales`, owner ruling 2026-09-08 (verbatim, read as *braid* words):

> "All selection of great words should be done through gamma gamma production
> and the semi-definite product solutions at q_0. Shouldn't use census."

This file states, before any search is run, the two predicates that ruling
needs (formalize-first, AGENTS.md §"Formalize-first probe discipline"):

* `GammaGammaWord` — a braid word is **γγ-produced** iff it is a product of
  pair-production vertices `σᵢ σᵢ₊₁⁻¹` (the `σ₀σ₁⁻¹ = γγ̄` reading of
  `computations/gamma_gamma_pair_production_decomposition.py`, under which
  the Borromean baryon `β_Bor = (σ₀σ₁⁻¹)³` is three sequential pair-production
  events, and `breit-wheeler-pair-production-derivation.md` §"Bare photon
  pair"). This is the *positive-negative* vertex, not the bare `σ₀²` of the
  Breit–Wheeler block; the two readings coexist in the corpus and the
  `.py` above is the one that names `γγ̄` as a braid-word factor.

* `SDPSelected` — the canonical `T_w` is the candidate whose Wedderburn
  projections are all positive semidefinite (`Matrix.PosSemidef`, block by
  block) and whose cost is minimal among such candidates. That is the
  feasibility-plus-optimality content of `prop:confinement-sdp`
  (`QOU.Interactions.ConfinementSDP` carries the primal–dual data; this file
  carries the *selection predicate* on words, which that module does not).

## What is proved (all sorry-free, falsifiable, checked before being stated)

* `writhe_eq_zero`      — every γγ-produced word has writhe `0`.
* `length_even`         — every γγ-produced word has an even crossing count.
* `altChar_eq_one`      — the alternating (sign) character `σᵢ ↦ −q⁻¹` of every
  γγ-produced word is exactly `1` (each vertex contributes `(−q⁻¹)(−q) = 1`).
  This is the lemma the accompanying probe measures: under convention D the
  H₃ trace-form radical is the q-antisymmetriser `v_k = (−1/q)^{len b_k}`, so
  the pairing of `v` with a word's normal-form coefficient vector is exactly
  the word's alternating character, and a γγ-word's demand profile is
  therefore **never** in the range of the Gram — the Frobenius rows
  `G x = nf` have no solution for any γγ-produced word, whatever the net row
  says.
* `not_gammaGamma_single` — a single crossing `σᵢ` is not γγ-produced (its
  writhe is `1`); so the template inter-nucleon `pp` bond `σ₀` is not, by
  itself, a pair-production word.
* `borromean_gammaGamma` — `β_Bor` is γγ-produced, and `toCorpus_borromean`
  ties this file's encoding to `QOU.StandardModel.BraidWords.borromean`.
* `h2_psdFeasible_iff_even` — on `H₂`, `SDPSelected`'s feasibility predicate,
  instantiated with the two one-dimensional Wedderburn blocks, reduces to the
  already-proved parity rule `QOU.QBeta.GluonVertexPsdParity.vertex_psd_iff_even`
  — so the abstract predicate is not vacuous: it recovers a known selection.
* `SDPSelected.cost_eq` — two SDP-selected words have equal cost.

## Base ring (§7c)

Words, writhe and `GammaGammaWord` are pure combinatorics (`ℕ`, `ℤ`, `Bool`).
The alternating character is stated over a generic `[Field R]` with `q ≠ 0`
— no ordering, no `Real`. The abstract `SDPSelected` is over any
`[Ring R] [PartialOrder R] [StarRing R]`, which is exactly what
`Matrix.PosSemidef` needs. Only the `H₂` instantiation lives on `ℝ`, because
`Matrix.posSemidef_diagonal_iff` needs `StarOrderedRing` and the parity rule
needs an order — that is the archimedean specialisation, kept at the end.

Nothing here reads AME, CODATA, or a census.
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Group.Even
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Real.StarOrdered
import Mathlib.Tactic
import QOU.QBeta.GluonVertexPsdParity
import QOU.StandardModel.ChiralFermionBraidWords

namespace QOU.Mass.GammaGammaWordSelection

/-! ## Words -/

/-- A crossing: which Artin generator `σ_gen` (0-based) and its sign
(`pos = true` for `σ_gen`, `false` for `σ_gen⁻¹`). -/
structure Crossing where
  /-- Generator index `i` of `σᵢ`, 0-based. -/
  gen : ℕ
  /-- `true` = positive crossing `σᵢ`, `false` = `σᵢ⁻¹`. -/
  pos : Bool
  deriving DecidableEq, Repr

/-- A braid word is a list of crossings; `[]` is the identity braid. -/
abbrev Word := List Crossing

/-- The pair-production vertex `σᵢ σᵢ₊₁⁻¹` — one photon on strands `(i, i+1)`
and one anti-photon on `(i+1, i+2)`, the `γγ̄` factor of
`gamma_gamma_pair_production_decomposition.py`. -/
def vertex (i : ℕ) : Word := [⟨i, true⟩, ⟨i + 1, false⟩]

/-- **γγ-produced words**: the words that are (left-to-right) products of
pair-production vertices. The empty word is the empty product. -/
inductive GammaGammaWord : Word → Prop
  | nil : GammaGammaWord []
  | cons (i : ℕ) {w : Word} (hw : GammaGammaWord w) : GammaGammaWord (vertex i ++ w)

/-- Sign of a crossing, `±1`. -/
def sign (c : Crossing) : ℤ := if c.pos then 1 else -1

/-- Writhe: the sum of the crossing signs. -/
def writhe (w : Word) : ℤ := (w.map sign).sum

theorem writhe_append (u v : Word) : writhe (u ++ v) = writhe u + writhe v := by
  simp [writhe, List.map_append, List.sum_append]

/-- One vertex pairs a positive with a negative crossing. -/
theorem writhe_vertex (i : ℕ) : writhe (vertex i) = 0 := by
  simp [writhe, vertex, sign]

/-- **Every γγ-produced word has writhe `0`.** -/
theorem writhe_eq_zero {w : Word} (h : GammaGammaWord w) : writhe w = 0 := by
  induction h with
  | nil => simp [writhe]
  | cons i _ ih => rw [writhe_append, writhe_vertex, ih, add_zero]

theorem length_vertex_append (i : ℕ) (w : Word) :
    (vertex i ++ w).length = 2 + w.length := by
  simp only [List.length_append, vertex, List.length_cons, List.length_nil]

/-- **Every γγ-produced word has an even number of crossings.** -/
theorem length_even {w : Word} (h : GammaGammaWord w) : Even w.length := by
  induction h with
  | nil => exact ⟨0, rfl⟩
  | cons i _ ih =>
    rw [length_vertex_append]
    exact Even.add ⟨1, rfl⟩ ih

/-- A single positive crossing has writhe `1`, hence is **not** γγ-produced.
In particular the template inter-nucleon `pp` bond `σ₀` is not, on its own, a
pair-production word. -/
theorem not_gammaGamma_single (i : ℕ) : ¬ GammaGammaWord [⟨i, true⟩] := by
  intro h
  have := writhe_eq_zero h
  simp [writhe, sign] at this

/-! ## The alternating character -/

section AltChar

variable {R : Type*} [Field R]

/-- The one-dimensional **alternating** representation of the Hecke algebra,
`σᵢ ↦ −q⁻¹` (and so `σᵢ⁻¹ ↦ −q`), evaluated on a word. Under convention D the
trace-form radical of `H₃(q)` is spanned by `v_k = (−1/q)^{len b_k}` — the
alternating character of the normal-form basis — so this is the functional
whose vanishing decides whether a word's normal form lies in the range of
the Gram. -/
def altChar (q : R) (w : Word) : R :=
  (w.map fun c => if c.pos then -q⁻¹ else -q).prod

theorem altChar_append (q : R) (u v : Word) :
    altChar q (u ++ v) = altChar q u * altChar q v := by
  simp [altChar, List.map_append, List.prod_append]

/-- One pair-production vertex has alternating character `(−q⁻¹)(−q) = 1`. -/
theorem altChar_vertex {q : R} (hq : q ≠ 0) (i : ℕ) : altChar q (vertex i) = 1 := by
  simp [altChar, vertex, hq]

/-- **The alternating character of every γγ-produced word is `1`.** -/
theorem altChar_eq_one {q : R} (hq : q ≠ 0) {w : Word} (h : GammaGammaWord w) :
    altChar q w = 1 := by
  induction h with
  | nil => simp [altChar]
  | cons i _ ih => rw [altChar_append, altChar_vertex hq, ih, one_mul]

/-- Hence it never vanishes: no γγ-produced word is killed by the alternating
block, which is what the D-frame Frobenius rows would require. -/
theorem altChar_ne_zero {q : R} (hq : q ≠ 0) {w : Word} (h : GammaGammaWord w) :
    altChar q w ≠ 0 := by
  rw [altChar_eq_one hq h]
  exact one_ne_zero

/-- A single positive crossing has alternating character `−q⁻¹` — nonzero, so
the template `pp` bond is likewise not in the Gram's range, but for a
different reason than a γγ-word (it is not a unit of the character). -/
theorem altChar_single (q : R) (i : ℕ) : altChar q [⟨i, true⟩] = -q⁻¹ := by
  simp [altChar]

end AltChar

/-! ## The Borromean baryon, tied to the corpus encoding -/

/-- `β_Bor = (σ₀σ₁⁻¹)³`, written as the nested product the `GammaGammaWord`
constructors produce. -/
def borromean : Word := vertex 0 ++ (vertex 0 ++ (vertex 0 ++ []))

/-- `β_Bor` is γγ-produced: three pair-production events. -/
theorem borromean_gammaGamma : GammaGammaWord borromean :=
  .cons 0 (.cons 0 (.cons 0 .nil))

theorem borromean_writhe : writhe borromean = 0 :=
  writhe_eq_zero borromean_gammaGamma

/-- Translate to the corpus encoding of `QOU.StandardModel.BraidWords`
(entry `±(i+1)` for `σᵢ^{±1}`). -/
def toCorpus (w : Word) : QOU.StandardModel.BraidWords.BraidWord :=
  w.map fun c => if c.pos then ((c.gen : ℤ) + 1) else -((c.gen : ℤ) + 1)

/-- `vertex 0` is the corpus's `gluonUnit = σ₀σ₁⁻¹ = [1, -2]`. -/
theorem toCorpus_vertex_zero :
    toCorpus (vertex 0) = QOU.StandardModel.BraidWords.gluonUnit := by
  decide

/-- This file's `borromean` is the corpus's `borromean`. -/
theorem toCorpus_borromean :
    toCorpus borromean = QOU.StandardModel.BraidWords.borromean := by
  decide

/-! ## What the SDP selects -/

section SDP

/-- **Wedderburn block data** for a candidate type `W`: for each block label
`l : ι` of dimension `d l`, the matrix image of each candidate under the
block projection `π_l`. -/
structure WedderburnBlocks (R : Type*) [Ring R] (W ι : Type*) (d : ι → ℕ) where
  /-- The block projections `π_l : W → Mat_{d l}(R)`. -/
  proj : W → (l : ι) → Matrix (Fin (d l)) (Fin (d l)) R

variable {R : Type*} [Ring R] [PartialOrder R] [StarRing R]
variable {W ι : Type*} {d : ι → ℕ}

/-- **PSD feasibility**: every Wedderburn projection of `w` is positive
semidefinite. This is constraint (1)+(2) of `prop:confinement-sdp` read on a
candidate word, with the actual `Matrix.PosSemidef` cone — not a placeholder. -/
def WedderburnBlocks.PSDFeasible (B : WedderburnBlocks R W ι d) (w : W) : Prop :=
  ∀ l : ι, (B.proj w l).PosSemidef

/-- **SDP selection.** `w` is the canonical word for a candidate set `cands`
and cost `cost` iff it is a candidate, it is PSD-feasible, and no PSD-feasible
candidate has smaller cost. -/
structure SDPSelected (B : WedderburnBlocks R W ι d) (cands : Set W) (cost : W → R)
    (w : W) : Prop where
  /-- `w` is one of the candidates. -/
  mem : w ∈ cands
  /-- Every Wedderburn projection of `w` is PSD. -/
  psd : B.PSDFeasible w
  /-- `w` minimises the cost over PSD-feasible candidates. -/
  minimal : ∀ w' ∈ cands, B.PSDFeasible w' → cost w ≤ cost w'

/-- Two SDP-selected words have equal cost: selection is unique up to cost
ties. -/
theorem SDPSelected.cost_eq {B : WedderburnBlocks R W ι d} {cands : Set W}
    {cost : W → R} {w₁ w₂ : W}
    (h₁ : SDPSelected B cands cost w₁) (h₂ : SDPSelected B cands cost w₂) :
    cost w₁ = cost w₂ :=
  le_antisymm (h₁.minimal w₂ h₂.mem h₂.psd) (h₂.minimal w₁ h₁.mem h₁.psd)

end SDP

/-! ## Archimedean specialisation: the `H₂` vertex

`H₂(q)` has two one-dimensional Wedderburn blocks, `(2)` with `σ₀ ↦ q` and
`(1,1)` with `σ₀ ↦ −q⁻¹`, so the candidate `σ₀^k` projects to the `1×1`
matrices `q^k` and `(−q⁻¹)^k`. This is the instantiation
`sdp_gamma_gamma_to_qqbar.py` solves by hand. -/

section H2

open QOU.QBeta.GluonVertexPsdParity

/-- The two `H₂` blocks (`true` = symmetric `(2)`, `false` = alternating
`(1,1)`), on candidates `k ↦ σ₀^k`. -/
noncomputable def h2Blocks (q : ℝ) : WedderburnBlocks ℝ ℕ Bool (fun _ => 1) where
  proj k b := Matrix.diagonal fun _ => if b then symEigenPow q k else altEigenPow q k

/-- **The abstract predicate recovers the proved parity rule.** For `0 < q`,
`σ₀^k` is PSD-feasible in the sense of `SDPSelected` iff `k` is even —
`QOU.QBeta.GluonVertexPsdParity.vertex_psd_iff_even`, re-derived through
`Matrix.PosSemidef` on the two blocks. -/
theorem h2_psdFeasible_iff_even {q : ℝ} (hq : 0 < q) (k : ℕ) :
    (h2Blocks q).PSDFeasible k ↔ Even k := by
  unfold WedderburnBlocks.PSDFeasible h2Blocks
  simp only [Matrix.posSemidef_diagonal_iff]
  rw [← vertex_psd_iff_even hq k]
  constructor
  · intro h
    exact ⟨by simpa using h true 0, by simpa using h false 0⟩
  · rintro ⟨hs, ha⟩ b _
    cases b <;> simpa

/-- `σ₀²`, the shipped gluon vertex, is PSD-feasible; `σ₀` is not. -/
theorem h2_two_feasible_one_not {q : ℝ} (hq : 0 < q) :
    (h2Blocks q).PSDFeasible 2 ∧ ¬ (h2Blocks q).PSDFeasible 1 := by
  refine ⟨(h2_psdFeasible_iff_even hq 2).mpr ⟨1, rfl⟩, ?_⟩
  intro h
  exact (Nat.not_even_iff_odd.mpr ⟨0, rfl⟩) ((h2_psdFeasible_iff_even hq 1).mp h)

end H2

end QOU.Mass.GammaGammaWordSelection
