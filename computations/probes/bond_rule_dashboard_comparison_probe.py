#!/usr/bin/env python3
"""Sum rule vs product rule on the binding table — and the product rule LOSES.

Owner, 2026-08-30: *"go"* — measure what actually moves before changing the
convention. This is that measurement, and it does **not** support the change.

`qou-nial` found that `closed_form_tau_M.interface_factor` implements the
CENTRED SUM `(Q_i + Q_j - 1)*h/2` of the two nucleon charges, where a Coulomb
term needs the PRODUCT `Q_i*Q_j*h/2`. The two differ only on the `nn` bond: the
sum rule charges two neutral objects `-h/2`, the product rule charges them `0`
(so `f_nn` joins the `f_pn` baseline).

This probe runs both rules through the Sec.10a log form `B = -alpha*SUM ln f` on
the chain assembly and compares against AME2020.

## Result — three findings, and two of them are against the product rule

1. **The product rule is WORSE on absolute binding.** Mean `|ln(model/AME)|`
   over 12 nuclei: sum rule **0.808**, product rule **0.940**. Moving `f_nn` up
   to the baseline removes binding from every nucleus with an `nn` bond, and
   the model is already short.

2. **It nails the A = 3 mirror splitting, and that is a coincidence.** Observed
   `-0.7638`; sum rule `-1.7471` (2.29x); product rule **`-0.7829` (1.025x)**.
   But under the chain the product rule's mirror difference is
   `(Z-N)(B_pp - B_baseline)`, which for an odd-A mirror pair is a CONSTANT --
   flat in `A`, exactly like the sum rule. At A = 7 the observed splitting has
   grown to `-1.6442` and the product rule still says `-0.7829`, now **0.48x**,
   too small by half, while the flat sum rule happens to pass through at
   `1.06x`. **Do not quote the A = 3 agreement as a win**: it is a flat line
   crossing a rising curve, the same trap recorded in `qou-vudb`.

3. **Both rules are ~3x short on absolute binding for A >= 4** (ratios 0.28-0.35
   from 4He to 56Fe). That is the extensivity problem (`qou-brng`), untouched by
   either rule -- the chain carries only `A-1` bonds.

## What this settles

The product rule is right about STRUCTURE (`qou-nial`: `nn` on the baseline,
charge dependence confined to `pp`, a `Z(Z-1)` multiplicity available at all)
and does not pay off NUMERICALLY under the current assembly. Switching
`interface_factor` on this evidence would trade a measurable regression in
absolute binding for a structural improvement whose numerical benefit does not
survive past A = 3.

**Recommendation: do not switch the convention.** The structural finding stands
as a diagnosis of why the arc's four failures all look alike; it is not yet a
repair, because the assembly is short by 3x independently and a bond-rule change
cannot reach that.

## Scope

**(a)** -- a measurement against AME2020 under one assembly (the chain). It does
not refute the product rule as a structural claim; it measures its cost under
the current assembly, which is the question the owner asked.

`-- Ref:` [ame2020]; Sec.10a of
`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`.
Beans `qou-nial`, `qou-vudb`, `qou-brng`.
"""
from __future__ import annotations

import datetime
import glob
import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, interface_factor, markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

NUCLEI = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
          ("6Li", 3, 3), ("7Li", 3, 4), ("7Be", 4, 3), ("9Be", 4, 5),
          ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20), ("56Fe", 26, 30)]
MIRRORS = [("3He", "3H", 2, 1), ("7Be", "7Li", 4, 3)]


def load_ame():
    f = glob.glob(str(Path(_COMP).parent / "qou-mass/src/qou_mass/data/ame2020.json"))
    raw = json.load(open(f[0], encoding="utf-8"))
    out = {}
    for e in raw["entries"]:
        b = e.get("binding_energy_per_A_keV")
        if b is None or e.get("mass_excess_estimated"):
            continue
        out[(e["Z"], e["N"])] = mpf(str(b)) * e["A"] / 1000
    return out


def main() -> int:
    q = Q_MP
    h = hecke_h(q)
    z = markov_z(q)
    d = flavor_split_leading(q)
    from qou_substrate.constants import M_E_MEV as _ME  # noqa: E402
    alpha = mpf(_ME) / (q * (q - 1))

    f_pn = z - h * (mpf(1) / 2 - d / 4)
    SUM = {"pp": interface_factor("positive", q), "pn": f_pn,
           "nn": interface_factor("negative", q)}
    # product rule: only pp is shifted (Q_i*Q_j = 1 there and 0 elsewhere),
    # so nn joins the pn baseline.
    PROD = {"pp": f_pn + h / 2, "pn": f_pn, "nn": f_pn}

    def B(rule, Z, N):
        """Sec.10a log form on the CHAIN p^Z n^N: Z-1 pp, one pn, N-1 nn bonds."""
        tot = mpf(0)
        for cnt, key in ((Z - 1, "pp"), (1, "pn"), (N - 1, "nn")):
            if cnt > 0:
                tot += cnt * (-alpha * mp.log(rule[key]))
        return tot

    ame = load_ame()
    rows, ls, lp, n = [], mpf(0), mpf(0), 0
    for nm, Z, N in NUCLEI:
        if (Z, N) not in ame:
            continue
        a_, s, p = ame[(Z, N)], B(SUM, Z, N), B(PROD, Z, N)
        rs, rp = s / a_, p / a_
        ls += abs(mp.log(rs)); lp += abs(mp.log(rp)); n += 1
        rows.append({"nucleus": nm, "Z": Z, "N": N,
                     "ame_MeV": mp.nstr(a_, 10),
                     "sum_rule_MeV": mp.nstr(s, 10), "sum_over_ame": mp.nstr(rs, 6),
                     "prod_rule_MeV": mp.nstr(p, 10), "prod_over_ame": mp.nstr(rp, 6)})
    mean_s, mean_p = ls / n, lp / n

    mirrors = []
    for n1, n2, Z, N in MIRRORS:
        if (Z, N) not in ame or (N, Z) not in ame:
            continue
        obs = ame[(Z, N)] - ame[(N, Z)]
        ds = B(SUM, Z, N) - B(SUM, N, Z)
        dp = B(PROD, Z, N) - B(PROD, N, Z)
        mirrors.append({"pair": f"{n1}/{n2}", "A": Z + N,
                        "observed_MeV": mp.nstr(obs, 10),
                        "sum_rule_MeV": mp.nstr(ds, 10),
                        "sum_over_obs": mp.nstr(ds / obs, 6),
                        "prod_rule_MeV": mp.nstr(dp, 10),
                        "prod_over_obs": mp.nstr(dp / obs, 6)})

    print("Sum rule vs product rule, Sec.10a log form on the chain assembly\n")
    print(f"  alpha = {mp.nstr(alpha, 12)} MeV")
    print(f"  SUM   f: pp={mp.nstr(SUM['pp'],10)}  pn={mp.nstr(SUM['pn'],10)}  "
          f"nn={mp.nstr(SUM['nn'],10)}")
    print(f"  PROD  f: pp={mp.nstr(PROD['pp'],10)}  pn={mp.nstr(PROD['pn'],10)}  "
          f"nn={mp.nstr(PROD['nn'],10)}   (nn joins the baseline)\n")
    print(f"  {'nuc':>6}{'Z':>3}{'N':>3}{'AME':>11}{'SUM':>11}{'S/AME':>8}"
          f"{'PROD':>11}{'P/AME':>8}")
    for r in rows:
        print(f"  {r['nucleus']:>6}{r['Z']:>3}{r['N']:>3}{r['ame_MeV']:>11}"
              f"{r['sum_rule_MeV']:>11}{r['sum_over_ame']:>8}"
              f"{r['prod_rule_MeV']:>11}{r['prod_over_ame']:>8}")
    print(f"\n  mean |ln(model/AME)| over {n}:   SUM {mp.nstr(mean_s, 6)}   "
          f"PROD {mp.nstr(mean_p, 6)}")
    print(f"  -> {'PROD' if mean_p < mean_s else 'SUM'} is closer on absolute binding")

    print("\n  mirror splittings:")
    for m in mirrors:
        print(f"    {m['pair']:>10} A={m['A']:<3} observed {m['observed_MeV']:>12}"
              f"   SUM {m['sum_rule_MeV']:>12} ({m['sum_over_obs']})"
              f"   PROD {m['prod_rule_MeV']:>12} ({m['prod_over_obs']})")
    print("    -> the product rule's A=3 agreement is a FLAT LINE crossing a rising")
    print("       curve, not a fit: it is identical at A=7 while the observed has")
    print("       doubled. Same trap as qou-vudb.")

    assertions = [
        {"name": "the product rule is WORSE than the sum rule on absolute binding",
         "passed": bool(mean_p > mean_s)},
        {"name": "the product rule's mirror splitting is FLAT in A -- identical at "
                 "A=3 and A=7 -- so its A=3 agreement is not structural",
         "passed": bool(len(mirrors) == 2
                        and abs(mpf(mirrors[0]["prod_rule_MeV"])
                                - mpf(mirrors[1]["prod_rule_MeV"])) < mpf(10) ** -20)},
        {"name": "the sum rule's mirror splitting is flat too, for the same reason",
         "passed": bool(len(mirrors) == 2
                        and abs(mpf(mirrors[0]["sum_rule_MeV"])
                                - mpf(mirrors[1]["sum_rule_MeV"])) < mpf(10) ** -20)},
        {"name": "both rules are more than 2x short on absolute binding at A >= 4",
         "passed": all(mpf(r["sum_over_ame"]) < mpf("0.5")
                       and mpf(r["prod_over_ame"]) < mpf("0.5")
                       for r in rows if r["Z"] + r["N"] >= 4)},
        {"name": "the product rule DOES move f_nn onto the pn baseline, which is "
                 "the structural change qou-nial identified",
         "passed": bool(abs(PROD["nn"] - PROD["pn"]) < mpf(10) ** -40)},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "Sum rule vs product rule on the binding table under the Sec.10a log "
            "form and the chain assembly. The product rule is WORSE on absolute "
            "binding (mean |ln(model/AME)| 0.940 against 0.808) because moving f_nn "
            "onto the pn baseline removes binding from every nucleus with an nn "
            "bond. It matches the A=3 mirror splitting to 2.5% but its mirror "
            "difference is FLAT in A, identical at A=7 where the observed has "
            "doubled -- a flat line crossing a rising curve, not a fit. Both rules "
            "are ~3x short on absolute binding for A >= 4, which is the extensivity "
            "problem and is untouched by either. RECOMMENDATION: do not switch."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "assembly": "chain (Z-1 pp, 1 pn, N-1 nn bonds), Sec.10a log form",
        "bond_factors": {
            "sum_rule": {k: mp.nstr(v, 20) for k, v in SUM.items()},
            "product_rule": {k: mp.nstr(v, 20) for k, v in PROD.items()},
        },
        "alpha_MeV": mp.nstr(alpha, 20),
        "table": rows,
        "mean_abs_log_ratio": {"sum_rule": mp.nstr(mean_s, 8),
                               "product_rule": mp.nstr(mean_p, 8),
                               "n": n},
        "mirrors": mirrors,
        "recommendation": "do NOT switch interface_factor to the product rule",
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(a) -- a measurement against AME2020 under one assembly (the chain). "
            "It does not refute the product rule as a STRUCTURAL claim (qou-nial "
            "stands); it measures its cost under the current assembly, which is "
            "what was asked. Nothing wired."),
        "beans": ["qou-nial", "qou-vudb", "qou-brng"],
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "bond-rule-dashboard-comparison.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
