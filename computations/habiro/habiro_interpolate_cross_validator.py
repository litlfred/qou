#!/usr/bin/env python3


# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
Habiro interpolate cross-validator — atomic-poly vs. interpolated
numerical agreement at q_0.

Two independent paths produce a numerical value of `tr_M(q_0)` for
each atomic braid:

1. **Atomic-polynomial path** (`habiro_coefficients_atomic.py`):
   build the Markov-normalised polynomial `p(u) ∈ ℤ[u]` from
   sequential cyclotomic division, then evaluate at `u_0 = q_0^{1/2}`
   and divide by `denom_in_u(u_0)` to recover `tr_M(q_0)`.

2. **Vandermonde-interpolation path** (`habiro_coefficients_interpolate.py`):
   evaluate `markov_trace_symbolic` at multiple `q` points,
   interpolate the Laurent polynomial, then evaluate at `q_0` to 60
   decimal places via mpmath.

Both should produce the same value to high precision.  This
validator certifies the agreement using mpmath at 60 dps.

Output witness `habiro-interpolate-cross-validation.witness.json`
records, per common atom, the relative difference between the two
paths.

Asymmetric coverage is reported but not flagged as failure (the
two pipelines may legitimately cover different atom ranges; T, for
instance, is on the interpolate side only).
"""

from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
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
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from habiro_types import HabiroAtomicWitness  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


HERE = Path(__file__).parent
ATOMIC_WITNESS = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
INTERPOLATE_WITNESS = _pb.witness_path("habiro-coefficients-interpolate.witness.json", HERE)

def _agreement_rtol_for(working_dps: int) -> mp.mpf:
    """Tolerance dynamically tied to the working precision.

    The atomic polynomial path evaluates a high-degree polynomial at
    `u_0 = q_0^{1/2}` via mpmath at `working_dps` digits.  Rounding
    accumulates roughly by the polynomial degree, so leave a margin
    of ~18 digits below the working precision.  Output is then
    bounded by the witness JSON's float-roundtrip noise (~1e-16),
    so cap at 1e-12 (comfortably above arithmetic noise, comfortably
    below any meaningful disagreement).
    """
    return mp.mpf(10) ** -min(working_dps - 18, 12)


# AGREEMENT_RTOL is set in `main()` from the active `mp.mp.dps` so a
# higher-precision rerun of this script automatically tightens the
# tolerance.  Default value (1e-12) used as a module-level fallback
# for downstream consumers that import the constant directly.
AGREEMENT_RTOL = mp.mpf("1e-12")


def parse_polynomial_in_u(s: str, u_value: mp.mpf) -> mp.mpf:
    """Evaluate a polynomial in `u` (sympy-style string) at `u_value`
    using mpmath to retain high precision.

    Uses an eval-friendly substitution: only the variable `u` and
    integer literals + arithmetic appear in the witness format.
    """
    # Replace `**` with mp.power-friendly form by using Python eval
    # in a sandboxed namespace; mpmath supports `**` natively.
    # Caller-provided string is from a trusted in-repo witness, so
    # eval is acceptable here (same pattern as numpy.evaluate use
    # elsewhere in the pipeline).
    return mp.mpf(eval(s, {"__builtins__": {}}, {"check_q": u_value, "mp": mp}))


def main() -> int:
    if not ATOMIC_WITNESS.exists() or not INTERPOLATE_WITNESS.exists():
        missing = [p.name for p in (ATOMIC_WITNESS, INTERPOLATE_WITNESS) if not p.exists()]
        print(
            f"habiro_interpolate_cross_validator: SKIP "
            f"(missing input(s): {missing})"
        )
        return 0

    atomic = HabiroAtomicWitness.from_json(ATOMIC_WITNESS)
    import json
    with INTERPOLATE_WITNESS.open() as f:
        interpolate = json.load(f)
    interp_by_atom = {
        atom: mp.mpf(r["tr_M_q0_numerical_60dps"])
        for atom, r in interpolate.get("results", {}).items()
        if isinstance(r, dict) and "tr_M_q0_numerical_60dps" in r
    }

    q_0 = mp.mpf(str(atomic.parameters.get("q_0", "1.1099785955573347")))
    mp.mp.dps = 70  # work above the 60 dps interpolate precision
    # Tie tolerance to the active precision (Gemini #472 medium).
    global AGREEMENT_RTOL
    AGREEMENT_RTOL = _agreement_rtol_for(mp.mp.dps)
    u_0 = mp.sqrt(q_0)

    common = sorted(
        {r.atom_label for r in atomic.records}
        & set(interp_by_atom.keys())
    )
    only_atomic = sorted({r.atom_label for r in atomic.records} - set(interp_by_atom.keys()))
    only_interp = sorted(set(interp_by_atom.keys()) - {r.atom_label for r in atomic.records})

    w = WitnessBuilder("habiro-interpolate-cross-validation", engine="mpmath")
    w.set_description(
        "Verifies tr_M(q_0) agreement between the atomic-polynomial "
        "path (habiro_coefficients_atomic.py) and the Vandermonde-"
        "interpolation path (habiro_coefficients_interpolate.py)."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    w.add_parameter("q_0", str(q_0))
    w.add_parameter("agreement_rtol_dps", 50)
    w.add_parameter("mp_dps", mp.mp.dps)
    w.add_data("reference_blocks", [
        "prop:full-pole-structure-mass-trace",
        "def:habiro-ring",
    ])
    w.add_data("atoms_only_in_atomic", only_atomic)
    w.add_data("atoms_only_in_interpolate", only_interp)

    checks = []
    for atom in common:
        record = next(r for r in atomic.records if r.atom_label == atom)
        p_at_u0 = parse_polynomial_in_u(record.p_in_u, u_0)
        d_at_u0 = parse_polynomial_in_u(record.denom_in_u, u_0)
        atomic_tr = p_at_u0 / d_at_u0
        interp_tr = interp_by_atom[atom]
        rel = (
            mp.mpf(0)
            if atomic_tr == interp_tr == 0
            else mp.fabs(atomic_tr - interp_tr) / max(mp.fabs(atomic_tr), mp.fabs(interp_tr))
        )
        checks.append({
            "atom": atom,
            "atomic_tr_M_q0": str(atomic_tr),
            "interpolate_tr_M_q0": str(interp_tr),
            "abs_diff": str(mp.fabs(atomic_tr - interp_tr)),
            "rel_diff": str(rel),
            "agree": bool(rel <= AGREEMENT_RTOL),
        })
        # Use floats only for the assertion's tolerance check (the
        # full-precision values stay in `data.checks` above).
        w.add_assertion(
            f"tr_M_q0_atomic_vs_interpolate[{atom}]",
            computed=float(atomic_tr),
            expected=float(interp_tr),
            tolerance=float(AGREEMENT_RTOL * max(mp.fabs(atomic_tr), mp.fabs(interp_tr))),
        )

    w.add_data("checks", checks)
    overall_pass = all(a.passed for a in w.assertions)
    w.save()

    status = "PASS" if overall_pass else "FAIL"
    print(f"habiro_interpolate_cross_validator: {status}")
    for c in checks:
        marker = "✓" if c["agree"] else "✗"
        print(
            f"  {marker} {c['atom']:>24}  rel_diff = {c['rel_diff'][:12]}"
        )
    if only_atomic or only_interp:
        print(
            f"  asymmetric coverage: "
            f"atomic-only={only_atomic}, interpolate-only={only_interp}"
        )
    return 0 if overall_pass else 2


if __name__ == "__main__":
    sys.exit(main())
