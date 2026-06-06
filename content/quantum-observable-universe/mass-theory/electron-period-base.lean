import Mathlib.Algebra.Ring.Defs

/-!
# QOU.Mass.electron_period_base — CAL-1 (m_e) IS the n=0 period

The prolonged-period recurrence is `a_{n+2} = τ·a_{n+1} − a_n`
(`prop:sl2-prolongation-recurrence`, det B = 1). Its `n=0` value is the
unprolonged Seiberg–Witten period — the **electron period** `a_D⁽ᵉ⁾`
(`prop:jet-sw-tau-decomposition`: "the n=0 term is the electron period").
Identifying that base with the leptonic scale `m_e` makes **CAL-1 the base
of the tower** rather than an external prefactor: every period is generated
from `(m_e, a_1, τ)`, so `m_e` propagates into all of them.

LaTeX label: `prop:electron-period-base`.

**Ground ring**: generic `[CommRing R]`. See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

variable {R : Type*} [CommRing R]

/-- The prolonged-period tower whose `n=0` base is the electron period `m_e`. -/
structure ElectronBaseTower (R : Type*) [CommRing R] where
  /-- CAL-1: the electron period = leptonic scale `m_e`. -/
  m_e : R
  /-- The `n=1` period. -/
  a1 : R
  /-- The recurrence trace `τ = tr B` (CAL-2 modulus). -/
  tau : R
  /-- The period sequence `a_n`. -/
  a : ℕ → R
  /-- `n=0` base IS `m_e`. -/
  base0 : a 0 = m_e
  /-- `n=1` value. -/
  base1 : a 1 = a1
  /-- The det B = 1 recurrence. -/
  recurrence : ∀ n, a (n + 2) = tau * a (n + 1) - a n

/-- **CAL-1 is the base.** The `n=0` period is `m_e`. -/
theorem electron_period_is_base (T : ElectronBaseTower R) : T.a 0 = T.m_e :=
  T.base0

/-- `m_e` appears explicitly in the `n=2` period: it is propagated by the
    recurrence, not bolted on as a prefactor. -/
theorem second_period_contains_me (T : ElectronBaseTower R) :
    T.a 2 = T.tau * T.a 1 - T.m_e := by
  have h := T.recurrence 0
  rw [T.base0] at h
  simpa using h

end QOU.Mass
