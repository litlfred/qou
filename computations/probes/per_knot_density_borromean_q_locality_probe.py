"""q-locality probe for the canonical `PerKnotDensity(𝓑₃, q)` evaluation.

Tests whether the production mass formula
    m_p_pred(q) = m_e · PerKnotDensity(𝓑₃, q)
has the correct *q-derivative* near q_0, matching the q-dependence
of m_p_CODATA equivalently expressed as a candidate linking weight
    λ_p_codata(q) = m_p_CODATA · ℏ_q² / (m_e · Vol(𝓑₃)).

Background — q-locality discipline (commits c1dca4d73 + c18e562b9
on main; PR #916 / #962 / PR #951 history): a structurally-correct
candidate linking_weight(q) should have small slope of
    (candidate(q) − λ_p_codata(q)) at q_0
i.e. the candidate moves in lockstep with the CODATA-implied target
as q varies. A large slope means the candidate only matches at the
substrate point q_0 — a coincidence, not a structural fit.

Empirical baselines from prior probes (PR #951 / commit 1a29b209b):

    candidate (purged or rejected)              slope (ppm/q)
    ──────────────────────────────────────────  ─────────────
    1/(1 − h_q · q_0^10) (Faddeev × Bring)      −1.5 × 10⁷
    5/2 − G · h_q²       (bare REPLACE)         −1.7 × 10⁷
    V_7 = Σ dim_q/[4]_q  (#916 Strategy H)      −1.86 × 10⁷
    5/2 − ℏ_q² · ⟨𝓑_3⟩   (#916 Strategy G)      −1.69 × 10⁷
    Family A canonical   (5/2 + 3h²/4)          −1.69 × 10⁷ [also fails]
    Strategy I (purged)  (5/2 + (3/4 − G)·h²)   −1.69 × 10⁷ [also fails]

This probe extends the analysis to the full canonical pipeline:
`PerKnotDensity(𝓑₃, q)` = (Vol(𝓑₃) / ℏ_q²) × linking_weight_FamilyA(q).

Per author directive (2026-05-24): "Re-run q-locality smooth-crossing
test on Geom-mapped form (PR #951 failed on standalone 5/2 − G·h²;
needs full Geom functor output not bare polynomial)". This script
runs that test end-to-end on the canonical PerKnotDensity call.

Outputs witness JSON with slope, pass/fail verdict, and comparison
to historical baselines.

Status: EXPLORATORY (q-locality is an audit-discipline test, not a
production compute). Per `local/production-vs-exploratory-discipline`.
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf

# 50-dps compute discipline (AGENTS.md §Precision goals L1 floor)
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

# Import canonical infrastructure
sys.path.insert(0, str(Path(__file__).parent))
from _li_2_q_util import per_knot_density_borromean  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# Constants — anchored on the registry / CODATA values
# CAL-1 from the registry, not re-typed: the literal here was
# "0.510998950", CODATA truncated to 9 s.f. (canonical 0.51099895069).
from codata_constants import M_E_MEV  # noqa: E402  # CAL-1
from mpmath import mpf as mpf_type  # noqa: E402

def _fmt_deep(obj):
    """Serialize every mpf in a nested structure with `_precision.fmt`.

    The producers here build one dict that serves twice: as the witness payload
    AND as the thing their own prints/comparisons read. Downcasting with
    `float()` at construction satisfied the printing but put raw binary64 into
    the witness. Stringifying the float instead would be laundering — the
    serializer says so in as many words ("never to stringify the float ...
    Carry mpmath.mpf from the source and serialize with `_precision.fmt`").

    So the dicts now hold mpf all the way through (mpf supports `:.4e`,
    `:.10f`, `abs()`, comparisons — everything these files do with them) and
    this converts at the witness boundary only, at OUTPUT_DPS rather than the
    compute precision, so guard digits are not published.
    """
    if isinstance(obj, dict):
        return {k: _fmt_deep(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_fmt_deep(v) for v in obj]
    if isinstance(obj, mpf_type):
        return fmt(obj)
    return obj

M_P_CODATA_MEV = mpf(M_P_MEV_VALIDATION)
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin

# q-locality discipline: tolerance and sweep window
SWEEP_DELTAS = [mpf("0.001"), mpf("0.01"), mpf("0.05")]
TOLERANCE_PPM_PER_Q = mpf("1e5")  # upstream q-locality threshold


def lambda_p_codata(q: mpf) -> mpf:
    """The linking weight value the framework would need at this q
    to make m_p_pred(q) exactly = m_p_CODATA. Inverse of the
    production formula:
        m_p_pred = m_e · (Vol(𝓑₃) / ℏ_q²) · linking_weight
        ↔ linking_weight = m_p_CODATA · ℏ_q² / (m_e · Vol(𝓑₃))
    """
    hbar_q = (q - 1) / q
    vol_b3 = 8 * mp.catalan
    return M_P_CODATA_MEV * hbar_q ** 2 / (M_E_MEV * vol_b3)


def per_knot_density_linking_weight(q: mpf) -> mpf:
    """The linking weight inside `per_knot_density_borromean(q)` — extract
    by dividing out Geom_leading = Vol(𝓑₃) / ℏ_q².
    """
    hbar_q = (q - 1) / q
    vol_b3 = 8 * mp.catalan
    geom_leading = vol_b3 / hbar_q ** 2
    return per_knot_density_borromean(q) / geom_leading


def slope_ppm_per_q(f, q_center: mpf, delta: mpf) -> mpf:
    """Numerical slope of (f − λ_p_codata) at q_center, evaluated
    over q ∈ [q_center − delta, q_center + delta], reported in ppm/q
    relative to f(q_center).
    """
    q_plus = q_center + delta
    q_minus = q_center - delta
    diff_plus = f(q_plus) - lambda_p_codata(q_plus)
    diff_minus = f(q_minus) - lambda_p_codata(q_minus)
    slope_abs = (diff_plus - diff_minus) / (2 * delta)
    return mpf("1e6") * slope_abs / f(q_center)


def run_probe() -> dict:
    """Run the q-locality probe and return a witness dict."""
    results = []
    for delta in SWEEP_DELTAS:
        slope = slope_ppm_per_q(per_knot_density_linking_weight, Q_0, delta)
        results.append({
            "delta": delta,
            "slope_ppm_per_q": slope,
            "abs_slope_ppm_per_q": abs(slope),
            "pass_q_locality": bool(abs(slope) < TOLERANCE_PPM_PER_Q),
        })

    # Reference values at q_0
    lw_q0 = per_knot_density_linking_weight(Q_0)
    target_q0 = lambda_p_codata(Q_0)
    gap_at_q0 = lw_q0 - target_q0
    gap_ppm = mpf("1e6") * gap_at_q0 / target_q0

    # Production prediction
    gf_q0 = per_knot_density_borromean(Q_0)
    m_p_pred = M_E_MEV * gf_q0
    relative_err = (m_p_pred - M_P_CODATA_MEV) / M_P_CODATA_MEV

    # Historical baseline slopes (from prior probes)
    historical_baselines = {
        "family_a_canonical_5_2_plus_3h2_over_4": "-1.69e7 ppm/q (PR #951)",
        "yekutieli_purged_5_2_plus_3_4_minus_G_h2": "-1.69e7 ppm/q (PR #951)",
        "bare_replace_5_2_minus_G_h2": "-1.7e7 ppm/q (PR #951)",
        "v_7_strategy_h": "-1.86e7 ppm/q (PR #916)",
        "strategy_g_5_2_minus_hbar2_borr_trace": "-1.69e7 ppm/q (PR #916)",
        "faddeev_x_bring_1_over_1_minus_hq_q010": "-1.5e7 ppm/q",
        "upstream_q_locality_tolerance": "≤ 1e5 ppm/q",
    }

    verdict = {
        "all_deltas_pass": all(r["pass_q_locality"] for r in results),
        "max_abs_slope_ppm_per_q": (max(abs(mpf(r["slope_ppm_per_q"]))
                                              for r in results)),
        "interpretation": (
            "PASS — PerKnotDensity's linking weight tracks λ_p_codata locally"
            if all(r["pass_q_locality"] for r in results)
            else "FAIL — PerKnotDensity's linking weight does NOT track "
                 "λ_p_codata locally; slope dominated by ℏ_q² prefactor "
                 "as in all prior bare-polynomial probes. Production "
                 "Family A linking weight (5/2 + 3h²/4) is not "
                 "structurally q-local with respect to the CODATA "
                 "target near q_0. Closure requires refinement of "
                 "PerKnotDensity at higher h² orders (S_4↓S_3 bijection "
                 "+ S_5↔SO(3) fiber action — see docs/audits/"
                 "2026-05-24-family-a-gap-audit.md)."
        ),
    }

    return {
        "compute": "per_knot_density_borromean_q_locality_probe",
        "description": (
            "q-locality discipline test applied to canonical "
            "`per_knot_density_borromean(q)` near q_0. Tests whether the "
            "linking weight inside PerKnotDensity has the same local "
            "q-derivative as the CODATA-implied target."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "M_E_MEV": str(M_E_MEV),
            "M_P_CODATA_MEV": str(M_P_CODATA_MEV),
            "tolerance_ppm_per_q": TOLERANCE_PPM_PER_Q,
            "sweep_deltas": list(SWEEP_DELTAS),   # already mpf; do not downcast
        },
        "results": {
            "linking_weight_at_q0": lw_q0,
            "lambda_p_codata_at_q0": target_q0,
            "gap_at_q0": gap_at_q0,
            "gap_ppm_at_q0": gap_ppm,
            "per_knot_density_at_q0": gf_q0,
            "m_p_pred_MeV": m_p_pred,
            "m_p_codata_MeV": M_P_CODATA_MEV,
            "relative_error": relative_err,
            "relative_error_pct": relative_err * 100,
            "slopes_by_delta": results,
        },
        "verdict": verdict,
        "historical_baselines": historical_baselines,
        "status": "exploratory",
        "tags": [
            "q-locality",
            "per-knot-density-refinement",
            "smooth-crossing",
            "family-a-gap",
            "borromean",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }


def main() -> None:
    print(f"q-locality probe for per_knot_density_borromean(q) near q_0 = {Q_0}")
    print(f"50-dps compute discipline; tolerance = {TOLERANCE_PPM_PER_Q} ppm/q")
    print("---")

    witness = run_probe()

    # Pretty-print key results
    print(f"linking_weight(q_0)  = {witness['results']['linking_weight_at_q0']:.10f}")
    print(f"λ_p_codata(q_0)      = {witness['results']['lambda_p_codata_at_q0']:.10f}")
    print(f"gap at q_0           = {witness['results']['gap_ppm_at_q0']:.1f} ppm")
    print(f"m_p_pred             = {witness['results']['m_p_pred_MeV']:.4f} MeV")
    print(f"m_p_codata           = {witness['results']['m_p_codata_MeV']:.4f} MeV")
    print(f"relative error       = {witness['results']['relative_error_pct']:+.3f}%")
    print("---")
    for r in witness['results']['slopes_by_delta']:
        verdict = "PASS" if r['pass_q_locality'] else "FAIL"
        print(f"δ = {r['delta']:.4f}: slope = {r['slope_ppm_per_q']:+.3e} ppm/q  [{verdict}]")
    print("---")
    print(f"Verdict: {witness['verdict']['interpretation']}")

    # Write witness
    out_path = Path(__file__).parent / "per-knot-density-borromean-q-locality-probe.witness.json"
    # fmt at the write boundary: the `witness` dict carries mpf all the way
    # through so the prints above keep their format specs, and only the
    # serialized copy is converted -- at OUTPUT_DPS, not compute precision.
    out_path.write_text(
        json.dumps(_fmt_deep(witness), indent=2, sort_keys=True) + "\n")
    print(f"\nWitness written to: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
