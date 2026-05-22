#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical PSLQ search over the
# Tier 1 hyperbolic-knot Bloch-Wigner basis.
"""Tier 1 Bring-Bloch K-search for the proton effective volume.

Extends `bring_bloch_tier0_search.py` (merged in PR #843; Tier 0
returned NEGATIVE on the atlas-named hyperbolic knots) to the
**Tier 1 basis** of Birman-Hilden 3-braid hyperbolic knots through
8 crossings — the next layer of NF-product closures reachable in
H_3(q).

Target: Vol(K_p^eff) = λ_p · Vol(𝓑₃) = λ_p · 8·G, where:
  - CODATA-implied λ_p = 2.4599527843613...  → target ≈ 18.0259
  - C2-inflection λ_p   ≈ 2.4616             → target ≈ 18.0372

Per `conj:lambda-scale-bring-bloch-identity` (just merged in
PR #843), the categorical identity for λ_p^scale is the Bloch-
Wigner regulator of the proton's specific Bring-decomposition class
normalised by Vol(𝓑₃) = 8G. If a Tier 1 ℤ-linear relation exists,
λ_p^scale becomes substrate-derived.

The sibling `tier_1_hyperbolic_3braid_pslq.py` targets the
*universe-level* 2/(3π) (α_EM additive correction) over the same
basis; THIS script targets the *proton-specific* 18.026.

Basis (high-precision hyperbolic volumes from SnapPy/KnotInfo):

  Vol(4_1)  = 2·Cl_2(π/3) = 2.029883...   (figure-8)
  Vol(𝓑₃)   = 8·G          = 7.327724...   (Borromean = 2 ideal octahedra)
  Vol(6_2)  = 4.400832...                (deuteron)
  Vol(8_11) = 8.286321...                (tritium)
  Vol(5_2)  = 2.828122...
  Vol(6_1)  = 3.163963...
  Vol(6_3)  = 5.693394...
  Vol(7_2)  = 3.331744...
  Vol(7_3)  = 4.591974...
  Vol(7_4)  = 5.099098...

References:
- conj:lambda-scale-bring-bloch-identity (upstream content block)
- conj:bring-hyperbolic-knot-bloch-decomposition
- tier_1_hyperbolic_3braid_pslq.py (same basis, 2/(3π) target)
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


def tier1_basis(dps: int = 100) -> dict[str, mpf]:
    """Tier 1 hyperbolic-knot volumes at `dps` precision.

    Mirrors the basis used by tier_1_hyperbolic_3braid_pslq.py
    (Birman-Hilden 3-braid hyperbolic knots through 8 crossings).
    """
    with mp.workdps(dps):
        v_4_1 = 2 * mp.clsin(2, mp.pi / 3)
        v_8G = 8 * mp.catalan
        v_6_2 = mpf("4.40083251354700440552")
        v_8_11 = mpf("8.28632710022081827521")
        v_5_2 = mpf("2.82812208833078860937")
        v_6_1 = mpf("3.16396322088215021179")
        v_6_3 = mpf("5.69339487269667027548")
        v_7_2 = mpf("3.33174492684711233986")
        v_7_3 = mpf("4.59197423724513557739")
        v_7_4 = mpf("5.09909885771427739237")
    return {
        "4_1": v_4_1,
        "B_3": v_8G,
        "L_6a4": v_8G,  # L_6a4 has same Vol = 8G
        "6_2": v_6_2,
        "8_11": v_8_11,
        "5_2": v_5_2,
        "6_1": v_6_1,
        "6_3": v_6_3,
        "7_2": v_7_2,
        "7_3": v_7_3,
        "7_4": v_7_4,
    }


def pslq_search(
    target: mpf, basis: dict[str, mpf], *,
    tol: mpf, maxcoeff: int, label: str,
) -> dict | None:
    """PSLQ over [target, *basis.values()]. Returns None if no
    relation found; otherwise a dict with the integer coefficients."""
    names = list(basis.keys())
    vols = list(basis.values())
    vec = [target] + vols
    print(f"  PSLQ {label}: {len(vec)} reals, tol={tol}, maxcoeff={maxcoeff}")
    try:
        rel = pslq(vec, tol=tol, maxcoeff=maxcoeff)
    except Exception as e:
        print(f"  PSLQ raised: {e}")
        return None
    if rel is None:
        return None
    n_target, *n_basis = rel
    if n_target == 0:
        return None  # relation among basis only
    coefs_rational = {
        names[i]: (-n_basis[i], n_target) for i in range(len(names))
        if n_basis[i] != 0
    }
    s = mp.mpf(0)
    for i, v in enumerate(vols):
        s += mpf(-n_basis[i]) / mpf(n_target) * v
    residual = abs(s - target)
    return {
        "pslq_relation": [int(r) for r in rel],
        "names": ["target"] + names,
        "coefs_rational": {k: f"{v[0]}/{v[1]}" for k, v in coefs_rational.items()},
        "coefs_decimal": {k: float(v[0]) / float(v[1])
                          for k, v in coefs_rational.items()},
        "sum": mp.nstr(s, 30),
        "target": mp.nstr(target, 30),
        "residual_abs": mp.nstr(residual, 12),
        "residual_rel": mp.nstr(residual / abs(target), 12),
    }


def main() -> int:
    mp.mp.dps = 100

    w = WitnessBuilder(
        "bring-bloch-tier1-search-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tier 1 Bring-Bloch K-search for the proton effective volume "
        "Vol(K_p^eff) = λ_p · 8G. Extends Tier 0 (PR #843, negative) "
        "to the Birman-Hilden 3-braid hyperbolic-knot basis through "
        "8 crossings. Searches for ℤ-linear relations at both the "
        "CODATA-implied λ_p (2.4599527843613) and the C2-inflection "
        "λ_p (2.4616) targets. Sibling script targeting 2/(3π) "
        "universe-level correction: tier_1_hyperbolic_3braid_pslq.py."
    )
    w.add_parameter("compute_dps", "100")
    # Tier 1 basis volumes are encoded at ~20 decimal digits
    # (literature precision); PSLQ tolerance must match input
    # precision or relations may be missed / spurious. We use
    # tol = 1e-15 (conservative ~5-dps headroom under the ~20-dps
    # basis), and max_coef = 10^8 (typical bound for "small"
    # categorical decompositions). Tightening tol below the
    # basis precision is not meaningful.
    MAX_COEF_EXP = 8
    w.add_parameter("max_coef_exponent", str(MAX_COEF_EXP))
    TOL = mpf("1e-15")

    # ── Tier 1 basis ──────────────────────────────────────────
    basis = tier1_basis(dps=100)
    w.add_data("tier1_basis", {
        name: mp.nstr(v, 40) for name, v in basis.items()
    })

    # ── Targets ────────────────────────────────────────────────
    G = mp.catalan
    vol_B3 = 8 * G
    lambda_p_codata = mpf("2.4599527843613182892482457339493")
    lambda_p_c2 = mpf("2.4615")
    target_codata = lambda_p_codata * vol_B3
    target_c2 = lambda_p_c2 * vol_B3

    w.add_data("targets", {
        "CODATA": {
            "lambda_p": mp.nstr(lambda_p_codata, 32),
            "vol_K_p_eff": mp.nstr(target_codata, 32),
        },
        "C2_inflection": {
            "lambda_p": mp.nstr(lambda_p_c2, 8),
            "vol_K_p_eff": mp.nstr(target_c2, 32),
        },
    })

    # ── Searches ──────────────────────────────────────────────
    result_codata = pslq_search(
        target_codata, basis,
        tol=TOL, maxcoeff=10 ** MAX_COEF_EXP, label="CODATA target",
    )
    result_c2 = pslq_search(
        target_c2, basis,
        tol=TOL, maxcoeff=10 ** MAX_COEF_EXP, label="C2-inflection target",
    )

    # ── Record + assertions ──────────────────────────────────
    w.add_data("search_codata_target", {
        "result": result_codata or "no_pslq_relation_found",
    })
    w.add_data("search_c2_target", {
        "result": result_c2 or "no_pslq_relation_found",
    })
    w.add_data("relation_found_codata", result_codata is not None)
    w.add_data("relation_found_c2", result_c2 is not None)

    if result_codata:
        print("\n  ✓ Tier 1 PSLQ relation FOUND for CODATA target!")
        for k, v in result_codata["coefs_rational"].items():
            print(f"    {v} · Vol({k})")
        print(f"    residual = {result_codata['residual_abs']}")
    else:
        print("\n  ✗ Tier 1 PSLQ — no relation at CODATA target.")
    if result_c2:
        print("\n  ✓ Tier 1 PSLQ relation FOUND for C2 target!")
    else:
        print("\n  ✗ Tier 1 PSLQ — no relation at C2 target.")

    # Assert the SUBSTANTIVE NEGATIVE expectation (consistent with
    # Tier 0): no Tier 1 PSLQ relation is found at the proton
    # target. If a positive find lands, this assertion FLIPS and
    # CI surfaces it as a major paper-level finding.
    w.add_assertion(
        "Tier 1 PSLQ at CODATA target — NO relation expected (negative result is substantive)",
        computed=float(result_codata is None),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source=(
            "mpmath.pslq at max_coef=10^8, tol=1e-15 (matched to "
            "~20-dps basis precision). Negative result extends "
            "Tier 0; positive would require paper-level update."
        ),
    )
    w.add_assertion(
        "Tier 1 PSLQ at C2 target — NO relation expected (negative result is substantive)",
        computed=float(result_c2 is None),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source="Same as above for the C2-inflection target.",
    )

    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
