# Chain 4 Kashiwara Crystal — NEGATIVE at n≤4 (with honest Step-2 ℏ_q bug correction)

**Date:** 2026-06-03
**PR:** #1772 ([claude/qbeta-chain4-kashiwara-2026-06-03](https://github.com/litlfred/qou/tree/claude/qbeta-chain4-kashiwara-2026-06-03))
**Status:** NEGATIVE — diagnostic-only, no closure

## Scope

Per 1ppQ ledger (cont. 5):
> "the residue A categorical-ID must be a TRUE Kashiwara CRYSTAL operator value — Option-E path (Chain 4)"

PR #1772 Chain 4 surveyed Kashiwara crystal invariants of partitions of n=3 (Step 1) and n=4 (Step 2) for a NEAR-1PPM or tighter match to the residue A prefactor `A / ℏ_q^15` at proton-pinned q₀.

## Step-2 ℏ_q bug (honest correction)

**Bug:** Step 2 hard-coded `H_Q_SUBSTRATE = 0.0922502` for the ℏ_q value, giving a prefactor target of ≈ 6.47.

**Correct formula:** ℏ_q = (q - 1) / q, per [`qbeta_residue_categorical_id_probe.py`](../../computations/qbeta/qbeta_residue_categorical_id_probe.py) line 48. At q_proton ≈ 1.10998:
- ℏ_q = 0.09908 (not 0.0922502)
- ℏ_q^15 ≈ 8.71 × 10⁻¹⁶
- A / ℏ_q^15 ≈ **2.07** (not 6.47)

**Impact:** Step 2's reported NEAR-1PCT for `cocharge_(1,1,1,1) = 6` was a bug artifact, NOT a single-anchor near-match. Caught by Step 3's cross-anchor diagnostic ([`qbeta_chain4_kashiwara_step3_cross_anchor.py`](../../computations/qbeta/qbeta_chain4_kashiwara_step3_cross_anchor.py)).

## Diagnostic verdicts

### n=3 partitions (Step 1)

All 11 enumerated candidates: MISS at corrected target ≈ 2.07. f^λ ≤ 2 for n=3 partitions; combinatorial invariants too small.

### n=4 partitions (Step 2, re-checked at corrected target)

37 candidates surveyed. Best results:

| Candidate | Value | Ratio to target ≈ 2.07 | Tier |
|---|---|---|---|
| q-dim_(2,2) | 2.04371 | 0.98647 | **NEAR-FUZZY** (1.35% off) |
| cocharge_(2,2) | 2 | 0.96538 | **NEAR-FUZZY** (3.46% off) |
| f^(2,2) | 2 | 0.96538 | **NEAR-FUZZY** (3.46% off) |
| f^(3,1) | 3 | 1.4481 | MISS |
| cocharge_(1,1,1,1) | 6 | 2.896 | MISS |
| q-dim_(3,1) | 3.04371 | 1.4692 | MISS |

**No NEAR-1PCT or tighter survives.** Per Δ_λ-gate + the c_3 4-session flip-flop history, NEAR-FUZZY (≥ 1% off) does NOT cross the bar.

### Cross-anchor (Step 3)

For the n=4 (2,2) candidate q-dim_(2,2) ≈ 2.04:
- q-dim is q-DEPENDENT; computed at q_proton and q_muon.
- The two anchors differ by ≈ 1.05 × 10⁻⁷ in q, ≈ 1.6 × 10⁻⁶ in ℏ_q^15.
- q-dim_(2,2) at the two anchors is approximately identical (q-dim is smooth in q).
- The NEAR-FUZZY tier at both anchors does NOT improve to NEAR-1PCT.

## Verdict

**Chain 4 at n ≤ 4: NEGATIVE.** No Kashiwara-crystal invariant of partitions of n ≤ 4 identifies the residue A categorically within the Δ_λ-gate-required tightness (NEAR-1PCT or tighter, both-anchor).

## Anti-pattern compliance

- ✅ TIERED reporting (no ansatz proposed at MISS or NEAR-FUZZY tier).
- ✅ Cross-anchor BEFORE any structural claim.
- ✅ Honest acknowledgement of Step-2 bug (no swept-under).
- ✅ No production wiring.
- ✅ Witness JSONs emitted: `qbeta-chain4-kashiwara-{crystal-scaffold,step2-n4,step3-cross-anchor}.witness.json`.

## Why this NEGATIVE matters

Per CLAUDE.md "Before declaring 'open' math" §, every NEGATIVE result tightens the search space. After Chain 4 n ≤ 4:

- The residue A is NOT a "small categorical invariant" from a low-partition Kashiwara crystal.
- The natural next directions (per ledger cont. 5 + this audit) are:
  - **n = 5 or higher partitions** — exponentially larger search space.
  - **Demazure character coefficients** at fundamental weights — different invariant family.
  - **Mixed-chain combinations** (Wenzl × Kashaev × Kashiwara) — not yet probed at all.

## Cross-references

- PR #1727 (merged) — established residue A ≈ 1.804 × 10⁻¹⁵ at simple pole, fibre-level, ANCHOR-INDEPENDENT.
- PR #1750 (merged) — Markov-trace SHAPE collapse; established c_k are L2/Markov-invariant.
- PR #1760 (open) — Chain 1 (Q_β Habiro element) family γ PASS, α + β NEGATIVE; original Chain 4 pointer.
- PR #1761 (merged) — general H_n(R, q) Lean lift of T_β = S·1.
- [1ppQ master ledger](../coordination/1ppq-qbeta.md) — sessions log.
- Existing residue search: [`qbeta_residue_categorical_id_probe.py`](../../computations/qbeta/qbeta_residue_categorical_id_probe.py) — 38 candidates across 6 hypothesis families, all NEGATIVE (best near-match `[2]_q · ℏ_q^15 · Schwinger` at 2.93% miss).
