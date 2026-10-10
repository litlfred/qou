---
# qou-iu3m
title: Legacy-marshalled frame lived in 3 anonymous copies — one named home + guard
status: completed
type: task
priority: normal
created_at: 2026-08-26T04:19:45Z
updated_at: 2026-08-26T13:20:06Z
---

Found while fixing `qou-qu2w` (the 2.157x nucleon-trace divergence), and it is
the reason that defect survived as long as it did.

## The hazard

`canonical_braid_marshalling.marshal_to_chi_lambda_braid` drops the crossing
`d`. On a nucleon chain that silently prices the two INTRA-nucleon `averaged`
crossings at `z` instead of `z - h/2`, so a trace built on it is 15.3 %
(proton) / 27.3 % (neutron) off the true trace of the stated Hecke element.

Some callers NEED that frame — they compare a closed form against an empirical
slow path that is itself bound to `chi_lambda_braid`, and both sides of such a
comparison must sit in one frame or it means nothing. Those callers are
correct, and the 2026-06-03 colour-averaging audit says to leave them.

What was NOT correct: the frame lived in **three anonymous local copies**.

    closed_form_tau_M_verification_phase5q.py   marshal_intra + a wrapper
                                                NAMED compute_tau_M_nucleon_H3
    rho_constit_equals_tau_M_proton_phase5l.py  marshal_intra (VERBATIM
                                                duplicate) + compute_tau_M_proton_H3
    constit_factor_varying_q_phase5k2.py        full-atom-word marshalling,
                                                frame undeclared

Two of them were named after the canonical helper while returning different
numbers, with nothing saying so. `marshal_intra` was byte-identical in the
first two (verified by `inspect.getsource`).

**That invisibility is the root of `qou-qu2w`.** The canonical helper had the
same bug; because there was no single place saying "this frame is lossy",
fixing one copy told you nothing about the others, and nothing flagged that a
fourth would be equally silent.

## Fix

  * New `computations/legacy_marshalled_frame.py` — one named, documented home
    for the frame, with the divergence stated in numbers and an explicit
    "do NOT re-point these callers at the canonical helper" warning.
  * phase5q and rho_constit: local copies DELETED, re-pointed at
    `legacy_nucleon_tau_M_H3`. The name collision is gone at the root rather
    than merely documented.
  * constit_factor: declares the frame in-file (it marshals the full atom
    word, a different use, so it keeps its direct call).
  * New `computations/test_legacy_frame_no_new_copies.py` — a guard that does
    NOT forbid the legacy frame, only forbids using it WITHOUT SAYING SO: a
    file calling the raw marshaller must either be baselined with a reason or
    name `legacy_marshalled_frame`. Keyed on an AST *call*, not a substring,
    because every one of these files mentions the marshaller in prose and a
    substring check would flag the explanations.

## Behaviour preserved, proved not assumed

Baselined the exact values before refactoring and re-checked after:

    tau_p 1.3215929842373445355   identical
    tau_n 1.2575579046963118128   identical

Bit-identical, so every legacy-frame comparison still compares what it did.


## CLOSED 2026-08-26 — landed on main (PR #5821 cone, merge 0bc2794da9)

`computations/legacy_marshalled_frame.py` is the one named home;
`test_legacy_frame_no_new_copies.py` guards it (AST Call node, not substring
— every such file discusses the marshaller in prose);
`probes/nucleon_h3_marshalling_divergence_probe.py` pins the root cause.
All three verified present on origin/main. The guard does not forbid the
legacy frame — it forbids using it WITHOUT saying so.
