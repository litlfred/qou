"""tier_1_hyperbolic_3braid_pslq.py

Tier-1 PSLQ extension after the Tier-0 negative
(`tier_0_atlas_pslq_check.py`): enlarges the Bloch-Wigner basis
to include hyperbolic knots beyond the named atlas, drawn from
the Birman-Hilden 3-braid hyperbolic-knot table through 8
crossings. Asks: does 2/(3π) lie in the Z-linear lattice of the
extended basis?

Basis (hyperbolic volumes at 100 dps; SnapPy 3.3.2 at
bits_prec=2000, each cross-checked against a randomized
re-triangulation. Corrected 2026-08-30 — see the note at the
constants: all eight literals were previously wrong inside the
digits they printed, one of them at the second digit):

  4_1  : 2.0298832...     (figure-8, Tier-0; closed form 2*Cl_2(pi/3))
  5_2  : 2.8281220...     (NEW)
  6_1  : 3.1639632...     (NEW)
  6_2  : 4.4008325...     (deuteron, Tier-0)
  6_3  : 5.6930210...     (NEW)
  7_2  : 3.3317442...     (NEW)
  7_3  : 4.5921256...     (NEW)
  7_4  : 5.1379412...     (NEW)
  8_11 : 8.2863168...     (tritium, Tier-0)
  8G   : 7.3277247...     (Borromean, Tier-0; closed form 8*Catalan)

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
    # ── Hyperbolic volumes at 100 dps, matching mp.dps above ──
    #
    # CORRECTED 2026-08-30 (bean qou-ckbv). Every one of the eight literals
    # below was previously WRONG INSIDE THE DIGITS IT PRINTED, while a
    # comment claimed "SnapPy values at ~50 dps":
    #
    #     knot   printed   actually good
    #     6_2       96          6
    #     8_11      90          5
    #     5_2       51         13
    #     6_1       51          8
    #     6_3       38          4
    #     7_2       35          6
    #     7_3       35          4
    #     7_4       32          2      <- wrong at the SECOND digit
    #
    # Six of the eight matched NO manifold in SnapPy's censuses at all
    # (searched 200,067 entries), so these were corrupted numbers rather
    # than correct volumes under the wrong labels.
    #
    # Why this mattered more here than in a display constant: PSLQ searches
    # for an integer relation among the basis. Fed values that are noise
    # past digit 2-13 but supplied at 100 dps, it reports a relation among
    # WRONG NUMBERS. This script's result is a NEGATIVE ("no relation
    # found"), and a negative is exactly what a corrupted basis produces
    # whether or not the real basis has a relation — the finding could not
    # have failed for the reason it claims. Re-run after this correction
    # before citing the Tier-1 negative anywhere.
    #
    # Provenance: snappy 3.3.2, `Manifold(k).volume(bits_prec=2000)`. Each
    # value independently confirmed against a RANDOMIZED re-triangulation
    # of the same manifold (volume is a topological invariant, so a
    # different triangulation is a genuine second route, not a re-read).
    # Method controlled on the two volumes with closed forms: SnapPy agrees
    # with 2*Cl_2(pi/3) to 4.5e-64 and with 8*G to 2.6e-65.
    v_6_2 = mpf("4.40083251612304610144120386564092803398348541851646"
                "5458521752513316600130972405316677122430240181317")
    v_8_11 = mpf("8.28631681780659258812682479775116716294874424541111"
                 "7139762993515683703595296757393453019207255602108")

    # Tier-1 extension (hyperbolic 3-braid knots)
    v_5_2 = mpf("2.82812208833078316276389880927663494277098131730064"
                "9477043520327258802548322471630936947017929999107")
    v_6_1 = mpf("3.16396322888314398399101471597315448481278767151811"
                "5266582922441975565984963084839871725288561503347")
    v_6_3 = mpf("5.69302109128130076511248327748122292694430173300688"
                "0037850870699995476072590906707654919542407040036")
    v_7_2 = mpf("3.33174423164111482391456910802971279554695790918600"
                "4921221604455598741372842366515578862260348786284")
    v_7_3 = mpf("4.59212569702706255019661399465547373235436032654327"
                "0894426065765041363091864797025835868422067745209")
    v_7_4 = mpf("5.13794120187341776984134833947484503564967509273571"
                "2368597748060678580307623518886258443309869104970")

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
