#!/usr/bin/env python3
"""
H₂O angle — GB-truncation INVERSE probe (owner: "explore the exact
GB-truncation fraction that lands on 104.5°").

The bracketing result (`h2o_angle_activeset_gb.py`): the leading weighting
gives 107.19°, the full L₊ quadratic on the lone gives 98.99° — observed
104.5° sits between. The open non-fitted question is whether the truncation
fraction that interpolates to 104.5° is a DERIVED constant of the framework
(a q-integer weight, a Markov weight, a Wedderburn weight) rather than a fit.

THE PROBE (inverse problem — solve, then COMPARE, never wire):
  Model:  w_H = tr_M(σ) = z,   w_L(f) = tr_M(e⁻) + f · tr_M(L₊)
                               = (h z² + z) + f · z² .
  1. Solve θ_VSEPR(f*) = 104.5° for f* by bisection (and the equivalent
     direct ratio r* = w_L/w_H with θ(r*) = 104.5°).
  2. Compare f* (and r*) against a battery of DERIVED candidates —
     q-integers ([2]_q, [3]_q and inverses), Markov data (z, z², h, hz),
     Wedderburn weights (W_SYM, W_STD), simple rationals (1/2, 1/3 — the
     benzene ½-shared-pair precedent) — and report % deviation, tiered:
     |dev| < 0.1% exact-class; < 1% near-match; < 5% weak; else no-match.
  3. Forward-evaluate the top structural candidates and report their angles.

DISCIPLINE. This is an inverse PROBE, not a wiring: nothing here feeds any
production weight. A near-match is reported as a tiered observation (per the
c_k tiered convention) for the selection question "which GB truncation order
is physically correct"; wiring would need a derivation of WHY that fraction
(e.g. the L₊ pair shared between the two lone-pair domains ⇒ ½, or a
[3]_q⁻¹ quantum-dimension normalisation), plus cross-anchor stability.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE),
           str(_HERE.parents[1] / "tools" / "pyhecke" / "python"),
           str(_HERE.parents[1] / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder
from pyhecke.gram import z, nf_tr, nf_of_word, W_SYM, W_STD
from q_parameter import Q as q0, Q_INV as qi, HA as h

THETA0 = 109.4712
THETA_OBS = 104.5


def vsepr_angle(wH, wL, theta0: float, n: float = 1.0) -> float:
    def E(x):
        th, ph = x
        sH, cH = np.sin(th / 2), np.cos(th / 2)
        sL, cL = np.sin(ph / 2), np.cos(ph / 2)
        dHH, dLL = 2 * sH, 2 * sL
        dHL = np.sqrt(sH ** 2 + sL ** 2 + (cH + cL) ** 2)
        if min(dHH, dLL, dHL) < 1e-6:
            return 1e9
        return wH * wH / dHH ** n + wL * wL / dLL ** n + 4 * wH * wL / dHL ** n
    r = minimize(E, [np.radians(theta0), np.radians(theta0)],
                 method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-13})
    return float(np.degrees(r.x[0]))


def _bisect(fun, lo, hi, target, tol=1e-7, iters=80):
    flo, fhi = fun(lo) - target, fun(hi) - target
    if flo * fhi > 0:
        raise SystemExit("bisection bracket failure")
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        fm = fun(mid) - target
        if abs(fm) < tol:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def main() -> None:
    # Witness built up front so durationMs covers the compute (per review).
    w = WitnessBuilder("h2o-angle-gb-truncation-inverse", engine="python")
    w_sigma = float(nf_tr(nf_of_word((0,))))        # z
    w_eminus = float(nf_tr(nf_of_word((0, 1, 0))))  # h z² + z
    w_Lplus = float(nf_tr(nf_of_word((0, 1))))      # z²

    print("=" * 72)
    print("H₂O angle — GB-truncation INVERSE probe (compare, don't wire)")
    print("=" * 72)
    print(f"  q₀={q0:.10f}  z={z:.10f}  h={h:.10f}")

    # 1. inverse solves
    f_star = _bisect(
        lambda f: vsepr_angle(w_sigma, w_eminus + f * w_Lplus, THETA0),
        0.0, 1.0, THETA_OBS)
    r_star = (w_eminus + f_star * w_Lplus) / w_sigma
    r_star_direct = _bisect(
        lambda r: vsepr_angle(1.0, r, THETA0), 1.0, 2.0, THETA_OBS)
    print(f"\n  f* (fraction of L₊ on the lone) = {f_star:.6f}")
    print(f"  r* = w_L/w_H at 104.5°          = {r_star:.6f} "
          f"(direct: {r_star_direct:.6f})")

    # 2. derived-candidate batteries
    two_q = float(q0 + qi)            # [2]_q
    three_q = float(q0**2 + 1 + qi**2)  # [3]_q
    f_cands = {
        "1/3": 1/3, "1/2": 0.5, "z": float(z), "z^2": float(z)**2,
        "h": float(h), "h*z": float(h*z), "2*h*z": float(2*h*z),
        "1/[2]_q": 1/two_q, "1/[2]_q^2": 1/two_q**2,
        "1/[3]_q": 1/three_q, "2/[3]_q": 2/three_q,
        "W_SYM": float(W_SYM), "W_STD": float(W_STD),
        "h*[2]_q": float(h)*two_q, "q-1": float(q0)-1,
        "(q-1)*2": 2*(float(q0)-1), "1-z": 1-float(z),
    }
    r_cands = {
        "1+h*z (leading)": 1+float(h*z), "1+h": 1+float(h),
        "q": float(q0), "q^2": float(q0)**2,
        "1+2hz": 1+2*float(h*z), "(1+hz)^2": (1+float(h*z))**2,
        "1+hz+z^2": 1+float(h*z)+float(z)**2,
        "1+hz+z^3": 1+float(h*z)+float(z)**3,
        "[3]_q/[2]_q": three_q/two_q,
        "[2]_q^2/[3]_q": two_q**2/three_q,
        "(q^2+1)/[2]_q": (float(q0)**2+1)/two_q,
        "1+z/2": 1+float(z)/2, "1+h+h*z^2": 1+float(h)+float(h)*float(z)**2,
        "sqrt(q)": float(q0)**0.5,
    }

    def tier(dev):
        a = abs(dev)
        return ("EXACT-class" if a < 0.1 else
                "near-match" if a < 1.0 else
                "weak" if a < 5.0 else "no")

    def battery(name, val, cands):
        print(f"\n  {name} = {val:.6f} — derived-candidate battery:")
        rows = []
        for label, c in sorted(cands.items(), key=lambda kv: abs(kv[1]-val)):
            dev = 100*(c-val)/val
            rows.append({"candidate": label, "value": float(c),
                         "deviation_pct": float(dev), "tier": tier(dev)})
        for rrow in rows[:6]:
            print(f"    {rrow['candidate']:<28}{rrow['value']:>10.6f}"
                  f"{rrow['deviation_pct']:>+9.3f}%   {rrow['tier']}")
        return rows

    f_rows = battery("f*", f_star, f_cands)
    r_rows = battery("r*", r_star, r_cands)

    # 3. forward-evaluate top structural candidates
    print(f"\n  forward check (top candidates → angle):")
    fwd = {}
    for label, c in [("f=1/3", 1/3), ("f=1/[3]_q", 1/three_q),
                     ("f=z^2", float(z)**2), ("f=h", float(h)),
                     ("f=1/2", 0.5)]:
        th = vsepr_angle(w_sigma, w_eminus + c * w_Lplus, THETA0)
        fwd[label] = {"fraction": float(c), "theta_deg": th,
                      "miss_deg": th - THETA_OBS}
        print(f"    {label:<12} f={c:.6f} → θ = {th:8.3f}°  "
              f"(miss {th-THETA_OBS:+.3f}°)")

    # 4. kernel-robustness scan — the tiering gate for the r* candidates
    q2 = float(q0) ** 2
    one_zhalf = 1 + float(z) / 2
    print(f"\n  kernel-robustness of r* (tiering gate; n=1 Coulomb is the "
          f"physical kernel):")
    kern = {}
    for n_k in (1.0, 2.0, 3.0, 6.0):
        rs = _bisect(lambda r: vsepr_angle(1.0, r, THETA0, n_k),
                     1.0, 4.0, THETA_OBS)
        kern[f"n={n_k:g}"] = {
            "r_star": rs,
            "dev_q2_pct": float(100 * (q2 - rs) / rs),
            "dev_1_plus_z_half_pct": float(100 * (one_zhalf - rs) / rs),
        }
        print(f"    n={n_k:<4g} r*={rs:.6f}  dev(q²)={100*(q2-rs)/rs:+.3f}%  "
              f"dev(1+z/2)={100*(one_zhalf-rs)/rs:+.3f}%")
    print("    → both candidates are near-matches ONLY at the Coulomb kernel "
          "(n=1); kernel-conditional.")

    best_f = f_rows[0]
    w.set_description(
        "Inverse probe for the GB-truncation fraction in the H₂O angle "
        "(owner: explore the exact fraction landing on 104.5°). Solves "
        "θ_VSEPR(f*)=104.5° for the fraction f* of the L₊ quadratic on the "
        "lone-pair weight (w_L = tr_M(e⁻)+f·tr_M(L₊), w_H=tr_M(σ)) and the "
        "equivalent ratio r*, then compares both against derived q-integer / "
        "Markov / Wedderburn candidates with tiered deviations. COMPARISON "
        "ONLY — nothing wired; a near-match is a selection hypothesis "
        "requiring a derivation + cross-anchor stability before any wiring."
    )
    w.set_content_block("prop:h2o-bond-angle-shift")
    w.add_parameter("q", float(q0))
    w.add_parameter("z", float(z))
    w.add_parameter("h", float(h))
    w.add_data("theta_observed_deg", THETA_OBS)
    w.add_data("f_star", f_star)
    w.add_data("r_star", r_star)
    w.add_data("r_star_direct", r_star_direct)
    w.add_data("f_candidates_ranked", f_rows)
    w.add_data("r_candidates_ranked", r_rows)
    w.add_data("forward_checks", fwd)
    w.add_data("kernel_robustness_scan", kern)
    w.add_data("best_f_candidate", best_f)
    w.add_assertion(
        "inverse solve reproduces the observed angle",
        computed=bool(abs(vsepr_angle(
            w_sigma, w_eminus + f_star * w_Lplus, THETA0) - THETA_OBS) < 1e-3),
        expected=True,
        source="bisection on the VSEPR minimiser",
    )
    w.add_data(
        "finding",
        f"f* = {f_star:.6f} (fraction of the L₊ quadratic on the lone pair "
        f"that lands exactly on 104.5°); best derived candidate: "
        f"{best_f['candidate']} = {best_f['value']:.6f} "
        f"({best_f['deviation_pct']:+.3f}%, {best_f['tier']}). r* = "
        f"{r_star:.6f}. Tiered comparison only — no wiring; promoting a "
        "candidate requires a structural derivation (e.g. sharing of the L₊ "
        "pair between domains, or a quantum-dimension normalisation) plus "
        "stability checks. KERNEL SCAN (demotion): the q² and 1+z/2 "
        "near-matches hold ONLY at the Coulomb kernel (n=1; at n=2/3/6 r* "
        "drifts to ≈1.28/1.32/1.45) — kernel-conditional near-matches. "
        "Coulomb is the physically canonical kernel for charged-domain "
        "repulsion, but the identification inherits that assumption.",
    )
    w.save()
    print("\nDone. Witness saved (h2o-angle-gb-truncation-inverse).")


if __name__ == "__main__":
    main()
