#!/usr/bin/env python3
"""Audit of the two cosh/GPMT levers on the scored γγ V³ base (beans qou-cds1, qou-pdix).

The bridge probe `qbeta_pdix_cds1_cosh_gpmt_bridge_probe.py` scores two
levers on the census words (`nuc11_*`, `nuc9`, `delta_S`). This probe asks
what the same two levers do on the base the dashboard scores today: V³ =
(σ₁σ₂⁻¹)³ for both nucleons, with the T³ weight-space trace Tr(K^{⊗3}·)/[2]³
(conditional on conjectures C1-C3, PR #8617). The 3x3 matrices are copied from
`per_observable_100x_status._qbeta_conditional_t3_split`. The probe checks that
its base reproduces that row (0.325433928735 MeV).

Lever A: does the full twist Δ² = (σ₁σ₂σ₁)² insert into the trace as the
uniform factor cosh(6 ln q)? Δ² is central and acts by a scalar on each
irreducible: q⁶ on (3), 1 on (2,1), q⁻⁶ on (1³). The weight spaces W_p and W_n
are 3-dimensional and carry only (3) ⊕ (2,1). So the q⁻⁶ that the "mirror
average" (q⁶+q⁻⁶)/2 relies on is not present here. Two things are computed:
  (i)  base·cosh(6 ln q)        — the bridge probe's lever, applied as written;
  (ii) the base computed with Δ²·V³ in place of V³ — the full twist actually inserted.
Neither closes the gap: F stays far above 1.

Lever B: GPMT adds a modified trace on (1³). The weight spaces carry no (1³),
so on this trace the correction is zero by construction. The probe asserts the
Δ² spectrum is {q⁶, 1, 1} on both weight spaces, which rules out (1³).

All arithmetic is mpmath at 60 dps. There are no fitted parameters and no
choice by residual. This probe emits no witness.
"""
from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/substrate", "computations/qbeta", "tools/qou-substrate/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

from mpmath import cosh, log, matrix, mp, mpf, nstr  # noqa: E402

mp.dps = 60

from codata_2022_source import M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qbeta_e0 import canonical as e0_canonical  # noqa: E402

def _recorded_v3_mev():
    """The dashboard's Q_beta pred_MeV, read from the witness rather than typed in."""
    import json
    with open(os.path.join(ROOT, "computations", "per-observable-100x-status.witness.json")) as fh:
        dash = json.load(fh)
    rows = dash["data"]["rows"] if "data" in dash else dash["rows"]
    return mpf(next(r for r in rows if r.get("obs") == "Q_beta")["pred_MeV"])


RECORDED_V3_MEV = _recorded_v3_mev()   # dashboard Q_beta row, pred_MeV
Q_CODATA_MEV = mpf("0.78233355931")       # CODATA 2022 registry value (owner ruling 2026-11-20)


def main() -> int:
    q = mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    d2 = q + qi
    A1 = matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
    A2 = matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
    B1, B2 = A2, A1

    def tr(M):
        return M[0, 0] + M[1, 1] + M[2, 2]

    def leg(T1, T2, pre):
        V = T1 * T2 ** -1
        V3 = V * V * V
        D = (T1 * T2 * T1) ** 2
        return pre * tr(V3) / d2 ** 3, pre * tr(D * V3) / d2 ** 3, D

    ep, ep_tw, DA = leg(A1, A2, q)
    en, en_tw, DB = leg(B1, B2, qi)
    E0 = e0_canonical(q=q, m_e=M_E_MEV)
    base = abs(en - ep) * E0
    cosh6 = cosh(6 * log(q))
    lever_a_as_written = base * cosh6
    lever_a_inserted = abs(en_tw - ep_tw) * E0

    tol = mpf(10) ** -40
    checks = []

    def check(name, ok, detail):
        checks.append(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    check("base_reproduces_dashboard_V3", abs(base - RECORDED_V3_MEV) < mpf("1e-12"),
          f"base = {nstr(base, 15)} MeV vs recorded {RECORDED_V3_MEV}")
    for lab, D in (("W_p", DA), ("W_n", DB)):
        ev = sorted(mp.eig(D)[0], key=lambda x: abs(x))
        want = [mpf(1), mpf(1), q ** 6]
        ok = all(abs(a - b) < tol for a, b in zip(ev, want))
        check(f"full_twist_spectrum_{lab}_is_q6_1_1", ok,
              "Δ² eigenvalues " + ", ".join(nstr(x, 12) for x in ev)
              + f" (q⁶ = {nstr(q**6, 12)}); no q⁻⁶, so no (1³) block and the GPMT term is 0")
    F_a = Q_CODATA_MEV / lever_a_as_written
    F_i = Q_CODATA_MEV / lever_a_inserted
    check("lever_A_as_written_does_not_close_on_V3", F_a > 1,
          f"base·cosh(6 ln q) = {nstr(lever_a_as_written, 12)} MeV, F = {nstr(F_a, 9)}")
    check("lever_A_inserted_full_twist_does_not_close_on_V3", F_i > 1,
          f"Δ²-inserted = {nstr(lever_a_inserted, 12)} MeV, F = {nstr(F_i, 9)}, "
          f"ratio to base {nstr(lever_a_inserted / base, 10)} ≠ cosh6 {nstr(cosh6, 10)}")
    check("inserted_twist_is_not_the_uniform_cosh_factor",
          abs(lever_a_inserted / base - cosh6) > mpf("1e-3"),
          f"|ratio − cosh6| = {nstr(abs(lever_a_inserted / base - cosh6), 6)}")
    print(f"{sum(checks)}/{len(checks)} checks passed")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
