import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.MarkovParameterFibreRank

The Markov stabilisation parameter `z` and the fibre rank `N` are the same
datum, and under the **full** bar involution that datum is bar-covariant with
law `bar(z) = z - h`.

## Context

`markov-axioms-primitive` stipulates the Markov parameter `z` in axiom M3
(`τ(x · σₙ) = z · τ(x)`).  Two conventions have been live in the corpus:

* **C** — `z = 1/(√q + 1/√q)`, historically the corpus default, hard-coded
  in binding's Wenzl bridge (`computations/y_lambda_wenzl_bridge.py`).
* **D** — `z = q³/(q² + 1)`, the Jones / `SU_q(2)` value, i.e. rank `N = 2`.

The Wenzl bridge's fractional rank condition `X = Qᴺ` (with `Q = q²`,
`X = qz/(1 - Q + qz)`) is equivalent to `z · [N]_q = qᴺ`, so a choice of `z`
*is* a choice of fibre rank.

## The condition M3 actually imposes

`def:bar-involution` has two independently-applicable halves: the
**coefficient** half `q ↦ q⁻¹` and the **diagram** half `σᵢ ↦ σᵢ⁻¹`.  M3
contains `σₙ`, so the bar-partner of `z` is *not* `z` — the involution
inverts the generator too.  The Hecke relation gives `σ⁻¹ = σ - h` exactly
(`hecke_inv_eq_sub` below), hence `τ(x · σₙ⁻¹) = (z - h)·τ(x)` and the
covariance condition M3 supports is

    bar(z) = z - h,        h = q - q⁻¹.

Computing bar-invariance as `z(q⁻¹) = z(q)` applies the coefficient half
alone.  That is what the earlier results in this file (retained below, and
still correct as stated) measure.

## What is proved here

`zRank N q = q^(2N-1)(q² - 1)/(q^(2N) - 1)` is the member of the family at
rank `N`, written without natural-number subtraction.

**Coefficient half** (unchanged, still true of what it states):

* `zRank_two` — convention D is exactly rank `2`.
* `zRank_bar` — `zRank N q⁻¹ = zRank N q / q^(2N)`.
* `pow_two_mul_eq_one_of_zRank_bar_invariant` — hence `q(q⁻¹)`-invariance of
  a nonzero `zRank N q` forces `q^(2N) = 1`: no fibre rank is bar-*invariant*
  in the coefficient-half sense.

**Full involution** (the operative law):

* `hecke_inv_eq_sub` — `σ² = hσ + 1` makes `σ - h` a two-sided inverse of
  `σ`; this is where `z - h` comes from, not an extra assumption.
* `zRank_bar_sub` — `zRank N q⁻¹ = zRank N q - (q - q⁻¹)` for **every** rank
  `N`.  The full law is an identity of the whole family: bar-covariance and
  the fibre reading are the same condition, not competing desiderata.
* `zD_bar_sub` — convention **D satisfies** it.
* `zC_bar`, `zC_ne_bar_sub` — convention **C fails** it, by exactly `h`:
  `zC` is coefficient-half invariant, so `bar(zC) = zC ≠ zC - h` whenever
  `h ≠ 0`.
* `zC_not_fibre_family` — consequently C is the parameter of **no** fibre
  rank.  Stated against functional equality (`∀ v`), because a *pointwise*
  solve for `N` at a single `q₀` always succeeds and is not a rank.

## Scope — what the bar law does and does not settle

**Does:** it *excludes* C.  C is coefficient-half invariant, so it violates
`bar(z) = z - h` by exactly `h`, at every `q` with `h ≠ 0`.  That exclusion
uses no experimental input at all, which is what makes it usable where a
match-the-number argument is forbidden (bean `qou-3qrv`).

**Does not:** single out D on its own.  The law is one equation, and
`bar_sub_of_bar_even` below shows its solution set is `zD +` (*any* bar-even
function) — the whole fibre family lies inside it, and so does more.  D is
pinned *within* that set by a separate, already-proved fact: it is the unique
normalised Markov trace on `H₃(q)` factoring through `TL₃` and faithful on it
(`QOU.BraidsAndKnots.MarkovTraceTLUniqueness`).

So the forcing argument for D is **two** independent steps, and this file
supplies only the first:

| step | excludes | proved in |
|---|---|---|
| bar-covariance of M3 | C (and every bar-even `z`) | here |
| TL₃ + faithfulness | every rank `N ≠ 2` | `MarkovTraceTLUniqueness` |

Neither step consults a measured value.  Nothing here claims a downstream
numeric value is correct.

Base ring: a general `Field R` per AGENTS §7c — the argument is purely
algebraic, needing only inverses.  No ordering, no `Real.sqrt`, no archimedean
hypothesis; those belong on the far side of the substrate wall.  `zC` is
parametrised by a square root `u` (with `q = u²`) rather than by `q`, because
C is not a rational function of `q` — which is itself the reason it lies
outside the family.

Companion compute:
`computations/markov_z_fibre_rank_bar_covariance_probe.py`
(witness `markov-z-fibre-rank-bar-covariance.witness.json`) and
`computations/markov_z_full_bar_condition_probe.py`
(witness `markov-z-full-bar-condition.witness.json`).
-/

namespace QOU.BraidKnot

variable {R : Type*} [Field R]

/-- The Markov stabilisation parameter at fibre rank `N`:
`zRank N q = q^(2N-1)·(q² - 1)/(q^(2N) - 1)`, equivalently `qᴺ/[N]_q`.

Written as `q^(2N)·(q² - 1) / (q·(q^(2N) - 1))` to avoid natural-number
subtraction in the exponent. -/
noncomputable def zRank (N : ℕ) (q : R) : R :=
  q ^ (2 * N) * (q ^ 2 - 1) / (q * (q ^ (2 * N) - 1))

/-- Convention D is rank `2`: `zRank 2 q = q³/(q² + 1)`.

The hypotheses are exactly non-degeneracy of the rank-2 parameter: `q ≠ 0`
and `q⁴ ≠ 1`, the latter split as `q² ≠ 1` and `q² ≠ -1`. -/
theorem zRank_two (q : R) (hq : q ≠ 0) (hm : q ^ 2 - 1 ≠ 0) (hp : q ^ 2 + 1 ≠ 0) :
    zRank 2 q = q ^ 3 / (q ^ 2 + 1) := by
  have h4 : q ^ (2 * 2) - 1 = (q ^ 2 - 1) * (q ^ 2 + 1) := by ring
  unfold zRank
  rw [h4]
  field_simp

/-- **Bar-covariance law.** Replacing `q` by `q⁻¹` rescales the rank-`N`
Markov parameter by `q^(-2N)`:

`zRank N q⁻¹ = zRank N q / q^(2N)`.

The whole family is bar-*covariant* of weight `q^(-2N)`; it is bar-invariant
only where `q^(2N) = 1`. -/
theorem zRank_bar (N : ℕ) (q : R) (hq : q ≠ 0) (hN : q ^ (2 * N) - 1 ≠ 0) :
    zRank N q⁻¹ = zRank N q / q ^ (2 * N) := by
  have hpow : q ^ (2 * N) ≠ 0 := pow_ne_zero _ hq
  have hN' : (1 : R) - q ^ (2 * N) ≠ 0 := fun h => hN (by linear_combination -h)
  have hinv : (q⁻¹) ^ (2 * N) = (q ^ (2 * N))⁻¹ := inv_pow q (2 * N)
  unfold zRank
  rw [hinv]
  field_simp
  ring

/-- Bar-invariance of a nonzero rank-`N` Markov parameter forces
`q^(2N) = 1`.

Contrapositive reading: at any `q` with `q^(2N) ≠ 1` — in particular any real
substrate `q₀ > 1` at any rank `N ≥ 1` — the rank-`N` Markov parameter is
**not** bar-invariant.  No fibre rank rescues bar-invariance. -/
theorem pow_two_mul_eq_one_of_zRank_bar_invariant
    (N : ℕ) (q : R) (hq : q ≠ 0) (hN : q ^ (2 * N) - 1 ≠ 0)
    (hz : zRank N q ≠ 0) (hbar : zRank N q⁻¹ = zRank N q) :
    q ^ (2 * N) = 1 := by
  have hpow : q ^ (2 * N) ≠ 0 := pow_ne_zero _ hq
  have h := zRank_bar N q hq hN
  rw [hbar] at h
  have key : zRank N q * q ^ (2 * N) = zRank N q := by
    conv_lhs => rw [h]
    exact div_mul_cancel₀ _ hpow
  have hfac : zRank N q * (q ^ (2 * N) - 1) = 0 := by linear_combination key
  rcases mul_eq_zero.mp hfac with h' | h'
  · exact absurd h' hz
  · linear_combination h'

/-- The quantum integer `[N]_q = (qᴺ - q⁻ᴺ)/(q - q⁻¹)`. -/
noncomputable def qInt (N : ℕ) (q : R) : R := (q ^ N - (q ^ N)⁻¹) / (q - q⁻¹)

/-- **`zRank` is the fibre quantum dimension.**  `zRank N q = qᴺ / [N]_q`.

This is the bridge to the Wenzl-bridge form used on the binding side: the
fractional-rank condition `X = Qᴺ` (with `Q = q²`, `X = qz/(1 - Q + qz)`) is
equivalent to `z·[N]_q = qᴺ`, i.e. to `z = zRank N q`.  So the two
descriptions of the family — the closed form above and "the Markov parameter
of fibre rank `N`" — are the same object, and `zC_not_fibre_family` below is
a statement about *that* family.

Recorded so that the exclusion of C from the family is a theorem rather than
a numerical inversion: solving `z_C = zRank N` pointwise at one `q₀` returns
`N ≈ 2.5995`, which is a number, not a rank. -/
theorem zRank_eq_qpow_div_qInt (N : ℕ) (q : R) (hq : q ≠ 0)
    (hN : q ^ (2 * N) - 1 ≠ 0) :
    zRank N q = q ^ N / qInt N q := by
  have hqN : q ^ N ≠ 0 := pow_ne_zero _ hq
  have hpow : q ^ (2 * N) ≠ 0 := pow_ne_zero _ hq
  have hsub : q ^ N - (q ^ N)⁻¹ ≠ 0 := by
    intro h
    apply hN
    have hmul : q ^ N * (q ^ N - (q ^ N)⁻¹) = q ^ (2 * N) - 1 := by
      field_simp
      ring
    rw [h, mul_zero] at hmul
    exact hmul.symm ▸ rfl
  unfold zRank qInt
  rw [div_div_eq_mul_div]
  rw [div_eq_div_iff (by simpa using mul_ne_zero hq hN) hsub]
  field_simp
  ring

/-! ### The full involution — `bar(z) = z - h` -/

/-- **The Hecke relation makes `σ - h` the inverse of `σ`.**  In any ring,
an element `s` with `s² = h·s + 1` and `h` commuting with `s` has `s - h` as
a two-sided inverse.

This is the whole source of the `z - h` in the bar-partner of Markov axiom
M3: applying the bar involution to `τ(x · σₙ) = z · τ(x)` inverts `σₙ`, and
`τ(x · σₙ⁻¹) = (z - h) · τ(x)` then follows from this identity — no further
hypothesis about the trace is used. -/
theorem hecke_inv_eq_sub {A : Type*} [Ring A] (s hh : A)
    (hcomm : hh * s = s * hh) (hrel : s * s = hh * s + 1) :
    s * (s - hh) = 1 ∧ (s - hh) * s = 1 := by
  constructor
  · have e : s * (s - hh) = s * s - s * hh := by noncomm_ring
    rw [e, hrel, hcomm]
    noncomm_ring
  · have e : (s - hh) * s = s * s - hh * s := by noncomm_ring
    rw [e, hrel]
    noncomm_ring

/-- **Full bar-covariance law of the Markov parameter.**

`zRank N q⁻¹ = zRank N q - (q - q⁻¹)` — for **every** rank `N`.

Unlike the coefficient-half law `zRank_bar`, this one has no `N`-dependent
weight: it is an identity of the entire fibre family.  So requiring the
Markov parameter to be bar-covariant does not compete with reading `z` as a
fibre rank; the two are the same condition, and no choice between them has to
be made. -/
theorem zRank_bar_sub (N : ℕ) (q : R) (hq : q ≠ 0) (hN : q ^ (2 * N) - 1 ≠ 0) :
    zRank N q⁻¹ = zRank N q - (q - q⁻¹) := by
  have hpow : q ^ (2 * N) ≠ 0 := pow_ne_zero _ hq
  rw [zRank_bar N q hq hN]
  unfold zRank
  field_simp
  ring

/-- **Convention D** — `z = q³/(q² + 1)`, the Jones / `SU_q(2)` value. -/
noncomputable def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- **Convention C** — `z = 1/(u + u⁻¹)` for a chosen square root `u` of `q`.

Parametrised by `u`, not `q`: C is not a rational function of `q`, and that
is exactly why it lies outside the fibre family (`zC_not_fibre_family`). -/
noncomputable def zC (u : R) : R := 1 / (u + u⁻¹)

/-- Convention D is the rank-2 member of the family. -/
theorem zD_eq_zRank_two (q : R) (hq : q ≠ 0) (hm : q ^ 2 - 1 ≠ 0) (hp : q ^ 2 + 1 ≠ 0) :
    zD q = zRank 2 q := (zRank_two q hq hm hp).symm

/-- **Convention D satisfies the full bar condition** `bar(z) = z - h`.

Both sides are `1/(q³ + q)`. -/
theorem zD_bar_sub (q : R) (hq : q ≠ 0) (hp : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ = zD q - (q - q⁻¹) := by
  unfold zD
  have hp' : (1 : R) + q ^ 2 ≠ 0 := fun h => hp (by linear_combination h)
  have h1 : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro h
    apply hp
    have e : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
    rw [e] at h
    exact (div_eq_zero_iff.mp h).resolve_right (pow_ne_zero 2 hq)
  field_simp
  ring

/-- **The bar law does not pin `z` on its own.**  If `g` is bar-even
(`g q⁻¹ = g q`) then `zD + g` satisfies `bar(z) = z - h` too, so the law's
solution set is `zD +` (bar-even functions) — a whole affine family, of which
the fibre family `zRank N` is only part.

Recorded to bound the claim: the law **excludes** C, it does not by itself
select D.  Selecting D within this set is what `MarkovTraceTLUniqueness`
does. -/
theorem bar_sub_of_bar_even (g : R → R) (q : R) (hq : q ≠ 0) (hp : q ^ 2 + 1 ≠ 0)
    (hg : g q⁻¹ = g q) :
    zD q⁻¹ + g q⁻¹ = (zD q + g q) - (q - q⁻¹) := by
  rw [hg, zD_bar_sub q hq hp]
  ring

/-- Convention C is invariant under the **coefficient half** alone. -/
theorem zC_bar (u : R) : zC u⁻¹ = zC u := by
  unfold zC
  rw [inv_inv, add_comm]

/-- **Convention C fails the full bar condition**, and fails it by exactly
`h`.  Since `bar(zC) = zC`, the condition `bar(z) = z - h` would force
`h = 0`; so C violates it at every `q` with `q² ≠ ±1`. -/
theorem zC_ne_bar_sub (u : R) (hh : u ^ 2 - (u ^ 2)⁻¹ ≠ 0) :
    zC u⁻¹ ≠ zC u - (u ^ 2 - (u ^ 2)⁻¹) := by
  rw [zC_bar u]
  intro hcon
  exact hh (by linear_combination hcon)

/-- **C is the Markov parameter of no fibre rank.**

Every rank-`N` parameter obeys `zRank_bar_sub`; `zC` obeys `zC_bar` instead.
The two are incompatible once `h ≠ 0`, so no `N` makes `zC` the rank-`N`
parameter.

Stated against *functional* equality (`∀ v`) deliberately: solving
`z_C = zRank N` for `N` pointwise at a single `q₀` always succeeds and
returns a `q`-dependent expression, which is a numerical inversion and not a
rank. -/
theorem zC_not_fibre_family (N : ℕ) (u : R) (hu : u ≠ 0)
    (hN : (u ^ 2) ^ (2 * N) - 1 ≠ 0)
    (hh : u ^ 2 - (u ^ 2)⁻¹ ≠ 0)
    (hfam : ∀ v : R, zC v = zRank N (v ^ 2)) :
    False := by
  have hq : (u ^ 2 : R) ≠ 0 := pow_ne_zero 2 hu
  have hbar := zRank_bar_sub N (u ^ 2) hq hN
  have h1 : zC u⁻¹ = zRank N ((u⁻¹ : R) ^ 2) := hfam u⁻¹
  have h3 : ((u⁻¹ : R)) ^ 2 = (u ^ 2)⁻¹ := inv_pow u 2
  rw [h3, hbar, ← hfam u] at h1
  rw [zC_bar u] at h1
  exact hh (by linear_combination h1)

end QOU.BraidKnot
