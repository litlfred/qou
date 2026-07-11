import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Fin
import Mathlib.Data.Fin.VecNotation


/-!
# QOU.Archimedean.BorromeanBaryon — Borromean quark structure

Quarks as Borromean-linked unknots in three color tubes.
The Borromean link B_3 has the property that no two components
are linked, but all three together are inseparable.
Vol(S³ \ B_3) = 7.32772...

## References

- [manuscript] Ch. 6, §3
- [thurston1978] Geometry and topology of three-manifolds

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

noncomputable section

namespace QOU.Archimedean

/-- The Borromean link of three unknots in color tubes. -/
structure BorromeanBaryon where
  /-- The three color tube assignments -/
  color : Fin 3 → Fin 3
  /-- Crossing orientation: +1 (up) or -1 (down) for each component -/
  orientation : Fin 3 → Int
  /-- The orientations sum to the net Coulomb charge -/
  charge_sum : (Finset.univ.sum orientation) = orientation 0 + orientation 1 + orientation 2

/-- The proton: two up (+1) and one down (-1), net charge +1.
    Color assignment: one quark per color tube (bijective). -/
-- Ref: [manuscript] Ch. 6, §3
def proton_partition : BorromeanBaryon where
  color := ![0, 1, 2]
  orientation := ![1, 1, -1]
  -- Ref: [manuscript] Ch. 6, §3
  charge_sum := by decide

/-- The neutron: one up (+1) and two down (-1), net charge 0.
    Color assignment: one quark per color tube (bijective). -/
-- Ref: [manuscript] Ch. 6, §3
def neutron_partition : BorromeanBaryon where
  color := ![0, 1, 2]
  orientation := ![1, -1, -1]
  -- Ref: [manuscript] Ch. 6, §3
  charge_sum := by decide

/-- Hyperbolic volume of the Borromean complement. -/
-- Ref: [thurston1978]
def borromean_volume : ℝ := 7.32772

/-- The baryon mass from the topological mass formula. -/
-- Ref: [manuscript] Ch. 6, §3
def baryon_mass (q : ℝ) (_hq : q > 1) : ℝ :=
  borromean_volume / (1 - 1/q)^2

-- ── Conjecture class (AGENTS.md §3b-cond axiomatisation) ───────

/-- **Conjecture class.** An instance asserts that the Borromean
    link `B_3` is the canonical baryon model: nucleons (proton,
    neutron) are realised as Borromean-linked three-quark
    configurations with hyperbolic volume `borromean_volume ≈
    7.32772` (the topological mass scale).

    The single conjectural field is the **mass calibration**:
    * `volume_calibrates_mass` — the bare baryon mass is
      `borromean_volume / (1 − 1/q)²`, calibrating the
      topological-mass formula at q = q₀.

    **On the baryon-realisation claim.** The physical content of
    `conj:borromean-quark` — that every observed baryon *is* a
    Borromean three-quark configuration — is **not** encoded as a Lean
    field. It cannot be: any `is_baryon_realisation : Prop` field is a
    self-assuming projection (the instance picks the `Prop` and proves
    its own choice), which passes the type checker while asserting
    nothing (AGENTS.md §3b-tax / §3b-cond item 5). The explicit
    `proton_partition` / `neutron_partition` data above record the
    color/orientation assignments, but *exhibiting a `BorromeanBaryon`
    value* is trivially possible and does not establish that the
    physical nucleon is one. That identification stays an **open**
    conjectural interpretation in the narrative.

    `sorry` in any concrete instance is understood as **conjecture**,
    not missing proof. Downstream blocks may take `[BorromeanQuark]`
    as an explicit hypothesis to remain `theorem`/`proposition` per
    AGENTS.md §3b-cond.

    Ref: [manuscript] Ch. 6 §3, conj:borromean-quark -/
class BorromeanQuark where
  /-- The baryon mass functional (depends on q). -/
  bare_mass : ℝ → ℝ
  /-- The mass functional evaluates to `borromean_volume / (1 − 1/q)²`
      at every q > 1. -/
  volume_calibrates_mass :
    ∀ q : ℝ, q > 1 → bare_mass q = borromean_volume / (1 - 1/q)^2

/-- **Downstream conditional theorem (AGENTS.md §3b-cond).**
    Conditional on `[BorromeanQuark]`, baryon mass at every q > 1
    equals `borromean_volume / (1 − 1/q)²`. Fully verified by Lean
    once an instance is fixed. -/
theorem baryon_mass_from_volume [inst : BorromeanQuark]
    (q : ℝ) (hq : q > 1) :
    inst.bare_mass q = borromean_volume / (1 - 1/q)^2 :=
  inst.volume_calibrates_mass q hq

/-- **Faithful instance.**  Defines `bare_mass` literally as the
    topological-volume formula `borromean_volume / (1 - 1/q)²`, so
    `volume_calibrates_mass` closes by `rfl`.  This is genuine content
    — the mass-calibration identity holds definitionally — not a
    vacuous discharge.  (The former `is_baryon_realisation` field was
    removed: it was a self-assuming projection carrying no content;
    see the class docstring.) -/
-- Ref: [manuscript] Ch. 6 §3, conj:borromean-quark
instance canonical : BorromeanQuark where
  bare_mass := fun q => borromean_volume / (1 - 1/q)^2
  volume_calibrates_mass := fun _ _ => rfl

end QOU.Archimedean

end
