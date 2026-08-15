#!/usr/bin/env python3
"""qns_nonlocal_transfer_probe — SF8: does the per-amplitude structure
survive nonlocal (second-neighbor) transfer?

EXPLORATORY PROBE (not production). Bean qou-zoev (epic qou-a3n3).

The amplitude repair (PR #5066) rests on the DN model's nearest-neighbor
structure: inflow to rung n only from rung n-1, interior term
nonpositive. The standing fidelity caveat is that full NS transfer is
NONLOCAL. This probe stress-tests the per-amplitude route by adding an
energy-conserving second-neighbor channel of strength gamma:

  du_n/dt = k_n u_{n-1}^2 + gamma k_n u_{n-2}^2
            - k_{n+1} u_n u_{n+1} - gamma k_{n+2} u_n u_{n+2}
            - nu k_n^2 u_n

(the inflow gamma*k_n*u_{n-2}^2 pairs with the outflow
-gamma*k_{n+2}*u_n*u_{n+2}: in sum u_n * du_n the two telescope exactly,
so the inviscid model conserves energy for every gamma — checked by a
nu=0 sanity run). gamma = 1 makes the nonlocal channel as strong as the
local one — HARSHER than NS, where triad interactions decay with scale
separation.

Measured, per eps and per gamma:
  1. Inviscid energy conservation (sanity; ladder-independent).
  2. The two-source trajectory equilibrium ratio on empty-start rungs
       r_n = sup_t u_n * (nu * k_n) / (sup u_{n-1}^2 + gamma sup u_{n-2}^2)
     r_n <= 1 validates the two-source per-amplitude equilibrium
     (rung_equilibrium_two_source) along actual trajectories.
  3. The dissipation-scale crossing B* (theta_n = sup u_n/(nu k_n) < 1
     beyond it): existence and k_phys(B*) still bounded by the
     Kolmogorov scale and decreasing in eps.

Verdicts: all three hold at gamma = 1 -> the per-amplitude route is
robust to (this class of) nonlocality; any failure -> honest negative
locating where nonlocal transfer breaks the structure.

Precision tier: float64 RK2 adaptive CFL (SF6/SF7 integrator). Run:
python3 -u computations/qns_nonlocal_transfer_probe.py 2>&1 | tee /tmp/qns_sf8.log
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

try:
    from _precision import fmt  # noqa: E402
except Exception:  # pragma: no cover - fallback keeps the probe runnable
    def fmt(value, dps=None, strip_zeros=False):  # type: ignore[misc]
        return str(value)


def _f(x):
    """Serialize float64-tier values as strings.

    Witnesses must not carry raw float64 (AGENTS.md §"QA is agent-owned";
    `computations/witness_raw_float64_audit.py`). This probe computes in the
    float64 tier by design, so the fix is at serialization, not at the
    numerics: `_precision.fmt` renders a float via `str()`, which
    round-trips exactly. Non-floats (int, bool, str, list) pass through
    untouched so counts and flags keep their JSON types.
    """
    return fmt(x) if isinstance(x, float) else x


N_DATA = 4
T_EDDY = 10.0
EPS_SWEEP = (1e-1, 1e-2, 3e-3)
GAMMA_SWEEP = (0.5, 1.0)
C_CFL = 5.0e-3
N_CAP = 400
SUP_FLOOR = 1e-20


def ladder_len(eps: float) -> int:
    return min(N_CAP, int(math.ceil(math.log(3.0) / math.log(1.0 + eps))))


def make_rhs(N, k, nu, gamma):
    def rhs(v):
        out = []
        for n in range(N):
            um1 = v[n - 1] if n > 0 else 0.0
            um2 = v[n - 2] if n > 1 else 0.0
            up1 = v[n + 1] if n < N - 1 else 0.0
            up2 = v[n + 2] if n < N - 2 else 0.0
            kp1 = k[n + 1] if n < N - 1 else k[-1] * (k[-1] / k[-2])
            kp2 = k[n + 2] if n < N - 2 else k[-1] * (k[-1] / k[-2]) ** (n + 2 - (N - 1))
            out.append(k[n] * um1 * um1 + gamma * k[n] * um2 * um2
                       - kp1 * v[n] * up1 - gamma * kp2 * v[n] * up2
                       - nu * k[n] ** 2 * v[n])
        return out
    return rhs


def energy_check(eps: float, gamma: float) -> float:
    """Short inviscid run; relative energy drift (RK2 discretization only)."""
    q = 1.0 + eps
    N = 16
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) if n < N_DATA else 0.0 for n in range(N)]
    rhs = make_rhs(N, k, 0.0, gamma)
    e0 = sum(x * x for x in u)
    t = 0.0
    while t < 0.5:
        cfl = max(k[n] * abs(u[n]) for n in range(N))
        dt = C_CFL / (cfl + 1e-30)
        r1 = rhs(u)
        mid = [u[j] + 0.5 * dt * r1[j] for j in range(N)]
        r2 = rhs(mid)
        u = [u[j] + dt * r2[j] for j in range(N)]
        t += dt
    e1 = sum(x * x for x in u)
    return abs(e1 - e0) / e0


def run(eps: float, gamma: float):
    q = 1.0 + eps
    N = ladder_len(eps)
    nu = eps / (2.0 * q)
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) if n < N_DATA else 0.0 for n in range(N)]
    sup_u = list(u)
    dt_visc = 0.4 / (nu * k[-1] ** 2 + 1e-30)
    rhs = make_rhs(N, k, nu, gamma)

    t, i, t0 = 0.0, 0, time.time()
    next_rep = 0.25
    while t < T_EDDY:
        cfl = max(k[n] * abs(u[n]) for n in range(N))
        dt = min(dt_visc, C_CFL / (cfl + 1e-30))
        r1 = rhs(u)
        mid = [u[j] + 0.5 * dt * r1[j] for j in range(N)]
        r2 = rhs(mid)
        u = [u[j] + dt * r2[j] for j in range(N)]
        for n in range(N):
            if u[n] > sup_u[n]:
                sup_u[n] = u[n]
        t += dt
        i += 1
        if t / T_EDDY >= next_rep:
            el = time.time() - t0
            print(f"    [eps={eps:.0e} g={gamma}] N={N}  "
                  f"{100 * t / T_EDDY:3.0f}%  steps={i}  elapsed={el:.0f}s",
                  flush=True)
            next_rep += 0.25

    theta = [sup_u[n] / (nu * k[n]) for n in range(N)]
    k_phys = [(q - 1.0) * k[n] for n in range(N)]

    bstar = None
    for n in range(N):
        if all(theta[m] < 1.0 for m in range(n, N)):
            bstar = n
            break

    # two-source trajectory equilibrium ratio on excited empty-start rungs
    ratios = []
    for n in range(N_DATA, N):
        if sup_u[n] < SUP_FLOOR:
            continue
        forcing = sup_u[n - 1] ** 2 + gamma * sup_u[n - 2] ** 2
        if forcing > 0.0:
            ratios.append(sup_u[n] * (nu * k[n]) / forcing)
    max_ratio = max(ratios) if ratios else 0.0

    return theta, k_phys, bstar, max_ratio, len(ratios), N


def main() -> None:
    w = WitnessBuilder("qns-nonlocal-transfer-probe", engine="python")
    print("=" * 76)
    print(f"SF8 nonlocal-transfer probe: second-neighbor gamma sweep "
          f"{GAMMA_SWEEP}, eps-scaled ladder (cap {N_CAP}), T={T_EDDY} eddy")
    print("=" * 76)
    all_econs, all_r_ok, all_bstar = True, True, True
    kb_by_gamma = {g: [] for g in GAMMA_SWEEP}
    for gamma in GAMMA_SWEEP:
        ec = energy_check(1e-1, gamma)
        econs_ok = ec < 1e-4
        all_econs &= econs_ok
        w.add_data(f"g{gamma}_inviscid_energy_drift", _f(ec))
        print(f"  gamma={gamma}: inviscid energy drift {ec:.2e} "
              f"({'OK' if econs_ok else 'LEAK'})")
        for eps in EPS_SWEEP:
            theta, k_phys, bstar, max_ratio, nrat, nlen = run(eps, gamma)
            kb = k_phys[bstar] if bstar is not None else -1.0
            kb_pred = 2.0 ** 0.75 * eps ** 0.25
            if bstar is not None:
                kb_by_gamma[gamma].append(kb)
            all_bstar &= bstar is not None
            r_ok = max_ratio <= 1.0
            all_r_ok &= r_ok
            w.add_data(f"g{gamma}_eps{eps:.0e}_bstar_rung",
                       bstar if bstar is not None else -1)
            w.add_data(f"g{gamma}_eps{eps:.0e}_kphys_at_bstar", _f(kb))
            w.add_data(f"g{gamma}_eps{eps:.0e}_kphys_bstar_predicted", _f(kb_pred))
            w.add_data(f"g{gamma}_eps{eps:.0e}_max_equilibrium_ratio", _f(max_ratio))
            w.add_data(f"g{gamma}_eps{eps:.0e}_n_excited_ratios", nrat)
            print(f"  gamma={gamma} eps={eps:.0e}: N={nlen}  B*={bstar}  "
                  f"k_phys(B*)={kb:.4f} (pred {kb_pred:.4f})  "
                  f"max r_n={max_ratio:.3f} ({'OK' if r_ok else 'VIOLATED'}, "
                  f"{nrat} rungs)")

    kb_decreasing = all(
        all(v[j] > v[j + 1] for j in range(len(v) - 1))
        for v in kb_by_gamma.values() if len(v) == len(EPS_SWEEP))

    w.add_assertion(
        "the second-neighbor channel conserves energy inviscidly for "
        "every gamma (the pairing telescopes; sanity for the model class)",
        computed=all_econs, expected=True,
        source="nu=0 short run, relative energy drift < 1e-4 (RK2 "
               "discretization error only)",
    )
    w.add_assertion(
        "the two-source per-amplitude equilibrium holds along actual "
        "trajectories at every gamma and eps: r_n = sup u_n * nu*k_n / "
        "(sup u_{n-1}^2 + gamma*sup u_{n-2}^2) <= 1 on every excited "
        "empty-start rung — the per-amplitude route survives "
        "second-neighbor nonlocality up to gamma = 1 (equal-strength, "
        "harsher than NS triad decay)",
        computed=all_r_ok, expected=True,
        source="max r_n per (gamma, eps) over empty-start rungs",
    )
    w.add_assertion(
        "the dissipation-scale crossing B* still exists at every "
        "(gamma, eps) and its physical wavenumber still decreases with "
        "eps — the collapse condition is not degraded by the nonlocal "
        "channel",
        computed=(all_bstar and kb_decreasing), expected=True,
        source="theta_n profile per rung; k_phys(B*) monotone in eps "
               "within each gamma",
    )
    w.set_description(
        "SF8 (bean qou-zoev): nonlocality stress test for the amplitude "
        "repair (PR #5066). Extends the DN q-shell model with an "
        "energy-conserving second-neighbor transfer channel of strength "
        "gamma (inflow gamma*k_n*u_{n-2}^2 paired with outflow "
        "-gamma*k_{n+2}*u_n*u_{n+2}; exact telescoping in the energy "
        "sum). Measures whether the per-amplitude structure survives: "
        "two-source trajectory equilibrium ratio r_n <= 1, "
        "dissipation-scale crossing existence and eps-monotonicity. "
        "gamma = 1 makes nonlocal transfer as strong as local — harsher "
        "than NS, where triads decay with scale separation. Scope (a); "
        "float64 RK2 exploratory tier; this probes ONE nonlocality "
        "class (second-neighbor), not full NS triad structure."
    )
    w.add_data("tier", "exploratory")
    w.add_data("gamma_sweep", [_f(x) for x in GAMMA_SWEEP])
    w.add_data("n_cap", N_CAP)
    w.add_data("n_data", N_DATA)
    w.save()
    print("Saved witness: qns-nonlocal-transfer-probe.witness.json")


if __name__ == "__main__":
    main()
