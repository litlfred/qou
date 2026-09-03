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
- [ ] Enumerate the witness blast radius; regenerate affected producers
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
- [ ] `hadron-knot-table.witness.json` — BLOCKED on `qou-sv7h`. The producer
      cannot finish (deuterium alone >11 min, Fe-56 ~144x that), so this
      witness cannot be regenerated until the scaling work lands.


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
