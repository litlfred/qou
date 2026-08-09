---
# qou-mnrd
title: 'main is RED on its own raw-float64 ratchet — 18 NEW + 2 REGRESSED (was 3 when opened)'
status: in-progress
type: task
priority: high
tags:
    - ci
    - precision
    - no-float64
    - ratchet
    - coordination
created_at: 2026-08-08T22:45:00Z
updated_at: 2026-08-09T17:00:00Z
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

### Triage: the 18 split by CATEGORY, and my "shared helper" guess was wrong

I wrote above that the clustering "looks like three arcs each writing float64
through a shared helper, not eighteen independent mistakes". That is not what
is there. Checked the producers instead of guessing:

    cluster                 files  fields   numpy?  category
    nastokes-*                4     1001     YES    (3) float64 upstream
    alpha/*                   1       91     YES    (3) float64 upstream
    deltalambda/threerow-*    4      296     no     (2) mpmath, downcast
    the rest (incl. qbeta)    9       97      —     mixed, small

using PR #4729's own taxonomy. The clusters are real but they are NOT one
shared helper — they are two different failure modes:

**`nastokes-*` and `alpha/*` (1092 fields, 5 producers) are numpy.**
`nastokes_multigen_cluster_additivity_probe.py:522` is
`trace=float(np.trace(Om))` — the linear algebra itself is float64. Draining
these is a genuine port (category 3 in #4729's terms: "mpmath adaptive
quadrature, gram_matrix_mp/tr_m_mp/hm_mp, clarabel-MPFR"), not a sink fix. The
835-field witness is one probe emitting `omega`/`trace`/`R2`/`R3` per germ per
shape per species — the count is large because the loop is wide, not because
the fix is.

**`deltalambda/threerow-*` (296 fields, 4 producers) is mpmath downcast.**
No numpy at all; ~20 `float(` calls each. But it is NOT pure sink coercion —
`threerow_qcross_trend_probe.py` downcasts mid-stream and decides on the
result:

    249:  "q_cross": float(a) * float(b),
    250:  "on_real_level_branch": bool(float(a) ** 2 < float(Q_STAR)),
    275:  a, b = float(a), float(b)

Line 250 is a VERDICT decided in float64, and 275 downcasts before further
use. So the fix is the same discipline #4729 already applied to the em-linking
producers — `mp.nstr` at the sink with the `mpf` kept alive wherever a value is
also compared or ordered — but it has to reach into the computation, not only
the serialisation.

### What this does to the cost of "drain main's debt first"

Not 1485 undifferentiated fields. Roughly:

  * 296 fields / 4 producers — same shape as the em-linking drains this PR
    already did, and #4729 has the pattern;
  * 1092 fields / 5 producers — numpy ports, the expensive kind;
  * ~97 fields / 9 producers — small and various, including the qbeta trio.

The cheap half is a fifth of the fields and would take the ratchet from 18 NEW
to 14 NEW — which does not make it green, so it does not on its own change the
decision on #4729.

---

## 2026-08-09 — #4729 is MERGED; this bean is now the live item

PR #4729 merged as `25387e2a4` with its title and body rewritten to say the
ratchet is red, rather than the "goes green" claim it was opened with. So the
one thing that was holding the honest statement out of `main` is gone: **`main`
now carries the guard, the 15 drains, and an accurate account of what is still
dirty.**

Re-measured on `main` at `25387e2a4`:

    NEW dirty witnesses : 18   (1,556 fields)
    REGRESSED           : 2
    drained since baseline : 6 file(s), -1,483 field(s)
    exit code           : 1

Unchanged from the pre-merge measurement, as expected — #4729 drained its own
15 and none of the 18 is one of them. The `drained (progress)` line is #4729's
work showing up against the baseline:

    38 -> 0    computations/inverse-markov-qvalues.witness.json
    30 -> 0    computations/jpsi-boundstate-mass.witness.json
    73 -> 61   computations/multi-layer-gap-decomposition.witness.json
    28 -> 21   computations/markov-free-energy-qvalues.witness.json
    11 ->  4   computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json
    37 -> 36   computations/binding-canonical.witness.json

## CLAIMED — the `deltalambda/threerow-*` cluster

Working the cheap half (category 2, mpmath downcast): 4 producers, 296 fields.

    126  computations/deltalambda/threerow-qcross-trend.witness.json
     82  computations/deltalambda/threerow-crossing-a-dependence.witness.json
     73  computations/deltalambda/threerow-4he-completion.witness.json
     15  computations/deltalambda/threerow-sign-crossing.witness.json

Branch: `claude/drain-deltalambda-threerow`, cut fresh from `main` at
`25387e2a4` (#4729's branch is merged and must not be built on).

**Not** claimed by this session: the `nastokes-*` + `alpha/*` numpy ports
(1092 fields, 5 producers) and the residual 9 small ones including the qbeta
trio. Those stay open for whoever takes them; do not assume this branch covers
them.

Expected outcome, stated up front so it can be checked rather than claimed:
this takes 18 NEW -> 14 NEW. **It does not make the ratchet green.**

---

## CORRECTION — the `deltalambda/threerow-*` cluster is not what I said it was

Above I claimed the four `threerow-*` witnesses were "the cheap half ... mpmath
downcast ... no numpy at all ... same shape as the em-linking drains this PR
already did". **Wrong on the diagnosis, and it hid a worse problem.** Checked by
reading the producers and running them, not by grepping for `numpy`:

**1. The f64 IS upstream, through a shared helper.** All four route χ^λ through
one of two helpers (`threerow_sign_crossing_probe.chi_atom`,
`threerow_chi_sparse.chi_atom_sparse`), and both call
`hecke_characters.build_seminormal_matrices`, which does `q_local = float(q)`
and returns numpy/scipy arrays. Each braid letter is then
`float(c)·σ + float(d)·I`. So χ is f64 END TO END, whatever precision `q`
carries in. Only 1 of the 4 files imports numpy itself — which is why a grep
for numpy said "no" and the grep was measuring the wrong thing.

**2. But the cluster is MIXED, not uniformly category 3.** Each witness carries
two kinds of block:

  * character-free (`G(q) = Σ y_λ(q)·Δ_λ`, `S_free`, the level ladder, the q
    grids) — genuine 50-dps mpmath, `float()`-ed only at the sink. float64 was
    discarding ~34 real digits.
  * character-dressed (`F_K = Σ y_λ·χ^λ·Δ_λ` and everything derived from it) —
    f64-limited by χ.

So the drain is per-FIELD, not per-file, and both categories appear in every
one of the four witnesses.

## The thing that actually mattered: NONE of the four producers would run

Not "carries float64" — **could not regenerate its own witness at all**, on
`main`, today:

    threerow_sign_crossing_probe.py         TypeError from reject_float64_q
    threerow_crossing_a_dependence_probe.py TypeError from reject_float64_q
    threerow_qcross_trend_probe.py          ModuleNotFoundError: scipy, then the same
    threerow_4he_completion_probe.py        ModuleNotFoundError: scipy, then the same

`reject_float64_q` landed in `efcaf79ed` (2026-08-08T19:29Z, "NO FLOAT64: the
braid word was f64 at source"). It rejects any mpf equal to its own float64 —
which includes the grid endpoint `q_lo = mpf("1.0001")`. Every one of these
probes sweeps a grid that starts there, so every one of them dies on its first
evaluation.

The guard is RIGHT and is not the defect: a 50-dps pipeline must not be
silently capped at 17 digits. Its own docstring prescribes the answer —
"`allow_float64=True` is the escape for paths that are legitimately f64 ...  so
the loss is declared at the call site instead of hidden" — and these probes are
exactly that case, already saying so in prose in their PRECISION notes and
witness caveats. What was missing was the machine-readable declaration. Added at
the two χ helpers.

**The frozen witnesses were CORRECT, just unreproducible.** After the
declaration, `threerow-sign-crossing` regenerated with all 51 data leaves
byte-identical. So this was not silent numeric drift; it was a producer that had
stopped being runnable and nothing noticing for a day.

### Why nothing noticed

Same root as the rest of this bean. `witness-staleness.yml` is dispatch-only by
owner decision, so no push has re-run these producers since 2026-06-30. A guard
that breaks four producers is exactly what a push-triggered run catches on the
next commit. This is the second concrete cost of the trigger-off window recorded
in this bean (the first was the three qbeta witnesses); it is recorded as cost,
not as an argument to re-open a decision that was asked and answered.

### The blast radius is wider than these four

`atom_braid_word_3A(..., q=...)` has 8 call sites across 6 files. Confirmed
also broken by the same guard, and NOT fixed here:

    computations/probes/gram_qtrace_hutchinson_probe.py

Not established either way (both exceeded a 4-minute probe budget before
reaching a verdict): `gram_norm_binding_probe.py`,
`gram_transfer_quadratic.py`, `threerow_isospin_parity_probe.py`. Whoever picks
those up: the fix is only `allow_float64=True` IF that call site's path really is
f64 — check it, do not copy the annotation across on faith.

## A gap in `str_at_true_precision`, found by diffing my own output

The obvious drain is `float(x)` -> `str_at_true_precision(x)`, and it is WRONG
here in the expensive direction. That helper's test is representational and
exact — "is this mpf equal to its own float64?" — which is right for a pure f64
kernel output. But `F = Σ y_λ(q)·χ^λ(β;q)·Δ_λ` MIXES a 50-dps mpmath weight with
an f64 character, so the product is not a 53-bit dyadic, the helper keeps all 50
digits, and ~34 of them are dyadic tail the χ kernel never supplied:

    was (raw float64) : -0.1949663511459454
    str_at_true_prec  : -0.19496635114594539089654509922868564866657011668554
    correct           : -0.19496635114594539

That middle line reads as measured and is WORSE than the float64 it replaced —
a drain that makes the ratchet green while degrading the witness. Caught only by
diffing every leaf against the pre-drain copy, which is now the routine for the
rest of this cluster.

Handled with a local `fmt_f64_limited` (= `fmt(x, 17)`) applied to whatever
passes through the χ kernel, `str_at_true_precision` to everything else. NOTE
the distinction it does not resolve: 17 digits is the f64 REPRESENTATION width,
while the ACCURACY of this χ path is the ~1.5e-6 the probes measure themselves
in `chi_vs_witness_max_rel_at_q0`. Serializing at 17 keeps the witness
reproducible; the accuracy lives in a caveat. Both are stated in the witness.

**This is a general hazard, not a threerow one.** Any producer combining an
mpmath weight with an f64 kernel hits it, and `str_at_true_precision` cannot see
it. Worth a follow-up: either teach the helper about mixed products (it would
need provenance, which it deliberately does not track) or document the limit in
its docstring so the next drain does not walk into it.

## Two verdicts that were being decided in float64

Not sink coercions — these reached into the computation, and are the reason the
"just fix the sink" framing was wrong:

  * `threerow_crossing_a_dependence_probe.scan_crossings` returned `float()`, so
    the PHYSICAL vs DIAGNOSTIC classification (`q <= q₀`) compared an f64
    crossing against a 50-dps q₀. No classification changes, but it was decided
    at 1e-17 on a value resolved to ~1e-16.
  * `threerow_qcross_trend_probe.exact_crossing_polys` had
    `bool(float(a)**2 < float(Q_STAR))` where `a` is an EXACT sympy rational
    bounding an isolated root — an exact bound round-tripped through f64 to be
    compared with a 50-dps q*. Now decided in mpf.

A third was latent: `qcross`'s monotonicity assertion reads the first crossing
back out of the witness dict. Serializing crossings to strings would have made
`seq[i+1] > seq[i]` a LEXICOGRAPHIC comparison and silently changed an
assertion's meaning. The mpf values are kept in a parallel structure.

## Undeclared dependency

`threerow_chi_sparse.py` imports `scipy.sparse` at module scope with no
fallback, so two of the four producers hard-require scipy. The repo has no
top-level `requirements.txt` or `pyproject.toml` declaring it (only
`qou-mass/pyproject.toml`, unrelated), and scipy was absent from this container
until installed by hand. Recorded, not fixed: adding a dependency manifest is a
structural change beyond this drain.

### CORRECTION to the blast-radius note above: `gram_qtrace` is a DIFFERENT defect

Above I wrote that `gram_qtrace_hutchinson_probe.py` is "confirmed also broken
by the same guard" and told whoever picks it up that "the fix is only
`allow_float64=True` IF that call site's path really is f64". **That advice
would have been wrong here, and would have papered over a live wrong number.**

Diagnosed properly: this probe never calls `set_compute_dps` at all. So `mp.dps`
is still mpmath's default 15 when it runs

    q0 = mp.mpf(str(_Q50))        # _Q50 = q_parameter.Q_50_DIGIT_STR

and the 50-digit substrate anchor is TRUNCATED as it is parsed:

    built at dps=15 : 1.109978582751380837834176      <- what the probe used
    built at dps=50 : 1.109978582751380807591669      <- the anchor
                                     ^ diverges at the 17th digit

The guard is not a false positive and the sweep is not "deliberately f64" — it
is catching a real truncation of q₀. The probe's own comment at that line claims
the opposite ("50-dps source: `mpf(str(q_parameter.Q))` ... atom_braid_word_3A
now rejects it"), i.e. someone already tried to fix this and the fix was
ineffective because dps was never raised. `allow_float64=True` here would have
silenced a correct guard and frozen the wrong anchor in place.

Correct fix: `set_compute_dps(50)` before the first `mp.mpf(<50-digit string>)`.
Applied. **This is the same defect class the bean already recorded once** — the
`VOL_41` constant built at module scope above `set_compute_dps` in
`one_loop_c_sigma_tetrahedral_probe.py`. Second instance, different producer,
found by a different gate. A static `module_const_precision_audit` catches the
module-scope form; this one is inside a function, so only running the producer
finds it.

**Not yet re-run**, so its witness is not regenerated here: the value of q₀ moves
in the 17th digit, so its numbers will move and that needs its own verification
pass rather than being folded into a drain commit.

`threerow_sign_crossing_decomp.py` was ALSO blocked by the guard and now runs
again as a side effect of the χ-helper declaration — it imports `chi_atom`.

`threerow_n12_isospin_control.py` is broken for an unrelated reason (it does
`import _path_bridge` without first putting `computations/` on `sys.path`, so it
fails from every cwd). Pre-existing, produces no witness, not touched.

---

## DONE — the `deltalambda/threerow-*` four are drained. 18 NEW -> 14 NEW

Branch `claude/drain-deltalambda-threerow` (cut fresh from `main` at
`25387e2a4`; #4729's branch was merged and must not be built on). Pushed.

    threerow-qcross-trend            126 -> 0
    threerow-crossing-a-dependence    82 -> 0
    threerow-4he-completion           73 -> 0
    threerow-sign-crossing            15 -> 0
                                     ----
                                     296 fields

Ratchet re-run on the result: `new_not_baselined` 18 -> 14, `total_fields`
541,817 -> 541,521 (-296, exactly these four). `regressed` unchanged at 2 —
neither is this branch's. **Still exits 1.** That was the stated expectation
before starting, and it is met, not beaten: this was a fifth of the fields.

**Nothing baselined, no `--rebaseline`, no number hand-edited.** The audit
witness is regenerated because its COUNTS moved.

### How each drain was verified

Not "the ratchet went green" — that is the weakest possible check, and as
recorded above a wrong drain can make it green while degrading the witness.
Each producer was diffed leaf-by-leaf against a pre-drain copy:

    witness                          fields  worst value move   assertions
    threerow-sign-crossing            15/15   9.0e-17           3/3 identical
    threerow-crossing-a-dependence    82/82   5.8e-15           6/6 identical
    threerow-4he-completion           73/73   2.9e-15           4/4 identical
    threerow-qcross-trend            126/126  1.1e-15           5/5 identical

Every assertion record is byte-identical to the pre-drain witness, and every
verdict is unchanged: D crosses and the n=9 crossings lie above the Wenzl pole;
⁴He's physical sign +1 -> -1 with a crossing at 1.02092; q₀'s position
COINCIDENTAL at 0.852 bits with 54 natural constants in the window.

The largest moves are all in the character-free blocks, and they are moves
TOWARD precision: those values were being truncated to f64 and now carry their
real 50 dps. The f64-derived blocks did not move at all — they are byte-equal
at 17 digits to what the float64 held.

`threerow-sign-crossing` is the strongest evidence the frozen witnesses were
correct: after only the `allow_float64` declaration and before any
serialization change, it regenerated with all 51 data leaves IDENTICAL.

### Cost, for the next person sizing the rest

Wall clock, on this container, single runs:

    threerow-sign-crossing              7 s
    threerow-crossing-a-dependence     ~3 min
    threerow-4he-completion            ~35 min   (n=12, 18-step bisection)
    threerow-qcross-trend            5013 s      (n=12 grid + 30-step bisection)

So ~1.5 h of compute for 296 fields. The `nastokes-*` + `alpha/*` numpy ports
(1092 fields, 5 producers) are a different and larger job — a real port, not a
serialization split — and nothing here reduces them.

### Still open on this bean

  * `nastokes-*` (4 files, 1001 fields) + `alpha/*` (1, 91) — numpy ports
  * the qbeta trio (3 files, 35) — the bean's original three, still undrained
  * 7 further small ones, and the 2 REGRESSED
  * `gram_qtrace_hutchinson_probe.py` — dps-ordering fix applied and COMMITTED
    (`02b612f96`); witness NOT regenerated. The producer gets past the guard now
    but outruns this container: no output after 4 min, and a background run was
    killed at ~10 min CPU (16 GB free, so slowness rather than memory). Its q₀
    moves in the 17th digit, so its numbers will move — that needs its own
    verification pass, and `gram-qtrace-hutchinson-probe.witness.json` is
    known-stale until someone does it.
  * `gram_norm_binding_probe.py`, `gram_transfer_quadratic.py`,
    `threerow_isospin_parity_probe.py` — never established whether the guard
    breaks them; each exceeded a 4-minute probe budget before reaching a verdict
