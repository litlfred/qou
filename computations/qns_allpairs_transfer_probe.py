#!/usr/bin/env python3
"""qns_allpairs_transfer_probe — SF9: does the per-amplitude structure
survive ALL-PAIRS nonlocal transfer with geometric decay?

EXPLORATORY PROBE (not production). Bean qou-p0be (epic qou-a3n3).

SF8 (PR #5072) showed the per-amplitude route survives a second-neighbor
channel. This probe goes to the closest shell-model image of full NS
triad structure: EVERY pair (m, n) with m < n is coupled, with weight
decaying geometrically in scale separation:

  w_{nm} = lam^{n-m-1}          (lam = 0 recovers the local DN model)

Each pair is energy-conserving by construction — inflow to rung n:
w*k_n*u_m^2, paired outflow at rung m: -w*k_n*u_m*u_n; the pair's
contribution to sum u*du is exactly zero. The rhs is

  du_n/dt = k_n*S_n - u_n*T_n - nu*k_n^2*u_n,
  S_n = sum_{m<n} lam^{n-1-m} u_m^2     (forward recursion, O(N))
  T_n = sum_{p>n} lam^{p-n-1} k_p u_p   (backward recursion, O(N))

so the all-pairs model costs the same as the local one — no coupling
truncation anywhere. lam = 0.9 keeps 10 rungs at >38% weight and 40
rungs at >1.5%: far more delocalized than NS triad decay.

Measured, per (lam, eps):
  1. Inviscid energy conservation (sanity; per-pair exact, drift = RK2).
  2. The all-source trajectory equilibrium ratio on empty-start rungs
       r_n = sup u_n * (nu*k_n) / sum_{m<n} lam^{n-1-m} (sup u_m)^2
     r_n <= 1 validates the per-amplitude equilibrium with the FULL
     geometric forcing sum, along actual trajectories.
  3. The dissipation-scale crossing B* (theta_n < 1 beyond): existence
     and eps-monotonic k_phys(B*).

Verdicts: all three at lam = 0.9 -> the per-amplitude route is robust
to all-pairs geometric nonlocality; any failure -> honest negative
locating where delocalization breaks the structure.

Precision tier: float64 RK2 adaptive CFL (SF6-SF8 integrator). Run:
python3 -u computations/qns_allpairs_transfer_probe.py 2>&1 | tee /tmp/qns_sf9.log
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
LAM_SWEEP = (0.5, 0.9)
C_CFL = 5.0e-3
N_CAP = 400
SUP_FLOOR = 1e-20


def ladder_len(eps: float) -> int:
    return min(N_CAP, int(math.ceil(math.log(3.0) / math.log(1.0 + eps))))


def make_rhs(N, k, nu, lam):
    def rhs(v):
        # forward: S[n] = sum_{m<n} lam^{n-1-m} v[m]^2
        S = [0.0] * N
        for n in range(1, N):
            S[n] = lam * S[n - 1] + v[n - 1] * v[n - 1]
        # backward: T[n] = sum_{p>n} lam^{p-n-1} k[p] v[p]
        T = [0.0] * N
        for n in range(N - 2, -1, -1):
            T[n] = lam * T[n + 1] + k[n + 1] * v[n + 1]
        return [k[n] * S[n] - v[n] * T[n] - nu * k[n] ** 2 * v[n]
                for n in range(N)]
    return rhs


def energy_check(eps: float, lam: float) -> float:
    q = 1.0 + eps
    N = 16
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) if n < N_DATA else 0.0 for n in range(N)]
    rhs = make_rhs(N, k, 0.0, lam)
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


def run(eps: float, lam: float):
    q = 1.0 + eps
    N = ladder_len(eps)
    nu = eps / (2.0 * q)
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) if n < N_DATA else 0.0 for n in range(N)]
    sup_u = list(u)
    dt_visc = 0.4 / (nu * k[-1] ** 2 + 1e-30)
    rhs = make_rhs(N, k, nu, lam)

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
            print(f"    [lam={lam} eps={eps:.0e}] N={N}  "
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

    # all-source trajectory equilibrium ratio on excited empty-start rungs:
    # forcing sum from the FULL geometric ladder of sups below rung n
    ratios = []
    for n in range(N_DATA, N):
        if sup_u[n] < SUP_FLOOR:
            continue
        forcing = sum((lam ** (n - 1 - m)) * sup_u[m] ** 2 for m in range(n))
        if forcing > 0.0:
            ratios.append(sup_u[n] * (nu * k[n]) / forcing)
    max_ratio = max(ratios) if ratios else 0.0

    return theta, k_phys, bstar, max_ratio, len(ratios), N


def main() -> None:
    w = WitnessBuilder("qns-allpairs-transfer-probe", engine="python")
    print("=" * 76)
    print(f"SF9 all-pairs transfer probe: geometric decay lam sweep "
          f"{LAM_SWEEP}, eps-scaled ladder (cap {N_CAP}), T={T_EDDY} eddy")
    print("=" * 76)
    all_econs, all_r_ok, all_bstar = True, True, True
    kb_by_lam = {g: [] for g in LAM_SWEEP}
    for lam in LAM_SWEEP:
        ec = energy_check(1e-1, lam)
        econs_ok = ec < 1e-4
        all_econs &= econs_ok
        w.add_data(f"lam{lam}_inviscid_energy_drift", _f(ec))
        print(f"  lam={lam}: inviscid energy drift {ec:.2e} "
              f"({'OK' if econs_ok else 'LEAK'})")
        for eps in EPS_SWEEP:
            theta, k_phys, bstar, max_ratio, nrat, nlen = run(eps, lam)
            kb = k_phys[bstar] if bstar is not None else -1.0
            kb_pred = 2.0 ** 0.75 * eps ** 0.25
            if bstar is not None:
                kb_by_lam[lam].append(kb)
            all_bstar &= bstar is not None
            r_ok = max_ratio <= 1.0
            all_r_ok &= r_ok
            w.add_data(f"lam{lam}_eps{eps:.0e}_bstar_rung",
                       bstar if bstar is not None else -1)
            w.add_data(f"lam{lam}_eps{eps:.0e}_kphys_at_bstar", _f(kb))
            w.add_data(f"lam{lam}_eps{eps:.0e}_kphys_bstar_predicted", _f(kb_pred))
            w.add_data(f"lam{lam}_eps{eps:.0e}_max_equilibrium_ratio", _f(max_ratio))
            w.add_data(f"lam{lam}_eps{eps:.0e}_n_excited_ratios", nrat)
            print(f"  lam={lam} eps={eps:.0e}: N={nlen}  B*={bstar}  "
                  f"k_phys(B*)={kb:.4f} (pred {kb_pred:.4f})  "
                  f"max r_n={max_ratio:.3f} "
                  f"({'OK' if r_ok else 'VIOLATED'}, {nrat} rungs)")

    kb_decreasing = all(
        all(v[j] > v[j + 1] for j in range(len(v) - 1))
        for v in kb_by_lam.values() if len(v) == len(EPS_SWEEP))

    w.add_assertion(
        "the all-pairs geometric coupling conserves energy inviscidly for "
        "every lam (per-pair pairing is exact; drift is RK2 only)",
        computed=all_econs, expected=True,
        source="nu=0 short run, relative energy drift < 1e-4",
    )
    w.add_assertion(
        "the all-source per-amplitude equilibrium holds along actual "
        "trajectories at every (lam, eps): r_n = sup u_n * nu*k_n / "
        "sum_{m<n} lam^{n-1-m} (sup u_m)^2 <= 1 on every excited "
        "empty-start rung — the per-amplitude route survives ALL-PAIRS "
        "nonlocality with decay as weak as lam = 0.9",
        computed=all_r_ok, expected=True,
        source="max r_n per (lam, eps) over empty-start rungs",
    )
    w.add_assertion(
        "the dissipation-scale crossing B* still exists at every "
        "(lam, eps) and its physical wavenumber still decreases with eps",
        computed=(all_bstar and kb_decreasing), expected=True,
        source="theta_n profile per rung; k_phys(B*) monotone in eps "
               "within each lam",
    )
    w.set_description(
        "SF9 (bean qou-p0be): all-pairs nonlocality stress test for the "
        "per-amplitude route (PRs #5066, #5072). Couples EVERY rung pair "
        "(m < n) with geometric weight lam^{n-m-1}, each pair "
        "energy-conserving by construction; the geometric structure "
        "telescopes into O(N) forward/backward recursions so no coupling "
        "truncation is needed. Measures the all-source trajectory "
        "equilibrium ratio and the dissipation-scale crossing across "
        "lam in {0.5, 0.9} and eps. lam = 0.9 is far more delocalized "
        "than NS triad decay. Scope (a); float64 RK2 exploratory tier; "
        "sweeping effects (phase decorrelation by large scales) are not "
        "representable in a real-amplitude shell model and remain the "
        "irreducible caveat."
    )
    w.add_data("tier", "exploratory")
    w.add_data("lam_sweep", [_f(x) for x in LAM_SWEEP])
    w.add_data("n_cap", N_CAP)
    w.add_data("n_data", N_DATA)
    w.save()
    print("Saved witness: qns-allpairs-transfer-probe.witness.json")


if __name__ == "__main__":
    main()
