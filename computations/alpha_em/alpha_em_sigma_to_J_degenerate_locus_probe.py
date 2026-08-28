#!/usr/bin/env python3
"""alpha_em_sigma_to_J_degenerate_locus_probe.py

Brick 3 of the correspondence-statement attack: CONSTRUCTS the sigma -> J map at
the degenerate locus, as far as it can be built without the full tau functor —
and finds the involution ROLE-SWAP that completes the dictionary.

Setting (from bricks 1-2, this PR): the unique tau target is {channel transpose
phi: q -> -q^{-1}  <->  complex conjugation on H^1(Bring)}, with the channels
merging at q = +-i = spec(J) (E4).

FINDINGS (exact, sympy):
  B1. TRIPLE COINCIDENCE on the democratic locus: {q : [2]_q = 0} =
      {q : phi(q) = q} = {q : w+ = w- = 1/2} = {+i, -i}. The transpose-fixed /
      equal-weight points are exactly the quantum-dimension-zero points — the
      channel idempotents e± = (sigma ± q^{∓1})/[2]_q blow up BECAUSE [2]_q -> 0;
      the merge (E4) is the Jones-Wenzl-type degeneration.
  B2. THE SEMISIMPLIFIED BRAIDING IS A SQUARE ROOT OF -1: at q = +-i the Hecke
      relation is (sigma -+ i)^2 = 0; mod the nilradical, sigma_ss = +-i and
      sigma_ss^2 = -1 — TYPE-CORRECT with the complex structure J (J^2 = -1).
      (Equivalently: sigma^2 = 2i*sigma + 1 with sigma = i gives -1.)
  B3. INVOLUTION ROLE-SWAP on the degenerate pair: the transpose phi FIXES each
      point (phi(+-i) = +-i) while the bar involution EXCHANGES them
      (bar(+-i) = -+i). So on the degenerate stratum the residual doubling is
      the POINT pair {q=i, q=-i}, and there BAR — not transpose — acts as the
      conjugation. The dihedral pair (bar, transpose) trades roles between the
      generic stratum (channel pair, swapped by transpose) and the degenerate
      stratum (point pair, swapped by bar).
  B4. THE CONSTRUCTED MAP IS EQUIVARIANT: the assignment
          q = +i |-> sigma_ss = +i  ( ~ J on H^{1,0} ),
          q = -i |-> sigma_ss = -i  ( ~ J on H^{0,1} )
      intertwines bar on the parameter with conjugation on spec(J):
      sigma_ss(bar(q)) = conj(sigma_ss(q)) — exact. This is the sigma -> J map
      at the degenerate locus: type-correct (B2) and involution-equivariant (B4).

WHAT REMAINS (the wall, unchanged but now maximally localized): promote this
degenerate-locus map to the tau functor — i.e., show tau carries the braiding's
degenerate pair to the ACTUAL complex structure of the Bring surface. Since J on
a surface IS the conformal structure, and the conformal structure defines the
Laplacian and hence the heat-kernel unit a0 = 1/(4pi), this is exactly the
missing Clause-A normalization: sigma -> J would tie the loop tower to the very
structure that defines a0. Named as the route; NOT derived here.

Honest caveats: [2]_q = 0 means the quantum dimension of A VANISHES at the
democratic points (outside the unitary regime; the semisimplification is the
quotient by the nilradical); and B1-B4 are type-correctness + equivariance of a
constructed map, not the functorial derivation.

Scope guard: derives NO clause; no fit; nothing wired; 1/(8pi) stays phase-4.
Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q, s = sp.symbols('q sigma')

    # B1: triple coincidence — [2]_q=0, transpose-fixed, equal-weight all = {±i}
    dim0 = set(sp.solve(sp.Eq(q + 1 / q, 0), q))
    tfix = set(sp.solve(sp.Eq(q, -1 / q), q))
    wequal = set(sp.solve(sp.Eq(q ** 2 / (q ** 2 - 1), sp.Rational(1, 2)), q))
    b1 = dim0 == tfix == wequal == {sp.I, -sp.I}
    check("triple_coincidence_dim0_transposefixed_equalweight", b1,
          f"{{[2]_q=0}} = {sorted(map(str,dim0))} = {{phi-fixed}} = {{w+=w-=1/2}} — the "
          "democratic points are exactly the quantum-dimension-zero points; the channel "
          "idempotents blow up as [2]_q->0 and the merge (E4) is the Jones-Wenzl-type "
          "degeneration")

    # B2: semisimplified braiding squares to -1 (type-correct with J)
    # at q=i: relation (s-i)^2; mod nilradical (s-i): s ≡ i, s^2 ≡ -1
    s2_mod = sp.rem(s ** 2, s - sp.I, s)          # evaluates s^2 at s=i
    s2_mod_m = sp.rem(s ** 2, s + sp.I, s)
    hecke_id = sp.simplify((2 * sp.I * sp.I + 1) - (-1)) == 0   # sigma^2=2i sigma+1 at sigma=i
    b2 = sp.simplify(s2_mod + 1) == 0 and sp.simplify(s2_mod_m + 1) == 0 and hecke_id
    check("semisimplified_braiding_squares_to_minus1", b2,
          "mod the nilradical at q=+-i: sigma_ss = +-i with sigma_ss^2 = -1 (exact; also "
          "directly from the Hecke relation sigma^2 = 2i*sigma + 1 at sigma=i) — "
          "TYPE-CORRECT with the complex structure J^2 = -1")

    # B3: role-swap — transpose fixes each degenerate point, bar exchanges them
    phi_i = sp.simplify(-1 / sp.I)
    phi_mi = sp.simplify(-1 / (-sp.I))
    bar_i = sp.simplify(1 / sp.I)
    bar_mi = sp.simplify(1 / (-sp.I))
    b3 = phi_i == sp.I and phi_mi == -sp.I and bar_i == -sp.I and bar_mi == sp.I
    check("involution_role_swap_on_degenerate_pair", b3,
          "phi(+-i) = +-i (transpose FIXES each degenerate point) while bar(+-i) = -+i "
          "(bar EXCHANGES them) — on the degenerate stratum the residual doubling is the "
          "POINT pair {q=i,q=-i} and BAR acts as the conjugation; the dihedral pair "
          "(bar, transpose) trades roles between generic (channel pair / transpose-swapped) "
          "and degenerate (point pair / bar-swapped) strata")

    # B4: the constructed map q=±i -> sigma_ss=±i intertwines bar with conjugation
    def sigma_ss(qval):
        return qval          # at the degenerate points sigma_ss = q (both = ±i)
    b4 = all(sp.simplify(sigma_ss(sp.simplify(1 / qv)) - sp.conjugate(sigma_ss(qv))) == 0
             for qv in (sp.I, -sp.I))
    check("sigma_to_J_map_equivariant", b4,
          "the constructed map {q=+i |-> sigma_ss=+i (~J on H^{1,0}), q=-i |-> sigma_ss=-i "
          "(~J on H^{0,1})} satisfies sigma_ss(bar(q)) = conj(sigma_ss(q)) EXACTLY — "
          "type-correct (B2) and involution-equivariant: the sigma->J identification is "
          "consistent at the degenerate locus; promoting it to the tau functor (J = the "
          "conformal structure that defines the Laplacian and hence a0) is the remaining "
          "Clause-A wall, now maximally localized")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "SIGMA->J CONSTRUCTED AT THE DEGENERATE LOCUS (scope-(a); derives no clause; no fit; "
        "nothing wired): triple coincidence — the democratic/transpose-fixed/equal-weight "
        "locus IS the quantum-dimension-zero locus {q=+-i} ([2]_q=0; the E4 merge is the "
        "Jones-Wenzl-type degeneration). There the semisimplified braiding sigma_ss = +-i "
        "squares to -1 (type-correct with J), the involutions ROLE-SWAP (transpose fixes the "
        "two points, bar exchanges them — bar is the conjugation on the degenerate stratum), "
        "and the assignment q=+-i |-> sigma_ss=+-i ~ J|_{H^{1,0}/H^{0,1}} is bar/conjugation-"
        "equivariant EXACTLY. Remaining wall (unchanged, maximally localized): promote this "
        "map to the tau functor — sigma -> J = the conformal structure defining the Laplacian "
        "and a0=1/(4pi), i.e. exactly the Clause-A normalization. Honest caveats: [2]_q=0 "
        "puts the democratic points outside the unitary regime; B1-B4 are type-correctness + "
        "equivariance, not the functorial derivation. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-sigma-to-J-degenerate-locus",
        "description": "Constructs the sigma->J map at the degenerate locus: triple coincidence "
                       "(democratic = transpose-fixed = [2]_q=0 locus = {±i}); semisimplified braiding "
                       "sigma_ss=±i squares to -1 (type-correct with J); involution role-swap (transpose "
                       "fixes the degenerate points, bar exchanges them = conjugation on that stratum); "
                       "the map q=±i -> sigma_ss=±i ~ J|H^{1,0}/H^{0,1} is bar/conjugation-equivariant "
                       "exactly. Remaining: promote to the tau functor (J = conformal structure => a0) — "
                       "the Clause-A wall, maximally localized. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-conjugation-doubling-dictionary.md",
        "tier": "symbolic-exact (sympy; locus solves, quotient-by-nilradical, involution equivariance)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "triple_coincidence": "{[2]_q=0} = {phi-fixed} = {w+=w-=1/2} = {+i,-i}",
            "sigma_ss": "±i at q=±i; sigma_ss^2 = -1 (J-type)",
            "role_swap": "transpose fixes the degenerate points; bar exchanges them (= conjugation there)",
            "constructed_map": "q=±i -> sigma_ss=±i ~ J on H^{1,0}/H^{0,1}; bar/conj-equivariant exact",
            "remaining_wall": "promote to tau: sigma->J = conformal structure => Laplacian => a0 "
                              "(Clause A), maximally localized",
            "verdict": verdict,
        },
        "context": {
            "builds_on": "bricks 1-2 (this PR): corrected dictionary + unique tau target + E4 spec(J) merge",
            "caveats": "[2]_q=0 at the democratic points (quantum dimension of A vanishes — outside the "
                       "unitary regime; semisimplification = quotient by nilradical); type-correctness + "
                       "equivariance, not the functorial derivation",
            "scope_guard": "derives NO clause; no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-sigma-to-J-degenerate-locus.witness.json")
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
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
