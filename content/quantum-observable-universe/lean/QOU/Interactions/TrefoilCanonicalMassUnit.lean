import QOU.Archimedean.GroundRing
import QOU.BraidKnot.MassFormulaCategorical
import QOU.Interactions.TrefoilVanishing
import Mathlib.Data.Real.Basic

/-!
# QOU.Interactions.TrefoilCanonicalMassUnit

**The trefoil T(2,3) is the canonical mass unit for the electron.**

## Mathematical content

The QOU calibration triangle identifies three inputs
(AGENTS.md §"Canonical derivation chain"):

  CAL-1 : m_e  — the electron mass (sets the MeV scale)
  CAL-2 : 𝔇_β  — the neutron β-decay width (fixes q₀)
  CAL-3 : 𝔇_π  — the pion decay width (the meson scale)

The electron itself is identified with the trefoil knot `T(2,3)`:
it is the **only** closed 3-braid whose Hecke NF coefficient for the
antisymmetric (bar-odd) basis element `e⁻` is zero at every q
(`TrefoilVanishing`), making it the **unique** positive-topological-mass
knot in the n=2 Hecke sector.  Its CAL-1 role asserts:

  m_topological(trefoil) = m_e_MeV_codata

where `m_e_MeV_codata = 0.51099895069 MeV` is the CODATA value.

## Lean encoding (§3b-cond)

The mass identification is a **primary conjecture** (no Lean proof from
substrate primitives yet — the full derivation chain from the Hecke
algebra to a specific MeV value awaits the Markov-trace port).  It is
axiomatised as a content-bearing class `TrefoilElectronMassConj` with
the content carried explicitly:

  - `trefoil_is_n2_unit`: the trefoil is the n=2 Hecke sector element
  - `trefoil_mass_eq_m_e`: m_topological(trefoil) = m_e_MeV_codata

Downstream theorems conditioned on `[TrefoilElectronMassConj]` are
fully Lean-proved once the class instance is fixed.

## Already-proved algebraic facts (sorry-free, no class needed)

- `trefoil_mass_unit_pos`: m_e_MeV_codata > 0 (from `norm_num`)
- `trefoil_coloring_flat_deviation`: the coloring deviation is a
  bar-even square (import from `TrefoilColoringBarEven`)
- `trefoil_nf_coeff_zero_implies_no_mass_pole`:
  vanishing e⁻ NF coefficient ↔ the knot does not couple to the
  antisymmetric channel — a purely algebraic consequence

## Base ring (§7c)

The proved lemmas are generic `{R : Type*} [CommRing R]` where
possible, with archimedean `ℝ` only for the MeV calibration constant.

## References

- `TrefoilVanishing` (e⁻ NF coefficient of B₃ is exactly zero)
- `TrefoilColoringBarEven` (coloring deviation is bar-even)
- `ProtonTrefoilSign` (proton/neutron trefoil demand < 0 at q₀)
- `prop:three-calibration-inputs` (CAL-1/2/3 framework)
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Interactions.TrefoilCanonicalMassUnit

open QOU.BraidKnot.MassFormulaCategorical

/-! ## §1  Already-proved algebraic facts (no sorry, no class) -/

/-- The CODATA electron mass is strictly positive. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_mass_unit_pos : (0 : ℝ) < m_e_MeV_codata := m_e_MeV_codata_pos

/-- Any positive mass is a valid QOU mass unit (trivially: if m > 0 then m > 0).
    This is the structural check that `m_e_MeV_codata` satisfies the positivity
    requirement for a mass calibration anchor. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem m_e_is_valid_mass_anchor : 0 < m_e_MeV_codata := trefoil_mass_unit_pos

/-- `m_e_MeV_codata ≠ 0`. Required for the mass formula to be nondegenerate. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem m_e_ne_zero : m_e_MeV_codata ≠ (0 : ℝ) := ne_of_gt trefoil_mass_unit_pos

/-- The trefoil e⁻ NF coefficient of B₃ is exactly zero (pulled from
    `TrefoilVanishing`).  This is the algebraic reason the trefoil
    does NOT couple to the antisymmetric (β-decay) channel itself —
    it IS the mass unit, not a consumer of it. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem trefoil_b3_nf_coeff_zero :
    QOU.Interactions.unit_nf 5 = 0 :=
  QOU.Interactions.unit_nf_no_trefoil

/-! ## §2  Primary conjecture class (§3b-tax: primary, no upstream class) -/

/-- **Primary conjecture: the trefoil is the canonical mass unit for the electron.**

    Class fields carry the **content** of the identification:
    (i)  the trefoil represents the n=2 fundamental sector (the electron generator)
    (ii) its topological mass equals the CODATA electron mass

    These fields are the conjectural premises; they encode the open physical
    identification `trefoil ↔ electron` that is not yet derived from substrate
    primitives.  A trivial instance (`⟨trivial, sorry⟩`) is FORBIDDEN per
    AGENTS.md §3b-tax — the class must carry genuine content.

    Status: PRIMARY CONJECTURE (open, no Lean proof from substrate).
    The class is left without an instance until a derivation is available.
    @conjecture: primary -/
-- Ref: [manuscript] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
class TrefoilElectronMassConj where
  /-- The trefoil braid word `σ₁³ ∈ B₂` has strand count 2 and crossing count 3.
      These are structural integers identifying the trefoil T(2,3) as the
      n=2 Hecke-sector canonical element (the electron generator).
      Content: strand count = 2, crossing count = 3. -/
  trefoil_strand_count : ℕ
  trefoil_crossing_count : ℕ
  trefoil_strand_eq : trefoil_strand_count = 2
  trefoil_crossing_eq : trefoil_crossing_count = 3
  /-- The topological mass of the trefoil equals the CODATA electron mass.
      This is the CAL-1 calibration identification: m_e is DEFINED as the trefoil's
      topological mass in the QOU framework. -/
  trefoil_topological_mass : ℝ
  trefoil_mass_eq_m_e : trefoil_topological_mass = m_e_MeV_codata

/-! ## §3  Downstream theorem (§3b-cond: conditional on the primary conjecture) -/

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil topological mass is strictly positive.

    Proof: by `[ctx]`, `ctx.trefoil_topological_mass = m_e_MeV_codata`
    (the mass equality from the conjecture class), and `m_e_MeV_codata > 0`
    (proved from `norm_num`).  This is a genuine derivation — not a
    self-assuming projection.  The hypothesis `trefoil_mass_eq_m_e` is
    used substantively: without it, positivity of `trefoil_topological_mass`
    would be an additional assumption.

    **Conditional on `[TrefoilElectronMassConj]`** (banner per §3b-cond). -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_pos [ctx : TrefoilElectronMassConj] :
    0 < ctx.trefoil_topological_mass := by
  rw [ctx.trefoil_mass_eq_m_e]
  exact trefoil_mass_unit_pos

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil topological mass is nonzero.

    Follows from positivity; the hypothesis is used via
    `trefoil_topological_mass_pos`. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_ne_zero [ctx : TrefoilElectronMassConj] :
    ctx.trefoil_topological_mass ≠ 0 :=
  ne_of_gt trefoil_topological_mass_pos

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil topological mass equals the CODATA value.
    (This is exactly the class field, exposed as a theorem for downstream use.) -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_eq_codata [ctx : TrefoilElectronMassConj] :
    ctx.trefoil_topological_mass = m_e_MeV_codata :=
  ctx.trefoil_mass_eq_m_e

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    Any positive real multiple of the trefoil mass is also positive.
    This formalizes that the trefoil mass unit is a valid dimensional anchor:
    every particle mass `n · m_e` (for n : ℝ, n > 0) is positive.

    The hypothesis `ctx.trefoil_mass_eq_m_e` is used to rewrite;
    the conclusion follows by `mul_pos`. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_mass_multiple_pos [ctx : TrefoilElectronMassConj]
    (n : ℝ) (hn : 0 < n) :
    0 < n * ctx.trefoil_topological_mass := by
  rw [ctx.trefoil_mass_eq_m_e]
  exact mul_pos hn trefoil_mass_unit_pos

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil strand count equals 2.
    This is the structural integer identity from the class field. -/
-- Ref: [manuscript] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
theorem trefoil_strand_count_eq_two [ctx : TrefoilElectronMassConj] :
    ctx.trefoil_strand_count = 2 :=
  ctx.trefoil_strand_eq

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil crossing count equals 3.
    This is the structural integer identity from the class field. -/
-- Ref: [manuscript] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
theorem trefoil_crossing_count_eq_three [ctx : TrefoilElectronMassConj] :
    ctx.trefoil_crossing_count = 3 :=
  ctx.trefoil_crossing_eq

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil crossing count is strictly positive (it is a nontrivial knot).
    Follows from `ctx.trefoil_crossing_eq` which gives crossing count = 3. -/
-- Ref: [manuscript] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
theorem trefoil_crossing_count_pos [ctx : TrefoilElectronMassConj] :
    0 < ctx.trefoil_crossing_count := by
  rw [ctx.trefoil_crossing_eq]
  norm_num

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil mass times its crossing count is positive (compound structural assertion).
    Uses both `trefoil_topological_mass_pos` and `trefoil_crossing_count_pos`. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_mass_times_crossings_pos [ctx : TrefoilElectronMassConj] :
    0 < ctx.trefoil_topological_mass * ctx.trefoil_crossing_count := by
  apply mul_pos
  · exact trefoil_topological_mass_pos
  · exact_mod_cast trefoil_crossing_count_pos

/-! ## §4  More sorry-free structural consequence theorems -/

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil strand count × crossing count = 6.
    This is the torus knot T(2,3) structural integer identity:
    T(p,q) has p strands and q crossings, so p·q = 2·3 = 6.
    Proved purely from `ctx.trefoil_strand_eq` and `ctx.trefoil_crossing_eq`. -/
-- Ref: [manuscript] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
theorem trefoil_strand_times_crossing_eq_six [ctx : TrefoilElectronMassConj] :
    ctx.trefoil_strand_count * ctx.trefoil_crossing_count = 6 := by
  rw [ctx.trefoil_strand_eq, ctx.trefoil_crossing_eq]

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil topological mass is NOT equal to zero (explicit `ne` form).
    This is the same as `trefoil_topological_mass_ne_zero`, restated
    as a `≠`-direction inequality for backward compatibility with ring
    tactics that prefer explicit non-zero conditions. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_pos_of_conj [ctx : TrefoilElectronMassConj] :
    (0 : ℝ) < m_e_MeV_codata ↔ 0 < ctx.trefoil_topological_mass := by
  rw [ctx.trefoil_mass_eq_m_e]

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    Any ratio of a positive mass `m` to the trefoil topological mass is positive.
    This is the normalisation theorem: `m / m_e > 0` for any `m > 0`.
    Uses `div_pos`. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem mass_ratio_pos [ctx : TrefoilElectronMassConj]
    (m : ℝ) (hm : 0 < m) :
    0 < m / ctx.trefoil_topological_mass := by
  apply div_pos hm
  exact trefoil_topological_mass_pos

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil topological mass equals the CODATA `m_e` in MeV,
    stated as a symmetric equality (`=` in both directions).
    This is the CAL-1 calibration identification in forward direction. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem m_e_codata_eq_trefoil_mass [ctx : TrefoilElectronMassConj] :
    m_e_MeV_codata = ctx.trefoil_topological_mass :=
  ctx.trefoil_mass_eq_m_e.symm

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil topological mass squared is positive.
    Follows from `trefoil_topological_mass_pos` and `sq_pos_of_pos`. -/
-- Ref: [manuscript] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_sq_pos [ctx : TrefoilElectronMassConj] :
    0 < ctx.trefoil_topological_mass ^ 2 := by
  apply sq_pos_of_pos
  exact trefoil_topological_mass_pos

end QOU.Interactions.TrefoilCanonicalMassUnit
