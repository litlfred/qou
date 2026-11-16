---
# qou-3zby
title: cross-check-trM-1ppb committed witness is stale on main — C/D straddle across its four methods
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T13:23:15Z
updated_at: 2026-10-13T19:30:00Z
parent: qou-2002
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

## Live confirmation, 2026-08-23: the Hoefsmit leg has ALREADY moved C -> D

Ran the gate on `main` (df9e1f3a95) and diffed the fresh witness against the
committed one. **Regeneration reverted, not committed** — the gate is still red
and this bean's own instruction is that the witness stays as recorded until
both causes are drained.

    leg (deuteron)    committed        fresh run
    hoefsmit_50dps    0.38828647...    0.57517233...
    hoef_vs_chi       0.4813           1.482e-7      <- collapsed 7 orders
    hoef_vs_peel      1.8213e-4        0.3248        <- partner swapped

So the *"hoef_vs_chi collapsing 7 orders is the tell"* recorded above is not a
prediction any more — it is **live on main**, and the direction is now
explicit: the Hoefsmit leg's committed value sits on the **peel/C** side
(agreeing with peel to 1.82e-4), while today's producer puts it on the
**chi/D** side (agreeing with chi to 1.48e-7). The committed witness predates
that migration.

### Two measurements that constrain the diagnosis

- **peel_vs_habiro = 0.0001820930999, identical to 11.5 digits across all four
  atoms** (deuteron, He-3, He-4, tritium). A per-atom-varying quantity cannot
  do that; whatever produces it is a global scale.
- **hoef_vs_chi varies 6.91e-8 .. 2.46e-7, a 3.56x spread across atoms.** That
  one is *not* a global scale.

### 🛑 An unresolved collision — do not repeat my error

I first read that constant 1.82e-4 as the **muon/proton pin separation**, per
this bean's own table. But `cross_check_trM_1ppb.py`'s docstring explains the
same number as the **colour-weighting amount** `δ·h/4 ~ 1.8e-4`, citing
`docs/audits/2026-06-23-trM-crosscheck-colorweighting-split-at-C.md`, and its
`cw_pairs`/`colorblind_max` split groups the legs on that axis instead.

**These are different axes and my data does not distinguish them** — both
predict a constant. Anyone reasoning about the 1.82e-4 must resolve which it
is first. A discriminating test: the pin reading predicts the constant scales
with the muon/proton q₀ separation (11.5 ppb) and vanishes if both legs are
re-run at one pin; the colour-weighting reading predicts it is
q₀-independent and vanishes only if both legs use the same `pn_convention`.
Run one leg at the other pin and see whether 1.82e-4 moves.

### And a correction about what the gate tests

The gate does **not** verdict on `|Δ|max` (that column is display only). Its
only gating pair is `cw_pairs = {peel_vs_chi}`; Hoefsmit and Habiro are
already documented as informational, non-gating. So the red is
`peel_vs_chi` = 0.481 / 0.955 / 1.20 — an order-1 disagreement between the two
colour-weighted exact methods. That is a **convention** failure, not a
precision one, and closing it needs peel and chi on one convention
(`qou-cds2`, blocked on the Gram singularity under D). No amount of work on
this bean's other legs will make the gate green.

---

**Independently corroborated on PR #5519** (/prepare-merge, 2026-08-23,
base 6e16716558). Same inherited exit 1, reached from a different branch
and a different container: `cross_check_trM_1ppb.py --strict` reports
6 atoms compared, 0 certified at 1 ppQ, 6 divergent. `origin/main`'s
committed copy already records `allPassed: false`, and the regenerated
assertions are byte-identical to it -- only computedAt / commitSha /
durationMs moved. So the gate is red on main, not on either branch, and
the numbers have not drifted further since qou-3zby was opened.

**Second, separable point for whoever drains this** -- prepare-merge
§1·a runs this producer with `--strict` and then stages the witness.
That flag is recorded: `invocation.argv` gains `"--strict"` and
`invocation.reproduce` becomes
`python3 -u computations/cross_check_trM_1ppb.py --strict`, which is not
how the committed copy was produced. Following the loop verbatim
therefore commits a provenance change nobody intended, on a witness
whose substantive fields did not move. I reverted it here rather than
commit it. `precision-gates.sh` already treats `invocation` as ephemeral
and auto-reverts on that basis, so the two disagree about whether the
field is worth committing; worth reconciling when this bean is worked.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-23 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — independent corroboration from a CONSUMER (bean `qou-am5t` / `qou-46ab`)

Reached this bean from the other end while draining `qou-46ab`'s recorded-constant
class, which is worth recording because it is a second, independent route to the
same defect.

`computations/habiro/habiro_coefficients_atomic.py` cited
`cross-check-trM-1ppb.witness.json` as the source of its cross-check targets and
published two **convention-C** numbers as those targets. Checking the witness to
correct them established, directly:

- it contains **neither** C literal (`1.06530622861316`, `0.92323329718615`);
- it carries `markov_peel` and `chi_cache_canonical` =
  `1.1457597828869253187149279265985273678220205972661`;
- `q0Anchor: "muon"`, `q0Value: 1.10997859564273904668179512938000175270…`.

So the straddle this bean names has a live **consumer-side** consequence: a
producer was pointing readers at this witness for a verification target while
publishing C values, and the witness is on the ideal/CAL-2 muon layer while
production compute defaults to the proton pin.

Also surfaced: its `1.1457597828869253187…` is one of **three** D-frame proton
|tr_M| values in the corpus, in two families ~79 ppb apart (the dominant one is
`1.1457596924573008697…`, ~90 occurrences). The μ–p tension is ~11.6 ppb, so the
pin accounts for under a tenth of that gap — this witness being muon-pinned does
NOT explain the spread. Full table on `qou-46ab`.

Not actioned here — the consumer docstring is corrected and this bean's own
subject (the witness's staleness) is untouched.


## 2026-10-13 — the exact-method legs are GREEN: 6/6 certified at 1 ppQ (PR #7795)

Owner-authorised "owning deuteron tr_M" tranche. The red this bean tracks had
three live causes on 2026-10-13, none of them the C/D split recorded above
(that one was drained by the convention-D cascade):

1. **Word ordering.** The committed witness (2026-09-07) read `allPassed True`
   only because its peel and chi-cache legs were BOTH the grouped intra-nucleon
   word (deuteron 0.57517233159876), superseded by the 2026-09-05 ruling
   (`qou-hu1f`). When the peel witness was regenerated borromean (2026-09-13)
   and `canonical-tr-m-via-chi-cache-muon` was not, a fresh run went 6/6
   DIVERGE. The aggregate ratios are exactly R_quark: 1.8206 / 2.0789 /
   3.7848 / 7.8682 / 6.8907 / 14.3248.
2. **Bridge pin straddle.** `tr_m_wenzl_bridge_mpfr._load_y_lambda` keyed the
   muon layer on the retired pin-A prefix, so a live-muon caller got PROTON
   y_lambda (and the cache key had no q). Hoefsmit vs peel: 1.19e-8 at muon,
   exact at proton. Fixed.
3. **Env-suffix mismatch.** `QOU_Q0_ANCHOR=ideal` wrote/looked for `-ideal`
   chi caches while the committed ones are `-muon`; the consumer fell back to
   proton chi (T/3He/4He) or grouped symbolic caches (p/n/D). Normalised
   through `resolve_q0_anchor`; p/n/D muon caches added.

After: deuteron 0.1519683457609422 on Hoefsmit, peel and chi-cache; worst
exact-method |delta| 1.7e-50; 6 compared, 6 certified, 0 divergent.

**Still open here: the Habiro leg** (`habiro-coefficients-extended`) is still
the grouped word (0.5751723316 at D). It is informational, not gating, and its
regeneration is the `qou-iayk` item. Status left `todo` for that reason.


## Progress Update — 2026-11-16 (PR litlfred/qou#8176)

- **Lean 4 Formalization (`0` `sorry`, `0` vacuity audit hits/advisories)**:
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/MuonAnchorInversionAndStraddleClassification.lean` (wired into `QOU.lean`) proves:
    - `cal2MuonQ_roundtrip_and_excess`, `cal2MuonQ_secant_and_rel_shift`, and `cal2MuonQ_strict_three_value_ordering` (`qou-5op4`)
    - `crossAnchor_drift_magnification_and_inv_hbar_sq_secant` (`qou-72rd`)
    - `habiroSymbolicPayload_stamp_independent_and_secant` (`qou-mha1`)
    - `markovZD_over_markovZC_and_diff` and `fourMethod_straddle_cross_ratio_and_rel_delta` (`qou-3zby`, `qou-dau6`)
- **50-dps Verification Probe & Witness (`0` raw `float64` fields)**:
  - `computations/probes/muon_anchor_inversion_and_straddle_classification_probe.py` -> `computations/probes/muon-anchor-inversion-and-straddle-classification-probe.witness.json` (`allPassed: true`, 4/4 assertions, `scriptHash: 3b8c800c79a2`, `scriptCommitSha: 80719a03fb31a87a5718702e605db5cbed1f57ce`).
- **PR**: `litlfred/qou#8176` (`0e75c0ddb6a55fd2ce17a4041ac822379106c89c`).
