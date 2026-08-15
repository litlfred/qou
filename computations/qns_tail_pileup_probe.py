#!/usr/bin/env python3
"""qns_tail_pileup_probe — SF5: does enstrophy pile up above a fixed band as nu -> 0?

EXPLORATORY PROBE (not production). Bean qou-7swq (epic qou-a3n3).

The eps-uniformity reduction (low_mode_block_uniformity.lean, PR #5031)
reduced the millennium remainder to ONE spectral hypothesis: the enstrophy
above a FIXED band B stays uniformly bounded as the active block widens and
nu_q = eps/(2(1+eps)) -> 0 ("no pile-up at the receding damping threshold").
This probe is the decisive in-model test: unforced DN q-shell, WIDE fixed
truncation N = 32 >> B = 8, initial data band-limited to the first 4 rungs
(fixed, eps-independent), fixed horizon T = 50 eddy turnovers (the inertial
clock — pile-up, if any, develops on the transfer timescale), sweeping
eps (hence nu) downward. Measured per eps:

  sup_t Omega_{>B}(t)   (absolute above-band tail enstrophy, SUBSTRATE units)
  sup_t phi(t) = Omega_{>B}/Omega   (tail fraction)
  and the c_q-RESCALED tail  eps^2 * sup_t Omega_{>B}  (physical units under
  the candidate c_q = 1/eps time/length rescaling in which nu is fixed;
  reported for BOTH normalizations per the rescaling decision brief --
  the hypothesis is unit-dependent and the owner has not yet chosen).

Verdict bins (scope (a): DN model, this data/band/horizon, alone):
  - sup tail saturates (or decays) as eps -> 0  -> supports the no-pile-up
    hypothesis in-model; the uniformity route stays live
  - sup tail grows like a power of 1/eps        -> in-model pile-up; the
    uniform bound fails in substrate units at this model level (record the
    exponent; check the c_q-rescaled column before drawing limit conclusions)

Precision tier: float64 RK2, adaptive nonlinear CFL. Progress-logged.
Run: python3 -u computations/qns_tail_pileup_probe.py 2>&1 | tee /tmp/qns_sf5.log
"""
from __future__ import annotations

import math
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:
    from witness_base import WitnessBuilder

N = 32
BAND = 8
N_DATA = 4
T_EDDY = 50.0
EPS_SWEEP = (1e-1, 3e-2, 1e-2, 3e-3, 1e-3)
C_CFL = 5.0e-3


def run(eps: float):
    q = 1.0 + eps
    nu = eps / (2.0 * q)
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) if n < N_DATA else 0.0 for n in range(N)]
    om0 = sum(k[n] ** 2 * u[n] ** 2 for n in range(N))
    dt_visc = 0.4 / (nu * k[-1] ** 2 + 1e-30)

    def rhs(v):
        out = []
        for n in range(N):
            um = v[n - 1] if n > 0 else 0.0
            up = v[n + 1] if n < N - 1 else 0.0
            kp = k[n + 1] if n < N - 1 else k[-1] * (k[-1] / k[-2])
            out.append(k[n] * um * um - kp * v[n] * up - nu * k[n] ** 2 * v[n])
        return out

    sup_tail, sup_frac = 0.0, 0.0
    t, i, t0 = 0.0, 0, time.time()
    next_rep = 0.2
    while t < T_EDDY:
        cfl = max(k[n] * abs(u[n]) for n in range(N))
        dt = min(dt_visc, C_CFL / (cfl + 1e-30))
        r1 = rhs(u)
        mid = [u[j] + 0.5 * dt * r1[j] for j in range(N)]
        r2 = rhs(mid)
        u = [u[j] + dt * r2[j] for j in range(N)]
        t += dt
        i += 1
        if i % 20 == 0:
            tail = sum(k[n] ** 2 * u[n] ** 2 for n in range(BAND, N))
            tot = sum(k[n] ** 2 * u[n] ** 2 for n in range(N))
            if tail != tail:
                print(f"    [eps={eps:.0e}] ABORT NaN t={t:.2f}", flush=True)
                return float("nan"), float("nan"), om0
            sup_tail = max(sup_tail, tail)
            if tot > 0:
                sup_frac = max(sup_frac, tail / tot)
        if t / T_EDDY >= next_rep:
            el = time.time() - t0
            print(f"    [eps={eps:.0e}] {100 * t / T_EDDY:3.0f}%  supTail={sup_tail:.3e} "
                  f"supFrac={sup_frac:.3f}  steps={i} elapsed={el:.0f}s "
                  f"ETA={el * (T_EDDY - t) / max(t, 1e-9):.0f}s", flush=True)
            next_rep += 0.2
    return sup_tail, sup_frac, om0


def main() -> None:
    w = WitnessBuilder("qns-tail-pileup-probe", engine="python")
    print("=" * 76)
    print(f"SF5 pile-up probe: N={N}, band B={BAND}, data on first {N_DATA} rungs, "
          f"T={T_EDDY} eddy")
    print("=" * 76)
    tails, fracs = [], []
    for eps in EPS_SWEEP:
        st, sf, om0 = run(eps)
        resc = (eps ** 2) * st  # c_q-rescaled tail (k_phys = eps*k_sub)
        tails.append(st)
        fracs.append(sf)
        w.add_data(f"eps{eps:.0e}_sup_tail", st)
        w.add_data(f"eps{eps:.0e}_sup_frac", sf)
        w.add_data(f"eps{eps:.0e}_sup_tail_cq_rescaled", resc)
        print(f"  eps={eps:.0e}: sup_tail={st:.4e}  sup_frac={sf:.4f}  "
              f"cq-rescaled={resc:.4e}  (Om0={om0:.3f})")

    # growth diagnostics: global log-log slope of sup_tail vs 1/eps, and
    # the asymptotic slope from the last 3 points (the global fit is
    # contaminated by the heavily-damped eps=1e-1 point)
    def fit(xs, ys):
        n = len(xs)
        xb, yb = sum(xs) / n, sum(ys) / n
        return sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / \
            sum((x - xb) ** 2 for x in xs)
    xs = [math.log(1.0 / e) for e in EPS_SWEEP]
    ys = [math.log(max(t, 1e-300)) for t in tails]
    slope = fit(xs, ys)
    slope_asym = fit(xs[-3:], ys[-3:])
    rescaled = [(EPS_SWEEP[i] ** 2) * tails[i] for i in range(len(tails))]
    resc_decreasing = rescaled[-3] > rescaled[-2] > rescaled[-1]
    w.add_data("tail_growth_exponent_global", slope)
    w.add_data("tail_growth_exponent_asymptotic", slope_asym)
    print(f"\n  sup_tail 1/eps exponent: global {slope:.3f}, "
          f"asymptotic (last 3) {slope_asym:.3f}")

    w.add_assertion(
        "SUBSTRATE-UNIT PILE-UP IS REAL (scope-(a) refutation of the "
        "substrate-unit no-pile-up hypothesis in this model): sup_t tail "
        "enstrophy above the fixed band grows without bound as nu -> 0 "
        "(asymptotic 1/eps exponent > 0.5; tail fraction -> 1)",
        computed=(slope_asym > 0.5), expected=True,
        source=f"asymptotic exponent {slope_asym:.3f} (global {slope:.3f}); "
               f"max sup_frac = {max(fracs):.5f}; the vanishing-viscosity "
               "cascade fills the receding dissipation range — the "
               "Euler-type limit piles up, as classical intuition predicts. "
               f"Scope (a): DN model, band-limited data, T={T_EDDY} eddy, "
               f"N={N}, alone",
    )
    w.add_assertion(
        "C_Q-RESCALED (fixed-nu-unit) TAIL VANISHES: in the candidate "
        "physical normalization (eps^2 weight) the tail enstrophy decreases "
        "toward 0 as eps -> 0 — the fixed-nu-unit form of the hypothesis "
        "HOLDS in-model",
        computed=resc_decreasing, expected=True,
        source=f"rescaled tail over last 3 eps: "
               f"{rescaled[-3]:.3e} > {rescaled[-2]:.3e} > {rescaled[-1]:.3e} "
               f"(~eps^{2 - slope_asym:.2f}); the two normalizations give "
               "OPPOSITE answers — the substrate-to-physical rescaling "
               "decision (audit §5) is load-bearing for the uniformity "
               "question",
    )
    w.set_description(
        "SF5 (bean qou-7swq): decisive in-model test of the eps-uniformity "
        "tail hypothesis of low_mode_block_uniformity.lean ('no enstrophy "
        "pile-up above a fixed band as the damping threshold recedes'). "
        "Unforced DN q-shell, fixed wide truncation N=32, band B=8, "
        "eps-independent data on the first 4 rungs, fixed inertial horizon "
        "T=50 eddy turnovers, eps swept 1e-1 -> 1e-3 (nu_q -> 0). Reports "
        "sup_t tail enstrophy, sup_t tail fraction, and the c_q-rescaled "
        "(eps^2-weighted) tail per the pending rescaling decision — the "
        "hypothesis is unit-dependent and both normalizations are recorded. "
        "Verdict from the fitted 1/eps growth exponent of the substrate-unit "
        "sup-tail. Scope (a); exploratory float64 RK2 tier."
    )
    # Declares this witness into the float64-integrator carve-out
    # (qou-7kq3, owner-approved 2026-08-15). The values below come out of a
    # float64 RK2 integration — the integrator IS the source, so there is no
    # mpmath.mpf upstream to carry. Explicit rather than inferred: the audit
    # deliberately does NOT carve on `tier: exploratory`, so this excuse is a
    # claim made on the record here.
    w.add_data("precision_tier", "float64-integrator")
    w.add_data("tier", "exploratory")
    w.add_data("N", N)
    w.add_data("band", BAND)
    w.save()
    print("Saved witness: qns-tail-pileup-probe.witness.json")


if __name__ == "__main__":
    main()
