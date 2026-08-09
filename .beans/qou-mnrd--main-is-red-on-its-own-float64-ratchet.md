---
# qou-mnrd
title: 'origin/main is RED on its own raw-float64 ratchet — three witnesses landed undrained'
status: todo
type: task
priority: high
tags:
    - ci
    - precision
    - no-float64
    - ratchet
    - coordination
created_at: 2026-08-08T22:45:00Z
updated_at: 2026-08-09T01:20:00Z
---

## The finding

`computations/witness_raw_float64_audit.py --strict` **exits 1 on `origin/main`**
(9d6fa7f2c, 2026-08-08). Three witnesses carry raw float64 and are not in
`computations/raw-float64-baseline.json`:

     16  computations/qbeta/qborel-growth-budget-probe.witness.json
     15  computations/qbeta/cauchymul-order-cancellation-witness.witness.json
      4  computations/qbeta/c3-w2-c1-pole-divisor.witness.json

Landed by, respectively, `6cd4f9567` (plan+beans(W2)), `a62c65204`
(probe(qou-6e88)), `54c41e4cd` (compute+lean(qou-wgnx)) — three different
sibling sessions.

## How it was found, and why that matters

Surfaced by `/prepare-merge` on `claude/drain-float64-ratchet`: the ratchet was
0 NEW / 0 REGRESSED for the whole of that branch's work, and went to 3 NEW the
moment `origin/main` was merged in. Confirmed as inherited, not merge damage:

  * all three files exist on `origin/main` (`git cat-file -e origin/main:<f>`);
  * `raw-float64-baseline.json` is byte-identical between `origin/main` and the
    merged branch, so the merge did not weaken the baseline;
  * none of the three appears in that baseline.

So `main` fails its own gate. **This is exactly the leak the ratchet exists to
stop** — see the audit's own motivating example, `jpsi-boundstate-mass.witness.json`
reaching `main` with 30 raw float64 fields while the padding audit stayed green.
The ratchet caught it this time; nothing enforced the catch.

## Do not fix it the easy way

The audit says so in its own output: *"fix AT THE PRODUCER (carry mpmath.mpf
from the source, serialize with `_precision.fmt`), then re-run it. Do NOT add
the file to the baseline to silence this."* Adding three lines to the baseline
would close the bean and defeat the mechanism.

## What to do

1. Fix each at its producer. `jpsi_boundstate_mass_probe.py` is the worked
   conversion the audit points to, including the case where a library has its
   own precision ceiling that must be recorded rather than assumed.
2. Separately: **why did these land?** The ratchet is a script, not a required
   check. If it is not wired into CI as blocking, three more will land next
   week. That wiring is the durable fix and is the more important half of this
   bean.

## Not claimed here

This branch does not fix them. They are other sessions' witnesses and draining
them is their arc's work, not this one's. Recorded so that
`claude/drain-float64-ratchet` is not read as having regressed the gate it is
named after — it did not; it inherited a red main.

## CORRECTION — the ratchet IS wired into CI, and strictly. 2026-08-09

The bean's item 2 asks "why did these land? ... If it is not wired into CI as
blocking, three more will land next week." **The premise is wrong.**
`.github/workflows/witness-staleness.yml` has run
`witness_raw_float64_audit.py --self-test` + `--strict` as a real blocking step
since the pipefail fix; six sibling precision gates sit beside it, all strict.
It is wired, and correctly.

What is missing is a **trigger**:

    on:
      # CI auto-triggers disabled (owner directive 2026-06-30): Actions billing.
      workflow_dispatch: {}

No push, no pull_request. The workflow has not run on a push since 2026-06-30.
That is the whole explanation for three witnesses from three sessions landing
undrained, and it explains why nothing caught them at any point in between.

**This is not an agent decision to reverse.** Re-enabling the trigger spends the
owner's Actions budget against an explicit directive. Flagged for the owner as a
decision, not fixed unilaterally; the durable fix available to agents is
elsewhere.

## What was actually done, and where the enforcement now lives

`scripts/precision-gates.sh` — one runner for the whole NO-FLOAT64 family, in
the same order as the workflow: q0-anchor flip, `mpf(<float>)` source,
float64-padding ratchet, `mp.dps` no-op, module-const precision, raw-float64
ratchet, q0-value drift, plus the no-free-parameter certificate as ADVISORY
(red by design on `A_omega = 3`, exactly as the workflow declares).

  * exits 1 on any blocking red, and does NOT stop at the first failure -- a
    preflight that hides four reds behind one is worse than none;
  * `--changed` short-circuits to a no-op unless the change touches a witness
    or a `computations/` script, so it is cheap enough to be a commit-time rule;
  * reports witnesses the RUN ITSELF dirtied separately from ones the agent
    dirtied -- those are audits whose committed output is stale, a different
    finding from a failing gate.

Wired at the two choke points agents actually pass through:

    AGENTS.md  §"QA is agent-owned; CI is a backup"  -> before every commit
    .claude/commands/prepare-merge.md  step 4b       -> BLOCKING, before push

and cross-referenced from the workflow header, with an explicit instruction to
keep the workflow's step list and the script's `GATES` array in sync.

## Two findings the bean did not have

**1. A SECOND gate was red, and it was this arc's own defect.**
`module_const_precision_audit.py --strict` exited 1 on
`computations/probes/one_loop_c_sigma_tetrahedral_probe.py:110`:

    VOL_41 = mpf("2.0298832128193072500424051085486440883603983786944…")

built at module scope, above `set_compute_dps()` in `main()`. mpmath was still
at its default 15 dps when the literal was parsed, so the 60 digits were
truncated to 53 bits at construction and no later dps setting can recover them.
Fixed by calling the idempotent `set_compute_dps()` at module scope above the
constant. LOSSY 1 -> 0. The probe still passes 4/4 and no assertion value moved
(the constant reaches the hot loop through `float()`), so this was latent rather
than active -- which is exactly the kind of defect a static gate exists for.

Worth naming: this landed in `e33b84aef`, on this same arc, in the window when
the trigger was off. The three qbeta witnesses were not an unlucky sibling; the
gap catches everyone including the session that opened the bean about it.

**2. Two committed audit witnesses are STALE, one substantively.**
Running the family regenerates them:

    computations/audits/q0-anchor-consistency-audit.witness.json
        Q0_ANCHOR_MISSING 1787 -> 1814   (27 newer witnesses carry no anchor;
        NOT a failure -- a witness gains its anchor when next produced via
        WitnessBuilder -- but the committed count was wrong)

    computations/q0-value-drift-audit.witness.json
        proton-pin 581 -> 582, canonical 697 -> 696
        computations/audits/braid-encoding-audit.witness.json parameters.q_0
        moved 1.1099785955573347 -> 1.1099785827513808, i.e. canonical -> the
        proton pin, 11.5 ppb apart.

The reclassification is a sibling re-running that audit without
`QOU_Q0_ANCHOR=ideal`. Per AGENTS.md §q₀ anchor convention proton-pinned values
are the documented physical-observations layer and NOT drift, so the gate is
green either way -- but the value in a committed witness moved by 11.5 ppb and
nothing recorded it. Both regenerated here so the committed record is accurate;
the braid-encoding witness itself is that arc's to decide on, and is not touched.

## Still not claimed

The three qbeta witnesses are NOT drained. They are other sessions' arcs, the
bean said so at the outset, and adding them to the baseline remains the one
move that is explicitly forbidden. `raw-float64 ratchet` is still RED on this
branch and on `main`, and `/prepare-merge` step 4b now tells agents to say so in
the PR rather than silence it.

## OWNER DECISION, 2026-08-09: leave the workflow dispatch-only

Asked directly, with the failure cost on the table (three witnesses reached
`main` in the trigger-off window) and three options offered: leave it
dispatch-only, add a path-filtered `pull_request` trigger scoped to
`computations/**` + `**/*.witness.json`, or restore full push+PR triggers.

**Decision: leave it dispatch-only.** The 2026-06-30 Actions-billing directive
stands, now reaffirmed with the cost known rather than by default.

So `scripts/precision-gates.sh` is not a stopgap until CI comes back — it IS the
gate. Treat a skipped run the way you would treat a skipped CI check. Do not
propose re-enabling the trigger again without a new reason; this was asked and
answered.

## Bean stays OPEN — the title condition is still true

`origin/main` is still RED on its own raw-float64 ratchet. The bean's item 2
(the durable wiring) is done and the owner decision behind it is recorded; item
1 is not, and was never this branch's to do:

     16  computations/qbeta/qborel-growth-budget-probe.witness.json        6cd4f9567
     15  computations/qbeta/cauchymul-order-cancellation-witness.witness.json  a62c65204
      4  computations/qbeta/c3-w2-c1-pole-divisor.witness.json             54c41e4cd

Whoever picks this up: fix each at its producer (carry `mpmath.mpf` from source,
serialize with `_precision.fmt`; `jpsi_boundstate_mass_probe.py` is the worked
conversion), re-run the producer, and re-run `scripts/precision-gates.sh`.
Adding any of the three to `raw-float64-baseline.json` closes the bean and
defeats the mechanism — the audit says so in its own output.

## First real use of the gate found a defect in the gate. 2026-08-09

`precision-gates.sh`'s "stale committed audit witnesses" reporter compared
`git status` before and after the run and attributed every difference to the
run. On its first outing it flagged a `.beans/*.md` file that was being appended
to in another shell while the gates were running. Fixed: the diff is now
filtered to `computations/**/*.witness.json`, which is the only thing the audits
can write. A reporter that cries wolf on unrelated edits is one agents learn to
skip, which is the failure mode this whole bean is about.

---

## 2026-08-09 — the scope grew: 3 → 18 NEW + 2 REGRESSED

Re-measured after integrating `origin/main` (498 commits) into
`claude/drain-float64-ratchet` for PR #4729:

    NEW dirty witnesses : 18   (was 3)
    REGRESSED           : 2    (was 0)

**15 of the new entries and both regressions arrived with main's 498
commits.** The original three (the qbeta trio below) are unchanged.

    835  computations/probes/nastokes-multigen-cluster-additivity.witness.json
    126  computations/deltalambda/threerow-qcross-trend.witness.json
     98  computations/probes/nastokes-orbit-symmetric-readout.witness.json
     91  computations/alpha/alpha-k-jones-markov-h12.witness.json
     82  computations/deltalambda/threerow-crossing-a-dependence.witness.json
     73  computations/deltalambda/threerow-4he-completion.witness.json
     52  computations/probes/nastokes-germ-gauge-covariance.witness.json
     25  computations/probes/canonical-ordering-dof.witness.json
     20  computations/atomic-tr-m-mpfr-50dps-proton.witness.json
     16  computations/probes/nastokes-transverse-curvature-seifert.witness.json
     16  computations/qbeta/qborel-growth-budget-probe.witness.json          <- original
     15  computations/deltalambda/threerow-sign-crossing.witness.json
     15  computations/qbeta/cauchymul-order-cancellation-witness.witness.json <- original
      6  computations/markov-z-fibre-rank-bar-covariance.witness.json
      5  computations/crossing-energy-channel-basis.witness.json
      5  computations/volume-binding-four-point.witness.json
      4  computations/qbeta/c3-w2-c1-pole-divisor.witness.json               <- original
      1  computations/ground-state-ordering-argmin-sweep.witness.json

    REGRESSED:
      1 -> 78    computations/chi-helium-4-h12-at-q0-50dps.witness.json
     36 -> 52    computations/probes/keystone-colored-sigma235-wrt.witness.json

Clusters, which is a hint about the producers rather than the witnesses:
`nastokes-*` (4 files, 1001 fields), `deltalambda/threerow-*` (4, 296),
`alpha/*` (1, 91). Those look like three arcs each writing float64 through a
shared helper, not eighteen independent mistakes.

### Why this matters for PR #4729

That PR's stated purpose is that the ratchet exits 0. It did, against the main
of 2026-08-08. It does not against the main of 2026-08-09. **The PR is
otherwise ready** — merges clean (origin/main is an ancestor), all its own
gates pass, its drains verified — but its headline claim is now false, through
no change of its own.

The ratchet is a moving target: main accrues float64 debt faster than a single
PR closes it. Whatever is decided for #4729, that is the structural problem,
and a per-PR drain will not fix it. The guard installed by #4729
(`QOU_WITNESS_STRICT_FLOAT64=warn` by default, at `WitnessBuilder.save`) is the
mechanism that would — but only once its default is `raise`, which #4729
deliberately did not do because ~1580 baseline witnesses would break their
producers on re-run.

**Not done here, and deliberately:** nothing baselined, no `--rebaseline`, no
number hand-edited. The two ratchet audit witnesses were regenerated and
committed because their COUNTS moved (staleness, not drift), per the gate's own
instruction.
