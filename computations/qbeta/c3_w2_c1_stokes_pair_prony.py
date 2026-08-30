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

## CORRECTION (added after the diagnostic below): the pair is NOT two Stokes sectors

An earlier revision of this docstring read the antipodality as the two-sector
structure, "the ± of the leading blocks propagating into the Borel plane".
**That reading is withdrawn.** It was circular, and the diagnostic added at the
end of `main()` shows why.

The asymptotic recurrence is `b_{m+2} ≈ K q^{−m} b_m` because
`b_{m+1}/b_m → 0` — measured at **9.3e-24 by m = 1000**. A two-step recurrence
`c_{m+2} = λ c_m` has characteristic roots `±√λ`, so it **manufactures an
antipodal pair by construction**. The exactness of `ξ₂/ξ₁ = −1` (21 digits) and
its branch-independence (2.2e-29) are precisely what that mechanism predicts —
a genuine two-sector Stokes structure would not generically give ratio exactly
−1 to 21 digits.

The even/odd decoupling and the ramification index 2 are the *same* structure
seen at two levels of description, so "the ± matches the leading blocks" is not
independent evidence of anything. The match was guaranteed.

**Consequence for the multipliers: this route does not reach them.** The
Prony pair resolves the even/odd split, not the connection data between Stokes
sectors. The alternating component is suppressed by ~1e-24 in the asymptotic
regime, so the sector information the multipliers encode is not visible in the
raw `b_m` at all. Extracting them needs the theta-normalised canonical
solutions inside the ramified single-slope picture — which this method does not
construct.

Scope-(a) negative on the Prony/ratio route. The numbers below stand; only the
sector interpretation is withdrawn.

## What is and is not canonical here

`ξ₂/ξ₁ = −1` is **convention-independent**, but per the correction above it is
*not* a Stokes datum — it is the signature of the even/odd decoupling.

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
# PATH BRIDGE — required before the provenance stamp can import
# `qou_substrate` (bean qou-ya1e). That module is not installed and not on
# PYTHONPATH; it is reachable only through `_path_bridge`, which
# `migrate_bare_producer_provenance.py` inserted the stamp WITHOUT. The
# import sits at function scope, so this producer did all its work and then
# died at the save with ModuleNotFoundError. Idiom copied verbatim from
# `qbeta/qbeta_c3_candidate_audit.py`.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

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
    print()
    print("=" * 70)
    print("  DIAGNOSTIC: is the pair Stokes structure, or two-step decoupling?")
    print("=" * 70)
    print("  b_{m+2} ~ K q^{-m} b_m holds when b_{m+1}/b_m -> 0. A two-step")
    print("  recurrence c_{m+2} = lam c_m has char roots +/- sqrt(lam) --")
    print("  it MANUFACTURES an antipodal pair with no Stokes content.")
    bb = _solutions(1, 0, q, N)
    ratios = []
    for m in (200, 600, 1000):
        rr = bb[m + 1] / bb[m]
        ratios.append((m, rr))
        print(f"    m={m:5d}   b_(m+1)/b_m = {mp.nstr(rr, 6)}")
    two_step = abs(ratios[-1][1]) < mp.mpf("1e-15")
    print()
    print(f"  two-step regime dominant: {two_step}")
    print("  => the antipodality is EXPLAINED by the decoupling. The sector")
    print("     reading is withdrawn; this route does not reach the multipliers.")
    print()
    print(f"    |xi| = {mp.nstr(v1, 20)}   (log_q = {mp.nstr(mp.log(v1) / lq, 16)})")
    print("    NOT canonical: |xi| depends on the q-Borel normalisation")
    print("    (here c_m = b_m q^{m(m-1)/4}). No identification attempted.")
    print("    xi_2/xi_1 = -1 is convention-independent but, per the diagnostic")
    print("    above, is the two-step decoupling signature -- NOT a Stokes datum.")

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
            "MIXED. CONFIRMED numerically: the q-Borel singularities form an exact "
            "antipodal pair, branch-independent to 2.2e-29 -- superseding step 2's "
            "'two nearby singularities' reading. WITHDRAWN: the interpretation of that "
            "pair as the two Stokes sectors. The diagnostic shows b_(m+1)/b_m -> 9.3e-24, "
            "so the recurrence is effectively two-step, and a two-step recurrence has "
            "characteristic roots +/- sqrt(lam) -- it manufactures an antipodal pair with "
            "no Stokes content. The match to the +/- of the leading blocks was circular "
            "(even/odd decoupling and ramification index 2 are the same structure). "
            "SCOPE-(a) NEGATIVE on the Prony/ratio route to the multipliers: the "
            "alternating component is suppressed by ~1e-24, so sector information is not "
            "visible in the raw b_m. Reaching the multipliers needs theta-normalised "
            "canonical solutions in the ramified picture, which this method does not build."
        ),
        "two_step_diagnostic": {
            "b_ratio_by_m": [{"m": int(m), "b_m1_over_b_m": str(mp.nstr(r, 8))} for m, r in ratios],
            "two_step_regime_dominant": bool(two_step),
            "sector_interpretation_withdrawn": True,
        },
        "scope": (
            "Separates and characterises the singularity pair. Does NOT extract the "
            "Stokes multipliers. |xi| deliberately not identified (normalisation-dependent). "
            "Numerical, no fit, nothing wired."
        ),
        "durationMs": int((time.perf_counter() - _t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-stokes-pair-prony.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=1) + "\n")
    n_pass = sum(1 for a in witness["assertions"] if a["passed"])
    print(f"\n  Witness: {out.name}  ({n_pass}/{len(witness['assertions'])} assertions passed)")


if __name__ == "__main__":
    main()
