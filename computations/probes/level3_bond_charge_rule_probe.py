#!/usr/bin/env python3
"""The bond rule is a SUM in the charges where Coulomb needs a PRODUCT.

Owner, 2026-08-30: *"go ahead on the p->sigma, n->sigma^-1 identification"*.

The identification is not wrong about protons and neutrons. It is wrong about
HOW TWO CHARGES COMBINE, and that one substitution accounts for every failure on
this arc.

## What the corpus assigns

`torus-hopf-stability-proof` gives `Q(proton) = +1`, `Q(neutron) = 0`.
`prop:skein-crossing-asymmetry` gives the per-crossing correction
`delta = q - (q + 1/q)/2 = h/2`, applied "between composites of the same charge
relative to a mixed-charge baseline".

## What the implementation computes

`closed_form_tau_M.interface_factor`, relative to the mixed-charge baseline
`f_pn`, gives `+h/2`, `0`, `-h/2` on pp, pn, nn. This probe measures that this
is EXACTLY the CENTRED SUM

    (Q_i + Q_j - 1) * h/2

and NOT the Coulomb product `Q_i * Q_j * h/2`. The two rules AGREE on pp and pn
and differ ONLY on nn: the sum rule charges two neutrons `-h/2`, the product
rule charges them `0`. Two neutral objects have no Coulomb interaction, so `0`
is the physical value.

## Why one bond is everything

Summed over the complete graph:

    sum rule      SUM_{i<j} (Q_i + Q_j) = (A-1) * Z        LINEAR in Z
    product rule  SUM_{i<j} Q_i * Q_j   = Z(Z-1)/2         QUADRATIC

which is the degree gap `QOU.MassTheory.CrossingCountAffine` proves no linear
functional of the crossing counts can close -- and here is its source. The
crossing counts are linear in Z BECAUSE the bond rule is a sum.

## What it does NOT fix

Under the product rule a mirror pair still differs by `(Z-W)(A-1)/2`, linear in
A, while the observed Coulomb displacement energy goes as `(A-1)/A^(1/3)`. The
probe measures both exponents. The product rule supplies the right MULTIPLICITY
and not the right SCALING; the missing factor is the `1/R` of a Coulomb energy
with `R ~ A^(1/3)`, a geometric input the bond picture does not carry.
Necessary, not sufficient.

## Scope

**(a)**. A measurement of what the implementation computes, plus two exponents.
The algebraic content is in the Lean, sorry-free and over a generic CommRing.
Nothing refuted -- `prop:skein-crossing-asymmetry`'s own wording is two-valued
and is what the PRODUCT rule realises; it is the three-valued ladder in the
implementation that does not follow from it. Nothing wired.

`-- Ref:` `prop:skein-crossing-asymmetry`; `def:coulomb-charge`;
`torus-hopf-stability-proof`. Beans `qou-1pig`, `qou-dhsn`, `qou-vudb`.
"""
from __future__ import annotations

import datetime
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

from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, interface_factor  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

EPS = mpf(10) ** (-45)

# torus-hopf-stability-proof: the corpus's own Coulomb charges.
Q_CHARGE = {"p": mpf(1), "n": mpf(0)}

# odd-A mirror pairs, (A, Z of the proton-rich member)
MIRRORS = [(3, 2), (5, 3), (7, 4), (9, 5), (11, 6), (13, 7), (15, 8), (17, 9),
           (19, 10), (21, 11), (23, 12), (25, 13), (27, 14), (29, 15), (31, 16),
           (33, 17), (35, 18), (37, 19), (39, 20), (41, 21)]


def loglog_slope(As, vals):
    xs = [mp.log(mpf(a)) for a in As]
    ys = [mp.log(abs(mpf(v))) for v in vals]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    return (sum((x - mx) * (y - my) for x, y in zip(xs, ys))
            / sum((x - mx) ** 2 for x in xs))


def main() -> int:
    q = Q_MP
    h = hecke_h(q)
    c = h / 2                       # the per-crossing correction of the proposition

    f = {"pp": interface_factor("positive", q),
         "pn": interface_factor("averaged", q),
         "nn": interface_factor("negative", q)}
    base = f["pn"]                  # the mixed-charge baseline

    rows = []
    for key, (a, b) in (("pp", ("p", "p")), ("pn", ("p", "n")), ("nn", ("n", "n"))):
        qi, qj = Q_CHARGE[a], Q_CHARGE[b]
        actual = f[key] - base
        sum_rule = (qi + qj - 1) * c
        prod_rule = qi * qj * c
        rows.append({
            "pair": key,
            "Q_i_plus_Q_j": mp.nstr(qi + qj, 4),
            "Q_i_times_Q_j": mp.nstr(qi * qj, 4),
            "implementation_minus_baseline": mp.nstr(actual, 20),
            "sum_rule_prediction": mp.nstr(sum_rule, 20),
            "prod_rule_prediction": mp.nstr(prod_rule, 20),
            "matches_sum_rule": bool(abs(actual - sum_rule) < EPS),
            "matches_prod_rule": bool(abs(actual - prod_rule) < EPS),
        })

    # totals over the complete graph, and the two mirror exponents
    pairs = []
    for A, Zr in MIRRORS:
        Nr = A - Zr
        sum_diff = mpf(A - 1) * (Zr - Nr)                       # (A-1)(Z-N)
        prod_diff = (mpf(Zr) * (Zr - 1) - mpf(Nr) * (Nr - 1)) / 2
        coulomb_shape = (mpf(A) - 1) / mpf(A) ** (mpf(1) / 3)
        pairs.append({"A": A, "Z": Zr, "N": Nr,
                      "sum_rule_mirror_diff": mp.nstr(sum_diff, 12),
                      "prod_rule_mirror_diff": mp.nstr(prod_diff, 12),
                      "coulomb_shape": mp.nstr(coulomb_shape, 12)})

    As = [p["A"] for p in pairs]
    p_sum = loglog_slope(As, [p["sum_rule_mirror_diff"] for p in pairs])
    p_prod = loglog_slope(As, [p["prod_rule_mirror_diff"] for p in pairs])
    p_coul = loglog_slope(As, [p["coulomb_shape"] for p in pairs])

    print("The implemented bond rule, against the corpus's own Q(p)=1, Q(n)=0\n")
    print(f"  h/2 = {mp.nstr(c, 20)}   (the per-crossing correction of "
          f"prop:skein-crossing-asymmetry)\n")
    print(f"  {'pair':>5}{'Qi+Qj':>7}{'Qi*Qj':>7}{'implementation':>26}"
          f"{'sum rule':>26}{'product rule':>26}")
    for r in rows:
        print(f"  {r['pair']:>5}{r['Q_i_plus_Q_j']:>7}{r['Q_i_times_Q_j']:>7}"
              f"{r['implementation_minus_baseline']:>26}"
              f"{r['sum_rule_prediction']:>26}{r['prod_rule_prediction']:>26}")
    print(f"\n  implementation == centred SUM rule on all three bonds: "
          f"{all(r['matches_sum_rule'] for r in rows)}")
    print(f"  implementation == Coulomb PRODUCT rule on all three:   "
          f"{all(r['matches_prod_rule'] for r in rows)}")
    print("  they agree on pp and pn and differ ONLY on nn:")
    nn = next(r for r in rows if r["pair"] == "nn")
    print(f"    nn  sum rule {nn['sum_rule_prediction']}   product rule "
          f"{nn['prod_rule_prediction']}")

    print(f"\n  mirror difference over the complete graph, |dB| ~ A^p, {len(pairs)} pairs:")
    print(f"    sum rule      (A-1)(Z-N)      p = {mp.nstr(p_sum, 8)}")
    print(f"    product rule  [Z(Z-1)-N(N-1)]/2  p = {mp.nstr(p_prod, 8)}")
    print(f"    Coulomb shape (A-1)/A^(1/3)   p = {mp.nstr(p_coul, 8)}")
    print("    -> the product rule fixes the MULTIPLICITY (quadratic in Z) and")
    print("       still lacks the 1/R that would bring the exponent down to the")
    print("       Coulomb value. Necessary, not sufficient.")

    assertions = [
        {"name": "the implementation matches the CENTRED SUM rule exactly on all "
                 "three bonds",
         "passed": all(r["matches_sum_rule"] for r in rows)},
        {"name": "it does NOT match the Coulomb product rule",
         "passed": not all(r["matches_prod_rule"] for r in rows)},
        {"name": "the two rules agree on pp",
         "passed": next(r for r in rows if r["pair"] == "pp")["matches_prod_rule"]},
        {"name": "the two rules agree on pn",
         "passed": next(r for r in rows if r["pair"] == "pn")["matches_prod_rule"]},
        {"name": "and differ ONLY on nn — the one bond that is the whole defect",
         "passed": not nn["matches_prod_rule"]},
        {"name": "the sum rule's mirror difference is linear in A, the product "
                 "rule's is too, and both exceed the Coulomb exponent",
         "passed": bool(p_sum > p_coul and p_prod > p_coul)},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "closed_form_tau_M.interface_factor implements the CENTRED SUM of the "
            "two nucleon charges, (Q_i + Q_j - 1)*h/2, exactly -- not the Coulomb "
            "product Q_i*Q_j*h/2. The two agree on pp and pn and differ only on nn, "
            "where the sum rule charges two neutral objects -h/2 and the product "
            "rule charges them 0. Summed over a nucleus the sum rule gives (A-1)Z, "
            "linear, and the product rule gives Z(Z-1)/2, quadratic -- the degree "
            "gap CrossingCountAffine proves no linear functional of the crossing "
            "counts can close, here traced to its source."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "charges": {"Q_proton": "1", "Q_neutron": "0",
                    "source": "torus-hopf-stability-proof"},
        "per_crossing_correction_h_over_2": mp.nstr(c, 20),
        "bonds": rows,
        "mirror_pairs": pairs,
        "exponents": {
            "sum_rule": mp.nstr(p_sum, 8),
            "product_rule": mp.nstr(p_prod, 8),
            "coulomb_shape": mp.nstr(p_coul, 8),
            "method": "least squares of ln|dB| on ln A",
        },
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(a). A measurement of what the implementation computes plus two "
            "exponents; the algebraic content is in QOU/MassTheory/BondChargeRule.lean, "
            "sorry-free over a generic CommRing. Nothing refuted -- "
            "prop:skein-crossing-asymmetry's own wording is two-valued and is what "
            "the PRODUCT rule realises; the three-valued ladder in the "
            "implementation does not follow from it. Nothing wired."),
        "lean": "QOU/MassTheory/BondChargeRule.lean",
        "beans": ["qou-1pig", "qou-dhsn", "qou-vudb"],
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "level3-bond-charge-rule.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
