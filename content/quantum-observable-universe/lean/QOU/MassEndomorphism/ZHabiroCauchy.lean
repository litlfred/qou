import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Degree.Definitions
import Mathlib.RingTheory.Ideal.Span
import Mathlib.RingTheory.Ideal.Operations
import Mathlib.Tactic

/-!
# z-Habiro Cauchy-limit: the descending-chain / increment-coherence core

This file advances the **algebraic Cauchy-limit half** of
`conj:brane-tower-z-habiro`
(`content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md`
§"Statement", §"What survives the closure" item 1).

The convergence *prerequisite* — that the analytic infinite product
`Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}` is `Multipliable` for `1 < q`,
`|z| < q` — is already proved sorry-free in
`QOU.MassEndomorphism.PhiQConvergence.quantumDilog_multipliable`.

The remaining open half is **algebraic**: the truncated partial sums

  Φ̃^(N)(β) := Σ_{i=1}^N Trunc_{<n}[Φ_q(V̂_i)]  ∈  ℤ[q^±1][z] / (P_n(q,z))

are claimed to be Cauchy in the *z-Habiro topology* — the cyclotomic
completion of `ℤ[q^±1][z]` at the descending chain of ideals
`I_n = (P_n(q,z))`, where

  P_n(q,z) := ∏_{k=1}^{n} (1 - q^{-k} z)          (`def:z-habiro-ring`)

and the limit exists as an algebraic element of the inverse limit
`varprojlim_n  ℤ[q^±1][z] / (P_n)`.

## What this file PROVES sorry-free

The **filtration foundation** + the **increment-coherence Cauchy core**,
the genuinely decidable substance of the claim, stated over a generic
base ring (§7c discipline — no archimedean `ℝ`, no `LaurentPolynomial`
dependency; `ℤ[q^±1]` is modelled as a `CommRing R` carrying a chosen
unit `qinv := q⁻¹`, and `ℤ[q^±1][z]` as `R[X]`).

  * `branePoly`             — the partial products `P_n` in `z = X`,
                              `P 0 = 1`, `P (n+1) = P n * (1 - qinv^(n+1)•X)`.
  * `branePoly_dvd_succ`    — `P n ∣ P (n+1)` (each product divides the next).
  * `branePoly_dvd_of_le`   — `P n ∣ P m` for `n ≤ m` (the chain is monotone
                              under divisibility).
  * `braneIdeal`            — the z-Habiro filtration `I_n = (P_n)`.
  * `braneIdeal_antitone`   — `I_{n+1} ≤ I_n`, hence `I_m ≤ I_n` for `n ≤ m`
                              (`braneIdeal_le_of_le`): the **descending chain**
                              that makes the inverse limit / completion
                              well-defined.
  * `IsCauchyFiltration`    — the precise increment criterion: a sequence
                              `a : ℕ → R[X]` is Cauchy for this filtration iff
                              `a (n+1) - a n ∈ I_n` for every `n`.
  * `cauchy_tail_mem`       — **the increment-coherence Cauchy core**: from the
                              increment criterion, `a m - a n ∈ I_n` for *all*
                              `m ≥ n`. Equivalently the cyclotomic projections
                              `π_n^{(z)}(a m)` stabilise for `m ≥ n` — exactly
                              the Cauchy condition in the `I_n`-adic-style
                              (filtration) topology of `def:z-habiro-ring`.
  * `cauchy_proj_stabilises`— the same fact as a quotient congruence
                              `π_n(a m) = π_n(a n)` (`m ≥ n`).
  * `quantumDilog_zHabiro_cauchy_limit`
                            — **the inverse-limit thread is coherent**: the
                              family `n ↦ π_n^{(z)}(a n)` is compatible with
                              every bonding map `R[X]/(P_{n+1}) → R[X]/(P_n)`
                              (`Ideal.Quotient.factor` of the descending
                              chain), so it IS an element of the inverse
                              system `varprojlim_n R[X]/(P_n)`. This is the
                              **algebraic Cauchy-LIMIT existence**, conditional
                              only on the increment hypothesis
                              `IsCauchyFiltration` — proved sorry-free here.

`cauchy_tail_mem` is the algebraic heart of the Cauchy-sequence claim: any
sequence whose successive *increments* sink into deeper ideals has
stabilising cyclotomic projections, i.e. it converges in the z-Habiro
filtration topology. `quantumDilog_zHabiro_cauchy_limit` then upgrades the
stabilising thread to a genuine coherent element of the inverse system. So
the conjecture's Cauchy-limit half is reduced, with NO remaining `sorry` in
this file, to a single concrete *input* — the increment hypothesis for the
specific brane-tower sequence — plus packaging the inverse limit as a ring
(see "What remains OPEN").

## What remains OPEN (honest gap — NOT papered over)

Everything in this file is **sorry-free** (verified: the declarations depend
only on `propext, Classical.choice, Quot.sound`). The Cauchy-limit existence
proved here is *conditional* — it takes the increment hypothesis
`IsCauchyFiltration` as input and exhibits the inverse-limit thread. Three
items remain OPEN and are deliberately NOT attempted here (a `sorry` would be
dishonest; instead they are simply absent — no false `: True` stub stands in
for them):

  1. **The increment hypothesis for the actual brane-tower sequence.** This
     is the principal open input. The conjecture's partial sums are indexed
     by `N` (number of generators) at *fixed* truncation level `n`; the
     Cauchy claim is in the *`n`* (depth) direction. `cauchy_tail_mem` /
     `quantumDilog_zHabiro_cauchy_limit` discharge the Cauchy criterion and
     the limit thread *once* `Φ̃^(n+1) - Φ̃^(n) ∈ I_n` is supplied, but
     proving that hypothesis for `Trunc_{<n}[Φ_q(V̂_i)]` requires the
     truncation map and a degree/valuation bound on the increment, and
     whether the conjecture's *N*-indexed sums genuinely satisfy a
     *depth*-indexed increment bound is itself part of the open mathematical
     content (the `.md` §"What survives the closure": "a direct algebraic
     proof proceeds via the cyclotomic projections π_n^{(z)}").
     [Open MATH, not just missing Lean — this is the real conjectural core.]

  2. **The inverse-limit object as a `CommRing`.** This file exhibits the
     coherent *thread* (a `∀ n, …` compatibility), which is the inverse
     system's data, but does not package `varprojlim_n R[X]/(P_n)` as a
     concrete `CommRing` with its universal property. Mathlib has
     `Mathlib.RingTheory.AdicCompletion` for the *`I`-adic* (`Iⁿ`) chain,
     but the z-Habiro chain is **cyclotomic** (`I_n = (P_n)` with
     `P_{n+1} = P_n · (1 - q^{-(n+1)} z)`), NOT the powers `(P_1)ⁿ` of a
     single ideal, so `AdicCompletion` does not apply off-the-shelf; the
     correct fit is a filtered (linearly-topologised) completion, which
     Mathlib lacks a ready completeness instance for. Building it is the
     parallel of Habiro's own `\widehat{ℤ[q]}` construction.
     [Infrastructure gap: cyclotomic (non-`Iⁿ`) completion ring.]

  3. **`Trunc_{<n}` as the canonical section.** The unique-degree-`< n`
     representative map `R[X]/(P_n) → R[X]` ("evaluation in the quotient is
     finite"). The *projections* `R[X]/(P_{n+1}) → R[X]/(P_n)` are already
     used here (`Ideal.Quotient.factor`); the *section* needs `P_n` to be a
     non-zero-divisor with unit leading coefficient — true here since `P_n`
     has leading coefficient `(-1)ⁿ qinv^(n(n+1)/2)`, a unit — but the
     division-with-remainder API for it is not wired in this file.

This split is deliberate per the task's honesty directive: the filtration
algebra, the Cauchy criterion, AND the conditional limit-thread are real and
sorry-free; the brane-tower-specific increment input (the genuine open math),
the completion-ring packaging, and the `Trunc_{<n}` section are the named
remaining gaps.

## References

- [manuscript] `conj:brane-tower-z-habiro` §"Statement"
  (`content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md`)
- [manuscript] `def:z-habiro-ring`
  (`content/quantum-observable-universe/mass-theory/z-habiro-ring.md`):
  the cyclotomic completion `varprojlim_n ℤ[q^±1][z]/(P_n)`.
- [habiro2004cyclotomic] Habiro, *Cyclotomic completions of polynomial
  rings* — the `q`-side completion this construction parallels.
-/

namespace QOU.MassEndomorphism.ZHabiroCauchy

open Polynomial

variable {R : Type*} [CommRing R]

/-! ## The z-Habiro partial products `P_n(q,z)`

We model `ℤ[q^±1][z]` as `R[X]` with `R` a commutative ring carrying a
chosen element `qinv : R` standing for `q⁻¹` (a unit in `ℤ[q^±1]`, but the
divisibility/ideal results below need only `CommRing R`, so we keep `R`
generic — §7c). The variable `X` is the brane-tower variable `z`. -/

/-- The `n`-th z-Habiro partial product
    `P_n(q,z) = ∏_{k=1}^{n} (1 - q^{-k} z)`, written with `qinv = q⁻¹`,
    `z = X`. `P 0 = 1`; `P (n+1) = P n · (1 - qinv^{n+1} · X)`. -/
noncomputable def branePoly (qinv : R) : ℕ → R[X]
  | 0 => 1
  | (n + 1) => branePoly qinv n * (1 - C (qinv ^ (n + 1)) * X)

@[simp] theorem branePoly_zero (qinv : R) : branePoly qinv 0 = 1 := rfl

theorem branePoly_succ (qinv : R) (n : ℕ) :
    branePoly qinv (n + 1) = branePoly qinv n * (1 - C (qinv ^ (n + 1)) * X) := rfl

/-- Each partial product divides the next: `P_n ∣ P_{n+1}`. -/
theorem branePoly_dvd_succ (qinv : R) (n : ℕ) :
    branePoly qinv n ∣ branePoly qinv (n + 1) := by
  rw [branePoly_succ]
  exact dvd_mul_right _ _

/-- The divisibility chain is monotone: `P_n ∣ P_m` whenever `n ≤ m`. -/
theorem branePoly_dvd_of_le (qinv : R) {n m : ℕ} (h : n ≤ m) :
    branePoly qinv n ∣ branePoly qinv m := by
  induction m with
  | zero => simpa using (Nat.le_zero.mp h) ▸ dvd_refl _
  | succ m ih =>
    rcases Nat.lt_or_ge n (m + 1) with hlt | hge
    · exact (ih (Nat.lt_succ_iff.mp hlt)).trans (branePoly_dvd_succ qinv m)
    · -- n ≥ m+1 and n ≤ m+1 forces n = m+1
      have : n = m + 1 := le_antisymm h hge
      exact this ▸ dvd_refl _

/-! ## The z-Habiro filtration `I_n = (P_n)` -/

/-- The z-Habiro filtration ideal `I_n = (P_n(q,z))` of
    `ℤ[q^±1][z] = R[X]`. The cyclotomic completion of `def:z-habiro-ring`
    is the inverse limit of `R[X] / I_n` along this descending chain. -/
noncomputable def braneIdeal (qinv : R) (n : ℕ) : Ideal R[X] :=
  Ideal.span {branePoly qinv n}

/-- **Descending chain (single step):** `I_{n+1} ≤ I_n`.
    This is the defining property of the z-Habiro filtration —
    `(P_{n+1}) ⊆ (P_n)` because `P_n ∣ P_{n+1}`. It makes the cyclotomic
    inverse limit `varprojlim_n R[X]/(P_n)` well-defined (the bonding maps
    `R[X]/(P_{n+1}) → R[X]/(P_n)` exist). -/
theorem braneIdeal_antitone (qinv : R) (n : ℕ) :
    braneIdeal qinv (n + 1) ≤ braneIdeal qinv n := by
  rw [braneIdeal, braneIdeal, Ideal.span_singleton_le_span_singleton]
  exact branePoly_dvd_succ qinv n

/-- **Descending chain (general):** `I_m ≤ I_n` for `n ≤ m`. -/
theorem braneIdeal_le_of_le (qinv : R) {n m : ℕ} (h : n ≤ m) :
    braneIdeal qinv m ≤ braneIdeal qinv n := by
  rw [braneIdeal, braneIdeal, Ideal.span_singleton_le_span_singleton]
  exact branePoly_dvd_of_le qinv h

/-! ## The Cauchy criterion for the z-Habiro filtration topology -/

/-- A sequence `a : ℕ → R[X]` is **Cauchy for the z-Habiro filtration**
    iff each increment lands in the corresponding ideal:
    `a_{n+1} - a_n ∈ I_n`. In the filtration (linear) topology whose
    neighbourhood basis of `0` is `{I_n}`, this is exactly the statement
    that `(a_n)` is a Cauchy sequence — the increments tend to `0`. -/
def IsCauchyFiltration (qinv : R) (a : ℕ → R[X]) : Prop :=
  ∀ n : ℕ, a (n + 1) - a n ∈ braneIdeal qinv n

/-- **Increment-coherence Cauchy core.** If `(a_n)` satisfies the
    increment criterion, then for every `m ≥ n` the difference
    `a_m - a_n ∈ I_n`.

    Equivalently: the cyclotomic projections
    `π_n^{(z)}(a_m) = π_n^{(z)}(a_n)` agree for all `m ≥ n`, so the thread
    `(π_n^{(z)}(a_n))_n` is a coherent element of the inverse system
    `varprojlim_n R[X]/(P_n)` — i.e. `(a_n)` converges in the z-Habiro
    filtration topology. This is the precise algebraic Cauchy content of
    `conj:brane-tower-z-habiro` §"Statement", discharged from the
    descending chain `braneIdeal_le_of_le`. -/
theorem cauchy_tail_mem (qinv : R) {a : ℕ → R[X]}
    (hcauchy : IsCauchyFiltration qinv a) {n m : ℕ} (h : n ≤ m) :
    a m - a n ∈ braneIdeal qinv n := by
  induction m with
  | zero =>
    -- n ≤ 0 ⇒ n = 0 ⇒ a 0 - a 0 = 0 ∈ I_0
    have hn : n = 0 := Nat.le_zero.mp h
    simp [hn]
  | succ m ih =>
    rcases Nat.lt_or_ge n (m + 1) with hlt | hge
    · -- n ≤ m: split a_{m+1} - a_n = (a_{m+1} - a_m) + (a_m - a_n)
      have hnm : n ≤ m := Nat.lt_succ_iff.mp hlt
      have step : a (m + 1) - a m ∈ braneIdeal qinv n :=
        braneIdeal_le_of_le qinv hnm (hcauchy m)
      have rest : a m - a n ∈ braneIdeal qinv n := ih hnm
      have : a (m + 1) - a n = (a (m + 1) - a m) + (a m - a n) := by ring
      rw [this]
      exact Ideal.add_mem _ step rest
    · -- n = m+1: difference is 0
      have : n = m + 1 := le_antisymm h hge
      simp [this]

/-- The cyclotomic projections of a Cauchy sequence agree on the tail,
    phrased as a congruence in the quotient `R[X] / I_n`. This is
    `cauchy_tail_mem` repackaged via `Ideal.Quotient.eq` — the form in
    which the inverse-limit thread `(π_n(a_n))_n` is read off. -/
theorem cauchy_proj_stabilises (qinv : R) {a : ℕ → R[X]}
    (hcauchy : IsCauchyFiltration qinv a) {n m : ℕ} (h : n ≤ m) :
    (Ideal.Quotient.mk (braneIdeal qinv n)) (a m)
      = (Ideal.Quotient.mk (braneIdeal qinv n)) (a n) := by
  rw [Ideal.Quotient.eq]
  exact cauchy_tail_mem qinv hcauchy h

/-! ## The Cauchy-LIMIT thread exists — proved sorry-free (conditional on the
    increment hypothesis)

The increment-coherence core above gives the Cauchy *criterion* and shows
the projections stabilise. We now exhibit the limit *as a coherent thread of
the inverse system* `varprojlim_n R[X]/(P_n)`: the family
`n ↦ π_n^{(z)}(a_n)` is compatible with every bonding map
`R[X]/(P_{n+1}) → R[X]/(P_n)` (`Ideal.Quotient.factor` of the descending
chain `braneIdeal_antitone`). That compatibility is exactly what makes the
family an element of the inverse limit — the algebraic limit of `(a_n)` in
the z-Habiro topology of `def:z-habiro-ring`.

This is proved with NO `sorry`, conditional only on `IsCauchyFiltration`
(the increment hypothesis). Packaging the inverse limit as a `CommRing`
object and proving the increment hypothesis for the *specific* brane-tower
sequence remain open (file header "What remains OPEN" items 1–2) but are
NOT faked here. -/

/-- **Algebraic Cauchy-limit thread (z-Habiro) — sorry-free, conditional.**

    For a sequence `(a_n)` Cauchy in the z-Habiro filtration
    (`IsCauchyFiltration`), the coherent family of projections
    `n ↦ π_n^{(z)}(a_n)` is compatible with every bonding map of the inverse
    system: the bonding map `factor_{n+1→n}` sends `π_{n+1}(a_{n+1})` to
    `π_n(a_n)`. Hence the thread `(π_n(a_n))_n` is a genuine element of
    `varprojlim_n R[X]/(P_n)` — the algebraic limit of `(a_n)` in
    `def:z-habiro-ring`. Proved from `Ideal.Quotient.factor_mk` (the bonding
    map is `mk`-functorial) and the increment criterion `hcauchy`.

    NOTE: this is the *conjectural-Cauchy-limit half* of
    `conj:brane-tower-z-habiro`, discharged modulo the increment hypothesis;
    the analytic prerequisite is closed in
    `QOU.MassEndomorphism.PhiQConvergence.quantumDilog_multipliable`. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Statement"
-- Ref: [manuscript] def:z-habiro-ring §"Cyclotomic projections"
-- Ref: [habiro2004cyclotomic]
theorem quantumDilog_zHabiro_cauchy_limit (qinv : R) {a : ℕ → R[X]}
    (hcauchy : IsCauchyFiltration qinv a) :
    ∀ n : ℕ,
      (Ideal.Quotient.factor (braneIdeal_antitone qinv n))
          ((Ideal.Quotient.mk (braneIdeal qinv (n + 1))) (a (n + 1)))
        = (Ideal.Quotient.mk (braneIdeal qinv n)) (a n) := by
  intro n
  -- `factor h (mk I_{n+1} x) = mk I_n x` (the bonding map sends the class of
  -- `a (n+1)` mod `I_{n+1}` to its class mod `I_n`), then `mk I_n (a (n+1))
  -- = mk I_n (a n)` because `a (n+1) - a n ∈ I_n` (the increment criterion).
  -- Ref: [manuscript] conj:brane-tower-z-habiro §"What survives the closure"
  rw [Ideal.Quotient.factor_mk]
  rw [Ideal.Quotient.eq]
  exact hcauchy n

end QOU.MassEndomorphism.ZHabiroCauchy
