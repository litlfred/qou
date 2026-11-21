/-
  Watson uniqueness on the sector-at-0 — the final wiring (bean el8w tranche 5).

  Assembles the two halves of the Watson change of variables into the full
  sector statement:
    * `watson_uniqueness_rhp_open` (`BorelWatsonShiftFull`) — Watson uniqueness
      on the open right HALF-PLANE `{re > 0}`;
    * `sectorTransport_mapsTo` (`BorelWatsonSectorTransport`) — the carrier
      `Φ_t(z) = (z^t)⁻¹` maps the SECTOR `{z ≠ 0 : |arg z| < π/(2t)}` (opening
      `π/t = βπ > π`) into `{re > 0}`.

  A function on the sector whose values are the PULLBACK `f = F ∘ Φ_t` of a
  half-plane function `F` inherits `F`'s uniqueness: if `F = G` on `{re > 0}`
  then `f = g` on the sector. This is exactly "sector uniqueness is the pullback
  of half-plane uniqueness through the change of variables", and it needs no
  branch-cut inverse identity — only the forward `MapsTo`. Sorry-free.

  This completes the Watson / Nevanlinna–Sokal uniqueness chain: the divergent
  case that the el8w regularity result (disc) could not reach is now a
  machine-checked theorem on the sector, modulo supplying the half-plane
  uniqueness `F = G` (which `watson_uniqueness_rhp_open` provides) and the
  factorizations `f = F ∘ Φ_t`, `g = G ∘ Φ_t`.

  Archimedean (ℂ).

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness sector wiring
-/

import QOU.Mathlib.BorelWatsonSectorTransport
import QOU.Mathlib.BorelWatsonShiftFull

namespace QOU.Mathlib.Borel

open Set Complex
open scoped Real

/-- **Watson uniqueness on the sector-at-0 (final wiring).** If `f` and `g` on
    the sector `{z ≠ 0 : |arg z| < π/(2t)}` are the pullbacks `f = F ∘ Φ_t`,
    `g = G ∘ Φ_t` of half-plane functions `F`, `G` that agree on `{re > 0}`,
    then `f = g` on the sector. The carrier `Φ_t(z) = (z^t)⁻¹` sends the sector
    into `{re > 0}` (`sectorTransport_mapsTo`), so each sector point's value is
    an agreed half-plane value. Supply `hFG` from `watson_uniqueness_rhp_open`
    to obtain the full sector-at-0 Watson uniqueness. -/
theorem watson_uniqueness_sector {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℂ E] {f g F G : ℂ → E} {t : ℝ} (ht : 0 < t)
    (hFG : EqOn F G {z : ℂ | 0 < z.re})
    (hf : EqOn f (fun z => F (sectorTransport t z))
      {z : ℂ | z ≠ 0 ∧ |z.arg| < Real.pi / (2 * t)})
    (hg : EqOn g (fun z => G (sectorTransport t z))
      {z : ℂ | z ≠ 0 ∧ |z.arg| < Real.pi / (2 * t)}) :
    EqOn f g {z : ℂ | z ≠ 0 ∧ |z.arg| < Real.pi / (2 * t)} := by
  intro z hz
  rw [hf hz, hg hz]
  exact hFG (sectorTransport_mapsTo ht hz)

end QOU.Mathlib.Borel
