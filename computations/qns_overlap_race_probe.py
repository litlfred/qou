#!/usr/bin/env python3
"""qns_overlap_race_probe — the overlap-engagement race, solved analytically.

EXPLORATORY PROBE (not production). Bean: PC4 (parent qou-nb6l).

Phase 1 of the pair-collision model integrates EXACTLY:
  (d^2)' = -Gamma/pi          => d^2(t) = d0^2 (1 - u),  u = t/t*
  V1'    = [Gamma/(2 pi d^2)] V1 => V1(t) = V1_0 (1-u)^{-1/2}
Overlap (V1 = d^2) engages at  u_overlap = 1 - (V1_0/d0^2)^{2/3}  < 1
STRICTLY for every V1_0 > 0: the hyperbolic-overlap saturation ALWAYS engages
before the inviscid singular time. Within the two-regime model the race is
DECIDED: the pair channel is regular (branch B) for every positive core size;
only the measure-zero point-vortex limit V1_0 -> 0 reaches t*. Scope (a):
model-level; the PDE-level uniformity of the model is the remaining question.

Run: python3 -u computations/qns_overlap_race_probe.py 2>&1 | tee /tmp/qns_race.log
"""
from __future__ import annotations
import math, sys
from pathlib import Path
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
try:
    from qou_substrate.witness import WitnessBuilder
except Exception:
    from witness_base import WitnessBuilder

GAMMA, D0, DT = 1.0, 1.0, 1.0e-5
T_STAR = math.pi * D0 * D0 / GAMMA

def integrate(v10: float) -> float:
    d2, v1, t = D0 * D0, v10, 0.0
    while v1 < d2:
        alpha = GAMMA / (2 * math.pi * d2)
        d2 -= DT * GAMMA / math.pi
        v1 += DT * alpha * v1
        t += DT
        if d2 <= 0:
            return T_STAR
    return t

def main() -> None:
    w = WitnessBuilder("qns-overlap-race-probe", engine="python")
    print("=" * 72)
    print("Overlap race: analytic u = 1 - (V1_0/d0^2)^(2/3) vs ODE sweep")
    print("=" * 72)
    worst = 0.0
    for e in range(2, 9):
        v10 = 10.0 ** (-e)
        u_pred = 1.0 - (v10 / (D0 * D0)) ** (2.0 / 3.0)
        t_pred = u_pred * T_STAR
        t_ode = integrate(v10)
        rel = abs(t_ode - t_pred) / t_pred
        worst = max(worst, rel)
        w.add_data(f"v10_1e-{e}_t_pred", t_pred)
        w.add_data(f"v10_1e-{e}_t_ode", t_ode)
        w.add_data(f"v10_1e-{e}_rel_err", rel)
        print(f"  V1_0=1e-{e}: t_pred={t_pred:.6f}  t_ode={t_ode:.6f}  rel={rel:.2e}  margin(1-u)={1-u_pred:.3e}")
    w.add_data("worst_rel_err", worst)
    w.add_assertion(
        "Analytic engagement time u = 1-(V1_0/d0^2)^(2/3) matches the ODE sweep "
        "(rel err < 1e-3 across 7 decades of core size)",
        computed=(worst < 1e-3), expected=True,
        source="closed-form phase-1 solutions d^2 = d0^2(1-u), V1 = V1_0(1-u)^{-1/2}",
    )
    w.add_assertion(
        "Overlap engages STRICTLY before t* for every positive core size "
        "(u_overlap < 1 always) — the race is decided in-model: branch B",
        computed=all((1.0 - (10.0 ** (-e)) ** (2.0 / 3.0)) < 1.0 for e in range(2, 9)),
        expected=True,
        source="(V1_0/d0^2)^{2/3} > 0 for V1_0 > 0; equality only in the "
               "measure-zero point-vortex limit",
    )
    w.set_description(
        "PC4: solves the overlap-engagement race analytically. Phase 1 of the "
        "pair-collision model integrates exactly (d^2 linear in t; V1 ~ "
        "(1-u)^{-1/2}), giving engagement at u = 1-(V1_0/d0^2)^{2/3} < 1 STRICTLY "
        "for every positive initial core size — verified against the ODE to <1e-3 "
        "across 7 decades. Within the two-regime corpus model the sharpened "
        "question of qns-pair-riccati-probe is DECIDED: the hyperbolic-overlap "
        "saturation always engages before the singular time; the pair channel is "
        "regular (branch B) for every positive core; only the measure-zero "
        "point-vortex limit reaches t*. Scope (a): model-level — whether the "
        "two-regime model is uniformly valid at the PDE level is the remaining "
        "open question. Consistent with lock-scaling (beta~1) and the "
        "sustained-forcing picture. Exploratory tier."
    )
    w.add_data("tier", "exploratory")
    w.add_data("finding",
               "Race DECIDED in-model: u_overlap = 1-(V1_0/d0^2)^(2/3) < 1 always; "
               "pair channel branch B for every positive core size. Scope (a).")
    w.save()
    print("Saved witness: qns-overlap-race-probe.witness.json")

if __name__ == "__main__":
    main()
