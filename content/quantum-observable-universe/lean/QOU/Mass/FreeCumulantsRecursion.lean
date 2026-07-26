/-
# Speicher moment–cumulant recursion — the third F3 (free-probability) brick

The first brick (`QOU/Mass/FreeCumulants.lean`) wrote the free moments
`m₀,…,m₄` as explicit non-crossing-partition polynomials in the free
cumulants `κ_k` and proved Speicher's first-block recursion for `n ≤ 4`
(`freeMoment{2,3,4}_recursion`). The second brick
(`QOU/Mass/NonCrossingPartitions.lean`) gave the `decide`-verified
count `|NC(n)| = C_n` for `n ≤ 4`. This brick advances the *recursion*
one and two orders further — to `n = 5` and `n = 6` — and records the
fully general closed recursion (the next brick) as precise prose.

## Speicher's first-block recursion

Condition a non-crossing partition `π ∈ NC(n)` on the block `B ∋ 1`
containing the first point. If `|B| = s`, its legs
`1 = p₁ < p₂ < … < p_s` cut the remaining `n − s` points into `s`
gaps — the open intervals `(p₁,p₂), …, (p_{s-1},p_s)` and the tail
`(p_s, n]` — and non-crossingness forces each gap to be partitioned
*independently* (a block of `π` may not straddle a leg of `B`). Summing
`κ_s` (the weight of `B`) against the product of the gaps' free moments,

$$
  m_n \;=\; \sum_{s=1}^{n} \kappa_s
            \!\!\sum_{\substack{i_1+\cdots+i_s = n-s \\ i_j \ge 0}}
            \; \prod_{j=1}^{s} m_{i_j},
$$

where the inner sum runs over the **weak compositions** of `n − s`
into `s` non-negative parts (one part per gap). Since `s ≥ 1` every
recursive index satisfies `i_j ≤ n − s ≤ n − 1 < n`, so the identity
determines the whole moment sequence from `m₀ = 1`.

The inner *gap sum* is `h_{s,N} := ∑_{i₁+…+i_s = N} ∏_j m_{i_j}`, the
`x^N`-coefficient of `M(x)^s` for the moment generating series
`M(x) = ∑_{k≥0} m_k x^k`. Its small values, used below (`m₀ = 1`):

| `h_{s,N}` | value |
|-----------|-------|
| `h_{1,N}` | `m_N` |
| `h_{2,3}` | `2 m₃ + 2 m₁ m₂` |
| `h_{2,4}` | `2 m₄ + 2 m₁ m₃ + m₂²` |
| `h_{3,2}` | `3 m₂ + 3 m₁²` |
| `h_{3,3}` | `3 m₃ + 6 m₁ m₂ + m₁³` |
| `h_{4,1}` | `4 m₁` |
| `h_{4,2}` | `4 m₂ + 6 m₁²` |
| `h_{5,0} = h_{6,0}` | `1` |
| `h_{5,1}` | `5 m₁` |

## The general recursion (documented next brick, not yet formalized)

The all-`n` statement is a single recursive definition

  `freeMomentRec κ n = ∑_{s=1}^{n} κ_s · (∑_{t ∈ antidiagonalTuple s (n-s)} ∏_{j} freeMomentRec κ (t j))`,

with `freeMomentRec κ 0 = 1`. The gap structure is exactly Mathlib's
`Finset.Nat.antidiagonalTuple s (n - s) : Finset (Fin s → ℕ)` — the
`s`-tuples of naturals summing to `n − s` — one entry `t j` per gap.
The cleanest Lean realization is a **structural** (List/Vector-memoized)
recursion on `n`: build `[m₀, …, m_n]` from `[m₀, …, m_{n-1}]`, reading
gap moments off the accumulator (so the sum contains no direct recursive
call and termination is immediate), then prove
`freeMomentRec κ k = freeMomentₖ κ` for `k ≤ 6` against the explicit
polynomials below. That definition + its agreement proof is the next
brick; here we ground the recursion itself two orders past the merged
`n ≤ 4`.

## Explicit free moments `m₅, m₆`

Grouped by block-type, the coefficient of `∏ κ_{|V|}` is the number of
non-crossing partitions of `[n]` with that block structure; the
coefficients sum to `C₅ = 42` and `C₆ = 132` (verified at the all-ones
evaluation below, extending
`FreeCumulants.freeMoment_eval_one_eq_catalanCount`).

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` throughout — every statement is a
polynomial identity in the formal cumulants `κ_k` (or a `ℕ`-valued
count). No ordering, no `Real`, no archimedean construct, no substrate
`q₀`. Reuses the merged `freeMoment₀,…,freeMoment₄`.
-/
import QOU.Mass.FreeCumulants
import Mathlib.Data.Nat.Choose.Central
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.Mass

variable {R : Type*} [CommRing R]

/-! ## Explicit order-5 and order-6 free moments

`freeMoment5` / `freeMoment6` are the non-crossing-partition polynomials
`∑_{π ∈ NC(n)} ∏_{V ∈ π} κ_{|V|}` for `n = 5, 6`, grouped by block-type
(the `κ`-monomial). The block-type multiplicities are the number of
non-crossing partitions of the given shape; they total `C₅ = 42` and
`C₆ = 132`. -/

/-- `m₅ = κ₅ + 5κ₁κ₄ + 5κ₂κ₃ + 10κ₁²κ₃ + 10κ₁κ₂² + 10κ₁³κ₂ + κ₁⁵`.
The block-type multiplicities `1,5,5,10,10,10,1` are the non-crossing
partition counts of shapes `{5}`, `{4,1}`, `{3,2}`, `{3,1,1}`, `{2,2,1}`,
`{2,1,1,1}`, `{1,1,1,1,1}`; they sum to `C₅ = 42`. -/
def freeMoment5 (κ : ℕ → R) : R :=
  κ 5 + 5 * κ 1 * κ 4 + 5 * κ 2 * κ 3 + 10 * κ 1 ^ 2 * κ 3
    + 10 * κ 1 * κ 2 ^ 2 + 10 * κ 1 ^ 3 * κ 2 + κ 1 ^ 5

/-- `m₆ = κ₆ + 6κ₁κ₅ + 6κ₂κ₄ + 3κ₃² + 15κ₁²κ₄ + 30κ₁κ₂κ₃ + 5κ₂³
+ 20κ₁³κ₃ + 30κ₁²κ₂² + 15κ₁⁴κ₂ + κ₁⁶`. The block-type multiplicities
`1,6,6,3,15,30,5,20,30,15,1` are the non-crossing partition counts of the
eleven shapes of `6`; they sum to `C₆ = 132`. -/
def freeMoment6 (κ : ℕ → R) : R :=
  κ 6 + 6 * κ 1 * κ 5 + 6 * κ 2 * κ 4 + 3 * κ 3 ^ 2 + 15 * κ 1 ^ 2 * κ 4
    + 30 * κ 1 * κ 2 * κ 3 + 5 * κ 2 ^ 3 + 20 * κ 1 ^ 3 * κ 3
    + 30 * κ 1 ^ 2 * κ 2 ^ 2 + 15 * κ 1 ^ 4 * κ 2 + κ 1 ^ 6

/-! ## Speicher's first-block recursion at `n = 5, 6`

Each inner factor is the gap sum `h_{s,n-s} = ∑_{i₁+…+i_s = n-s} ∏_j m_{i_j}`
of the table in the module docstring, written in the merged free moments
`freeMoment₀,…,freeMoment₄` (and `freeMoment5` for `n = 6`). Each is a
`ring` identity — the polynomial content of the non-crossing first-block
decomposition. -/

/-- `m₅ = κ₁·m₄ + κ₂·(2m₃ + 2m₁m₂) + κ₃·(3m₂ + 3m₁²) + κ₄·(4m₁) + κ₅·m₀`.
The first-block recursion of `FreeCumulants.freeMoment{2,3,4}_recursion`
extended to order 5: `h_{2,3} = 2m₃+2m₁m₂`, `h_{3,2} = 3m₂+3m₁²`,
`h_{4,1} = 4m₁`, `h_{5,0} = 1`. -/
theorem freeMoment5_recursion (κ : ℕ → R) :
    freeMoment5 κ
      = κ 1 * freeMoment4 κ
        + κ 2 * (2 * freeMoment3 κ + 2 * freeMoment1 κ * freeMoment2 κ)
        + κ 3 * (3 * freeMoment2 κ + 3 * freeMoment1 κ ^ 2)
        + κ 4 * (4 * freeMoment1 κ)
        + κ 5 * freeMoment0 κ := by
  simp only [freeMoment5, freeMoment4, freeMoment3, freeMoment2, freeMoment1,
    freeMoment0]
  ring

/-- `m₆ = κ₁·m₅ + κ₂·(2m₄ + 2m₁m₃ + m₂²) + κ₃·(3m₃ + 6m₁m₂ + m₁³)
+ κ₄·(4m₂ + 6m₁²) + κ₅·(5m₁) + κ₆·m₀`. The order-6 first-block recursion:
`h_{2,4} = 2m₄+2m₁m₃+m₂²`, `h_{3,3} = 3m₃+6m₁m₂+m₁³`, `h_{4,2} = 4m₂+6m₁²`,
`h_{5,1} = 5m₁`, `h_{6,0} = 1`. -/
theorem freeMoment6_recursion (κ : ℕ → R) :
    freeMoment6 κ
      = κ 1 * freeMoment5 κ
        + κ 2 * (2 * freeMoment4 κ + 2 * freeMoment1 κ * freeMoment3 κ
            + freeMoment2 κ ^ 2)
        + κ 3 * (3 * freeMoment3 κ + 6 * freeMoment1 κ * freeMoment2 κ
            + freeMoment1 κ ^ 3)
        + κ 4 * (4 * freeMoment2 κ + 6 * freeMoment1 κ ^ 2)
        + κ 5 * (5 * freeMoment1 κ)
        + κ 6 * freeMoment0 κ := by
  simp only [freeMoment6, freeMoment5, freeMoment4, freeMoment3, freeMoment2,
    freeMoment1, freeMoment0]
  ring

/-! ## Catalan bridge at orders 5 and 6

At all cumulants `= 1` each non-crossing partition contributes `1`, so
`freeMomentₙ(1,1,…) = |NC(n)| = C_n`. This extends
`FreeCumulants.freeMoment_eval_one_eq_catalanCount` (`n ≤ 4`) to
`C₅ = 42` and `C₆ = 132`, expressed via Mathlib's `Nat.centralBinom`
(`C_n = centralBinom n / (n+1) = Nat.catalan n`). -/

/-- The Catalan values `C₅ = 42, C₆ = 132`, via Mathlib's
`Nat.centralBinom` (`C_n = centralBinom n / (n+1)`). -/
theorem catalanCount_values_56 :
    Nat.centralBinom 5 / 6 = 42 ∧ Nat.centralBinom 6 / 7 = 132 := by
  refine ⟨?_, ?_⟩ <;> norm_num [Nat.centralBinom, Nat.choose]

/-- **NC-count bridge, orders 5 and 6.** The free moments at all
cumulants `= 1` are the Catalan numbers `C₅ = 42`, `C₆ = 132`: the sums
of the block-type multiplicities of `freeMoment5` / `freeMoment6` equal
`|NC(5)|` / `|NC(6)|`. -/
theorem freeMoment56_eval_one_eq_catalanCount :
    freeMoment5 (fun _ => (1 : R)) = ((Nat.centralBinom 5 / 6 : ℕ) : R)
      ∧ freeMoment6 (fun _ => (1 : R)) = ((Nat.centralBinom 6 / 7 : ℕ) : R) := by
  obtain ⟨h5, h6⟩ := catalanCount_values_56
  refine ⟨?_, ?_⟩
  · rw [h5]; simp only [freeMoment5]; norm_num
  · rw [h6]; simp only [freeMoment6]; norm_num

end QOU.Mass
