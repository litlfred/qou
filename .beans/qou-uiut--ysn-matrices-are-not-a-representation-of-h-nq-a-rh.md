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

- [ ] Witness blast radius: every producer reaching `atom_character_raw`,
      `_crossing_M22`, `unified_iterative_correction` or `chi_at_q` emitted
      numbers from matrices that were not a representation. Those witnesses
      are WRONG, not stale, and must be regenerated from the producers.
