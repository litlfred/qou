import QOU.BringsSurface.RiemannHurwitzCellular
import QOU.RiemannSurface.GermStabiliserCyclic
import Mathlib.Analysis.Complex.Basic

/-!
# `QOU.BringsSurface.GenusFourFromGermStabilisers` — `hstabA` / `hstabS` discharged

Bean `qou-qhcr`. The capstone `genus_eq_four_of_cellular` took the hypotheses

* `hstabA`: every vertex stabiliser of the `A₅`-action has order `1, 2, 3` or `5`;
* `hstabS`: every vertex stabiliser of the `S₅`-action has order `1, …, 6`;

and the group orders `hA60`, `hS120`. Here they are **derived**:

* the orders come from isomorphisms `GA ≃* A₅`, `GS ≃* S₅`;
* the stabiliser orders come from **cyclicity** of the stabilisers, via the element orders of
  `A₅` and `S₅` (`card_cyclic_of_A5`, `card_cyclic_of_S5`, kernel `decide`);
* cyclicity comes from an effective germ action at the fixed point
  (`GermAction.isCyclic`, M1b, `qou-m1bg`).

`genus_eq_four_of_cyclic_stabilisers` assumes cyclic stabilisers;
`genus_eq_four_of_germ_stabilisers` assumes instead that each stabiliser acts effectively by
holomorphic (strictly differentiable) germs fixing its point.

## Still taken as given

* **The chart step (M2):** a point stabiliser of a holomorphic action on a Riemann surface acts
  by germs in a centred chart, effectively (identity theorem on the surface). It enters as
  `hgermA` / `hgermS`.
* **The cell structure (M3 steps 2–3):** `hEA hFA hES hFS hXA hYA hXS hYS`, as in the capstone.
  `QOU.RiemannSurface.CombinatorialMapQuotient` identifies the orbit counts in `hYA`/`hYS` with
  the cells of a quotient map, but does not discharge them.
* **`H¹ = 2W` with `W` irreducible (G2/G3):** enters as `hdim`, as in the capstone.

Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, §III.7.7 and §V.1.
-/

namespace QOU.BringsSurface.GenusFourFromGermStabilisers

open MulAction Filter Topology
open QOU.BringsSurface.RiemannHurwitzCellular
open QOU.RiemannSurface.GermStabiliserCyclic

theorem card_of_A5 {Γ : Type*} [Group Γ] [Fintype Γ] (e : Γ ≃* alternatingGroup (Fin 5)) :
    Fintype.card Γ = 60 := by
  rw [Fintype.card_congr e.toEquiv]; decide

theorem card_of_S5 {Γ : Type*} [Group Γ] [Fintype Γ] (e : Γ ≃* Equiv.Perm (Fin 5)) :
    Fintype.card Γ = 120 := by
  rw [Fintype.card_congr e.toEquiv]; decide

/-- **Genus 4 from cyclic stabilisers.** `genus_eq_four_of_cellular` with `hA60`, `hS120`,
`hstabA`, `hstabS` replaced by `GA ≅ A₅`, `GS ≅ S₅` and cyclicity of the vertex stabilisers. -/
theorem genus_eq_four_of_cyclic_stabilisers
    (GA GS : Type*) [Group GA] [Fintype GA] [Group GS] [Fintype GS]
    (eA : GA ≃* alternatingGroup (Fin 5)) (eS : GS ≃* Equiv.Perm (Fin 5))
    (VA EA FA VS ES FS : Type*)
    [MulAction GA VA] [MulAction GA EA] [MulAction GA FA]
    [MulAction GS VS] [MulAction GS ES] [MulAction GS FS]
    [Fintype VA] [Fintype EA] [Fintype FA] [Fintype VS] [Fintype ES] [Fintype FS]
    [Fintype (Quotient (orbitRel GA VA))] [Fintype (Quotient (orbitRel GA EA))]
    [Fintype (Quotient (orbitRel GA FA))]
    [Fintype (Quotient (orbitRel GS VS))] [Fintype (Quotient (orbitRel GS ES))]
    [Fintype (Quotient (orbitRel GS FS))]
    [∀ v : VA, Fintype (stabilizer GA v)] [∀ e : EA, Fintype (stabilizer GA e)]
    [∀ f : FA, Fintype (stabilizer GA f)]
    [∀ v : VS, Fintype (stabilizer GS v)] [∀ e : ES, Fintype (stabilizer GS e)]
    [∀ f : FS, Fintype (stabilizer GS f)]
    (hEA : ∀ e : EA, Fintype.card (stabilizer GA e) = 1)
    (hFA : ∀ f : FA, Fintype.card (stabilizer GA f) = 1)
    (hES : ∀ e : ES, Fintype.card (stabilizer GS e) = 1)
    (hFS : ∀ f : FS, Fintype.card (stabilizer GS f) = 1)
    (hcycA : ∀ v : VA, IsCyclic (stabilizer GA v))
    (hcycS : ∀ v : VS, IsCyclic (stabilizer GS v))
    (g hA hS : ℕ)
    (hXA : ((Fintype.card VA : ℤ) - Fintype.card EA + Fintype.card FA) = 2 - 2 * g)
    (hYA : ((Fintype.card (Quotient (orbitRel GA VA)) : ℤ)
          - Fintype.card (Quotient (orbitRel GA EA)) + Fintype.card (Quotient (orbitRel GA FA)))
          = 2 - 2 * hA)
    (hXS : ((Fintype.card VS : ℤ) - Fintype.card ES + Fintype.card FS) = 2 - 2 * g)
    (hYS : ((Fintype.card (Quotient (orbitRel GS VS)) : ℤ)
          - Fintype.card (Quotient (orbitRel GS ES)) + Fintype.card (Quotient (orbitRel GS FS)))
          = 2 - 2 * hS)
    (hg : 2 ≤ g) (hdim : g = 1 ∨ g = 3 ∨ g = 4 ∨ g = 5) : g = 4 :=
  genus_eq_four_of_cellular GA GS (card_of_A5 eA) (card_of_S5 eS) VA EA FA VS ES FS
    hEA hFA hES hFS
    (fun v => haveI := hcycA v; card_cyclic_of_A5 eA (stabilizer GA v))
    (fun v => haveI := hcycS v; card_cyclic_of_S5 eS (stabilizer GS v))
    g hA hS hXA hYA hXS hYS hg hdim

/-- **Genus 4 from germ actions at the fixed points.** As above, with cyclicity of each vertex
stabiliser derived from an effective germ action at its point (M1b). The germ actions are the
chart step and remain hypotheses. -/
theorem genus_eq_four_of_germ_stabilisers
    (GA GS : Type*) [Group GA] [Fintype GA] [Group GS] [Fintype GS]
    (eA : GA ≃* alternatingGroup (Fin 5)) (eS : GS ≃* Equiv.Perm (Fin 5))
    (VA EA FA VS ES FS : Type*)
    [MulAction GA VA] [MulAction GA EA] [MulAction GA FA]
    [MulAction GS VS] [MulAction GS ES] [MulAction GS FS]
    [Fintype VA] [Fintype EA] [Fintype FA] [Fintype VS] [Fintype ES] [Fintype FS]
    [Fintype (Quotient (orbitRel GA VA))] [Fintype (Quotient (orbitRel GA EA))]
    [Fintype (Quotient (orbitRel GA FA))]
    [Fintype (Quotient (orbitRel GS VS))] [Fintype (Quotient (orbitRel GS ES))]
    [Fintype (Quotient (orbitRel GS FS))]
    [∀ v : VA, Fintype (stabilizer GA v)] [∀ e : EA, Fintype (stabilizer GA e)]
    [∀ f : FA, Fintype (stabilizer GA f)]
    [∀ v : VS, Fintype (stabilizer GS v)] [∀ e : ES, Fintype (stabilizer GS e)]
    [∀ f : FS, Fintype (stabilizer GS f)]
    (hEA : ∀ e : EA, Fintype.card (stabilizer GA e) = 1)
    (hFA : ∀ f : FA, Fintype.card (stabilizer GA f) = 1)
    (hES : ∀ e : ES, Fintype.card (stabilizer GS e) = 1)
    (hFS : ∀ f : FS, Fintype.card (stabilizer GS f) = 1)
    (hgermA : ∀ v : VA, ∃ A : GermAction (stabilizer GA v) ℂ,
      ∀ s, A.act s =ᶠ[𝓝 0] id → s = 1)
    (hgermS : ∀ v : VS, ∃ A : GermAction (stabilizer GS v) ℂ,
      ∀ s, A.act s =ᶠ[𝓝 0] id → s = 1)
    (g hA hS : ℕ)
    (hXA : ((Fintype.card VA : ℤ) - Fintype.card EA + Fintype.card FA) = 2 - 2 * g)
    (hYA : ((Fintype.card (Quotient (orbitRel GA VA)) : ℤ)
          - Fintype.card (Quotient (orbitRel GA EA)) + Fintype.card (Quotient (orbitRel GA FA)))
          = 2 - 2 * hA)
    (hXS : ((Fintype.card VS : ℤ) - Fintype.card ES + Fintype.card FS) = 2 - 2 * g)
    (hYS : ((Fintype.card (Quotient (orbitRel GS VS)) : ℤ)
          - Fintype.card (Quotient (orbitRel GS ES)) + Fintype.card (Quotient (orbitRel GS FS)))
          = 2 - 2 * hS)
    (hg : 2 ≤ g) (hdim : g = 1 ∨ g = 3 ∨ g = 4 ∨ g = 5) : g = 4 :=
  genus_eq_four_of_cyclic_stabilisers GA GS eA eS VA EA FA VS ES FS hEA hFA hES hFS
    (fun v => by obtain ⟨A, hA⟩ := hgermA v; exact A.isCyclic hA)
    (fun v => by obtain ⟨A, hA⟩ := hgermS v; exact A.isCyclic hA)
    g hA hS hXA hYA hXS hYS hg hdim

end QOU.BringsSurface.GenusFourFromGermStabilisers
