#!/usr/bin/env python3
"""mu2_target_and_per_order_law_probe.py
=========================================

**The third point exists, and it REFUTES the geometric per-order law.**

`mu4_magnitude_gap_anatomy_probe.py` established that the 9.56× A=4 magnitude
gap is a product of two opposite misses (`k₃ = 0.5486`, `k₄ = 5.2419`), and
warned that reading `k_n = a·rⁿ` off those two numbers is a **tautology** — two
parameters on two points, exact for any pair. It named the test: a μ₂ target
from the same simplex.

**THE μ₂ TARGET EXISTS AND IS EXACTLY ZERO — structurally, not incidentally.**
The simplex is deuteron-anchored, so it reproduces the 2-body datum exactly and
leaves no 2-body residual. All three producers that build it say so, and two
assert it:

    deltalambda_kappa_interface_residual_simplex_probe.py
        residual_pure_ge3body = abs(mu2) < mp.mpf("1e-40")
        print("  μ₂(edge)    = ...   ← ZERO: no 2-body component")
    mu3_target_frame_robustness_probe.py
        assert corr["per_baseline"][k]["mu2_is_zero"], "μ₂ must be 0 (deuteron)"
    helium_four_body_cluster_probe.py
        mu2 = M[2];  mu3 = M[3] - 3*mu2;  mu4 = M[4] - 6*mu2 - 4*mu3

The **measured** μ₂ is not zero: the committed He4 witness carries six nonzero
per-bond values (mean −0.5840). So the third correction factor is well defined:

    k₂ = target/measured = 0 / (−0.5840) = 0   EXACTLY

**THE TEST, AND IT IS DECISIVE.** A geometric per-order law `k_n = a·rⁿ` with
`k₂ = 0` forces `a·r² = 0`, hence `a = 0` or `r = 0`. Either forces `k₃ = k₄ =
0`. But `k₃ = 0.5486` and `k₄ = 5.2419`, both nonzero. **No finite `(a, r)` fits
all three points: the geometric per-order reading is REFUTED**, not merely
untested.

This is a scope-(b) exclusion with a cited invariant — the structural vanishing
of the 2-body residual under a deuteron-anchored simplex — and it is the reason
the two-point reading had to be resisted rather than quoted.

WHAT IT DOES AND DOES NOT SETTLE
--------------------------------
It **closes** one hypothesis about the shape of the gap: the misses are not a
geometric rescaling in body order. It does **not** explain the gap, does not
touch the scope-(a) wall recorded in `a4-interface-magnitude-one-scalar-gate`
(the mechanism is surjective onto every target, so the magnitude stays open and
uncloseable by computation), and does not claim any other functional form is
excluded — only the geometric one, and only because `k₂ = 0`.

A caveat stated rather than buried: `k₂ = 0` is a property of the SIMPLEX's
construction, not an independent measurement. It is the right third point for
this test because it is the same kind of quantity as `k₃` and `k₄` — a
target-over-measured ratio for the same model against the same H₁₂ cumulants —
but anyone re-anchoring the simplex away from the deuteron would need to redo it.

PRECISION
---------
mpmath at 30 dps. The measured inputs come from the committed He4 witness, which
serializes them as raw float64; the verdict turns on `k₂` being exactly 0 versus
`k₃`, `k₄` being O(1), which no float64 question can affect.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import subprocess
import time

import mpmath as mp  # noqa: E402

from _precision import fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 30
HE4 = "computations/deltalambda/helium4-mu4-cluster-moment.witness.json"


def main() -> int:
    t0 = time.monotonic()
    raw = subprocess.run(["git", "show", f"origin/main:{HE4}"],
                         capture_output=True, text=True, check=True).stdout
    m = json.loads(raw)["data"]["mu4_cluster_moment"]

    n_bonds = len(m["mu2_per_bond"])
    mu2_meas = mp.mpf(str(m["sum_mu2"])) / n_bonds
    mu3_meas = mp.mpf(str(m["mu3_mean"]))
    mu4_meas = mp.mpf(str(m["mu4_measured"]))
    mu2_t, mu3_t, mu4_t = mp.mpf(0), mp.mpf("0.4708"), mp.mpf("-4.591")

    k2 = mu2_t / mu2_meas
    k3 = mu3_t / mu3_meas
    k4 = mu4_t / mu4_meas

    # geometric law k_n = a*r^n : k2 == 0 forces a==0 or r==0, forcing k3==k4==0
    geometric_survives = (k2 != 0) or (k3 == 0 and k4 == 0)

    print(f"  measured mu2 (mean over {n_bonds} bonds) = {mp.nstr(mu2_meas, 10)}  (nonzero)")
    print(f"  target   mu2 = 0 EXACTLY (structural: deuteron-anchored simplex)")
    print()
    for nm, k in (("k2", k2), ("k3", k3), ("k4", k4)):
        print(f"  {nm} = target/measured = {mp.nstr(k, 8)}")
    print()
    print("  geometric law k_n = a*r^n at three points:")
    print("    k2 = 0  =>  a*r^2 = 0  =>  a = 0 or r = 0  =>  k3 = k4 = 0")
    print(f"    but k3 = {mp.nstr(k3, 6)}, k4 = {mp.nstr(k4, 6)} — both nonzero")
    print(f"    => geometric per-order law SURVIVES? {geometric_survives}  (REFUTED)")

    w = WitnessBuilder("mu2-target-and-per-order-law", start_time=t0)
    w.set_description(
        "The mu2 target exists and is structurally ZERO (deuteron-anchored "
        "simplex), supplying the third point the anatomy probe named. It "
        "REFUTES the geometric per-order law k_n = a*r^n: k2 = 0 forces a = 0 "
        "or r = 0, either of which forces k3 = k4 = 0, contradicting the "
        "measured nonzero k3, k4. Scope-(b) with a cited invariant. Does not "
        "explain the magnitude gap and does not touch the scope-(a) wall.")
    w.add_data("mu2_target_is_structurally_zero", {
        "value": fmt(mu2_t),
        "reason": ("the simplex is deuteron-anchored, so it reproduces the "
                   "2-body datum exactly and leaves no 2-body residual"),
        "asserted_in": [
            "deltalambda_kappa_interface_residual_simplex_probe.py "
            "(residual_pure_ge3body = abs(mu2) < 1e-40)",
            "mu3_target_frame_robustness_probe.py "
            "(assert ... mu2_is_zero, 'mu2 must be 0 (deuteron)')",
        ],
    })
    w.add_data("correction_factors", {
        "k2": fmt(k2), "k3": fmt(k3), "k4": fmt(k4),
        "mu2_measured_mean_per_bond": fmt(mu2_meas),
        "n_bonds": n_bonds,
    })
    w.add_data("geometric_per_order_law", {
        "form": "k_n = a * r^n",
        "survives": geometric_survives,
        "argument": ("k2 = 0 forces a*r^2 = 0, hence a = 0 or r = 0; either "
                     "forces k3 = k4 = 0, contradicting the measured nonzero "
                     "k3 = 0.5486 and k4 = 5.2419. No finite (a, r) fits all "
                     "three points."),
        "scope": "(b), cited invariant = structural vanishing of the 2-body residual",
    })
    w.add_data("caveat", (
        "k2 = 0 is a property of the SIMPLEX's construction, not an "
        "independent measurement. It is the right third point because it is "
        "the same kind of quantity as k3 and k4 — target-over-measured for the "
        "same model against the same H12 cumulants — but re-anchoring the "
        "simplex away from the deuteron would require redoing it."))
    w.add_assertion("mu2_target_is_zero", mu2_t == 0, True)
    w.add_assertion("mu2_measured_is_nonzero", mu2_meas != 0, True)
    w.add_assertion("geometric_per_order_law_refuted", geometric_survives, False)
    w.save()
    print(f"\nwall {time.monotonic()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
