#!/usr/bin/env python3
"""
Faddeev/Rogers modular-double transformation on the GS categorical net.

Applies the analytic continuation t -> i*t (the modular double / two-saddle
crossing) to the categorical GS net departure Q_beta^GS/Q_A - 1, and checks
that it carries the cosh-like departure (leading +t^2) to the cos-like shape
of the observable ladder (leading -t^2).

Scope: audit-only, symbolic-exact. This is a SHAPE observation, not a c_k
determination -- nothing here wires to production (registry section 8, the
flip-flop guard). See the c_k truncation-order framing in AGENTS.md before
reading any c_3 conclusion out of it; the whole c_k ladder is convention-C
frame and awaits re-derivation under D (bean qou-cds1).

The input series is NOT hardcoded. It is read from the upstream witness
`qbeta-crossing-weight-hecke.witness.json`, whose producer
(`qbeta_crossing_weight_hecke_probe.py`) derives it as `sp.expand(ratio_A - 1)`
from the H_3 Groebner-Shirshov reducer. Reconstructing this probe by pasting
the recorded polynomial in as a literal would have made it re-verify its own
input; reading it from the producer that derives it keeps the provenance chain
intact.

Reconstruction note (2026-08-16, bean qou-zdz5): the original producer was
never committed. The witness landed on main via 40bbec1955 -- a
`fix(docs): resolve defterm and markdown cross-reference validation errors`
commit that also swept in `session.json` and `tmp.json`, i.e. an untargeted
add over a dirty tree -- while the script stayed behind in the working tree.
A 27-line earlier draft exists at 59a533b8e6 on the unmerged branch
`claude/qbeta-c3-synthesis-2026-07-07`, but it is a different revision
(scriptHash 8ed1b40d0b43 vs the witness's 7fa824f3edea), computes a bare
9/8*hbar^2 stand-in rather than the degree-7 series, and writes no witness at
all. This file reconstructs the probe from the witness's recorded assertions
and result shape, sourcing the input from upstream.

Usage:
    python3 computations/qbeta/qbeta_c3_faddeev_rogers_probe.py

Output:
    computations/qbeta/qbeta-c3-faddeev-rogers-transformation.witness.json
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))

UPSTREAM_WITNESS = "qbeta-crossing-weight-hecke.witness.json"
UPSTREAM_FIELD = "Q_beta_GS_over_Q_A_minus_1"


def _repo_head_sha() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=_HERE,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


def _load_gs_departure(t: sp.Symbol) -> sp.Expr:
    """Read the GS net departure from the producer that derives it.

    `t` is passed in as an explicit local: a bare `sympify` mints its own
    `Symbol('t')`, and two symbols of the same name but different assumptions
    do not unify -- `subs` then silently no-ops and `coeff` returns 0.
    """
    path = os.path.join(_HERE, UPSTREAM_WITNESS)
    with open(path, encoding="utf-8") as f:
        w = json.load(f)
    raw = w["result"][UPSTREAM_FIELD]
    return sp.sympify(raw, locals={"t": t})


def main() -> int:
    # No `real=True`: the continuation sends t -> i*t, so the transformed
    # series is genuinely complex.
    t = sp.Symbol("t")

    gs_departure = sp.expand(_load_gs_departure(t))
    # Faddeev modular double / Rogers two-saddle continuation.
    transformed = sp.expand(gs_departure.subs(t, sp.I * t))

    lead_before = sp.simplify(gs_departure.coeff(t, 2))
    lead_after = sp.simplify(transformed.coeff(t, 2))

    a1 = lead_before == 1
    a2 = lead_after == -1
    all_passed = bool(a1 and a2)

    assertions = [
        {
            "name": "1_gs_departure_cosh_like",
            "passed": bool(a1),
            "detail": f"GS Departure leading t^2 term is {lead_before}",
        },
        {
            "name": "2_transformed_departure_cos_like",
            "passed": bool(a2),
            "detail": f"Transformed leading t^2 term is {lead_after}",
        },
    ]

    verdict = (
        "PASS: Faddeev/Rogers transformation maps the cosh-like GS categorical "
        "net to a cos-like observable ladder shape (negative leading t^2 term)."
        if all_passed else
        f"FAIL: leading t^2 term {lead_before} -> {lead_after}; expected 1 -> -1."
    )

    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-c3-faddeev-rogers-transformation",
        "description": "Applies the Faddeev modular double / Rogers two-saddle "
                       "transformation (hbar_q -> i*hbar_q) to the categorical GS net "
                       "departure to bridge the cosh-like growth to the cos-like "
                       "observable ladder.",
        "audit_only": True,
        "tier": "symbolic-exact",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "GS_Departure": str(gs_departure),
            "Faddeev_Transformed_Departure": str(transformed),
            "verdict": verdict,
        },
        "context": {
            "input_source": f"{UPSTREAM_WITNESS} -> result.{UPSTREAM_FIELD}",
            "input_producer": "computations/qbeta/qbeta_crossing_weight_hecke_probe.py",
            "flip_flop_guard": "registry section 8 -- no c_k wired",
            "convention": "convention-C frame; awaits re-derivation under D (bean qou-cds1)",
        },
    }

    out = os.path.join(_HERE, "qbeta-c3-faddeev-rogers-transformation.witness.json")
    with open(out, "w", encoding="utf-8") as f:
        # Provenance envelope. This producer writes its witness as raw JSON, so
        # nothing stamps `scriptHash` — and a witness without one cannot be
        # compared against its producer, so it drops OUT of the self-staleness
        # audit and reads as "not stale" forever. Regenerating it then looks
        # like progress while removing it from the count: a false drain.
        # Full rationale and the detector: computations/witness_drain_audit.py.
        #
        # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
        # fields in place and leaves the on-disk shape untouched, so consumers
        # of legacy `assertions` records (which key on `label`, not `name`) do
        # not have to change. `engine` is passed back from the payload because
        # the helper overwrites it, and a descriptive engine string is worth
        # keeping.
        try:
            from witness_base import WitnessBuilder  # noqa: E402
        except ImportError:  # cluster subdir without the _path_bridge bootstrap
            import sys as _sys
            from pathlib import Path as _Path
            _sys.path.insert(0, str(next(
                _a / "substrate" for _a in _Path(__file__).resolve().parents
                if (_a / "substrate" / "witness_base.py").is_file())))
            from witness_base import WitnessBuilder  # noqa: E402
        WitnessBuilder.stamp_staleness_metadata(
            witness, script_path=__file__,
            engine=witness.get("engine", 'sympy'))
        json.dump(witness, f, indent=2)

    print("=== Faddeev/Rogers transformation on the GS categorical net ===")
    print(f"GS Departure:          {gs_departure}")
    print(f"Transformed Departure: {transformed}")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
