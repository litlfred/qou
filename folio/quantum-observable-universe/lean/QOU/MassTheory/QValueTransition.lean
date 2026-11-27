import Mathlib.Tactic

/-!
# QOU.Archimedean.QValueTransition — the mass-difference FORM of the `Q`-value

Carrier for the **mass-difference form** stated in content block
[`quantum-observable-universe/predicted-spectra/q-value-transition.ts`](quantum-observable-universe/predicted-spectra/q-value-transition.ts).

This is NOT the block's primary definition. The primary definition —
the `𝒬_q`-value as a categorical **action** difference,
`𝒬_q = 𝔖_q(parent) − 𝔖_q(daughter) − 𝔖_q(e) − 𝔖_q(ν̄)` — is
`QOU.Archimedean.QqValue.value` in the block's sibling file
`predicted-spectra/q-value-transition.lean`, and the block's `lean.ref`
names that declaration.

What this file carries is the archimedean realisation in which the
transition is evaluated as a neutral-atomic mass difference,
`Q = M(Z,N) − M(Z+1,N−1)` with
`M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)`, together with the one
arithmetic fact about it (`q_mass_difference`): expanding the masses
leaves the `n − p − e` gap plus the change in binding. The identification
of this form with the action difference is a realisation step, not a
theorem of this file; nothing here relates `Q` to `QqValue.value`.
(§7c: archimedean over `ℝ` — physical masses; counts carried as `ℤ`.)
-/

namespace QOU.Archimedean

/-- Data for the mass-difference form of a `β⁻`-decay `Q`-value.

    A carrier for the realised form, not the primary definition (see the
    module header): the nucleon/electron masses, the binding energy
    `B(Z,N)`, the neutral-atomic mass `M(Z,N)` pinned to its formula, and the
    `Q`-value pinned to the parent–daughter mass difference. -/
structure QValueTransition where
  /-- Proton mass `m_p`. -/
  m_p : ℝ
  /-- Neutron mass `m_n`. -/
  m_n : ℝ
  /-- Electron mass `m_e`. -/
  m_e : ℝ
  /-- Binding energy `B(Z,N)`. -/
  B : ℤ → ℤ → ℝ
  /-- Neutral-atomic mass `M(Z,N)`. -/
  M : ℤ → ℤ → ℝ
  /-- `M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)`. -/
  M_def : ∀ Z N : ℤ,
    M Z N = (Z : ℝ) * m_p + (N : ℝ) * m_n + (Z : ℝ) * m_e - B Z N
  /-- `Q`-value of `𝒩(Z,N) → 𝒩(Z+1,N−1) + e⁻ + ν̄`. -/
  Q : ℤ → ℤ → ℝ
  /-- `Q = M(Z,N) − M(Z+1,N−1)`. -/
  Q_def : ∀ Z N : ℤ, Q Z N = M Z N - M (Z + 1) (N - 1)

-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/q-value-transition.ts

/-- Expanding the masses, the `Q`-value is the neutron–proton–electron mass
    gap plus the change in binding energy:
    `Q = m_n − m_p − m_e + (B(Z+1,N−1) − B(Z,N))`. -/
theorem q_mass_difference (T : QValueTransition) (Z N : ℤ) :
    T.Q Z N = T.m_n - T.m_p - T.m_e + (T.B (Z + 1) (N - 1) - T.B Z N) := by
  rw [T.Q_def, T.M_def, T.M_def]
  push_cast
  ring

end QOU.Archimedean
