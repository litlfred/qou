/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Σ(2,3,5) false-theta exponent is integral: `n² ≡ 1 (mod 120)` on the support

The Poincaré sphere `Σ(2,3,5)` carries two normalisations of the same false theta
series, and the corpus and the literature use different ones. Jacoby–Lawrence,
*Some computations of Ohtsuki series* (`library/04procbryden/04procbryden.pdf`) p. 55 write the
Ohtsuki series as

  `q(q − 1)·Z_∞(Σ(2,3,5))(q) = 1 − ½·∑_{n≥1} χ(n)·q^{(n²−1)/120}`

with `χ : ℤ/60ℤ → {−1,0,1}` odd and `χ = +1` **exactly** at `1, 11, 19, 29`, while the
Lawrence–Zagier / Hikami false theta is normalised as `Ψ(q) = ∑ χ(n) q^{n²/120}`.

This file proves the arithmetic fact that reconciles them: on the support of `χ` the
exponent `(n²−1)/120` is an **integer**, so the two series differ by exactly the single
universal factor `q^{1/120}` — not by any `n`-dependent reindexing.

  `Ψ(q) = q^{1/120} · ∑ χ(n) q^{(n²−1)/120}`

That is why Jacoby–Lawrence's normalisation is the integral one: its exponents on
`n = 1, 11, 19, 29` are `0, 1, 3, 7` (see `sigma235_exponent_low` below), whereas the
`n²/120` exponents are `1/120, 121/120, 361/120, 841/120` — never integers.

**Support.** `χ` is the odd extension mod 60 of `{1, 11, 19, 29}`, so it is supported on
the eight residues `{1, 11, 19, 29, 31, 41, 49, 59}` (the last four being `60 − r`,
where `χ = −1`). Sign is irrelevant to the exponent, so all eight are covered.

**Why `mod 60` suffices to pin `n² mod 120`.** Writing `n = 60k + r`,
`n² = r² + 120·(r·k + 30k²)`, so the residue of `n²` mod 120 depends only on `r` — this
is the step that makes the statement about a mod-60 character into a mod-120 fact.

**Scope.** Pure integer arithmetic. This proves the *exponent integrality* and hence the
exact relation between the two normalisations. It says nothing about the value of either
series, about `Z_∞` itself, or about which normalisation any downstream evaluation should
use — those are analytic/convention questions, not settled here. §7c: `ℤ` throughout, no
archimedean structure, no `ℝ`. Sorry-free. Nothing wired; no fit.

-- Ref: [leitner2026] Jacoby–Lawrence, *Some computations of Ohtsuki series*, p. 55
--      (`library/04procbryden/04procbryden.pdf`); Lawrence–Zagier normalisation as cited there.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.MathlibExt

/-- The eight residues mod 60 on which the `Σ(2,3,5)` character `χ` is nonzero:
`{1, 11, 19, 29}` where `χ = +1`, and their partners `60 − r` where `χ = −1`. -/
def Sigma235Support (n : ℤ) : Prop :=
  n % 60 = 1 ∨ n % 60 = 11 ∨ n % 60 = 19 ∨ n % 60 = 29 ∨
  n % 60 = 31 ∨ n % 60 = 41 ∨ n % 60 = 49 ∨ n % 60 = 59

/-- **The exponent is integral.** On the support of `χ`, `n²` is `1` more than a multiple
of `120`; equivalently `(n²−1)/120 ∈ ℤ`.

This is the fact that makes the Jacoby–Lawrence normalisation `q^{(n²−1)/120}` a genuine
power series, and pins the discrepancy with `q^{n²/120}` to the single constant `q^{1/120}`
rather than to any `n`-dependent difference. -/
theorem sigma235_sq_eq_120_mul_add_one (n : ℤ) (h : Sigma235Support n) :
    ∃ m : ℤ, n ^ 2 = 120 * m + 1 := by
  obtain ⟨k, hk⟩ : ∃ k : ℤ, n = 60 * k + n % 60 := ⟨n / 60, by omega⟩
  rcases h with h | h | h | h | h | h | h | h <;> rw [h] at hk <;> subst hk
  · exact ⟨30 * k ^ 2 + k, by ring⟩
  · exact ⟨30 * k ^ 2 + 11 * k + 1, by ring⟩
  · exact ⟨30 * k ^ 2 + 19 * k + 3, by ring⟩
  · exact ⟨30 * k ^ 2 + 29 * k + 7, by ring⟩
  · exact ⟨30 * k ^ 2 + 31 * k + 8, by ring⟩
  · exact ⟨30 * k ^ 2 + 41 * k + 14, by ring⟩
  · exact ⟨30 * k ^ 2 + 49 * k + 20, by ring⟩
  · exact ⟨30 * k ^ 2 + 59 * k + 29, by ring⟩

/-- Divisibility form of `sigma235_sq_eq_120_mul_add_one`. -/
theorem sigma235_dvd_sq_sub_one (n : ℤ) (h : Sigma235Support n) :
    (120 : ℤ) ∣ n ^ 2 - 1 := by
  obtain ⟨m, hm⟩ := sigma235_sq_eq_120_mul_add_one n h
  exact ⟨m, by omega⟩

/-- The four exponents Jacoby–Lawrence's series actually carries at the four positive
support residues: `0, 1, 3, 7`. These are the numbers a reader can check against p. 55,
and they are integers exactly because of `sigma235_sq_eq_120_mul_add_one`. -/
theorem sigma235_exponent_low :
    (1 ^ 2 - 1) / 120 = (0 : ℤ) ∧ (11 ^ 2 - 1) / 120 = (1 : ℤ) ∧
    (19 ^ 2 - 1) / 120 = (3 : ℤ) ∧ (29 ^ 2 - 1) / 120 = (7 : ℤ) := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- The `n²/120` normalisation is **not** integral: at `n = 1` the exponent numerator `n²`
leaves remainder `1` on division by `120`. Stated as the sharp negative so the two
normalisations cannot be silently identified. -/
theorem sigma235_lz_exponent_not_integral :
    ¬ ((120 : ℤ) ∣ 1 ^ 2) := by decide

end QOU.MathlibExt
