import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.YoungDiagramKernelCSMargin — the airtight Cauchy–Schwarz core of the M₁>0 route

The first odd hook-power moment `M₁ = Cov_Planch(Σ_□ h, Σ_□ c²)` is the sole open input of the Δ_λ
super-exponential growth bound (`YoungDiagramKernel.lean`, bean `qou-k5r5`). The **Cauchy–Schwarz
reduction** (PR #5896, `docs/audits/2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md`)
splits `M₁ = P − N` with

  `P = Cov(Σ|c|, ω₃) = ρ_P · σ_A · σ_W`,   `N = −Cov(ΣD², ω₃)`,   `Σh = Σ|c| + ΣD²`,

and observes that Cauchy–Schwarz gives `N ≤ σ_D · σ_W` for free (`|corr(ΣD², ω₃)| ≤ 1`). Hence the
**(CS) margin condition** `σ_D < ρ_P · σ_A` (with the common `σ_W = σ(ω₃)` cancelling) is *sufficient*
for `M₁ > 0`.

This file formalizes exactly that sufficiency — the **airtight algebraic core** of the route — as a
sorry-free theorem. Following the §3b-cond discipline, the theorem is **non-degenerate**: the analytic
inputs (`P = ρ_P σ_A σ_W`; the Cauchy–Schwarz bound `N ≤ σ_D σ_W`; the margin `σ_D < ρ_P σ_A`) are
carried as **explicit hypotheses**, and the conclusion `M₁ > 0` is **derived** from them by real
algebra — it is not a self-assuming projection. The hypotheses are supplied, for `n ≥ N₀`, by the
descent-DPP finite-n variance bound written out in
`docs/audits/2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md`; for `3 ≤ n < N₀` the exact
table (`YoungDiagramKernel.m1_pos_of_le_eight` and the `Fraction` extension) closes the window.

Stated over a generic ordered commutative ring (`[CommRing] [LinearOrder] [IsStrictOrderedRing]`, §7c — no field or division needed): only
ordered-ring arithmetic and `<` are used; no archimedean construct (square roots, real-ordering-only
tactics) appears, so no specialization to the reals is warranted at this level. The real σ's and ρ_P
instantiate the real field at the point of use.

(Note: `scripts/check-sidecars.sh` flags this file "§7c MIXED" because `linarith` is one of its STRONG
archimedean markers. That is a false positive of the documented kind: `linarith` here discharges linear
inequalities over the *abstract* ordered ring — there is **no `ℝ`** and no archimedean construct in the
file, so it is base-ring-minimal, not archimedean-specialized.)
-/

namespace QOU.BraidsAndKnots.YoungDiagramKernelCSMargin

/-- **The Cauchy–Schwarz margin core of `M₁ > 0` (sorry-free).**

Given the Fulman split `M₁ = P − N` with `P = ρ_P σ_A σ_W`, the Cauchy–Schwarz bound `N ≤ σ_D σ_W`,
a positive `σ_W`, and the **(CS) margin** `σ_D < ρ_P σ_A`, the moment is strictly positive:

  `M₁ = P − N ≥ ρ_P σ_A σ_W − σ_D σ_W = σ_W (ρ_P σ_A − σ_D) > 0`.

Every hypothesis is an analytic *input* (three of them supplied by the descent-DPP finite-n bound, one
— the Cauchy–Schwarz `N ≤ σ_D σ_W` — a universal inequality); the conclusion is *derived*. This is the
only step of the M₁>0 route that is pure algebra, and it is airtight. Note `σ_A` need not even appear
as a separate positivity hypothesis: the margin `σ_D < ρ_P σ_A` already forces `ρ_P σ_A > σ_D ≥ 0`
whenever `σ_D ≥ 0`, but we do not assume `σ_D ≥ 0` — the proof needs only `σ_W > 0` and the margin. -/
theorem m1_pos_of_cs_margin {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (P N M1 sigA sigD sigW rhoP : R)
    (hP : P = rhoP * sigA * sigW)
    (hN : N ≤ sigD * sigW)
    (hM1 : M1 = P - N)
    (hsigW : 0 < sigW)
    (hCS : sigD < rhoP * sigA) :
    0 < M1 := by
  have hmargin : 0 < rhoP * sigA - sigD := by linarith
  have hkey : 0 < sigW * (rhoP * sigA - sigD) := mul_pos hsigW hmargin
  have hsplit : M1 = sigW * (rhoP * sigA - sigD) + (sigD * sigW - N) := by
    rw [hM1, hP]; ring
  have hslack : 0 ≤ sigD * sigW - N := by linarith
  rw [hsplit]; linarith

/-- **All-`n` positivity from (CS)-margin-for-large-`n` plus the exact finite base (sorry-free).**

The logical skeleton of the `M₁ > 0 ∀n` closure: if `M₁(n) > 0` for every `n` below a threshold `N₀`
(the exact table) and the (CS) margin certificate holds for every `n ≥ N₀` (the analytic bound), then
`M₁(n) > 0` for all `n`. Here `M1 : ℕ → R` is the (scaled) moment sequence and `pos_lt`/`pos_ge` are
the two supplied certificates; the theorem merely splits on `n < N₀`. Trivial by design — it records
that the two halves of the reduction compose with no gap, so that when the analytic `pos_ge` is
discharged (with an explicit `N₀`) and `pos_lt` is the exact table, the all-`n` statement follows. -/
theorem m1_pos_all_of_base_and_tail {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (M1 : ℕ → R) (N0 : ℕ)
    (pos_lt : ∀ n, n < N0 → 0 < M1 n)
    (pos_ge : ∀ n, N0 ≤ n → 0 < M1 n) :
    ∀ n, 0 < M1 n := by
  intro n
  rcases lt_or_ge n N0 with h | h
  · exact pos_lt n h
  · exact pos_ge n h

/-- **The M₁>0 all-`n` reduction skeleton (sorry-free) — `[analytic (CS) inputs] ⟹ M₁>0 ∀n`.**

This is the honest §3b-cond terminal form of the `M₁>0` arc: it **derives** `M₁(n) > 0` for *every*
`n` from two supplied certificates, chaining `m1_pos_of_cs_margin` (the Cauchy–Schwarz core) with the
base/tail split. It is **non-degenerate** — none of the hypotheses is the conclusion; the conclusion
is composed from them by real algebra:

- **Finite base** `base` : `M₁(n) > 0` for `n < N₀`. Supplied by the exact `Fraction`/`decide`
  table (`YoungDiagramKernel.m1_pos_of_le_eight` and its extension; certified to `n = 78`).
- **Tail, via the (CS) inputs** for each `n ≥ N₀`: the Fulman split `M₁ n = P n − N n`, the
  factorisation `P n = ρ_P n · σ_A n · σ_W n`, the Cauchy–Schwarz bound `N n ≤ σ_D n · σ_W n`,
  positivity `0 < σ_W n`, and — the one genuinely analytic input — the **(CS) margin**
  `σ_D n < ρ_P n · σ_A n`.

That margin hypothesis `hCS` is **exactly** what a rigorous Bessel/Debye/Euler–Maclaurin bound on the
descent-DPP variance ingredients would discharge (for an explicit `N₀`); everything else here is
either a definition, the universal Cauchy–Schwarz inequality, or the exact table. So this theorem
states precisely **what is assumed versus proved**: `M₁>0` for all `n` is *proved* modulo the single
analytic margin certificate — it is the reduction, not the closure. See
`docs/audits/2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md` for the scheme that would
supply `hCS`, and the `qou-h315` epic for the machinery still to be built.

Base ring: generic ordered commutative ring (no `ℝ`, no division); `linarith` over it is
base-ring-minimal (the `check-sidecars` "§7c MIXED" flag is the documented false positive). -/
theorem m1_pos_all_of_cs_inputs {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (M1 P N sigA sigD sigW rhoP : ℕ → R) (N0 : ℕ)
    (base : ∀ n, n < N0 → 0 < M1 n)
    (hP : ∀ n, N0 ≤ n → P n = rhoP n * sigA n * sigW n)
    (hN : ∀ n, N0 ≤ n → N n ≤ sigD n * sigW n)
    (hM1 : ∀ n, N0 ≤ n → M1 n = P n - N n)
    (hsigW : ∀ n, N0 ≤ n → 0 < sigW n)
    (hCS : ∀ n, N0 ≤ n → sigD n < rhoP n * sigA n) :
    ∀ n, 0 < M1 n := by
  refine m1_pos_all_of_base_and_tail M1 N0 base (fun n hn => ?_)
  exact m1_pos_of_cs_margin (P n) (N n) (M1 n) (sigA n) (sigD n) (sigW n) (rhoP n)
    (hP n hn) (hN n hn) (hM1 n hn) (hsigW n hn) (hCS n hn)

end QOU.BraidsAndKnots.YoungDiagramKernelCSMargin
