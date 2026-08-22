import QOU.Torsion.MassIdentity

/-!
# §7  Mass Identity — archimedean realisation

The observable-side layer of `def:mass-identity`: the substrate parameter and
the non-negativity of the integrand.

## Base ring (§7c) — this is the post-wall half of a deliberate split

`QOU/Torsion/MassIdentity.lean` holds the **generic core**, over an arbitrary
`[CommRing R]`.  This file holds everything that needs the wall, and it needs
its own module rather than a section of the core because `check-wall-side`
treats a real-field type coexisting with generic-`R` markers in one file as a
split-me defect — correctly, and it caught a first attempt that kept both here.

Two things live on this side, and only two:

* `sp : SubstrateParameter M` — irreducibly archimedean.  Its `field : M → ℝ`
  comes with `field_pos`, `field_ge_one` and `not_root_of_unity`: order
  conditions and a root-of-unity condition, none of which a generic ring can
  state.
* `integrand_nonneg` — an **order** on the codomain.

Everything else — the cycle, its non-emptiness, and the two
multiplicative-integration factors — is ring-free or generic and stays in the
core.

## Why the split cost nothing

`MassIdentity.sp` was **inert**: nothing anywhere in the tree read it
(grep-verified; the `.sp` hits are `Symplectic.sp`, `cr.sp` and
`eigenvalue.sp` on unrelated structures).  So the deeper of the two archimedean
anchors came out for free.  And the only consumer,
`TopologicalMassDecomposition`, is `ℝ` throughout already — it wanted this
layer all along and simply was not labelled as one.

Bean `qou-puwe`, option 1.  **Fixes the wall-side defect only**; the block's
prose still defines mass as the Frobenius–Hopf categorical trace while the core
formalises nonabelian multiplicative integration, which is option 3 and remains
open.
-/


namespace QOU.Torsion

/-- **Archimedean realisation of the mass identity.**

    The generic core plus exactly what needs the wall: the substrate parameter,
    and the non-negativity of the integrand on the cycle.

    An `ℝ`-instantiation of `MassIdentity` — the core's ring is fixed here and
    nowhere earlier. -/
structure ArchimedeanMassIdentity (M : Type*) extends MassIdentity ℝ M where
  /-- The substrate parameter `q : M → ℝ`.  Archimedean by construction: its
      `field` is ordered and bounded below by `1`. -/
  sp : SubstrateParameter M
  /-- The integrand is non-negative on the cycle.  An **order** condition, and
      the reason this structure cannot live in the generic core. -/
  integrand_nonneg : ∀ (p : M), p ∈ vortexCycle →
    0 ≤ connectionGradient p * leviCurvatureCoupling p

/-- **Corollary (ℂ mass identity).**
    LaTeX: `\label{cor:mass-identity-C}` -/
structure MassIdentityC (M : Type*) extends ArchimedeanMassIdentity M where
  cqou : CQuantumObservableUniverse
  base_eq : cqou.M = M
  cycle_dim : ℕ := 2
  cr_compatible : cycle_dim ≤ 2 * cqou.n := by omega
  mass_nonneg : ∀ (p : M), p ∈ vortexCycle →
    0 ≤ connectionGradient p * leviCurvatureCoupling p :=
    integrand_nonneg

end QOU.Torsion
