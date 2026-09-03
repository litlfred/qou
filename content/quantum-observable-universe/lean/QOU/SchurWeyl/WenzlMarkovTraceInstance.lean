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
| `realGen_of_sq_ne_one` | over `ℝ` the genericity hypothesis follows from `q² ≠ 1` |
| `wtraceW_ne_of_level_ne` | the same, as an inequality, needing only `q ≠ 0` and `q² ≠ 1` |

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
  formulation, not a better proof.  **Over `ℝ` this excludes nothing beyond `q² ≠ 1`** — see
  `realGen_of_sq_ne_one`, which discharges it.
* `r ≠ 0`.  At `r = 0` the bracket `[0]_Q` is the empty sum `0` and the normalisation
  `w_μ = s_μ / [r]_Q^{|μ|}` is undefined.
* `z_r` is a point of the **Wenzl lattice**.  Nothing here says a Markov trace exists at an
  arbitrary `z` off it — only that if one does and it sits at some `z_r`, it is this one.

## Base ring (§7c)

`ℝ` throughout, forced by `seminormalRep` / `seminormalParam`.  The generic content this file
first carried has been moved to where it belongs, so that the substrate→archimedean wall of §7c
falls on a **file** boundary: `ne_one_of_gen`, `levelBracket_ne_zero_of_gen`,
`wenzlMarkovParam_spec` and `level_unique_of_wenzlMarkovParam_eq` are generic `[Field R]` in
`WenzlWeightLevelR`, and `MarkovTraceFamily.param_eq` is generic `[CommRing K]` in
`MarkovTraceUnique`.  Note the last of those is *stronger* for having moved: stated over `ℝ` it
looked like a fact about this trace, and it is a fact about any Markov trace family over any
commutative ring.

LaTeX label: `thm:wenzl-markov-trace-instance`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset

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

/-! ## The level-`r` instance, and uniqueness at every level -/

/-- **The level-`r` Markov trace.**

`w = wenzlWeight r (q²)` at `z_r = Q^r / (q · [r]_Q)`, `Q = q²`.  The three weight inputs are
exactly the three theorems #5662 generalised: `sum_dim_wenzlWeight_eq_one`,
`sum_addable_wenzlWeight_all`, `markov_wenzlWeight`.  Nothing else is needed, and in particular no
level-specific argument appears — the level enters only through those three. -/
noncomputable def wenzlMarkovTrace (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) {r : ℕ} (hr : r ≠ 0) :
    HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ ((q ^ 2) ^ r / (q * levelBracket r (q ^ 2))) :=
  markovTraceOfWeight q hq0 hq2 (wenzlWeight r (q ^ 2)) _
    (fun n => sum_dim_wenzlWeight_eq_one (q ^ 2) (pow_ne_zero 2 hq0) hgen
      (levelBracket_ne_zero_of_gen hgen hr) (ne_one_of_gen hgen) n)
    (fun ν => sum_addable_wenzlWeight_all (q ^ 2) (pow_ne_zero 2 hq0) hgen
      (levelBracket_ne_zero_of_gen hgen hr) (ne_one_of_gen hgen) ν)
    (fun _ y => markov_wenzlWeight q hq0 hq2 hgen hr y)

theorem wenzlMarkovTrace_tr (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) {r : ℕ} (hr : r ≠ 0) :
    (wenzlMarkovTrace q hq0 hq2 hgen hr).tr = wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) := rfl

/-- **Uniqueness of the Markov trace at every integer level `r`.**

*Every* Markov trace on the Hecke tower whose parameter is the level-`r` Wenzl parameter is the
`wenzlWeight r (q²)`-weighted seminormal trace.  At `r = 2` this is
`MarkovTraceInstance.eq_wtrace_of_markov` (see `wenzlMarkovTrace_two_tr`).

The uniqueness argument is `markovTrace_unique`, unchanged and level-free; what makes the statement
available at level `r` is `wenzlMarkovTrace`, the instance. -/
theorem eq_wenzlWtrace_of_markov (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) {r : ℕ} (hr : r ≠ 0)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ ((q ^ 2) ^ r / (q * levelBracket r (q ^ 2))))
    (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    T.tr n x = wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) n x :=
  HeckeCoset.markovTrace_unique T (wenzlMarkovTrace q hq0 hq2 hgen hr) n x

/-- **Conservativity: at `r = 2` the level-`r` trace is `wtrace`**, the convention-D object of
`MarkovTraceInstance` — pointwise, on every `H_n(q)`.  A generalisation that does not contain its
own special case is a different object wearing the same name; this is the evidence that this one
does. -/
theorem wenzlMarkovTrace_two_tr (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq21 : q ^ 2 + 1 ≠ 0)
    (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    wtraceW q hq0 hq2 (wenzlWeight 2 (q ^ 2)) n x = wtrace q hq0 hq2 n x := by
  rw [wtraceW_apply, wtrace_apply]
  exact Finset.sum_congr rfl fun ν _ =>
    by rw [wenzlWeight_two_eq_ocneanuWeight q hq0 hq21]

end SeminormalRep

/-! ## The level is a functional invariant of the trace -/

/-- **Distinct levels give distinct traces.**

If the level-`r` and level-`s` weighted seminormal traces agree on every `H_n(q)` — indeed, if they
agree at the single element `σ₀ ∈ H_1(q)` — then `r = s`.

This is the composition the two uniqueness statements admit: `param_eq` reads the parameter off the
trace, and `level_unique_of_markovParameter` reads the level off the parameter.  Neither alone says
this.  In particular the level is not extra bookkeeping attached to the trace; it is **recoverable
from one value of it**. -/
theorem level_unique_of_wenzlMarkovTrace_eq (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) {r s : ℕ} (hr : r ≠ 0) (hs : s ≠ 0)
    (h : SeminormalRep.wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) 1
          (Hecke.σ ℝ q q⁻¹ 1 (Fin.last 0))
        = SeminormalRep.wtraceW q hq0 hq2 (wenzlWeight s (q ^ 2)) 1
          (Hecke.σ ℝ q q⁻¹ 1 (Fin.last 0))) : r = s := by
  have hpr := (SeminormalRep.wenzlMarkovTrace q hq0 hq2 hgen hr).param_eq
  have hps := (SeminormalRep.wenzlMarkovTrace q hq0 hq2 hgen hs).param_eq
  rw [SeminormalRep.wenzlMarkovTrace_tr q hq0 hq2 hgen hr] at hpr
  rw [SeminormalRep.wenzlMarkovTrace_tr q hq0 hq2 hgen hs] at hps
  exact level_unique_of_wenzlMarkovParam_eq hq0 hgen hr hs (by rw [← hpr, ← hps]; exact h)

/-! ## Over `ℝ` the genericity hypothesis is not a restriction -/

/-- **`hgen` is provable over `ℝ`**, from `q ≠ 0` and `q² ≠ 1` alone.

`Q = q²` is a *positive* real, and a positive real is a root of unity only by being `1`
(`k·log Q = 0` with `log Q ≠ 0` forces `k = 0`).  So the "`Q` is not a root of unity" hypothesis
carried through the whole level-`r` chain adds **nothing** over `ℝ` beyond `q² ≠ 1`.

This is worth stating because the scope notes on the level-`r` files read as though genericity were
a live restriction — "at a root of unity `H_n(q)` is not semisimple and partitions stop indexing the
irreducibles".  That is true of the *general* theory, and it is exactly why the hypothesis is there;
but over the real base ring the excluded locus is `{q² = 1}` and nothing else.  In particular it does
**not** exclude the substrate value: `q₀ ≈ 1.10998` has `q₀² ≈ 1.232 ≠ 1`, so the level-`r` Markov
trace exists there for every `r ≥ 1`.

Reading this the other way is the caution: it does not say the general-`Q` statements are stronger
than they look.  Over `ℂ`, or over a cyclotomic field, `hgen` is a real hypothesis and the level-`r`
weight genuinely fails without it.  What is vacuous is the *specialisation to `ℝ`*. -/
theorem realGen_of_sq_ne_one {q : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1 := by
  intro k hk h
  have hQ0 : (0 : ℝ) < q ^ 2 := by positivity
  have hlog : (k : ℝ) * Real.log (q ^ 2) = 0 := by
    rw [← Real.log_zpow, h, Real.log_one]
  have hlQ : Real.log (q ^ 2) ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one hQ0 hq2
  have hk0 : (k : ℝ) = 0 := by
    rcases mul_eq_zero.mp hlog with h1 | h2
    · exact h1
    · exact absurd h2 hlQ
  exact hk (by exact_mod_cast hk0)

/-- **Uniqueness at every level, over `ℝ`, with no genericity hypothesis.**

`eq_wenzlWtrace_of_markov` with `hgen` discharged by `realGen_of_sq_ne_one`. -/
theorem SeminormalRep.eq_wenzlWtrace_of_markov_real (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    {r : ℕ} (hr : r ≠ 0)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ ((q ^ 2) ^ r / (q * levelBracket r (q ^ 2))))
    (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    T.tr n x = SeminormalRep.wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) n x :=
  SeminormalRep.eq_wenzlWtrace_of_markov q hq0 hq2 (realGen_of_sq_ne_one hq0 hq2) hr T n x

/-- **Distinct levels give distinct traces** — the contrapositive, stated as the inequality it is,
and needing only `q ≠ 0` and `q² ≠ 1`.

The two traces already differ at the *single* element `σ₀ ∈ H_1(q)`.  So the level is not merely
determined by the whole functional: one evaluation separates every pair of levels. -/
theorem wtraceW_ne_of_level_ne (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {r s : ℕ}
    (hr : r ≠ 0) (hs : s ≠ 0) (hrs : r ≠ s) :
    SeminormalRep.wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) 1 (Hecke.σ ℝ q q⁻¹ 1 (Fin.last 0))
      ≠ SeminormalRep.wtraceW q hq0 hq2 (wenzlWeight s (q ^ 2)) 1
          (Hecke.σ ℝ q q⁻¹ 1 (Fin.last 0)) :=
  fun h => hrs (level_unique_of_wenzlMarkovTrace_eq q hq0 hq2
    (realGen_of_sq_ne_one hq0 hq2) hr hs h)

end QOU.SchurWeyl
