---
# qou-t1a0
title: Triage the 5 BLOCKING convention-C bindings, and resolve the qou-zuva / qou-wlnx contradiction
status: completed
type: task
priority: high
created_at: 2026-11-14T07:02:22Z
updated_at: 2026-11-14T07:19:06Z
parent: qou-cxh0
---

Re-measured on main fee4ad592: `python3 scripts/convention-c-value-audit.py --root computations` gives 148 confirmed / 143 adjudicated / BLOCKING 5 / 597 D, where status doc §3a (2026-10-10, 77695711d) says 143 / 143 / 0 / 576. Ledger integrity checked first: a failed load would report all 148 as BLOCKING.

Sites: frobenius_s_parity_convention_d_probe.py:64 and :191; v9_markov_trace_convention_d_probe.py:161; qbeta_cos_resummation_d_probe.py:92; spectral_decomposition_qvalue_d.py:72. Four are co-bound with z_D.

qou-ztee (completed) built the ledger forecasting this exact census floor; its ruling is "if the count is wrong, fix the REPORT" -- draining a comparison arm deletes the measurement and is AGENTS.md 1a audit-dodging. A co-binding is a value-level hint, NOT proof; `z_C_historical` is a label.

CONTRADICTION to settle first: sites 4 and 5 are claimed by in-progress beans qou-zuva and qou-wlnx whose titles say "redo in convention D" -- incompatible with the comparison-arm reading. Exactly one reading can be right. frobenius_s_parity_convention_d_probe is in NO bean (grep -rl over beans/defs/ returns 0).


## 2026-11-14 — DONE: all five adjudicated, BLOCKING 5 -> 0 (PR litlfred/qou#7817)

All five are **(a) deliberate two-arm C-vs-D comparison arms.** The measurement
that settles (a) against (b), and the one this bean was missing, is **downstream
consumers — there are none.** Each C-labelled witness field
(`tr_markov_C_correct_trace`, `formA_cos_C_historical`, `cos_alpha_C_historical`,
`Q_bare_C_HISTORICAL`, `tr_M_C_HISTORICAL`, `pauli_C_HISTORICAL`) occurs in
exactly two files across `computations/ scripts/ docs/ folio/ tools/ qou-mass/
beans/`: its own producer and its own witness. No C value reaches an assertion, a
canonical witness field or an exit code. Sites 1-2 write no witness at all
(`:33` "No witness is written"; no `WitnessBuilder`, no such witness in tree).

Five rows added to `docs/audits/convention-c-comparison-ledger.json`, entries
143 -> 148, all `verdict: "comparison"`, keyed `qou-fd2u` (sites 1-2),
`qou-m7py` (3), `qou-zuva` (4), `qou-wlnx` (5). Each `source_hash` recomputed
independently from the live file with the audit's own `_site_hash` before
landing. Audit now exits 0: 148 confirmed / 148 adjudicated / **BLOCKING 0**.

### Two things this bean asserted that were wrong

1. **"Exactly one reading can be right" for sites 4-5 was a FALSE DICHOTOMY.**
   Both readings are right: those producers ARE `qou-zuva`'s and `qou-wlnx`'s own
   delivered artefacts. `qou-zuva`'s 2026-10-10 entry records the new producer and
   "C figure reproduces as 1014.8 -> 185.1 (labelled historical)" — it asked for
   the labelled C arm — and the creating commits `d994e144a8` / `b2408388ca` cite
   the beans by name. Both beans stay open on derivational items unrelated to the
   C binding.
2. **"frobenius_s_parity_convention_d_probe is in NO bean" was already false when
   written, and this bean's own creation invalidated it** ~3 minutes later. The arc
   bean `qou-fd2u` (2026-10-10T08:52:03Z) predates it and records the probe's
   result. Accurate form: the filename appears in no bean; the arc bean is
   `qou-fd2u`.

### BLOCKING 0 is a transient floor, not a finish line

Fifth recurrence in ten weeks per the ledger's own history: 5->0, 11->5, 5->0,
then **0->26** ("because sibling sessions landed new probes since"), 6->0, now
5->0. The count re-accretes whenever a D-subject producer lands with its
comparison arm — the healthy case, since a D result *about* C needs a C arm.
Read `BLOCKING > 0` as an unregistered-comparison queue, not a migration
regression. Today's four commits postdate both the 2026-10-10 baseline and the
`6 -> 0` ledger pass by 7-24 h (dated via the GitHub API; the shallow clone
cannot see them).

Completed under rule 13a as mechanical: no conjecture is touched. The arc's one
open item remains `qou-cds1` (research).
