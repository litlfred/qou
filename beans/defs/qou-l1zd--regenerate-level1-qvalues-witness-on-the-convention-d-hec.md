---
# qou-l1zd
title: Regenerate level1-qvalues witness on the convention-D Hecke engine
status: completed
type: task
priority: normal
tags:
    - convention-d
created_at: 2026-11-15T18:05:00Z
updated_at: 2026-11-15T23:30:00Z
parent: qou-avtq
---
`computations/hecke/hecke_engine.py` `HeckeRational.z` moved from the rounded
convention-C `4993/10000` to exact convention-D `q^3/(q^2+1)` (PR #7927, commit
dd02b31c3f, owner ruling 2026-11-15). `computations/level1-qvalues.witness.json`
(auditOnly, computedAt 2026-03-27) was computed on the C engine and is now stale
against its producer.

Re-run measured 2026-11-15 on the D engine: 3H 0.00 s, 14C 0.39 s, 60Co 125 s,
90Sr 747 s; stopped at the 15-min cap inside 137Cs. 137Cs and 210Bi remain and are
longer (exact Fraction arithmetic; z_D denominator 2232100 vs 10000). Run with
`python3 -u level1-qvalues.py 2>&1 | tee /tmp/level1.log` and a multi-hour budget,
or add a per-nucleus option. Other HeckeRational consumers not re-run:
hadron_knot_table.py (known >50 min per bound atom), hecke_rust_bridge.py.

## 2026-11-15 23:30Z

Done on branch claude/level1-witness-convention-d-2026-11-15, draft PR #8073 (issue #8072). All 6 decays computed under D. The O(A) traced_volumes_all sweep gives the same exact rationals about 50x faster (210Bi 428 s). 210Bi Q_q = +156.25: no negative site, so the fallback applies. Complete when #8073 merges.

## 2026-11-15 23:26Z

PR #8073 merged (rebase). Completed. Float64 follow-up is on branch claude/level1-qvalues-no-float64-2026-11-15.
