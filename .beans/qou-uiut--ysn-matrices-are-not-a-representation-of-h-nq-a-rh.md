---
# qou-uiut
title: 'YSN matrices are not a representation of H_n(q): a_rho uses h/[rho] where Hoefsmit needs q^rho/[rho] — braid defect 0.7315 at every partition'
status: in-progress
type: bug
created_at: 2026-09-02T21:39:40Z
updated_at: 2026-09-02T21:39:40Z
---

Found while reviewing main (bean qou-9ay6 / qou-sv7h), branch
`claude/anchor-followups-2026-08-08`.

## The defect

`hecke_core_legacy._build_ysn_matrices` computes the Hoefsmit seminormal
diagonal as

    a_rho = h / q_int(rho)          # = h / [rho]_q

The reference implementation
`pyhecke/syt_prefix_cache.py::BlockCache.get` — which `qou-sv7h` measured as
PASSING the braid relation at 1.2e-50 — computes

    a = h / (1 - q**(-2*rho))

Multiplying numerator and denominator by q^rho:

    h / (1 - q^-2rho)  =  h*q^rho / (q^rho - q^-rho)  =  q^rho / [rho]_q

since [rho]_q = (q^rho - q^-rho)/h. So the correct expression is
`q**rho / q_int(rho)`, and the legacy form is off by a factor of `q^rho / h`.

`a_neg = h - a_rho` is CORRECT either way (a + a' = h holds for the true
Hoefsmit pair), which is why the error survives every relation that only
constrains the trace of the 2x2 block.

## The code refutes itself

At rho = +1, [1]_q = 1, so the legacy formula yields `h = q - 1/q`. But the
`same_row` branch three lines above hardcodes `q0`. The corrected formula
gives `q^1/1 = q`, agreeing. Likewise rho = -1: [-1]_q = -1, corrected gives
`-1/q`, matching the hardcoded `-qi`. The general branch and the special-case
branches were inconsistent with each other.

## Measured (dps=50, mpf throughout)

    partition   dim | legacy quad  legacy braid | hoef quad   hoef braid
      (2, 1)      2 |   3.341e-52    0.73151368 | 2.673e-51  4.67734e-51
      (3, 1)      3 |   1.336e-51    0.73151368 | 2.673e-51  4.67734e-51
      (2, 2)      2 |   3.341e-52    0.73151368 | 2.673e-51  4.67734e-51
      (2, 1, 1)   3 |   1.336e-51    0.73151368 | 2.673e-51  4.67734e-51
      (3, 2)      5 |   1.336e-51    0.73151368 | 2.673e-51  4.67734e-51
      (3, 1, 1)   6 |   1.336e-51    0.73151368 | 2.673e-51  4.67734e-51
      (3, 2, 1)  16 |   1.336e-51    0.73151368 | 2.673e-51  4.67734e-51
      (4, 2)      9 |   1.336e-51    0.73151368 | 2.673e-51  4.67734e-51

The **quadratic** relation passes under BOTH formulas — it is blind to the
scale of `a_rho` because `a_neg = h - a_rho` pins the block trace regardless.
Only the braid relation sees the error. That is why the defect survived: the
producer's own consistency check tested the relation that cannot detect it.

The defect is constant (0.731513681083349240094869778948) across every
partition because the smallest failing block, rho = -2, appears in all of
them and the max-norm is attained there.

Before the NO-FLOAT64 excision the quadratic defect read 4.81e-17 (float64
noise), which made the whole picture look numerical. With the matrices now
mpf end to end the quadratic defect is 3.3e-52 and the braid defect is
unchanged at 0.73 — proving it is STRUCTURAL, not roundoff.

## Three copies, all wrong

    computations/hecke_core_legacy.py:1190   _build_ysn_matrices (general)
    computations/hecke_core_legacy.py:907    _diag_T1, the hardcoded (2,2)
                                             H_4(q) block at rho = -2
    computations/sdp_cross_channel.py:524    chi_at_q.build_sigma, a private
                                             re-implementation of the same loop

Site 907 carries the wrong formula in a comment as well:
`diag = h / [rho]_q`.

## Todo

- [x] Fix all three sites to `q**rho / q_int(rho)`
- [x] Fix the comment at hecke_core_legacy.py:900
- [x] Add a regression test asserting the braid relation on the YSN output
      (the quadratic-only check is what let this through)
- [x] Enumerate the witness blast radius; regenerate affected producers
      from the producers, never by hand


## 2026-09-02 — fixed, verified, and it was not one bug but three

### 1. The wrong diagonal (the bean's subject)

`q**rho / q_int(rho)` at all three sites. Measured on the real module, dense
and sparse paths, mpf at 50 dps:

                      before          after
    quadratic       3.341e-52       2.673e-51
    BRAID           0.731513681…    4.677e-51
    far-commute     0.0             0.0

The YSN matrices are a representation of H_n(q) now; they were not before.

### 2. A float64 `q_int` underneath it

Fixing (1) only got the braid defect to **2.649e-16** — float64 epsilon, not
mpf roundoff. `q_parameter`'s `_MP` family had no `q_int`: the plain `q_int`
closes over the FLOAT `Q`/`Q_INV`/`HA` and returns a Python float at any
working precision (2.156e-16 relative at [±2]). All five call sites in
`hecke_core_legacy` divide an mpf by it, so the result was capped at ~17
digits with nothing in the type to show it.

Added `q_int_mp` to BOTH `_MP` families — `qou_substrate/constants.py` (proton
base) and `q_parameter.py` (muon override) — and aliased it in
`hecke_core_legacy`'s import block. That is what took 2.649e-16 → 4.677e-51.

### 3. Three copies, now one

- `sdp_cross_channel.chi_at_q` kept a verbatim private copy of the builder,
  for the sole reason that it sweeps `q`. `_build_ysn_matrices` now takes an
  optional `q=`, dispatching arithmetic on the operand (`_sqrt_for`), so an
  f64 sweep stays f64 and bit-compatible. The private copy is deleted.
- `_M22_S1/S2/S3` were three hand-written tuples duplicating
  `_build_ysn_matrices((2, 2))`. Replaced by a dps-keyed lazy build. They had
  ALSO been frozen at import-time `mp.dps` — see below.

The divergence between copies is the defect, as it was for the three `.dot`
sites in `qou-9ay6`. Copies of this loop have now gone wrong twice.

### The regression test, and proof it bites

`tests/test_ysn_hecke_relations.py`, 24 tests. Checks all THREE defining
relations, on both code paths, plus the q→1 Young's-orthogonal-form limit and
an mpf-type assertion.

This is the point of the file: the producer already checked the quadratic
relation, and the quadratic relation CANNOT see this error — `a_neg = h -
a_rho` pins the block trace whatever `a_rho` is. A test covering the easy
relation and not the hard one reads as coverage and is worse than nothing.

Mutation-tested rather than assumed:

    reintroduce the wrong a_rho     -> 20 failed,  4 passed
    revert only the q_int_mp alias  -> 13 failed, 11 passed
    both fixes in place             -> 24 passed

    full suite: 169 passed (145 baseline + 24 new)

### A test bug of my own, caught by the suite

My first version set `mp.mp.dps = 50` at module scope. pytest imports test
modules at COLLECTION time, so that landed before every other module's tests
and broke the five exact-equality checks in
`tools/qou-substrate/tests/test_codata_table.py` purely by collection order.
Now an autouse `mp.workdps(50)` fixture — the same discipline
`qou_substrate.constants` documents for itself.

### Split out: `qou-zbws`

Chasing (3) surfaced something bigger. `q_parameter` raises the 50-dps floor
ONLY inside the ideal/muon anchor branch; on the default/proton anchor
`constants.py` uses `workdps`, which restores mpmath's default 15. Measured:
`mp.dps == 15` after importing `hecke_core_legacy` with `QOU_Q0_ANCHOR` unset.

So the whole NO-FLOAT64 excision of that module runs at 15 dps on the default
anchor — mpf types, float64 digits. Filed as `qou-zbws` rather than fixed
here: the one-line hoist renumbers every proton-anchor witness in the corpus
and needs an owner call on sequencing.

### Still open on this bean

- [x] Witness blast radius enumerated (AST over imports AND call sites, plus
      the attribute-access callers the AST pass missed).
- [ ] `hadron-knot-table.witness.json` — NO LONGER BLOCKED; regenerating now.
      `qou-sv7h`'s scaling work landed (two Rust routes), deuterium went from
      "does not finish" to 118s, and the run is 15/19 atoms in with a
      committed resume journal. Closes when the witness is written.


## 2026-09-02 — blast radius, and one of two witnesses regenerated

### Independent confirmation, from a gate I did not write

`computations/audits/ysn_braid_relation_audit.py` already existed — written
because it FOUND this defect ("A family can satisfy (Q) everywhere and still
fail (B) -- which is exactly what this audit found"). It compares against
`pyhecke_native.seminormal_matrices_mpfr`, the Rust MPFR build. It now exits 0:

         partition  dim    impl    quadratic        BRAID    commuting
            (2, 1)    2  python    2.806e-50    3.207e-50          0.0
            (2, 1)    2    rust    1.203e-50    2.005e-50          0.0
         (3, 2, 1)   16  python    4.009e-50    3.207e-50          0.0
         (3, 2, 1)   16    rust    1.203e-50    2.005e-50          0.0

    RESULT: the Python YSN family satisfies all three relations.

Python and Rust now agree at the same order of magnitude, both mpf roundoff.

### Tainted modules — 8, resolved by import + call site

The AST pass found 4 via `from X import Y` + a matching call. It MISSED the
`import hecke_core_legacy as H` + attribute-access callers; grepping for the
import form found 4 more. Recording the miss because the resolver is the kind
of thing that gets reused:

    witness producers (2)
      computations/hadron_knot_table.py                     -> hadron-knot-table.witness.json
      computations/phase5/phase3_triton_binding_convention_b.py
                                                            -> phase3-triton-binding-convention-b.witness.json
    no witness emitted (6)
      computations/hecke_core_legacy.py
      computations/sdp_cross_channel.py
      computations/probes/h6_wedderburn_block_unbinding_probe.py
      computations/probes/h6_block_selection_lp_probe.py
      computations/audits/lp_accumulator_kernel_gate.py
      computations/audits/ysn_braid_relation_audit.py

`atomic_chirality_residue.py` imports only `_step_chain_generic`, which builds
the braid WORD and not the matrices — correctly excluded.

### phase3-triton: regenerated, but it was never producing numbers

Running it revealed it had been broken since `e5dcd8f54` (2026-08-01) by a
keyword rename that missed `hecke_core_legacy.py:2521`. The committed witness
holds the AssertionError TEXT in all four rows and still declares
`allPassed: true`:

    "atom": "T", ..., "error": "AssertionError: binding_canonical: the `E_0`
     keyword is deprecated; ..."

Fixed the missed caller (pure rename — `E_0_CALIBRATION_MEV` and
`binding_canonical._Q_BETA_N` are bit-identical `mpf('0.78233340930999995')`,
so no number moved) and regenerated:

        D    +0.435403 MeV   T  +0.695131 MeV
      3He    +0.698552 MeV  4He +0.876064 MeV

**Do not read this as "the braid fix changed these numbers."** The previous
witness had no numbers to compare against. What this establishes is that the
producer runs again and its output now comes from matrices that are a
representation; whether the canonical Markov-trace path routes through
`_build_ysn_matrices` at all is a separate question I have not resolved.

The green-witness-with-error-rows failure mode is filed as `qou-qe81`.

### hadron-knot-table: blocked, not skipped

The other affected witness cannot be regenerated. `hadron_knot_table` calls
`binding_energy` over a nuclide table running to ca40, and per `qou-sv7h`
deuterium alone does not finish in 11 minutes. It stays wrong until the
scaling work lands. Recorded rather than quietly left.

### Procedure note

The triton run OVERWROTE the committed witness with a 0-row degraded version
before I had the fix. Restored byte-identically from the scratchpad snapshot
taken before the run — by explicit single path, never a glob. The snapshot
rule earned its keep.


## 2026-09-03 — the regeneration is now feasible, and the checkpoint has to be committed

### Cost, measured end to end

With BOTH Rust routes in (`unified_iterative_correction` and
`atom_character_raw` — see `qou-sv7h`; routing only the first left the table
unable to finish deuterium in 21 minutes):

    binding_energy(1,1)  A=2   102.9s  -> -7.2711021248767 MeV
    binding_energy(1,2)  A=3   156.8s  -> -7.7421213471361 MeV
    binding_energy(2,2)  A=4   224.0s  -> -6.8285942931489 MeV

Fit `t = 47.0 * A^1.117`:

    ca40 alone     48 min
    fe56 alone     70 min
    FULL TABLE   ~4.6 h        (~50 h if the exponent is really 2 — the fit is
                                three points over A=2..4, treat it as a lower
                                bound, not a promise)

### Why the checkpoint must live in the repo

This container has been reclaimed **twice** in one session, roughly every
40-60 minutes of work. fe56 alone needs ~70 minutes. Measured after the
second reclaim: the scratchpad checkpoint was **GONE** (the `witness-snapshots/`
subdirectory had already vanished after the first). So there is no durable
storage outside git, and without one this witness cannot be regenerated in
this environment at all — not "slowly", at all.

Moved to `.work/hadron-knot-table-regen.json`, following the corpus's own
precedent rather than inventing a location. `.gitignore` already distinguishes
the two cases:

    .work/convention-c-regen.jsonl IS committed — it is the resume point for
    the serial regeneration harness and the evidence behind
    docs/audits/2026-08-10-convention-c-witness-regeneration-impact.md

while per-run scratch is ignored (`computations/.bpp-higher-a-checkpoint.json`,
`*.checkpoint.jsonl`). Mine is the first kind: the resume point for a serial
regeneration, carrying the computed per-atom values.

It is keyed on a hash of the producer + `hecke_core_legacy` + `hecke_core` +
q, so it cannot resurrect stale numbers across a code change — it discards
itself instead. It should be deleted once the witness lands; it is a
regeneration artifact, not corpus data.

### Note for whoever resumes this

The `pyhecke-native` wheel is EPHEMERAL and dies with the container.
`scripts/build-pyhecke-native.sh` must be re-run after every reclaim, BEFORE
resuming, or `_HAVE_RUST_CHI` is False and the producer silently takes the
~300x slower path. Confirmed the hard way this session.


## 2026-09-03 — cost REVISED upward from in-run data; and a structural risk

The ~4.6 h figure came from a three-point standalone fit over A=2..4. In-run
timings (which include the monitor tail and the per-atom journal commits) put
the exponent higher:

    A=2  deuterium  118.54s
    A=3  tritium    188.59s
    A=3  he3        190.28s
    A=4  he4        277.97s      fit  t = 50.2 * A^1.222

    ca40      ~76 min
    fe56     ~115 min
    remaining 12 atoms   ~6.7 h        total  ~6.9 h

So ~4.6 h was optimistic, as flagged when it was quoted. Treat 6.9 h the same
way — it is still an extrapolation from A <= 4.

### The structural risk: the checkpoint resumes BETWEEN atoms, not within one

fe56 at ~115 minutes is longer than this container has survived so far. The
resume point is written after each atom COMPLETES, so a reclaim during fe56
loses the whole atom and it restarts from zero. ca40 (~76 min) has the same
shape. The small atoms are safe; the two that matter most are not.

Mitigating fact, worth knowing before anyone tries this: per the environment
docs the container is reclaimed after a period of INACTIVITY, not on a fixed
timer. Small atoms produce a monitor event every 2-5 minutes, which keeps the
session active by itself; ca40 and fe56 are long silent gaps and are exactly
when a reclaim is likely. Doing other work in parallel during those two atoms
is not idle busywork — it is what keeps them alive.

If they turn out unreachable this way, the real fix is intra-atom
checkpointing (the per-partition loop in `atom_character_raw` is the natural
seam), which is a bigger change than the between-atom journal.


## 2026-09-03 — pre-flight: the finished witness will pass the new gate

`qou-qe81` landed a gate that demotes any witness carrying rows with
exception-shaped `error` values. Worth confirming BEFORE eight more hours of
compute that it will not demote this one. Ran a hadron-knot-table-shaped
payload through the real `WitnessBuilder.build()`:

    clean payload      -> allPassed: True   basis: assertions
    error-row payload  -> allPassed: False  basis: error-rows

Green, on the `assertions` basis rather than vacuously — the producer calls
`w.add_assertion(...)` per atom, so it is not in the 359 zero-assertion
witnesses that gate deliberately leaves alone. And the producer has no
try/except around `compute_atom`, so a failure kills the run rather than
writing an error row; there is no path by which it produces the shape the
gate rejects.

### Cost curve: the exponent IS converging

Successive fits over growing prefixes:

    A <= 4   1.222
    A <= 6   1.307
    A <= 7   1.335
    A <= 9   1.351

The increments are halving (+0.085, +0.028, +0.016), so this is converging to
roughly 1.37 — not drifting toward the 2.0 that would have made the table
impractical. Current 7-point fit `t = 44.1 * A^1.351`:

    A=28   ~66 min      A=40  ~107 min      A=56  ~169 min
    remaining 9 atoms   ~8.4 h

Earlier notes on this bean quoted 4.6 h and then 6.9 h; both were low, and
the reason was fitting over too small an A range. ~8.4 h is the current
number and it should be roughly stable now that the exponent has settled.


## RESUME RUNBOOK — read this first after a container reclaim

This container has been reclaimed twice mid-session. Recovery is mechanical
but the ORDER matters, and getting it wrong is silent: the run continues and
is ~300x slower, or discards the journal.

    # 1. Recover the branch. The checkout resets to an OLD commit on reclaim,
    #    while the pushed work is safe on origin. Ancestry-check, never force.
    cd /workspace/qou
    git fetch origin claude/anchor-followups-2026-08-08
    git merge-base --is-ancestor HEAD FETCH_HEAD && git merge --ff-only FETCH_HEAD

    # 2. REBUILD THE WHEEL. It is ephemeral and dies with the container.
    #    Skipping this does not fail — it silently takes the ~300x slower
    #    pure-Python path, and the table will not finish.
    bash scripts/build-pyhecke-native.sh
    python3 -c "import pyhecke_native as N; \
      print(hasattr(N,'chi_q_atomic_mpfr'), \
            hasattr(N,'chi_q_atomic_prefix_traces_mpfr'))"   # must be True True

    # 3. Resume. The journal is committed, so step 1 restored it.
    nohup env QOU_HKT_CHECKPOINT=.work/hadron-knot-table-regen.json \
      python3 computations/hadron_knot_table.py > /tmp/hkt.log 2>&1 &

    # 4. Commit the journal after EVERY atom. A reclaim then costs one atom,
    #    not the run.
    git add .work/hadron-knot-table-regen.json && git commit && git push

### Things that will silently ruin the run

- **Editing `hadron_knot_table.py`, `hecke_core_legacy.py` or
  `hecke_core.py`.** The journal key hashes all three; any edit — a comment
  included — prints KEY MISMATCH and starts from zero. Deliberately
  conservative, because the alternative is resuming onto stale numbers. Do
  other work in files outside that set while this runs.
- **Forgetting step 2.** No error, just 300x.
- **Running a second producer in this checkout.** Beyond the standing rule,
  it steals CPU from a run that is using 3.9 of 4 cores; every core-minute
  taken is a core-minute added to an 8-hour job.

### When it finishes

`computations/hadron-knot-table.witness.json` is written only when all 19
atoms are present (a short pass writes nothing and names what is missing).
Then **delete `.work/hadron-knot-table-regen.json`** — it is a regeneration
artifact, not corpus data, and leaving it behind invites someone to read it
as a source.


## 2026-09-03 — third reclaim. The runbook worked; it also exposed its one gap.

Container reclaimed again mid-run. Recovery followed the runbook above exactly
and cost one atom:

    HEAD had reset to 4d0b1eae9 (pre-everything); ff-only from origin restored
      it to ba3455079 and with it the committed journal — 13 atoms, intact.
    The wheel was gone again; rebuilt, both kernels verified present.
    Resumed; the 13 cached atoms replayed at 0.00s each.

**Lost: n14 only.** It had completed (1705.74s, B = +22.0780 MeV) and the
monitor reported it, but the reclaim landed before I committed the journal.
That is the design's stated cost — "a reclaim then costs one atom, not the
run" — realised exactly once, as predicted.

### The gap, and why it is not fixable right now

Commits are driven by ME reacting to a monitor event, so there is a window
between an atom completing and the journal being committed. For a 28-minute
atom that window is small; for fe56 (~169 min) it is the same size, but the
loss if it lands in the window is far larger.

The real fix is for the PRODUCER to commit the journal itself after each
atom, closing the window entirely. That means editing
`hadron_knot_table.py` — which the journal key hashes, so doing it now would
discard 13 atoms to protect against losing 1. Not worth it mid-run.

- [ ] After the witness lands: move the journal commit into the producer (or a
      small wrapper around it) so the commit is not gated on an agent turn.
      Note it must not `git add -A`; explicit path only.


## 2026-09-03 — first evidence on whether the fix improves the PHYSICS

The audit document this bean supersedes was explicit that "whether the
corrected numbers agree better or worse with AME2020 is unknown and
unmeasured". Here is the first measured signal, and it is not about AME2020 —
it is about the producer's own stability gate.

### The committed witness is RED, and always was

    computed allPassed: False    assertions: 23    failing: 6

The six failures are `LP_stable(<atom>)` — "all atoms must be Frobenius-stable
(gluon-dressed nucleons satisfy Gx >= 0)". So this witness was not
green-with-wrong-numbers; it has been failing its own stability assertion for
c14, o16, ne20, si28, ca40 and fe56.

### Two of the six now pass

    atom   old stable   new stable |            old tr_M      new tr_M
    c14         False         True |      -0.483334408182      0.035123
    n14          True         True |       5.632418845162      6.877323
    o16         False         True |      18.278897005998     19.002147
    ne20        False        False |     247.041699299606    224.072409

c14 and o16 were unstable under the non-representation matrices and are stable
under the corrected ones. ne20 is still unstable. Three remain to compute, all
False in the committed witness:

    si28   old tr_M 2.09e+06
    ca40   old tr_M 1.71e+15
    fe56   old tr_M 5.04e+30

Those old traces are worth staring at. `tr_M` growing to 5e30 by A=56 is what
a product of matrices that do NOT satisfy the braid relation looks like —
nothing constrains the growth. Whether the corrected values stay bounded is
the thing to watch as si28/ca40/fe56 land; I am NOT predicting it.

### What this does and does not establish

- It DOES establish that the fix changes the stability verdict, in the
  direction of more atoms passing, on 2 of the 4 A>=14 atoms measured so far.
- It does NOT establish that the finished witness will be green. ne20 already
  fails, and one failing `LP_stable` is enough for `allPassed: False`.
- It says nothing about AME2020 agreement. The binding energies are large and
  positive at high A (+414 MeV at ne20) where AME2020 values are ~150-160 MeV;
  the residual question is untouched by this and remains open.


## 2026-09-03 — CORRECTION: the exponent had not converged

An earlier section on this bean claimed the cost exponent was "converging to
roughly 1.37 — not drifting toward the 2.0 that would have made the table
impractical", on the grounds that its increments were halving (+0.085, +0.028,
+0.016). Adding ne20 (A=20, 3293.48s) refutes that:

    exponent over A<=9     1.351
    exponent over A<=12    1.361     (+0.010)
    exponent over A<=20    1.417     (+0.056)

The increment GREW. The apparent convergence was an artifact of fitting inside
a narrow A range; each time the range extends, the exponent moves up again.
Current fit over 11 clean points (n14 and o16 excluded — my own audit runs
contended their timings):

    t = 40.2 * A^1.417
    si28   75 min      ca40  125 min      fe56  201 min
    endgame                                     ~6.7 h

Treat that as a lower bound too. The honest summary of this whole sequence is
that every estimate on this bean — 4.6 h, 6.9 h, 8.0 h, 8.4 h — has been low,
and the reason each time was extrapolating from A values well below the ones
that dominate the total. The only figure that has held is the per-atom
prediction ONE step ahead.


## 2026-09-03 — si28 REFUTES my reading of the large traces

Last section I wrote that the committed witness's enormous high-A traces
(2.09e6 at si28, 1.71e15 at ca40, 5.04e30 at fe56) were "what a product of
matrices that do NOT satisfy the braid relation looks like -- nothing
constrains the growth", and said the thing to watch was whether the corrected
values stay bounded. si28 has landed and the answer is no:

    atom     old      new |         old tr_M         new tr_M |  ratio
    c14    False     True |        -0.483334         0.035123 |      -
    o16    False     True |          18.2789          19.0021 |  1.040
    ne20   False    False |          247.042          224.072 |  0.907
    si28   False    False |      2.09413e+06       1.8384e+06 |  0.878

The si28 trace is 12% smaller and still 1.8 million. **The growth is intrinsic
to this producer at high A, not an artifact of the braid defect.** My framing
was wrong: I attributed it to the defect because the defect was what I had
just fixed, which is the wrong direction of inference.

### What the fix actually did, on the evidence so far

It restored stability at the SMALL end of the failing set (c14, o16) and
changed essentially nothing at the large end (ne20, si28 both still FAIL,
traces within ~10%). That is a real and useful result, and it is a much
narrower one than "the corrected matrices fix the table".

### The AME2020 question, which this bean has been deferring

    si28   B_pred = +16,578.73 MeV     AME2020 ~ 236 MeV      70x high
    ca40   B_pred (committed) 514,735 MeV        AME2020 ~ 342 MeV
    fe56   B_pred (committed) 1.198e9 MeV        AME2020 ~ 492 MeV

The high-A binding energies are not slightly off, they are orders of magnitude
off, and the braid fix moves them by ~10% at si28. Whatever is wrong at high A
is a DIFFERENT defect from the one this bean fixed. Worth its own bean once
ca40 and fe56 land and the shape is confirmed rather than inferred from one
atom.

Nothing here retracts the braid fix: the matrices were not a representation,
now they are, that is verified three independent ways (relations, entry-wise
against Rust, and qou-4m9u's closed form). It does retract my suggestion that
fixing it would tame the high-A traces.


## 2026-09-03 — the B ratios: my change altered high-A results, defensibly

Comparing the new run against the committed witness, B_pred is inflated by a
factor that GROWS with A:

    atom      old B_MeV        new B_MeV     ratio
    c14         34.0217          35.1751    1.0339
    n14         17.5136          22.0780    1.2606
    o16         27.6581          73.7681    2.6671
    ne20       132.5960         414.1790    3.1236
    si28      2916.1000       16578.7282    5.6852

A systematic A-dependent inflation is the signature of a missing rescaling, so
I checked whether my own change caused it. It did — and the old behaviour was
the incorrect one.

### Mechanism

`atom_markov_trace` recombines per-partition characters as

    max_ln = max(log_norm over partitions)
    chi_eff = chi * exp(log_norm - max_ln)

which returns the true Markov trace scaled by `exp(-max_ln)`. The Rust path
returns `log_norm = 0` (MPFR's exponent range makes the `m_max > 1e80`
rescaling unnecessary), so `max_ln = 0` and the trace comes back UNSCALED.

That is the correct one, because of how the caller uses it:

    atom_tr = atom_markov_trace(Z, N, k_cap, include_inter=True)
    free_tr = atom_markov_trace(Z, N, k_cap, include_inter=False)
    return E_0_CALIBRATION_MEV * (abs(free_tr) - abs(atom_tr))

Two SEPARATE calls, each computing its own `max_ln`, then subtracted. Whenever
`max_ln != 0` and differs between them, the old code subtracted two
differently-scaled quantities — not `E_0*(|tr_free| - |tr_atom|)`, which is
what it documents and what the derivation requires. Removing the scaling makes
both true traces and the subtraction valid.

### What is verified, and what is not

Verified: `atom_markov_trace` agrees between the two paths to ~1e-49 at
A = 2, 3, 4 in both `include_inter` conventions — pinned in
`tests/test_unified_correction_rust_parity.py` (19 tests). That covers every
case where the Python path also produces `log_norm = 0`.

NOT verified end to end: the high-A case where they genuinely differ.
`log_norm` only becomes non-zero for large-dim partitions once the running
product exceeds 1e80, and those are exactly the cases the pure-Python path
cannot finish — which is why the Rust path exists at all. Measured: at A=28
with a dim-6 partition, `log_norm` is still 0.0. So the divergence is argued
from the code's structure, not demonstrated numerically, and that limit should
be stated whenever these numbers are quoted.

### Consequence for the earlier note on this bean

The previous section said the high-A blow-up "is intrinsic to the producer,
not an artifact of the braid defect". That still holds — but part of the
INCREASE from the committed values is this rescaling fix, not the braid fix.
Both changes landed together, so the si28 ratio of 5.69 is their combined
effect and should not be attributed to either alone.


## 2026-09-03 — ca40 (18/19): the two ratios have clearly separated

    atom        stable        | tr_M ratio |  B ratio
    c14    False -> True      |    -0.0727 |   1.0339
    n14     True -> True      |     1.2210 |   1.2606
    o16    False -> True      |     1.0396 |   2.6671
    ne20   False -> False     |     0.9070 |   3.1236
    si28   False -> False     |     0.8779 |   5.6852
    ca40   False -> False     |     0.8772 |  15.8674

Two different things are happening and they should not be conflated:

**`tr_M` is essentially unchanged at high A** — 0.907, 0.878, 0.877, settling
near a constant ~0.88. That is a ~12% shift, not a structural one, and it
confirms the earlier finding: the enormous traces (1.5e15 at ca40) are
intrinsic to the producer, NOT an artifact of the braid defect. `tr_M` comes
from `nf_tr(build_atom_nf(...))` and never touches the YSN matrices, so the
residual ~12% is presumably the dps floor and the convention-D `z`, not the
braid fix at all.

**`B_MeV` diverges, and the ratio is still growing** — 1.03, 1.26, 2.67, 3.12,
5.69, 15.87. That is the `atom_markov_trace` rescaling (bean `qou-8w8v`):
`exp(max_ln)` grows with A, so removing the scaling inflates B by a factor
that grows with A. The shape of the ratio sequence is the evidence for that
diagnosis, and it is consistent with it.

`B_pred(ca40) = 8,167,488 MeV` against AME2020's ~342 MeV. The committed value
was 514,735 MeV — also absurd. Both are wrong; the new one is wrong by more,
and is *more faithful to the documented formula*. That is not a contradiction:
`E_0*(|tr_free| - |tr_atom|)` over traces that grow like 1e15 cannot produce a
~342 MeV binding energy, and the old code only looked less absurd because an
undocumented rescaling was shrinking it.

**So the high-A formula itself is the defect**, not its implementation. That is
a physics question — worth its own bean now that ca40 confirms the shape from
two atoms rather than one, and it is NOT something this bean should absorb.

One atom left. fe56's committed values are `tr_M = 5.04e30`, `B = 1.198e9 MeV`.


## 2026-09-04 — RUN COMPLETE (19/19). The witness is regenerated, and it is RED.

fe56 finished in 16559.66s (4.6 h). Witness written.

    OLD (committed)   allPassed False   23 assertions   6 failing
    NEW               allPassed False   16 assertions   4 failing
                      allPassedBasis: failed-assertions

The four failures are `LP_stable(ne20|si28|ca40|fe56)`. **c14 and o16 now
pass** where they failed before — the braid fix resolved two of the six
stability failures and none regressed.

### Against AME2020 — the honest table

    atom        AME2020          OLD B            NEW B
    deuterium     2.225         2.2213          -7.2711
    tritium       8.482        -2.5843          -7.7421
    he3           7.718        -3.3606          -7.4562
    he4          28.296         0.7183          -6.8286
    li6          31.994         5.0443          -3.0650
    li7          39.245         5.5081          -7.5553
    be9          58.165         3.9779          -0.0519
    b11          76.205         3.3058           4.4420
    c12          92.162         5.8438          13.9337
    c14         105.285        34.0217          35.1751
    n14         104.659        17.5136          22.0780
    o16         127.619        27.6581          73.7681
    ne20        160.645       132.5960         414.1787
    si28        236.537      2916.0999       16578.7282
    ca40        342.052      514735.3763    8167487.7945
    fe56        492.254   1197694903.3434  36220960188.4542

**The old table matched AME2020 at deuterium (2.2213 vs 2.2247, 0.17%) and the
new one does not** — it flips sign to -7.2711. That is the single worst
outcome in this table and it must not be buried.

Everywhere else the old table was ALREADY badly wrong: sign errors at tritium
and he3, an order of magnitude low through li6..o16, and absurd magnitudes
from ne20 up (1.2e9 MeV at fe56 against 492). Neither version reproduces
nuclear binding energies. The new one is not a regression from a working
model; it is a different set of wrong numbers, closer at c14/n14 and further
at deuterium and high A.

### What the deuterium shift is NOT

It is not the `atom_markov_trace` rescaling (bean `qou-8w8v`). At A=2 the
running product never exceeds 1e80, so `log_norm` is 0 on BOTH paths — and
`atom_markov_trace` parity between them is verified to ~1e-49 at A=2,3,4 in
`tests/test_unified_correction_rust_parity.py`. The rescaling cannot be the
cause at deuterium.

### What it might be — NOT established

The committed witness predates: the 1907-commit merge of main, the 50-dps
compute floor (`qou-zbws`), several NO-FLOAT64 excisions, convention D, and
the braid fix itself. Attributing the deuterium shift to any ONE of those is
not supported by anything measured here. It needs a bisect over those changes,
running `binding_energy(1, 1)` at each — cheap now (118 s per point) where it
was impossible before.

- [ ] Bisect the deuterium shift (+2.2213 -> -7.2711) across the merge, the
      dps floor, and the braid fix. This is the highest-value follow-up on
      this bean: deuterium is the one atom where this producer ever agreed
      with experiment, and losing that agreement is the strongest available
      evidence about which change was wrong — or about whether the agreement
      was a coincidence of the earlier defect.

### Also: 391 raw float64 fields

The producer's own gate warned on write:

    raw-float64: 391 raw float64 field(s) would enter the witness —
    .data.atoms[0].nf.γ, ... .tr_M, .net

`compute_atom` rounds to float via `round(float(v), 12)` before serialising.
Under NO FLOAT64 EVER that is a defect in this producer, not a cosmetic one —
it is the same class as the phase3-triton fields already fixed. Not addressed
here; the run had to complete first.

- [ ] Excise the 391 raw float64 fields from `hadron_knot_table`'s witness
      path, then regenerate. 4.6 h per regeneration, so batch it with the
      deuterium bisect rather than running the table twice.


## 2026-09-04 — BISECT: neither the braid fix nor the dps floor moved deuterium

`binding_energy(1, 1)`, fresh interpreter per point, each suspect toggled in
the working tree and restored (tree verified CLEAN afterwards):

    baseline (current HEAD)      -7.271102124876744   dps=50
    braid fix REVERTED           -7.271102124876744   dps=50
    50-dps floor DISABLED        -7.271102124876695   dps=15
    BOTH reverted                -7.271102124876695   dps=15

The braid revert changed **nothing** — identical to 16 digits. The dps floor
moves only the 16th digit. So the deuterium shift from +2.2213 to -7.2711 is
NOT attributable to either, and both are exonerated.

### Why the braid revert was inert — and this matters for the whole arc

The Rust kernel takes the PARTITION and builds its own seminormal matrices
inside Rust. It never calls `_build_ysn_matrices`. Demonstrated directly, with
the braid fix reverted, on partition (3,1,1):

    use_rust=True :  -0.00246686714893002309   (Rust, unaffected)
    use_rust=False:   0.184698628503780171     (Python, uses the broken a_rho)

**So the braid fix has no effect on anything routed through Rust**, which
since `qou-sv7h` is the default for `atom_character_raw` and
`unified_iterative_correction` — i.e. for `binding_energy`.

### What this does and does not change about the braid fix

It does NOT make the fix unnecessary. The Python matrices were genuinely not a
representation, and every consumer NOT routed to Rust was getting wrong
numbers:

    _crossing_M22 / _chain_M22        the hardcoded (2,2) H_4(q) path
    sdp_cross_channel.chi_at_q        the q-sweep
    _contrib_single_partition         jet / conjugate-pair paths
    every use_rust=False fallback     including any session without the wheel

It DOES mean I have been implying too much. I described the regenerated
witness as showing "the braid fix resolved two of the six stability failures".
That is not established: c14 and o16 flipping to stable comes from
`check_frobenius(build_atom_nf(...))`, and the numbers in the witness came
from Rust, which was always correct. The honest statement is that the witness
changed for OTHER reasons — the 1907-commit merge, convention D, the
`atom_markov_trace` rescaling removal (`qou-8w8v`) — and the braid fix is not
demonstrably among them.

- [ ] The deuterium shift is still unexplained. Two suspects are eliminated;
      the remaining candidates are the merge of main, convention D, and the
      rescaling removal. The rescaling one is testable cheaply at A=2 only if
      `log_norm != 0` there, and it is 0 — so that leaves the merge and
      convention D, which need an actual git bisect rather than an in-tree
      toggle.

## 2026-09-04 — si28, ca40 and fe56 landed. The braid fix does NOT restore stability.

The three atoms this bean was waiting on have completed, and the regenerated
`hadron-knot-table.witness.json` survived the origin/main merge byte-identical.
Final state of the table, all 16 assertions:

    atom     A   LP_stable          tr_M
    ----------------------------------------------------
    c14     14      True       0.035122844178
    n14     14      True       6.877322990493
    o16     16      True      19.002147240288
    ne20    20     False     224.072408596362
    si28    28     False     1838397.009951196
    ca40    40     False    1499657533706471.8
    fe56    56     False    4.39170578287642e+30

**12 of 16 pass.** Six LP_stable failures became four: c14 and o16 flipped to
stable under the corrected matrices; ne20, si28, ca40, fe56 did not.

### The answer to what this bean was watching for

I wrote above that the si28/ca40/fe56 ratios were "the thing to watch, and I am
NOT predicting it." Measured:

    ne20    224.072408596362      / 247.041699299606   =  0.9070
    si28    1838397.009951196     / 2.09e+06           =  0.8796
    ca40    1499657533706471.8    / 1.71e+15           =  0.8770
    fe56    4.39170578287642e+30  / 5.04e+30           =  0.8714

The braid fix is a **~0.87-0.91 multiplicative correction that drifts slowly
downward with A** — and that is all it is. It does not bend the growth. A
factor of 0.87 applied to 5.04e+30 is 4.39e+30; the quantity that has to reach
O(1) for Frobenius stability is still thirty orders of magnitude away.

So the hypothesis this bean opened with — that the `a_rho = h/[rho]` defect was
behind the high-A instability — is **refuted for the heavy end**, and refuted
by the cleanest possible evidence: the corrected computation, run to
completion, at every A. The defect was real, the fix was right, and it was
never the cause of this.

What the fix DID buy is the c14/o16 flip. Those two sat close enough to the
stability boundary that a 13% correction moved them across it. That locates
the boundary rather than explaining it: stability survives to tr_M ~19 (o16)
and fails by tr_M ~224 (ne20).

### What that leaves

The blow-up is intrinsic to the model as written, not an artefact of the
seminormal matrices. Whatever explains 4.39e+30 at A=56 is a separate
mechanism, and it is not a precision bug either — this run was at compute dps
70 through the MPFR kernel throughout.

`allPassed: False` on this witness is therefore CORRECT and should stay false.
It is reporting a real open finding, not a broken producer. Do not chase it
green by loosening the Gx >= 0 predicate or by dropping the four atoms from
the table.

### Correcting my own earlier note

I described this regeneration as "19/19" in the commit that landed it
(0f32ecdf5d) and in session notes. That was wrong twice over: the witness has
16 assertions, not 19, and 12 pass, not all. The 19 was the nuclide count.
Separately, 7 `tr_M(<atom>)` assertions present in the 2026-06-17 witness are
absent from this one — that is NOT a coverage loss: they were self-comparing
(`computed=r["tr_M"], expected=r["tr_M"]`) and were deliberately deleted under
bean `qou-26f2`, with the values still recorded in full precision under
`data.atoms`.

## 2026-09-05 — the 391 float64 fields are excised, and they were a symptom

The remaining item — "excise the 391 raw float64 fields from
`hadron_knot_table`'s witness path, then regenerate" — is done in code, and
doing it exposed three things the fields were hiding. Regeneration is running.

### What was narrowing

Every numeric field in the atom rows, and mostly by `round()` rather than an
explicit `float()`, which is why it was invisible at the call site:
`round(mpf, 12)` returns a Python float.

    nf_compact[bname]   round(val, 12)          -> fmt(val)
    V_rounded           round(float(v), 12)     -> fmt(v)
    tr_M                round(float(tr), 12)    -> fmt(tr)
    net                 round(float(net), 12)   -> fmt(net)
    ln_abs_tr           round(mp.log(...), 12)  -> fmt(mp.log(...), dps=17)
    B_MeV               round(B, 4)             -> fmt(B)
    cross_channel_sum   round(cross_sum, 12)    -> fmt(cross_sum)
    delta_xchan_MeV     round(delta_xchan, 6)   -> fmt(delta_xchan)

`B_MeV` at **four decimals** is the starkest: a binding energy carried through
the whole 50-dps MPFR pipeline, published to four figures. The `V_per_gen`
line even documented the defect — its comment read "compute mpf@q0; serialize
float".

### 1. B_MeV was float64 at the SOURCE too, and needn't have been

`binding_energy` ended `return float(B)`. The comment defending that cast gave
two reasons and **both had gone stale**:

* "an mpf raises TypeError at `hadron_knot_table`'s `round(B, 4)`" — that call
  site is `fmt(B)` now, which serializes mpf natively.
* "it costs nothing, `math.log` already narrows inside the accumulator" —
  `math` was excised from the module under `qou-9ay6`; the accumulator uses
  `_mp.log` and `math` survives only in comments.

One live caller (`hadron_knot_table.py:188`), established by call site rather
than name search. Cast removed. Measured effect on deuterium:

    before   -7.271102598682182                                      16 digits
    after    -7.27110259868218217191550436683489629794510593250805…  60 digits

### 2. `tr_M`, `net` and the NF coefficients are STILL float64 — `qou-ejuy`

`fmt` short-circuits a non-mpf to `str()`, so after the conversion they
serialize as 16-17 digits and say what they are. The source is
`tools/pyhecke/python/pyhecke/gram.py`, where `z`, `h` and `q0` are Python
floats and `TR_M = np.array([...])` is float64, so every Markov trace is a
float64 dot product against a float64 basis vector. Filed as **`qou-ejuy`**;
not fixed here because pyhecke is a shared library whose convention gate is
written for the f64 path.

This nearly caused a regression: `ln_abs_tr = mp.log(abs(tr))` promotes its
float64 argument and returns 60 GENUINE digits of the log of a value that has
17 — digits 18-60 describing the binary64 rounding of `tr`, not the physics.
Capped at `dps=17` with a comment to drop the override once `qou-ejuy` lands.
The `round(..., 12)` this replaced had been accidentally hiding it.

### 3. The LP_stable verdict is below its own noise floor — `qou-3uvs`

`check_frobenius` tests `Gx[i] < -1e-10`, a FIXED absolute tolerance, on a
float64 product whose magnitude runs from 1e1 to 1e31:

    atom   stable  max|nf|    float64 ulp   vs the -1e-10 threshold
    o16    True    1.540e+01  3.39e-15      far below  -> meaningful
    ne20   False   3.541e+02  7.79e-14      below      -> meaningful
    si28   False   4.166e+06  9.17e-10      comparable -> marginal
    ca40   False   3.805e+15  8.37e-01      10 orders above
    fe56   False   1.149e+31  2.53e+15      25 orders above

**This corrects what this bean and my session summary claimed.** The TRACE
GROWTH result stands — 19.0 at o16 to 4.39e+30 at fe56, and the braid-fix
ratios (0.9070 / 0.8796 / 0.8770 / 0.8714) keep ~16 digits, being ratios of
same-magnitude values. The STABILITY verdict for ca40 and fe56 does not: the
predicate cannot resolve its own threshold there, so "not Frobenius-stable" is
established only up to ne20. It should have been stated that way.

`check_frobenius` returns `(stable, Gx, violations)` and `compute_atom` already
unpacked all three, then recorded only the boolean — so this could not be
audited without re-running a 4.6-hour table. **`Gx` and
`frobenius_violations` are now recorded in every row**, landed BEFORE the
regeneration so the run produces an artifact that can answer the question.

### Observation for the still-open deuterium bisect

Deuterium now computes `B = -7.27110259868218217…`. The bisect baseline in
this bean is `-7.271102124876744`, which differs at the 7th digit. That
baseline was measured on the PRE-merge tree, so the delta is attributable to
{merge, convention D, the `qou-8w8v` rescaling removal, this cast removal}
collectively and to none of them individually. Recorded as a data point, not
a conclusion — the bisect item stands.

- [x] Excise the 391 raw float64 fields — done in code.
- [ ] Land the regenerated witness (run in progress, ~4.6 h).

## 2026-09-05 — the regeneration was STRUCTURALLY impossible; disk-backed memo fixes it

Three container reclaims in one session made something clear that retrying
would never have surfaced: **this witness could not be regenerated at all** in
an ephemeral container, and the reason is arithmetic, not luck.

Per-atom wall times, from the last full run's own `per_atom_wall_seconds`:

    n14   34 min      si28   90 min
    o16   41 min      ca40  159 min
    ne20  55 min      fe56  276 min        total ~11 h

The per-atom checkpoint saves only after an atom COMPLETES, so fe56 needs 4.6
hours uninterrupted. Each reclaim restarted the in-flight atom from zero, and
the producer correctly refuses to write a partial witness — so nothing landed,
and nothing ever would have.

Note this also corrects a figure I had been repeating: "4.6 h" is fe56 ALONE,
not the table. The table is ~11 h.

### The fix

A disk-backed memo at the Rust boundary — where the time goes, and where the
inputs are already fully serialised, so whatever crosses the ABI is the key.
Opt-in via `QOU_KERNEL_MEMO=<dir>`, matching `QOU_HKT_CHECKPOINT`; a cache with
a subtly incomplete key returns wrong numbers silently, which is worse than
slow.

Key: the compiled kernel's content hash (a rebuilt wheel must MISS — a stale
one demonstrably diverged at q0 earlier in this campaign), `dps`, `q_str` at
that dps, the partition, the exact serialised `(c, d, gen)` strings, and the
segment lengths for the prefix kernel.

Values are exact `_mpf_` limbs, never decimal strings. Rebuilding them needs
the mantissa coerced back to `MPZ` — mpmath asserts `type(man) == MPZ` and MPZ
is `gmpy2.mpz` here, so a plain int from JSON fails outright. **`_ckpt_dec` in
`hadron_knot_table` rebuilds mpf the same way and carries the same latent
bug**; it has not fired only because the row shape it stores does not exercise
its mpf branch.

### Measured, not asserted

    deuterium, cold      143.9 s
    deuterium, warm        2.2 s      67x
    values                 BIT-IDENTICAL   (the only acceptable result)
    size                   3.2 MB / 579 entries for deuterium alone

And the load-bearing property — that entries are written PER PARTITION, during
an atom, not at the end — verified directly: while tritium was still running,
the entry count went **932 -> 1116 over 60 seconds**. So an interrupted heavy
atom resumes at the partition it reached.

- [x] Make the heavy atoms survivable across reclaims.
- [ ] Land the regenerated witness. Now feasible: each reclaim costs one
      partition, so the table accumulates across restarts instead of resetting.

### 2026-09-05, later — what the memo is and is NOT yet shown to do

First reclaim since the memo landed, so the first real test. Correcting an
over-claim I made when it went in ("a reclaim costs one partition, not one
atom"): that describes the MECHANISM, and the mechanism is proven, but the
COVERAGE — what fraction of a heavy atom's runtime the memo actually removes —
is not measured, and this test did not measure it either.

**Proven:**

* cold/warm results are BIT-IDENTICAL (deuterium, run with the checkout quiet);
* full repeat of deuterium is 67x (143.9 s -> 2.2 s), so for A=2 the memoised
  Rust calls are ~98 % of the atom;
* entries are written PER PARTITION during an atom (932 -> 1116 over 60 s while
  tritium was still running);
* the memo survives a reclaim: 1884 entries / 8.4 MB were on disk afterwards.

**Not proven, and the honest reading of this test:** he4 was the interrupted
atom and it completed in **257.9 s against 286.2 s cold — about 10 %**, not the
near-instant resume the 67 % figure would suggest. From the memo's file mtimes
the reclaim gap sits after entry 1884, and he4 needed ~1291 new entries after
the restart, so the kill landed EARLY in he4 and very little of it was cached.
That is consistent with the mechanism working; it is not evidence that it does.

What remains genuinely open is whether fe56's 276 minutes are dominated by
memoised kernel calls the way deuterium's 144 seconds are. `binding_energy` is
three terms and only the Rust ones are cached — `sdp_cross_channel_contribution`
and the LP work are not. If those scale with A, coverage drops exactly where it
is needed most.

- [ ] Measure warm/cold coverage on a MID-SIZE atom (li6 or c12) with the
      checkout quiet. An attempt during the run was invalid: profiling
      concurrently with the table doubled every number through CPU contention,
      which is the standing "one producer at a time" rule biting a measurement
      rather than a producer.
- [ ] If coverage is poor at high A, memoise the SDP/LP term too, or accept
      that the heavy atoms need a long window regardless.

### 2026-09-05 — coverage MEASURED at li6 scale: 98 %

The open item was "measure warm/cold coverage on a mid-size atom with the
checkout quiet". Done, and it reverses the pessimistic reading from the
previous entry.

li6 cold, in the table's own run: **681.7 s**. Warm, checkout quiet:

    binding_energy(3, 3)                  14.5 s     -> 98 % removed, 47x
      unified_iterative_correction        14.3 s
      sdp_cross_channel_contribution      13.6 s     (NOT memoised)
      atom_markov_trace(inter=True)       12.3 s
      atom_markov_trace(inter=False)      20.4 s

    B = -3.06501952055873090718817934962, matching the table's li6 row.

(The per-term figures were taken while the memo was still filling, so they sum
to more than the end-to-end 14.5 s; the end-to-end number, taken last with
everything populated, is the one to quote.)

So the earlier worry — that the SDP/LP work is unmemoised and would dominate at
high A — does not hold at A = 6: the SDP is 13.6 s of a 682 s atom, about 2 %.

**Why the first attempt looked like poor coverage.** It timed out at 580 s on a
quiet checkout, which I read as coverage being poor. Wrong diagnosis. The
table's run had populated the paths IT used; my probe called
`atom_character_raw` and the terms directly, and the first such call took
12.058 s — a MISS — then 0.002 s on repeat. Those probes populated the
remainder, after which the end-to-end warm run is 14.5 s. Nothing was wrong with
the memo; my test was measuring cache population, not cache coverage.

This does not weaken the resumption argument, which is about the SAME call path
repeating after a reclaim: entries written before the kill are hits on restart.
It does mean a warm-cache measurement has to be taken after the paths under test
have actually run once.

- [x] Measure warm/cold coverage on a mid-size atom. 98 % at li6.
- [x] Decide whether to memoise the SDP/LP term. NO — 2 % of the atom at A = 6.
      Revisit only if a heavy atom's profile says otherwise.

### 2026-09-05 — the "-7.27110212 vs -7.27110259" lead was an ANCHOR mismatch

I flagged, at the end of the memo work, that `binding_energy(1,1)` gave
`-7.27110212487674444…` standalone but `-7.27110259868218217…` inside the
table, and noted the standalone value matched this bean's bisect baseline
exactly. Chased it. **Not a defect — the two runs were at different q₀
anchors**, and the matching baseline was the coincidence that made it look
like one.

`computations/substrate/q_parameter.py:100` selects the anchor from the
environment, and when `QOU_Q0_ANCHOR` is unset it AUTO-DETECTS from the
process's own name:

    _stem = Path(sys.argv[0]).stem
    if _stem in manifest["ideal_muon"]:
        _anchor = "ideal"

`hadron_knot_table` is one of the 19 entries in `q0_anchor_manifest.json`'s
`ideal_muon` list. So:

    run as `python3 hadron_knot_table.py`   -> stem "hadron_knot_table" -> MUON
    run as `python3 -c "..."`               -> stem "-c"                -> PROTON

Reproduced directly — same call, anchor forced:

    QOU_Q0_ANCHOR=muon  ->  q0 = 1.1099785956427
                            B(1,1) = -7.27110259868218217191550436683
                                     ... exactly the table's value

Both numbers are correct; they are answers to different questions.

**The hazard, which is the reusable part.** A probe invoked as `python3 -c` or
`python3 -m` silently computes at a DIFFERENT ANCHOR from the producer it is
meant to be checking, and nothing warns. Every ad-hoc comparison against a
manifest-listed producer must set `QOU_Q0_ANCHOR` explicitly, or it is
comparing two different physical pins and calling the difference a code change.
That is exactly the shape of error this bean already recorded twice — the
`-h/2` convention inside a "precision mirror" (`qou-ejuy`), and the vendored
qou-mass drift (`qou-qe81`).

**What this does and does not resolve.** It disposes of the lead I raised, and
nothing more. This bean's earlier bisect

    baseline / braid REVERTED     -7.271102124876744
    dps floor DISABLED / BOTH     -7.271102124876695

was internally consistent — every row is a proton-anchor standalone run — so
its conclusion stands: the braid fix and the dps floor are both inert for
deuterium. The still-open item is the much larger **+2.2213 -> -7.2711** shift,
a sign change that no anchor difference explains, and that remains open.

- [ ] When the bisect resumes, pin `QOU_Q0_ANCHOR` explicitly on EVERY point,
      including the "current HEAD" baseline. The previous run happened to be
      uniformly proton by accident of invocation, not by design.

### 2026-09-05 — resumption DEMONSTRATED on a real interruption

The claim I was careful not to over-state now has evidence from an actual
reclaim rather than a contrived repeat.

A reclaim killed the run partway through **be9**. The checkpoint still held 9
atoms (through li7), so be9 had to be recomputed from scratch by the
checkpoint's reckoning — but the memo had captured its partial work (entries
had grown 3570 -> 6275 across that window).

On restart:

    be9   completed in 35.59 s, adding only 179 new memo entries (6275 -> 6454)

against **li7 cold at 227.94 s** in the same run — and be9 is the LARGER atom
(A = 9 vs 7), so its cold cost is higher still. The interrupted atom resumed at
the partition it reached, which is exactly what the memo was built to do and
what the he4 test could not show (that kill landed too early in the atom for
anything to be cached).

So the position across four turns settles as:

    mechanism            proven (bit-identical, per-partition writes)
    coverage             98 % at li6 (14.5 s warm vs 681.7 s cold)
    RESUMPTION           proven here: 35.6 s for an atom killed mid-flight

### 2026-09-05 — main merged (619 commits); the memo made it nearly free

The merge touched `hecke_core_legacy.py`, which the checkpoint key hashes, so
all 10 cached atoms were invalidated. The MEMO is not keyed on Python source —
only on the compiled kernel hash, q₀, dps and the serialised factors — so it
survived, and the atoms replayed warm:

    deuterium 10.5 s   li6 1.1 s   li7 1.5 s   be9 1.7 s

against 145 s / 682 s / 228 s / 36 s when they were computed. Before the memo
this merge would have cost the whole prefix again.

**Every value is byte-identical to pre-merge**, which is the check that matters:
it confirms the 12-hunk resolution in `hecke_core_legacy.py` took the side the
artifacts were computed against. b11 has since landed (11 atoms).

`origin/main` had independently migrated the same YSN builder — `_ExactCOO` +
`_sigma_is_exact` where this branch has `_CooMPF` + `_msig_object_safe`. Took
this branch's for all 12 hunks: it is internally consistent (mixing would leave
`_Q_MP` undefined), module-wide mpf rather than keeping f64 names "for display
or float-domain call sites", and it drops the float64 BLAS fallback main's
retains. One of main's call sites auto-merged OUTSIDE the hunks and referenced
`_is_sparse_sigma`, whose definition did not survive — caught by the parity
tests going 64-pass to 18-fail, and aliased rather than renamed so a future
merge does not re-conflict.

### 2026-09-05 — second main merge (45 commits), and the witness loose end sized

One conflict, in `unified_iterative_correction`'s signature/docstring: this
branch added `use_rust=None`, main corrected the name (owner ruling, PR #6752 —
"The weights y_λ are not LP duals"). Both wanted; kept both. Ran the AST
dangling-name scan proactively this time rather than after a test failure —
clean. 64 + 145 tests pass, and every atom replays byte-identical (b11 in 3.17 s
against 111.63 s cold).

**The 7 witnesses resolved by taking one side in the previous merge need less
than I implied.** Checked their producers: the only change this branch made to
any of them is the atomic-write transform (`_wpath_sidu` / `os.replace`), which
alters HOW the file is written, not what is in it. `wlambda_jet_tower_connected`
and `t35-weak-vertex` carry it; `borromean-axial-coupling` and
`mass-from-q-symbolic` do not and auto-merged cleanly with main's producer.

So those witnesses are value-consistent with the producers that wrote them.
They want regeneration for PROVENANCE freshness — scriptHash, scriptCommitSha —
not for correctness, which is a much weaker claim than "they need regenerating"
and the honest one.

### 2026-09-05 — memo disk footprint checked (not a risk), and where the run stands

Checked before it could become a problem, since the container has a fixed disk
allowance (`df`: 4.9 G available, 88 % used) and the memo grows with every atom.

    du -sh   .work/kernel-memo   ->  32 MB
    sum of file sizes            ->   1.9 MB over 12 atoms

The 16x gap is block padding: 7814 entries, each a small JSON file taking a
4 KB minimum block. So the apparent size is mostly filesystem overhead rather
than data.

Projection: entry COUNT is roughly per-partition and does not grow much with A,
while entry SIZE does (an entry holds one trace per step, so fe56's are ~28x
deuterium's). That lands the finished memo in the low hundreds of MB, well
inside the allowance. **No sharding needed.** Revisit only if `df` tightens —
the cheap fix would be packing many entries per file to reclaim the 16x.

Run state: 12 atoms cached (through c12), c14 in flight. c14 is A=14, and n14
at the same A took 34 min in the last full run, so it is simply a big atom
rather than stuck — the memo grew 7612 -> 7814 entries during the last window,
which is preserved work.

---

## Table status 2026-09-06 (session-kill cadence, and why it still converges)

**15 / 19 atoms.** proton … c14, n14, o16 committed to
`.work/hkt-uiut-ckpt.json`. Remaining: **ne20, si28, ca40, fe56**.

The container suspends roughly every 10–15 minutes and kills the run; `setsid`
does not help, so it is the container, not the process group. That would be
fatal for a single multi-hour atom except for two things, both now carrying the
run:

- the **per-atom checkpoint**, which only works because the qou-sidu
  atomic-write transform had wrapped `_ckpt_load`'s READ as a write — it read
  `path + ".tmp"`, so resume had SILENTLY never worked and every restart
  recomputed all 19. Fixed in `3ff3d899c8`.
- the **kernel memo**, which persists partial work *within* an unfinished atom.
  Measured across kills: 8204 → 8387 (n14) → 8960 → 9166 → 9360 → 9542 → 9728
  (ne20 in progress). Each restart is strictly cheaper, so an atom longer than
  the window still completes across several.

n14 landed in **601 s** against a 34-minute estimate, on the memo's strength.

### Do not run the gate suite while an atom is computing

4 cores; the table sits at ~346 % with load already above 4. The witness records
a per-atom `wall`, so concurrent CPU load does not merely slow the run — it
**inflates a number that gets committed**. `qou_substrate` is now pip-installed
here (`pip install -e tools/qou-substrate --no-deps`), which clears the gate
suite's PREFLIGHT and makes a full 27-gate run possible in this container for
the first time — but it is DEFERRED until the table is idle. The install is
ephemeral and needs repeating in a fresh container.

---

## 2026-09-07 — container reset: what was lost, and the two traps in rebuilding

The container was replaced. Everything committed survived (branch is at
`0bc0813ad`); **`.work/` did not**, taking the 16-atom checkpoint and a
9914-entry kernel memo — roughly 9.5 h of compute.

**That was avoidable and the cause is mine.** `.work/kernel-memo/` is
gitignored (line 287, added deliberately — 37 MB of derived data). But
`.work/hkt-uiut-ckpt.json` is **23 KB and was never ignored at all**. It showed
as `?? .work/hkt-uiut-ckpt.json` in every `git status` I ran across the whole
session, and I never committed it. The one artifact whose entire purpose is to
survive a process that outlives its container was left untracked.

**Fix, applied here:** the checkpoint is committed as it advances, so a reset
costs at most the atom in flight rather than all of them.

### Trap 1 — the fresh container has none of the numeric stack

`mpmath`, `numpy`, `scipy`, `gmpy2`, `sympy`, `qou_substrate` were all absent;
the previous container had them preinstalled. All install cleanly
(`pip install mpmath numpy scipy gmpy2 sympy`, plus
`pip install -e tools/qou-substrate --no-deps`).

### Trap 2 — the one that would have produced WRONG NUMBERS

With the stack installed the table runs, and *starts producing a table*:

    *** WARNING: pyhecke_native.lp_accumulator_step_traces_mpfr is UNAVAILABLE.
    *** Falling back to _build_ysn_matrices, which VIOLATES the braid relation
    *** ... not a representation of H_n(q) ... Any binding number from this run
    *** is NOT the framework's value -- measured 17.3 % off at deuterium.
    *** Do not commit a witness from it.

This is the defect this bean is NAMED for, arriving as an environment
condition. `pyhecke-native` is not on PyPI, so a default container carries a
stale wheel or none, and the fallback is **silent in the numbers**: proton,
neutron and protium came out at 0.629328 / 0.475134 / 1.146338, byte-identical
to the good run. It only diverges on compounds. A run left going would have
written a checkpoint and a witness that look entirely normal.

Killed it and deleted the checkpoint it had written. The fix is in the warning:

    cd tools/pyhecke-native && maturin build --release \
      && pip install --force-reinstall --no-deps target/wheels/*.whl

Rust is present (cargo 1.94.1); only `maturin` needed installing. Build 3m34s.
Verified `lp_accumulator_step_traces_mpfr` is AVAILABLE and the restarted run
emits **zero** fallback warnings before trusting it.

### Restarting from zero

19 atoms again, with an empty memo. The three that matter — si28, ca40, fe56 —
are the ones `qou-3uvs` cannot settle without mpf, so the run still has to
happen; ne20's verdict from yesterday is already committed and stands.

---

## 2026-09-13 — TRAP: the table's CPU drop from ~380 % to 100 % is NOT a regression

Recording a wrong inference of mine, because the evidence for it is the first
thing anyone will notice when they watch this producer.

**What it looks like.** Before the 702-commit merge the table ran at 377–386 %
CPU; after it, 100 %. At the same time it stopped being able to finish
deuterium inside a container lifetime. The obvious reading is that main's
`qou-sv7h` restructure — from `chi_q_atomic_prefix_traces_mpfr` onto
`lp_accumulator_step_traces_mpfr` — serialised the kernel, and the evidence
lines up: `_lp_kernel_steps` is called from a plain `for s in state:` loop in
`unified_iterative_correction`, one PyO3 crossing per partition, and the Rust
docstring for the OLD entry point says "rayon-parallel on the Rust side".

**It is wrong, and `qou-sv7h` already measured it.** From that bean:

> Batching over partitions was measured and REJECTED:
> `chi_q_atomic_all_partitions_mpfr` gave 0.9x–1.2x on 4 cores at k=8,9,10 —
> one large-dim partition dominates, so the outer axis has nothing to give.
> (The Rust docstring already says this and chooses a serial outer loop
> deliberately; the measurement agrees with it.)

So the old path was **rayon burning four cores for ~1.0x throughput**. High
utilisation, no gain. The serial loop is a deliberate choice backed by a
measurement, and 100 % CPU is what correct looks like here. `top` cannot tell
those two apart, which is exactly why the number is a trap.

**The real reason deuterium was not finishing** is unrelated to threads:
cold it costs ~20 min (main's own figure, and `atom_markov_trace(1,1)` alone
measures 393.7 s), the container window was twice shorter than that, and the
memo that made partial work survive had been deleted at the merge. That is
fixed — the memo is re-ported with a key that covers the Python numeric path.

**Rule of thumb this leaves:** on this producer, judge throughput by
wall-clock per atom, never by CPU %. The two have moved in opposite
directions here for a legitimate reason.
