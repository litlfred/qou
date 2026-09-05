#!/usr/bin/env python3
"""
B3-U (bean z61d) -- u-side transfer: does the fibre parity descend to the c_k?

Runs the three gates pre-stated in the merged scope doc
docs/scope/2026-07-07-z-ck-fmap-b3-uside-transfer-scope.md §3
(committed BEFORE this run via PR #3455). Exact symbolic; NO anchors, NO c_k
value, NO fit, NO wiring.

Setup: u = b*hbar_q^2, hbar_q = 1 - 1/q, so bar(u) = q^2 * u
(ZBarParity.hbar_sq_bar_even_twist). The observable ladder is g(u) = sum c_k u^k;
the c_k are its coefficients via the Habiro (u;u)_m -> u^k change of basis.

  B3-U1  basis image: is P_m(bar(u))/P_m(u) = P_m(q^2 u)/P_m(u) a Laurent
         monomial in (q,u)?  (clean twist analogue of KC16)  KILL if not.
  B3-U2  per-rung twist: overall-F bar-even (KC7) under (q->1/q, u->q^2 u)
         forces c_k(1/q) = q^{-2k} c_k(q). Test against the derived c_2 = -1.
  B3-U3  D(q) placement: u ~ (q-1)^2 is EVEN order in (q-1); a bar-odd carrier
         (D(q), odd order at q=1) cannot be a real power series in u.

All three failing the "clean descent" reading is the expected, honest outcome:
it prunes the naive Habiro-basis transfer and localizes the odd channel to the
archimedean evaluation map (owner 2026-06-16: c_k(q) are fibre q-functions
EVALUATED by the Markov pairing at Vol=1). Scope-(a): the naive re-expansion is
excluded as the descent mechanism; the ingredients (KC15/KC16) are not excluded.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def _repo_head_sha():
    """Repo HEAD at emission time. Raises rather than returning None so a
    witness is never written with missing provenance (I14 PROV_MISSING)."""
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
    ).strip()
    if not sha:
        raise RuntimeError("empty commitSha — refusing to emit witness without provenance")
    return sha


def _is_monomial(expr):
    expr = sp.powsimp(sp.cancel(sp.together(expr)))
    num, den = sp.fraction(sp.together(expr))
    return (len(sp.Add.make_args(sp.expand(num))) == 1
            and len(sp.Add.make_args(sp.expand(den))) == 1)


def _order_at_1(expr, q, maxord=8):
    t = sp.symbols("t")
    g = sp.expand(sp.series(expr.subs(q, 1 + t), t, 0, maxord).removeO())
    for n in range(maxord):
        if sp.simplify(g.coeff(t, n)) != 0:
            return n
    return maxord


def main():
    q, u, b = sp.symbols("q u b", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # sanity: bar(u) = q^2 u
    u_of_q = b * (1 - 1 / q) ** 2
    bar_u_over_u = sp.simplify(u_of_q.subs(q, 1 / q) / u_of_q)
    check("sanity_bar_u_equals_q2_u", sp.simplify(bar_u_over_u - q**2) == 0)

    def P(m, arg):
        r = sp.Integer(1)
        for j in range(1, m + 1):
            r *= (1 - arg**j)
        return r

    # --- B3-U1: basis image is a clean monomial twist?  (expect NO) ---
    u1_clean = all(_is_monomial(P(m, q**2 * u) / P(m, u)) for m in range(1, 5))
    # gate is stated as "clean descent"; the honest finding is the NEGATION.
    check("B3U1_basis_image_NOT_clean_monomial_twist", not u1_clean)

    # --- B3-U2: per-rung twist c_k(1/q) = q^{-2k} c_k(q) vs derived c_2 = -1 ---
    c2 = sp.Integer(-1)
    u2_holds = sp.simplify(c2.subs(q, 1 / q) - q ** (-2 * 2) * c2) == 0
    check("B3U2_per_rung_twist_FAILS_on_derived_c2", not u2_holds)

    # --- B3-U3: u even-order in (q-1); bar-odd carrier odd-order -> mismatch ---
    ord_u = _order_at_1(u_of_q, q)            # expect 2 (even)
    # kappa_(2,1) is the corpus's exactly-bar-odd carrier; its order at q=1:
    kappa = (q - 1) ** 3 * (q + 1) / q**2
    ord_kappa = _order_at_1(kappa, q)         # expect 3 (odd)
    u3_mismatch = (ord_u % 2 == 0) and (ord_kappa % 2 == 1)
    check("B3U3_u_even_order_vs_bar_odd_odd_order_mismatch", u3_mismatch)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "OBSTRUCTION (scope-(a)): the fibre parity structure (KC15 D(q), KC16 "
        "index-alternating basis) does NOT descend to the observable c_k via a naive "
        "re-expansion in u = b*hbar_q^2. (U1) The (u;u)_m Habiro basis carries no clean "
        "monomial bar-twist -- failing already at m=1 (ratio (q^2 u-1)/(u-1)), verified "
        "m=1..4 -- because bar(u)=q^2 u is a SCALING, not the KC16 inversion. (U2) "
        "The per-rung twist q^{-2k} that overall-F bar-evenness would impose is "
        "contradicted by the derived c_2 = -1 (a bar-trivial constant). (U3) u vanishes "
        "to EVEN order 2 in (q-1) while a bar-odd carrier vanishes to ODD order, so "
        "bar-odd fibre content cannot map to real u-power coefficients. Net: the odd "
        "channel enters through the ARCHIMEDEAN EVALUATION map (tau-functor / Markov "
        "pairing at Vol=1; owner 2026-06-16), NOT a fibre basis change. The naive "
        "re-expansion route is excluded as the descent mechanism; KC15/KC16 ingredients "
        "are NOT excluded. NO c_k value; nothing wired."
        if all_passed else
        "INCONCLUSIVE -- a gate did not behave as pre-stated; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-b3u-uside-transfer",
        "description": "B3-U (bean z61d): u-side transfer gates U1/U2/U3 pre-stated in "
                       "scope doc §3 (merged PR #3455). Tests whether fibre parity "
                       "(KC15/KC16) descends to the observable c_k via re-expansion in "
                       "u = b*hbar_q^2. Exact symbolic; no anchors.",
        "audit_only": True,
        "tier": "structural-exact (symbolic; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "bar_u": "q^2 * u",
            "u1_basis_image_monomial": u1_clean,
            "u2_per_rung_twist_holds_on_c2": u2_holds,
            "u_order_at_1": ord_u,
            "kappa_order_at_1": ord_kappa,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone, bean z61d (I-B step B3-U)",
            "scope_prestatement": "docs/scope/2026-07-07-z-ck-fmap-b3-uside-transfer-scope.md §3 (merged PR #3455)",
            "lean_u_twist": "QOU.QBeta.uPow_bar_twist / hbar_sq_bar_even_twist (ZBarParity)",
            "archimedean_eval_note": "owner 2026-06-16: c_k(q) fibre functions evaluated by Markov pairing at Vol=1",
            "registry": "docs/coordination/ck-dk-canonical-registry.md §9",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "qbeta-b3u-uside-transfer.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("=== B3-U : u-side transfer gates ===")
    print("bar(u) = q^2 u ;  u order@1 =", ord_u, " kappa order@1 =", ord_kappa)
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
