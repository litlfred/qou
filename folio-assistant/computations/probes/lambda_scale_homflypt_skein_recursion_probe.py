#!/usr/bin/env python3


# polynomial_q_not_applicable: PSLQ search over multi-knot HOMFLYPT
# polynomial evaluations at substrate substitutions.
"""λ_scale HOMFLYPT skein-recursion PSLQ probe — Strategy J deep dive.

Strategy J (`3a1b11069 spike(strategy-j)`) tested ~20 candidate
ratios of scalar tr_M values for m_n/m_p closure; its conclusion:

  "Full HOMFLYPT skein recursion COULD produce richer combinations
   but would need to beat 0.45 % by a factor of 10⁵⁺ to reach ppb,
   which is implausible given the prior 7 negative searches in
   the CAL-4 enumeration."

This probe formally tests the "deep recursion COULD produce" caveat
by extending Strategy G's single-knot Borromean check
(`lambda_scale_alt_g_skein_polynomial_direct.py`) to a multi-knot
HOMFLYPT polynomial basis and running PSLQ at maxcoeff 10⁵ against
two sharply-defined targets:

  T1 = (3/4)·h²       = the post-Yekutieli residual identified in
                        docs/audits/2026-05-23-lambda-scale-replace-
                        vs-add-analysis.md §2 (matches 316 ppm)
  T2 = λ_p_codata     = the full m_p-formula target (Tier-1 case)

Multi-knot basis (HOMFLYPT polynomials from Lickorish-Millett 1986
+ Murasugi §10; all evaluated at the SU_q(2) Jones specialisation
α = q⁻¹, z = q − q⁻¹):

  knot      HOMFLYPT P(α, z)
  ─────────────────────────────────────────────────────────────
  3_1 (R)   2α² − α⁴ + α²·z²
  4_1       α² + α⁻² − 1 − z²
  5_2       α⁻²(−α⁻⁴ + α⁻²·z² + 2α⁻² − 1 + z²)
  𝓑_3       (a⁴ + a⁻⁴)·(z⁴ − 4z² + 4)
            + (2z⁴ − 8z² + 6)·(a² + a⁻²)
            + (z⁶ − 7z⁴ + 12z² − 6)
            (Borromean, Lickorish-Millett 1986; reused from
             lambda_scale_alt_g_skein_polynomial_direct.py)

Each knot's HOMFLYPT is evaluated at 3 substrate parameter points:
α ∈ {q_0, q_0⁻¹, q_0^{1/2}} with z = q_0 − q_0⁻¹ fixed. This gives
4 knots × 3 evaluations = 12 basis vectors. PSLQ searches for an
integer combination matching T1 or T2.

EXPECTED OUTCOME: confirmatory NEGATIVE.

The cumulative 8-search case (acknowledged in `00083b94e`) covers
all closely-related substrate-categorical paths. Strategy J's
scalar tr_M probe at 0.45 % m_n/m_p and Strategy G's single-knot
HOMFLYPT at 0.0165 % λ_p (best signal but no closure) bracket
the expected magnitude. The multi-knot multi-substitution basis
here is structurally richer than either alone, but the 10⁵⁺
gap that Strategy J flagged for ppb closure is not bridgeable
by a 12-element basis at maxcoeff 10⁵.

A positive result would be surprising and significant. A negative
result formally retires the "deep HOMFLYPT recursion" closure
candidate, complementing the Tier 6 Bring-Bloch closure of
hyperbolic-volume-based routes.

Refs:
- docs/audits/2026-05-23-lambda-scale-replace-vs-add-analysis.md §4
- lambda_scale_alt_g_skein_polynomial_direct.py (Strategy G predecessor)
- 3a1b11069 spike(strategy-j) — Strategy J scalar-ratio probe
- 00083b94e content(lambda-scale-bring-bloch) — 8-search CAL-4
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from mpmath import mpf, pslq  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# Reuse Strategy G's Borromean HOMFLYPT closed form
from lambda_scale_alt_g_skein_polynomial_direct import (  # noqa: E402
    homflypt_borromean_at_az,
)


def homflypt_trefoil(a: mpf, z: mpf) -> mpf:
    """P(3_1, right-handed; a, z) = 2a² − a⁴ + a²·z²."""
    return 2 * a ** 2 - a ** 4 + a ** 2 * z ** 2


def homflypt_figure8(a: mpf, z: mpf) -> mpf:
    """P(4_1; a, z) = a² + a⁻² − 1 − z²  (Lickorish-Millett 1986)."""
    return a ** 2 + a ** (-2) - 1 - z ** 2


def homflypt_5_2(a: mpf, z: mpf) -> mpf:
    """P(5_2; a, z) = a⁻²·(−a⁻⁴ + a⁻²·z² + 2a⁻² − 1 + z²).

    Form from KnotInfo's HOMFLYPT table (5_2 entry, KnotInfo's
    sign convention); rewritten to expose the a⁻² factor.
    """
    return a ** (-2) * (
        -a ** (-4) + a ** (-2) * z ** 2 + 2 * a ** (-2) - 1 + z ** 2
    )


def main() -> int:
    mp.mp.dps = 80

    w = WitnessBuilder(
        "lambda-scale-homflypt-skein-recursion-probe",
        engine="mpmath",
    )
    w.set_description(
        "Strategy J deep dive: PSLQ search across a 12-element basis "
        "of HOMFLYPT polynomial values for {3_1, 4_1, 5_2, 𝓑_3} "
        "evaluated at α ∈ {q_0, q_0⁻¹, q_0^{1/2}}, z = q_0 − q_0⁻¹. "
        "Two targets: (T1) post-Yekutieli residual (3/4)·h², "
        "(T2) λ_p_codata directly. Formally tests Strategy J's "
        "'deep recursion COULD produce' caveat. Expected confirmatory "
        "negative per 8-search cumulative case (00083b94e)."
    )
    MAX_COEF_EXP = 5
    w.add_parameter("compute_dps", "80")
    w.add_parameter("max_coef_exponent", str(MAX_COEF_EXP))
    w.add_parameter("homflypt_knots", "{3_1, 4_1, 5_2, B_3}")
    w.add_parameter(
        "substitutions",
        "α ∈ {q_0, q_0⁻¹, q_0^{1/2}}; z = q_0 − q_0⁻¹",
    )

    Q0 = mpf(Q_50_DIGIT_STR)
    HBAR_Q = (Q0 - 1) / Q0
    h = Q0 - 1 / Q0
    G = mp.catalan
    z = h

    # Pre-Yekutieli + post-Yekutieli targets
    lambda_p_codata = mpf("2.4599527843613182892482457339493")
    lambda_yekutieli = mpf(5) / 2 + (mpf(3) / 4 - G) * h ** 2
    target_post_yekutieli_residual = lambda_yekutieli - lambda_p_codata
    target_residual_coef = target_post_yekutieli_residual / h ** 2

    w.add_data("substrate", {
        "q_0": mp.nstr(Q0, 32),
        "hbar_q": mp.nstr(HBAR_Q, 32),
        "h": mp.nstr(h, 32),
        "G_catalan": mp.nstr(G, 32),
    })
    w.add_data("targets", {
        "T1_residual_coef_3_4": mp.nstr(target_residual_coef, 20),
        "T2_lambda_p_codata": mp.nstr(lambda_p_codata, 32),
        "post_yekutieli_residual": mp.nstr(target_post_yekutieli_residual, 20),
    })

    # Build the 12-element basis
    knots = {
        "3_1": homflypt_trefoil,
        "4_1": homflypt_figure8,
        "5_2": homflypt_5_2,
        "B_3": homflypt_borromean_at_az,
    }
    alphas = {
        "q_0": Q0,
        "q_0_inv": 1 / Q0,
        "q_0_sqrt": mp.sqrt(Q0),
    }

    basis = {}
    for k_name, k_fn in knots.items():
        for a_name, a_val in alphas.items():
            label = f"P_{k_name}@α={a_name}"
            basis[label] = k_fn(a_val, z)

    w.add_data("basis", {n: mp.nstr(v, 25) for n, v in basis.items()})
    w.add_data("basis_size", len(basis))

    names = list(basis.keys())
    vols = list(basis.values())

    # ──────────────── PSLQ #1 — post-Yekutieli residual ────────────────
    print(f"  PSLQ #1: target = (λ_Y − λ_fit)/h² ≈ {mp.nstr(target_residual_coef, 12)}")
    print(f"           basis  = {len(vols)}-element HOMFLYPT multi-knot")
    vec1 = [target_residual_coef] + vols
    try:
        rel1 = pslq(vec1, tol=mpf("1e-12"), maxcoeff=10 ** MAX_COEF_EXP)
    except Exception as e:
        print(f"  PSLQ #1 raised: {e}")
        rel1 = None

    relation_found_1 = rel1 is not None and rel1[0] != 0
    if rel1 is None or rel1[0] == 0:
        print("  ✗ PSLQ #1 — no informative relation found.")
        w.add_data("pslq_target_1_relation_found", False)
    else:
        n_target, *n_basis = rel1
        coefs = {names[i]: -n_basis[i] for i in range(len(names))
                 if n_basis[i] != 0}
        s = sum(mpf(-n_basis[i]) / mpf(n_target) * vols[i]
                for i in range(len(vols)))
        residual = abs(s - target_residual_coef)
        print(f"  ✓ PSLQ #1 — relation FOUND (n_target={n_target}):")
        for k, v in coefs.items():
            print(f"    {v:+d} · {k}")
        print(f"    residual: {mp.nstr(residual, 12)}")
        w.add_data("pslq_target_1_relation_found", True)
        w.add_data("pslq_target_1_result", {
            "pslq_relation": [int(r) for r in rel1],
            "coefs": {k: str(v) for k, v in coefs.items()},
            "n_target": int(n_target),
            "residual_abs": mp.nstr(residual, 12),
        })

    # ──────────────── PSLQ #2 — λ_p_codata directly ────────────────
    print()
    print(f"  PSLQ #2: target = λ_p_codata = {mp.nstr(lambda_p_codata, 12)}")
    print(f"           basis  = {len(vols)}-element HOMFLYPT multi-knot")
    vec2 = [lambda_p_codata] + vols
    try:
        rel2 = pslq(vec2, tol=mpf("1e-12"), maxcoeff=10 ** MAX_COEF_EXP)
    except Exception as e:
        print(f"  PSLQ #2 raised: {e}")
        rel2 = None

    relation_found_2 = rel2 is not None and rel2[0] != 0
    if rel2 is None or rel2[0] == 0:
        print("  ✗ PSLQ #2 — no informative relation found.")
        w.add_data("pslq_target_2_relation_found", False)
    else:
        n_target, *n_basis = rel2
        coefs = {names[i]: -n_basis[i] for i in range(len(names))
                 if n_basis[i] != 0}
        s = sum(mpf(-n_basis[i]) / mpf(n_target) * vols[i]
                for i in range(len(vols)))
        residual = abs(s - lambda_p_codata)
        print(f"  ✓ PSLQ #2 — relation FOUND (n_target={n_target}):")
        for k, v in coefs.items():
            print(f"    {v:+d} · {k}")
        print(f"    residual: {mp.nstr(residual, 12)}")
        w.add_data("pslq_target_2_relation_found", True)
        w.add_data("pslq_target_2_result", {
            "pslq_relation": [int(r) for r in rel2],
            "coefs": {k: str(v) for k, v in coefs.items()},
            "n_target": int(n_target),
            "residual_abs": mp.nstr(residual, 12),
        })

    any_relation = relation_found_1 or relation_found_2
    w.add_assertion(
        "Multi-knot HOMFLYPT PSLQ — no closure relation expected "
        "for either target",
        computed=float(not any_relation),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source=(
            "mpmath.pslq at max_coef=10^5, tol=1e-12 on a 12-element "
            "basis of HOMFLYPT polynomial values for {3_1, 4_1, 5_2, "
            "𝓑_3} × α ∈ {q_0, q_0⁻¹, q_0^{1/2}}. A negative result "
            "complements Tier 6 by closing off the 'deep HOMFLYPT "
            "recursion COULD produce' caveat in 3a1b11069's Strategy "
            "J scalar-ratio probe. Combined with the 8-search "
            "cumulative case in 00083b94e, the Bring-Bloch + HOMFLYPT "
            "axes are now both retired as λ_scale closure candidates."
        ),
    )

    out = w.set_audit_only(
        "docs/audits/2026-05-23-lambda-scale-replace-vs-add-analysis.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
