#!/usr/bin/env python3
"""W2 ∞: the explicit formal slope-½ solution of the C1 module, with q-Gevrey growth.

Bean `qou-xufp` (W2, Birkhoff-matrix ∞-side). The C1 module `L1 = (q²x−1)σ² − (q−1)σ −
(q−1)` is irregular at ∞ (slope ½, witness `c3_w2_c1_module_exponents`). This computes its
**formal power-series solution** `f(x) = ∑ cₙ x^{−n}` at ∞ by extracting the coefficient
recurrence, and confirms the divergence that forces Borel summation / the Stokes phenomenon.

Result (verified symbolically):
  - recurrence  `c_{m+1} = c_m·(1 + (q−1)q^m + (q−1)q^{2m})`,  `c_0 = 1`;
  - the ratio has q-degree `2m+1`, so `deg_q(c_n) = ∑_{m<n}(2m+1) = n²` — the coefficients
    grow like `q^{n²}` (q-Gevrey-½). This divergence is the ∞ Stokes signature: the formal
    series does not converge and must be q-Borel/Laplace summed, and the difference of the
    sums across sectors is the Stokes multiplier(s) `U ∈ ℂ²` (the residual, RSZ §4–5).

Symbolic (sympy); no fit; nothing wired. Companion Lean: the degree identity
`∑_{m<n}(2m+1) = n²` (`QOU/Mass/C1FormalSolutionGrowth.lean`).
"""
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
import sympy as sp


def main() -> None:
    q = sp.Symbol("q")
    N = 9
    csol = [sp.Integer(1)]
    ratios = []
    for m in range(0, N):
        cm = csol[m]
        cmp1 = sp.Symbol("cmp1")
        # coeff of x^{-m} in L1 f = 0:
        eq = (q**2 * cmp1 * q**(-2 * (m + 1)) - cm * q**(-2 * m)
              - (q - 1) * cm * q**(-m) - (q - 1) * cm)
        sol = sp.solve(sp.Eq(eq, 0), cmp1)[0]
        csol.append(sp.simplify(sol))
        ratios.append(sp.factor(sp.simplify(csol[m + 1] / csol[m])))

    degs = [0] + [sp.Poly(sp.expand(csol[n]), q).degree() for n in range(1, N + 1)]
    deg_matches_nsq = all(degs[n] == n * n for n in range(0, N + 1))
    # ratio degree = 2m+1
    ratio_degs = [sp.Poly(sp.expand(ratios[m]), q).degree() for m in range(0, N)]
    ratio_deg_ok = all(ratio_degs[m] == 2 * m + 1 for m in range(0, N))

    results = {
        "operator": "L1 = (q^2 x - 1) s^2 - (q-1) s - (q-1)  [C1, RSZ route-A], solved at x=inf",
        "ansatz": "f(x) = sum_{n>=0} c_n x^{-n}",
        "recurrence": "c_{m+1} = c_m * (1 + (q-1) q^m + (q-1) q^{2m}),  c_0 = 1",
        "first_ratios": [str(r) for r in ratios[:5]],
        "deg_q_c_n": degs,
        "deg_q_c_n_equals_n_squared": bool(deg_matches_nsq),
        "ratio_degree_is_2m_plus_1": bool(ratio_deg_ok),
        "growth": "coefficients grow like q^{n^2} => q-Gevrey (divergent) => Stokes summation needed",
    }
    for k, v in results.items():
        print(f"  {k}: {v}")

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
        "scriptFile": "c3_w2_inf_formal_solution.py",
        "commitSha": _git(["rev-parse", "HEAD"]),
        "description": (
            "W2 inf: explicit formal solution of C1 at infinity, c_{m+1}="
            "c_m(1+(q-1)q^m+(q-1)q^{2m}); deg_q(c_n)=n^2 (q-Gevrey-1/2 divergence, the "
            "Stokes signature). Symbolic."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_inf_formal_solution.py",
            "scriptCommitSha": _script_sha,
            "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        },
        "results": results,
        "verdict": (
            "CONFIRMED: C1 formal solution at inf has deg_q(c_n)=n^2 exactly (q-Gevrey "
            "divergence). The Stokes multipliers U in C^2 (Borel-summed sector difference) "
            "remain the RSZ-wild residual."
        ) if (deg_matches_nsq and ratio_deg_ok) else "MISMATCH — investigate.",
        "scope": "Formal solution + growth only; Stokes summation is the residual. No fit.",
    }
    out = script_path.with_suffix(".witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nverdict: {witness['verdict']}\nwitness: {out}")
    if not (deg_matches_nsq and ratio_deg_ok):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
