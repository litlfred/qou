"""qbeta_residue_a_precision_ceiling — how many digits of A are real?

Answers the author's question (PR #1804 D3 follow-up): can residue A be
recomputed to ≥30 digits to unblock the PSLQ period probe?

KEY FINDING (feasibility): A is NOT compute-precision-limited. It is the
asymptotic limit

    A = lim_{k→∞} c_k · u_subst^k

extracted in Step 1 of PR #1727 from the simple-pole signature, sampled
only at k = 8, 9, 10 (the c_k beyond 10 require an ansatz fit, forbidden
per CLAUDE.md). The c_k are already 50 dps — so the limiter is the
ASYMPTOTIC CONVERGENCE, not the arithmetic precision.

This script quantifies the achievable precision honestly:
  1. Recompute x_k = c_k·u_subst^k for k = 4..10 at 120 dps; confirm the
     tail spread is intrinsic (not compute noise) by checking it is
     stable as compute dps rises.
  2. Several extrapolation estimators of the k→∞ limit:
       - raw mean over k = 8,9,10 (the Step-1 method)
       - Aitken Δ² on (8,9,10) and on (7,8,9)
       - 3-point geometric solve x_k = A + B·ρ^k from (8,9,10)
  3. The SPREAD across these estimators is the honest error bar on A.
     achievable_digits = −log10(spread / A).

NO ansatz for c_11+. Extrapolation uses only the existing canonical
c_2..c_10. The extrapolated A is reported WITH its error bar — no
over-claiming.

Usage:
  python3 folio-assistant/computations/qbeta/qbeta_residue_a_precision_ceiling.py
Emits: qbeta-residue-a-precision-ceiling.witness.json
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import json  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent


def load_u_subst(dps: int) -> mp.mpf:
    """u_subst = b · ℏ_q² from the canonical N=3 operator witness."""
    mp.mp.dps = dps
    src = HERE.parent / "q-beta-operator-valued-N3.witness.json"
    with src.open() as f:
        d = json.load(f)["data"]
    b = mp.mpf(str(d["hoefsmit_b"]))
    hbar_q_sq = mp.mpf(str(d["hbar_q_sq"]))
    return b * hbar_q_sq


def load_ck(dps: int) -> dict[int, mp.mpf]:
    """c_2..c_10 from the SDP-extended witness (c_k_extracted_50dps)."""
    mp.mp.dps = dps
    src = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    if not src.exists():
        src = HERE.parent / "qbeta-decay-sdp-extended-ck.witness.json"
    with src.open() as f:
        raw = json.load(f)["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mp.mpf(str(v)) for k, v in raw.items()}


def x_sequence(c_k: dict[int, mp.mpf], u: mp.mpf) -> dict[int, mp.mpf]:
    """x_k = c_k · u^k."""
    return {k: c_k[k] * u ** k for k in sorted(c_k)}


def aitken(x0: mp.mpf, x1: mp.mpf, x2: mp.mpf) -> mp.mpf | None:
    """Aitken Δ²: accelerated limit of x0, x1, x2."""
    d2 = (x2 - x1) - (x1 - x0)
    if d2 == 0:
        return None
    return x0 - (x1 - x0) ** 2 / d2


def geometric_3pt(x0: mp.mpf, x1: mp.mpf, x2: mp.mpf) -> tuple:
    """Solve x_k = A + B·ρ^k from three consecutive points.

    ρ = (x2−x1)/(x1−x0); A = x0 − (x1−x0)/(ρ−1).
    Returns (A, rho) or (None, None) if degenerate.
    """
    d1 = x1 - x0
    d2 = x2 - x1
    if d1 == 0:
        return None, None
    rho = d2 / d1
    if rho == 1:
        return None, None
    A = x0 - d1 / (rho - 1)
    return A, rho


def main() -> int:
    print("=" * 78)
    print("Q_β residue-A precision ceiling — how many digits of A are real?")
    print("=" * 78)

    # 1. Confirm the tail spread is intrinsic (stable as compute dps rises).
    print("\n--- 1. Is the spread intrinsic (asymptotic) or compute noise? ---")
    spreads = {}
    for dps in (50, 80, 120):
        u = load_u_subst(dps)
        c_k = load_ck(dps)
        x = x_sequence(c_k, u)
        tail = [x[k] for k in (8, 9, 10)]
        m = sum(tail) / 3
        spread = max(abs(t - m) / abs(m) for t in tail)
        spreads[dps] = spread
        print(f"  dps={dps:>3}: tail_mean={mp.nstr(m, 14)}  "
              f"rel_spread={mp.nstr(spread, 8)}")
    spread_stable = abs(spreads[120] - spreads[50]) / spreads[50] < mp.mpf("1e-6")
    print(f"  → spread stable across dps: {spread_stable}  ⇒ the spread is "
          f"{'INTRINSIC (asymptotic), not compute noise' if spread_stable else 'compute-sensitive'}.")

    # Work at 120 dps from here.
    mp.mp.dps = 120
    u = load_u_subst(120)
    c_k = load_ck(120)
    x = x_sequence(c_k, u)

    print("\n--- 2. The x_k = c_k·u^k tail (120 dps) ---")
    for k in sorted(x):
        if k >= 4:
            print(f"  x_{k:>2} = {mp.nstr(x[k], 18)}")

    # 3. Extrapolation estimators of the k→∞ limit L = lim c_k·u^k.
    # NB: the residue is A = u_subst · L (the canonical "1.804e-15"); L
    # is the tail limit (≈ 2.118e-13). u_subst is exact, so A and L have
    # IDENTICAL relative precision — achievable_digits applies to both.
    print("\n--- 3. Extrapolation estimators of L = lim_k c_k·u^k ---")
    estimators: dict[str, mp.mpf] = {}

    raw_mean = sum(x[k] for k in (8, 9, 10)) / 3
    estimators["raw_mean_8_9_10"] = raw_mean

    a_high = aitken(x[8], x[9], x[10])
    if a_high is not None:
        estimators["aitken_8_9_10"] = a_high
    a_low = aitken(x[7], x[8], x[9])
    if a_low is not None:
        estimators["aitken_7_8_9"] = a_low

    L_geo, rho = geometric_3pt(x[8], x[9], x[10])
    if L_geo is not None:
        estimators["geometric_8_9_10"] = L_geo

    for name, val in estimators.items():
        print(f"  {name:22s} = {mp.nstr(val, 18)}")
    if rho is not None:
        print(f"  (geometric ρ = {mp.nstr(rho, 8)}  "
              f"⇒ {'clean single-geometric' if abs(rho) < 1 and rho > 0 else 'NON-clean (ρ≤0 or |ρ|≥1): 3-pt fit unreliable'})")

    # 4. Honest error bar = spread across estimators.
    print("\n--- 4. Honest error bar = spread across estimators ---")
    vals = list(estimators.values())
    L_best = estimators.get("geometric_8_9_10", raw_mean)
    A_residue = u * L_best          # canonical residue A = u_subst · L
    est_spread = max(abs(v - L_best) / abs(L_best) for v in vals)
    achievable_digits = -mp.log10(est_spread) if est_spread > 0 else mp.mpf(99)
    print(f"  L_best (geometric)   = {mp.nstr(L_best, 18)}")
    print(f"  A_residue = u·L      = {mp.nstr(A_residue, 18)}  (canonical ≈1.804e-15)")
    print(f"  estimator spread     = {mp.nstr(est_spread, 6)} (relative; same for A and L)")
    print(f"  ACHIEVABLE DIGITS    ≈ {mp.nstr(achievable_digits, 4)}")
    print()

    reaches_30 = achievable_digits >= 30
    reaches_15 = achievable_digits >= 15
    print("=" * 78)
    print(f"VERDICT: A (= u_subst·L) and L are reliable to ≈ "
          f"{mp.nstr(achievable_digits, 3)} sig digits from canonical c_2..c_10.")
    print(f"  ≥30 digits (period-search grade)?  {reaches_30}")
    print(f"  ≥15 digits (12-const PSLQ grade)?  {reaches_15}")
    if not reaches_15:
        print("  The 3-rung extrapolation does NOT reach even 15 digits — the")
        print("  estimators disagree beyond that, and ρ is non-clean. The")
        print("  precision ceiling is set by having only k=8,9,10 in the")
        print("  asymptote, NOT by arithmetic precision (50-dps c_k).")
        print()
        print("  GENUINE UNBLOCK PATH: a higher-order CANONICAL extraction of")
        print("  c_11..c_15 (proved/near-match closed forms per rung, like the")
        print("  c_2..c_10 ladder) — a separate research program, NOT an ansatz")
        print("  fit. With ~6 more rungs the asymptote tightens geometrically")
        print("  and Richardson/Aitken can then reach the period-search grade.")
    print()

    # ─── Witness ──────────────────────────────────────────────────────
    w = WitnessBuilder("qbeta-residue-a-precision-ceiling", engine="mpmath")
    w.set_description(
        f"Precision-ceiling analysis of residue A = lim_k c_k·u_subst^k "
        f"(PR #1727 Step 1). A is the asymptotic limit sampled at k=8,9,10 "
        f"(spread {mp.nstr(spreads[120], 4)}); the c_k are 50 dps so the "
        f"limiter is asymptotic convergence, NOT arithmetic precision "
        f"(spread stable across dps={spread_stable}). Extrapolation "
        f"(raw mean, Aitken Δ², 3-pt geometric) gives L ≈ {mp.nstr(L_best, 14)} "
        f"(residue A = u_subst·L ≈ {mp.nstr(A_residue, 8)}) "
        f"reliable to ≈ {mp.nstr(achievable_digits, 3)} sig figs (estimator "
        f"spread {mp.nstr(est_spread, 4)}). ≥30 digits: {reaches_30}; ≥15: "
        f"{reaches_15}. Genuine unblock = canonical c_11..c_15 extraction "
        f"(NOT an ansatz fit). Diagnostic-only."
    )
    w.add_data("u_subst", mp.nstr(u, 40))
    w.add_data("x_tail", {f"x_{k}": mp.nstr(x[k], 30) for k in (7, 8, 9, 10)})
    w.add_data("spread_vs_dps", {str(k): mp.nstr(v, 8) for k, v in spreads.items()})
    w.add_data("spread_intrinsic", str(bool(spread_stable)))
    w.add_data("estimators", {k: mp.nstr(v, 24) for k, v in estimators.items()})
    w.add_data("geometric_rho", mp.nstr(rho, 10) if rho is not None else "degenerate")
    w.add_data("L_limit_best", mp.nstr(L_best, 24))
    w.add_data("A_residue_best", mp.nstr(A_residue, 24))
    w.add_data("note_A_vs_L",
               "L = lim c_k·u^k ≈ 2.118e-13 (tail limit); residue A = "
               "u_subst·L ≈ 1.804e-15 (canonical). u_subst exact ⇒ A and L "
               "share the same relative precision / achievable_digits.")
    w.add_data("estimator_spread_relative", mp.nstr(est_spread, 8))
    w.add_data("achievable_digits", mp.nstr(achievable_digits, 6))
    w.add_data("reaches_30_digits", str(bool(reaches_30)))
    w.add_data("reaches_15_digits", str(bool(reaches_15)))
    w.add_data("genuine_unblock_path",
               "Canonical (proved/near-match) extraction of c_11..c_15, "
               "extending the c_2..c_10 ladder — NOT an ansatz fit. With more "
               "rungs the asymptote tightens and extrapolation reaches grade.")
    w.add_assertion(
        name="A_reaches_30_digits_from_current_ck",
        computed=bool(reaches_30),
        expected=False, tolerance=0,
        source="A is the k→∞ limit of c_k·u^k sampled at k=8,9,10 only. "
               "Default expectation: 3 canonical rungs cannot pin A to 30 "
               "digits; the limiter is asymptotic convergence, not precision.",
    )
    w.add_assertion(
        name="spread_is_intrinsic_not_compute_noise",
        computed=bool(spread_stable),
        expected=True, tolerance=0,
        source="Tail spread stable as compute dps rises 50→120 ⇒ intrinsic "
               "asymptotic spread, confirming compute precision is not the "
               "limiter.",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
