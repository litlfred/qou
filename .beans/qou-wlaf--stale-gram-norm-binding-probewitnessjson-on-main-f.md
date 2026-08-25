---
# qou-wlaf
title: 'STALE: gram-norm-binding-probe.witness.json on main fails its own cross-check assertion by 7 orders of magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T16:43:22Z
updated_at: 2026-08-25T19:11:39Z
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
