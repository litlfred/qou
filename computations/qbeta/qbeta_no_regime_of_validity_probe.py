#!/usr/bin/env python3
"""No choice of scale rescues `B = Q_beta . Delta_tr` — 4.6 decades at the OPTIMUM.

The full-table scan (`qbeta_full_ame_scan_probe.py`) found the deficit changes
sign: undershoot below A ~ 150, overshoot above, 46 % of nuclides overshot. The
obvious question is whether the crossover is structural or an accident of the
calibration constant `Q_beta`, which enters the law only as an overall scale.

This settles it by finding the BEST POSSIBLE scale and showing it fails anyway.
That is a stronger negative than showing one particular choice fails, and it is
the opposite of a fit: the optimum is computed in order to be refuted.

*** 1. THE CONSTANT IS NOT THE PROBLEM ***

The scale minimising log-spread is the geometric mean of `B / Delta_tr`:

    optimal        = 0.9482640138 MeV
    corpus Q_beta  = 0.7823334093 MeV        ratio 1.2121

The corpus value is already within 21 % of the best a single scale can do. So
the law is not mis-calibrated.

*** 2. AND NO SCALE WORKS ***

With that optimal scale, the residual `B / (scale . Delta_tr)` still runs

    min 0.00201403   max 78.7504   max/min = 39101   =  4.59 DECADES

A one-parameter scale multiplying an exponential cannot track a roughly linear
function across A. Multiplying by a constant slides the curve up or down; it
cannot change that one side grows like `t_p^Z` and the other like `a_V A`.

*** 3. SO THE CROSSOVER LOCATION IS NOT STRUCTURAL ***

`Delta_tr ~ t_p^Z t_n^N`, so along a fixed `N/Z` the growth per proton is
`c = ln t_p + (N/Z) ln t_n`, with `ln t_p = +0.1360679039` and
`ln t_n = -0.01233203987`:

    N/Z = 1.0   c = 0.12373586   a 10x change in the scale moves Z* by 18.6  (dA ~ 37)
    N/Z = 1.2   c = 0.12126946                                  19.0  (dA ~ 42)
    N/Z = 1.5   c = 0.11756984                                  19.6  (dA ~ 49)

So "the law works near A = 150" is a property of the chosen `Q_beta`, movable by
~40 A-units per decade. What IS structural is that a crossover exists at all —
an exponential and a line cross exactly once, whatever the constants.

*** THE CONCLUSION ***

**`B = Q_beta . Delta_tr` has no regime of validity in A.** It can be made to
agree at isolated points by choosing the scale, and it then fails on both sides.
Agreement at any particular A is a coincidence of the calibration, not evidence
of a working law there.

*** SCOPE ***

Scope-(a). Nothing here touches the ALGEBRA: `Delta_tr(Z,N)` is closed-form,
derived with zero fitted constants, and reproduces every measured value to
1e-35. What is refuted is the physical ansatz that binding is a constant times
that quantity. Whether some OTHER functional of the same operator works is
untouched — and the arc's earlier results say the missing piece is not a
reweighting, not reachable by larger N, and not in the interface subalgebra.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

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
    f = T_P**Z * T_N**N
    return f - f * B_PP**(Z - 1) * B_NN**(N - 1) * B_PN


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    rows = []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        if Z < 1 or N < 1:
            continue
        bpa = e.get("binding_energy_per_A_keV")
        if not bpa:
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B <= 0:
            continue
        d = delta_tr(Z, N)
        if d <= 0:
            continue
        rows.append((A, Z, N, B, d))

    ok = True
    print("=" * 74)
    print(f"1. THE BEST POSSIBLE SCALE — {len(rows)} nuclides")
    print("=" * 74)
    logs = [mp.log(B / d) for (_, _, _, B, d) in rows]
    best = mp.exp(sum(logs) / len(logs))
    print(f"  optimal scale (geometric mean of B/Delta_tr) = {mp.nstr(best, 10)} MeV")
    print(f"  corpus Q_beta                                = {mp.nstr(QB, 10)} MeV")
    print(f"  ratio                                         = {mp.nstr(best/QB, 6)}")
    ok &= chk("corpus_scale_is_already_near_optimal",
              abs(best / QB - 1) < mp.mpf("0.5"), True,
              "within 21 % of the best a single scale can do — so the law is "
              "not mis-calibrated")

    print("\n" + "=" * 74)
    print("2. AND IT STILL FAILS")
    print("=" * 74)
    res = [B / (best * d) for (_, _, _, B, d) in rows]
    lo, hi = min(res), max(res)
    decades = mp.log10(hi / lo)
    print(f"  residual B/(scale.Delta_tr):  min {mp.nstr(lo, 6)}   max {mp.nstr(hi, 6)}")
    print(f"  max/min = {mp.nstr(hi/lo, 6)}   =  {mp.nstr(decades, 4)} decades")
    ok &= chk("optimal_scale_still_spans_more_than_three_decades",
              decades > 3, True,
              "a one-parameter scale on an exponential cannot track a line")

    print("\n" + "=" * 74)
    print("3. SO THE CROSSOVER LOCATION IS A PROPERTY OF THE CONSTANT")
    print("=" * 74)
    ltp, ltn = mp.log(T_P), mp.log(T_N)
    print(f"  ln t_p = {mp.nstr(ltp, 10)}   ln t_n = {mp.nstr(ltn, 10)}")
    shifts = []
    for nz in (mp.mpf(1), mp.mpf("1.2"), mp.mpf("1.5")):
        c = ltp + nz * ltn
        dz = mp.log(10) / c
        shifts.append({"N_over_Z": str(nz), "growth_per_proton": mp.nstr(c, 8),
                       "dZ_per_decade": mp.nstr(dz, 6),
                       "dA_per_decade": mp.nstr(dz * (1 + nz), 6)})
        print(f"  N/Z={mp.nstr(nz,2)}  c = {mp.nstr(c,8)} /proton   "
              f"10x scale moves Z* by {mp.nstr(dz,5)}  (dA ~ {mp.nstr(dz*(1+nz),5)})")
    ok &= chk("crossover_moves_tens_of_mass_units_per_decade",
              all(mp.mpf(s["dA_per_decade"]) > 20 for s in shifts), True,
              "so 'the law works near A = 150' is about the chosen Q_beta")
    ok &= chk("growth_per_proton_is_positive_so_a_crossing_must_exist",
              all(mp.mpf(s["growth_per_proton"]) > 0 for s in shifts), True,
              "the EXISTENCE of a crossover is structural even though its "
              "location is not")

    print("\n  🛑 B = Q_beta . Delta_tr has NO REGIME OF VALIDITY in A. It can be")
    print("     made to agree at isolated points by choosing the scale, and then")
    print("     fails on both sides. Agreement at any particular A is a")
    print("     coincidence of the calibration.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-no-regime-of-validity",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "corpus_Q_beta_MeV": str(QB),
                       "binding_law": "B = Q_beta(n).Delta_tr(Z,N)",
                       "source": "qou-mass/src/qou_mass/data/ame2020.json"},
        "data": {"n_nuclides": len(rows),
                 "optimal_scale_MeV": mp.nstr(best, 15),
                 "optimal_over_corpus": mp.nstr(best / QB, 10),
                 "residual_min": mp.nstr(lo, 10), "residual_max": mp.nstr(hi, 10),
                 "residual_decades": mp.nstr(decades, 8),
                 "ln_t_p": mp.nstr(ltp, 15), "ln_t_n": mp.nstr(ltn, 15),
                 "crossover_sensitivity": shifts},
        "context": {
            "axis": "is the A ~ 150 crossover structural, or an accident of the "
                    "calibration constant Q_beta?",
            "answer": "Its EXISTENCE is structural — an exponential and a line "
                      "cross exactly once — but its LOCATION is not, moving "
                      "37-49 mass units per decade of scale. And no scale "
                      "rescues the law: at the optimum (0.9483 MeV, only 1.21x "
                      "the corpus value) the residual still spans 4.59 decades.",
            "method": "The optimum is computed in order to be REFUTED, which is "
                      "the opposite of a fit: showing the best possible choice "
                      "fails is stronger than showing one choice fails.",
            "conclusion": "B = Q_beta . Delta_tr has no regime of validity in A. "
                          "Agreement at any particular A is a coincidence of the "
                          "calibration.",
            "scope": "Scope-(a). Nothing touches the ALGEBRA — Delta_tr(Z,N) is "
                     "closed-form, derived with zero fitted constants, and "
                     "reproduces every measured value to 1e-35. What is refuted "
                     "is the ansatz that binding is a constant times it. Whether "
                     "some OTHER functional of the same operator works is "
                     "untouched.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-no-regime-of-validity.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_p
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
