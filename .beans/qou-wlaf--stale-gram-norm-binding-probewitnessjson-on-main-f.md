---
# qou-wlaf
title: 'STALE: gram-norm-binding-probe.witness.json on main fails its own cross-check assertion by 7 orders of magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T16:43:22Z
updated_at: 2026-08-26T03:16:33Z
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
