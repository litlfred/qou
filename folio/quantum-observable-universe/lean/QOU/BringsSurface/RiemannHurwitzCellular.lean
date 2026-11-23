import Mathlib.GroupTheory.GroupAction.CardCommute
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import QOU.BringsSurface.IrreducibleH1ForcesGenusFour

/-!
# `QOU.BringsSurface.RiemannHurwitzCellular` — Riemann–Hurwitz from orbit–stabilizer

Bean `qou-qhcr`. Supplies the Riemann–Hurwitz input that
`QOU.BringsSurface.IrreducibleH1ForcesGenusFour` took as the hypothesis `RH`.

## Statement

A finite group `G` acts on a finite cell structure `(V, E, F)` of a closed surface `X`
(vertices, edges, faces). The quotient `Y = X/G` has the orbit sets as its cells. As is
standard, the branch points are taken among the vertices, so `G` acts **freely on edges and
faces**. Then

  `χ(X) = |G|·χ(Y) − Σ_{vertex orbits ω} (|G| − |G|/|Stab ω|)`,

which is Riemann–Hurwitz. With `χ(X) = 2 − 2g` and `χ(Y) = 2 − 2h` this is exactly the
predicate `RH |G| g h ts`, where `ts` lists `|G| − |G|/|Stab ω|` over the vertex orbits
(`rh_of_cellular`). Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, §V.1.

The proof is orbit–stabilizer only (`MulAction.card_eq_sum_card_group_div_card_stabilizer`).

## What is still taken as given

* That a compact Riemann surface with a holomorphic `G`-action has such a `G`-equivariant
  cell structure, and that `χ = 2 − 2g` for it. These are topological facts that Mathlib
  does not have for Riemann surfaces. They enter as the cell data and as `hX`, `hY`.
* That a point stabiliser is cyclic, so its order is an element order of `G`
  (`1, 2, 3, 5` for `A₅`). This enters as `hstabA` / `hstabS`.
* The irreducible dimensions of `A₅` (`hdim`), as in the arithmetic file.
-/

namespace QOU.BringsSurface.RiemannHurwitzCellular

open MulAction
open QOU.BringsSurface.IrreducibleH1ForcesGenusFour

variable (G : Type*) [Group G] [Fintype G]

/-- A set with free `G`-action has `|G|` times as many elements as orbits. -/
theorem card_eq_mul_orbits_of_free (α : Type*) [MulAction G α] [Fintype α]
    [Fintype (Quotient (orbitRel G α))] [∀ a : α, Fintype (stabilizer G a)]
    (hfree : ∀ a : α, Fintype.card (stabilizer G a) = 1) :
    Fintype.card α = Fintype.card G * Fintype.card (Quotient (orbitRel G α)) := by
  rw [MulAction.card_eq_sum_card_group_div_card_stabilizer G α]
  simp [hfree, Finset.sum_const, Finset.card_univ, mul_comm]

/-- **Riemann–Hurwitz, cellular form.** -/
theorem riemann_hurwitz_cellular (V E F : Type*)
    [MulAction G V] [MulAction G E] [MulAction G F]
    [Fintype V] [Fintype E] [Fintype F]
    [Fintype (Quotient (orbitRel G V))] [Fintype (Quotient (orbitRel G E))]
    [Fintype (Quotient (orbitRel G F))]
    [∀ v : V, Fintype (stabilizer G v)] [∀ e : E, Fintype (stabilizer G e)]
    [∀ f : F, Fintype (stabilizer G f)]
    (hE : ∀ e : E, Fintype.card (stabilizer G e) = 1)
    (hF : ∀ f : F, Fintype.card (stabilizer G f) = 1) :
    ((Fintype.card V : ℤ) - Fintype.card E + Fintype.card F) =
      (Fintype.card G : ℤ) * ((Fintype.card (Quotient (orbitRel G V)) : ℤ)
          - Fintype.card (Quotient (orbitRel G E)) + Fintype.card (Quotient (orbitRel G F)))
        - ∑ ω : Quotient (orbitRel G V),
            ((Fintype.card G : ℤ)
              - ((Fintype.card G / Fintype.card (stabilizer G ω.out) : ℕ) : ℤ)) := by
  rw [card_eq_mul_orbits_of_free G E hE, card_eq_mul_orbits_of_free G F hF,
    MulAction.card_eq_sum_card_group_div_card_stabilizer G V]
  rw [Finset.sum_sub_distrib]
  simp only [Nat.cast_sum, Nat.cast_mul, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  ring

/-- **Riemann–Hurwitz gives the predicate `RH`.** With `χ(X) = 2 − 2g` and
`χ(X/G) = 2 − 2h`, the cellular formula is `RH |G| g h ts` for `ts` the list of vertex-orbit
contributions `|G| − |G|/|Stab ω|`. -/
theorem rh_of_cellular (V E F : Type*)
    [MulAction G V] [MulAction G E] [MulAction G F]
    [Fintype V] [Fintype E] [Fintype F]
    [Fintype (Quotient (orbitRel G V))] [Fintype (Quotient (orbitRel G E))]
    [Fintype (Quotient (orbitRel G F))]
    [∀ v : V, Fintype (stabilizer G v)] [∀ e : E, Fintype (stabilizer G e)]
    [∀ f : F, Fintype (stabilizer G f)]
    (hE : ∀ e : E, Fintype.card (stabilizer G e) = 1)
    (hF : ∀ f : F, Fintype.card (stabilizer G f) = 1)
    (g h : ℕ)
    (hX : ((Fintype.card V : ℤ) - Fintype.card E + Fintype.card F) = 2 - 2 * g)
    (hY : ((Fintype.card (Quotient (orbitRel G V)) : ℤ)
          - Fintype.card (Quotient (orbitRel G E)) + Fintype.card (Quotient (orbitRel G F)))
          = 2 - 2 * h) :
    RH (Fintype.card G) g h
      ((Finset.univ : Finset (Quotient (orbitRel G V))).toList.map
        fun ω => Fintype.card G - Fintype.card G / Fintype.card (stabilizer G ω.out)) := by
  have hRH := riemann_hurwitz_cellular G V E F hE hF
  rw [hX, hY] at hRH
  unfold RH
  rw [Finset.sum_map_toList]
  zify
  rw [Finset.sum_congr rfl (fun ω _ => Nat.cast_sub
    (Nat.div_le_self (Fintype.card G) (Fintype.card (stabilizer G ω.out))))]
  linarith

/-- The vertex-orbit list of an `A₅`-action (point stabilisers of order `1,2,3,5`) consists
of `A5Branch` values. -/
theorem a5Branch_of_stab (n s : ℕ) (hn : n = 60) (hs : s = 1 ∨ s = 2 ∨ s = 3 ∨ s = 5) :
    A5Branch (n - n / s) := by
  unfold A5Branch; subst hn; rcases hs with rfl | rfl | rfl | rfl <;> decide

/-- The vertex-orbit list of an `S₅`-action (point stabilisers of order `1,…,6`) consists of
`S5Branch` values. -/
theorem s5Branch_of_stab (n s : ℕ) (hn : n = 120)
    (hs : s = 1 ∨ s = 2 ∨ s = 3 ∨ s = 4 ∨ s = 5 ∨ s = 6) : S5Branch (n - n / s) := by
  unfold S5Branch; subst hn; rcases hs with rfl | rfl | rfl | rfl | rfl | rfl <;> decide

/-- **Genus 4 from the cellular data.** A group `GA` of order 60 (the icosahedral `A₅`) and a
group `GS` of order 120 (`S₅`) act on the same closed surface of genus `g ≥ 2`, through
`G`-equivariant cell structures with free action on edges and faces and cyclic point
stabilisers (orders `1,2,3,5` for `A₅`, `1,…,6` for `S₅`). If `H¹ = 2W` with `W` an
irreducible `A₅`-representation, so that `g ∈ {1,3,4,5}`, then `g = 4`. Riemann–Hurwitz is
now proved (`rh_of_cellular`), not assumed. -/
theorem genus_eq_four_of_cellular
    (GA GS : Type*) [Group GA] [Fintype GA] [Group GS] [Fintype GS]
    (hA60 : Fintype.card GA = 60) (hS120 : Fintype.card GS = 120)
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
    (hstabA : ∀ v : VA, Fintype.card (stabilizer GA v) = 1 ∨ Fintype.card (stabilizer GA v) = 2
      ∨ Fintype.card (stabilizer GA v) = 3 ∨ Fintype.card (stabilizer GA v) = 5)
    (hstabS : ∀ v : VS, Fintype.card (stabilizer GS v) = 1 ∨ Fintype.card (stabilizer GS v) = 2
      ∨ Fintype.card (stabilizer GS v) = 3 ∨ Fintype.card (stabilizer GS v) = 4
      ∨ Fintype.card (stabilizer GS v) = 5 ∨ Fintype.card (stabilizer GS v) = 6)
    (g hA hS : ℕ)
    (hXA : ((Fintype.card VA : ℤ) - Fintype.card EA + Fintype.card FA) = 2 - 2 * g)
    (hYA : ((Fintype.card (Quotient (orbitRel GA VA)) : ℤ)
          - Fintype.card (Quotient (orbitRel GA EA)) + Fintype.card (Quotient (orbitRel GA FA)))
          = 2 - 2 * hA)
    (hXS : ((Fintype.card VS : ℤ) - Fintype.card ES + Fintype.card FS) = 2 - 2 * g)
    (hYS : ((Fintype.card (Quotient (orbitRel GS VS)) : ℤ)
          - Fintype.card (Quotient (orbitRel GS ES)) + Fintype.card (Quotient (orbitRel GS FS)))
          = 2 - 2 * hS)
    (hg : 2 ≤ g) (hdim : g = 1 ∨ g = 3 ∨ g = 4 ∨ g = 5) : g = 4 := by
  have hRA := rh_of_cellular GA VA EA FA hEA hFA g hA hXA hYA
  have hRS := rh_of_cellular GS VS ES FS hES hFS g hS hXS hYS
  rw [hA60] at hRA
  rw [hS120] at hRS
  refine genus_eq_four_of_A5_irreducible_and_S5 g hA hS _ _ ?_ hRA ?_ hRS hg hdim
  · intro t ht
    simp only [List.mem_map, Finset.mem_toList, Finset.mem_univ, true_and] at ht
    obtain ⟨ω, rfl⟩ := ht
    exact a5Branch_of_stab _ _ rfl (hstabA _)
  · intro t ht
    simp only [List.mem_map, Finset.mem_toList, Finset.mem_univ, true_and] at ht
    obtain ⟨ω, rfl⟩ := ht
    exact s5Branch_of_stab _ _ rfl (hstabS _)

end QOU.BringsSurface.RiemannHurwitzCellular
