---
# qou-dqgp
title: 'TRIAGE: which LAYER each mechanism-5 producer''s quantity belongs to'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:47:01Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

## What this is

The **layer** half of `qou-aj91`. That bean's own recommendation was to fix
the STAMP first (`WitnessBuilder.q0Value` reporting the anchor the payload
used) and leave the layer question per-producer. PR #5699 does the stamp.
This is the per-producer layer decision, delivered as a triage rather than a
sweep.

- Audit: `docs/audits/2026-08-24-mech5-producer-layer-triage.md`
- Ledger: `docs/audits/2026-08-24-mech5-producer-layer-triage.json` (95 rows)
- Detector: `computations/audits/mech5_pin_bind_taint_audit.py`
- PR #5706 (draft)

## Three corrections to `qou-aj91`, measured 2026-08-24

**1. The population is 95, not 85 — a DETECTOR gap, not corpus churn.**
`q0_muon_population_partition.py` reports 51: it excludes `ROUTES_ANCHOR`
files by design (hiding all 26 rule-4 straddles, where a producer reads the
pin AND imports `q_parameter`) and gates on `json.load|read_text|open(`, which
hides the exact idiom `qou-aj91` quotes — `record_upstream(Q_PIN, ...)` opens
nothing of its own. A sixth read shape exists too: `bwhk_st_matrix_
corroboration` binds `q0Value`, not `derived_50_digit`, out of the same
witness. Two AST detectors find 79 and 74 with only 58 in common; union 95.
**Do not treat 95 as final either.**

**2. The predicted straddle is mostly NOT live.** Of the 76 committed
witnesses these producers emit: 25 stamped `muon` carry muon, 4 stamped
`proton`, 1 `independent`, and **46 carry no `q0Anchor` at all**. The dominant
state is SILENCE, not a lie — against rule 4's "say which pin you used". So
the stamp fix makes the two real contradictions VISIBLE rather than creating
them.

**3. Only 2 genuine declaration/data contradictions, not the 2 named.**
`qou-aj91` names `alpha_k_jones_markov_h12` and `per_atom_audit_witnesses`.
The first has **already migrated** — it takes q0 from
`q_parameter.Q_50_DIGIT_STR` and keeps the pin read only in a history comment.
(PR #5699's own finding 1 reaches the same conclusion independently.) The
actual pair is:

- `per_atom_audit_witnesses.py` — tagged `physical_proton`, witness stamped
  `proton` with the proton `q0Value`, `h` and `h^2` computed from the MUON
  anchor at line 70. Three declarations against one payload. Also carries a
  separate NO-FLOAT64 defect (`float(mp.mpf(...))` then all-float arithmetic).
- `gram_matrix_seminormal_h6.py` — untagged, binds `Q0_MP` from the muon pin
  at line 78, and `option-e-phase1-gram-h6.witness.json` carries
  `q0Anchor: "proton"` with the full 50-dps proton value.

## The triage

| bucket | n | disposition |
|---|---|---|
| A infra / already-correct | 4 | `q_parameter`, `_li_2_q_util`, the guard test, and the exemplar |
| B declared two-anchor comparison | 16 | DO NOT MIGRATE — removing the muon leg destroys the comparison |
| C legitimately muon | 8 | ideal/CAL-2 layer, AGENTS.md-named, or a frozen deprecated record |
| D contradiction | 2 | the real defects |
| E should be proton | 18 | untagged + Physical-Observations quantity |
| F hygiene | 39 | untagged structural probes; 11.54 ppb cannot move their conclusions |
| G needs the author | 8 | self-consistent `ideal_muon` on a physical quantity |

**The exemplar to copy is `probes/qbeta_habiro_residual_probe.py`.** It was in
this population and is already fixed, and the fix keeps BOTH reads with
distinct jobs: q0 from `q_parameter.Q_50_DIGIT_STR` by name, the pin witness
read only to feed `_assert_anchor_matches_value`. Reading the pin witness is
not the defect; BINDING q0 to it is.

## What needs the author (bucket G)

Eight producers are internally consistent — muon read, `ideal_muon` tag, muon
stamp — while computing a Physical-Observations quantity, which the 2026-08-07
directive puts on proton. The tag is a prior agent's declaration; overruling it
means re-tagging AND moving numbers. Two carry extra weight:

- `q1_mass_gap_probe.py` states PROTON intent in its own prose while tagged
  `ideal_muon` and stamped `muon` — the declaration conflicts with itself. It
  also co-reads `plancherel_weights_n3` and `two_q` from the pin witness, so
  re-pointing only its `["q"]` read would CREATE a straddle.
- `qbeta/qbeta_decay_sdp_extended_ck.py` — do not touch pending `qou-cds1`;
  the whole `c_k` ladder is convention-C-frame and awaits re-derivation.

## Fixed on PR #5706

`derived_masses.py::_q_0()` documented `q_parameter.Q_50_DIGIT_STR` as a
"legacy float64 fallback" that is "identical to ~50 digits". Measured, they
agree to **9** digits (separation -11.5371 ppb = the mu-p substrate tension),
and it is the experimental pin, not a legacy fallback. `derived_masses` is a
production module predicting mass and binding observables, so a stated
equivalence on its q0 accessor is exactly what stops a reader from
investigating. DOCSTRING ONLY — `ast.unparse` after docstring-strip is
byte-identical before and after.

## Deliberately NOT done

Routing the 57 `E`+`F` producers through `q_parameter`. That moves numbers in
57 places with no per-file review; the C->D precedent (`qou-2zjp`) shows such
a move reaching 14.741 %. It belongs to `qou-1c4y` under the recorded
2026-08-19 authorisation and its four constraints.

Also not measured: whether each `E` producer's numbers move by the full
11.54 ppb or by less. That needs a per-producer re-run — the sweep this
triage exists to scope, not to perform.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8332, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
