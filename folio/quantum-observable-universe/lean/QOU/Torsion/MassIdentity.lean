import QOU.QuantumObservableUniverse

/-!
# §7  Mass Identity — generic core

The inertial mass of a stable vortex via nonabelian multiplicative
integration (Yekutieli): `m = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖`.

## Base ring (§7c) — split at the wall (bean `qou-puwe`, option 1)

`GroundRingAnnotations` lists `Torsion/` as **generic `k`, formal chain ✓**,
while this structure was `ℝ`-valued throughout.  That was an in-tree
contradiction, not an inference.  Resolved by splitting at the substrate wall,
following the pattern `QOU/Torsion/HeckeMassElement.lean` already establishes
one file away: a generic core, then a separate archimedean realisation.

This file is the **pre-wall half**.  Nothing here is ordered, normed, or fed to
a real-analytic function.  The observable-side content —
`ArchimedeanSubstrateField` and the integrand's non-negativity — lives in
`QOU/Torsion/ArchimedeanMassIdentity.lean`, in its **own module**: a real-field
type coexisting with generic-`R` markers in one file is precisely what
`check-wall-side` flags, and it caught a first attempt that kept both here.

**What moved, and why each move was free:**

* `sp : ArchimedeanSubstrateField M` — irreducibly archimedean, and **inert**:
  nothing in the tree ever read `MassIdentity.sp` (grep-verified; the `.sp`
  hits are `Symplectic.sp`, `cr.sp` and `eigenvalue.sp` on unrelated
  structures).  The deeper of the two anchors came out at zero cost.
* `integrand_nonneg` — an **order** on the codomain, which a generic
  `CommRing` cannot state.
* `connectionGradient` and `leviCurvatureCoupling` generalise to `M → R`;
  neither was ordered or normed here.

`vortexCycle` and `cycle_nonempty` were already ring-free.

**Scope.** This is option 1 of `qou-puwe` and fixes the **wall-side** defect
only.  The other defect that bean records is untouched: `mass-identity.md`
defines mass as the Frobenius–Hopf **categorical trace**
`m(ϱ) = ‖tr((∫_A ⊗ id) ∘ Δ ∘ ϱ)‖`, whereas this file formalises **nonabelian
multiplicative integration**, and neither text mentions the other's formula.
The ref is correct — it carries the block's own label — but the mathematics is
a different object.  Closing that is option 3, and it remains open.
-/


namespace QOU.Torsion

/-! ## §7  Mass Identity -/

/-- **Mass Identity** (generic core): `m = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖`.

    The vortex cycle together with the two multiplicative-integration factors,
    over an arbitrary base ring.  The archimedean realisation is
    `QOU.Torsion.ArchimedeanMassIdentity`.

    LaTeX: `\label{def:mass-identity}` -/
structure MassIdentity (R : Type*) [CommRing R] (M : Type*) where
  /-- `∇_A q`, the connection gradient along the cycle. -/
  connectionGradient : M → R
  /-- The Levi curvature coupling `L ∧ F⁺` along the cycle. -/
  leviCurvatureCoupling : M → R
  /-- The vortex cycle `γ ⊆ Σ` being integrated over. -/
  vortexCycle : Set M
  /-- The cycle is not empty — there is something to integrate. -/
  cycle_nonempty : vortexCycle.Nonempty

end QOU.Torsion
