/-
# GAP-A-4: the A=3 Δ_λ magnitude from the coordination-graph edge structure
# (jet-filtration DEPTH), NOT the brane-tower LEVEL — a braid-order obstruction.

Companion to `QOU.MassTheory.BorromeanMagnitudeLift` (#4364) and the three-walls
consolidation (2026-07-26).  #4364 lifted the derived A=3 Borromean 3-body cluster
to the `H₉` joint-trace level via width-3 cabling of the word `(Δ_A·Δ_B⁻¹)³`,
reaching `c₃ = E₀·κ·h⁴ = +0.297 MeV = 0.63× μ₃` (`μ₃ = +0.4708`,
`AdditiveResidualSimplex` #4320) — a `~1.6×` NEAR-MISS.  `lift_is_coefficient_ratio`
(#4364) proved a LEVEL lift is a pure coefficient rescale (the shared `h⁴` cancels),
and the three-walls audit closed every LEVEL/WIDTH route:

* the geometric q-Plancherel weight `W_λ = d_q²/D²` **overshoots** ~30× (#4392, S⁴=1
  ⇒ no other geometric measure);
* the derived color cable width `w = 3` gives **exactly** #4364's `H₉` near-miss;
* the one alternate level rule `n★ = ℓ·n₀+k` (`conj:brane-level-selection`) is a
  refuted overshoot (10⁵–10⁷ %).

So the missing `r* = μ₃ / 0.297 = 1.585×` is **not** any derived LEVEL.  This file
attacks the LAST un-excluded reading (GAP-A-4): the **coordination-graph edge
structure** (the inter-nucleon bond set), NOT the tower level.

## The structural finding (proved here, 0-fit, forward) — and the WALL it hits

`#4364`'s cabled word `(Δ_A·Δ_B⁻¹)³` uses **only two** of the three cable-pairs:
`Δ_A` bonds cables `{0,1}`, `Δ_B` bonds cables `{1,2}`.  The non-adjacent bond
`{0,2}` is **absent**.  A braid **linearly orders** its strands, so the coordination
graph realizable by *adjacent* block-transpositions is the **path** `P₃`
(`A−1 = 2` edges), NOT the physical triton's complete coordination graph `K₃`
(`C(A,2) = 3` edges: every nucleon pair bonded).  The missing third edge `{0,2}` is
the braid-linear-order obstruction — a candidate *structural* source for the
`~1.585×`, if the 3-body coefficient scaled with the bond count.

* `pathEdges A = A − 1`, `completeEdges A = C(A,2)`; at `A = 3` the values are `2`
  and `3` and the **edge ratio is `completeEdges 3 / pathEdges 3 = 3/2`**
  (`edge_ratio_A3`).  This is the forward-derived, 0-fit candidate factor
  (`3/2 = 1.5`, converging with #4392's own both-Σ=1 fit-trap value `1.504`, ~5 %
  short of `r* ≈ 1.585`).

**But the edge-count factor has NO Brunnian-order-preserving braid realization**
(companion probe `brane_tower_level_coordination_edge_probe.py`, 0 fit): adding the
third bond `Δ_C = (1 2)(0 1)(1 2)` as a genuine link (`triangle` word `(Δ_A·Δ_B⁻¹·Δ_C)³`)
**breaks** the Brunnian order-suppression — the measured leading `h`-exponent drops
from `4.098` (path, `O(h⁴)`) to `1.776` (`O(h²)`), and the magnitude **overshoots
~400×** with a flipped sign (`c₃ = −189 MeV`): the now-non-trivial `{0,2}` sub-link
contributes at `O(h²)`.  The bar-balanced symmetrization (`cyclic` word
`(Δ_A·Δ_B⁻¹)(Δ_B·Δ_C⁻¹)(Δ_C·Δ_A⁻¹)`) instead **cancels to `0`** (`c₃ ≈ 10⁻¹⁴`).
So there is **no** braid word that adds the third coordination edge while keeping the
`O(h⁴)` Brunnian order *and* scaling by `3/2`.  The `3/2` edge count is a
graph-combinatorial fact that does **not** translate to a `3/2` amplitude — the
`lift_is_coefficient_ratio` (#4364) cancellation needs a **shared `h⁴`**, which the
order-breaking third bond destroys.  **Verdict: WALL(scope-a).**

## Honesty (STRICT anti-fit, §"Axiomatization is NOT a Proof")

The proposition "the 3-body coefficient scales *linearly* with the coordination
edge count" is **NOT proved** — it is the genuine open input, and the companion
probe **refutes its premise at the braid level** (no order-preserving realization).
Per §3b-cond it is axiomatised as a `class` carrying that RULE as an explicit
hypothesis field; the conditional theorem `fullCoordAmplitude_eq` *derives* the
full-coordination coefficient from it (no `sorry`) — a conditional result, whose
premise the compute shows does not hold (conditional-proved ≠ premise-established).
The measured path value and orders enter only as explicit hypotheses, so `μ₃` is
never inverted.  `edge_scaling_near_miss` records that even *granting* the rule the
`3/2` arithmetic does not close `= μ₃`; `edge_reweight_requires_brunnian` records the
measured order-break that voids the rule's premise.  Nothing wired.

Base ring (§7c): `ℝ` — archimedean magnitude/ordering facts (a numeric value `≠` a
numeric target, positive coefficients).

## References

- [leitner2026] §mass-theory/binding-manybody-jet-filtration (`conj:binding-manybody-eq-jet-filtration`)
- [milnor1954] https://doi.org/10.2307/1969685  (Milnor link invariants; Brunnian μ̄₁₂₃)
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-! ### Coordination-graph edge counts: braid-realizable path `P₃` vs physical `K₃` -/

/-- The edge count of the **path** `P_A` on `A` nucleons — the coordination graph
realizable by *adjacent* block-transpositions in a braid (strands are linearly
ordered).  `|E(P_A)| = A − 1`.  This is what `#4364`'s `(Δ_A·Δ_B⁻¹)³` realizes
(`Δ_A : {0,1}`, `Δ_B : {1,2}`; the non-adjacent bond `{0,2}` is absent). -/
def pathEdges (A : ℕ) : ℕ := A - 1

/-- The edge count of the **complete** coordination graph `K_A` — every nucleon
pair bonded, the physical light-nucleus coordination.  `|E(K_A)| = C(A,2)`. -/
def completeEdges (A : ℕ) : ℕ := A.choose 2

/-- Path edges at `A = 3`: the two adjacent bonds `{0,1}`, `{1,2}`. -/
theorem pathEdges_three : pathEdges 3 = 2 := rfl

/-- Complete edges at `A = 3`: all three pairs `{0,1}`, `{1,2}`, `{0,2}`. -/
theorem completeEdges_three : completeEdges 3 = 3 := rfl

/-- **The braid-order gap at A = 3.**  The complete triton coordination graph `K₃`
has `3` edges but the braid-realizable path `P₃` has only `2`: the non-adjacent
`{0,2}` bond is the missing edge.  So `completeEdges 3 = pathEdges 3 + 1`. -/
theorem braid_order_gap_A3 : completeEdges 3 = pathEdges 3 + 1 := rfl

/-- **The forward-derived edge ratio at A = 3** (as reals): `|E(K₃)|/|E(P₃)| = 3/2`.
This is the 0-fit candidate amplitude factor for the missing bond — derived from the
graph structure, never from `μ₃`. -/
theorem edge_ratio_A3 :
    (completeEdges 3 : ℝ) / (pathEdges 3 : ℝ) = 3 / 2 := by
  simp only [completeEdges, pathEdges]
  norm_num

/-! ### Level magnitude shape (reused from #4364): `c₃ = E₀ · h⁴ · κ` -/

/-- The physical 3-body magnitude at a coefficient `κ`: `E₀ · h⁴ · κ` (#4364's
`levelMagnitude`; a level/edge re-weight changes `κ` only, `h⁴` is invariant).
Generic over `[CommRing R]` (§7c): it is a pure ring identity; the numeric
verdict theorems specialise it to `ℝ`. -/
def levelMagnitude {R : Type*} [CommRing R] (E0 h κ : R) : R := E0 * (h ^ 4 * κ)

/-- Re-weighting the path coefficient `κ_P` by the edge ratio `ρ = 3/2` scales the
magnitude by exactly `ρ` — the `E₀·h⁴` cancels (the #4364 coefficient-ratio law,
specialised to an edge re-weight). -/
theorem edge_reweight_is_ratio {R : Type*} [CommRing R] {E0 h κP ρ : R} :
    levelMagnitude E0 h (ρ * κP) = ρ * levelMagnitude E0 h κP := by
  unfold levelMagnitude; ring

/-! ### §3b-cond conditional class: the edge-scaling RULE is the open hypothesis -/

/-- **Conjecture class (`conj:binding-manybody-eq-jet-filtration`, edge-scaling
reading).**  Axiomatises the *open* rule that the irreducible 3-body coefficient
scales **linearly with the coordination edge count** (bond channels), together with
the derived path coefficient `κ_P` (`#4364`'s `H₉` value) and the derived edge ratio
`ρ`.  The `ruleLinear` field is the conjecture's content — that `κ` of the full
coordination graph is `ρ · κ_P`.  Having an instance is the conjecture; the theorem
below is proved *from* it (no `sorry`).

This is honest §3b-cond structure: the RULE `κ_full = ρ · κ_P` is NOT proved (a
coefficient tuned to close would be a FIT); it is carried as a hypothesis, and the
`fullCoordAmplitude_eq` corollary derives the full-coordination magnitude from it. -/
class CoordinationEdgeAmplitude (R : Type*) [CommRing R] where
  /-- Electron-mass ρ_F scale factor `E₀`. -/
  E0 : R
  /-- Hecke `h = q − q⁻¹`. -/
  h : R
  /-- Derived path (`P₃`, 2-edge) `h⁴`-coefficient — `#4364`'s `H₉` value. -/
  kappaPath : R
  /-- Derived edge ratio `ρ = |E(K₃)|/|E(P₃)|` (= `3/2`, `edge_ratio_A3`). -/
  rho : R
  /-- The full-coordination `h⁴`-coefficient. -/
  kappaFull : R
  /-- **The open RULE (the conjecture's content):** the full-coordination 3-body
      coefficient is the path coefficient scaled by the edge ratio. -/
  ruleLinear : kappaFull = rho * kappaPath

/-- **Conditional corollary (proved from the class, no `sorry`):** the
full-coordination 3-body magnitude equals the edge ratio times the derived path
magnitude.  This is a *derivation from the class hypothesis*, not a proof of the
rule; the rule (`ruleLinear`) is the open input. -/
theorem fullCoordAmplitude_eq {R : Type*} [CommRing R]
    [C : CoordinationEdgeAmplitude R] :
    levelMagnitude C.E0 C.h C.kappaFull = C.rho * levelMagnitude C.E0 C.h C.kappaPath := by
  unfold levelMagnitude
  rw [C.ruleLinear]; ring

/-! ### Honest scope-(a) verdict: the `3/2` edge factor does NOT close `= μ₃` -/

/-- Closure predicate: the A=3 magnitude closes iff the full-coordination magnitude
equals `μ₃`.  (`κ_full` fixed and derived; `μ₃` the target — a `κ` tuned to satisfy
it would be a FIT.) -/
def MagnitudeCloses (E0 h κFull μ₃ : ℝ) : Prop := levelMagnitude E0 h κFull = μ₃

/-- **NEAR-MISS (scope-a): the `3/2` edge-reweight of `#4364`'s `0.297` gives
`0.4455 ≠ 0.4708 = μ₃`.**  Stated with the derived path value `0.297` and the derived
edge ratio `3/2` as explicit hypotheses, so `μ₃` is never inverted.  The
full-coordination magnitude is `(3/2)·0.297 = 0.4455`, which is `≠ 0.4708`: the
edge-count factor `3/2 = 1.5` is `~5 %` short of the needed `r* ≈ 1.585`. -/
theorem edge_scaling_near_miss {E0 h κPath : ℝ}
    (hPath : levelMagnitude E0 h κPath = (0.297 : ℝ)) :
    ¬ MagnitudeCloses E0 h ((3 / 2 : ℝ) * κPath) (0.4708 : ℝ) := by
  unfold MagnitudeCloses
  rw [edge_reweight_is_ratio, hPath]
  norm_num

/-- **The residual after the edge factor is still positive** (`0.4708 − 0.4455 =
0.0253 > 0`): even *granting* the (refuted) rule, the full-coordination `K₃` factor
`3/2` undershoots `μ₃`.  So the edge count alone never closes GAP-A-4. -/
theorem edge_scaling_residual_pos {E0 h κPath : ℝ}
    (hPath : levelMagnitude E0 h κPath = (0.297 : ℝ)) :
    0 < (0.4708 : ℝ) - levelMagnitude E0 h ((3 / 2 : ℝ) * κPath) := by
  rw [edge_reweight_is_ratio, hPath]
  norm_num

/-- **The WALL: the edge-scaling rule's premise is voided by the measured
order-break.**  A `3/2` coefficient rescale is valid only if the third-bond word
keeps the **shared `h⁴`** that `lift_is_coefficient_ratio` (#4364) cancels — i.e.
stays Brunnian at leading order `4`.  The companion probe MEASURES the triangle
word `(Δ_A·Δ_B⁻¹·Δ_C)³` to have leading `h`-exponent `1.776` (`O(h²)`, carried here
as the hypothesis `hOrd`), which is `≠ 4`.  Hence the third bond does **not** stay
Brunnian, the shared-`h⁴` premise fails, and the `3/2` edge rescale does not apply:
the coordination-edge reading **walls (scope-a)**.  (`μ₃` never appears — a pure
order fact.) -/
theorem edge_reweight_requires_brunnian {ordTriangle : ℝ}
    (hOrd : ordTriangle = (1.776 : ℝ)) : ordTriangle ≠ (4 : ℝ) := by
  rw [hOrd]; norm_num

end QOU.MassTheory
