#!/usr/bin/env python3
"""qns_backscatter_sustainment_probe — SF4: does BACKSCATTER re-open self-sustainment?

EXPLORATORY PROBE (not production). Bean: qou-y7ey (epic qou-a3n3).

The SF1-SF3 arc closed the unforced sustained channel in the DN
(Desnyansky-Novikov) q-shell model: decay is viscous-clock (SF2) and
N-uniform (SF3). The named fidelity caveat was that DN has NO backscatter
(energy moves only forward); full NS has backward/nonlocal transfer, which
could in principle feed the low modes and re-open self-sustainment. SF4
tests exactly that caveat with a GOY-class shell model (Gledzer 1973;
Ohkitani-Yamada 1989): complex amplitudes u_n, three-shell interactions

  du_n/dt = i( a*k_n    *conj(u_{n+1})*conj(u_{n+2})
             + b*k_{n-1}*conj(u_{n-1})*conj(u_{n+1})
             + c*k_{n-2}*conj(u_{n-1})*conj(u_{n-2}) ) - nu*k_n^2*u_n

with (a, b, c) = (1, -delta, delta-1), a+b+c = 0 (delta = 1/2 is the
standard 3D regime). The b and c terms carry energy BACKWARD. Key
structural check (verified by hand before coding): in the triad
(m, m+1, m+2) the three interaction terms carry coefficients a*k_m,
b*k_{(m+1)-1} = b*k_m, c*k_{(m+2)-2} = c*k_m — all the SAME k_m on ANY
ladder — so dE/dt = -2*sum_m k_m*(a+b+c)*Im(conj(u_m u_{m+1} u_{m+2}))
vanishes identically: the q-integer ladder k_n = [n]_q keeps EXACT
energy conservation. No hidden leak biases the probe. (A first draft
used a Sabra-style mixed-conjugation form whose unconjugated term flips
the condition to a+b-c = 0; with (1,-delta,delta-1) that leaks energy
secularly and blew up to NaN — the GOY all-conjugated form is the
correct ladder-independent conservative model.)

Protocol mirrors SF3: k_n = [n]_q at q = 1+eps, nu_q = eps/(2q), unforced
Kolmogorov load |u_n| = k_n^{-1/3} (deterministic golden-ratio phases),
viscous-scaled horizon T = 1.5*t_visc, classical same-nu control
(k_n = n). Measured: survival S = <Om>_late/Om_0 (time average over the
last 30% of the horizon) as a geometric mean over a 4-member
deterministic phase ensemble — GOY is chaotic, so a single-trajectory
ENDPOINT enstrophy fluctuates over orders of magnitude between phase
realisations and is not a stable observable (a first run measured
endpoint ratios R jumping 0.013 -> 50 -> 0.15 across N; the late-window
ensemble metric removes that noise). Ratio R = S_q/S_c reported
(i) across the SF3 N-sweep at delta = 1/2 (standard 3D-like regime), and
(ii) across a delta-sweep at fixed N (backscatter-strength robustness).

Verdict bins (scope (a): this model/load/eps, alone):
  - S_q(N) flat and R ~ 1  -> backscatter does NOT re-open sustainment;
    the SF-arc regularity picture survives its own fidelity caveat
  - S_q(N) grows or R >> 1 -> backscatter re-opens the channel; the
    DN-based closure was a model artifact

Precision tier: float64 RK2 (qualitative decay ratios; not canonical).
Run: python3 -u computations/qns_backscatter_sustainment_probe.py 2>&1 | tee /tmp/qns_sf4.log
"""
from __future__ import annotations

import cmath
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

EPS = 1.0e-2
F_VISC = 1.5
N_SWEEP = (8, 12, 16, 20, 24)
DELTA_STD = 0.5
DELTA_SWEEP = (0.1, 0.5, 0.9)
N_DELTA = 16
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0


PHASE_ENSEMBLE = (0.0, 0.25, 0.5, 0.75)


def load(ks, off):
    """Kolmogorov amplitudes, deterministic golden-ratio phases + ensemble offset."""
    return [ks[n] ** (-1.0 / 3.0)
            * cmath.exp(2j * math.pi * (((n + 1) * GOLDEN + off) % 1.0))
            for n in range(len(ks))]


def enstrophy(ks, u):
    return sum(ks[n] ** 2 * abs(u[n]) ** 2 for n in range(len(ks)))


def run_one(ks, nu, delta, tag, off):
    """Unforced GOY decay to the viscous-scaled horizon.

    Returns <Om>_late/Om_0 with <.>_late the time average over the last 30%
    of the horizon — a chaos-robust survival metric (a single endpoint value
    fluctuates over orders of magnitude between phase realisations).
    """
    N = len(ks)
    a, b, c = 1.0, -delta, delta - 1.0
    u = load(ks, off)
    om0 = enstrophy(ks, u)
    T = F_VISC / (nu * ks[0] ** 2)
    dt_visc = 0.4 / (nu * ks[-1] ** 2 + 1e-30)
    C_CFL = 5.0e-3

    def rhs(v):
        out = []
        for n in range(N):
            um1 = v[n - 1].conjugate() if n >= 1 else 0j
            um2 = v[n - 2].conjugate() if n >= 2 else 0j
            up1 = v[n + 1].conjugate() if n <= N - 2 else 0j
            up2 = v[n + 2].conjugate() if n <= N - 3 else 0j
            km1 = ks[n - 1] if n >= 1 else 0.0
            km2 = ks[n - 2] if n >= 2 else 0.0
            nl = 1j * (a * ks[n] * up1 * up2
                       + b * km1 * um1 * up1
                       + c * km2 * um1 * um2)
            out.append(nl - nu * ks[n] ** 2 * v[n])
        return out

    t0 = time.time()
    t, i, next_report = 0.0, 0, 0.2
    om_acc, t_acc = 0.0, 0.0
    while t < T:
        # adaptive nonlinear CFL: energy is exactly conserved by the GOY
        # nonlinearity, so max k|u| is bounded and dt has a floor
        cfl = max(ks[n] * abs(u[n]) for n in range(N))
        dt = min(dt_visc, C_CFL / (cfl + 1e-30))
        r1 = rhs(u)
        mid = [u[j] + 0.5 * dt * r1[j] for j in range(N)]
        r2 = rhs(mid)
        u = [u[j] + dt * r2[j] for j in range(N)]
        t += dt
        i += 1
        if t > 0.7 * T:  # late-window time average
            om_acc += enstrophy(ks, u) * dt
            t_acc += dt
        if t / T >= next_report:
            om = enstrophy(ks, u)
            if om != om:  # NaN guard — abort loudly, never report a silent nan
                print(f"    [{tag}] ABORT: NaN at t={t:.3f} step {i}", flush=True)
                return float("nan")
            el = time.time() - t0
            eta = el * (T - t) / max(t, 1e-30)
            print(f"    [{tag}] {100 * t / T:3.0f}%  Om/Om0={om / om0:.3e}  "
                  f"dt={dt:.2e} steps={i}  elapsed={el:.0f}s ETA={eta:.0f}s",
                  flush=True)
            next_report += 0.2
    return (om_acc / t_acc) / om0


def run(ks, nu, delta, tag):
    """Geometric-mean survival over the deterministic phase ensemble."""
    vals = []
    for off in PHASE_ENSEMBLE:
        s = run_one(ks, nu, delta, f"{tag} p{off}", off)
        if s != s:
            return float("nan")
        vals.append(max(s, 1e-300))
    gm = math.exp(sum(math.log(v) for v in vals) / len(vals))
    spread = max(vals) / min(vals)
    print(f"    [{tag}] ensemble gm={gm:.3e} spread={spread:.1e}", flush=True)
    return gm


def main() -> None:
    w = WitnessBuilder("qns-backscatter-sustainment-probe", engine="python")
    q = 1.0 + EPS
    nu = EPS / (2.0 * q)
    print("=" * 76)
    print(f"SF4: GOY backscatter probe, eps={EPS}, nu={nu:.4e}, T={F_VISC}*t_visc")
    print("=" * 76)

    # (i) N-sweep at delta = 1/2, mirroring SF3
    print(f"\n-- N-sweep at delta={DELTA_STD} --")
    Ss, Rs = [], []
    for N in N_SWEEP:
        kq = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
        kc = [float(n) for n in range(1, N + 1)]
        sq = run(kq, nu, DELTA_STD, f"N={N} q")
        sc = run(kc, nu, DELTA_STD, f"N={N} cl")
        R = sq / sc if sc > 0 else float("inf")
        Ss.append(sq); Rs.append(R)
        w.add_data(f"N{N}_S_q", sq)
        w.add_data(f"N{N}_R", R)
        print(f"  N={N:2d}: S_q={sq:.4e}  S_cl={sc:.4e}  R={R:.3f}")

    # (ii) delta-sweep at fixed N (backscatter-strength robustness)
    print(f"\n-- delta-sweep at N={N_DELTA} --")
    kq = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N_DELTA + 1)]
    kc = [float(n) for n in range(1, N_DELTA + 1)]
    Rd = []
    for d in DELTA_SWEEP:
        sq = run(kq, nu, d, f"d={d} q")
        sc = run(kc, nu, d, f"d={d} cl")
        R = sq / sc if sc > 0 else float("inf")
        Rd.append(R)
        w.add_data(f"delta{d}_S_q", sq)
        w.add_data(f"delta{d}_R", R)
        print(f"  delta={d}: S_q={sq:.4e}  S_cl={sc:.4e}  R={R:.3f}")

    # stepwise: any 10x jump between consecutive N counts as growth (an
    # endpoint-only comparison could miss an intermediate spike)
    grows = any(Ss[i + 1] > 10.0 * Ss[i] for i in range(len(Ss) - 1))
    flat_R = all(0.2 < r < 5.0 for r in Rs)
    delta_robust = all(0.2 < r < 5.0 for r in Rd)
    w.add_data("S_spread", max(Ss) / max(min(Ss), 1e-300))
    w.add_assertion(
        "Backscatter does NOT re-open self-sustainment: S_q stays flat/decreasing "
        "across the N-sweep (no growth with truncation)",
        computed=(not grows), expected=True,
        source=f"GOY delta={DELTA_STD}, S_q across N={N_SWEEP}; scope (a): this "
               "model/load/eps, alone",
    )
    w.add_assertion(
        "q/classical survival ratio stays near 1 with backscatter present "
        "(N-sweep and delta-sweep)",
        computed=(flat_R and delta_robust), expected=True,
        source=f"R(N) and R(delta) within [0.2, 5]; delta in {DELTA_SWEEP}",
    )
    w.set_description(
        "SF4 (bean qou-y7ey, epic qou-a3n3): tests the SF-arc's named fidelity "
        "caveat — DN has no backscatter — by rerunning the SF3 protocol in a "
        "GOY-class shell model (complex amplitudes, all-conjugated three-shell interactions, "
        "(a,b,c)=(1,-delta,delta-1), a+b+c=0, with exact energy conservation on the "
        "q-integer ladder, verified analytically: all triad (m,m+1,m+2) terms share the "
        "factor k_m, so conservation is ladder-independent). Unforced Kolmogorov "
        "load, viscous-scaled horizon, classical same-nu controls; N-sweep at "
        "delta=1/2 plus delta-sweep at N=16. If survival grows with N or "
        "R=S_q/S_cl >> 1, backward transfer re-opens the unforced sustained "
        "channel and the DN-based closure was a model artifact; if flat with "
        "R ~ 1, the regularity picture survives its own caveat and sustained "
        "forcing remains the only in-model blow-up channel. Scope (a); "
        "exploratory tier; float64 RK2."
    )
    # Declares this witness into the float64-integrator carve-out
    # (qou-7kq3, owner-approved 2026-08-15). The values below come out of a
    # float64 RK2 integration — the integrator IS the source, so there is no
    # mpmath.mpf upstream to carry. Explicit rather than inferred: the audit
    # deliberately does NOT carve on `tier: exploratory`, so this excuse is a
    # claim made on the record here.
    w.add_data("precision_tier", "float64-integrator")
    w.add_data("tier", "exploratory")
    w.add_data("eps", EPS)
    w.add_data("delta_std", DELTA_STD)
    w.save()
    print("Saved witness: qns-backscatter-sustainment-probe.witness.json")


if __name__ == "__main__":
    main()
