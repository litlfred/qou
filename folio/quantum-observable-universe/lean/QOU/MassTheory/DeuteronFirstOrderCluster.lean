/-
# The μ₃ submodularity door is structurally VACUOUS at the deuteron (A = 2)

**Distinct parallel attack on the Δ_λ / deuteron-magnitude gate** (branch
`claude/deltalambda-submodularity-parallel-2026-08-02`), deliberately routed
away from the two live siblings:

* PR #4615 (`deltalambda-magnitude-deuteron`) attacks the **per-pair uniform
  magnitude** `z` — the K₂ / K₄ Gram determinant `det(I + G)` — and finds `z`
  physical at A=2 but insufficient (closes `0.506/2.225`), dead at A=4.
* The Option-E A=3 anti-self-adjoint sibling (main `33131b24`) attacks the
  single free amplitude `E` of the 3-body lift.

This file attacks a **third, orthogonal** object: the owner-suggested
**μ₃ cluster-modularity / submodularity door**
(`QOU.MassTheory.Mu3ClusterModularity`, main `0e9bfc67`,
`c₃ = −E₀·Δ²g`, `μ₃ > 0 ⟺ Δ²g < 0`).  The question posed:
*does the submodular structure supply the deuteron binding magnitude the DT
count (`Δ_λ = (−1)^{n(λ)}·dim V_λ`, #4601, B_D = 0.380 MeV, −82.9 %) does not?*

## The answer is a clean scope-(b) STRUCTURAL NEGATIVE, and this file proves it.

The μ₃ door is the **second mixed finite difference**
`Δ²g = g_ab − g_a − g_b + g_∅` of the joint block-trace over **two** interface
bonds `{a, b}` — the *connected 3-body* (A ≥ 3) Ursell content.  The deuteron
(A = 2) is a **single-bond** configuration: it carries exactly one p–n interface
generator, so the second bond `b` is absent.  "Absent bond `b`" means adding it
changes nothing: `g_b = g_∅` and `g_ab = g_a`.  Substituting:

    Δ²g = g_a − g_a − g_∅ + g_∅ = 0.

So the μ₃ cluster `c₃ = −E₀·Δ²g = 0` **identically** at A=2.  The submodularity
door contributes exactly zero to the deuteron — it is not that the door is shut
(supermodular), it is that the door **does not exist** below A=3.  The μ₃
machinery is a *correction to* the pairwise base case, and the deuteron **is**
that base case.

**Why this is the honest complement to #4615.**  #4615 kills the per-pair
magnitude mechanism (uniform `z` fails at every A).  This file kills the
beyond-pairwise cluster mechanism (the μ₃/submodularity hierarchy is *vacuous*
at A=2).  Together: neither the per-pair amplitude nor the cluster structure
supplies the deuteron 5.853× deficit — it lives entirely in the **bare
first-order per-bond amplitude** (`firstDiff` below), which remains the single
open magnitude object (the FITTED `C_knot = 5.853` of #4601/#4615).

## Derive-then-check (locked BEFORE any compute; 0 fit)

* B_D (AME2020) = 2.224 MeV                             — the target.
* first-order DT-derived (#4601) = 0.380 MeV           — undershoots.
* deficit factor = 2.224 / 0.380 = 5.853               — the open magnitude.
* μ₃ second-order contribution at A=2  = **0** (this file, proved).

No AME quantity is fitted, no normalization wired.  The Lean asserts a sign/zero
identity, not a magnitude.

## Machine-verification

**Mathlib-free** (`import`-free core: `Int` + `omega`/`decide` only), so it is
`lean`-checkable without the Mathlib olean cache (respecting the ~3 GB disk /
~5 GB olean wall).  The identities are stated over `Int` as the representative
ring; each is a pure additive-group identity that holds verbatim over `ℝ` (where
the block-traces `g_S` actually live) by the same one-step cancellation.
`lean DeuteronFirstOrderCluster.lean` exits 0, sorry-free.
-/

namespace QOU.MassTheory.DeuteronFirstOrderCluster

/-! ### The finite-difference cluster hierarchy (over `Int`, Mathlib-free)

We mirror `QOU.MassTheory.Mu3ClusterModularity.secondDiff` (which is stated over
`ℝ` with `import Mathlib.Tactic`) in the `import`-free `Int` core, so the
structural facts below are machine-checked without the Mathlib cache.  Every
identity is a group identity: it is true over `ℝ` verbatim. -/

/-- **First mixed difference** (connected 2-body / single-bond Ursell term):
`Δ¹g = g_a − g_∅`.  This is the *whole* cluster content of a single bond — the
deuteron's honest binding object. -/
def firstDiff (g₀ gₐ : Int) : Int := gₐ - g₀

/-- **Second mixed difference** (connected 3-body Ursell term / the μ₃ door):
`Δ²g = g_ab − g_a − g_b + g_∅`.  `Δ²g < 0` is submodularity (the μ₃ > 0 door);
`Δ²g > 0` is supermodularity (door shut). -/
def secondDiff (g₀ gₐ g_b gₐᵦ : Int) : Int := gₐᵦ - gₐ - g_b + g₀

/-- The connected 3-body cluster `c₃ = −E₀·Δ²g` (matches
`Mu3ClusterModularity.cluster3`, sign convention `E₀·(gₐ + g_b − g₀ − gₐᵦ)`). -/
def cluster3 (E₀ g₀ gₐ g_b gₐᵦ : Int) : Int := E₀ * (gₐ + g_b - g₀ - gₐᵦ)

/-! ### The deuteron collapse: the μ₃ door is identically zero at A = 2 -/

/-- **A single-bond (deuteron) configuration** is one where the second interface
bond `b` is absent, encoded by "adding `b` changes nothing":
`g_b = g_∅` and `g_ab = g_a`.  Under this the **second mixed difference vanishes
identically**.  The μ₃ submodularity door therefore supplies *nothing* to a
single-bond object — regardless of the (unknown, possibly submodular) sign of
the joint trace, because there is no second bond for it to act on. -/
theorem secondDiff_single_bond_vanishes (g₀ gₐ : Int) :
    secondDiff g₀ gₐ g₀ gₐ = 0 := by
  dsimp [secondDiff]
  omega

/-- **The μ₃ cluster is identically zero at A = 2.**  Consequently
`c₃ = −E₀·Δ²g = 0` for the deuteron for **every** `E₀`: the connected-3-body /
submodularity mechanism cannot contribute to the single-bond binding magnitude.
This is the scope-(b) structural negative on the owner-suggested route. -/
theorem cluster3_single_bond_vanishes (E₀ g₀ gₐ : Int) :
    cluster3 E₀ g₀ gₐ g₀ gₐ = 0 := by
  dsimp [cluster3]
  omega

/-! ### The telescoping decomposition: where the deuteron content actually lives -/

/-- **Möbius / inclusion decomposition of the total two-bond change.**  The full
change of the joint block-trace from the empty configuration to both bonds
present decomposes exactly into the two first-order (single-bond) terms plus the
one second-order (3-body) term:

    g_ab − g_∅ = Δ¹g_a + Δ¹g_b + Δ²g.

This is the finite Möbius inversion on the Boolean lattice `{∅, a, b, ab}`. -/
theorem total_change_decomp (g₀ gₐ g_b gₐᵦ : Int) :
    gₐᵦ - g₀ = firstDiff g₀ gₐ + firstDiff g₀ g_b + secondDiff g₀ gₐ g_b gₐᵦ := by
  dsimp [firstDiff, secondDiff]
  omega

/-- **The deuteron's binding content is entirely FIRST-order.**  Specialising the
decomposition to a single-bond configuration (`g_b = g_∅`, `g_ab = g_a`): the
total change equals `firstDiff g₀ gₐ` alone — the second-order (μ₃) and the
absent-bond first-order terms both vanish.  Hence the deuteron magnitude is
carried by the bare per-bond amplitude `Δ¹g`, and any deficit in it (the 5.853×)
**cannot** be recovered from cluster structure, which is empty here. -/
theorem deuteron_content_is_first_order (g₀ gₐ : Int) :
    gₐ - g₀
      = firstDiff g₀ gₐ
        + firstDiff g₀ g₀        -- absent second bond: contributes 0
        + secondDiff g₀ gₐ g₀ gₐ -- μ₃ door: contributes 0
    ∧ firstDiff g₀ g₀ = 0
    ∧ secondDiff g₀ gₐ g₀ gₐ = 0 := by
  dsimp [firstDiff, secondDiff]
  refine ⟨?_, ?_, ?_⟩ <;> omega

/-! ### Contrapositive framing: a nonzero μ₃ contribution REQUIRES a real second bond

The only way the second mixed difference is nonzero is if the second bond is
genuinely present — i.e. `g_b ≠ g_∅` or `g_ab ≠ g_a`.  For the deuteron neither
holds (there is one bond), so the door is provably shut-because-absent. -/

/-- **A nonzero μ₃ door forces a genuinely present second bond.**  If
`secondDiff g₀ gₐ g_b gₐᵦ ≠ 0` then the configuration is *not* single-bond:
`g_b ≠ g₀ ∨ gₐᵦ ≠ gₐ`.  Contrapositive of `secondDiff_single_bond_vanishes`
lifted to arbitrary second-bond values — the μ₃ mechanism is exclusive to
A ≥ 3. -/
theorem nonzero_cluster_needs_second_bond
    {g₀ gₐ g_b gₐᵦ : Int} (h : secondDiff g₀ gₐ g_b gₐᵦ ≠ 0) :
    g_b ≠ g₀ ∨ gₐᵦ ≠ gₐ := by
  by_cases hb : g_b = g₀
  · by_cases hab : gₐᵦ = gₐ
    · have h0 : secondDiff g₀ gₐ g_b gₐᵦ = 0 := by
        rw [hb, hab]
        exact secondDiff_single_bond_vanishes g₀ gₐ
      exact absurd h0 h
    · exact Or.inr hab
  · exact Or.inl hb

/-- Whenever the total two-bond change is purely additive in the single-bond
first differences (`gₐᵦ - g₀ = firstDiff g₀ gₐ + firstDiff g₀ g_b`), the second
mixed difference `secondDiff g₀ gₐ g_b gₐᵦ` and the three-body cluster
`cluster3 E₀ g₀ gₐ g_b gₐᵦ` both vanish. -/
theorem secondDiff_and_cluster3_zero_of_additive (E₀ g₀ gₐ g_b gₐᵦ : Int)
    (hadd : gₐᵦ - g₀ = firstDiff g₀ gₐ + firstDiff g₀ g_b) :
    secondDiff g₀ gₐ g_b gₐᵦ = 0 ∧ cluster3 E₀ g₀ gₐ g_b gₐᵦ = 0 := by
  have htot := total_change_decomp g₀ gₐ g_b gₐᵦ
  have hs0 : secondDiff g₀ gₐ g_b gₐᵦ = 0 := by omega
  refine ⟨hs0, ?_⟩
  dsimp [cluster3, secondDiff] at hs0 ⊢
  have hpar : gₐ + g_b - g₀ - gₐᵦ = 0 := by omega
  rw [hpar, Int.mul_zero]

end QOU.MassTheory.DeuteronFirstOrderCluster
