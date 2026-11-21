import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.CharZero.Defs
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.LinearCombination

/-!
# Computational-time identification of the Schwinger variable

Content block: `conj:schwinger-measure-computational-time`
(predicted-spectra). Formal record of the §5 lead of
`docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md`.

THE IDENTIFICATION (open): the binding sector's (q-)Borel variable and the
one-loop Schwinger proper-time variable are the same substrate object —
under owner premise P2 ("proper time is computational time"), both are the
substrate's computation-step count. Its quantitative shadow is the single
class field below: the keystone-forced binding normalizer `N(n)` is the
`n`-th moment of the loop's proper-time measure `ς·ds/s` against `e^{-s}`,
whose classical evaluation is `ς·(n−1)!` (Γ-integral, recorded exactly in
the exploration probe, block B5). The class encodes that moment identity
algebraically; the analytic integral representation lives in the narrative
and the probe, keeping this file import-light and archimedean-free.

Honest tiering:

* **Primary conjecture (§3b-tax):** `BorelProperTimeIdentification` is
  content-bearing (one parameter-quantified equation field — not `True`,
  not empty) and has NO instance: the honest open state. Do not fabricate
  an instance.
* **Conditional theorem (proved, sorry-free):** given the class and the
  keystone-proved normalizer identity `n·N(n) = n!`
  (`QOU.Mass.KeystoneBridgeC1Binding`, sorry-free on `main`), the measure
  unit is forced: `ς = 1` (`unit_eq_one_of_keystone_normalizer`). This is
  the honest reduced form of the exploration's consequence (i).
* **Distinguisher (proved, sorry-free, unconditional):** a half unit
  breaks the moment/normalizer match — `c·m! ≠ m!` for any `c` with
  `2c = 1`, in characteristic zero (`half_unit_breaks_normalizer`).

Base ring (§7c): generic `{K : Type*} [CommRing K] [CharZero K]` — the
statements use only *ring* operations and factorial casts; no division,
no `Real.*`, no ordering. `CharZero` is exactly what makes `m! ≠ 0` in
`K`. The one place a half appeared (`1/2`) is carried by the R[h]
pattern instead: the distinguisher quantifies over an element `c` pinned
by the multiplicative relation `2·c = 1`, which over a characteristic-zero
field is exactly `c = 1/2`, and over `ℤ[1/2]`-algebras is available
without a field. The archimedean shell (measure shape rigidity,
nat-per-e-fold reading) lives on the `ℝ`-side of the wall in
`QOU.Archimedean.SchwingerMeasureShape`.

Complementary sibling record (same tranche): the library file
`QOU.Archimedean.BorelProperTimeMoment` attacks the same identification
analytically over `ℝ` (moment integral `∫ sⁿ e^{−s} ds/s = (n−1)!`,
Carleman determinacy hypothesis, bar-covariance falsifier) with its own
§3b-tax class `BindingKernelSchwingerRepresentation`. This content-block
sibling carries the fibre-algebraic (generic-field) face of the same open
identification; the two classes name the same open premise from the two
sides of the wall and neither has an instance.

-- @conjecture: primary
-/

namespace QOU.Archimedean.SchwingerMeasureComputationalTime

/-- **Primary conjecture (open — no instance).** The binding Borel variable
is the loop proper time: the keystone-forced binding normalizer `N` is the
moment sequence of the Schwinger proper-time measure with unit `ς`. The
quantitative content is the single field `moment_eq_normalizer`,
`N (m + 1) = ς · m!` — the algebraic shadow of the integral representation
`N(n) = ∫₀^∞ sⁿ e^{−s} ς ds/s = ς·(n−1)!` at `n = m + 1` (index shifted to
keep ℕ-subtraction out). An unproved primary conjecture is honestly
represented by this content-bearing class with no instance. -/
-- Ref: [leitner2026] docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md §5
class BorelProperTimeIdentification {K : Type*} [CommRing K] [CharZero K]
    (ς : K) (N : ℕ → K) : Prop where
  /-- The normalizer is the `ς`-unit proper-time moment: `N (m+1) = ς · m!`. -/
  moment_eq_normalizer : ∀ m : ℕ, N (m + 1) = ς * (m.factorial : K)

/-- **Conditional unit forcing (proved, sorry-free).** GIVEN the
identification and the keystone-proved normalizer identity
`(m+1) · N(m+1) = (m+1)!` — the `n·N(n) = n!` bridge of
`QOU.Mass.KeystoneBridgeC1Binding`, taken here as the named hypothesis
`hkey` per the `_of_` discipline — the Schwinger measure unit is forced:
`ς = 1`. The `m = 0` instance already decides it: `N 1 = 1! = 1` from the
keystone leg and `N 1 = ς · 0! = ς` from the identification. -/
theorem unit_eq_one_of_keystone_normalizer {K : Type*} [CommRing K] [CharZero K]
    (ς : K) (N : ℕ → K) [inst : BorelProperTimeIdentification ς N]
    (hkey : ∀ m : ℕ, ((m + 1 : ℕ) : K) * N (m + 1) = ((m + 1).factorial : K)) :
    ς = 1 := by
  have h1 := hkey 0
  have h2 := inst.moment_eq_normalizer 0
  simp [Nat.factorial] at h1 h2
  rw [h2] at h1
  exact h1

/-- **Exact distinguisher (proved, unconditional).** A half unit breaks the
moment/normalizer match at every order: `c·m! ≠ m!` for any `c` satisfying
`2·c = 1`, over any characteristic-zero commutative ring. This records, at
the fibre-algebra level, the exploration's `n!/2 ≠ n!` distinguisher between
the ρ-split reading (`ς = 1`, the ½ in the channel split) and the
energy-Jacobian reading (`ς = 1/2` on the proper-time side).

§7c: the half is carried by its defining relation `hhalf : 2·c = 1` rather
than written as the field division `1/2`, so no `Field`/`field_simp` is
needed. Over a characteristic-zero field the unique such `c` is `1/2`, so
this specialises back to the previous statement. -/
theorem half_unit_breaks_normalizer {K : Type*} [CommRing K] [CharZero K]
    (m : ℕ) (c : K) (hhalf : (2 : K) * c = 1) :
    c * (m.factorial : K) ≠ (m.factorial : K) := by
  have hfac : (m.factorial : K) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero m
  intro hc
  exact hfac (by linear_combination (-2 : K) * hc + (m.factorial : K) * hhalf)

end QOU.Archimedean.SchwingerMeasureComputationalTime
