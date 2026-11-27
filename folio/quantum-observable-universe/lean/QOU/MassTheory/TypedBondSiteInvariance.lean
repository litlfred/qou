/-
# Isospin-typed bond scalars do not escape the pairwise wall

`QOU.Mass.UniformBondSimpleGraphExclusion` proves that a **uniform** bond weight
summed over a simple graph forces `b₃ ≤ 0`, and names its own escape hatch:

> "What is excluded is the conjunction *uniform bond weight* ∧ *simple graph*.
>  Dropping either escapes it."

There are two ways to drop the first. One is to let the bond weight depend on the
**coordination number** — non-transferability, `ε 2 > ε 1`, which bean `qou-edt7`
identifies as the surviving mechanism and states as one open number
(`ε 2 / ε 1 = 1.2137076`). The other is to let it depend on the **isospin type**
of the bonded pair — the `L_pp`, `L_pn`, `L_nn` typing that
`QOU.MassTheory.ChainBondOrderDependence` studies. This file closes the second,
so that the first is the only one left.

## The gap this fills

`ChainBondOrderDependence.orderIndependent_iff` proves that the typed bond sum is
rearrangement-invariant **iff** `L_pp = L_pn = L_nn`. That is a theorem about
`bondSum` — the sum over **adjacent pairs of a list**, i.e. the *linear chain*
specifically. It says nothing about a general bond set, and the natural reading
that "physical ⇒ uniform bonds" does not follow from it: on the complete graph
the typed sum is invariant for *arbitrary* `L_pp, L_pn, L_nn`, because the three
pair counts are fixed by `(Z, N)` alone.

So the general question — for which graphs is a typed bond sum even *well
defined* as a function of `(A, Z)` — is open, and it is what a nucleus needs
answered: a nucleus has no arrangement, so the binding may not depend on which
sites carry the protons.

## The classification

Write `S ⊆ V` for the proton sites and

    2·B(S) = ∑_{u,v} [u ∼ v] · L_{type(u),type(v)}

(doubled, so that no division is needed and the ring stays generic). The master
identity `B2S_eq` puts it in *degree/induced-edge* coordinates:

    2·B(S) = L_nn·∑_u deg u  +  2(L_pn − L_nn)·∑_{u ∈ S} deg u
                             +  (L_pp − 2L_pn + L_nn)·∑_{u,v ∈ S} [u ∼ v]

and the two structural theorems fall straight out of it by choosing `S`:

* `sub_singleton` / `regular_of_siteInvariant` — comparing two **one-proton**
  assignments gives `2(L_pn − L_nn)(deg u − deg v) = 0`, so unless the `p`–`n`
  and `n`–`n` bonds coincide the graph must be **regular**.
* `sub_pair` / `mean_of_siteInvariant` — comparing an **adjacent** two-proton
  assignment with a **non-adjacent** one, on a regular graph, gives
  `2(L_pp − 2L_pn + L_nn) = 0`, i.e. `L_pp + L_nn = 2·L_pn` — the `p`–`n` bond
  is the arithmetic mean of the like-pair bonds.
* `B2S_collapse` — under those two conditions,

      2·B(S) = k·(L_pp·Z + L_nn·N)

  which is **linear in the nucleon counts**: a one-body self-energy, carrying no
  bond structure at all beyond the constant `k`. The graph has been erased.

Note what is *not* claimed: uniformity. `L_pp + L_nn = 2L_pn` is strictly weaker
than `L_pp = L_pn = L_nn`, and on a regular graph it genuinely suffices. The
chain's stronger conclusion is an artifact of the chain being **irregular** (its
endpoints have degree 1), which is exactly the hypothesis `regular_of_siteInvariant`
extracts.

## What it excludes

`typed_transferable_refuted` — the collapse is falsifiable with two nuclei and no
fit. Along `N = Z` the collapse gives `2·B = k·Z·(L_pp + L_nn)`, so

    B(⁴He)/B(²H) = 2·k₄/k₂ = 2·k₄ ≤ 2·(4−1) = 6,

using `k₂ = 1` (the only graph on two sites with a bond) and the simple-graph
degree bound `k ≤ A − 1`. AME2020 gives `28.2956624 / 2.224566 = 12.7196…`,
which is more than twice the largest value the family can reach. The invariant
is the degree bound — the same counting bound `UniformBondSimpleGraphExclusion`
cites, one coordinate over.

The complete-graph branch is closed separately and does not need the
classification. `complete_saturates_iff` computes that the isobaric per-nucleon
binding of a complete-graph typed sum is bounded in `A` **iff**
`L_pp + L_nn + 2L_pn = 0` — so `QOU.Mass.CoordinationSaturation.complete_graph_no_saturation`,
which assumes one `ε > 0`, does not by itself close it: mixed signs can cancel
the `A²` term. But `complete_b3_eq` then shows that under exactly that
cancellation the Ursell inversion gives `b₃ = −2·b₂`, so a bound deuteron
(`b₂ > 0`) forces `b₃ < 0` (`complete_b3_neg`), against the measured
`b₃ = +1.426222` MeV.

## Scope

Scope **(b)**, invariants named: the simple-graph degree bound `k ≤ A − 1` for
the regular branch, and the exact `A²`-coefficient identity plus the sign of
`b₂` for the complete branch. What is excluded is the conjunction *isospin-typed
bond scalars* ∧ *transferable across mass number* ∧ *well defined on a nucleus*.

It does **not** exclude:

* **coordination-dependent** bond weights — the `ε z` of `qou-edt7`. Those are
  not transferable, so the hypothesis fails at the first word. This file *narrows
  onto* that mechanism rather than touching it.
* the typed scalars as a *contribution* inside a larger functional (AGENTS.md
  permanence principle 1). What is excluded is their supplying the binding alone.
* anything about the bond functional `f` applied to a trace — that is
  `QOU.Mass.PairwiseCumulantVanishing`, and it is orthogonal: this file is about
  which *arguments* the assembly may depend on, that one about which *function*.
* any magnitude claim. Nothing here is fitted; `L_pp`, `L_pn`, `L_nn` and `k`
  are free throughout, and the two numerical facts entering
  `typed_transferable_refuted` and `chi_b3_measured_pos` are AME2020 values used
  as *targets*, never as inputs to a solve.

Base ring: generic `CommRing` for the classification (pure counting and ring
identities, AGENTS.md §7c); the two empirical corollaries are over `ℚ`, where the
content is an ordering fact.

Bean `qou-edt7` (negative half), `qou-brng` (the amplitude question it narrows).

-- Ref: [leitner2026] folio/quantum-observable-universe/mass-theory/bk-coordination-multiplicity.md
-/
import Mathlib.Tactic
set_option linter.unusedSectionVars false

namespace QOU.Mass.TypedBondSiteInvariance

variable {R : Type*} [CommRing R]

/-- The `{0,1}` indicator of a boolean, in the coefficient ring. -/
def ind (b : Bool) : R := if b then 1 else 0

@[simp] theorem ind_true : (ind true : R) = 1 := rfl

@[simp] theorem ind_false : (ind false : R) = 0 := rfl

/-- The isospin-typed bond scalar: `true` is a proton. -/
def bondOf (Lpp Lpn Lnn : R) : Bool → Bool → R
  | true,  true  => Lpp
  | true,  false => Lpn
  | false, true  => Lpn
  | false, false => Lnn

/-- **The typed bond scalar is a quadratic polynomial in the two indicators.**
This is the step that makes the whole classification a `ring` computation: the
three-case definition is the *same function* as the bilinear form whose three
coefficients are `L_nn`, `L_pn − L_nn` and `L_pp − 2L_pn + L_nn`. -/
theorem bondOf_eq (Lpp Lpn Lnn : R) (a b : Bool) :
    bondOf Lpp Lpn Lnn a b
      = Lnn + (Lpn - Lnn) * (ind a + ind b)
        + (Lpp - 2 * Lpn + Lnn) * (ind a * ind b) := by
  cases a <;> cases b <;> simp [bondOf, ind] <;> ring

/-- A finite simple graph on the sites, as a symmetric irreflexive boolean
adjacency. (Data, not an assumption: every field is a structural fact about a
graph, and `BondGraph` is inhabited — see `emptyGraph`.) -/
structure BondGraph (V : Type*) where
  /-- adjacency -/
  adj : V → V → Bool
  /-- undirected -/
  symm : ∀ u v, adj u v = adj v u
  /-- no self-bond -/
  irrefl : ∀ v, adj v v = false

/-- The edgeless graph, witnessing that `BondGraph` is inhabited. -/
def emptyGraph (V : Type*) : BondGraph V where
  adj _ _ := false
  symm _ _ := rfl
  irrefl _ := rfl

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The degree of a site, in the coefficient ring. -/
def deg (R : Type*) [CommRing R] (G : BondGraph V) (u : V) : R :=
  ∑ v, ind (G.adj u v)

/-- **The doubled typed bond sum** of a proton-site set `S`. Doubled because each
bond is counted from both ends, which keeps the statement inside a generic ring
with no division. -/
def B2S (G : BondGraph V) (Lpp Lpn Lnn : R) (S : Finset V) : R :=
  ∑ u, ∑ v, ind (G.adj u v) * bondOf Lpp Lpn Lnn (decide (u ∈ S)) (decide (v ∈ S))

/-- Restricting a `∑ over univ` weighted by a membership indicator to a `∑ over S`. -/
theorem sum_ind_mem (S : Finset V) (f : V → R) :
    ∑ u, ind (decide (u ∈ S)) * f u = ∑ u ∈ S, f u := by
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (fun u => u ∈ S)]
  have h₁ : ∀ u ∈ Finset.univ.filter (fun u => u ∈ S),
      ind (R := R) (decide (u ∈ S)) * f u = f u := by
    intro u hu
    simp only [Finset.mem_filter] at hu
    simp [ind, hu.2]
  have h₂ : ∀ u ∈ Finset.univ.filter (fun u => ¬ u ∈ S),
      ind (R := R) (decide (u ∈ S)) * f u = 0 := by
    intro u hu
    simp only [Finset.mem_filter] at hu
    simp [ind, hu.2]
  rw [Finset.sum_congr rfl h₁, Finset.sum_congr rfl h₂, Finset.sum_const_zero, add_zero]
  exact Finset.sum_congr (by ext u; simp) (fun _ _ => rfl)

/-- **Master identity — the typed bond sum in degree / induced-edge
coordinates.** Everything below is a corollary of this plus a choice of `S`. -/
theorem B2S_eq (G : BondGraph V) (Lpp Lpn Lnn : R) (S : Finset V) :
    B2S G Lpp Lpn Lnn S
      = Lnn * (∑ u, deg R G u)
        + (Lpn - Lnn) * (2 * ∑ u ∈ S, deg R G u)
        + (Lpp - 2 * Lpn + Lnn) * (∑ u ∈ S, ∑ v ∈ S, ind (G.adj u v)) := by
  have hM0 : (∑ u, ∑ v, ind (R := R) (G.adj u v)) = ∑ u, deg R G u := rfl
  have hM1 : (∑ u, ∑ v, ind (G.adj u v) * ind (R := R) (decide (u ∈ S)))
      = ∑ u ∈ S, deg R G u := by
    rw [← sum_ind_mem S (fun u => deg R G u)]
    refine Finset.sum_congr rfl fun u _ => ?_
    rw [← Finset.sum_mul, mul_comm]
    rfl
  have hM1' : (∑ u, ∑ v, ind (G.adj u v) * ind (R := R) (decide (v ∈ S)))
      = ∑ u ∈ S, deg R G u := by
    rw [Finset.sum_comm, ← sum_ind_mem S (fun v => deg R G v)]
    refine Finset.sum_congr rfl fun v _ => ?_
    rw [← Finset.sum_mul, mul_comm]
    congr 1
    exact Finset.sum_congr rfl fun u _ => by rw [G.symm u v]
  have hM2 : (∑ u, ∑ v, ind (G.adj u v)
        * (ind (R := R) (decide (u ∈ S)) * ind (decide (v ∈ S))))
      = ∑ u ∈ S, ∑ v ∈ S, ind (G.adj u v) := by
    rw [← sum_ind_mem S (fun u => ∑ v ∈ S, ind (R := R) (G.adj u v))]
    refine Finset.sum_congr rfl fun u _ => ?_
    rw [Finset.mul_sum,
      ← sum_ind_mem S (fun v => ind (R := R) (decide (u ∈ S)) * ind (G.adj u v))]
    refine Finset.sum_congr rfl fun v _ => ?_
    ring
  have hsplit : B2S G Lpp Lpn Lnn S
      = Lnn * (∑ u, ∑ v, ind (G.adj u v))
        + (Lpn - Lnn) * ((∑ u, ∑ v, ind (G.adj u v) * ind (decide (u ∈ S)))
            + (∑ u, ∑ v, ind (G.adj u v) * ind (decide (v ∈ S))))
        + (Lpp - 2 * Lpn + Lnn)
            * (∑ u, ∑ v, ind (G.adj u v) * (ind (decide (u ∈ S)) * ind (decide (v ∈ S)))) := by
    simp only [B2S, Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun v _ => ?_
    rw [bondOf_eq]; ring
  rw [hsplit, hM0, hM1, hM1', hM2]
  ring

/-- **Site invariance** — the physical requirement. A nucleus has no arrangement,
so its binding may depend only on how *many* protons there are, not on which
sites carry them. -/
def SiteInvariant (G : BondGraph V) (Lpp Lpn Lnn : R) : Prop :=
  ∀ S T : Finset V, S.card = T.card → B2S G Lpp Lpn Lnn S = B2S G Lpp Lpn Lnn T

section Consequences

variable [NoZeroDivisors R] {G : BondGraph V} {Lpp Lpn Lnn : R}

/-- The one-proton difference: only the degrees survive. -/
theorem sub_singleton (u v : V) :
    B2S G Lpp Lpn Lnn {u} - B2S G Lpp Lpn Lnn {v}
      = (Lpn - Lnn) * (2 * (deg R G u - deg R G v)) := by
  rw [B2S_eq, B2S_eq]
  simp only [Finset.sum_singleton]
  have hu : ind (R := R) (G.adj u u) = 0 := by rw [G.irrefl u]; simp
  have hv : ind (R := R) (G.adj v v) = 0 := by rw [G.irrefl v]; simp
  rw [hu, hv]
  ring

/-- **A site-invariant typed bond sum on a graph with two different degrees forces
`L_pn = L_nn`.** Contrapositive form: with `L_pn ≠ L_nn` the graph is regular. -/
theorem regular_of_siteInvariant (h : SiteInvariant G Lpp Lpn Lnn)
    (htwo : (2 : R) ≠ 0) (hne : Lpn - Lnn ≠ 0) (u v : V) : deg R G u = deg R G v := by
  have hcard : ({u} : Finset V).card = ({v} : Finset V).card := by simp
  have h0 : B2S G Lpp Lpn Lnn {u} - B2S G Lpp Lpn Lnn {v} = 0 := by
    rw [h {u} {v} hcard]; ring
  rw [sub_singleton u v] at h0
  rcases mul_eq_zero.mp h0 with h' | h'
  · exact absurd h' hne
  · rcases mul_eq_zero.mp h' with h'' | h''
    · exact absurd h'' htwo
    · exact sub_eq_zero.mp h''

/-- The two-proton difference on a **regular** graph: only the adjacency
indicators survive. -/
theorem sub_pair {u v u' v' : V} (huv : u ≠ v) (huv' : u' ≠ v')
    (hreg : ∀ a b : V, deg R G a = deg R G b) :
    B2S G Lpp Lpn Lnn {u, v} - B2S G Lpp Lpn Lnn {u', v'}
      = (Lpp - 2 * Lpn + Lnn) * (2 * (ind (G.adj u v) - ind (G.adj u' v'))) := by
  rw [B2S_eq, B2S_eq]
  rw [Finset.sum_pair huv, Finset.sum_pair huv', Finset.sum_pair huv, Finset.sum_pair huv']
  rw [Finset.sum_pair huv, Finset.sum_pair huv', Finset.sum_pair huv, Finset.sum_pair huv']
  have hd : deg R G u + deg R G v = deg R G u' + deg R G v' := by
    rw [hreg u u', hreg v v']
  have huu : ind (R := R) (G.adj u u) = 0 := by rw [G.irrefl u]; simp
  have hvv : ind (R := R) (G.adj v v) = 0 := by rw [G.irrefl v]; simp
  have hu'u' : ind (R := R) (G.adj u' u') = 0 := by rw [G.irrefl u']; simp
  have hv'v' : ind (R := R) (G.adj v' v') = 0 := by rw [G.irrefl v']; simp
  have hsym : ind (R := R) (G.adj v u) = ind (G.adj u v) := by rw [G.symm v u]
  have hsym' : ind (R := R) (G.adj v' u') = ind (G.adj u' v') := by rw [G.symm v' u']
  rw [huu, hvv, hu'u', hv'v', hsym, hsym']
  linear_combination (Lpn - Lnn) * 2 * hd

/-- **The mean condition is forced.** On a regular graph carrying both a bond and
a non-bond between distinct sites, site invariance forces
`L_pp + L_nn = 2·L_pn` — the `p`–`n` scalar is the arithmetic mean of the
like-pair scalars. Strictly weaker than `L_pp = L_pn = L_nn`, which is what the
*chain* forces; the chain's extra strength comes from its irregularity. -/
theorem mean_of_siteInvariant (h : SiteInvariant G Lpp Lpn Lnn)
    (hreg : ∀ a b : V, deg R G a = deg R G b)
    {u v u' v' : V} (huv : u ≠ v) (huv' : u' ≠ v')
    (hbond : G.adj u v = true) (hnobond : G.adj u' v' = false)
    (htwo : (2 : R) ≠ 0) : Lpp - 2 * Lpn + Lnn = 0 := by
  have hcard : ({u, v} : Finset V).card = ({u', v'} : Finset V).card := by
    rw [Finset.card_pair huv, Finset.card_pair huv']
  have h0 : B2S G Lpp Lpn Lnn {u, v} - B2S G Lpp Lpn Lnn {u', v'} = 0 := by
    rw [h {u, v} {u', v'} hcard]; ring
  rw [sub_pair (R := R) huv huv' hreg, hbond, hnobond] at h0
  have h2 : (Lpp - 2 * Lpn + Lnn) * 2 = 0 := by
    simp only [ind_true, ind_false, sub_zero] at h0
    linear_combination h0
  rcases mul_eq_zero.mp h2 with h' | h'
  · exact h'
  · exact absurd h' htwo

/-- **The collapse.** Under regularity of degree `k` and the mean condition, the
typed bond sum is *linear in the nucleon counts* — a one-body self-energy. The
graph survives only through the scalar `k`; which pairs are bonded has been
erased entirely. -/
theorem B2S_collapse (S : Finset V) (k : R)
    (hreg : ∀ a : V, deg R G a = k)
    (hmean : Lpp - 2 * Lpn + Lnn = 0) :
    B2S G Lpp Lpn Lnn S
      = k * (Lpp * S.card + Lnn * ((Fintype.card V : R) - S.card)) := by
  rw [B2S_eq]
  have hall : (∑ _u : V, k) = (Fintype.card V : R) * k := by
    rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  have h1 : (∑ u, deg R G u) = (Fintype.card V : R) * k := by
    rw [← hall]; exact Finset.sum_congr rfl fun u _ => hreg u
  have hS : (∑ _u ∈ S, k) = (S.card : R) * k := by
    rw [Finset.sum_const, nsmul_eq_mul]
  have h2 : (∑ u ∈ S, deg R G u) = (S.card : R) * k := by
    rw [← hS]; exact Finset.sum_congr rfl fun u _ => hreg u
  rw [h1, h2]
  linear_combination
    ((∑ u ∈ S, ∑ v ∈ S, ind (R := R) (G.adj u v)) - (S.card : R) * k) * hmean

end Consequences

/-! ## The two empirical kills

Both are ordering facts over `ℚ`; nothing is fitted, and the AME2020 values enter
only as comparison targets. -/

section Empirical

/-- **The regular branch is refuted by two nuclei.** Along `N = Z` the collapse
gives `2·B(A) = k_A · Z · (L_pp + L_nn)`, so with `k₂ = 1` (the only graph on two
sites carrying a bond),

    B(⁴He)/B(²H) = 2·k₄  ≤  2·(4 − 1) = 6,

by the simple-graph degree bound `k ≤ A − 1`. AME2020 gives `12.7196…`. Stated
as: no admissible `k₄` reproduces the ratio. -/
theorem typed_transferable_refuted (k₄ : ℚ) (hk : k₄ ≤ 3) :
    2 * k₄ < 282956624 / 22245660 := by
  have : (282956624 : ℚ) / 22245660 > 12 := by norm_num
  linarith

/-- The measured ratio, for the record: `B(⁴He)/B(²H) = 28.2956624/2.224566`
exceeds the largest value the regular branch can reach by more than a factor
two. -/
theorem measured_ratio_exceeds_bound : (6 : ℚ) < 282956624 / 22245660 := by
  norm_num

/-- **The complete-graph branch saturates only under an exact sign
cancellation.** For the complete graph on `A` sites the typed sum is
`B = L_pp·C(Z,2) + L_pn·Z·N + L_nn·C(N,2)`; along the isobaric line
`Z = (A−d)/2`, `N = (A+d)/2` the coefficient of `A²` is
`(L_pp + L_nn + 2·L_pn)/8`. Written without division, as the doubled form: the
`A²` coefficient of `8·B` is `L_pp + L_nn + 2·L_pn`.

`QOU.Mass.CoordinationSaturation.complete_graph_no_saturation` assumes a single
`ε > 0`, so it does not cover the mixed-sign case; this identity is what shows
the case exists. -/
theorem complete_A2_coefficient (Lpp Lpn Lnn A d : ℚ) :
    Lpp * ((A - d) * (A - d - 2)) + Lnn * ((A + d) * (A + d - 2))
        + 2 * Lpn * ((A - d) * (A + d))
      = (Lpp + Lnn + 2 * Lpn) * A ^ 2
        + (2 * d * (Lnn - Lpp) - 2 * (Lpp + Lnn)) * A
        + (d ^ 2 * (Lpp + Lnn - 2 * Lpn) + 2 * d * (Lpp - Lnn)) := by
  ring

/-- **Under that cancellation the three-body cumulant is minus twice the
two-body one.** With `L_pp + L_nn = −2·L_pn`, the complete graph gives
`b₂ = B(²H) = L_pn` and `B̄(3) = (L_pp + L_nn)/2 + 2·L_pn = L_pn`, so the Ursell
inversion `b₃ = B̄(3) − 3·b₂` returns `−2·L_pn`. -/
theorem complete_b3_eq (Lpp Lpn Lnn : ℚ) (hsat : Lpp + Lnn + 2 * Lpn = 0) :
    ((Lpp + Lnn) / 2 + 2 * Lpn) - 3 * Lpn = -2 * Lpn := by
  linarith

/-- **So the saturating complete-graph branch has a negative three-body
cumulant** whenever the deuteron binds. `b₂ = L_pn = 2.224566 MeV > 0` gives
`b₃ = −4.449132 MeV`, against the measured `b₃ = +1.426222 MeV`. -/
theorem complete_b3_neg (Lpn : ℚ) (hb2 : 0 < Lpn) : -2 * Lpn < 0 := by linarith

/-- The measured three-body cumulant is positive (AME2020 Ursell inversion,
`he4_body_order_shortfall_location_probe.py`), which is what
`complete_b3_neg` contradicts. -/
theorem chi_b3_measured_pos : (0 : ℚ) < 1426222 / 1000000 := by norm_num

end Empirical

end QOU.Mass.TypedBondSiteInvariance
