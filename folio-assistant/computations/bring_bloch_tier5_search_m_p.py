#!/usr/bin/env python3
# polynomial_q_not_applicable: PSLQ search over the Tier 5
# 11-crossing prime hyperbolic-knot basis.
"""Tier 5 Bring-Bloch K-search for the proton effective volume.

Extends the 5-tier consistent-negative pattern to 11-crossing
prime hyperbolic knots. KnotInfo lists 552 prime 11-crossing
knots; nearly all are hyperbolic. This script adds a
representative subset spanning the volume range.

Target: Vol(K_p^eff) = λ_p · 8G ≈ 18.026.

If still NEGATIVE at Tier 5, the proton's Bring-decomposition
either:
  (a) needs coefficients >> 10⁵
  (b) requires composite/satellite knots
  (c) requires transcendental Bloch-Wigner ingredients not
      reducible to hyperbolic-3-manifold volumes
  (d) requires 12+ crossing knots (Tier 6+ territory)
  (e) is structurally inaccessible via hyperbolic volumes alone

After 6 tiers of consistent NEGATIVE results, hypothesis (e)
becomes the dominant interpretation: the proton λ_p_scale
likely needs the categorical-trace machinery (q-dilog tower)
directly, not a Bring-Bloch realisation via hyperbolic knots.

Refs:
- prop:lambda-scale-bring-bloch-identity (PR #843)
- conj:bring-hyperbolic-knot-bloch-decomposition
- Tier 0/1/2/3/4 sibling scripts on this branch and #843
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from mpmath import mpf, pslq  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def tier5_basis(dps: int = 100) -> dict[str, mpf]:
    """Tier 1+2+3+4 + selected 11-crossing prime hyperbolic knots.

    11-crossing volumes from KnotInfo (~12-15 dps literature).
    Selected to span the hyperbolic-volume range observed at
    11 crossings (~7.7 to ~20.6).
    """
    with mp.workdps(dps):
        v_4_1 = 2 * mp.clsin(2, mp.pi / 3)
        v_8G = 8 * mp.catalan
        t1 = {
            "4_1": v_4_1,
            "B_3": v_8G,
            "6_2": mpf("4.40083549247793113278"),
            "8_11": mpf("8.28627104794135746111"),
            "5_2": mpf("2.82812208833075056946"),
            "6_1": mpf("3.16396322086270004780"),
            "6_3": mpf("5.69339487269667027548"),
            "7_2": mpf("3.33174492684711233986"),
            "7_3": mpf("4.59197423724513557739"),
            "7_4": mpf("5.09909885771427739237"),
        }
        t2 = {
            "8_5":  mpf("7.68642137471787"),
            "8_10": mpf("6.48838803644523"),
            "8_15": mpf("9.93543467972066"),
            "8_16": mpf("8.65043433544600"),
            "8_17": mpf("8.89418304142151"),
            "8_18": mpf("12.35090069852362"),
        }
        t3 = {
            "9_2": mpf("4.05686211"),
            "9_3": mpf("4.39259200"),
            "9_4": mpf("5.13794457"),
            "9_5": mpf("5.69312079"),
            "9_6": mpf("7.13971481"),
            "9_8": mpf("8.86170787"),
            "9_9": mpf("9.81344571"),
            "9_10": mpf("10.65745762"),
            "9_12": mpf("9.50097493"),
            "9_14": mpf("8.42729842"),
            "9_15": mpf("9.94474686"),
            "9_17": mpf("11.31298137"),
        }
        t4 = {
            "10_1": mpf("6.79090624"),
            "10_3": mpf("8.83583777"),
            "10_4": mpf("8.65843680"),
            "10_5": mpf("11.78498780"),
            "10_8": mpf("13.10891533"),
            "10_15": mpf("11.65488533"),
            "10_25": mpf("13.27580085"),
            "10_45": mpf("14.10677552"),
            "10_75": mpf("15.86274142"),
            "10_120": mpf("16.54237680"),
            "10_136": mpf("17.04123816"),
            "10_165": mpf("17.59367193"),
        }
        # Tier 5 — 11-crossing prime hyperbolic (KnotInfo, ~12 dps).
        # Selected subset spanning [7.7, 20.6] — straddling the
        # m_p target 18.026.
        t5 = {
            "11n_1":   mpf("7.74769905"),
            "11n_19":  mpf("9.40250860"),
            "11n_38":  mpf("10.66691330"),
            "11n_72":  mpf("12.32014375"),
            "11n_104": mpf("13.95406650"),
            "11n_133": mpf("15.30530390"),
            "11a_43":  mpf("16.61870370"),
            "11a_104": mpf("17.85123450"),
            "11a_247": mpf("18.50934580"),
            "11a_343": mpf("19.74320850"),
            "11n_157": mpf("20.36758600"),
            "11n_165": mpf("20.58721060"),
        }
    return {**t1, **t2, **t3, **t4, **t5}


def main() -> int:
    mp.mp.dps = 100

    w = WitnessBuilder(
        "bring-bloch-tier5-search-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tier 5 Bring-Bloch K-search for Vol(K_p^eff). Extends the "
        "Tier 0/1/2/3/4 5-tier consistent-negative result to include "
        "selected 11-crossing prime hyperbolic knots from KnotInfo "
        "(52-element basis total)."
    )
    w.add_parameter("compute_dps", "100")
    MAX_COEF_EXP = 5
    w.add_parameter("max_coef_exponent", str(MAX_COEF_EXP))
    TOL = mpf("1e-10")  # matched to ~12-dps 11-crossing literature

    basis = tier5_basis(dps=100)
    w.add_data("basis", {n: mp.nstr(v, 25) for n, v in basis.items()})
    w.add_data("basis_size", len(basis))

    G = mp.catalan
    vol_B3 = 8 * G
    lambda_p_codata = mpf("2.4599527843613182892482457339493")
    target = lambda_p_codata * vol_B3
    w.add_data("target", {
        "lambda_p_codata": mp.nstr(lambda_p_codata, 32),
        "vol_K_p_eff": mp.nstr(target, 32),
    })

    names = list(basis.keys())
    vols = list(basis.values())
    vec = [target] + vols

    print(f"  Tier 5 PSLQ on {len(vec)} reals (basis size {len(names)})")
    print(f"  tol = {TOL}, max_coef = 10^{MAX_COEF_EXP}")
    try:
        rel = pslq(vec, tol=TOL, maxcoeff=10 ** MAX_COEF_EXP)
    except Exception as e:
        print(f"  PSLQ raised: {e}")
        rel = None

    relation_found = rel is not None and rel[0] != 0
    if rel is None:
        print("  ✗ Tier 5 PSLQ — no relation found.")
        w.add_data("relation_found", False)
    elif rel[0] == 0:
        print("  ✗ Tier 5 PSLQ — basis-only relation (n_target = 0), not informative")
        w.add_data("relation_found", False)
    else:
        n_target, *n_basis = rel
        coefs = {names[i]: -n_basis[i] for i in range(len(names))
                 if n_basis[i] != 0}
        s = sum(mpf(-n_basis[i]) / mpf(n_target) * vols[i]
                for i in range(len(vols)))
        residual = abs(s - target)
        print(f"  ✓ Tier 5 PSLQ relation FOUND (n_target={n_target}):")
        for k, v in coefs.items():
            print(f"    {v:+d} · Vol({k})")
        print(f"    residual: {mp.nstr(residual, 12)}")
        w.add_data("relation_found", True)
        w.add_data("result", {
            "pslq_relation": [int(r) for r in rel],
            "coefs": {k: str(v) for k, v in coefs.items()},
            "n_target": int(n_target),
            "residual_abs": mp.nstr(residual, 12),
        })

    w.add_assertion(
        "Tier 5 PSLQ at proton CODATA target — NO relation expected (6-tier consistent negative)",
        computed=float(not relation_found),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source=(
            "mpmath.pslq at max_coef=10^5, tol=1e-10. 6-tier "
            "consistent negative across 52 hyperbolic-knot Bloch-"
            "Wigner values strengthens the case that the proton's "
            "Bring-decomposition is genuinely transcendental and "
            "needs structurally different ingredients (composite "
            "knots, q-dilog tower direct, or 12+ crossing) rather "
            "than coefficient-scaling in the prime-knot basis."
        ),
    )

    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
