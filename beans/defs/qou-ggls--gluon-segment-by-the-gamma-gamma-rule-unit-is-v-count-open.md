---
# qou-ggls
title: 'Gluon segment by the gamma-gamma rule: the unit is V = s0 s1^-1, the count is not fixed; whole-word reading 3 admits only V^1'
status: todo
type: task
priority: normal
created_at: 2026-11-15T12:00:00Z
updated_at: 2026-11-15T12:00:00Z
parent: qou-99qc
---

Owner-approved task (relayed 2026-11-15): derive the nucleon gluon segment by the γγ rule, then enumerate if it is not unique.
- Branch `claude/gg-gluon-segment-2026-11-15`, PR #7876.
- Pre-registered at a341245311 (step 1) and a9ca10d266 (step 2).
- Probe: `computations/probes/gg_gluon_segment/` (36/36, exact over Q(q), proton pin, convention D).

**Step 1.** On three strands the γγ rule has one vertex, V = σ0σ1⁻¹. That vertex is the corpus `gluonUnit` (`toCorpus_vertex_zero`). So the unit is unique. The number of units in a separate gluon segment is not fixed, so the output is the family {V^k}.

Corpus side-rules name three members:
- k = 1: the 2-letter slot of the crossing budget 11.
- k = 3: the gluon as its own SDP component, selected like the core.
- k = 0: the retired "B3 IS the gluon".

σ0² is not γγ (`gluonPair_not_gammaGamma`). It has a separate corpus derivation: H2 PSD parity, owner ruling 2026-08-30.

**Step 2** (k = 0..3, CORE·TAIL·V^k, census quark tail held fixed):
- g_odd = 0 identically for every k. The trace-level bar obstruction of qou-z08b belongs to σ0² specifically.
- Whole-word reading 3 at the proton pin admits **k = 1 only**, for both nucleons: χ_(2,1) = +0.21703 (p) and +0.42941 (n). It passes on q ∈ (1, 1.42916).
- k = 0, 2 and 3 fail for both nucleons.
- Q_β at z_D for the k = 1 element is 0.229517 MeV (−70.66 %). This is reported only and played no part in any choice.

**OPEN, owner decision, not taken here:**
1. Does the γγ rule (gluon unit V) or the H2 PSD-parity rule (σ0²) govern the gluon segment?
2. Does the reading-3 survivor (σ0σ1⁻¹)⁴·TAIL replace nuc11_interleaved?

Also still open: the quark tail is census-derived (qou-ales option 4), and the dashboard is not re-scored (qou-iagg).

## 2026-11-20 — ported to the bean mount (W3)

This bean was a file in PR #7876. Beans are branch-mounted now, so PR #7876 could not merge it. It is written to the mount unchanged. The probe files moved to the port branch `claude/gg-probes-port-2026-11-20`; both producers re-run there and reproduce the committed witness payloads (gluon segment 36/36; quark tail exit 0).
