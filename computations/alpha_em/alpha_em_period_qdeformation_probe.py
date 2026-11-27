#!/usr/bin/env python3
"""alpha_em_period_qdeformation_probe.py

Bean qou-tq20 (B2 lift), tranche 5: the PERIOD-SIDE q-DEFORMATION — the next
falsifiable comparison after consistency-1 (#4019), using the theta-machinery
of the #3934 front (per-factor 2-D lattice thetas of the isogeny blocks).

SETUP. Consistency-1 matched the endpoint: Markov channel dims 4*(3/4,1/4) =
(3,1) = isotypic dims of Jac(Bring) ~ E_{5 tau0}^3 x E_{tau0}. The
identification predicts the geometric side carries a DEFORMATION of the
(3,1) weights matching the Markov ratio r(q) = y_[2]/y_[1,1] (r(1)=3). The
natural geometric deformation is the HEAT family: per-factor full heat
traces theta_{G(tau)^{-1}}(t), giving

    R_geo(t) = 3 * theta_{G(5 tau0)^{-1}}(t) / theta_{G(tau0)^{-1}}(t).

FORMALIZE-FIRST PRUNING (pre-stated): comparing two monotone one-parameter
families under a FREE reparameterization t(q) is VACUOUS — any two monotone
curves match. The dictionary-independent content is ONLY:
  (i)  endpoint values: R_geo(t->inf) = 3 (factor multiplicities; matches
       r(1) = 3 — this IS consistency-1's anchor) and R_geo(t->0) = 15
       (= 3 * area ratio Im(5 tau0)/Im(tau0) = 3*5, EXACT — canonical via
       the #3934 isogeny-block Grams);
  (ii) whether the categorical parameter q15 solving r(q15) = 15 (the
       image of the geometric t->0 endpoint under ANY monotone dictionary
       anchored at q=1 <-> t=inf) is a DISTINGUISHED constant of the
       framework — candidate list PRE-STATED below, tolerance exact-grade.

CANDIDATES (pre-stated, closed): 1/q0, |nome(tau0)|, |nome(tau0)|^{1/5},
1/sqrt(5), e^{-2 pi/5}, 1/phi (golden), 1/phi^2, 1/5.

RESULT (computed below, asserted): q15 = 0.625562447879731667532550949732...
misses EVERY candidate (nearest: 1/phi at 1.22% relative — a clean miss for
exact quantities). HONEST NULL: the endpoint-to-distinguished-constant
dictionaries are killed at scope-(a); the deformation matching remains
DICTIONARY-GATED — the identification is neither confirmed beyond
consistency-1 nor refuted (the true dictionary, if any, does not send the
t->0 endpoint to a currently-distinguished q). Recorded, not interpreted:
r(1/q0) = 4.0072 (0.18% from 4; NOT in the pre-stated list, so not scored).

Scope guard: scope-(a); no fit (candidate list pre-stated, no post-hoc
additions scored); nothing wired; 1/(8 pi) stays phase-4.
Self-contained (sympy + mpmath + corpus y_lambda_at; theta machinery after
the #3934 front's factorized probe).
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
T0 = mp.mpc(-0.5, mp.mpf("0.186676"))  # Bring modulus (#3934 front)


def gram(tau):
    return [[mp.mpf(1), mp.re(tau)], [mp.re(tau), mp.re(tau) ** 2 + mp.im(tau) ** 2]]


def inv2(B):
    a, b, d = B[0][0], B[0][1], B[1][1]
    det = a * d - b * b
    return [[d / det, -b / det], [-b / det, a / det]]


def theta2(B, t, R=30):
    a, b, d = B[0][0], B[0][1], B[1][1]
    s = mp.mpf(0)
    for i in range(-R, R + 1):
        for j in range(-R, R + 1):
            s += mp.e ** (-mp.pi * t * (a * i * i + 2 * b * i * j + d * j * j))
    return s


def r_geo(t):
    th5 = theta2(inv2(gram(5 * T0)), t)
    th1 = theta2(inv2(gram(T0)), t)
    return 3 * th5 / th1


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # V1: geometric endpoints — exact area ratio + theta-numeric confirmation
    area_ratio = mp.im(5 * T0) / mp.im(T0)  # = 5 exactly
    lo, hi = r_geo(mp.mpf("8")), r_geo(mp.mpf("0.02"))
    grid = [r_geo(mp.mpf(t)) for t in ("0.02", "0.1", "0.5", "1", "2", "8")]
    mono = all(grid[i] > grid[i + 1] for i in range(len(grid) - 1))
    v1 = (abs(area_ratio - 5) < mp.mpf(10) ** -30
          and abs(lo - 3) < mp.mpf(10) ** -6 and abs(hi - 15) < mp.mpf("0.05") and mono)
    check("geometric_heat_family_endpoints", v1,
          f"R_geo(t) = 3·θ_{{G(5τ₀)⁻¹}}/θ_{{G(τ₀)⁻¹}}: t→∞ limit 3 (numeric {mp.nstr(lo, 10)}; "
          f"factor multiplicities = consistency-1 anchor), t→0 limit 15 = 3·(Im 5τ₀/Im τ₀) "
          f"(exact area ratio 5; numeric {mp.nstr(hi, 8)} at t=0.02), monotone on the grid — "
          "the canonical geometric deformation of the (3,1) weights spans exactly [3, 15]")

    # V2: categorical family — corpus-canonical Markov ratio r(q)
    y = y_lambda_at(2)
    y2s, y11s = y[(2,)], y[(1, 1)]
    q = sorted(y2s.free_symbols, key=str)[0]
    r_sym = sp.simplify(y2s / y11s)
    r1 = sp.simplify(r_sym.subs(q, 1))
    rf = sp.lambdify(q, r_sym, "mpmath")
    r_vals = [rf(mp.mpf(x)) for x in ("0.6", "0.7", "0.8", "0.9", "1.0")]
    mono_cat = all(r_vals[i] > r_vals[i + 1] for i in range(len(r_vals) - 1))
    v2 = r1 == 3 and mono_cat
    check("categorical_markov_ratio_family", v2,
          "r(q) = y_[2]/y_[1,1] (corpus canonical): r(1) = 3 exactly (= the shared anchor), "
          "monotone decreasing toward q=1 on [0.6, 1] — the categorical deformation family "
          "covers [3, 15] on an interval [q₁₅, 1]")

    # V3: the dictionary endpoint q15 (image of t->0 under any monotone dictionary)
    f15 = sp.lambdify(q, r_sym - 15, "mpmath")
    q15 = mp.findroot(f15, mp.mpf("0.5"))
    v3 = abs(rf(q15) - 15) < mp.mpf(10) ** -25 and mp.mpf("0.6") < q15 < mp.mpf("0.65")
    check("dictionary_endpoint_q15_computed", v3,
          f"r(q₁₅) = 15 at q₁₅ = {mp.nstr(q15, 25)} (30-dps root of the exact symbolic ratio)")

    # V4: pre-stated distinguished-candidate test (the dictionary-free check)
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — proton default, by name
    Q0_PROTON = Q_MP
    phi = (1 + mp.sqrt(5)) / 2
    cands = {
        "1/q0": 1 / Q0_PROTON,   # proton pin by name (was the RETIRED muon literal; bean qou-4bef)
        "|nome(tau0)|": mp.e ** (-2 * mp.pi * mp.im(T0)),
        "|nome(tau0)|^(1/5)": (mp.e ** (-2 * mp.pi * mp.im(T0))) ** (mp.mpf(1) / 5),
        "1/sqrt(5)": 1 / mp.sqrt(5),
        "e^(-2pi/5)": mp.e ** (-2 * mp.pi / 5),
        "1/phi": 1 / phi,
        "1/phi^2": 1 / phi ** 2,
        "1/5": mp.mpf(1) / 5,
    }
    dists = {k: abs(q15 - v) / v for k, v in cands.items()}   # mpf, never float64 (bean qou-4bef)
    nearest = min(dists, key=dists.get)
    any_match = any(d < 1e-6 for d in dists.values())
    v4 = not any_match  # the pre-stated rule: exact-grade tolerance; a 1e-6 match would flag
    check("distinguished_candidate_test_null", v4,
          f"q₁₅ vs the PRE-STATED candidate list at exact-grade tolerance 1e-6: NO match — "
          f"nearest is {nearest} at {mp.nstr(dists[nearest] * 100, 6)}% relative (a clean miss for exact "
          "quantities). HONEST NULL: endpoint-to-distinguished-constant dictionaries are "
          "killed; the deformation matching stays dictionary-gated. Recorded, not scored "
          f"(post-hoc): r(1/q0) = {mp.nstr(rf(1/Q0_PROTON), 8)}")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "PERIOD-SIDE q-DEFORMATION: STRUCTURED NULL (scope-(a); no fit; nothing wired): the "
        "canonical geometric heat deformation of the (3,1) isotypic weights spans exactly "
        "[3, 15] (endpoints exact: multiplicity 3 at t→∞ = consistency-1's anchor; 3·area-"
        "ratio 15 at t→0, canonical via the #3934 isogeny-block Grams), and the categorical "
        "Markov family covers the same range on [q₁₅, 1] — but the dictionary endpoint "
        "q₁₅ = 0.6255624478… matches NO pre-stated distinguished constant (nearest 1/φ at "
        "1.22%). Formalize-first pruning made explicit: free-reparameterization curve "
        "matching is vacuous; only endpoints + distinguished points are dictionary-free, and "
        "the distinguished-point test returns NULL. The identification survives (nothing "
        "refuted — the true dictionary need not send t→0 to a distinguished q) but gains no "
        "second consistency point; the τ-identification remains OPEN and dictionary-gated. "
        "NO tier change."
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
        "computation": "alpha-em-period-qdeformation",
        "description": "Bean qou-tq20 tranche 5: period-side q-deformation check via the #3934 "
                       "theta machinery. Geometric heat family of the (3,1) isotypic weights spans "
                       "[3,15] exactly (endpoints exact); the categorical Markov ratio covers the "
                       "same range on [q15, 1]; the dictionary endpoint q15 = 0.62556... matches NO "
                       "pre-stated distinguished constant (nearest 1/phi at 1.22%). Structured "
                       "null: endpoint dictionaries killed; identification neither refuted nor "
                       "doubly-confirmed; wall stays open, dictionary-gated. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-period-qdeformation.md",
        "tier": "symbolic-exact (Markov ratio) + 40-dps theta numerics (geometric family); "
                "pre-stated decision rules; structured null",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy+mpmath", "engineVersion": sp.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "geometric_family": "R_geo(t) = 3 theta_{G(5t0)^-1}/theta_{G(t0)^-1}: [15 -> 3], "
                                "monotone; endpoints exact",
            "categorical_family": "r(q) = y_[2]/y_[1,1]: r(1)=3; covers [3,15] on [q15,1]",
            "q15": mp.nstr(q15, 30),
            "candidate_test": {k: mp.nstr(d, 20) for k, d in sorted(dists.items(), key=lambda kv: kv[1])},   # serialised from mpf
            "outcome": "structured null — no distinguished-constant match; dictionary-gated",
            "recorded_not_scored": "r(1/q0) ~ 4.0072",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-tq20 (B2 lift) tranche 5; consistency-1 #4019 merged",
            "theta_source": "per-factor 2-D lattice thetas after the #3934 front "
                            "(bring_genus4_epstein_theta_factorized_probe)",
            "scope_guard": "pre-stated candidates only; no post-hoc scoring; no fit; nothing "
                           "wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-period-qdeformation.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor="proton")
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
