#!/usr/bin/env python3
"""
proton_identity_extension_audit.py — audit whether the proton
substrate identity extends to the neutron + ⁴He.

## Conclusion

The substrate identity

  y_(3)(q_0) · (m_p + 12·m_e) = 2 · m_μ · |tr_M(β_Bor, q_0)|

is **specific to the proton's β_Bor + H_3 structure**:

- **Neutron**: solving N for `m_n = 2·m_μ·F_Bor − N·m_e` gives
  N ≈ 9.469 — NOT a clean integer.  The neutron derivation goes
  through `m_n = m_p + Δm_pn` via canonical Hecke-skein flavor-split
  (prop:flavor-split-substrate), NOT via its own substrate identity.

- **⁴He**: uses H_12 (12-strand atomic braid, n_0 = 3A = 12), not
  H_3 (β_Bor).  The identity's ingredients (|tr_M(β_Bor)|, [3]_q!,
  q^3) are H_3-specific.  ⁴He extension would need:
  |tr_M(T_w_⁴He)| + [12]_q! + canonical ⁴He dominant-partition q-power.

- **N_neutron − N_proton = −2.531 = −Δm_pn/m_e**: confirms the
  proton's "N=12" and the neutron's "N≈9.47" differ by exactly
  the n-p mass splitting in m_e units — the flavor-split structure.

## Implication

The proton-mass substrate identity is one element of a categorical
chain:
  - m_p:  via β_Bor + 12·m_e correction (this identity)
  - m_n:  via m_p + canonical Δm_pn (flavor-split skein)
  - ⁴He:  via per-atom canonical T_w + Wedderburn structure
        (different equation, not this identity)

The identity is therefore best understood as a SPECIFIC categorical
relation at the proton's H_3 level, not a universal mass formula.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    M_E_MEV,
    M_MU_MEV_VALIDATION,
)


def q_int(q, n):
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def main():
    set_compute_dps()
    q = Q_MP
    h = q - 1 / q
    m_e = mpf(M_E_MEV)  # registry (no inline literal)
    m_mu = mpf(M_MU_MEV_VALIDATION)  # registry (no inline literal)
    m_p = mpf(M_P_MEV_VALIDATION)
    m_n = mpf(M_N_MEV_VALIDATION)

    qfact_3 = q_int(q, 3) * q_int(q, 2) * q_int(q, 1)
    trM_lean = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    y_3 = q ** 3 / qfact_3
    F_Bor = trM_lean / y_3  # = |tr_M|·[3]_q!/q^3

    N_proton = (2 * m_mu * F_Bor - m_p) / m_e
    N_neutron = (2 * m_mu * F_Bor - m_n) / m_e
    Delta_npn_over_me = (m_n - m_p) / m_e

    print("=" * 76)
    print("  Proton-identity extension audit (β_Bor → neutron, ⁴He)")
    print("=" * 76)
    print()
    print("  Solve N in m_X = 2·m_μ·F_Bor − N·m_e:")
    print()
    print(f"  N_proton  = {mp.nstr(N_proton, 14)}  → near-integer 12 (Δ = "
          f"{mp.nstr(N_proton - 12, 12)})")
    print(f"  N_neutron = {mp.nstr(N_neutron, 14)}  → NOT a clean integer "
          f"(Δ from 9.5 = {mp.nstr(N_neutron - mpf('9.5'), 8)})")
    print()
    print(f"  N_proton − N_neutron = {mp.nstr(N_proton - N_neutron, 14)}")
    print(f"  Δm_pn / m_e          = {mp.nstr(Delta_npn_over_me, 14)}")
    print(f"  Match: {N_proton - N_neutron - Delta_npn_over_me} (should be 0)")
    print()
    print("  Verdict: identity is specific to PROTON / β_Bor / H_3.")
    print("  Neutron derivation goes through m_p + canonical Δm_pn (skein flavor-split),")
    print("  NOT via its own substrate identity with integer N.")

    w = WitnessBuilder("proton-identity-extension-audit", engine="mpmath")
    w.set_description(
        "Tests whether the proton mass substrate identity "
        "m_p = 2·m_μ·F_Bor − 12·m_e generalises to the neutron and ⁴He. "
        "Result: the identity is specific to β_Bor + H_3.  For the neutron, "
        "N_neutron ≈ 9.469 is NOT a clean integer; the neutron derivation "
        "uses m_p + canonical Δm_pn (Hecke-skein flavor-split) instead.  ⁴He "
        "uses H_12 / different braid, so the identity's ingredients (|tr_M(β_Bor)|, "
        "[3]_q!, q^3) don't directly apply.  The identity is one element of a "
        "categorical chain, not a universal mass formula."
    )
    w.set_audit_only("docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md")
    w.add_parameter("q0", mp.nstr(q, 25))
    w.add_data("N_proton", mp.nstr(N_proton, 25))
    w.add_data("N_neutron", mp.nstr(N_neutron, 25))
    w.add_data("Delta_npn_over_m_e", mp.nstr(Delta_npn_over_me, 25))
    w.add_data("N_diff_minus_Delta_pn", mp.nstr(N_proton - N_neutron - Delta_npn_over_me, 25))
    w.add_data("identity_is_proton_specific", True)
    w.add_data("neutron_via_flavor_split_not_own_identity", True)

    w.add_assertion(
        name="N_proton_near_integer_12",
        computed=abs(N_proton - 12),
        expected=0.0,
        tolerance=1e-3,
        source="N_proton solving the identity should be near integer 12 (0.24 ppm match).",
    )
    w.add_assertion(
        name="N_neutron_NOT_clean_integer",
        computed=abs(round(N_neutron) - N_neutron) > mpf("0.4"),
        expected=1.0,
        tolerance=1e-12,
        source="N_neutron should NOT be close to any integer (off by ~0.47), confirming the identity is proton-specific.",
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
