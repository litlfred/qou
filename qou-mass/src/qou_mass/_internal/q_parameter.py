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
del _sys, _Path

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
    # SEARCH upward rather than counting `.parent`s. A fixed count cannot be
    # right for both layouts this shim lives in: 3 up in computations/substrate/,
    # 5 up once the vendor sync flattens it into qou-mass/.../_internal/. The
    # hardcoded 4 was wrong in BOTH, so the fallback never fired anywhere; it
    # only stayed invisible because `import _path_bridge` normally puts the
    # substrate on sys.path first — and the vendor sync STRIPS that import.
    _QOU_SUBSTRATE_PYTHON = None
    for _anc in Path(__file__).resolve().parents:
        _cand = _anc / "tools" / "qou-substrate" / "python"
        if _cand.is_dir():
            _QOU_SUBSTRATE_PYTHON = _cand
            break
    if _QOU_SUBSTRATE_PYTHON is not None and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

from qou_substrate.constants import *  # noqa: F401,F403,E402


# ─────────────────────────────────────────────────────────────────────
# CAL-LAYER q₀ ANCHOR SELECTION (computations/ layer) — bean `yfvb`, 2026-07-06.
#
# Per the two-layer calibration convention (AGENTS.md §"q₀ anchor convention"):
#   • IDEAL / canonical 3-CAL  → q₀ is MUON-anchored (CAL-2 = 𝔇_β, proxy m_μ/m_e);
#     the canonical-derivation producers (~455 muon witnesses).
#   • PHYSICAL-Observations     → q₀ is PROTON-anchored (m_p/m_e, most precise);
#     the precision/prediction producers (~279 proton witnesses).
#
# The corpus is genuinely MIXED (sweep 2026-07-06: 279 proton + 455 muon), so a
# blanket flip is WRONG. This block applies the muon (ideal) anchor when EITHER
# (a) the caller opts in via the `QOU_Q0_ANCHOR` env var, OR (b) the env var is
# unset AND the running producer's stem is listed under `ideal_muon` in
# `q0_anchor_manifest.json` (the auto-select below). Everything else — env unset
# and stem not in `ideal_muon`, or an explicit physical/proton value — keeps the
# physical/proton anchor (the `import *` above, unchanged). So a canonical
# producer is muon either by its manifest tag or by exporting
# `QOU_Q0_ANCHOR=ideal`; a physical producer leaves it unset and is not tagged.
#
#   QOU_Q0_ANCHOR ∈ {ideal, muon, canonical}  → muon override (below)
#   QOU_Q0_ANCHOR unset / {physical, proton, experimental} → proton (no override)
#
# When muon is selected, we re-derive the ENTIRE q-family (f64 + _MP +
# Q_50_DIGIT_STR) and re-define the q-closures from `q-pinning-50-digit.witness.json`
# (the ONLY faithful muon source — matches NEITHER `q_at()` proton NOR the
# `q_muon_at()` closed form), leaving `qou_substrate.constants` untouched.
# Design + sweep + validation gate: docs/audits/2026-07-06-q0-producer-muon-refactor-design.md
import os as _os
import sys as _sys

# Resolve the anchor: explicit env var wins; else auto-select from the manifest
# by the running producer's stem (ideal_muon ⇒ muon; anything else ⇒ proton).
_anchor = _os.environ.get("QOU_Q0_ANCHOR", "").strip().lower()
if not _anchor:
    try:
        import json as _mj
        from pathlib import Path as _MP
        _man = _mj.loads((_MP(__file__).resolve().parent.parent
                          / "q0_anchor_manifest.json").read_text(encoding="utf-8"))
        _stem = _MP(_sys.argv[0]).stem if (_sys.argv and _sys.argv[0]) else ""
        if _stem in _man.get("ideal_muon", []):
            _anchor = "ideal"
    except Exception:
        pass

if _anchor in ("ideal", "muon", "canonical"):
  try:
    import json as _json
    import math as _math
    from pathlib import Path as _P

    _QPIN = _P(__file__).resolve().parent.parent / "q-pinning-50-digit.witness.json"
    _d = _json.loads(_QPIN.read_text(encoding="utf-8"))["derived_50_digit"]
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

    # ── derived uncertainty family, recomputed over the muon Q ──
    # The `import *` above brought PROTON-era Q_INV_ERR/HA_ERR/… (constants.py
    # lines 116-121); leaving them bound to the proton Q while Q itself is now
    # muon makes uncertainty propagation inconsistent for the ~6 downstream
    # importers (e.g. mass-from-q-symbolic.py imports HA_ERR/S_SKEIN_ERR/…).
    # Q_ERR stays the anchor's absolute q-uncertainty (~3.2e-12); only the
    # Q-dependent derivatives are re-evaluated at the muon point.
    Q_INV_ERR     = Q_ERR / Q**2
    HA_ERR        = Q_ERR * (1 + Q_INV**2)
    E_CROSS_ERR   = 0.5 * HA_ERR
    S_SKEIN_ERR   = Q_ERR * 0.5 * (Q**(-0.5) + Q**(-1.5))
    TWO_Q_ERR     = Q_ERR * abs(1 - Q_INV**2)
    TANH_LN_Q_ERR = Q_ERR * 2.0 / TWO_Q**2

    # ── mpmath _MP family (mirror constants.py lines 249-266, muon base) ──
    try:
        import mpmath as _mp
        # Owner directive 2026-07-06: "global dps 50 for compute accuracy".
        # The muon-anchored compute runs at a standing global precision of
        # 50 dps — this is the intended compute floor, NOT a temporary bump,
        # so it is set globally (superseding the workdps-restore of Copilot
        # #3419: 50 dps is where compute should stay). 50 dps ≫ the 1e-10
        # observable reproduction tolerance and the 1e-15 (1 ppQ) L1 target,
        # so it does not regress either precision leg; the q-pinning witness's
        # 70-digit q is read in full and only the compute working precision is
        # pinned at 50. Producers that need more raise it via set_compute_dps().
        _mp.mp.dps = max(_mp.mp.dps, 50)
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

        # ── q_at / q_str re-bound to the canonical MUON source ──
        # The imported `q_at`/`q_str` (from `import *`) Newton-solve the PROTON
        # pin, so a producer doing `from q_parameter import q_at; q_at(dps)` got
        # PROTON even under the ideal anchor — the bean-`yfvb` sweep (2026-07-06)
        # found this is why muon-committed producers still drifted proton-ward
        # (both the direct-`qou_substrate` importers and the ones already on
        # `q_parameter.q_at`). Re-bind to the 70-digit muon witness string so
        # `q_at(dps)` is muon-consistent at any working precision (the witness is
        # the ONLY faithful muon source — matches neither the proton solve nor the
        # `q_muon_at()` closed form). `dps` sets the mpf working precision; the 70
        # significant digits are the canonical muon ceiling.
        _MUON_Q_STR = _d["q"]

        def q_at(dps: int = 50, _s=_MUON_Q_STR, _m=_mp):
            prev = _m.mp.dps
            try:
                _m.mp.dps = max(prev, dps)
                return +_m.mpf(_s)
            finally:
                _m.mp.dps = prev

        def q_str(dps: int = 50, _s=_MUON_Q_STR, _m=_mp):
            return _m.nstr(_m.mpf(_s), dps, strip_zeros=False)
    except ImportError as _ie:
        # NO SILENT FALLBACK (owner directive 2026-07-06): under the ideal anchor
        # the caller explicitly asked for muon. mpmath is required to bind the
        # _MP family AND the muon `q_at`/`q_str`; without it those names stay the
        # proton values from `import *`, so a producer would silently emit PROTON
        # under an ideal request — exactly the tnjb corruption this branch closes.
        raise RuntimeError(
            "q_parameter: ideal/muon anchor requested (QOU_Q0_ANCHOR="
            f"{_anchor!r}) but mpmath is unavailable — cannot establish the muon "
            "q_at/_MP family; refusing to fall back to proton silently."
        ) from _ie
  except Exception as _exc:
    # NO SILENT FALLBACK: an unreadable/non-canonical q-pinning witness under the
    # ideal anchor must HARD-FAIL, not leave the proton `import *` values in place
    # (which would silently proton-drift the witness). A requested muon anchor that
    # cannot be satisfied is an error, never a silent proton result.
    raise RuntimeError(
        f"q_parameter: ideal/muon anchor requested (QOU_Q0_ANCHOR={_anchor!r}) but "
        f"the muon override could not be established: {_exc!r}. Refusing to fall "
        "back to proton silently (bean yfvb / tnjb anti-corruption)."
    ) from _exc
