"""§S7 — Python consumer for the `PrecisionScalar` witness-JSON envelope.

Wire-format twin of the Rust struct in
`tools/hecke-engine/src/precision_scalar.rs` and the TypeScript
Zod schema in `folio-assistant/schemas/precision-scalar.ts`.

Shape:
    {"value": "1.10997859555418057528...", "dps": 50}

The producer emits high-precision values from `MpfrFloat` / `RationalReal`
as decimal strings tagged with their source precision, avoiding the
f64 round-trip that capped legacy witness JSON values at ~16 dps.

This module provides one routing helper:

  read_scalar(node) -> mpmath.mpf | float

If `node` is a plain number, return `float(node)` (legacy path).
If `node` is a `{"value": "...", "dps": int}` dict, parse via
`mpmath.mpf` at the recorded precision and return.

Consumers should call this for every numeric scalar pulled from a
witness JSON.  Ground-truth comparisons (CODATA matches, ppb
errors) should then use mpmath arithmetic, not float, so the
50-dps precision survives all the way to the comparison.

Per workplan
`tools/hecke-engine/CLARABEL_PRECISION_PLAN.md` §S7.4.
"""

from __future__ import annotations

from typing import Any, Union

try:
    import mpmath as _mp

    HAS_MPMATH = True

    def _mpf_at(value: str, dps: int) -> "_mp.mpf":
        """Parse a decimal string at the given dps via mpmath's
        scoped `workdps` context — thread-safe and never leaks
        the precision change to other concurrent users of the
        global `mpmath.mp.dps`."""
        with _mp.workdps(max(_mp.mp.dps, dps + 4)):
            return _mp.mpf(value)

    Scalar = Union[float, "_mp.mpf"]
except ImportError:
    HAS_MPMATH = False
    Scalar = float


def is_precision_scalar(node: Any) -> bool:
    """True iff `node` is a `PrecisionScalar` envelope dict."""
    return (
        isinstance(node, dict)
        and "value" in node
        and "dps" in node
        and isinstance(node["value"], str)
        and isinstance(node["dps"], int)
    )


def read_scalar(node: Any) -> Scalar:
    """Route a witness JSON scalar to the right Python representation.

    - Plain number -> `float(node)` (legacy path).
    - `PrecisionScalar` envelope -> `mpmath.mpf` at recorded precision.

    The mpmath path is engaged only if mpmath is importable; if not,
    a `RuntimeError` is raised so callers can detect the missing
    high-precision capability rather than silently dropping to f64.
    """
    if is_precision_scalar(node):
        if not HAS_MPMATH:
            raise RuntimeError(
                "read_scalar: cannot read PrecisionScalar without mpmath; "
                "install via `pip install mpmath` or convert via "
                "`float(node['value'])` if precision loss is acceptable"
            )
        return _mpf_at(node["value"], int(node["dps"]))
    if isinstance(node, (int, float)):
        return float(node)
    raise TypeError(
        f"read_scalar: expected number or PrecisionScalar envelope, "
        f"got {type(node).__name__}: {node!r}"
    )


def write_scalar(value: Scalar, dps: int = 50) -> dict | float:
    """Inverse of `read_scalar`: emit a witness-JSON-suitable
    representation.

    - For mpmath.mpf inputs: emit a `PrecisionScalar` envelope.
    - For float inputs: emit a plain f64 number (legacy path).
    """
    if HAS_MPMATH and isinstance(value, _mp.mpf):
        with _mp.workdps(max(_mp.mp.dps, dps + 4)):
            return {"value": _mp.nstr(value, dps, strip_zeros=False), "dps": dps}
    return float(value)


# ── Self-test (run as `python -m folio_assistant.computations.precision_scalar`) ─
if __name__ == "__main__":
    import json

    if HAS_MPMATH:
        _mp.mp.dps = 60
        x = _mp.mpf("1.10997859555418057528159407960950937799328227995869")
        env = write_scalar(x, dps=50)
        assert isinstance(env, dict), f"expected dict envelope, got {type(env)}"
        assert env["dps"] == 50
        # Round-trip via JSON string
        s = json.dumps(env)
        env2 = json.loads(s)
        x2 = read_scalar(env2)
        assert abs(x - x2) < _mp.mpf("1e-48"), f"round-trip drift > 1e-48: {x - x2}"
        print(f"[ok] PrecisionScalar round-trip: 50-dps q_0 → JSON → mpmath")
        print(f"     diff |x - x2| = {x - x2}")
    else:
        print("[skip] mpmath not installed; PrecisionScalar HP path unavailable")

    # Legacy-number path
    f = read_scalar(1.10997859555418057)
    assert isinstance(f, float)
    print(f"[ok] legacy float scalar: {f}")
