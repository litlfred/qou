---
# qou-1oxx
title: 'Bar-parity pairs are frame-mismatched: chi at-q0 colour-weighted, at-qinv colour-blind'
status: completed
type: task
priority: normal
created_at: 2026-08-26T07:07:20Z
updated_at: 2026-08-26T15:45:27Z
---

Found 2026-08-26 while fully discharging `qou-cds4`'s witness line. Third
instance of one root pattern: a SIGN-based representation that cannot carry
the crossing coefficient `d` (cf. qou-qu2w, qou-iu3m).

## The mismatch

    chi-deuteron-h6-at-q0-50dps      colour-weighted-averaged-crossing  2026-08-10
    chi-deuteron-h6-at-qinv-50dps    averaged-crossings                 2026-07-18
    ... and identically for tritium-h9, helium-3-h9, helium-4-h12.

All FOUR pairs. The q0 side was regenerated colour-weighted and the qinv side
was left behind a month earlier.

## Why it matters: a live observable compares across frames

Seven live consumers reference the qinv witnesses, several of them bar-parity
/ conjugation probes whose entire job is to pair chi(q) against chi(1/q):

    bar_pairing_binding_observable.py          (docstring names both)
    probes/probe_d_barparity_binding.py:97-99  (loads one of each)
    probes/probe_d_delta_lambda_terms.py
    deltalambda/deuteron_conjugation_parity_categorical_probe.py
    deltalambda/deltalambda_conjugation_symmetric_excluded_probe.py

So the bar-parity observable is currently built from a colour-weighted q0 and
a colour-blind qinv. Bar-parity feeds Delta_lambda reasoning.

## It is NOT a label bug — the label is honest

`chi_at_q_inv_via_native_mpfr._word_to_signed` maps each crossing to a SIGN:

    |d| ~ 0        -> sgn = +1
    |d + h0| ~ 0   -> sgn = -1
    |d + h0/2| ~ 0  OR  |d + h0(1/2 - delta/4)| ~ 0  -> sgn = 0

Both averaged variants land on sgn=0. The in-file comment records that the
colour-weighted one "used to hit the raise below" and was added as an accepted
case (bean qou-gdtb) — i.e. made not to CRASH, not made REPRESENTABLE. It even
imports `_pn_delta()` solely to RECOGNISE the weighted crossing and then
discard the distinction.

Note `run_atom` calls `atom_braid_word_3A(Z, N)` — the CANONICAL default — so
the word going in is colour-weighted and the representation throws the
weighting away. The witness's "averaged-crossings" label is therefore accurate
about the value.

## Severity, bounded

That path has THREE channels, so it DOES distinguish averaged from plain
sigma. It collapses only the two AVERAGED variants. The error is the
colour-weighting delta — 0.0141 % per p-n interface — NOT the 17 % plain-sigma
collapse of qou-qu2w. Real and structural, but small.

## Fix shape

Needs a d-preserving qinv path, mirroring the qou-qu2w fix (which re-pointed
at `chi_monotone_transfer.chi_all_lambda`). Not done inline because it moves
bar-parity numbers that feed Delta_lambda, and because the qinv path currently
routes through `pyhecke_native`, so the substitute has to be chosen rather than
assumed.

Cheap first step for whoever takes it: confirm by MEASUREMENT, as with the
chi-*-at-q0 oracles — recompute one qinv witness under both averaged variants
and check whether the committed value matches the blind one. If it does, the
diagnosis above is confirmed end-to-end rather than read off the source.


## 🛑 CORRECTION 2026-08-26 — my prescribed fix was WRONG, measured

The section above says this is "the same shape as marshal_to_chi_lambda_braid"
and that the fix "needs a d-preserving qinv path". **Both are wrong**, and I
found out by running the confirmation step this bean itself specified.

`chi_all_lambda` REJECTS the word at 1/q0:

    ValueError: unrecognised crossing (c=1.0, d=-0.10453...)

because the word carries `d` pinned NUMERICALLY at q0. Measured, the deuteron
word's distinct `d` values are:

    0.0              sigma
   -0.209060298796   sigma^-1        = -h(q0)
   -0.104530149398   averaged blind  = -h(q0)/2
   -0.104458247770   averaged wtd    = -h(q0)(1/2 - delta/4)

and at 1/q0 the substrate `h` FLIPS SIGN:

    h(q0)   =  0.209060298796
    h(1/q0) = -0.209060298796

so `-h(q0)/2 = -0.10453` is not the averaged coefficient at 1/q0 — there it is
`+0.10453`. A value-preserving re-evaluation is therefore IMPOSSIBLE: carrying
`d` across the bar is not conservative, it is wrong.

**So the sign/type representation is NECESSARY, not a defect.** To evaluate chi
at 1/q0 you must know the crossing TYPE and REBUILD `d` there. That is exactly
what `_word_to_signed` does, and it is the right design.

### The actual defect is narrower

The type vocabulary has only THREE slots (sigma / sigma^-1 / averaged), so the
two averaged variants have nowhere to go and are merged. The fix is a FOURTH
slot — `averaged_weighted` — plus rebuilding `d` at 1/q0 per type. Much
smaller than a rewrite, and it does not touch the representation choice.

### Severity re-confirmed from the same measurement

The deuteron word contains FOUR blind averaged crossings (intra-nucleon, two
per nucleon — colour-blind by definition, nothing to weight) and ONE weighted
crossing (the single p-n interface). The 3-slot collapse therefore loses
exactly the p-n weighting on one crossing, which is the 0.0141 % figure
already stated. Consistent.

### Lesson

I wrote a fix prescription from reading the source and it was wrong in the
direction that would have caused work: "preserve d" is the OPPOSITE of correct
across the bar involution. The cheap confirmation step was in the bean because
I did not trust the reading — and it earned its place on the first run.


## 🛑 SECOND CORRECTION 2026-08-26 — the FOURTH-SLOT prescription is also
## questionable, for an independent reason: the canonical convention is NOT
## bar-invariant

The correction above narrowed the fix to "a fourth type slot
(`averaged_weighted`) + rebuild `d` at 1/q0 per type". That still carries an
unstated premise: that the q0 side and the qinv side OUGHT to be in the same
p-n frame. Sibling work landed on `main` (bean `qou-cblw`, commit `a4b7cb4f39`)
that makes the premise doubtful.

A sibling bean is not a primary source (AGENTS.md states this explicitly), so I
verified every identity symbolically myself rather than relaying them. All five
confirmed, with `z` the Markov parameter, `h = q - 1/q`, and
`delta = (q-1)^2 (1 - q^-4)/3` the flavour split:

    bar(z) - (z - h)                         = 0
        -> f_pp and f_nn ARE bar-conjugates of one another

    f_strict - (f_pp + bar(f_pp))/2          = 0
        -> the strict/colour-BLIND form IS the bar-symmetriser, by construction

    bar(delta) + q^2 * delta                 = 0
        -> bar(delta) = -q^2 delta, i.e. delta is bar-MIXED (neither even nor odd)

    bar(f_strict) - f_strict                 = 0
        -> the colour-BLIND form IS bar-invariant

    bar(f_canon) - f_canon = (q-1)^5 (q+1)^3 (q^2+1) / (12 q^5)
        -> the colour-WEIGHTED (canonical, R3) form is NOT bar-invariant
        at the proton pin: 1.66849e-5   (sibling's claimed 1.67e-05 ✓)

### What this does to the prescription

`f_canon = w_p f_pp + w_n f_nn` with `w = 1/2 +- delta/4` is a weighted mean of
two bar-conjugates. It is bar-invariant only if the weights are bar-invariant,
and `delta` is bar-MIXED, so it is not. The strict form is exactly the
equal-weight case, which IS the symmetriser.

So for a probe whose entire job is to pair `chi(q)` against `chi(1/q)`, the
colour-BLIND `qinv` witness may be the RIGHT object, not a stale one: the
bar-parity statement is a statement about the bar-symmetric form. Making both
sides colour-weighted — what this bean prescribes — would put a
non-bar-invariant quantity on both sides of a bar-parity test and change what
the test measures by 1.67e-5, which is COMPARABLE to the 0.0141% p-n weighting
this bean set out to restore.

### Re-scoped: this is now a QUESTION, not a defect with a known fix

The measured frame mismatch is real and still stands as a finding. What is no
longer established is that closing it means "make the qinv side colour-weighted".
Two dispositions are now live, and they are NOT the same for every consumer:

  (a) The bar-parity / conjugation probes (`bar_pairing_binding_observable.py`,
      `probes/probe_d_barparity_binding.py`,
      `deltalambda/deuteron_conjugation_parity_categorical_probe.py`,
      `deltalambda/deltalambda_conjugation_symmetric_excluded_probe.py`)
      may WANT the colour-blind form on BOTH sides — in which case the defect
      is on the q0 side, the opposite end from where this bean pointed.

  (b) Consumers that want the canonical (R3) observable want colour-weighted on
      both sides and must accept that `bar` moves it by 1.67e-5.

Deciding between them is a question about what the bar-parity observable is FOR,
which is upstream of this bean and is the subject of `qou-cblw`. Do not
implement the fourth slot as a mechanical fix until that is settled — the
implementation is cheap, but it would silently pick (b) for consumers that need
(a).

### Lesson (second time in one bean)

Both of my prescriptions here were written from reading source and both were
wrong. The first assumed `d` could be carried across the bar; the second assumed
both sides should be in the canonical frame. In each case the error was an
UNSTATED premise about the bar involution, not a misreading of the code.


## ✅ OWNER DECISION 2026-08-26 — and THREE more corrections from re-measuring

Owner picked, from a four-way question: **(1) match the qinv side to the
canonical convention**, **(3) emit BOTH frames and let consumers pick**, and
**(4) fix the false label + provenance**. Option (2), matching everything to
colour-blind, was not chosen.

Before implementing I re-measured on `main`, and three things in the sections
above are **wrong**. All three were written from reading source.

### C1. The mechanism ALREADY EXISTS — on the other side of the pair

Both corrections above argue about how to represent the colour weighting.
Neither noticed that `chi_at_q0_via_hoefsmit_mpfr.py:325` already solved it:

    avg_shifts: list[str] = []          # per-crossing, "" meaning "h/2 here"
    ...
    rust_out = _rust_chi_all(n, word_signed, q_str, dps,
                             None if not any(avg_shifts) else avg_shifts)

and the kernel signature is

    #[pyo3(signature = (n_strands, word, q_str, dps, avg_shifts=None))]

The qinv driver called the **four-argument** form
(`chi_at_q_inv_via_native_mpfr.py:141`), so it silently took the kernel default
`h(q)/2` — the colour-blind average. The fix is one argument, not a redesign.

**So the "fourth type slot" prescription was wrong in SHAPE too** — the third
correction to the same fix. The mechanism is a **continuous per-crossing shift
string**, not a discrete enum slot. A fourth slot would have re-implemented,
in a worse form, something the kernel already accepts.

### C2. The blast radius is SMALLER than this bean claims

The section above lists five bar-parity consumers. Measured, only **two** load
the *bound* pair:

    probes/probe_d_barparity_binding.py       chi-deuteron-h6-at-q0 + -at-qinv
    probes/probe_d_delta_lambda_terms.py      same

The two `deltalambda/` conjugation probes use the **free** deuteron
(`chi-deuteron-free-h6-at-{q0,qinv}-50dps`), and BOTH sides of that pair
measure `averaged-crossings` — matched, and correctly so: a free word has no
p-n interface, so there is nothing to weight. They were never affected.

### C3. The qinv label was never MEASURED — it was inferred from the filename

    "convention": "averaged-crossings",
    "convention_inferred_by": "chi_convention_audit.py --fix
                               (computation-id:/^chi-(?!.*-free-).*-at-qinv-50dps$/)"

alongside `"q0Anchor": "ambiguous"` and `"scriptCommitSha": "unknown"`. The
label is a fact about the **path**, not about the numbers. It happens to be
correct; nothing in the witness established that. This is what option (4)
fixes — and note the `at-q0` side had the identical disease and was cured the
same way (`chi_at_q0_via_hoefsmit_mpfr.py:164`, "Derive the convention label
from the word instead of asserting it").

### Measured: exactly ONE weighted crossing per atom

    deuteron  23 factors   11 sigma / 7 sigma^-1 / 4 averaged-blind / 1 weighted
    tritium   35 factors   16 / 12 / 6 / 1
    helium-3  35 factors   18 / 10 / 6 / 1
    helium-4  47 factors   23 / 15 / 8 / 1

which confirms the 0.0141 %-per-interface severity stated above, and confirms
the intra-nucleon averaged crossings are colour-blind by construction.

### The shift must be REBUILT at the target, and here is why, numerically

    h(1/q0)/2                    = -0.104530149397819658
    h(1/q0)*(1/2 - delta(1/q0)/4) = -0.104618735975170679
    h(q0)/2                      = +0.104530149397819658   <- SIGN FLIPPED

`delta` is evaluated **at the target q** via `flavor_split_leading(q)`, which
takes q as an argument and is exact at whatever precision it is handed — never
`_avg_color_delta()`, which is pinned at q0. The blind/weighted gap is
`8.86e-05` at `1/q0` against `7.19e-05` at `q0`: **not symmetric**, exactly as
`bar(delta) = -q^2 delta` predicts.

### What ships

  * `chi-{atom}-h{n}-at-qinv-50dps`                  colour-blind, UNCHANGED
    values and UNCHANGED computation-id, so no existing consumer moves.
  * `chi-{atom}-h{n}-at-qinv-50dps-colour-weighted`  canonical (R3), NEW.

Neither is "the stale one". The colour-blind frame is a coherent object and is
arguably the right one for a bar-parity question, since it IS the
bar-symmetriser and IS bar-invariant. What was wrong was pairing it against a
colour-weighted `at-q0` **without saying so**.


## Reproducibility envelope, and why it is NOT sibling `qou-569e` (2026-08-26)

Regenerating these witnesses shows LAST-DIGIT movement. Measured, so it is not
re-derived or mistaken for a regression:

    within one process   three consecutive kernel calls BIT-IDENTICAL
    4-arg vs 5-arg-None  BIT-IDENTICAL (deuteron 11/11, helium-3 30/30) --
                         the avg_shifts argument added here is NOT a cause
    across processes     the 50th (last serialised) digit CAN move: tritium
                         (3,3,2,1) matched main on one run and differed by
                         1.42e-50 on the next, same code, same container
    vs origin/main       an environment delta ALSO applies: main's committed
                         witnesses record mpmath 1.3.0 / pyhecke_native_build
                         c7ea7ebb0d76c4e2; this container is mpmath 1.4.1 /
                         c85ef99ee89ce1c3

Largest observed 4.34e-50 relative (helium-4, 4 of 77 partitions), ~35 orders
below the L1 target of 1e-15.

**Do NOT restate "byte-identical" as a property of this producer.** I reported
it for D/T/3He and it then failed on a re-run of the same code. It was luck.

### Distinct from sibling bean `qou-569e` -- do not merge the two

`qou-569e` (landed on main 2026-08-26) reports that two committed witnesses do
not reproduce on a clean `main` worktree, one by **23 %**, and attributes it to
IMPORT-CONE drift. That is a different phenomenon from this one at every level:

    qou-569e   23 % value move        import-cone drift   a real number changed
    here       ~1e-50 digit movement  serialisation floor  no value changed

A reader who sees "witnesses do not reproduce" in both could reasonably collapse
them. They should not be collapsed: one is a corpus-integrity problem, the other
is the last printed digit of a 50-dps serialisation.

### This branch is NOT exposed to the qou-569e drift -- checked, not assumed

`qou-569e` names `fbc0858af` (chi_lambda_braid symbolic_q now returns) as the
probable cause. Verified here:

  * `fbc0858af` is ALREADY an ancestor of this branch's HEAD, so these
    witnesses were built with it, not before it.
  * this producer references neither `chi_lambda_braid` nor `symbolic_q`.
  * of the 20 commits main is ahead by, NONE touch any module in this
    producer's import cone (`mass_at_3A_proper`, `canonical_braid_crossings`,
    `_li_2_q_util`, `q_parameter`, `_precision`, `witness_base`, `tools/pyhecke`).

So merging main in cannot invalidate what was generated here.


## ✅ MERGED 2026-08-26 — PR #5830, rebase-merge 7a5f6bf240

All four atoms ship both frames. Verification at merge (no CI exists; the
agent's own verification IS the gate, per AGENTS.md rule 10):

    precision-gates.sh --changed   GATES_EXIT=0, no RED
                                   (was RED: raw-float64 ratchet -- drained)
    raw-float64 ratchet, direct    exit 0, 0 NEW dirty, 0 REGRESSED
    chi_convention_audit           exit 0, ok 36 / mismatch 2
                                   (clean main is 32/2; the 2 are pre-existing)
    probe_d_barparity_binding      exit 0, 2/2, 5.859e-04, Sum a^odd 1.13e-72
    probe_d_delta_lambda_terms     exit 0, 2/2, rel 2 = 5.859e-04

Both probes reported values IDENTICAL before and after a rebase across 31 of
main's commits -- the practical confirmation of the import-cone check above.

Copilot did not enqueue (get_check_runs total_count 0). That is n=6 for bean
qou-gwe9, whose measurement is n=5.

**What remains open: ** --  does
not cover the  family, so the widened PRODUCER_CONVENTION
acceptance is not backed by an independent measurement. Found by auditing my
own change. Not a regression from this work; a gap this work exposed.


(The line above lost three identifiers to shell backtick-expansion when it was
appended. Restated intact:)

**What remains open: `qou-awwk`** — `chi_convention_from_values_audit` does not
cover the `-at-qinv-` family, so the widened `PRODUCER_CONVENTION` acceptance in
`chi_convention_audit` is not backed by an independent measurement. Found by
auditing my own change rather than the corpus. Not a regression from this work;
a gap this work exposed and named.
