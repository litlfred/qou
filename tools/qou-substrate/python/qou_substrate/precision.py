"""
qou_substrate.precision — shared precision infrastructure for QOU
compute scripts.

Centralizes the COMPUTE precision (mp.mp.dps) and the SERIALIZATION
precision used when emitting mpmath values into witness JSON.

USAGE
-----

At the top of any mpmath-based script::

    from qou_substrate import set_compute_dps, fmt
    # equivalently: from qou_substrate.precision import set_compute_dps, fmt

    set_compute_dps()           # set mp.mp.dps to COMPUTE_DPS (default 50)
    ...
    w.add_data("alpha", fmt(alpha))   # serialize at OUTPUT_DPS

Or with explicit per-script override::

    set_compute_dps(60)         # raise compute precision
    fmt(x, dps=50)              # override output dps for one value

WHY
---

mp.mp.dps controls the working precision of mpmath operations.  The
last few digits of any mp.mpf are inherently floor noise that varies
by:

  - mpmath version (the noise grows/shrinks with internal table sizes)
  - OS / libm version (transcendental functions like ``mp.sqrt`` lean
    on libm in some code paths)
  - Python interpreter rebuilds

Serializing values at full mp.dps with ``str(mpf)`` exposes those
trailing noise digits in committed witness JSON, which then drifts
between CI and local environments — producing reproducibility CI
failures even when the *physics* is bit-stable to ~45 digits.

The convention: COMPUTE at OUTPUT_DPS + GUARD digits, SERIALIZE at
OUTPUT_DPS.  GUARD = 10 by default (well below the precision a
single ``str(mpf)`` would expose).

ENVIRONMENT OVERRIDES
---------------------

Per-process overrides (useful in CI / sanity checks)::

    QOU_COMPUTE_DPS=60   python3 script.py     # raise compute precision
    QOU_OUTPUT_DPS=45    python3 script.py     # raise output precision
    QOU_PRECISION_GUARD=15  python3 script.py  # raise guard separately

CONSTANTS
---------

  COMPUTE_DPS_DEFAULT   = 70   (mp.mp.dps target)
  OUTPUT_DPS_DEFAULT    = 60   (serialization precision)
  PRECISION_GUARD_DEFAULT = 10 (COMPUTE = OUTPUT + GUARD)

  2026-05-31 (PR #1595 via 1ppq-qbeta queue probe-precision-headroom-bump):
  Bumped from 50/40/10 → 70/60/10. Rationale: 1 ppQ target (10⁻¹⁵)
  requires only 15 dps; previous defaults (65/50/15) already gave
  35 orders of magnitude headroom. New 70/60/10 gives 45 orders of
  magnitude headroom — pure future-proofing for sub-ppQ precision
  goals (1 part per quintillion = 10⁻¹⁸ → N ≥ log₁₀(10¹⁸)/2.07 − 1 ≈ 8
  rungs of the Q_β ladder, per qbeta_ck_truncation_order_analysis.py).
  Existing witnesses do NOT need regen — they remain mathematically
  valid at 50 dps. Future witnesses pick up the new defaults
  organically as scripts re-run.
"""
from __future__ import annotations

import os
from typing import Any
from mpmath import mp, mpf

# ── Defaults ────────────────────────────────────────────────────
# Bumped 2026-05-31 (PR #1595): 50→60 output, 65→70 compute. See
# top-of-file note. Existing witnesses don't need regen; new ones
# pick up the higher precision organically.
PRECISION_GUARD_DEFAULT: int = 10
OUTPUT_DPS_DEFAULT: int = 60
COMPUTE_DPS_DEFAULT: int = OUTPUT_DPS_DEFAULT + PRECISION_GUARD_DEFAULT  # 70

# ── Environment overrides ───────────────────────────────────────
def _env_int(key: str, default: int, minimum: int = 1) -> int:
    """Read a positive int from env ``key``, falling back to ``default``.

    Rejects unparseable values *and* values below ``minimum`` (default
    1) — ``mp.nstr(..., 0)`` raises and ``mp.dps = 0`` is meaningless,
    so we never accept ≤ 0 even when explicitly set in the env.
    """
    v = os.environ.get(key)
    if not v:
        return default
    try:
        parsed = int(v)
    except ValueError:
        return default
    if parsed < minimum:
        return default
    return parsed


COMPUTE_DPS: int = _env_int("QOU_COMPUTE_DPS", COMPUTE_DPS_DEFAULT)
OUTPUT_DPS: int = _env_int("QOU_OUTPUT_DPS", OUTPUT_DPS_DEFAULT)
PRECISION_GUARD: int = _env_int("QOU_PRECISION_GUARD", PRECISION_GUARD_DEFAULT)

# Auto-correct if env vars combine to violate guard
if COMPUTE_DPS - OUTPUT_DPS < PRECISION_GUARD:
    # Bump COMPUTE_DPS to keep the guard
    COMPUTE_DPS = OUTPUT_DPS + PRECISION_GUARD


def set_compute_dps(dps: int | None = None) -> int:
    """Set ``mp.mp.dps`` to ``dps`` (or ``COMPUTE_DPS`` if ``None``).

    Returns the actual value of ``mp.mp.dps`` after the set.
    Idempotent.
    """
    if dps is None:
        dps = COMPUTE_DPS
    mp.dps = dps
    return mp.dps


def str_at_true_precision(value: Any) -> str:
    """``str(value)``, except that a 53-bit value is not printed as if measured.

    **A drop-in for ``str(<mpf>)``, deliberately not for ``fmt(<mpf>)``.** The
    two disagree: ``fmt`` serializes at ``OUTPUT_DPS`` while ``str`` uses the
    live ``mp.dps``, and producers routinely set them to different values
    (``compute_dps: 70, output_dps: 60`` is typical). Routing the untouched
    path through ``fmt`` would quietly change the digit count of every value
    this helper is *not* meant to affect, so the fallback is ``str``.

    ``fmt`` writes every ``mpf`` at ``OUTPUT_DPS``. That is right for a value
    computed at full working precision and wrong for one that reached ``mpf``
    from a 53-bit source — an f64 kernel, a numpy trace, a float-valued dict
    entry. Printing *that* at 50 dps emits the binary64 expansion: 30+ digits
    of dyadic tail carrying no information and reading as measured.

        1.559758658103424178165141711360774934291839599609375
        vs the 1.5597586581034242 the kernel actually produced

    **The test is exact and per value: an mpf equal to its own float64 holds
    53 bits and nothing more.** No tolerance, and no flag that has to be kept
    in sync with the code. Per value matters because several producers can
    take either path at runtime — ``chi_numeric`` vs the numpy kernel, mpfr vs
    the f64 fallback — so a whole-producer decision is wrong for half the runs,
    and shortening a value that *did* carry more than 53 bits destroys real
    digits.

    A genuinely high-precision result that happens to be representable is not
    harmed: the short form is then exact, so the check cannot misfire in the
    direction of losing information.

    See ``docs/audits/2026-08-07-producer-repadding-empirical-sweep.md``.
    """
    # float64-intentional: this IS the representability test -- the whole
    # point is to detect a value that carries no more than 53 bits and
    # render it short. Measuring the nearest double is the function.
    if isinstance(value, mpf) and value == mpf(float(value)):
        return fmt(float(value))   # float branch of fmt == natural repr
    return str(value)


def fmt(value: Any, dps: int | None = None, strip_zeros: bool = False) -> str:
    """Serialize an mpmath value to its output-precision string form.

    Uses ``mp.nstr`` with ``OUTPUT_DPS`` (default) or an explicit per-
    call override.  ``strip_zeros=False`` keeps trailing zeros so
    JSON byte-stability is preserved across runs.

    Routing:

    - ``mpf`` (real) and ``mpc`` (complex): formatted via ``mp.nstr``
      at the requested precision — the canonical numeric path.
    - Everything else (``int``, ``float``, ``str``, ``Path``, lists,
      dicts, ``None``, …): short-circuited to ``str(value)`` without
      touching ``mp.nstr``.  ``int`` and ``float`` get their natural
      Python repr (no spurious mpf-promotion noise on a 0.1-style
      float).  Use ``str(...)`` directly for non-numeric witness
      fields; ``fmt`` tolerates them only as a safety net.
    """
    if dps is None:
        dps = OUTPUT_DPS
    from mpmath import mpc  # local import: mpc is rarely needed
    if isinstance(value, (mpf, mpc)):
        return mp.nstr(value, dps, strip_zeros=strip_zeros)
    return str(value)

# ── JSON-safe non-finite serialization ───────────────────────────
#
# WHY THIS EXISTS. `json.dump` writes bare `NaN`, `Infinity` and `-Infinity`
# by default. **JSON has no such tokens** — RFC 8259 numbers are finite
# decimals — so a witness containing one is not valid JSON and a strict
# parser rejects the whole file. Python's own `json.load` accepts them, which
# is why it goes unnoticed: the producer round-trips its own output happily.
#
# A 2026-08-09 sweep found 24 witnesses under `computations/` carrying one.
# The causes split cleanly in two, and they want DIFFERENT fixes:
#
#   1. A swallowed failure. `_habiro_coefficient_extract` wrote `float('nan')`
#      from a bare `except Exception`, hiding a real bug (a sympify `locals`
#      mapping the wrong name, so `.subs` silently no-opped). Fix the bug; do
#      NOT serialize the NaN.
#   2. A DELIBERATE sentinel for a genuine mathematical pole —
#      `casimir_macdonald_probe.macdonald_norm` returns `mpf("inf")` when the
#      arm-leg denominator vanishes (every arm-0 cell at t = 1,
#      Hall-Littlewood). The value is correct and meaningful; only the
#      serialization is invalid.
#
# Case 2 is what this helper is for, and its absence is the structural reason
# these literals kept appearing: a producer with a legitimate infinity had no
# sanctioned way to write it, so it wrote the bare literal.

NONFINITE_MARKERS = {"nan": "nan", "inf": "inf", "-inf": "-inf"}


def json_safe_float(value: Any) -> Any:
    """Return `value` unchanged if finite, else an explicit marker STRING.

    ``float('inf') -> "inf"``, ``float('-inf') -> "-inf"``, ``NaN -> "nan"``.

    Deliberately a marker rather than ``None``: a pole and a missing value are
    different facts, and ``null`` conflates them. Deliberately not ``1e999``
    either — that is how a non-finite becomes a silently wrong finite number.

    Use this ONLY where the non-finite is a real result (a pole, a divergent
    norm). If it came from a swallowed exception, fix the exception: a NaN
    standing in for "this computation failed" should be recorded as null
    ALONGSIDE the reason, not laundered into a marker that reads like a value.
    """
    import math as _math
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return value
    if isinstance(value, int):
        return value
    if _math.isnan(value):
        return NONFINITE_MARKERS["nan"]
    if _math.isinf(value):
        return NONFINITE_MARKERS["inf" if value > 0 else "-inf"]
    return value


# ── Audit / Precision Guard (qou-opm1) ───────────────────────────
# Expose mpmath aliases to prevent silent downcasting to float64 via `math`
mpsin = mp.sin
mpcos = mp.cos
mpsqrt = mp.sqrt
mpexp = mp.exp
mpasin = mp.asin
mpacos = mp.acos
mpatan2 = mp.atan2
mppi = mp.pi

# If the qou-opm1 audit sidecar parameter is enabled, we aggressively monkeypatch 
# the builtin math module so any accidental usage of `math.sin` immediately raises 
# an error or transparently promotes to `mp.sin` (preventing silent downcasting).
QOU_OPM1 = os.environ.get("QOU_OPM1", "0") in ("1", "true", "yes")

if QOU_OPM1:
    import math
    def _guard_downcast(name):
        def _guarded(*args, **kwargs):
            raise RuntimeError(
                f"Precision Guard (QOU_OPM1): Illegal downcast to float64 via math.{name}. "
                f"Use the mp{name} alias from qou_substrate.precision instead."
            )
        return _guarded
    
    math.sin = _guard_downcast("sin")
    math.cos = _guard_downcast("cos")
    math.sqrt = _guard_downcast("sqrt")
    math.exp = _guard_downcast("exp")
    math.asin = _guard_downcast("asin")
    math.acos = _guard_downcast("acos")
    math.atan2 = _guard_downcast("atan2")

# ── Topological Mass Ladder Witnesses ────────────────────────────
# Exact algebraic cyclotomic expansions generated by hecke-engine faddeev_fk
# over the quadratic extension field Q(sqrt(3)).
def f_3_witness():
    """Returns the exact 70-dps arbitrary precision Faddeev structural moment f_3.
    This corresponds to the pre-Archimedean topological mass limit mapping.
    """
    # f_3 = 2 + (7142821 / 6480) * sqrt(3)
    return mpf('2') + (mpf('7142821') / mpf('6480')) * mpsqrt(3)

def f_1_witness(): return -(mpf('7') / mpf('6')) * mpsqrt(3)
def f_2_witness(): return -(mpf('5407') / mpf('72')) + (mpf('1') / mpf('3')) * mpsqrt(3)
def f_4_witness(): return -(mpf('2774900693') / mpf('120960')) - (mpf('2461') / mpf('108')) * mpsqrt(3)
def f_5_witness(): return (mpf('8572817') / mpf('9720')) + (mpf('11795319232141') / mpf('97977600')) * mpsqrt(3)
