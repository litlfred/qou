---
# qou-aj91
title: 'ARCHITECTURE: 85 producers read the anchor-defining witness directly, bypassing q_parameter'
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T17:35:38Z
updated_at: 2026-08-26T04:17:09Z
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


## Narrow fix implemented — PR #5699 (draft, 2026-08-24)

Branch `claude/aj91-witnessbuilder-anchor-stamp-2026-08-24`, tip 234d0ee2f9.
Implements the bean's own recommendation: fix the STAMP, not the 85 producers.

**`resolve_q0_anchor_payload_first()`** in `qou_substrate.witness` consults
`_q0_anchor_from_payload` (already present, previously used only to DROP a
stale pin) before the manifest, and is wired into both writers of the field
(`stamp_staleness_metadata` and `build`). Precedence: explicit declaration >
manifest `ambiguous` > payload evidence > manifest/env.

**Two findings that change what this bean says.**

1. **The upstream-hash signal is UNSOUND — do not use it.** `record_upstream(Q_PIN)`
   looks like a ready-made detector for the same 85. `alpha_k_jones_markov_h12`
   still records that upstream deliberately ("for provenance ... it remains the
   canonical 3-CAL pin document") while computing from `q_parameter.Q_50_DIGIT_STR`,
   i.e. PROTON. Inferring muon from it would have flipped a CORRECT proton stamp
   to a false muon one. Consequence for this bean: **the census of 85 is an idiom
   grep, not a list of 85 live muon producers** — at least one has migrated and
   keeps the read only in a comment.

2. **`_q0_anchor_from_payload` matched only `isinstance(v, str)`**, which misses
   the commonest producer shape: stamp BEFORE `json.dump(..., default=str)`, so
   at stamp time `parameters.q0` is still an `mpf`. It failed SILENTLY — fell back
   to the manifest and looked like an ordinary answer. Found only by RE-RUNNING a
   producer; re-reading its committed output could not show it.

**Measured over 2737 committed witnesses:** 6 stamps contradict their own
payload q0; 154 unstamped witnesses carry readable evidence and gain a correct
stamp; 1931 record no q0 and keep the manifest path. The 6 are invisible to
`q0_anchor_consistency_audit.py`, which compares anchor against the value beside
it, never against the payload.

**Verified:** `meson_mass_from_hecke` re-run under old vs new code — stamp
proton -> muon, payload BYTE-IDENTICAL, zero differing non-anchor keys.
`precision-gates.sh --changed` EXIT=0, all blocking green. Tests 24/0.

**Still open (NOT done here):** which layer each of the 85 producers' quantity
actually belongs to. This makes each witness state the layer it was computed at
— a precondition for that question, not an answer. No sweep.


## 2026-08-26 — population re-measured: 74, and five different numbers were in circulation

This bean says **85**. I have quoted **283** at the owner. Both are wrong, and
so are two intermediate figures I produced getting here. Measured today:

    148   raw-text grep for "q-pinning-50-digit"        <- over-counts via PROSE
    283   my earlier figure                             <- per-WITNESS, not per-producer
    119   AST-normalised, pin string appears in code    <- includes auditors + regexes
     85   this bean, 2026-08-24                         <- stale
    ---
     74   producers that read the pin AS A FILE PATH    <- the honest number

The 119 → 74 gap is the same defect class this arc keeps hitting: a script that
carries `"q-pinning-50-digit"` as a **regex or search string** is not a script
that **reads** it. Among the 45 excluded were **two of my own audit scripts**
(`q0_independence_checker.py`, `no_q0_recorded_producer_split.py`), which
pattern-match the name. Sixth instance. The discriminator that works: the
string must be an argument to a path/open/read call.

### The 74, by declaration

    54   untagged (default proton at runtime; compute is muon regardless)
    18   ideal_muon (consistent: read muon, declared muon)
     5   physical_proton (STRADDLE: read muon, declared proton) -- was 2 in this
         bean on 2026-08-24, so the straddle set GREW
     1   ambiguous

### Evidence on the fork this bean refuses to settle by sweep

Of the **54 untagged**:

    41   SILENT on the pin -- no stated rationale either way
    10   state MUON intent ("canonical muon-q0 ... never hardcode", drift-proof)
     3   state BOTH (comparison?)

So Reading A — *"pinning to the canonical anchor is a deliberate, drift-proof
design"* — is **explicitly stated by 10 of 54**. The other 44 say nothing.

**Silence is not evidence of either reading**, and that is the finding, not a
tiebreak. An idiom that propagates by copy-paste and a design choice nobody
bothered to restate look identical in the source. What can be said:

- the 10 who state it are a **real constituency**, so a blanket "route
  everything through `q_parameter`" would override documented intent;
- the 5 straddles are wrong under **either** reading — they read muon and
  declare proton — so they are safe to fix now, independently of the fork;
- the 41 silent ones are where the decision actually bites, and nothing in the
  source decides it.

### Recommendation (judgement, not a finding)

Split the bean. The 5 straddles are unambiguous and small. The 10 stated-muon
producers should be *tagged* `ideal_muon` so their intent stops being invisible
to the manifest — that is a declaration change, not a numerical one. Only the 41
silent ones need the owner's ruling, and by then the population is small enough
to look at.


## 2026-08-26 — reroute scoped before editing: the 44 are NOT one batch

Owner authorised rerouting the 44 silent direct-pin producers through
`q_parameter`. Scoped before touching any of them, and two properties split the
set in ways a by-count batching would have hidden.

### 1. Twelve of the 44 have NO committed witness

    32   have a committed witness  -> the ~11.5 ppb move is MEASURABLE
    12   have none                 -> the move is UNMEASURABLE

For those twelve there is no before/after to compare, so rerouting them is a
blind numerical change: nothing on disk records what they produced at the muon
pin, and nothing will show what changed. They should be re-run and their witness
COMMITTED FIRST, at the muon pin, so the migration has a baseline — otherwise
the reroute silently discards the only evidence of the prior value.

### 2. Nine of the 44 use `record_upstream` — rerouting DROPS provenance

The uniform idiom is:

    Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
    Q = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])

`record_upstream` does two things: it reads the value AND registers the upstream
witness in `data.upstream_witness_hashes`. The obvious replacement —
`from q_parameter import Q_50_DIGIT_STR` — supplies the value and **loses the
provenance record**.

So the reroute is not a substitution, it is a substitution plus a provenance
decision: either accept the loss (the pin is no longer an input, so arguably
there is nothing upstream to record), or keep `record_upstream` for provenance
while taking the VALUE from `q_parameter` — which is a straddle-shaped hybrid
and needs care.

### Proposed batching, by SHAPE not by count

    A.  9  use record_upstream          -> needs the provenance decision first
    B. 12  no committed witness         -> baseline the witness at muon FIRST
    C. 23  plain read, witness exists   -> the clean batch; reroute + regenerate,
                                           before/after measurable per file

**C is the only batch that is mechanical.** It is also the one where the ~11.5
ppb claim can actually be checked file by file. A and B each carry a decision
that is not mine.
