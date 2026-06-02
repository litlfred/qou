"""Shared substrate-quantities for Q_β categorical-derivation probes.

Centralizes the standard physics constants and intermediate quantities
used by the Q_β precision-ladder probes:

  - q_0 (CAL-2 substrate, loaded from q-pinning-50-digit.witness.json)
  - h, z, ℏ_q (substrate-derived)
  - α = (z-1)h/2 (single-wrap V_(2,1) eigenphase)
  - b = √(q⁴+q²+1)/(q²+1) (Hoefsmit off-diagonal coupling)
  - Q_A (Form A baseline from prop:neutron-qvalue-symbolic)
  - Q_AME (CODATA m_n - m_p - m_e at full mp precision)
  - α_N1 = α - b·ℏ_q²/2 (single-wrap Kashiwara-shifted eigenphase)

Avoids re-deriving these quantities in every probe script.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
from pathlib import Path

import mpmath as mp

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION

HERE = Path(__file__).resolve().parent


def q_0_at_50dps() -> mp.mpf:
    """CAL-2 substrate parameter at 50 dps from canonical pinning witness."""
    with (_pb.witness_path("q-pinning-50-digit.witness.json", HERE)).open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def compute_substrate_quantities() -> dict:
    """Return all substrate-derived quantities at current `mp.mp.dps`."""
    q = q_0_at_50dps()
    h = q - 1 / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    hbar_q = (q - 1) / q
    alpha = (z - 1) * h / 2
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)
    alpha_N1 = alpha - b * hbar_q ** 2 / 2

    m_e = mp.mpf(str(M_E_MEV))
    m_p = mp.mpf(str(M_P_MEV_VALIDATION))
    m_n = mp.mpf(str(M_N_MEV_VALIDATION))
    Q_AME = m_n - m_p - m_e

    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    return {
        "q": q,
        "h": h,
        "z": z,
        "hbar_q": hbar_q,
        "alpha": alpha,
        "alpha_N1": alpha_N1,
        "hoefsmit_b": b,
        "m_e": m_e,
        "m_p": m_p,
        "m_n": m_n,
        "Q_AME": Q_AME,
        "Q_A": Q_A,
    }


# Standard structural-coefficient predictions for the c_k precision
# ladder (per prop:q-beta-categorical-precision-ladder).
#   k=1: Kashiwara f̃_1 → coefficient = b (set per-call due to dps)
#   k=2: Kashiwara b²  → γ_2 = -1 (in γ_k = c_k / b^k convention)
#   k=3: Hopf at q=1   → c_3 = -2 (independent of b)
#   k=4: Mixed         → c_4 = b² + 1/2
# These are STRUCTURAL PREDICTIONS, not empirical fits.
def kashiwara_gamma_2() -> mp.mpf:
    """Structural prediction: γ_2 = -1 (so c_2 = -b² in (1 + γ_2 b² ℏ⁴) convention)."""
    return mp.mpf(-1)


def hopf_jones_classical_limit() -> mp.mpf:
    """J_Hopf(q=1) = -2 — classical-limit Hopf-link Jones polynomial."""
    return mp.mpf(-2)


def kashiwara_plus_half_c_4(b: mp.mpf) -> mp.mpf:
    """Structural prediction: c_4 = b² + 1/2 (Kashiwara b² + half-Hopf)."""
    return b ** 2 + mp.mpf("1/2")
