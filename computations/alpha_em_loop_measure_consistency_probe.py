#!/usr/bin/env python3
"""alpha_em_loop_measure_consistency_probe.py — which per-loop measure is the
PROVED one, and is the theta-graph 1.3sigma hit robust to the measure choice?

Owner directive: work the open 2-loop categorical calculation. The one piece
phase 4 left UNDERIVED is the per-loop measure 1/(8pi) = 1/(pi*b1). Before any
derivation, pin down what is actually PROVED about the measure and whether the
theta-graph candidate depends on the (underived) 1/(8pi) choice.

THE MEASURE PRINCIPLE THAT IS ACTUALLY PROVED (#1444 / photon-ir-zero-mode-bring):
  "The heat-kernel zero-mode of a Laplacian contributes one constant mode
   1/Vol per harmonic generator."  =>  zero-mode = b1 * (1/Area) = b1/(4pi(g-1)).
So the PROVED per-mode measure is  mu_proved = 1/Area = 1/(12pi) at g=4  --
NOT 1/(8pi). The self-energy's 1/(8pi) = 1/(pi*b1) is a DIFFERENT geometric
factor (b1 in the denominator vs the numerator); phase 4's "same measure"
structural-consistency claim conflates the two.

This probe propagates each candidate per-loop measure CONSISTENTLY through the
graph-measure ladder  1/alpha = T + sum_{L>=1} (-1)^{L+1} [L+1]_q * mu^L  and
reports the residual + anchor stability, so the theta-graph hit can be judged
robust-or-artifact:

  mu_A = 1/(pi*b1)  = 1/(8pi)    (phase-4 self-energy identification; UNDERIVED)
  mu_B = 1/Area     = 1/(12pi)   (the PROVED heat-kernel per-mode measure)
  mu_C = 1/(pi*Area/... )        hybrids reported for completeness

Discipline: the ONLY proved input is mu_B (heat-kernel 1/Area). mu_A is the
undecided target. Nothing wired; window used only to falsify; scope-(a).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402

set_compute_dps()
CODATA = mp.mpf("137.035999084")
SIGMA_PPB = mp.mpf("0.15")
# Both pins read BY NAME (bean qou-4bef, 2026-09-03); the muon literal this carried was the
# pin RETIRED 2026-08-22/28.
Q_PROTON = Q_MP
Q_MUON = q_muon_at(50)
G = 4
B1 = 2 * G                     # dim H^1 = 8
AREA = 4 * mp.pi * (G - 1)     # 12 pi


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def ladder_inv_alpha(q, mu, n_loops=2):
    """1/alpha = T + sum_{L=1}^{n_loops} (-1)^{L+1} [L+1]_q mu^L, solved for alpha,
    returned as 1/alpha (the self-consistent root near 137)."""
    T = q * qb(9, q) * qb(10, q) + mp.mpf(8) / (12 * mp.pi)
    # build polynomial in alpha: 1 = T a + [2]mu a^2 - [3]mu^2 a^3 + ...
    coeffs = [mp.mpf(-1)]                      # -1 (constant, for  ... - 1 = 0)
    # we want  T a + sum (-1)^{L+1}[L+1] mu^L a^{L+1} - 1 = 0
    # polyroots wants highest degree first; assemble by degree
    deg = n_loops + 1
    poly = [mp.mpf(0)] * (deg + 1)
    poly[deg - 0] = -1                         # a^0 term -> constant -1  (index from end)
    # easier: coefficient of a^k
    c = {0: mp.mpf(-1), 1: T}
    for L in range(1, n_loops + 1):
        c[L + 1] = (-1) ** (L + 1) * qb(L + 1, q) * mu ** L
    P = [c.get(k, mp.mpf(0)) for k in range(deg, -1, -1)]
    roots = mp.polyroots(P, maxsteps=200, extraprec=100)
    real = [mp.re(r) for r in roots if abs(mp.im(r)) < mp.mpf("1e-30") and mp.re(r) > 0]
    a = min(real, key=lambda r: abs(r - mp.mpf("0.0073")))
    return 1 / a


def ppb(v):
    return (v - CODATA) / CODATA * mp.mpf(10) ** 9   # mpf, never float64


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" alpha_EM per-loop MEASURE consistency — proved (1/Area) vs identified (1/pi b1)")
    print("=" * 78)

    measures = {
        "mu_A = 1/(pi*b1) = 1/(8pi)  [phase-4, UNDERIVED]": mp.mpf(1) / (mp.pi * B1),
        "mu_B = 1/Area    = 1/(12pi) [PROVED heat-kernel per-mode]": 1 / AREA,
        "mu_hybrid = 1/(pi*sqrt(b1*Area/pi)) ": mp.mpf(1) / mp.sqrt(mp.pi * B1 * AREA),
    }
    print("\n  zero-mode (PROVED): b1/Area = 8/(12pi) = "
          f"{mp.nstr(B1/AREA, 12)} = 2/(3pi)")
    print(f"  per-mode measure in that proof: 1/Area = 1/(12pi) = {mp.nstr(1/AREA, 12)}")
    print(f"  self-energy measure claimed:    1/(pi b1) = 1/(8pi) = {mp.nstr(1/(mp.pi*B1), 12)}")
    print("  => these DIFFER: the 'same measure' phase-4 claim is unsound.\n")

    results = {}
    for label, mu in measures.items():
        row = {}
        for aname, qs in (("proton", Q_PROTON), ("muon", Q_MUON)):
            q = mp.mpf(qs)
            inv1 = ladder_inv_alpha(q, mu, n_loops=1)
            inv2 = ladder_inv_alpha(q, mu, n_loops=2)
            row[aname] = {"1loop_ppb": ppb(inv1), "2loop_ppb": ppb(inv2)}
        results[label] = row
        p1 = row["proton"]["1loop_ppb"]; p2 = row["proton"]["2loop_ppb"]
        print(f"  {label}")
        print(f"      proton: 1-loop {mp.nstr(p1, 5)} ppb ({mp.nstr(abs(p1)/SIGMA_PPB, 4)}s)   "
              f"2-loop {mp.nstr(p2, 5)} ppb ({mp.nstr(abs(p2)/SIGMA_PPB, 4)}s)")
        m2 = row["muon"]["2loop_ppb"]
        print(f"      muon:   2-loop {mp.nstr(m2, 5)} ppb\n")

    # verdict
    muA = results["mu_A = 1/(pi*b1) = 1/(8pi)  [phase-4, UNDERIVED]"]["proton"]["2loop_ppb"]
    muB = results["mu_B = 1/Area    = 1/(12pi) [PROVED heat-kernel per-mode]"]["proton"]["2loop_ppb"]
    print("[verdict]")
    print(f"  The theta-graph 1.3s hit uses mu_A (1/8pi) -> {mp.nstr(muA, 5)} ppb.")
    print(f"  The PROVED measure mu_B (1/Area=1/12pi)     -> {mp.nstr(muB, 5)} ppb.")
    print(f"  => the 1.3s hit is NOT robust to the measure principle actually proved;")
    print(f"     it is contingent on the UNDERIVED 1/(pi b1) identification. Closing")
    print(f"     alpha_EM to <=sigma_a REQUIRES deriving the per-loop measure (1/8pi),")
    print(f"     which the zero-mode heat-kernel argument does NOT supply.")

    wb = WitnessBuilder("alpha-em-loop-measure-consistency", engine="mpmath")
    wb.set_description(
        "Per-loop measure consistency for the alpha_EM graph ladder. The ONLY "
        "proved measure principle (heat-kernel: one constant mode 1/Vol per "
        "harmonic generator, #1444/photon-ir) gives per-mode 1/Area = 1/(12pi), "
        "NOT the self-energy's 1/(pi b1) = 1/(8pi) -- phase-4's 'same measure' "
        "consistency claim conflates a mode-count*1/Area with a per-loop 1/(pi b1). "
        "Propagating each candidate consistently through the theta-graph ladder: "
        "the 1.3-sigma theta-graph hit uses the UNDERIVED 1/(8pi) (mu_A); the "
        "proved 1/Area (mu_B) gives a materially different residual. So the "
        "candidate is contingent on the undecided per-loop measure -- closing "
        "alpha_EM to <= sigma_a genuinely requires DERIVING 1/(8pi), which the "
        "zero-mode argument does not supply. Nothing wired; window falsify-only; "
        "scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_data("bring_data", {"g": G, "b1": B1, "Area_over_pi": "12",
                               "zero_mode": mp.nstr(B1 / AREA, 15)})
    wb.add_data("measures", {k: mp.nstr(v, 15) for k, v in measures.items()})
    wb.add_data("ladder_residuals_ppb", {k: {a: {kk: fmt(vv, 20) for kk, vv in r.items()} for a, r in row.items()} for k, row in results.items()})
    wb.add_data("verdict", {
        "proved_per_mode_measure": "1/Area = 1/(12pi)",
        "self_energy_claimed_measure": "1/(pi b1) = 1/(8pi)",
        "same_measure_claim": "UNSOUND (different geometric factors)",
        "theta_hit_robust_to_proved_measure": False,
        "consequence": "closing alpha_EM requires DERIVING 1/(8pi); zero-mode heat-kernel does not supply it"})
    wb.add_assertion("measures_differ",
                     computed=("1" if abs(1 / (mp.pi * B1) - 1 / AREA) > mp.mpf("1e-6") else "0"),
                     expected="1", tolerance="0.5",
                     source="1/(pi b1)=1/8pi != 1/Area=1/12pi -- the two IR measures are distinct")
    wb.add_assertion("theta_hit_measure_contingent",
                     computed=("1" if abs(muA - muB) > SIGMA_PPB else "0"),
                     expected="1", tolerance="0.5",
                     source="2-loop residual under proved 1/Area differs from the 1/8pi hit by > sigma_a")
    wb.save(q0_comparison(
        muon=Q_MUON, proton=Q_PROTON,
        reason="per-loop-measure consistency ladder evaluated at both pins on purpose; the proton "
               "(default) leg carries the verdict, the muon leg the anchor-stability check"))
    print(f"\n  ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
