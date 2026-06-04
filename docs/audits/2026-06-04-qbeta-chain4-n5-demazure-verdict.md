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
[`folio-assistant/computations/qbeta/qbeta_chain4_kashiwara_step4_n5.py`](../../folio-assistant/computations/qbeta/qbeta_chain4_kashiwara_step4_n5.py).
Witness:
[`folio-assistant/computations/qbeta/qbeta-chain4-kashiwara-step4-n5.witness.json`](../../folio-assistant/computations/qbeta/qbeta-chain4-kashiwara-step4-n5.witness.json).

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

## Step 5 — Demazure character STUB

Script:
[`folio-assistant/computations/qbeta/qbeta_chain4_demazure_fund_weights.py`](../../folio-assistant/computations/qbeta/qbeta_chain4_demazure_fund_weights.py).
Witness:
[`folio-assistant/computations/qbeta/qbeta-chain4-demazure-fund-weights.witness.json`](../../folio-assistant/computations/qbeta/qbeta-chain4-demazure-fund-weights.witness.json).

### Stub status (NOT a true Demazure character probe)

The current script does NOT enumerate reduced Weyl-group words or
apply Demazure operators D_i. It returns q-binomials
`[n−1 choose j−1]_q` as a representative proxy. This is mathematically
the FULL character of the j-th fundamental representation of sl_n
(not a Demazure-truncated partial character), which the stub
explicitly documents.

### Results (10 candidates, single proton anchor)

| Best candidate | Value | Ratio | Tier |
|---|---|---|---|
| D_full(ω_2)_sl3 = [2]_q | 2.0109 | 0.9706 | NEAR-FUZZY |
| Σ D_full(ω_1) [sl3, sl4, sl5] | 3.0000 | 1.4481 | NEAR-CLOSE |
| D_full(ω_2)_sl4 = [3]_q | 3.0437 | 1.4692 | NEAR-CLOSE |

### Honest acknowledgement

The Step 5 stub surfaces a NEAR-FUZZY at `D_full(ω_2)_sl3 ≈ 2.0109`,
which is **literally `[2]_q = q + q⁻¹` at proton anchor**. This is
already in the predecessor's existing residue-A candidate set
(per PR #1772 audit § "Cross-references": `[2]_q · ℏ_q^15 · Schwinger`
at 2.93% miss is the prior best NEAR-FUZZY). So:

- The NEAR-FUZZY is **NOT a Demazure-specific finding**.
- The stub does **NOT realize the Demazure invariant family**.
- A true Demazure probe requires wiring D_i operator action on the
  Weyl module — deferred to a follow-up.

### Verdict — Step 5

**STUB-NEGATIVE.** No new finding. The single NEAR-FUZZY is the
already-known [2]_q duplicate. The true Demazure invariant family
remains unprobed; this PR closes neither way.

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
| Demazure characters at ω_i | UNPROBED — stub did not realize the family |
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

1. **Real Demazure characters at ω_i**: wire D_i operator action,
   enumerate reduced words, compute partial characters. The stub
   leaves this UNPROBED. ~1 day of compute work; high value.
2. **Mixed chains** (Wenzl × Kashaev × Kashiwara): never probed at
   all. The 1ppQ ledger lists this as cont. 5 directly. Modest
   compute; potentially high value.
3. **n ≥ 6 partitions**: exponentially larger search space; would
   need targeted filtering by shape rather than brute enumeration.
