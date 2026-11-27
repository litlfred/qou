import Mathlib.Data.Int.Basic
import Mathlib.Tactic.NormNum.Basic


/-!
# QOU.Archimedean.LeptonNumber — Lepton number as Skein smoothing count

Lepton number is the number of Skein smoothings applied to a nuclear
normal form.  Each smoothing produces exactly one lepton-antilepton
pair, so lepton number is conserved by construction.

LaTeX label: `def:lepton-number-categorical`

## References
- [leitner2026] §6/lepton-number-categorical
-/

namespace QOU.Archimedean

/-- The lepton number of a particle.

    In the QOU framework, lepton number counts Skein smoothings:
    - Charged leptons (e⁻ = σ₀σ₁σ₀, e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹): L = +1 or -1
    - Neutrinos (unknot components): L = -1 or +1
    - Hadrons (no smoothing): L = 0

    Each Skein smoothing L₀ produces one (lepton, antilepton) pair
    with total lepton number 0. -/
-- Ref: [leitner2026] §6/lepton-number-categorical
structure LeptonNumber where
  /-- The lepton number value. -/
  L : ℤ

/-- A Skein smoothing event: produces exactly one lepton pair. -/
-- Ref: [leitner2026] §6/lepton-number-categorical
structure SkeinSmoothing where
  /-- Lepton number of the charged component. -/
  charged : ℤ
  /-- Lepton number of the neutral component. -/
  neutral : ℤ
  /-- The pair sums to zero. -/
  pair_conservation : charged + neutral = 0

/-- β⁻ smoothing: electron (L=+1) + antineutrino (L=-1). -/
-- Ref: [leitner2026] §6/lepton-number-categorical
def betaMinusSmoothing : SkeinSmoothing where
  charged := 1
  neutral := -1
  pair_conservation := by norm_num

/-- β⁺ smoothing: positron (L=-1) + neutrino (L=+1). -/
-- Ref: [leitner2026] §6/lepton-number-categorical
def betaPlusSmoothing : SkeinSmoothing where
  charged := -1
  neutral := 1
  pair_conservation := by norm_num

/-- Lepton number is conserved: any sequence of k Skein smoothings
    produces total lepton number 0 in the lepton sector. -/
-- Ref: [leitner2026] §6/lepton-number-categorical
theorem lepton_number_conservation (smoothings : List SkeinSmoothing) :
    (smoothings.map (fun s => s.charged + s.neutral)).sum = 0 := by
  induction smoothings with
  | nil => simp
  | cons s rest ih =>
    simp [List.map_cons, List.sum_cons, s.pair_conservation, ih]

end QOU.Archimedean
