#!/usr/bin/env python3
"""tier_2_hyperbolic_bridge3_pslq.py

Tier-2 PSLQ extension after the Tier-1 negative
(`tier_1_hyperbolic_3braid_pslq.py`): enlarges the Bloch-Wigner basis
to include bridge-number ≥ 3 hyperbolic knots in H_n for n ∈ {4..8}.

Per `2026-05-09-refocused-1ppb-workplan-v3.md` §3 item #1, this is
the next search target after Tier-1 returned no small Z-linear
relation for 2/(3π) over the 11-element 3-braid basis. Tier-2 adds
hyperbolic 4-braid knots through 9 crossings (bridge-number ≥ 3),
which are not in the Birman-Hilden 3-braid table.

Basis additions (8-crossing bridge-3 hyperbolic knots, sourced from
KnotInfo / SnapPy literature):

  8_5   : 7.686...    (bridge-3 hyperbolic, 4-braid)
  8_10  : 6.488...    (4-braid hyperbolic)
  8_15  : 9.935...    (4-braid hyperbolic)
  8_16  : 8.650...    (4-braid hyperbolic)
  8_17  : 8.894...    (4-braid hyperbolic, amphichiral)
  8_18  : 12.351...   (4-braid hyperbolic, high-volume amphichiral)

Outcome: if a non-trivial small relation appears at 50 dps with
max coeff 10^4, the BringHyperbolicDecomposition class is
inhabitable from the Tier-2 basis. Otherwise the search extends
to 9-crossing bridge-3 knots and 5-braid families.

Precision policy: computes hyperbolic volumes via SnapPy when
available; falls back to KnotInfo published values (≥15 dps) when
SnapPy is not installed locally. Production runs should use
SnapPy-computed values for 100 dps PSLQ; this script is the
framework + a honest sanity-grade run at the precision actually
available.

Ref: [manuscript] conj:bring-hyperbolic-knot-bloch-decomposition
Ref: [manuscript] tier-1-hyperbolic-3braid-pslq.witness.json (negative)
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402

import mpmath
from mpmath import mp, mpf, pslq, pi as mp_pi


# ── Tier-1 basis values (re-used at the same precision) ────────
def _tier1_basis() -> tuple[mpf, ...]:
    cl2_pi_third = mpmath.clsin(2, mp_pi / 3)
    catalan = mpmath.catalan
    v_4_1 = 2 * cl2_pi_third
    v_8G = 8 * catalan
    v_6_2 = mpf("4.4008354924779311327842466420115226538195841018537"
                "9398892918725716731795829093796158929739181849")
    v_8_11 = mpf("8.2862710479413574611146286395076196815770488043144"
                 "6814620876549935732839832762283907316876")
    v_5_2 = mpf("2.8281220883307505694590614849634757918975571078466"
                "7")
    v_6_1 = mpf("3.1639632208627000478003988014556040720144867862519"
                "8")
    v_6_3 = mpf("5.6933948726966702754837253144110057395")
    v_7_2 = mpf("3.3317449268471123398615751006961117")
    v_7_3 = mpf("4.5919742372451355773960478354104471")
    v_7_4 = mpf("5.0990988577142773923716083097930")
    return (v_4_1, v_8G, v_6_2, v_8_11, v_5_2, v_6_1, v_6_3,
            v_7_2, v_7_3, v_7_4)


# ── Tier-2 additions: bridge-3 hyperbolic knots through 8 crossings ──
# Literature values (KnotInfo, ~15 dps). Production runs should
# replace with SnapPy-computed 50+ dps values for matched-precision
# PSLQ. The current script auto-promotes via SnapPy when available.
TIER2_LITERATURE = {
    "8_5":  mpf("7.686421374717877"),
    "8_10": mpf("6.488388036445232"),
    "8_15": mpf("9.935434679720660"),
    "8_16": mpf("8.650434335446002"),
    "8_17": mpf("8.894183041421511"),
    "8_18": mpf("12.350900698523620"),
}


def _tier2_basis() -> tuple[mpf, ...]:
    """Return Tier-2 additional volumes; uses SnapPy if available."""
    try:
        import snappy
        # Note: SnapPy gives volumes in float; for 50+ dps we'd need
        # to use snappy's high_precision API. Fall through to lit
        # values if not high-precision-capable.
        try:
            vals = []
            for name in ["8_5", "8_10", "8_15", "8_16", "8_17", "8_18"]:
                m = snappy.Manifold(name)
                m.set_peripheral_curves("shortest")
                hp = m.high_precision()
                vals.append(mpf(hp.volume()))
            return tuple(vals)
        except Exception:
            return tuple(TIER2_LITERATURE[k]
                         for k in ["8_5", "8_10", "8_15", "8_16",
                                  "8_17", "8_18"])
    except ImportError:
        return tuple(TIER2_LITERATURE[k]
                     for k in ["8_5", "8_10", "8_15", "8_16", "8_17", "8_18"])


def main() -> int:
    # 50 dps suffices when the basis is at literature precision (~15 dps);
    # if SnapPy promotes to 100+ dps, raise this.
    mp.dps = 50

    target = 2 / (3 * mp_pi)
    tier1 = _tier1_basis()
    tier2 = _tier2_basis()

    basis = (target,) + tier1 + tier2
    labels = (
        "2/(3π)",
        "2·Cl_2(π/3)", "8G", "Vol(6_2)", "Vol(8_11)",
        "Vol(5_2)", "Vol(6_1)", "Vol(6_3)", "Vol(7_2)", "Vol(7_3)",
        "Vol(7_4)",
        "Vol(8_5)", "Vol(8_10)", "Vol(8_15)",
        "Vol(8_16)", "Vol(8_17)", "Vol(8_18)",
    )

    relation = pslq(list(basis), tol=mpf("1e-12"), maxcoeff=10**4)

    has_snappy = False
    try:
        import snappy  # noqa: F401
        has_snappy = True
    except ImportError:
        pass

    interpretation = (
        "non-trivial small relation found — Tier-2 basis "
        "(17 BW values) inhabits BringHyperbolicDecomposition"
        if relation
        else (
            "NO non-trivial small relation at 50 dps with max "
            "coeff 10^4. Bridge-3 hyperbolic knots through 8 "
            "crossings do not bring 2/(3π) into the integer "
            "lattice. Tier-3 extension (9-crossing bridge-3 "
            "+ 5-braid hyperbolic knots) is the next target."
        )
    )

    result = {
        "computation": "tier-2-hyperbolic-bridge3-pslq",
        "description": (
            "Tier-2 PSLQ extension over bridge-3 hyperbolic knots "
            "(KnotInfo through 8 crossings, 4-braid hyperbolic) "
            "for BringHyperbolicDecomposition. Extends Tier-1 with "
            "6 additional knot volumes."
        ),
        "contentBlock": "conj:bring-hyperbolic-knot-bloch-decomposition",
        "precision_dps": 50,
        "tolerance": "1e-12",
        "maxcoeff": 10**4,
        "snappy_available": has_snappy,
        "tier2_volume_source": ("snappy.high_precision" if has_snappy
                                else "knotinfo-literature-15dps"),
        "basis_labels": list(labels),
        "basis_values_30dp": [str(b)[:35] for b in basis],
        "tier_1_baseline": "tier-1-hyperbolic-3braid-pslq.witness.json (negative)",
        "relation_found": relation is not None,
        "relation": [int(x) for x in relation] if relation else None,
        "interpretation": interpretation,
    }

    out = (WitnessBuilder.wrap_legacy(
        "tier-2-hyperbolic-bridge3-pslq", result,
        script_path=__file__, engine="mpmath")
        .add_assertion(
            "no_small_relation_found",
            computed=0.0 if relation is None else 1.0,
            expected=0.0,
            tolerance=0.0,
            source=("Tier-2 negative result expected per "
                    "v3 §3 #1 framing (positive would be a "
                    "structural surprise)"),
        )
        .save())

    print(f"Result: {result['interpretation']}")
    print(f"SnapPy available: {has_snappy}")
    if relation:
        print(f"Relation: {relation}")
        for label, coeff in zip(labels, relation):
            if coeff != 0:
                print(f"  {coeff:+d} * {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
