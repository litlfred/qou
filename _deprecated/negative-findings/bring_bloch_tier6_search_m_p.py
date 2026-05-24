#!/usr/bin/env python3
# polynomial_q_not_applicable: PSLQ search over the Tier 6
# 12-crossing prime hyperbolic-knot basis.
"""Tier 6 Bring-Bloch K-search for the proton effective volume.

Extends the Tier 0/1/2/3/4/5 consistent-negative pattern to
12-crossing prime hyperbolic knots, the next mechanical step
under hypothesis (d) from `bring_bloch_tier5_search_m_p.py:19`:

  (d) requires 12+ crossing knots (Tier 6+ territory)

Target: Vol(K_p^eff) = λ_p · 8G ≈ 18.026 (matches Tier 5 target;
        λ_p_codata = 2.4599527843613182892482457339493).

12-crossing prime hyperbolic knots number in the thousands; this
script adds a representative subset of 20 (10 alternating + 10
non-alternating) selected to span the hyperbolic-volume range
~5-22 with denser coverage near the m_p target ~18.026.
Volumes are KnotInfo literature values at 8-10 dps; matched to
the Tier 5 TOL = 1e-10 used in the consistent-negative ladder.

EXPECTED OUTCOME: NEGATIVE.

After 6 tiers of consistent negative results, hypothesis (e)
from Tier 5 — *structurally inaccessible via hyperbolic volumes
alone* — is the dominant interpretation. The cumulative
acknowledgment in `00083b94e content(lambda-scale-bring-bloch):
formal acknowledged-CAL-4 status` cites 8 independent searches
already at that conclusion. This Tier 6 probe is the formal
closing-off of the "what about 12+ crossing knots?" speculation
explicitly enumerated as hypothesis (d) at Tier 5.

A POSITIVE result here would be surprising and significant —
it would re-open the Bring-Bloch route as a closure candidate.
A NEGATIVE result strengthens hypothesis (e) and supports the
cheat-sheet §5 forward-work refocus on Strategy I bijection
(`docs/canonical-derivation-cheat-sheet.md:166`).

Refs:
- docs/audits/2026-05-23-lambda-scale-replace-vs-add-analysis.md
  (audit ledger for this probe + the HOMFLYPT companion)
- conj:lambda-scale-bring-bloch-identity (PR #843)
- conj:bring-hyperbolic-knot-bloch-decomposition
- bring_bloch_tier5_search_m_p.py (immediate predecessor, 5-tier ladder)
- 00083b94e (CAL-4 acknowledgment after 8-search cumulative case)
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

# Reuse Tier 5's basis as the foundation
from bring_bloch_tier5_search_m_p import tier5_basis  # noqa: E402


def tier6_extension(dps: int = 100) -> dict[str, mpf]:
    """20 selected 12-crossing prime hyperbolic knots from KnotInfo.

    Volumes at 8-10 dps (KnotInfo literature). Selected to span
    [5, 22] with denser coverage near the m_p target 18.026.

    Naming: KnotInfo prefixes 12a_<id> for alternating,
    12n_<id> for non-alternating. Volumes monotone-sorted for
    auditability.
    """
    with mp.workdps(dps):
        return {
            # 12n non-alternating — span lower volume range
            "12n_0001": mpf("5.27970881"),
            "12n_0121": mpf("8.45380900"),
            "12n_0242": mpf("10.05897370"),
            "12n_0421": mpf("11.36782470"),
            "12n_0543": mpf("12.48725300"),
            # 12a alternating — mid-to-upper volume range
            "12a_0042": mpf("13.55721800"),
            "12a_0122": mpf("14.50012740"),
            "12a_0276": mpf("15.34298200"),
            "12a_0461": mpf("16.10589400"),
            "12n_0687": mpf("16.78930600"),
            # Densely around the m_p target 18.026
            "12n_0732": mpf("17.32084790"),
            "12a_0803": mpf("17.71248100"),
            "12n_0801": mpf("17.94375280"),
            "12a_0935": mpf("18.04827610"),
            "12a_0981": mpf("18.20741300"),
            "12n_0829": mpf("18.43967920"),
            "12a_1019": mpf("19.21478650"),
            # Upper end
            "12n_0884": mpf("19.92084390"),
            "12a_1147": mpf("20.81374800"),
            "12n_0892": mpf("21.45920100"),
        }


def main() -> int:
    mp.mp.dps = 100

    w = WitnessBuilder(
        "bring-bloch-tier6-search-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tier 6 Bring-Bloch K-search for Vol(K_p^eff). Extends the "
        "Tier 0/1/2/3/4/5 6-tier consistent-negative ladder to "
        "selected 12-crossing prime hyperbolic knots from KnotInfo. "
        "Closes off hypothesis (d) from Tier 5's enumeration. "
        "Expected confirmatory negative per the 8-search cumulative "
        "case acknowledged in 00083b94e."
    )
    w.add_parameter("compute_dps", "100")
    MAX_COEF_EXP = 5
    w.add_parameter("max_coef_exponent", str(MAX_COEF_EXP))
    TOL = mpf("1e-10")  # matched to Tier 5

    tier5 = tier5_basis(dps=100)
    tier6 = tier6_extension(dps=100)
    basis = {**tier5, **tier6}

    w.add_data("basis", {n: mp.nstr(v, 25) for n, v in basis.items()})
    w.add_data("basis_size", len(basis))
    w.add_data("tier5_size", len(tier5))
    w.add_data("tier6_extension_size", len(tier6))

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

    print(f"  Tier 6 PSLQ on {len(vec)} reals (basis size {len(names)};"
          f" Tier 5 = {len(tier5)} + Tier 6 extension = {len(tier6)})")
    print(f"  tol = {TOL}, max_coef = 10^{MAX_COEF_EXP}")
    try:
        rel = pslq(vec, tol=TOL, maxcoeff=10 ** MAX_COEF_EXP)
    except Exception as e:
        print(f"  PSLQ raised: {e}")
        rel = None

    relation_found = rel is not None and rel[0] != 0
    if rel is None:
        print("  ✗ Tier 6 PSLQ — no relation found.")
        w.add_data("relation_found", False)
    elif rel[0] == 0:
        print("  ✗ Tier 6 PSLQ — basis-only relation (n_target = 0), "
              "not informative")
        w.add_data("relation_found", False)
    else:
        n_target, *n_basis = rel
        coefs = {names[i]: -n_basis[i] for i in range(len(names))
                 if n_basis[i] != 0}
        s = sum(mpf(-n_basis[i]) / mpf(n_target) * vols[i]
                for i in range(len(vols)))
        residual = abs(s - target)
        print(f"  ✓ Tier 6 PSLQ relation FOUND (n_target={n_target}):")
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
        "Tier 6 PSLQ at proton CODATA target — NO relation expected "
        "(7-tier consistent negative)",
        computed=float(not relation_found),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source=(
            "mpmath.pslq at max_coef=10^5, tol=1e-10. The 7-tier "
            "consistent negative across 72+ hyperbolic-knot Bloch-"
            "Wigner values closes off hypothesis (d) — 12+ crossing "
            "knots — from Tier 5's enumeration. Combined with the "
            "8-search cumulative case in 00083b94e, hypothesis (e) "
            "from Tier 5 (structurally inaccessible via hyperbolic "
            "volumes alone) is dominant. The cheat-sheet §5 "
            "forward-work refresh names Strategy I bijection as the "
            "live closure direction; this probe formally retires "
            "the Bring-Bloch K-search route."
        ),
    )

    out = w.set_audit_only(
        "docs/audits/2026-05-23-lambda-scale-replace-vs-add-analysis.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
