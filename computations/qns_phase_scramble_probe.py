#!/usr/bin/env python3
"""qns_phase_scramble_probe — SF11: isolate the PHASE effect from the
triad-structure confound of SF10.

EXPLORATORY PROBE (not production). Bean qou-ougq (epic qou-a3n3).

SF10 (PR #5083) found sup|u_n|(Sabra) > sup u_n(real DN) at every
(seed, eps) — but named the confound: Sabra triads include
inflow-from-above, so the cross-model ratio mixes phase dynamics with
triad structure. This probe removes the confound by comparing the SAME
Sabra model against ITSELF with phases scrambled:

  coherent run:   the SF10 Sabra evolution, untouched
  scrambled run:  identical, except at a fixed cadence every rung's
                  phase is replaced by a deterministic hash phase
                  (moduli untouched — energy is preserved exactly by
                  the scramble; only phase COHERENCE is destroyed)

Two cadences: every step (full decorrelation — the sweeping-dominated
limit) and every 0.1 eddy (partial). The phase hash is deterministic
(no RNG state): phi(n, j) = 2*pi*frac(R*(n+1)*(j+13) + S*(n+7)),
j = scramble counter, R/S irrational.

Verdict variable: the scramble ratio on tail rungs

  s_n = sup|u_n|(scrambled) / sup|u_n|(coherent)

  s_n <= 1 everywhere -> phase decorrelation WEAKENS (or preserves)
  tail excitation: the coherent evolution is the worst case, so the
  fully-coherent real-amplitude models of the SF arc are CONSERVATIVE
  with respect to sweeping/decorrelation, and SF10's cross-model
  amplification is attributable to triad structure, not phases.

  s_n > 1 somewhere -> decorrelation amplifies: honest negative, the
  sweeping caveat has teeth in-model.

Also re-measured on the scrambled runs: the modulus equilibrium ratio
r_n (the rung_equilibrium_forced instance) — the Lean-backed form
should hold regardless of phases (the triangle bound is phase-free).

Precision tier: float64 complex RK2 adaptive CFL (SF10 integrator).
Run:
python3 -u computations/qns_phase_scramble_probe.py 2>&1 | tee /tmp/qns_sf11.log
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
DELTA = 0.5
WINDING = (math.sqrt(5.0) - 1.0) / 2.0          # golden initial phases
HASH_R = math.pi - 3.0                           # irrational hash multipliers
HASH_S = math.e - 2.0
CADENCES = {"full": 0.0, "partial": 0.1}         # scramble interval in eddy
C_CFL = 5.0e-3
N_CAP = 400
SUP_FLOOR = 1e-20


def ladder_len(eps: float) -> int:
    return min(N_CAP, int(math.ceil(math.log(3.0) / math.log(1.0 + eps))))


def make_rhs_sabra(N, k, nu):
    def rhs(v):
        out = []
        for n in range(N):
            up1 = v[n + 1] if n < N - 1 else 0.0j
            up2 = v[n + 2] if n < N - 2 else 0.0j
            um1 = v[n - 1] if n > 0 else 0.0j
            um2 = v[n - 2] if n > 1 else 0.0j
            kp1 = k[n + 1] if n < N - 1 else 0.0
            km1 = k[n - 1] if n > 0 else 0.0
            nl = (kp1 * up1.conjugate() * up2
                  - DELTA * k[n] * um1.conjugate() * up1
                  + (1.0 - DELTA) * km1 * um1 * um2)
            out.append(1j * nl - nu * k[n] ** 2 * v[n])
        return out
    return rhs


def hash_phase(n: int, j: int) -> float:
    x = HASH_R * (n + 1) * (j + 13) + HASH_S * (n + 7)
    return 2.0 * math.pi * (x - math.floor(x))


def run_sabra(eps: float, scramble_interval: float | None):
    """scramble_interval: None = coherent; 0.0 = every step; > 0 = eddy
    interval between scrambles."""
    q = 1.0 + eps
    N = ladder_len(eps)
    nu = eps / (2.0 * q)
    k = [(q ** n - 1.0) / (q - 1.0) for n in range(1, N + 1)]
    u = [k[n] ** (-1.0 / 3.0) * cmath.exp(2j * math.pi * WINDING * n)
         if n < N_DATA else 0.0j for n in range(N)]
    sup_u = [abs(x) for x in u]
    dt_visc = 0.4 / (nu * k[-1] ** 2 + 1e-30)
    rhs = make_rhs_sabra(N, k, nu)

    t, i, t0 = 0.0, 0, time.time()
    jscr = 0
    next_scr = 0.0 if scramble_interval is not None else float("inf")
    next_rep = 0.25
    while t < T_EDDY:
        if t >= next_scr:
            jscr += 1
            u = [abs(u[n]) * cmath.exp(1j * hash_phase(n, jscr))
                 for n in range(N)]
            next_scr = (t + scramble_interval if scramble_interval > 0.0
                        else t)          # 0.0 -> re-scramble every step
            if scramble_interval == 0.0:
                next_scr = -1.0          # trigger on every iteration
        cfl = max(k[n] * abs(u[n]) for n in range(N))
        dt = min(dt_visc, C_CFL / (cfl + 1e-30))
        r1 = rhs(u)
        mid = [u[j] + 0.5 * dt * r1[j] for j in range(N)]
        r2 = rhs(mid)
        u = [u[j] + dt * r2[j] for j in range(N)]
        for n in range(N):
            a = abs(u[n])
            if a > sup_u[n]:
                sup_u[n] = a
        t += dt
        i += 1
        if t / T_EDDY >= next_rep:
            el = time.time() - t0
            tag = ("coh" if scramble_interval is None
                   else f"scr{scramble_interval}")
            print(f"    [{tag} eps={eps:.0e}] N={N}  "
                  f"{100 * t / T_EDDY:3.0f}%  steps={i}  elapsed={el:.0f}s",
                  flush=True)
            next_rep += 0.25
    return sup_u, k, nu, N


def modulus_ratio(sup_u, k, nu, N):
    ratios = []
    for n in range(N_DATA, N):
        if sup_u[n] < SUP_FLOOR:
            continue
        sup = lambda m: sup_u[m] if 0 <= m < N else 0.0
        kp1 = k[n + 1] if n < N - 1 else 0.0
        km1 = k[n - 1] if n > 0 else 0.0
        F = (kp1 * sup(n + 1) * sup(n + 2)
             + DELTA * k[n] * sup(n - 1) * sup(n + 1)
             + (1.0 - DELTA) * km1 * sup(n - 1) * sup(n - 2))
        if F > 0.0:
            ratios.append(sup_u[n] * (nu * k[n] ** 2) / F)
    return (max(ratios) if ratios else 0.0), len(ratios)


def main() -> None:
    w = WitnessBuilder("qns-phase-scramble-probe", engine="python")
    print("=" * 76)
    print(f"SF11 phase-scramble probe: Sabra vs phase-scrambled Sabra, "
          f"cadences {dict(CADENCES)}, T={T_EDDY} eddy")
    print("=" * 76)
    all_s_ok, all_r_ok = True, True
    for eps in EPS_SWEEP:
        sup_coh, k, nu, N = run_sabra(eps, None)
        for cad_name, interval in CADENCES.items():
            sup_scr, _, _, _ = run_sabra(eps, interval)
            svals = [sup_scr[n] / sup_coh[n] for n in range(N_DATA, N)
                     if sup_scr[n] > SUP_FLOOR and sup_coh[n] > SUP_FLOOR]
            max_s = max(svals) if svals else 0.0
            r_max, nrat = modulus_ratio(sup_scr, k, nu, N)
            s_ok = max_s <= 1.0
            r_ok = r_max <= 1.0
            all_s_ok &= s_ok
            all_r_ok &= r_ok
            w.add_data(f"{cad_name}_eps{eps:.0e}_max_scramble_ratio",
                       _f(max_s))
            w.add_data(f"{cad_name}_eps{eps:.0e}_max_modulus_ratio",
                       _f(r_max))
            w.add_data(f"{cad_name}_eps{eps:.0e}_n_compared", len(svals))
            print(f"  cad={cad_name} eps={eps:.0e}: max s_n={max_s:.3f} "
                  f"({'decorrelation weakens' if s_ok else 'AMPLIFIES'}, "
                  f"{len(svals)} rungs)  max r_n={r_max:.3f} "
                  f"({'OK' if r_ok else 'VIOL'})")

    w.add_assertion(
        "phase decorrelation does NOT amplify the tail: the scramble "
        "ratio s_n = sup|u_n|(scrambled)/sup|u_n|(coherent) <= 1 on every "
        "excited tail rung, at both cadences (every-step and 0.1-eddy) "
        "and every eps — the coherent evolution is the in-model worst "
        "case, so the SF arc's fully-coherent real-amplitude models are "
        "CONSERVATIVE with respect to sweeping/decorrelation, and SF10's "
        "cross-model amplification is attributable to triad structure, "
        "not phase coherence",
        computed=all_s_ok, expected=True,
        source="max s_n per (cadence, eps) over tail rungs excited in "
               "both runs; deterministic hash phases, moduli untouched",
    )
    w.add_assertion(
        "the modulus damped-forced form (rung_equilibrium_forced "
        "instance) holds on the SCRAMBLED runs too: r_n <= 1 on every "
        "excited empty-start rung — the Lean-backed route is "
        "phase-insensitive, as the triangle bound predicts",
        computed=all_r_ok, expected=True,
        source="max r_n per (cadence, eps) on scrambled runs",
    )
    w.set_description(
        "SF11 (bean qou-ougq): isolates the phase effect from SF10's "
        "triad-structure confound by comparing the complex Sabra q-shell "
        "against itself with deterministically hash-scrambled phases "
        "(moduli untouched, energy preserved by the scramble) at two "
        "cadences. s_n <= 1 means decorrelation weakens tail excitation "
        "and the coherent model is the worst case. Scope (a); float64 "
        "complex RK2 exploratory tier; sweeping in full NS also advects "
        "structures spatially, which no shell model represents — the "
        "residual caveat, now narrowed to spatial advection only."
    )
    w.add_data("tier", "exploratory")
    w.add_data("delta", _f(DELTA))
    w.add_data("cadences_eddy", {k2: _f(v) for k2, v in CADENCES.items()})
    w.add_data("n_cap", N_CAP)
    w.add_data("n_data", N_DATA)
    # AGENTS.md §"q0 anchor convention" rule 4: say which pin you used. This
    # probe uses NONE. The `q` here is the Sabra/DN shell-spacing ratio
    # q = 1 + eps with eps in EPS_SWEEP — a ladder parameter of the turbulence
    # model, nothing to do with the substrate modulus. That eps = 1e-1 puts it
    # at 1.1, next door to q_0 ~ 1.10998, is a coincidence and exactly why this
    # needs saying out loud rather than being left to a reader's inference.
    # Nothing in the import cone (_path_bridge — sys.path only; qou_substrate.
    # witness; _precision) reads q_parameter, constants.Q, or y_lambda_at.
    #
    # So the honest record is `independent`, not the standing proton default:
    # stamping a pin the compute never read is the misrecord this field exists
    # to prevent. Via save(extra=...) and NOT add_data(), which nests under
    # `data` where the audit reading body["q0Anchor"] cannot see it. No
    # q0Value — there is no value, and one here is a Q0_FLIP.
    w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Sabra/DN shell model: the only q here is the shell-spacing ratio "
            "q = 1 + eps swept over EPS_SWEEP, not the substrate modulus. "
            "eps = 1e-1 gives q = 1.1, adjacent to q0 = 1.10998 — coincidence, "
            "and the reason this needs stating rather than inferring. Import "
            "cone reaches no q_parameter and no qou_substrate.constants."
        ),
    })
    print("Saved witness: qns-phase-scramble-probe.witness.json")


if __name__ == "__main__":
    main()
