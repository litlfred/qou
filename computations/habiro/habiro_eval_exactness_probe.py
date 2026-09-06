#!/usr/bin/env python3
"""habiro_eval_exactness_probe.py — regression guard for the two silent defects
in `habiro_exact_qbeta.eval_a_m_at_u`.

Bean `qou-cds1`.  Scope-(b): both are exact-arithmetic facts about a producer,
not modelling judgements.

## The defects (fixed 2026-09-06; this probe stops them returning)

1. **float64 in a `computations/` producer.**  The helper did
   `u = float(u_val)` and string-substituted the decimal, truncating the
   50-dps `u` to ~17 digits — the exact thing a comment 25 lines below in the
   same file forbade ("NOT float() — would silently truncate the 50-dps
   u_val").  The comment described a property the code did not have.

   Measured on `tr_M(proton)`: **1.63e-15 relative**, i.e. ~35 of the 50
   declared digits, and OVER the framework's own L1 target of 1 ppQ = 1e-15.
   The producer's own self-consistency assertion moved
   `1.000000000000001673 -> 1.000000000000000046` when fixed — from above the
   L1 line to 35x below it.

2. **Silent zero.**  `except Exception: return mp.mpf(0)` turned any parse
   failure into a coefficient of ZERO — a wrong answer rather than a failure.
   All 71 expressions in the atomic witness parse, so nothing was being
   absorbed in practice; the hazard was that nothing ever would be reported.

## Ruling out the confound, because there is one

The container that re-ran the producer carries `mpmath 1.4.1` where the
committed witness recorded `1.3.0`, so the number movement could in principle
be the library bump rather than the fix.  It is not: the post-fix values agree
with an INDEPENDENT sympy `N(..., 60)` evaluation, a different code path from
mpmath's polynomial arithmetic.  (`numpy` / `scipy` / the Python version also
differ, and are irrelevant — this producer imports neither; its only compute
dependency is mpmath.)

## Precision

mpmath at 60 dps; the reference values via sympy exact rationals.  No `float(`
outside display, no `statistics`, no `math.`.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "habiro"):
    _sys.path.insert(0, str(_p))

import mpmath as mpm                                            # noqa: E402
import sympy as sp                                              # noqa: E402
from mpmath import mp                                           # noqa: E402

from q_parameter import q_at                                    # noqa: E402
from habiro_exact_qbeta import eval_a_m_at_u                    # noqa: E402
from witness_base import WitnessBuilder                         # noqa: E402

mp.dps = 60
RESULTS: list[dict] = []


def record(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


q0 = q_at(60)
u0 = mpm.sqrt(q0)
W = json.load(open(_COMP / "habiro" / "habiro-coefficients-atomic.witness.json"))
usym = sp.symbols("u")


def exact(expr_str):
    e = sp.sympify(str(expr_str).replace("check_q", "u"))
    return mp.mpf(str(sp.N(e.subs(usym, sp.Float(str(u0), 60)), 60)))


def old_float64(expr_str):
    """The pre-fix body, kept here so the defect is measured, not asserted."""
    uu = float(u0)
    return mp.mpf(eval(str(expr_str).replace("check_q", f"({uu})").replace("u", f"({uu})")))


exprs = []
for d in W["results"].values():
    exprs += [c["a_m"] for c in d["habiro_coefficients"]] + [d["denom_in_u"]]

worst_now = mp.mpf(0)
worst_old = mp.mpf(0)
for e in exprs:
    ref = exact(e)
    if ref == 0:
        continue
    worst_now = max(worst_now, abs(eval_a_m_at_u(e, u0) - ref) / abs(ref))
    worst_old = max(worst_old, abs(old_float64(e) - ref) / abs(ref))

record(
    "helper_is_now_exact",
    worst_now < mp.mpf(10) ** (-40),
    f"worst relative deviation of eval_a_m_at_u from an independent sympy "
    f"N(...,60) evaluation, over all {len(exprs)} expressions in the atomic "
    f"witness: {mpm.nstr(worst_now, 4)} (< 1e-40). The helper now binds `u` "
    f"into the eval namespace instead of substituting its decimal expansion.",
)

record(
    "the_old_float64_path_was_over_the_L1_target",
    worst_old > mp.mpf(10) ** (-16),
    f"the pre-fix body, re-run here, deviates by up to {mpm.nstr(worst_old, 4)} "
    f"— against the framework's L1 compute-precision target of 1 ppQ = 1e-15. "
    f"This is measured by running the old code, not inferred from the diff.",
)

raised = False
try:
    eval_a_m_at_u("u ** (", u0)
except ValueError:
    raised = True
except Exception:
    pass
record(
    "silent_zero_fallback_is_gone",
    raised,
    "eval_a_m_at_u now raises ValueError on an unparseable expression instead "
    "of returning mp.mpf(0). A producer that substitutes zero for a "
    "coefficient it could not read reports a wrong number rather than a "
    "failure; all 71 live expressions parse, so making it loud costs nothing.",
)

wit = json.load(open(_COMP / "habiro" / "habiro-exact-qbeta.witness.json"))
resid = abs(mp.mpf(str(wit["assertions"][0]["computed"])) - 1)
record(
    "producer_assertion_now_under_1_ppQ",
    resid < mp.mpf(10) ** (-15),
    f"the producer's own self-consistency assertion sits at 1 + "
    f"{mpm.nstr(resid, 4)}; it was 1 + 1.673e-15, i.e. OVER the 1 ppQ L1 "
    f"target. The fix moved it from above the line to ~35x below it.",
)

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "is habiro_exact_qbeta.eval_a_m_at_u exact, and does it fail loudly?",
    "answer": "Yes to both, after the 2026-09-06 fix. It was float64-limited "
              "(1.63e-15, over the L1 1 ppQ target) and absorbed parse failures "
              "as zero.",
    "scope": "(b) — exact-arithmetic facts about a producer.",
    "worst_rel_dev_now": mpm.nstr(worst_now, 6),
    "worst_rel_dev_old_float64": mpm.nstr(worst_old, 6),
    "producer_assertion_residual": mpm.nstr(resid, 6),
    "expressions_checked": len(exprs),
    "mpmath_bump_ruled_out": "post-fix values agree with an independent sympy "
        "N(...,60) evaluation, so the movement is the fix and not the container's "
        "mpmath 1.3.0 -> 1.4.1; the producer imports no numpy/scipy/sympy.",
    "q0": mpm.nstr(q0, 20),
    "q0_pin": "proton (q_at)",
    "dps": mp.dps,
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(
    out, script_path=__file__, engine="python+sympy+mpmath",
    q0_value=mpm.nstr(q0, 50),
)
wpath = _HERE.parent / "habiro-eval-exactness.witness.json"
wpath.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wpath}")
print(f"allPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
