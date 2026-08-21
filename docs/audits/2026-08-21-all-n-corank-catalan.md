# The all-`n` corank: `Σ_{ℓ(λ)≤2} (dim V_λ)² = catalan n` proved

*2026-08-21 — branch `claude/tl-all-n-corank-2026-08-21`, [PR #5360](https://github.com/litlfred/qou/pull/5360).*

## What changed

`corank(n) = n! − Catalan(n)` was four measurements (`n = 3,4,5,6 → 1, 10, 78,
588`, [`tl_n6_discriminator.py`](../../computations/probes/tl_n6_discriminator.py)).
The arithmetic gap between those and a general-`n` statement was
**bean `qou-0cyu` item G5**:

```
Σ_j m_j(n)² = catalan n          with m_j(n) = C(n,j) − C(n,j−1)
```

proved in [`BallotNumbers.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/BallotNumbers.lean)
only at `n = 3, 4, 5`. **It is now proved for general `n`, sorry-free**
(`ballot_sq_sum_catalan`), and wired through actual hook-length dimensions
(`dimHLF_two_row_sq_sum`) to the corank statement (`corank_general`).

## The route, and why both of the bean's prices were wrong

`qou-0cyu` priced G5 twice, and recorded the second pricing as a correction of
the first:

> **G5.** I listed this in `qou-u2jg` as "pure combinatorics, no q" — as though
> it were the EASY one. It is not. By RSK it says: 321-avoiding permutations are
> Catalan. Mathlib has `catalan` but no RSK, no ballot numbers, and no
> pattern-avoidance theory. Two routes: (a) formalise enough RSK — LARGE;
> (b) a direct induction on the ballot recursion — plausibly MEDIUM and worth
> trying FIRST.

Route (b) **does not close**, and it is worth saying why rather than leaving the
next agent to find out. The ballot recursion

```
m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)
```

is *linear*; the Catalan recursion `C_{n+1} = Σ_i C_i C_{n−i}` is a
*convolution*. Squaring the first produces cross terms `2 Σ_j m_j m_{j−1}` for
which the second has no slot. That mismatch is precisely why **G2** — which is
linear in the `m_j` — does succumb to induction on the same recursion, and G5
does not. The bean's own reasoning for why `ballot_succ_succ` is "the engine"
for G2 is correct, and is exactly the reason it is not the engine for G5.

What closes it is a third route the bean did not consider: **reflection plus
Vandermonde, with no induction and no tableau.**

| Step | Lemma | Content |
|---|---|---|
| 1 | `ballot_sq_sum_full` | Run the sum over the **full** range `k = 0…n+1`. There the summand is a binomial difference and Vandermonde (`Nat.add_choose_eq`) evaluates all three resulting sums: `Σ_k m_k(n)² = 2·C(2n,n) − 2·C(2n,n+1)`. |
| 2 | `catalan_eq_choose_sub` | `catalan n = C(2n,n) − C(2n,n+1)`, from `succ_mul_catalan_eq_centralBinom` and `Nat.choose_succ_right_eq` by cancelling `n+1`. |
| 3 | `ballot_reflect` + `ballot_sq_sum_fold` | `m_{n+1−k}(n) = −m_k(n)`, so the full sum is exactly **twice** the half sum. |

Every ingredient is in Mathlib at the pinned rev. Nothing needed adding.

Two details a reviewer should check rather than take on trust:

- **`C(2n, n+1)`, not `C(2n, n−1)`.** Equal by symmetry, but `n+1` involves no
  truncated `ℕ` subtraction, so the statement is correct at `n = 0` with no side
  condition. The `n−1` spelling gives `C(0,0) − C(0,0) = 0` there — the same
  off-by-one that `ballot` is defined to avoid, reappearing one level up.
- **The odd-`n` fixed point.** The fold has a fixed point exactly when `n` is
  odd, at `k = (n+1)/2`, where reflection forces `m_k = −m_k`. That the summand
  vanishes there is `ballot_boundary_zero` — **already proved**, for G2's parity
  split. The same lemma resolves both parity splits, which is some evidence the
  split is structural rather than an index artefact.

## Two things the corpus already had that a topic-grep would have found first

Recording these because in both cases the task framing assumed work that was
already done, and the cheap check was to look.

**1. The two-row reduction is a theorem here, not an observation.** The brief
asked whether `f^{(n−k,k)}` is the ballot number "in this repo's conventions",
to be checked numerically. It is — and
[`SYTDimHLFPair.lean:29`](../../content/quantum-observable-universe/lean/QOU/Mathlib/SYTDimHLFPair.lean)
**proves it sorry-free**, with a docstring that says so in as many words:

```lean
theorem dimHLF_pair (a b : ℕ) (hab : b ≤ a) (hb : 1 ≤ b) :
    dimHLF [a, b] = Nat.choose (a + b) b - Nat.choose (a + b) (b - 1)
```

So the wiring in [`TwoRowDimCatalan.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/TwoRowDimCatalan.lean)
is unconditional about **real Frame–Robinson–Thrall dimensions**, not merely
numerically supported. The only work in the bridge is the `ℕ → ℤ` cast:
`dimHLF_pair` is a *truncated* `ℕ` subtraction, so it agrees with the honest `ℤ`
difference only when `C(n,k−1) ≤ C(n,k)` — which holds precisely below the
centre of the row, i.e. exactly under `2k ≤ n`, the condition that makes
`(n−k, k)` a partition at all. The side condition is the partition condition
twice over.

**2. `n = 7` and `n = 8` were already computed, and the probe already ran to
`n = 8`.** [`wenzl_level_two_vanishing.py`](../../computations/probes/wenzl_level_two_vanishing.py)
loops `range(1, 9)` and `range(3, 9)`. Re-run on this branch, exit 0, output
byte-identical to the committed witness:

```
2c. y_lam = 0 <=> lam has >= 3 rows, n = 1..8               OK
3. corank = n! - Catalan(n) from the >= 3-row blocks, n=3..8 OK
    [1, 10, 78, 588, 4611, 38890]
```

## What is measured, what is arithmetic — do not blur these

| `n` | Gram-rank measurement | symbolic `y_λ` vanishing over ℚ(q) | dimension arithmetic |
|---|---|---|---|
| 3, 4, 5 | ✅ `gram_radical_cellular_revalidation.py` | ✅ | ✅ |
| 6 | ✅ `tl_n6_discriminator.py` | ✅ | ✅ |
| 7, 8 | ❌ **none exists** | ✅ `wenzl_level_two_vanishing.py` | ✅ |
| 9–14 | ❌ | ❌ | ✅ `two_row_ballot_catalan_reduction.py` |

The `n = 7` Gram rank is a 5040×5040 exact rank on a matrix that costs
`O(n!²)` to build; the existing probe reaches `n = 6` and was not extended here.
`corank_seven_value` / `corank_eight_value` in
[`MarkovGramDegenerate.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovGramDegenerate.lean)
say **prediction** in their docstrings for this reason. Do not cite them as
measurements.

## Epistemic tiering of the corank chain

| Link | Tier | Where |
|---|---|---|
| `Σ_{ℓ(λ)≤2} (dim V_λ)² = catalan n`, all `n` | **`proved-lean`, unconditional** | `ballot_sq_sum_catalan`, `dimHLF_two_row_sq_sum` |
| two-row dim = ballot number | **`proved-lean`, unconditional** | `dimHLF_pair` (pre-existing) |
| `n! − Σ … = n! − catalan n`, all `n` | **`proved-lean`, unconditional** | `corank_general` |
| `rank G ≤ catalan n` given a radical subspace of the right dimension | **`proved-lean`, conditional on stated hypotheses** | `gram_rank_le_catalan` |
| `y_λ = 0 ⟺ ℓ(λ) > r` at Wenzl level `r` | **`conditional`** — class-carried | `IsOcneanuWeightSystem`, `_of_wenzl` |
| **tr_M = Σ_λ y_λ χ_λ (Wedderburn diagonalisation)** | **`conditional`** — class-carried, **no instance anywhere** | `QOU.Hecke.WedderburnDecomp` |

### The premise the brief did not name

The task briefing named **one** class-carried premise (Wenzl, `qou-fpjy`).
There are **two**. The Wedderburn diagonalisation itself — the step that makes
"the Gram form is diagonal with entries ∝ `y_λ`" true, and hence the step the
entire corank decomposition rests on — is also a class field with no instance.
The corpus already says so, at
[`WedderburnTraceDecomposition.lean:31`](../../content/quantum-observable-universe/lean/QOU/QBeta/WedderburnTraceDecomposition.lean):

> *No instance of `WedderburnDecomp` exists anywhere in the tree.*

and bean `qou-luq7` carries it as a live DEFECT: `trace_decomposition` projects
a class field, so it derives nothing.

This is the "conditional-proved ≠ premise-established" failure mode in
AGENTS.md, and it compounds with `qou-fpjy`: **neither** premise is visible to
`#print axioms`, because a class hypothesis is a binder rather than an axiom. So
every declaration in this branch reports
`[propext, Classical.choice, Quot.sound]` — truthfully — while the corank
statement as a *physical* claim rests on two unformalised inputs. A clean axiom
report is not evidence to the contrary.

`qou-0cyu` also notes the way out for the second one, unused: Mathlib **has**
Artin–Wedderburn (`exists_algEquiv_pi_matrix_divisionRing_finite` in
`Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean`), and PR #4857 proved
`finrank H_n(q) = n!`. The existence half and the finiteness half have never
been put together. That is the highest-leverage remaining item, not this one.

## Verification (CI is `workflow_dispatch`-only; this is the agent-owned gate)

- `lean`-direct, **exit 0, no errors, no warnings** on all three touched Lean
  files, each against its **real import cone** — the 7-module SYT/ballot cone
  and `TemperleyLiebTower` built as addon oleans with `lean`-direct. **No
  `lake build` was run**; the main checkout's 6990 Mathlib oleans are intact
  (bean `qou-r13s`).
- **Zero `sorry` tactics.** Stated carefully, because a bare `grep -c sorry`
  is misleading here: `BallotNumbers.lean` and `MarkovGramDegenerate.lean`
  return 0, but `TwoRowDimCatalan.lean` returns **3** — all three inside the
  module docstring, in the words *"sorry-free"* (twice) and *"`sorryAx`"*.
  There is no `sorry` tactic in any of the three files. The authoritative check
  is the axiom sweep below, not the grep. `MarkovGramDegenerate.lean`'s count
  is unchanged from `HEAD` (0 → 0). No `native_decide` (0 in all three files),
  no `: True := trivial`, no `axiom`.
- `#print axioms` on **all 22** new declarations (8 in `BallotNumbers`, 9 in
  `TwoRowDimCatalan`, 5 in `MarkovGramDegenerate`):
  `[propext, Classical.choice, Quot.sound]`, **no `sorryAx`** — read subject to
  the caveat above.
- `two_row_ballot_catalan_reduction.py` exit 0, `n = 1..14`, including a
  Burnside control (`Σ_{all λ} dim² = n!`) that validates the hook-length code
  independently of anything two-row.
- `wenzl_level_two_vanishing.py` exit 0, witness JSON byte-identical.

## Files

- [`BallotNumbers.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/BallotNumbers.lean) — G5 for general `n`
- [`TwoRowDimCatalan.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/TwoRowDimCatalan.lean) — the SYT bridge
- [`MarkovGramDegenerate.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovGramDegenerate.lean) — `corank_general`, `gram_rank_le_catalan`
- [`two_row_ballot_catalan_reduction.py`](../../computations/probes/two_row_ballot_catalan_reduction.py) — the numerical control
