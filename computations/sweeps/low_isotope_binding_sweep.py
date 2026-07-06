#!/usr/bin/env python3


# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Low-isotope mass-volume binding-energy sweep.

Applies the formalized framework from
particle-interactions §8 (thurston-volume-additivity /
mass-volume-factorization / crossing-graded-mass-expansion /
lifted-crossing-locality / frobenius-packing-density) to light
isotopes with Z = 1..10.  Includes ⁸Be (unstable, lifetime
~10⁻¹⁶ s) as a topologically meaningful α-chain node.

Strategies (in order of specificity):

  (A) Census knot match — for A = 2, 3 the complement of the
      atomic braid is a named hyperbolic knot/link from SnapPy's
      census (D → 6_2, T → 8_11, ³He → Borromean 6³_2).
      B = ρ(A) · Vol(census_knot).

  (B) α-cluster unfolding — for A ≥ 4 Z=N (α-chain atoms):
      B = n_α · B(⁴He) + C(n_α, 2) · c_αα,
      with c_αα = m_e · Vol(7²_1) = 2.425 MeV fit from ¹²C.

  (C) Partial-shell extrapolation — for odd-A or Z ≠ N atoms:
      Interpolate between nearest α-chain anchors using a linear
      "shell-filling fraction" f(A) = (A - A_below) / (A_above - A_below).
      This is a phenomenological stop-gap pending direct knot ID.

Outputs:
  low-isotope-binding-sweep.witness.json  — full sweep table,
      organized by strategy, with residuals.

Notes:
- AME2020 binding energies from published table; proton + neutron
  masses not subtracted, B is pure binding.
- No free parameters per strategy; c_αα is not a fit here
  (re-used from jsj_alpha_clustering fit of ¹²C = Vol(7²_1)·m_e).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, HBAR_Q, HBAR_Q_SQ
# CAL-1: m_e sourced from codata_constants registry (P31-triage Phase A);
# coerced to float for json-serialisable arithmetic in this script.
from codata_constants import M_E_MEV as _M_E_MEV_MP

# Knot volumes — single source of truth (knot_volumes module,
# mpmath 50dps Clausen / SnapPy HP literature). Pre-refactor these
# were f64 hardcoded literals at varying precision (VOL_7_2_1 =
# 4.7495 = 4 digits, VOL_6_2 = 4.40083 = 5 digits, etc.); now all
# derive from the same 50-dps source. See knot-vol _precision
# propagation in PR #781 coordination ledger.
from knot_volumes import (  # noqa: E402
    CATALAN_G,
    VOL_BORROMEAN,
    VOL_7_SQ_1 as VOL_7_2_1,    # legacy alias preserved
    VOL_6_2,
    VOL_8_11,
)

M_E_MEV = float(_M_E_MEV_MP)

# Strategy-(B) α-cluster parameters
B_4HE_MEV = 28.295674                     # AME2020
c_alpha_alpha_MEV = M_E_MEV * VOL_7_2_1   # ≈ 2.4269 MeV — derived, not fit here

# ── AME2020 binding energies (Z ≤ 10) ────────────────────────────
# B in MeV, source: AME2020 table; A = Z + N.
AME: list[tuple[str, int, int, float]] = [
    # (symbol, Z, N, B_MeV)
    ("1H",   1, 0,   0.000),   # proton, no binding
    ("2H",   1, 1,   2.22458),
    ("3H",   1, 2,   8.4818),
    ("3He",  2, 1,   7.7180),
    ("4He",  2, 2,  28.29566),
    ("6Li",  3, 3,  31.9941),
    ("7Li",  3, 4,  39.2446),
    ("8Be",  4, 4,  56.4995),  # unstable (10⁻¹⁶ s)
    ("9Be",  4, 5,  58.1651),
    ("10Be", 4, 6,  64.9775),
    ("10B",  5, 5,  64.7512),
    ("11B",  5, 6,  76.2054),
    ("12C",  6, 6,  92.1617),
    ("13C",  6, 7,  97.1081),
    ("14N",  7, 7, 104.6589),
    ("15N",  7, 8, 115.4919),
    ("16O",  8, 8, 127.6193),
    ("17O",  8, 9, 131.7629),
    ("18O",  8, 10, 139.8074),
    ("19F",  9, 10, 147.8013),
    ("20Ne", 10, 10, 160.6449),
    ("21Ne", 10, 11, 167.4060),
    ("22Ne", 10, 12, 177.7700),
]


def strategy_A_census(symbol: str, Z: int, N: int) -> tuple[float | None, str]:
    """Light atoms with named census knot for the atomic link."""
    A = Z + N
    if A == 2:
        # D = p + n, atomic link = knot 6_2, single-chirality
        return M_E_MEV * VOL_6_2, "census:6_2,ρ=m_e"
    if A == 3 and Z == 1:
        # T = 1p + 2n, atomic link = knot 8_11, CPT-saturated
        return 2 * M_E_MEV * VOL_8_11, "census:8_11,ρ=2m_e"
    if A == 3 and Z == 2:
        # ³He = 2p + 1n, atomic link ≈ Borromean, CPT-saturated
        return 2 * M_E_MEV * VOL_BORROMEAN, "census:Borromean,ρ=2m_e"
    return None, ""


def _alpha_chain_binding(n_alpha: int) -> float:
    """Closed-form α-chain binding for n_α alpha clusters with
    all-pairs coupling c_αα (= m_e · Vol(7²_1)):

        B = n_α · B(⁴He) + C(n_α, 2) · c_αα.

    Shared helper used by strategy_B_alpha_cluster and
    strategy_C_partial_shell to avoid duplicated formula.
    """
    n_pairs = n_alpha * (n_alpha - 1) // 2
    return n_alpha * B_4HE_MEV + n_pairs * c_alpha_alpha_MEV


def strategy_B_alpha_cluster(symbol: str, Z: int, N: int) -> tuple[float | None, str]:
    """α-chain atoms (A = 4 n_α, Z = N = 2 n_α)."""
    A = Z + N
    if Z != N or A % 4 != 0:
        return None, ""
    n_alpha = A // 4
    if n_alpha < 1:
        return None, ""
    n_pairs = n_alpha * (n_alpha - 1) // 2
    B_pred = _alpha_chain_binding(n_alpha)
    return B_pred, f"α-cluster:n_α={n_alpha},pairs={n_pairs}"


def strategy_C_partial_shell(symbol: str, Z: int, N: int) -> tuple[float | None, str]:
    """Linear interpolation between nearest α-chain anchors.

    Shell-filling fraction f = (A - A_below) / (A_above - A_below)
    where A_below, A_above are the nearest α-chain mass numbers with
    Z = N = n_α · 2.

    This is phenomenological — a stop-gap pending direct knot ID
    for odd-A and asymmetric atoms.
    """
    A = Z + N
    # α-chain anchors: A = 4n with Z = N = 2n
    anchors = [4, 8, 12, 16, 20, 24]
    if A <= 4:
        return None, ""
    # Find bracketing anchors
    A_below = max((x for x in anchors if x <= A), default=4)
    A_above = min((x for x in anchors if x >= A), default=A_below)
    if A_above == A_below:
        # exactly on an anchor — use the α-chain helper directly
        n_alpha = A_below // 4
        B_below = _alpha_chain_binding(n_alpha)
        return B_below, f"anchor:{A_below}"

    n_below = A_below // 4
    n_above = A_above // 4
    B_below = _alpha_chain_binding(n_below)
    B_above = _alpha_chain_binding(n_above)
    frac = (A - A_below) / (A_above - A_below)
    B_pred = B_below + frac * (B_above - B_below)
    return B_pred, (
        f"partial-shell:f={frac:.3f} from A={A_below}→{A_above}"
    )


def predict(symbol: str, Z: int, N: int) -> tuple[float, str]:
    """Apply strategies A → B → C in order; return the first that fires."""
    for strat in (strategy_A_census, strategy_B_alpha_cluster, strategy_C_partial_shell):
        B_pred, tag = strat(symbol, Z, N)
        if B_pred is not None:
            return B_pred, tag
    return 0.0, "none"


def main() -> int:
    rows = []
    print(f"\n  Substrate q_0 = {Q0:.6f}")
    print(f"  m_e = {M_E_MEV:.6f} MeV, 2m_e = {2*M_E_MEV:.6f} MeV")
    print(f"  Vol(Borromean) = 8G ≈ {VOL_BORROMEAN:.4f}")
    print(f"  Vol(6_2) ≈ {VOL_6_2:.4f}, Vol(8_11) ≈ {VOL_8_11:.4f}")
    print(f"  c_αα = m_e · Vol(7²_1) ≈ {c_alpha_alpha_MEV:.4f} MeV\n")

    header = f"  {'atom':>6} {'A':>3} {'B_AME':>10} {'B_pred':>10} {'err_%':>8}  strategy"
    print(header)
    print("  " + "-" * (len(header) - 2))

    for symbol, Z, N, B_ame in AME:
        A = Z + N
        B_pred, tag = predict(symbol, Z, N)
        if B_ame == 0 and B_pred == 0:
            err_pct = 0.0
        elif B_ame == 0:
            err_pct = float("inf")
        else:
            err_pct = 100.0 * (B_pred - B_ame) / B_ame
        print(f"  {symbol:>6} {A:>3} {B_ame:>10.4f} {B_pred:>10.4f} {err_pct:>+8.2f}  {tag}")
        rows.append({
            "symbol": symbol,
            "Z": Z,
            "N": N,
            "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": B_pred,
            "residual_MeV": B_pred - B_ame,
            "error_pct": err_pct,
            "strategy": tag,
        })

    # Summary statistics by strategy
    strategy_groups: dict[str, list[dict]] = {}
    for r in rows:
        key = r["strategy"].split(":")[0] or "none"
        strategy_groups.setdefault(key, []).append(r)

    print("\n  Summary by strategy:")
    stats = {}
    for key, group in strategy_groups.items():
        ok = [r for r in group if r["B_AME_MeV"] > 0]
        if not ok:
            continue
        abs_errs = [abs(r["error_pct"]) for r in ok if abs(r["error_pct"]) != float("inf")]
        mean_err = sum(abs_errs) / len(abs_errs) if abs_errs else 0
        max_err = max(abs_errs) if abs_errs else 0
        print(f"    {key:>18}: n={len(ok):>2}  mean|err|={mean_err:>6.2f}%  max|err|={max_err:>6.2f}%")
        stats[key] = {"n": len(ok), "mean_abs_err_pct": mean_err, "max_abs_err_pct": max_err}

    witness = {
        "name": "low-isotope-binding-sweep",
        "description": (
            "Low-isotope (Z = 1..10) binding-energy sweep using the "
            "mass-volume factorization framework (Ch 11 §8).  Three "
            "strategies applied in order: (A) census-knot match for "
            "A ≤ 3, (B) α-cluster unfolding for Z = N, A = 4n, "
            "(C) partial-shell linear interpolation for odd-A and "
            "non-N=Z atoms.  Zero free parameters per strategy."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "framework_refs": [
            "conj:mass-volume-factorization",
            "conj:crossing-graded-mass-expansion",
            "conj:lifted-crossing-locality",
            "rem:frobenius-packing-density",
            "rem:soft-confinement-at-q0",
        ],
        "constants": {
            "q_0": Q0,
            "hbar_q_sq": HBAR_Q_SQ,
            "M_E_MEV": M_E_MEV,
            "CATALAN_G": CATALAN_G,
            "VOL_BORROMEAN_8G": VOL_BORROMEAN,
            "VOL_6_2": VOL_6_2,
            "VOL_8_11": VOL_8_11,
            "VOL_7_2_1": VOL_7_2_1,
            "B_4HE_MEV": B_4HE_MEV,
            "c_alpha_alpha_MEV": c_alpha_alpha_MEV,
        },
        "rows": rows,
        "stats_by_strategy": stats,
    }

    out_path = Path(__file__).parent / "low-isotope-binding-sweep.witness.json"
    out_path.write_text(json.dumps(witness, indent=2))
    print(f"\n  Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
