import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic


/-!
# QOU.Archimedean.quantum_dilogarithm_volume — Nuclear energy from the quantum dilogarithm

The nuclear binding energy is the quantum dilogarithm volume of the
Markov trace, normalised by ℏ_q²:

  E_bind(p, n) = Φ_q(N(Z, N)) / ℏ_q²

where Φ_q(N(Z, N)) = Σ log|z · aᵢ + bᵢ| = log Π|V̂ᵢ|
is the natural q-deformation of the hyperbolic volume.

LaTeX label: `prop:quantum-dilogarithm-volume`

## References

- [manuscript] §5/quantum-dilogarithm-volume
- [turaev2010] https://doi.org/10.1515/9783110221848

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- The quantum Planck constant ℏ_q = (q - 1)/q. -/
noncomputable def hbar_q (q : ℝ) : ℝ := (q - 1) / q

/-- The quantum dilogarithm volume of a nuclear link:
    Φ_q(N(Z,N)) = Σᵢ log|V̂ᵢ| = log Π|V̂ᵢ|.

    This is the intensive volume, scaling as O(A) rather than
    O(e^A) for the raw Hecke weight. -/
noncomputable def quantumDilogarithmVolume (markovFactors : List ℝ) : ℝ :=
  (markovFactors.map fun v => Real.log |v|).foldl (· + ·) 0

/-- The nuclear binding energy from the quantum dilogarithm volume. -/
noncomputable def bindingEnergy (q : ℝ) (markovFactors : List ℝ) : ℝ :=
  quantumDilogarithmVolume markovFactors / (hbar_q q) ^ 2

/-- **Quantum dilogarithm volume** (Proposition):

    The nuclear binding energy equals the quantum dilogarithm volume
    of the Markov trace normalised by ℏ_q²:

      E_bind(p, n) = Φ_q(N(Z, N)) / ℏ_q²

    At q = 1, all crossings have equal weight, V̂ᵢ = 1,
    Φ_q = 0 (no binding).  At q > 1, crossing asymmetry
    creates nonzero Φ_q and the nucleus is bound. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
-- Ref: [manuscript] §5/quantum-dilogarithm-volume
-- Dropped the unused hypotheses `hq : 1 < q`, `parentFactors daughterFactors`
-- and `h_parent_len` (2026-08-22; vacuity ledger,
-- `proof-no-unused-hypothesis-rfl`).  The equation is the definitional
-- unfolding of `bindingEnergy`, which holds for every `q` and every factor
-- list; none of the dropped binders were consumed by the `rfl` proof, and
-- keeping them falsely suggested the identity depended on `q > 1` or on the
-- parent/daughter data.  The two remaining binders `q` and `markovFactors`
-- both appear in the conclusion.
theorem quantum_dilogarithm_volume
    (q : ℝ) (markovFactors : List ℝ)
    : bindingEnergy q markovFactors =
      quantumDilogarithmVolume markovFactors / (hbar_q q) ^ 2 := by
  unfold bindingEnergy
  rfl

/-- The Q-value for beta decay is the difference in quantum
    dilogarithm volumes between parent and daughter, normalised
    by ℏ_q². -/
-- Ref: [manuscript] §5/quantum-dilogarithm-volume
theorem beta_decay_qvalue
    (q : ℝ) (hq : 1 < q)
    (parentFactors daughterFactors : List ℝ)
    : bindingEnergy q parentFactors - bindingEnergy q daughterFactors =
      (quantumDilogarithmVolume parentFactors -
       quantumDilogarithmVolume daughterFactors) / (hbar_q q) ^ 2 := by
  unfold bindingEnergy
  -- Ref: [manuscript] §5/quantum-dilogarithm-volume
  -- a/c - b/c = (a - b)/c
  simp [sub_div]

/-- At q = 1 (classical limit), ℏ_q = 0, reflecting that the
    classical regime has no binding energy (degenerate configurations). -/
-- Ref: [manuscript] §5/quantum-dilogarithm-volume
theorem classical_limit_no_binding : hbar_q 1 = 0 := by
  unfold hbar_q
  norm_num

end QOU.Archimedean
