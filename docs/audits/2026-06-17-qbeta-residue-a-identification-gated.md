# Q_β residue-A categorical ID is GATED on exact c_k (feasibility prune)

**Date:** 2026-06-17
**Status:** formalize-first feasibility assessment (no search run — it would be premature)
**Context:** PR #1727 (`2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`)
left an open target: *identify the dominant simple-pole residue `A ≈ 1.804e-15`
categorically* (candidates `ℏ_q^N` / `(b·ℏ_q²)^N` / `b^N·ℏ_q^M`). This note
checks whether that identification is feasible **now**, before running it.

## The data does not support an identification yet

The dominant pole of `G(u) = Σ c_k u^k` is at `u_substrate ≈ 0.008517`; the
residue is `A = (c_k·u_substrate^k)·u_substrate` (simple-pole tail constant ×
`u_substrate`). Two independent reads of the tail constant `c_k·u^k` (k=8–10):

| extraction | tail const `c_k·u^k` | spread | ⇒ `A` |
|---|---|---|---|
| raw (PR #1727 anchor) | `2.118e-13` | **0.02%** | `1.804e-15` |
| bias-corrected (PR #1839 cross-check) | `7.06e-14` | **200%** | `~6.0e-16` |

(witnesses: `qbeta-singularity-type-probe.witness.json`,
`qbeta-radius-of-convergence-gate-probe.witness.json`; the latter notes
"bias-corrected c_8+ **ARE noisy** — precision-floor refuted-class".)

The two reads disagree by **~3×**, and the bias-corrected one has a **200%**
spread. So `A` is currently known to **less than one significant figure** once
the extraction bias is accounted for.

## Why that kills identification now (entropy bound)

Per the PSLQ entropy discipline (CLAUDE.md §"Formalize-first probe discipline";
[PR #1805]): identifying a closed form from a candidate class needs
`precision > n_terms · log10(2·height)` significant figures. Even a 1-constant
candidate (`ℏ_q^N`, `(b·ℏ_q²)^N`) at modest height needs ~10 figures to be
decisive. With `A` uncertain by 3× (≈ 0.5 figures), **any** candidate "matches"
— the search would manufacture a false near-match (the c_k flip-flop failure
mode). So the residue-A identification is **not run here**.

## Unblock

Reliable high-precision `c_k` — i.e. **the exact operator-level extraction in
PR #2106 (Hoefsmit Stage B)**, which replaces the noisy SDP/bias-corrected c_k
with exact per-block values. Once #2106 lands exact `c_8…c_{12}` to ≥ 12
figures, `A` is pinned to ≥ 10 figures and the named-candidate test
(`ℏ_q^N` / `(b·ℏ_q²)^N` / `b^N·ℏ_q^M`, tiered, cross-anchor, no fit) becomes
decisive. Until then, residue-A ID is **gated**, not open.

## Cross-references
- Dominant simple pole + residue: `2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md` (PR #1727)
- Subdominant (silver/`Q_A`) pole: `2026-06-17-qbeta-silver-pole-subdominant-correction.md` (PR #2454)
- Noisy bias-corrected c_8+: `qbeta-radius-of-convergence-gate-probe.witness.json` (PR #1839)
- Exact c_k unblock: PR #2106 (Hoefsmit Stage B)
