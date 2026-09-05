#!/usr/bin/env python3
"""C1 ∞-side: PROVE deg_q(c_n) = n^2, and record the leading coefficient.

Upgrades the 2026-08-01 record (`docs/audits/2026-08-01-c1-inf-formal-solution-qgevrey.md`),
where `deg_q(c_n) = n^2` is stated as "verified symbolically for n <= 9". That
degree law is what carries the q-Gevrey slope-1/2 claim -- i.e. the statement
that the C1 formal solution at infinity is divergent and must be q-Borel/Laplace
summed. A spot-check to n <= 9 is not a proof of an all-n claim, and per the
formalize-first discipline the invariant that prunes a search should be proved
before the search is run.

THE PROOF (elementary, complete)
--------------------------------
The recurrence is

    c_{m+1} = c_m * f_m,   f_m := 1 + (q-1) q^m + (q-1) q^{2m},   c_0 = 1.

Expand f_m = 1 - q^m - q^{2m} + q^{m+1} + q^{2m+1}.

  * m >= 1: the exponents m, 2m, m+1, 2m+1 are distinct and 2m+1 is strictly
    the largest, so no cancellation can touch the top: deg f_m = 2m+1 with
    leading coefficient 1.
  * m = 0:  the two (q-1) terms COLLIDE, f_0 = 1 + 2(q-1) = 2q - 1, which has
    deg 1 = 2*0+1 -- the same degree the general formula predicts -- but
    leading coefficient 2, not 1.

Degrees add under multiplication over the integral domain Z[q], so

    deg c_n = sum_{m=0}^{n-1} (2m+1) = n^2 .                    [] proved

and the leading coefficient is the product of the leading coefficients,
    lc(c_n) = 2 * 1 * ... * 1 = 2   for n >= 1   (lc(c_0) = 1).

So the degree law holds for ALL n, not merely n <= 9, and the slope-1/2
conclusion drawn from it is rigorous rather than empirical.

WHAT THIS SCRIPT DOES
---------------------
Independently re-derives the coefficients by exact polynomial arithmetic over
Z[q] (integer dicts -- no floats, no sympy) and checks both claims out to
n = 30, i.e. 3x the previously recorded window. It is a CHECK of a proved
statement, not the evidence for it.

Nothing here is fitted and nothing is wired to production.
"""

from __future__ import annotations

import json
import os
import subprocess
from typing import Dict

Poly = Dict[int, int]  # exponent -> coefficient, over Z[q]

N_MAX = 30


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = e1 + e2
            out[k] = out.get(k, 0) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def factor(m: int) -> Poly:
    """f_m = 1 + (q-1) q^m + (q-1) q^{2m}, expanded exactly."""
    f: Poly = {0: 1}
    for e in (m, 2 * m):
        f[e + 1] = f.get(e + 1, 0) + 1
        f[e] = f.get(e, 0) - 1
    return {e: c for e, c in f.items() if c != 0}


def degree(p: Poly) -> int:
    return max(p)


def leading_coeff(p: Poly) -> int:
    return p[max(p)]


def main() -> None:
    c: Poly = {0: 1}
    rows = []
    degree_law_holds = True
    lc_law_holds = True

    for n in range(0, N_MAX + 1):
        if n > 0:
            c = mul(c, factor(n - 1))
        d = degree(c)
        lc = leading_coeff(c)
        expected_d = n * n
        expected_lc = 1 if n == 0 else 2
        ok_d = d == expected_d
        ok_lc = lc == expected_lc
        degree_law_holds &= ok_d
        lc_law_holds &= ok_lc
        rows.append(
            {
                "n": n,
                "deg_q_c_n": d,
                "n_squared": expected_d,
                "degree_matches": ok_d,
                "leading_coeff": lc,
                "leading_coeff_matches": ok_lc,
                "n_terms": len(c),
            }
        )

    # Per-factor degrees: the inductive step, checked directly.
    factor_rows = []
    factor_law_holds = True
    for m in range(0, N_MAX):
        fm = factor(m)
        d = degree(fm)
        ok = d == 2 * m + 1
        factor_law_holds &= ok
        factor_rows.append(
            {
                "m": m,
                "deg_f_m": d,
                "two_m_plus_1": 2 * m + 1,
                "matches": ok,
                "leading_coeff": leading_coeff(fm),
            }
        )

    print(f"{'n':>3} {'deg_q(c_n)':>11} {'n^2':>6} {'ok':>5} {'lc':>4}")
    for r in rows:
        if r["n"] <= 12 or r["n"] % 5 == 0:
            print(
                f"{r['n']:>3} {r['deg_q_c_n']:>11} {r['n_squared']:>6} "
                f"{str(r['degree_matches']):>5} {r['leading_coeff']:>4}"
            )
    print()
    print(f"deg_q(c_n) == n^2 for all n <= {N_MAX} : {degree_law_holds}")
    print(f"lc(c_n) == 2 for 1 <= n <= {N_MAX}     : {lc_law_holds}")
    print(f"deg f_m == 2m+1 for all m < {N_MAX}    : {factor_law_holds}")

    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=here, stderr=subprocess.DEVNULL,
        ).decode().strip() or "uncommitted"
    except Exception:
        sha = "uncommitted"

    witness = {
        "schema": "witness/v1",
        "description": (
            "C1 infinity-side degree law deg_q(c_n) = n^2: elementary proof "
            "(recorded in the module docstring and the companion audit) plus an "
            "exact Z[q] check to n=30. Upgrades the 2026-08-01 'verified "
            "symbolically for n <= 9' spot-check to an all-n statement, and "
            "records lc(c_n) = 2 for n >= 1 (the m=0 collision), which the "
            "earlier record did not note."
        ),
        "computation": {"script": os.path.relpath(script, os.path.dirname(here))},
        "witness": {"scriptCommitSha": sha},
        "recurrence": "c_{m+1} = c_m * (1 + (q-1) q^m + (q-1) q^{2m}), c_0 = 1",
        "claims": {
            "degree_law": "deg_q(c_n) = n^2 for all n >= 0",
            "degree_law_status": "PROVED (elementary induction; degrees add over Z[q])",
            "leading_coeff_law": "lc(c_n) = 2 for n >= 1, lc(c_0) = 1",
            "leading_coeff_status": "PROVED (lc multiplies; only f_0 has lc != 1)",
            "factor_degree": "deg f_m = 2m+1 for all m >= 0",
        },
        "verification": {
            "n_max": N_MAX,
            "previous_recorded_window": 9,
            "degree_law_holds": degree_law_holds,
            "leading_coeff_law_holds": lc_law_holds,
            "factor_degree_law_holds": factor_law_holds,
            "arithmetic": "exact integer polynomial arithmetic over Z[q]; no floats",
        },
        "rows": rows,
        "factor_rows": factor_rows,
        "wired_to_production": False,
        "is_fit": False,
    }
    out = os.path.join(here, "c1-inf-degree-law-proof-probe.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(out, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    print(f"\nwitness -> {os.path.relpath(out)}")


if __name__ == "__main__":
    main()
