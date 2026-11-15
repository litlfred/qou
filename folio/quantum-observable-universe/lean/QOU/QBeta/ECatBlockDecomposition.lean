/-
  Infrastructure for the `E_cat` double integral: its per-block decomposition,
  and why a double integral escapes the letter-sum exclusion.

  THE TARGET. `QOU/MobiusEnergy.lean` (`prop:mobius-energy`) specifies the
  categorical Möbius energy of a knot `γ` as

      E_cat(γ) = λ ∘ tr_A ∬_{S¹×S¹ ∖ diag}
                   (Δ(γ(s)) ⊗ Δ(γ(t))) ⋆_q ‖dγ/ds ∧_q dγ/dt‖ ds dt

  with `λ` the Frobenius form and `tr_A` the algebra trace. That composite is
  the object the canonical chain decomposes as `tr_M = Σ_λ y_λ χ_λ`, the
  non-abelian Stokes step being what puts the `S¹ × S¹` double integral into
  `H_n(q)` so Wedderburn can split it.

  WHY THIS FILE EXISTS. `QOU/Mass/GammaGammaWordSelection.lean` defines

      structure SDPSelected (B) (cands) (cost : W → R) (w) : Prop

  with `cost` a FREE PARAMETER, and every instantiation in the corpus fills it
  with `fun w => (w.length : ℝ)` — the crossing count. That is precisely the
  letter-sum class `QOU/QBeta/LetterSumBlindness.lean` excludes scope-(b): a
  sum over letters is permutation-invariant while the closure is not, so the
  crossing count cannot separate `σ₁σ₀` from `σ₀σ₁`. This file supplies what
  goes in that socket instead.

  WHAT IS PROVED HERE, and the first one is the load-bearing one.

  §1 `blockDecomposition_of_linear` — **the per-block split is a THEOREM, not
  an assumption.** Stated for an arbitrary linear functional `I`, so it says
  the decomposition holds for ANY linear integral and is not an artefact of a
  particular measure:

      I (Σ_λ y_λ • f_λ)  =  Σ_λ y_λ * I (f_λ)

  This matters for the anti-laundering discipline. `MobiusEnergy.lean` carries
  its classical limit as a structure FIELD — an assumption — and its own header
  records an incident where that field made `E_cat` blind (`E_cat = 1 + const`
  for every knot) with no `sorry` to flag it. The decomposition here is NOT of
  that kind: it is derived from linearity and needs no new hypothesis. §2
  instantiates it at Mathlib's Bochner integral so the claim is about the real
  integral and not only about an abstraction.

  §3 is the part that connects to the exclusion. A letter sum is
  permutation-invariant; a PAIR sum whose kernel depends on the SEPARATION of
  the two letters is NOT. `pairSum_not_perm_invariant` exhibits a concrete
  separation-dependent kernel and a concrete transposition on which the pair
  sum changes. Since the O'Hara integrand's `1/d²` is exactly such a kernel,
  this is the structural reason the double integral is not caught by
  `LetterSumBlindness` — the escape is the separation dependence, and nothing
  weaker.

  §4 records the socket fit: a cost assembled from per-block data has type
  `W → R` and is therefore admissible in `SDPSelected` / `FrobeniusSelected`
  without any change to those structures.

  🛑 WHAT IS NOT PROVED, AND MUST NOT BE READ IN.

  * Nothing here computes `E_cat`. The double integral has no producer in the
    corpus; `energy : ℝ` in `CategoricalMobiusEnergy` is a bare structure
    field. §1-§2 say how it decomposes IF it exists; they do not construct it.
  * Nothing here claims the resulting cost SELECTS the live 11-letter word, or
    any word. §3 shows the pair-sum class is not excluded by the
    permutation-invariance argument. A prune that fails to fire is not a
    positive result.
  * The classical-limit leg of `MobiusEnergy.lean` is untouched and still
    assumed, with the blindness incident unretired (bean `qou-pzsi`).
  * Convention: the block weights `y_λ` are left abstract. Under convention D
    `y_(1³) = 0`, so the alternating block drops out of any such sum — that is
    a fact about the weights, not about this decomposition.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [leitner2026] QOU/MobiusEnergy.lean  (prop:mobius-energy, the target)
  -- Ref: [leitner2026] QOU/Mass/GammaGammaWordSelection.lean  (the cost socket)
  -- Ref: [leitner2026] QOU/QBeta/LetterSumBlindness.lean  (the exclusion this escapes)
  -- Ref: [leitner2026] computations/confinement_lp_braid_gram_probe.py
  --      ("a surviving formulation has to break (a): change the objective,
  --        not the Gram")
  -- Ref: [leitner2026] .beans/qou-pzsi , .beans/qou-99qc
-/
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Data.List.Perm.Basic
import Mathlib.Tactic.NormNum

namespace QOU.QBeta.ECatBlockDecomposition

open BigOperators

/-! ### 1. The per-block decomposition is a consequence of LINEARITY -/

/-- **The block decomposition of `E_cat`, derived rather than assumed.**

`I` is the integral, presented as an arbitrary linear functional; `y` are the
Wedderburn block weights `y_λ`; `f λ` is the per-block integrand
`χ_λ[(Δ(γ(s)) ⊗ Δ(γ(t))) ⋆_q ‖…‖]`. The conclusion

    I (Σ_λ y_λ • f λ)  =  Σ_λ y_λ * I (f λ)

says the total energy is the `y`-weighted sum of per-block integrals, so the
per-block vector `t_λ := y_λ * I (f λ)` is a REFINEMENT of `E_cat` and not a
different quantity.

Stated over a generic commutative ring with `I` an arbitrary linear map: the
decomposition is a fact about linearity, so it cannot be an artefact of the
measure, of the `q`-deformation, or of the particular blocks. -/
theorem blockDecomposition_of_linear {ι R V : Type*} [Fintype ι] [CommRing R]
    [AddCommGroup V] [Module R V] (I : V →ₗ[R] R) (y : ι → R) (f : ι → V) :
    I (∑ i, y i • f i) = ∑ i, y i * I (f i) := by
  rw [map_sum]
  simp [map_smul, smul_eq_mul]

/-- The total is exactly the sum of the per-block costs: with
`t_λ := y_λ * I (f λ)`, we get `E_cat = Σ_λ t_λ`. This is the Lean form of the
assembly identity `tr_M = Σ_λ t_λ` that `computations/nucleus_sdp_assembly.py`
asserts numerically, and it makes the per-block vector and the scalar total two
views of one object. -/
theorem total_eq_sum_blockCosts {ι R V : Type*} [Fintype ι] [CommRing R]
    [AddCommGroup V] [Module R V] (I : V →ₗ[R] R) (y : ι → R) (f : ι → V) :
    I (∑ i, y i • f i) = ∑ i, (fun j => y j * I (f j)) i :=
  blockDecomposition_of_linear I y f

/-- **A per-block VECTOR is strictly finer than its total.** Two block
decompositions can have the same total and different components, so a cost
built from the vector can separate cases the scalar cannot.

This is the precise sense in which decomposing `E_cat` over partitions buys
something: it is not merely a re-writing. Exhibited concretely rather than
asserted. -/
theorem blockVector_strictly_finer_than_total :
    ∃ (t t' : Fin 2 → ℤ), (∑ i, t i) = (∑ i, t' i) ∧ t ≠ t' := by
  refine ⟨![0, 2], ![1, 1], by decide, ?_⟩
  intro h
  have : (0 : ℤ) = 1 := congrFun h 0
  exact absurd this (by decide)

/-! ### 2. The same statement at Mathlib's integral, so it is about the real
double integral and not only about an abstraction -/

open MeasureTheory

/-- **The block decomposition at the Bochner integral.**

The integrand is a finite `y`-weighted sum of per-block integrands, each
integrable; the integral of the sum is the weighted sum of the integrals. With
`α := S¹ × S¹ ∖ diag` and `μ` the product measure this is exactly the
`E_cat` decomposition, with no hypothesis beyond integrability of each block's
integrand.

Integrability is a genuine hypothesis and is stated, not assumed away: the
O'Hara integrand is regularised precisely so that it is integrable across the
diagonal, and on the flat-torus geodesic realisation it is identically zero
there (`qbeta_bring_ohara_bridge_probe`, check [C2]). -/
theorem integral_blockDecomposition {ι α : Type*} [Fintype ι]
    [MeasurableSpace α] (μ : Measure α) (y : ι → ℝ) (f : ι → α → ℝ)
    (hf : ∀ i, Integrable (f i) μ) :
    ∫ x, (∑ i, y i * f i x) ∂μ = ∑ i, y i * ∫ x, f i x ∂μ := by
  rw [integral_finset_sum _ (fun i _ => (hf i).const_mul (y i))]
  simp_rw [integral_const_mul]

/-! ### 3. Why a DOUBLE INTEGRAL escapes the letter-sum exclusion:
separation dependence -/

/-- Pairs of a distinguished head letter with each later letter, carrying the
SEPARATION `d` between them. This is the discrete shadow of the O'Hara
integrand's dependence on `|s - t|`. -/
def headPairs (K : ℕ → ℕ → ℕ → ℕ) (x : ℕ) : List ℕ → ℕ → ℕ
  | [], _ => 0
  | y :: ys, d => K x y d + headPairs K x ys (d + 1)

/-- Sum over ordered pairs of letters, weighted by a kernel that sees both
letters AND their separation along the word. The O'Hara integrand is of this
shape, with `K` carrying the `1/d²` factor. -/
def pairSum (K : ℕ → ℕ → ℕ → ℕ) : List ℕ → ℕ
  | [] => 0
  | x :: xs => headPairs K x xs 1 + pairSum K xs

/-- **A separation-dependent pair sum is NOT permutation-invariant.**

This is the escape, and it is the whole reason a double integral can do what a
letter sum provably cannot. `LetterSumBlindness.letterSum_perm_invariant`
shows any `Σ_letters f(letter)` is constant on the permutation orbit; here a
concrete kernel and a concrete transposition give different values.

The mechanism is worth stating because it is the design constraint on any
replacement cost: permuting the letters does not change the multiset, but it
DOES change which pairs sit at which separation, so a kernel that reads the
separation sees the reordering. A pair kernel that ignored `d` and was
symmetric in its two letters would be permutation-invariant again and would
buy nothing. -/
theorem pairSum_not_perm_invariant :
    ∃ (K : ℕ → ℕ → ℕ → ℕ) (l l' : List ℕ),
      l.Perm l' ∧ pairSum K l ≠ pairSum K l' := by
  refine ⟨fun x _ d => x * d, [0, 1, 2], [1, 0, 2], List.Perm.swap 1 0 [2], ?_⟩
  decide

/-! ### 4. The socket: a per-block cost is admissible where the crossing count
currently sits -/

/-- A cost assembled from per-block data. `blocks w` is the per-block vector
`t_λ(w)` of the word `w`; the cost is its `y`-weighted total. The point is the
TYPE: this is a `W → R`, so it drops into `SDPSelected` / `FrobeniusSelected`
in place of `fun w => (w.length : R)` with no change to those structures. -/
def blockCost {W ι R : Type*} [Fintype ι] [CommRing R]
    (y : ι → R) (blocks : W → ι → R) : W → R :=
  fun w => ∑ i, y i * blocks w i

/-- The block cost of a word is its per-block vector's weighted total —
the `W`-indexed form of §1, and the statement that the socket receives the
same object §1 decomposes. -/
theorem blockCost_apply {W ι R : Type*} [Fintype ι] [CommRing R]
    (y : ι → R) (blocks : W → ι → R) (w : W) :
    blockCost y blocks w = ∑ i, y i * blocks w i := rfl

/-- **The block cost CAN separate two words**, unlike the crossing count,
provided their per-block vectors differ in a way the weights do not cancel.
Exhibited concretely: the exclusion in `LetterSumBlindness` does not extend to
this class.

Not a claim that it separates the four gluon candidates — that is a
measurement, and it is not made here. -/
theorem blockCost_can_separate :
    ∃ (W ι : Type) (_ : Fintype ι) (y : ι → ℤ) (blocks : W → ι → ℤ) (w w' : W),
      blockCost y blocks w ≠ blockCost y blocks w' := by
  refine ⟨Bool, Fin 1, inferInstance, fun _ => 1,
          fun b _ => cond b 0 1, true, false, ?_⟩
  simp [blockCost]

end QOU.QBeta.ECatBlockDecomposition
