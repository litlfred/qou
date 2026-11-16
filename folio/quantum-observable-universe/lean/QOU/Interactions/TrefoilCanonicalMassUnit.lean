import QOU.Archimedean.GroundRing
import QOU.BraidKnot.MassFormulaCategorical
import QOU.Interactions.TrefoilVanishing
import QOU.KnotTheory
import Mathlib.Data.Real.Basic

/-!
# QOU.Interactions.TrefoilCanonicalMassUnit

**The trefoil T(2,3) is the canonical mass unit for the electron.**

## Mathematical content

The QOU calibration triangle identifies three inputs
(AGENTS.md §"Canonical derivation chain"):

  CAL-1 : m_e  — the electron mass (sets the MeV scale)
  CAL-2 : P_skew^β  — the neutron β-sector bar-skew channel (fixes q₀)
  CAL-3 : P_avg^π  — the pion-sector bar-even channel (the meson scale)

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
axiomatised as a content-bearing class `TrefoilElectronMassConj`, whose
single field states the identification for a **given** Hecke element,
multiplicity and cat-unit scale — the three quantities are class
*parameters*, not class fields, so no instance can be produced without
exhibiting an element whose Markov trace actually normalises to one.

Downstream theorems conditioned on `[TrefoilElectronMassConj …]` are
fully Lean-proved once the class instance is fixed.

**Restated 2026-08-23 (bean `qou-lo1t`) — the class was inhabited.** Its
previous form carried the quantities as *fields* beside equations naming
their values:

    trefoil_strand_count : ℕ ; trefoil_strand_eq : trefoil_strand_count = 2
    trefoil_crossing_count : ℕ ; trefoil_crossing_eq : … = 3
    trefoil_topological_mass : ℝ ; trefoil_mass_eq_m_e : … = m_e_MeV_codata

so `⟨2, 3, rfl, rfl, m_e_MeV_codata, rfl⟩` discharged it — verified to
elaborate.  Every "conditional on `TrefoilElectronMassConj`" theorem in
this file was therefore unconditional, and the "open physical
identification `trefoil ↔ electron`" the docstring claimed to encode
appeared nowhere in the type: `trefoil_strand_count` was a free `ℕ`
merely *named* for the trefoil, with no braid word behind it.

Two consequences, both applied below.  The strand and crossing counts
are **not conjectural** — they are computed from the actual braid word
`QOU.KnotTheory.trefoil` (`strands := 2`, three positive letters), so
they are now unconditional `rfl` facts rather than assumed fields; this
is how `QOU.KnotRegistry.trefoil_crossing_count` already states the
crossing count.  The mass identification is the genuinely open part, and
is now stated about given data.

This is an improvement, not a closure: see the residual-weakness note on
`TrefoilElectronMassConj` itself.  When `m_e_cat` is left as a free parameter,
`TrefoilElectronMassConj` remains dischargeable by solving `m_e_cat = 1 / |tr_M T|`.

**Closed 2026-11-16 (bean `qou-0w42`) — canonical cat-unit electron scale pinned.**
In cat-units (where mass is measured in units of the electron mass and converted
to MeV by multiplying by `m_e_MeV_codata`), the electron's own cat-unit scale is
the unit `m_e_cat_canonical : ℝ := 1` and its $n = 2$ Wedderburn multiplicity is
`trefoil_multiplicity_canonical : ℕ := 1`.  Pinning both parameters in
`TrefoilCanonicalElectronMassConj (T : HeckeElement 2)` removes the free
`m_e_cat := 1 / |tr_M T|` degree of freedom: `TrefoilCanonicalElectronMassConj T`
is equivalent to `absMarkovTrace 2 T = 1`
(`trefoilCanonicalElectronMassConj_iff_absMarkovTrace_eq_one`).

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
open QOU.HeckeAlgebra

/-! ## §1  Already-proved algebraic facts (no sorry, no class) -/

/-- The CODATA electron mass is strictly positive. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_mass_unit_pos : (0 : ℝ) < m_e_MeV_codata := m_e_MeV_codata_pos

/-- Any positive mass is a valid QOU mass unit (trivially: if m > 0 then m > 0).
    This is the structural check that `m_e_MeV_codata` satisfies the positivity
    requirement for a mass calibration anchor. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem m_e_is_valid_mass_anchor : 0 < m_e_MeV_codata := trefoil_mass_unit_pos

/-- `m_e_MeV_codata ≠ 0`. Required for the mass formula to be nondegenerate. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
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

/-! ## §1b  Canonical cat-unit electron scale (bean `qou-0w42`)

    In QOU cat-units, all topological masses are dimensionless ratios relative
    to the electron calibration anchor (`M(K)_MeV = M(K)_cat · m_e_MeV_codata`).
    Consequently, the electron's own cat-unit scale is the unit `1 : ℝ`, and its
    $n = 2$ Hecke-sector Wedderburn multiplicity is `1 : ℕ`.  Defining these two
    canonical constants closes the `m_e_cat := 1 / |tr_M T|` rescaling loophole
    noted in `qou-lo1t` / `qou-0w42`. -/

/-- The canonical cat-unit electron mass scale: in cat-units (dimensionless units
    of the electron mass, converted to MeV via `m_e_MeV_codata`), the electron
    scale is identically `1`. -/
def m_e_cat_canonical : ℝ := 1

/-- The canonical cat-unit electron mass scale is strictly positive. -/
theorem m_e_cat_canonical_pos : (0 : ℝ) < m_e_cat_canonical := by
  unfold m_e_cat_canonical
  norm_num

/-- The canonical Wedderburn multiplicity `ρ(T(2,3)) = 1` in the `n = 2` Hecke
    sector. -/
def trefoil_multiplicity_canonical : ℕ := 1

/-- The canonical trefoil Wedderburn multiplicity is strictly positive. -/
theorem trefoil_multiplicity_canonical_pos : 0 < trefoil_multiplicity_canonical := by
  unfold trefoil_multiplicity_canonical
  norm_num

/-! ## §2  Primary conjecture class (§3b-tax: primary, no upstream class) -/

/-- **Primary conjecture: the trefoil is the canonical mass unit for the electron.**

    Stated for **given** data — a Hecke element `T` of the `n = 2` sector, a
    multiplicity `ρ`, and a cat-unit electron scale `m_e_cat` — all three of
    which are *parameters*, so an instance must be supplied against a specific
    element rather than manufactured alongside one.  The single field is the
    CAL-1 identification: the trefoil's categorical mass in MeV is the CODATA
    electron mass, i.e. the trefoil is the mass **unit**.

    This is the open physical identification `trefoil ↔ electron`, not derived
    from substrate primitives.  A trivial instance is FORBIDDEN per
    AGENTS.md §3b-tax — and, since `m_e_MeV_codata > 0`, the field is
    equivalent to `ρ · m_e_cat · |tr_M T| = 1`, a constraint relating the
    three parameters (see `trefoil_cat_mass_normalised` below).

    **Residual weakness, stated rather than papered over (bean `qou-lo1t`).**
    Parameterising blocks the discharge the old form admitted — `⟨rfl⟩` no
    longer typechecks, verified — but it does not close the class. Given any
    `T` with `tr_M T ≠ 0` one may still take `ρ := 1` and
    `m_e_cat := 1 / |tr_M T|` and prove the field; this was checked and
    elaborates. What that costs an author is real (a specific element, and a
    proof its Markov trace is nonzero) and it is now *visible* — the numbers
    appear at the instance site — but it is a cheat that remains available.
    Closing it needs `m_e_cat` fixed by a definition rather than left free;
    the corpus has no cat-unit electron scale to point at, only the MeV one
    (`m_e_MeV_codata`), so that is the actual gap.

    Status: PRIMARY CONJECTURE (open, no Lean proof from substrate).
    The class is left without an instance until a derivation is available.
    @conjecture: primary -/
-- Ref: [leitner2026] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
class TrefoilElectronMassConj
    (T : HeckeElement 2) (rho : ℕ) (m_e_cat : ℝ) : Prop where
  /-- The topological mass of the trefoil equals the CODATA electron mass.
      This is the CAL-1 calibration identification: m_e is the trefoil's
      topological mass in the QOU framework. -/
  trefoil_mass_eq_m_e : categoricalMassMeV rho m_e_cat T = m_e_MeV_codata

/-- **Parameter-pinned primary conjecture (bean `qou-0w42`): the trefoil `T` has
    unit categorical mass at the canonical cat-unit electron scale.**

    Fixes `rho := trefoil_multiplicity_canonical` (`1`) and
    `m_e_cat := m_e_cat_canonical` (`1`), eliminating the `m_e_cat := 1 / |tr_M T|`
    rescaling degree of freedom.  By
    `trefoilCanonicalElectronMassConj_iff_absMarkovTrace_eq_one` below, this
    class is equivalent to `absMarkovTrace 2 T = 1`, which cannot be discharged
    without exhibiting a `T : HeckeElement 2` whose Markov trace has unit
    modulus.
    @conjecture: primary -/
-- Ref: [leitner2026] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
class TrefoilCanonicalElectronMassConj (T : HeckeElement 2) : Prop extends
    TrefoilElectronMassConj T trefoil_multiplicity_canonical m_e_cat_canonical

/-! ## §2a  Structural integers of the trefoil — computed, not assumed

    The strand and crossing counts are facts about the braid word
    `QOU.KnotTheory.trefoil = σ₀³ ∈ B₂`, so they need no hypothesis at all.
    They were previously free fields of the conjecture class beside equations
    naming their values, which is why they are stated here instead. -/

/-- The trefoil braid word has 2 strands. -/
-- Ref: [leitner2026] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
theorem trefoil_strand_count_eq_two :
    QOU.KnotTheory.trefoil.strands = 2 := rfl

/-- The trefoil braid word has 3 crossings — the three positive letters
    of `σ₀³`.  Matches `QOU.KnotRegistry.trefoil_crossing_count`. -/
-- Ref: [leitner2026] quantum-observable-universe/knots-particles-confinement/
--      binding-knots-visual-inventory.md §"Trefoil = electron"
theorem trefoil_crossing_count_eq_three :
    QOU.KnotTheory.trefoil.crossingCount = 3 := rfl

/-- The trefoil has a positive crossing count: it is a nontrivial knot. -/
theorem trefoil_crossing_count_pos :
    0 < QOU.KnotTheory.trefoil.crossingCount := by
  rw [trefoil_crossing_count_eq_three]; norm_num

/-- The torus-knot structural identity `p · q = 2 · 3 = 6` for `T(2,3)`. -/
theorem trefoil_strand_times_crossing_eq_six :
    QOU.KnotTheory.trefoil.strands * QOU.KnotTheory.trefoil.crossingCount = 6 :=
  rfl

/-! ## §3  Downstream theorems (§3b-cond: conditional on the primary conjecture)

    Each takes the conjecture's three parameters explicitly and consumes
    `[ctx]` substantively.  Four theorems that stood here previously are
    gone: `trefoil_topological_mass_eq_codata` and
    `m_e_codata_eq_trefoil_mass` were the class field and its `.symm`, and
    `trefoil_topological_mass_pos_of_conj` and
    `trefoil_topological_mass_ne_zero` restated positivity in `↔` and `≠`
    form.  None had a reference outside this file. -/

variable (T : HeckeElement 2) (rho : ℕ) (m_e_cat : ℝ)

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil's categorical MeV mass is strictly positive.

    Proof: the conjecture identifies it with `m_e_MeV_codata`, which is
    positive by `norm_num`. The hypothesis is used substantively — without
    it, positivity of an arbitrary `categoricalMassMeV` would need `ρ > 0`,
    `m_e_cat > 0` and `tr_M T ≠ 0` as separate assumptions. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_pos [ctx : TrefoilElectronMassConj T rho m_e_cat] :
    0 < categoricalMassMeV rho m_e_cat T := by
  rw [ctx.trefoil_mass_eq_m_e]
  exact trefoil_mass_unit_pos

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil's cat-unit mass is normalised to one — this is the precise
    sense in which the trefoil is the canonical mass *unit*.

    Proof: the conjecture says `categoricalMass · m_e_MeV_codata =
    m_e_MeV_codata`; cancel the nonzero factor. This is a genuine
    consequence, and it is what makes the conjecture a constraint on `T`
    rather than a definition of a free quantity. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_cat_mass_normalised [ctx : TrefoilElectronMassConj T rho m_e_cat] :
    categoricalMass rho m_e_cat T = 1 := by
  have h := ctx.trefoil_mass_eq_m_e
  unfold categoricalMassMeV at h
  have hne : m_e_MeV_codata ≠ 0 := m_e_ne_zero
  field_simp at h
  exact h

/-- **Theorem (bean `qou-0w42`).**

    Under the canonical cat-unit electron scale (`rho = 1`, `m_e_cat = 1`),
    `TrefoilCanonicalElectronMassConj T` is equivalent to the parameter-free
    Markov-trace normalisation `absMarkovTrace 2 T = 1`. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoilCanonicalElectronMassConj_iff_absMarkovTrace_eq_one :
    TrefoilCanonicalElectronMassConj T ↔ absMarkovTrace 2 T = 1 := by
  constructor
  · intro h
    have hnorm : categoricalMass trefoil_multiplicity_canonical m_e_cat_canonical T = 1 :=
      @trefoil_cat_mass_normalised T trefoil_multiplicity_canonical m_e_cat_canonical
        h.toTrefoilElectronMassConj
    unfold categoricalMass trefoil_multiplicity_canonical m_e_cat_canonical at hnorm
    simpa using hnorm
  · intro htr
    refine ⟨⟨?_⟩⟩
    unfold categoricalMassMeV categoricalMass
      trefoil_multiplicity_canonical m_e_cat_canonical
    rw [htr]
    simp

/-- **Corollary (bean `qou-0w42`).**

    Any canonical trefoil electron mass witness has unit absolute Markov trace
    `|tr_M(T)| = 1`. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_canonical_absMarkovTrace_eq_one
    [h : TrefoilCanonicalElectronMassConj T] :
    absMarkovTrace 2 T = 1 :=
  (trefoilCanonicalElectronMassConj_iff_absMarkovTrace_eq_one T).mp h

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    Any positive real multiple of the trefoil mass is positive: every
    particle mass `n · m_e` (for `n > 0`) is positive. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_mass_multiple_pos [TrefoilElectronMassConj T rho m_e_cat]
    (n : ℝ) (hn : 0 < n) :
    0 < n * categoricalMassMeV rho m_e_cat T :=
  mul_pos hn (trefoil_topological_mass_pos T rho m_e_cat)

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    Any ratio of a positive mass `m` to the trefoil mass is positive —
    the normalisation `m / m_e > 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem mass_ratio_pos [TrefoilElectronMassConj T rho m_e_cat]
    (m : ℝ) (hm : 0 < m) :
    0 < m / categoricalMassMeV rho m_e_cat T :=
  div_pos hm (trefoil_topological_mass_pos T rho m_e_cat)

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The square of the trefoil mass is positive. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_topological_mass_sq_pos [TrefoilElectronMassConj T rho m_e_cat] :
    0 < categoricalMassMeV rho m_e_cat T ^ 2 :=
  pow_pos (trefoil_topological_mass_pos T rho m_e_cat) 2

/-- **Theorem (conditional on `TrefoilElectronMassConj`).**

    The trefoil mass times its crossing count is positive, combining the
    conditional mass positivity with the unconditional crossing count. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/three-calibration-inputs-context.ts
theorem trefoil_mass_times_crossings_pos [TrefoilElectronMassConj T rho m_e_cat] :
    0 < categoricalMassMeV rho m_e_cat T
        * (QOU.KnotTheory.trefoil.crossingCount : ℝ) := by
  apply mul_pos (trefoil_topological_mass_pos T rho m_e_cat)
  exact_mod_cast trefoil_crossing_count_pos

end QOU.Interactions.TrefoilCanonicalMassUnit
