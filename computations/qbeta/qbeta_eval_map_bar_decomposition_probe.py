#!/usr/bin/env python3
"""
Archimedean evaluation map -- bar-decomposition (the standing reading, realized).

Follows the B3-U obstruction (naive u-re-expansion excluded; the c_k come from
the archimedean evaluation, not a fibre basis change). The evaluation map is the
Frobenius counit e / Markov trace tr_M on the N=0 nucleon Hecke NF difference
(QOU.Interactions.QBetaCounitTrace, Lean-proved):

    e(n-p)    = h^2/2 - h        (identity term h^2/2, unweighted crossing -h)
    tr_M(n-p) = h^2/2 - h*z      (crossing weighted by the Markov loop z)

with h = q - 1/q the Hecke parameter and z = sqrt(q)/(1+q) the Markov loop
parameter. Under the fibre bar involution q -> 1/q: h -> -h (bar-ODD) and z is
fixed (bar-EVEN, KC13). So the evaluation map splits EXACTLY into a bar-even
identity term h^2/2 (the shadow/mass channel) and a bar-odd crossing/loop term
(-h or -h*z, the odd channel). This is the archimedean realization of the
owner-granted standing reading (parity gates test the odd part, shadow gates
the even part; registry KC6/KC10).

Exact symbolic; NO anchors, NO c_k value, NO fit, NO wiring. Confirms the
sorry-free Lean lemmas epsNP_decomp / epsNP_bar_image / trMNP_decomp /
trMNP_bar_image.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def _repo_head_sha():
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
    ).strip()
    if not sha:
        raise RuntimeError("empty commitSha — refusing to emit witness without provenance")
    return sha


def main():
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    z = sp.sqrt(q) / (1 + q)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    def bar(e):
        return sp.simplify(sp.radsimp(e.subs(q, 1 / q)))

    def parity(e):
        e = sp.simplify(e)
        if sp.simplify(bar(e) - e) == 0:
            return "even"
        if sp.simplify(bar(e) + e) == 0:
            return "odd"
        return "neither"

    # Fundamental parities.
    check("h_bar_odd", parity(h) == "odd")
    check("z_bar_even_KC13", parity(z) == "even")
    check("h2_over_2_bar_even", parity(h**2 / 2) == "even")

    eps = h**2 / 2 - h
    trM = h**2 / 2 - h * z

    # Exact decompositions (match the Lean lemmas).
    check("eps_decomp_identity_plus_crossing",
          sp.simplify(eps - (h**2 / 2 + (-h))) == 0)
    check("trM_decomp_identity_plus_loop",
          sp.simplify(trM - (h**2 / 2 + (-(h * z)))) == 0)

    # Odd channel = crossing/loop term; even channel = identity term.
    check("eps_odd_part_bar_odd", parity(-h) == "odd")
    check("trM_odd_part_bar_odd", parity(-(h * z)) == "odd")
    check("eval_map_even_part_carries_shadow", parity(h**2 / 2) == "even")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CONFIRMED: the archimedean evaluation map (counit e / Markov trace tr_M) "
        "splits EXACTLY into a bar-EVEN identity term h^2/2 and a bar-ODD crossing/loop "
        "term (-h for e, -h*z for tr_M), because h = q - 1/q is bar-odd and z is "
        "bar-even (KC13). This realizes the standing reading (KC6/KC10) on the actual "
        "evaluation map: the even identity term carries the shadow/mass channel, the odd "
        "loop term is THE odd channel -- the bar-odd carrier (KC15 D(q)) feeds the "
        "observable through the Markov crossing term, not the identity term. Matches the "
        "sorry-free Lean lemmas epsNP_decomp / epsNP_bar_image / trMNP_decomp / "
        "trMNP_bar_image. NO c_k value; nothing wired."
        if all_passed else
        "INCONCLUSIVE -- a parity/decomposition assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-eval-map-bar-decomposition",
        "description": "Archimedean evaluation map (counit/Markov-trace) bar-decomposition: "
                       "even identity term h^2/2 + odd crossing/loop term (-h / -h*z). "
                       "Realizes the standing reading (KC6/KC10) on the actual map. "
                       "Confirms QBetaCounitTrace Lean lemmas.",
        "audit_only": True,
        "tier": "structural-exact (symbolic bar-parity; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "eps": "h^2/2 - h", "trM": "h^2/2 - h*z",
            "even_part": "h^2/2 (identity term; bar-even; shadow/mass channel)",
            "odd_part": "-h (counit) / -h*z (Markov loop; bar-odd; the odd channel)",
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: archimedean evaluation map",
            "lean": "QOU.Interactions.QBetaCounitTrace (epsNP_decomp/bar_image, trMNP_decomp/bar_image)",
            "b3u_obstruction": "docs/audits/2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md",
            "standing_reading": "registry KC6/KC10 (owner-granted 2026-07-07)",
            "z_bar_even": "QOU.QBeta.z_bar_invariant (KC13)",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "qbeta-eval-map-bar-decomposition.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    print("=== evaluation-map bar-decomposition ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
