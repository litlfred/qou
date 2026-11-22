/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Behrend weighting for `A_ω(4₁) = 3` must be non-constant — a parity obstruction

**Bean `qou-dt14`** (front-2 characterization). Companion to
`StokesDTCountExceedsRecursionOrder.lean` (bean `qou-qnnq`), which established the
honest negative:

* the QOU Wedderburn/Springer **graded Euler characteristic** over the `H₃(q)`
  blocks is `Σ_{λ ⊢ 3} Δ_λ = 1 − 2 − 1 = −2` (sorry-free, `partitionEuler3_eq`);
* the knot Stokes/DT/BPS **count** is `S⁺(0)₀₁ = 3`;
* `−2 ≠ 3`, and the two are *different DT objects* — the per-partition Springer
  fibre vs the per-knot character variety. The lever map records the missing input
  as an **irreducibly external, Behrend-weighted DT moduli count** (driver-14).

This file asks the next question — not *what is* the missing count, but **what must
any supplier of it satisfy** — and extracts a structural constraint, in the
formalize-first spirit (prune the class before searching it).

## The constraint

A Donaldson–Thomas count is a *Behrend-weighted* Euler characteristic
`DT = Σ_n n · χ_eu(ν⁻¹(n))` over the strata of the constructible Behrend function
`ν`. The unweighted total is the ordinary Euler characteristic. Hence:

* **`no_constant_weight_yields_three`** — if `ν` is **constant** (value `c`), then
  `DT = c · χ_eu`. With `χ_eu = −2` this is *even* for every integer `c`, while the
  target count `3` is **odd**. So no constant weighting supplies it.
* **`at_least_two_strata`** — consequently the Behrend stratification of any
  moduli supplying `3` over `χ_eu = −2` has **at least two strata**.
* **`odd_count_needs_odd_stratum`** — sharper: some stratum must carry an **odd**
  weighted contribution `n_i · χ_eu,i` (both its Behrend value and its Euler characteristic odd).

## What this prunes

The Behrend function of a **smooth** moduli space is the constant `(−1)^dim`
(Behrend 2009). By `no_constant_weight_yields_three`, **no smooth moduli space
with `χ_eu = −2` can supply the count `3`** — the supplier must be genuinely
singular, with at least two Behrend strata, one of them odd·odd. This excludes
the entire "smooth moduli + (signed) Euler characteristic" family of attempts,
which is the shape every QOU-internal route has taken so far (the Wedderburn /
Springer graded Euler characteristic is exactly such an unweighted count) — and it
explains *structurally* why those routes produce `−2` and not `3`: they have no
mechanism to be odd.

The invariant is **parity**, and it is named — per the AGENTS.md (a)/(b) rule this
licenses the exclusion as scope-**(b)** for the constant-weight class, not merely
a failed numerical probe.

## Honest scope (STRICT)

This **characterizes** the missing input; it does **not** supply it, and it does
**not** close `bwse`, `A_ω`, or `Δ_λ`. It is also known in advance (lever map,
#4601, derive-then-check) that **closing the DT count would not close binding** —
the derived `Δ_λ` fragment leaves the deuteron at `B(D) = 0.380 MeV` (−82.9 %). So
this is deliberately bounded work: a prune, not a closure claim. The `χ_eu = −2` and
`count = 3` inputs are the corpus's own established values, carried here as
explicit hypotheses rather than re-derived. No fit; nothing wired; L2 unchanged.

Mathlib-free (`Init` only) — so it is machine-verified independently of the
Mathlib olean cache.

-- Ref: [leitner2026] docs/audits/2026-08-02-stokes-dt-bridge-moduli-gap-unification.md
-/
import Init.Data.Int.Basic
import Init.Data.List.Basic
import Init.Omega

namespace QOU.QBeta.DTBehrendParityObstruction

/-! ### Notation (§7aa)

We write `χ_eu` for an **Euler characteristic** (`chiEuTotal` for the whole moduli,
`chiEuS` for a single stratum). The glyph `χ` alone is a notation violation: in QOU it
is shared by the **characters** — `χ_λ` in the Frobenius pairing
`tr_M = Σ_λ y_λ χ_λ`, and `χ_ζ(c)` — and by the Lyapunov exponent `χ_q`. The Euler
characteristic keeps the standard glyph but always carries the roman subscript
(`notation/notation-collisions.md`). Write `χ_eu`, never an uppercase `\Chi`: there is
no such KaTeX/LaTeX macro (uppercase Greek chi is glyph-identical to Latin X), so it
would fail the render gate. The orbifold Euler *number* of `Σ(2,3,5)` keeps its own
conventional symbol `e = −1/30`.

### Which number is "the Euler characteristic"? (`−2`, not `−6`)

Two integers circulate and must not be conflated:

| object | value | source |
|---|---|---|
| QOU Wedderburn/Springer Euler characteristic `Σ_{λ ⊢ 3} Δ_λ` | `−2` | `StokesDTCountExceedsRecursionOrder.partitionEuler3_eq` |
| GGM sandwich `(0,1)` entry | `−6 = (−2)·3` | `StokesQZeroDTCount.sandwich_offdiagonal_qzero` |
| Stokes/DT/BPS **count** `S⁺(0)₀₁` | `3` | `StokesQZeroDTCount.stokes_qzero_offdiagonal` |

The `−6` is the *product* of the sandwich prefactor `−2` and the count `3`, not an
Euler characteristic — though the original G3 directive hinted "Euler = −6", which
is exactly the ambiguity this table removes.

**The obstruction does not depend on resolving it.** `chiEu_even_blocks_three`
below rules out *every even* total, so both `−2` and `−6` are excluded, and the
result is immune to which object is meant. -/

/-- A Behrend stratification, as the list of its strata: each carries the Behrend
function's constant value `n` on that stratum, paired with that stratum's Euler
characteristic `chiEuS`. -/
abbrev Strata := List (Int × Int)

/-- The unweighted Euler characteristic `χ_eu(M) = Σ χ_eu,i` (Behrend strata partition
the moduli, and `χ_eu` is motivic/additive). -/
def chiEuTotal : Strata → Int
  | [] => 0
  | p :: t => p.2 + chiEuTotal t

/-- The Behrend-weighted Donaldson–Thomas count `DT = Σ_i n_i · χ_eu,i`. -/
def dtCount : Strata → Int
  | [] => 0
  | p :: t => p.1 * p.2 + dtCount t

/-- **Constant Behrend weight cannot yield the count `3` over `χ_eu = −2`.**
If the Behrend function is constant with value `c`, the count is `c · χ_eu = c · (−2)`,
which is even for every integer `c`; the target `3` is odd. This is the parity
obstruction, stated at its source. -/
theorem no_constant_weight_yields_three (c : Int) : c * (-2) ≠ 3 := by
  omega

/-- The same for `−6`, the GGM sandwich `(0,1)` entry — the other integer the G3
directive called "Euler". Also even, also excluded. -/
theorem no_constant_weight_yields_three_neg_six (c : Int) : c * (-6) ≠ 3 := by
  omega

/-- **The obstruction in full generality: every even total is excluded.** For *any*
even Euler characteristic `E` and any constant Behrend value `c`, the weighted count
`c · E` is even and so cannot equal the odd target `3`.

This is why the `−2` vs `−6` ambiguity is harmless: both are even, so the
constant-weight class is excluded either way. Only an *odd* total could be rescued
by a constant weight — and the QOU machinery produces even ones. -/
theorem chiEu_even_blocks_three (E c : Int) (hE : E % 2 = 0) : c * E ≠ 3 := by
  obtain ⟨k, hk⟩ : ∃ k, E = 2 * k := ⟨E / 2, by omega⟩
  intro h
  rw [hk, ← Int.mul_assoc, Int.mul_comm c 2, Int.mul_assoc] at h
  omega

/-- The weighted count of a single-stratum (i.e. constant-weight) stratification is
`n · χ_eu`. -/
theorem dtCount_single (n chiEuS : Int) : dtCount [(n, chiEuS)] = n * chiEuS := by
  simp [dtCount]

/-- The Euler characteristic of a single-stratum stratification is that stratum's
`chiEuS`. -/
theorem chiEuTotal_single (n chiEuS : Int) : chiEuTotal [(n, chiEuS)] = chiEuS := by
  simp [chiEuTotal]

/-- **At least two Behrend strata.** A stratification with total Euler
characteristic `−2` and Behrend-weighted count `3` cannot have fewer than two
strata: the empty one has `χ_eu = 0 ≠ −2`, and a single stratum forces the even
`n · (−2) = 3`. Hence the supplier of the knot DT count is genuinely singular
(a smooth moduli has the constant Behrend function `(−1)^dim`). -/
theorem at_least_two_strata (S : Strata)
    (hE : chiEuTotal S = -2) (hD : dtCount S = 3) : 2 ≤ S.length := by
  match S with
  | [] => simp [chiEuTotal] at hE
  | [(n, chiEuS)] =>
      rw [chiEuTotal_single] at hE
      rw [dtCount_single, hE] at hD
      exact absurd hD (no_constant_weight_yields_three n)
  | _ :: _ :: _ => simp [List.length]

/-- If every stratum contributes an even weighted term, the whole count is even. -/
theorem dtCount_even_of_all_even (S : Strata)
    (h : ∀ p ∈ S, (p.1 * p.2) % 2 = 0) : dtCount S % 2 = 0 := by
  induction S with
  | nil => simp [dtCount]
  | cons a t ih =>
      have ha : (a.1 * a.2) % 2 = 0 := h a (List.Mem.head _)
      have ht : dtCount t % 2 = 0 := ih fun p hp => h p (List.Mem.tail _ hp)
      simp only [dtCount]
      omega

/-- **Some stratum must be odd·odd.** Sharpening the parity obstruction, in
contrapositive (constructive) form: if *every* stratum contributes an even weighted
term `n_i · χ_eu,i`, the count cannot be `3`. Equivalently, any construction supplying
the knot DT count must exhibit a stratum carrying **both** an odd Behrend value and
an odd Euler characteristic. -/
theorem odd_count_needs_odd_stratum (S : Strata)
    (hall : ∀ p ∈ S, (p.1 * p.2) % 2 = 0) : dtCount S ≠ 3 := by
  have h := dtCount_even_of_all_even S hall
  omega

end QOU.QBeta.DTBehrendParityObstruction
