import BraidKnotOctonion.GenusFourFromEquivariantMap

/-!
# `QOU.BringsSurface.A5LeastHyperbolicChi` — `−6` is the largest hyperbolic `χ` of an `A₅`-surface

Bean `qou-qhcr` (the branch-point count 6 of the `χ = −6` chain); siblings `qou-w8es` (G3),
`qou-khmu` (G2), `qou-m3tr` / `qou-yslf` (M3).

## What this file adds

The genus-4 capstones (`genus_eq_four_of_cellular`, `chi_eq_neg_six_of_equivariant_map`) use
three inputs besides the cell structure:

1. an `A₅`-action (the fibre group of `klein-bring-icosahedral-bridge`, lifted to the base: G2);
2. `H¹ = 2W` with `W` an irreducible `A₅`-representation (G3), which gives the genus window;
3. an `S₅`-action, which removes genus 5 from that window.

This file shows that **inputs 2 and 3 can be traded for one extremal statement**:

> Among closed connected surfaces of negative Euler characteristic that carry an `A₅`-action of the
> kind the capstones consider (free on edges and faces, cyclic vertex stabilisers), the largest
> Euler characteristic is `−6`.

The upper bound `χ ≤ −6` is proved here for every such surface (`chi_le_neg_six_of_A5_map`). It
uses only Riemann–Hurwitz (already proved cellularly) and the element orders `1, 2, 3, 5` of `A₅`:
no representation theory, no `S₅`, no genus window. Attainment is the existing
`genus_four_attained` (signature `(0; 2, 5, 5)`); an explicit `A₅`-map with `χ = −6` is recorded in
the probe `computations/probes/a5_least_hyperbolic_chi_probe.py`.

Equivalently, in orbifold terms: `χ = 60 · χ_orb(X/A₅)`, and among hyperbolic signatures with
periods in `{2, 3, 5}` the one closest to zero is `(0; 2, 5, 5)` with `χ_orb = −1/10`. So the `6`
of the chain is `60 / 10`.

## What this does and does not settle

* It does **not** derive the `A₅`-action on the base (G2 stays open).
* It replaces G3 + `S₅` by a **selection principle**: "the base is the least hyperbolic surface
  carrying the action" (maximal `χ < 0`, equivalently minimal hyperbolic area). Whether a QOU axiom
  supplies that principle is an owner question; nothing here asserts it. The principle is stated
  as a hypothesis-free extremal theorem, so the reader can see exactly what it would buy.
* Hyperbolicity (`χ < 0`, i.e. `g ≥ 2`) is the input `hχ2`; per `qou-qhcr` §5 it comes from
  Step 4 (`g ≥ 1`) plus observability (`χ ≠ 0`).
* The bound is sharp only as a bound on `χ`; it says nothing about which surface attains it.
  (Bring's curve does; so does the great-dodecahedron map, which is the same surface.)

No `sorry`, no axiom, no `native_decide`.

Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, 2nd ed., §V.1 (Riemann–Hurwitz).
-/

namespace QOU.BringsSurface.A5LeastHyperbolicChi

open MulAction Equiv
open QOU.RiemannSurface.CombinatorialMapQuotient QOU.RiemannSurface.MapGenusNonneg
  QOU.RiemannSurface.CombinatorialMapEuler QOU.RiemannSurface.GermStabiliserCyclic
  QOU.BringsSurface.IrreducibleH1ForcesGenusFour QOU.BringsSurface.RiemannHurwitzCellular
  QOU.BringsSurface.GenusFourFromGermStabilisers QOU.BringsSurface.GenusFourFromEquivariantMap

set_option linter.unusedSectionVars false

/-! ## 1. Arithmetic: `A₅` has no hyperbolic genus below 4 -/

/-- **Arithmetic core.** An `A₅`-action on a closed surface of genus `g ≥ 2` (Riemann–Hurwitz
with branch contributions `60 − 60/m`, `m ∈ {1,2,3,5}`) has `g ≥ 4`. -/
theorem a5_hyperbolic_genus_ge_four (g h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, A5Branch t) (hRH : RH 60 g h ts) (hg : 2 ≤ g) : 4 ≤ g := by
  have h23 := a5_genus_ne_two_three g h ts hts hRH
  omega

/-- The same in Euler-characteristic form: `χ < 0` forces `χ ≤ −6`. -/
theorem a5_chi_le_neg_six (g h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, A5Branch t) (hRH : RH 60 g h ts) (hχ : (2 : ℤ) - 2 * g < 0) :
    (2 : ℤ) - 2 * g ≤ -6 := by
  have := a5_hyperbolic_genus_ge_four g h ts hts hRH (by omega)
  omega

/-- **Attained.** Genus 4 is reached, by the signature `(0; 2, 5, 5)` (`30 + 48 + 48 = 126`). So
`−6` is the maximum, not merely a bound. -/
theorem a5_chi_neg_six_attained : RH 60 4 0 [30, 48, 48] ∧ ∀ t ∈ [30, 48, 48], A5Branch t := by
  refine ⟨genus_four_attained.1, ?_⟩
  intro t ht
  simp only [List.mem_cons, List.not_mem_nil, or_false] at ht
  unfold A5Branch
  omega

/-- **Every hyperbolic genus up to 8 that the `A₅` arithmetic allows.** The admissible genera
`2 ≤ g ≤ 8` are exactly `4, 5, 6`. So `4` is least, and the next two are the ones `S₅` (removes
5) and the dimension bound (removes 6 only with irreducibility) argue about in the capstones. -/
theorem a5_hyperbolic_genus_small (g h : ℕ) (ts : List ℕ)
    (hts : ∀ t ∈ ts, A5Branch t) (hRH : RH 60 g h ts) (hg : 2 ≤ g) (hg8 : g ≤ 8) :
    g = 4 ∨ g = 5 ∨ g = 6 := by
  obtain ⟨a, b, c, hs⟩ := a5_sum ts hts
  unfold RH at hRH
  interval_cases g <;> omega

/-! ## 2. Cellular form: one group, no genus window -/

/-- **Genus `≥ 4` from an `A₅`-cell structure.** As `genus_eq_four_of_cyclic_stabilisers`, but
for the `A₅`-action alone and with neither `H¹ = 2W` nor `S₅`: a hyperbolic surface with such an
action has genus at least 4. -/
theorem genus_ge_four_of_cellular_A5
    (GA : Type*) [Group GA] [Fintype GA] (eA : GA ≃* alternatingGroup (Fin 5))
    (V E F : Type*) [MulAction GA V] [MulAction GA E] [MulAction GA F]
    [Fintype V] [Fintype E] [Fintype F]
    [Fintype (Quotient (orbitRel GA V))] [Fintype (Quotient (orbitRel GA E))]
    [Fintype (Quotient (orbitRel GA F))]
    [∀ v : V, Fintype (stabilizer GA v)] [∀ e : E, Fintype (stabilizer GA e)]
    [∀ f : F, Fintype (stabilizer GA f)]
    (hE : ∀ e : E, Fintype.card (stabilizer GA e) = 1)
    (hF : ∀ f : F, Fintype.card (stabilizer GA f) = 1)
    (hcyc : ∀ v : V, IsCyclic (stabilizer GA v))
    (g h : ℕ)
    (hX : ((Fintype.card V : ℤ) - Fintype.card E + Fintype.card F) = 2 - 2 * g)
    (hY : ((Fintype.card (Quotient (orbitRel GA V)) : ℤ)
          - Fintype.card (Quotient (orbitRel GA E)) + Fintype.card (Quotient (orbitRel GA F)))
          = 2 - 2 * h)
    (hg : 2 ≤ g) : 4 ≤ g := by
  have hR := rh_of_cellular GA V E F hE hF g h hX hY
  rw [card_of_A5 eA] at hR
  refine a5_hyperbolic_genus_ge_four g h _ ?_ hR hg
  intro t ht
  simp only [List.mem_map, Finset.mem_toList, Finset.mem_univ, true_and] at ht
  obtain ⟨ω, rfl⟩ := ht
  haveI := hcyc ω.out
  exact a5Branch_of_stab _ _ rfl (card_cyclic_of_A5 eA (stabilizer GA ω.out))

/-! ## 3. Map form: `χ ≤ −6` for every hyperbolic `A₅`-map -/

/-- **`χ ≤ −6` from an `A₅`-equivariant connected map.** A connected combinatorial map
(darts `D`, rotation `σ`, fixed-point-free involution `α`) with an `A₅`-action commuting with
`σ, α`, free on edges and faces, with cyclic vertex stabilisers, and with `χ ≤ −2` (hyperbolic),
has `χ ≤ −6`. Compare `chi_eq_neg_six_of_equivariant_map`, which needs in addition an `S₅`-action
and the window `χ ∈ {0, −4, −6, −8}` from `H¹ = 2W`. -/
theorem chi_le_neg_six_of_A5_map
    {D : Type*} [Fintype D] [DecidableEq D] [Nonempty D]
    (σ α : Perm D) (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x) (hconn : orbits σ α = 1)
    (GA : Type*) [Group GA] [Fintype GA] [MulAction GA D]
    (eA : GA ≃* alternatingGroup (Fin 5))
    (hσA : Equivariant σ GA) (hαA : Equivariant α GA)
    (hEA : letI := cycleAction hαA; ∀ (g : GA) (e : Cycles α), g • e = e → g = 1)
    (hFA : letI := cycleAction (hσA.mul hαA); ∀ (g : GA) (f : Cycles (σ * α)), g • f = f → g = 1)
    (hcycA : letI := cycleAction hσA; ∀ v : Cycles σ, IsCyclic (stabilizer GA v))
    (hχ2 : (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) ≤ -2) :
    (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) ≤ -6 := by
  classical
  obtain ⟨g, hg⟩ := exists_genus_nonneg σ α hinv hfix hconn
  obtain ⟨hA, hYA⟩ := quotient_genus hσA hαA hinv hfix hEA hconn
  have hX : ((Nat.card (Cycles σ) : ℕ) : ℤ) - (Nat.card (Cycles α) : ℕ)
      + (Nat.card (Cycles (σ * α)) : ℕ) = 2 - 2 * g := hg
  have hg2 : 2 ≤ g := by omega
  have h4 : 4 ≤ g := by
    letI iVA := cycleAction (G := GA) hσA
    letI iEA := cycleAction (G := GA) hαA
    letI iFA := cycleAction (G := GA) (hσA.mul hαA)
    simp only [Nat.card_eq_fintype_card] at hX hYA
    exact genus_ge_four_of_cellular_A5 GA eA
      (Cycles σ) (Cycles α) (Cycles (σ * α))
      (fun e => card_stabilizer_eq_one e (hEA · e))
      (fun f => card_stabilizer_eq_one f (hFA · f))
      hcycA g hA hX hYA hg2
  omega

end QOU.BringsSurface.A5LeastHyperbolicChi
