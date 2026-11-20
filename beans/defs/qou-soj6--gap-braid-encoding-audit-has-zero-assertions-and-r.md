---
# qou-soj6
title: 'GAP: braid_encoding_audit has ZERO assertions and reports allPassed=true'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T15:12:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---

`computations/audits/braid_encoding_audit.py` runs to **exit 0** and writes a
witness with **zero assertions** and **`allPassed: true`** — measured on both the
committed witness and a fresh run. **It cannot fail.** Whatever it audits, it
reports nothing about, and any consumer reading `allPassed` gets a green light.

This is pre-existing and not caused by the missing input — the committed witness
also has 0 assertions — but the missing input compounds it. The audit loads
`atomic-braid-mass-table.witness.json` (deleted 2026-05-19, commit
`7f30a57924d`, owner directive) behind an `.exists()` guard and substitutes

    s3 = ... if s3_path.exists() else {"data": {"rows": []}}

so `s3_rows` is `{}`. Every downstream read is then a `.get(...)` that returns
`None`:

    line 426:  raw = s3_rows.get(key, {}).get("term1_atomic_total")
    line 436:  "strategy_3_tr_M_missing": s3_rows.get("p", {}).get(...)
    line 448:  "strategy_3_tr_M_missing": s3_rows.get("n", {}).get(...)

**So it is an audit with no assertions, running on an empty dataset, reporting
green.** That is the `qou-srvu` vacuous-green shape in its strongest form.

## What is NOT claimed here

That its non-assertion output is wrong. The fresh run and the committed witness
differ **only in provenance** (`scriptCommitSha`, `pyhecke_native_build`,
`engineVersion` mpmath 1.3.0 → 1.4.1) — **no number moved**. Its data is
reproducible; it simply makes no checkable claim.

## The fix is a design question, not a mechanical one

The obvious move — assert the upstream is present — would make it **permanently
red**, since the input was deliberately deleted and cannot come back. So the
real options are:

1. give it assertions over the inputs it *does* have (option-b proton chain,
   Markov-trace assembly), and drop the Strategy-3 arm;
2. retire it with the other legacy consumers (`qou-s1yn`);
3. leave it, and have the vacuous-green ratchet flag it as a known exemption.

Not decided here. Recommendation (judgement): **1** — the audit has two other
live upstreams, so it can be made falsifiable without resurrecting anything.

Found while triaging the six remaining consumers of the removed witness.


## THE 43% ASSERTION INVESTIGATED — it is not two values, it is FIVE

Probe: `computations/probes/trm_proton_five_values_census.py`.

| value | source | status |
|---|---|---|
| **1.884319467254976** | `option-b-proton-mass-full-chain.witness.json` | **VERIFIED CANONICAL** |
| 1.88432 | axiomatic content block (hardcoded in the audit) | matches, 2.83e-7 |
| **1.6331535640480814…** | `TR_M_AT_Q0["p"]` in `canonical_a_k_magnitude_audit.py` | **13.33 % off, and LIVE** |
| 1.0653062285923893 | `markov-trace-assembly-proton.derivation.json` | 43.46 % off, unexplained |
| ≈ 2.12258 | the deprecated producer's own docstring | 12.64 % off, unexplained |

**Which one is right is settled, not assumed.** Recomputing
`Σ_λ y_λ · χ^λ(σ₁⁷σ₂⁴)` over λ ⊢ 3 with the canonical Wenzl-bridge weights at
the proton pin gives **1.88431946725497503**, reproducing the option-b value to
**5.17e-16** — machine precision. So option-b *is* the canonical Jones–Markov
trace, derived here rather than trusted.

### Four explanations ruled out, each by measurement

- **The pin.** Characters move only in the 8th significant digit between pins;
  the full trace goes 1.884319467 → 1.884319714. An 11.5 ppb change cannot make
  a 43 % gap.
- **Convention C.** `_y_lambda_at_convention_C_HISTORICAL` returns the **same**
  weights as the live accessor at n = 3 (0.5054042265, 0.2472978867, 0) and the
  **same** total. Worth recording, because "it's convention C" is the first
  hypothesis anyone reaches for here — and it is wrong.
- **The braid word.** σ₁⁷σ₂⁴ and its reverse both give 1.884319467; (σ₁σ₂)³
  gives 1.4398, σ₁³σ₂³ 0.7200, σ₁²σ₂² 1.2726. None is 1.0653.
- **A normalisation, or the other weight family.** option-b ÷ {[2]_q, [3]_q,
  [3]_q!, q, q², q³, √[3]_q} = {0.9371, 0.6191, 0.3079, 1.6976, 1.5294, 1.3779,
  1.0801}; `W_λ = d_q²/[3]_q!` gives 1.2424. None is 1.0653.

### The one that matters operationally

**1.63315 is not an archived number.** It is `TR_M_AT_Q0["p"]`, imported by the
**live** `build_markov_trace_assembly_neutron_chain.py` (via the `["n"]` entry)
and by `phase5/phase2_proton_m_e_hecke_diagnostic.py`. `braid_encoding_audit`'s
own comment already identified 1.63315 as the value that "disagreed with this
audit's own upstream by 15 %" — **the content block was migrated and this
constant was not.**

### Scope, and what is NOT done

This establishes which value is canonical and rules out four explanations for
the others. It does **not** establish what 1.0653, 2.12258 or 1.63315 *are*, and
**changes none of them**: `TR_M_AT_Q0` feeds live producers, so correcting it
moves published numbers and belongs in its own tranche with a diff.

Also noted: the derivation file carries **no provenance at all** — no
`scriptFile`, no `commitSha`, no `engine` — and its producer
`build_markov_trace_assembly_chain.py` is in `_deprecated/`, while its own
docstring states a *third* value (≈2.12258) that contradicts the file it writes.



## Cross-reference 2026-09-06 — a SEVENTH value, recorded on `qou-7zff`

The canonical chi cache moved again on the 2026-09-05 intra-ordering ruling
(`qou-hu1f`) and now holds `0.62932840220292191817…` (proton) /
`0.47513351715568221251…` (neutron) — matching none of the five in this bean's
census, nor the sixth. Cache-before/after ratios **1.82060** and **2.07887**.

Two things worth carrying back here: the `1.0653` claimant has **two spellings**
in the tree (`…62285923893` in the census, `…62380758782` in a live assertion),
and `gap_a4_T2_per_knot_vol_probe_perknot_rerun`'s `*_matches_documented`
assertions were **already red before** the regeneration — they report a real
disagreement and must not be re-pinned. Full measurement on `qou-7zff`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8407, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
