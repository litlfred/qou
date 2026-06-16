import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Q_β energy scale: per-Hecke-step energy and the counit closed form

Companion to `QOU/Interactions/qbeta_counit_vs_trace.lean` and the audit
`docs/audits/2026-06-16-q-beta-path-a-counit-transition-resolution.md`.

The β-decay Q-value is the framework's relation
`Q_β = ε(Δ) · 𝔈₀`, where

* `ε(Δ)` is the **Frobenius counit** of the neutron−proton normal-form
  difference (the *net reduction content* — see the companion file), and
* `𝔈₀` is the **energy of one Hecke reduction step** `σ² → hσ + 𝟙`
  (`content/.../particle-interactions/energy-scale-planck.md`):
  `𝔈₀ = m_e · c_q² · ℏ_q^E` with information-speed-squared
  `c_q² = 1/(q−1)²` and action-per-tick `ℏ_q^E = (q−1)/q`.

So `Q_β = (net reduction content) × (energy per Hecke step)` — a
**counit (transition) observable**, categorically distinct from the
Markov-trace (static loop / partition-function) mass. These lemmas pin the
two algebraic facts the resolution rests on:

1. `𝔈₀` factorises to `m_e / (q(q−1))`;
2. `ε(Δ) · 𝔈₀` is the closed form `m_e (q+1)(q²−2q−1) / (2q³)`.

`ℏ_q^E = (q−1)/q` (energy-scale action-per-tick) is **distinct** from the
Hecke parameter `h = q − q⁻¹`; they are kept separate here. All statements
hold over an arbitrary field (no archimedean structure; CLAUDE.md §7c).
-/

namespace QOU.Interactions.QBetaEnergyScale

variable {R : Type*} [Field R]

/-- Information speed squared in `q`-Planck units, `c_q² = 1/(q−1)²`. -/
def cqSq (q : R) : R := 1 / (q - 1) ^ 2

/-- Action per Planck tick (energy-scale convention), `ℏ_q^E = (q−1)/q`.
    Distinct from the Hecke parameter `h = q − q⁻¹`. -/
def hbarE (q : R) : R := (q - 1) / q

/-- Energy of one Hecke reduction step `σ² → hσ + 𝟙`, in units of `m_e`:
    `𝔈₀ = m_e · c_q² · ℏ_q^E`. -/
def E0 (me q : R) : R := me * cqSq q * hbarE q

/-- **`𝔈₀` factorisation.** The per-Hecke-step energy collapses to
    `m_e / (q(q−1))` — the form derived from CAL-1 (`m_e`) + CAL-2 (`q₀`). -/
theorem E0_eq (me q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    E0 me q = me / (q * (q - 1)) := by
  unfold E0 cqSq hbarE; field_simp

/-- Frobenius counit of the `N=0` neutron−proton NF difference, in `q`
    (via `h = q − q⁻¹`): `ε(Δ) = (q²−1)(q²−2q−1) / (2q²)`. Matches
    `QBetaCounitTrace.epsNP_q`. -/
def epsNPq (q : R) : R := (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2)

/-- **Q_β closed form.** The β-decay Q-value as *(net reduction content)*
    `×` *(per-Hecke-step energy)*:
    `Q_β = ε(Δ) · 𝔈₀ = m_e (q+1)(q²−2q−1) / (2q³)`. -/
theorem Qbeta_closed (me q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (htwo : (2 : R) ≠ 0) :
    epsNPq q * E0 me q = me * (q + 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 3) := by
  unfold epsNPq E0 cqSq hbarE; field_simp; ring

end QOU.Interactions.QBetaEnergyScale
