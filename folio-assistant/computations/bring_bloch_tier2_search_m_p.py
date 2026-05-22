#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical PSLQ search over the
# Tier 2 hyperbolic-knot Bloch-Wigner basis.
"""Tier 2 Bring-Bloch K-search for the proton effective volume.

Extends `bring_bloch_tier1_search_m_p.py` (Tier 1 negative for
proton-specific target) to the Tier 2 basis — bridge-3 hyperbolic
knots through 8 crossings, mirroring
`tier_2_hyperbolic_bridge3_pslq.py` which targets 2/(3π).

Target: Vol(K_p^eff) = λ_p · 8G ≈ 18.026 (CODATA) / 18.037 (C2).

Basis: Tier 1 (11 elements) + Tier 2 (6 elements):
  4_1, 𝓑₃, L_{6a4}, 6_2, 8_11, 5_2, 6_1, 6_3, 7_2, 7_3, 7_4,
  8_5, 8_10, 8_15, 8_16, 8_17, 8_18

The Tier-2 knots are 4-braid (bridge-number ≥ 3) hyperbolic
through 8 crossings, not reachable from H_3(q) NF-products.
Literature volumes from KnotInfo (~15 dps; production should
promote to SnapPy 50+ dps).

References:
- conj:lambda-scale-bring-bloch-identity (consumer)
- conj:bring-hyperbolic-knot-bloch-decomposition
- tier_2_hyperbolic_bridge3_pslq.py (2/(3π) target with same basis)
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


def tier2_basis(dps: int = 100) -> dict[str, mpf]:
    """Tier 1 + Tier 2 hyperbolic-knot volumes."""
    with mp.workdps(dps):
        v_4_1 = 2 * mp.clsin(2, mp.pi / 3)
        v_8G = 8 * mp.catalan
        # Tier 1 values (Birman-Hilden 3-braid through 8 crossings)
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
        # Tier 2 additions (bridge-3 8-crossing, 4-braid)
        t2 = {
            "8_5":  mpf("7.68642137471787"),
            "8_10": mpf("6.48838803644523"),
            "8_15": mpf("9.93543467972066"),
            "8_16": mpf("8.65043433544600"),
            "8_17": mpf("8.89418304142151"),
            "8_18": mpf("12.35090069852362"),
        }
    return {**t1, **t2}


def main() -> int:
    mp.mp.dps = 100

    w = WitnessBuilder(
        "bring-bloch-tier2-search-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tier 2 Bring-Bloch K-search for Vol(K_p^eff) = λ_p · 8G. "
        "Extends Tier 0 (PR #843) and Tier 1 (this branch) — both "
        "returned negative — to the bridge-3 hyperbolic-knot basis "
        "through 8 crossings (16-element basis total). Sibling: "
        "tier_2_hyperbolic_bridge3_pslq.py targets 2/(3π) instead."
    )
    w.add_parameter("compute_dps", "100")
    MAX_COEF_EXP = 6  # Tier 2 literature precision is ~15 dps,
    #                  so capping max_coef at 10^6 is appropriate.
    w.add_parameter("max_coef_exponent", str(MAX_COEF_EXP))

    basis = tier2_basis(dps=100)
    w.add_data("tier2_basis", {n: mp.nstr(v, 30) for n, v in basis.items()})

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

    # tol=1e-12 matches Tier 2 KnotInfo basis precision (~14-15 dps
    # strings); a tighter tol would label genuine relations as
    # "missed" rather than informative-negative.
    TOL = mpf("1e-12")
    print(f"  PSLQ on {len(vec)} reals, tol={TOL} (Tier 2 lit "
          f"precision), maxcoeff=10^{MAX_COEF_EXP}")
    try:
        rel = pslq(vec, tol=TOL, maxcoeff=10 ** MAX_COEF_EXP)
    except Exception as e:
        print(f"  PSLQ raised: {e}")
        rel = None

    # `relation_found` semantics: true iff PSLQ returns a non-trivial
    # ℤ-relation whose target coefficient is non-zero. A basis-only
    # relation (rel[0] == 0) is not informative for the target search.
    relation_found = rel is not None and rel[0] != 0
    if rel is None:
        print("  ✗ Tier 2 PSLQ — no relation found.")
        w.add_data("relation_found", False)
    elif rel[0] == 0:
        print("  ✗ Tier 2 PSLQ — basis-only relation (n_target = 0), not informative")
        w.add_data("relation_found", False)
    else:
        n_target, *n_basis = rel
        coefs = {names[i]: -n_basis[i] for i in range(len(names))
                 if n_basis[i] != 0}
        s = sum(mpf(-n_basis[i]) / mpf(n_target) * vols[i]
                for i in range(len(vols)))
        residual = abs(s - target)
        print(f"  ✓ Tier 2 PSLQ relation FOUND:")
        for k, v in coefs.items():
            print(f"    {v:+d} · Vol({k}) (over n_target = {n_target})")
        print(f"    residual: {mp.nstr(residual, 12)}")
        w.add_data("relation_found", True)
        w.add_data("result", {
            "pslq_relation": [int(r) for r in rel],
            "names": ["target"] + names,
            "coefs": {k: str(v) for k, v in coefs.items()},
            "n_target": int(n_target),
            "residual_abs": mp.nstr(residual, 12),
        })

    # Assert SUBSTANTIVE NEGATIVE expectation: no Tier 2 PSLQ
    # relation TARGETING the CODATA λ_p (basis-only relations
    # ignored). If a positive find lands, this assertion flips
    # and CI surfaces it as a major paper-level finding.
    w.add_assertion(
        "Tier 2 PSLQ at proton CODATA target — NO relation expected (negative result is substantive)",
        computed=float(not relation_found),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source=(
            "mpmath.pslq at max_coef=10^6, tol=1e-12 (matched to "
            "~14-15 dps basis precision for Tier 2 KnotInfo values). "
            "Negative result extends Tier 0 + Tier 1; positive "
            "would require paper-level update."
        ),
    )
    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
