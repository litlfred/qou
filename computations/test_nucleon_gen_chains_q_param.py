#!/usr/bin/env python3
# polynomial_q_not_applicable: regression test, no witness output.
"""Regression test for the q-parameterised `nucleon_gen_chains`.

Guards the STRICT backward-compat invariant of the q-parameterised-braid-word
core refactor (docs/workplans/2026-06-17-q-parameterised-braid-word-core.md):
the default `q=None` path must be BYTE-IDENTICAL to the historical q₀ output,
so all ~124 existing consumers that omit `q` are unaffected. Also checks that
an explicit `q=q₀` reproduces `q=None`, and that `q=q₀⁻¹` materialises the
σ⁻¹/avg templates at the conjugate value (the bit that unlocks tr_M(q⁻¹)).

Run:  python3 computations/test_nucleon_gen_chains_q_param.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from pyhecke.atom import (  # noqa: E402
    nucleon_gen_chains, _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from q_parameter import Q as Q0  # noqa: E402


def main() -> int:
    mp.mp.dps = 50
    # 1. q=None is byte-identical to the precomputed module constants.
    g0n, g1n = nucleon_gen_chains(['u', 'u', 'd'])
    assert g0n == _PROTON_G0, "q=None proton g0 != _PROTON_G0"
    assert g1n == _PROTON_G1, "q=None proton g1 != _PROTON_G1"
    n0n, n1n = nucleon_gen_chains(['u', 'd', 'd'])
    assert n0n == _NEUTRON_G0, "q=None neutron g0 != _NEUTRON_G0"
    assert n1n == _NEUTRON_G1, "q=None neutron g1 != _NEUTRON_G1"

    # 2. explicit q=q0 reproduces q=None to the float floor.
    q0 = mp.mpf(str(Q0))
    g0q, g1q = nucleon_gen_chains(['u', 'u', 'd'], q=q0)
    md = max(abs(float(a[1]) - float(b[1])) for a, b in zip(g0q + g1q, g0n + g1n))
    assert md < 1e-9, f"q=q0 vs q=None max |Δd| = {md} too large"

    # 3. q=q0^-1 materialises the σ⁻¹ template at the conjugate value:
    #    g1[0] = (1, -h); h(q0^-1) = -h(q0), so d flips sign.
    qi = mp.mpf(1) / q0
    g0i, g1i = nucleon_gen_chains(['u', 'u', 'd'], q=qi)
    h0 = float(q0 - 1 / q0)
    assert abs(float(g1n[0][1]) - (-h0)) < 1e-12, "q0 σ⁻¹ template wrong"
    assert abs(float(g1i[0][1]) - (h0)) < 1e-9, "q0^-1 σ⁻¹ template not materialised"

    print("PASS  nucleon_gen_chains q-param: q=None byte-identical; "
          f"q=q0 reproduces (max|Δd|={md:.1e}); q=q0^-1 materialises (σ⁻¹ "
          f"d: {float(g1n[0][1]):.6f} → {float(g1i[0][1]):.6f}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
