#!/usr/bin/env python3
"""
z -> c_k f-map keystone -- bar-parity of the z-side atoms (the z-alone exclusion).

Formalize-first structural probe (bean ea56, PR #3449; ledger
docs/coordination/z-ck-fmap-keystone.md). Exact symbolic only: NO anchors, NO
c_k value, NO fit, NO wiring. Companion to the sorry-free Lean certificate
QOU/QBeta/ZBarParity.lean (lean-direct exit 0).

What is checked (all sympy-exact, fibre bar involution q -> 1/q):

  1. z(q) = sqrt(q)/(1+q) is EXACTLY bar-EVEN (twist 1): z(1/q) = z(q).
  2. hbar_q = 1 - 1/q is bar-ODD up to the monomial twist -q; hence the
     ladder variable u = b*hbar_q^2 is bar-even up to twist q^2.
  3. kappa_(2,1) = (q-1)^3 (q+1) / q^2 is EXACTLY bar-ODD (twist 1)
     (re-verifies the 2026-06-13 heat f-map audit finding).
  4. Closure: z^m and rational functions of z alone stay bar-even (sampled
     m = 1..6 and two rational combinations); z^m * kappa stays bar-odd.

Consequence (scope-(a) structural exclusion): the c_k-recursion kernel's
leading coefficient a_1 is bar-ODD (QBetaCKRecursionKernelConstraints.lean)
and empirically nonzero (a_1 = -c_3); a scalar functional of z alone is
bar-EVEN, so it can never source a_1. The surviving z->c_k f-map class
factors as (bar-even z-functional) x (bar-odd carrier). This narrows the
hypothesis class; it does not construct the f-map.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def _repo_head_sha():
    """Repo HEAD at emission time (I14 witness_provenance_audit fields)."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except Exception:
        return None


def bar(expr, q):
    """Fibre bar involution q -> 1/q, exact."""
    return sp.cancel(sp.together(expr.subs(q, 1 / q)))


def parity(expr, q):
    """Return 'even' / 'odd' / 'neither' for exact bar-parity (twist 1)."""
    b = bar(expr, q)
    if sp.simplify(b - expr) == 0:
        return "even"
    if sp.simplify(b + expr) == 0:
        return "odd"
    return "neither"


def main():
    q = sp.symbols("q", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # 1. z = sqrt(q)/(1+q) is exactly bar-even.
    z = sp.sqrt(q) / (1 + q)
    z_parity = parity(z, q)
    check("z_bar_even_twist_1", z_parity == "even")

    # 2. hbar = 1 - 1/q: bar(hbar) = -q*hbar; u ~ hbar^2: bar(hbar^2) = q^2*hbar^2.
    hbar = 1 - 1 / q
    hbar_twist = sp.simplify(bar(hbar, q) / hbar)
    check("hbar_bar_odd_twist_minus_q", sp.simplify(hbar_twist + q) == 0)
    hbar2_twist = sp.simplify(bar(hbar**2, q) / hbar**2)
    check("hbar_sq_bar_even_twist_q_sq", sp.simplify(hbar2_twist - q**2) == 0)

    # 3. kappa_(2,1) = (q-1)^3 (q+1) / q^2 exactly bar-odd.
    kappa = (q - 1) ** 3 * (q + 1) / q**2
    kappa_parity = parity(kappa, q)
    check("kappa21_bar_odd_twist_1", kappa_parity == "odd")

    # 4a. Closure: z^m bar-even for m = 1..6.
    powers_even = all(parity(z**m, q) == "even" for m in range(1, 7))
    check("z_powers_1_to_6_bar_even", powers_even)

    # 4b. Two rational functionals of z alone stay bar-even.
    f1 = (1 + 3 * z**2) / (2 - z)          # generic rational functional
    f2 = z**3 - 5 * z + sp.Rational(7, 2)  # generic polynomial functional
    check("rational_functional_of_z_bar_even",
          parity(f1, q) == "even" and parity(f2, q) == "even")

    # 4c. Parity composition: (z-functional) x kappa stays bar-odd.
    products_odd = all(parity(z**m * kappa, q) == "odd" for m in (1, 2, 3))
    check("z_power_times_kappa_bar_odd", products_odd)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "STRUCTURAL EXCLUSION (scope-(a)): every scalar functional of z alone is "
        "bar-EVEN, while the kernel's leading coefficient a_1 is bar-ODD and nonzero "
        "(a_1 = -c_3, QBetaCKRecursionKernelConstraints.lean) -- so no scalar rational "
        "function of z alone can source a_1. The surviving z->c_k f-map class factors "
        "as (bar-even z-functional) x (bar-odd carrier, e.g. kappa_(2,1)). This narrows "
        "the ea56 hypothesis class; it derives NO c_k value and wires NOTHING."
        if all_passed else
        "INCONCLUSIVE -- a parity assertion failed; re-examine before using the "
        "exclusion. Do not cite until green."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-z-bar-parity-fmap-class",
        "description": "z->c_k f-map keystone: exact bar-parity of the z-side atoms. "
                       "z = sqrt(q)/(1+q) bar-even (twist 1); hbar bar-odd (twist -q); "
                       "u ~ hbar^2 bar-even (twist q^2); kappa_(2,1) bar-odd (twist 1); "
                       "closure checks. Companion to QOU/QBeta/ZBarParity.lean.",
        "audit_only": True,
        "tier": "structural-exact (symbolic bar-parity identities; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "z": str(z),
            "z_parity": z_parity,
            "hbar_twist": str(hbar_twist),
            "hbar_sq_twist": str(hbar2_twist),
            "kappa21": str(kappa),
            "kappa21_parity": kappa_parity,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone (bean ea56)",
            "ledger": "docs/coordination/z-ck-fmap-keystone.md",
            "lean_certificate": "QOU/QBeta/ZBarParity.lean",
            "kernel_constraints": "QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean",
            "heat_fmap_audit": "docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md",
            "refuted_class_map": "docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-z-bar-parity-fmap-class.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    print("=== z -> c_k f-map: z-side bar-parity / z-alone exclusion ===")
    print("z parity        :", z_parity)
    print("hbar twist      :", hbar_twist, " (expect -q)")
    print("hbar^2 twist    :", hbar2_twist, " (expect q^2)")
    print("kappa21 parity  :", kappa_parity)
    print("ALL PASSED      :", all_passed)
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
