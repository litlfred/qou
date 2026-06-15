/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Lommel ORDER recurrence and the "tower from two seeds"

This is the *order* three-term recurrence (in the order index `ν`), distinct
from the *argument* q-difference recurrence formalised in
`QOU/QBeta/QBesselContiguityRecurrence.lean` (which is q-holonomic / k-varying
in the power-series index). The Hahn–Exton q-Bessel functions of the FIRST and
SECOND kind both satisfy the same order recurrence

    J_{ν+1}(x;q) = b_ν(x;q) · J_ν(x;q) − J_{ν-1}(x;q),                 (◇)

and the q-Lommel polynomials `h_{n,ν}(x;q)` are obtained by iterating (◇) from
two seeds (`notation-register-table4-data.md`: "the tower from two seeds"). The
coefficient `b_ν(x;q)` is a DERIVED closed form (the q-analogue of the classical
Lommel `b_ν = 2ν/x`; Ismail 1982, Koelink–Swarttouw), NOT a fitted parameter.

**Why this matters for the binding `Δ_λ` ladder.** The decisive structural fact
is `two_seed_unique` below: a three-term recurrence with a *given* coefficient
sequence `b` is determined by its first two terms. So IF the canonical binding
ladder `Δ_λ` satisfies (◇) with the derived `b_ν`, then two seeds (e.g. D and T)
PREDICT every heavier `Δ_λ` — with no fit (the gate forbids fitting `b_ν`, not
testing a derived one). `Δ_predict_succ` packages that one-step prediction; the
empirical derive-or-refute against ⁴He is the compute companion
(`folio-assistant/computations/qbeta/qlommel_delta_lambda_two_seed_test.py`).

Generic base ring `[Field K]` (`q`, `x` are formal fibre parameters; CLAUDE.md
§7c). Sorry-free.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta

variable {K : Type*} [Field K]

/-- The order three-term recurrence `a (n+2) = b n · a (n+1) − a n`
(the q-Lommel / q-Bessel order contiguity (◇), as a relation on any sequence
`a : ℕ → K` with coefficient sequence `b : ℕ → K`). -/
def IsOrderThreeTermRec (b a : ℕ → K) : Prop :=
  ∀ n, a (n + 2) = b n * a (n + 1) - a n

/-- **One-step prediction.** Under the recurrence, the next term is fixed by the
two previous terms and the (derived) coefficient — no free parameter. -/
theorem Δ_predict_succ {b a : ℕ → K} (ha : IsOrderThreeTermRec b a) (n : ℕ) :
    a (n + 2) = b n * a (n + 1) - a n := ha n

/-- **Tower from two seeds.** Two solutions of the *same* order recurrence (same
coefficient sequence `b`) that agree on the first two terms agree everywhere.
This is the structural reason a derived `b_ν` plus two seeds determines the whole
`Δ_λ` ladder — the bootstrap that removes the need for the missing tower data. -/
theorem two_seed_unique (b a a' : ℕ → K)
    (ha : IsOrderThreeTermRec b a) (ha' : IsOrderThreeTermRec b a')
    (h0 : a 0 = a' 0) (h1 : a 1 = a' 1) :
    ∀ n, a n = a' n := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 => exact h0
    | 1 => exact h1
    | (k + 2) =>
      rw [ha k, ha' k, ih (k + 1) (by omega), ih k (by omega)]

/-- **Closed two-seed expansion at the first heavy level.** For an A = 2,3,4
tower indexed `ν = 0,1,2`, the top value is fixed by the two seeds and the single
interior coefficient `b 0`: `a 2 = b 0 · a 1 − a 0`. This is exactly the
derive-or-refute used on `Δ_λ` (predict ⁴He from {D, T} and the derived `b`). -/
theorem two_seed_top (b a : ℕ → K) (ha : IsOrderThreeTermRec b a) :
    a 2 = b 0 * a 1 - a 0 := ha 0

/-- **Two-root (second-kind) geometric solution ⟹ DERIVED coefficient.** If
`r · s = 1`, the two-sided geometric sequence `a n = α·rⁿ + β·sⁿ` solves the
order recurrence with the *constant* coefficient `b = r + s` — derived, not
fitted (`r, s` are the two roots of `t² − b·t + 1`).

This is the formal bridge for the binding `Δ_λ` ladder: the canonical residual
`Δ_λ(K) ≈ q₀^(10A−5)` (`docs/audits/2026-06-09-delta-lambda-canonical-residual.md`)
is geometric with ratio `r = q₀¹⁰`, so `s = r⁻¹ = q₀⁻¹⁰` and the **derived**
recurrence coefficient is `b = q₀¹⁰ + q₀⁻¹⁰ = 2cosh(10·log q₀)`. The `+β·sⁿ`
term is the **second-kind admixture** (Y_ν / K_ν branch) that carries the
per-isotope deviations from the pure first-kind geometric law. The open keystone
is a categorical derivation of the exponent `10A−5 = 5(2A−1)` — the `5` is the
Bring quintic — from the W_free vs W_atom crossing/jet bookkeeping; this lemma
is the recurrence half that the exponent derivation feeds. -/
theorem two_root_geometric (r s α β : K) (hrs : r * s = 1) :
    IsOrderThreeTermRec (fun _ => r + s) (fun n => α * r ^ n + β * s ^ n) := by
  intro n
  show α * r ^ (n + 2) + β * s ^ (n + 2)
      = (r + s) * (α * r ^ (n + 1) + β * s ^ (n + 1)) - (α * r ^ n + β * s ^ n)
  have hr2 : r ^ (n + 2) = r ^ n * r * r := by rw [pow_succ, pow_succ]
  have hr1 : r ^ (n + 1) = r ^ n * r := by rw [pow_succ]
  have hs2 : s ^ (n + 2) = s ^ n * s * s := by rw [pow_succ, pow_succ]
  have hs1 : s ^ (n + 1) = s ^ n * s := by rw [pow_succ]
  rw [hr2, hr1, hs2, hs1]
  linear_combination (-(α * r ^ n + β * s ^ n)) * hrs

/-- **Double-root / C-finite linear expansion.** The special case `r = s = 1`,
corresponding to the recurrence coefficient `b = 2`. The general solution
is the linear sequence `a n = α + β * n`. This formalises the decisive C-finite
recurrence found in the extended alpha-cluster tower where `b_ν ≈ 2` and `ρ ≈ 1`
(constant binding fractions). -/
theorem double_root_linear (α β : K) :
    IsOrderThreeTermRec (fun _ => 2) (fun n => α + β * (n : K)) := by
  intro n
  show α + β * (n + 2 : K) = 2 * (α + β * (n + 1 : K)) - (α + β * (n : K))
  push_cast
  ring

end QOU.QBeta
