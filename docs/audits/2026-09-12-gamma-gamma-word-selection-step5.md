# γγ word selection, step 5 — reading 3 (Frobenius positivity) formalised; it selects `β_Bor` on the whole interval

**Bean:** `qou-ales`. **Owner ruling (chat, 2026-09-12, verbatim):** *"try PSD condfinement 3
for now, but keep 1 2 for later."* This record adopts reading 3 provisionally, formalises it,
and keeps readings 1 and 2 on record. Steps 1–3 are on `main` (#7184, #7192); step 4 is on
PR #7207 with this step.

**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/GammaGammaFrobeniusSelection.lean`
(23 declarations; `#print axioms` on every one: at most `[propext, Classical.choice,
Quot.sound]`; no `sorryAx`; `lean -DautoImplicit=false -s 65536` exit 0, 0 warnings, against
the same rebuilt-from-source shadow as step 4).

Nothing below reads AME2020, a CODATA binding value, or a census. No probe is added: the
numerical content of this step is exactly the step-4 witness (the `χ_(2,1)` column), and the
step-3 witness's Markov weights `y_(3) = 0.5054`, `y_(2,1) = 0.2473`, `y_(1³) = 0` under
convention D at the proton pin, of which only the **sign** of `y_(2,1)` enters.

## 1. The three readings, and what is kept

| reading | predicate on a word `w` | Lean | status |
|---|---|---|---|
| 1 literal | every `π_λ(w)` is `Matrix.PosSemidef` | `WedderburnBlocks.PSDFeasible` / `SDPSelected` (step 1) | **kept**; on `H₃` admits a non-trivial γγ word iff some vertex power is `±1` (step 4), and none with `k ≤ 5` for `1 < q ≤ 23/20` |
| 2 symmetric part | every `π_λ(w) + π_λ(w)ᵀ` is PSD | `SymPSDFeasible` (new) | **kept**; agrees with 3 at `H₃` (step-3 measurement); no selection theorem yet |
| 3 Frobenius | `χ_λ(w) = tr π_λ(w) ≥ 0` on every block with `y_λ > 0` | `FrobeniusFeasible` / `FrobeniusSelected` (new) | **adopted for now** |

The one relation between them that costs nothing is proved: **1 ⇒ 3 and 2 ⇒ 3**
(`FrobeniusFeasible.of_psdFeasible`, `…of_symPSDFeasible` — a PSD matrix has non-negative
trace, `Matrix.PosSemidef.trace_nonneg`, and the symmetric part has trace `2·tr`). So the
reading-3 minimum is a **lower bound** on whatever readings 1 or 2 select later on the same
candidates and cost (`FrobeniusSelected.cost_le_of_psdFeasible`, `…_of_symPSDFeasible`,
`SDPSelected.frobenius_cost_le`). Switching to 1 or 2 later can only move the selection to a
word with at least six crossings.

## 2. Reading 3 on `H₃`

* `frobeniusFeasible_iff_std` — for a γγ-word only the `(2,1)` block decides: the `(3)` and
  `(1³)` characters of a γγ-word are `1` (`trivChar_eq_one`, `altChar_eq_one`).
* `vertexPow_frobeniusFeasible_iff` — for `(σ₀σ₁⁻¹)^k` feasibility is
  `0 < y_(2,1) → 0 ≤ tr V^k`, `V` the step-4 vertex image.
* `hoefsmit_vertexPow_frobenius_table` — at the concrete Hoefsmit data, for **every**
  `1 < q ≤ 23/20` and every `y` with `y_(2,1) > 0`:

  | k | `χ_(2,1)(V^k)`, `x = h²` | sign on `0 < x ≤ 1/10` | reading 3 |
  |---|---|---|---|
  | 1 | `−1 − x` | − | infeasible |
  | 2 | `x² + 2x − 1` | − | infeasible |
  | 3 | `2 − 3x² − x³` | + | **feasible** |
  | 4 | `x⁴ + 4x³ + 2x² − 4x − 1` | − | infeasible |
  | 5 | `−x⁵ − 5x⁴ − 5x³ + 5x² + 5x − 1` | − | infeasible |

* **`frobeniusSelected_borromean`** — with candidates the non-zero vertex powers `1 ≤ k ≤ 5`
  (`vertexPowCands 5`, the γγ words of `H₃` with at most ten crossings; owner ruling
  2026-08-30: minimal *non-zero* feasible) and cost = crossing count, the reading-3 selection
  is `k = 3 = β_Bor`, for every `1 < q ≤ 23/20` and every `y` with `y_(2,1) > 0`.
  `frobeniusSelected_length_eq_six`: any reading-3-selected word on these candidates has six
  crossings.

The proton pin `q₀ ≈ 1.10998` is inside the interval (`h_sq_le_of_q_le`), and under
convention D `y_(2,1) = 0.2473 > 0` there (step-3 witness). So the step-3 measurement
"the `H₃` selector picks `β_Bor`" is now a theorem on an interval, under the adopted reading.

## 3. What stays open

1. **`k > 5`.** The candidate set stops at ten crossings because `chi_signs_of_small` stops at
   `k = 5`. Extending is a matter of more Chebyshev closed forms; nothing suggests a cheaper
   survivor, but it is not proved.
2. **Which reading the confinement SDP *means*** is still an owner call; reading 3 is
   provisional, and readings 1 and 2 are kept (§1). Reading 2 has no selection theorem.
3. **The `H₆` interface** (the pp bond `(σ₂σ₃⁻¹)³`, step 3) is measured, not in Lean.
4. Non-γγ letters (step-3 §4.2) and the `θ/π` rationality question (step-4 §5.1) are untouched.

## 4. Verification

`lean -DautoImplicit=false -s 65536` against the hardlinked `QOU` shadow of step 4 (import
cone rebuilt from source): **exit 0, 0 errors, 0 warnings**, first compile. `#print axioms` on
all 23 declarations: no `sorryAx`. `scripts/check-sidecars.sh`: the only marker on the new
file is the §7c "mixed generic + archimedean" note, shared with the step-3/4 files — the
abstract predicates are over a generic `[Ring R] [PartialOrder R]`; `ℝ` enters only through
`Matrix.PosSemidef.trace_nonneg` (Mathlib states it for `RCLike`) and the interval lemmas.
