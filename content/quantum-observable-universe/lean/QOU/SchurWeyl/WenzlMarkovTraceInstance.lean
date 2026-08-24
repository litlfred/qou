import QOU.SchurWeyl.MarkovTraceInstance
import QOU.SchurWeyl.WenzlMarkovLevelR
import QOU.SchurWeyl.WenzlNormalisation

/-!
# QOU.SchurWeyl.WenzlMarkovTraceInstance — the level-`r` Markov trace, and its uniqueness

`MarkovTraceInstance` closes the convention-D chain: the Ocneanu weight defines a Markov trace, and
`markovTrace_unique` identifies *every* Markov trace at that parameter with it.  #5662 generalised
the three weight properties — vanishing, branching, normalisation — and the Markov condition itself
to every integer level `r`.  This file carries the identification across.

## The one thing that was *not* `r = 2`-specific

`HeckeCoset.markovTrace_unique` never mentions a level.  It is stated for two
`MarkovTraceFamily K q qi z` at a common `z`, over a generic `[CommRing K]`, and its proof runs on
the coset spanning family alone.  So "uniqueness at `r = 2`" was not a level-2 theorem with a
level-2 proof; it was a level-free theorem applied to the one level for which an **instance**
existed.  What this file adds is the missing instances — one per level — not a new uniqueness
argument.

That is worth stating plainly, because "generalise uniqueness" invites the assumption that the
uniqueness *proof* needs work.  It does not.  The `r`-dependence lived entirely in
`ocneanuMarkovTrace`.

| | |
|---|---|
| `markovTraceOfWeight` | any weight with normalisation + branching + Markov is a `MarkovTraceFamily` |
| `wenzlMarkovTrace` | the level-`r` instance, at `z_r = Q^r / (q · [r]_Q)`, `Q = q²` |
| `eq_wenzlWtrace_of_markov` | **uniqueness at every integer level `r`** |
| `wenzlMarkovTrace_two_tr` | conservativity: at `r = 2` the trace *is* `wtrace` |
| `MarkovTraceFamily.param_eq` | the parameter is recoverable from the family: `z = tr₁(σ₀)` |
| `level_unique_of_wenzlMarkovTrace_eq` | **distinct levels give distinct traces** |

## The two uniqueness questions are different, and both are needed

They are easy to conflate, so:

* **Uniqueness of the trace, given the parameter** — `markovTrace_unique`.  Fixing `z` pins the
  functional `tr` on every `H_n(q)`.  Nothing there is about levels; `z` ranges over the whole ring.
* **Uniqueness of the level, given the parameter** —
  `QBeta.WenzlWeight.level_unique_of_markovParameter`.  Fixing `z` pins the *integer* `r`, for `Q`
  not a root of unity.  Nothing there is about traces.

Neither implies the other: the first says a `z` has at most one trace, the second says a `z` is hit
by at most one level.  `level_unique_of_wenzlMarkovTrace_eq` is what you get by running them
together in the one direction that composes — `tr` determines `z` (`param_eq`), `z` determines `r`
— and it is a statement about neither alone: **the level is a functional invariant of the trace**,
readable off a single value `tr₁(σ₀)`.

## Scope

* Genericity `hgen`: `Q = q²` is not a root of unity.  At a root of unity `H_n(q)` is not
  semisimple and partitions stop indexing the irreducibles; the statement would need a different
  formulation, not a better proof.
* `r ≠ 0`.  At `r = 0` the bracket `[0]_Q` is the empty sum `0` and the normalisation
  `w_μ = s_μ / [r]_Q^{|μ|}` is undefined.
* `z_r` is a point of the **Wenzl lattice**.  Nothing here says a Markov trace exists at an
  arbitrary `z` off it — only that if one does and it sits at some `z_r`, it is this one.

## Base ring (§7c)

`ℝ` for everything touching `seminormalRep` / `seminormalParam`; the two purely algebraic lemmas
(`ne_one_of_gen`, `levelBracket_ne_zero_of_gen`) are generic `[Field R]`, and
`MarkovTraceFamily.param_eq` is generic `[CommRing K]`.

LaTeX label: `thm:wenzl-markov-trace-instance`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset

/-! ## Genericity supplies the side conditions the weight needs -/

variable {R : Type*} [Field R]

/-- A `Q` that is not a root of unity is not `1`. -/
theorem ne_one_of_gen {Q : R} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) : Q ≠ 1 :=
  fun h => hgen 1 one_ne_zero (by rw [h]; simp)

/-- **The level bracket is nonzero under genericity.**

`[r]_Q = 0` would make `1 − Q^r = (1 − Q)·[r]_Q` vanish, i.e. `Q^r = 1` with `r ≠ 0`.  So the `hbr`
hypothesis carried separately through `WenzlNormalisation` is *implied* by `hgen`, and the level-`r`
chain runs on one genericity assumption rather than two. -/
theorem levelBracket_ne_zero_of_gen {Q : R} {r : ℕ}
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hr : r ≠ 0) : levelBracket r Q ≠ 0 := by
  intro h
  have h1 : (1 : R) - Q ^ r = (1 - Q) * levelBracket r Q :=
    one_sub_pow_eq_mul_levelBracket r Q
  rw [h, mul_zero, sub_eq_zero] at h1
  exact hgen (r : ℤ) (by exact_mod_cast hr) (by rw [zpow_natCast, ← h1])

/-! ## The parameter is recoverable from the family -/

namespace HeckeCoset

variable {K : Type*} [CommRing K] {q qi z : K}

/-- **The Markov parameter is a value of the trace**, namely `z = tr₁(σ₀)`.

Take `x = 1` in the Markov axiom: `tr₁(ι(1)·σ₀) = z · tr₀(1) = z`.  Two Markov trace families whose
underlying `tr` agree therefore carry the *same* parameter — which is what lets `markovTrace_unique`
(one `z`, one trace) be used in the other direction. -/
theorem MarkovTraceFamily.param_eq (T : MarkovTraceFamily K q qi z) :
    T.tr 1 (Hecke.σ K q qi 1 (Fin.last 0)) = z := by
  have h := T.tr_markov 0 (1 : Hecke K q qi 0)
  rw [map_one, one_mul, T.tr_one] at h
  rw [h, mul_one]

end HeckeCoset

/-! ## Any weight system with the three properties is a Markov trace -/

namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

/-- The seminormal trace weighted by an arbitrary `w`.

`wtrace` is the `w = ocneanuWeight q z_D` case; the level-`r` trace below is the
`w = wenzlWeight r (q²)` case.  Keeping `w` free isolates exactly which of the four
`MarkovTraceFamily` axioms depend on the weight (three) and which does not (cyclicity). -/
noncomputable def wtraceW (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (w : YoungDiagram → ℝ) (n : ℕ) :
    Hecke ℝ q q⁻¹ n →ₗ[ℝ] ℝ where
  toFun x := ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
    w ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace
  map_add' x y := by
    simp only [map_add, Matrix.trace_add, mul_add]
    exact Finset.sum_add_distrib
  map_smul' c x := by
    simp only [map_smul, Matrix.trace_smul, smul_eq_mul, RingHom.id_apply, Finset.mul_sum]
    exact Finset.sum_congr rfl fun ν _ => by ring

theorem wtraceW_apply (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (w : YoungDiagram → ℝ) (n : ℕ)
    (x : Hecke ℝ q q⁻¹ n) :
    wtraceW q hq0 hq2 w n x = ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
      w ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace := rfl

/-- **Cyclicity needs no property of `w` at all** — `seminormalRep` is an `AlgHom`, so this is
`Matrix.trace_mul_comm` blockwise. -/
theorem wtraceW_cyclic (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (w : YoungDiagram → ℝ) (n : ℕ)
    (x y : Hecke ℝ q q⁻¹ n) :
    wtraceW q hq0 hq2 w n (x * y) = wtraceW q hq0 hq2 w n (y * x) := by
  rw [wtraceW_apply, wtraceW_apply]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [map_mul, map_mul, Matrix.trace_mul_comm]

/-- Normalisation of the weight gives `tr(1) = 1`. -/
theorem wtraceW_one (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (w : YoungDiagram → ℝ)
    (hnorm : ∀ n : ℕ, (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
      (numStandardYoungTableaux ν.1 : ℝ) * w ν.1) = 1) (n : ℕ) :
    wtraceW q hq0 hq2 w n 1 = 1 := by
  rw [wtraceW_apply]
  have key : ∀ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
      w ν.1 * ((seminormalRep q hq0 hq2 n ν.2) 1).trace
        = (numStandardYoungTableaux ν.1 : ℝ) * w ν.1 := by
    intro ν
    rw [map_one, Matrix.trace_one, numStandardYoungTableaux, Nat.card_eq_fintype_card]
    ring
  rw [Finset.sum_congr rfl fun ν _ => key ν]
  exact hnorm (n + 1)

/-- **Branching of the weight gives consistency under the inclusion.**

The representation-theoretic half — corner decomposition of the diagonal sum,
`compress_seminormalRep_heckeIncl`, the corner↔addable reindexing — is weight-agnostic; the weight
enters only in the last line, as `hbranch`. -/
theorem wtraceW_incl (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (w : YoungDiagram → ℝ)
    (hbranch : ∀ ν : YoungDiagram,
      (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, w (addCellOrSelf ν s.1)) = w ν)
    (m : ℕ) (y : Hecke ℝ q q⁻¹ m) :
    wtraceW q hq0 hq2 w (m + 1) (heckeIncl ℝ q q⁻¹ m y) = wtraceW q hq0 hq2 w m y := by
  classical
  rw [wtraceW_apply, wtraceW_apply]
  set F : {ν : YoungDiagram // ν.cells.card = m + 1} → (ℕ × ℕ) → ℝ :=
    fun ν c => w (addCellOrSelf ν.1 c) * (seminormalRep q hq0 hq2 m ν.2 y).trace with hF
  have step : ∀ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
      w L.1 * (seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y)).trace
        = ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            F ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := by
    intro L
    have hpos : 0 < L.1.cells.card := by rw [L.2]; omega
    rw [trace_eq_sum_compress hpos, Finset.mul_sum]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [hF]
    have hadd : addCellOrSelf (eraseCorner L.1 c.1 c.2) c.1 = L.1 := by
      rw [addCellOrSelf_of (isAddableCell_eraseCorner c.1 c.2), addCell_eraseCorner]
    simp only [hadd]
    rw [compress_seminormalRep_heckeIncl hq0 hq2 m L.2 c.1 c.2
      (card_eraseCorner_of_card c.1 c.2 L.2) y]
  calc ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        w L.1 * (seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y)).trace
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
          ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            F ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := Finset.sum_congr rfl fun L _ => step L
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, F ν s.1 :=
        sum_corner_eq_sum_addable (m + 1) F
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          w ν.1 * (seminormalRep q hq0 hq2 m ν.2 y).trace := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [hF]
        simp only
        rw [← Finset.sum_mul, hbranch ν.1]

/-- The Markov condition, in the `genMat` form the corner assembly produces, gives the
`MarkovTraceFamily` Markov axiom. -/
theorem wtraceW_markov (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (w : YoungDiagram → ℝ) (z : ℝ)
    (hmarkov : ∀ (m : ℕ) (y : Hecke ℝ q q⁻¹ m),
      (∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
          w L.1 * ((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace)
        = z * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
            w ν.1 * (seminormalRep q hq0 hq2 m ν.2 y).trace)
    (m : ℕ) (y : Hecke ℝ q q⁻¹ m) :
    wtraceW q hq0 hq2 w (m + 1)
        (heckeIncl ℝ q q⁻¹ m y * Hecke.σ ℝ q q⁻¹ (m + 1) (Fin.last m))
      = z * wtraceW q hq0 hq2 w m y := by
  rw [wtraceW_apply, wtraceW_apply, ← hmarkov m y]
  refine Finset.sum_congr rfl fun L _ => ?_
  rw [map_mul, seminormalRep_last q hq0 hq2 L.2]

/-- **Any weight with normalisation, branching and the Markov condition is a Markov trace.** -/
noncomputable def markovTraceOfWeight (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (w : YoungDiagram → ℝ) (z : ℝ)
    (hnorm : ∀ n : ℕ, (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
      (numStandardYoungTableaux ν.1 : ℝ) * w ν.1) = 1)
    (hbranch : ∀ ν : YoungDiagram,
      (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, w (addCellOrSelf ν s.1)) = w ν)
    (hmarkov : ∀ (m : ℕ) (y : Hecke ℝ q q⁻¹ m),
      (∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
          w L.1 * ((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace)
        = z * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
            w ν.1 * (seminormalRep q hq0 hq2 m ν.2 y).trace) :
    HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ z where
  tr := wtraceW q hq0 hq2 w
  tr_one := wtraceW_one q hq0 hq2 w hnorm
  tr_cyclic := wtraceW_cyclic q hq0 hq2 w
  tr_incl := wtraceW_incl q hq0 hq2 w hbranch
  tr_markov := wtraceW_markov q hq0 hq2 w z hmarkov

end SeminormalRep
end QOU.SchurWeyl
