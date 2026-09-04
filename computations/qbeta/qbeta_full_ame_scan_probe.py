#!/usr/bin/env python3
"""The framework against ALL 3555 nuclides — it crosses the data near A ~ 140.

Until now the binding law had been evaluated on four atoms, because anything
larger needed seminormal matrices at `n = 3A` and the blocks reach 16,336,320
dimensions by `n = 18`. With `Delta_tr(Z,N)` in closed form
(`qbeta_bond_factors_derived_probe.py`, zero fitted constants) the whole AME2020
table is instant.

*** THE RESULT ***

    B_pred(Z,N) = Q_beta(n) . Delta_tr(Z,N)
    Delta_tr(Z,N) = t_p^Z t_n^N (1 - b_pp^(Z-1) b_pn^[Z,N>=1] b_nn^(N-1))

against `B_AME`:

     A    Z    N   B_AME (MeV)   B_pred (MeV)   B_AME/B_pred
     2    1    1         2.225         0.4354          5.109
     4    2    2        28.296         0.8761          32.30
    12    6    6        92.162          1.643          56.10
    20    9   11       154.403          2.324          66.43
    40   18   22       343.810          6.906          49.78
    56   25   31       489.347          16.02          30.54
   100   43   57       859.512          134.6          6.384
   150   63   87      1236.202           1414         0.8745   <- crossover
   208   84  124      1630.586        1.56e+04         0.1045
   238   94  144      1801.270       4.753e+04        0.03790

**The deficit is not monotonic and it changes sign.** Along this median-per-A
slice it rises past 66x near A = 20, falls, and the heaviest A whose median
ratio still exceeds 1 is **A = 150**; by 238-U the framework OVERSHOOTS by a
factor of 26. **1641 of 3554 nuclides are overshoots (46 %)** — nearly half the
table.

The single worst undershoot over the whole table is not on that slice: it is
**A = 39, Z = 11, N = 28 at 95.45x**, a very neutron-rich sodium isotope. The
66x above is the median at A = 20, not the maximum — the two are different
statistics and only the second is a bound.

*** WHY: AN EXPONENTIAL CROSSING A LINE ***

`Delta_tr` is dominated by `t_p^Z t_n^N` with `t_p = 1.1458 > 1`, so `B_pred`
grows EXPONENTIALLY in Z while real binding grows roughly linearly in A. Two
such curves cross exactly once, and they do, around A ~ 140.

*** WHAT THIS SETTLES ***

Three claims in the corpus rest on the four light calibration atoms, and all
three are now visibly artefacts of where those atoms sit:

  * "the framework supplies 8-20 % of binding" — true at A <= 4, false above
    A ~ 140 where it supplies more than 100 %.
  * "the missing term must be added" — for half the table the term would have to
    be SUBTRACTED.
  * "Delta_tr is extensive" — already withdrawn on the closed form; this is the
    same fact seen against data.

The four calibration atoms are not merely unrepresentative, they sit on the
steep rising flank of the deficit curve, below its A ~ 20 maximum.

*** SCOPE ***

Scope-(a). Nothing is refuted about the ALGEBRA — the closed form reproduces
every measured `Delta_tr` to 1e-35 and is derived with no fitted constant. What
this measures is the fit of `B = Q_beta . Delta_tr` to nature, and the answer is
that it fails in two opposite directions on either side of A ~ 140.

Entries with non-positive `B_AME` or `B_pred` are excluded and counted rather
than silently dropped.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 30
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
QB = mp.mpf("0.78233340931")

T_P = ((Q0**22 + Q0**20 + 2*Q0**18 + 2*Q0**16 + 3*Q0**14 + 2*Q0**12
        + Q0**10 - Q0**8 - Q0**4 - Q0**2 - 1) / (4*Q0**9*(Q0**2 + 1)**2))
T_N = ((Q0**18 - Q0**16 + 2*Q0**14 - 2*Q0**12 + 4*Q0**10 - 3*Q0**8
        + 3*Q0**6 - 2*Q0**4 + Q0**2 - 1) / (4*Q0**9))
B_PP = Q0**3 / (Q0**2 + 1)
B_NN = 1 / (Q0**3 + Q0)
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1) / (12*Q0**5*(Q0**2 + 1)))

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def delta_tr(Z: int, N: int):
    free = T_P**Z * T_N**N
    atom = free * B_PP**(Z - 1 if Z >= 1 else 0) * B_NN**(N - 1 if N >= 1 else 0)
    if Z >= 1 and N >= 1:
        atom *= B_PN
    return free - atom


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    entries = json.loads(AME.read_text())["entries"]
    rows, skipped = [], {"no_binding": 0, "nonpositive_B": 0, "nonpositive_pred": 0,
                         "single_species": 0}
    for e in entries:
        Z, N, A = e["Z"], e["N"], e["A"]
        if Z < 1 or N < 1:
            skipped["single_species"] += 1
            continue
        bpa = e.get("binding_energy_per_A_keV")
        if bpa is None:
            skipped["no_binding"] += 1
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B <= 0:
            skipped["nonpositive_B"] += 1
            continue
        P = QB * delta_tr(Z, N)
        if P <= 0:
            skipped["nonpositive_pred"] += 1
            continue
        rows.append({"A": A, "Z": Z, "N": N, "B": B, "P": P, "ratio": B / P})

    print("=" * 74)
    print(f"1. SCAN — {len(rows)} nuclides evaluated, {sum(skipped.values())} excluded")
    print("=" * 74)
    for k, v in skipped.items():
        print(f"  excluded ({k}): {v}")
    ok = True
    ok &= chk("scanned_more_than_3000_nuclides", len(rows) > 3000, True,
              "first evaluation of the binding law beyond four atoms")

    print("\n" + "=" * 74)
    print("2. THE DEFICIT CURVE")
    print("=" * 74)
    print(f"  {'A':>4}{'Z':>4}{'N':>4}{'B_AME(MeV)':>14}{'B_pred(MeV)':>15}"
          f"{'B/B_pred':>13}")
    by_a = {}
    for r in rows:
        by_a.setdefault(r["A"], []).append(r)
    sample = []
    for A in (2, 4, 12, 20, 40, 56, 100, 150, 208, 238):
        if A not in by_a:
            continue
        cand = sorted(by_a[A], key=lambda r: r["Z"])
        r = cand[len(cand) // 2]
        sample.append({"A": r["A"], "Z": r["Z"], "N": r["N"],
                       "B_AME": mp.nstr(r["B"], 8), "B_pred": mp.nstr(r["P"], 6),
                       "ratio": mp.nstr(r["ratio"], 6)})
        print(f"  {r['A']:>4}{r['Z']:>4}{r['N']:>4}{mp.nstr(r['B'],7):>14}"
              f"{mp.nstr(r['P'],6):>15}{mp.nstr(r['ratio'],6):>13}")

    over = [r for r in rows if r["ratio"] < 1]
    under = [r for r in rows if r["ratio"] >= 1]
    peak = max(rows, key=lambda r: r["ratio"])
    print(f"\n  worst UNDERshoot: A={peak['A']} Z={peak['Z']} N={peak['N']}"
          f"  ratio {mp.nstr(peak['ratio'], 6)}")
    print(f"  nuclides the framework OVERSHOOTS (ratio < 1): {len(over)} / {len(rows)}"
          f"  ({100*len(over)//len(rows)} %)")
    ok &= chk("the_deficit_changes_SIGN_across_the_table",
              len(over) > 0 and len(under) > 0, True,
              "for nearly half the table the missing term would have to be "
              "SUBTRACTED, not added")
    ok &= chk("substantial_fraction_are_overshoots",
              len(over) > len(rows) // 4, True)
    ok &= chk("worst_undershoot_is_a_light_nucleus", peak["A"] < 60, True,
              "the deficit peaks on the light flank, not at the extremes")

    # crossover: heaviest A whose median ratio still exceeds 1
    med = {}
    for A, rs in by_a.items():
        vals = sorted(r["ratio"] for r in rs)
        med[A] = vals[len(vals) // 2]
    crossing = max((A for A in sorted(med) if med[A] > 1), default=None)
    print(f"  heaviest A with median ratio > 1 (crossover): A = {crossing}")
    ok &= chk("crossover_is_far_above_the_calibration_atoms",
              crossing is not None and crossing > 100, True,
              "the four calibration atoms sit at A <= 4")

    print("\n" + "=" * 74)
    print("3. THE CALIBRATION ATOMS ARE ON THE RISING FLANK")
    print("=" * 74)
    for A in (2, 3, 4):
        for r in sorted(by_a.get(A, []), key=lambda r: r["Z"]):
            print(f"  A={r['A']} Z={r['Z']} N={r['N']}  ratio "
                  f"{mp.nstr(r['ratio'], 6)}")
    calib = [r for r in rows if r["A"] <= 4]
    ok &= chk("calibration_atoms_sit_below_the_peak",
              all(r["ratio"] < peak["ratio"] for r in calib), True,
              "so 'the framework supplies 8-20 % of binding' describes where "
              "those atoms are, not the law")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-full-ame-scan",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "Q_beta_n_MeV": str(QB),
                       "binding_law": "B = Q_beta(n).Delta_tr(Z,N)",
                       "delta_tr": "t_p^Z t_n^N (1 - b_pp^(Z-1) b_pn b_nn^(N-1))",
                       "source": "qou-mass/src/qou_mass/data/ame2020.json",
                       "trace_convention": "D (SU(2)/Temperley-Lieb)"},
        "data": {"n_evaluated": len(rows), "excluded": skipped,
                 "sample_curve": sample,
                 "worst_undershoot": {"A": peak["A"], "Z": peak["Z"],
                                      "N": peak["N"],
                                      "ratio": mp.nstr(peak["ratio"], 8)},
                 "n_overshoot": len(over), "n_undershoot": len(under),
                 "crossover_A": crossing},
        "context": {
            "axis": "how does the binding law fare across the whole nuclide "
                    "table, now that Delta_tr is closed-form?",
            "answer": "It fails in two opposite directions. The deficit rises to "
                      "~66x near A = 20, falls, crosses unity near A ~ 140, and "
                      "reaches a 26x OVERSHOOT at 238-U. 1642 of 3555 nuclides "
                      "are overshoots. Delta_tr is exponential in Z while real "
                      "binding is roughly linear in A, and two such curves cross "
                      "once.",
            "consequence": "Claims resting on the four light atoms are artefacts "
                           "of where those atoms sit: 'supplies 8-20 % of "
                           "binding' is false above A ~ 140, and for nearly half "
                           "the table a missing term would have to be SUBTRACTED.",
            "scope": "Scope-(a). Nothing is refuted about the algebra — the "
                     "closed form reproduces every measured Delta_tr to 1e-35 "
                     "with no fitted constant. What is measured is the fit of "
                     "B = Q_beta . Delta_tr to nature.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-full-ame-scan.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
