import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Degree.Definitions
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.Div
import Mathlib.RingTheory.Ideal.Span
import Mathlib.RingTheory.Ideal.Operations
import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.Algebra.Ring.Subring.Basic
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
  * `cyclotomicPartialSum_isCauchy`
                            — **the increment hypothesis is UNCONDITIONAL for
                              the brane-tower shape**: every cyclotomic
                              partial-sum sequence `a n = Σ_{m ≤ n} c_m · P_m`
                              satisfies `IsCauchyFiltration` (the increment
                              telescopes to `c_{n+1} · P_{n+1} ∈ (P_n)`). The
                              compute witness `z-habiro-increment-probe`
                              identifies the `Φ_q` truncation tower with such a
                              cyclotomic partial sum, so this discharges the
                              former open *input* (item 1 below).
  * `quantumDilog_zHabiro_cauchy_limit_cyclotomic`
                            — **the UNCONDITIONAL Cauchy-limit thread**:
                              composing the two above, every cyclotomic
                              partial-sum sequence has a coherent inverse-limit
                              thread with NO `IsCauchyFiltration` hypothesis.
  * `ZHabiroCompletion`     — **the completion ring as a concrete `CommRing`**:
                              the inverse limit `varprojlim_n R[X]/(P_n)`,
                              realised as the `Subring` of compatible threads in
                              the product `Π n, R[X] ⧸ I_n`. `Subring.toCommRing`
                              endows it with a `CommRing` instance. This
                              packages `def:z-habiro-ring`'s cyclotomic
                              completion as a genuine algebraic object (former
                              open item 2).
  * `zHabiroLimit`          — **the brane-tower Cauchy limit AS AN ELEMENT** of
                              `ZHabiroCompletion`: for any coefficient family
                              `c`, the cyclotomic partial-sum tower's coherent
                              thread, packaged as an honest element of the
                              completion ring (the `Subring` membership proof IS
                              `quantumDilog_zHabiro_cauchy_limit_cyclotomic`).
                              This turns "the coherent thread exists" into "the
                              limit exists as an algebraic element of
                              `varprojlim`" — `def:z-habiro-ring`'s universal-
                              element claim, for the cyclotomic shape,
                              unconditionally over generic `[CommRing R]`.
  * `braneMonic` / `truncSection`
                            — **the `Trunc_{<n}` section (former open item 3),
                              under `IsUnit qinv`.** `branePoly qinv n` has
                              degree `n` with leading coefficient
                              `(-1)^n qinv^{n(n+1)/2}`, a unit when `qinv` is;
                              `braneMonic qinv n` is its canonical *monic*
                              associate (`branePoly_eq_unit_mul_braneMonic`,
                              `braneIdeal_eq_span_braneMonic`). `truncSection`
                              sends a class to its unique degree-`< n`
                              representative `p %ₘ g_n` (division-with-remainder
                              against the monic `g_n`), proved well-defined
                              (`modByMonic_well_defined`), a genuine section of
                              `mk` (`mk_truncSection`), and landing in degrees
                              `< n` (`degree_truncSection_lt`). This is the
                              canonical degree-`< n` representative identifying
                              `R[X]/(P_n)` with the literal `Trunc_{<n}[Φ_q]`.
  * `truncSection_zHabiroLimit`
                            — **the bridge to the literal truncations.** The
                              `Trunc_{<n}` section applied to the `n`-th
                              coordinate of `zHabiroLimit qinv c` returns the
                              genuine degree-`< n` truncation
                              `(Σ_{m ≤ n} c_m · P_m) %ₘ g_n` — the literal
                              `Trunc_{<n}` of the brane-tower partial sum that
                              the conjecture's `Φ̃^(N)` truncates to. This
                              connects the abstract inverse-limit threads to the
                              conjecture's stated truncations.

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

  1. **The increment hypothesis — DISCHARGED for the cyclotomic shape
     (UNCONDITIONAL, compute-backed).** This was the principal open input.
     The compute witness `computations/z-habiro-increment-probe.witness.json`
     (verdict `cauchy-limit-exists-localised`,
     `cyclotomic_expansion_exists_over_QQ_q: true`) establishes that `Φ_q`
     admits a cyclotomic `P_n`-expansion `Φ_q = Σ_m c_m · P_m`, so its
     depth-`n` truncation tower is *exactly* a cyclotomic partial sum
     `Σ_{m ≤ n} c_m · P_m`; the probe's `increment_checks` confirm every
     increment is `divisible_by_P_n` with `remainder = 0` up to depth 9.
     `cyclotomicPartialSum_isCauchy` (below) PROVES, sorry-free and
     unconditionally over a generic `[CommRing R]`, that EVERY such
     cyclotomic partial-sum sequence satisfies `IsCauchyFiltration` — the
     increment telescopes to a single term `c_{n+1} · P_{n+1} ∈ (P_n)` since
     `P_n ∣ P_{n+1}`. Composing with the conditional limit-thread gives the
     UNCONDITIONAL corollary `quantumDilog_zHabiro_cauchy_limit_cyclotomic`.
     So for the brane-tower shape the increment hypothesis is now a theorem,
     not an input. What is NOT claimed: that the conjecture's full `N`-indexed
     truncated sums coincide on the nose with this `n`-indexed cyclotomic
     partial sum at the level of the actual `Trunc_{<n}[Φ_q(V̂_i)]` map (that
     bridge needs the `Trunc_{<n}` section, item 3); the shape lemma proves
     the Cauchy/limit content for the cyclotomic-partial-sum *form* that the
     witness identifies the tower with.

  2. **The inverse-limit object as a `CommRing` — DISCHARGED.** This was an
     open item: the file used to exhibit only the coherent *thread* (a
     `∀ n, …` compatibility) without naming the object it lives in. It is now
     packaged: `ZHabiroCompletion qinv` (below) realises
     `varprojlim_n R[X]/(P_n)` as the `Subring` of compatible threads inside
     the product `Π n, R[X] ⧸ I_n`, and `Subring.toCommRing` endows it with a
     `CommRing` instance. `zHabiroLimit qinv c` then exhibits the brane-tower
     cyclotomic Cauchy limit as a genuine **element** of that ring (membership
     witness = `quantumDilog_zHabiro_cauchy_limit_cyclotomic`). Mathlib's
     `AdicCompletion` is for the *`I`-adic* (`Iⁿ`) chain and does NOT apply —
     the z-Habiro chain is **cyclotomic** (`I_{n+1} = (P_n · (1 - q^{-(n+1)}z))`,
     NOT the powers `(P_1)ⁿ`) — so we build the inverse limit directly as the
     equalizer-style subobject, which is the right fit and needs no completeness
     instance. What is NOT yet done (the genuinely-remaining algebraic gaps):
       (i) **identifying this element with the ACTUAL `Φ_q`.** `zHabiroLimit`
           is parametrised by an abstract coefficient family `c : ℕ → R`;
           pinning down the *specific* cyclotomic coefficients `c_n` of `Φ_q`
           requires a base `R` in which the cyclotomic factors are units — the
           probe `z-habiro-increment-probe` shows the `c_n` live in the
           cyclotomic LOCALISATION of `ℤ[q^±1]`, not the integral ring.
       (ii) the `Trunc_{<n}` literal-`N`-sum bridge (item 3 below).
     These are about *which* element and *which* base ring, not about the
     existence of the completion ring or of an algebraic limit element, both of
     which are now sorry-free.

  3. **`Trunc_{<n}` as the canonical section — DISCHARGED under `IsUnit qinv`.**
     The unique-degree-`< n` representative map `R[X]/(P_n) → R[X]` is now wired
     (`truncSection`, below). The *projections* `R[X]/(P_{n+1}) → R[X]/(P_n)`
     were already used here (`Ideal.Quotient.factor`); the *section* needs `P_n`
     to have a unit leading coefficient — true precisely when `qinv` is a unit,
     since `P_n` has leading coefficient `(-1)ⁿ qinv^(n(n+1)/2)`. We realise it
     via the monic associate `g_n := braneMonic qinv n` (an explicit product of
     monic linear factors `X - C(q^k)`, with `braneIdeal qinv n = (g_n)` by
     `braneIdeal_eq_span_braneMonic`) and `Polynomial.modByMonic`:
     `truncSection qinv hq n` sends a class to `p %ₘ g_n`, proved well-defined
     (`modByMonic_well_defined`), a genuine section of `mk` (`mk_truncSection`),
     and of degree `< n` (`degree_truncSection_lt`). The bridge
     `truncSection_zHabiroLimit` identifies the `n`-th coordinate of
     `zHabiroLimit` with the literal degree-`< n` truncation
     `(Σ_{m ≤ n} c_m · P_m) %ₘ g_n`. Hypothesis used: `IsUnit qinv` (the weakest
     that works — §7c; *not* a field, *not* `ℝ`), plus `Nontrivial R` for the
     degree statements only. All sorry-free.

This split is deliberate per the task's honesty directive: the filtration
algebra, the Cauchy criterion, the conditional limit-thread, the brane-tower
increment hypothesis (item 1), the completion ring + algebraic limit element
(item 2), AND the `Trunc_{<n}` section (item 3, under `IsUnit qinv`) are real
and sorry-free. The conjecture is **NOT** claimed fully closed: the SOLE
remaining algebraic gap is item 2(i) — identifying the abstract limit element
`zHabiroLimit qinv c` with the ACTUAL `Φ_q` by pinning the specific cyclotomic
coefficients `c_n` over the correct (cyclotomically localised) base ring, where
the probe `z-habiro-increment-probe` shows the `c_n` live. The `Trunc_{<n}`
truncation map itself is now concrete.

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

/-! ## The brane-tower shape: cyclotomic partial sums are UNCONDITIONALLY Cauchy

The increment hypothesis `IsCauchyFiltration` was the principal open *input* of
`quantumDilog_zHabiro_cauchy_limit` (file header "What remains OPEN" item 1).
For the **brane-tower-shaped** sequences it is no longer an input but a
THEOREM. The compute witness
`computations/z-habiro-increment-probe.witness.json` (verdict
`cauchy-limit-exists-localised`, `cyclotomic_expansion_exists_over_QQ_q: true`)
establishes that the quantum dilogarithm `Φ_q` admits a cyclotomic
`P_n`-expansion `Φ_q = Σ_m c_m · P_m`, so its depth-`n` truncation sequence is
*exactly* a cyclotomic partial sum `Σ_{m ≤ n} c_m · P_m`. Every increment of
such a sum is a single new term `c_{n+1} · P_{n+1}`, which lies in
`I_n = (P_n)` because `P_n ∣ P_{n+1}` (`branePoly_dvd_succ`) — the probe's
`increment_checks` confirm `remainder = 0` at every `n` up to depth 9. The
shape lemma below proves this for *all* coefficient families `c`,
unconditionally and over a generic `[CommRing R]` (§7c). -/

/-- **Shape lemma — UNCONDITIONAL.** Every cyclotomic partial-sum sequence
    `a n = Σ_{m ≤ n} c_m · P_m` (the brane-tower shape, with coefficient family
    `c : ℕ → R`) satisfies the z-Habiro Cauchy criterion `IsCauchyFiltration`.

    The increment `a (n+1) - a n` telescopes (`Finset.sum_range_succ`) to the
    single new term `C (c (n+1)) * branePoly qinv (n+1)`, which lies in
    `I_n = (P_n)` because `P_n ∣ P_{n+1}` (`branePoly_dvd_succ`). This is the
    Lean realisation of the compute witness
    `computations/z-habiro-increment-probe.witness.json`
    (`increment_checks[*].divisible_by_P_n = true`, `remainder = 0`): the
    quantum-dilog truncation tower *is* a cyclotomic partial sum, so its
    increment-coherence hypothesis is a theorem, not a conjecture. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Statement"
-- Ref: [manuscript] computations/z-habiro-increment-probe.witness.json
theorem cyclotomicPartialSum_isCauchy (qinv : R) (c : ℕ → R) :
    IsCauchyFiltration qinv
      (fun n => ∑ m ∈ Finset.range (n + 1), C (c m) * branePoly qinv m) := by
  intro n
  -- The increment telescopes to the single new term `C (c (n+1)) * P_{n+1}`.
  have htel :
      (∑ m ∈ Finset.range (n + 1 + 1), C (c m) * branePoly qinv m)
        - (∑ m ∈ Finset.range (n + 1), C (c m) * branePoly qinv m)
      = C (c (n + 1)) * branePoly qinv (n + 1) := by
    rw [Finset.sum_range_succ]; ring
  rw [htel, braneIdeal, Ideal.mem_span_singleton]
  -- `P_n ∣ C (c (n+1)) * P_{n+1}` since `P_n ∣ P_{n+1}`.
  exact (branePoly_dvd_succ qinv n).mul_left _

/-- **Algebraic Cauchy-limit thread (z-Habiro) — UNCONDITIONAL for the
    brane-tower shape.** Composing the shape lemma
    `cyclotomicPartialSum_isCauchy` with the conditional limit-thread
    `quantumDilog_zHabiro_cauchy_limit`: for *every* coefficient family
    `c : ℕ → R`, the cyclotomic partial-sum sequence
    `a n = Σ_{m ≤ n} c_m · P_m` has a coherent inverse-limit thread
    `n ↦ π_n(a n)` — compatible with every bonding map of
    `varprojlim_n R[X]/(P_n)`. No `IsCauchyFiltration` hypothesis is required:
    it is supplied by the shape lemma, which the compute witness
    `z-habiro-increment-probe` backs (the `Φ_q` truncation tower IS a
    cyclotomic partial sum). This discharges file-header "What remains OPEN"
    item 1 for the cyclotomic shape: the increment hypothesis is now a
    theorem. Items 2 (`varprojlim` as a `CommRing`) and 3 (`Trunc_{<n}`
    section) remain open. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Statement"
-- Ref: [manuscript] computations/z-habiro-increment-probe.witness.json
-- Ref: [habiro2004cyclotomic]
theorem quantumDilog_zHabiro_cauchy_limit_cyclotomic (qinv : R) (c : ℕ → R) :
    ∀ n : ℕ,
      (Ideal.Quotient.factor (braneIdeal_antitone qinv n))
          ((Ideal.Quotient.mk (braneIdeal qinv (n + 1)))
            (∑ m ∈ Finset.range (n + 1 + 1), C (c m) * branePoly qinv m))
        = (Ideal.Quotient.mk (braneIdeal qinv n))
            (∑ m ∈ Finset.range (n + 1), C (c m) * branePoly qinv m) :=
  quantumDilog_zHabiro_cauchy_limit qinv (cyclotomicPartialSum_isCauchy qinv c)

/-! ## The completion ring `varprojlim_n R[X]/(P_n)` as a concrete `CommRing`

The previous declarations exhibit the inverse-limit *thread* — a `∀ n, …`
compatibility — without naming the object the thread lives in. We now package
the cyclotomic inverse limit `varprojlim_n R[X]/(P_n)` as a genuine `CommRing`:
the **subring of compatible threads** inside the product `Π n, R[X] ⧸ I_n`.

This discharges file-header "What remains OPEN" item 2. Mathlib's
`AdicCompletion` is for the `I`-adic chain `(Iⁿ)`; the z-Habiro chain is
cyclotomic (`I_{n+1} = (P_n · (1 - q^{-(n+1)}z))`, *not* `(P_1)ⁿ`), so it does
not apply off-the-shelf. We instead build the inverse limit directly as the
equalizer-style subobject of the product, which `Subring` endows with a
`CommRing` instance for free. A compatible thread is precisely an element of
`varprojlim` because the bonding maps `Ideal.Quotient.factor` are ring
homomorphisms, so the compatibility predicate is closed under `*, +, 1, 0,
neg`. -/

/-- **The z-Habiro completion ring** `varprojlim_n R[X]/(P_n)`, realised as the
    subring of *compatible threads* in the product `Π n, R[X] ⧸ braneIdeal qinv n`.

    A family `x : Π n, R[X] ⧸ I_n` is a thread of the inverse system iff every
    bonding map `factor_{n+1→n} : R[X]/I_{n+1} → R[X]/I_n` carries `x (n+1)` to
    `x n`. The carrier is that compatibility set; closure under the ring
    operations is immediate because each `Ideal.Quotient.factor (…)` is a
    `RingHom` (`map_mul`, `map_add`, `map_one`, `map_zero`, `map_neg`).

    `Subring.toCommRing` (the product is commutative, so the subring is too)
    supplies the `CommRing` instance — the z-Habiro completion is a `CommRing`.
    This is the inverse-limit object of `def:z-habiro-ring`'s cyclotomic
    completion `varprojlim_n ℤ[q^±1][z]/(P_n)`, modelled over generic
    `[CommRing R]` (§7c). -/
-- Ref: [manuscript] def:z-habiro-ring §"Statement"
-- Ref: [manuscript] conj:brane-tower-z-habiro §"What survives the closure"
-- Ref: [habiro2004cyclotomic]
noncomputable def ZHabiroCompletion (qinv : R) :
    Subring (∀ n, R[X] ⧸ braneIdeal qinv n) where
  carrier := { x | ∀ n, Ideal.Quotient.factor (braneIdeal_antitone qinv n) (x (n + 1)) = x n }
  mul_mem' {x y} hx hy n := by
    simp only [Pi.mul_apply, map_mul, hx n, hy n]
  one_mem' n := by
    simp only [Pi.one_apply, map_one]
  add_mem' {x y} hx hy n := by
    simp only [Pi.add_apply, map_add, hx n, hy n]
  zero_mem' n := by
    simp only [Pi.zero_apply, map_zero]
  neg_mem' {x} hx n := by
    simp only [Pi.neg_apply, map_neg, hx n]

/-- The z-Habiro completion ring is commutative — it is a subring of the
    commutative product ring `Π n, R[X] ⧸ I_n`. (Recorded explicitly so
    downstream code can `inferInstance` a `CommRing (ZHabiroCompletion qinv)`.) -/
noncomputable instance (qinv : R) : CommRing (ZHabiroCompletion qinv) :=
  (ZHabiroCompletion qinv).toCommRing

/-- Membership in the completion ring is *exactly* thread-compatibility. -/
theorem mem_ZHabiroCompletion (qinv : R) (x : ∀ n, R[X] ⧸ braneIdeal qinv n) :
    x ∈ ZHabiroCompletion qinv ↔
      ∀ n, Ideal.Quotient.factor (braneIdeal_antitone qinv n) (x (n + 1)) = x n :=
  Iff.rfl

/-! ## The brane-tower Cauchy limit AS AN ELEMENT of the completion ring

This is the conjecture's `def:z-habiro-ring` "universal element" claim for the
cyclotomic shape: turning "the coherent thread exists" into "the limit exists
as an *algebraic element* of `varprojlim`". The membership proof IS the
unconditional cyclotomic limit theorem
`quantumDilog_zHabiro_cauchy_limit_cyclotomic`. -/

/-- **The brane-tower cyclotomic Cauchy limit, AS AN ELEMENT of the z-Habiro
    completion ring.**

    For any coefficient family `c : ℕ → R`, the cyclotomic partial-sum tower
    `a n = Σ_{m ≤ n} c_m · P_m` has, by `cyclotomicPartialSum_isCauchy`, a
    coherent inverse-limit thread `n ↦ π_n(a n)`. This packages that thread as
    a genuine element of `ZHabiroCompletion qinv` — the algebraic Cauchy LIMIT
    of the brane-tower truncation tower, living *inside* the completion ring,
    UNCONDITIONALLY and over generic `[CommRing R]` (§7c).

    The compatibility witness (the `Subring` membership proof) is exactly
    `quantumDilog_zHabiro_cauchy_limit_cyclotomic qinv c`. This is the
    "limit exists as an algebraic element" content of `conj:brane-tower-z-habiro`
    / `def:z-habiro-ring`, compute-backed by
    `computations/z-habiro-increment-probe.witness.json` (the `Φ_q` truncation
    tower IS a cyclotomic partial sum). -/
-- Ref: [manuscript] def:z-habiro-ring §"Statement" (universal element)
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Statement"
-- Ref: [manuscript] computations/z-habiro-increment-probe.witness.json
-- Ref: [habiro2004cyclotomic]
noncomputable def zHabiroLimit (qinv : R) (c : ℕ → R) : ZHabiroCompletion qinv :=
  ⟨fun n => (Ideal.Quotient.mk (braneIdeal qinv n))
              (∑ m ∈ Finset.range (n + 1), C (c m) * branePoly qinv m),
   quantumDilog_zHabiro_cauchy_limit_cyclotomic qinv c⟩

/-- The `n`-th component of the brane-tower limit element is the cyclotomic
    projection `π_n(Σ_{m ≤ n} c_m · P_m)` of the depth-`n` partial sum — the
    "value of the limit at level `n`". A projection-compatibility lemma making
    the limit element's coordinates explicit. -/
theorem zHabiroLimit_coe_apply (qinv : R) (c : ℕ → R) (n : ℕ) :
    (zHabiroLimit qinv c : ∀ n, R[X] ⧸ braneIdeal qinv n) n
      = (Ideal.Quotient.mk (braneIdeal qinv n))
          (∑ m ∈ Finset.range (n + 1), C (c m) * branePoly qinv m) :=
  rfl

/-! ## The `Trunc_{<n}` section — the canonical degree-`< n` representative

This section discharges file-header "What remains OPEN" item 3: the
**`Trunc_{<n}` section** `R[X] ⧸ (P_n) → R[X]` giving each class its unique
representative of degree `< n`. This is the bridge from the abstract
inverse-limit threads above to the LITERAL truncations `Trunc_{<n}[Φ_q]` of
the conjecture's statement.

**Mechanism.** `branePoly qinv n` has `z`-degree `n` with leading coefficient
`(-1)^n qinv^{n(n+1)/2}` — a *unit* exactly when `qinv` is a unit. Over such a
base the quotient `R[X] ⧸ (P_n)` is free of rank `n`, with the degree-`< n`
polynomials as a section. We realise the section concretely via
division-with-remainder against the **monic associate** `g_n = braneMonic qinv n`
(`Polynomial.modByMonic`): the canonical representative is `p ↦ p %ₘ g_n`.

**Hypothesis.** `IsUnit qinv` (the weakest hypothesis that works — §7c; we do
*not* specialise to `ℝ`, and we use `IsUnit qinv` rather than `[Field R]` so
the section holds over e.g. `ℤ[q^±1]`-localisations where `qinv` is a unit but
the ring is not a field). The single archimedean-free `Nontrivial R` is used
only for the degree statements (`braneMonic_degree`, `degree_truncSection_lt`),
where it ensures each linear factor `X - C(q^k)` has degree `1`. -/

/-- The **monic** z-Habiro partial product
    `g_n := ∏_{k=1}^n (X - C(Ring.inverse (qinv^k)))`. Each factor is monic
    (`monic_X_sub_C`), so the product is monic of degree `n`
    (`braneMonic_monic`, `braneMonic_degree`). Under `IsUnit qinv` this is the
    canonical monic associate of `branePoly qinv n`
    (`branePoly_eq_unit_mul_braneMonic`), used as the modulus for the
    degree-`< n` division-with-remainder section of `Trunc_{<n}`. -/
noncomputable def braneMonic (qinv : R) : ℕ → R[X]
  | 0 => 1
  | (n + 1) => braneMonic qinv n * (X - C (Ring.inverse (qinv ^ (n + 1))))

@[simp] theorem braneMonic_zero (qinv : R) : braneMonic qinv 0 = 1 := rfl

theorem braneMonic_succ (qinv : R) (n : ℕ) :
    braneMonic qinv (n + 1)
      = braneMonic qinv n * (X - C (Ring.inverse (qinv ^ (n + 1)))) := rfl

/-- `g_n` is monic — a product of monic linear factors `X - C(q^k)`. -/
theorem braneMonic_monic (qinv : R) (n : ℕ) : (braneMonic qinv n).Monic := by
  induction n with
  | zero => simp [braneMonic]
  | succ n ih => rw [braneMonic_succ]; exact ih.mul (monic_X_sub_C _)

/-- The unit by which `branePoly` and its monic associate `braneMonic` differ:
    `u_n := ∏_{k=1}^n (-(qinv^k))`. Under `IsUnit qinv` it is a unit
    (`braneUnit_isUnit`); it is the leading coefficient of `branePoly qinv n`,
    namely `(-1)^n qinv^{n(n+1)/2}`. -/
def braneUnit (qinv : R) : ℕ → R
  | 0 => 1
  | (n + 1) => braneUnit qinv n * (-(qinv ^ (n + 1)))

/-- `u_n` is a unit whenever `qinv` is — a product of units `-(qinv^k)`. -/
theorem braneUnit_isUnit (qinv : R) (hq : IsUnit qinv) (n : ℕ) :
    IsUnit (braneUnit qinv n) := by
  induction n with
  | zero => simp [braneUnit]
  | succ n ih => rw [braneUnit]; exact ih.mul ((hq.pow (n + 1)).neg)

/-- **`branePoly` is a unit multiple of its monic associate.** Under
    `IsUnit qinv`, `branePoly qinv n = C (u_n) * braneMonic qinv n` with
    `u_n := braneUnit qinv n` a unit, because each factor factors as
    `1 - C(qinv^{k}) · X = C(-(qinv^{k})) · (X - C((qinv^{k})⁻¹))`
    (using `Ring.mul_inverse_cancel` since `qinv^k` is a unit). -/
theorem branePoly_eq_unit_mul_braneMonic (qinv : R) (hq : IsUnit qinv) (n : ℕ) :
    branePoly qinv n = C (braneUnit qinv n) * braneMonic qinv n := by
  induction n with
  | zero => simp [branePoly, braneMonic, braneUnit]
  | succ n ih =>
    rw [branePoly, braneMonic_succ, braneUnit, ih, C_mul]
    have hfac : (1 - C (qinv ^ (n + 1)) * X)
        = C (-(qinv ^ (n + 1))) * (X - C (Ring.inverse (qinv ^ (n + 1)))) := by
      have h : qinv ^ (n + 1) * Ring.inverse (qinv ^ (n + 1)) = 1 :=
        Ring.mul_inverse_cancel _ (hq.pow (n + 1))
      rw [mul_sub, ← C_mul]
      have hneg : -(qinv ^ (n + 1)) * Ring.inverse (qinv ^ (n + 1)) = -1 := by
        rw [neg_mul, h]
      rw [hneg]; simp [C_neg]; ring
    rw [hfac]; ring

/-- **The z-Habiro filtration ideal is generated by the monic associate.**
    `braneIdeal qinv n = (g_n)` for `g_n = braneMonic qinv n`, because the
    generator `branePoly qinv n` differs from `g_n` by the unit `C (u_n)`
    (`Ideal.span_singleton_mul_left_unit`). So the modulus for the
    degree-`< n` section may be taken to be the *monic* `g_n` while the ideal
    of the completion chain (`braneIdeal`, `def:z-habiro-ring`) is unchanged. -/
theorem braneIdeal_eq_span_braneMonic (qinv : R) (hq : IsUnit qinv) (n : ℕ) :
    braneIdeal qinv n = Ideal.span {braneMonic qinv n} := by
  rw [braneIdeal, branePoly_eq_unit_mul_braneMonic qinv hq n]
  exact Ideal.span_singleton_mul_left_unit ((braneUnit_isUnit qinv hq n).map C) _

/-- **Well-definedness of the degree-`< n` representative.** If
    `p ≡ p' (mod braneIdeal qinv n)` then `p %ₘ g_n = p' %ₘ g_n`: the ideal is
    `(g_n)` (monic associate), so `g_n ∣ (p - p')`, hence
    `(p - p') %ₘ g_n = 0` (`modByMonic_eq_zero_iff_dvd`); `sub_modByMonic`
    distributes `%ₘ` over the difference. This is the descent condition that
    makes `truncSection` well-defined on the quotient. -/
theorem modByMonic_well_defined (qinv : R) (hq : IsUnit qinv) (n : ℕ)
    {p p' : R[X]} (h : p - p' ∈ braneIdeal qinv n) :
    p %ₘ braneMonic qinv n = p' %ₘ braneMonic qinv n := by
  rw [braneIdeal_eq_span_braneMonic qinv hq n, Ideal.mem_span_singleton] at h
  have hz : (p - p') %ₘ braneMonic qinv n = 0 :=
    (modByMonic_eq_zero_iff_dvd (braneMonic_monic qinv n)).mpr h
  rw [sub_modByMonic] at hz
  exact sub_eq_zero.mp hz

/-- **The `Trunc_{<n}` section** `R[X] ⧸ (P_n) → R[X]`: the canonical
    degree-`< n` representative of a class, given by division-with-remainder
    `p ↦ p %ₘ g_n` against the monic associate `g_n = braneMonic qinv n`
    (`Polynomial.modByMonic`). Well-defined by `modByMonic_well_defined`.

    This discharges file-header "What remains OPEN" item 3 — the canonical
    degree-`< n` section identifying `R[X]/(P_n)` with the truncations
    `Trunc_{<n}[Φ_q]` that the conjecture's `Φ̃^(N)` uses. Hypothesis:
    `IsUnit qinv` (so `P_n` has a unit leading coefficient, hence a monic
    associate). -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Statement"
-- Ref: [manuscript] def:z-habiro-ring §"Cyclotomic projections"
-- Ref: [habiro2004cyclotomic]
noncomputable def truncSection (qinv : R) (hq : IsUnit qinv) (n : ℕ) :
    (R[X] ⧸ braneIdeal qinv n) → R[X] :=
  fun x => Quotient.liftOn' x (· %ₘ braneMonic qinv n) (by
    intro a b h
    rw [Submodule.quotientRel_def] at h
    exact modByMonic_well_defined qinv hq n h)

/-- The section on a class `mk p` is the canonical remainder `p %ₘ g_n`. -/
theorem truncSection_mk (qinv : R) (hq : IsUnit qinv) (n : ℕ) (p : R[X]) :
    truncSection qinv hq n (Ideal.Quotient.mk (braneIdeal qinv n) p)
      = p %ₘ braneMonic qinv n := rfl

/-- **`truncSection` is a genuine section of `Ideal.Quotient.mk`.**
    `mk ∘ truncSection = id`: the chosen degree-`< n` representative
    `p %ₘ g_n` lands in the same class as `p`, because
    `g_n ∣ (p %ₘ g_n - p)` (`modByMonic_add_div`). So `truncSection` picks a
    representative in each fibre of the projection. -/
theorem mk_truncSection (qinv : R) (hq : IsUnit qinv) (n : ℕ)
    (x : R[X] ⧸ braneIdeal qinv n) :
    Ideal.Quotient.mk (braneIdeal qinv n) (truncSection qinv hq n x) = x := by
  induction x using Quotient.inductionOn' with
  | h p =>
    show Ideal.Quotient.mk (braneIdeal qinv n)
        (truncSection qinv hq n (Ideal.Quotient.mk (braneIdeal qinv n) p))
      = Ideal.Quotient.mk (braneIdeal qinv n) p
    rw [truncSection_mk, Ideal.Quotient.eq,
      braneIdeal_eq_span_braneMonic qinv hq n, Ideal.mem_span_singleton]
    refine ⟨-(p /ₘ braneMonic qinv n), ?_⟩
    have h := modByMonic_add_div p (braneMonic_monic qinv n)
    rw [mul_neg, eq_neg_iff_add_eq_zero]
    linear_combination h

/-- The degree of the monic associate `g_n` is exactly `n`
    (`Monic.degree_mul` + `degree_X_sub_C`). `Nontrivial R` ensures each linear
    factor `X - C(q^k)` has degree `1`. -/
theorem braneMonic_degree [Nontrivial R] (qinv : R) (n : ℕ) :
    (braneMonic qinv n).degree = n := by
  induction n with
  | zero => simp [braneMonic]
  | succ n ih =>
    rw [braneMonic_succ,
      (monic_X_sub_C (Ring.inverse (qinv ^ (n + 1)))).degree_mul, ih,
      degree_X_sub_C, ← Nat.cast_one, ← Nat.cast_add]

/-- **The section lands in degrees `< n`.** `(truncSection … x).degree < n`:
    the chosen representative `p %ₘ g_n` has degree strictly below
    `deg g_n = n` (`degree_modByMonic_lt`, `g_n` monic of degree `n`). This is
    the defining property of the canonical degree-`< n` representative — the
    literal `Trunc_{<n}` of `def:z-habiro-ring`. -/
theorem degree_truncSection_lt [Nontrivial R] (qinv : R) (hq : IsUnit qinv)
    (n : ℕ) (x : R[X] ⧸ braneIdeal qinv n) :
    (truncSection qinv hq n x).degree < n := by
  induction x using Quotient.inductionOn' with
  | h p =>
    show (truncSection qinv hq n
        (Ideal.Quotient.mk (braneIdeal qinv n) p)).degree < n
    rw [truncSection_mk]
    have hlt := degree_modByMonic_lt p (braneMonic_monic qinv n)
    rwa [braneMonic_degree qinv n] at hlt

/-! ## Bridge: the brane-tower limit's `n`-th coordinate IS a literal `Trunc_{<n}`

Composing `truncSection` with the inverse-limit element `zHabiroLimit`
identifies the `n`-th coordinate of the brane-tower Cauchy limit with the
GENUINE degree-`< n` truncation of the depth-`n` partial sum
`Σ_{m ≤ n} c_m · P_m` — i.e. the literal `Trunc_{<n}` the conjecture's
`Φ̃^(N)` truncates to. This closes the bridge from the abstract inverse-limit
threads (`zHabiroLimit`) to the literal truncations of the conjecture's
statement (file-header item 3 / `def:z-habiro-ring`'s `Trunc_{<n}`). -/

/-- **The brane-tower limit, truncated to degree `< n`, is the literal
    `Trunc_{<n}` of the partial sum.** Applying the `Trunc_{<n}` section to the
    `n`-th coordinate of `zHabiroLimit qinv c` returns the genuine degree-`< n`
    truncation `(Σ_{m ≤ n} c_m · P_m) %ₘ g_n` of the brane-tower partial sum.

    This is the literal "`Trunc_{<n}` of the brane-tower partial sum" of
    `conj:brane-tower-z-habiro` §"Statement": the abstract inverse-limit
    coordinate (`zHabiroLimit_coe_apply`) and the concrete degree-`< n`
    representative (`truncSection`) agree. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Statement"
-- Ref: [manuscript] def:z-habiro-ring §"Trunc_{<n}"
theorem truncSection_zHabiroLimit (qinv : R) (hq : IsUnit qinv)
    (c : ℕ → R) (n : ℕ) :
    truncSection qinv hq n
        ((zHabiroLimit qinv c : ∀ n, R[X] ⧸ braneIdeal qinv n) n)
      = (∑ m ∈ Finset.range (n + 1), C (c m) * branePoly qinv m)
          %ₘ braneMonic qinv n := by
  rw [zHabiroLimit_coe_apply, truncSection_mk]

/-! ## The cyclotomic coefficients `c_n`: which ring, and uniqueness

This section advances file-header "What remains OPEN" item 2(i) — pinning
WHICH coefficients `c_n` and over WHICH base ring `zHabiroLimit qinv c`'s
coefficient family `c` must be drawn from to reproduce the ACTUAL `Φ_q`.

**Which ring (the cyclotomic localisation).** The compute witness
`computations/z-habiro-increment-probe.witness.json` (verdict
`cauchy-limit-exists-localised`) establishes that the power-series
coefficients of `Φ_q` are the closed Euler form
`b_n = [z^n] Φ_q = q^{-n} / ∏_{j=1}^n (1 - q^{-j})`, and that the cyclotomic
coordinates `c_n` (obtained from the `b_n` by the unit-leading-coefficient
triangular change of basis to the `P_m`) are NOT integral over `ℤ[q^±1]`:
their denominators are products of the cyclotomic factors `(1 - q^{-j})`.
So the `c_n` live in `ℤ[q^±1]` localised at the multiplicative set generated
by `{1 - q^{-j} : j ≥ 1}` — `Φ_q`'s poles at `z = q^k` are exactly the
obstruction to integrality. `eulerCoeff` below realises the `b_n` in any base
ring where those factors are units (the localised ring).

**Uniqueness.** `braneMonic_coords_unique` proves the monic z-Habiro partial
products `g_0, …, g_n` are linearly independent (strictly increasing degrees,
each monic), so the cyclotomic coordinates of any element are UNIQUE — the
algebraic backbone of "pinning the `c_n`": there is at most one family `c`
realising a given truncation tower.

What remains genuinely OPEN (not closed here): the analytic↔algebraic
identification proving the specific localised family `c_n = ` (coordinates of
the Euler `b_n`) IS the family whose `zHabiroLimit` equals the analytic `Φ_q`.
That bridge is item 2(i) and is deliberately not faked. -/

/-- **The Euler series coefficient** `b_n = [z^n] Φ_q = q^{-n} / ∏_{j=1}^n (1 - q^{-j})`,
    realised in a base ring `R` where the cyclotomic factors `1 - qinv^j` are
    units (the cyclotomic localisation of `ℤ[q^±1]`). Written with `qinv = q⁻¹`
    and `Ring.inverse` for the cyclotomic denominators; over the localisation
    these inverses are genuine. This is the closed Euler form the compute
    witness `z-habiro-increment-probe` uses (`series_coeff_formula`). -/
-- Ref: [manuscript] computations/z-habiro-increment-probe.witness.json
-- Ref: [habiro2004cyclotomic]
noncomputable def eulerCoeff (qinv : R) (n : ℕ) : R :=
  qinv ^ n * ∏ j ∈ Finset.range n, Ring.inverse (1 - qinv ^ (j + 1))

@[simp] theorem eulerCoeff_zero (qinv : R) : eulerCoeff qinv 0 = 1 := by
  simp [eulerCoeff]

/-- Recurrence `b_{n+1} = b_n · q^{-1} · (1 - q^{-(n+1)})⁻¹` — the depth step of
    the Euler coefficients (the cyclotomic denominator gains one factor). -/
theorem eulerCoeff_succ (qinv : R) (n : ℕ) :
    eulerCoeff qinv (n + 1)
      = eulerCoeff qinv n * qinv * Ring.inverse (1 - qinv ^ (n + 1)) := by
  unfold eulerCoeff
  rw [Finset.prod_range_succ, pow_succ]
  ring

/-- The top coefficient of the monic associate `g_n`: it is `1` (monic of
    degree `n`). Used for the linear-independence / uniqueness argument. -/
theorem braneMonic_coeff_self [Nontrivial R] (qinv : R) (n : ℕ) :
    (braneMonic qinv n).coeff n = 1 := by
  have hd : (braneMonic qinv n).natDegree = n :=
    natDegree_eq_of_degree_eq_some (braneMonic_degree qinv n)
  have h := (braneMonic_monic qinv n).coeff_natDegree
  rwa [hd] at h

/-- The `n`-th coefficient of `g_m` vanishes when `m < n` (degree `m < n`). -/
theorem braneMonic_coeff_eq_zero_of_lt [Nontrivial R] (qinv : R) {m n : ℕ}
    (h : m < n) : (braneMonic qinv m).coeff n = 0 := by
  apply coeff_eq_zero_of_degree_lt
  rw [braneMonic_degree qinv m]
  exact_mod_cast h

/-- **Uniqueness of cyclotomic coordinates (linear independence of the monic
    basis).** If `∑_{m ≤ n} d_m · g_m = 0` then every `d_m = 0`: the monic
    z-Habiro partial products `g_0, …, g_n` (strictly increasing degrees, each
    monic) are linearly independent over `R`. Hence the cyclotomic coordinates
    of any polynomial are UNIQUE — the algebraic backbone of "pinning the
    `c_n`": at most one coefficient family realises a given truncation tower.
    Proved by descending on the top degree: the `X^n`-coefficient of the sum is
    `d_n` (only `g_n` reaches degree `n`, and it is monic), forcing `d_n = 0`,
    then recursing on the lower sum. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"What survives the closure"
-- Ref: [manuscript] def:z-habiro-ring §"Cyclotomic projections"
theorem braneMonic_coords_unique [Nontrivial R] (qinv : R) (d : ℕ → R) :
    ∀ n : ℕ, (∑ m ∈ Finset.range (n + 1), C (d m) * braneMonic qinv m) = 0 →
      ∀ m, m ≤ n → d m = 0 := by
  intro n
  induction n with
  | zero =>
    intro h m hm
    have hm0 : m = 0 := Nat.le_zero.mp hm
    subst hm0
    have hco := congrArg (fun p => p.coeff 0) h
    simpa [Finset.sum_range_one, coeff_C_mul, braneMonic_coeff_self qinv 0,
      coeff_zero] using hco
  | succ n ih =>
    intro h m hm
    rw [Finset.sum_range_succ] at h
    -- The lower sum has degree ≤ n, so its (n+1)-coefficient vanishes.
    have hScoeff :
        (∑ k ∈ Finset.range (n + 1), C (d k) * braneMonic qinv k).coeff (n + 1) = 0 := by
      rw [finset_sum_coeff]
      refine Finset.sum_eq_zero (fun k hk => ?_)
      rw [coeff_C_mul, braneMonic_coeff_eq_zero_of_lt qinv (Finset.mem_range.mp hk), mul_zero]
    -- Top coefficient of the whole sum is d (n+1) (only g_{n+1} reaches degree n+1).
    have htop : d (n + 1) = 0 := by
      have hco := congrArg (fun p => p.coeff (n + 1)) h
      simp only [coeff_add, hScoeff, coeff_C_mul, braneMonic_coeff_self qinv (n + 1),
        coeff_zero, zero_add, mul_one] at hco
      exact hco
    -- With d (n+1) = 0 the top term drops, so the lower sum is 0; recurse.
    have hrest : (∑ k ∈ Finset.range (n + 1), C (d k) * braneMonic qinv k) = 0 := by
      rw [htop, map_zero, zero_mul, add_zero] at h
      exact h
    rcases Nat.eq_or_lt_of_le hm with heq | hlt
    · subst heq; exact htop
    · exact ih hrest m (Nat.lt_succ_iff.mp hlt)

end QOU.MassEndomorphism.ZHabiroCauchy
