---
# qou-y98b
title: 'Gate the q0Anchor refill: ~50% of newly-added witnesses land unstamped'
status: in-progress
type: task
priority: normal
created_at: 2026-08-28T15:24:07Z
updated_at: 2026-09-03T09:06:25Z
---

Claimed by branch `claude/q0-anchor-refill-gate-2026-08-28`, PR #5891.

## The refill is measured on ARRIVALS, not on the standing count

Standing counts move for two reasons at once (drains and arrivals), which is
why two endpoint readings mislead. Measured instead on witness files *added*
between two revs, reading blobs out of git:

    ADDED origin/main~500..HEAD   n=101   unstamped=60  (59.4%)
    ADDED origin/main~250..HEAD   n= 44   unstamped=20  (45.5%)
    ADDED origin/main~100..HEAD   n= 31   unstamped=16  (51.6%)

**~50% of every newly-added witness lands with no q0Anchor.** The stamped half
is essentially all `proton`. Confirms qou-kx04's "growing faster than it is
being drained" with a rate rather than two counts.

Standing population, read from git at eight revisions (census excludes nothing;
raw `computations/**`):

    2026-08-10 ~3000   2887 total  2240 MISSING  77.6%
    2026-08-19 ~1500   2998        2277          76.0%
    2026-08-24 ~1000   3055        2223          72.8%
    2026-08-25  ~500   3069        2015          65.7%   <- a drain landed
    2026-08-27  HEAD   3170        2066          65.2%   <- +51 in two days

## Two numbers, both real

    raw computations/**              2066
    audit scope (live)               1678

The audit skips `_deprecated` (line 280) and `AUDIT_SUFFIXES`. The 388 gap is
bookkeeping scope, not stamping. Quote which one you mean.

## Cause partition (new: computations/audits/q0_anchor_missing_cause_partition.py)

    UNDECLARED        1199   71.5%
    NOT_BUILDER        365   21.8%
    NO_PRODUCER         55    3.3%
    DECLARED_STALE      59    3.5%
    GENERATED_MIRROR     0    0.0%

**Using WitnessBuilder is NOT sufficient to get stamped.** `build()` writes
`q0Anchor` only when the pin is POSITIVELY DECLARED — a manifest entry or
`QOU_Q0_ANCHOR`. Undeclared producers are left unstamped on purpose (defaulting
one in would assert a pin nobody established). The manifest lists 410 stems
against ~2800 producers, so absence is the common case, and 71.5% of the
missing population is exactly that gap.

`UNDECLARED` spans **1154 distinct producers** — a long tail, top producer
contributing 5. A per-producer drain is the wrong shape of fix.

## Why nothing blocks it

`q0_anchor_consistency_audit.py` IS wired into `precision-gates.sh:61` and
`witness-staleness.yml:76`, both `--strict`. But line 328 is
`if args.strict and n_flip:` — Q0_FLIP only, and Q0_FLIP is 0. The audit's own
header calls Q0_ANCHOR_MISSING "pre-backfill; not a failure". Correct for a
CONTRADICTION detector; it just means the inflow is ungated.


## OUTCOME — gate built, validated, wired (PR #5891)

`computations/audits/q0_anchor_ratchet.py` + `computations/q0-anchor-missing-baseline.json`,
wired into `scripts/precision-gates.sh` as BLOCKING with a self-test.

Follows the repo's own idiom (witness_raw_float64_audit + raw-float64-baseline):
the 1678 existing unstamped witnesses are baselined and tolerated; an unstamped
witness NOT in the baseline fails --strict; the baseline drains, never grows.

Blocking is safe here — green at its own baseline, so it can only fire on a NEW
regression. It never writes or guesses an anchor: WitnessBuilder's principle that
an undeclared producer stays unstamped is untouched.

### Validated, not asserted

- historical replay: baseline at ~500, run at HEAD -> RED with **exactly 60**,
  matching the independent added-file measurement (two methods, same number)
- --rebaseline REFUSES to grow 1627 -> 1678, file byte-unchanged; accepts a drain
- fixture test of default path resolution: backlog tolerated / new caught /
  stamped ignored / audit-emitted out of scope
- `--self-test` mutation-tested: two blinding mutants (scan dropping every hit,
  _is_in_scope excluding all witnesses) are both KILLED. A self-test that cannot
  fail is theatre.
- flag is `--self-test`, the spelling precision-gates.sh line 467 actually
  invokes. An unknown flag would make the self-test error, and the harness prints
  the same gate name either way — a gate that never ran reads exactly like a gate
  that passed.

### Corrected numbers (rev-pinned; supersede the working-tree figures above)

At cdbdc84af1, all read from git:

    UNSTAMPED          1678
    UNDECLARED         1193  71.1%
    NOT_BUILDER         356  21.2%
    DECLARED_STALE       65   3.9%
    NO_PRODUCER          55   3.3%
    INERT_DECLARATION     9   0.5%   <- NEW class

**Why the earlier figures were wrong, and it matters beyond this bean.** They
were computed against the working tree, which a concurrent agent switched to its
own branch mid-session — moving the manifest from 410 declared stems to 728
between two of my reads. Everything now reads from git at a named rev. In a
repo worked by several agents against one checkout, a working-tree measurement
is not reproducible even by its own author.

### INERT_DECLARATION — a manifest entry that cannot fire

`build()` reads the manifest, so a declaration on a producer that hand-rolls
`json.dump` never executes. Worked case found while validating:
`signed-crossing-feasibility` oscillates muon -> missing -> muon -> missing.
It was dropped by `5baf5a45c3`, whose subject is *"register the producer's real
pin"* and which DID add the stem under `physical_proton`. The producer ends in
`out.write_text(json.dumps(w, indent=2))`. The declaration reads as done and
does nothing.

### One deliberate escape hatch, named rather than hidden

Growth is permitted ONLY via `--establish "<reason>"`, which records the reason
and the added entries INTO the baseline for review. It exists because main moves
while this PR is open and those arrivals are not this branch's doing — without
it the gate blocks its own landing and the way through would be to delete the
baseline file so `prev` is empty. That hatch exists either way; this makes it
visible. It must never absorb a witness the branch itself created.

### NOT closed by this bean

The 1678 backlog. The gate stops the inflow; draining is separate work, and the
partition says how to scope it: UNDECLARED (1193) is a manifest+builder problem
over 1149 producers, NOT_BUILDER (356) needs producer migration, NO_PRODUCER (55)
are orphans needing a producer or a deletion.


## 2026-09-03 — continuing on claude/q0-refill-147-2026-09-03, PR #6454

PR #5891 (this bean's original claim) is MERGED; the gate is live and it is now
firing. Its own cause partition said the drain was 'a manifest+builder problem
over 1149 producers' and left it open. This is the first tranche of that drain,
scoped to what the gate actually reports.

**The 150 the ratchet calls NEW is two things, and neither is quiet debt.**
  * The baseline records generated_from_rev origin/main 03f57c2b75 (2026-08-28)
    but was committed into a tree from 08-30/09-01. Measured: 114 of the 150
    already existed on main at the commit that last touched the baseline, and
    0 of the 150 existed at 03f57c2b75. Stale on arrival.
  * Add-commit dates: 73 on 08-30, 48 on 08-31, 15/7/1 on 09-01..03. Almost all
    t7qv / M1 / milnor. Live output, still arriving — consistent with this
    bean's own ~50%-of-arrivals rate.

**Triage of the 150** (cone trace for q0 reads + WitnessBuilder check):
  115  UNDECLARED, reads q0, no muon signal  -> declared physical_proton (#6454)
   22  NOT_BUILDER (hand-rolled)             -> producer-side, M1 arc's own
   10  no q0 signal at all                   -> want 'independent' + reason
    1  muon_pin_A_residual_surface_audit     -> (E1) comparison, needs q0Values
    2  NO_PRODUCER (bnn/bpp-higher-a-resumable)

The manifest declaration cannot move a number: q_parameter keys on ideal_muon
alone (substrate/q_parameter.py:108), so these stems already resolved to proton.
The entry only makes the declaration positive so build()'s require_declared
passes. Verified both directions.

**Correction to my own first pass.** I reported 24 witnesses as having no
producer. 22 of them do — the resolver keyed on scriptFile and on a
witness-stem->script-stem guess, and the M1 cluster names its producer after the
epic (m1-area-symmetry.witness.json <- wlambda_covariance_epic_M1_area_symmetry.py).
All 22 are hand-rolled, so the exclusion stands; only the reason was wrong.
Any witness->producer tool keyed on stem is blind to the whole
wlambda_covariance_epic_* family.

**Detector blindness, measured, not fixed.** _Q0_FIELDS is a four-name allowlist
('q_0_50dps','q0','q_0','q0_50dps'). Of the 150, 29 record a prefix-matching q0
value somewhere and 14 record it ONLY under a key the allowlist does not know
(q, q0_value, q0Value, q0_muon_pin, q0_proton_pin, q0_current, z, z_1,
q_core_window, abs_mu_sym). Payload evidence outranks the manifest in
resolve_q0_anchor_payload_first, so those are witnesses that PROVE their own pin
and the resolver cannot read it.

**Environment hazard (qou-x5mi) probed, not assumed.** Three of the smallest
declared producers re-run and diff byte-identical to HEAD modulo provenance —
only +q0Anchor/+q0Value. A bounded 93-producer sweep is running to establish
how far that generalises; anything that moves a number is reverted, not landed.


## 2026-09-03 — PR #6454 MERGED (593bda46cb, rebase-merge, 5 commits linear)

Landed: 115 manifest declarations under physical_proton (728 -> 843) + 85
witnesses stamped by re-running their producers. Re-verified on the merge head:

              origin/main   branch
  unstamped      1748        1663    (-85)
  NEW refill      153          68    (-85)

Both still red; the gate was red before and is 85 less red now. Baseline file
untouched — nothing widened.

**Sweep result over the 93 build()-path producers:**
  83  stamp-only (payload byte-identical modulo provenance) -> landed
   4  'moved' -> diagnosed, see below
   5  timeout at the 150 s cap
   1  crash (mu4_magnitude_gap_anatomy_probe: KeyError 'inputs')
   6  wrote no witness at all
   0  sprayed a sibling witness (measured, not assumed)

**The 4 movers were four different things, not four instances of one hazard:**

 1. phase_b_lr_branching_constraint_probe — NOT a mover. MY volatility mask was
    incomplete: the whole diff was `build_s`, that producer's own spelling of a
    wall-clock timing. Landed. Lesson: the mask cannot be a fixed list.
 2. operator_selection_active_set_probe — a genuine STALE CONSUMER, and the
    re-run is the fix. Its section 2 reads nucleus-real-sdp-*.witness.json and
    republishes their duals. It had the deuteron at active_blocks
    [(2,1,1,1,1),(2,2,2),(3,3)] / y0_star -0.014433988; the live upstream (and
    the re-run) give [(4,2),(5,1),(6,)] / y0_star +0.06426714876225478.
    Upstream was regenerated by 393fec6bfa, whose message claims "full

propagation" — it did not reach this consumer, and nothing detected it because
    a stale consumer is self-consistent and its assertions still pass (5/5
    before and after). y0_star is the LP net-constraint shadow price and it
    SIGN-FLIPS. Bounded: checked the other 4 consumers of nucleus-real-sdp-*,
    none republishes the deuteron duals, so the gap was this one file.
 3. muon_pin_migration_stage1_inventory — inventories the migration, so it
    tracks corpus state by design. Not landed, not a defect.
 4. four_body_term_and_the_h12_collapse — RESOLVED 2026-09-03, and it is NOT a
    mover either. Re-run under a widened mask, the entire diff is a build time:

        data/h12_blocks/build_seconds   '0.04' -> '0.05'
        assertions[1]/source            "... built 0.04s; ..." -> "... built 0.05s; ..."

    Note the second line. The same timing is FORMATTED INTO AN ASSERTION'S
    `source` STRING, so no field-name mask can ever reach it — a witness that
    prints a duration into human-readable prose is non-reproducible by
    construction, and a re-run comparison will call it MOVED forever. That is a
    detector-blindness entry in its own right, and a producer-side defect worth
    fixing (drop the timing from the assertion source; keep it in its own field).

**CONCLUSION: the qou-x5mi environment hazard did not appear ONCE in a
93-producer sweep.** All four apparent movers are accounted for — two are
timings my mask missed, one is a real upstream staleness the sweep usefully
surfaced, one is an inventory that tracks corpus state by design. Zero are
mpmath-version drift. This does not refute qou-x5mi (that bean measured four
producers that genuinely moved, by a different method and on a different set);
it bounds it: on this population the rate is 0/87 completed, so a producer-side
declaration is far cheaper than that bean's framing implies. Scope-(a): this is
about these 93 producers, not about all producers.

**Not done, and whose:** the 22 hand-rolled M1 producers (wlambda_covariance_epic_*)
need a one-line producer-side save({"q0Anchor": ...}) each — the M1 arc's own;
the 10 with no q0 signal want "independent" + a reason, which needs a deeper
cone trace than the file-local grep that classified them; 1 comparison audit
(muon_pin_A_residual_surface_audit) needs q0Values; 2 orphans
(bnn/bpp-higher-a-resumable) have no producer at all.


### CORRECTION to item 4 above, same day — "a producer-side defect worth fixing" is WRONG

I wrote that formatting `build_s` into an assertion's `source` string is a
producer-side defect. Read at the producer, it is not:

    ok = max(D12) == 297 and abs(norm - 1) < 1e-12 and build_s < 60
    assertions.append(("A2_h12_is_seven_small_blocks", ok,
                       f"7 blocks, max dim {max(D12)}, sum y.dim={norm:.12f}, "
                       f"built {build_s:.2f}s; reach by A: {reach}"))

The assertion's own predicate includes `build_s < 60` — the build staying under
a minute IS part of what this assertion claims, so the measured time IS the
evidence for it, and printing it in `source` is correct. Likewise
`data/h12_blocks/build_seconds` is legitimate telemetry.

**The defect is in the COMPARISON, not the producer.** A re-run diff that keys
volatility on field NAMES cannot reach a value formatted into prose, so it will
report this witness MOVED forever. The fix is to normalise timing-shaped
substrings (`\b\d+\.\d+\s*s\b` -> `<T>`) in the comparison, which is what the
second sweep does. Proposing a producer edit here would have been me widening
scope into a live arc to fix something that is not broken.

Same shape as the `build_s` mask gap two items up, one level deeper: the first
was a field name I had not listed, this is a value with no field name at all.
