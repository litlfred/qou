#!/usr/bin/env python3
# polynomial_q_not_applicable: regression test, no witness output.
"""Regression test for the q-parameterised tr_M path (stages 2-3).

STRICT canonical-compute invariants
(docs/workplans/2026-06-17-q-parameterised-braid-word-core.md):
  • tr_M^atom(D) at q₀ = 0.388357… (the #2080 cross-check) — UNCHANGED.
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
from q_parameter import Q as Q0  # noqa: E402


def main() -> int:
    mp.mp.dps = 50
    q0 = mp.mpf(str(Q0)); qi = mp.mpf(1) / q0

    # 1. canonical q₀ value unchanged (q=None default path).
    ta, _, _, _ = tr_m_atom_zn(1, 1)
    assert abs(float(ta) - 0.388357) < 1e-5, f"D tr_M_atom(q0) drifted: {float(ta)}"

    # 2. explicit q=q0 reproduces q=None.
    ta_q0, _, _, _ = tr_m_atom_zn(1, 1, q=q0)
    assert abs(float(ta_q0) - float(ta)) < 1e-12, "q=q0 != q=None"

    # 3. q₀⁻¹ now computes + matches the #2397 retarget bolt-on.
    ta_i, _, _, _ = tr_m_atom_zn(1, 1, q=qi)
    assert abs(float(ta_i) - 0.0077684) < 1e-6, f"D tr_M_atom(q0^-1) = {float(ta_i)}"

    # 4. bar-norm via the canonical path matches #2397.
    bar_a = tr_m_bar_norm(1, 1, include_free=False)
    assert abs(float(bar_a) - 0.0549265) < 1e-6, f"D bar-norm = {float(bar_a)}"

    # 5. multi-q returns one (tr_a, tr_f) per grid point.
    grid = [q0, qi, mp.mpf("1.05")]
    res = tr_m_atom_multi_q(1, 1, grid)
    assert set(res) == set(grid) and all(len(v) == 2 for v in res.values())

    print(f"PASS  tr_M q-param: q₀ canonical {float(ta):.6f} (unchanged); "
          f"q₀⁻¹ {float(ta_i):.7f} (computes, =#2397); bar-norm {float(bar_a):.7f}; "
          f"multi-q grid of {len(grid)} OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
