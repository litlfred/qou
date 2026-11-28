import QOU.Transcendental.Nuclear.SpectatorEnergyMap
import QOU.Nuclear.WeightSpaceNucleon

/-!
# What the decay vertex must add (prereg Addendum 16)

Units `m_e = 1` (CAL-1). `E₀ = e0 q = 1/(q(q − 1))`. Energies under premise (G) and route T:
`E = −E₀ log(q^m · T)`.

* `lepton_cancels_cell` (placement C, premise L: ν has weight `+1`, e⁻ has `−1`, each a single
  strand with trace `1`): `(E_n − E_p) + (E_ν − E_e) = 0`. The vertex must supply all of `Q_β`.
* `qbeta_B_lt` (placement B: `E(e⁻) = 1`, `E(ν̄) ≥ 0`): `cell − 1 − E(ν̄) < 2/q − 1 < 1` for `q > 1`.
* `vertex_needed_B`: for any `Q ≥ 1`, `Q − (cell − 1 − E(ν̄)) > Q − (2/q − 1) > 0`.

No measured value appears here.
-/

namespace QOU.QBeta.BetaVertexBudget

open QOU.QBeta.SpectatorEnergyMap QOU.QBeta.WeightSpaceNucleon

/-- Placement C: the lepton strand's weight step cancels the nucleon cell. -/
theorem lepton_cancels_cell (q T : ℝ) (hq : 0 < q) (hT : 0 < T) :
    (energy (e0 q) q T (-1) - energy (e0 q) q T 1)
      + (energy (e0 q) q 1 1 - energy (e0 q) q 1 (-1)) = 0 := by
  have h1 := np_eq_cell (e0 q) q T hq hT
  have h2 := np_eq_cell (e0 q) q 1 hq one_pos
  linarith

/-- Placement B without a vertex term: `Q_β < 2/q − 1 < 1` for every `q > 1`. -/
theorem qbeta_B_lt (q Eν : ℝ) (hq : 1 < q) (hν : 0 ≤ Eν) :
    2 * e0 q * Real.log q - 1 - Eν < 2 / q - 1 ∧ 2 / q - 1 < 1 := by
  have hb := (log_cell_bounds q hq).2
  have hq0 : 0 < q := by linarith
  refine ⟨by linarith, ?_⟩
  have : 2 / q < 2 := by rw [div_lt_iff₀ hq0]; linarith
  linarith

/-- The vertex term needed under B for any comparison value `Q ≥ 1`. -/
theorem vertex_needed_B (q Eν Q : ℝ) (hq : 1 < q) (hν : 0 ≤ Eν) (hQ : 1 ≤ Q) :
    Q - (2 / q - 1) < Q - (2 * e0 q * Real.log q - 1 - Eν) ∧ 0 < Q - (2 / q - 1) := by
  obtain ⟨h1, h2⟩ := qbeta_B_lt q Eν hq hν
  exact ⟨by linarith, by linarith⟩

end QOU.QBeta.BetaVertexBudget
