/-
# R2-core, the provable part — the Schwinger measure SHAPE is rigid; the unit is one nat per e-fold

Owner-directed R2-core attack (2026-07-19: "derive (or rule on) the
framework's proper-time measure normalization — take into account the
information-theory corpus and E = m·c_q²"), under the standing ruling that
R2 is NOT derived-proved. This file proves, sorry-free, everything in
R2-core that mathematics CAN pin — isolating the residue as a single unit
convention of the same species the corpus already uses.

* `scale_invariant_density_unique` — a proper-time density satisfying the
  scale-invariance functional equation `f(λ·s)·λ = f(s)` is `f(1)/s`: the
  Schwinger measure `c·ds/s` is the ONLY scale-invariant choice, up to the
  single scalar `c`. Corpus motivation for scale invariance: the horizon
  boundary datum is invariant under rescaling
  (`horizon-conformal-invariance`) — the loop's UV end has no preferred
  proper-time scale.
* `one_nat_per_efold` — `∫ 1/t` over one e-fold `[s, e·s]` equals 1: with
  the corpus convention `k_B = 1` (`boltzmann-constant`: entropy in nats),
  the measure's scalar `c` IS the nat-count per proper-time e-fold.
  R2-core's "unit normalization" = `c = 1` = ONE NAT PER E-FOLD — a
  time-unit convention of exactly the species the corpus already canonized
  in `discrete-planck-step` ("one full Reeb circuit = one unit of time",
  resolving a transcendental factor by unit choice).
* `efold_jacobian_two` — under the Schwinger dimension `s ~ E⁻²` (the
  `E = m·c_q²` bridge, `mass-energy-equivalence`): one ENERGY e-fold is
  TWO proper-time e-folds. This pins the arithmetic of the RIVAL reading
  of the ½ (an energy-e-fold unit convention would supply ½ via this
  Jacobian) — mutually exclusive with the program's ρ-split reading (each
  alone gives 1/(8π); both together would give 1/(16π)). The adjudication
  is OPEN and flagged; this lemma makes it well-posed.
* `unit_total_gives_eighth` — with `c = 1` (one unit total `a₀`) and the
  ½ split, the per-channel measure is `1/(8π)` — the working coefficient.

Honest scope (STRICT, per the 2026-07-19 ruling): the choice `c = 1` is a
CONVENTION-species identification, NOT proved here or anywhere — this file
proves the shape rigidity, the nat-per-e-fold reading, the rival's
arithmetic, and the assembly; the unit choice and the ½-adjudication stay
open and owner-gated. Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Archimedean.SchwingerMeasureShape

/-- **Shape rigidity.** A proper-time density satisfying the
scale-invariance functional equation is `f(1)/s`: the Schwinger measure
`c·ds/s` is the unique scale-invariant choice, up to the scalar `c = f(1)`. -/
theorem scale_invariant_density_unique (f : ℝ → ℝ)
    (h : ∀ lam s : ℝ, 0 < lam → 0 < s → f (lam * s) * lam = f s) :
    ∀ s : ℝ, 0 < s → f s = f 1 / s := by
  intro s hs
  have h1 := h s 1 hs one_pos
  rw [mul_one] at h1
  rw [eq_div_iff (ne_of_gt hs)]
  exact h1

/-- **One nat per e-fold.** In the logarithmic coordinate `ln t` — where the
Schwinger measure `dt/t` is Lebesgue (`d(ln t)`; `∫_s^{es} dt/t = ln(es) −
ln s` by the fundamental theorem) — one e-fold `[s, e·s]` has measure
exactly 1: with `k_B = 1` (nats), the measure's scalar is the nat-count per
proper-time e-fold. -/
theorem one_nat_per_efold (s : ℝ) (hs : 0 < s) :
    Real.log (Real.exp 1 * s) - Real.log s = 1 := by
  rw [Real.log_mul (Real.exp_ne_zero 1) (ne_of_gt hs), Real.log_exp]
  ring

/-- **The rival's arithmetic, pinned.** Under the Schwinger dimension
`s = E⁻²` (the `E = m·c_q²` bridge), one energy e-fold is two proper-time
e-folds: the log-measure Jacobian is exactly 2. This states the rival
reading of the ½ precisely (adjudication vs the ρ-split reading: OPEN). -/
theorem efold_jacobian_two (E lam : ℝ) (hE : 0 < E) (hlam : 0 < lam) :
    Real.log ((lam * E)⁻¹ ^ 2) - Real.log (E⁻¹ ^ 2) = -(2 * Real.log lam) := by
  rw [Real.log_pow, Real.log_pow, Real.log_inv, Real.log_inv,
    Real.log_mul (ne_of_gt hlam) (ne_of_gt hE)]
  push_cast
  ring

/-- With the unit total (`c = 1`, one per-mode unit `a₀`) and the ½ split,
the per-channel measure is `1/(8π)` — the working coefficient. -/
theorem unit_total_gives_eighth :
    (1 : ℝ) * (1 / (4 * Real.pi)) * (1 / 2) = 1 / (8 * Real.pi) := by
  have h := Real.pi_ne_zero
  field_simp
  ring

end QOU.Archimedean.SchwingerMeasureShape
