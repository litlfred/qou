---
# qou-6p3b
title: 'qfac/dim_q threading: 12 decisions, not 133 edits (scoped)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:15:32Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-4cu3
---

## Scoped 2026-08-24 — full analysis in docs/audits/2026-08-24-qfac-dimq-threading-scope.md

Follow-on to `qou-wee5` (closed, #5646). **The site count is the wrong unit.**

### Measured (main @ b134176d93)

    191 call sites; 47 already pass q; 144 defaulted
    -11 generated qou-mass mirror (regenerated, never hand-edited)
    = 133 LIVE in 67 files -> 114 in producers, 19 in library modules

Producer sites by their own manifest bucket: 85 unlisted (->proton),
28 physical_proton, **1 ideal_muon**.

### The reframe

The anchor is a property of the RUNNING PROCESS, not the file. Threading
`Q0_PROTON` is **inert wherever the entry point already resolves proton — 113
of the 114 producer sites.** Those edits change no number today.

Real cost = entry points that can resolve muon AND reach these functions:
**12 muon producers.** And **11 of the 12 reach them INDIRECTLY**, via
`mass_at_3A_proper` / `hecke_characters` — only
`qbeta_hoefsmit_tbeta_matrix_build_probe.py:124` calls `dim_q` directly.

**So editing 133 call sites would leave the 11 exactly as they are.**

### Known failure mode, already paid for

Forcing proton on a deliberately-muon producer creates a NEW straddle. Measured
in #5634: `vhat_per_crossing_chain` moved 17 fields and flipped its own
`scalar_vs_matrix_agree` True -> False. It and `he3_tritium_cosh_asymmetry_diagnosis`
were reverted to their own q, then moved 0. **2 of the 12 are confirmed
deliberately muon; the other 10 are unadjudicated.**

### Recommended: B -> A -> C

- **B (API):** optional forwarding `q` on `mass_at_3A_proper` /
  `hecke_characters` entry points, using the backwards-compatible shape proven
  in #5646. Required before A is even expressible for the 11.
- **A (12 decisions):** per producer — deliberately muon (pass its own q) or
  accidentally muon (migrate + regenerate)? 14 witnesses in scope. ALL the
  judgement lives here. **Sequence behind #5500** (muon anchor -> CODATA 2022,
  audit red, 53 witnesses) — it collides directly.
- **C (113 inert sites):** mechanical, expect 0 fields moved, batch-sweep
  exception applies. **Buys no correctness today** — purely preventative against
  a producer later joining `ideal_muon`. Worth doing or not is a judgement call,
  and should be made as one rather than assumed.

### Not claimed

Nothing straddles today — the gate is green (clean=8 / STRADDLE=0). And which of
the 10 unadjudicated producers is deliberate is exactly what must not be guessed.


## Tranche A adjudicated — it is 7 decisions, not 10, and now 2/2/3 (2026-08-24)

### Three were already settled in AGENTS.md, not open at all

§q0-anchor-convention (~line 2023) names three producers that **refuse a proton
run by design**: `atomic_tr_m_mpfr_50dps` (dual-layer, one witness per layer),
`he4_stage2_ranking_seminormal_xcheck` (asserts the muon prefix off the
anchor-defining witness), `cross_check_trM_1ppb` ("L1 cross-check must run under
the MUON q0 pin"). An independent evidence scan flagged the same three before I
read that passage.

Plus the two measured deliberate in #5634 (`vhat_per_crossing_chain`,
`he3_tritium_cosh_asymmetry_diagnosis`). **5 of 12 settled; 7 open.**

### The 7, measured under an anchor flip — RUN TWICE, identical both times

| producer | verdict | disposition |
|---|---|---|
| `lever1_binding_habiro_single_element_test` | **clean** | MIGRATE — listing is inert |
| `gg_production_bond_probe` | **NO-WITNESS** | MIGRATE — writes nothing, no artifact consequence |
| `aoperator_a5_crosscheck` | **STRADDLE, 13 fields incl `/allPassed`** | **HOLD** |
| `qbeta_hoefsmit_tbeta_matrix_build_probe` | **STRADDLE, 3 fields at `/…/dim_q`** | **HOLD** |
| `binding_via_interface_knot` | TIMEOUT 240s | UNTESTED — needs a longer budget |
| `block_swap_binding` | TIMEOUT 240s | UNTESTED |
| `gram_norm_binding_probe` | TIMEOUT 240s | UNTESTED |

Run 1 spanned a branch switch while Tranche C was modifying `hecke_characters`
— the module `qbeta_hoefsmit`'s moving `dim_q` field comes from — so it was
re-run on the committed tree. **Identical, verdict for verdict and count for
count.** The risk was real to flag and did not materialise.

### The correction this measurement forced

I had recommended migrating SIX on header evidence — none of the seven mentions
muon or cross-anchor comparison, and binding is scale-cancelling. Measurement
says `aoperator_a5_crosscheck` flips `/allPassed`, a BOOLEAN ASSERTION, under
the anchor. That is the `vhat_per_crossing_chain` signature exactly.

**Header silence is not evidence of accidental listing.** Migrating it would
have broken a producer's own consistency check — the same failure #5634 already
paid for once.

### Defensible action

**Migrate 2, hold 2, measure 3** — not "migrate 6". Still sequenced behind
PR #5500 (muon anchor -> CODATA 2022, audit red, 53 witnesses), which touches the
same witnesses.


## CORRECTION: the anchor-flip verdicts on 5 of the 7 were UNSOUND (2026-08-24)

I ran all seven through `anchor_flip_straddle_audit` **by explicit path**, which
bypasses the `--candidates` selector. That selector exists to enforce the
audit's own stated precondition — *sound only for producers with a q of their
own*. I quoted that precondition in the tool and then did not apply it.

Measured, do these producers have an INDEPENDENT q (not the manifest-resolved
shim)?

| producer | q source | audit sound? |
|---|---|---|
| `aoperator_a5_crosscheck` | shim only | **NO** |
| `binding_via_interface_knot` | **no q at all** | **NO** |
| `block_swap_binding` | shim only | **NO** |
| `gg_production_bond_probe` | shim only | **NO** |
| `gram_norm_binding_probe` | shim only | **NO** |
| `lever1_binding_habiro_single_element_test` | independent | yes |
| `qbeta_hoefsmit_tbeta_matrix_build_probe` | independent | yes |

**A producer whose only q is the manifest's cannot straddle** — there is no
second layer to mix. Its numbers move under an anchor flip because you changed
its one and only anchor. That is a RE-PIN, which is trivially true, not a
defect.

### What survives

- `lever1_binding_habiro_single_element_test` — **clean**, and the verdict is
  sound. MIGRATE, free.
- `qbeta_hoefsmit_tbeta_matrix_build_probe` — **STRADDLE at `/…/dim_q`**, sound.
  HOLD. This is the one real straddle in the set.

### What was wrong

- `aoperator_a5_crosscheck` "STRADDLE, /allPassed flips" is **NOT a straddle**.
  `/allPassed` is `all(a["passed"] …)`; with no independent q, the flip means an
  assertion whose EXPECTED side is anchor-independent while its computed side is
  not. Still a concrete reason to HOLD it — just a different defect class, and
  the hold now rests on the right evidence.

### What this saved

I was about to spend HOURS measuring the three TIMEOUT producers. One leg of
`binding_via_interface_knot` alone exceeded 1700 s without finishing. **The
measurement could never have answered the question** — all three lack an
independent q, so the instrument does not apply to them. Killed the run.

### Disposition for the 5

Pure policy: should they be muon-pinned? **No straddle risk either way**, because
none has a second layer. `aoperator_a5_crosscheck` should still be held for its
assertion. The other four are free to migrate on the directive alone, with the
usual per-producer witness diff.

TRANCHE A — PR #5755 (draft), branch claude/tranche-a-proton-assertion-check-2026-08-25.

TWO COMMITS

  1. computations/audits/proton_pin_assertion_check.py — a second tool, asking
     what the anchor-flip test cannot: does this producer's OWN assertions
     still pass at the proton pin? Sound regardless of whether the producer
     carries a q of its own (the precondition 5 of my 7 earlier anchor-flip
     verdicts violated, #5721). Verdicts PASSES-AT-PROTON / FAILS-AT-PROTON /
     NO-WITNESS / UNKNOWN; a timeout reports UNKNOWN, never a pass.

  2. aoperator_a5_crosscheck migrated ideal_muon -> physical_proton.

MY HOLD WAS BACKWARDS. Measured, both legs:

    physical  allPassed=True   failing=[]
    ideal     allPassed=False  failing=['a5_per_lambda_max_abs_diff']

It works at proton and FAILS at muon. I had recommended holding it because it
"depends on the muon pin"; it depends on the proton pin. Worse than a
mis-scoped hazard: sitting in ideal_muon, it ran AS CONFIGURED at the anchor
where one of its own assertions fails, while its committed witness claimed
allPassed=true. Both cannot be right.

HOW IT WENT WRONG: I took the DIRECTION from the sign of a boolean flip
without checking which leg was which. Seeing "/allPassed moves" I assumed it
moved toward failure at proton. Only calibrating the new tool against a known
answer surfaced it before it shipped as advice.

RESULT: allPassed True->True; q0Anchor None->proton (was UNSTAMPED); 22s; no
sibling churn. 14 non-ephemeral fields move, all cross-check residuals at
1e-12..1e-15 against a ~1.9e-6 tolerance.

FLAGGED, NOT EXPLAINED: the tolerance moves 1.9177226708e-06 -> 1.9177218447e-06,
rel 4.31e-7 = 37x the 11.5 ppb mu-p tension. CONSISTENT WITH a high power of q
(at A=5, lambda|-15) but I have NOT verified that mechanism and am not
asserting it. Six orders of margin either way, so it does not affect the
migration. Needs someone who knows what that tolerance is built from.

VERIFICATION — precision-gates exits 1 AND THE RED IS NOT MINE. I claimed
exit 0 before checking; corrected. Red is the raw-float64 ratchet at 4 NEW
dirty witnesses (deltalambda/deuteron-interface-handle-curvature,
qbeta/birkhoff-barodd-pythagoras-bridge, qbeta/a3-branching-asymmetry-vs-required,
deltalambda/yekutieli-trefoil-surface2form-discretization) — all last touched
2026-08-09, sixteen days ago, so a long-standing red on main, not today's
sibling churn. Two proofs: git diff origin/main...HEAD reports all four
IDENTICAL to origin/main, and the audit is a pure function of (witness tree,
baseline) while this branch moves one witness at delta 0 and leaves the
baseline alone. aoperator was ALREADY baselined; 15 -> 15 fields, delta 0.
No baseline widened.

NOT MIGRATED, DELIBERATELY
  - binding_via_interface_knot fails identically at BOTH anchors in 2s on
    data_loaded ("AME 2020 deuteron binding") — pre-existing broken, already
    recorded allPassed:false in its committed witness. Re-pinning a producer
    that cannot run buys nothing. (Also corrects my earlier claim that one leg
    exceeded 1700s; on current main it exits in 2s.)
  - block_swap_binding, gram_norm_binding_probe: UNKNOWN, >1500s. Need a real
    budget, not a verdict.
  - Remainder of Tranche A sequenced behind #5500.
VERDICT 1 of 2 — block_swap_binding: UNKNOWN at 7200.33s (2026-08-25T12:40:30Z)

Recorded in the checkpoint with elapsed seconds, so the next budget is chosen
from a measurement rather than a guess. That was the point of the exercise; the
UNKNOWN is a result, not a failure to get one.

WHAT IT ESTABLISHES

  - a measured lower bound: this producer needs > 2 h at 4He, n=12. Before, the
    only figure was "exceeded 1500 s".
  - the proton override took effect: the log's own header reads
    q0 = 1.109978582751380807..., the proton pin, not the muon one.
  - it is NOT memory-bound and was never at OOM risk. RSS 223 -> 558 MB, linear
    at ~4.9 MB/min; host available was 14.7 GB. CPU 99.9 % with TIME == ELAPSED
    throughout, so it was computing, not hung or blocked on I/O.
  - the crash-safe restore works on a REAL 2-hour kill, not only in --selftest:
    0 dirty witnesses afterwards, `git status` clean.

WHAT IT DOES NOT ESTABLISH — and this is the part not to over-read

Whether block_swap_binding WORKS at the proton pin. A timeout is silent on that.
So it stays in ideal_muon: UNMEASURED and undecided, NOT held for cause. Those
two have looked identical in my reporting before, and conflating them is exactly
what produced the backwards aoperator_a5_crosscheck HOLD.

THE COST SHAPE — a linear budget increase is probably the WRONG next move

The producer's entire output in two hours was the header plus ONE row:

    sigma block-perm   tr_M(W_atom.beta)   tr_M(W_free.beta)
              id           2.89958832          12.60718540

and the log was already 455 B — i.e. that row was complete — at 19 s. It was
still 455 B at 7200 s.

So: row 1 finished in <= 19 s; row 2 did NOT finish in the remaining 7181 s.
That is a jump of > 378x between the first and second block permutation, which
says the identity row has a shortcut the others do not, rather than that the
whole table is uniformly slow. Doubling or quadrupling the budget is therefore a
bet on an unmeasured constant. The cheaper next step is to instrument the
producer to report per-row timing, or to establish the cost of ONE non-identity
row on its own, before spending another multi-hour block.

Not proposing that as work yet — recording it so the next agent does not simply
re-run at 4 h and lose another half day.

=== ARC REVIEW after 1603 commits on main (2026-08-29) ===

WHERE THE ARC STANDS

PR #5755 is still OPEN and draft. Nothing in it has landed. Measured against
main, not assumed:
  - proton_pin_assertion_check.py is NOT on main (only anchor_flip_straddle_audit).
  - aoperator_a5_crosscheck is STILL in ideal_muon on main.
  - ideal_muon 35 -> 32 (siblings migrated 3), physical_proton -> 689.
  - block_swap_binding, gram_norm_binding_probe: both still ideal_muon.

So the cds3 drain (#5989, #5992, 18 producers) did NOT subsume Tranche A; it
worked a disjoint set. No duplication, nothing of mine superseded.

THE FINDING GOT SHARPER, NOT STALER

Main ran a q0Anchor BACKFILL over 573 witnesses plus a flip-detector audit for
enforcement (b8eb7d9e66). Main's aoperator witness is STILL q0Anchor: None,
q0Value: None, asserting allPassed: true from ideal_muon — the anchor where its
own a5_per_lambda_max_abs_diff FAILS. The backfill missed it, so the enforcement
audit has nothing to enforce here. Re-ran the producer at proton on main's
current code (which changed twice in the interval): exit 0, 22s, q0Anchor
proton, allPassed True, 4/4 assertions. Reproduces.

FIVE SIBLING COMMENTS LANDED. THREE CHANGED THE TOOL.

1. #5792 — ENV-BYPASS, the serious one. QOU_Q0_ANCHOR is only read by
   q_parameter. A producer that loads q-pinning-50-digit.witness.json itself
   gets MUON regardless, so the check would run it at muon, pass its muon-tuned
   assertions, and report PASSES-AT-PROTON. MEASURED: 17 of 32 ideal_muon stems.
   (#5792 says 7 of 13 — a different subset, not a disagreement.)
   FIXED: new verdict UNSOUND-ENV-BYPASS, decided from source BEFORE running,
   0 s, cannot dirty the tree. Verified on cross_check_trM_1ppb.
   MY THREE VERDICTS ARE UNAFFECTED — all group A, checked not assumed.

2. #5805 — read the VALUE not the DELTA. True->False, True->null and the field
   going absent are three findings in one shape. `is False` silently passed the
   last two. FIXED: `is not True`, splitting FAILS-AT-PROTON from UNCLEAR. Added
   NO-ASSERTIONS: a producer that writes a witness but asserts nothing
   established nothing, and calling that PASSES was the same false reassurance
   one layer down.

3. #5765 — asked for a citable artifact. My verdicts were in /tmp, which the
   container reclaim duly took. FIXED: committed at
   computations/audits/proton-pin-assertion-verdicts.json with a READ_THIS_FIRST
   stating the soundness precondition, so it cannot be quoted without it.

ONE SIBLING INFERENCE IS WRONG, AND IT IS LOAD-BEARING

#5765 reads `_PINS = {muon, proton}` in aoperator_a5_crosscheck as a two-pin
COMPARISON PATH and asks whether this PR's migration broke it. There is no
comparison path. _PINS is a reverse-lookup that DERIVES the stamp from the q
the run actually used; the comment directly above it says "DERIVE the anchor
label from the q0 this run actually used — never assert it." Two consequences:
the migration breaks nothing, and this producer already does what #5699 is
generalising, so it is on the RIGHT side of the stamp-vs-arithmetic gap #5765
raises rather than an instance of it.

LONG-RUN STATE — the resumability earned itself

The container was reclaimed mid-run. /tmp/qou-proton-pin-check/checkpoint.json
SURVIVED, holding in_flight: gram_norm_binding_probe, so a restart restores the
tree and re-runs it. block_swap_binding's UNKNOWN (7200.33s) is preserved.
gram_norm is recorded PENDING, not UNKNOWN — it was interrupted at ~2100s while
on 3H, and an interrupted run measured nothing.

NEXT, in the order I would take it:

  1. Land #5755. It is now even with main (merge resolved: main's manifest +
     my one move; main's witness + a real re-run). Blocked only on merge
     permission.
  2. The 17 group-B stems are the REAL Tranche A blocker, not the two slow
     producers. Until they route through q_parameter (qou-aj91 mechanism 5)
     their manifest entry is decorative and no assertion check can measure them.
     That is a bigger and more tractable target than another multi-hour run.
  3. gram_norm_binding_probe: restart from the checkpoint. Its per-isotope log
     will pin the wall at a specific n, which block_swap's could not.
  4. block_swap_binding: do NOT re-run at a larger budget. Row 1 <=19s, row 2
     unfinished at 7181s (>378x). Instrument per-row timing or cost one
     non-identity row first.

=== LANDED 2026-08-29 — PR #5755 merged to main as 8176c8270747 ===

Rebase-merged (AGENTS.md rule 8), 8 commits, 7 files. Live on main:
  - aoperator_a5_crosscheck is in physical_proton (verified on the merged tree).
  - computations/audits/proton_pin_assertion_check.py + its verdicts artifact.
  - the producer-level float64 tolerance fix.

TWO THINGS THE LANDING ITSELF TAUGHT

1. GitHub REFUSED the rebase-merge ("This branch can't be rebased") because the
   branch carried three merge commits from main. AGENTS.md already prescribes
   the fix under the squash prohibition — "clean the branch locally with git
   rebase -i and rebase-merge the cleaned-up history instead" — so no new
   decision was needed. Flattened locally onto main, force-with-lease, merged.
   Worth knowing before proposing squash next time: a branch that has merged
   main repeatedly is NOT a squash case, it is a local-rebase case.

2. THE REBASE SWEPT IN FOUR SIBLING AUDIT WITNESSES, and this is the durable
   lesson. q0-anchor-consistency-audit (639 lines), witness-provenance-audit
   (343), and the two witness-raw-float64--*-audit files rode along, because
   they regenerate as a SIDE EFFECT of every precision-gates run and each
   conflict resolution dutifully carried them forward.

   A resolution that is correct COMMIT BY COMMIT can still be wrong for the
   BRANCH: each replay only sees its own conflict, never the accumulated diff.
   The merge-based history had these correctly restored; the rebase reintroduced
   them. Reverted in 8176c82707.

   RULE: after any rebase, check the whole `git diff --name-only
   origin/main...HEAD` against the file set the PR is supposed to touch — not
   merely that each step resolved cleanly.

STATE OF THE ARC AFTER LANDING
  ideal_muon is now 21 stems (was 32 when this arc's review was written, 35 at
  its start) — siblings have been draining it in parallel. Re-measure before
  quoting; the 17-of-32 env-bypass figure recorded above is a 2026-08-29
  measurement against a list that is moving.

  NEXT, unchanged in priority:
   1. The group-B env-bypass stems (qou-aj91) — until they route through
      q_parameter their manifest entry is decorative and no assertion check can
      measure them. Bigger and more tractable than either slow producer.
   2. gram_norm_binding_probe — restart from the checkpoint; it is PENDING, not
      UNKNOWN (interrupted at ~2100s on 3H by a container reclaim).
   3. block_swap_binding — do NOT re-run at a larger budget. Row 1 <=19s, row 2
      unfinished at 7181s (>378x). Instrument per-row timing first.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

qfac/dim_q threading is q-deformation plumbing, not the Markov parameter. Keep
open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8292, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
