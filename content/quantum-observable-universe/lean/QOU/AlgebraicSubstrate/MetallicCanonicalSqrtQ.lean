import Mathlib.Tactic

/-!
# QOU.AlgebraicSubstrate.MetallicCanonicalSqrtQ

Sorry-free proofs of the `q = 4` coincidences of the CANONICAL
(Wenzl-JM / Ocneanu) Markov-trace convention on `H₄(q)`, surfaced by the
exact-Gram S(4) probe (PR #2081) and derived in closed form by
`metallic_q4_canonical_coincidence_proof.py` (exact sympy over ℚ(s),
`s = √q`; generator convention locked to `pyhecke_native` by a 360-case
verification, worst relative error 1.8e-15).

## The closed forms (machine-derived, sympy remainder 0)

With `z = s/(s² + 1)` the canonical Markov parameter and costs
`t(w) = tr_M(T_w)` on `H₄(q)`:

  - `t(γ) = 1`,  `t(σ₁) = z`
  - `t(σ₁σ₂σ₁) = (s² + s − 1)/(s² + 1)`
  - `t(σ₁σ₂σ₁σ₃) = s(s² + s − 1)/(s² + 1)²  = z · t(σ₁σ₂σ₁)`

## Theorems proved (all sorry-free)

  - `diff_gamma_s121`: `t(γ) − t(σ₁σ₂σ₁) = (2 − s)/(s² + 1)`
  - `diff_s1_s1213`: `t(σ₁) − t(σ₁σ₂σ₁σ₃) = −s(s − 2)/(s² + 1)²`
  - `q4_coincidence_one`: `t(γ) = t(σ₁σ₂σ₁) ↔ s = 2`  (s > 0)
  - `q4_coincidence_two`: `t(σ₁) = t(σ₁σ₂σ₁σ₃) ↔ s = 2`  (s > 0)
  - `markov_factorization`: the second coincidence is the first times z
    (Markov stability) — ONE primitive identity
  - `markovZ_at_two`: `z = 2/5 ∈ ℚ` at the coincidence point
  - `q4_not_metallic`: no integer n has `4² − 4n − 1 = 0` — the
    coincidence point `q = s² = 4` is NOT a metallic ratio
  - `markovZ_odd`, `diff_gamma_s121_galois`: the Galois action
    `s ↦ −s` of `ℚ(s)/ℚ(q)` is odd on z and pairs the locus `s = 2`
    with `s = −2` — the same `q = 4`

Together: the canonical convention's coincidence arithmetic lives in
`√q` (the rationality field of its Markov normalization), while the
plancherel convention's lives in `q − q⁻¹` (the metallic ladder —
see `QOU.AlgebraicSubstrate.MetallicSilverFamily`).

-- Ref: [manuscript] rem:sdp-degeneracy-at-metallic-coincidence
-- Ref: [audit] docs/audits/2026-06-09-metallic-qrho-calibration-nova-cascade.md
-- Ref: [witness] folio-assistant/computations/metallic-q4-canonical-coincidence-proof.witness.json
-/

namespace QOU.AlgebraicSubstrate.MetallicCanonicalSqrtQ

/-- The canonical (Wenzl-JM) Markov parameter `z = s/(s² + 1)`, `s = √q`. -/
noncomputable def markovZ (s : ℝ) : ℝ := s / (s ^ 2 + 1)

/-- `tr_M(T_{σ₁}) = z` (closed form). -/
noncomputable def tSigma1 (s : ℝ) : ℝ := s / (s ^ 2 + 1)

/-- `tr_M(T_{σ₁σ₂σ₁}) = (s² + s − 1)/(s² + 1)` (closed form). -/
noncomputable def tS121 (s : ℝ) : ℝ := (s ^ 2 + s - 1) / (s ^ 2 + 1)

/-- `tr_M(T_{σ₁σ₂σ₁σ₃}) = s(s² + s − 1)/(s² + 1)²` (closed form). -/
noncomputable def tS1213 (s : ℝ) : ℝ :=
  s * (s ^ 2 + s - 1) / (s ^ 2 + 1) ^ 2

lemma den_pos (s : ℝ) : (0 : ℝ) < s ^ 2 + 1 := by positivity

lemma den_ne (s : ℝ) : (s ^ 2 + 1 : ℝ) ≠ 0 := ne_of_gt (den_pos s)

/-- `t(γ) − t(σ₁σ₂σ₁) = (2 − s)/(s² + 1)`: the machine-derived numerator
    is LINEAR in s with root s = 2. -/
theorem diff_gamma_s121 (s : ℝ) :
    1 - tS121 s = (2 - s) / (s ^ 2 + 1) := by
  unfold tS121
  field_simp
  ring

/-- `t(σ₁) − t(σ₁σ₂σ₁σ₃) = −s(s − 2)/(s² + 1)²`. -/
theorem diff_s1_s1213 (s : ℝ) :
    tSigma1 s - tS1213 s = -(s * (s - 2)) / (s ^ 2 + 1) ^ 2 := by
  unfold tSigma1 tS1213
  field_simp
  ring

/-- Markov stability: `t(σ₁σ₂σ₁σ₃) = z · t(σ₁σ₂σ₁)` — appending the
    disjoint generator σ₃ multiplies the trace by z, so the two q = 4
    coincidences are ONE primitive identity. -/
theorem markov_factorization (s : ℝ) :
    tS1213 s = markovZ s * tS121 s := by
  unfold tS1213 markovZ tS121
  field_simp

/-- First coincidence: `t(γ) = t(σ₁σ₂σ₁) ↔ s = 2` for s > 0. -/
theorem q4_coincidence_one {s : ℝ} (hs : 0 < s) :
    (1 : ℝ) = tS121 s ↔ s = 2 := by
  unfold tS121
  rw [eq_div_iff (den_ne s)]
  constructor
  · intro h; nlinarith [h]
  · intro h; subst h; ring

/-- Second coincidence: `t(σ₁) = t(σ₁σ₂σ₁σ₃) ↔ s = 2` for s > 0.
    Proved by reduction to the first via Markov stability. -/
theorem q4_coincidence_two {s : ℝ} (hs : 0 < s) :
    tSigma1 s = tS1213 s ↔ s = 2 := by
  have hz : markovZ s ≠ 0 := by
    unfold markovZ
    exact div_ne_zero (ne_of_gt hs) (den_ne s)
  have hs1 : tSigma1 s = markovZ s * 1 := by
    unfold tSigma1 markovZ; ring
  rw [hs1, markov_factorization]
  constructor
  · intro h
    exact (q4_coincidence_one hs).mp (mul_left_cancel₀ hz h)
  · intro h
    rw [← (q4_coincidence_one hs).mpr h]

/-- At the coincidence point the Markov parameter is RATIONAL:
    `z(2) = 2/5`.  This is the structural signature — the canonical
    ladder lives at rational points of the z-parameterization. -/
theorem markovZ_at_two : markovZ 2 = 2 / 5 := by
  unfold markovZ; norm_num

/-- `q = s² = 4` is NOT a metallic ratio: the metallic minimal
    polynomial `q² − nq − 1` does not vanish at 4 for any integer n
    (it would force `4n = 15`). -/
theorem q4_not_metallic (n : ℤ) :
    (4 : ℝ) ^ 2 - (n : ℝ) * 4 - 1 ≠ 0 := by
  intro h
  have h4 : (n : ℝ) * 4 = 15 := by linarith
  have hz : (n * 4 : ℤ) = 15 := by exact_mod_cast h4
  omega

/-- The Galois action `s ↦ −s` of `ℚ(s)/ℚ(q)` is ODD on the Markov
    parameter: `z(−s) = −z(s)`.  This is exactly how the canonical
    convention escapes `ℚ(q)`. -/
theorem markovZ_odd (s : ℝ) : markovZ (-s) = -markovZ s := by
  unfold markovZ
  rw [neg_sq]
  ring

/-- The Galois-partner locus: at `−s` the first difference has
    numerator `(2 + s)`, pairing the root `s = 2` with `s = −2` —
    both map to the SAME `q = s² = 4`. -/
theorem diff_gamma_s121_galois (s : ℝ) :
    1 - tS121 (-s) = (2 + s) / (s ^ 2 + 1) := by
  unfold tS121
  simp only [neg_sq]
  field_simp
  ring

end QOU.AlgebraicSubstrate.MetallicCanonicalSqrtQ
