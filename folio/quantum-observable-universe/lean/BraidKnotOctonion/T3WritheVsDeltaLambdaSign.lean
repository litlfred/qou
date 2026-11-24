/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/

/-!
# QOU.BraidsAndKnots.T3WritheVsDeltaLambdaSign

## Does the derived weak-isospin `T₃` writhe-sign reproduce the mixed-sign `Δ_λ`?

Serves bean `qou-buxs` (child of `qou-20sx`).  Formalises the decisive
structural finding of `computations/t3_writhe_vs_delta_lambda_sign.py`.

The weak-isospin grading of `WeakIsospinT3Grading.lean` (PR #4618) is
`T₃ = sign(κ)/2`, `κ =` signed writhe: the **per-quark datum is `sign(κ)`**,
the sign of the *net* writhe.  The Option-E deuteron closure needs the
per-partition chirality sign
`sgn(w₀^{S_{λ'}}) = ∏_j (-1)^{C(c_j,2)}` (`c_j` = column heights of `λ`), a
mixed-sign pattern the PROBE-4 KL-positivity prune (2026-06-16) proved must be
supplied *exogenously from the braid images*.

Aggregating the crossing sign over the Young/Wedderburn **column
antisymmetrizer** (guided by the chiral-EFT `τ₁·τ₂` Pauli/exchange-symmetry
template, Hammer–König–van Kolck arXiv:1906.12122 p.12) admits **two readings
that differ**, and the difference is the whole result:

* **crossing-COUNT parity** `crossingCountParity c = (-1)^{C(c,2)}` — the sign
  *character* / Slater-determinant sign.  Its product over column heights is
  `sgn(w₀^{S_{λ'}})` itself (the target's own definition).
* **net-writhe SIGN** `netWritheSign c` — the *literal* `T₃` statistic
  `sign(κ)`: a column of height `c ≥ 2` is a negative half-twist with net
  writhe `-C(c,2)`, so `sign(net) = -1` for every `c ≥ 2` and `+1` for `c ≤ 1`.

These two per-column factors **coincide iff `C(c,2)` is odd** (`c ≡ 2,3 mod 4`)
and both are `+1` at `c ≤ 1`; they **diverge at `c = 4,5`** — first realised by
a partition of `6`.  So the literal `T₃` sign-of-net-writhe reproduces `Δ_λ`
for `n = 3` (all column heights `≤ 3`) but **fails at `n = 6`**.

### What is proved below (`decide`; genuine finite decidable checks, no fit)

* `heightFourStatisticsDisagree` — the falsifiable root: at column height `4`
  the two sign statistics disagree (`crossingCountParity 4 = 1`,
  `netWritheSign 4 = -1`).  This is why the maps part ways; had they agreed the
  whole negative would vanish.
* `n3_literalT3_reproduces_target` — for every partition of `3` the literal-`T₃`
  aggregation equals the target sign (`3/3`, coincidental: heights `≤ 3`).
* `n6_literalT3_fails_at_3111` — for the partition `(3,1,1,1) ⊢ 6` the
  literal-`T₃` aggregation **differs** from the target: the honest negative.
  (Its conjugate has a height-`4` column.)

This file is deliberately **import-free** (pure core Lean 4, `Int`-valued,
decidable) so the arithmetic is self-verifiable without Mathlib; it makes no
archimedean (`ℝ`) or categorical claim, only the finite sign comparison.

Refs:
  - docs/audits/2026-08-02-t3-writhe-vs-delta-lambda-sign.md (this probe)
  - docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md (the target is mixed-sign)
  - content/.../lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean (T₃)
  -- Ref: [leitner2026] Ch. "Predicted Spectra"; Option-E Δ_λ closure ledger
-/

namespace QOU.BraidsAndKnots.T3WritheVsDeltaLambda

/-- Sign of `(-1)^k`, computed via parity (no `Monoid.npow` needed). -/
def parityFactor (k : Nat) : Int := if k % 2 = 0 then 1 else -1

/-- Number of crossings in the half-twist antisymmetrizer of `c` strands,
    `C(c,2) = c(c-1)/2`. -/
def cross2 (c : Nat) : Nat := c * (c - 1) / 2

/-- **Crossing-COUNT parity** of a column of height `c`: `(-1)^{C(c,2)}`.
    This is the sign-character / Slater-determinant factor; its product over
    the columns is `sgn(w₀^{S_{λ'}})`, the `Δ_λ` chirality sign. -/
def crossingCountParity (c : Nat) : Int := parityFactor (cross2 c)

/-- **Net-writhe SIGN** of a column of height `c`: the *literal* `T₃` datum
    `sign(κ)`.  The column is a negative half-twist (net writhe `-C(c,2)`), so
    the sign is `-1` for `c ≥ 2` and `+1` for `c ≤ 1`. -/
def netWritheSign (c : Nat) : Int := if 2 ≤ c then -1 else 1

/-- Column heights of a partition `λ` (rows, weakly decreasing) = its conjugate
    `λ'`.  `colHeights λ j = #{ rows longer than j }`. -/
def colHeights (lam : List Nat) : List Nat :=
  let w := lam.foldl (fun m r => max m r) 0        -- largest row = #columns
  (List.range w).map (fun j => (lam.filter (fun r => j < r)).length)

/-- Target `Δ_λ` chirality sign `sgn(w₀^{S_{λ'}}) = ∏_j (-1)^{C(c_j,2)}`. -/
def targetSign (lam : List Nat) : Int :=
  (colHeights lam).foldl (fun acc c => acc * crossingCountParity c) 1

/-- Literal-`T₃` aggregation: product of the per-column net-writhe signs. -/
def literalT3Sign (lam : List Nat) : Int :=
  (colHeights lam).foldl (fun acc c => acc * netWritheSign c) 1

/-! ### The falsifiable root: the two statistics disagree at height 4 -/

/-- **At a column of height 4 the two sign statistics disagree.**  The
    crossing-count parity is `(-1)^6 = +1`; the net-writhe sign is `-1`.  This
    is the concrete reason the literal `T₃` grading cannot be the `Δ_λ` sign:
    `Δ_λ` reads a crossing-COUNT parity, `T₃` reads a net-orientation sign, and
    they differ exactly when `C(c,2)` is even (`c ≡ 0,1 mod 4`, first at `c=4`). -/
theorem heightFourStatisticsDisagree :
    crossingCountParity 4 = 1 ∧ netWritheSign 4 = -1 ∧
      crossingCountParity 4 ≠ netWritheSign 4 := by
  decide

/-- The statistics **agree** at heights `1,2,3` (why `n = 3` matches). -/
theorem lowHeightsAgree :
    (crossingCountParity 1 = netWritheSign 1) ∧
    (crossingCountParity 2 = netWritheSign 2) ∧
    (crossingCountParity 3 = netWritheSign 3) := by
  decide

/-! ### `n = 3`: literal `T₃` reproduces the target (coincidental, heights ≤ 3) -/

/-- For all three partitions of `3`, the literal-`T₃` aggregation equals the
    target `Δ_λ` sign.  A genuine `3/3` match — but coincidental, since every
    column height is `≤ 3` (where the two statistics agree, `lowHeightsAgree`). -/
theorem n3_literalT3_reproduces_target :
    literalT3Sign [3] = targetSign [3] ∧
    literalT3Sign [2, 1] = targetSign [2, 1] ∧
    literalT3Sign [1, 1, 1] = targetSign [1, 1, 1] := by
  decide

/-- The `n = 3` target itself is mixed-sign `1+/2-` (matching the prune):
    `(3) ↦ +1`, `(2,1) ↦ -1`, `(1,1,1) ↦ -1`. -/
theorem n3_target_values :
    targetSign [3] = 1 ∧ targetSign [2, 1] = -1 ∧ targetSign [1, 1, 1] = -1 := by
  decide

/-! ### `n = 6`: the honest negative — literal `T₃` fails at a height-4 column -/

/-- **`(3,1,1,1) ⊢ 6`: literal `T₃` disagrees with the target.**  Its conjugate
    is `(4,1,1)` — a height-`4` column — so the target reads
    `crossingCountParity 4 = +1` while the literal `T₃` reads
    `netWritheSign 4 = -1`.  Concretely `literalT3Sign = -1 ≠ +1 = targetSign`.
    This is the decisive Lean-checked negative: the derived `T₃` writhe-sign
    does **not** reproduce the mixed-sign `Δ_λ` pattern. -/
theorem n6_literalT3_fails_at_3111 :
    literalT3Sign [3, 1, 1, 1] ≠ targetSign [3, 1, 1, 1] := by
  decide

/-- The two other `n = 6` failures, at the height-4/5 columns
    `(2,2,1,1) ↝ λ'=(4,2)` and `(2,1,1,1,1) ↝ λ'=(5,1)`. -/
theorem n6_literalT3_fails_at_2211_and_21111 :
    literalT3Sign [2, 2, 1, 1] ≠ targetSign [2, 2, 1, 1] ∧
    literalT3Sign [2, 1, 1, 1, 1] ≠ targetSign [2, 1, 1, 1, 1] := by
  decide

/-- Sanity: the `n = 6` target is genuinely mixed-sign (a `+` and a `-` block),
    so the failures above are failures against a real chirality pattern, not an
    all-one target. -/
theorem n6_target_mixed_sign :
    targetSign [6] = 1 ∧ targetSign [1, 1, 1, 1, 1, 1] = -1 := by
  decide

end QOU.BraidsAndKnots.T3WritheVsDeltaLambda
