/-
  Watson-uniqueness brick 4b-ii (interior) — the composed sector→half-plane
  transport map (bean el8w tranche 5).

  Assembles the two merged carrier bricks into the single map the Watson
  argument runs on:

    * brick 4b-i (`BorelWatsonSector`): `z ↦ z^t` contracts the sector
      `{|arg z| < π/(2t)}` (opening `π/t = βπ > π`) into the open right
      half-plane, and is holomorphic on the slit plane;
    * brick 4a (`BorelWatsonTransport`): inversion `w ↦ w⁻¹` preserves the open
      right half-plane and holomorphy.

  Their composite `Φ_t(z) = (z^t)⁻¹` is the transport that carries the
  sector-at-0 (where the Gevrey-1 asymptotic lives) to the half-plane-at-∞
  (where brick 3's `watson_uniqueness_rhp` applies): `z^t` sends `0 → 0` and
  contracts the opening to `π`; inversion then sends `0 → ∞`. This file proves
  the INTERIOR of that transport, sorry-free — `Φ_t` maps the open sector into
  the open half-plane (`sectorTransport_mapsTo`) and is holomorphic there
  (`analyticAt_sectorTransport`).

  Remaining for full Watson (honestly, the single last piece): the boundary
  `DiffContOnCl` limiting argument — `watson_uniqueness_rhp` needs continuity up
  to `{re ≥ 0}`, whose two tips `0`/`∞` are the sector tips where `Φ_t` is not
  continuous; the genuine argument shrinks to `{re > ε}` and lets `ε → 0`. That
  limiting step is the sole open item of el8w tranche 5; NOT axiomatized.

  Archimedean (ℂ): complex holomorphy, `cpow`, inversion.

  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 4b-ii
-/

import QOU.Mathlib.BorelWatsonTransport
import QOU.Mathlib.BorelWatsonSector

namespace QOU.Mathlib.Borel

open Complex Set
open scoped Real

/-- The **composed sector→half-plane transport** `Φ_t(z) = (z^t)⁻¹`. -/
noncomputable def sectorTransport (t : ℝ) (z : ℂ) : ℂ := (z ^ (t : ℂ))⁻¹

/-- The transport `Φ_t` maps the open sector `{z ≠ 0 : |arg z| < π/(2t)}` into
    the open right half-plane `{re > 0}`: `z^t` lands in `{re > 0}` (brick 4b-i)
    and inversion preserves it (brick 4a). -/
theorem sectorTransport_mapsTo {t : ℝ} (ht : 0 < t) :
    MapsTo (sectorTransport t)
      {z : ℂ | z ≠ 0 ∧ |z.arg| < Real.pi / (2 * t)} {z : ℂ | 0 < z.re} :=
  fun _ hz => inv_re_pos (re_cpow_pos_of_abs_arg_lt hz.1 ht hz.2)

/-- The transport `Φ_t` is holomorphic on the open sector: `z^t` is analytic on
    the slit plane (brick 4b-i, which contains the sector) and is nonzero there
    (`‖z^t‖ = ‖z‖^t > 0`), so its inverse is analytic. -/
theorem analyticAt_sectorTransport {t : ℝ} {z : ℂ} (hz : z ∈ slitPlane) :
    AnalyticAt ℂ (sectorTransport t) z := by
  have hz0 : z ≠ 0 := slitPlane_ne_zero hz
  have hcpow : AnalyticAt ℂ (fun w : ℂ => w ^ (t : ℂ)) z :=
    analyticAt_cpow_const hz
  have hne : (z ^ (t : ℂ)) ≠ 0 := by
    rw [Complex.cpow_def_of_ne_zero hz0]; exact Complex.exp_ne_zero _
  exact hcpow.inv hne

end QOU.Mathlib.Borel
