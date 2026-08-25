---
# qou-6p3b
title: 'qfac/dim_q threading: 12 decisions, not 133 edits (scoped)'
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:15:32Z
updated_at: 2026-08-25T09:51:12Z
updated_at: 2026-08-25T12:42:12Z
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
