import Mathlib.Algebra.Ring.Units
import Mathlib.Algebra.Group.Invertible.Basic
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
Hecke parameter `h = q − q⁻¹`; they are kept separate here.

## Base ring (AGENTS.md §7c)

Generic `[CommRing R]` — **not** a field.  Nothing here is archimedean (no
ordering, no `Real.*`), and every division the narrative writes is a division
by a quantity the old statements already had to assume nonzero.  Each is
therefore carried as an invertible datum instead, which is the exact
`CommRing` analogue of that side condition:

| old field hypothesis | §7c replacement |
|---|---|
| `q ≠ 0` | `q : Rˣ`, so `1/q` is the ring element `↑q⁻¹` |
| `q - 1 ≠ 0` | `d : Rˣ` with `hd : ↑d = q − 1` |
| `(2 : R) ≠ 0` | `[Invertible (2 : R)]`, so `1/2` is `⅟(2 : R)` |

Over a field "nonzero" and "invertible" coincide, so no generality is lost
and the old statements are recovered with `Units.mk0` / `invertibleOfNonzero`.
-/

namespace QOU.Interactions.QBetaEnergyScale

variable {R : Type*} [CommRing R]

/-- Information speed squared in `q`-Planck units, `c_q² = 1/(q−1)²`, with
    the temporal weight `q − 1` carried as the unit `d : Rˣ`. -/
def cqSq (d : Rˣ) : R := (↑d⁻¹ : R) ^ 2

/-- Action per Planck tick (energy-scale convention), `ℏ_q^E = (q−1)/q`.
    Distinct from the Hecke parameter `h = q − q⁻¹`. -/
def hbarE (q d : Rˣ) : R := (d : R) * (↑q⁻¹ : R)

/-- Energy of one Hecke reduction step `σ² → hσ + 𝟙`, in units of `m_e`:
    `𝔈₀ = m_e · c_q² · ℏ_q^E`. -/
def E0 (me : R) (q d : Rˣ) : R := me * cqSq d * hbarE q d

/-- **`𝔈₀` factorisation.** The per-Hecke-step energy collapses to
    `m_e / (q(q−1))` — here in its division-free form `m_e · q⁻¹ · d⁻¹`,
    the form derived from CAL-1 (`m_e`) + CAL-2 (`q₀`). -/
theorem E0_eq (me : R) (q d : Rˣ) :
    E0 me q d = me * (↑q⁻¹ : R) * (↑d⁻¹ : R) := by
  have hdi : (↑d⁻¹ : R) * (d : R) = 1 := Units.inv_mul d
  calc E0 me q d
      = me * (↑d⁻¹ : R) ^ 2 * ((d : R) * (↑q⁻¹ : R)) := rfl
    _ = me * (↑q⁻¹ : R) * (↑d⁻¹ : R) * ((↑d⁻¹ : R) * (d : R)) := by ring
    _ = me * (↑q⁻¹ : R) * (↑d⁻¹ : R) := by rw [hdi, mul_one]

variable [Invertible (2 : R)]

/-- Frobenius counit of the `N=0` neutron−proton NF difference, in `q`
    (via `h = q − q⁻¹`): `ε(Δ) = (q²−1)(q²−2q−1) / (2q²)`. Matches
    `QBetaCounitTrace.epsNP_q`. -/
def epsNPq (q : Rˣ) : R :=
  ((q : R) ^ 2 - 1) * ((q : R) ^ 2 - 2 * (q : R) - 1) * ⅟(2 : R) * (↑q⁻¹ : R) ^ 2

/-- **Q_β closed form.** The β-decay Q-value as *(net reduction content)*
    `×` *(per-Hecke-step energy)*:
    `Q_β = ε(Δ) · 𝔈₀ = m_e (q+1)(q²−2q−1) / (2q³)`. -/
theorem Qbeta_closed (me : R) (q d : Rˣ) (hd : (d : R) = (q : R) - 1) :
    epsNPq q * E0 me q d
      = me * ((q : R) + 1) * ((q : R) ^ 2 - 2 * (q : R) - 1) * ⅟(2 : R)
          * (↑q⁻¹ : R) ^ 3 := by
  have hdi : (↑d⁻¹ : R) * (d : R) = 1 := Units.inv_mul d
  have hq2 : (q : R) ^ 2 - 1 = (d : R) * ((q : R) + 1) := by rw [hd]; ring
  calc epsNPq q * E0 me q d
      = ((q : R) ^ 2 - 1) * ((q : R) ^ 2 - 2 * (q : R) - 1) * ⅟(2 : R)
            * (↑q⁻¹ : R) ^ 2
          * (me * (↑d⁻¹ : R) ^ 2 * ((d : R) * (↑q⁻¹ : R))) := rfl
    _ = (d : R) * ((q : R) + 1) * ((q : R) ^ 2 - 2 * (q : R) - 1) * ⅟(2 : R)
            * (↑q⁻¹ : R) ^ 2
          * (me * (↑d⁻¹ : R) ^ 2 * ((d : R) * (↑q⁻¹ : R))) := by rw [hq2]
    _ = me * ((q : R) + 1) * ((q : R) ^ 2 - 2 * (q : R) - 1) * ⅟(2 : R)
            * (↑q⁻¹ : R) ^ 3
          * (((↑d⁻¹ : R) * (d : R)) * ((↑d⁻¹ : R) * (d : R))) := by ring
    _ = me * ((q : R) + 1) * ((q : R) ^ 2 - 2 * (q : R) - 1) * ⅟(2 : R)
            * (↑q⁻¹ : R) ^ 3 := by rw [hdi, mul_one, mul_one]

end QOU.Interactions.QBetaEnergyScale
