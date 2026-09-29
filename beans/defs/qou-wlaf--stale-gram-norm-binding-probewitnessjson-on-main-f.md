---
# qou-wlaf
title: 'STALE: gram-norm-binding-probe.witness.json on main fails its own cross-check assertion by 7 orders of magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T16:43:22Z
updated_at: 2026-09-06T09:20:57Z
---

MEASURED 2026-08-25, branch `claude/gram-norm-threshold-investigation-v8ck94`.

## What is stale

`computations/probes/gram-norm-binding-probe.witness.json` as committed on
`main` does not reproduce from today's code, and it is wrong by far more than a
rounding difference. Against the independent 50-dps transfer engine
`tr_m_atom_via_transfer.tr_m_atom_zn` — which is the very cross-check the probe
itself asserts on:

    iso    field      engine (50 dps)   committed witness   rel err
    2H     tr_atom      0.5751722439      0.3883571887       3.25e-01
    2H     tr_free      1.1317169043      0.9835261820       1.31e-01
    3H     tr_atom      0.2293101021      0.1040710693       5.46e-01
    3H     tr_free      1.1178462290      0.9080241198       1.88e-01
    3He    tr_atom      0.4037670369      0.2065784751       4.88e-01
    3He    tr_free      1.2966756122      1.0477565676       1.92e-01

Everything derived from those moves with them: `G_atom`/`G_free` 5-12 %,
`B_sym` ~27-28 %, `B_gram` up to 49 %, `R_abs`/`R_signed` 6-33 %.

## It fails its OWN assertion, which is what makes this unambiguous

The committed witness records

    linear_trace_matches_transfer_engine   computed = 5.77e-15   tol = 1e-8   passed

so the cross-check held when the file was written. Recomputing that same
assertion against the committed numbers today gives **3.2e-01** — seven orders
of magnitude outside the witness's own stated tolerance. This is not a judgement
call about staleness heuristics; the artifact contradicts itself.

## Not caused by the float64 coercion committed on this branch

The `_letters` float64 coercion (see `qou-9ohz`) was verified at ²H to agree
with the object-dtype path to **9e-16** relative — the float64 floor. It cannot
produce a 5-100 % move. The freshly recomputed values agree with the 50-dps
engine to ~1e-9 and the probe's assertions pass.

## Probable cause, and the part that is NOT established

The committed witness records `wall_sec` of **0.71 s for ³H** — matching the
module docstring's "A <= 3 (n <= 9, instant)" and matching the 0.5 s measured
after the coercion fix. A session on 2026-08-24/25 measured **>2131 s** for that
same isotope on unmodified code. So between the witness being written and now,
`atom_braid_word_3A` began emitting `mpmath.mpf` coefficients — which is correct
for the word under the NO-FLOAT64 discipline, and which simultaneously (a) moved
these numbers and (b) turned this probe's matmuls into object dtype (1.8e4x).
One upstream change, both effects.

**Not established:** exactly which commit did it. Agent clones here are shallow
— `git log` on `mass_at_3A_proper.py`, `wedderburn_jones_markov.py` and the
witness all return only the single merge `fed69b1c4`, so the drift cannot be
dated from this checkout. Do not assert a commit without fetching real history.

## Done on this branch

Witness regenerated (all four isotopes, `--with-4he`) under the fixed probe.
Both assertions pass: `linear_trace_matches_transfer_engine` = 6.03e-15 against
a 1e-8 tolerance, and reversal invariance 5.17e-16 against 1e-10.

Wall times, regenerated vs committed: ²H 0.02 / 0.01, ³H **0.45 / 0.71**,
³He 0.42 / 0.62, ⁴He **418 / 1169** s.

**Raw-float64 field count is 248, i.e. FLAT against the 248 in the baseline —
it does not drain.** (An earlier note of mine said "248 -> 148, drains"; that
148 was a three-isotope run without `--with-4he` and comparing it to the
four-isotope baseline was not a like-for-like comparison. Corrected here.) The
repo ratchet reports `REGRESSED (count increased): 0`, so this change is
ratchet-neutral, not ratchet-draining. Draining it would mean carrying `mpf`
through serialization, which this probe cannot do while its seminormal operand
is float64 — the same open item as above.

## What this bean is still for

The sibling question nobody has answered: **which other witnesses were produced
by consumers of `atom_braid_word_3A` before it was mpf-ified, and are therefore
stale in the same way?** The generic staleness triage keys on `scriptHash` of
the producer, and this class is invisible to it — the producer file is unchanged;
a *dependency* changed. That is the import-cone drift case AGENTS.md flags as
"the one that actually bites". The count is unmeasured. Do not assume it is 1.


---

## Blast radius MEASURED (2026-08-25) — bounded, and the cheap triage route is closed

The section above said the count was unmeasured. It is now bounded, though not
resolved.

**Upper bound: 106 witnesses.** Of 3088 `*.witness.json` scanned, 106 record a
top-level `scriptFile` whose stem is one of the **153** scripts that genuinely
*import* `atom_braid_word_3A` / `per_generator_V_hat_3A` (AST-checked imports,
not name mentions; `_deprecated/` excluded). Largest contributors:
`compute_atom_chi_rust` (4), `bar_pairing_binding_observable` (3),
`binding_production_route_C_vs_D_probe` (3),
`binding_sum_C_vs_D_per_isotope_probe` (3), `atomic_tr_m_mpfr_50dps` (2),
`rho_k_markov_multiplicativity_probe` (2), `markov_peel_atomic_witness` (2).

**106 is an UPPER BOUND on a SUBSET, and three gaps make it neither.** It counts
only *direct* importers — transitive ones are missed entirely; **490** of the
3088 witnesses record no `scriptFile` at all and are invisible to this method;
and being emitted by an importer does not imply the number moved. Do not quote
106 as a stale count.

**The cheap triage route is closed — this is the actionable finding.** The
gram-norm case was settled without re-running anything, by comparing a stored
`tr_atom`/`tr_free` against the independent 50-dps `tr_m_atom_zn` engine. Of the
106, **exactly 1 carries a comparable trace field: the gram-norm witness
itself.** So the other 105 cannot be adjudicated from stored data — each needs
its producer re-run. That is why this is a bean and not a PR: it is a
long-compute campaign, not a scan.

**Detector caution, recorded because it will bite the next person.** The first
pass of this measurement returned **0** — it looked for `d["witness"]
["scriptFile"]`, but provenance in these files is at **top level**
(`d["scriptFile"]`), so the nested lookup found nothing and read as a clean
tree. Caught only by asserting the known positive was detected. Any re-run of
this measurement must self-test against `gram-norm-binding-probe.witness.json`
before its count is trusted.


---

## A SECOND instance of this class, and it points the other way (2026-08-25)

Raised by the sibling on [#5763](https://github.com/litlfred/qou/pull/5763),
who asked twice for it to be folded in here. It belongs: same shape as the
gram-norm case — a committed witness disagreeing with a fresh recompute of its
own producer — but with the sign reversed, and on a more consequential file.

`computations/witness-raw-float64-audit.witness.json` is the witness that
**reports the raw-float64 gate itself**. Its committed copy on `main` recorded

    dirty_witnesses: 1288    total_fields: 258324

while the live audit on that same tree reported **1293 / 258420, NEW 5** —
the difference being exactly the five undrained witnesses (1293−5 = 1288).
So the committed witness was recording the **drained** state while the tree
was still undrained.

**That is the dangerous direction.** A stale witness that *overstates* a
problem costs one wasted pass. One that *understates* it hides a live gate
failure: anyone reading that file instead of running the audit would have
concluded the ratchet was clean when it was red.

**Re-measured here after #5763's drain merged (`6137e6244`):** `dirty_witnesses`
is now **1288 live**, so the count dimension has resolved — not because the
witness was corrected, but because the **tree caught up to what the witness
already claimed**. Worth stating plainly, since "it agrees now" is a much
weaker fact than "it was right all along". `total_fields` still does not
reproduce: committed **258324** vs live **258188**, a 136-field gap in the
overstating direction now. The file is closer to correct than it was and is
still not a reproduction of the current tree.

**Why this matters for the method, not just the file.** The gram-norm instance
was found because its own recorded assertion contradicted a fresh recompute.
This one has **no `environment` block and no assertions at all** — keys are
`schema`, `name`, `description`, `data` — so the self-contradiction test that
caught gram-norm cannot see it. It was caught only because a human-directed
agent happened to run the audit and compare. Any systematic sweep for this
class needs a producer re-run and a field diff, which is the same conclusion
the ≤106 measurement above reached from the other direction.


---

## Reproduced on this branch, within hours — the class is not rare (2026-08-25)

The strongest evidence for this bean is that its own fix went stale while it
was being written.

The regenerated `gram-norm-binding-probe.witness.json` committed earlier on
`claude/gram-norm-threshold-investigation-v8ck94` recorded

    2H  G_atom = 4.922708485093256

Then the branch was rebased onto `main` at `41389ea6bf`, picking up 29 commits
(the convention-C / B4 migration series, the `fmt()`-padded q0 literal fix, the
`build_seminormal_matrices_mp` addition). Re-running the **identical producer**
on the **identical source** now gives

    2H  G_atom = 4.92270711355717        rel shift 2.8e-7

The producer file did not change. Its recorded `scriptHash` did not change.
Nothing in `scriptHash`-keyed staleness triage can see this. An upstream input
moved, and a freshly-committed witness became a stale one in the time it took
to rebase.

**How it was isolated, because the first three hypotheses were all wrong and
each is worth ruling out cheaply next time:**

  * *Convention-C leak in the symbolic y_λ path?* **No.** `y_lambda_at(n,
    q_val=None)` (symbolic, substituted at 55 digits) and `y_lambda_at(n,
    q_val=float(Q0))` (numeric) agree to **0.000e+00** across all 11 partitions
    of 6. Raised because the excised-C history makes it the obvious suspect;
    dropped because it measured clean.
  * *The two seminormal builders disagreeing?* **No.** `build_seminormal_
    matrices` vs `build_seminormal_matrices_mp` over every σ, every entry, all
    partitions of 6: max absolute deviation **3.331e-16**. This independently
    confirms the 4.441e-16 figure the `_mp` author reported.
  * *A bug in the probe's own `_gram_and_trace`?* **No.** Same process, probe
    function vs a hand-rolled loop with dense identity and the same coercion:
    **0.000e+00** on both G and T.

Only after all three came back clean did the rebase become the remaining
explanation, and it is confirmed by the value moving with nothing local
changed.

**Two consequences for how this bean should be worked.**

1. **The ≤106 measurement above is a snapshot, not a standing count.** Any of
   those witnesses can go stale on any merge that touches the import cone. A
   campaign that re-runs 105 producers over days will have its early results
   staling behind it. Re-runs must be pinned to a single `main` SHA and the SHA
   recorded, or the campaign chases its own tail.
2. **A witness cross-check assertion is not enough on its own.** This probe's
   `linear_trace_matches_transfer_engine` passed at 6e-15 both before and after
   the shift, because it validates `T`, not `G`. `G` — the quantity the probe
   exists to measure — is cross-checked by nothing, which is why a 2.8e-7 move
   in it was silent. Worth checking, per witness, WHICH fields the assertions
   actually cover before trusting an `allPassed: true`.


---

## RETRACTION: the "reproduced on this branch" section above is WRONG

The section headed *"Reproduced on this branch, within hours"* claimed that
rebasing onto `main` at `41389ea6bf` shifted this probe's `2H G_atom` from
`4.922708485093256` to `4.92270711355717`, and presented that as this bean's
own thesis reproducing itself. **It is not true and it is withdrawn.**

Measured properly: two independent full `--with-4he` runs, hours apart, at
different CPU loads, one with nothing else on the box. Every field of every
isotope is **bit-identical** to the committed witness — `G_atom`, `tr_atom`,
`B_sym`, `r_gram_sym` across ²H, ³H, ³He, ⁴He, all `rel = 0.00e+00`. The
producer is reproducible post-rebase. The committed witness is correct.

**Where 4.92270711355717 came from: my own test harnesses, not the producer.**
Every reading of that value came from a script that did
`sys.path.insert(0, 'probes')` and then `import gram_norm_binding_probe`,
executing the module under a different import context than
`python3 probes/gram_norm_binding_probe.py` gives it — a tree with
`_path_bridge` doing its own `sys.path` surgery. The harness and the producer
resolve their sibling imports differently, so the harness was measuring a
slightly different object and reporting it as the producer's value. I have not
isolated which import differs, and am not claiming to.

Note the trap in the corroboration: my "same process, `main()` and a direct
call agree exactly" test **also** ran under the harness context, so both sides
shared the same wrong context and agreed with each other. Two numbers agreeing
is not evidence when they are wrong together.

**What survives, and is worth more than the retracted claim.** The three
exonerating measurements were real and stand: symbolic vs numeric `y_λ` agree
to `0.000e+00` (no convention-C leak); `build_seminormal_matrices` vs
`build_seminormal_matrices_mp` agree to `3.331e-16` (independently confirming
the `_mp` author's 4.441e-16); the probe's `_gram_and_trace` matches a
hand-rolled loop. And the two consequences recorded in that section hold on
their own merits regardless of the retracted premise: a re-run campaign should
still pin one `main` SHA, and `allPassed: true` is still no comfort when the
assertion validates `T` while the quantity of interest is `G`.

**The lesson is the one this repo already writes down: measure the producer as
producers actually invoke it, or you measure your own harness.** That is the
second time in this session — the first was a detector reading a nested
`witness.scriptFile` and reporting 0 on a tree with a known positive in it.
Both were caught only by checking against something already known to be true.
For a producer, "run it the way the manifest runs it" is the check.

The ORIGINAL finding of this bean is untouched by all of this: the witness on
`main` before this branch disagreed with the 50-dps transfer engine by 13-55 %
and failed its own recorded assertion by seven orders of magnitude. That was
measured from committed data, not from a harness.



---

## The gate is GONE — the residue is runnable now (2026-08-25)

This bean and PR #5775 both say the 105-producer re-run campaign should wait on
`qou-9ohz`'s `per_generator_V_hat_3A` scalar collapse, so the producers do not
each pay the 1.8e4x object-dtype penalty during the very campaign meant to
re-run them.

**That patch is already on `main`** and has been for some time; I checked the
wrong way and reported it missing three times. Measured today:
`per_generator_V_hat_3A(1, 2)` (3H, A=3) returns in **0.21 s**, against the
2.5 h+ the unpatched path took. Details and the two rules I drew from missing
it are in `qou-9ohz`.

So there is no gate. The campaign is runnable, and the discipline recorded
above still applies to it in full: **pin one `main` SHA and record it** (the
<=106 list stales on any cone-touching merge), self-test any detector against
`gram-norm-binding-probe.witness.json` before trusting a count, restore the
whole `computations/` tree between runs because producers write sibling
witnesses, capture stdout as well as stderr, and check for a traceback rather
than trusting an exit code — several producers in this corpus refuse by design
and explain themselves on stdout.


---

## Campaign attempt 1: STOPPED, harness not trustworthy (2026-08-25)

Built and launched the re-run campaign now the gate is gone. Stopped it after 5
of 95 producers because it produced a verdict I could prove wrong, and I am not
reporting counts from a harness with a known false positive.

**What is solid and reusable:**

  * **Pinned SHA `f6501fba549591122523ebb76ce118e49a7003e1`**, recorded in the
    output, per the discipline above.
  * **Target list re-measured: 114 witnesses over 95 distinct producers**, from
    153 AST-verified importers. The detector **self-tested against
    `gram-norm-binding-probe.witness.json` and passed** before any count was
    used.
  * **114, not 106.** The list GREW by 8 in the hours since the snapshot above.
    That is direct confirmation of the caution recorded there — the count is a
    snapshot, not a standing figure — and it is why the SHA pin matters.

**The defect.** The runner classified
`atom-braid-active-partitions.witness.json` as MOVED. It has not moved:

  * flattened leaf-by-leaf comparison of the git baseline against a fresh run:
    **0 differing fields**;
  * the runner's own `strip()`-then-compare, executed standalone on that same
    pair: **`strip equal? True`**.

So the identical comparison says IDENTICAL outside the loop and MOVED inside
it. The cause is **not isolated** — candidates I could not separate before
stopping include the restore/compare ordering relative to sibling-witness
writes by the *previous* producer, and the runner's two-`cwd` retry. Do not
assume it is one of those; measure it.

**Verdicts observed before the stop (NOT to be quoted as results):** 4 MOVED,
1 IDENTICAL over 5 producers. At least one of those 4 is a false positive.

**For the next attempt.** Use the flattened-leaf comparison, which is the one
verified correct against a known case, and give the runner a **self-test on a
known-IDENTICAL producer** — the same shape as the detector self-test that did
work. A runner that cannot demonstrate it reports IDENTICAL for a witness
known not to move has not been validated, only run.

Scripts left at `/tmp/residue_campaign.py` (targeting, self-tested, sound) and
`/tmp/residue_run.py` (execution, **defective as described**). The targeting
half is worth keeping; the comparison half needs replacing, not patching.

This is the third harness-measurement error in this session, after the nested
`witness.scriptFile` detector and the import-context retraction above. The
pattern is consistent enough to state as a rule: **in this corpus, validate the
measuring instrument against a known answer before believing any count it
produces** — and validate it in the loop it will actually run in, not
standalone, since that is precisely where this one diverged.


---

## Attempt 2: instrument VALIDATED, campaign partial (8/95), and one structural fix outstanding

Attempt 2 fixed what attempt 1 got wrong. The in-loop self-test
(`atom_braid_active_partitions`, verified by hand not to move) **passes**, so
these verdicts are trustworthy in a way attempt 1's were not.

Getting there took two more masks, each named by the self-test rather than
found by another sweep:

  * **`.engineVersion`** — an environment artifact, the class flagged on #5763.
    This alone accounted for attempt 1's false MOVED.
  * **`bridge_elapsed_sec`, `python_hoefsmit_elapsed_sec`,
    `rust_canonical_chi_elapsed_sec`** — wall-clock fields the exact-name mask
    missed because they are SUFFIXED. Masking is now suffix-aware, for timing
    keys only.

The mask stays narrow on purpose. `.assertions[].source` embeds a **computed
number** (`"max|chi_comb-chi_young|=5.9119161e-48 < 1e-25"`), so masking it
would hide true positives — the worse failure of the two.

### Result so far — and "MOVED" is the wrong granularity

    processed        8 of 95
    IDENTICAL        3
    MOVED            4     ->  substantive 3, provenance-only 1
    TIMEOUT          1     (180 s budget; says nothing about the witness)

**`atomic_tr_m_mpfr_50dps` moves in `.scriptHash` ONLY.** No number changed —
that is provenance drift, not stale content, and it must not be counted
alongside a witness whose values moved. Report this axis three ways
(substantive / provenance-only / identical), never as a bare MOVED count. The
recorded per-witness `fields` make the split computable from the checkpoint
without re-running anything.

Three of eight moving substantively is a real signal that the class is not
rare, but **8 is far too small a sample to extrapolate to 95** and no rate
should be quoted from it.

### Structural fix still needed: do not sweep in the working tree

The campaign was stopped early because it **dirties the working tree**. It
restores `computations/` between producers, but at any instant the tree
carries whatever the running producer wrote — including
`witness-raw-float64-audit.witness.json`, an audit witness that
[`b28296c0d`] already had to revert once for being swept in accidentally.

Restoring mid-run is not a fix either: it would hand the currently-running
producer a restored baseline and could manufacture a false IDENTICAL.

**The next run should execute in a `git worktree` or a throwaway clone**, so
the sweep cannot touch the session's tree at all. That removes the dirty-tree
problem and the contamination risk together, and it is the reason this
attempt stopped at 8 rather than a defect in the instrument.

Harness committed at `computations/audits/witness_dependency_residue_{targets,run}.py`
with the pinned-SHA and self-test discipline built in.


---

## Field re-audit of every MOVED_SUBSTANTIVE — all 8 hold (2026-08-26)

Three false MOVEDs had already been traced to volatile fields the mask did not
anticipate (`engineVersion`; `*_elapsed_sec`; `elapsed_*_sec`). Since the
instrument's only observed failure mode is over-reporting, the surviving
verdicts were re-audited field-by-field rather than trusted.

**All 8 survive.** The moved fields are the framework's own computed
quantities, not provenance and not wall-clock:

  * Markov traces — `tr_M_atom`, `tr_M_free`, `tr_M_D`, `markov_trace`,
    `trM_combiner`, `trM_transfer`, `tr_bound`, `tr_free`
  * binding energies — `B_MeV`, `B_single_link_MeV`, `delta_m_over_m_pct`,
    `delta_tr_per_bond`
  * symbolic results — `polynomial_q`, `coeff`, `value_at_q0`, `difference`
  * masses — `m_atom_per_irrep_total`, `m_free_per_irrep_total`

So committed witnesses on `main` record trace and binding values that do not
reproduce from today's code. That is the finding this bean exists for, now on
8 producers rather than the 1 it started from.

**The audit's own screen produced two false positives, by the same bug it was
looking for.** A regex for volatile-looking names flagged
`alpha_k_times_delta_phi` (matched "time" inside *times*) and
`delta_tr_h3a_direct` (matched "dir" inside *direct*). Both are physics
quantities. Substring matching where word matching was meant — precisely the
error that let `elapsed_reduce_sec` through the mask, committed again one
layer up in the tool built to catch it. Neither reached a verdict, because the
screen only nominates for human reading, but a version that auto-excluded on
that regex would have silently dropped two real findings.

Worth keeping as the standing caution for this axis: **a MOVED verdict is only
as good as the mask, and must be read with its field list attached.** The
counts are not self-supporting.


---

# RESULT (partial, and landed deliberately before the sweep completes)

Pinned to `main` at `f6501fba549591122523ebb76ce118e49a7003e1`. 21 of 95
producers measured. Recorded now rather than held, because the finding does
not depend on the remaining 74 and the sweep advances roughly one producer per
container lifetime.

    MOVED_SUBSTANTIVE       8
    MOVED_PROVENANCE_ONLY   1
    IDENTICAL              10
    TIMEOUT                 1   excluded — a budget artifact, not evidence
    CRASH                   1   excluded

**No rate is claimed.** 21/95 is under a quarter of the population and the
tail is not known to resemble the head.

## The eight committed witnesses that do not reproduce

Each was field-audited individually (see the re-audit section above); the
moved fields are the framework's own computed quantities, not provenance and
not wall-clock.

    computations/a_operator/a-operator-recursive-a3-h9.witness.json
    computations/atom-nf-symbolic-D.witness.json
    computations/binding-canonical.witness.json
    computations/binding-depth-stratified.witness.json
    computations/binding-per-bond-decomposition.witness.json
    computations/binding-rotation-phase-lead.witness.json
    computations/probes/binding-volume-difference-probe.witness.json
    computations/canonical-with-proper-tower.witness.json

What moved: Markov traces (`tr_M_atom`, `tr_M_free`, `tr_M_D`,
`markov_trace`, `trM_combiner`, `trM_transfer`, `tr_bound`, `tr_free`),
binding energies (`B_MeV`, `B_single_link_MeV`, `delta_m_over_m_pct`,
`delta_tr_per_bond`), symbolic results (`polynomial_q`, `coeff`,
`value_at_q0`), masses (`m_atom_per_irrep_total`, `m_free_per_irrep_total`).

## What this establishes, and what it does not

**Establishes:** the class this bean opened with — a witness stale because a
*dependency* moved while its own producer file did not — is not a one-off. It
holds on at least 8 producers, and it is invisible to `scriptHash`-keyed
staleness triage by construction.

**Does not establish:** *why* each moved, or that the current value is right
and the committed one wrong. A re-run reproduces today's code; it does not
adjudicate which value is correct. Anyone acting on this list must diff the
values and decide, not simply regenerate.

**Deliberately not done here:** regenerating them. That is a separate change
with its own review — eight witnesses carrying trace and binding numbers is
not a drive-by commit, and the 2.8e-7-scale shifts seen in the gram-norm case
are large enough to matter to anything downstream.

## Caveat that travels with these numbers

The instrument over-reports. Four false MOVEDs were caught and removed
(`engineVersion`, `*_elapsed_sec`, `elapsed_*_sec`, and one screen-level
regex slip), every one a volatile field the mask had not anticipated — none a
defect in the comparison itself. **A MOVED verdict is only as good as its
mask and must be read with its field list attached.** These eight survived an
explicit field-by-field audit; any verdict added later deserves the same
before it counts.


---

## CORRECTION: worktree isolation is NOT complete (2026-08-26)

PR #5805 and its commit say a detached worktree "removes the hazard
structurally instead of relying on cleanup". **That is too strong.** It
reduces the hazard; it does not remove it.

Caught by the session's own guard, which is the only reason it did not land:
after a tier-1 sweep run entirely inside `/tmp/residue-wt`, the SESSION tree
showed `computations/witness-raw-float64-audit.witness.json` modified —
`total_fields` 258146 -> 258142, `baseline_fields` 487626 -> 487597,
`drained_files` 913 -> 888. mtime 03:29:52, mid-sweep.

That is the *same file* named in this bean as the b28296c0d
already-reverted-once case, and the same file my own check-in note said to
watch for exactly this reason.

**Why a worktree does not stop it.** `git rev-parse --show-toplevel` correctly
returns the worktree root, so path-resolution by git is safe. Two routes are
not:

  * a hardcoded absolute path — `computations/forward_ref_classifier.py`
    contains a literal `/home/user/qou`;
  * the witness-write path itself, which runs the raw-float64 ratchet inline
    on every witness write (visible as the `⚠ raw-float64:` line producers
    emit), and can write its audit witness outside the tree the producer is
    confined to.

Neither is defeated by choosing a different cwd or a different checkout. Only
a filesystem-level confinement (container, mount namespace, read-only bind)
would actually remove this class.

**Reverted, not committed.** Committing a regenerated audit witness is the
precise mistake b28296c0d had to undo, and the counts here are derived from a
tree being perturbed by the sweep that produced them.

**Consequence for the sweep's results:** none of the verdicts are affected —
they are computed by diffing witnesses inside the worktree against a git
baseline, and this escape only writes one audit witness in the session tree.
But the guard must keep being run: `git status --short | wc -l` in
`/home/user/qou` at every check, treating non-zero as a defect rather than
noise. That instruction was already recorded; this is the first time it fired.


---

## The CRASH bucket is three different things (2026-08-26)

AGENTS.md is explicit that a non-zero exit is not a defect and that a guard
raised as a domain exception is indistinguishable from a crash by shape — the
discriminator is the exception TYPE and its message. Applied to the sweep's
four CRASH verdicts, they are not one class:

**Real defects (2):**

  * `braid_encoding_audit` —
    `TypeError: unsupported format string passed to mpf.__format__`.
    The mpf-formatting class; the same family as the two defects PR #5615
    fixed, so this is a further instance rather than a new kind.
  * `probe_4b_li6_non_rectangular_scan` —
    `TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))`.
    An mpf reaching a numpy/scipy boundary — **the same object-dtype family as
    the gram-norm finding this whole bean started from**, surfacing here as a
    hard failure instead of a 1.8e4x slowdown.

**Environment, not a defect (1):**

  * `difference_knot_binding_probe` — `ModuleNotFoundError: No module named
    'snappy'`. SnapPy is absent from this container. The producer is not
    broken and must not be counted as such.

**A guard doing its job (1), with a caveat worth a look:**

  * `probe_canonical_braid_interface_composition` —
    `ValueError: Unrecognised interface d=-0.104458247769726; expected one of
    {0, -h/2=-0.1045, -h=-0.2091}`. A domain check refusing an unrecognised
    value and naming the expected set: a refusal, not a crash.

    **But note what it is refusing.** The rejected `d = -0.104458…` and the
    expected `-h/2 = -0.1045` agree to four decimals. On its face the guard is
    rejecting a value that may be the one it expects, on an exact comparison
    where a tolerance was meant. Flagging rather than asserting — this needs
    someone to read the guard, and it is out of scope for this bean.

So of 4 CRASH verdicts: **2 real, 1 environmental, 1 a guard.** Reporting "4
producers crash" would have been wrong in three different ways, and is exactly
the over-count AGENTS.md records having made before (14 claimed, 2 real).

**Runner improved so this never needs re-running.** It now records the
exception line in each result, because classifying a CRASH previously meant
re-running the producer by hand. Same reasoning as recording the moved field
names, which has now paid for itself four times.


### RETRACTION of the mechanism above — the worktree never leaked

The section headed *"worktree isolation is NOT complete"* blamed the sweep,
naming a hardcoded `/home/user/qou` in `forward_ref_classifier.py` and the
inline ratchet on the witness-write path as escape routes. **That diagnosis is
wrong and is withdrawn.** Neither was involved.

The writer is `scripts/precommit-precision-warn.sh` — the repo's own
`PreToolUse` hook on `Bash`, wired at `.claude/settings.json:40` and described
in AGENTS.md. It does

    cd "$(git rev-parse --show-toplevel)"
    python3 computations/witness_raw_float64_audit.py --strict

on every commit touching a witness or a `computations/` script. That audit
writes `witness-raw-float64-audit.witness.json` as a side effect, in the
SESSION tree, because that is where the hook runs.

So **my own commits were producing the file I was attributing to the sweep.**
The timing fitted the sweep because the sweep is what I was committing about.

Evidence that settles it: `witness_raw_float64_audit.py` resolves its output
via `Path(__file__).resolve().parent`, so a copy executed from
`/tmp/residue-wt` writes inside the worktree by construction. It cannot reach
the session tree from there. Only the session copy can, and only the hook runs
the session copy.

**What was right and stays:** reverting rather than committing. A regenerated
audit witness is the `b28296c0d` class whatever produced it, and its counts
here are a side effect of a hook, not a measurement anyone requested.

**What was wrong:** the claim that worktree isolation is incomplete. On this
evidence it held perfectly. I over-generalised from one dirty file to a
structural conclusion, and picked two plausible mechanisms without testing
either — the same "reasoned from shape instead of measuring" failure this bean
already records twice.

**Consequence:** the file will reappear on every commit this session makes
that touches `computations/`. That is the hook working as designed, not a
defect and not a sweep escape. Revert it; do not commit it; do not read it as
evidence of anything about the sweep.


---

## The CRASH count over-reports too — narrow PYTHONPATH (2026-08-26)

Same shape as the MOVED mask gaps: the instrument blames the corpus for its
own limitation.

Two of seven CRASH verdicts were `ModuleNotFoundError` on **in-repo** modules —
`char_fast` and `markov_peel`, which exist at `computations/substrate/` and
`computations/markov/`. The runner put only `computations/` on `PYTHONPATH`,
but producers run from their own directory and import siblings by bare name.
Re-run with the subdirectories added:

  * `term5_aK_audit` — exit **124**. Not a crash at all; it is SLOW, and
    belongs in the timeout/budget class.
  * `rho_k_markov_multiplicativity_probe` — gets past the import to
    `FileNotFoundError` on `_deprecated/atomic-tr-m-mpfr-50dps.witness.json`.
    A missing-input problem, not an import failure. Whether that is a producer
    defect or a worktree-checkout artifact is **not established** and should
    not be assumed either way.

So two of seven were verdicts about the harness. AGENTS.md documents this
precise misclassification ("2 needed `computations/` on `PYTHONPATH`"; "1
passed only in isolation, so the runner carried order-dependence") — the
warning was there and the runner still shipped with it.

**Consequence: the CRASH count from the current run is not trustworthy and
must not be quoted.** The sweep in flight was launched before this fix, so its
CRASH verdicts still carry the narrow path. They need re-running before any
crash figure is published. The MOVED/IDENTICAL verdicts are unaffected —
those producers ran to completion, so the path was sufficient for them by
construction.

Fixed: `PYTHONPATH` now includes every non-dotfile, non-underscore
subdirectory of `computations/`.

**Fifth instrument defect, same direction every time.** engineVersion,
`*_elapsed_sec`, `elapsed_*_sec`, a substring screen, and now a narrow
PYTHONPATH — every one made the corpus look worse than it is. That
consistency is itself worth stating: **this instrument's errors are
false-positive errors**, so its counts are upper bounds, and a verdict is only
usable with its evidence attached.


---

## What actually moved — analysis at 78/95 (2026-08-26)

Field-level analysis of the substantive verdicts, from recorded data only (no
re-runs, nothing executed against the in-flight sweep).

### Not every "substantive" move is staleness

Of 34 substantive verdicts, **33 are real value changes** — the committed
value was non-null and differs. **One is a null → value fill**
(`qlommel_b_ladder_slope_derivation`): the committed witness had `q0Value:
null` and today's code records a value. That is main's pin-stamping work
(#5797 / `qou-1c4y`) *adding* provenance, an improvement, not drift. Counting
it as staleness would have overstated the finding by one.

So the headline is **33**, and the distinction is worth keeping: a field going
null → value is provenance being added; a field changing value is the thing
this bean is about.

### The sharpest sub-finding: four witnesses no longer pass their own assertions

`allPassed` / `passed` moved in five witnesses. Four were committed with
`allPassed: True`:

    mu3_abs_choice_robustness_probe
    option_a_vol_per_knot_light_series
    trace_convention_reconciliation
    triangle_bond_submodularity_probe

A boolean that moved from `True` can only have moved to `False`. These are
witnesses that **record their own assertions passing and no longer reproduce
that** — the same self-contradiction that identified the original gram-norm
case, now on four more producers. This is the strongest form of the class,
because it needs no interpretation: the artifact fails a test it says it
passed.

(The fifth, `iterative_lp_dual_h6_deuteron`, was committed `False`, so its
move is in the other direction and is not evidence of decay.)

### `q0Value` moves are a different story and should not be pooled

`q0Value` moved in three. One (`mu3_frechet_perblock_probe`) had a real
committed value, `1.1099785827513804319`, anchor `proton`. Two had `null`.
Given the muon → proton pin migration landing on main, these are plausibly
*expected* consequences of that work rather than independent drift —
**not established either way here**, and deliberately not folded into the
staleness headline.

### Field frequency across the 33

    10  computed        5  allPassed / passed      4  B_AME_MeV
     3  q0Value         2  tr_M_free               2  B_MeV
     2  delta_m_over_m_pct

`B_AME_MeV` is the AME2020 experimental reference, not a framework output; its
movement suggests a reference-table update and is a different question again.

**None of this changes the instrument caveat.** These are upper bounds, read
with their field lists attached.


---

## CRASH triage COMPLETE — 7 verdicts, four different causes

All seven classified. "Seven producers crash" would have been wrong about four
of them.

**Real producer defects (3):**

  * `braid_encoding_audit` — `TypeError: unsupported format string passed to
    mpf.__format__`. The mpf-formatting family PR #5615 fixed twice already.
  * `probe_4b_li6_non_rectangular_scan` — `TypeError: no supported conversion
    for types: (dtype('float64'), dtype('O'))`.
  * `reeb_rotation_pn_test` — `TypeError: ufunc 'isfinite' not supported for
    the input types`.

The last two are **the same object-dtype family as the gram-norm finding this
bean opened with** — an `mpf` reaching a numpy boundary. There it cost 1.8e4x
in wall time; here it is a hard failure. Same root cause, two different
symptoms, and worth noting that the slow variant is the one that hides.

**Environment, not a defect (1):**

  * `difference_knot_binding_probe` — `ModuleNotFoundError: No module named
    'snappy'`. SnapPy is absent from this container.

**A guard working correctly (1):**

  * `probe_canonical_braid_interface_composition` — refuses an unrecognised
    interface value and names the expected set. Caveat still open: it rejects
    `d = -0.104458247769726` while naming `-h/2 = -0.1045`, which agree to four
    decimals. Possibly an exact comparison where a tolerance was meant; needs
    its owner to read it.

**My harness, not the producers (2):**

  * `term5_aK_audit` — with subdirectories on `PYTHONPATH` it reaches exit
    **124**. Not a crash: SLOW.
  * `rho_k_markov_multiplicativity_probe` — reaches `FileNotFoundError` on a
    `_deprecated/` witness. A missing-input question, not an import failure,
    and whether that is a producer defect or a checkout artifact is **not
    established**.

**So: 3 real, 1 environmental, 1 a guard, 2 harness.** AGENTS.md records this
same over-count being made once before at larger scale (14 claimed, 2 real).
The lesson repeats because the failure shapes genuinely are
indistinguishable without reading the exception — which is why the runner now
records it.


### Precision correction to the "four witnesses fail their own assertions" claim

That section says a boolean moving from `True` "can only have moved to
`False`". **Not strictly true, and I cannot settle it from the data I have.**

`allPassed` differing from its committed `True` admits three readings:

  * `True -> False` — the witness now fails its own assertions (the claim as
    stated);
  * `True -> null` — the field is present but unset;
  * the field is **absent** in the fresh run — the leaf comparison flags that
    identically, since it compares key sets.

The runner records which field names moved, **not their values**, so the
checkpoint cannot separate these. Distinguishing them needs a re-run of those
four producers with values captured — deliberately not done while the sweep
is in flight, because running a producer in the shared worktree risks
corrupting the diff of whichever producer the sweep is measuring.

**What survives unweakened:** all three readings mean the committed witness
does not reproduce, which is this bean's finding. Only the *sharpened*
version — "records passing assertions and now fails them" — is unproven, and
it is the version worth having, so it should be settled rather than dropped.

Queued, not concluded: re-run `mu3_abs_choice_robustness_probe`,
`option_a_vol_per_knot_light_series`, `trace_convention_reconciliation` and
`triangle_bond_submodularity_probe` with values recorded, once the sweep is
done and the worktree is free.

Worth noting the runner would have answered this for free had it stored the
before/after values alongside the field names. Recording names was already the
single most useful thing it does; recording values is the obvious next
increment.


---

# FINAL RESULT — sweep complete at 91/95

Pinned to `main` at `f6501fba549591122523ebb76ce118e49a7003e1`. Raw per-producer
verdicts committed alongside this at
`computations/audits/witness-dependency-residue-sweep.results.json`, so the
figures below are checkable rather than asserted.

    MOVED_SUBSTANTIVE      37
    MOVED_PROVENANCE_ONLY   2
    IDENTICAL              31
    TIMEOUT                 9   excluded — budget artifact, not evidence
    CRASH                   9   excluded — triaged separately above
    ------------------------------
    scoreable              70

**37 of 70 scoreable producers emit witnesses whose committed values on `main`
do not reproduce** — a little over half, against the ONE this bean opened with.
Every substantive verdict was screened field-by-field; the moved fields are
Markov traces, binding energies, symbolic results and masses, not provenance
and not wall-clock.

## Three limits that travel with the number

1. **Upper bound, not a count.** Five instrument defects were found and fixed
   during the sweep — `engineVersion`, `*_elapsed_sec`, `elapsed_*_sec`, a
   substring screen, a narrow `PYTHONPATH` — and **every one inflated the
   apparent damage**. None was a defect in the comparison itself. The failure
   mode is consistently false-positive, so 37 is a ceiling.
2. **~19 producers unmeasured, non-randomly.** 9 timeouts, 9 crashes, 4 never
   reached. These are the *expensive* producers, so they cannot be assumed to
   behave like the fast half in either direction.
3. **A re-run establishes non-reproduction, not correctness.** It says today's
   code disagrees with the committed value. It does not say which is right.
   Anyone acting on the list must diff and decide.

## Why it ended at 91 rather than 95

The session's disk allowance was exhausted: the worktree grew 1.1 GB -> **14
GB** and filled the filesystem, after which no command would run at all — even
`echo` failed, because the harness writes an output file before executing
anything. Recovered via the `CLAUDE_CODE_TMPDIR` redirect the ENOSPC message
names, which let one command through to delete the worktree.

Two things worth recording for the next long sweep here:

  * **A worktree used for producer runs is not size-stable.** It grew 13x.
    Whatever the sweep restores between producers, something accumulates.
    Budget for it or bound it.
  * **My "checkpoint secured" claim during the emergency was false.** The `cp`
    ran under ENOSPC and produced a **0-byte** file; I reported it as secured
    without verifying. The real data survived only because the live checkpoint
    happened to sit outside the worktree — luck, not the precaution I claimed
    to have taken. Verify a backup by reading it back, especially when the
    reason you are taking it is that the disk is failing.


## RESOLVED — the four `allPassed` witnesses: confirmed `True -> False`

Earlier in this bean I recorded the assertion finding and then **softened
it**, because `allPassed` differing from its committed `True` admits three
readings — `True -> False`, `True -> null`, or the field being **absent**
from the fresh witness entirely. Only the first is the interesting claim,
and the sweep's field-level diff could not distinguish them: it records
*that* a field moved, not what it moved to.

Measured directly, in the session tree (safe once the worktree was gone),
each producer re-run with `PYTHONPATH` covering every `computations/`
subdirectory, against the git baseline at
`f6501fba549591122523ebb76ce118e49a7003e1`:

    mu3_abs_choice_robustness_probe      committed True  -> fresh False
    option_a_vol_per_knot_light_series   committed True  -> fresh False
    trace_convention_reconciliation      committed True  -> fresh False
    triangle_bond_submodularity_probe    committed True  -> fresh False

All four. Not null, not absent — **False**.

So the sharpened claim now stands: **four witnesses committed on `main`
record their own self-assertions passing, and those assertions now fail.**
A producer that writes `allPassed` is stating that its internal
cross-checks agreed at the moment of writing; the committed artifact says
they did, and today they do not. That is a strictly stronger finding than
"a number moved" — a moved number needs someone to adjudicate which value
is right, whereas a failed self-assertion is the producer's own verdict on
itself.

Tree reverted clean afterwards (`git status --short` empty); no witness
regenerated into the commit.

This is the one claim in this bean I had explicitly queued as
*not established*. It is now established.


## CORRECTION — the CRASH bucket holds FIVE real defects, not three

I reported *"3 real defects, 1 environment, 1 guard, 2 harness artifacts,
2 other"*. The "2 other" were `probe_4c_li6_large_d_scan` and
`probe_4f_h3_sigma_avg_asymmetry`, and they are **the same defect as the
three I did name** — an `mpmath.mpf` reaching a float64-only consumer.

Found by checking the whole `probe_4*` family against the committed
results rather than only the producers I had already opened. All five
consumers route `atom_braid_word_3A`'s word through the same
`apply_T_w`, and three of them die at the identical line.

Both halves measured per producer, never inferred from family membership:

    producer     pre-fix (HEAD~3)          post-fix
    probe_4b     crash                     exit 0, 16 shapes scanned
    probe_4c     exit 1, apply_T_w:126     exit 0, verdict FALSIFIED
    probe_4f     exit 1, apply_T_w:126     exit 0

So: one upstream change (#5745, 2026-08-25) left five consumers dead;
three casts in three functions revive them.

## The two excluded buckets are different KINDS of thing

Screened all 12 unmeasured producers: **10 use no numpy or scipy at all**
— high-dps `mpmath`, no sympy, `set_compute_dps()`. Their cost is real
arithmetic, not object-dtype contamination. So:

  * **CRASH** was a *defect* bucket — 5 of 9, now fixed.
  * **TIMEOUT** is a *cost* bucket — nothing a cast will fix.

Only one of the two was ever a bug, and the "~19 unmeasured" caveat
should not be read as "19 possible defects". At a 5x budget,
`bar_pairing_binding_observable`, `block_swap_binding` and
`chi_at_q_inv_via_native_mpfr` each TIMEOUT at **900 s**, having already
exceeded 25 s and 180 s twice.

`block_swap_binding` deserves its own line: it is the producer the
original stall investigation was about. `gram_norm_binding_probe` got
the object-dtype fix (3H 2131 s -> 0.45 s) and this one never did.

## Two things NOT established, stated as such

1. **The committed results file cannot corroborate the triage.** Zero of
   the 91 records carry an `exception` key — every verdict predates that
   runner feature, and the file is one vintage throughout (79 records
   with 7 keys, 12 with `timeout_count`). What it does support is the
   **counts**, which re-derive exactly. The triage is hand re-runs only.
2. **`probe_4c`'s FALSIFIED verdict is not a new result.** Its committed
   witness from 2026-07-07 already records the three falsifying
   partitions, the same values and the same failing assertion. The crash
   blocked re-verification, not discovery. I initially wrote that it had
   been "invisible"; that was wrong.

## Methodological note — three contaminated controls in one session

Twice a corroborating measurement shared a defect with the thing it was
checking (the retracted "reproduced on this branch" claim and its
cross-check, both from my harness's import context). The third: I ran the
pre-fix control against `git show HEAD~2:` — which is the fix commit
itself, so the "pre-fix" code was the fixed code. That would have
produced the exact opposite conclusion, and what caught it was the
control agreeing with the treatment to **every digit**.

**When a check agrees suspiciously well with what it is checking,
suspect a shared defect before accepting the agreement.**


## FINAL TALLY — sweep complete, and the unmeasured tail is NOT different

The 12 unmeasured producers were re-run at a 900 s budget (5x the tier-2
budget), pinned to the same SHA, self-test green. Four completed.

                           before      after
    MOVED_SUBSTANTIVE        37    ->    40
    MOVED_PROVENANCE_ONLY     2    ->     3
    IDENTICAL                31    ->    31
    TIMEOUT                   9    ->     8
    CRASH                     9    ->     9
    scoreable                70    ->    74

**40 of 74 scoreable producers do not reproduce — 54 %, against 53 %
before.** The four recovered split 3 substantive / 1 provenance-only,
the same ratio as the fast half:

    mu3_door_sign_C_vs_D_probe      MOVED   300.4 s
    probe_9b_laurent_degree_10a5    MOVED   299.3 s
    orbit_trace_identity_proof      MOVED   511.1 s
    paper_six_term_isotope_sweep    MOVED   701.9 s

That partly answers limit 2 in the earlier summary. I wrote that the
unmeasured producers 'cannot be assumed to behave like the fast half in
either direction'. Four of them now have, closely. Eight remain
unmeasured at 900 s and the caveat still holds for those — but the
expensive tail is no longer purely unknown.

## Plus a 45th, found outside the sweep

`block_swap_binding` — the producer this bean's stall investigation was
originally about — is now measurable at **5 s** (see qou-mtx9: it was the
wrong compute engine, not a defect). Its 2026-06-22 witness moves on
every substantive field, including a **20 % move on its headline
binding signal**. The refreshed witness is deliberately not committed.


## 2026-08-30 — the class now has a DETECTOR, and a calibration this bean's own case supplied

This bean generalised the class correctly and found its instances by hand. What
it did not have is an automated sweep. Added:
[`computations/witness_assertion_replay_audit.py`](../computations/witness_assertion_replay_audit.py)
— re-runs a producer and compares the **recorded assertions** to the fresh
ones, classifying `REPRODUCES / NOW_FAILS / VALUE_DRIFT / ASSERTIONS_RENAMED /
ASSERTIONS_VANISHED`, with the non-decidable outcomes (`TIMEOUT`,
`ENV_MISSING`, `REFUSED`, `NO_PRODUCER`) reported separately so the sample size
is never overstated.

**Two of this bean's own warnings are built in.** Provenance is read from the
**top-level** `scriptFile`, not a nested one — the pitfall recorded above that
made a first attempt read clean. And the whole `computations/` tree is restored
from git after **every** run, because producers write sibling witnesses;
`witness_producer_executes_audit` restores only the file under test, which is a
live gap in that auditor.

**Coverage ceiling, measured rather than assumed.** Of 2948 live committed
witnesses: 2647 carry a top-level `scriptFile`, 2213 are green, 1986 have
assertions — **1779 have all three and are replayable in principle.** 1169 are
invisible to this method, and the audit says so rather than implying coverage.

**`gram-norm-binding-probe` REPRODUCES today.** This bean's headline instance
was fixed on its own branch ("Witness regenerated ... Both assertions pass"),
and the detector agrees — 6.19e-15 and 4.12e-16, both passing. Recorded because
a detector that reported a finding here would have been *wrong*, and I checked
that before trusting it rather than after.

**A calibration the first sweep earned.** 40 replayed, 36 decidable, one flagged
`ASSERTIONS_VANISHED`: `active-set-lr-scaling-profile`. Verified by hand — it is
a **false positive**. The producer now profiles to A=7 instead of A=6, so its
assertion is *name-indexed by its own reach* and renamed
`max_block_dim_eq_2_pow_A_at_A6` → `..._at_A7`; both pass, nothing is stale.
Reclassified as `ASSERTIONS_RENAMED` (advisory) whenever the fresh set is
non-empty and all-passing; the finding is reserved for a name that vanished with
nothing passing in its place.

**Result on that sample: 0 genuine findings in 36 decidable.** The class is
real — three hand-found instances across 15 days — but this slice is clean, and
that is worth saying plainly rather than leaving the impression of a fire.


## Not stale — and a measured FALSE NEGATIVE in this bean's own detector (2026-09-06)

Reached by `scripts/bean-staleness-triage.py` (7th of 284 artifact beans).

**The headline is fixed and this bean already says so.** `gram-norm-binding-probe.witness.json`
on `main` carries the engine value `0.5751722439`, the stale `0.3883571887` is
gone, `allPassed: True`, `computedAt: 2026-08-29T11:11:22`. The 2026-08-30
update records it, with the discipline note worth repeating: *"a detector that
reported a finding here would have been **wrong**, and I checked that before
trusting it rather than after."*

### 🔴 A fifth gap, and it is confirmed by execution rather than argued

`witness_assertion_replay_audit` reports **`REPRODUCES`** on
`computations/markov-identity-symbolic.witness.json` —
*"✓ every decidable witness in this sample still reproduces"* — on a witness
measured on **2026-09-05** to carry values the current code does not produce:

| sample point | committed | recomputed |
|---|---|---|
| `proton_q0` | 1.1457596924573008697 | **0.62932840220292191817** |
| `1.3` | 3.3688168001572002037 | **1.277736943233662226** |
| `0.7` | −4.7449410256554617359 | **−0.3531913855255301353** |
| `2` | 116.33458984375 | **51.77927734375** |

Roughly **2× at every point**, at sample points that did not change. Run:
`--only markov-identity-symbolic --limit 3 --timeout 900` (the default 120 s
cannot replay this producer — its deuteron bridge alone is 520 s — so at the
default it would have been a timeout, not a verdict).

**Why it is missed, from the code rather than from guessing.** `VALUE_DRIFT`
compares `recorded` against `fresh` **keyed by assertion name** (line 158). The
drifted quantities here are `peel` values in the witness *payload*, not
assertions. This witness has exactly **one** assertion —
`identity_holds_identically_in_q_for_every_atom_tested` — and it is `True` both
before and after, because the residual is identically zero **regardless of
`peel`'s normalisation**. The assertion is robust to precisely the drift that
moved the payload.

**So the uncovered case is one step past this bean's own framing:** its
docstring says *"recorded green, no longer true"*, and none of the five
auditors covers **"assertions still hold, recorded non-assertion payload
moved."** `witness_reproducibility_check` does byte-equality but only for
`*.derivation.json`, so witness payload drift falls between them.

The instance is in the **replayable 1779**, not the 1169 invisible — top-level
`scriptFile`, green, has assertions — so this is a false negative inside the
covered population, not a coverage-ceiling case.

### Proposed close, with its cost stated

Compare the **payload** under a volatile-field mask on a replay the detector is
already doing (it restores the tree afterwards, so both versions are in hand).
The mask is the one AGENTS.md already specifies for witness comparison —
`timestamp`, `computedAt`, `elapsed_seconds`, `durationMs`, `measured_at`,
`start_time_monotonic`, the `invocation` block.

**Honest cost:** payload comparison is noisier than assertion comparison, which
is presumably why it was not done. Timings and any incidentally-recorded
environment detail will drift constantly, so an unmasked version would be
useless and even a masked one may need per-producer tuning. Offered as a
proposal for the detector's owner, not applied here — this bean's own posture
is that a detector reporting a wrong finding is worse than one reporting none.

**Not reopening the headline.** `gram-norm-binding-probe` is fixed; this is
about the detector that grew out of it.
