"""Keystone final number — solve τ = tr(B) from the SL₂ recurrence.

With the depth fixed at 2 (`s5_bring_hodge_depth.py`) and `det B = 1`
(symplectic polarisation, `prop:sl2-prolongation-recurrence`), the kernel
is `R = x² − τ·x + 1` — a SINGLE unknown `τ = tr B`. The recurrence
`a_{n+2} = τ·a_{n+1} − a_n` then gives `τ` from any three consecutive
prolonged periods:

    τ = (a_n + a_{n+2}) / a_{n+1} .

Self-validation: the torus periods `P_m = cosh((2m+1)η₀)/(2cosh η₀)` satisfy
`det = 1` with `τ = 2cosh(2η₀)`; this module recovers that from `P_1,P_2,P_3`
and verifies the recurrence on every window through `P_5`. For the hyperbolic
binding sector,
`a_D⁽⁴⁾` = Family-A is wired; `a_D⁽²⁾, a_D⁽³⁾` are gated on #1765 — those
three values then yield `τ` (hence `R`, hence P1 unconditional).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
for _p in (str(_HERE.parent), str(_HERE)):
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402


def tau_from_three(a_n, a_n1, a_n2):
    """τ = (a_n + a_{n+2}) / a_{n+1} from the SL₂ recurrence
    a_{n+2} = τ·a_{n+1} − a_n (det = 1)."""
    return (a_n + a_n2) / a_n1


def verify_recurrence(seq, tau, tol):
    """Check a_{n+2} = τ·a_{n+1} − a_n on every window of `seq`."""
    return all(
        abs(tau * seq[i + 1] - seq[i] - seq[i + 2]) <= tol
        for i in range(len(seq) - 2)
    )


def _torus_P(m, eta0):
    return mp.cosh((2 * m + 1) * eta0) / (2 * mp.cosh(eta0))


def _emit_witness() -> None:
    from witness_base import WitnessBuilder
    from q_parameter import Q_50_DIGIT_STR as Qs

    mp.mp.dps = COMPUTE_DPS
    eta0 = mp.log(mp.mpf(Qs))
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 8))

    # Torus self-validation (m = 1..5 ⇒ P_1..P_5).
    P = [_torus_P(m, eta0) for m in range(1, 6)]
    tau = tau_from_three(P[0], P[1], P[2])      # from P_1,P_2,P_3
    expected = 2 * mp.cosh(2 * eta0)
    solved_ok = abs(tau - expected) < tol
    recur_ok = verify_recurrence(P, tau, tol)

    w = WitnessBuilder("sl2-tau-solver", engine="mpmath")
    w.set_audit_only(
        "docs/workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md"
    )
    w.add_parameter("q_0", Qs)
    w.add_data("torus_tau_solved", mp.nstr(tau, 16))
    w.add_data("torus_tau_expected_2cosh2eta", mp.nstr(expected, 16))
    w.add_data("binding_tau_status",
               "τ for the binding sector needs a_D^(2),a_D^(3) from #1765 "
               "(a_D^(4)=Family-A wired); then τ=(a_D^(2)+a_D^(4))/a_D^(3)")
    w.add_assertion("torus_tau_eq_2cosh2eta", computed=int(solved_ok),
                    expected=1, source="τ=(P_1+P_3)/P_2 = 2cosh(2η₀)")
    w.add_assertion("torus_recurrence_det1_holds", computed=int(recur_ok),
                    expected=1, source="P_{m+2}=τ·P_{m+1}−P_m on all windows (det=1)")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = COMPUTE_DPS
    from q_parameter import Q_50_DIGIT_STR as Qs
    eta0 = mp.log(mp.mpf(Qs))
    P = [_torus_P(m, eta0) for m in range(1, 6)]
    tau = tau_from_three(P[0], P[1], P[2])
    print("SL₂ τ-solver (det B = 1 ⇒ R = x² − τx + 1)")
    print(f"  torus τ = (P_1+P_3)/P_2 = {mp.nstr(tau, 12)}")
    print(f"  expected 2cosh(2η₀)     = {mp.nstr(2*mp.cosh(2*eta0), 12)}")
    print(f"  recurrence det=1 holds on all windows: "
          f"{verify_recurrence(P, tau, mp.mpf(10)**(-(COMPUTE_DPS-8)))}")
    print("  binding τ: needs a_D^(2),a_D^(3) from #1765 (a_D^(4)=Family-A wired)")
    _emit_witness()
