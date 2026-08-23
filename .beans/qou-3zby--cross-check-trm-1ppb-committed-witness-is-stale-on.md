---
# qou-3zby
title: cross-check-trM-1ppb committed witness is stale on main — C/D straddle across its four methods
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T13:23:15Z
updated_at: 2026-08-23T08:53:19Z
---

Found during /prepare-merge on PR #5199 (provenance triage). NOT that branch's regression -- cross_check_trM_1ppb.py reads none of its files (inputs are atomic-tr-m-mpfr-50dps, canonical-tr-m-via-chi-cache, habiro-coefficients-extended, markov-peel-atomic-tr-m-muon, q-pinning-50-digit). Confirmed inherited: a pristine origin/main worktree (cbb49a1a35) exits 1 on the same gate.

The regenerated numbers show a C/D straddle ACROSS the four methods -- the chi path moved to D while peel and habiro stayed on C:

  metric            committed        fresh
  hoef_vs_chi         0.481        1.45e-07   <- improved 7 orders
  hoef_vs_peel      0.000182         0.325    <- degraded
  hoef_vs_habiro     6.02e-49        0.325    <- degraded
  rel_delta_max        0.4813        0.4810

6/6 atoms DIVERGE, 0 certified at 1 ppQ. hoef_vs_chi collapsing to 1e-7 is the tell that Hoefsmit and chi are now on the same convention; peel and habiro are not.

The regenerated witness was deliberately NOT committed on #5199: draining another arc's witnesses is that arc's work, and burying a substantive physics-gate change in an unrelated provenance PR hides the signal. This belongs to the convention-D cascade.

L1 impact: this IS the L1 compute-precision gate (AGENTS.md Precision goals). While it is red, 'L1 compute met' is not supportable by this cross-check.


## DIAGNOSED 2026-08-21 — it is TWO defects, and only one was in this bean

Probe: computations/qbeta/qbeta_trm_crosscheck_convention_pin_split_probe.py (4/4).
Deuteron |tr_M|, the atom all four methods cover, at the muon runtime pin:

  method       convention   pin      recorded q0
  Hoefsmit         D        muon         NO
  chi-cache        D        muon         yes
  markov_peel      C        muon         yes
  Habiro           C       PROTON        NO

Classified from RATIOS alone, no external reference needed:
  Hoefsmit vs chi-cache  3.22e-09   same convention, same pin
  peel     vs Habiro     1.821e-04  same convention, DIFFERENT pin
  Hoefsmit / peel        1.4810393  the C->D ratio

DEFECT 1 (this bean already had it): the C/D straddle, the 1.481 factor.

DEFECT 2 (NEW): a PIN straddle. Habiro matches convention C at the PROTON
pin to 2.71e-13 -- exact, not near -- inside a gate that raises SystemExit
unless the RUNTIME pin is muon. The runtime guard gives FALSE ASSURANCE:
refusing to start off-muon makes the run look pin-uniform while a committed
input sits at the other pin.

Why it survived: the guard checked ONE of its four inputs. Its own comment
said so ('the peel witness's recorded q0'). Habiro records no q0Value to
compare -- it is q0Anchor=ambiguous, a state the q0-anchor audit explicitly
tolerates -- and Hoefsmit records no anchor at all. 1966 of 2681 witnesses
(73%) carry no q0Anchor, so 'no recorded pin' is the normal case.

FIXED HERE: the guard now checks EVERY input that records a q0, and NAMES
the ones that do not instead of skipping them. Self-tested both directions
-- silent when correct, SystemExit on a planted proton q0 in chi-cache.

NOT a corpus-wide class: exactly ONE script in computations/ enforces a
runtime pin. Stated because the 73% invites the over-claim.

## Incidental: habiro-coefficients-extended exists TWICE

computations/ and computations/habiro/ -- identical payload and scriptHash,
DIFFERENT q0Anchor (ambiguous vs absent). The gate loads the top-level one
via _path_bridge.witness_path. My first probe used rglob, read the OTHER
copy, and reported the wrong anchor for its headline input until I caught
it. A diagnosis of a gate must read the gate's own files. Worth its own
bean.

## What remains, and to whom

  the PIN straddle    -> regenerate habiro-coefficients-extended under
                         QOU_Q0_ANCHOR=ideal and stamp its anchor
  the CONVENTION split -> the convention-D cascade

Neither is drained here. The gate is still red at 6/6 divergent, correctly:
this makes the reason legible, it does not make the number green.


## RETRACTED — my 2026-08-23 framing was wrong (never merged)

I appended a section here claiming this bean and `qou-dau6` were **competing
hypotheses with no adjudication between them**, and offered a **third**
candidate (import-cone drift). Both claims are false. This replaces it.

**Precision about "never reached main" — my first retraction said that, and
it is wrong.** The correction was made before #5514 merged, but the merge is
a REBASE, so the false commit `b9d0c5bfb9` replayed onto `main` and sits in
its history. No revision of this file on `main` asserts the false claim, and
the final state is clean — but the commit is there, and `git log -p` will
show it. Recorded because a retraction that misstates its own blast radius
is the same defect one level down.

### 1. The adjudication EXISTS, and predates my append by two days

`667c9ab3f6` on `main` (2026-08-21) — *"the tr_M cross-check is red for TWO
reasons; the guard saw one"*. I did not grep for it. That is the corpus-grep
checklist, skipped.

### 2. The two beans are BOTH RIGHT — the red has two simultaneous causes

Classified from ratios alone, no external reference value needed:

    method       convention   pin      recorded q0
    Hoefsmit         D        muon         NO
    chi-cache        D        muon         yes
    markov_peel      C        muon         yes
    Habiro           C       PROTON        NO

    Hoefsmit vs chi-cache  3.22e-09   same convention, same pin
    peel     vs Habiro     1.821e-04  same convention, DIFFERENT pin
    Hoefsmit / peel        1.4810393  the C->D ratio

So: a **C/D convention straddle** (this bean) AND a **muon/proton pin
mismatch** (`qou-dau6`). Not either/or. My "pick one" framing was the defect.

### 3. My third hypothesis is WITHDRAWN — it was cause (1) all along

I cited `hoefsmit_50dps` moving `0.388 -> 0.575` on a bare re-run as evidence
of import-cone drift, because AGENTS.md uses those exact digits as its
canonical import-cone example. Measured:

    0.575 / 0.388            = 1.48196
    C->D ratio (above)       = 1.4810393
    3-sig-fig band of inputs = [1.47876, 1.48516]   contains it

**The move IS the convention change.** I pattern-matched the digits instead
of dividing them, which took one line. Note the failure mode: the append was
correctly hedged as "HYPOTHESIS not a finding", and the reviewing agent
passed it on that hedge. **A well-labelled claim is not a true one**, and the
label is not a substitute for the check.

### What is actually open (from `667c9ab3f6`, which drained none of it)

The gate stays red at 6/6 **correctly** — that commit made the reason
legible, not the number green. Two independent fixes, neither done:

1. **Pin straddle** — regenerate `habiro-coefficients-extended` under
   `QOU_Q0_ANCHOR=ideal`. Blocked: see `qou-iayk`.
2. **C->D split** — belongs to the convention-D cascade (`qou-cds1`), not
   here.

`cross-check-trM-1ppb.witness.json` is deliberately NOT regenerated. Do not
"fix" this red by re-running and committing: until both causes are drained, a
re-run records the straddle rather than resolving it.

## Independently reproduced 2026-08-23 (prepare-merge, PR #5494)

Reproduced on the #5494 branch rebased onto main (eadcb02e08), container
sympy 1.14.0 / pyhecke_native 0.9.0. Regenerating cross_check_trM_1ppb
gives numbers matching this bean's table exactly:

  hoef_vs_peel   0.00018212626385904026 -> 0.324798555527689657
  hoefsmit_50dps 0.38828647155940888    -> 0.57517233101788385
  rel_delta_max  0.48130900224209445    -> 0.48103926609393223

--strict exits 1; 6/6 atoms diverge. Confirms inherited: PR #5494 touches
neither that producer nor its cone, and main's committed witness already
carries allPassed: false.

Same disposition as #5199 — regenerated witness NOT committed; reverted and
stated in the PR instead.

Correction to my own first reading: I initially attributed the move to the
sympy 1.12 -> 1.14 gap between this container and the witness's recorded
environment. The environment stamp does differ, but this bean's probe already
diagnosed the mechanism as the convention C/D straddle, and the numbers
landing on this bean's values to full precision says the straddle is the
cause, not the sympy bump. An environment difference was the easier
explanation, not the right one.
