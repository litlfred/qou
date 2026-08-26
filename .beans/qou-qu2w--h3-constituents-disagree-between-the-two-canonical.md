---
# qou-qu2w
title: H3 constituents disagree between the two canonical tr_M(4He) producers by 2.157x
status: todo
type: task
priority: normal
created_at: 2026-08-25T22:10:20Z
updated_at: 2026-08-25T22:11:31Z
---

Found 2026-08-25 while flipping `_habiro_coefficient_extract.py` to the
canonical `bring_color_weighted` p-n interface (bean `qou-cds4`, PR #5801).
**NOT caused by that flip** — both producers disagreed by this factor before it.

Two producers compute tr_M(⁴He) at q₀, both now in the canonical frame:

    habiro-coefficients-helium-4.witness.json      0.16097414544240738
    atomic-tr-m-helium4-canonical.witness.json     0.34716181818783578
    ratio                                          2.1567

The difference is entirely in the **H₃ constituent traces**, not in the
interface convention (both now price p-n as `z - h(1/2 - delta/4)`):

    habiro chain, from habiro-coefficients-atomic.witness.json
        tau_p = 1.1457596924573008697   tau_n = 0.98774368811580957163
    compute_tau_M_nucleon_H3 (closed_form_tau_M)
        tau_p = 1.321592984237344535    tau_n = 1.257557904696311813

    (1.321592984 * 1.257557905)^2 / (1.145759692 * 0.987743688)^2 = 2.1567

which is the whole ratio, exactly.

So one of the two H₃ baselines is not canonical, or the two are computing
different objects under one name. Worth settling: the habiro chain feeds 25
committed mass-table witnesses and ~72 consumers, and `compute_tau_M_nucleon_H3`
feeds the closed-form path.

Not in scope for PR #5801, which changes only the interface convention.
Recorded in docs/audits/2026-08-23-habiro-mass-table-convention-c-attribution.md.
