---
# qou-aj91
title: 'ARCHITECTURE: 85 producers read the anchor-defining witness directly, bypassing q_parameter'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T17:35:38Z
updated_at: 2026-10-04T15:11:52Z
parent: qou-5vkl
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


## 2026-08-26 — batch C is NOT mechanical either: the reroute is DEPENDENCY-ORDERED

Went to execute batch C (the 24 with a witness and no `record_upstream`) and
stopped at the first file. The finding changes the shape of the whole migration.

### Rerouting a producer whose UPSTREAM is muon-built MANUFACTURES a straddle

`hydrogen_qshuffle_compound.py` reads the pin **and** loads two more witnesses:

    terms-2-3-atom-per-gen-mpfr-50dps.witness.json   carries the muon value
    proton-mass-full-tower-50dps.witness.json        q0Anchor: "muon", explicitly

Moving its q₀ to proton while it keeps consuming muon-built inputs mixes an
experimental-layer q₀ with ideal-layer data **inside one computed quantity** —
the straddle AGENTS.md forbids "regardless of size", and the exact defect this
epic exists to remove. The reroute would not fix a straddle; it would create one.

**So a producer's q₀ can only move after its upstream witnesses have moved.**
This is a dependency-ordered migration, not a batch of independent edits. Any
by-count batching (≤ 49 files per PR) cuts across the dependency graph and will
straddle whatever it happens to split.

### Batch C re-partitioned by upstream layer

    12   truly NO upstream witness      -> safe to reroute alone
     5   consumes a MUON-built witness  -> BLOCKED until upstream migrates
     4   upstream is proton             -> safe
     3   upstream unlabelled            -> UNKNOWN layer, needs a look

### Two detector corrections, both mine, both caught before editing

1. A first pass keyed on `witness_path("…")` and reported **14** truly-clean.
   It missed `json.load(open(COMP / "…"))` and `json.loads((COMP / "…").read_text())`
   — `he4_binding_k_presentation_correction_probe` loads
   `canonical-tr-m-via-chi-cache.witness.json` that way. Keying on **any
   `.witness.json` string literal in code_only'd source** gives **12**, and moves
   the straddle count 4 → **5**. I nearly edited 14 files off a false-clean list.
2. The `.witness.json` scan runs through `code_only` — a filename in a docstring
   is not a dependency. Same discipline as `qou-5li4`; without it the prose
   naming an upstream witness counts as consuming it.

### What is actually ready

The **12** are ready to edit: no upstream witness, a committed witness to
measure against, no `record_upstream`. Their read shapes are NOT uniform
(`witness_path(…)`, `json.load(open(COMP / …))`, `json.loads((COMP / …).read_text())`),
so this is 12 individual edits, not a sed.

**Not attempted here**, deliberately: 12 non-uniform edits plus 12 producer
re-runs plus 12 before/after comparisons is its own PR with its own verification,
and starting it at the tail of a long session is how an unverified change lands.
The list and the shapes are recorded so it can be picked up cold.


## 2026-08-26 — batch C executed: PR #5823, 11 producers, 2 numbers moved

The 12 this bean recorded as "ready to edit" turned out to be **11 to reroute
plus 1 to exclude**, and the "each moves numbers ~11.5 ppb" framing was wrong
for **9 of the 11**. Both corrections are to this bean's own text.

### 9 of 11 do not move a number, and it is provable rather than merely observed

Those nine use q₀ for one thing only:

    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))

`dnet = net(neutron) − net(proton)` evaluated at q₀, reduced to its **sign**.
A Newton step from q₀ puts `dnet`'s nearest root **10 153 554 × the pin
separation** away (Δq_root = 0.130 vs Δq_pin = 1.28e-8), so an 11.5 ppb move
cannot flip it. Re-running confirms: byte-identical in every numeric payload
key; only volatile provenance moved.

So the discriminator for this batch was never "has a witness" — it is
**how many times `q0` appears in the file**. Two occurrences ⇒ sign-only.
The two that moved are exactly the two with more (3 and 13).

`yekutieli_borromean_h2_extraction` is identical for a third reason worth
keeping separate: its witness stores only `kappa_computed`, the h² Taylor
coefficient **at h = 0**, which is q₀-independent by construction. `tr_M(q₀)`
is printed, never recorded. Its "identical" is real, not a witness that
silently failed to rewrite — checked by mtime and by the builder's own
"[unchanged]" report.

### The one real bug

`qbeta_barodd_d_ladder_ord17_probe` builds a μ–p comparison:

    q_num = {"proton": q0}          # q0 WAS the muon pin
    q_num["muon"] = q_muon_at(50)

Both rows were the same number (`h = 0.209060321996` vs `0.20906032199`), so
a diagnostic that exists to exhibit the μ–p tension was comparing muon to
muon. Post-reroute they differ by 1.11e-7 = `(1 + 1/q²)·Δq/h`, the real
separation. **This is the first case in the epic where the mechanism-5 read
was not merely mislabelled but made a comparison vacuous.**

### mass-from-q-symbolic: excluded, and the census mis-scored it

It met every batch-C criterion. It must not be rerouted: it computes at
proton throughout and reads the muon pin once so the ideal-layer identity
can be checked *in its own layer*.

This bean's census scored it **"silent on the pin"**. It is not — the
rationale is stated in the file, four lines above the read. The read-site
classifier only looked at the read site. So the "41 silent / 10 stated-muon"
split in the 2026-08-26 entry above is a **lower bound on stated intent**,
and any producer in the silent bucket may have its rationale a few lines
away. Do not treat that bucket as evidence of absent intent without
re-checking with a wider window.

Fixed by stating it at the read and declaring the stem `ambiguous`.

### Environment control — the step that made the attribution real

The container has `mpmath` 1.3.0 where several baselines recorded 1.4.1, so a
before/after diff alone could not separate pin from environment. Re-running
the **OLD code in THIS container**:

* borel-pade: 2 provenance fields differ, no payload ⇒ all 21 payload moves
  are the reroute.
* barodd: exactly the 12 `muon/*` fields differ; every `proton/*` field
  reproduces byte-identically ⇒ the 26 moved fields split **14 mine / 12
  not**.

Without that control I would have reported 26 fields moved by the reroute.

### A drift this surfaced, filed separately as `qou-2zw0`

The 12 `muon/*` fields move because the committed muon row is
`h(frozen pin 1.1099785955573347…)` while `q_muon_at(50)` derives
`1.109978595642739…` from live CODATA and cannot produce the frozen pin.
Import-cone drift — every producer's `scriptHash` still matches its witness.
The baseline `commitSha` does not resolve (`rewritten` class), so the cause
is **undetermined**, not established.

### Remaining mechanism-5 untagged: 33, unchanged and still not batchable

    10  record_upstream        rerouting DROPS provenance — a decision
    11  no committed witness   no baseline; witness must be committed first
    12  muon-built upstream    BLOCKED: moving q₀ first MANUFACTURES a straddle

The dependency ordering recorded above stands and is the critical path for
`qou-1c4y`. Nothing here shortens it.


## 2026-08-26 — the "11 with no committed witness" batch is 0 ready, 11 blocked

Went to execute it. **The plan recorded above for this batch rests on a false
premise and cannot be run as written.** It says:

> They should be re-run and their witness COMMITTED FIRST, at the muon pin, so
> the migration has a baseline.

Measured, that is impossible for most of them:

     7  write NO output at all — stdout-only probes
     3  hand-roll a witness with write_text (no WitnessBuilder)
     1  uses WitnessBuilder
    --
    11

For the **7 stdout-only** there is no witness to baseline and none to compare
after, so a reroute is a blind numerical change in both directions. Giving
them one is bean `1j39`'s scope (I-infra-no-witnessbuilder batch port), not a
step inside this batch.

### And the 1 that could be baselined is blocked too

`qbeta_c3_barodd_determined_solve_probe` is clean on every other axis — no
`record_upstream`, no upstream witness, proper `WitnessBuilder`. Ran it
(71.7 s, exit 0). It emits **9 raw float64 fields**, and with its witness
present `witness_raw_float64_audit.py --strict` **exits 1** on 3 NEW dirty
fields. Committing that baseline is forbidden: *"Do NOT add the file to the
baseline to silence this."*

Deleted the uncommitted witness rather than commit it. Filed as `qou-poi1`,
which measures the general hole: **14 producers emit a witness that is never
committed and is not gitignored, so the ratchet — which scans only committed
witnesses — cannot see any of them.**

Rerouting it would buy little in any case: the producer's own verdict is
*"ANCHOR-BLIND to ~2.7e-11 (muon ≈ proton)"*.

### Two corrections to this bean's own classification

1. **"No committed witness" was wrong for 2 of the 11.**
   `qbeta_argu_phase_branch_selection_probe` and
   `qbeta_meridian_holonomy_anchor_swing_probe` DO have committed witnesses.
   My index keyed on `witness.scriptFile`, and both records are
   **`scriptFile: null`** — the "bare producers" class. So the index was right
   to miss them and the real defect is missing provenance. They are invisible
   to every provenance-keyed audit, this bean's census included.

2. **Counting `q0` occurrences to find sign-only producers does not generalise.**
   It worked for batch C. Here, three producers show `q0` **zero** times and
   read the pin anyway, under `q_0`, `Q0_MPF` and `Q0_F64`
   (`gram_matrix_seminormal_n`, `pyhecke_jones_markov_atlas`,
   `pyhecke_n_generic`). Keying on one spelling of a variable name is the same
   defect class as keying on one spelling of a convention — count the *reads*,
   not the identifier.

   Two of those three also do `float(mp.mpf(...))` on the substrate parameter
   (`gram_matrix_seminormal_n:231`, `pyhecke_n_generic:100`, the latter named
   `Q0_F64`). That is a NO-FLOAT64 defect, pre-existing, separate from the pin
   question, and not fixed here.

### Where the batch actually stands

Nothing in this batch is executable until either `1j39` gives the 7 a witness
mechanism, or the owner accepts a reroute with no before/after record. The
latter is not mine to decide. **Do not re-attempt this batch expecting it to
be the "cheap" one** — that was this bean's own framing and it was wrong.

The 12 blocked on muon-built upstreams remain the critical path for
`qou-1c4y`, unchanged.

=== INTERSECTION WITH THE ideal_muon CARVE-OUT (from qou-6p3b, 2026-08-29) ===

This bean measures the bypass corpus-wide (85 producers). Here is the cut that
decides whether Tranche A can be finished at all:

  ideal_muon on main:            32 stems
    group A, manifest-driven:    14   <- QOU_Q0_ANCHOR reaches these
    group B, reads the pin file: 17   <- it does NOT
    source not found on disk:     1   (alpha_high_precision)

So 53% of the muon carve-out is inside this bean's blast radius. For those 17
the manifest entry is DECORATIVE: they take muon from the file whether or not
the stem is listed, so migrating them by editing q0_anchor_manifest.json moves
no number at all.

WHY THIS IS A CORRECTNESS ISSUE AND NOT ONLY AN ARCHITECTURE ONE

proton_pin_assertion_check.py decides "may this producer be migrated?" by
setting QOU_Q0_ANCHOR=physical and reading the producer's own assertions. On a
group-B producer that override is inert: it would run at MUON, pass its
muon-tuned assertions, and be reported PASSES-AT-PROTON. A false pass on a
migration question is worse than no answer, because nothing distinguishes it
from a real one.

Fixed on the qou-6p3b branch (PR #5755) by refusing rather than guessing: new
verdict UNSOUND-ENV-BYPASS, decided from the producer source BEFORE running, so
it costs 0 s and cannot dirty the tree. Verified on cross_check_trM_1ppb.
That makes the tool honest; it does not make the 17 measurable. Only routing
them through q_parameter does — i.e. this bean.

THE 17:
  atomic_tr_m_mpfr_50dps, chi_lambda_he4_full_partition_table,
  cross_check_trM_1ppb, cross_check_trM_cw_seminormal_leg,
  frakV_askey_wilson_recurrence_tie_probe, he4_binding_k_stage2_probe,
  he4_stage2_ranking_seminormal_xcheck, lambda_scale_substrate_probe,
  q0_anchor_consistency_audit, q1_mass_gap_probe, q_pinning_50_digit,
  qbeta_decay_sdp_extended_ck, qbeta_fsc_g_pattern_comparison, qbeta_physics,
  qbeta_symbolic_sdp_strict_complementarity, rho_f_categorical_probe,
  wlambda_q0_continuation

CAUTION — at least three of these must NOT be routed:
q_pinning_50_digit DEFINES the anchor (AGENTS.md constraint 1: never re-pin the
anchor-defining witness); q0_anchor_consistency_audit is the flip detector and
needs both pins; cross_check_trM_1ppb states in its own source that the L1
cross-check must run under the muon pin. So the drainable set is at most 14, and
each needs its rationale read before it is touched.

Reachability data committed at
computations/audits/proton-pin-assertion-verdicts.json (PR #5755).

=== LANDED 2026-08-30 — PR #6054 merged as c6003a5103 (rebase, 4 commits) ===

VERIFIED ON MAIN, not assumed: both stems in physical_proton; ideal_muon 21 ->
19, physical_proton 707; AGENTS.md carries -7.4588 with zero -8.006 remaining;
the regenerated downstream witness agrees field-for-field with its upstream
source and stamps q0Anchor: proton.

FOUR THINGS WORTH KEEPING, in descending order of how much they cost to learn.

1. THE REACHABILITY DETECTOR WAS WRONG IN BOTH DIRECTIONS, AND THE COUNT HID IT.
   Matching the bare strings "q-pinning-50-digit"/"q_pinning_50_digit" anywhere
   in a source gave 15 of 21 refused. The CORRECTED test also gives 15 — over a
   different set. False positive: rho_f_categorical_probe names the producer in
   a docstring link and never reads the witness (refused though measurable; run,
   it returns NO-ASSERTIONS). False negative: qbeta_jacobi_anger_tower_general
   reaches muon via q_muon_at() and never names the file, so NO filename test of
   any tightness sees it — it was being RUN, i.e. a false pass, the dangerous
   direction. The fix had to WIDEN (q_muon_at, _q0_value_for_anchor,
   load_q_50dps) as well as NARROW. A matching count is not agreement.

2. c_k^even ARE ANCHOR-INDEPENDENT. Byte-identical at both pins; only the
   abs_ck_uk products move, by ~4e-7 (11.5 ppb amplified by u^2). I claimed a
   7-9 % anchor effect and retracted it. The error: comparing a committed
   witness against a fresh PROTON run and attributing the whole delta to the one
   variable I had changed. The control I skipped — the muon re-run — costs
   seconds. Same shape as the aoperator HOLD inversion in #5755. NEVER attribute
   a c_k move to an anchor without running BOTH legs.

3. THE 7-9 % WAS A WITNESS THAT HAD NEVER BEEN REGENERATED. The producer's own
   upstream source (qbeta-c4even-exact-sseries.witness.json) already carried the
   fresh values, byte-identical, stamped proton. My hypothesis that -8.006 was a
   leftover convention-C value is REFUTED: it is unchanged at every commit
   touching the file, including 70d1ade383 ("excise C tiers 2+3: 176 producer
   sites to convention D") and 119885a4c6 ("re-run 154 muon/proton producers").
   It did not move at the C->D excision. Recording the discarded hypothesis
   because "stale because convention C" would have been a plausible and entirely
   wrong entry in the C-migration ledger.

4. A NON-ZERO EXIT IS NOT EVIDENCE ABOUT THE ANCHOR. New BROKEN-AT-BOTH verdict:
   qbeta_hoefsmit_tbeta_matrix_build_probe dies on the mpf.__format__ TypeError
   identically at both pins. FAILS-AT-PROTON would have frozen a merely broken
   producer in ideal_muon forever. Second leg spent only on failure.

CARVE-OUT STATE (re-measure before quoting — it moved 35 -> 32 -> 21 -> 19 in
under a day as siblings drained in parallel):
    group A measurable   5  ->  now 3 with both migrations landed
    group B refused     15

NEXT
 1. hadron_knot_table — last measurable stem, never run. AGENTS.md records
    >50 min for ONE bound atom: budget --timeout 7200 --log-dir. The tool is
    crash-safe and resumable, so a container reclaim is survivable.
 2. The 15 refused stems CANNOT be measured by this tool by construction. They
    need routing through q_parameter first. At least three must NEVER be routed:
    q_pinning_50_digit (defines the anchor), q0_anchor_consistency_audit (the
    flip detector, needs both pins), cross_check_trM_1ppb (its own source says
    the L1 cross-check must run at muon).

=== hadron_knot_table: UNKNOWN at 7200.15s (2026-08-30T04:57:29Z) ===

The fifth and last MEASURABLE stem is now measured. Verdict UNKNOWN, and the
run was clean: 100% CPU throughout (7196s cpu / 7190s wall, RSS 611 MB), tree
clean afterwards, checkpoint in_flight cleared.

WHAT IT ESTABLISHES — a much stronger bound than AGENTS.md carries

AGENTS.md records deuterium "ran for a full 50 minutes and was killed by its own
timeout". This run extends that by more than 2x:

  - all THREE A=1 atoms (proton, neutron, protium) were complete by the FIRST
    30s progress tick;
  - the producer log then NEVER GREW again, across 239 further ticks;
  - so deuterium -- atom 4 of 19, the first BOUND atom -- consumed >=7170s
    (~2 hours) and did not finish.

The step from the A=1 group to one bound atom is therefore >239x, measured
rather than inferred.

WHAT IT DOES NOT ESTABLISH

Whether hadron_knot_table works at the proton pin. A timeout is silent on that.
It stays ideal_muon as UNMEASURED, NOT held-for-cause -- the same distinction
that had to be restated for block_swap_binding, and the one whose collapse
produced the backwards aoperator HOLD at the start of this arc.

WHY THIS ONE IS MORE USEFUL THAN block_swap_binding's UNKNOWN

block_swap_binding printed one row and stopped, so its timeout located nothing.
This producer reports PER ATOM, so the wall is pinned exactly: atom 4, the first
bound one. That is the difference between "somewhere past row 1" and a named
boundary, and it is why per-unit logging was worth insisting on.

CONSEQUENCE FOR ANY RE-RUN

Do NOT simply raise the budget. 19 atoms at >2h for the first bound one is not a
budget problem; a full table is out of reach by orders of magnitude. If the
anchor question for this producer matters, the tractable routes are (a) run it
restricted to the A=1 atoms, which complete in <30s and DO exercise the pin, or
(b) instrument deuterium to report intermediate progress so the cost is
attributable. Neither is done here.

MEASURABLE SURFACE NOW FULLY ACCOUNTED FOR (5 of 5)
  alpha_5_lp_dual_crystal                   PASSES-AT-PROTON  -> MIGRATED
  qbeta_c4even_ladder_reconstruction_probe  PASSES-AT-PROTON  -> MIGRATED
  rho_f_categorical_probe                   NO-ASSERTIONS
  qbeta_hoefsmit_tbeta_matrix_build_probe   BROKEN-AT-BOTH
  hadron_knot_table                         UNKNOWN (>=7170s on atom 4 of 19)

The remaining 15 are UNSOUND-ENV-BYPASS and cannot be measured by this tool at
all until they route through q_parameter. Three of them must never be routed.


## Manifest audit: 2 of 753 stems point at a producer that no longer exists (2026-08-30)

Fell out of refreshing the reachability block for #6105. Method: for every stem in
`computations/q0_anchor_manifest.json`, rglob `computations/**/<stem>.py` with the
check tool's `SKIP` tuple applied. 753 stems audited — `ideal_muon` 19,
`physical_proton` 718, `ambiguous` 16.

| list | stem | only file | deprecated in |
|---|---|---|---|
| `ideal_muon` | `alpha_high_precision` | `_deprecated/alpha_high_precision.py` | `f62425070e` 2026-08-25 |
| `physical_proton` | `binding_k_enumerator` | `_deprecated/binding_k_enumerator.py` | `626f332b08` 2026-08-10 |

`ambiguous` is clean.

**The two are not equivalent, and the asymmetry is the point.** `q_parameter`
selects by `Path(sys.argv[0]).stem`, and its default for an unlisted stem is
proton. So:

- `binding_k_enumerator` under `physical_proton` is genuinely **inert** — the entry
  restates the default. Deleting it is a true no-op.
- `alpha_high_precision` under `ideal_muon` is **not inert**. Running
  `computations/_deprecated/alpha_high_precision.py` directly still matches the
  entry and rebinds every constant to the **muon** pin. Deleting the entry would
  silently re-pin that file to proton.

I have changed neither. The muon one is a behaviour change on a file the corpus
has deliberately excised as a fit, which is exactly the sort of quiet re-pin the
2026-08-19 sweep constraints exist to prevent; the proton one is not worth a
commit on its own.

**Do not count either as an unmeasured group-A hold.** They are not producers
awaiting a verdict — they are manifest entries whose producers were excised
deliberately, in commits that did not update the manifest.

**A stale GAP bean fell out of it.** `qou-2zjp` (*'alpha_high_precision is broken
on main — bisection bracket no longer contains a root'*) is still `todo`, last
updated 2026-08-25T01:03Z — **hours before** the excision commit the same day. Its
measurement stands; whether the bean is moot depends on whether its convention-C→D
`z` diagnosis generalises beyond the one file. Noted on that bean; not closed,
because that is a scope judgement and I did not write it.


## Option-1 routing COMPLETE — 9 of 9, and the detector was lying about all of them (2026-09-03)

Owner chose option 1 (route all). Done. Two of the nine were carrying live
defects, and the tenth finding was in my own tool.

### The nine

`qbeta_physics`, `cross_check_trM_cw_seminormal_leg`,
`qbeta_fsc_g_pattern_comparison`, `he4_binding_k_stage2_probe`,
`he4_stage2_ranking_seminormal_xcheck`, `qbeta_decay_sdp_extended_ck`,
`qbeta_symbolic_sdp_strict_complementarity`,
`frakV_askey_wilson_recurrence_tie_probe`, `lambda_scale_substrate_probe`.

All stay `ideal_muon` except `cross_check_trM_cw_seminormal_leg` → `physical_proton`
(its reference witness is proton-stamped).

**Safety invariant, established before anything was touched:** `q_parameter`
derives the muon anchor from `q_muon_at(70)`, byte-identical to all 70 digits with
what the direct reads returned. So routing moves no number, and every regenerated
witness must be metadata-only. Verified per file; the two exceptions are called out
below rather than smoothed over.

### Two live defects found by doing it

**`cross_check_trM_cw_seminormal_leg` was RED on `main`.** It compares against
`markov-peel-atomic-tr-m.witness.json` (stamped `q0Anchor: proton`) at a 1e-15
tolerance while pinning itself to muon — a gap seven orders of magnitude wider
than the tolerance. `|Δ|/ref` 7.89e-08 … 2.53e-07 FAIL on all six atoms →
1.46e-50 … 5.70e-50 OK. **The bypass is what hid it:** group-B producers are
precisely the ones the assertion check cannot run.

**`qbeta_physics` was straddling a caller by 30 ppb.** Not a producer — no
`main()`, no witness, never `sys.argv[0]`, so its own `ideal_muon` listing could
never fire. `paper_six_term_isotope_sweep` (unlisted ⇒ proton) imports `Q_MP` at
line 81 and used it at 107/1103, then called `compute_substrate_quantities()` and
got muon: 11.6141 ppb in q₀, **30.1589 ppb in `Q_A`** (amplified ~2.6× by the
`|q²−2q−1|` near-cancellation).

### A third bypass mechanism, invisible to every q₀ detector

`os.environ.setdefault("QOU_Q0_ANCHOR", "ideal")` — a script forcing its own
anchor at import, overriding the manifest, matching **none** of the pin markers.
Found and removed in `cross_check_trM_cw_seminormal_leg:42` and
`he4_binding_k_stage2_probe:77`. **One remains:**
`deltalambda/he4_binding_k_presentation_correction_probe.py:77`.

### The detector was reporting all nine as still bypassed

`env_override_reaches()` substring-matched the witness **filename**, which cannot
tell reading a file from mentioning it. It matched routing comments,
`w.add_upstream(witness_path(...))` provenance edges, and a witness string
describing history. Fixed: key on **`derived_50_digit`**, the field a value-read
always subscripts and a provenance reference never does, over comment- and
docstring-stripped source.

**My first fix attempt was itself wrong** — making "imports a q from
`q_parameter`" decisive is too strong, since a file doing *both* is still
bypassed; it turned `cross_check_trM_1ppb` and `atomic_tr_m_mpfr_50dps` into
false positives. Caught by a 15-case test, not by eye. Verified 15/15 before
adoption.

| | before | after |
|---|---|---|
| group A (measurable) | 3 | **11** |
| group B (env-bypassed) | 15 | **6** |

**Part of that movement is producers being fixed and part is the detector
stopping lying about them — do not quote it as one thing.**

### B is now exclusions only, all six principled

Anchor definer; flip detector (needs both pins); L1-muon cross-check (its source
says so); dual-layer producer (asserts both); deliberate two-anchor comparison;
and `q1_mass_gap_probe`, which validates `two_q` and `plancherel_weights_n3` from
the **same** witness — values derived at its own q₀ — so routing q₀ away while
keeping those comparisons would manufacture the very straddle this tranche
removes. Nothing is left in B by accident.

### Two shifts that looked like mine and were not

- `qbeta_symbolic_sdp_strict_complementarity` reports "2 assertions, FAILURES".
  The committed witness already carried `allPassed: false`, and the producer's
  own verdict is a deliberate NEGATIVE. Checked against `git show HEAD:`.
- `lambda-scale`'s `lambda_n_target` moved at the **16th digit** (~9.7e-17) —
  float64 epsilon, wrong *shape* for the 0.0769 ppb anchor scale. Two controls:
  importing `q_parameter` does not change `mp.dps` (80 → 80), and re-running the
  **unrouted** original gives the identical new value. Pre-existing staleness.

### Still open

The he4 witness pair. `he4-binding-k-stage2.witness.json` still carries the
**retired** pin and is the authoritative value the xcheck reads back; its
producer is long-compute (154 characters, checkpointing). The xcheck's
regenerated witness is deliberately **not committed** — alone it would bake in a
0.0769 ppb straddle. They move together.

Also open: the one remaining `setdefault` in
`he4_binding_k_presentation_correction_probe.py:77`.


## TRAP (second instance, new variant): `pgrep -f` matched my own WAIT LOOP

Recorded because I fell for the same class twice in one arc and the second form
is worse than the first.

**First form**, earlier this arc: `pgrep -f <producer>` matched the *tool*
running the producer, because the tool's argv carries the producer's filename. I
profiled the wrapper and reported a 0 %-CPU hang on a run that was at 100 % CPU.

**Second form, 2026-09-03**: I armed
`until ! pgrep -f "python3 -u deltalambda/he4_binding_k_stage2_probe"; do sleep 20; done`
as a background wait. That loop's own command line **contains the pattern**, so
`pgrep` always matches it, the condition is never true, and the loop cannot
terminate. Worse, every later `pgrep` check I ran returned that loop's PID — so
the producer looked alive for hours after it had died.

**What it cost.** The producer actually died at 05:09:31 when the container
restarted, at 109/154 characters. I reported "still running, 109/154,
checkpointing" **twice** afterwards, on the strength of a PID that was my own
watcher. Caught only by checking `stat -c '%y'` on the log and the checkpoint:
both 3.5 h stale while `pgrep` still returned a PID.

**The discriminators, in order of reliability:**

1. **File mtime.** `stat -c '%y' <log> <checkpoint>` — a live long-compute writes
   periodically. A stale mtime is proof of death; a fresh PID is not proof of
   life.
2. **`ps -eo pid,%cpu,cmd` with the watchers filtered out**
   (`| grep -v "pgrep\|grep\|until"`), and read the %CPU. The real producer here
   shows 384 %; a wrapper or a watcher shows 0.0.
3. **Never wait with a loop whose own command line contains the pattern it
   greps for.** Key the wait on the LOG instead:
   `until grep -qE "witness ->|Traceback|Error|Killed" <log>; do sleep 30; done`.
   The loop's argv contains the log path, not the producer name, so it cannot
   match itself — and the alternation covers failure as well as success, so
   silence is not mistaken for progress.

Generalisation worth keeping: **a process-existence check is the weakest
evidence of progress available.** Prefer evidence the work itself emits.


## TRAP: `cmd | tail -N && git push` masks the exit code — I force-pushed a mid-rebase HEAD

**What happened, 2026-09-03.** I ran, as one line:

    git rebase origin/main 2>&1 | tail -2 && git push --force-with-lease

The rebase hit a conflict and stopped at **commit 2 of 10**. The push ran anyway
and **force-updated the remote to a branch missing 8 of my 10 commits.**

**Why `&&` did not protect me.** In a pipeline, `$?` is the exit status of the
LAST command, not the first. `git rebase` exited non-zero; `tail` exited **0**;
`&&` saw 0 and proceeded. The `| tail -2` I added purely to keep the output short
is what disarmed the guard.

**Why `--force-with-lease` did not protect me either.** The lease checks that the
REMOTE has not moved since I fetched. It had not — *I* was the one moving
backwards. A lease guards against clobbering someone else's push; it says nothing
about whether your own local ref is in a sane state.

**Cost.** Nothing was lost (the commits were in the rebase todo and the reflog),
but for several minutes the PR's branch on GitHub contained one commit out of
ten, and anyone reading it would have seen a truncated tranche.

**Rules, going forward:**

1. **Never pipe a command whose exit status gates the next one.** If output
   needs trimming, capture it: `out=$(git rebase origin/main 2>&1); rc=$?; echo
   "$out" | tail -2; [ $rc -eq 0 ] || exit 1`. Or use `set -o pipefail`.
2. **Never chain rebase and push in one line at all.** Rebase, then *check*
   (`ls -d .git/rebase-merge`, `git rev-list --count origin/main..HEAD`), then
   push as a separate call. The check is one command and it is the whole
   protection.
3. **Before any force-push, assert the commit count.** I expected 10 and the
   local ref had 1. A single `git rev-list --count origin/main..HEAD` compared
   against what the tranche should contain would have caught it before the push
   rather than after.

Same family as the `pgrep` trap recorded above: **a convenience wrapper around a
command silently replaced the signal I was reading.** There, the watcher's argv
matched the pattern; here, `tail`'s exit code replaced `rebase`'s.


## LANDED — the option-1 tranche is complete on main (2026-09-03)

Five PRs merged: **#6105, #6151, #6163, #6495, #6504.**

**End state, measured on main after the last merge:**

    ideal_muon = 19    A = 12    B = 6    no-live-producer = 1

B is exclusions only: `q_pinning_50_digit` (defines the anchor),
`q0_anchor_consistency_audit` (flip detector, needs both pins),
`cross_check_trM_1ppb` (source requires muon), `atomic_tr_m_mpfr_50dps`
(dual-layer, asserts both), `qbeta_jacobi_anger_tower_general` (deliberate
two-anchor comparison), `q1_mass_gap_probe` (validates other fields of the same
witness, derived at its own q₀). Nothing in B by accident.

### Ten producers routed, not nine

The tenth (`he4_binding_k_presentation_correction_probe`) was a loose end I
created: converting its `setdefault` to a manifest listing made a
previously-UNLISTED stem visible to the split for the first time, and it was
correctly flagged bypassed because the conversion left the value read in place.
The count going 6 → 7 was the measured surface growing, not a regression.

### Two claims of mine that needed correcting after the fact

1. **"B = 6"** was measured on my branch before I listed the tenth stem. On main
   it read 7 until #6495 routed it.
2. **"Verified 15/15"** was true for the set I tested — the 9 routed producers
   and the 6 exclusions — and I stated it as though it established the detector
   generally. It did not. A test set assembled from files I had just edited
   cannot exhibit a shape none of them had, and #6504 found exactly such a shape:
   `derived_50_digit` inside a witness PAYLOAD STRING, surviving both the
   comment and docstring stripping.

**Residual blind spot, recorded rather than fixed:** the detector still counts a
descriptive payload literal naming the field. Teaching it to separate prose from
a subscript key is a fragile discriminator (`d["derived_50_digit"]` is a
Constant too), and in the one case found the string was independently stale. If
a second instance appears, that is the signal to revisit.

### What doing the routing surfaced that nothing else would have

- `cross_check_trM_cw_seminormal_leg` **RED on main**, 1e-7 against a 1e-15
  tolerance → 1e-50 green. Hidden precisely BECAUSE it was group-B.
- `qbeta_physics` straddling one caller by **30.1589 ppb** in `Q_A`.
- A third bypass mechanism (`os.environ.setdefault("QOU_Q0_ANCHOR", …)`) that no
  q₀ detector could see — 3 found, **0 live remain**, AST-verified.
- A false negative in the detector itself, reporting every correctly-routed file
  as still broken.
- The he4 pair regenerated together off the retired pin (2 of `qou-3f7a`'s
  population drained as a side effect).

### Three traps recorded above, one family

`pgrep -f` matching its own wait loop; `| tail` masking a failed rebase's exit
code so a force-push shipped 1 of 10 commits; a payload string defeating a
source-stripping detector. In each, **a convenience layer silently replaced the
signal being read.**


## Re-measured 2026-09-06 — the tranche has HELD, and the audit's own witness was stale

Found by `scripts/bean-staleness-triage.py` (7th of 291 artifact beans, 29
commits over its named paths since 2026-09-03).

### The 2026-09-03 end state still holds

`computations/q0_anchor_manifest.json` on `main`: **`ideal_muon` = 19**,
`physical_proton` = 907, `ambiguous` = 15 — unchanged from the recorded
`ideal_muon = 19 / A = 12 / B = 6 / no-live-producer = 1`. Nothing has regrown.

### But `muon_anchor_reader_invisible_staleness_audit` had NOT been re-run

Its committed witness was written at `d3011b1d66`; the producer was edited
afterwards at `23d95c998f` (*"ratchet the q0-dataflow blind spot — and key it
on structure, not on the date"*), so the recorded numbers were one
producer-generation behind. Re-ran it (12 s, exit 0, **6/6 assertions pass**)
and committed the honest result — `2250c83978`, not hand-edited.

| | committed | re-run |
|---|---|---|
| `producers_reading_anchor` | 86 | **88** |
| `paired_by_provenance` | 65 | **66** |
| `paired_by_stem` | 31 | **30** |
| `visible_to_a_q0_gate` | 52 | **55** |
| `at_risk` (invisible class) | 4 | **3** |

The reader surface **grew** by 2 while the at-risk set shrank by 1: the
invisible class loses `qbeta-markov-trace-norm-probe`, leaving
`lambda-scale-derivation-probes-123`,
`qbeta-c3-per-block-categorical-probe` and `qbeta-symbolic-tbeta-min-l2`.
So the surface is not converging on its own — it is being drained faster than
it accretes, which is a different claim and the one the numbers support.

### A nuance worth carrying about the "0 of ~700 safe to refresh" rule

That finding (`qou-e9pp`) is about refreshing **blind** — re-running expensive
producers whose numbers cannot move. It is not a prohibition on regenerating a
cheap audit whose numbers demonstrably *did*: this producer is a 12-second scan
with no free parameters and a changed `scriptHash`, so re-running it is the
correct handling rather than an exception to the rule.

### Status

The option-1 tranche is landed and holding; the open item is unchanged and is
the one this bean says must not be resolved by editing 85 files — **which of
the two readings of the anchor-read idiom is intended.** Nothing here settles
that, and nothing here needs it settled.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

In-progress in Round 100 PR litlfred/qou#8447.
