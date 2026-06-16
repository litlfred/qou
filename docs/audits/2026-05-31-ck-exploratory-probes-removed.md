# Exploratory c_k / d_k probes — removed from paper (2026-05-31)

> **Purpose.** Records 9 content blocks that were removed from the QOU
> paper because their primary content was a **negative / falsified / near-
> match** empirical probe rather than a derivation. Their intellectual
> content (the negative findings + structural leads they surfaced) is
> preserved here so it remains discoverable without polluting the
> scholarly paper with retracted material. Companion to the
> [`Q_β bridge narrowing`](2026-05-31-qbeta-bridge-narrowing.md) and
> the [`1 ppQ coordination ledger`](../coordination/1ppb.md).
>
> **Why removed.** Per the author (2026-05-31): "we don't want negatives
> experimentally probed in the paper". These blocks documented
> mechanisms (c_3 = J_Hopf, c_4 = b² + ½, c_5/c_6 per-block, α_5 J-M
> centrality, etc.) that subsequently turned out to be q₀-dependent
> near-matches or were superseded by later structural work. Each block
> already carried an errata / "Status: open R&D" / "Status: falsified" /
> "negative-result" tag — the right home for that content is the audit
> ledger, not chapter prose.
>
> **Reversibility.** All blocks are recoverable from git history at the
> commit referenced below; the cut is a paper-hygiene action, not data
> loss.

## Cut list (9 blocks, 26 files)

| # | label | kind | siblings | core finding (preserved below) |
|---|-------|------|----------|-------------------------------|
| 1 | `prop:hopf-jones-c3-categorical` | proposition | .ts .md .lean .qa.json | `c_3 = J_Hopf(q=1) = -2`: 3.35% near-match at canonical (m_p-pin) q₀, NOT Taylor-exact — refuted by [`item-1 Δtr_M vs Form A test`](../../computations/qbeta/qbeta-delta-tr-vs-formA.witness.json). Locked behind §3b-cond `QbetaC3StructuralFormClass` in `q-beta-categorical-precision-ladder.lean`. |
| 2 | `prop:kashiwara-jones-c4-categorical` | proposition | .ts .md .lean .qa.json | `c_4 = b² + ½`: own errata banner already superseded it (9.5% off, sign-flipped). The Jones × Kashiwara mixing pattern (`c_4 = c_3·b⁴`) is itself a q₀-dependent near-match. |
| 3 | `rem:per-wedderburn-block-c5-c6` | remark | .ts .md .lean .qa.json | dim_q² and y_λ per-block decompositions both FALSIFIED at c_3 (dim_q² gives −8 not −2; `Σ y_λ(q₀) = 0.719 ≠ 1`). No known non-trivial uniform per-block rule. Cross-confirmed by `qbeta_per_block_uniform_rule_verify.py`. |
| 4 | `rem:alpha-5-jm-central-empirical-findings` | remark | .ts .md .qa.json | Tagged `"negative-result"`. α_5 J-M centrality was investigated as a shell-correction route; finding was negative (atom-dependent, no clean structural form). |
| 4a | `…-table1-data` | table | .ts .md | (data table accompanying #4) |
| 4b | `…-table2-data` | table | .ts .md | (data table accompanying #4) |
| 5 | `prose:derivation-audit-report` | prose | .ts .md .qa.json | 259-line internal audit cataloguing empirical/fitting/numerology dependencies. Belongs in `docs/audits/`, not paper prose. The current authoritative audit is [`docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md`](2026-05-30-qbeta-ck-mp-dk-deep-audit.md) (read the ADDENDUM, not the body) + the addendum-consistent [bridge narrowing](2026-05-31-qbeta-bridge-narrowing.md). |
| 5a | `…-table1-data` | table | .ts .md | (data table accompanying #5) |
| 5b | `tbl:derivation-audit-report-table2-data` | table | .ts .md | (data table accompanying #5) |

Total: 9 blocks, 26 files. Zero Lean importers depended on the Lean
siblings (verified before cut), so no downstream Lean breakage.

## Manifest edits

- `content/quantum-observable-universe/mass-theory/mass-theory.ts`:
  removed 7 block names from 4 section block-lists.
- `content/quantum-observable-universe/mass-endomorphism/mass-endomorphism.ts`:
  removed 1 block name.

## Cross-links to canonical findings

The negative findings that motivated these blocks are now canonically
captured in two places (single source of truth):

1. **Q_β bridge narrowing** —
   [`docs/audits/2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md).
   Lists six ruled-out mechanisms for the open `f` bridge, including the
   c_3 = J_Hopf, geometric/Li_2^q E_0 towers, dim_q², and y_λ per-block
   routes (mechanisms #1, #3–#6 below the §-line in that doc — items
   #1–4 of the cut list above are sub-cases of those mechanisms).

2. **Deep audit ADDENDUM** —
   [`docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md` § ADDENDUM](2026-05-30-qbeta-ck-mp-dk-deep-audit.md#addendum-2026-05-30-same-day--fourth-flip-flop-discovered).
   The discipline lock: only Taylor-exact (residual < compute precision
   at canonical q₀) wires to production. q₀-dependent residuals = form-
   fitting. Only c_2 = −1 passes.

3. **1 ppQ coordination ledger** —
   [`docs/coordination/1ppb.md`](../coordination/1ppb.md).
   The cross-PR / cross-session ledger driving the 1 ppQ programme;
   tracks which observables are at the substrate floor vs the open
   bridge.

## What stays in the paper (NOT cut)

These blocks were also identified by the sweep but are LEGITIMATE
content and remain in the paper:

| block | why kept |
|-------|----------|
| `conj:depth-stratified-frobenius-reciprocity` | genuine open conjecture (`kind: conjecture`), not a falsified probe |
| `rem:hecke-algebra-type-scaffold` | Lean-infrastructure TODO scaffolding; has an inbound `uses` ref from `markov-trace-operator-construction.ts` |
| `conj:brane-tower-z-habiro` | genuine open conjecture |
| `rem:ck-extraction-from-algebraic-rules` | has errata banner but body remains useful for algebraic-rules exposition |
| `prop:frobenius-gram-matrix` | has errata banner but the proposition itself is valid |
| `conj:e-hartree-categorical-derivation` | conjecture with a sub-hypothesis that was falsified — flagged in-block, not the block's whole content |
| `rem:m-tau-knot-prediction` | observational note with a §F5 component falsified — the rest is a valid observation |
| `rem:chi-v21-hoefsmit-matrix-derivation` | structural derivation, status field flags work-in-progress not falsification |

## Discipline rule for future authoring

A content block whose **primary content is a negative empirical finding**
("hypothesis falsified", "near-match X% off", "Status: open R&D — no
known rule") should be written as an entry in `docs/audits/` from the
start, not as a paper block. Paper blocks (definition / proposition /
remark / conjecture / prose) are for canonical content — derivations,
genuine open conjectures, structural exposition. Falsified probes are
audit material.
