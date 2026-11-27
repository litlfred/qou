import BraidKnotOctonion.A5LeastHyperbolicChi
import MathlibExt.VoltageLift

/-!
# `QOU.BringsSurface.A5VoltageMapChi` — the `χ ≤ −6` bound for a lifted triangulation

Bean `qou-yslf`, parent `qou-qhcr`.

`chi_le_neg_six_of_A5_map` asks for an `A₅`-map with four properties: free on edges, free on
faces, cyclic vertex stabilisers, connected. For a map obtained by lifting a base map along
`A₅`-valued voltages (`MathlibExt.VoltageLift`), two of them hold automatically:

* free on edges: `lift_edges_free`;
* cyclic vertex stabilisers: `lift_vertex_stabilizer_isCyclic`.

So `chi_le_neg_six_of_A5_voltage_map` needs only the two properties that belong to the base
triangulation and its monodromy: free on faces (every branch value is a vertex) and connected (the
monodromy generates `A₅`). Those two, and the existence of the base triangulation with its
monodromy (Radó's theorem plus covering theory), are what remains of `qou-yslf`.

No `sorry`, no axiom, no `native_decide`.
-/

namespace QOU.BringsSurface.A5VoltageMapChi

open MulAction Equiv
open QOU.RiemannSurface.CombinatorialMapQuotient QOU.RiemannSurface.MapGenusNonneg
  QOU.RiemannSurface.CombinatorialMapEuler QOU.RiemannSurface.VoltageLift
  QOU.BringsSurface.A5LeastHyperbolicChi

abbrev A5 := alternatingGroup (Fin 5)

variable {E : Type*} [Fintype E] [DecidableEq E] [Nonempty E]

instance : Fintype (Lift A5 E) := inferInstanceAs (Fintype (A5 × E))
instance : DecidableEq (Lift A5 E) := inferInstanceAs (DecidableEq (A5 × E))
instance : Nonempty (Lift A5 E) := inferInstanceAs (Nonempty (A5 × E))

/-- **`χ ≤ −6` for a lifted triangulation.** Let `(σ, α)` be a map on base darts `E`, with
`A₅`-valued voltages `νσ`, `να` (`να` inverse-symmetric along `α`). If the lifted map is
connected, `A₅` acts freely on its faces, and it is hyperbolic, then its Euler characteristic is
at most `−6`. Edge freeness and cyclic vertex stabilisers are not hypotheses: they follow from
the lift. -/
theorem chi_le_neg_six_of_A5_voltage_map
    (σ α : Perm E) (νσ να : E → A5)
    (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x) (hν : ∀ x, να (α x) = (να x)⁻¹)
    (hconn : orbits (liftPerm σ νσ) (liftPerm α να) = 1)
    (hFA : letI := cycleAction ((liftPerm_equivariant σ νσ).mul (liftPerm_equivariant α να))
      ∀ (g : A5) (f : Cycles (liftPerm σ νσ * liftPerm α να)), g • f = f → g = 1)
    (hχ2 : (numCycles (liftPerm σ νσ) : ℤ) - numCycles (liftPerm α να)
      + numCycles (liftPerm σ νσ * liftPerm α να) ≤ -2) :
    (numCycles (liftPerm σ νσ) : ℤ) - numCycles (liftPerm α να)
      + numCycles (liftPerm σ νσ * liftPerm α να) ≤ -6 :=
  chi_le_neg_six_of_A5_map (liftPerm σ νσ) (liftPerm α να)
    (liftPerm_involution α να hinv hν) (liftPerm_fixedPointFree α να hfix) hconn
    A5 (MulEquiv.refl _) (liftPerm_equivariant σ νσ) (liftPerm_equivariant α να)
    (fun g e he => lift_edges_free α να hinv hν hfix g e he) hFA
    (fun v => lift_vertex_stabilizer_isCyclic σ νσ v) hχ2

end QOU.BringsSurface.A5VoltageMapChi
