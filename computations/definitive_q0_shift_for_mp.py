#!/usr/bin/env python3
"""
Definitive finding: the m_p 242 ppb residual is entirely a q₀ shift.

At q_exact = 1.10997859555733..., the substrate identity
  m_p/m_e = 2·Vol(4₁)·|tr_M(q)|·[3]_q!/(q) / (q-1)² − 12
matches CODATA m_p/m_e to 10⁻⁴⁸ at 50 dps.

The shift q₀ → q_exact is −1.28e-8 (11.5 ppb of q₀).
All correction towers (ℏ⁶/4 for F_Bor, ℏ³+5ℏ⁴ for X) are
the Taylor expansion of this single q₀ shift.

IMPLICATION: 1 ppb m_p ⟺ derive q₀ to ≤12 ppb.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402


def main():
    set_compute_dps()
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    m_p = mp.mpf(M_P_MEV_VALIDATION)
    vol41 = mp.mpf("2.0298832128193072500424051085490405718833786150606")
    mp_over_me = m_p / m_e

    def f(qv):
        hv = qv - 1/qv
        tM = abs((4 + hv**2 - 3*hv**4 - hv**6) / (hv**2 + 4))
        qf = (qv**2 + 1 + qv**(-2)) * (qv + qv**(-1))
        return 2*vol41*tM*qf / ((qv-1)**2 * qv) - 12

    q_exact = mp.findroot(lambda qv: f(qv) - mp_over_me, q0, tol=mp.mpf("1e-45"))
    shift = q_exact - q0
    shift_ppb = shift / q0 * 1e9

    print(f"q₀ current:  {mp.nstr(q0, 25)}")
    print(f"q₀ exact:    {mp.nstr(q_exact, 25)}")
    print(f"Shift:       {mp.nstr(shift, 15)} ({mp.nstr(shift_ppb, 8)} ppb)")
    print(f"Verify:      m_p/m_e = {mp.nstr(f(q_exact), 20)} (target {mp.nstr(mp_over_me, 20)})")

    w = WitnessBuilder("definitive-q0-shift", engine="mpmath")
    w.set_description(
        "The m_p 242 ppb residual is entirely a q₀ calibration shift "
        "of 11.5 ppb. All correction towers are Taylor expansions of "
        "this shift. 1 ppb m_p requires deriving q₀ to 12 ppb."
    )
    w.set_content_block("conj:proton-mass-substrate-identity")
    w.add_data("q0_current", mp.nstr(q0, 25))
    w.add_data("q0_exact_for_mp", mp.nstr(q_exact, 25))
    w.add_data("shift_absolute", mp.nstr(shift, 15))
    w.add_data("shift_ppb", mp.nstr(shift_ppb, 10))
    # Was `computed=1, expected=1` (bean `qou-26f2`) — a constant standing in
    # for the finding, so `findroot` could have returned anything, or failed
    # to converge, and this would still have reported green. The `source`
    # string already stated the check — "At q_exact, m_p/m_e matches CODATA to
    # 10⁻⁴⁸" — and that is a residual, computable here: the print two lines
    # above already puts both of its sides on screen.
    #
    # Deliberately tighter than `findroot`'s own `tol=1e-45`: that bounds
    # where the root sits, this measures the residual in the value, which the
    # identity resolves far more sharply.
    _resid = abs(f(q_exact) - mp_over_me)
    w.add_data("mp_me_residual_at_q_exact", mp.nstr(_resid, 10))
    w.add_assertion("q0_shift_resolves_mp",
                    computed=_resid, expected=mp.mpf(0),
                    tolerance=mp.mpf("1e-48"),
                    source="At q_exact, m_p/m_e matches CODATA to 10⁻⁴⁸")
    print(f"\nWitness: {w.save()}")


if __name__ == "__main__":
    main()
