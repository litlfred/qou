"""Topic 2 probe: M_first_Φ_8 boundary scan across mirror pairs.

PR #1625 established that for ATOMIC-STEP pair-differences
(D−n, ³He−n, ³He−D, ⁴He−n, ⁴He−D, ⁴He−³He) where Φ_8 appears,

  M_first_Φ_8 = 7  UNIVERSALLY

(the M at which the partial sum Σ_{m=0..M} Δa_m·(u;u)_m first
becomes divisible by Φ_8 = u⁴+1).

Per the PR #1625 audit: this is the level-2 SU(2) Wenzl projector
kernel at q = ζ_8, which kills partitions with first column ≥ 4
via [4]_q = 0. The boundary M=7 = ord(σ_i in H_n(ζ_8)) − 1.

This probe extends the test to MIRROR PAIRS (Z, N) ↔ (N, Z):
  Does the universal M=7 boundary hold for mirror pairs too?

If YES → strong evidence the Wenzl annihilator mechanism is
        UNIVERSAL across pair-difference types (atomic-step
        AND mirror).

If NO  → mirror pairs have a different boundary structure,
        and the Φ_8 multiplicity drops at A=6, A=14 are
        explained by a DIFFERENT mechanism than the atomic-step
        Φ_8 universality.

Also computes M_first_Φ_8² (the boundary at which Φ_8² divides)
for mirror pairs with multiplicity ≥ 2.

Connects to:
  prop:categorical-neutrality-saturated-shells
  conj:diagrammatic-double-magic-lr-fusion
  PR #1625 (level-2 SU(2) Wenzl categorical witness)
  PR #1642 (mass-table Habiro)
  PR #1649 (this branch — A=6, A=14 anomalies)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from habiro_coefficients_atomic import load_a_m as _load_a_m  # noqa: E402
from habiro_coefficients_atomic import mirror_trace_diff_numerator as _mirror_trace_diff  # noqa: E402
from habiro_coefficients_atomic import cyclotomic_expansion as _cyc_expand  # noqa: E402 — shared loader; refuses a self-failed witness (qou-s41x)


# The last column is mult(Φ_8), MEASURED under convention D with the corrected
# trace-differencing (bean qou-0ndb). It was a convention-C table; two entries
# moved when the differencing was fixed:
#     ⁶He − ⁶Be   2 -> 0
#     ¹⁴O − ¹⁴C   4 -> 12   (now MATCHES 2⌊(A−1)/2⌋; it refuted under C)
MIRROR_PAIRS = [
    ("n − p",       1, "neutron",      "proton",       0),
    ("³He − ³H",    3, "helium-3",     "tritium",      2),
    ("⁵Li − ⁵He",  5, "lithium-5",    "helium-5",     4),
    ("⁶He − ⁶Be",  6, "helium-6",     "beryllium-6",  0),
    ("⁷Be − ⁷Li",  7, "beryllium-7",  "lithium-7",    6),
    ("⁸B − ⁸Li",   8, "boron-8",      "lithium-8",    6),
    ("⁹B − ⁹Be",   9, "boron-9",      "beryllium-9",  8),
    ("¹⁰C − ¹⁰Be", 10, "carbon-10",    "beryllium-10", 8),
    ("¹²N − ¹²B",  12, "nitrogen-12",  "boron-12",    10),
    ("¹⁴O − ¹⁴C",  14, "oxygen-14",    "carbon-14",   12),
]


def main() -> int:
    t0 = time.perf_counter()
    u = sp.symbols('u')
    cyc_8 = u**4 + 1
    cyc_8_sq = cyc_8 ** 2

    def load_a_m(slug):
        # Delegates to the shared loader, which REFUSES a witness flagging its
        # own reconstruction_matches false (bean qou-s41x). This was one of
        # three byte-identical copies, none of which consulted that flag.
        return _load_a_m(slug, u, witness_dir=HERE)

    def q_poch(m):
        if m == 0:
            return sp.Integer(1)
        return sp.prod(1 - u**k for k in range(1, m + 1))

    def divides(p, c):
        return sp.div(p, c, u)[1] == 0

    print("=" * 78)
    print(" M_first_Φ_8 BOUNDARY SCAN — MIRROR PAIRS")
    print("=" * 78)
    print(f"{'Pair':<14} {'A':>3} {'M_max':>5} {'mult(Φ_8)':>10} "
          f"{'M_first_Φ_8':>13} {'M_first_Φ_8²':>14} {'M=7?':>5}")
    print("─" * 80)

    results = []
    for label, A, X_slug, Y_slug, expected_mult in MIRROR_PAIRS:
        try:
            ax = load_a_m(X_slug)
            ay = load_a_m(Y_slug)
            M_max = min(max(ax), max(ay))

            # Habiro-expand the TRUE difference, then partial-sum THAT.
            #
            # Subtracting a_m coefficients builds d_X·t_X − d_Y·t_Y, which is
            # proportional to t_X − t_Y only where the denominators agree.
            # Measured: under convention C they agree at q=1 on every canonical
            # pair — so the published C boundary numbers stand as computed —
            # while under D they differ by a factor of 4 and every multiplicity
            # collapses to 0. Proved sorry-free in
            # QOU/Habiro/MirrorPairNormalisation.lean (coeffDiff_at_coincidence).
            #
            # M_first is defined on the Habiro expansion, so the correct object
            # is the expansion OF the true difference, not a difference of two
            # expansions (bean qou-0ndb).
            _diff = _mirror_trace_diff(X_slug, Y_slug, u, witness_dir=HERE)
            _dcoeffs = {c["m"]: sp.sympify(c["a_m"], locals={"u": u})
                        for c in _cyc_expand(_diff, u, max_m=M_max + 1)}

            S = sp.Integer(0)
            M_first_phi8 = None
            M_first_phi8_sq = None
            for m in range(M_max + 1):
                delta = _dcoeffs.get(m, sp.Integer(0))
                S = S + delta * q_poch(m)
                # Skip identically-zero S (e.g. m < some lower bound)
                if S == 0:
                    continue
                if M_first_phi8 is None and divides(S, cyc_8):
                    M_first_phi8 = m
                if M_first_phi8_sq is None and divides(S, cyc_8_sq):
                    M_first_phi8_sq = m
                # Both found — done
                if M_first_phi8 is not None and (
                    M_first_phi8_sq is not None or expected_mult < 2
                ):
                    # If expected mult is 0 or 1, no Φ_8² boundary
                    break

            matches_universal = (M_first_phi8 == 7) if expected_mult > 0 else None
            print(f"{label:<14} {A:>3} {M_max:>5} {expected_mult:>10} "
                  f"{str(M_first_phi8):>13} {str(M_first_phi8_sq):>14} "
                  f"{'✓' if matches_universal else ('✗' if matches_universal is False else '—'):>5}")
            results.append({
                "pair": label,
                "A": A,
                "M_max_used": M_max,
                "mult_Phi_8_observed": expected_mult,
                "M_first_Phi_8": M_first_phi8,
                "M_first_Phi_8_squared": M_first_phi8_sq,
                "matches_universal_M_eq_7": matches_universal,
            })
        except FileNotFoundError as e:
            print(f"{label:<14} (witness missing — {e})")
            results.append({"pair": label, "error": str(e)})
        except Exception as e:
            print(f"{label:<14} ERR: {type(e).__name__}: {e}")
            results.append({"pair": label, "error": str(e)})

    # ─── Analysis ────────────────────────────────────────────────
    print()
    print("=" * 78)
    print(" UNIVERSAL M_first_Φ_8 = 7 PREDICTION")
    print("=" * 78)
    pairs_with_phi8 = [r for r in results
                       if isinstance(r.get("mult_Phi_8_observed"), int)
                       and r["mult_Phi_8_observed"] > 0]
    universal_match = sum(
        1 for r in pairs_with_phi8 if r["matches_universal_M_eq_7"])
    n_phi8_pairs = len(pairs_with_phi8)
    print(f"  Mirror pairs with mult(Φ_8) > 0:        {n_phi8_pairs}")
    print(f"  Pairs matching PR #1625 universal M=7: {universal_match}/{n_phi8_pairs}")
    print()
    if universal_match == n_phi8_pairs and n_phi8_pairs > 0:
        print("  ✓ UNIVERSAL M_first_Φ_8 = 7 HOLDS for mirror pairs")
        print("    → confirms Wenzl-annihilator mechanism (PR #1625) extends")
        print("    → from atomic-step pairs to mirror pairs uniformly.")
    elif universal_match == 0 and n_phi8_pairs > 0:
        print("  ✗ UNIVERSAL M=7 FAILS for mirror pairs")
        print("    → mirror pair Φ_8 has a different boundary mechanism.")
    else:
        print(f"  Mixed: {n_phi8_pairs - universal_match} pairs don't match M=7")
        print("    → mirror pair Φ_8 boundary is pair-dependent.")

    # ─── Φ_8² boundary structure (PR #1625 noted ⁴He−³He has M=15 for Φ_8²) ─
    pairs_with_phi8_sq = [r for r in results
                           if r.get("M_first_Phi_8_squared") is not None
                           and isinstance(r["M_first_Phi_8_squared"], int)]
    if pairs_with_phi8_sq:
        print()
        print(f"  Pairs with detected M_first_Φ_8² (mult ≥ 2):")
        for r in pairs_with_phi8_sq:
            print(f"    {r['pair']} (A={r['A']}, mult={r['mult_Phi_8_observed']}): "
                  f"M_first_Φ_8² = {r['M_first_Phi_8_squared']}")

    elapsed = time.perf_counter() - t0

    payload = {
        "computation": "topic2-mirror-pair-phi8-boundary-scan",
        "description": (
            "Topic 2 probe: extend PR #1625's universal M_first_Φ_8 = 7 "
            "finding (atomic-step pair-differences) to mirror pairs "
            "(Z, N) ↔ (N, Z). Tests whether the Wenzl-annihilator "
            "mechanism is universal across pair-difference types."
        ),
        "reference_blocks": [
            "docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md",
            "docs/audits/2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md",
            "docs/audits/2026-06-01-qbeta-habiro-a6-refutes-refined-scaling-law.md",
            "prop:categorical-neutrality-saturated-shells",
            "PR #1625 (level-2 SU(2) Wenzl)",
            "PR #1642 (mass-table Habiro)",
            "PR #1649 (this branch)",
        ],
        # Wrap rows under a dict-typed `data` slot. A bare top-level list
        # for `data` breaks witness_dependency_drift.py, which does
        # `w.get("data", {}).get("upstream_witness_hashes")` (I6 schema
        # drift). See docs/audits/2026-05-16-stale-witness-infra-gap.md.
        "data": {"rows": results},
        "verdict": {
            "n_pairs_tested": len(results),
            "n_pairs_with_phi8": n_phi8_pairs,
            "n_pairs_matching_universal_M_eq_7":
                universal_match if n_phi8_pairs > 0 else None,
            "universal_M_eq_7_holds_for_mirror_pairs":
                universal_match == n_phi8_pairs and n_phi8_pairs > 0,
            "n_phi8_squared_boundaries_detected": len(pairs_with_phi8_sq),
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        name="topic2-mirror-pair-phi8-boundary-scan",
        payload=payload,
        script_path=__file__,
        engine="sympy Poly + cyclotomic divisibility",
        output_dir=HERE,
    )
    wb.save()
    print()
    print(f"  Elapsed: {elapsed:.1f} s")
    print(f"  Witness: topic2-mirror-pair-phi8-boundary-scan.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
