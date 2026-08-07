#!/usr/bin/env python3
"""C1 ∞-side, step 3: resolve the q-Borel singularity pair (two-pole Prony).

Bean `qou-odh5`. Step 2 (`c3_w2_c1_qborel_singularity.py`) found that the
plain ratio test `c_{m+1}/c_m` converges to ~1e-10 *within* a branch but gives
answers differing by 3.7e-4 *between* branches, and read that as "two nearby
singularities". This script resolves the structure properly and the picture is
cleaner than that reading.

## Method

A single-pole ratio test cannot see a pair. Assume instead

    c_m  ~  A₁ r₁^m + A₂ r₂^m      (large m)

and recover `r₁, r₂` from the 2-term linear recurrence they satisfy
(`c_{m+2} = p·c_{m+1} + s·c_m`), solved from two consecutive triples — a
two-pole Prony / Hankel fit. The singularities are `ξ_i = 1/r_i`.

## Result

**The two singularities are an exact antipodal pair.**

    ξ₁ = +2.3651035824525764564
    ξ₂ = −2.3651035824525764564
    ξ₁ + ξ₂ = 2.1e-21      (numerical zero at 600 dps)

Converged to 14 digits by m = 700 and stable to m = 1000.

**It is a module invariant, not a branch artifact.** The two independent
solution branches `(b₀,b₁) = (1,0)` and `(0,1)` give the same `|ξ|` to
**2.2e-29**. This *corrects* step 2's reading: the 3.7e-4 "branch spread"
there was the single-pole ratio test blending an antipodal pair in
branch-dependent proportions, not two genuinely different singularities per
branch. There is one pair, shared.

**This is the ± of the leading blocks.** Step 1 found
`B₁,₂ = ±√(q−1)/q` from the ramified edge polynomial. The sign-symmetry of
the leading blocks propagates exactly to the sign-symmetry of the Borel
singularities — as it must, since the ramification `x = z²` is what
introduced the square root in the first place.

## What is and is not canonical here

`ξ₂/ξ₁ = −1` is **convention-independent** and is the Stokes-relevant datum
at this level: the two singular directions are antipodal.

`|ξ| = 2.36510358…` is **not** canonical — it depends on the normalisation
chosen for the q-Borel transform (here `c_m = b_m q^{m(m−1)/4}`; another
admissible convention shifts `|ξ|` by a power of `q`). No identification of
`|ξ|` is attempted for that reason, and none should be read into its
proximity to `q^{33/4}`.

## Scope

Locates and separates the singularity pair. Does **not** compute the Stokes
multipliers, which are the residues/connection data at these points.
Numerical, no fit to any target, nothing wired.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import time
from pathlib import Path
import mpmath as mp

DPS = 600
N = 1200


def _q_int(k, q):
    return (q**k - q**(-k)) / (q - 1 / q)


def _solutions(b0, b1, q, n):
    b = [mp.mpf(b0), mp.mpf(b1)]
    for m in range(n):
        b.append((b[m + 1] + b[m]) / _q_int(m + 2, q))
    return b


def _prony2(c, m):
    """Two-pole Prony: recover the pair (1/r1, 1/r2) from c_m..c_{m+3}."""
    M = mp.matrix([[c[m + 1], c[m]], [c[m + 2], c[m + 1]]])
    rhs = mp.matrix([c[m + 2], c[m + 3]])
    p, s = mp.lu_solve(M, rhs)
    disc = p * p + 4 * s
    r1 = (p + mp.sqrt(disc)) / 2
    r2 = (p - mp.sqrt(disc)) / 2
    return 1 / r1, 1 / r2


def main() -> None:
    _t0 = time.perf_counter()
    mp.mp.dps = DPS
    q = mp.mpf("1.1099785827513808075916690956")
    lq = mp.log(q)

    print("=" * 70)
    print("  Two-pole Prony: separating the q-Borel singularity pair")
    print("=" * 70)

    conv = []
    b = _solutions(1, 0, q, N)
    c = [b[m] * q**(mp.mpf(m) * (m - 1) / 4) for m in range(N)]
    for m in (300, 500, 700, 1000):
        x1, x2 = _prony2(c, m)
        conv.append((m, x1, x2))
        print(f"    m={m:5d}   xi_1 = {mp.nstr(x1, 16):>22s}   xi_2 = {mp.nstr(x2, 16):>22s}")
    print()

    branch = {}
    for name, (i0, i1) in [("b^(1) (1,0)", (1, 0)), ("b^(2) (0,1)", (0, 1))]:
        bb = _solutions(i0, i1, q, N)
        cc = [bb[m] * q**(mp.mpf(m) * (m - 1) / 4) for m in range(N)]
        x1, x2 = _prony2(cc, 1000)
        branch[name] = (x1, x2)
        print(f"    {name}:  xi = {mp.nstr(x1, 20)} , {mp.nstr(x2, 20)}")
        print(f"                 xi_1 + xi_2 = {mp.nstr(x1 + x2, 6)}   (0 => exact antipodal pair)")

    v1 = abs(branch["b^(1) (1,0)"][0])
    v2 = abs(branch["b^(2) (0,1)"][0])
    branch_agree = abs(v1 - v2) / v1
    pair_sum = abs(branch["b^(1) (1,0)"][0] + branch["b^(1) (1,0)"][1]) / v1
    ratio = branch["b^(1) (1,0)"][1] / branch["b^(1) (1,0)"][0]

    print()
    print(f"    branch agreement on |xi| : {mp.nstr(branch_agree, 6)}")
    print(f"    xi_2 / xi_1              : {mp.nstr(ratio, 18)}")
    print()
    print("    => ONE antipodal pair, shared by both branches (a module")
    print("       invariant). Step 2's 3.7e-4 'branch spread' was the")
    print("       single-pole ratio test blending this pair in")
    print("       branch-dependent proportions, not distinct singularities.")
    print()
    B = mp.sqrt(q - 1) / q
    print(f"    leading blocks B_1,2 = +/- {mp.nstr(B, 16)}")
    print("    the +/- of the blocks propagates to the +/- of the singularities,")
    print("    as it must: the ramification x = z^2 introduced the square root.")
    print()
    print(f"    |xi| = {mp.nstr(v1, 20)}   (log_q = {mp.nstr(mp.log(v1) / lq, 16)})")
    print("    NOT canonical: |xi| depends on the q-Borel normalisation")
    print("    (here c_m = b_m q^{m(m-1)/4}). No identification attempted.")
    print("    xi_2/xi_1 = -1 IS canonical and is the Stokes-relevant datum.")

    script_path = Path(__file__).resolve()
    try:
        sha = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(script_path)],
                             capture_output=True, text=True, check=False).stdout.strip() or "unknown"
    except Exception:
        sha = "unknown"

    witness = {
        "schema": "witness/v1",
        "engine": "mpmath",
        "scriptFile": script_path.name,
        "commitSha": sha,
        "description": (
            "C1 infinity step 3 (bean qou-odh5). Two-pole Prony resolves the q-Borel "
            "singularity structure into an EXACT ANTIPODAL PAIR xi = +/- 2.36510358..., "
            "sum zero to 21 digits, branch-independent to 2.2e-29. This corrects step 2's "
            "reading of a 3.7e-4 'branch spread' as two nearby singularities: that was a "
            "single-pole ratio test blending one antipodal pair. The +/- matches the "
            "leading blocks B = +/- sqrt(q-1)/q. |xi| is normalisation-dependent and is "
            "NOT identified; xi_2/xi_1 = -1 is the canonical datum. Multipliers not extracted."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_c1_stokes_pair_prony.py",
            "scriptCommitSha": sha,
            "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        },
        "results": {
            "method": "two-pole Prony / Hankel on c_m = b_m q^{m(m-1)/4}",
            "dps": DPS,
            "n_terms": N,
            "xi_1": str(mp.nstr(branch["b^(1) (1,0)"][0], 20)),
            "xi_2": str(mp.nstr(branch["b^(1) (1,0)"][1], 20)),
            "xi_ratio": str(mp.nstr(ratio, 18)),
            "pair_sum_relative": str(mp.nstr(pair_sum, 6)),
            "branch_agreement_relative": str(mp.nstr(branch_agree, 6)),
            "leading_blocks_B": str(mp.nstr(B, 16)),
            "abs_xi_is_normalisation_dependent": True,
            "corrects": (
                "step 2 (c3-w2-c1-qborel-singularity.witness.json) read the 3.7e-4 "
                "branch spread as two nearby singularities; it is one antipodal pair "
                "blended by a single-pole estimator"
            ),
        },
        "assertions": [
            {"name": "exact_antipodal_pair",
             "computed": str(mp.nstr(pair_sum, 4)), "expected": "<1e-15",
             "passed": pair_sum < mp.mpf("1e-15")},
            {"name": "ratio_is_minus_one",
             "computed": str(mp.nstr(ratio, 12)), "expected": "-1",
             "passed": abs(ratio + 1) < mp.mpf("1e-15")},
            {"name": "branch_independent_module_invariant",
             "computed": str(mp.nstr(branch_agree, 4)), "expected": "<1e-20",
             "passed": branch_agree < mp.mpf("1e-20")},
        ],
        "verdict": (
            "CONFIRMED: the q-Borel singularities of C1 form an exact antipodal pair, "
            "branch-independent to 2.2e-29, mirroring the +/- of the leading blocks "
            "B = +/- sqrt(q-1)/q. Supersedes step 2's 'two nearby singularities' reading. "
            "The Stokes multipliers (residues at the pair) remain open."
        ),
        "scope": (
            "Separates and characterises the singularity pair. Does NOT extract the "
            "Stokes multipliers. |xi| deliberately not identified (normalisation-dependent). "
            "Numerical, no fit, nothing wired."
        ),
        "durationMs": int((time.perf_counter() - _t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-stokes-pair-prony.witness.json"
    out.write_text(json.dumps(witness, indent=1) + "\n")
    n_pass = sum(1 for a in witness["assertions"] if a["passed"])
    print(f"\n  Witness: {out.name}  ({n_pass}/{len(witness['assertions'])} assertions passed)")


if __name__ == "__main__":
    main()
