import Mathlib.Tactic

/-!
# C1 at `∞` — ramification, and the two leading blocks

The `W2` `∞`-side of the `c₃` investigation. The `q`-difference operator is

    L₁ = (q²x − 1)·σ² − (q−1)·σ − (q−1)        (C1, RSZ route-A)

and the question is the Stokes data of its solutions at `∞`.

## Why ramification is forced, not chosen

At `∞` the valuation is `v_∞(a) = −deg(a)`, so the three coefficients sit at

    (0, 0),  (1, 0),  (2, −1).

The middle point lies *strictly above* the chord `(0,0)–(2,−1)`
(`middle_strictly_above_chord`), so it is not a vertex: the Newton polygon is
the **single edge** `(0,0)–(2,−1)` of slope `−1/2`. A non-integral slope makes
the companion matrix nilpotent at `∞`, and one cannot read a leading block off
a nilpotent limit. That nilpotency is not an obstacle to route around — it *is*
what a non-integral slope looks like in the companion frame.

RSZ (Astérisque 355 §3.3) prescribes the fix: a slope with denominator `d` is
resolved by ramifying with index `d`. Here `d = 2`, via `x = z²`, `q = p²`,
`τF(z) = F(pz)`. After it the hull is `(0,0), (1,0), (2,−2)`, slope `−1`,
**integral** (`ramified_slope_is_integral`), and the leading data is readable.

## CORRECTION 2026-08-07 — the edge polynomial carries a theta twist

An earlier version of this file stated the edge polynomial as `p⁴T² − p² + 1`,
with roots `±√(q−1)/q`, and called those roots the leading blocks. **That was
the differential-equation convention applied to a `q`-difference operator, and
it is wrong.**

The canonical solutions here are *theta-normalised*: `y = θ_p(z/T)⁻¹ h(z)`,
with `θ_p(pw) = w·θ_p(w)`. Iterating that gives

    θ_p(pⁱ w) = p^{i(i−1)/2} · wⁱ · θ_p(w)

a **quadratic** factor in `i`. So the `aᵢ(z)τⁱ` term contributes
`Aᵢ · p^{−i(i−1)/2} · Tⁱ`, and the edge polynomial is

    Σᵢ Aᵢ · p^{−i(i−1)/2} · Tⁱ = 0

With the twist it *is* the indicial equation of the theta ansatz. Without it
the `i = 2` term was too large by `p`, moving the roots by `q^{1/4}`:

| | edge polynomial | root |
|---|---|---|
| untwisted (old, wrong) | `p⁴T² − p² + 1` | `±√(q−1)/q` |
| twisted (correct) | `p³T² − p² + 1` | `±√(q−1)/q^{3/4}` |

This is not a matter of taste between conventions. The untwisted root
**provably fails** the indicial equation — numerically `−5.6e-3`, not roundoff
(`computations/qbeta/c3_w2_c1_theta_canonical.py`, which also builds both
canonical solutions explicitly and verifies them by substitution to `~1e-62`).
`untwisted_forces_trivial_p` below is the algebraic form of that: the two roots
agree **only** at `p = 1`, so the error is invisible exactly in the classical
limit and nowhere else.

The arithmetic that the old version proved — that `p⁴T² − p² + 1` has roots
`±√(q−1)/q` — was *true about that polynomial*. What was wrong was calling that
polynomial the edge polynomial, and its roots the blocks that index the Stokes
sectors. Same failure mode as bean `qou-64jx`: an object computed correctly,
then given a name whose meaning it does not have.

## Scope — what is NOT proved here

This is the leading **exponential** data that *indexes* the two Stokes sectors.
It is **not** the two Stokes multipliers, which are the connection data
*between* sectors and need the connection matrix of the theta-normalised
solutions at `0` and `∞`. Prerequisite, not closure. Nothing is wired to
production.

The base-ring split follows §7c: the edge algebra is stated over a generic
`CommRing`/`Field`, and only the square-root extraction descends to `ℝ`.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_ramification_leading_blocks.py
-- Ref: [manuscript] computations/qbeta/c3_w2_c1_theta_canonical.py
-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
-/

namespace QOU.QBeta.C1Ramified

/-! ## Part 1 — the Newton polygon at `∞`

Only the three `∞`-valuations enter, so they are recorded as plain integers.
Doubling the chord test keeps everything in `ℤ`: for points `(0,y₀)`, `(1,y₁)`,
`(2,y₂)`, the middle point is strictly above the chord iff `2y₁ > y₀ + y₂`. -/

/-- `v_∞` of the coefficients of `L₁ = (q²x−1)σ² − (q−1)σ − (q−1)`, indexed by
the power of `σ`. -/
def vInf : Fin 3 → ℤ
  | 0 => 0
  | 1 => 0
  | 2 => -1

/-- `v_∞` after the index-`2` ramification `x = z²`: only `a₂` moves, its
degree in `z` doubling from `1` to `2`. -/
def vInfRamified : Fin 3 → ℤ
  | 0 => 0
  | 1 => 0
  | 2 => -2

/-- **The middle point is not a vertex.** `2·v₁ > v₀ + v₂`, so `(1, 0)` lies
strictly above the chord and the lower hull is the single edge. -/
theorem middle_strictly_above_chord :
    2 * vInf 1 > vInf 0 + vInf 2 := by decide

/-- The same after ramification — the hull is still a single edge. -/
theorem middle_strictly_above_chord_ramified :
    2 * vInfRamified 1 > vInfRamified 0 + vInfRamified 2 := by decide

/-- **The unramified slope is `−1/2`.** Non-integral: this is the obstruction. -/
theorem unramified_slope :
    ((vInf 2 - vInf 0 : ℤ) : ℚ) / 2 = -1/2 := by norm_num [vInf]

/-- **The unramified slope is not an integer** — the precise statement of the
obstruction that forces ramification. -/
theorem unramified_slope_not_integral :
    ¬ ∃ n : ℤ, ((vInf 2 - vInf 0 : ℤ) : ℚ) / 2 = (n : ℚ) := by
  rintro ⟨n, hn⟩
  rw [unramified_slope] at hn
  have h2 : (2 : ℚ) * (n : ℚ) = -1 := by field_simp at hn; linarith
  have : (2 * n : ℤ) = -1 := by exact_mod_cast h2
  omega

/-- **Ramification integralises the slope**: index `2` sends `−1/2` to `−1`. -/
theorem ramified_slope_is_integral :
    ((vInfRamified 2 - vInfRamified 0 : ℤ) : ℚ) / 2 = (-1 : ℤ) := by
  norm_num [vInfRamified]

/-- The ramification index is exactly the denominator of the original slope. -/
theorem ramification_index_eq_slope_denominator :
    ((-1 : ℚ)/2).den = 2 := by norm_num

/-! ## Part 2 — the theta twist

`θ_p(pw) = w·θ_p(w)` iterated gives `θ_p(pⁱw) = p^{i(i−1)/2} wⁱ θ_p(w)`. The
exponent `i(i−1)/2` is the triangular number, and it is what the `τⁱ` term of
the edge polynomial must be divided by. Only `i ≤ 2` is needed for a rank-2
operator, so the concrete values are recorded rather than the general
recursion. -/

/-- The theta-twist exponent `i(i−1)/2` in `θ_p(pⁱw) = p^{i(i−1)/2} wⁱ θ_p(w)`. -/
def twistExp (i : ℕ) : ℕ := i * (i - 1) / 2

@[simp] theorem twistExp_zero : twistExp 0 = 0 := rfl
@[simp] theorem twistExp_one : twistExp 1 = 0 := rfl
@[simp] theorem twistExp_two : twistExp 2 = 1 := rfl
@[simp] theorem twistExp_three : twistExp 3 = 3 := rfl

/-- **The twist is trivial below `i = 2`.** This is why the error was invisible
in the two lower-order terms and bit only at `τ²`. -/
theorem twistExp_eq_zero_of_le_one {i : ℕ} (h : i ≤ 1) : twistExp i = 0 := by
  interval_cases i <;> rfl

/-! ## Part 3 — the (twisted) edge polynomial

Generic algebra: no ordering, no square roots. -/

/-- **The edge equation.** With the theta twist, the `i = 2` coefficient `p⁴`
becomes `p⁴·p^{−1} = p³`, so the edge polynomial is `p³T² − p² + 1` and the
edge equation is `p³T² = p² − 1`. -/
theorem edge_eq_iff {R : Type*} [CommRing R] (p T : R) :
    p ^ 3 * T ^ 2 - p ^ 2 + 1 = 0 ↔ p ^ 3 * T ^ 2 = p ^ 2 - 1 := by
  constructor <;> intro h <;> linear_combination h

/-- **The untwisted root is not merely a different convention — it is wrong
except in the classical limit.**

If some `S ≠ 0` satisfied *both* the untwisted edge equation `p⁴S² = p²−1` and
the correct one `p³S² = p²−1`, then `p = 1`. So the two disagree at every
`p ≠ 1`, and the old answer cannot be recovered by renaming. -/
theorem untwisted_forces_trivial_p {K : Type*} [Field K] (p S : K)
    (hp : p ≠ 0) (hS : S ≠ 0)
    (huntwisted : p ^ 4 * S ^ 2 = p ^ 2 - 1)
    (htwisted : p ^ 3 * S ^ 2 = p ^ 2 - 1) : p = 1 := by
  have hdiff : p ^ 3 * S ^ 2 * (p - 1) = 0 := by linear_combination huntwisted - htwisted
  have h3 : p ^ 3 ≠ 0 := pow_ne_zero _ hp
  have hS2 : S ^ 2 ≠ 0 := pow_ne_zero _ hS
  rcases mul_eq_zero.mp hdiff with h | h
  · exact absurd h (mul_ne_zero h3 hS2)
  · exact sub_eq_zero.mp h

/-- The two roots of the edge polynomial **sum to zero** — it is even in `T`. -/
theorem blocks_sum_zero {R : Type*} [CommRing R] (B : R) : B + -B = 0 := by ring

/-- The two roots **multiply to** `−(p²−1)/p³`, division-free. -/
theorem blocks_prod {R : Type*} [CommRing R] (p B : R)
    (h : p ^ 3 * B ^ 2 = p ^ 2 - 1) :
    p ^ 3 * (B * -B) = -(p ^ 2 - 1) := by linear_combination -h

/-! ## Part 4 — solving over `ℝ`

The square root is the one archimedean step (§7c). -/

/-- **The leading blocks.** For `p > 0` with `p² ≥ 1`, the solutions of the
twisted edge equation are `B₁,₂ = ±√((p²−1)/p³)`. In the unramified variable
`q = p²` that is `±√(q−1)/q^{3/4}` — **not** `±√(q−1)/q`. -/
theorem leading_blocks (p T : ℝ) (hp : 0 < p) (hp1 : 1 ≤ p ^ 2) :
    p ^ 3 * T ^ 2 = p ^ 2 - 1 ↔
      T = Real.sqrt ((p ^ 2 - 1) / p ^ 3) ∨ T = -Real.sqrt ((p ^ 2 - 1) / p ^ 3) := by
  have hp3 : (0 : ℝ) < p ^ 3 := by positivity
  have hnn : (0 : ℝ) ≤ (p ^ 2 - 1) / p ^ 3 := by
    apply div_nonneg (by linarith) hp3.le
  constructor
  · intro h
    have hT2 : T ^ 2 = (p ^ 2 - 1) / p ^ 3 := by
      field_simp
      linarith [h]
    have habs : |T| = Real.sqrt ((p ^ 2 - 1) / p ^ 3) := by
      rw [← Real.sqrt_sq_eq_abs, hT2]
    rcases (abs_eq (Real.sqrt_nonneg _)).mp habs with h' | h'
    · exact Or.inl h'
    · exact Or.inr h'
  · intro h
    have hT2 : T ^ 2 = (p ^ 2 - 1) / p ^ 3 := by
      rcases h with h | h <;> subst h <;>
        [skip; rw [neg_pow, neg_one_pow_two, one_mul]] <;>
        rw [Real.sq_sqrt hnn]
    rw [hT2]
    field_simp

/-- **The two sectors are distinct exactly when `p ≠ 1`.** At `p = 1` the blocks
collide — the classical, non-`q`-deformed limit, which is also the only place
the untwisted convention would have agreed. -/
theorem blocks_distinct_iff (p : ℝ) (hp : 0 < p) (hp1 : 1 ≤ p ^ 2) :
    Real.sqrt ((p ^ 2 - 1) / p ^ 3) ≠ -Real.sqrt ((p ^ 2 - 1) / p ^ 3) ↔ p ≠ 1 := by
  have hp3 : (0 : ℝ) < p ^ 3 := by positivity
  have hnn : (0 : ℝ) ≤ (p ^ 2 - 1) / p ^ 3 := div_nonneg (by linarith) hp3.le
  constructor
  · intro h hq
    apply h
    subst hq
    norm_num
  · intro hq hcontra
    have h0 : Real.sqrt ((p ^ 2 - 1) / p ^ 3) = 0 := by linarith
    have hle : (p ^ 2 - 1) / p ^ 3 ≤ 0 := Real.sqrt_eq_zero'.mp h0
    have : p ^ 2 - 1 ≤ 0 := by
      by_contra hc
      push_neg at hc
      exact absurd hle (not_le.mpr (by positivity))
    have hp2 : p ^ 2 = 1 := by linarith
    have : (p - 1) * (p + 1) = 0 := by linarith [hp2]
    rcases mul_eq_zero.mp this with h | h
    · exact hq (by linarith [sub_eq_zero.mp h])
    · linarith

/-- **The Stokes space is two-dimensional** at `p ≠ 1`: exactly two roots, hence
exactly two sectors. -/
theorem stokes_sector_count (p : ℝ) (hp : 0 < p) (hp1 : 1 < p) :
    ({Real.sqrt ((p ^ 2 - 1) / p ^ 3),
      -Real.sqrt ((p ^ 2 - 1) / p ^ 3)} : Finset ℝ).card = 2 := by
  have hp2 : (1 : ℝ) ≤ p ^ 2 := by nlinarith
  rw [Finset.card_insert_of_notMem, Finset.card_singleton]
  simp only [Finset.mem_singleton]
  exact (blocks_distinct_iff p hp hp2).mpr (by linarith)

end QOU.QBeta.C1Ramified
