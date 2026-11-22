---
# qou-j9zj
title: float64 taint in meson_gmor_derivation_probe.py:276 (winner_vs_fusion via abs(best_a[1]-fusion_sum))
status: completed
pr: 8226
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T04:24:34Z
updated_at: 2026-11-22T21:20:33Z
parent: qou-9nnz
---

Surfaced by mpf-mixed-arithmetic-audit during a precision-gates.sh --changed run on 2026-09-03 (unrelated to the qou-o6ov work that triggered the gate). Pre-existing, not introduced by me.

Site: computations/probes/meson_gmor_derivation_probe.py:276
  computed=mp.nstr(winner_vs_fusion, 18)
where (line 274)  winner_vs_fusion = abs(best_a[1] - fusion_sum)
The audit classes best_a[1] / fusion_sum as float64-tainted, so the printed
18-digit value is display of a float64 quantity (kind=printed, CANDIDATE).

Fix: carry best_a[1]/fusion_sum as mpf from source (or if they are genuinely
float64 upstream, that upstream is the real defect). PROBES ARE NOT EXEMPT
(AGENTS.md). Low priority: it is a printed diagnostic, but a printed float64
'agreement' is exactly the 1e-16-floor trap the NO-FLOAT64 rule warns about.
Not this arc's domain (meson GMOR, not Magnus) — hence a bean, not an inline fix.


## Round 52 Progress
- [x] PR https://github.com/litlfred/qou/pull/8226 (`523155d5604cc384f307eb1cb22785f1fded85da`): carried `miss` and PDG quark masses as `mpmath.mpf`, serialized all 6 numeric `add_data` fields via `_precision.fmt`, and regenerated `meson-gmor-derivation-probe.witness.json` (0 raw float64).

## 2026-11-22 — CLOSED: the fix is on main via port #8226 (bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Checked against main `3c4c98fccf3`.

The "Progress" entry above records the fix on a batch PR that never merged. It reached main as `adb97b5d36` ("port #8226: ..."), which names this bean. Verified on main: `meson-gmor-derivation-probe.witness.json` holds 0 JSON floats; the producer carries `miss` and the PDG masses as mpf.
