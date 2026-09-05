#!/usr/bin/env python3
"""
T3 (bean pxvo) -- Z3 carrier preflight: q=1 vanishing orders + the
parity-vs-shadow tension flag.

Kill criteria / claims pre-stated in ledger SS4-ter (commit 44b0b82c):

  T3-1 (order bookkeeping, decidable):
    - kappa_(2,1) = (q-1)^3 (q+1) / q^2 vanishes at q=1 to order exactly 3;
    - z - 1/2 vanishes at q=1 to order exactly 2 (z = sqrt(q)/(1+q) is
      CRITICAL at q=1: dz/dq|_1 = 0), so rational functions of z realize only
      EVEN vanishing/pole orders at q=1;
    - hence (rational-in-z) x kappa_(2,1) has ODD total q=1 order and can
      never equal the finite NONZERO shadow a_1(1) = 2. Scope-(a): kills the
      naive f(z)*kappa_(2,1) sub-class of Z3 as the SOLE a_1 source (for f
      q=1-regular rational in z).

  T3-2 (tension flag, YELLOW owner item -- verified, not resolved):
    - any exactly-bar-odd f regular at q=1 has f(1) = 0 (f(1) = -f(1));
    - the kernel constraint set asserts a_1 bar-ODD (ck_a1_bar_odd, from
      #1887) AND the q=1 shadow a_1 = -c_3 -> 2 != 0;
    - jointly impossible for q=1-regular a_1: either the #1887 parity is an
      odd-PART/swing statement (not exact pointwise parity), or a_1 is
      singular at q=1. Flagged for owner ruling; affects every K2-style
      parity gate in the f-map program.

Exact symbolic. NO anchors, NO c_k value, NO fit, NO wiring.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def _repo_head_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except Exception:
        return None


def vanishing_order(f, q, at=1, maxorder=8):
    """Smallest n with nonzero coefficient of (q-at)^n in the series of f."""
    t = sp.symbols("t")
    g = sp.expand(sp.series(f.subs(q, at + t), t, 0, maxorder).removeO())
    for n in range(maxorder):
        c = g.coeff(t, n)
        if sp.simplify(c) != 0:
            return n, sp.simplify(c)
    return maxorder, None


def main():
    q = sp.symbols("q", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    z = sp.sqrt(q) / (1 + q)
    kappa = (q - 1) ** 3 * (q + 1) / q**2

    # T3-1a: kappa vanishes at q=1 to order exactly 3.
    n_k, c_k = vanishing_order(kappa, q)
    check("kappa_q1_order_exactly_3", n_k == 3 and c_k is not None)

    # T3-1b: z - 1/2 vanishes at q=1 to order exactly 2 (z critical at q=1).
    n_z, c_z = vanishing_order(z - sp.Rational(1, 2), q)
    check("z_minus_half_q1_order_exactly_2", n_z == 2 and c_z is not None)
    dz1 = sp.simplify(sp.diff(z, q).subs(q, 1))
    check("dz_dq_at_1_is_zero", dz1 == 0)

    # T3-1c: powers (z - 1/2)^k realize orders 2k (even only), k = 1..3.
    even_only = all(vanishing_order((z - sp.Rational(1, 2)) ** k, q)[0] == 2 * k
                    for k in (1, 2, 3))
    check("z_functional_orders_even_only_sampled", even_only)

    # T3-1d: consequence -- f(z)*kappa with f = 1/(z-1/2)^k (k=1: order -2)
    # has total order 3-2k, odd for all k; it is never 0 (finite nonzero) at
    # q=1. Sampled: k=1 -> order 1 (vanishes); k=2 -> order -1 (pole).
    ord_k1 = vanishing_order(kappa / (z - sp.Rational(1, 2)), q)[0]
    check("kappa_over_zhalf_order_1_vanishes", ord_k1 == 1)
    pole_k2 = sp.simplify(sp.limit(kappa / (z - sp.Rational(1, 2)) ** 2, q, 1,
                                   dir="+")) in (sp.oo, -sp.oo, sp.zoo)
    check("kappa_over_zhalf_sq_poles", bool(pole_k2))

    # T3-2: parity-vs-shadow tension. Exactly-odd regular f => f(1) = 0.
    # Verify on the corpus's proved odd carrier kappa; then record the flag.
    check("bar_odd_kappa_vanishes_at_1", sp.simplify(kappa.subs(q, 1)) == 0)
    # The shadow requires a_1(1) = 2 != 0 -- the joint impossibility is a
    # derivation, recorded (not an assertion about which horn resolves it).

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "T3-1 EXCLUSION (scope-(a)): (rational-in-z, q=1-regular f) x kappa_(2,1) has "
        "odd q=1 order (3 - 2k) and can never equal the finite nonzero shadow "
        "a_1(1) = 2 -- the naive f(z)*kappa sub-class of Z3 is excluded as the sole "
        "a_1 source. T3-2 TENSION (YELLOW, owner): 'a_1 exactly bar-odd' + "
        "'a_1 q=1-regular with shadow 2' are jointly impossible; the #1887 parity "
        "must be an odd-part/swing statement or a_1 is q=1-singular. Nothing wired."
        if all_passed else
        "INCONCLUSIVE -- an order/parity assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-t3-carrier-q1-order-preflight",
        "description": "T3 (bean pxvo): q=1 vanishing-order bookkeeping for the Z3 "
                       "carrier class (kappa order 3; z critical, z-functionals even "
                       "orders only => f(z)*kappa excluded as sole a_1 source) + the "
                       "parity-vs-shadow tension flag. Pre-stated in ledger SS4-ter "
                       "(commit 44b0b82c).",
        "audit_only": True,
        "tier": "structural-exact (symbolic series orders; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "kappa_q1_order": n_k, "kappa_leading_coeff": str(c_k),
            "z_minus_half_q1_order": n_z, "z_minus_half_leading_coeff": str(c_z),
            "tension_flag": "a_1 exactly-bar-odd AND a_1(1)=2 jointly impossible for "
                            "q=1-regular a_1 (odd => vanishes at the bar fixed point). "
                            "Owner ruling needed: odd-part/swing reading of #1887, or "
                            "q=1-singular a_1.",
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone, bean pxvo (T3)",
            "prestatement": "docs/coordination/z-ck-fmap-keystone.md SS4-ter (commit 44b0b82c)",
            "kernel_constraints": "QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean",
            "ea56": "QOU/QBeta/ZBarParity.lean",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-t3-carrier-q1-order-preflight.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("=== T3 : Z3 carrier q=1-order preflight ===")
    print("kappa order at q=1     :", n_k, "leading:", c_k)
    print("(z-1/2) order at q=1   :", n_z, "leading:", c_z)
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
