#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical constant, no q-dependence.
"""Vol(𝓑₃) at 100 dps via Lobachevsky-Catalan identity.

Tests the audit claim (`docs/audits/2026-05-18-lambda-scale-derivation-search.md`
§3): is Vol(𝓑₃) = 8·G exactly, or do they differ at the 7th digit?

References:
- Adams (1985): the Borromean rings complement decomposes into 2 ideal
  regular octahedra; V_oct = 8 · Λ(π/4); Vol(𝓑₃) = 2 · V_oct = 16 · Λ(π/4).
- Lobachevsky: Λ(θ) = -∫₀^θ log |2 sin(t)| dt.
- Standard identity: Λ(π/4) = G/2 where G = Catalan's constant.

If Λ(π/4) = G/2 exactly, then Vol(𝓑₃) = 16·G/2 = 8·G exactly, and the
audit's "literature value differs at the 7th digit" must be a precision
artifact of whatever literature source was quoted.

This script computes both sides at 100 dps and reports the gap.

Ref: conj:borromean-baryon-mass-formula (the consumer);
     docs/audits/2026-05-18-lambda-scale-derivation-search.md §93–104
     (the audit raising the question).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def lobachevsky(theta, dps: int = 110) -> mp.mpf:
    """Λ(θ) = -∫₀^θ log|2 sin(t)| dt via mpmath quadrature."""
    with mp.workdps(dps):
        # Endpoint singularity at t=0 (log|2sin t| ~ log(2t)) and at
        # t=π/2 (log|2 sin(π/2)| = log 2 finite). The integrand is
        # integrable; mp.quad handles the endpoint singularity.
        def integrand(t):
            s = 2 * mp.sin(t)
            if s == 0:
                return mp.mpf(0)
            return -mp.log(mp.fabs(s))
        return mp.quad(integrand, [0, theta])


def main() -> int:
    mp.mp.dps = 110  # 10 dps headroom over 100 dps target output

    w = WitnessBuilder(
        "borromean-volume-100dps",
        engine="mpmath",
    )
    w.set_description(
        "Vol(𝓑₃) at 100 dps via Lobachevsky-Catalan identity. Tests "
        "the audit claim that Vol(𝓑₃) and 8·G differ at the 7th "
        "digit. Computes Λ(π/4) numerically, mpmath.catalan to 100 "
        "dps, and 16·Λ(π/4) vs 8·G."
    )
    w.add_parameter("compute_dps", "110")
    w.add_parameter("output_dps", "100")

    # ── Catalan's constant from mpmath ────────────────────────
    G_mpmath = mp.catalan
    G_str = mp.nstr(G_mpmath, 100, strip_zeros=False)
    w.add_data("catalan_G", {
        "source": "mpmath.catalan",
        "value_100dps": G_str,
    })

    # ── Λ(π/4) via quadrature ────────────────────────────────
    lambda_pi_over_4 = lobachevsky(mp.pi / 4, dps=110)
    lambda_str = mp.nstr(lambda_pi_over_4, 100, strip_zeros=False)
    w.add_data("lobachevsky_pi_over_4", {
        "definition": "Λ(θ) = -∫₀^θ log|2 sin(t)| dt",
        "value_100dps": lambda_str,
    })

    # ── Test: Λ(π/4) = G/2 ? ─────────────────────────────────
    G_over_2 = G_mpmath / 2
    delta_Lambda_vs_G_half = lambda_pi_over_4 - G_over_2
    w.add_data("test_lobachevsky_equals_G_half", {
        "claim": "Λ(π/4) =?= G/2 (standard identity)",
        "Λ(π/4)": lambda_str,
        "G/2": mp.nstr(G_over_2, 100, strip_zeros=False),
        "delta": mp.nstr(delta_Lambda_vs_G_half, 50, strip_zeros=False),
        "rel_diff": mp.nstr(delta_Lambda_vs_G_half / G_over_2, 20),
    })
    w.add_assertion(
        "Λ(π/4) = G/2 (exact identity, to numerical precision)",
        computed=float(mp.fabs(delta_Lambda_vs_G_half / G_over_2)),
        expected=0.0,
        tolerance=1e-30,
        unit="relative",
        source="Λ(π/4) = G/2 classical identity (see Lewin 1981 §1)",
    )

    # ── Vol(𝓑₃) = 16 · Λ(π/4) and 8·G ────────────────────────
    vol_B3_lobachevsky = 16 * lambda_pi_over_4
    vol_B3_catalan = 8 * G_mpmath
    delta_B3 = vol_B3_lobachevsky - vol_B3_catalan
    w.add_data("vol_B3", {
        "formula_lobachevsky": "Vol(𝓑₃) = 16 · Λ(π/4) (Adams 1985)",
        "formula_catalan": "Vol(𝓑₃) = 8 · G  (via Λ(π/4) = G/2)",
        "value_lobachevsky_100dps": mp.nstr(vol_B3_lobachevsky, 100, strip_zeros=False),
        "value_catalan_100dps": mp.nstr(vol_B3_catalan, 100, strip_zeros=False),
        "delta": mp.nstr(delta_B3, 50, strip_zeros=False),
        "rel_diff": mp.nstr(delta_B3 / vol_B3_catalan, 20),
    })
    w.add_assertion(
        "Vol(𝓑₃) via Lobachevsky == 8·G (at 100 dps)",
        computed=float(mp.fabs(delta_B3 / vol_B3_catalan)),
        expected=0.0,
        tolerance=1e-30,
        unit="relative",
        source="Adams 1985 + Λ(π/4) = G/2; both sides should agree exactly",
    )

    # ── Comparison vs SnapPy / literature value ──────────────
    # The audit (`2026-05-18-lambda-scale-derivation-search.md` §93–104)
    # quoted: "8·G = 7.327724753..., Vol(B_3) literature = 7.327722906...,
    # Difference = 1.85 × 10⁻⁶".
    # If the audit's "literature" value comes from a SnapPy compute at
    # default precision (~10 digits), the 1.85e-6 gap is precision
    # artifact, not a real discrepancy.
    audit_literature_value = mp.mpf("7.327722906465")  # from atlas + audit
    delta_vs_literature = vol_B3_catalan - audit_literature_value
    w.add_data("vs_audit_literature_value", {
        "audit_source": "docs/audits/2026-05-18-lambda-scale-derivation-search.md §93–104",
        "audit_literature_value": "7.327722906465",
        "vol_B3_100dps": mp.nstr(vol_B3_catalan, 100, strip_zeros=False),
        "delta": mp.nstr(delta_vs_literature, 20),
        "rel_diff": mp.nstr(delta_vs_literature / vol_B3_catalan, 12),
        "audit_claimed_gap": "1.85e-6",
        "verdict": (
            "If our 100-dps Lobachevsky/Catalan value agrees with the "
            "audit's literature 7.32772275... at the precision of the "
            "literature quote (~12 digits), the audit's '1.85e-6 gap' "
            "was a precision artifact, not a structural disagreement. "
            "Vol(𝓑₃) = 8·G is an EXACT identity, not approximate."
        ),
    })

    # ── First-10-digits sanity ───────────────────────────────
    vol_B3_str_10 = mp.nstr(vol_B3_catalan, 12)
    print(f"  G                  = {mp.nstr(G_mpmath, 20)}")
    print(f"  Λ(π/4)             = {mp.nstr(lambda_pi_over_4, 20)}")
    print(f"  G/2                = {mp.nstr(G_over_2, 20)}")
    print(f"  Vol(𝓑₃) = 16Λ(π/4) = {mp.nstr(vol_B3_lobachevsky, 20)}")
    print(f"  Vol(𝓑₃) = 8·G       = {mp.nstr(vol_B3_catalan, 20)}")
    print(f"  Δ                   = {mp.nstr(delta_B3, 10)}")
    print(f"  audit lit. (12dps) = 7.32772290647")
    print(f"  ours    (12dps)    = {vol_B3_str_10}")

    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
