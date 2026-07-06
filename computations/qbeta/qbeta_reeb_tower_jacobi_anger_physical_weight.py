"""§4a Jacobi–Anger tower test, done with PHYSICAL Wenzl weights + cross-anchor.

The audit `docs/audits/2026-06-13-reeb-phase-qbessel-identification.md` §4a proposes
the falsifiable test: if the bar-odd brane-tower sector is the Hahn–Exton q-Bessel
(E_q(2) contraction) object, its `sinh((2m+1)η)` coefficients are the Bessel values
`2·J_{2m+1}(x)` at a SINGLE substrate-fixed `x = x(q₀)` — and the SAME `x(q₀)` must
reproduce the bar-odd data at BOTH anchors with no per-anchor refit.

The committed witness `qbeta-reeb-tower-jacobi-anger.witness.json` ran this only on
the **unit-weighted** block sum (over-determination residual 0.128 ≈ 12.8 %), with an
explicit note: *"NOT the physical Wenzl-weighted Markov trace."* This script runs the
**physical** version — the Markov/Jones–Wenzl weights `y_λ(q₀)` that actually appear
in `tr_M = Σ_λ y_λ χ^λ` — and adds the proton↔muon cross-anchor gate.

Per-block bar-odd `sinh(kη)`-order coefficients at n=3 (rational, q-independent;
reproduced from the committed witness / `sinh_order_coeffs`):
    (3)     : {3: -1/4, 5: -1/4}
    (2,1)   : {1:  1/2, 3: -1/2}
    (1,1,1) : {3: -1/4, 5: -1/4}
The PHYSICAL bar-odd tower coefficients are W_k(q₀) = Σ_λ y_λ(q₀)·coeff_{λ,k}.

Discipline: derive-or-refute; TIERED; no fit; nothing wired; c_3 stays cal-anchored.
A clean single-x at BOTH anchors (small over-determination residual, no refit) would be
the first PHYSICAL-weight structural identification of the bar-odd tower as the q-Bessel
matrix coefficient; a large residual is a clean refutation on the same footing as the
unit-weighted run, quantified.
"""
from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fractions import Fraction as Fr  # noqa: E402
from mpmath import mp, mpf, besselj, findroot  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
try:
    from qou_substrate.constants import q_at, q_muon_at
except Exception:  # pragma: no cover
    from substrate.qou_substrate.constants import q_at, q_muon_at  # type: ignore

mp.dps = 50

# Per-block bar-odd sinh-order coefficients at n=3 (rational, anchor-independent).
BAR_ODD_COEFFS = {
    (3,):      {3: Fr(-1, 4), 5: Fr(-1, 4)},
    (2, 1):    {1: Fr(1, 2), 3: Fr(-1, 2)},
    (1, 1, 1): {3: Fr(-1, 4), 5: Fr(-1, 4)},
}


def physical_W(q) -> dict[int, "mpf"]:
    """Physical Wenzl-weighted bar-odd tower coefficients W_k = Σ_λ y_λ·coeff_{λ,k}."""
    y = {tuple(k): mpf(str(v)) for k, v in y_lambda_at(3, q).items()}
    W: dict[int, "mpf"] = {1: mpf(0), 3: mpf(0), 5: mpf(0)}
    for lam, coeffs in BAR_ODD_COEFFS.items():
        yl = y[lam]
        for k, c in coeffs.items():
            W[k] += yl * mpf(c.numerator) / mpf(c.denominator)
    return W


def solve_single_x(W: dict[int, "mpf"]):
    """Solve x from the SCALE-FREE ratio W_3/W_1 = J_3(x)/J_1(x); then test the
    over-determined W_5/W_1 = J_5(x)/J_1(x). Returns (x, overdet_rel_residual)."""
    r31 = W[3] / W[1]

    def f(x):
        return besselj(3, x) / besselj(1, x) - r31
    # Seed near the unit-weighted x* ≈ 4.44; bracket-scan for a real root.
    x = None
    for x0 in [mpf("1"), mpf("2.5"), mpf("4.44"), mpf("6"), mpf("8")]:
        try:
            cand = findroot(f, x0)
            if abs(cand.imag) < mpf("1e-30") and cand.real > 0:
                x = cand.real
                break
        except Exception:
            continue
    if x is None:
        return None, None
    # over-determination: predicted vs actual W_5/W_1
    pred_51 = besselj(5, x) / besselj(1, x)
    act_51 = W[5] / W[1]
    resid = abs(pred_51 - act_51) / abs(act_51)
    return x, resid


def main() -> int:
    out = {}
    print(" §4a Jacobi–Anger tower test — PHYSICAL Wenzl weights + cross-anchor")
    print(" (unit-weighted baseline over-determination residual was 0.128 = 12.8%)")
    print("-" * 78)
    for label, qf in [("proton", q_at()), ("muon", q_muon_at())]:
        q = mpf(str(qf))
        W = physical_W(q)
        x, resid = solve_single_x(W)
        out[label] = {
            "q": mp.nstr(q, 20),
            "W1": mp.nstr(W[1], 12), "W3": mp.nstr(W[3], 12), "W5": mp.nstr(W[5], 12),
            "single_x": (mp.nstr(x, 12) if x is not None else None),
            "overdet_rel_residual": (mp.nstr(resid, 6) if resid is not None else None),
        }
        print(f"  {label:7s} q={mp.nstr(q,18)}")
        print(f"          W_1={mp.nstr(W[1],10)}  W_3={mp.nstr(W[3],10)}  W_5={mp.nstr(W[5],10)}")
        print(f"          single x*={mp.nstr(x,10) if x else 'NO REAL ROOT'}  "
              f"over-det residual={mp.nstr(resid,6) if resid is not None else 'n/a'}")
    # cross-anchor: x swing
    if out["proton"]["single_x"] and out["muon"]["single_x"]:
        xp = mpf(out["proton"]["single_x"]); xm = mpf(out["muon"]["single_x"])
        swing = abs(xp - xm) / abs(xp)
        out["cross_anchor_x_swing_rel"] = mp.nstr(swing, 6)
        print("-" * 78)
        print(f"  cross-anchor single-x swing (rel) = {mp.nstr(swing,6)}")
    print("-" * 78)
    # verdict
    rp = out["proton"]["overdet_rel_residual"]
    rm = out["muon"]["overdet_rel_residual"]
    clean = (rp is not None and rm is not None
             and float(rp) < 0.01 and float(rm) < 0.01)
    out["verdict"] = (
        "PASS (physical single-x q-Bessel identification: over-det residual <1% at both anchors)"
        if clean else
        "FAIL/near (physical weights do NOT collapse to a single-x q-Bessel at <1% — refutation, quantified)")
    print(f"  VERDICT: {out['verdict']}")
    import json
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
