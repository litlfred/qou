"""q_parameter — back-compat shim. The canonical module is now
``qou_substrate.constants`` in ``tools/qou-substrate/``.

This file is a thin re-export so the 265 scripts in this directory that
do ``from q_parameter import Q, HA, ...`` keep working without
modification. New code should import from ``qou_substrate`` directly
once ``qou-substrate`` is on PyPI.

The substrate parameter is derived from CODATA m_p/m_e + SnapPy
Vol(4_1) (re-pinned 2026-05-28 from the muon anchor to the more precise
proton anchor — m_μ/m_e is now a prediction); see
``qou_substrate.constants`` for the full derivation docstring.

Promotion rationale: ``docs/workplans/2026-05-24-library-reuse-production-readiness.md``
Tier-2 item 2a.
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

# NOTE (2026-07-04): a local duplicate `_solve_q_proton_f64` used to live
# here, but it was dead code (underscore-private, uncalled — `from … import *`
# below does not re-export underscore names) and had drifted: it still
# embedded the fitted `(1 + 46u⁴)(1 + 4u⁵)(1 − 29u⁶)` habiro tower that the
# owner ruling 2026-07-03 stripped from the canonical solver and PR #3280
# dropped from the m_p producer. Removed to leave a single source of truth —
# the canonical `qou_substrate.constants._solve_q_proton_f64` (tower-free) —
# which can be imported directly from the canonical module if needed. This does
# NOT change `Q` / `Q_50_DIGIT_STR` (both are public names, so they DO come
# through the `import *` below). A separate, owner-gated q₀ re-pin of the
# canonical value is tracked outside this file (see PR #3302).

import sys
from pathlib import Path

try:
    import qou_substrate.constants as _qs_constants  # noqa: F401
except ImportError:
    _QOU_SUBSTRATE_PYTHON = (
        Path(__file__).resolve().parent.parent.parent.parent  # was: ...parent.parent.parent (pre-Phase-6 — substrate moved into substrate/, added one more .parent to reach repo root)
        / "tools" / "qou-substrate" / "python"
    )
    if _QOU_SUBSTRATE_PYTHON.is_dir() and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

from qou_substrate.constants import *  # noqa: F401,F403,E402


# ─────────────────────────────────────────────────────────────────────
# CANONICAL MUON-q₀ OVERRIDE (computations/ layer) — bean `yfvb`, 2026-07-06.
#
# The ~840 committed `computations/*.witness.json` are the muon-q₀ canonical
# derivation, but since the 2026-05-28 re-pin the `import *` above brings in the
# PROTON q₀ (`q_at()`).  Re-running any producer would drift its witness
# proton-ward by ~11.5 ppb (the `tnjb` bug).  The single faithful source of the
# canonical value is `q-pinning-50-digit.witness.json` — it matches NEITHER
# `q_at()` (proton) NOR `q_muon_at()` (a different muon closed form).  So here we
# re-derive the ENTIRE q-family (f64 + _MP + Q_50_DIGIT_STR) and re-define the
# q-closure functions from that witness, leaving the package layer
# (`qou_substrate.constants`) untouched (proton, for precision/prediction).
# Design + validation gate: docs/audits/2026-07-06-q0-producer-muon-refactor-design.md
try:
    import json as _json
    import math as _math
    from pathlib import Path as _P

    _QPIN = _P(__file__).resolve().parent.parent / "q-pinning-50-digit.witness.json"
    _d = _json.loads(_QPIN.read_text())["derived_50_digit"]
    if not _d["q"].startswith("1.109978595557"):
        raise ValueError(f"q-pinning witness q={_d['q'][:16]} not canonical muon")

    # ── f64 family ──
    # Take ONLY q from the witness (its f64 IS bit-identical to the committed
    # q0_f64), then derive every dependent with the SAME f64 ops as
    # constants.py lines 84-103 — NOT from the witness's q_inv/hbar_q strings,
    # which round ~1 ULP differently and would perturb dim_q at the ~15th digit.
    Q         = float(_d["q"])
    HBAR_Q    = 1.0 - 1.0 / Q
    HBAR_Q_SQ = HBAR_Q * HBAR_Q
    Q_INV     = 1.0 / Q
    HA        = Q - Q_INV
    E_CROSS   = 0.5 * HA
    S_SKEIN   = _math.sqrt(Q) - 1.0 / _math.sqrt(Q)
    TWO_Q     = Q + Q_INV
    TANH_LN_Q = HA / TWO_Q
    LN_Q      = _math.log(Q)
    Q_50_DIGIT_STR = _d["q"]

    # ── q-closure functions re-defined over the muon globals ──
    # (the imported `q_int`/`log_q` close over qou_substrate's PROTON globals;
    #  redefine here so `from q_parameter import q_int` gets the muon value.)
    def log_q(x, _LN_Q=LN_Q):
        return _math.log(x) / _LN_Q

    def q_int(n, _Q=Q, _QI=Q_INV, _HA=HA):
        return (_Q**n - _QI**n) / _HA

    def q_int_err(n, _Q=Q, _QI=Q_INV, _HA=HA, _QE=Q_ERR):
        num_deriv = n * (_Q**(n - 1) + _QI**(n + 1))
        denom_corr = (_Q**n - _QI**n) * (1 + _QI**2) / _HA
        return abs(num_deriv / _HA - denom_corr / _HA) * _QE

    # ── mpmath _MP family (mirror constants.py lines 249-266, muon base) ──
    try:
        import mpmath as _mp
        _prev = _mp.mp.dps
        _mp.mp.dps = max(_prev, 60)
        Q_MP         = _mp.mpf(_d["q"])
        Q_INV_MP     = _mp.mpf(1) / Q_MP
        HBAR_Q_MP    = _mp.mpf(1) - Q_INV_MP
        HBAR_Q_SQ_MP = HBAR_Q_MP ** 2
        HA_MP        = Q_MP - Q_INV_MP
        E_CROSS_MP   = HA_MP / 2
        S_SKEIN_MP   = _mp.sqrt(Q_MP) - _mp.mpf(1) / _mp.sqrt(Q_MP)
        TWO_Q_MP     = Q_MP + Q_INV_MP
        TANH_LN_Q_MP = HA_MP / TWO_Q_MP
        LN_Q_MP      = _mp.log(Q_MP)
        _mp.mp.dps = _prev
    except ImportError:
        pass
except Exception as _exc:  # leave proton values if witness unreadable
    import sys as _sys
    print(f"[q_parameter] muon override skipped: {_exc}", file=_sys.stderr)
