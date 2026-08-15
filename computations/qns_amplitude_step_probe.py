#!/usr/bin/env python3
"""qns_amplitude_step_probe — SF6: does the amplitude-form step hold along the
actual DN tail evolution?

EXPLORATORY PROBE (not production). Bean qou-g0dl (epic qou-a3n3).

The Phi chip (boundary_flux_tail_bound, PR #5058) closed the sup-in-time tail
bound conditional on the AMPLITUDE-FORM STEP:

  dOmega_tail/dt <= F*a - D*Omega_tail,

with a = u_{B+1} (first tail amplitude), F = 2*k_{B+1}^3*u_B^2 (the DN
boundary coupling, band-controlled), and D an effective tail damping. The
honest risk, named in the Lean docstring: the tail's INTERIOR enstrophy
transfer (the cascade term sum_{n>B+1} 2k_n^3 u_n u_{n-1}^2 - ...) is not
sign-definite — the step holds only if tail dissipation dominates interior
production. This probe measures it directly.

Protocol: unforced DN q-shell (the setting of the theorems), N = 32, band
B = 8, band-limited data (first 4 rungs), T = 50 eddy, eps swept. At sampled
steps with Omega_tail > 0, compute the EFFECTIVE DAMPING

  D_eff(n) = (F(n)*a(n) - dOmega_tail/dt(n)) / Omega_tail(n)

(the largest D for which the step holds at that instant). Verdicts:
  - min_t D_eff >= D_floor > 0 uniformly in eps  -> the amplitude-form step
    is VALIDATED in-model with that D (bean (a) closes at probe level)
  - min_t D_eff <= 0 at some times                -> interior production beats
    dissipation there; record when/how much (honest negative or transient)
Comparison scale: the naive dissipation floor 2*nu*k_{B+1}^2 (every tail
mode dissipates at least this fast) MINUS whatever the interior cascade eats.

Precision tier: float64 RK2 with adaptive CFL; dOmega/dt from the RK step
difference over dt. Run:
python3 -u computations/qns_amplitude_step_probe.py 2>&1 | tee /tmp/qns_sf6.log
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
    untouched so counts and flags keep their JSON types. Matches the
    qns-nonlocal-transfer sibling.
    """
    return fmt(x) if isinstance(x, float) else x


N = 32
BAND = 8
N_DATA = 4
T_EDDY = 50.0
EPS_SWEEP = (1e-1, 1e-2, 1e-3)
C_CFL = 5.0e-3
OMT_FLOOR = 1e-12   # skip D_eff samples when the tail is numerically empty


def run(eps: float):
    q = 1.0 + eps
    nu = eps / (2.0 * q)
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) if n < N_DATA else 0.0 for n in range(N)]
    dt_visc = 0.4 / (nu * k[-1] ** 2 + 1e-30)
    d_floor = 2.0 * nu * k[BAND] ** 2   # naive per-mode dissipation floor

    def rhs(v):
        out = []
        for n in range(N):
            um = v[n - 1] if n > 0 else 0.0
            up = v[n + 1] if n < N - 1 else 0.0
            kp = k[n + 1] if n < N - 1 else k[-1] * (k[-1] / k[-2])
            out.append(k[n] * um * um - kp * v[n] * up - nu * k[n] ** 2 * v[n])
        return out

    def omt(v):
        return sum(k[n] ** 2 * v[n] ** 2 for n in range(BAND, N))

    min_deff, min_deff_t = float("inf"), -1.0
    viol_steps, samples = 0, 0
    t, i, t0 = 0.0, 0, time.time()
    next_rep = 0.25
    while t < T_EDDY:
        cfl = max(k[n] * abs(u[n]) for n in range(N))
        dt = min(dt_visc, C_CFL / (cfl + 1e-30))
        om_before = omt(u)
        r1 = rhs(u)
        mid = [u[j] + 0.5 * dt * r1[j] for j in range(N)]
        r2 = rhs(mid)
        u_next = [u[j] + dt * r2[j] for j in range(N)]
        om_after = omt(u_next)
        if om_before > OMT_FLOOR:
            samples += 1
            domdt = (om_after - om_before) / dt
            a = u[BAND]                      # first tail amplitude u_{B+1}
            F = 2.0 * k[BAND] ** 3 * u[BAND - 1] ** 2
            deff = (F * a - domdt) / om_before
            if deff < min_deff:
                min_deff, min_deff_t = deff, t
            if deff <= 0.0:
                viol_steps += 1
        u = u_next
        t += dt
        i += 1
        if t / T_EDDY >= next_rep:
            el = time.time() - t0
            print(f"    [eps={eps:.0e}] {100 * t / T_EDDY:3.0f}%  "
                  f"minDeff={min_deff:.3e}@t={min_deff_t:.2f}  "
                  f"viol={viol_steps}/{samples}  elapsed={el:.0f}s", flush=True)
            next_rep += 0.25
    return min_deff, min_deff_t, viol_steps, samples, d_floor


def main() -> None:
    w = WitnessBuilder("qns-amplitude-step-probe", engine="python")
    print("=" * 76)
    print(f"SF6 amplitude-step probe: N={N}, B={BAND}, unforced band data, "
          f"T={T_EDDY} eddy")
    print("=" * 76)
    all_pos = True
    for eps in EPS_SWEEP:
        md, mt, viol, samp, dfl = run(eps)
        ratio = md / dfl if dfl > 0 else float("inf")
        all_pos &= (md > 0)
        w.add_data(f"eps{eps:.0e}_min_Deff", _f(md))
        w.add_data(f"eps{eps:.0e}_min_Deff_time", _f(mt))
        w.add_data(f"eps{eps:.0e}_violation_steps", viol)
        w.add_data(f"eps{eps:.0e}_samples", samp)
        w.add_data(f"eps{eps:.0e}_naive_floor", _f(dfl))
        w.add_data(f"eps{eps:.0e}_Deff_over_floor", _f(ratio))
        print(f"  eps={eps:.0e}: min D_eff={md:.4e} (at t={mt:.2f})  "
              f"violations {viol}/{samp}  naive floor={dfl:.3e}  "
              f"ratio={ratio:.2f}")

    w.add_assertion(
        "SCOPE-(a) REFUTATION for small eps: the amplitude-form step FAILS "
        "along the DN tail evolution during the cascade-front transient — "
        "D_eff goes strongly negative at eps <= 1e-2 (interior tail "
        "production beats dissipation + boundary accounting), while holding "
        "at eps = 1e-1",
        computed=(not all_pos), expected=True,
        source="min D_eff: +14.8 at eps=1e-1 (0 violations) but -22.1 at "
               "eps=1e-2 (682/3575 steps) and -23.1 at eps=1e-3 "
               "(3544/18567), all at t~0.32 — the cascade-front passage. "
               "The boundary_flux_tail_bound Lean theorem stands as a "
               "conditional; its in-model instantiation via THIS step form "
               "(single boundary amplitude, naive floor D) is refuted, "
               "scope (a): this form, this band, alone. The correct "
               "effective step must account interior production.",
    )
    w.set_description(
        "SF6 (bean qou-g0dl): probe-level validation of the amplitude-form "
        "step hypothesis of boundary_flux_tail_bound (PR #5058) — "
        "dOmega_tail/dt <= F*a - D*Omega_tail with a = u_{B+1}, "
        "F = 2 k_{B+1}^3 u_B^2 (the DN boundary coupling). Measures the "
        "effective damping D_eff pointwise along unforced DN runs (N=32, "
        "B=8, band-limited data, T=50 eddy) across eps; the step is "
        "validated iff min_t D_eff > 0. The named risk is the tail's "
        "interior cascade production (not sign-definite) vs tail "
        "dissipation. Scope (a); float64 RK2 exploratory tier; the Lean "
        "chain's remaining full-NS caveat (nonlocal transfer) is untouched "
        "by this probe."
    )
    w.add_data("tier", "exploratory")
    w.add_data("N", N)
    w.add_data("band", BAND)
    w.save()
    print("Saved witness: qns-amplitude-step-probe.witness.json")


if __name__ == "__main__":
    main()
