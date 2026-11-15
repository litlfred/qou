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

- [leitner2026] Ch. 6, §3
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
-- Ref: [leitner2026] Ch. 6, §3
def proton_partition : BorromeanBaryon where
  color := ![0, 1, 2]
  orientation := ![1, 1, -1]
  -- Ref: [leitner2026] Ch. 6, §3
  charge_sum := by decide

/-- The neutron: one up (+1) and two down (-1), net charge 0.
    Color assignment: one quark per color tube (bijective). -/
-- Ref: [leitner2026] Ch. 6, §3
def neutron_partition : BorromeanBaryon where
  color := ![0, 1, 2]
  orientation := ![1, -1, -1]
  -- Ref: [leitner2026] Ch. 6, §3
  charge_sum := by decide

/-- Hyperbolic volume of the Borromean complement. -/
-- Ref: [thurston1978]
def borromean_volume : ℝ := 7.32772

/-- The baryon mass from the topological mass formula. -/
-- Ref: [leitner2026] Ch. 6, §3
def baryon_mass (q : ℝ) (_hq : q > 1) : ℝ :=
  borromean_volume / (1 - 1/q)^2

-- ── The mass calibration, as what it is ───────────────────────

/-- **The mass calibration, stated as an identity rather than as a
    discharged hypothesis** (bean `qou-znut`, resolved 2026-08-24).

    This was a `class BorromeanQuark` with a `topological_mass : ℝ → ℝ`
    field and a `volume_calibrates_mass` field asserting that field
    equals `borromean_volume / (1 - 1/q)²`, plus an unguarded
    `instance canonical` supplying the right-hand side as the field's
    value so the assertion closed by `rfl`.

    The reading recorded here is that this is **definitional and that is
    correct**: `topological_mass` never was an independent functional
    that had to be shown to agree with a volume formula. It *is* the
    volume formula. The instance's docstring said so — "the
    mass-calibration identity holds definitionally" — and the class
    docstring already conceded the part that is genuinely open, that
    exhibiting a Borromean configuration "does not establish that the
    physical nucleon is one" and that identification "stays an **open**
    conjectural interpretation in the narrative".

    What the typeclass added was the appearance of a hypothesis. A
    reader meeting `theorem baryon_mass_from_volume [BorromeanQuark]`
    takes it for a derivation of baryon mass from hyperbolic volume,
    discharged by an instance; it is a rewriting of a definition, and
    `baryon_mass` below was already that definition. Since the reading
    is that there was nothing to discharge, the honest shape is the one
    without the binder — a `def` and a `theorem … := rfl`. Dropping the
    class changes no proof: `baryon_mass_from_volume`'s content is
    unchanged, and it now says as much in its type.

    **What is NOT claimed here, and was not claimed before.** That the
    physical nucleon mass is `borromean_volume / (1 - 1/q)²`. That is
    `conj:borromean-quark`, it lives in the narrative, and no Lean
    declaration in this file asserts it. -/
theorem baryon_mass_from_volume (q : ℝ) (hq : q > 1) :
    baryon_mass q hq = borromean_volume / (1 - 1/q)^2 :=
  rfl

end QOU.Archimedean

end
