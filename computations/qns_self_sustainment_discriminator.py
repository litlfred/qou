#!/usr/bin/env python3
"""qns_self_sustainment_discriminator — SF2: is the eps->0 sustainment real or viscous?

EXPLORATORY PROBE (not production). Bean: SF2 (epic qou-a3n3).

SF1 found sustainment emerging at small eps over a FIXED 30-turnover horizon,
confounded by the viscous time >> horizon. This probe removes the confound:

  - horizon scaled to the viscous time: T = 1.5 * t_visc, t_visc = 1/(nu*k1^2)
  - classical same-nu CONTROL: identical DN dynamics with k_n = n (q=1
    wavenumbers) vs the q-system k_n = [n]_q, same nu = nu_q(eps), same
    Kolmogorov-shaped load in each system's own wavenumbers.

Discriminators, per eps:
  - S_q  = Om_end/Om_0 for the q-system at T = 1.5 t_visc
  - S_cl = Om_end/Om_0 for the classical control
  - R = S_q/S_cl : R ~ 1 -> no q-specific self-sustainment (SF1's horizon
    effect was viscous); R >> 1 -> genuine q-core self-forcing; R << 1 ->
    q-damping kills faster than classical.
Scope (a), model-level, exploratory tier (float64 RK2).
Run: python3 -u computations/qns_self_sustainment_discriminator.py 2>&1 | tee /tmp/qns_sf2.log
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

try:
    from _precision import fmt  # noqa: E402
except Exception:  # pragma: no cover - fallback keeps the probe runnable
    def fmt(value, dps=None, strip_zeros=False):  # type: ignore[misc]
        return str(value)


def _f(x):
    """Serialize float64-tier values as strings.

    Witnesses must not carry raw float64 (`computations/witness_raw_float64_audit.py`).
    These probes compute in the float64 tier by design, so the fix is at
    serialization, not at the numerics: `_precision.fmt` renders a float via
    `str()`, which round-trips exactly. Non-floats (int, bool, str, list) pass
    through untouched so counts and flags keep their JSON types.
    """
    return fmt(x) if isinstance(x, float) else x

N = 12
F_VISC = 1.5

def run(ks, nu):
    k = ks + [ks[-1] * (ks[-1] / ks[-2])]  # one extra for the transfer term
    u = [k[n] ** (-1.0 / 3.0) for n in range(N)]
    om0 = sum(k[n] ** 2 * u[n] ** 2 for n in range(N))
    t_eddy = 1.0 / (k[0] * u[0])
    t_visc = 1.0 / (nu * k[0] ** 2)
    T = F_VISC * t_visc
    dt = min(0.4 / (nu * k[N - 1] ** 2 + 1e-30), 0.02 * t_eddy)
    steps = int(T / dt)
    for _ in range(steps):
        def rhs(v):
            out = []
            for n in range(N):
                um = v[n - 1] if n > 0 else 0.0
                up = v[n + 1] if n < N - 1 else 0.0
                out.append(k[n] * um * um - k[n + 1] * v[n] * up - nu * k[n] ** 2 * v[n])
            return out
        r1 = rhs(u)
        mid = [u[i] + 0.5 * dt * r1[i] for i in range(N)]
        r2 = rhs(mid)
        u = [u[i] + dt * r2[i] for i in range(N)]
    om = sum(k[n] ** 2 * u[n] ** 2 for n in range(N))
    return om / om0, steps

def main() -> None:
    w = WitnessBuilder("qns-self-sustainment-discriminator", engine="python")
    print("=" * 76)
    print(f"SF2 discriminator: T = {F_VISC}*t_visc, q-system vs classical same-nu control")
    print("=" * 76)
    all_ratio_near_1 = True
    for e in (1, 2, 3):
        eps = 10.0 ** (-e)
        q = 1.0 + eps
        nu = eps / (2.0 * q)
        kq = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
        kc = [float(n) for n in range(1, N + 1)]
        sq, st1 = run(kq, nu)
        sc, st2 = run(kc, nu)
        R = sq / sc if sc > 0 else float("inf")
        near1 = 0.2 < R < 5.0
        all_ratio_near_1 = all_ratio_near_1 and near1
        w.add_data(f"eps_1e-{e}_S_q",_f(sq))
        w.add_data(f"eps_1e-{e}_S_classical",_f(sc))
        w.add_data(f"eps_1e-{e}_R",_f(R))
        print(f"  eps=1e-{e}: S_q={sq:.4e}  S_cl={sc:.4e}  R={R:.3f}  steps={st1}/{st2}  "
              f"{'~viscous (no q-sustainment)' if near1 else 'DIVERGENT BEHAVIOUR'}")
    w.add_assertion(
        "q-system tracks the classical same-nu control at the viscous-scaled "
        "horizon (R within [0.2, 5]) at every tested eps — SF1's small-eps "
        "sustainment was the viscous timescale, NOT q-specific self-forcing",
        computed=all_ratio_near_1, expected=True,
        source=f"T = {F_VISC}*t_visc; DN model; eps = 1e-1..1e-3; scope (a)",
    )
    w.set_description(
        "SF2 (epic qou-a3n3): removes SF1's confound by scaling the horizon to "
        "the viscous time (T = 1.5/nu k1^2) and running a classical same-nu "
        "control (k_n = n) against the q-system (k_n = [n]_q). If the enstrophy "
        "survival ratio R = S_q/S_cl stays near 1, the small-eps sustainment "
        "seen in SF1 is the viscous timescale and NOT genuine q-core "
        "self-forcing; the unforced finite core then decays at every eps on its "
        "own clock, and the sustained-forcing blow-up channel requires "
        "EXTERNAL or infinite-dimensional sustainment — sharpening the hard "
        "core once more. R >> 1 would instead be evidence of q-specific "
        "self-sustainment. Scope (a); exploratory tier; float64 RK2."
    )
    w.add_data("tier",_f("exploratory"))
    w.add_data("f_visc",_f(F_VISC))
    w.save()
    print("Saved witness: qns-self-sustainment-discriminator.witness.json")

if __name__ == "__main__":
    main()
