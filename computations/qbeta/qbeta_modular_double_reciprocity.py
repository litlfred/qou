#!/usr/bin/env python3
"""
Option B (bean `qou-dvlt`): is the modular dual's 1e-165 suppression at the
substrate an `arg b` artifact, or intrinsic?  **INTRINSIC.**

`phi_b_evaluator.py`'s substrate regime takes b = sqrt(ln q0 / 2pi)*exp(i pi/4),
so b^2 = i*ln q0/(2pi) is purely imaginary and

    q  = exp( 2 pi i b^2) = exp(-ln q0) = 1/q0      (real, as the substrate needs)
    q~ = exp(-2 pi i/b^2) = exp(-4 pi^2 / ln q0)

Write b^2 = i y. Then log q = -2 pi y and log q~ = -2 pi / y, so

    log q * log q~ = 4 pi^2        identically in y

The y CANCELS. That is not a consequence of the +pi/4 choice: demanding a REAL q
at all forces b^2 purely imaginary, after which y is the only freedom left, and
the product does not depend on it. There is no convention to re-choose.

Consequences measured here:

  * the reciprocity holds at the substrate to 0.0 relative error, and
    Re(b^2) = 0 exactly;
  * the two sides of the double BALANCE at |log q| = 2pi, i.e. q = exp(-2pi)
    ~ 0.00187. The substrate has |log q| = 0.10434, so it is **60.2x too close
    to 1**, and the reciprocity forces |log q~| = 378.3 => |q~| ~ 4.8e-165;
  * for the dual merely to clear double precision (|q~| > 1e-16) one would need
    q0 > 2.92. The substrate is at 1.10998.

WHY THIS CLOSES FRONT (a) AS STATED. `BarInvolutionDomainObstruction` (PR #5093)
proved a single q-series cannot supply the bar-even projection and that the
object required is a PAIR -- the Garoufalidis-Zagier shape, whose second entry is
exactly this modular dual. `phi_b_evaluator` already realises that pair at the
substrate. But the second entry is 1e-165 there, and q0 is an INPUT, so nothing
in the construction can be re-chosen to avoid it.

Sitting near 1 IS sitting at the degenerate point of the modular double. The
framework's own substrate value puts it there.

Scope-(b), invariant named: log q * log q~ = 4 pi^2 holds identically in y, hence
in every real-q regime. It excludes any attempt to obtain a USABLE modular dual
at a substrate near 1. It says nothing about the state integral at other q, and
nothing about (H1).

WHAT IS PROVED WHERE (do not over-cite the Lean). The Lean companion
QOU.QBeta.ModularDoubleReciprocity proves the ALGEBRA -- (c y)(c/y) = c^2 -- over
a generic field, about definitions that are STIPULATED to be -(c y) and -(c/y).
It does NOT prove that log q = -2 pi y and log q~ = -2 pi/y for Faddeev's actual
q, q~; that identification is imported from the modular-double literature, and it
is THIS PROBE that checks it at the substrate (Re(b^2) = 0 exactly, q = 1/q0
exactly, reciprocity to 0.0) -- at that point only, by evaluating exp.

So the honest form of the conclusion is: GIVEN the standard identification, the
degeneracy is forced by an algebraic identity. The force is real; the premise is
imported. Per AGENTS.md "sorry-free != derived", this is not "Lean proves the
modular double degenerates".
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 60


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    q0 = q_at()                 # experimental (proton) pin
    lnq0 = mp.log(q0)

    # the substrate convention, exactly as phi_b_evaluator states it
    b = mp.sqrt(lnq0 / (2 * mp.pi)) * mp.expjpi(mp.mpf(1) / 4)
    b2 = b ** 2
    q = mp.exp(2j * mp.pi * b2)
    qt = mp.exp(-2j * mp.pi / b2)

    print("=" * 76)
    print("Option B — is the modular dual's suppression intrinsic?  YES.")
    print("=" * 76)
    print(f"\n  q0    = {mp.nstr(q0, 22)}")
    print(f"  ln q0 = {mp.nstr(lnq0, 22)}")
    print(f"  b^2   = {mp.nstr(b2, 20)}")
    print(f"          Re(b^2) = {mp.nstr(abs(mp.re(b2)), 6)}  (purely imaginary)")
    print(f"  q     = {mp.nstr(mp.re(q), 22)}   vs 1/q0 = {mp.nstr(1 / q0, 22)}")
    print(f"          |q - 1/q0| = {mp.nstr(abs(q - 1 / q0), 6)}")
    print(f"  q~    = {mp.nstr(abs(qt), 10)}  = 10^{mp.nstr(mp.log10(abs(qt)), 8)}")

    print("\n" + "-" * 76)
    print("THE RECIPROCITY:  log q * log q~ = 4 pi^2, identically in y")
    print("-" * 76)
    lhs = mp.log(abs(q)) * mp.log(abs(qt))
    rhs = 4 * mp.pi ** 2
    recip_err = abs(lhs - rhs) / rhs
    print(f"\n  log|q| * log|q~| = {mp.nstr(lhs, 25)}")
    print(f"  4 pi^2           = {mp.nstr(rhs, 25)}")
    print(f"  relative error   = {mp.nstr(recip_err, 6)}")
    print("\n  The y cancels, so no choice of y — and hence no choice of the")
    print("  convention — moves the product. The dual is NOT a free parameter.")

    # independence of y, demonstrated rather than asserted
    print("\n  Same product at three unrelated y (demonstrating the cancellation):")
    y_indep = []
    for y in (mp.mpf("0.001"), mp.mpf(1), mp.mpf("17.25")):
        p = (-2 * mp.pi * y) * (-2 * mp.pi / y)
        y_indep.append({"y": mp.nstr(y, 8), "product": mp.nstr(p, 20)})
        print(f"    y = {mp.nstr(y, 8):>10}   product = {mp.nstr(p, 20)}")

    print("\n" + "-" * 76)
    print("Where the double BALANCES, and how far the substrate is from it")
    print("-" * 76)
    balanced = 2 * mp.pi
    shortfall = balanced / abs(lnq0)
    q_balanced = mp.exp(-balanced)
    print(f"\n  balance needs |log q| = 2 pi = {mp.nstr(balanced, 14)}")
    print(f"  substrate has |log q| =        {mp.nstr(abs(lnq0), 14)}")
    print(f"  short by                       {mp.nstr(shortfall, 8)} x")
    print(f"  the balanced q would be exp(-2pi) = {mp.nstr(q_balanced, 14)}")
    print(f"  forced |log q~| = 4pi^2/|log q| =   {mp.nstr(rhs / abs(lnq0), 12)}")

    # what q0 would be needed for the dual to clear double precision
    need_ln = rhs / (16 * mp.log(10))
    need_q0 = mp.exp(need_ln)
    print(f"\n  For |q~| > 1e-16 (double precision) one needs ln q0 > "
          f"{mp.nstr(need_ln, 8)},")
    print(f"  i.e. q0 > {mp.nstr(need_q0, 8)}.  The substrate is at "
          f"{mp.nstr(q0, 8)}.")

    print("\n" + "-" * 76)
    print("Verdict")
    print("-" * 76)
    print("""
  INTRINSIC. The suppression is forced by the reciprocity together with q0
  being near 1 — and q0 is an INPUT, not a convention. Front (a) as stated
  ("build the GZ pair at the substrate") is closed: the pair's second entry is
  numerically absent exactly where the framework needs it.

  Sitting near 1 IS sitting at the degenerate point of the modular double.
""")

    assertions = [
        {"name": "b_squared_is_purely_imaginary",
         "passed": bool(abs(mp.re(b2)) < mp.mpf("1e-50"))},
        {"name": "q_equals_inverse_q0",
         "passed": bool(abs(q - 1 / q0) < mp.mpf("1e-50"))},
        {"name": "reciprocity_log_q_times_log_qdual_eq_4pi2",
         "passed": bool(recip_err < mp.mpf("1e-40")),
         "detail": "rel err " + mp.nstr(recip_err, 6)},
        {"name": "product_independent_of_y",
         "passed": bool(len({r["product"] for r in y_indep}) == 1)},
        {"name": "substrate_far_from_balanced_point",
         "passed": bool(shortfall > 10),
         "detail": mp.nstr(shortfall, 6) + "x too close to 1"},
        {"name": "dual_below_double_precision_at_substrate",
         "passed": bool(abs(qt) < mp.mpf("1e-16"))},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-modular-double-reciprocity",
        "description": (
            "Option B (bean qou-dvlt): the modular dual's ~1e-165 suppression at the "
            "substrate is INTRINSIC, not an arg-b artifact. With b^2 = i y the "
            "reciprocity log q * log q~ = 4 pi^2 holds identically in y — the y "
            "cancels — so demanding a real q leaves no convention to re-choose. "
            "Measured at the substrate: Re(b^2) = 0 exactly, q = 1/q0 exactly, "
            "reciprocity to 0.0 relative error. The double balances at |log q| = 2pi "
            "(q = e^-2pi ~ 0.00187); the substrate's |log q| = 0.10434 is 60.2x too "
            "close to 1, forcing |log q~| = 378.3 and |q~| ~ 4.8e-165. For the dual "
            "merely to clear double precision one would need q0 > 2.92. This closes "
            "front (a) as stated: PR #5093 proved the parity read-off needs a PAIR, "
            "and the pair's second entry is numerically absent at the substrate — "
            "with q0 an input, nothing can be re-chosen. Scope-(b); says nothing "
            "about (H1)."),
        "audit_only": True,
        "tier": "exact identity + numerical confirmation (no fit)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "q0": mp.nstr(q0, 25),
            "ln_q0": mp.nstr(lnq0, 25),
            "b_squared_imag": mp.nstr(mp.im(b2), 20),
            "b_squared_real_abs": mp.nstr(abs(mp.re(b2)), 6),
            "q": mp.nstr(mp.re(q), 25),
            "abs_q_dual": mp.nstr(abs(qt), 12),
            "log10_abs_q_dual": mp.nstr(mp.log10(abs(qt)), 10),
            "log_q_times_log_q_dual": mp.nstr(lhs, 25),
            "four_pi_squared": mp.nstr(rhs, 25),
            "reciprocity_relative_error": mp.nstr(recip_err, 8),
            "y_independence_check": y_indep,
            "balanced_abs_log_q": mp.nstr(balanced, 16),
            "substrate_abs_log_q": mp.nstr(abs(lnq0), 16),
            "shortfall_factor": mp.nstr(shortfall, 12),
            "balanced_q_value": mp.nstr(q_balanced, 16),
            "forced_abs_log_q_dual": mp.nstr(rhs / abs(lnq0), 12),
            "q0_needed_for_dual_above_1e_minus_16": mp.nstr(need_q0, 10),
        },
        "context": {
            "axis": "front (a) triage, option B — is the dual degeneracy intrinsic?",
            "lean": "QOU.QBeta.ModularDoubleReciprocity (sorry-free, 4 declarations)",
            "inputs": [
                "computations/qbeta/phi_b_evaluator.py (the substrate b convention)",
                "tools/qou-substrate/.../constants.py::q_at (proton pin)",
            ],
            "closes": (
                "front (a) as stated — build the GZ pair at the substrate. The pair "
                "exists in phi_b_evaluator but its second entry is 1e-165 there."),
            "scope": (
                "Scope-(b), invariant named (the reciprocity, identical in y). Does "
                "NOT exclude the state integral at other q, and does not bear on "
                "(H1) c_3^even = -Vol(4_1)."),
        },
    }

    out_path = HERE / "qbeta-modular-double-reciprocity.witness.json"
    with open(out_path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"witness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
