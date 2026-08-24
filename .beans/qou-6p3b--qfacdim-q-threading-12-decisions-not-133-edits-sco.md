---
# qou-6p3b
title: 'qfac/dim_q threading: 12 decisions, not 133 edits (scoped)'
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:15:32Z
updated_at: 2026-08-24T14:16:17Z
---

## Scoped 2026-08-24 — full analysis in docs/audits/2026-08-24-qfac-dimq-threading-scope.md

Follow-on to `qou-wee5` (closed, #5646). **The site count is the wrong unit.**

### Measured (main @ b134176d93)

    191 call sites; 47 already pass q; 144 defaulted
    -11 generated qou-mass mirror (regenerated, never hand-edited)
    = 133 LIVE in 67 files -> 114 in producers, 19 in library modules

Producer sites by their own manifest bucket: 85 unlisted (->proton),
28 physical_proton, **1 ideal_muon**.

### The reframe

The anchor is a property of the RUNNING PROCESS, not the file. Threading
`Q0_PROTON` is **inert wherever the entry point already resolves proton — 113
of the 114 producer sites.** Those edits change no number today.

Real cost = entry points that can resolve muon AND reach these functions:
**12 muon producers.** And **11 of the 12 reach them INDIRECTLY**, via
`mass_at_3A_proper` / `hecke_characters` — only
`qbeta_hoefsmit_tbeta_matrix_build_probe.py:124` calls `dim_q` directly.

**So editing 133 call sites would leave the 11 exactly as they are.**

### Known failure mode, already paid for

Forcing proton on a deliberately-muon producer creates a NEW straddle. Measured
in #5634: `vhat_per_crossing_chain` moved 17 fields and flipped its own
`scalar_vs_matrix_agree` True -> False. It and `he3_tritium_cosh_asymmetry_diagnosis`
were reverted to their own q, then moved 0. **2 of the 12 are confirmed
deliberately muon; the other 10 are unadjudicated.**

### Recommended: B -> A -> C

- **B (API):** optional forwarding `q` on `mass_at_3A_proper` /
  `hecke_characters` entry points, using the backwards-compatible shape proven
  in #5646. Required before A is even expressible for the 11.
- **A (12 decisions):** per producer — deliberately muon (pass its own q) or
  accidentally muon (migrate + regenerate)? 14 witnesses in scope. ALL the
  judgement lives here. **Sequence behind #5500** (muon anchor -> CODATA 2022,
  audit red, 53 witnesses) — it collides directly.
- **C (113 inert sites):** mechanical, expect 0 fields moved, batch-sweep
  exception applies. **Buys no correctness today** — purely preventative against
  a producer later joining `ideal_muon`. Worth doing or not is a judgement call,
  and should be made as one rather than assumed.

### Not claimed

Nothing straddles today — the gate is green (clean=8 / STRADDLE=0). And which of
the 10 unadjudicated producers is deliberate is exactly what must not be guessed.
