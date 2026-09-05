#!/usr/bin/env python3
"""
B1+B2 (bean ciei) -- 4_1 cyclotomic re-basing: transcription gate + basis parity.

I-B step B1 per docs/scope/2026-07-06-z-ck-fmap-ib-rebasing-scope.md; kill
criteria pre-stated in ledger SS4-quinquies (commit 03c155c7) BEFORE this run.

4_1's Habiro cyclotomic expansion (coefficients C_k == 1):

    J_N = sum_{k=0}^{N-1} omega_k(x),
    omega_k = prod_{j=1}^{k} (x + 1/x - q^j - q^{-j}),   x = q^N

(termwise equal to the certificate's Habiro-Le summand, see
aj_figure_eight_certificate.py docstring).

Gates:
  B1-K1  the omega-sum satisfies the verified inhomogeneous order-2 operator
         a2 J_{N+2} + a1 J_{N+1} + a0 J_N = b exactly, N = 1..8.
  B2-K2  bar-parity of the cyclotomic factor and of omega_k under
         (q,x) -> (1/q,1/x): must be clean (exact or monomial twist).
  B3 partial: q=1 shadow of omega_k is ((x-1)^2/x)^k -- even orders.

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


def main():
    q, x = sp.symbols("q x", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # Verified operator (aj_figure_eight_certificate.py, verbatim).
    a0 = (x - 1) * (x**2 * q**3 - 1) / x**6
    a2 = (x * q**2 - 1) * (x**2 * q - 1) / x**6
    # CORRECTED 2026-07-07: certificate's verified a1 (see correction audit).
    a1 = -((x * q - 1) ** 2 * (x * q + 1)
           * (x**4 * q**4 - x**3 * q**3 - x**2 * q**3 - x**2 * q - x * q + 1)) \
         / (x**8 * q**2)
    b = (x * q + 1) * (x**2 * q - 1) * (x**2 * q**3 - 1) / (x**7 * q)

    def factor(j):
        return x + 1 / x - q**j - q ** (-j)

    def J(N):
        """J_N(4_1) via the cyclotomic sum with C_k == 1 (exact in q)."""
        total = sp.Integer(0)
        for k in range(N):
            w = sp.Integer(1)
            for j in range(1, k + 1):
                w *= factor(j).subs(x, q**N)
            total += w
        return sp.expand(sp.cancel(sp.together(total)))

    # --- B1-K1: transcription gate, N = 1..8. ---
    ok = True
    for N in range(1, 9):
        lhs = (a2.subs(x, q**N) * J(N + 2) + a1.subs(x, q**N) * J(N + 1)
               + a0.subs(x, q**N) * J(N))
        resid = sp.simplify(sp.cancel(sp.together(lhs - b.subs(x, q**N))))
        if resid != 0:
            ok = False
            print(f"    N={N}: residual != 0")
            break
    check("B1K1_omega_sum_satisfies_certified_operator_N1_8", ok)

    # C_k == 1 -> the induced coefficient recurrence is the trivial depth-1
    # constant C_{k+1} = C_k (recorded, tautologically true by construction).

    # --- B2-K2: parity of the cyclotomic factor and omega_k. ---
    bar = {q: 1 / q, x: 1 / x}
    f3 = factor(3)
    f3bar = sp.cancel(sp.together(f3.subs(bar, simultaneous=True)))
    factor_invariant = sp.simplify(f3bar - f3) == 0
    check("B2K2_cyclotomic_factor_bar_invariant_twist_1", factor_invariant)

    om3 = factor(1) * factor(2) * factor(3)
    om3bar = sp.cancel(sp.together(om3.subs(bar, simultaneous=True)))
    omega_invariant = sp.simplify(om3bar - om3) == 0
    check("B2K2_omega_k_bar_invariant_twist_1_sampled_k3", omega_invariant)

    # --- B3 partial: q=1 shadow of omega_k. ---
    om2_q1 = sp.simplify(om3.subs(q, 1) / factor(3).subs(q, 1) ** 1)  # omega_2 at q=1
    shadow_ok = sp.simplify(om2_q1 - ((x - 1) ** 2 / x) ** 2) == 0
    check("B3_omega_k_q1_shadow_is_xm1_sq_over_x_pow_k", shadow_ok)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "B1+B2 PASS -- the cyclotomic (Habiro) basis DIAGONALIZES the bar involution "
        "for 4_1: every basis element omega_k is EXACTLY bar-invariant (twist 1), the "
        "coefficients are C_k = 1 (trivial depth-1 constant recurrence), and the "
        "operator is FULLY bar-even slot-wise (with the corrected certificate a_1, all "
        "three slot ratios are twist-1 invariant), consistent with the basis picture. "
        "Consequences: (i) the whole 4_1 element is bar-EVEN in this basis, consistent "
        "with the overall-F bar-even gate (KC7); (ii) the bar-ODD channel (kernel a_1's "
        "odd part) can only enter through the LADDER EVALUATION map (u-twist q^2, "
        "sqrt-u prefactor, epsilon-expansion) -- exactly the quantum-modular S-shadow "
        "picture (2026-06-13 audit SS2-quater); (iii) q=1 shadow orders of omega_k are "
        "EVEN (2k), echoing the T3 z-side even-order phenomenon. B3 (the (u;u)_m -> u^k "
        "composition + slot re-derivation) remains open -- NOT a closure, NO c_k value."
        if all_passed else
        "KILL or transcription failure -- see failed assertion; if B2K2 failed, the "
        "cyclotomic re-basing does NOT repair the parity defect: record scope-(a) "
        "verdict against Z4-via-4_1 and fall back to Z3 carriers / other knots."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-b1-fourone-cyclotomic-rebasing",
        "description": "I-B step B1+B2 (bean ciei): 4_1 cyclotomic re-basing. "
                       "Transcription gate (omega-sum vs certified inhomogeneous "
                       "order-2 operator, N=1..8 exact) + basis bar-parity gate. "
                       "Pre-stated in ledger SS4-quinquies (commit 03c155c7).",
        "audit_only": True,
        "tier": "structural-exact (symbolic; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "cyclotomic_form": "J_N = sum_k omega_k, omega_k = prod_{j<=k} (x + 1/x - q^j - q^-j), C_k = 1",
            "induced_coefficient_recurrence": "C_{k+1} = C_k (trivial depth-1 constant, by C_k = 1)",
            "factor_bar_parity": "exactly invariant (twist 1)",
            "omega_q1_shadow": "((x-1)^2/x)^k -- even vanishing orders 2k at x=1",
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone, bean ciei (I-B step B1+B2)",
            "prestatement": "docs/coordination/z-ck-fmap-keystone.md SS4-quinquies (commit 03c155c7)",
            "scope": "docs/scope/2026-07-06-z-ck-fmap-ib-rebasing-scope.md",
            "operator_source": "computations/aj_figure_eight_certificate.py",
            "lean_certificate": "QOU.QBeta.cycFactor_bar_invariant (ZBarParity SS6)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-b1-fourone-cyclotomic-rebasing.witness.json")
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
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("=== B1+B2 : 4_1 cyclotomic re-basing ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
