---
# qou-t1a0
title: Triage the 5 BLOCKING convention-C bindings, and resolve the qou-zuva / qou-wlnx contradiction
status: todo
type: task
priority: high
created_at: 2026-11-14T07:02:22Z
updated_at: 2026-11-14T07:02:51Z
parent: qou-cxh0
---

Re-measured on main fee4ad592: `python3 scripts/convention-c-value-audit.py --root computations` gives 148 confirmed / 143 adjudicated / BLOCKING 5 / 597 D, where status doc §3a (2026-10-10, 77695711d) says 143 / 143 / 0 / 576. Ledger integrity checked first: a failed load would report all 148 as BLOCKING.

Sites: frobenius_s_parity_convention_d_probe.py:64 and :191; v9_markov_trace_convention_d_probe.py:161; qbeta_cos_resummation_d_probe.py:92; spectral_decomposition_qvalue_d.py:72. Four are co-bound with z_D.

qou-ztee (completed) built the ledger forecasting this exact census floor; its ruling is "if the count is wrong, fix the REPORT" -- draining a comparison arm deletes the measurement and is AGENTS.md 1a audit-dodging. A co-binding is a value-level hint, NOT proof; `z_C_historical` is a label.

CONTRADICTION to settle first: sites 4 and 5 are claimed by in-progress beans qou-zuva and qou-wlnx whose titles say "redo in convention D" -- incompatible with the comparison-arm reading. Exactly one reading can be right. frobenius_s_parity_convention_d_probe is in NO bean (grep -rl over beans/defs/ returns 0).
