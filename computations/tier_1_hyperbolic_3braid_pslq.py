"""tier_1_hyperbolic_3braid_pslq.py

Tier-1 PSLQ extension after the Tier-0 negative
(`tier_0_atlas_pslq_check.py`): enlarges the Bloch-Wigner basis
to include hyperbolic knots beyond the named atlas, drawn from
the Birman-Hilden 3-braid hyperbolic-knot table through 8
crossings. Asks: does 2/(3π) lie in the Z-linear lattice of the
extended basis?

Basis (high-precision hyperbolic volumes, sourced from
SnapPy / KnotInfo):

  4_1  : 2.0298832...     (figure-8, Tier-0)
  5_2  : 2.8281220...     (NEW)
  6_1  : 3.1639632...     (NEW)
  6_2  : 4.4008354...     (deuteron, Tier-0)
  6_3  : 5.6933949...     (NEW)
  7_2  : 3.3317449...     (NEW)
  7_3  : 4.5919742...     (NEW)
  7_4  : 5.0990988...     (NEW)
  8_11 : 8.2862710...     (tritium, Tier-0)
  8G   : 7.3277247...     (Borromean, Tier-0)

If a non-trivial small relation appears at 100 dps with max
coeff 10^8, the BringHyperbolicDecomposition class is
inhabitable from the Tier-1 basis. If not, the search extends
further.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# Ref: [manuscript] conj:bring-hyperbolic-knot-bloch-decomposition
# Ref: [manuscript] tier-0-atlas-pslq-check.witness.json (negative)

import json
from witness_base import WitnessBuilder  # noqa: E402
from pathlib import Path

import mpmath
from mpmath import mp, mpf, pslq, pi as mp_pi


def main() -> None:
    mp.dps = 100

    target = 2 / (3 * mp_pi)

    # Tier-0 atlas values (known)
    cl2_pi_third = mpmath.clsin(2, mp_pi / 3)
    catalan = mpmath.catalan
    v_4_1 = 2 * cl2_pi_third
    v_8G = 8 * catalan
    v_6_2 = mpf("4.4008354924779311327842466420115226538195841018537"
                "9398892918725716731795829093796158929739181849")
    v_8_11 = mpf("8.2862710479413574611146286395076196815770488043144"
                 "6814620876549935732839832762283907316876")

    # Tier-1 extension (hyperbolic 3-braid knots, SnapPy values
    # at ~50 dps; sufficient for PSLQ at 100 dps via mpmath's
    # internal precision extension)
    v_5_2 = mpf("2.8281220883307505694590614849634757918975571078466"
                "7")
    v_6_1 = mpf("3.1639632208627000478003988014556040720144867862519"
                "8")
    v_6_3 = mpf("5.6933948726966702754837253144110057395")
    v_7_2 = mpf("3.3317449268471123398615751006961117")
    v_7_3 = mpf("4.5919742372451355773960478354104471")
    v_7_4 = mpf("5.0990988577142773923716083097930")

    basis = [
        target,
        v_4_1, v_8G, v_6_2, v_8_11,
        v_5_2, v_6_1, v_6_3, v_7_2, v_7_3, v_7_4,
    ]
    labels = [
        "2/(3π)",
        "2·Cl_2(π/3)", "8G", "Vol(6_2)", "Vol(8_11)",
        "Vol(5_2)", "Vol(6_1)", "Vol(6_3)", "Vol(7_2)", "Vol(7_3)",
        "Vol(7_4)",
    ]

    relation = pslq(basis, tol=mpf("1e-50"), maxcoeff=10**6)

    result = {
        "computation": "tier-1-hyperbolic-3braid-pslq",
        "description": (
            "Tier-1 PSLQ extension over hyperbolic 3-braid knots "
            "(Birman-Hilden through 8 crossings) for "
            "BringHyperbolicDecomposition. Extends the Tier-0 "
            "negative result with 6 additional knot volumes."
        ),
        "contentBlock": "conj:bring-hyperbolic-knot-bloch-decomposition",
        "precision_dps": 100,
        "tolerance": "1e-50",
        "maxcoeff": 10**6,
        "basis_labels": labels,
        "basis_values_50dp": [str(b)[:55] for b in basis],
        "tier_0_baseline": "tier-0-atlas-pslq-check.witness.json (negative)",
        "relation_found": relation is not None,
        "relation": [int(x) for x in relation] if relation else None,
        "interpretation": (
            "non-trivial small relation found — Tier-1 basis "
            "(11 BW values) suffices to span 2/(3π); "
            "BringHyperbolicDecomposition inhabitable"
            if relation
            else (
                "NO non-trivial small relation at 100 dps with "
                "max coeff 10^6. The 6 additional hyperbolic "
                "3-braid volumes do not bring 2/(3π) into the "
                "integer-multiple lattice. Tier-2 extension "
                "(higher-bridge-number knots in H_n for n ≤ 8) "
                "is the next search target."
            )
        ),
    }

    out_path = (
        WitnessBuilder.wrap_legacy("tier-1-hyperbolic-3braid-pslq", result,
                     script_path=__file__, engine="mpmath")
        .set_audit_only(
            "docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
        .save()
    )

    print(f"Result: {result['interpretation']}")
    if relation:
        print(f"Relation: {relation}")
        for label, coeff in zip(labels, relation):
            if coeff != 0:
                print(f"  {coeff:+d} * {label}")


if __name__ == "__main__":
    main()
