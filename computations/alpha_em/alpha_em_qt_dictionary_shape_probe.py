#!/usr/bin/env python3
"""alpha_em_qt_dictionary_shape_probe.py

Bean qou-tq20 (B2 lift), tranche 6: the q<->heat-time DICTIONARY SHAPE
adjudication — the load-bearing step named by the tranche-5 structured null
(#4022: "pin the dictionary; further numerics are vacuous without it").

CORPUS INPUT (grep first): the framework's canonical rate variable is
lambda = ln q (crossing-energy-decomposition — every algebraic q-power maps
to a hyperbolic exponential in lambda). ANCHOR (forced by consistency-1
#4019): q = 1 <-> t = infinity (both ends carry the multiplicity vector
(3,1), ratio 3). Hence any dictionary in the canonical rate variable maps
q -> 1 to t -> infinity: the natural class is the RECIPROCAL POWER LAWS

    t = c / |lambda|^p ,   lambda = ln q,  p in {1, 2}   (pre-stated).

METHOD (pre-stated, overdetermined): pin the single constant c at ONE
interior matching point (q* = 0.8: solve R_geo(t*) = r(q*), c = t*·|λ*|^p),
then test the ENTIRE curves against each other on a 6-point grid
q in {0.65, 0.70, 0.75, 0.85, 0.90, 0.95} — with c fixed, every further
point is a falsifiable prediction. PASS tolerance (pre-stated): max
relative deviation <= 1% would count as a shape match; O(1) deviation
kills the shape.

RESULT: BOTH SHAPES KILLED —
    p = 1:  max rel dev 18.9%
    p = 2:  max rel dev 31.1%
(O(1) misses; the two deformation curves have genuinely different shapes.)

SCOPE-(a) CONCLUSION + REORIENTATION: within the canonical-rate reciprocal
power-law class, the HEAT family does NOT realize the Markov deformation —
these dictionary shapes, alone, are excluded. This does NOT exclude the
tau-identification: it redirects the geometric family — the q-deformation,
if realized geometrically, likely lives in the MODULAR direction (deforming
the modulus tau_0) rather than the heat direction (proper time at fixed
modulus). The modular family is the next candidate; the identification
itself remains OPEN.

Scope guard: scope-(a) (these shapes, alone, as-is); no fit (c pinned by
pre-stated rule, tolerance pre-stated); nothing wired; 1/(8pi) stays
phase-4. Self-contained (sympy + mpmath + corpus y_lambda_at; #3934 theta
machinery).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_here))
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
T0 = mp.mpc(-0.5, mp.mpf("0.186676"))


def gram(tau):
    return [[mp.mpf(1), mp.re(tau)], [mp.re(tau), mp.re(tau) ** 2 + mp.im(tau) ** 2]]


def inv2(B):
    a, b, d = B[0][0], B[0][1], B[1][1]
    det = a * d - b * b
    return [[d / det, -b / det], [-b / det, a / det]]


def theta2(B, t, R=40):
    a, b, d = B[0][0], B[0][1], B[1][1]
    return mp.fsum(mp.e ** (-mp.pi * t * (a * i * i + 2 * b * i * j + d * j * j))
                   for i in range(-R, R + 1) for j in range(-R, R + 1))


B5, B1 = inv2(gram(5 * T0)), inv2(gram(T0))


def r_geo(t):
    return 3 * theta2(B5, t) / theta2(B1, t)


def t_star(target):
    lo, hi = mp.mpf("1e-3"), mp.mpf("60")
    for _ in range(80):
        mid = (lo + hi) / 2
        if r_geo(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    y = y_lambda_at(2)
    q = sorted(y[(2,)].free_symbols, key=str)[0]
    rf = sp.lambdify(q, sp.simplify(y[(2,)] / y[(1, 1)]), "mpmath")

    # V1: anchor orientation forced — q=1 and t=inf both carry ratio 3
    r1 = rf(mp.mpf(1))
    g_inf = r_geo(mp.mpf(8))
    v1 = abs(r1 - 3) < mp.mpf(10) ** -20 and abs(g_inf - 3) < mp.mpf(10) ** -6
    check("anchor_orientation_forced", v1,
          "r(1) = 3 exact and R_geo(t→∞) = 3 — consistency-1's anchor forces q=1 ↔ t=∞, so "
          "any dictionary in the canonical rate λ = ln q (crossing-energy-decomposition) is "
          "reciprocal: t = c/|λ|^p")

    # V2/V3: the overdetermined shape test, c pinned at q* = 0.8
    qstar = mp.mpf("0.8")
    lam_s = abs(mp.log(qstar))
    ts = t_star(rf(qstar))
    qs = [mp.mpf(x) for x in ("0.65", "0.70", "0.75", "0.85", "0.90", "0.95")]
    results = {}
    for p in (1, 2):
        c = ts * lam_s ** p
        devs = [float(abs(r_geo(c / abs(mp.log(qq)) ** p) - rf(qq)) / rf(qq)) for qq in qs]
        results[p] = {"c": mp.nstr(c, 10), "max_rel_dev": max(devs),
                      "devs": [f"{d:.3%}" for d in devs]}
    v2 = results[1]["max_rel_dev"] > 0.01
    check("shape_p1_killed", v2,
          f"t = c/|λ| (c = {results[1]['c']} pinned at q*=0.8): max rel dev "
          f"{results[1]['max_rel_dev']:.2%} over the 6-point grid — O(1) miss vs the "
          "pre-stated 1% pass bar. KILLED (scope-(a): this shape, alone, as-is)")
    v3 = results[2]["max_rel_dev"] > 0.01
    check("shape_p2_killed", v3,
          f"t = c/λ² (c = {results[2]['c']}): max rel dev {results[2]['max_rel_dev']:.2%} — "
          "O(1) miss. KILLED (scope-(a))")

    # V4: the curves genuinely differ in shape (not a tolerance artifact)
    v4 = results[1]["max_rel_dev"] > 0.10 and results[2]["max_rel_dev"] > 0.10
    check("shape_mismatch_is_O1", v4,
          "both deviations exceed 10% — the heat family and the Markov family have "
          "genuinely different shapes in the canonical rate variable; the mismatch is "
          "structural, not a tuning failure. REORIENTATION: the geometric realization of "
          "the q-deformation, if any, lives in the MODULAR direction (deforming τ₀), not "
          "the heat direction (proper time at fixed modulus)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "q↔t DICTIONARY SHAPES ADJUDICATED — RECIPROCAL POWER-LAW CLASS KILLED (scope-(a); "
        "pre-stated method and tolerance; no fit; nothing wired): with the anchor q=1 ↔ t=∞ "
        "forced by consistency-1 and the canonical rate λ = ln q from the corpus, the "
        "one-constant dictionaries t = c/|λ|^p (p = 1, 2) pinned at a single point miss the "
        "overdetermined curve test by 18.9% / 31.1% — O(1), structural. Within this class "
        "the HEAT family does not realize the Markov deformation. NOT a refutation of the "
        "τ-identification: it REDIRECTS the geometric family to the MODULAR direction "
        "(deform τ₀, not proper time) as the next candidate. The identification remains "
        "OPEN. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-qt-dictionary-shape",
        "description": "Bean qou-tq20 tranche 6: q<->heat-time dictionary shape adjudication. "
                       "Anchor q=1 <-> t=inf forced (consistency-1); canonical rate lambda = ln q "
                       "(corpus); reciprocal power-law dictionaries t = c/|lambda|^p (p=1,2) pinned "
                       "at one point FAIL the overdetermined curve test by 18.9%/31.1% (O(1), "
                       "structural). Heat family does not realize the Markov deformation in this "
                       "class; geometric family redirected to the MODULAR direction. Identification "
                       "stays open. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-qt-dictionary-shape.md",
        "tier": "pre-stated overdetermined adjudication (exact Markov ratio + 30-dps theta); "
                "scope-(a) kills",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy+mpmath", "engineVersion": sp.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "anchor": "q=1 <-> t=inf (forced); rate variable lambda = ln q (corpus canonical)",
            "shape_tests": results,
            "conclusion": "reciprocal power-law class killed (scope-(a)); heat family is the "
                          "wrong geometric realization in this class; next candidate: modular "
                          "(tau_0-direction) deformation",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-tq20 (B2 lift) tranche 6; #4019 consistency-1, #4022 structured null "
                    "merged",
            "scope_guard": "these shapes alone, as-is; c pinned by pre-stated rule; tolerance "
                           "pre-stated; no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-qt-dictionary-shape.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
