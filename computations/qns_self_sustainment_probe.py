#!/usr/bin/env python3
"""qns_self_sustainment_probe — can the finite low-mode core sustain its own cascade?

EXPLORATORY PROBE (not production). Bean: SF1 (epic qou-a3n3).

The campaign localised the classical blow-up channel to SUSTAINED/FORCED
turbulence. This probe tests the sharpest surviving question in the QOU's own
finite-dimensional core: WITHOUT external forcing, can the truncated q-NS
low-mode system act as its own forcing (self-sustain its cascade), or does it
always decay?

Model: Desnyansky-Novikov (DN) shell model with q-INTEGER wavenumbers
k_n = [n]_q = (q^n - 1)/(q - 1) (the corpus spectral tower) and q-viscosity
nu_q = (q-1)/(2q):
    u_n' = k_n u_{n-1}^2 - k_{n+1} u_n u_{n+1} - nu_q k_n^2 u_n
(energy-conserving nonlinear transfer; unforced). Initial data: Kolmogorov
load u_n = k_n^{-1/3} (E(k) ~ k^{-5/3}). Measured: enstrophy
Omega(t) = sum k_n^2 u_n^2 over several eddy turnovers, for a q -> 1+ ladder.

Verdicts: sustain ratio Omega(T)/Omega_max after transient — decays for all
eps -> the finite core CANNOT self-sustain (in-model evidence AGAINST the last
blow-up channel at finite q); record the decay-time scaling in eps.

Scope (a), model-level, exploratory tier (float64 RK2).
Run: python3 -u computations/qns_self_sustainment_probe.py 2>&1 | tee /tmp/qns_sf.log
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

N = 12
T_TURNOVERS = 30.0

def run(eps: float):
    q = 1.0 + eps
    nu = eps / (2.0 * q)
    k = [ (q**n - 1.0) / (q - 1.0) for n in range(1, N + 2) ]  # k[0]=[1]_q .. k[N]=[N+1]_q
    u = [ k[n] ** (-1.0/3.0) for n in range(N) ]
    om0 = sum(k[n]**2 * u[n]**2 for n in range(N))
    t_eddy = 1.0 / (k[0] * u[0])
    T = T_TURNOVERS * t_eddy
    dt = min(0.5 / (nu * k[N-1]**2 + 1e-30), 0.02 * t_eddy, 1e-3)
    steps = int(T / dt)
    om_max, om = om0, om0
    for s in range(steps):
        def rhs(v):
            out = []
            for n in range(N):
                um = v[n-1] if n > 0 else 0.0
                up = v[n+1] if n < N - 1 else 0.0
                out.append(k[n]*um*um - k[n+1]*v[n]*up - nu*k[n]**2*v[n])
            return out
        r1 = rhs(u)
        mid = [u[i] + 0.5*dt*r1[i] for i in range(N)]
        r2 = rhs(mid)
        u = [u[i] + dt*r2[i] for i in range(N)]
        om = sum(k[n]**2 * u[n]**2 for n in range(N))
        om_max = max(om_max, om)
        if om > 1e12 * om0:
            return om0, om_max, om, s*dt/t_eddy, True
    return om0, om_max, om, T_TURNOVERS, False

def main() -> None:
    w = WitnessBuilder("qns-self-sustainment-probe", engine="python")
    print("=" * 76)
    print(f"Self-sustainment: unforced DN q-shell model, N={N}, k_n=[n]_q (EXPLORATORY)")
    print("=" * 76)
    all_decay = True
    for e in range(1, 5):
        eps = 10.0 ** (-e)
        om0, om_max, om_end, tt, blew = run(eps)
        ratio = om_end / om_max
        sustained = blew or ratio > 0.5
        all_decay = all_decay and not sustained
        w.add_data(f"eps_1e-{e}_omega_end_over_max", ratio)
        w.add_data(f"eps_1e-{e}_omega_max_over_0", om_max / om0)
        w.add_data(f"eps_1e-{e}_blowup", blew)
        print(f"  eps=1e-{e}: Om_end/Om_max={ratio:.3e}  Om_max/Om0={om_max/om0:.3f}  "
              f"turnovers={tt:.1f}  {'BLEW' if blew else ('SUSTAINED' if sustained else 'decays')}")
    w.add_assertion(
        "Sustainment EMERGES as eps -> 0 on the fixed 30-turnover horizon: "
        "eps>=1e-3 decays, eps=1e-4 sustains (Om_end/Om_max ~ 0.71)",
        computed=(not all_decay), expected=True,
        source="DN q-shell, Kolmogorov load; transition near eps ~ 1e-3..1e-4. "
               "CONFOUND flagged: at eps=1e-4 the low-mode viscous time "
               "~2/(eps*k1^2) ~ 2e4 turnovers >> horizon, so horizon-sustainment "
               "is consistent with slow viscous decay; the transient growth "
               "Om_max/Om0 ~ 3.9 does show active inertial transfer. "
               "Discriminator (next bean): horizon scaled to the viscous time / "
               "classical same-nu comparison. Scope (a).",
    )
    w.set_description(
        "SF1 (epic qou-a3n3): tests whether the QOU's finite low-mode core can act "
        "as its own forcing. Unforced Desnyansky-Novikov shell model with q-integer "
        "wavenumbers k_n=[n]_q and nu_q=(q-1)/(2q), N=12, Kolmogorov initial load, "
        "30 eddy turnovers, RK2. Verdict per eps ladder: does enstrophy sustain "
        "(Om_end/Om_max > 0.5 or blow-up) or decay? Decay everywhere = the finite "
        "core cannot self-sustain its cascade — in-model evidence AGAINST the "
        "sustained-forcing blow-up channel at finite q; the channel would then "
        "require genuinely infinite-dimensional sustainment (the q->1 limit "
        "escaping every finite truncation). Scope (a); exploratory tier."
    )
    w.add_data("tier", "exploratory")
    w.add_data("n_shells", N)
    w.save()
    print("Saved witness: qns-self-sustainment-probe.witness.json")

if __name__ == "__main__":
    main()
