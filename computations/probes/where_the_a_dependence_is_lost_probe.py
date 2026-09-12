#!/usr/bin/env python3
"""Localising the flatness: the A-dependence survives the trace and dies in the sum.

PR #6427 measured that `unified_iterative_correction` is **flat in A** — 4He and
6Li return the same number to within 5 % at every truncation `k_exact >= 7`,
while `A` grows 1.5x and `C(A,2)` grows 2.5x. That PR recorded *where* the
A-dependence is lost as unmeasured. This probe measures it, by instrumenting the
three layers the quantity passes through.

## Layer 1 — the braid chain: A-dependence IS fed in, correctly

`_step_chain_generic(nucleon_type, prev_types, n_gens)` appends one
inter-nucleon crossing per previous nucleon, so the chain must lengthen with A:

    nucleus  A  n_gens  steps  crossings  distinct g  inter-nucleon
    he4      4     3      4        50          3            6
    li6      6     3      6        81          3           15

`inter` is exactly `C(4,2) = 6` and `C(6,2) = 15`. **The pairwise coordination
count is present in the input.** (The generator index is `g % n_gens`, so those
extra crossings wrap onto the same `n_gens` generators — a plausible-looking
mechanism for the flatness, and layer 2 shows it is not the one.)

## Layer 2 — the per-partition trace: A-dependence SURVIVES

Same partition, both nuclei, final `ln|tr|` from the Rust LP-accumulator kernel:

    partition (3,1)   he4  -1.29903312921154638     li6  +0.0942572825986714428
    partition (5,1)   he4  +0.582942120394291209    li6  +0.135627791973087475

Not a small perturbation — at (3,1) the two differ in sign. **The per-partition
traces are strongly A-dependent.**

## Layer 3 — the weighted sum: A-dependence is GONE, and Pass 2 is not the cause

`unified_iterative_correction` accumulates `cumul_total` over partitions in
Pass 1.  When this probe was written, Pass 2 then replaced it with
`gated_total`, the sum over the partitions whose final trace is "tight"; that
sign gate was DROPPED 2026-09-12 (owner ruling, bean `qou-jgx7`) after its
complementary-slackness justification was refuted sorry-free (PR #7251), so
`cumul_total` is now the return value and the gated sum survives only as the
diagnostic `gated_total_DISPROVED_SELECTION_MeV`.  **This probe's conclusion is
unaffected and its numbers do not move** — it computed both columns itself and
its finding is about the RAW one.  If the flatness were introduced by that gate,
the raw sum would be extensive and the gated one flat. It is not:

    k   he4 raw      li6 raw      RAW ratio   he4 gated    li6 gated   GATED ratio
    5   -0.736660    -0.923253      1.2533    -0.375110    -0.539213     1.4375
    7   -2.471104    -2.855260      1.1555    -1.515118    -1.414063     0.9333
    9   -6.691821    -7.266773      1.0859    -3.711582    -3.404341     0.9172

**The raw, pre-gate sum is already flat** — and getting flatter with `k`
(1.253 -> 1.156 -> 1.086), against `C(A,2)` growing 2.5x. The gate is A-aware
(tight partitions 5->10, 18->22, 42->48) and roughly neutral on the ratio.

## Conclusion, and its scope

The A-dependence enters the chain correctly, survives into the per-partition
traces, and is **cancelled in the `y_λ`-weighted telescoped sum over
partitions** — downstream of the trace, upstream of Pass 2. That is where a fix
has to look; the gate and the chain builder are both exonerated.

This is **scope-(a)**: it localises the symptom in this one computational path
at k = 5,7,9. It does not identify the cancellation mechanism, and it does not
exclude any ingredient from a corrected closure.

## Precision note

`raw_total_MeV` and `gated_total_DISPROVED_SELECTION_MeV` (named
`gated_total_MeV` when this probe was written) are `mpmath.mpf` **containers**, but they
carry only ~17 significant digits: `repr` at `mp.dps = 50` returns
`mpf('-0.73665972744972374')`. The information was narrowed to float64 upstream
by the `math.log(abs(tr_run))` inside the step loop — pre-existing, recorded in
PR #6427, not introduced here, and **not** by `cumul_total = 0.0`, which is
promoted on first addition. Checked rather than assumed, because the mpf type
makes the narrowing invisible to a type check.

The ratios above are therefore good to ~1e-15, fifteen orders below the effects
being measured (ratios differing by 0.1), so the conclusion does not rest on the
narrowed arithmetic — but it would be wrong to call these values 50-dps. The
layer-2 traces come straight from the kernel and *are* full-precision `mpf`. No
quantity computed *by this probe* is float64.

Writes no witness: this measures the shape of an existing defect, it does not
produce a value anything downstream consumes.
"""

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
import hecke_core_legacy as H  # noqa: E402

set_compute_dps(50)

NUCLEI = [("he4", 2, 2), ("li6", 3, 3)]


def _ordering(Z, N):
    """Ground-state ordering, matching `unified_iterative_correction`."""
    o = []
    for i in range(max(Z, N)):
        if i < Z:
            o.append('p')
        if i < N:
            o.append('n')
    return o


def main() -> int:
    checks = []

    def check(name, ok, detail):
        checks.append((name, ok, detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)

    # ---- Layer 1: the chain -------------------------------------------
    print("\nLAYER 1 -- the braid chain")
    print(f"  {'nucleus':8s} {'A':>2s} {'ngens':>5s} {'steps':>5s} "
          f"{'crossings':>9s} {'distinct g':>10s} {'inter':>5s}")
    chains_by = {}
    inter_by = {}
    for nm, Z, N in NUCLEI:
        o = _ordering(Z, N)
        for ngens in (3, 5):
            tot, gs, inter, chains = 0, set(), 0, []
            for k in range(len(o)):
                ch = H._step_chain_generic(o[k], o[:k], ngens)
                chains.append(ch)
                tot += len(ch)
                gs |= {g for _, _, g in ch}
                inter += k
            chains_by[(nm, ngens)] = chains
            inter_by[(nm, ngens)] = inter
            print(f"  {nm:8s} {Z+N:2d} {ngens:5d} {len(o):5d} {tot:9d} "
                  f"{len(gs):10d} {inter:5d}")

    for nm, Z, N in NUCLEI:
        A = Z + N
        expect = A * (A - 1) // 2
        check(f"inter-crossings at {nm} equal C(A,2)",
              inter_by[(nm, 3)] == expect,
              f"{inter_by[(nm, 3)]} == C({A},2) = {expect}")

    # ---- Layer 2: the per-partition trace ------------------------------
    print("\nLAYER 2 -- the per-partition trace (Rust kernel, 50 dps)")
    traces = {}
    for part, ngens in (((3, 1), 3), ((5, 1), 5)):
        for nm, _, _ in NUCLEI:
            ks = H._lp_kernel_steps(part, chains_by[(nm, ngens)])
            if ks is None:
                print("  pyhecke_native unavailable -- layer 2 skipped")
                traces = None
                break
            tr, ln = ks[-1]
            traces[(part, nm)] = ln + mp.log(abs(tr))
            print(f"  partition {part}  {nm:5s}  final ln|tr| = "
                  f"{mp.nstr(traces[(part, nm)], 18)}")
        if traces is None:
            break

    if traces is not None:
        for part in ((3, 1), (5, 1)):
            a, b = traces[(part, "he4")], traces[(part, "li6")]
            check(f"per-partition trace differs between nuclei at {part}",
                  abs(a - b) > mp.mpf("0.01"),
                  f"|{mp.nstr(a, 8)} - {mp.nstr(b, 8)}| = {mp.nstr(abs(a-b), 6)}")

    # ---- Layer 3: raw vs gated total -----------------------------------
    print("\nLAYER 3 -- the weighted sum, ungated vs the DISPROVED Pass-2 selection")
    print(f"  {'k':>2s} {'he4 raw':>12s} {'li6 raw':>12s} {'RAW':>7s} "
          f"{'he4 gated':>12s} {'li6 gated':>12s} {'GATED':>7s} {'tight':>11s}")
    raw_ratio = {}
    for k in (5, 7, 9):
        got = {}
        for nm, Z, N in NUCLEI:
            _, steps = H.unified_iterative_correction(
                Z, N, return_per_step=True, k_max=k, k_exact=k)
            last = steps[-1]
            # Key renamed 2026-09-12 (bean `qou-jgx7`): the Pass-2 sign gate
            # was dropped, so `raw_total_MeV` is now also the return value and
            # the gated sum survives only as an explicitly-scoped diagnostic.
            # This probe's Layer 3 compares the two DELIBERATELY, so it keeps
            # reading both; nothing it concludes depended on which one the
            # producer happened to return.
            got[nm] = (last['raw_total_MeV'],
                       last['gated_total_DISPROVED_SELECTION_MeV'],
                       last['n_tight_final'])
        rr = got['li6'][0] / got['he4'][0]
        gr = got['li6'][1] / got['he4'][1]
        raw_ratio[k] = rr
        print(f"  {k:2d} {got['he4'][0]:12.6f} {got['li6'][0]:12.6f} {rr:7.4f} "
              f"{got['he4'][1]:12.6f} {got['li6'][1]:12.6f} {gr:7.4f} "
              f"{got['he4'][2]:5d}->{got['li6'][2]:<5d}")

    check("the RAW pre-gate sum is already flat (ratio < 1.3 while C(A,2) x2.5)",
          all(r < 1.3 for r in raw_ratio.values()),
          f"raw ratios {', '.join(mp.nstr(raw_ratio[k], 5) for k in (5, 7, 9))}")
    check("the RAW ratio trends TOWARD 1 as k grows (gate is not the cause)",
          raw_ratio[5] > raw_ratio[7] > raw_ratio[9],
          f"{raw_ratio[5]:.4f} > {raw_ratio[7]:.4f} > {raw_ratio[9]:.4f}")

    n_ok = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{n_ok}/{len(checks)} checks passed")
    print("\nLOCALISED: the A-dependence enters the chain, survives the "
          "per-partition\ntrace, and is cancelled in the y_lambda-weighted sum "
          "-- downstream of the\ntrace, upstream of Pass 2. Scope-(a).")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
