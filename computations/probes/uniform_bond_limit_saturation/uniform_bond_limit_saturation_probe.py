#!/usr/bin/env python3
"""
uniform_bond_limit_saturation_probe.py -- owner card 2026-11-27, "Component change of the closure".

QUESTION. Bond rule (3inf) of docs/audits/2026-11-27-bond-rules-and-length-cutoff.md is the
uniform average over bond words of length L, L -> infinity. It needs no weight and no cutoff,
and its limit is the closed form r = y_(n) / tr(x), y_(n) = [n+1]_q / [2]_q^n, n = 3A.
That audit measured it at A = 2, 3 only. What does it give for A >= 4, and for decay?

INPUTS. No new choice and no target data.
  * y_(n) is exact for every n.
  * tr(x) of the free word: read off the two committed witnesses (A = 2, 3) as
    ln tr(x) = -ln r_A + ln y_(n), and lt1_A = ln tr(x) / A per nucleon.
    Check K1 asserts lt1_2 == lt1_3, so tr(x) factorises over the free nucleons;
    only then is B(A) = E0 (A lt1 - ln[n+1] + n ln[2]) extrapolated.
  * E0 = 4.2274833556 MeV (log chart, as in the source audit).
  * EM self-energy, for decay only: coulomb_isospin_channel.em_energy_mev with the
    CAL-3-conditional radius (PR #9691). Conditional, labelled so.

STRUCTURE. B(A)/A -> 3 E0 ln(1 + q^-2) + E0 lt1 + O(ln A / A), proved here only as the
elementary limit [n+1]/[2]^n ~ q^n / (q + q^-1)^n / (1 - q^-2) (check K3, numeric).
The rule does not depend on the bond words at all: the source audit's objection
("it reads the free word against the fully symmetrised state") stands.

AME is comparison only. Scope (a): this rule, alone, is measured, not adopted.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path[:0] = [str(COMP / "substrate"), str(COMP)]
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

mp.mp.dps = 50
q = mp.mpf(Q_50_DIGIT_STR)
E0 = mp.mpf("4.2274833556")
SRC = COMP / "probes/bond_rules_length_bound"
AME_B_MEV = {2: ("2H", "2.224566"), 3: ("3H", "8.481798"), 4: ("4He", "28.295673")}  # comparison only


def qi(n):
    return (q**n - q**-n) / (q - 1 / q)


def ln_y(n):
    return mp.log(qi(n + 1)) - n * mp.log(qi(2))


def main() -> int:
    checks, lt = {}, {}
    for A in (2, 3):
        w = json.loads((SRC / f"bond-rules-length-bound-A{A}.witness.json").read_text())
        mlr = mp.mpf(w["data"]["rule3inf_uniform_limit"]["spectral_limit_minus_ln_r"])
        lt[A] = (mlr + ln_y(3 * A)) / A
    lt1 = lt[2]
    checks["K1_free_trace_factorises_lt1_A2_eq_A3"] = abs(lt[2] - lt[3]) < mp.mpf("1e-15")

    def B(A):
        n = 3 * A
        return E0 * (A * lt1 - ln_y(n))

    for A, src in ((2, "9.11923129296"), (3, "16.0934102331")):
        checks[f"K2_reproduces_source_A{A}"] = abs(B(A) - mp.mpf(src)) < mp.mpf("1e-9")

    asym = 3 * E0 * mp.log(1 + q**-2) + E0 * lt1
    checks["K3_B_over_A_tends_to_asymptote"] = abs(B(4000) / 4000 - asym) < mp.mpf("1e-2")
    checks["K4_B_over_A_increasing_A2_to_A208"] = all(B(a) / a < B(a + 1) / (a + 1) for a in range(2, 208))

    rows = {}
    for A in (2, 3, 4, 5, 6, 12, 16, 40, 56, 120, 208):
        row = {"B_MeV": mp.nstr(B(A), 10), "B_over_A_MeV": mp.nstr(B(A) / A, 8)}
        if A in AME_B_MEV:
            nm, b = AME_B_MEV[A]
            row["AME_nuclide"], row["B_over_AME"] = nm, mp.nstr(B(A) / mp.mpf(b), 6)
        rows[str(A)] = row
        print(f"A={A:4d} B={mp.nstr(B(A), 8):>10} MeV  B/A={mp.nstr(B(A) / A, 6)}" +
              (f"  B/AME({row['AME_nuclide']})={row['B_over_AME']}" if "AME_nuclide" in row else ""))
    print(f"asymptote B/A = {mp.nstr(asym, 10)} MeV; lt1 = {mp.nstr(lt1, 15)}")

    # alpha decay: sign of Q_alpha, model vs AME, EM conditional on the CAL-3 radius
    from coulomb_isospin_channel import em_energy_mev, r_rms_cal3_conditional  # noqa: E402
    ame = json.loads((COMP / "data/ame2020.json").read_text())["entries"]
    me = {(int(e["Z"]), int(e["N"])): mp.mpf(str(e["mass_excess_keV"])) / 1000 for e in ame
          if not e.get("mass_excess_estimated") and e.get("mass_excess_keV") is not None}
    cache = {}

    def bt(Z, N):
        A = Z + N
        if A not in cache:
            cache[A] = B(A)
        return cache[A] - (em_energy_mev(Z, A, r_rms_cal3_conditional(A)) if Z >= 2 else 0)

    n = ok = pos = posok = 0
    for (z, nn), m in me.items():
        if z < 3 or nn < 3 or (z - 2, nn - 2) not in me:
            continue
        qe = m - me[(z - 2, nn - 2)] - me[(2, 2)]
        if abs(qe) <= mp.mpf("0.01"):
            continue
        qm = bt(z - 2, nn - 2) + bt(2, 2) - bt(z, nn)
        n += 1
        ok += (qm > 0) == (qe > 0)
        if qe > 0:
            pos += 1
            posok += qm > 0
    alpha = {"scored": n, "sign_agrees": ok, "AME_unstable": pos, "AME_unstable_agrees": posok,
             "AME_stable": n - pos, "AME_stable_agrees": ok - posok,
             "note": "EM term conditional on the CAL-3 radius; AME used only to score the sign"}
    print("alpha", alpha)

    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)
    if WitnessBuilder is not None:
        wb = WitnessBuilder("uniform-bond-limit-saturation", engine="mpmath")
        wb.set_description("Bond rule (3inf), uniform long-word limit, extended to A >= 4: saturation "
                           "of B/A and the alpha-decay sign; candidate rule, not adopted; AME comparison only.")
        for k, v in checks.items():
            wb.add_assertion(k, computed=str(bool(v)), expected="True", tolerance="0")
        wb.add_data("E0_MeV", mp.nstr(E0, 12))
        wb.add_data("lt1_per_nucleon_ln_tr", mp.nstr(lt1, 25))
        wb.add_data("asymptote_B_over_A_MeV", mp.nstr(asym, 15))
        wb.add_data("rows", rows)
        wb.add_data("alpha_sign_score", alpha)
        wb.save()
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
