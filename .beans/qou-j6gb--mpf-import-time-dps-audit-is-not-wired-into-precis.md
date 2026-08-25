---
# qou-j6gb
title: mpf_import_time_dps_audit is NOT wired into precision-gates.sh — 288 findings, 185 proven lossy, gate silent
status: in-progress
type: bug
priority: normal
created_at: 2026-08-10T02:36:03Z
updated_at: 2026-08-25T16:49:23Z
---


## The finding

`computations/mpf_import_time_dps_audit.py` exists, is position-aware, runs, and
exits **1** under `--strict`:

    module-scope mpf built before precision is raised: 288  [witness-emitting scripts]
       proven lossy (literal arg):                     185
       position-risky (expr arg, not statically provable): 103
    files affected: 91

It is **not in `scripts/precision-gates.sh`'s `GATES` array.** The eight that are:

    q0-anchor flip            q0_anchor_consistency_audit.py
    mpf(<float>) source       mpf_float_source_audit.py
    float64-padding ratchet   witness_float64_padding_audit.py
    mp.dps no-op              mpf_context_dps_audit.py
    module-const precision    module_const_precision_audit.py
    raw-float64 ratchet       witness_raw_float64_audit.py
    q0-value drift ratchet    q0_value_drift_audit.py
    no-free-parameter cert    no_free_parameter_certificate.py   (advisory)

Per bean `qou-mnrd` and AGENTS.md §"QA is agent-owned; CI is a backup",
`precision-gates.sh` **is** the gate — `witness-staleness.yml` is dispatch-only
under the owner's 2026-06-30 Actions-billing directive, reaffirmed 2026-08-09.
So an audit outside that array is an audit nobody runs.

## Why this matters more than the raw count

The defect it detects hit **five times in the drain arc** (`qou-mnrd`), each time
found by accident when something happened to print at high dps, each time a
one-line fix:

    VOL_41              one_loop_c_sigma_tetrahedral_probe.py
    q0                  gram_qtrace_hutchinson_probe.py
    TOLERANCE_PPQ       cross_check_trM_1ppb.py
    REG_ZC / REG_ZD     y_lambda_su_n.py                      (two constants)

All five were caught by *other* gates (`module-const precision`,
`float64-padding`) reacting to downstream symptoms. The audit built specifically
for the cause was sitting right there, unrun. `qou-brkp` records that this same
audit was ALSO silent on two files its own remediation had broken — that bug is
fixed, but the audit went from "silent for a parse reason" to "silent because
nothing calls it", which is the same outcome by a different route.

## Why it is probably unwired, and what to do about it

Almost certainly because adding it blocking turns the gates red on day one: 288
findings is not a thing anyone drains in one sitting.

**Wire it as a ratchet, not as a pass/fail.** That is exactly the shape that took
`witness_raw_float64_audit.py` from red to green over this arc:

  1. baseline the current 288 into a `mpf-import-time-dps-baseline.json`, with
     the audit's own "do NOT add a file to the baseline to silence this" warning
     in its header;
  2. block only NEW and REGRESSED entries;
  3. add it to `GATES` with `blocking=yes`, and to the workflow's step list —
     `precision-gates.sh` carries an explicit instruction to keep those two in
     sync.

Then the 185 proven-lossy are a background drain like the float64 ones, and a
sixth instance cannot land.

**Do the 185 before the 103.** "Proven lossy (literal arg)" means a decimal
string was parsed at 15 dps and the digits are gone — statically certain, and the
fix is the idempotent `set_compute_dps()` above the constant. The 103
"position-risky (expr arg)" are not statically provable and some will be fine;
mixing them into the same ratchet dilutes a signal that is currently exact.

## Not done here

Not wired, not baselined. Wiring a new blocking gate changes what every agent's
pre-commit and `/prepare-merge` must pass, which is a scoped decision rather than
a drive-by — and the 288 number should be re-measured at the moment it is
baselined, not taken from this bean.

---

## DONE — wired as a ratchet, 2026-08-10

Owner said "do ratchet". Implemented exactly the shape recommended above, in the
same idiom as `witness_raw_float64_audit.py`.

### Baseline

    computations/mpf-import-time-dps-baseline.json
    91 files / 185 literal / 103 expr

Matches the pre-wiring measurement exactly, so nothing was reclassified on the
way in.

### `literal` and `expr` are baselined and compared SEPARATELY

Per the recommendation above, and it is the one design point worth defending: a
`literal` finding is statically certain (a decimal string parsed at 15 dps —
the digits are gone), an `expr` finding is only position-risky and some are
fine. If the ratchet summed them, a file could gain a proven defect and drain an
unproven one in the same edit and show no change. Separate counts make that
impossible.

### Unparseable files are never baselined and always fail

Not a stylistic choice. Bean `qou-brkp` records this audit having reported
*clean* for two files its own remediation had just broken, because `scan_file`
returned zero rows on a parse failure — "no information" rendered as "no
findings". The parse bug is fixed, but the ratchet would have re-introduced the
same hole if a broken file could be baselined at zero. There are **0** such
files at baseline time, so this cannot be red on arrival; if one appears it is a
real regression.

### Verified by making it fail, not only by watching it pass

A ratchet that has never been seen to fire is a no-op — the same principle the
`--self-test` flags in this family exist for. Three cases:

    A  new file with a lossy module-scope mpf   → exit 1, listed by name   ✓
    B  baselined file gains one constant        → exit 1, REGRESSED shown  ✓
    C  probe removed / file restored            → exit 0                   ✓

Plus `--self-test` green (8 cases) and `--strict` green at baseline
(0 NEW, 0 REGRESSED, +0/+0).

`--rebaseline` refuses to run under `--all`: that scan includes scripts emitting
no witness, which the baseline does not cover, so rebaselining from it would
silently widen the tolerated set by ~100 files.

### Wired in BOTH lists

    scripts/precision-gates.sh   GATES[]  →  "import-time dps ratchet|…|--strict|yes|yes"
    .github/workflows/witness-staleness.yml  →  matching step

The script's header carries an instruction to keep those two in sync, and the
whole point of this bean is that a detector in neither list is not a gate. Added
a note to that header saying so in as many words, with this bean as the worked
example.

## Still open — the 185

The ratchet stops a sixth instance; it does not fix the five that landed. The
backlog is now a visible, shrinking number instead of an unrun script.

**Do the 185 `literal` ones first.** Each is statically proven lossy and the fix
is one line — `set_compute_dps()` at module scope above the constant. The 103
`expr` ones are not statically provable and some will be fine; working them
first would spend effort on maybes while certainties sit.

Largest single offenders at baseline:

    48  computations/inverse-markov-qvalues.py
    14  computations/binding_block_multiplicative.py
    14  computations/meson_mass_from_hecke.py
     8  computations/m_tau_complex_volume_search.py

Bean stays open with status in-progress until the `literal` count reaches 0.

## Drain pass 1+2 — 185 → 80 proven-lossy, 42 files

    literal (proven lossy)   185 -> 80    (-105)
    expr    (position-risky) 103 -> 90    (-13, incidental: same files)
    files drained             42
    NEW / REGRESSED            0 / 0      throughout

Applied via AST, not text anchoring — see the commit for why (`qou-brkp`'s
insertion-inside-a-dict-literal). Verified three ways each pass: every changed
file parses, every changed file **imports** (the check `qou-brkp`'s breakage
would have failed), and the full gate family stays green.

Pass 2 widened one refusal that was too narrow. Pass 1 skipped any file that did
not *import* `set_compute_dps`; but `a4_interface_kl_subpath_closure.py` and
`a4_option_e_color_tube_closure.py` **define their own** local
`set_compute_dps()` and never call it at module scope. The name was available
all along. Genuine findings, not false positives — and worth remembering as a
shape: a helper defined and never invoked reads as "handled" to a grep.

## Remaining: 80 literal across 26 files, and they need a decision

Every one of the 26 is blocked on the same thing — the name `set_compute_dps` is
neither imported nor defined, so the one-line fix has nowhere to land. Two routes,
and they are not equivalent:

  * **add `from _precision import set_compute_dps`** — canonical, and what the
    other 152 producers do. Needs `computations/substrate` on `sys.path`, which
    is what `_path_bridge` provides; ~19 of the 26 already import it.
  * **insert `mp.dps = 50` at module scope** — no import needed, accepted by the
    audit's `_raises_dps`, and already the idiom in the option_e and probe
    families. But it hard-codes the precision instead of deferring to
    `_precision`, so it drifts if the canonical value ever changes.

Route 1 where `_path_bridge` is present, route 2 elsewhere, is the obvious split
— but adding an import to 19 files is a wider blast radius than inserting a call,
and it should be someone's deliberate call rather than a third automated pass.

Largest remaining, all literal counts:

    12  computations/meson_mass_from_hecke.py
     8  computations/inverse-markov-qvalues.py
     8  computations/meson_gen3_eta_phi.py
     6  computations/deltalambda/perknot_pn_bond_resolved_extensivity_probe.py
     6  computations/probes/yardstick_free_phase_binding_probe.py

## Drain COMPLETE for the proven-lossy class — 185 → 0

    literal (proven lossy)   185 -> 0     (-185)
    expr    (position-risky) 103 -> 51    (-52, incidental)
    files drained             68
    NEW / REGRESSED            0 / 0      throughout all three passes

Pass 3 took the last 26, where the name `set_compute_dps` was neither imported
nor defined. Two routes, chosen per file from what the file can actually reach:

    route 1  (19 files)  imports `_path_bridge`, so `from _precision import
                         set_compute_dps` is reachable — canonical, matches the
                         other 152 producers.
    route 2  ( 7 files)  no bridge; assign dps directly.

Route 2 has a trap worth recording: **both `mp.dps = 50` and `mp.mp.dps = 50`
satisfy the audit's `_raises_dps`, but only one works at runtime**, and which
depends on the import style —

    from mpmath import mp   ->  mp.dps = 50
    import mpmath as mp     ->  mp.mp.dps = 50

so the alias is read off the AST rather than guessed. A gate that accepts both
forms cannot tell you that you picked the wrong one; the source check would go
green on a file whose constants are still built at 15 dps.

Which is why pass 3 was verified at RUNTIME, not just by parsing:

    26 files: import OK 26/26, and mpmath.mp.dps >= 50 after import 26/26

with dps reset to 15 before each import, so one module's raise cannot mask
another's failure. That check is what proves the alias detection right; parsing
and importing would both have passed a wrong alias silently.

## Remaining: 51 `expr` findings, and they are a different question

Not statically provable — `mpf(<expr>)` where the argument is computed. Some are
genuinely fine (an expression over already-high-precision values), some are the
same defect wearing a different sleeve. They need reading, not a fourth
automated pass, and the ratchet holds the line at 51 meanwhile.

Bean stays in-progress on that account. The class it was opened for — the one
that landed five times unnoticed — is closed and cannot recur silently: the gate
is wired in both lists, the proven-lossy count is 0, and anything new fails.

## CORRECTION — the drain does NOT only drain the padding ratchet

The pass-1 commit (`e089dcd1a`) claimed:

> Committed witnesses still carry values computed with the lossy constants;
> they correct themselves when their producers are next run, and that can only
> DRAIN the padding ratchet, never regress it — a constant that gains digits
> removes padding rather than adding it.

**Wrong, and caught by the gate rather than by me.** The reasoning holds for the
constant itself and stops there. Raising module-scope dps also raises the OUTPUT
precision of everything else the producer serializes — including values that are
genuinely float64. Those were previously printed at ~15 digits and looked clean;
at 50 dps they print the binary64 expansion, which is exactly what the padding
audit is built to catch.

Observed, on three producers whose witnesses got rewritten when the pass-3
verification imported them (they write at import time, no `__main__` guard):

    inverse-markov-qvalues   nucleon_results[*].Q_exp, quark_results[*].Q_exp
    meson-mass-from-hecke
    u1-hypercharge-assignment

    committed  "0.782333409310022"                     (15 digits, dps=15)
    after fix  "0.78233340931002215423717416342697..."  (binary64 expansion)

    float64-padding ratchet: 13 baseline -> 18 found, 5 NEW  → RED

The underlying `Q_exp` was **always float64**. Nothing became less precise; the
drain removed the mask. Those three witnesses were reverted here — they were
written by an import side effect, not by a deliberate producer run — and the
padding ratchet is back to 13/13, 0 NEW.

### What this means for the rest of the drain

68 producers now build their constants at 50 dps. Any of them that ALSO carries
a genuine float64 will go red on the padding ratchet the first time it is
deliberately re-run. That is the drain working — a hidden float64 becoming
visible is the point — but it is a **downstream cost that has to be planned**,
not discovered one producer at a time. Three are already identified above.

Concretely, before re-running any of the 68: expect padding findings, and fix
them at the producer (carry the value as a string/mpf from its source) rather
than reverting the dps fix. Reverting would re-hide the float64.

### Method note

The witnesses were rewritten by the verification step itself, because those
three producers write at import time. An import smoke test is not side-effect
free in this corpus. It is still the right check — it is what proved route 2's
alias detection correct — but it needs a `git status` sweep afterwards, which is
how these were caught.

## State on main, 2026-08-15 (re-measured after main moved 1021 commits)

    literal (proven lossy)   0      exit 0
    expr    (position-risky) 51
    drained since baseline   68 files
    NEW / REGRESSED          0 / 0

The drain survived 1021 commits of other people's work intact. Worth stating
plainly because it was not obvious it would: 68 producers were edited, and the
window included at least one incident (recorded on PR #4903 by the #4899 arc)
where a merge resolution taken "to ours" silently reverted a float64 drain on
four witnesses. That the `literal` count is still 0 was checked, not assumed.

The bean's original class — the one that landed five times unnoticed — is
**closed**: the gate is wired in both lists, `literal` is 0, and anything new
fails.

## The remaining 51 `expr`, and a target handed over from #4899

Still not statically provable, still needing reading rather than a fourth
automated pass.

But #4899 flagged a related gap that this bean's gate **cannot** see, and it is
worth recording here because it is the natural next target and the reasoning is
not obvious:

> `markov_trace_recursive.py` never called `set_compute_dps()`, so every `mpf`
> in it ran at the default 15 dps — the producer was float64 wearing 60 digits,
> and `mpf_context_dps_audit` reported the gated paths clean throughout.

A producer that **never raises its working precision at all** is invisible to
this gate, to the padding scan, and to the raw-float64 scan alike — because the
numbers it emits are *honestly* float64. There is no fake precision to detect
and no mpf built too early; the whole computation is simply low. What exposed it
was tightening a comparison until three assertions failed at digit 17 with
dyadic tails.

So the gate family has a blind spot shaped exactly like its own premise: every
member assumes precision was raised *somewhere* and asks whether a value got in
before it. None asks whether it was raised at all. A "producer never calls
set_compute_dps / mp.dps and emits a witness" check would be cheap and static,
and would be a genuinely new axis rather than a fourth variation.

## The #4899 blind spot now has a gate — `never_raises_dps_audit.py`

Wired into both lists, ratcheted at **46 producers / 206 constructions**.

It flags a file only when ALL of these hold, and the third is the one that makes
it sound:

    1. emits a witness            (WitnessBuilder / .witness.json)
    2. CONSTRUCTS mpmath values   (AST-level: mp.mpf, mp.sqrt, bare mpf(...))
    3. is RUNNABLE                (has an `if __name__ == "__main__":` guard)
    4. never raises precision     (set_compute_dps / .dps assign / workdps)

**`mp.dps` is GLOBAL STATE**, so an imported helper legitimately inherits the
precision its caller set. `_li_2_q_util.py` builds 40 mpmath values, raises dps
nowhere, and is entirely correct — it is only ever called from producers that
raised it first. Without condition 3 the audit flags 66 files and the genuine
findings drown in helpers working as designed; with it, 46. Condition 2 matters
too: a string match on "mpmath" caught audits that merely scan for the word,
145 files rather than 66.

### Worked true positive

    computations/sweeps/paper_six_term_isotope_sweep.py:145
        out[r["atom"]] = abs(mp.mpf(r["tr_M_at_q0_50dps"]))

It reads a field whose NAME says 50 dps and lifts it at 15, discarding 35
digits. Its witness contains no string longer than 25 decimals anywhere — the
whole file computes and emits at binary64 while sourcing 50-dps inputs.

### Note for whoever drains this

Unlike the import-time backlog, **fixing these MOVES PUBLISHED VALUES.** There
the constant was mis-built and everything downstream of it was already fine;
here the producer genuinely computed low, so raising dps changes what it emits.
Expect the witness to move and expect that to be the point — and expect the
padding ratchet to react, per the correction recorded above.

`markov_trace_recursive.py`, the instance #4899 reported, already raises dps on
main and is **not** flagged. The gate could not be validated against it; it was
validated by construction instead — a self-test that fires each condition and
holds each exemption (8 cases), plus new-file / removed round-trip on the
ratchet.

## Pre-existing bug found while wiring: the advisory gate CLOBBERS the real one

`scripts/precision-gates.sh` runs `witness_raw_float64_audit.py` twice — once
blocking over the corpus, once advisory with `--scan-root docs/audits/scripts`.
Both write the SAME witness, so the advisory subtree run overwrites the
canonical one:

    dirty_witnesses  1561 -> 5
    total_fields  534,192 -> 20
    drained_files      14 -> 1572
    regressed           1 -> 0

The second row is the dangerous one: a scan of a 5-file subtree reports
`regressed: 0` into the file that is supposed to record the corpus-wide ratchet
state. Anyone reading the committed witness rather than re-running the gate gets
"green" from a run that examined 20 fields.

Pre-existing on `main` (line 89), not introduced here, and NOT fixed here —
the fix is to give the advisory run its own output path, which is a change to a
shared gate script and wants its own scope. Recorded so it is not rediscovered
as a mystery.

## First never-raises drain: `paper_six_term_isotope_sweep.py` — and it was DEAD

    never-raises ratchet: 46 producers / 206 constructions -> 45 / 167

Two separate defects in one file, and the first one is the reason nobody had
noticed the second.

**It could not run at all.** Line 1342 referenced `M_P_MEV_VALIDATION` bare,
while the file only ever imports that name *aliased and function-scoped*
(`as _M_P_CODATA`, at lines 858 and 1203). So the module raised `NameError` on
reaching `ISOTOPES`. Not slow, not skipped — dead, exactly like
`term6_full_pole_sum` earlier in this arc. Fixed with a local import matching
the convention the other two sites state explicitly (validation-only CODATA,
for fit residuals, never a prediction input); its neighbours in that list are
plain CODATA floats, which is what this entry was meant to be.

**It computed everything at 15 dps.** `set_compute_dps()` at module scope, which
also covers the `mp.mpf(str(...))` constants immediately below it. The symptom
that made this the top drain target:

    out[r["atom"]] = abs(mp.mpf(r["tr_M_at_q0_50dps"]))

a field whose NAME says 50 dps, truncated to 15 on the way in.

### The witness is NOT regenerated, and the reason is worth recording

At 50 dps the producer is intractable in this container. It sweeps 8 modes
(`brane-legacy, drop, q1-base, r-side-bare, li2q, habiro, per-partition-k,
combined`) through **four separate loops**, i.e. ~32 mode-passes. Measured:

    4h 32m elapsed at 100% CPU, ~1.5 mode-passes done

which extrapolates to days. Raising working precision 15 → 50 makes mpmath
arithmetic several times slower, so this is a direct and expected consequence of
the fix — expected in kind, not in degree.

**No damage: this producer writes its witness at the END, not incrementally**,
so killing it left the committed file byte-identical. That is worth contrasting
with `rho_k_co_casimir_extended.py`, whose incremental save destroyed its
witness three times before being fixed — same interrupt, opposite outcome,
purely because of when the write happens.

So the state is: source correct, witness stale-but-honest (still the 15-dps
numbers, as committed). Whoever regenerates it needs a faster host, and should
expect **every published value in it to move** — that is the point of the drain,
not a side effect.

### Note on the remaining 44

This one took ~5 hours of compute to *not* finish. Before draining another,
check what it costs to re-run: a producer whose witness cannot be regenerated
leaves the source and the published numbers disagreeing, which is a worse state
than either fixing or leaving both. Prefer the cheap ones first — the ratchet
does not care about order.

## Cost-triaged drain: 46 → 11 producers, 206 → 44 constructions

Took the lesson from the sweep and **triaged by re-run cost before touching
anything**: ran all 45 remaining producers under a 20 s cap, timing each. That
is a cheap measurement and it changed what got worked:

    completed < 20s : 35   (most under 2s)
    timed out       :  5   (cost unknown, left alone)
    ALREADY BROKEN  :  4   (non-zero exit, not a timeout)

The four broken ones — `derived_masses.py`, `gram_matrix_seminormal_n.py`,
`hecke/hecke_engine.py`, `toffoli-lp-stability.py` — are dead producers of the
same kind as the six-term sweep and `term6_full_pole_sum`. Not touched here;
draining a producer that cannot run leaves source and witness disagreeing with
no way to check which is right.

**The triage runs write witnesses.** 24 files came back dirty and were reverted
wholesale (`git checkout -- computations/`), plus two witnesses that had not
existed before and were deleted. Shape guard clean afterwards. Worth planning
for rather than discovering: timing a producer is not a read-only operation.

### Applied to the 35 cheap ones

34 fixed (one skipped: no mpmath import to key an alias off), then **all 34
verified to import AND to actually reach dps ≥ 50 at runtime**, with mpmath
reset to 15 before each so one module's raise cannot mask another's.

One fixer bug caught by that runtime check, and it is the same alias trap as
before wearing a different hat: `canonical_mass.py` imports `mpmath as mp`
*inside a function*, so there is no module-scope `mp` to assign to and the
generated `mp.mp.dps = 50` raised `NameError`. Fixed by hand, raising dps at the
local import instead. **A module-scope insert is only valid if the binding it
uses is module-scope** — the AST walk that finds the alias must respect that.

### Then regenerated, and five witnesses were NOT kept

34 producers re-ran cleanly. Of the resulting witnesses, five were reverted
rather than committed, each caught by a gate rather than by inspection:

    COLLAPSED (shape guard)
      a4-brunnian-deficit-closed-form   durationMs 573,059 -> 4,997
      probe-4-li6-rectangular-python    payload 58 -> 36 leaves, assertions 1 -> 0
      shadow-price-c-321-q0             payload 28 -> 13 leaves (54% gone)

    REGRESSED (raw-float64 ratchet)
      atom-level-wedderburn-tower       1 -> 103 raw float64
      catalan-binding                   35 -> 47

None of the three collapsed producers takes CLI arguments, so this is not the
`--max-a` default trap from `ground-state`; the cause is unidentified and they
are left with source fixed and witness stale. The two REGRESSED are the
downstream consequence recorded earlier in this bean — raising working precision
surfaces float64 that low output precision was hiding — and they need their
serialization fixed at the producer before their witnesses can be regenerated.

### Net

    never-raises ratchet   46 producers / 206 constructions -> 11 / 44
    raw-float64            15 files DRAINED, -2,379 fields
    NEW / REGRESSED        0 / 0 from this work
    padding ratchet        13/13, 0 NEW
    shape guard            0 collapsed

The one remaining red in the family is `rho-k-co-casimir-extended` 3 -> 4, which
predates this work and is documented above as needing a ≥ 24 GiB host.

## CORRECTION — "4 already broken" was 1. The triage measured my invocation, not the producers

I recorded four producers as dead, "of the same kind as the six-term sweep", and
said reviving them was probably the bigger win. **Three of the four were fine.**
Checked one at a time instead of trusting the exit code:

    derived_masses.py            NOT broken. Raises a deliberate, well-worded
                                 FileNotFoundError: its upstream
                                 beta-decay-energy-scale.witness.json does not
                                 exist here, and the message says to run that
                                 compute first. Correct behaviour on an unmet
                                 dependency — and the upstream producer exists.

    hecke/hecke_engine.py        NOT broken. Requires CLI arguments; run bare it
                                 prints usage and exits non-zero, by design.
                                 `--all` runs it to completion.

    toffoli-lp-stability.py      NOT broken. MY HARNESS: the triage exported only
                                 tools/pyhecke/python, so `qou_substrate` was
                                 missing. With tools/qou-substrate/python on the
                                 path it exits 0.

    gram_matrix_seminormal_n.py  GENUINELY broken, and fixed here.

**The methodological point, which is the reusable part:** the triage ran each
producer bare, with an incomplete PYTHONPATH and no arguments, and recorded the
exit code. That measures *"exits non-zero under one particular invocation"*, not
*"is broken"* — and I reported the second while having measured the first. A
non-zero exit is a prompt to look, never a diagnosis.

The same caveat applies to the **5 "timed out"** entries, which I have not
re-examined: a 20 s cap says nothing about why a producer is slow, and at least
one of them may simply want arguments.

### The one real defect

    computations/gram_matrix_seminormal_n.py:245
        print(f"  λ = {lam:<24}  ...")

`lam` is a partition TUPLE, and tuple has no `__format__` accepting an alignment
spec, so this raised `TypeError: unsupported format string passed to
tuple.__format__` and killed the sweep on its first block. Fixed with
`str(lam)`; the file now runs to completion (H_6, 87.3 s).

Worth noting what kind of bug this is: **the failure is in the progress PRINT,
not the computation.** Nothing it calculated was ever wrong — the producer just
could not finish saying so. That is the same shape as the `NameError` in the
six-term sweep: a defect in code that has nothing to do with the mathematics,
sitting in a producer nothing runs.

## Re-examined the 5 "timed out" — that bucket was mostly sound (4/5)

Re-ran all five with the full PYTHONPATH (`tools/pyhecke/python` **and**
`tools/qou-substrate/python`) and a 240 s cap instead of 20 s. Only one of the
five takes CLI arguments, so "wants args" was not the explanation it turned out
to be for the *broken* bucket:

    rc=124  240s   audits/term5_aK_audit.py
    rc=0     56s   beta_ew_delta_I_conjugate_pairing.py     ← miscategorised
    rc=124  240s   garside-irrep-qvalues.py
    rc=124  240s   probes/pn_pair_two_sector_split.py
    rc=124  240s   shell_closure_phi8_correlation_test.py

So this bucket was **4/5 accurate**, against **1/4** for "already broken". Worth
recording the asymmetry rather than just the correction: a timeout is a weak
claim ("did not finish in N seconds") that mostly survives re-measurement, while
a non-zero exit is a strong claim ("is broken") that mostly did not. The bucket
built on the weaker inference was the more reliable one, because the stronger
one was reading a specific invocation as a property of the producer.

`beta_ew_delta_I_conjugate_pairing.py` completes in 56 s — it was never broken
or intractable, just past a 20 s cap chosen for speed. Drained and regenerated:

    never-raises ratchet   11 producers / 44 constructions -> 10 / 42
    raw-float64            0 NEW, 0 REGRESSED from this change
    shape guard            0 collapsed

The remaining four genuinely exceed 240 s and stay untouched, consistent with
the cost-triage rule: do not drain a producer whose witness cannot then be
regenerated.

**Housekeeping:** the re-triage left one untracked artifact,
`habiro-coefficients-nitrogen-16.witness.json`, written by a run that was then
killed at the cap (rc=124). Deleted — a partial witness from a SIGKILLed
producer is exactly the thing `witness_shape_guard` exists to catch, and it
should not be committed just because it happens to be new rather than modified.
An untracked file is easier to overlook than a dirty one.

## CORRECTION — the two "REGRESSED" witnesses were TRUNCATED, not regressed

I reverted `atom-level-wedderburn-tower` (1 → 103 raw float64) and
`catalan-binding` (35 → 47) as regressions caused by raising precision, and
recorded them as needing "serialization fixed at the producer". **Both readings
were wrong.** Comparing committed against regenerated, field by field:

    atom-level-wedderburn-tower
        COMMITTED     results: {}          — ZERO entries. 28 fields total.
        REGENERATED   results: 6 atoms     — 199 fields, 171 of them new.
        type changes between them: 0

    catalan-binding
        COMMITTED     ~97 leaves, 35 raw float64
        REGENERATED   ~224 leaves, 47 raw float64

Not a single field changed TYPE in either. The extra float64 arrives with extra
**content**: the committed witnesses are truncated, and `atom-level-wedderburn-
tower`'s publishes literally nothing — an empty `results` dict.

**And its raw-float64 baseline entry of `1` is an artifact of that emptiness.**
`witness_shape_guard`'s own docstring names this exact hazard:

> a gutted witness scores zero raw floats, which reads as a perfect drain

which is what has happened here, one step short of zero. The ratchet has been
recording a truncated witness as nearly clean, and the moment anyone completes
it the gate reads the completion as a 100-field regression.

### Why they cannot simply be completed

The float64 in these is **genuine and by construction**, not a serialization
slip. `atom_level_wedderburn_tower.py` computes in float64 deliberately:

    d_q_val   = float(dim_q(shape))
    w_lambda  = d_q_val ** 2 / float(nfac)
    phi       = float(Phi_q(phi_arg))
    descended = 0.0                       # float accumulator

So `set_compute_dps()` cannot help it — the casts discard precision after the
raise, which is a different defect from the one this bean's gate detects. My
"fix the serialization" framing was wrong twice over: the values are not
mis-serialized mpf, they are honest float64, and the way to drain them is to
**port the producer off `float()`**, which is a real job rather than a tweak.

Left as-is: source drained (both do call `set_compute_dps()` now, committed in
`254644182`), witnesses committed-and-truncated, ratchet unmoved. Completing
either requires the port first, or the completion registers as a regression.

### Method note

I twice reported a cause before checking the diff — first "serialization", then,
seeing an empty `git diff` on the producer, "my drain never touched this file"
(it had; the change was already committed, so the working tree was clean). Both
were resolved the same way: compare the two artefacts directly and count. A
witness diff is cheap and answers the question that guessing does not.


## Re-measured 2026-08-25 — WIRED, and 288 -> 22

The finding above says the audit "is **not** in `scripts/precision-gates.sh`'s
`GATES` array" and reports 288 findings / 185 proven lossy / 91 files. Both
halves have moved:

**It IS wired now.** Running `scripts/precision-gates.sh` on clean detached
`origin/main` (1259c7fdefb) reports it as a gating section and the run exits 1:

    RED: import-time dps ratchet  raw-float64 ratchet

**And the backlog has drained by an order of magnitude:**

    2026-08-10   288 findings   185 proven lossy   91 files
    2026-08-25    22 findings     2 proven lossy   12 files

So the residue is 2 proven-lossy (literal arg) and 20 position-risky (expr arg,
not statically provable). The remaining files:

    computations/borromean_binding_recompute.py                     (3, expr)
    computations/probes/one_loop_cusp_normalisation_tension_probe.py (3, expr)
    computations/substrate/q_parameter.py                            (3, expr)
    computations/probes/chirality_weighted_3body_cluster_probe.py    (2, expr)
    ... 8 more files

**Worth stating plainly for anyone reading the gate output: main is RED and has
been.** That is not a regression and not a surprise — it is this gate being
correctly wired over a backlog that was never fully drained. Verified
byte-identical on clean main and on an unrelated feature branch, so a red here
does not indicate anything about the branch under test.

Consequence for the merge discipline in AGENTS.md §"Phase-4 verification
gate": with CI dispatch-only, `precision-gates.sh` IS the gate, and it cannot
currently be used as a pass/fail signal on trunk. Until this residue is drained,
an agent verifying a branch must compare its gate output against clean main
rather than requiring exit 0 -- which is what I did for PRs #5751 and #5752.


## FIXED — the import-time dps gate is now GREEN

The 2 proven-lossy sites were both in `computations/probes/mu3_door_sign_C_vs_D_probe.py:73`:

    UPSTREAM_C3_ABS = {"T": mp.mpf("-1.769"), "3He": mp.mpf("-1.405")}

built at MODULE SCOPE, while `set_compute_dps()` was called only at line 98,
inside a function. So both mpf were constructed at mpmath's default 15 dps and
carried 15-dps binary precision for the whole run -- string literals
notwithstanding, which is the point the audit makes that a `mpf("...")` grep
would miss.

Fix is one line: call `set_compute_dps()` at module scope, before any mpf is
built. Result:

    proven lossy (literal arg)   2 -> 0
    findings                    22 -> 20
    files affected              12 -> 11
    NEW files (not baselined)    1 -> 0
    audit --strict            exit 1 -> exit 0

    precision-gates.sh   RED: import-time dps ratchet raw-float64 ratchet
                      -> RED: raw-float64 ratchet

That file was the ratchet's only NEW (non-baselined) entry, which is why one
line cleared the gate: the ratchet keys on NEW/REGRESSED, not on the total. The
20 position-risky (expr arg) sites remain and are NOT a gate failure -- they are
baselined backlog needing per-site judgement about whether the expression is
evaluated before precision is raised.

## The OTHER trunk red is not mine and I did not identify it

`raw-float64 ratchet` remains red on main with:

    NEW dirty witnesses : 5
    REGRESSED           : 0

I did not determine WHICH five. The audit has no flag that lists them and my
attempt to diff the current dirty set against `raw-float64-baseline.json`
(1409 entries) failed -- my extractor did not match the witness's structure and
reported 0 current dirty, which is obviously wrong. Stating that rather than
guessing. Whoever picks this up needs those five names first; `REGRESSED: 0`
says nothing got worse, so this is 5 additions someone made without draining.


## CORRECTION 2026-08-25: the five ARE listed, by the audit itself

The section above says "The audit has no flag that lists them" and recommends
whoever picks it up build an extractor. **That is wrong, and the extractor is
unnecessary.** `witness_raw_float64_audit.py` prints the names in its own stdout,
unprompted, immediately under the count:

      NEW witnesses carrying raw float64 — fix AT THE PRODUCER
      (carry mpmath.mpf from the source, serialize with _precision.fmt),
      then re-run it. Do NOT add the file to the baseline to silence this.
            42  computations/deltalambda/deuteron-interface-handle-curvature.witness.json
            28  computations/qbeta/birkhoff-barodd-pythagoras-bridge.witness.json
            21  computations/qbeta/a3-branching-asymmetry-vs-required.witness.json
             4  computations/deltalambda/yekutieli-trefoil-surface2form-discretization.witness.json
             1  computations/deltalambda/sigma1cubed-seifert-surface-term.witness.json

No flag, no baseline diff, no extractor. `--help` does not advertise it, which is
presumably how the earlier attempt went to the baseline instead -- worth noting as
the actual lesson: the tool answered the question in its default output while the
search was for an option to make it do so.

## Disposition of the five (2026-08-25)

All five producers are PROBES, landed 2026-08-02/09 -- i.e. BEFORE the
2026-08-18 AGENTS.md "PROBES ARE NOT EXEMPT" directive. Pre-directive debt, now
caught by the ratchet. Four were genuine float64 compute; one is an audit
over-flag.

FIXED (ported to mpf end to end; 0 raw floats remain in each witness):
  ffb57ab2d  a3-branching-asymmetry-vs-required        worst move 7.2e-16
  808156bb4  birkhoff-barodd-pythagoras-bridge         worst move 3.4e-16
  ca3fd097c  yekutieli-trefoil-surface2form            worst move 1.3e-16

  Every movement is at the float64 floor and no boolean verdict flipped, so
  these are honesty/serialization fixes, not corrections -- the old numbers were
  right to the digits the old arithmetic could hold.

BLOCKED -> bean qou-8xb1:
  deuteron-interface-handle-curvature (42 fields). Calls
  `hecke_characters.build_seminormal_matrices`, which coerces `q` to float at
  the INPUT (line 168) and allocates `np.zeros((dim,dim))` (line 228). Measured:
  passing an mpf q returns BIT-IDENTICAL output to passing an f64 q. It is the
  qou-d8gq failure mode surviving in the sibling builder -- qou-d8gq fixed
  `pyhecke/syt_prefix_cache.py` only. 102 consumers under computations/, 65
  emitting witnesses. NOT fixable by wrapping fmt() around the outputs: that is
  the float64-padding defect by construction.

AUDIT OVER-FLAG -> bean qou-hhm3:
  sigma1cubed-seifert-surface-term (1 field). The producer already computes in
  mpf; the single finding is `elapsed_sec = 0.001`, a wall-clock timer with no
  mpf source to have lost digits from. Same argument qou-xt5l accepted for
  integral floats.

NET: NEW dirty witnesses 5 -> 2. The ratchet stays red on main until qou-8xb1
lands; that is a real infra decision (qou-d8gq measured honest mpf matmul at
642x slower), not a drain.

Also corrected while here: the note above reads "this is 5 additions someone made
without draining". Accurate as far as the ratchet goes, but the four real ones
predate the directive that made them defects, so "without draining" reads more
culpably than the history supports.


## "The recorded mpmath version" is not one fact -- it is per-witness

The handoff into this session said re-runs could not settle anything because
"this container has mpmath 1.3.0 against the recorded 1.4.1". Measured across
the 3088 committed witnesses under `computations/`:

    recorded mpmath 1.3.0 : 1201 witnesses
    recorded mpmath 1.4.1 :  702 witnesses
    recorded 0.0.0        :    2

There is no single recorded version to be matched or mismatched. This container
has 1.4.1, so it matches 702 and differs from 1201 -- and the four AUDIT
witnesses the gate rewrites record 1.3.0, i.e. the opposite direction from the
one the handoff named.

The handoff's CONCLUSION still stands (do not regenerate those audits here) but
for a different and stronger reason, which is the one qou-hlp5 already gives:
this container is missing **scipy, sympy and clarabel** entirely. Verified by the
tell qou-hlp5 documents -- the dependency list SHRINKS in the regenerated
witness:

    -    "scipy": "1.17.1"
    -    "sympy": "1.14.0"
    -    "clarabel": "0.11.1"
    -    "mpmath": "1.3.0"   ->   +    "mpmath": "1.4.1"

Practical rule: check the environment block of THE witness you are about to
regenerate, not a remembered version number. `mpmath` alone was installable here
(pip, 1.4.1) and was enough to re-run the three pure-python probes, whose
witnesses carry no scipy/sympy/clarabel dependency at all.
