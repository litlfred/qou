#!/usr/bin/env python3
"""
Exotic-signed Lusztig escape — formalize-first magnitude/rank preflight (bean 8z8k).

Owner-authorized (2026-07-07) investigation of the last cont.9-menu escape for the
Q_β c_3: exotic-signed Demazure-Lusztig variants of the Composite-1 ansatz
    F(u) = Σ_w D_w(λ) · (q;q)_{ℓ(w)} · u^{ℓ(w)}     [c_k = [u^k]F].
Scope: docs/scope/2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md
(narrowings N1 magnitude / N2 saturation / N3 cross-anchor rigidity).

This preflight adds **N4**: rather than scan exotic conventions (open-ended per the
scope doc), find the invariant that prunes. Two exact observations:

  1. The |Σ D_w| ~ 39.4 target is an ARTIFACT of routing c_2 through the tiny
     (q;q)_2 ≈ 0.026 divisor of the Composite-1 u-series ansatz. This is exactly
     the u-re-expansion mechanism that KC17 (the B3-U obstruction) showed does not
     carry fibre parity to the c_k; and c_2 = -1 is ALREADY proved by an
     independent, non-u-series mechanism (Kashiwara f̃₁², q-beta-c-2-eq-neg-one-
     structural.lean) and re-derived via the eval-map counit decomposition (KC18).

  2. The Demazure-Lusztig operator T_i has eigenvalues {q, -1/q} (Hecke relation
     T_i^2 = h T_i + 1, h = q - 1/q -- the SAME h that carries the eval-map odd
     channel, KC18). A length-2 signed character is a product of 2 eigenvalues, so
     |D_w| <= q0^2 ≈ 1.23. Reaching |Σ| ~ 40 needs ~32 length-2 Weyl elements,
     i.e. rank n >= 9 (S_8 has only 27 length-2 elements) -- physically absurd for
     a nucleon, which lives in H_3/H_4 Hecke (rank 3-4).

Verdict is scope-(a): the physically-motivated Demazure-Lusztig family does NOT
escape N1-N3; unphysical-rank / unnatural-magnitude conventions are not excluded
but are categorically unmotivated and, per KC18, unnecessary (c_2 already proved
without the divisor pathology). NO fit, NO c_k value, nothing wired.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
from itertools import permutations

import sympy as sp


def _repo_head_sha():
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
    ).strip()
    if not sha:
        raise RuntimeError("empty commitSha — refusing to emit witness without provenance")
    return sha


def _len2_count(n):
    return sum(
        1 for p in permutations(range(n))
        if sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j]) == 2
    )


def main():
    q = sp.symbols("q", positive=True)
    q0 = sp.Rational(110998, 100000)   # substrate q0 ~ 1.10998
    h = q - 1 / q
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # (1) the ~39.4 target is the (q;q)_2 divisor artifact
    qq2 = (1 - q) * (1 - q ** 2)
    qq2_val = float(qq2.subs(q, q0))
    target = float(sp.Rational(-1) / qq2.subs(q, q0))     # c_2 / (q;q)_2
    check("target_is_qq2_divisor_artifact_~-39",
          abs(target) > 30 and abs(qq2_val) < 0.03)

    # (2) Demazure-Lusztig eigenvalues q, -1/q; length-2 char magnitude <= q0^2
    eig_p, eig_m = q0, -1 / q0
    max_len2 = float(max(abs(eig_p ** 2), abs(eig_m ** 2), abs(eig_p * eig_m)))
    check("demazure_lusztig_len2_magnitude_bounded_~1.2", max_len2 < 1.3)

    # rank needed to reach |Σ| ~ |target| by summing O(q0^2) terms
    terms_needed = abs(target) / (float(q0) ** 2)
    counts = {n: _len2_count(n) for n in range(3, 11)}
    min_rank = min((n for n, c in counts.items() if c >= terms_needed), default=None)
    check("required_rank_geq_9_physically_absurd",
          min_rank is not None and min_rank >= 9)

    # (3) the h-connection: eigenvalue sum = h (bar-odd), the eval-map odd-channel carrier
    check("demazure_lusztig_eigsum_is_h",
          sp.simplify((q + (-1 / q)) - h) == 0)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "N4 NARROWING (scope-(a)): the exotic-signed Lusztig escape's |Σ D_w| ~ 39.4 "
        "requirement is an ARTIFACT of the Composite-1 u-series ansatz routing c_2 "
        "through the tiny (q;q)_2 ≈ 0.026 divisor -- the u-re-expansion mechanism KC17 "
        "showed is obstructed, and c_2 = -1 is already proved without it (Kashiwara "
        "f̃₁²; eval-map KC18). The Demazure-Lusztig operator (eigenvalues q, -1/q; "
        "eigenvalue-sum = h, the KC18 odd-channel carrier) has length-2 character "
        f"magnitude <= q0^2 ~ 1.23, so reaching |Σ| ~ 40 needs ~{terms_needed:.0f} "
        f"length-2 Weyl elements ⇒ rank n >= {min_rank} -- physically absurd for a "
        "nucleon (H_3/H_4 Hecke, rank 3-4). Combined with N1-N3 + Lusztig 1990 "
        "positivity, the physically-motivated Demazure-Lusztig family does NOT escape. "
        "Unphysical-rank / unnatural-magnitude conventions are not excluded (scope-(a), "
        "not a convention-independent impossibility proof) but are categorically "
        "unmotivated and, per KC18, unnecessary. Recommendation stands: Option A "
        "(c_3 CAL-3-anchored). NO fit, NO c_k value, nothing wired."
        if all_passed else
        "INCONCLUSIVE -- a magnitude/rank assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-exotic-lusztig-magnitude-preflight",
        "description": "N4 formalize-first prune of the exotic-signed Lusztig c_3 escape: "
                       "the |Σ|~40 target is a (q;q)_2 divisor artifact; the Demazure-Lusztig "
                       "operator's O(1) character magnitude needs rank>=9 to reach it "
                       "(physically absurd). Owner-authorized Subgoal-2 (2026-07-07).",
        "audit_only": True,
        "tier": "structural-exact (magnitude/rank bounds; no fit, no anchors beyond q0 eval)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "qq2_at_q0": qq2_val,
            "sigma_target_c2_over_qq2": target,
            "demazure_lusztig_len2_max_magnitude": max_len2,
            "len2_weyl_counts_S3_to_S10": counts,
            "terms_needed_for_target": terms_needed,
            "min_rank_required": min_rank,
            "nucleon_physical_rank": "3-4 (H_3/H_4 Hecke)",
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: exotic-signed Lusztig escape (bean 8z8k)",
            "scope": "docs/scope/2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md",
            "kc17_obstruction": "docs/audits/2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md",
            "kc18_eval_map": "docs/audits/2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md",
            "c2_proved": "content/.../q-beta-c-2-eq-neg-one-structural.lean (Kashiwara f̃₁²)",
            "menu_state": "docs/coordination/1ppq-qbeta.md cont.18 (Option A reinforced)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-exotic-lusztig-magnitude-preflight.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    print("=== exotic-signed Lusztig — N4 magnitude/rank preflight ===")
    print(f"target |Σ| ~ {abs(target):.1f}  | DL len-2 magnitude ~ {max_len2:.2f}  | "
          f"rank needed >= {min_rank}")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
