---
# qou-aj91
title: 'ARCHITECTURE: 85 producers read the anchor-defining witness directly, bypassing q_parameter'
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:35:38Z
updated_at: 2026-08-24T17:36:23Z
---

## What

85 producers resolve q0 by reading the ANCHOR-DEFINING witness directly:

    Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
    q = mp.mpf(record_upstream(Q_PIN, ...)["derived_50_digit"]["q"])

`derived_50_digit.q` is what `witness._q0_value_for_anchor("muon")` returns --
it IS the muon anchor's definition. So these producers compute at muon
regardless of what `q_parameter` would hand them, and `QOU_Q0_ANCHOR` cannot
reach them.

## Scope, measured 2026-08-24

    ideal_muon        16   consistent: read muon, declared muon
    physical_proton    2   STRADDLE: read muon, declared proton
                           (alpha_k_jones_markov_h12, per_atom_audit_witnesses)
    untagged          67   straddle in effect -- untagged defaults to proton at
                           runtime, but the computation is muon either way
    -----------------------
    total             85

The 67 untagged are the interesting bulk. Their WitnessBuilder `.q0Value` stamp
comes from `q_parameter` (proton), while their payload is muon -- so the
witness declares one layer over the other, which AGENTS.md forbids regardless
of size.

## The question, which is not an agent's to answer alone

Is reading the pinning witness deliberate? Some of these say so explicitly:

    # canonical muon-q0, read at runtime from the pinning witness
    # (drift-proof, full 50-dps) -- never hardcode
    (bwhk_st_matrix_corroboration)

That is a coherent design: pin to the canonical anchor, immune to manifest
churn. If it is the intent, the defect is the `.q0Value` STAMP claiming proton,
and the fix is in WitnessBuilder, not in 85 producers.

If it is NOT the intent, the fix is to route them through `q_parameter` -- but
that silently moves numbers in 85 producers at once, which needs its own
review, not a sweep.

**Do not resolve this by editing 85 files.** Decide which of the two readings
is correct first.

## How it was found

Nine producers in the qou-1c4y migration flipped `.q0Value` to proton while a
muon value survived at `.data.q_pinned` / `.parameters.q_0_50dps`. They were
reverted rather than committed (PR #5664). Grepping the idiom found the other
76. This is the fifth distinct mechanism by which a producer holds a muon value,
after: manifest tag, local literal, shared-module literal, and the provenance
stamp moving on its own.
