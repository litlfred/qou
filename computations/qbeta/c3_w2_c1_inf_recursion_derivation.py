#!/usr/bin/env python3
"""The C1 `inf`-side recursion, derived from L1 rather than taken from a witness.

Bean `qou-slpd` item 4 (remainder). `QOU/Mass/C1FormalSolutionGrowth.lean` builds
its whole growth chain on

    c_{m+1} = c_m * (1 + (q-1) q^m + (q-1) q^{2m}),   c_0 = 1

and that recursion entered the corpus from
`computations/qbeta/c3-w2-inf-formal-solution.witness.json` — i.e. asserted, not
derived. Everything above it in the chain is now Lean (ratio degree 2m+1,
deg_q c_n = n^2, q-Gevrey order 2 / level 1/2), so this was the last
witness-sourced input on that strand.

## What is checked here, and what is checked in Lean

The operator, in x = q^m with sigma: x -> q x
(docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md section 1):

    L1 = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1)

Applied to the `inf`-side ansatz f = sum_{k>=0} c_k x^{-k}, using
sigma(x^{-k}) = q^{-k} x^{-k}, the coefficient of x^{-n} collects four terms:

    q^2 * q^{-2(n+1)} c_{n+1}      from  q^2 x * sigma^2 f   (index shift k=n+1)
      - q^{-2n} c_n                from  - sigma^2 f
      - (q-1) q^{-n} c_n           from  - (q-1) sigma f
      - (q-1) c_n                  from  - (q-1) f

**This script machine-checks that collection** — symbolically, with a truncated
series and symbolic coefficients, so the term-by-term reading is verified rather
than eyeballed. The Lean side (`l1CoeffAt_eq_zero_iff`) then proves that this
expression vanishes **iff** the recursion holds. Together the two close the gap:
recursion <=> L1 annihilates the ansatz's x^{-n} coefficients.

## The obstruction, stated because it is real

The ansatz does NOT satisfy `L1 f = 0` outright. Multiplying by x shifts the
k = 0 term of sigma^2 f up to x^{+1}, leaving

    coefficient of x^{+1} in L1 f  =  q^2 c_0

which is nonzero exactly when c_0 != 0 — and the corpus takes c_0 = 1. So the
honest statement is: the recursion is equivalent to L1 f having **no x^{-n} term
for any n >= 0**, with a single leftover at x^{+1}. That leftover is what a
nonzero Newton slope forces — a pure power series in 1/x cannot be a solution of
an irregular operator; a characteristic prefactor is needed. This script checks
the leftover too, so it is on the record rather than quietly dropped.

-- Ref: [manuscript] docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md
-- Ref: [ramis-sauloy-zhang2013] Asterisque 355 section 2.2 (Newton polygon)
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import sympy as sp

N = 8  # truncation: coefficients of x^{-n} are exact for 0 <= n <= N


def main() -> None:
    t0 = time.perf_counter()
    q, x = sp.symbols("q x", positive=True)
    c = sp.symbols(f"c0:{N + 2}")

    f = sum(c[k] * x ** (-k) for k in range(N + 2))

    def sigma(g):
        """sigma : x -> q x."""
        return g.subs(x, q * x)

    L1f = sp.expand((q ** 2 * x - 1) * sigma(sigma(f))
                    - (q - 1) * sigma(f)
                    - (q - 1) * f)

    # clear denominators so sympy can treat it as a polynomial in x
    shift = N + 1
    P = sp.Poly(sp.expand(L1f * x ** shift), x)

    def coeff_of_x_pow(e: int):
        """coefficient of x^e in L1 f."""
        return sp.simplify(P.coeff_monomial(x ** (e + shift)))

    def predicted(n: int):
        return sp.simplify(
            q ** 2 * q ** (-2 * (n + 1)) * c[n + 1]
            - q ** (-2 * n) * c[n]
            - (q - 1) * q ** (-n) * c[n]
            - (q - 1) * c[n]
        )

    res: dict = {}
    checks: list = []

    print("=" * 78)
    print("  1. coefficient of x^{-n} in L1 f  vs  the four-term collection")
    print("=" * 78)
    print(f"    truncation N = {N}; exact for 0 <= n <= N")
    print()
    print(f"    {'n':>4}  {'coeff(L1 f, x^-n) - predicted':>34}")
    all_match = True
    for n in range(N + 1):
        diff = sp.simplify(sp.expand(coeff_of_x_pow(-n) - predicted(n)))
        ok = diff == 0
        all_match = all_match and ok
        print(f"    {n:>4}  {str(diff):>34}   {'OK' if ok else 'MISMATCH'}")
    res["coefficient_match_all_n"] = bool(all_match)
    checks.append({
        "name": "l1_coefficient_is_the_four_term_collection",
        "detail": f"symbolic, n = 0..{N}, symbolic c_k: coefficient of x^-n in "
                  "L1 f equals q^2 q^{-2(n+1)} c_{n+1} - q^{-2n} c_n "
                  "- (q-1) q^{-n} c_n - (q-1) c_n. This is what "
                  "QOU.Mass.C1FormalSolutionGrowth.l1CoeffAt encodes.",
        "passed": bool(all_match),
    })
    print()

    print("=" * 78)
    print("  2. the recursion is exactly what makes those coefficients vanish")
    print("=" * 78)
    rec_ok = True
    for n in range(N + 1):
        # solve coefficient(x^-n) = 0 for c_{n+1}
        sol = sp.solve(sp.Eq(coeff_of_x_pow(-n), 0), c[n + 1])
        want = sp.simplify(c[n] * (1 + (q - 1) * q ** n + (q - 1) * q ** (2 * n)))
        got = sp.simplify(sol[0]) if sol else None
        ok = got is not None and sp.simplify(got - want) == 0
        rec_ok = rec_ok and ok
        if n < 4 or not ok:
            print(f"    n={n}: c_{n + 1} = {sp.simplify(got)}")
            print(f"         want  = {want}   {'OK' if ok else 'MISMATCH'}")
    print(f"    ... all n = 0..{N}: {'OK' if rec_ok else 'MISMATCH'}")
    res["recursion_recovered_all_n"] = bool(rec_ok)
    checks.append({
        "name": "recursion_is_equivalent_to_vanishing_coefficients",
        "detail": "solving coeff(x^-n) = 0 for c_{n+1} returns exactly "
                  "c_n (1 + (q-1) q^n + (q-1) q^{2n}) for every n = 0.."
                  f"{N}. Lean proves the same equivalence in general as "
                  "l1CoeffAt_eq_zero_iff.",
        "passed": bool(rec_ok),
    })
    print()

    print("=" * 78)
    print("  3. the leftover at x^{+1} — the ansatz does NOT solve L1 f = 0")
    print("=" * 78)
    obstruction = coeff_of_x_pow(1)
    want_obs = sp.simplify(q ** 2 * c[0])
    obs_ok = sp.simplify(obstruction - want_obs) == 0
    print(f"    coeff(L1 f, x^+1) = {obstruction}")
    print(f"    predicted q^2 c_0 = {want_obs}    {'OK' if obs_ok else 'MISMATCH'}")
    print("    With c_0 = 1 this is q^2 != 0. So the recursion characterises")
    print("    'no x^{-n} term for n >= 0', not 'L1 f = 0'. A pure power series")
    print("    in 1/x cannot solve an operator with a nonzero Newton slope.")
    res["obstruction"] = str(obstruction)
    checks.append({
        "name": "x_plus_one_obstruction_is_q_squared_c0",
        "detail": "the ansatz leaves exactly one term outside the x^{-n} range, "
                  "coeff = q^2 c_0, nonzero for c_0 = 1. Recorded rather than "
                  "dropped; Lean carries it as l1Obstruction.",
        "passed": bool(obs_ok),
    })
    print()

    print("=" * 78)
    print("  4. no other leftover: every power above x^{+1} vanishes")
    print("=" * 78)
    extra = [sp.simplify(coeff_of_x_pow(e)) for e in range(2, 5)]
    extra_ok = all(e == 0 for e in extra)
    print(f"    coefficients of x^2, x^3, x^4 : {[str(e) for e in extra]}")
    print(f"    all zero: {extra_ok}")
    res["higher_powers_vanish"] = bool(extra_ok)
    checks.append({
        "name": "no_leftovers_above_x_plus_one",
        "detail": "x^2, x^3, x^4 coefficients are identically zero, so x^{+1} is "
                  "the only obstruction.",
        "passed": bool(extra_ok),
    })
    print()

    passed = all(ch["passed"] for ch in checks)
    print("=" * 78)
    print(f"  {sum(ch['passed'] for ch in checks)}/{len(checks)} checks passed")
    print("=" * 78)
    print("""
  CONCLUSION.  The C1 inf-side recursion is DERIVED from
  L1 = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1), not taken from a witness. The
  coefficient of x^{-n} in L1 f is the four-term collection above (checked here
  symbolically), and it vanishes iff c_{n+1} = c_n (1 + (q-1)q^n + (q-1)q^{2n})
  (proved in Lean, l1CoeffAt_eq_zero_iff). The single leftover at x^{+1} is
  q^2 c_0, which is the expected signature of a nonzero Newton slope and is now
  on the record.
""")

    script_path = Path(__file__).resolve()
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                             text=True, cwd=script_path.parent).stdout.strip()
    except Exception:
        sha = "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "sympy",
        "scriptFile": script_path.name,
        "scriptSha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "commitSha": sha or "unknown",
        "description":
            "Bean qou-slpd item 4 (remainder). Derives the C1 inf-side "
            "recursion c_{m+1} = c_m (1 + (q-1)q^m + (q-1)q^{2m}) from the "
            "operator L1 = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1), replacing "
            "the witness-sourced assertion that QOU.Mass.C1FormalSolutionGrowth "
            "built its growth chain on. Applies L1 symbolically to a truncated "
            "ansatz f = sum c_k x^{-k} with symbolic coefficients and checks "
            "that the coefficient of x^{-n} is exactly the four-term collection "
            "q^2 q^{-2(n+1)} c_{n+1} - q^{-2n} c_n - (q-1)q^{-n} c_n - (q-1) c_n "
            "for every n = 0..8 — the term-by-term reading that Lean's l1CoeffAt "
            "encodes and that would otherwise be inspection. Solving those "
            "coefficients for c_{n+1} returns the recursion. Also records the "
            "single leftover at x^{+1}, equal to q^2 c_0 and hence nonzero for "
            "c_0 = 1: the ansatz does not satisfy L1 f = 0 outright, which is "
            "the expected signature of a nonzero Newton slope, and every power "
            "above x^{+1} vanishes.",
        "computation": {
            "operator": "(q^2 x - 1) sigma^2 - (q-1) sigma - (q-1), sigma: x -> q x",
            "ansatz": "f = sum_{k=0}^{N+1} c_k x^{-k}, symbolic c_k",
            "truncation": N,
            "exactRange": f"coefficients of x^-n exact for 0 <= n <= {N}",
        },
        "results": res,
        "checks": checks,
        "verdict":
            "The recursion is derived, not asserted. Coefficient of x^-n in "
            "L1 f = the four-term collection (symbolic, all n = 0..8), and Lean's "
            "l1CoeffAt_eq_zero_iff proves that collection vanishes iff the "
            "recursion holds — so recursion <=> L1 kills every x^{-n} "
            "coefficient. The one honest caveat, now recorded in both the script "
            "and Lean (l1Obstruction): the ansatz leaves q^2 c_0 at x^{+1}, so it "
            "is not a solution of L1 f = 0 outright. That is what a nonzero "
            "Newton slope forces, and it does not affect the growth chain, which "
            "only ever used the recursion. Nothing wired to production.",
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-inf-recursion-derivation.witness.json"
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
    print(f"  witness -> {out.name}   ({witness['durationMs']} ms)")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
