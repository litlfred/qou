"""tier_2_higher_bridge_pslq.py

Tier-2 PSLQ extension after the Tier-0 + Tier-1 negatives:
extends the basis to all available high-precision hyperbolic-knot
Bloch-Wigner volumes drawn from SnapPy directly (manifold-name
lookup → high-precision volume), avoiding the lower-precision
hardcoded constants from the deprecated atlas methodology.

Basis (all SnapPy high-precision, ≥60 dps):
  4_1, 5_2, 6_1, 6_2, 6_3, 7_2, 7_3, 7_4, 8_11, 9_42
  K_11a259 (^6Li), L_11a62 (^7Li)
  Borromean (8G via Catalan), figure-8 derived (2·Cl_2(π/3))

Excluded:
  Whitehead Vol = 4G — known Q-degeneracy with Borromean
    (8G = 2·4G; PSLQ would catch THAT before any target relation).

Tolerance: tol=1e-50 with 100-dps PSLQ. All basis values come
from SnapPy at ≥60 dps, justifying the tight tolerance.

If a non-trivial small relation appears with max coeff 10^6,
BringHyperbolicDecomposition is inhabitable from the Tier-2 basis.
If not (negative result), K-theoretic identification requires
content outside the H_3 + bridge-3 hyperbolic regime.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# Ref: [manuscript] conj:bring-hyperbolic-knot-bloch-decomposition

from pathlib import Path

import mpmath
from mpmath import mp, mpf, pslq, pi as mp_pi

from witness_base import WitnessBuilder


def get_snappy_volume(name: str, dps: int = 60) -> mpf:
    """Compute hyperbolic volume of a knot/link by SnapPy manifold
    name at the requested decimal precision."""
    import snappy
    mpmath.mp.dps = max(mpmath.mp.dps, dps + 5)
    M = snappy.Manifold(name)
    # high_precision().volume() returns an mpmath mpf at mp.dps
    return mpf(str(M.high_precision().volume()))


def main() -> None:
    mp.dps = 100
    target = 2 / (3 * mp_pi)

    # Cl_2 / Catalan-derived basis members (algebraically exact)
    cl2_pi_third = mpmath.clsin(2, mp_pi / 3)
    catalan = mpmath.catalan
    v_4_1 = 2 * cl2_pi_third
    v_8G = 8 * catalan

    # SnapPy high-precision hyperbolic volumes (at 60 dps)
    snappy_knots = [
        ("5_2", "Vol(5_2)"),
        ("6_1", "Vol(6_1)"),
        ("6_2", "Vol(6_2)"),
        ("6_3", "Vol(6_3)"),
        ("7_2", "Vol(7_2)"),
        ("7_3", "Vol(7_3)"),
        ("7_4", "Vol(7_4)"),
        ("8_11", "Vol(8_11)"),
        ("9_42", "Vol(9_42)"),
        ("11a259", "Vol(K_11a259)"),
        ("L11a62", "Vol(L_11a62)"),
    ]

    snappy_vols = []
    snappy_labels = []
    for manifold_name, label in snappy_knots:
        vol = get_snappy_volume(manifold_name, dps=60)
        snappy_vols.append(vol)
        snappy_labels.append(label)

    basis = [target, v_4_1, v_8G] + snappy_vols
    labels = ["2/(3π)", "2·Cl_2(π/3)", "8G"] + snappy_labels

    relation = pslq(basis, tol=mpf("1e-50"), maxcoeff=10**6)

    payload = {
        "computation": "tier-2-higher-bridge-pslq",
        "description": (
            "Tier-2 PSLQ extension over hyperbolic knots from "
            "SnapPy at high precision (≥60 dps). All basis values "
            "now come from SnapPy directly (replacing earlier "
            "hardcoded atlas constants which had ≤5 sig figs for "
            "K_11a259 / L_11a62 and contained transcription errors "
            "for several other knots). Tests whether 2/(3π) lies "
            "in the integer-multiple lattice of these BW values."
        ),
        "contentBlock": "conj:bring-hyperbolic-knot-bloch-decomposition",
        "precision_dps": 100,
        "tolerance": "1e-50",
        "tolerance_note": (
            "All basis values at ≥60 dps via SnapPy "
            "high_precision().volume() or via mpmath clsin/catalan "
            "(algebraically exact). Whitehead Vol = 4G excluded "
            "as known Q-degeneracy with Borromean (8G = 2·4G)."
        ),
        "maxcoeff": 10**6,
        "basis_labels": labels,
        "basis_values_55dp": [str(b)[:60] for b in basis],
        "tier_0_baseline": (
            "tier-0-atlas-pslq-check.witness.json (negative)"
        ),
        "tier_1_baseline": (
            "tier-1-hyperbolic-3braid-pslq.witness.json (negative)"
        ),
        "relation_found": relation is not None,
        "relation": [int(x) for x in relation] if relation else None,
        "interpretation": (
            f"non-trivial small relation found — Tier-2 basis "
            f"({len(basis)} BW values) suffices to span 2/(3π); "
            "BringHyperbolicDecomposition inhabitable. "
            "Verify at higher precision before accepting."
            if relation
            else (
                f"NO non-trivial small relation at {mp.dps} dps "
                f"with max coeff {10**6} and tol 1e-50 over a "
                f"{len(basis)}-element high-precision SnapPy basis. "
                "K-theoretic identification requires content "
                "outside the H_3 + bridge-3 hyperbolic regime — "
                "either genuinely higher Heegaard genus or a "
                "non-NF representative. Three negative tiers now "
                "rule out the 'atlas + bridge-3' hypothesis."
            )
        ),
    }

    out = (
        WitnessBuilder.wrap_legacy(
            "tier-2-higher-bridge-pslq",
            payload,
            script_path=__file__,
            engine="mpmath",
        )
        .set_audit_only("docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
        .save()
    )

    print(f"Result: {payload['interpretation']}")
    if relation:
        print(f"Relation: {relation}")
        for label, coeff in zip(labels, relation):
            if coeff != 0:
                print(f"  {coeff:+d} * {label}")
    print(f"Witness written to {out}")


if __name__ == "__main__":
    main()
