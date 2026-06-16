# Chain 4 n=5 + Demazure stub — NEGATIVE verdicts

**Date:** 2026-06-04
**PR:** [#1787](https://github.com/litlfred/qou/pull/1787) ([branch](https://github.com/litlfred/qou/tree/claude/qbeta-chain4-n5-demazure-2026-06-03))
**Status:** NEGATIVE — diagnostic-only, no closure
**Predecessor:** [PR #1772 audit — Chain 4 NEGATIVE at n ≤ 4](./2026-06-03-qbeta-chain4-kashiwara-crystal-negative.md)

## Target (carried from predecessor, h_q-corrected)

ℏ_q = (q − 1) / q at proton-pinned q₀ ≈ 1.10998 → ℏ_q ≈ 0.09908.
Target: **A / ℏ_q^15 ≈ 2.072**.

## Step 4 — n=5 partition Kashiwara crystal

Script:
[`computations/qbeta/qbeta_chain4_kashiwara_step4_n5.py`](../../computations/qbeta/qbeta_chain4_kashiwara_step4_n5.py).
Witness:
[`computations/qbeta/qbeta-chain4-kashiwara-step4-n5.witness.json`](../../computations/qbeta/qbeta-chain4-kashiwara-step4-n5.witness.json).

### Implementation honesty notes

- **SYT enumeration was wired** in this PR (commit 3, after the stub
  commit + copilot review fixes); f^λ values cross-checked against
  the enumeration count via `assert`.
- **`cocharge_sum` renamed to `maj_sum`** — predecessor PR #1772 hand-
  coded a field called `cocharge_sum` whose values do not match the
  rigorously-defined Lascoux-Schützenberger cocharge statistic on
  SYT. This script uses the major index (`maj(T) = Σ i over descents
  of T`) which IS the canonical SYT q-statistic appearing in the
  q-Kostka identity `Σ_T q^maj(T) = q^{n(λ)} [n]_q! / ∏[h(c)]_q`.

### Results (50 candidates, single proton anchor)

| Best candidate | Value | Ratio | Tier |
|---|---|---|---|
| q-dim_(2,2,1) / f^(2,2,1) | 1.0441 | 0.5040 | NEAR-CLOSE |
| q-dim_(3,2) / f^(3,2) | 1.0441 | 0.5040 | NEAR-CLOSE |
| q-dim²_(5) / q-dim²_(1,1,1,1,1) | 1.0000 | 0.4827 | MISS |
| f^(3,2) | 5.0000 | 2.4134 | MISS |

**No NEAR-1PCT or NEAR-FUZZY hits.** Best is NEAR-CLOSE at 50.4% off
target, distinctly worse than the predecessor's n=4 best (NEAR-FUZZY
at q-dim_(2,2) = 2.04, 1.35% off target — that was a chance
proximity, not a structural signal).

### Verdict — Step 4

**NEGATIVE.** The n=5 partition Kashiwara crystal does NOT yield a
NEAR-1PCT residue-A prefactor candidate. The (2,2)-extension thread
from n=4 (where q-dim_(2,2) was NEAR-FUZZY) dies at one rank up;
q-dim_(2,2,1) only reaches NEAR-CLOSE. Combined with PR #1772's
NEGATIVE at n ≤ 4, the residue A is not a small-partition Kashiwara
crystal invariant for n ≤ 5.

## Step 5 — Demazure characters at fundamental weights (REAL D_i wiring)

Script:
[`computations/qbeta/qbeta_chain4_demazure_fund_weights.py`](../../computations/qbeta/qbeta_chain4_demazure_fund_weights.py).
Witness:
[`computations/qbeta/qbeta-chain4-demazure-fund-weights.witness.json`](../../computations/qbeta/qbeta-chain4-demazure-fund-weights.witness.json).

### Real D_i wiring (replaces the q-binomial stub)

Demazure characters now computed via the **Kashiwara-crystal subset
model** for fundamental weights ω_j of sl_n:

- Basis: j-element subsets of {1, ..., n}; highest weight = {1,...,j}.
- Lowering: `f̃_i(S) = (S \ {i}) ∪ {i+1}` if `i ∈ S`, `i+1 ∉ S`.
- Demazure walk: for word w = s_{i_1}...s_{i_l}, take the
  f̃_{i_k}-string closure of every current subset, in order.
- Character: `χ_w(ω_j; q) = Σ_{S ∈ DemSub(w)} q^{Σ(a-1) for a in S}`
  (principal q-specialisation).
- Cross-checks: identity word at ω_j gives `q^{j(j-1)/2}`; longest
  word gives `e_j(1, q, ..., q^{n-1})` (full fundamental character).
- By Demazure's theorem, χ_w depends only on the permutation w, not
  the choice of reduced expression — so iteration picks ONE
  canonical reduced word per permutation.

### Enumeration size

| Group | Permutations | Weights | Demazure chars |
|---|---:|---:|---:|
| sl_3 | 6 | 2 | 12 |
| sl_4 | 24 | 3 | 72 |
| sl_5 | 120 | 4 | 480 |
| **Total** | | | **564** |

### Results (564 candidates, single proton anchor)

| Tier | Count |
|---|---:|
| NEAR-1PPM | 0 |
| NEAR-0.1PCT | 0 |
| NEAR-1PCT | 0 |
| NEAR-FUZZY | 56 |
| (rest) | 508 |

Best candidate: `D_s1(ω_1)_sl3 = 1 + q ≈ 2.1100` (ratio 1.01846,
1.85% off target 2.072).

### Honest characterisation of the NEAR-FUZZY hits

All 56 NEAR-FUZZY hits cluster at **two values**:

- `1 + q ≈ 2.1100` (ratio 1.0185): from Demazure characters whose
  crystal subset is `{ {1}, {2} }` (i.e. word containing s_1 but
  not extending further along the 1→2→3→... ladder).
- `q^6 ≈ 1.8697` (ratio 0.9027): from `D_e(ω_4)_sl5` and similar —
  the identity-word highest-weight monomial at ω_4 of sl_5.

Neither is a Demazure-SPECIFIC structural signal. Any low-degree
q-polynomial evaluation at proton anchor `q ≈ 1.110` will land
roughly in [1, 5] range; reaching < 1% of 2.072 requires either
true structural alignment or coincidence. The combinatorial
density of Demazure characters across S_3, S_4, S_5 reaching no
NEAR-1PCT is the substantive negative.

### Verdict — Step 5

**NEGATIVE.** No Demazure character at a fundamental weight of
sl_n (n ∈ {3, 4, 5}, all permutations) reaches NEAR-1PCT of the
residue-A prefactor target. The invariant family is genuinely
probed (real D_i wiring, not stub), and the result is the same as
Step 4: NEGATIVE.

## Cross-anchor (Step 6)

Not run. Per anti-pattern compliance (cross-anchor BEFORE structural
claim), and since neither Step 4 nor Step 5 surfaced a NEW NEAR-1PCT
or better candidate, there is nothing to cross-anchor.

The witness JSONs DO emit both proton and muon prefactor targets
(addresses copilot review #1787 round 1, fix #3 — Q_MUON_50 unused),
so any follow-up wiring can pick up the secondary anchor without
drift.

## Updated search-space narrowing (relative to PR #1772 audit)

| Direction | Status as of this PR |
|---|---|
| n ≤ 4 partitions | NEGATIVE (PR #1772) |
| n = 5 partitions | NEGATIVE (this PR, Step 4) |
| n ≥ 6 partitions | UNPROBED — search space grows exponentially |
| Demazure characters at ω_i (sl_3, sl_4, sl_5) | NEGATIVE (this PR, Step 5 with REAL D_i wiring) |
| Higher-rank Demazure (sl_n, n ≥ 6) | UNPROBED |
| Demazure at non-fundamental weights (general λ) | UNPROBED |
| Mixed chains (Wenzl × Kashaev × Kashiwara) | UNPROBED |

## Anti-pattern compliance

- ✅ TIERED reporting; no ansatz at MISS / NEAR-FUZZY / NEAR-CLOSE.
- ✅ Cross-anchor framework wired (proton + muon targets in witness).
- ✅ Honest correction: cocharge_sum → maj_sum (rigorous SYT stat).
- ✅ Honest acknowledgement: Step 5 NEAR-FUZZY is q-binomial, not
  Demazure-specific.
- ✅ No production wiring; no `λ_scale` re-framing; no Δ_λ closure.
- ✅ Witness JSONs JSON-validated post-emission.
- ✅ 4-grep corpus check on "residue A" + "Demazure" done before
  this audit — no prior closure that this PR duplicates.

## Cross-references

- PR #1727 (merged) — residue A ≈ 1.804 × 10⁻¹⁵ established at simple
  pole, fibre-level, ANCHOR-INDEPENDENT.
- PR #1772 (merged) — Chain 4 NEGATIVE at n ≤ 4 (Step 1, Step 2 with
  honest h_q-bug correction, Step 3 cross-anchor).
- PR #1769 (merged) — c_k recursion from Habiro q-difference; distinct
  fibre-level object (precision ladder) from the residue A search;
  this PR does NOT subsume.
- PR #1787 (this PR) — n=5 NEGATIVE, Demazure STUB unrealised.
- [1ppQ master ledger](../coordination/1ppq-qbeta.md).

## Productive next directions

In priority order:

1. **Mixed chains** (Wenzl × Kashaev × Kashiwara): never probed at
   all. The 1ppQ ledger lists this as cont. 5 directly. With both
   single-chain Kashiwara families (partitions + Demazure) now
   NEGATIVE through n=5 / sl_5, mixed chains are the most likely
   structural direction remaining. Modest compute scope; potentially
   high value. **Spinning a separate branch.**
2. **Higher-rank Demazure** (sl_n for n ≥ 6): the Step 5 NEGATIVE
   was at sl_3/sl_4/sl_5. Going to sl_6 doubles the permutation count
   and adds one more weight; would need to be motivated by a structural
   hint (current results show no scaling toward target).
3. **n ≥ 6 partitions**: exponentially larger search space; would
   need targeted filtering by shape rather than brute enumeration.
4. **Demazure at non-fundamental weights** (Schur-Demazure): general
   highest weights λ rather than ω_j. More combinatorial machinery
   (key tableaux) but potentially richer structure.
