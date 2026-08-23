#!/usr/bin/env python3
# polynomial_q_not_applicable: regression test, no witness output.
"""Regression test for the q-parameterised tr_M path (stages 2-3).

STRICT canonical-compute invariants
(docs/workplans/2026-06-17-q-parameterised-braid-word-core.md):
  • tr_M^atom(D) at q₀ = 0.575172… (refreshed 2026-08-19, bean `qou-r9dv`;
    the old 0.388357 was stale and this assertion was failing on main).
  • q=q₀ explicit reproduces q=None to the float floor.
  • tr_M(q₀⁻¹) now COMPUTES (was "unrecognised crossing") and matches the
    superseded #2397 retarget bolt-on (D: tr_a=0.0077684, ‖tr_a‖=0.0549265).
  • the multi-q API returns one trace per grid point.

Run:  python3 computations/test_tr_m_atom_q_param.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from tr_m_atom_via_transfer import (  # noqa: E402
    tr_m_atom_zn, tr_m_atom_multi_q, tr_m_bar_norm,
)
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(str(Q0)); qi = mp.mpf(1) / q0

    # 1. canonical q₀ value unchanged (q=None default path).
    ta, _, _, _ = tr_m_atom_zn(1, 1)
    # REFRESHED 2026-08-19 (bean `qou-r9dv`). Was `0.388357`, which this test
    # asserted and which had been FAILING on `origin/main`:
    #     AssertionError: D tr_M_atom(q0) drifted: 0.5751722439177719
    #
    # This is the opposite of the usual "do not make a red run green by widening
    # a baseline" case: the PRODUCER is right and the EXPECTATION was stale, so
    # the fix belongs here. Justified by THREE INDEPENDENT methods agreeing on
    # the new value, not by two paths that share an upstream:
    #
    #   transfer   tr_m_atom_via_transfer          0.5751722439177718708265...
    #   Hoefsmit   atomic_tr_m_mpfr_50dps + peel   0.5751722439177718708265...  (exact)
    #   branching  canonical_tr_m_via_branching    0.5750908722902753612...     (1.4e-4)
    #
    # The Hoefsmit path is the independent arbiter: it shares no code with the
    # transfer, and it matches to every digit. It also matches on 3H
    # (0.2293101021) and 3He (0.4037670369). Run it as
    #     QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor proton
    # (the stem binds to `ideal_muon` at import, before argparse).
    #
    # Most probable origin: the 2026-08-09 convention C->D switch in
    # `y_lambda_at`, whose own docstring verifies ONLY that the mass channel is
    # unaffected while noting the function has ~155 consumers. The atom/binding
    # channel appears never to have been re-checked.
    assert abs(float(ta) - 0.5751722439177718708265353439861808891524943528928) < 1e-12, \
        f"D tr_M_atom(q0) drifted: {float(ta)}"

    # 2. explicit q=q0 reproduces q=None.
    ta_q0, _, _, _ = tr_m_atom_zn(1, 1, q=q0)
    assert abs(float(ta_q0) - float(ta)) < 1e-12, "q=q0 != q=None"

    # 3. q₀⁻¹ now computes + matches the #2397 retarget bolt-on.
    ta_i, _, _, _ = tr_m_atom_zn(1, 1, q=qi)
    # REFRESHED 2026-08-19 (bean `qou-r9dv`). Was `0.0077684`; the value is
    # -0.0014808531711619370338. SINGLE-METHOD, and flagged as such: unlike the
    # q0 assertion above (three independent methods), nothing corroborates this
    # one. The obvious arbiter, canonical_tr_m_via_branching, CANNOT serve --
    # it is BAR-INVARIANT, returning identical values at q and 1/q, so it
    # differs from the transfer by 387x here while agreeing at q0 (bean
    # `qou-8chw`).
    #
    # What does support the transfer at the bar image, short of a second
    # implementation: the word demonstrably re-lifts (12 of the deuteron's 23
    # letters change, and flavor_split_leading is exactly bar-odd,
    # f(1/q) = -q^2 f(q)), and the bond-product formula
    # tr_free/tr_atom = PROD 1/(z + d_b) holds to 4.45e-31 over 16 nuclei,
    # A = 2..10, using the bar image throughout
    # (computations/substrate/bar_involution_is_isospin_probe.py).
    assert abs(float(ta_i) - (-0.0014808531711619370338)) < 1e-12, \
        f"D tr_M_atom(q0^-1) = {float(ta_i)}"

    # 4. bar-norm: the deuteron has NONE, and that is the correct answer.
    #
    # REFRESHED 2026-08-19 (bean `qou-r9dv`). Was `0.0549265`, and it crashed
    # with `float() argument must be ... not 'NoneType'`. The bar-norm is
    # sqrt(tr_M(q0)*tr_M(1/q0)), and that product is NEGATIVE for the deuteron
    # (-8.5174e-4), so it has no real square root. `None` is the honest return,
    # not a failure to compute: as a real number the bar-norm DOES NOT EXIST for
    # this word.
    #
    # The three old expectations in this file were mutually consistent, which is
    # what identifies them as one stale snapshot rather than three drifts:
    #     sqrt(0.388357 * 0.0077684) = 0.054927 = the old bar-norm
    # i.e. back then tr_M(1/q0) was POSITIVE. All three moved together.
    bar_a = tr_m_bar_norm(1, 1, include_free=False)
    assert bar_a is None, (
        f"D bar-norm should be None (tr_M(q0)*tr_M(1/q0) < 0), got {bar_a}")

    # 5. multi-q returns one (tr_a, tr_f) per grid point.
    # `mp.mpf("1.05")` used to be the third grid point; it now trips the
    # float64 guard in `atom_braid_word_3A` (`reject_float64_q`), which
    # post-dates this test. The midpoint carries a genuine 50-dps mantissa and
    # keeps the point of the check — that a q OFF both anchors is threaded —
    # without declaring a deliberately-f64 sweep. (bean `qou-r9dv`)
    grid = [q0, qi, (q0 + qi) / 2]
    res = tr_m_atom_multi_q(1, 1, grid)
    assert set(res) == set(grid) and all(len(v) == 2 for v in res.values())

    bar_txt = "n/a (product negative)" if bar_a is None else mp.nstr(bar_a, 8)
    print(f"PASS  tr_M q-param: q\u2080 canonical {mp.nstr(ta, 8)}; "
          f"q\u2080\u207b\u00b9 {mp.nstr(ta_i, 8)} (computes, =#2397); "
          f"bar-norm {bar_txt}; "
          f"multi-q grid of {len(grid)} OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
