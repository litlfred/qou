---
# qou-khmj
title: 'GAP: gen_q0_anchor_manifest.py does not detect three proton-pinned producers — fbor_normalisation_barsymmetry_probe, fbor_q3_is_qschur_plancherel_weight_probe, phase2b_dim_v21_bridge_derivation. All three import Q_MP/Q_50_DIGIT_STR from q_parameter (so NOT independent), but the generator omits them, so their witnesses ship with no q0Anchor and land in Q0_ANCHOR_MISSING. Fix the generator''s detection, not the manifest by hand.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T13:14:03Z
updated_at: 2026-10-04T15:12:53Z
parent: qou-2002
---


## 2026-08-23 — the bean was the small end of a much larger defect (PR #5550)

Root cause found, and it is TWO independent blind spots:

1. **`_producer_stem` was root-only** — looked for the producer in
   `computations/` only, so every witness under `probes/`, `qbeta/`,
   `substrate/` etc. returned None and was never even read. Measured: **700
   live** witnesses invisible (plus 153 `_deprecated/`) against 891 resolved.
   Manifest effect: `ideal_muon` **3 → 111**, `physical_proton` 406 → 497,
   `ambiguous` 1 → 32. Fixed in PR #5550.

   Severity is bounded and one-directional: `q_parameter` resolves an unlisted
   stem to **proton** (standing default), so proton-intended subdirectory
   producers were right by accident, muon-intended ones were silently given
   proton, and `ideal_muon` was unreachable outside root. 108 producers whose
   committed witnesses carry the muon fingerprint were resolving to proton on
   re-run — same class as the Q0_FLIP 262 incident, one layer down.

2. **Detection is by the q₀ value SERIALIZED in the witness.** A producer that
   reads q₀ without recording it is invisible even with (1) fixed. This is why
   the three witnesses that opened this bean are STILL absent after #5550.

**This bean stays open for (2)** — the producer-side fix: make
`fbor_normalisation_barsymmetry_probe`, `fbor_q3_is_qschur_plancherel_weight_probe`
and `phase2b_dim_v21_bridge_derivation` record the q₀ they read. That is also
the right thing independent of detection, per the standing directive to say
which pin a witness used.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-23 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

---

## Verification & Fix Update (2026-11-15 — Owner Ruling Q-9NNZ-2 = 1)

- **Status:** Kept `in-progress` pending owner review/merge of PR [`litlfred/qou#8082`](https://github.com/litlfred/qou/pull/8082) (`1076c65f2a00f2604e1ba22458355ff382e7bde9`).
- **Verified on `main` & Completed in PR #8082 (`1076c65f2a`):**
  1. Verified on `main` (`27f26d2616`, `2026-08-23`): `phase2b_dim_v21_bridge_derivation.py`, `fbor_normalisation_barsymmetry_probe.py`, and `fbor_q3_is_qschur_plancherel_weight_probe.py` call `resolve_q0_anchor(__file__)` and stamp `q0Anchor: "proton"` + `q0Value` in their committed witnesses.
  2. Identified and fixed the remaining manifest generator gap in PR [`litlfred/qou#8082`](https://github.com/litlfred/qou/pull/8082) (`1076c65f2a`): updated `_producer_stem()` in `computations/gen_q0_anchor_manifest.py` to check `<stem>_probe.py` and `<stem>_derivation.py`, and added `fbor_normalisation_barsymmetry_probe`, `fbor_q3_is_qschur_plancherel_weight_probe`, and `phase2b_dim_v21_bridge_derivation` to `physical_proton` in `computations/q0_anchor_manifest.json` so `q0_anchor_is_declared()` returns `True` for all three producers.
