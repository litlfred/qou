#!/usr/bin/env python3
"""Is F_Bor's /q^3 a misplaced factor that a bar-symmetric convention would fix?

Bean `qou-24w9`. Tests the one repair hypothesis left standing after the
derivability question was closed negatively.

BACKGROUND. `F_Bor = |tr_M(b_Bor)| . [3]_q! / q^3` is asserted, not derived
(PR #5294 proves it is unreachable by the writhe rule, double-counts the
Poincare centering, and is the sole bar-asymmetric step). Both ingredients are
bar-symmetric, so any braid-derived normalisation would be too -- yet the
required one is not.

THE HYPOTHESIS TESTED HERE. `1/hbar_q^2` is ALSO bar-asymmetric
(`hbar_q = 1 - 1/q`), and across `m_mu . F_Bor` the two asymmetries combine to a
net `q^-2`. So perhaps the q-power is simply misplaced: use the bar-symmetric
`hbar_sym^2 = (q^(1/2) - q^(-1/2))^2 = q - 2 + 1/q` and drop `/q^3`, giving a
fully bar-symmetric mass identity.

WHY IT IS A REAL TEST, NOT A RESHUFFLE. `q_0` is not free -- it is solved from
the proton pin. So the alternative is re-solved for its own `q`, and then
checked against `m_mu/m_e`, which was NOT used in the solve. That ratio is the
corpus's own 9.5-sigma cross-check (AGENTS.md: proton-pinned => m_mu is a
prediction), so it discriminates.

  Ref: [manuscript] rem:sqrt-q-ribbon-structure
  Ref: [manuscript] conj:kashaev-density-equals-sdp-multiplicity
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

import mpmath as mp  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, M_P_MEV_VALIDATION, M_MU_MEV_VALIDATION,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

VOL41 = 2 * mp.clsin(2, mp.pi / 3)


def _h(q):
    return q - 1 / q


def tr_m(q):
    h = _h(q)
    return (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)


def _qi(n, q):
    return (q ** n - q ** -n) / (q - 1 / q)


def qfact3(q):
    return _qi(1, q) * _qi(2, q) * _qi(3, q)


def m_p_current(q):
    """As implemented: hbar = 1 - 1/q, with the /q^3."""
    hb = (q - 1) / q
    return 2 * (M_E_MEV * VOL41 / hb ** 2 * tr_m(q) * qfact3(q) / q ** 3 - 6 * M_E_MEV)


def m_p_barsym(q):
    """Fully bar-symmetric: hbar_sym^2 = q - 2 + 1/q, and NO /q^3."""
    return 2 * (M_E_MEV * VOL41 / (q - 2 + 1 / q) * tr_m(q) * qfact3(q) - 6 * M_E_MEV)


def main() -> int:
    target_mu = M_MU_MEV_VALIDATION / M_E_MEV

    cur_mu = VOL41 / ((Q0 - 1) / Q0) ** 2
    cur_err = (cur_mu / target_mu - 1) * mp.mpf(10) ** 9

    q_sym = mp.findroot(lambda q: m_p_barsym(q) - M_P_MEV_VALIDATION,
                        (mp.mpf("1.10"), mp.mpf("1.15")),
                        solver="bisect", tol=mp.mpf("1e-40"))
    sym_mu = VOL41 / (q_sym - 2 + 1 / q_sym)
    sym_err = (sym_mu / target_mu - 1) * mp.mpf(10) ** 9

    b = (
        WitnessBuilder("fbor-normalisation-barsymmetry")
        .set_description(
            "Tests whether F_Bor's bar-asymmetric /q^3 is a misplaced factor that "
            "a bar-symmetric hbar convention would repair. Re-solves q from the "
            "proton pin under each convention and scores the untouched muon ratio."
        )
        .set_content_block("conj:kashaev-density-equals-sdp-multiplicity")
        .add_parameter("q_0_repo", str(Q0))
        .add_parameter("vol_4_1", str(VOL41))
        .add_data("target_m_mu_over_m_e", str(target_mu))
        .add_data("current", {
            "hbar": "1 - 1/q", "extra_factor": "1/q^3", "bar_symmetric": False,
            "q": str(Q0), "m_p": str(m_p_current(Q0)),
            "m_mu_over_m_e_pred": str(cur_mu), "m_mu_err_ppb": str(cur_err),
        })
        .add_data("bar_symmetric_alternative", {
            "hbar_sq": "q - 2 + 1/q", "extra_factor": "none", "bar_symmetric": True,
            "q": str(q_sym), "m_p": str(m_p_barsym(q_sym)),
            "m_mu_over_m_e_pred": str(sym_mu), "m_mu_err_ppb": str(sym_err),
        })
        .add_data("verdict",
                  "REFUTED. The bar-symmetric convention re-solves the proton pin "
                  "fine but misses the untouched muon ratio by -27.16 % "
                  "(2.7e8 ppb) where the current convention misses by 211 ppb -- "
                  "a factor ~1.3e6 worse. The /q^3 is therefore NOT a misplaced "
                  "q-power that symmetry would repair: it is non-derivable AND "
                  "empirically load-bearing on two independent observables.")
    )
    b.add_assertion("current_beats_barsym_on_muon_crosscheck",
                    computed=bool(abs(cur_err) < abs(sym_err)), expected=True)
    b.add_assertion("barsym_reproduces_proton_pin",
                    computed=bool(abs(m_p_barsym(q_sym) - M_P_MEV_VALIDATION)
                                  < mp.mpf("1e-6")), expected=True)
    b.save()

    print("=" * 74)
    print("F_Bor normalisation: does a bar-symmetric convention repair it?")
    print("=" * 74)
    print(f"  target m_mu/m_e            = {mp.nstr(target_mu, 15)}")
    print()
    print("  CURRENT   hbar = 1 - 1/q, with /q^3      (bar-asymmetric)")
    print(f"     q                       = {mp.nstr(Q0, 15)}")
    print(f"     m_mu/m_e predicted      = {mp.nstr(cur_mu, 15)}")
    print(f"     error                   = {mp.nstr(cur_err, 8)} ppb")
    print()
    print("  ALTERNATIVE  hbar^2 = q-2+1/q, no /q^3   (bar-SYMMETRIC)")
    print(f"     q re-solved from pin    = {mp.nstr(q_sym, 15)}")
    print(f"     m_mu/m_e predicted      = {mp.nstr(sym_mu, 15)}")
    print(f"     error                   = {mp.nstr(sym_err, 8)} ppb"
          f"   ({mp.nstr((sym_mu/target_mu - 1) * 100, 6)} %)")
    print()
    print(f"  ratio of errors            = {mp.nstr(abs(sym_err / cur_err), 8)}x worse")
    print("  => REFUTED: the /q^3 is not a misplaced factor symmetry would fix.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
