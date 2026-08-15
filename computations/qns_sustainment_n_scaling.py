#!/usr/bin/env python3
"""qns_sustainment_n_scaling — SF3: does sustainment re-emerge as N grows?

EXPLORATORY PROBE (not production). Bean: SF3 (epic qou-a3n3).

SF2 showed the unforced finite q-core decays like its classical control at
every tested eps — the sustained channel needs external forcing or an
INFINITE-DIMENSIONAL escape. SF3 tests the escape route directly: sweep the
truncation N at fixed eps and measure whether the enstrophy survival ratio at
the viscous-scaled horizon GROWS with N (sustainment re-emerging as N -> inf)
or stays flat (uniform-in-N decay — the strongest in-model regularity
picture, closing the escape at the shell-model level).

Same DN dynamics as SF1/SF2: k_n = [n]_q, nu_q = (q-1)/(2q), Kolmogorov load,
T = 1.5 * t_visc. Measured per N: S(N) = Om_end/Om_0 and the q/classical
ratio R(N). Scope (a); exploratory tier (float64 RK2).
Run: python3 -u computations/qns_sustainment_n_scaling.py 2>&1 | tee /tmp/qns_sf3.log
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

EPS = 1.0e-2
F_VISC = 1.5
N_SWEEP = (8, 12, 16, 20, 24)

def run(N, ks, nu):
    k = ks + [ks[-1] * (ks[-1] / ks[-2])]
    u = [k[n] ** (-1.0 / 3.0) for n in range(N)]
    om0 = sum(k[n] ** 2 * u[n] ** 2 for n in range(N))
    t_eddy = 1.0 / (k[0] * u[0])
    T = F_VISC / (nu * k[0] ** 2)
    dt = min(0.4 / (nu * k[N - 1] ** 2 + 1e-30), 0.02 * t_eddy)
    for _ in range(int(T / dt)):
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
    return sum(k[n] ** 2 * u[n] ** 2 for n in range(N)) / om0

def main() -> None:
    w = WitnessBuilder("qns-sustainment-n-scaling", engine="python")
    q = 1.0 + EPS
    nu = EPS / (2.0 * q)
    print("=" * 76)
    print(f"SF3: N-sweep at eps={EPS}, T={F_VISC}*t_visc — does sustainment grow with N?")
    print("=" * 76)
    Ss, Rs = [], []
    for N in N_SWEEP:
        kq = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
        kc = [float(n) for n in range(1, N + 1)]
        sq = run(N, kq, nu)
        sc = run(N, kc, nu)
        R = sq / sc if sc > 0 else float("inf")
        Ss.append(sq); Rs.append(R)
        w.add_data(f"N{N}_S_q",_f(sq))
        w.add_data(f"N{N}_R",_f(R))
        print(f"  N={N:2d}: S_q={sq:.4e}  R={R:.3f}")
    flat_S = max(Ss) / max(min(Ss), 1e-300)
    flat_R = all(0.2 < r < 5.0 for r in Rs)
    grows = Ss[-1] > 10.0 * Ss[0]
    w.add_data("S_spread",_f(flat_S))
    w.add_assertion(
        "Survival is uniform in N (no growth of S_q with truncation; the "
        "infinite-dimensional escape does NOT open at the shell-model level)",
        computed=(not grows), expected=True,
        source=f"S_q across N={N_SWEEP}: spread {flat_S:.2e}; scope (a): this "
               "model/load/eps, alone",
    )
    w.add_assertion(
        "q/classical ratio stays near 1 across the N sweep",
        computed=flat_R, expected=True,
        source="R(N) within [0.2, 5] for all N",
    )
    w.set_description(
        "SF3 (epic qou-a3n3): tests the infinite-dimensional escape route left "
        "open by SF2 — sweep truncation N in (8..24) at fixed eps=1e-2, unforced "
        "DN q-shell (k_n=[n]_q), viscous-scaled horizon, with classical same-nu "
        "controls. If survival S_q(N) grows with N, sustainment re-emerges toward "
        "N->inf (escape open); if uniform, the unforced decay is N-uniform and "
        "the escape closes at the shell-model level — leaving external forcing "
        "as the only in-model route to the sustained channel. Scope (a); "
        "exploratory tier; float64 RK2."
    )
    w.add_data("tier",_f("exploratory"))
    w.add_data("eps",_f(EPS))
    w.save()
    print("Saved witness: qns-sustainment-n-scaling.witness.json")

if __name__ == "__main__":
    main()
