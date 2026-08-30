---
# qou-fsva
title: 'Close the AME drain''s verification tail: 4 unverified producers, 6 stdout-only, fr_pullback deferred'
status: completed
type: task
priority: normal
created_at: 2026-08-30T06:24:05Z
updated_at: 2026-08-30T09:05:56Z
---


The TARGET drain (3b5c12537) verified 42 of 53 producers by re-running HEAD in
a worktree and comparing witnesses leaf-by-leaf. Eleven were left uncovered.
This bean closes all of them.

- [x] 4 producers reported as "fail identically at HEAD" — 2 were the harness, 2 were real bugs; all four now run and compare
- [x] 6 stdout-only producers — stdout IS the artifact; all six diffed, each shows only the routed value and what derives from it
- [ ] fr_pullback_borromean_h3a_test, deferred as too slow to pair

## FIRST FINDING: two of the four were the HARNESS, not the code

The repo runs producers with a PYTHONPATH that .github/workflows/lp-dual-gate.yml
and scripts/precommit-precision-warn.sh both spell out:

    computations:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate

The verification sweep ran them bare. Under the documented path,
probe_isospin_mirror_v9_generalization and from_scratch/derive_t_h5 both exit 0.
They were never broken; they were run wrong, on both sides, which is exactly why
they looked symmetric and therefore pre-existing.

Two are genuinely broken and stay broken under the documented path:
  d_from_scratch                       FileNotFoundError -- reads
                                       computations/habiro-coefficients-atomic.witness.json
                                       but the file is in computations/habiro/
  deltalambda_binding_cross_isotope    dim_q() takes 1 positional argument but 2 given

## CHECKED: the bare environment did not change what got imported

Two copies of codata_constants.py exist (computations/substrate/ and
qou-mass/src/qou_mass/_internal/). If a producer had resolved a different one
under the sweep than it will in CI, the verified behaviour would not be the
shipped behaviour. Probed all 53 under both environments: 52 resolve to the same
file with the same AME values, and the 53rd differs only in how the probe
harness itself failed. The existing verification stands.

## SECOND FINDING: the roadmap's REVIEW class was mostly a stalled trace

383 of the 389 REVIEW sites were "bound to an AME literal, but no role signal".
That is not ambiguous code — it is a taint that stops one hop too early. The
corpus writes `B_AME = 2.224566`, then `b_exp = B_AME`, then
`err_pct = (pred - b_exp) / b_exp`; the classifier tainted only `B_AME`, saw
`b_exp` as a sink with no signal, and gave up.

Closing the taint over ALIASES (bare name, trivial wrapper, subscript of a
tainted AME table) — but deliberately NOT over arithmetic, because a derived
quantity's name IS the signal — moved 97 sites:

    before   TARGET   0 / 0    INPUT   0 / 0    REVIEW 389 / 140
    after    TARGET  79 / 27   INPUT  18 / 5    REVIEW 292 / 108

INPUT IS NOT ZERO. The drain commit (3b5c12537) said "the 3-cal blocker is not
in this tail" on the strength of INPUT = 0. That reading was an artifact of the
stalled trace. probes/binding_mayer_linked_cluster_probe.py:

    b2 = AME["D"]                 # measured deuteron binding
    pred = comb(A[k], 2) * b2     # a PREDICTION built from it
    ... vs AME[k]                 # compared against the measurement

Committed as ee596db88 with three self-test cases, including an alias chain that
hides a calibration — the case that makes the closure load-bearing.

## The repr/Decimal defect class, caught by scan this time

Round 1 found `repr(mpf)` writing "mpf('28.29...')" into a witness only by
diffing two runs; the producer exited 0. Round 2 scanned for the shape first and
found 8 `Decimal(mpf)` sites in 2 files before running anything. Both fixed by
str() first. The scan is cheap and belongs ahead of every drain round.

## THIRD FINDING: taint must cross loop unpacking, and must do it POSITIONALLY

The corpus keeps AME values in row tuples:

    ISOTOPES = [("D", 1, 1, 2.22456612, "1·m_e·Vol(6_2)", m_e * VOLS["6_2"]), ...]
    for label, Z, N, B_AME, formula, leading in ISOTOPES:
        leading_err_pct = (leading - B_AME) / B_AME * 100

Taint that cannot cross the unpack stops at ISOTOPES, which is never itself in
arithmetic — so the file reads as a value that is merely recorded when it is the
comparison target of the whole probe.

Tainting EVERY loop variable fixes that and introduces a new error: `Z`, `N`,
`A`, `row`, `_` join the sink census, and INPUT jumped 18 -> 40. Thirteen of
those were false, manufactured out of loop counters. Reading the row tuples and
tainting only the slot that actually holds the AME literal brought INPUT back to
27 and left TARGET measurable.

    alias only          TARGET  79 / 27   INPUT  18 / 5    REVIEW 292 / 108
    + unpack (all)      TARGET 103 / 29   INPUT  40 / 12   REVIEW 167 / 72
    + unpack (slot)     TARGET   0 / 0    INPUT  27 / 8    REVIEW 170 / 73

TARGET reaches 0 because rounds 2-4 drained it as it appeared.

## REVIEW WILL NOT GO TO ZERO BY CLASSIFIER, AND SHOULD NOT BE FORCED TO

164 of the remaining sites use the AME value in arithmetic under 136 DISTINCT
result names — near one per site. That is case-by-case physics, not a missing
pattern.

A structural 3-cal detector was prototyped and REJECTED: taint the AME value,
close over arithmetic to get "derived" names, then flag any comparison mixing a
derived name with a tainted one. It reports 17 files / 57 sites, and the hits
include `magic_A_formula.py:146  B_pred - B_AME` (an ordinary residual) and
`mpf_import_time_dps_audit.py:349  list(cases) + scan_cases` (list
concatenation). "Derived meets tainted in a BinOp" is what every residual looks
like. Shipping it would have reported 57 fresh 3-cal violations that are not
violations.

The honest closure: the roadmap routes attention, it does not adjudicate. It got
much better at routing (389 -> 170 REVIEW, and a real INPUT class where there
was none). The residue is a reading task, and pretending otherwise by loosening
a regex until the number hits zero would be the one failure this roadmap exists
to prevent.

## Closure of the four

  probe_isospin_mirror_v9_generalization  HARNESS (missing PYTHONPATH). Running
      it correctly then exposed a REAL regression from the drain:
      `D(AME_B_..._VALIDATION)` — Decimal(mpf) raises TypeError, and HEAD passed
      a string there. Fixed with D(str(...)). Witness now compares: 32 leaves
      same, 25 moved, all three routed constants and the err_pct fields they
      feed, max 7.73e-6 on a residual.
  from_scratch/derive_t_h5                HARNESS. stdout differs only in
      timing lines; the tritium move (2.12e-7) is below printed precision.
  d_from_scratch                          REAL: read
      habiro-coefficients-atomic.witness.json from computations/ when it lives
      in computations/habiro/. Fixed. Both sides now run; only B_AME_MeV
      (3.60e-8) and err_pct (1.79e-7) move.
  deltalambda_binding_cross_isotope       REAL: c86e55ec9 changed the call site
      to dim_q(lam, Q0_PROTON) and added the import but never gave dim_q the
      parameter. Broken on every run since. Threading q through is numerically
      identical to dropping the argument (q_at(40) IS the proton pin), so the
      fix does not turn on a judgement call. Its three failing assertions are
      PRE-EXISTING: applying only the bug fix to HEAD reproduces them exactly,
      and MINE differs from HEAD by one digit in `t` — the tritium constant.

## A witness deliberately NOT committed

d-from-scratch.witness.json regenerates with python 3.11.15 where the committed
copy records 3.12.3. The numbers are right and the provenance is weaker, which
is exactly what the repo's own stamp warns about. The .py fix is committed and
the witness is left alone: the staleness detector will then correctly ask for a
re-run in an environment that is not a downgrade. Checked all dirty witnesses —
this is the only one affected.

## The mpf-substitution defect taxonomy

Routing a literal to the registry changes its TYPE: a `str` or `float` becomes
an `mpf`. Every defect found across four drain rounds is that one change meeting
a call site that assumed the old type. Three classes, in descending nastiness:

  SILENT   `repr(mpf)` -> "mpf('28.2956624...')" where repr(float) wrote a
           number. Producer exits 0, witness looks fine until the field is
           parsed. Found only by diffing two runs (alpha_k_jones_markov_h12).

  LOUD     `Decimal(mpf)` raises TypeError; `mp.mpf(repr(mpf))` raises
           ValueError because the repr is not a number. Found by running --
           but only under the CORRECT PYTHONPATH, since a bare run failed
           earlier for an unrelated reason and looked symmetric.

  LATENT   `json.dump(...)` with no `default=` raises the first time an mpf
           reaches the payload -- which may be a branch the sweep does not
           take. Found by scanning for the shape, not by running: 10 drained
           producers had a bare json.dump, and only 3 of them had surfaced as
           failures.

SCAN BEFORE YOU RUN, AND SCAN WITH THE REAL TAINT. A one-hop taint (names bound
directly to a `*_VALIDATION` expression) misses `B_AME = AME_BINDING.get(name,
0.0)`, which is exactly where mass_table_comprehensive's `mp.mpf(repr(B_AME))`
lives. The scan now reuses the triage's own alias closure. It reports 24 sites,
of which one was real and the rest are benign (`round(mpf, 6)`, `"{:.4f}".format
(mpf)` and `int()` on genuinely-integer dict fields all behave) -- a false
positive rate worth paying for a class that otherwise ships silently.

The scan is `scratchpad/risky_scan.py <targets.json>`; it is a scratch tool, not
committed, but the shape is written down here so the next round does not
rediscover it by burning a sweep.

## Summary of Changes

All eleven uncovered producers are now verified, plus five more that surfaced
while closing them.

**fr_pullback_borromean_h3a_test** — the deferred item. It was not merely slow:
it has raised `TypeError` on every run since c86e55ec9, which changed four call
sites to `dim_q(s, Q0_PROTON)` and added the import but never gave `dim_q` the
parameter. It computes for ~80 minutes before reaching the broken call, which
is why nothing caught it. An AST arity audit over the whole corpus found the
same half-finished edit in `probe_chirality_delta_lambda_the3_diagnostic` and
(fixed earlier) `deltalambda_binding_cross_isotope_probe`; no other call/def
mismatch exists. All three now accept the argument and CHECK it against the
factory's q rather than ignoring it.

**Four witnesses had no same-named producer** — the stem heuristic failed on
case (`binding_sum_C_vs_D_per_isotope_probe.py` writes
`binding-sum-c-vs-d-deut.witness.json`). Each witness records its own producer
in `scriptFile`; that is the reliable mapping. All four re-run and compare
clean: 0 unexplained leaves.

**catalan_binding** is not an empty witness. It writes 11KB with 0 assertions,
and its rc=1 is a pre-existing raw-float64 guard failure — 35 float64 fields
entering the witness where the guard wants mpf carried through `_precision.fmt`.
Symmetric at HEAD, unrelated to the drain, left alone.

**pn_alpha_lp_dual cannot be verified by re-running at all.** It runs
scipy.linprog and an SCS solve. HEAD against ITSELF — same code, two runs —
differs in 2320 leaves, 402 of them beyond the drain bound, which is exactly the
count that had been attributed to the routing. Its dual variables are not
reproducible run-to-run.

**A third of the baselines were stale.** 33 of 64 dirty witnesses were being
compared against the COMMITTED copy rather than a same-container re-run — the
unsoundness the whole exercise exists to avoid. `binding_per_bond_decomposition`
looked like a real regression (a "29% gap" becoming "24%") purely because its
HEAD witness predated the container.
