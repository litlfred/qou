---
# qou-aj91
title: 'ARCHITECTURE: 85 producers read the anchor-defining witness directly, bypassing q_parameter'
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:35:38Z
updated_at: 2026-08-24T18:07:44Z
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


## Evidence on the intent question (measured 2026-08-24)

The bean asks whether reading the pinning witness is deliberate. The producers'
own comments at the read site are evidence. Across all 85:

     4  DELIBERATE — the comment says so
    47  commented at the read site, but never says WHY muon
    30  NO comment at the read site at all
     4  mentions muon only incidentally

**Three of the four "deliberate" are INFRASTRUCTURE that should read the
anchor**: `q_parameter` (it defines the muon override), `q0_repin_sweep` (it
must not re-pin the definer), and `cross_check_trM_1ppb` (an L1 cross-check
that must run at muon). The fourth is `bwhk_st_matrix_corroboration`:

    # canonical muon-q0, read at runtime from the pinning witness
    # (drift-proof, full 50-dps) -- never hardcode

So among ORDINARY producers, stated intent is close to absent. The reading this
supports is that the idiom is **conventional — copied from a neighbour — rather
than chosen**, and that the four infrastructure cases are the only ones where
it is load-bearing.

**This is evidence, not proof.** Absence of a comment is not absence of intent;
an author may have meant it and not written it down. It shifts the prior, and
it identifies which four to ask about first rather than all 85.

### Why it still should not be swept

If the idiom is conventional, the fix is NOT to route 77 producers through
`q_parameter` in one commit -- that silently moves numbers in 77 places at once,
and the C->D precedent (qou-2zjp) shows how large such a move can be (14.741 %
on alpha*). It is a per-producer question of which layer each quantity belongs
to, and several of these are slow.

The cheaper first move is the one this evidence points at: decide whether
`WitnessBuilder`'s `.q0Value` stamp should report the anchor the PAYLOAD was
computed at rather than whatever `q_parameter` resolves to. That fixes the
STRADDLE (the witness lying about its own layer) for all 85 at once, without
moving a single number, and leaves the layer question to be settled per
producer afterwards.
