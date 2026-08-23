#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output across counterfactual q.
"""
Two-quark binding LP — active-set + Mahler-height sweep across metallic ratios.

Setup: n=2 strand count (smallest non-trivial Hecke), basis {γ, σ_0} of
H_2(q).  Two Wedderburn blocks (2) and (1,1), both 1-dim.  Closed-form
Markov traces:

    t_1 = tr_M(γ)   = 2 (q + q⁻¹)
    t_2 = tr_M(σ_0) = q² − q⁻²

Frobenius Gram:
    G_11 = 2 (q + q⁻¹)
    G_12 = G_21 = q² − q⁻²
    G_22 = (q + q⁻¹)(q² + q⁻²)

LP: minimise t_1 x_1 + t_2 x_2  s.t.
    x_1 + x_2 = n_target,
    G_11 x_1 + G_12 x_2 ≥ 0   (Frobenius row 1)
    G_21 x_1 + G_22 x_2 ≥ 0   (Frobenius row 2)
    x_i ≥ −M

The active set 𝒜 = {i : Frobenius row i is tight at optimum}.

At each q in the sweep:
  1. Solve the LP.  Report x*, y*, active set.
  2. Compute the "Mahler-height proxy" for each Markov trace.  We use
     the simplest height proxy: at fixed precision 10⁻¹², find the
     best rational approximation p/q to the value, and report
     log(p+q).  At metallic q = δ_n, the value q − q⁻¹ = n is
     integer ⇒ proxy = log(n+1) (low).  At generic q the proxy is
     much higher.

If the active set CHANGES at metallic ratios (boundary jumps), the
sharpened (M2) conjecture is empirically confirmed at the LP-vertex
level.  Otherwise the metallic structure stays purely algebraic and
doesn't reach the LP combinatorial output.

Output: PNG + witness JSON.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from scipy.optimize import linprog
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).parent


def delta_n(n: int) -> mp.mpf:
    return (mp.mpf(n) + mp.sqrt(n * n + 4)) / 2


PHI = delta_n(1)
DELTA_SILVER = delta_n(2)
DELTA_BRONZE = delta_n(3)
Q0 = mp.mpf("1.1099785955541805")


# ── Markov-trace and Gram closed forms at n=2 ──────────────────────────


def t1(q: mp.mpf) -> mp.mpf:
    """tr_M(γ) = 2 (q + q⁻¹)."""
    return 2 * (q + 1 / q)


def t2(q: mp.mpf) -> mp.mpf:
    """tr_M(σ_0) = q² − q⁻²."""
    return q * q - 1 / (q * q)


def G_matrix(q: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return (G_11, G_12, G_22) closed forms."""
    G11 = 2 * (q + 1 / q)
    G12 = q * q - 1 / (q * q)
    G22 = (q + 1 / q) * (q * q + 1 / (q * q))
    return G11, G12, G22


# ── LP solver ──────────────────────────────────────────────────────────


def solve_lp(q: mp.mpf, n_target: float = 1.0, M: float = 1e6) -> dict:
    """Solve the 2-quark binding LP at parameter q.

    Returns dict with x*, dual y*, active set indicator, optimal value.
    """
    tt1 = float(t1(q))
    tt2 = float(t2(q))
    G11, G12, G22 = (float(x) for x in G_matrix(q))

    # scipy.linprog uses min c^T x with A_ub x ≤ b_ub, A_eq x = b_eq.
    c = np.array([tt1, tt2], dtype=float)
    # Frobenius positivity: Gx ≥ 0 → -Gx ≤ 0.
    A_ub = np.array([
        [-G11, -G12],
        [-G12, -G22],
    ], dtype=float)
    b_ub = np.array([0.0, 0.0], dtype=float)
    A_eq = np.array([[1.0, 1.0]], dtype=float)
    b_eq = np.array([n_target], dtype=float)
    bounds = [(-M, None), (-M, None)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")

    if not res.success:
        return {
            "status": f"failed: {res.message}",
            "q": str(q),
        }

    x_star = res.x.tolist()
    # Dual variables — extract from scipy's output.
    # res.eqlin.marginals = y_0 for the equality (net) constraint
    # res.ineqlin.marginals = -y_i for the inequalities (negative because A_ub x ≤ b_ub means dual ≤ 0)
    y_0 = float(res.eqlin.marginals[0]) if res.eqlin.marginals is not None else 0.0
    y_ineq = -np.array(res.ineqlin.marginals) if res.ineqlin.marginals is not None else np.zeros(2)
    y_star = y_ineq.tolist()  # shadow prices of Frobenius positivity

    # Active set: indices i with y_i > tol.
    tol = 1e-7
    active_set = [i for i, y in enumerate(y_star) if abs(y) > tol]

    return {
        "status": "optimal",
        "x_star": x_star,
        "y0_star": y_0,
        "y_star": y_star,
        "active_set": active_set,
        "primal_obj": float(c @ res.x),
        "dual_obj": float(n_target * y_0),
        "duality_gap": float(c @ res.x - n_target * y_0),
        "Frobenius_slack": [
            float(G11 * x_star[0] + G12 * x_star[1]),
            float(G12 * x_star[0] + G22 * x_star[1]),
        ],
    }


# ── Mahler-height proxy ─────────────────────────────────────────────────


def best_rational_approx(v: float, denom_limit: int = 10**6) -> Fraction:
    """Continued-fraction-based best rational approximation."""
    return Fraction(v).limit_denominator(denom_limit)


def mahler_height_proxy(v: float, denom_limit: int = 10**6) -> float:
    """log(numerator + denominator) of best rational approx — drops to
    log(n+1) at integer v=n."""
    if not math.isfinite(v):
        return float("nan")
    f = best_rational_approx(v, denom_limit)
    p = abs(f.numerator)
    qd = abs(f.denominator)
    return math.log(p + qd)


# ── Sweep ───────────────────────────────────────────────────────────────


def linspace(a: mp.mpf, b: mp.mpf, k: int) -> list[mp.mpf]:
    return [a + (b - a) * i / (k - 1) for i in range(k)]


def build_sweep() -> list[mp.mpf]:
    eps = mp.mpf("0.005")
    return (
        linspace(Q0 + eps, PHI - eps, 30)
        + [PHI]
        + linspace(PHI + eps, DELTA_SILVER - eps, 30)
        + [DELTA_SILVER]
        + linspace(DELTA_SILVER + eps, DELTA_BRONZE - eps, 20)
        + [DELTA_BRONZE]
    )


def main() -> None:
    print("Two-quark LP active-set + Mahler-height sweep…", file=sys.stderr)

    qs = build_sweep()
    qs_float = [float(q) for q in qs]

    primal_vals: list[float] = []
    active_sets: list[list[int]] = []
    y_star_1: list[float] = []
    y_star_2: list[float] = []
    y_0_star: list[float] = []
    x_star_1: list[float] = []
    x_star_2: list[float] = []
    height_t1: list[float] = []
    height_t2: list[float] = []
    height_q_minus_qinv: list[float] = []
    height_chi_3: list[float] = []  # for χ^(3)(σ) = q itself

    for q in qs:
        lp = solve_lp(q, n_target=1.0)
        primal_vals.append(lp.get("primal_obj", float("nan")))
        active_sets.append(lp.get("active_set", []))
        y_star_1.append(lp.get("y_star", [0, 0])[0])
        y_star_2.append(lp.get("y_star", [0, 0])[1])
        y_0_star.append(lp.get("y0_star", 0.0))
        x_star_1.append(lp.get("x_star", [0, 0])[0])
        x_star_2.append(lp.get("x_star", [0, 0])[1])

        height_t1.append(mahler_height_proxy(float(t1(q))))
        height_t2.append(mahler_height_proxy(float(t2(q))))
        height_q_minus_qinv.append(mahler_height_proxy(float(q - 1 / q)))
        height_chi_3.append(mahler_height_proxy(float(q)))

    # Active-set transitions: where does it change between consecutive qs?
    transitions: list[dict] = []
    for i in range(1, len(qs)):
        if active_sets[i] != active_sets[i - 1]:
            transitions.append({
                "q_below": str(qs[i - 1]),
                "q_above": str(qs[i]),
                "set_below": active_sets[i - 1],
                "set_above": active_sets[i],
            })

    # ── 3-panel plot ────────────────────────────────────────────────────
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    # Panel 1: LP optimum coefficients + dual shadow prices
    ax = axes[0]
    ax.plot(qs_float, x_star_1, "tab:blue", lw=1.5,
            label=r"$x_1^*$ (coeff of $\gamma$)")
    ax.plot(qs_float, x_star_2, "tab:orange", lw=1.5,
            label=r"$x_2^*$ (coeff of $\sigma_0$)")
    ax.plot(qs_float, y_0_star, "k--", lw=1.0,
            label=r"$y_0^*$ (net shadow price)")
    ax.axhline(0, color="gray", lw=0.5)
    ax.set_ylabel("LP primal / dual values")
    ax.set_title(r"Two-quark LP: $\min t_1 x_1 + t_2 x_2$ s.t. $x_1+x_2=1$, $Gx \geq 0$")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2: Frobenius shadow prices (y_1, y_2) — active set indicator
    ax = axes[1]
    ax.plot(qs_float, y_star_1, "tab:green", lw=1.7,
            label=r"$y_1^*$ (Frobenius row 1 shadow)")
    ax.plot(qs_float, y_star_2, "tab:red", lw=1.7,
            label=r"$y_2^*$ (Frobenius row 2 shadow)")
    ax.axhline(0, color="gray", lw=0.5)
    ax.set_ylabel(r"shadow price $y_i^*$  ($> 0 \Leftrightarrow$ active)")
    ax.set_title(r"Active set $\mathcal{A} = \{i : y_i^* > 0\}$ — does it change at metallic ratios?")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 3: Mahler-height proxy = log(p+q) of best rational approx
    ax = axes[2]
    ax.plot(qs_float, height_q_minus_qinv, "tab:purple", lw=1.6,
            label=r"$h(q - q^{-1}) = \log(p+q_{\rm denom})$")
    ax.plot(qs_float, height_chi_3, "tab:cyan", lw=1.2,
            label=r"$h(q) = h(\chi^{(3)}(\sigma))$")
    ax.plot(qs_float, height_t1, "tab:blue", lw=1.0, alpha=0.6,
            label=r"$h(t_1)$")
    ax.plot(qs_float, height_t2, "tab:orange", lw=1.0, alpha=0.6,
            label=r"$h(t_2)$")
    ax.set_yscale("log")
    ax.set_ylabel(r"Mahler-height proxy: $\log(p+q_{\rm denom})$")
    ax.set_xlabel(r"$q$ (real, $\mathrm{Im}(q) = 0$)")
    ax.set_title(r"Diophantine height of Markov traces — DROPS at metallic ratios (Pisot signature)")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(alpha=0.3)

    # Mark metallic anchors on all panels
    for ax in axes:
        for q_special, name, color in [
            (Q0, r"$q_0$", "tab:red"),
            (PHI, r"$\varphi$", "goldenrod"),
            (DELTA_SILVER, r"$\delta_2$ silver", "silver"),
            (DELTA_BRONZE, r"$\delta_3$ bronze", "peru"),
        ]:
            ax.axvline(float(q_special), color=color, lw=1.2, ls=":", alpha=0.7)

    plt.tight_layout()
    out_png = HERE / "two-quark-active-set-mahler-sweep.png"
    fig.savefig(out_png, dpi=140, bbox_inches="tight")
    print(f"Saved plot: {out_png}", file=sys.stderr)

    witness = {
        "description": (
            "Two-quark binding LP at strand count n=2.  Closed-form "
            "Markov-trace cost t(q) and Frobenius Gram G(q) over basis "
            "{γ, σ_0} of H_2(q).  Sweep q across metallic intervals "
            "[q_0, φ, δ_silver, δ_bronze].  At each q: solve LP, record "
            "active set 𝒜 = {i : y_i^* > 0} and Mahler-height proxy for "
            "the Markov traces.  Tests sharpened conjecture (M2)."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "anchors": {
            "q_0": str(Q0),
            "phi": str(PHI),
            "delta_silver": str(DELTA_SILVER),
            "delta_bronze": str(DELTA_BRONZE),
        },
        "n_q_points": len(qs),
        "closed_forms": {
            "t1_gamma":     "2 (q + q^{-1})",
            "t2_sigma_0":   "q^2 - q^{-2}",
            "G_11":         "2 (q + q^{-1})",
            "G_12":         "q^2 - q^{-2}",
            "G_22":         "(q + q^{-1})(q^2 + q^{-2})",
        },
        "active_set_transitions": transitions,
        "n_transitions": len(transitions),
        "verdict": (
            "If active_set_transitions is empty across the sweep, the "
            "active set is q-CONSTANT — metallic structure does not "
            "reach the LP combinatorial output at n=2.  If transitions "
            "exist AT metallic ratios, sharpened (M2) is confirmed at "
            "this level.  If transitions exist elsewhere, the LP-vertex "
            "structure is driven by character zeros (same pattern as the "
            "Jones / n=4 probes), not by metallic ratios."
        ),
        "limitations": [
            "n=2 has only 2 LP variables and 2 Frobenius constraints — "
            "the smallest non-trivial case.  Higher-n LPs (n=3 Borromean "
            "d=6) have richer active-set structure but require explicit "
            "Markov-trace + Gram tabulation.",
            "Mahler-height proxy uses `Fraction.limit_denominator(10^6)`. "
            "At metallic q the value (q - q⁻¹) IS an integer to machine "
            "precision so the proxy hits 0 floor; at generic q the proxy "
            "grows with denominator complexity.  Not a true Mahler "
            "measure, but tracks the right structural distinction.",
            "scipy.linprog uses HIGHS solver in double precision; for a "
            "true algebraic-integer LP at q = δ_n we'd need a symbolic "
            "solver (sympy or QSOpt-Ex).  This probe shows the floating-"
            "point shadow.",
        ],
    }
    out_json = HERE / "two-quark-active-set-mahler-sweep.witness.json"
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` — and a witness without one cannot be
    # compared against its producer, so it drops OUT of the self-staleness
    # audit and reads as "not stale" forever. Regenerating it then looks
    # like progress while removing it from the count: a false drain.
    # Full rationale and the detector: computations/witness_drain_audit.py.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched, so consumers
    # of legacy `assertions` records (which key on `label`, not `name`) do
    # not have to change. `engine` is passed back from the payload because
    # the helper overwrites it, and a descriptive engine string is worth
    # keeping.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", 'python+mpmath'))
    out_json.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Saved witness: {out_json}", file=sys.stderr)

    print(f"\nActive-set transitions found: {len(transitions)}")
    if transitions:
        for t in transitions[:10]:
            qb = float(t["q_below"])
            qa = float(t["q_above"])
            # Check if bracketing a metallic ratio
            brackets = []
            if qb <= float(PHI) <= qa:
                brackets.append("φ")
            if qb <= float(DELTA_SILVER) <= qa:
                brackets.append("δ_silver")
            if qb <= float(DELTA_BRONZE) <= qa:
                brackets.append("δ_bronze")
            tag = ", ".join(brackets) if brackets else "interior"
            print(f"  q ∈ [{qb:.6f}, {qa:.6f}]: "
                  f"{t['set_below']} → {t['set_above']}  [{tag}]")
    else:
        print("  (active set is constant across the entire sweep — "
              "metallic structure does NOT reach LP combinatorics at n=2)")


if __name__ == "__main__":
    main()
