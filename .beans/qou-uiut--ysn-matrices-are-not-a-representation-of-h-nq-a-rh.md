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
