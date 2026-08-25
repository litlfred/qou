#!/usr/bin/env python3
"""W2: local exponents of the C1 q-difference module (Birkhoff-matrix, 0-side).

Bean `qou-xufp` (W2, symbol extraction). Following the DRSZ Birkhoff-matrix recipe
(`library/equations-aux-q-differences/Equations_aux_q-differences.pdf` §3.3), the connection matrix
`P(x) = (X^∞)⁻¹ X^0` of a q-difference module needs the local canonical solutions at 0
and ∞, each built from the q-characters `e_{q,c}` of the *exponents* (eigenvalues of the
companion `A(0)`, `A(∞)`).

C1 = RSZ route-A `L1 = (q²x−1)σ² − (q−1)σ − (q−1)` (`2026-07-20-qlift-routeA-rsz-invariants.md`),
companion `σY = A(x)Y`, `A(x) = [[0,1],[(q−1)/(q²x−1), (q−1)/(q²x−1)]]`.

This computes:
  - at 0 (Fuchsian): the exponents = eigenvalues of `A(0) = [[0,1],[1−q,1−q]]`, i.e. roots
    of `t² + (q−1)t + (q−1)`; exponent discriminant `(q−1)(q−5)`. These feed the 0-side
    canonical solution `X^0 = M^0 · diag(e_{q,λ₊}, e_{q,λ₋})`.
  - at ∞: `A(∞) = [[0,1],[0,0]]` is nilpotent (`det 0`) ⇒ NOT Fuchsian ⇒ irregular,
    slope-½ (matches route-A). So the pure Fuchsian recipe gives only the 0-side; the full
    Birkhoff matrix needs the q-Gevrey/Stokes solution at ∞ (RSZ Astérisque 355).

Symbolic — no fit, nothing wired. Reports the 0-side exponent data + the ∞ obstruction.
"""
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
import sympy as sp


def main() -> None:
    q, X, t = sp.symbols("q X t")
    A = sp.Matrix([[0, 1], [(q - 1) / (q**2 * X - 1), (q - 1) / (q**2 * X - 1)]])
    A0 = A.subs(X, 0)
    charpoly0 = sp.expand(A0.charpoly(t).as_expr())          # t^2 + (q-1)t + (q-1)
    exps0 = [sp.simplify(e) for e in sp.solve(charpoly0, t)]
    exp_disc = sp.expand((q - 1) ** 2 - 4 * (q - 1))          # (q-1)(q-5)
    inf_leading = sp.limit(A[1, 0], X, sp.oo)                 # 0 => A(inf) nilpotent

    results = {
        "operator": "L1 = (q^2 x - 1) s^2 - (q-1) s - (q-1)   [C1, RSZ route-A]",
        "A0": [[0, 1], ["1-q", "1-q"]],
        "exponent_poly_at_0": str(charpoly0),
        "exponents_at_0": [str(e) for e in exps0],
        "exponent_trace_at_0": "1 - q",
        "exponent_det_at_0": "q - 1",
        "exponent_discriminant_at_0": str(sp.factor(exp_disc)) + "  (= (q-1)(q-5))",
        "A_inf_lower_left_limit": str(inf_leading),
        "A_inf": "[[0,1],[0,0]] nilpotent, det 0",
        "fuchsian_at_0": True,
        "fuchsian_at_inf": False,
        "inf_singularity": "irregular, slope 1/2 (needs q-Gevrey/Stokes; RSZ Asterisque 355)",
    }
    for k, v in results.items():
        print(f"  {k}: {v}")

    # cross-check: exponents satisfy the exponent poly, sum/product match trace/det
    ok = all(sp.simplify(e**2 + (q - 1) * e + (q - 1)) == 0 for e in exps0)
    ok = ok and sp.simplify(sum(exps0) - (1 - q)) == 0 and sp.simplify(sp.prod(exps0) - (q - 1)) == 0
    print("  cross_check_exponents:", bool(ok))

    script_path = Path(__file__).resolve()

    def _git(a):
        try:
            return subprocess.check_output(["git", *a], cwd=script_path.parent, text=True).strip() or "unknown"
        except Exception:
            return "unknown"

    _script_sha = _git(["log", "-1", "--format=%H", "--", str(script_path)])
    if _script_sha == "unknown":
        _script_sha = _git(["rev-parse", "HEAD"])

    witness = {
        "schema": "witness/v1",
        "engine": "python+sympy",
        "scriptFile": "c3_w2_c1_module_exponents.py",
        "commitSha": _git(["rev-parse", "HEAD"]),
        "description": (
            "W2: C1 q-difference module local exponents. At 0 (Fuchsian): roots of "
            "t^2+(q-1)t+(q-1), exp-disc (q-1)(q-5). At inf: nilpotent companion => "
            "irregular slope-1/2, needs Stokes. 0-side of the Birkhoff recipe. Symbolic."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_c1_module_exponents.py",
            "scriptCommitSha": _script_sha,
            "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        },
        "results": results,
        "cross_check_exponents_ok": bool(ok),
        "verdict": (
            "CONFIRMED (0-side): C1 exponents at 0 = roots of t^2+(q-1)t+(q-1). "
            "Full Birkhoff matrix blocked at inf (irregular slope-1/2, needs Stokes)."
        ),
        "scope": "0-side Fuchsian exponent data only; inf-side Stokes is the residual. No fit.",
    }
    out = script_path.with_suffix(".witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nverdict: {witness['verdict']}\nwitness: {out}")


if __name__ == "__main__":
    main()
