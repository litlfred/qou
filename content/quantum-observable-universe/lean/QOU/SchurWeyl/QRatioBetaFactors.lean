import QOU.SchurWeyl.SchurPrincipalBetaForm

/-!
# QOU.SchurWeyl.QRatioBetaFactors — the `q`-ratio factor at a β-pair

`schurPrincipal_mul_const` reduces branching to comparing `P(β') / P(β)` against the `q`-ratio,
where `P(β) = ∏_{i<j<r}(1 − Q^{β_i−β_j})` and `β' = β + e_a`.  Only pairs involving `a` differ, so
the comparison is per-pair, and this file does those two cases.

| | |
|---|---|
| `betaR_addCell` | `β_i(μ + □ at row `a`) = β_i(μ) + [i = a]` |
| `qratio_factor_lower` | pairs `j > a` — an **exact** match, no leftover factor |
| `qratio_factor_upper` | pairs `j < a` — the same match, times one `Q` |

Both are the same cancellation seen from the two sides: writing `x_i = Q^{β_i}`, divide numerator and
denominator by whichever of `Q^{β_a}`, `Q^{β_j}` is the smaller power.  The asymmetry is entirely in
*which* is smaller, and it is what produces the `Q^{#\{j < a\}} = Q^a` that `nPart_addCell` supplies
from the other side.

**No non-vanishing hypothesis.**  Both statements are equalities of quotients, and at a root of unity
where a denominator vanishes both sides are `_/0 = 0`.  The `Q ≠ 0` hypothesis is only needed to
cancel the common power.

## Base ring (§7c)

Generic `[Field F]` — quotients.  No ordering, no `ℝ`.

LaTeX label: `lem:qratio-beta-factors`
-/

namespace QOU.SchurWeyl

open YoungDiagram QOU.Mathlib QOU.Mathlib.SYTBeta

/-- **Adding a box at row `a` raises exactly one β-number.** -/
theorem betaR_addCell {r : ℕ} {μ : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell μ s) (i : ℕ) :
    betaR r (addCell μ s hs) i = betaR r μ i + (if i = s.1 then 1 else 0) := by
  rw [betaR, betaR, rowLen_addCell hs i]
  omega

variable {F : Type*} [Field F]

/-- **The `q`-ratio factor at a pair below `a`** (`j > a`, so `β_j ≤ β_a`).

`(Q·Q^{β_a} − Q^{β_j})/(Q^{β_a} − Q^{β_j}) = (1 − Q^{β_a+1−β_j})/(1 − Q^{β_a−β_j})`

— the right-hand side is exactly the `P(β')`-factor over the `P(β)`-factor, with **no** leftover
power of `Q`. -/
theorem qratio_factor_lower (Q : F) (hQ : Q ≠ 0) (b c : ℕ) (h : c ≤ b) :
    (Q * Q ^ b - Q ^ c) / (Q ^ b - Q ^ c)
      = (1 - Q ^ (b + 1 - c)) / (1 - Q ^ (b - c)) := by
  have hQc : (Q : F) ^ c ≠ 0 := pow_ne_zero _ hQ
  have h1 : (Q : F) ^ b = Q ^ c * Q ^ (b - c) := by
    rw [← pow_add]; congr 1; omega
  have h2 : Q * (Q : F) ^ b = Q ^ c * Q ^ (b + 1 - c) := by
    rw [← pow_succ', ← pow_add]; congr 1; omega
  rw [h2, h1,
    show (Q : F) ^ c * Q ^ (b + 1 - c) - Q ^ c = Q ^ c * (Q ^ (b + 1 - c) - 1) from by ring,
    show (Q : F) ^ c * Q ^ (b - c) - Q ^ c = Q ^ c * (Q ^ (b - c) - 1) from by ring,
    mul_div_mul_left _ _ hQc,
    show (1 : F) - Q ^ (b + 1 - c) = -(Q ^ (b + 1 - c) - 1) from by ring,
    show (1 : F) - Q ^ (b - c) = -(Q ^ (b - c) - 1) from by ring, neg_div_neg_eq]

/-- **The `q`-ratio factor at a pair above `a`** (`j < a`, so `β_a < β_j`).

`(Q·Q^{β_a} − Q^{β_j})/(Q^{β_a} − Q^{β_j}) = Q · (1 − Q^{β_j−β_a−1})/(1 − Q^{β_j−β_a})`

— the same `P(β')`-over-`P(β)` factor, times **one** `Q`.  Summed over the `a` rows above, those
`Q`s are the `Q^a` that `nPart_addCell` accounts for. -/
theorem qratio_factor_upper (Q : F) (hQ : Q ≠ 0) (b c : ℕ) (h : b + 1 ≤ c) :
    (Q * Q ^ b - Q ^ c) / (Q ^ b - Q ^ c)
      = Q * ((1 - Q ^ (c - b - 1)) / (1 - Q ^ (c - b))) := by
  have hQb : (Q : F) ^ b ≠ 0 := pow_ne_zero _ hQ
  have h1 : (Q : F) ^ c = Q ^ b * Q ^ (c - b) := by
    rw [← pow_add]; congr 1; omega
  have h2 : Q * (Q : F) ^ (c - b - 1) = Q ^ (c - b) := by
    rw [← pow_succ']; congr 1; omega
  rw [h1,
    show Q * (Q : F) ^ b - Q ^ b * Q ^ (c - b) = Q ^ b * (Q - Q ^ (c - b)) from by ring,
    show (Q : F) ^ b - Q ^ b * Q ^ (c - b) = Q ^ b * (1 - Q ^ (c - b)) from by ring,
    mul_div_mul_left _ _ hQb, mul_div_assoc']
  congr 1
  rw [mul_sub, mul_one, h2]

end QOU.SchurWeyl
