# Chain 4 continuation — n=5 partitions + Demazure characters — PLAN

**Date:** 2026-06-03
**Branch:** `claude/qbeta-chain4-n5-demazure-2026-06-03`
**Status:** PLAN — diagnostic-only, no closure claim
**Predecessor:** [PR #1772 audit — Chain 4 NEGATIVE at n ≤ 4](./2026-06-03-qbeta-chain4-kashiwara-crystal-negative.md)

## Why this branch exists

The Chain 4 Kashiwara-crystal sweep at n ≤ 4 was NEGATIVE (no
NEAR-1PCT or tighter, both-anchor) — see the predecessor audit.
The predecessor explicitly listed two natural next directions
that haven't been probed:

1. **n = 5 (or higher) partitions** — exponentially larger search
   space; the n=4 sweep produced NEAR-FUZZY hits at q-dim_(2,2)
   and cocharge_(2,2), so the (2,2)-shaped (`f̃₁²`) family still
   has structural pull and may sharpen at one rank up.
2. **Demazure character coefficients at fundamental weights** —
   different invariant family from f^λ / cocharge / q-dim. Key
   tableau (Lascoux-Schützenberger) machinery; coefficients at
   fundamental weights ω_i of sl_n have no direct analog in the
   `partition_invariants_n4` candidate set probed so far.

Both directions remain **diagnostic-only**. Per Δ_λ-gate + the
c_3 4-session flip-flop, only NEAR-1PCT both-anchor crosses the
bar; this PR will report TIERED results without ansatz.

## Target (re-stated, h_q corrected)

Per the predecessor audit's honest correction:

- ℏ_q = (q − 1) / q at proton-pinned q₀ = 1.10997858…
- ℏ_q ≈ 0.09908 (not the buggy 0.0922502 from Step 2)
- ℏ_q^15 ≈ 8.71 × 10⁻¹⁶
- **A / ℏ_q^15 ≈ 2.07**

This is the corrected target carried into Steps 4 and 5 of Chain 4.

## Scope

### Step 4 — n=5 partitions

7 partitions: `(5)`, `(4,1)`, `(3,2)`, `(3,1,1)`, `(2,2,1)`,
`(2,1,1,1)`, `(1,1,1,1,1)`. Per-partition invariants:

| invariant | formula |
|---|---|
| f^λ | n! / ∏ h(c) (hook-length formula) |
| hook product | ∏ h(c) over cells |
| cocharge_sum | Σ over SYT(λ) of cocharge(T) |
| q-dim_q(λ) | [n]_q! / ∏ [h(c)]_q at q = q₀ |
| (2,2,1)-projection | (2,2)-shaped sub-invariants extended by 1 cell |

Candidate set: per-partition values + cross-partition sums +
ratios suggested by Lean reference `f̃₁²` (continuing the
square-shape thread from n=4).

Script: [`computations/qbeta/qbeta_chain4_kashiwara_step4_n5.py`](../../computations/qbeta/qbeta_chain4_kashiwara_step4_n5.py).
Witness JSON emitted to
`computations/qbeta/qbeta-chain4-kashiwara-step4-n5.witness.json`.

Decision rule (per predecessor audit anti-pattern compliance):

- ≥ NEAR-1PCT at proton anchor → compute at muon anchor (Step 5b
  cross-anchor)
- NEAR-FUZZY only → record as MISS, no structural claim
- ZERO survivors → audit doc records terminal NEGATIVE for n=5

### Step 5 — Demazure characters at fundamental weights ω_i

Demazure characters are partial sums of Weyl characters obtained
by Demazure operators along reduced Weyl-group words. For sl_n
at fundamental weight ω_i, the characters are described by
key tableaux (Lascoux-Schützenberger).

Plan: for sl_3 (= H_n(q) at n=3, dual to the residue-A search)
and sl_4 (matching the n=4 negative result), compute:

- D_w(ω_i) for w running over reduced words in S_n
- Specialise at q₀ → numerical character coefficients
- Compare against A / ℏ_q^15 ≈ 2.07

Script: [`computations/qbeta/qbeta_chain4_demazure_fund_weights.py`](../../computations/qbeta/qbeta_chain4_demazure_fund_weights.py).
Witness JSON emitted to
`computations/qbeta/qbeta-chain4-demazure-fund-weights.witness.json`.

### Step 6 — Cross-anchor sweep (only if a Step 4 or 5 candidate
NEAR-1PCT at proton anchor)

Re-compute the surviving candidate at muon-anchor q₀ ≈ 1.10997869.
Per the c_k Im(q) fibre-vs-archimedean distinction (AGENTS.md
§"Critical framing — Im(q)"), a real-valued ANCHOR-DEPENDENT
near-match remains valid as a fibre-level diagnostic; what we
flag is anchor-SWING > 1% (the c_3 flip-flop pattern).

## Anti-pattern compliance (per AGENTS.md "Before declaring open math")

- ✅ TIERED reporting; no ansatz at MISS or NEAR-FUZZY.
- ✅ Cross-anchor BEFORE structural claim.
- ✅ No production wiring; no `λ_scale` re-framing; no Δ_λ closure
  claim.
- ✅ Witness JSONs emitted per script (script_hash + commit_sha).
- ✅ Compute-author discipline: `.qa.json` sidecars regenerated
  on commit.
- ✅ Honest 4-grep checklist on any "open" declaration in audit.

## Predecessor commits (PR #1772, on main)

- `b7863ac04a` — block(qbeta): content-block triple for general-lift T_β = S·1
- `720ea7422e` — scaffold(qbeta): Chain 4 Step 1 Kashiwara crystal diagnostic
- `188ed30e9d` — diagnostic(qbeta): Chain 4 Steps 2+3 with HONEST h_q-bug correction
- `9708bba525` — review(copilot #1772): order-class prose + 1_A in title
- `0c8acb2403` — audit(qbeta): Chain 4 Kashiwara crystal NEGATIVE at n≤4

## Open questions for this PR to answer (in order)

1. Does any n=5 partition invariant reach NEAR-1PCT both-anchor?
2. Does any Demazure character coefficient at a fundamental weight
   reach NEAR-1PCT both-anchor?
3. If both NEGATIVE: does the c_k recursion approach (PR #1769,
   recently landed on main) subsume the residue-A search, or are
   c_k and residue-A genuinely distinct fibre-level objects?

Question 3 is informational only and recorded as ledger update,
not closure.
