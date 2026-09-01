#!/usr/bin/env python3
"""tier_2_hyperbolic_bridge3_pslq.py

Tier-2 PSLQ extension after the Tier-1 negative
(`tier_1_hyperbolic_3braid_pslq.py`): enlarges the Bloch-Wigner basis
to include bridge-number ≥ 3 hyperbolic knots in H_n for n ∈ {4..8}.

Per `2026-05-09-refocused-1ppb-workplan-v3.md` §3 item #1, this is
the next search target after Tier-1 returned no small Z-linear
relation for 2/(3π) over the 11-element 3-braid basis. Tier-2 adds
hyperbolic 4-braid knots **through 8 crossings** (bridge-number ≥ 3),
which are not in the Birman-Hilden 3-braid table. The 9-crossing
extension is reserved for Tier-3 (per the v3 doc).

Basis additions (8-crossing bridge-3 hyperbolic knots). Values
CORRECTED 2026-08-30 (bean qou-ckbv) — the previous table was
labelled "KnotInfo, ~15 dps" and four of its six entries had zero
to three correct significant digits:

  8_5   : 6.997...    (bridge-3 hyperbolic, 4-braid)     was 7.686...
  8_10  : 8.651...    (4-braid hyperbolic)               was 6.488...
  8_15  : 9.931...    (4-braid hyperbolic)               was 9.935...
  8_16  : 10.579...   (4-braid hyperbolic)               was 8.650...
  8_17  : 10.986...   (4-braid hyperbolic, amphichiral)  was 8.894...
  8_18  : 12.351...   (4-braid hyperbolic, high-volume amphichiral)

Outcome: if a non-trivial small relation appears at 50 dps with
max coeff 10^4, the BringHyperbolicDecomposition class is
inhabitable from the Tier-2 basis. Otherwise the search extends
to 9-crossing bridge-3 knots and 5-braid families.

Precision policy: computes hyperbolic volumes via SnapPy when
available; otherwise falls back to the `TIER2_LITERATURE` table,
which since 2026-08-30 holds SnapPy-3.3.2-verified values at 50 dps
rather than the wrong "≥15 dps literature" figures it held before.
Both paths now agree to 50 dps, so the result no longer depends on
whether SnapPy happens to be installed — which it previously did,
at the first significant digit.

Ref: [manuscript] conj:bring-hyperbolic-knot-bloch-decomposition
Ref: [manuscript] tier-1-hyperbolic-3braid-pslq.witness.json (negative)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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
    # CORRECTED 2026-08-30 (bean qou-ckbv) — this file carried the same
    # eight bad literals as tier_1_hyperbolic_3braid_pslq.py, the corrupted
    # basis having been copied between them. All eight were wrong inside
    # the digits they printed (good to 2-13 while printing 32-96), and six
    # of the eight matched no manifold in SnapPy's censuses at all. See the
    # long note at the constants in tier_1 for the per-knot table and for
    # why a PSLQ negative computed from them establishes nothing.
    #
    # Provenance: snappy 3.3.2 `Manifold(k).volume(bits_prec=2000)`, each
    # confirmed against a randomized re-triangulation of the same manifold.
    v_6_2 = mpf("4.40083251612304610144120386564092803398348541851646"
                "5458521752513316600130972405316677122430240181317")
    v_8_11 = mpf("8.28631681780659258812682479775116716294874424541111"
                 "7139762993515683703595296757393453019207255602108")
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
    return (v_4_1, v_8G, v_6_2, v_8_11, v_5_2, v_6_1, v_6_3,
            v_7_2, v_7_3, v_7_4)


# ── Tier-2 additions: bridge-3 hyperbolic knots through 8 crossings ──
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
mp.dps = 50

# CORRECTED 2026-08-30 (bean qou-ckbv). This table was labelled
# "Literature values (KnotInfo, ~15 dps)". It was not 15 dps and it was
# not KnotInfo: measured against SnapPy 3.3.2, four of the six had ZERO
# to THREE correct significant digits.
#
#     knot   old literal            true value             good digits
#     8_5    7.686421374717877      6.997189147792215           1
#     8_10   6.488388036445232      8.651148558017082           0
#     8_15   9.935434679720660      9.930648293796183           3
#     8_16   8.650434335446002     10.579021916899270           0
#     8_17   8.894183041421511     10.985907606284820           0
#     8_18  12.350900698523620     12.350906209158200           6
#
# Not a misaligned table: none of the six old values is the volume of ANY
# knot through 9 crossings, so they were not correct numbers under wrong
# labels. They were simply wrong.
#
# This is the FALLBACK path, taken exactly when SnapPy is unavailable —
# i.e. in the pipeline image this table exists to serve. A fallback wrong
# at the first digit does not degrade gracefully; it silently substitutes
# noise for a volume, which is the failure mode `_tier2_basis`'s
# source-tag was added to make visible.
#
# Provenance: snappy 3.3.2 `Manifold(k).volume(bits_prec=2000)` at 50 dps,
# each confirmed against a randomized re-triangulation of the same
# manifold.
TIER2_LITERATURE = {
    "8_5":  mpf("6.9971891477922154788005778791455176889638409556479"),
    "8_10": mpf("8.6511485580170819661711202663143702421843667756045"),
    "8_15": mpf("9.9306482937961829810021321555831152804819325499403"),
    "8_16": mpf("10.579021916899270325808684550088672898504885279597"),
    "8_17": mpf("10.985907606284820303688439759183069403959794127785"),
    "8_18": mpf("12.350906209158200174736304438426152014199256704120"),
}


def _tier2_basis() -> tuple[tuple[mpf, ...], str]:
    """Return (Tier-2 volumes, source-tag).

    Per Copilot review on #585: track whether SnapPy HP volumes were
    actually used (import success ≠ HP success). Returns the source
    tag alongside the values so the witness records reality.
    """
    keys = ["8_5", "8_10", "8_15", "8_16", "8_17", "8_18"]
    try:
        import snappy
        try:
            vals = []
            for name in keys:
                m = snappy.Manifold(name)
                m.set_peripheral_curves("shortest")
                hp = m.high_precision(bits=200)
                vals.append(mpf(str(hp.volume())))
            return tuple(vals), "snappy.high_precision(bits=200)"
        except Exception:
            return (tuple(TIER2_LITERATURE[k] for k in keys),
                    "snappy-3.3.2-verified-50dps table (snappy HP failed)")
    except ImportError:
        return (tuple(TIER2_LITERATURE[k] for k in keys),
                "snappy-3.3.2-verified-50dps table (snappy unavailable)")


def main() -> int:
    # 50 dps suffices when the basis is at literature precision (~15 dps);
    # if SnapPy promotes to 100+ dps, raise this.
    mp.dps = 50

    target = 2 / (3 * mp_pi)
    tier1 = _tier1_basis()
    tier2, tier2_source = _tier2_basis()

    basis = (target,) + tier1 + tier2
    labels = (
        "2/(3π)",
        "2·Cl_2(π/3)", "8G", "Vol(6_2)", "Vol(8_11)",
        "Vol(5_2)", "Vol(6_1)", "Vol(6_3)", "Vol(7_2)", "Vol(7_3)",
        "Vol(7_4)",
        "Vol(8_5)", "Vol(8_10)", "Vol(8_15)",
        "Vol(8_16)", "Vol(8_17)", "Vol(8_18)",
    )

    # Per Gemini review on #585: tie tol to mp.eps so the search
    # actually runs at the configured 50 dps. Hardcoded `1e-12`
    # truncated PSLQ to f64-grade precision.
    pslq_tol = mp.eps * mpf("1e3")
    relation = pslq(list(basis), tol=pslq_tol, maxcoeff=10**4)

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
        "tolerance": str(pslq_tol),
        "maxcoeff": 10**4,
        "snappy_available": has_snappy,
        "tier2_volume_source": tier2_source,
        "basis_labels": list(labels),
        # Per Copilot review on #585: use mpmath.nstr for stable
        # 30-decimal formatting (str(b)[:35] truncated mid-digit).
        "basis_values_30dp": [mpmath.nstr(b, 30, strip_zeros=False)
                              for b in basis],
        "tier_1_baseline": "tier-1-hyperbolic-3braid-pslq.witness.json (negative)",
        "relation_found": relation is not None,
        "relation": [int(x) for x in relation] if relation else None,
        "interpretation": interpretation,
    }

    out = (WitnessBuilder.wrap_legacy(
        "tier-2-hyperbolic-bridge3-pslq", result,
        script_path=__file__, engine="mpmath")
        # Per Copilot review on #585: mark as audit-only so
        # audit-wiring.ts doesn't bucket it as orphan.
        .set_audit_only("docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
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
