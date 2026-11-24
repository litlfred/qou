/-
  Per-neutron ladder algebra — the degenerate (c = 2) recurrence layer
  behind the 2026-07-02 holomorphic-tie probe (bean 2o66; probe witness
  `computations/binding-qbeta-recurrence-tie-probe.witness.json`).

  The probe measured that the free/atom Markov-trace ratio over neutron
  chains (Z ∈ {1,2}, N = 1..4) is EXACTLY geometric per added neutron —
  Z-independent factor e^ℓ, ℓ(q₀) = 1.2369781644668708…, ℓ(q₀⁻¹) =
  0.34477368001157065… — so its log-ladder is arithmetic and satisfies
  the three-term recurrence with the DEGENERATE bar-even multiplier
  c = 2 (the s = 0 boundary of the Chebyshev family c = q^s + q^{-s}).

  This file proves the algebra layer over a generic commutative ring
  (§7c — no ℝ, no log): a geometric ladder satisfies the multiplicative
  degenerate recurrence (vanishing multiplicative Casoratian), an
  arithmetic ladder satisfies the additive degenerate recurrence with
  c = 2, the multiplier 2 is σ-fixed for EVERY ring hom σ (so
  `QOU.Knot.SelfDuality.recurrence_descent` applies with c = 2, tying
  both parity ladders — but vacuously: any arithmetic ladder does this),
  and both parity combinations of two arithmetic ladders are arithmetic.

  What is NOT proved here (stays compute-witnessed, bean 2o66 open leg):
  that the transfer-matrix atom word IS per-neutron multiplicative —
  that identification lives in the word-builder construction
  (`tr_m_atom_via_transfer.py`) and enters below only as a hypothesis.
-/
import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Algebra.Group.Basic

namespace QOU.Knot.PerNeutronLadder

variable {R : Type*} [CommRing R]

/-- **Geometric ladder ⇒ closed form.** If each neutron multiplies the
    trace ratio by a fixed `ρ`, the ladder is `ρ^n`-geometric. -/
theorem geometric_closed_form (T : ℕ → R) (ρ : R)
    (hT : ∀ n, T (n + 1) = ρ * T n) (n : ℕ) :
    T n = ρ ^ n * T 0 := by
  induction n with
  | zero => simp
  | succ k ih => rw [hT k, ih, pow_succ', mul_assoc]

/-- **Geometric ⇒ vanishing multiplicative Casoratian.** The
    multiplicative avatar of the degenerate `c = 2` recurrence — the
    probe's exact finding about the free/atom trace ratio, stated
    without any `log` (generic `R`, §7c). -/
theorem geometric_multiplicative_casoratian (T : ℕ → R) (ρ : R)
    (hT : ∀ n, T (n + 1) = ρ * T n) (n : ℕ) :
    T (n + 2) * T n = T (n + 1) * T (n + 1) := by
  have h1 := hT n
  have h2 := hT (n + 1)
  rw [h2, h1]
  simp only [mul_left_comm, mul_comm]

/-- **Arithmetic ladder ⇒ degenerate three-term recurrence.** A
    constant-step ladder (the log-leg of a geometric one) satisfies
    `V₊ = c·Vₖ − V₋` with the degenerate multiplier `c = 2`. -/
theorem arithmetic_degenerate_recurrence (L : ℕ → R) (ℓ : R)
    (hL : ∀ n, L (n + 1) = L n + ℓ) (n : ℕ) :
    L (n + 2) = 2 * L (n + 1) - L n := by
  have h1 := hL n
  have h2 := hL (n + 1)
  rw [h2, h1, two_mul, eq_sub_iff_add_eq]
  simp only [add_left_comm, add_comm]

/-- **The degenerate multiplier is σ-fixed for every ring hom.** So the
    hypothesis of `QOU.Knot.SelfDuality.recurrence_descent` holds with
    `c = 2` for ANY bar-involution — which is exactly why the probe's
    parity tie at `c = 2` is real but carries no non-trivial
    Askey–Wilson content: every arithmetic ladder ties its parities. -/
theorem two_sigma_fixed (σ : R →+* R) : σ (2 : R) = 2 := by
  rw [← one_add_one_eq_two, map_add, map_one]

/-- **Parity descent of arithmetic ladders.** If the `q₀`-leg and the
    `q₀⁻¹`-leg are both arithmetic (steps `ℓ`, `ℓ'`), the bar-even
    combination `L + L'` and the bar-odd combination `L − L'` are
    arithmetic with steps `ℓ + ℓ'` and `ℓ − ℓ'` — hence each satisfies
    the same degenerate `c = 2` recurrence. The archimedean instance is
    the probe's per-neutron parity quanta `E₀·ℓ_even`, `E₀·ℓ_odd`. -/
theorem parity_ladders_arithmetic (L L' : ℕ → R) (ℓ ℓ' : R)
    (hL : ∀ n, L (n + 1) = L n + ℓ) (hL' : ∀ n, L' (n + 1) = L' n + ℓ') :
    (∀ n, L (n + 1) + L' (n + 1) = (L n + L' n) + (ℓ + ℓ')) ∧
    (∀ n, L (n + 1) - L' (n + 1) = (L n - L' n) + (ℓ - ℓ')) := by
  refine ⟨fun n => ?_, fun n => ?_⟩
  · rw [hL n, hL' n]
    simp only [add_left_comm, add_comm]
  · rw [hL n, hL' n, sub_add_sub_comm]

end QOU.Knot.PerNeutronLadder
