import Mathlib.Algebra.Order.Group.Int
import Mathlib.Algebra.Order.Ring.Abs

/-!
# QOU.FluidDynamics.ns_kummer_specialisation — Kummer-level specialisation of the obstruction

**Proposition** ([`prop:ns-kummer-specialisation`](../../../quantum-observable-universe/fluid-dynamics/ns-kummer-specialisation.md)).

*Let `κ₀ = e(ξ)` with `tr(κ₀) = χ(A)`.  Then (i) the specialisation
`κ₀|_{q=1}` is non-zero in `H²(S, G_m)/n` for every `n ∤ χ(A)`; (ii) the
set `{n : n ∤ χ(A)}` is infinite; (iii) the obstruction vanishes exactly at
the Kummer levels `n ∣ χ(A)`.*

## Formalisation notes
- **Base ring (§7c).** No ring parameter at all: the content is pure
  `ℤ`/`ℕ` divisibility arithmetic (the Euler characteristic is genuinely an
  integer).  No `ℝ`.
- **Non-degenerate conditional — with two outright proofs.** The single
  genuine hypothesis is (iii), the divisibility characterisation
  `kappa_iff_dvd` (the cohomological computation), plus the setup
  `χ(A) ≠ 0`.  From these the theorem **proves** (i) — the contrapositive
  of (iii)'s forward direction — and **proves** (ii) outright by integer
  arithmetic: any `n > |χ(A)|` fails to divide `χ(A)` (`Int.le_of_dvd`), so
  beyond every `N` there is a non-divisor.  Neither (i) nor (ii) is carried
  as a class field.
-/

namespace QOU.FluidDynamics

/-- Hypotheses for the Kummer-level specialisation (§7c: `ℤ`/`ℕ`
    arithmetic, no ring parameter).  Only the divisibility
    characterisation (iii) and the non-degeneracy of `χ(A)` are assumed;
    sub-claims (i) and (ii) are *proved* in `ns_kummer_specialisation`. -/
class NsKummerSpecialisationContext where
  /-- Euler characteristic `χ(A)` of the QOU substrate. -/
  chi_A : ℤ
  /-- **Setup:** the Euler characteristic is non-zero (e.g. `-6` for the
      Descartes universe); divisibility by every `n` would otherwise be
      vacuous. -/
  chi_A_ne_zero : chi_A ≠ 0
  /-- Predicate: the obstruction `κ₀ mod n` vanishes in `H²(S, G_m)/n`. -/
  kappa_vanishes : ℕ → Prop
  /-- **(iii) — the cohomological computation:** the obstruction vanishes
      at level `n ≥ 1` exactly when `n ∣ χ(A)` (Kummer levels). -/
  kappa_iff_dvd : ∀ n : ℕ, 1 ≤ n → (kappa_vanishes n ↔ (n : ℤ) ∣ chi_A)

/-- **Kummer specialisation** ([`prop:ns-kummer-specialisation`]).

    (i) non-divisor levels have non-vanishing obstruction — *proved* as the
    contrapositive of `kappa_iff_dvd`; (ii) non-divisor levels are
    unbounded — *proved* outright from `χ(A) ≠ 0` via `Int.le_of_dvd`
    (a divisor of `χ(A)` is at most `|χ(A)|`); (iii) restates
    `kappa_iff_dvd`. -/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/ns-kummer-specialisation.ts
theorem ns_kummer_specialisation [ctx : NsKummerSpecialisationContext] :
    (∀ n : ℕ, 1 ≤ n → ¬ ((n : ℤ) ∣ ctx.chi_A) → ¬ ctx.kappa_vanishes n) ∧
    (∀ N : ℕ, ∃ n : ℕ, N < n ∧ ¬ ((n : ℤ) ∣ ctx.chi_A)) ∧
    (∀ n : ℕ, 1 ≤ n → (ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A)) := by
  refine ⟨fun n hn hndvd hk => hndvd ((ctx.kappa_iff_dvd n hn).mp hk),
          fun N => ⟨ctx.chi_A.natAbs + N + 1, by omega, fun hdvd => ?_⟩,
          ctx.kappa_iff_dvd⟩
  have hle : (↑(ctx.chi_A.natAbs + N + 1) : ℤ) ≤ |ctx.chi_A| :=
    Int.le_of_dvd (abs_pos.mpr ctx.chi_A_ne_zero) ((dvd_abs _ _).mpr hdvd)
  rw [Int.abs_eq_natAbs] at hle
  omega

end QOU.FluidDynamics
