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
updated_at: 2026-08-10T02:10:00Z
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

---

## Second batch: 14 NEW -> 7 NEW, 2 REGRESSED -> 1

Everything drainable in this container is now drained. Running total for the
branch: **18 NEW + 2 REGRESSED -> 7 NEW + 1 REGRESSED**, 541,817 -> 541,393
fields.

Drained and verified this batch (all leaf-diffed against a pre-drain copy,
assertions byte-identical):

    keystone-colored-sigma235-wrt   36 -> 0   (was REGRESSED at 52)
    qborel-growth-budget            16 -> 0
    cauchymul-order-cancellation    15 -> 0
    canonical-ordering-dof          25 -> 0
    markov-z-fibre-rank-bar-cov      6 -> 0
    crossing-energy-channel-basis    5 -> 0
    volume-binding-four-point        5 -> 0
    c3-w2-c1-pole-divisor            4 -> 0

### The qbeta trio — this bean's ORIGINAL three — are done

And the reason they landed undrained is now concrete: **all three write their
own `json.dump` and never pass `WitnessBuilder.save`**, so #4729's guard could
not see them. That is the bypass #4729's own PR body flagged as its known
limit; the trio is the worked example of it.

All three turned out to be EXACT RATIONAL computations done in float64 —
integer kernel degrees over integers, `log_q` values over `n^2`. Fixed with
`fractions.Fraction`, verdicts decided exactly, serialized as both `p/q` and a
50-dps decimal. The noise was real: `abs_diff` was `0.0012499999999999734` for
a quantity that is exactly `1/800`, and the final Cauchy ratio was
`0.9948979591836735` for exactly `195/196`.

### Three more things that were decided in float64

  * `keystone`'s `qint_value_map_refuted` compared f64 shadows of mpf ratios,
    and its colored-support residue was `int(round(float(val))) % 60` — an
    integer residue pulled through an f64 round-trip.
  * `c3-w2-c1`'s decay factors were `round(x, 4)`-ed into the witness AND
    tested there: two of the four printed as exactly `10.0` — the one value
    that would mean "exactly linear" — where they are 9.99997 and 9.99998.
  * `canonical-ordering-dof`'s 1%-of-B_AME test ran on a `float()`-ed spread.

### A gap in the ratchet's model: inherited float64

`canonical-ordering-dof` reads `B_pred_MeV` / `B_AME_MeV` out of
`mass-table-comprehensive.witness.json`, which **is in the baseline** with
75,112 raw float64 fields. The baseline covers the SOURCE of those numbers; it
does not cover a COPY of them into a new witness. So a baselined witness
quietly seeds new ratchet debt in every downstream consumer, and the consumer
gets flagged for the producer's debt. Worth deciding deliberately: either
consumers must re-serialize inherited values (what was done here — `repr` at
the true f64 width, declaring the inheritance), or the audit needs a notion of
provenance it currently has no way to express.

## What is left, and why each is left

**Drainable, but not in this container (3 files, 99 fields).** Regenerating
these here would DESTROY data, so the source is fixed and the witness is
deliberately not re-run:

    atomic-tr-m-mpfr-50dps-proton   20   needs pyhecke_native (absent). A bare
                                         run nulls n_crossings_canonical and
                                         drops the rust tr_M values. Also needs
                                         QOU_Q0_ANCHOR=proton --anchor proton.
    chi-helium-4-h12-at-q0-50dps    78   same native kernel. All 78 are
                                         compute_time_sec — the 1 -> 78
                                         "regression" was a completion pass
                                         adding per-partition timings, not a
                                         precision loss.
    ground-state-ordering-argmin      1   its witness carries a `lean_bridge`
                                         block NO producer writes (added by
                                         7c60b2f38, cited by
                                         docs/audits/2026-08-09-ground-state-
                                         ordering-truth-value.md). Re-running
                                         deletes it. The probe also defaults to
                                         --max-a 14 while the witness is
                                         max_A=16, so a bare run shrinks the
                                         sweep 62 -> 47 cases.

All three timing fixes are committed, so they land the moment someone re-runs
on a host with the native kernel (and, for ground-state, once the lean_bridge
block has a producer).

**The real remaining work: the numpy ports (5 files, 1092 fields).**

    nastokes-multigen-cluster-additivity   835
    nastokes-orbit-symmetric-readout        98
    alpha-k-jones-markov-h12                91
    nastokes-germ-gauge-covariance          52
    nastokes-transverse-curvature-seifert   16

These are category 3 in #4729's taxonomy — the linear algebra itself is
float64 (`trace=float(np.trace(Om))`). Not a serialization split; a port. They
are 78% of the remaining fields and none of this batch's technique applies.

### Reproducibility defects found along the way (not float64, but worse)

Recording these because a witness nobody can regenerate is a bigger problem
than one carrying float64:

  * `ground-state-ordering-argmin-sweep` — producer deletes a published block
    (above), and its default flag shrinks the sweep.
  * `atomic-tr-m-mpfr-50dps` — bare run silently degrades to the non-native
    path; the `--anchor proton` guard is good and DID fire.
  * `threerow_n12_isospin_control.py` — `import _path_bridge` without putting
    `computations/` on `sys.path`; fails from every cwd. No witness, untouched.
  * scipy is undeclared repo-wide (no top-level requirements.txt/pyproject).

---

## Third batch: the numpy cluster. 7 NEW -> 3 NEW

    nastokes-multigen-cluster-additivity   835 -> 0
    nastokes-orbit-symmetric-readout        98 -> 0
    nastokes-germ-gauge-covariance          52 -> 0
    nastokes-transverse-curvature-seifert   16 -> 0
    alpha-k-jones-markov-h12                91 -> (source fixed, cannot run here)

**Branch total: 18 NEW + 2 REGRESSED -> 3 NEW + 1 REGRESSED**, 541,817 ->
540,392 fields (-1,425).

### These were NOT ported to mpmath, and that is the right answer

My earlier note sized this cluster as "a real port, the expensive kind". That
was wrong about what the fix should be. Reading the producers:

  * `nastokes-transverse-curvature-seifert` imports **no numpy at all** — it
    was in the cluster by name only. Its floats were mpf AME constants being
    `float()`-ed on the way in, plus two exact integer-over-integer
    combinatorial ratios. Fixed exactly, worst value move 0.0.
  * The three real numpy probes each already carry their own precision
    control: multigen re-runs R_3 at 40 dps in mpmath at dim 11, and says so
    in its own caveat. The verdicts are 0-vs-O(1e3) questions, not
    1-part-per-quadrillion questions.

Porting a dim-77 sweep over ten germ pairs and four isotopes to mpmath would
cost hours per run to produce digits the question does not use — and it would
publish precision the numpy kernel never had. So each numeric field is written
at **binary64's own round-trip width** (`repr`), applied once at the single
`add_data` sink rather than at ~30 call sites, so a field added later cannot
quietly miss it.

Verified harder than a leaf diff: every one of the 985 values round-trips to a
**bit-identical** float, leaf counts unchanged (1135 / 170 / 71), and 16/16,
17/17, 15/15 assertions byte-identical.

### A witness that was not valid JSON

`nastokes-orbit-symmetric-readout` contained a bare `NaN` literal at
`part_C.He4.band-local.SA_average_over_mean`. `json.dump` emits that by
default, but **JSON has no such token** — any strict parser rejected the file.
Confirmed: the pre-drain witness fails `json.load(..., parse_constant=raise)`
and the drained one passes. The NaN value itself is unchanged and still says
what it said; it is simply no longer smuggled through as an invalid literal.
Worth a sweep of the other witnesses for the same thing.

## What remains, and none of it is drain work

    alpha-k-jones-markov-h12        91   pyhecke_native absent (module-scope
                                         import — the probe will not even load)
    atomic-tr-m-mpfr-50dps-proton   20   pyhecke_native
    chi-helium-4-h12-at-q0-50dps    78   pyhecke_native   [REGRESSED]
    ground-state-ordering-argmin     1   its lean_bridge block has no producer

All four have their **producer sinks already fixed and committed**. They land
the moment someone re-runs on a host with `pyhecke_native` — except
ground-state, which needs the `lean_bridge` block to get a producer first.

The alpha change is **syntax-checked only**, flagged as such in its commit:
the module cannot be imported here, so it has never been executed. Whoever
re-runs it on a native-kernel host should diff the witness before committing,
the same way every other drain in this branch was checked.

---

## Fourth batch: pyhecke_native BUILT. 3 NEW + 1 REGRESSED -> 1 NEW + 1 REGRESSED

The three witnesses I had recorded as "cannot be regenerated in this container"
were only blocked on a missing Rust extension, and the repo ships a script to
build it: `scripts/build-pyhecke-native.sh`. It works, ~4 minutes.

    pip install maturin; maturin build --release; pip install the wheel

Its header explains the one non-obvious part, and it matters for any agent
hitting this again: the Cargo graph pins a git fork
(`github.com/litlfred/Clarabel.rs`), the sandbox rewrites every
`https://github.com/...` to a local mirror that only serves `litlfred/qou`, so
the fork 403s at `cargo metadata`. The script temporarily drops that one
rewrite and restores it via a trap. **The wheel is EPHEMERAL** — it lives in
the session's user site-packages and dies with the container, so re-run the
script in any fresh session before Hecke-precision compute.

    alpha-k-jones-markov-h12        91 -> 0   ZERO value differences
    atomic-tr-m-mpfr-50dps-proton   20 -> 0   values CORRECTED, see below
    chi-helium-4-h12-at-q0-50dps    78        NOT regenerated — see below

### Match the environment before accepting a regenerated witness

`alpha`'s first regeneration recorded `clarabel: null` and `mpmath: 1.3.0`
where the committed witness had `0.11.1` and `1.4.1` — a provenance
DOWNGRADE, from this container being thinner than the one that produced it.
Fixed by installing both to match, after which the environment block is
byte-identical and there are ZERO value differences across all 91 numbers.

Two traps found doing that, both worth knowing:

  * **`WitnessBuilder.save` is content-diff-aware**, so once the drained
    content is on disk, later runs PRESERVE the existing file including its
    stale `environment` block. Installing clarabel and re-running changed
    nothing. The witness has to be DELETED to force a genuine rewrite.
  * A version delta in `environment` is invisible in a normal "did the values
    move?" diff, because no value moves. It has to be checked separately.

### `atomic-tr-m-mpfr-50dps-proton`: the values were STALE, by 1h34m

The drain is the lesser half of that commit. The committed witness agrees with
a fresh run to only ~18 significant digits, then diverges:

    proton  old 1.065306134791738413807655...
            new 1.065306134791738450558029...

Isolated before committing, because "my change moved a number" is the first
thing to rule out: re-running the PRE-drain source produces the new value too.
Then dated it —

    witness computedAt   2026-08-08T17:55:45Z
    efcaf79ed landed     2026-08-08T19:29:17Z   (1h34m later)
      "NO FLOAT64: the braid word was f64 at source"

So every digit past the ~17th in that 50-dps witness was computed from an
f64-limited braid word and was never real. The new values are the correction,
not a regression. Same q0, same anchor, same hoefsmit-python-fallback method,
identical environment, deterministic across repeats.

**This is the second witness in this bean found to predate a fix that changed
its numbers** (the first being the threerow four, which predated the guard
rather than a value change). The pattern to expect: anything computed in the
window around 2026-08-08 may carry pre-`efcaf79ed` digits.

### `chi-helium-4-h12-at-q0-50dps`: NOT a drain decision, so not made

Its 78 fields are all `compute_time_sec`, and the obvious move — run
`_b0vf_complete_he4_witness.py`, which advertises "rewrites the witness in
place" — is WRONG, and I nearly did it. Running it produces:

  * all 77 `chi_lambda` values different at the **7th** digit;
  * `tr_M_at_q0` different at the 8th;
  * a `_provenance` block the committed witness does not have;
  * `producer` changing from `chi_at_q0_via_hoefsmit_mpfr.py` to
    `branch-decomp + chi_lambda_all_partitions_mpfr`.

The committed `tr_M_at_q0` is EXACTLY the new run's `markov_peel_scalar`. So
the two scripts publish two DIFFERENT quantities under the same key — the
markov-peel scalar vs the Wenzl Sigma y chi pairing — separated by the
documented dual-path gap (1.94e-7, inside its own 4.80e-7 tolerance). Running
the b0vf script would silently swap the semantics of a published field while
appearing to be a float64 cleanup.

**Which method owns this witness is a domain decision, not a drain.** So the
witness is reverted and untouched. What IS done: the timing sinks are fixed in
`chi_at_q0_via_hoefsmit_mpfr.py`, the producer the witness names in its own
`producer` field — I had previously fixed only `chi_4he_via_rust_lossless.py`
and the b0vf script, i.e. the wrong two.

A regeneration via the correct owner (`--fresh`, n=12, 77 partitions in mpfr)
is running but is slow; whoever finishes it should expect the same
pre-`efcaf79ed` staleness question the atomic witness had, and should diff
before committing.

## State: 1 NEW + 1 REGRESSED, 541,817 -> 540,281 fields

    ground-state-ordering-argmin-sweep   1   blocked: its lean_bridge block has
                                             no producer (see earlier entry)
    chi-helium-4-h12-at-q0-50dps        78   blocked: needs the owner decision
                                             above, not drain work

---

## The bare-literal issue: 20 live invalid witnesses -> 4, and WHY each happened

A JSON-validity sweep of all 2841 witnesses under `computations/` found 25 that
fail `json.load(..., parse_constant=raise)` — 20 live, 5 deprecated. `json.dump`
emits bare `NaN` / `Infinity` / `-Infinity` by default and **JSON has no such
tokens** (RFC 8259 numbers are finite decimals), so those files are not valid
JSON. Python's own loader accepts them, which is exactly why nobody noticed: a
producer round-trips its own output happily and only a non-Python consumer ever
discovers the file is unreadable.

**The causes are not one thing.** Sorting them turned out to be the whole job,
because they want different fixes and conflating them is how a "cleanup" makes
a witness worse:

| cause | example | right fix |
|---|---|---|
| swallowed bug | habiro (18 fields) | fix the bug — do NOT serialize the NaN |
| deliberate pole sentinel | casimir t=1 (27) | marker `"inf"` — the value is correct |
| genuine divergence | term6 deuteron (5) | marker + a status that says so |
| undefined by construction | qbeta k=4 (7), a-K u0=0 (4) | `null` + recorded reason |
| f64 overflow | su4 heavy nuclei (10) | `null` + reason — not representable |
| infeasible solve | frobenius-repose (30) | `null` — no solution exists |
| missing upstream key | braid-encoding-audit (2) | `null` + a `_missing` flag |
| hardcoded math fact | gap-a4 J(edge) = ∞ (1) | marker — it IS infinity |

Two structural fixes, both in the substrate:

  * **`qou_substrate.precision.json_safe_float`** — markers (`"inf"`, `"-inf"`,
    `"nan"`), deliberately NOT `null` (a pole and a missing value are different
    facts) and NOT `1e999` (that is how a non-finite becomes a silently wrong
    finite number). Its absence is the structural reason these literals kept
    appearing: **a producer with a legitimate infinity had no sanctioned way to
    write one**, so it wrote the bare literal. Its docstring says explicitly not
    to use it to launder a swallowed exception.
  * **A `QOU_WITNESS_STRICT_NONFINITE` guard** at `WitnessBuilder.save`, same
    warn-by-default shape as the raw-float64 guard beside it. It has already
    earned its place: after I fixed su4's `W_lam` it caught the 8 DERIVED fields
    (`B_lincomp` and everything computed from it) that I had missed.

### The habiro bug is worth reading twice

Nine witnesses carried NaN in `tr_M_at_q0_via_u_poly`. The cause:

    sp.sympify(denom, locals={"check_q": u})

maps the wrong NAME. `to_u_polynomial(expr, q, check_q)` renders its returned
strings using whatever SYMBOL the caller passes, and the callers pass `u` — so
modern strings say `"u"`, and that mapping parsed them into a FRESH
`Symbol('u')` with no assumptions. `Symbol('u') != Symbol('u', positive=True,
real=True)`, so `.subs(u, ...)` silently no-opped, `sp.N` returned an
expression rather than a number, `mp.mpf(str(<expression>))` raised
ValueError — and a bare `except Exception` wrote `float('nan')` and printed the
reason to stdout, where it was lost.

The cross-check had therefore been failing silently for months. With the
mapping fixed it PASSES: proton now gives `1.0653061442544443` via the u-poly
against `tr_M_at_q0 = 1.0653061442544502`. The handler now records `null` plus
`tr_M_at_q0_check_error`, so the next failure is diagnosable.

The mapping accepts BOTH names now: older witnesses in this family legitimately
say `check_q`, from a caller that passed a symbol of that name.

### Four left, none of them blocked on the fix

    a-K-via-lp-dual        source FIXED, witness not regenerated: this container
                           now has clarabel 0.11.1 (installed to match the alpha
                           witness's environment) and this witness's environment
                           does NOT. With clarabel present the LP takes a
                           different solve path and x_star moves ~1e-6 — a
                           different, still-valid optimum. That is #4729's "the
                           probe was measuring its solver" finding again, and
                           baking it in under cover of a JSON fix would repeat
                           the mistake. Which solver this witness pins to is its
                           owner's call. (Also: needs
                           PYTHONPATH=tools/pyhecke/python to import at all.)
    term6-full-pole-sum    source FIXED (status logic + markers). Producer is
                           already broken on HEAD — dies in
                           complex(float(re), float(im)), "Cannot convert
                           expression to float". Verified by running the
                           unmodified HEAD copy.
    A-operator-rank-probe  not reached; producer exceeds a 200s budget.
    habiro-...-oxygen-14   no live producer — oxygen-14 is not in any ATOMS list
                           in the habiro extract scripts.

### Re-running a witness is not free — three ways it silently changes

Every one of these bit me at least once, and each is invisible to a naive
"did the values move?" check:

  1. **Anchor.** A bare re-run uses today's DEFAULT q0. casimir was computed at
     the ideal-muon pin and a fresh run moved 182 values at ~1e-8; su4 the same,
     285 values. Both re-run with `QOU_Q0_ANCHOR=ideal` to match. gap-a4 goes
     the OTHER way and cannot be steered at all — it reads a HARDCODED
     `Q_0_50DPS` constant, so `QOU_Q0_ANCHOR` has no effect and its committed
     proton value could not have come from the current code.
  2. **Environment.** `alpha`'s first regeneration recorded `clarabel: null` and
     `mpmath 1.3.0` where the committed witness had `0.11.1` and `1.4.1` — a
     provenance DOWNGRADE that no value diff would show. And installing clarabel
     to fix that is what changed a-K's LP solution.
  3. **Content-diff-aware save.** Once the new content is on disk, later runs
     PRESERVE the existing file including its stale `environment` block. The
     witness has to be DELETED to force a genuine rewrite.

### Two pre-existing defects found while verifying

  * `casimir_macdonald_probe` has ALWAYS exited 1, after writing its witness —
    an f-string formats a tuple with `:<14`, so that print block has never run.
  * `term6` reported a DIVERGENT Mittag-Leffler sum with
    `status: "complete-simple-poles-only"`. The status only ever asked whether a
    higher-order pole was unresolved, never whether the sum was finite.

### Also: 5 deprecated witnesses are invalid, one for a different reason

`_deprecated/qbeta-gb-filtration-residues.witness.json` is malformed in a way
NaN does not explain — it contains hand-written `+20.27` and `+202689`, and
JSON forbids a leading plus. Not touched (deprecated).

---

## MERGED — PR #4893, `8cf939a3b`. Ratchet on `main`: 4 NEW, 0 REGRESSED

From 18 NEW + 2 REGRESSED when this branch started. **Both REGRESSED entries
are gone.** Rebase-merged as 47 linear commits per AGENTS.md rule 8.

Two mechanical notes for the next merge of this kind:

  * **A branch containing a merge commit cannot be rebase-merged** — GitHub
    returns `405 This branch can't be rebased`. Integrating `origin/main` with
    `git merge` therefore forecloses the repo's DEFAULT merge method. Fix:
    `git rebase origin/main` locally to linearize, then rebase-merge. Verified
    the linearization was content-neutral (`git diff backup HEAD` empty) before
    force-pushing with an explicit `--force-with-lease=<ref>:<sha>`.
  * The `witness-raw-float64-audit` witness conflicts on EVERY such merge and
    rebase, because both sides carry a stale snapshot of its own counts.
    Neither side is the answer: resolve by taking either and **re-running the
    producer**, which is what the file is for.

## STALE PUBLISHED VALUES — `charm-frobenius-block-projection` (NOT a drain issue)

Found while sizing the three witnesses main brought in. This one's committed
numbers **do not reproduce from current `main`**, and not by a little:

    pred_charm_over_light          1.3486556457833476 -> 0.9757693178472477   (28%)
    pred_top_over_light            0.05475486952775208 -> 0.0                 (100%)
    y_chi_block.(1, 1, 1)          0.02274494257734719 -> 0.0                 (100%)
    y_chi_block.(3,)               0.4153957953606134 -> 0.5054042265039308   (22%)
    y_chi_block.(2, 1)             0.5602258846477554 -> 0.49315793733285646  (12%)

38 fields move by more than 1e-9. Two go to exactly zero.

**I first assumed mpmath 1.4.1 vs 1.3.0 and I was wrong** — downgrading to
1.3.0 and re-running gives the same new values, so the interpreter environment
is not the cause. The producer's own inputs or code changed under a witness
that was never re-run.

NOT regenerated here, deliberately: a 28% move in a published physics ratio is
not something to bundle into a float64-serialization commit. It needs its arc's
owner to say which number is right. Recorded as its own open item.

`m-tau-complex-volume-search` has a smaller version of the same: `snappy_volume`
-4.34e-14 -> -1.48e-8. Both are numerically zero, but the committed one is not
what a fresh run produces.

## Drained since the merge

    delta-lambda-alexander-phase4   67 -> 0   (branch
                                    claude/drain-main-inherited-float64)

It is the only one of main's three that reproduces EXACTLY before the drain, so
the drain is the sole change. Every value is f64-limited by construction (sympy
`.evalf()` then `complex()`), so it is written at binary64's round-trip width;
all 67 round-trip bit-identically.

## Open

    charm-frobenius-block-projection   79   values stale by up to 28% — owner
    m-tau-complex-volume-search        54   snappy_volume does not reproduce
    ground-state-ordering-argmin-sweep  1   lean_bridge block has no producer

Inherited reds on `main` that are NOT this bean's arc, recorded so the next
prepare-merge does not mistake them for new:

    float64-padding ratchet   cross-check-trM-1ppb.witness.json  (dbd91b5ff)
    module-const precision    y_lambda_su_n.py REG_ZC / REG_ZD

---

## THE RATCHET IS GREEN. 0 NEW, 0 REGRESSED — and so are the other two gates

`scripts/precision-gates.sh`: **All blocking precision gates green.**

From 18 NEW + 2 REGRESSED when this bean's arc started, through 21 NEW + 2 that
`main` accrued in parallel. **Nothing baselined, no `--rebaseline`, no number
hand-edited** — every entry fixed at its producer and verified by diffing the
regenerated witness against a pre-drain copy.

### The last entry was stuck on a destructive producer, not on float64

`ground-state-ordering-argmin-sweep` sat at 1 field for the whole arc because
re-running it DELETED a published result: its witness carries a `lean_bridge`
block **no producer writes** (added by `7c60b2f38`, cited by
`docs/audits/2026-08-09-ground-state-ordering-truth-value.md`), and the write
was a plain overwrite.

Fixed by making the write MERGE — any top-level block already on disk that the
run does not compute is carried forward, and the run prints which. A producer
that silently drops published data is a worse defect than a stale field. Run
with `--max-a 16` to match the committed sweep (the script's default 14 would
shrink it 62 -> 47 cases). `lean_bridge` byte-identical, zero non-timing
differences.

### The other two gates: one root cause, inherited from main

Both were the same defect — an `mpf()` literal parsed at module import while
mpmath is still at its DEFAULT 15 dps, with the real precision set later inside
a function:

    float64-padding    cross_check_trM_1ppb.py  TOLERANCE_PPQ = mpf("1e-15")
                       at module scope; mp.dps = args.dps in main(). str()
                       then printed the binary64 expansion
                       0.000000000000001000000000000000077705399876661079...
                       for a value that is exactly 1e-15.

    module-const       y_lambda_su_n.py  REG_ZC / REG_ZD, the
                       trace-convention-registry reference constants, rounded
                       to 53 bits before self_test() raises dps to 30 —
                       "already wrong when built".

Both fixed as the gate's own message prescribes: idempotent
`set_compute_dps()` at module scope above the constants.

**This is now the FOURTH instance of that defect class in this bean** —
`VOL_41` in the tetrahedral probe, `gram_qtrace`'s q0, and now these two. It is
the single most repeated precision bug in the corpus, it is invisible until
something prints the value at high dps, and the fix is one line every time.
Worth a lint rule rather than a fifth discovery.

### `m-tau`: the value that "did not reproduce" was NONDETERMINISTIC

Not staleness. `snappy_volume` for the torus carriers returned
`-4.335420911161236e-14` on one call and `-2.4684863123708434e-07` on the next,
**in the same process**, with `solution_type` = "contains degenerate
tetrahedra". A torus-knot complement is Seifert-fibred, not hyperbolic, so the
volume is exactly zero — the module's own docstring says so — and SnapPy was
returning the residual of a degenerate solve.

17 digits of solver noise were being published as a measurement, which is why
the witness could never reproduce. Now the exact 0 with a note; `solution_type`
still carries the degeneracy; the `hyperbolic` verdict is untouched (threshold
1e-4, orders above any residual). Two consecutive full runs now differ in
nothing outside metadata.

## Open, and none of it is drain work

    charm-frobenius-block-projection   RESOLVED — was convention C, see qou-wgta
    the C cache + 15 direct readers     qou-wgta P0, recorded there
    4 witnesses still not valid JSON    a-K (solver-pinning decision), term6
                                        (producer broken on HEAD), oxygen-14
                                        (no live producer), A-operator-rank
                                        (>200s budget)

---

## Two more producers revived; the bare-literal count is 20 live -> 3

### `term6_full_pole_sum` was DEAD on main, for the habiro bug's mirror image

I recorded earlier that term6's producer "is already broken on HEAD" and left
its witness. The cause turns out to be the same defect as the habiro NaNs,
seen from the consumer side:

    term6 reads p_in_u / denom_in_u out of
    habiro/habiro-coefficients-atomic.witness.json and does
    `sp.sympify(s)` with NO locals, then `.subs(u, sqrt(q))`.

That witness (2026-07-18) stores those polynomials in terms of **`check_q`**,
because `to_u_polynomial(expr, q, check_q)` renders its strings using whatever
SYMBOL the caller passed. So the sympified expression got its own free symbol,
the subs no-opped, the expression stayed symbolic, and
`float(complex(sp.N(...)))` raised "Cannot convert expression to float".

Fixed with `locals={"u": u, "check_q": u}` — the same both-names fix applied to
the habiro extract. **The producer runs for the first time**, and the status
logic committed earlier finally takes effect:

    term6_simple_residue_partial  Infinity  ->  "inf"   (marker)
    term6_in_MeV                  Infinity  ->  null
    status   "complete-simple-poles-only"  ->  "divergent-simple-pole-sum"

Drained in the same pass, 72 raw float64 -> 0.

Proton/neutron MeV move ~1.3e-9 and that is INHERITED: `m_e_MeV` was refined
upstream from 0.51099895 to 0.51099895069, which is exactly that ratio.

**Three instances of the sympify-locals bug now** (habiro extract ×2 sites,
term6 consumer). The root is that `to_u_polynomial`'s output variable name is
whatever the caller passed, so every string it produces is only parseable if
you know which symbol that was. Worth fixing at the source — have it always
render in one name, or record the name alongside the string — rather than
teaching each consumer both.

### `A-operator-rank`: a deliberate sentinel, like casimir

`drop_ratio = smallest_nonzero / next_zero if next_zero > 0 else inf`. The
`inf` means the next singular value is exactly zero, i.e. the rank gap is
perfectly clean — and `status` reads `rank_determined` on it, correctly. The
value is right; the bare `Infinity` token was not. Marker applied; producer
re-running (it exceeds a 200 s budget, hence the earlier "not reached").

### `oxygen-14` is an ORPHAN, and provably so

No live producer names it: `_habiro_coefficient_extract.ATOMS` stops at A=10
(carbon-10) and oxygen-14 is A=14; the helium extract and
`habiro_coefficients_interpolate.py` do not mention it either.

Its history says why: the witness's `computedAt` is 2026-06-29, but the ONLY
commit touching the file is `d156e8d50` (2026-08-02) — a docs+bean commit about
the saddle-offset probe, nothing to do with habiro. So it sat uncommitted for a
month and was swept into an unrelated commit from someone's working tree.

Its 2 NaN fields are exactly the ones the habiro fix repairs, so re-running
would fix it — but nothing runs it. Either add (8, 6) to ATOMS deliberately
(A=14 means 16·16 = 256 strands, a real cost) or drop the file. Not a call to
make silently.

### `a-K-via-lp-dual`: the solver question has a concrete answer

Earlier I left this as "which solver it pins to is its owner's call". The
mechanism is now known and narrows the question: `solve_operator_selection_lp`
takes `backend="auto"`, documented as *"clarabel MPFR at ~50 dps when its
binary or wheel is available, else scipy HiGHS f64"*.

The committed witness's `environment` has **no clarabel**, so it was computed on
the scipy/HiGHS **f64** path. This container has the clarabel wheel, so "auto"
takes a different branch — which is why `x_star` moves ~1e-6.

So the decision is not "pick a solver", it is: **should this witness be pinned
to the f64 fallback, or regenerated on the higher-precision path now that
clarabel is available?** One caution against assuming the latter is simply
better: the strong_duality residuals did NOT improve (2.7e-15 -> 1.2e-14) when
they should be ~1e-50 if MPFR were really active, so it is worth confirming the
wheel actually enables the MPFR path rather than a second f64 backend, before
treating the new numbers as more precise. Not resolved here.

---

## 2026-08-10 — the ratchet is GREEN. PR #4895 open.

The bean's title condition is finally addressable. Measured on
`claude/drain-main-inherited-float64` @ `32ffd6fe7`, committed as
`computations/witness-raw-float64-audit.witness.json`:

    new_not_baselined : 0     (was 18)
    regressed         : 0     (was 2)
    drained_files     : 18
    total_fields      : 540,028
    baseline_files    : 1,582

`scripts/precision-gates.sh` — **all blocking precision gates green**, not the
ratchet alone. The other two that were red are both one root cause, the
mpf-literal-before-`mp.dps` defect: `cross_check_trM_1ppb.py`'s
`TOLERANCE_PPQ` (float64-padding) and `y_lambda_su_n.py`'s `REG_ZC`/`REG_ZD`
(module-const). That is the **fourth and fifth** instance of that class in this
bean; the lint-rule note above stands and is now the highest-value durable item
left in it.

**Nothing baselined, no `--rebaseline`, no number hand-edited.** Every entry was
fixed at its producer and verified by diffing the regenerated witness against a
pre-drain copy, field by field.

### The four that closed since the last entry, and why each was NOT a drain

None of these four was float64 discipline. Each was a distinct defect the
ratchet merely surfaced:

    charm-frobenius-block-projection  79  computed under trace convention C,
                                          which b88aabc73 excised 59 minutes
                                          AFTER the witness's computedAt.
                                          Proven by checking out the pre-fix
                                          bridge and reproducing the committed
                                          values exactly. See qou-wgta.
    delta-lambda-alexander-phase4     67  reproduced exactly beforehand, so the
                                          drain is the only change. 67/67
                                          round-trip bit-identically.
    m-tau-complex-volume-search       54  published a NONDETERMINISTIC field
                                          (degenerate SnapPy solve residual).
                                          Now exact 0 + note.
    ground-state-ordering-argmin-sweep 1  its producer DELETED a published,
                                          cited block (`lean_bridge`, written by
                                          no producer, cited by an audit doc).
                                          The write now merges.

The `ground-state` one is worth generalising: it sat at 1 field for the entire
arc because **re-running it destroyed data**, so nobody could re-run it to drain
it. Any witness carrying a hand-added block has this property. A plain overwrite
in a producer is a data-loss bug whenever the witness has ever been edited by
something other than that producer.

### Bare `NaN`/`Infinity`: 20 live invalid witnesses -> 2

Two more producers revived (`term6_full_pole_sum`, `A-operator-rank`), both
documented above. The marker (`"inf"` / `"-inf"` / `"nan"` strings from
`json_safe_float`, plus the `QOU_WITNESS_STRICT_NONFINITE` guard at
`WitnessBuilder.save`) is now the convention.

**One hazard the marker introduces, recorded because it will recur:** a marker
is a `str` where a `float` used to be, so any code that READS the field back
breaks. In `A-operator-rank` that was not just a `:.2e` print — `n_exact_drop`
read `drop_ratio` back out of the dict and compared it to `1e6`, and that count
feeds an **assertion**. Left alone it would have changed what the witness
asserts, not merely crashed. Same read-back hazard as `qcross`'s monotonicity
check. When applying the marker, grep for readers of the field, not just
writers.

### Still open, and none of it is drain work

    a-K-via-lp-dual           source fixed, witness NOT regenerated. Needs the
                              clarabel/MPFR question answered first: duality
                              residuals did not improve (2.7e-15 -> 1.2e-14)
                              when MPFR should give ~1e-50, so confirm the wheel
                              actually enables that path before treating the new
                              numbers as more precise. Owner decision.
    habiro-coefficients-      provably orphaned (no live ATOMS entry covers
      oxygen-14               A=14; swept in from a working tree). Either add
                              (8, 6) to ATOMS deliberately — 256 strands, a real
                              cost — or drop the file. Owner decision.
    the C cache + its 17      qou-wgta P0. `y-lambda-at-q0.witness.json` is
      direct readers          verified C; `wedderburn_jones_markov` refuses to
                              serve it, but 17 files open the JSON directly and
                              bypass that guard. Recorded there with the
                              blast radius.

### Bean status

Stays **in-progress**. The title condition — "`main` is RED on its own
raw-float64 ratchet" — is false on this branch and will be false on `main` only
once #4895 merges. Do not close it before then, and re-measure rather than
assume: `main` accrues float64 debt from sibling arcs faster than any single PR
closes it, which is the structural point this bean has been making since the
3 -> 18 revision.

PR: https://github.com/litlfred/qou/pull/4895 (branch
`claude/drain-main-inherited-float64`, 15 commits, base `main`).

---

## CORRECTION 2026-08-10 — `a-K-via-lp-dual` was an ANCHOR, not a solver

The entry above ("the solver question has a concrete answer") reasoned from
`solve_operator_selection_lp`'s `backend="auto"` default and concluded the
committed witness was scipy-f64 while this container would take clarabel-MPFR,
offering the unimproved duality residuals as a caution. **All of that was wrong,
and it was wrong at the first step:**

    computations/aK_via_lp_dual_hecke_basis.py:161
    result = solve_operator_selection_lp(t, G, n_target, backend="scipy")

The call site has pinned scipy since the file's first commit. `auto` is the
*function* default — I read the docstring instead of the call. Clarabel was never
in play in either run, so the residuals (2.7e-15 vs 1.2e-14, both f64 noise about
a ~1e-15 objective, tolerance 1e-6) were never evidence about MPFR.

What actually moved was the q₀ anchor: `t_i` = z at muon in the committed
witness, z at proton in the re-run, matching to f64 epsilon (6.4e-17 / 9.5e-17).
11.5 ppb in q₀ → 3.0e-10 in z → ~4.2e-7 in `x_star`. Fixed by declaring the
producer `ideal_muon` in `q0_anchor_manifest.json`; regenerated 235/240 fields
identical, 4 NaN → null, 1 field moved one ulp in its 50th decimal digit.
Raw float64 101 vs baseline 105, so a drain. Commit `0a5b2b6c7`.

**The generalisable part is now its own bean: `qou-po7i`.** The anchor is chosen
by `sys.argv[0]`'s stem, 2384 of 2785 producers are undeclared, and 1887
witnesses record no anchor at all — so a silent 11.5 ppb re-anchoring gets
attributed to whatever else changed, which is exactly the mistake above.

## CORRECTION 2026-08-10 — `habiro-coefficients-oxygen-14` is NOT orphaned

The entry above ("provably orphaned, and provably so") is wrong on both its
pieces of evidence:

  * **"No live producer names it."** I checked `_habiro_coefficient_extract.ATOMS`,
    which stops at A=10 — the wrong list. `extend_even_a_mirror_pair_test.py`
    carries its OWN atom list, `EVEN_A_OPEN`, including
    `("¹⁴O (oxygen-14, A=14)", "oxygen-14", 8, 6, 224)`, and calls `analyse_atom`
    + `_write_witness` directly (lines 84-97). It is a live producer.
  * **"The only commit touching the file is an unrelated docs commit."** That is
    an artifact of a SHALLOW CLONE (`git rev-parse --is-shallow-repository` →
    true). The history needed to make that claim is not in this container. The
    "swept in from a working tree" story rests on nothing.

Worse, the file has TWO live readers — `extend_even_a_mirror_pair_test.py:117`
and `topic2_mirror_pair_phi8_boundary_scan.py:76`, both via
`load_a_m("oxygen-14")` — so dropping it breaks them. Its 2 NaN fields are
exactly the ones the sympify-locals fix repairs, so the resolution is
regeneration, not deletion.

**Method note for both corrections:** each rested on a grep whose ABSENCE of a
match I read as proof, in a repo where the thing I was grepping for lives in more
than one list and the history is truncated. A negative grep is evidence about the
grep. Confirm an orphan by finding the readers, not by failing to find the writer.

## 2026-08-10 — invalid JSON is now ZERO, and oxygen-14 was regenerated not dropped

Strict-JSON sweep of every live witness: **2552 scanned, 0 invalid.** The arc's
count went 20 → 2 → 0. (One parse error remains under `_deprecated/`,
`qbeta-gb-filtration-residues.witness.json`, and it is not a nonfinite token —
Python's own loader rejects it too. Out of scope, recorded here so it is not
rediscovered as a regression.)

The last two:

  * **`a-K-via-lp-dual-hecke-basis`** — a q₀ anchor, not a solver. Corrected
    above; the systemic half is `qou-po7i`.
  * **`habiro-coefficients-oxygen-14`** — regenerated. `tr_M_at_q0_via_u_poly`
    NaN → 8.17775810558832e-06 and `tr_M_at_q0_rel_err` NaN → **0.0**. The
    rel_err is the load-bearing one: tr_M at q₀ computed two independent ways,
    directly and through the reconstructed u-polynomial, now agrees exactly.
    That is a cross-check passing, not a crash avoided. 216/220 fields identical.

`reconstruction_matches: False` in that witness is **pre-existing and unchanged**
(n_nonzero 34, all_integral true, both before and after). Not this arc's, and not
investigated here — but it is a false in a committed witness that two live
scripts read, so someone should decide whether it is expected for A=14.

Branch rebased onto `origin/main` (35 commits, zero file overlap, clean) and all
blocking precision gates re-run green on the integrated tree: ratchet 0 NEW /
0 REGRESSED, drained_files 19, total_fields 540,024.

## Fresh measurement 2026-08-10 (agent-4912 session, off PR #4935)

Re-measured on `origin/main` @ `86c58229a3` while running
`precision-gates.sh --changed` for an unrelated one-witness metadata refresh.
**The composition has changed and the count is well down** from this bean's
title figure (18 NEW + 2 REGRESSED):

```
witnesses carrying raw float64 : 1577
total raw float64 fields       : 540,512
baseline files / fields        : 1582 / 540,334
drained since baseline         : 21 file(s), -178 field(s)

NEW dirty witnesses            : 1
      25  computations/kappa-shell8-excess-convention.witness.json
REGRESSED (count increased)    : 1
     395 -> 867  computations/a-K-via-lp-dual-full.witness.json
```

Notes:

- **None of the three qbeta witnesses this bean opened on are still NEW** —
  they have been drained. The drain counter (`21 file(s), -178 field(s)`)
  corroborates.
- The surviving REGRESSED entry is `a-K-via-lp-dual-full`, which is
  **`qou-ftuv`'s** scope (LP-dual witnesses carry raw float64 by construction;
  draining needs the shared contract changed). Not independently actionable
  here.
- The surviving NEW entry is `kappa-shell8-excess-convention` (25 fields),
  adjacent to `qou-o16k`.
- Confirmed inherited, not branch damage, by the same test this bean used:
  both files are byte-identical to `origin/main` (`git diff origin/main -- <f>`
  empty) and neither is touched by the measuring branch.

So the remaining red is **two known-owned items**, not a broad regression.
Nothing was baselined, `--rebaseline` was not run, and no number was
hand-edited to reach this reading.

---

## 2026-08-15 — the ratchet's one remaining red, and a regeneration that does NOT work here

Re-measured on `main` at `ebc21d1ae` (main moved 1021 commits since the last
entry):

    NEW dirty witnesses : 0
    REGRESSED           : 1     rho-k-co-casimir-extended.witness.json  3 -> 4
    drained since baseline : 14 file(s)  (incl. binding-k-enumerator 2210 -> 0)

**The one red is timing metadata, not physics.** All four fields are
`per_atom[i].compute_wall_sec` — `0.34`, `9.28`, `9.45`, `2533.2`. The producer
was ALREADY fixed by `29b209ce9` ("float64: four timing fields serialised as
strings"), changing `round(t1-t0, 2)` to `f"{t1-t0:.2f}"`. Only the witness was
never regenerated, so this is the second half of someone else's change, and it
is what holds `/prepare-merge` §4b red for every PR.

### The regeneration is not viable in this container

Attempted and abandoned. `rho_k_co_casimir_extended.py` with its default
`--max-A 4` (the 6 committed atoms):

    elapsed 2h05m, still on the helium-4 leg
    worker CPU: 11m51s / 4m35s / 1m35s / 0m00s  (9.9% / 3.7% / 1.3% / 0%)
    parent CPU: 1 second

The committed witness records `compute_wall_sec = 2533.2` for helium-4 — 42
minutes on whatever host produced it. Three hours in and not finished, with
workers averaging under 5% CPU, says the bottleneck here is not arithmetic. Four
workers at 10/4/1/0 percent is a distribution problem or contention, not a busy
machine. Whoever picks this up should not simply "run it for longer" without
finding out why the workers idle.

### INCIDENT — I gutted the witness, exactly as `witness_shape_guard` predicts

The producer **saves incrementally** (writes the witness after each atom, so an
interrupt does not lose completed work). Two hours in, the on-disk witness was
therefore 5 atoms, not 6, with `durationMs` 2,552,837 -> 7,738.

I then ran `git add -A` for an unrelated bean commit and swept it in:

    6f7ac1001   rho-k-co-casimir-extended.witness.json | 1551 +----------------
                                                          1415 deletions

Caught by diffing against `origin/main` rather than by noticing at commit time.
The commit was local-only, so the fix was to restore from `origin/main` and
amend; the gutted copy never reached the remote. `witness_shape_guard.py` — the
gate written for the *original* rho-k gutting incident — reports
"OK — no witness lost content" after the restore, and would have caught it at
`/prepare-merge` had it got that far.

**This is the SECOND time this arc that a git operation during a background
write has damaged the tree.** The first was `git stash` mid-run (recorded
above). Same root cause, different verb. The rule that actually generalises:

> An incremental-save producer means the working tree is a moving target for as
> long as it runs. Do not run `git add -A`, `git stash`, `git checkout` or
> `git commit` while one is in flight — stage explicit paths, or wait.

`git add -A` is the worst offender because it is the habit, not the exception.

### Bean status

Stays open. The red is real, the fix is known (regenerate the witness with the
already-fixed producer), and the blocker is compute rather than diagnosis.

## Bottleneck analysis of the ⁴He leg — measured, and one hypothesis killed

Asked directly why ⁴He is slow and whether it uses `pyhecke_native`.

**It does not use pyhecke_native, and it cannot.** `_chi_worker` calls
`hoefsmit_numpy.chi_numpy` — a numpy f64 kernel. The wheel does export exactly
the right-shaped function, `chi_lambda_all_partitions_f64` ("χ^λ for every
partition λ ⊢ n_strands ... rayon-parallel"), which would replace the entire
Python pool with one Rust call. It takes a word of `(sign, gen_1based)` with
`sign ∈ {1, -1, 0}`, and the canonical atomic braids use **four** crossing kinds:

    proton     n=11   sigma 6   sigma_inv 3    averaged 2
    deuteron   n=23   sigma 11  sigma_inv 7    averaged 4   averaged_weighted 1
    helium-3   n=35   sigma 18  sigma_inv 10   averaged 6   averaged_weighted 1
    helium-4   n=47   sigma 23  sigma_inv 15   averaged 8   averaged_weighted 1

`averaged_weighted` has no sign encoding, and `canonical_braid_crossings.py`
already says so in as many words: *"⚠ Lossy for `averaged_weighted`, by
construction. A sign cannot [express it]"*. One crossing out of 47 — but it is
an interface crossing, so it carries physics. **The native kernel is not a
drop-in here without extending the Rust word encoding.**

### What the cost actually is

Measured `chi_numpy` on the ⁴He braid:

    dim 1925 →  7.1 s        dim 3520 → 30.4 s     ⇒  cost ~ dim^2.4
    largest λ of 12 is (5,3,2,1,1), dim 7700       ⇒  ≈ 200 s for that one λ
    77 partitions, total dimension 140,152; the top 8 carry 31% of it

So ~20 minutes of single-core work, irreducibly, on this kernel.

### Hypothesis killed: it is NOT memory

Dense f64 at dim 7700 is 474 MB, and four workers holding one each is 1.9 GB —
which looks alarming and is not the problem. The box has **16 GB with 15 GB
free and no cgroup limit**. Checked before theorising.

### What it actually is — two compounding scheduling faults

**1. BLAS oversubscription.** numpy is built on scipy-openblas, which defaults
to one thread per core, and the producer forks four workers: 4 x 4 = 16 runnable
threads on 4 cores. Measured, 4 partitions of dim ≈ 2100 through a 4-worker pool:

    BLAS threads unset : 25.4 s
    BLAS threads = 1   : 18.6 s        1.37x

**2. Load imbalance.** `pool.map`'s default chunksize splits 77 λ into ~4
contiguous blocks, and cost varies by three orders of magnitude across them.
Observed worker CPU on the abandoned run: **11m51s / 4m35s / 1m35s / 0m00s** over
2h05m wall — one worker carrying the run, one never scheduled any real work.

### Applied

  * BLAS thread pinning via `os.environ.setdefault` at the TOP of the module,
    before anything loads numpy — OpenBLAS reads these at library load and a
    fork inherits the loaded library, so setting them inside the worker is too
    late. `setdefault`, so a deliberate operator export still wins.
  * Longest-processing-time-first ordering (Specht dimension as the proxy) with
    `chunksize=1`, then un-permuting back to `parts` order.

**The un-permute is the risk this introduces** — the per-λ loop indexes
`chi_values[i]` against `parts[i]`, so a reordering bug would silently pair the
wrong χ with the wrong λ. Verified on n=6 (11 partitions, non-trivial
permutation): **11/11 identical** to the un-reordered path.

### Honest accounting of the speedup

The 1.37x from thread pinning is measured. The LPT/chunksize gain is **not** —
by construction it only shows on the heterogeneous full set, and measuring it
means running the 20-minute job. The imbalance it targets is evidenced by the
worker-CPU spread above, not by a before/after. Do not quote a combined figure.

### Remaining options, if this is still too slow

  * **Extend the native kernel** to encode `averaged_weighted` — much the
    biggest win (Rust + rayon over partitions) and a real cross-language change.
  * **Sparse path.** `threerow_chi_sparse.chi_atom_sparse` already exists and was
    written for precisely this shape: keep the Hoefsmit matrices CSR and
    accumulate the trace column-batch by column-batch, O(L·dim²) instead of
    O(L·dim³), memory O(dim·B). Its docstring calls the dense identity at
    dim 7700 out by name.
  * **The chi cache.** `chi-helium-4-h12-at-q0-50dps.witness.json` exists but is
    flagged `partial`; this producer never consults it, unlike
    `habiro_coefficients_atomic`, which takes an `atom_cache_label`.

## The ⁴He leg CANNOT run on a 16 GiB box — and three corrections to my own analysis

**Correction 1: it IS memory.** I wrote "Hypothesis killed: it is NOT memory"
above, on the strength of `free -m` showing 15 GiB available. That measured the
idle state, not the peak, and it was wrong.

**Correction 2: my load-balancing fix caused an OOM.** Longest-processing-time
ordering is right for balance, but it also puts the four LARGEST partitions in
flight at once. The previous block-chunked schedule never hit the ceiling only
because it happened to stagger them. First OOM:

    Killed process 23356  anon-rss:5263136kB          (4 workers, ~5 GiB each)

**Correction 3: the peak is 3x what I first recorded.** I took 5.0 GiB from
`ps` on a worker that was *about to be killed*, i.e. one that had not finished
growing, and built a `84 bytes/dim²` model on it. A single SERIAL process on
(5,3,2,1,1), dim 7700, actually peaks at **15.9 GiB**:

    Killed process 26199  anon-rss:15884144kB          (1 worker)

≈ **268 bytes/dim²**, ~33 dense dim×dim f64 matrices resident at once. Read the
peak off the OOM line's `anon-rss`, never off `ps` mid-flight.

So ⁴He at n=12 does not fit at ANY worker count on 16 GiB. This is an
environmental limit, not a scheduling one. The committed witness's
`compute_wall_sec = 2533.2` was produced on a larger machine.

## What the producer does now

  * **BLAS threads pinned** at module scope before numpy loads (measured 1.37x;
    worker state went `Sl`→`R`, ~14% → ~97% utilisation).
  * **Worker count derived from `MemAvailable`** and the largest λ scheduled —
    adaptive, so n=9 legs still use all 4 cores (0.0 GiB/worker) and only n=12
    is capped.
  * **Refuses rather than attempts** when not even one process fits, recording
    `skip_insufficient_memory` with the required/available bytes.
  * **Carry-forward on BOTH write paths.** The incremental save used to
    overwrite `per_atom` with whatever the run had reached, so an interrupt
    destroyed committed atoms — the `ground-state` defect again, and the reason
    this witness was gutted three times today. Now a run preserves atoms it did
    not reach, and a `skip_*` result does NOT displace a committed one.

That last one took three attempts to get right, and the two failures are worth
recording because they are both plausible-looking half-fixes:

    keyed on label only    -> the skip STUB counted as "have it" and overwrote
                              the committed entry: 77 per_lambda rows replaced
                              by a 5-field stub. Quieter than dropping the atom,
                              exactly as much data gone.
    guarded only the       -> `_save_incremental` preserved ⁴He correctly on
    incremental saves         every intermediate write, then the FINAL
                              `builder.save()` — a separate WitnessBuilder that
                              never read the disk — overwrote it anyway.
                              A guard applied on all but the last write is not
                              a guard.

## Why the regenerated witness is NOT committed

With ⁴He preserved and the other three timings drained, the ratchet goes GREEN
(rho-k 4 → 1 raw float64 against a baseline of 3, i.e. a drain; 0 NEW,
0 REGRESSED). It would have closed the one red holding §4b for everyone.

**The witness shape guard flagged it, correctly, and I did not override it.**
`durationMs` collapses 2,552,837 → 794: the file would carry ⁴He's real 77-row
`per_lambda` block, computed over 2533 s, while advertising a 794 ms run. The
content is intact — that part the guard's heuristic misreads — but the result is
a hybrid that reads as a complete fresh run and is not one. `--accept` exists for
intended shrinks and would have made it green in one flag.

Publishing that to close a gate is the same move as widening a baseline. The red
is honest; the hybrid would not be.

## What is actually needed

Run `rho_k_co_casimir_extended.py` on a host with **≥ 24 GiB** free (15.9 GiB
peak plus headroom). The producer is now safe to run anywhere: on a small box it
skips ⁴He and preserves the committed block rather than destroying it. On a big
one it recomputes everything and the ratchet closes.

Cheaper alternative, if a big box is not available: port this producer to
`threerow_chi_sparse.chi_atom_sparse`, which keeps the Hoefsmit matrices CSR and
accumulates the trace column-batch by column-batch — O(dim·B) memory instead of
O(dim²). Its docstring calls out the dense identity at dim 7700 by name; it was
written for exactly this wall.

---

## 2026-08-15 (later) — regeneration is not merely SLOW, it restates the science

Appended rather than filed separately: the entry above already establishes the
red (rho-k 3 → 4, all `per_atom[i].compute_wall_sec`, producer fixed by
`29b209ce9`, witness never regenerated) and that regeneration was abandoned on
**performance** grounds — 2h05m, workers at 9.9/3.7/1.3/0.0 % CPU. This adds a
second, independent reason not to run it as hygiene, found while draining the
last gating red after `qou-pgdw` / PR #5141 landed.

**Two recorded upstream witnesses have drifted** since the committed rho-k was
computed:

- `canonical-mass-table-extended` — `86b861f6…` → `aa62e686…`
- `y-lambda-wenzl-bridge-symbolic` — `f289cd26…` → `690a3f6e…`

So a re-run does not merely refresh timing metadata; it **restates the Δ_λ
science**. Measured on three of the four atoms (~20 s by skipping ⁴He):

| atom | `abs_tr_M_at_q0` | `rho_K_pred_co_casimir` |
|---|---|---|
| deuteron | 0.38829 → 0.57509 | 9464.88 → 6390.44 |
| tritium | 0.10407 → 0.22931 | 52978.84 → 24044.14 |
| helium-3 | 0.20658 → 0.40377 | 26677.80 → 13649.10 |

`err_ppm` moves only in the 5th significant figure (67.5614 → 67.5677,
8.0768 → 8.0775, 12.7705 → 12.7716). Intermediates restated ~2× while the
conclusion holds — the signature of an upstream **normalization / convention
change** (the convention-D cascade), not a numerical error.

**Consequence for ownership.** Even on a big box where the ⁴He leg completes,
this must not land as a float64-drain commit: it would hide a ~2× intermediate
restatement behind a hygiene banner, and it would pass every gate while doing
so. The refresh belongs to the **Δ_λ / convention-D arc**, where that shift
gets reviewed as science.

**Two measurement notes**, both corrections to first readings:

- The fast and slow chi paths agree **exactly at 60 digits**. An initial read of
  `6390.4406431251356` as float64-degraded was the console table's truncation,
  not the witness.
- `--atoms <subset>` overwrites the **whole** witness with only that subset —
  the same gutting mode this bean's incident note describes, reachable without
  any git operation at all. Reproduced locally and restored each time. Any
  refresh must be a single FULL run, and must confirm **both** gates afterwards:
  raw-float64 → 0 **and** shape intact (6 `per_atom` entries, `durationMs`
  ≈ 2.5e6). A zero with a small `durationMs` is a partial write, not a drain.

No carve-out is proposed: `F64_INTEGRATOR_TIER` would be wrong here, since
these are wall-clock diagnostics rather than integrator output.

---

## Cross-check from another session: the stated RED condition no longer holds

Not changing this bean's status — it is not mine — but the headline is stale
enough to mislead a reader deciding whether to act.

Measured on `main` @ `7a781b494b7`, 2026-08-19:

    witnesses carrying raw float64 : 1539
    baseline files / fields        : 1572 / 536,570
    drained since baseline         : 48 file(s), +4,264 field(s)
    NEW dirty witnesses            : 0
    REGRESSED (count increased)    : 0

So `--strict` is green: the "18 NEW + 2 REGRESSED" in the title is no longer
the state of the tree. The three witnesses named in §"The finding"
(`qborel-growth-budget-probe`, `cauchymul-order-cancellation-witness`,
`c3-w2-c1-pole-divisor`) are no longer reported.

Two gates that did not exist when this was opened now cover adjacent holes and
are worth knowing about before re-opening it: `witness_shape_guard.py`
(blocking — a gutted witness scores zero raw floats and reads as a perfect
drain, which this ratchet cannot distinguish) and
`numpy_mpmath_dtype_leak_audit.py` (blocking, green).

Still genuinely uncovered: `docs/audits/scripts/`, where the ratchet runs
ADVISORY only and carries 6 dirty witnesses — tracked as `qou-irzg`.
