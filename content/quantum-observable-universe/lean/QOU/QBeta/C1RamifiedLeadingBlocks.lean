import Mathlib.Tactic

/-!
# C1 at `∞` — ramification, and the two leading blocks `B = ±√(q−1)/q`

The `W2` `∞`-side of the `c₃` investigation. The `q`-difference operator is

    L₁ = (q²x − 1)·σ² − (q−1)·σ − (q−1)        (C1, RSZ route-A)

and the question is the Stokes data of its solutions at `∞`.

## Why ramification is forced, not chosen

At `∞` the valuation is `v_∞(a) = −deg(a)`, so the three coefficients sit at

    (0, 0),  (1, 0),  (2, −1).

The middle point lies *strictly above* the chord `(0,0)–(2,−1)`
(`middle_strictly_above_chord`), so it is not a vertex: the Newton polygon is
the **single edge** `(0,0)–(2,−1)` of slope `−1/2`. A non-integral slope makes
the companion matrix nilpotent at `∞` (`A(∞) = ![![0,1],![0,0]]`, `det = 0`),
and one cannot read a leading block off a nilpotent limit. That nilpotency is
not an obstacle to route around — it *is* what a non-integral slope looks like
in the companion frame.

RSZ (Astérisque 355 §3.3) prescribes the fix: a slope with denominator `d` is
resolved by ramifying with index `d`. Here `d = 2`, via `x = z²`, `q = p²`.
The `q^{1/2}` that appears is the ramification, and it is the source of the
"square roots". After it the hull is `(0,0), (1,0), (2,−2)`, slope `−1`,
**integral** (`ramified_slope_is_integral`), and the leading data is readable.

## What the edge polynomial gives

The integral edge carries the polynomial `p⁴T² − p² + 1`, whose roots are the
two leading blocks. The whole content is the observation that
`p⁴T² = (p²T)²`, so over *any* commutative ring the edge equation is

    (p²T)² = p² − 1                                       (`edge_eq_iff`)

i.e. in the unramified variable `q = p²`, `(qT)² = q − 1`. Over `ℝ` with
`q ≥ 1` this solves to

    B₁,₂ = ±√(q−1)/q                                      (`leading_blocks_q`)

and the two sectors are distinct exactly when `q ≠ 1` (`blocks_distinct_iff`).

## Scope — what is NOT proved here

This is the leading **exponential** data that *indexes* the two Stokes
sectors. It is **not** the two Stokes multipliers, which are the connection
data *between* sectors and need the `q`-Borel / theta-kernel resummation at
level `d = 2`. Prerequisite, not closure. Nothing is wired to production.

Two numerical readings that *did* attempt to shortcut past building the
canonical solutions (a Prony blend, and a direct `C` extraction) both returned
negatives: the sector data is not visible in `bₘ` asymptotics. Those are
recorded as scope-(a) negatives — "these estimators, alone, do not see it" —
not as structural exclusions. The theta-normalised canonical solutions remain
the genuine untried route (bean `qou-wgnx`).

The base-ring split follows §7c: the edge algebra is stated over a generic
`CommRing`, and only the square-root extraction descends to `ℝ`.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_ramification_leading_blocks.py
-- Ref: [rsz2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
-/

namespace QOU.QBeta.C1Ramified

/-! ## Part 1 — the Newton polygon at `∞`

Only the three `∞`-valuations enter, so they are recorded as plain integers.
Doubling the chord test keeps everything in `ℤ`: for points `(0,y₀)`, `(1,y₁)`,
`(2,y₂)`, the middle point is strictly above the chord iff `2y₁ > y₀ + y₂`. -/

/-- `v_∞` of the coefficients of `L₁ = (q²x−1)σ² − (q−1)σ − (q−1)`, indexed by
the power of `σ`. `a₀ = a₁ = −(q−1)` have degree `0`; `a₂ = q²x − 1` has
degree `1`, hence `v_∞ = −1`. -/
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
strictly above the chord `(0,0)–(2,−1)` and the lower hull is the single edge.
This is what makes the polygon one edge rather than two. -/
theorem middle_strictly_above_chord :
    2 * vInf 1 > vInf 0 + vInf 2 := by decide

/-- The same after ramification — the hull is still a single edge. -/
theorem middle_strictly_above_chord_ramified :
    2 * vInfRamified 1 > vInfRamified 0 + vInfRamified 2 := by decide

/-- **The unramified slope is `−1/2`**, stated over `ℚ` as
`(v₂ − v₀)/(2 − 0)`. Non-integral: this is the whole obstruction. -/
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

/-- **Ramification integralises the slope**: index `2` sends `−1/2` to `−1`.
This is the RSZ step, and it is why the leading blocks become readable. -/
theorem ramified_slope_is_integral :
    ((vInfRamified 2 - vInfRamified 0 : ℤ) : ℚ) / 2 = (-1 : ℤ) := by
  norm_num [vInfRamified]

/-- The ramification index is exactly the denominator of the original slope. -/
theorem ramification_index_eq_slope_denominator :
    ((-1 : ℚ)/2).den = 2 := by norm_num

/-! ## Part 2 — the edge polynomial

The integral edge of the ramified polygon runs from `(0,0)` to `(2,−2)`; the
middle coefficient is off the edge and does not contribute. The edge
polynomial is therefore built from `a₂`'s leading coefficient `p⁴` and `a₀`'s
value `−(p²−1)`, giving `p⁴T² − p² + 1`.

Everything here is generic (`CommRing`) — no ordering, no square roots. -/

/-- **The edge equation, in its useful form.** `p⁴T² − p² + 1 = 0` is exactly
`(p²T)² = p² − 1`. This single rearrangement is the whole algebraic content:
the "square roots" of the leading blocks are the square roots of `p² − 1`,
divided by `p²`. -/
theorem edge_eq_iff {R : Type*} [CommRing R] (p T : R) :
    p ^ 4 * T ^ 2 - p ^ 2 + 1 = 0 ↔ (p ^ 2 * T) ^ 2 = p ^ 2 - 1 := by
  constructor <;> intro h <;> linear_combination h

/-- In the **unramified** variable `q = p²` the edge equation reads
`(qT)² = q − 1`. -/
theorem edge_eq_iff_q {R : Type*} [CommRing R] (q T : R) :
    q ^ 2 * T ^ 2 - q + 1 = 0 ↔ (q * T) ^ 2 = q - 1 := by
  constructor <;> intro h <;> linear_combination h

/-- The two roots of the edge polynomial **sum to zero** — the edge polynomial
is even in `T`, so the two sectors are symmetric about the origin. -/
theorem blocks_sum_zero {R : Type*} [CommRing R] (B : R) : B + -B = 0 := by ring

/-- The two roots **multiply to** `−(q−1)/q²`, read off the edge polynomial's
constant-to-leading ratio. Stated multiplicatively to stay division-free. -/
theorem blocks_prod {R : Type*} [CommRing R] (q B : R) (h : (q * B) ^ 2 = q - 1) :
    q ^ 2 * (B * -B) = -(q - 1) := by linear_combination -h

/-! ## Part 3 — solving over `ℝ`

The square root is the one archimedean step, so this is where `ℝ` enters
(§7c). `q ≥ 1` is exactly the condition for the blocks to be real. -/

/-- **The leading blocks.** For `q ≥ 1` and `q ≠ 0`, the solutions of the edge
equation are `B₁,₂ = ±√(q−1)/q`. -/
theorem leading_blocks_q (q T : ℝ) (hq1 : 1 ≤ q) (hq0 : q ≠ 0) :
    (q * T) ^ 2 = q - 1 ↔
      T = Real.sqrt (q - 1) / q ∨ T = -(Real.sqrt (q - 1) / q) := by
  have hnn : (0 : ℝ) ≤ q - 1 := by linarith
  constructor
  · intro h
    have habs : |q * T| = Real.sqrt (q - 1) := by
      rw [← Real.sqrt_sq_eq_abs, h]
    rw [abs_eq (Real.sqrt_nonneg _)] at habs
    rcases habs with h' | h'
    · left; field_simp; linarith [h']
    · right; field_simp; linarith [h']
  · intro h
    rcases h with h | h <;> subst h <;> field_simp <;>
      rw [Real.sq_sqrt hnn]

/-- Both blocks do solve the edge equation — the forward check, kept separate
so it can be cited without the `iff`. -/
theorem leading_block_pos_is_root (q : ℝ) (hq1 : 1 ≤ q) (hq0 : q ≠ 0) :
    (q * (Real.sqrt (q - 1) / q)) ^ 2 = q - 1 := by
  have hnn : (0 : ℝ) ≤ q - 1 := by linarith
  field_simp
  rw [Real.sq_sqrt hnn]

/-- **The two sectors are distinct exactly when `q ≠ 1`.** At `q = 1` the two
leading blocks collide and the two-sector picture degenerates — which is the
classical (non-`q`-deformed) limit. -/
theorem blocks_distinct_iff (q : ℝ) (hq1 : 1 ≤ q) (hq0 : q ≠ 0) :
    Real.sqrt (q - 1) / q ≠ -(Real.sqrt (q - 1) / q) ↔ q ≠ 1 := by
  have hnn : (0 : ℝ) ≤ q - 1 := by linarith
  constructor
  · intro h hq
    apply h
    subst hq
    simp
  · intro hq hcontra
    have h0 : Real.sqrt (q - 1) / q = 0 := by linarith
    have hs : Real.sqrt (q - 1) = 0 := by
      rcases div_eq_zero_iff.mp h0 with h | h
      · exact h
      · exact absurd h hq0
    have : q - 1 ≤ 0 := Real.sqrt_eq_zero'.mp hs
    exact hq (by linarith)

/-- **The Stokes space is two-dimensional** at `q ≠ 1`: the edge polynomial has
exactly two distinct roots, so exactly two sectors. Recorded as the cardinality
of the root set. -/
theorem stokes_sector_count (q : ℝ) (hq1 : 1 < q) :
    ({Real.sqrt (q - 1) / q, -(Real.sqrt (q - 1) / q)} : Finset ℝ).card = 2 := by
  have hq0 : q ≠ 0 := by linarith
  rw [Finset.card_insert_of_notMem, Finset.card_singleton]
  simp only [Finset.mem_singleton]
  exact (blocks_distinct_iff q (le_of_lt hq1) hq0).mpr (by linarith)

end QOU.QBeta.C1Ramified
