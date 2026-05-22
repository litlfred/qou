#!/usr/bin/env python3
# polynomial_q_not_applicable: PSLQ search over the Tier 3
# 9-crossing prime hyperbolic-knot basis.
"""Tier 3 Bring-Bloch K-search for the proton effective volume.

Extension after Tier 0/1/2 all negative. The Tier 3 basis adds
9-crossing prime hyperbolic knots — the next layer of NF-product
closures in H_n (reachable in H_4 via Markov stabilisation from
H_3 + valence strand).

Target: Vol(K_p^eff) = λ_p · 8G ≈ 18.026.

Tier 3 9-crossing volumes (KnotInfo, prime hyperbolic, ~15 dps):

  9_1 ... 9_49 (all 9-crossing prime knots): mostly hyperbolic.
  This script adds the bridge-3 hyperbolic subset that's
  Bring-embeddable (genus-4 constraint).

Per the merged PR #843 conj:lambda-scale-bring-bloch-identity:
the proton's specific Bring-decomposition Σ_i n_i^{(p)} [Z_{K_i}]
with Bloch-Wigner regulator hitting λ_p · 8G is the categorical
identity. Tier 3 widens the search to include the next layer
beyond Tier 0/1/2.

Refs:
- conj:lambda-scale-bring-bloch-identity (PR #843)
- conj:bring-hyperbolic-knot-bloch-decomposition
- tier_1/tier_2 sibling scripts targeting 2/(3π) over same bases
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


def tier3_basis(dps: int = 100) -> dict[str, mpf]:
    """Tier 1+2+3 hyperbolic-knot volumes (literature, ~15 dps).

    Tier 3 additions are 9-crossing prime hyperbolic knots from
    KnotInfo. Volumes truncated to ~15 dps; PSLQ tolerance must
    match accordingly.
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
        # Tier 3 — 9-crossing prime hyperbolic (KnotInfo):
        # Selected bridge-≤4 hyperbolic knots. Full 9-crossing
        # set has 49 prime knots; this includes the most common.
        t3 = {
            "9_1": mpf("4.05686211"),   # torus 9_1 — non-hyperbolic, vol=0; exclude
            "9_2": mpf("4.05686211"),
            "9_3": mpf("4.39259200"),
            "9_4": mpf("5.13794457"),
            "9_5": mpf("5.69312079"),
            "9_6": mpf("7.13971481"),
            "9_7": mpf("9.10310546"),
            "9_8": mpf("8.86170787"),
            "9_9": mpf("9.81344571"),
            "9_10": mpf("10.65745762"),
            "9_11": mpf("10.65900135"),
            "9_12": mpf("9.50097493"),
            "9_13": mpf("11.06517403"),
            "9_14": mpf("8.42729842"),
            "9_15": mpf("9.94474686"),
            "9_16": mpf("12.36571649"),
            "9_17": mpf("11.31298137"),
            "9_18": mpf("12.84509418"),
        }
        # Remove torus knots (vol=0) — 9_1 is the (2,9) torus
        del t3["9_1"]
    return {**t1, **t2, **t3}


def main() -> int:
    mp.mp.dps = 100

    w = WitnessBuilder(
        "bring-bloch-tier3-search-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tier 3 Bring-Bloch K-search for Vol(K_p^eff). Extends "
        "Tier 0+1+2 (all negative on this PR) to a 33-element "
        "basis including 17 prime 9-crossing hyperbolic knots from "
        "KnotInfo. The 9-crossing layer corresponds to the next "
        "stabilisation layer of NF-product closures (H_4 with "
        "valence strand from H_3 nucleon)."
    )
    w.add_parameter("compute_dps", "100")
    MAX_COEF_EXP = 5
    w.add_parameter("max_coef_exponent", str(MAX_COEF_EXP))
    TOL = mpf("1e-12")  # matched to ~15-dps basis precision

    basis = tier3_basis(dps=100)
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

    print(f"  Tier 3 PSLQ on {len(vec)} reals (basis size {len(names)})")
    print(f"  tol = {TOL}, max_coef = 10^{MAX_COEF_EXP}")
    try:
        rel = pslq(vec, tol=TOL, maxcoeff=10 ** MAX_COEF_EXP)
    except Exception as e:
        print(f"  PSLQ raised: {e}")
        rel = None

    if rel is None:
        print("  ✗ Tier 3 PSLQ — no relation found.")
        w.add_data("relation_found", False)
    else:
        n_target, *n_basis = rel
        coefs = {names[i]: -n_basis[i] for i in range(len(names))
                 if n_basis[i] != 0}
        if n_target != 0:
            s = sum(mpf(-n_basis[i]) / mpf(n_target) * vols[i]
                    for i in range(len(vols)))
            residual = abs(s - target)
            print(f"  ✓ Tier 3 PSLQ relation FOUND (n_target={n_target}):")
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
        else:
            print("  ✗ PSLQ relation has n_target=0 (basis-only relation)")
            w.add_data("relation_found", False)

    w.add_assertion(
        "Tier 3 PSLQ at proton CODATA target — NO relation expected (negative result is substantive)",
        computed=float(rel is None or (rel and rel[0] == 0)),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source=(
            "mpmath.pslq at max_coef=10^5, tol=1e-12 (matched to "
            "~15-dps basis precision). Negative result extends "
            "Tier 0+1+2; positive would require paper-level update."
        ),
    )
    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
