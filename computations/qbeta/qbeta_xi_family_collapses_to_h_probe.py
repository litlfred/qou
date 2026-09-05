#!/usr/bin/env python3
"""RETRACTION: the Xi_k family carries NO structure beyond h. It collapses.

Bean `qou-ximf` proposed Xi_k = (1+Q^k)/(1+Q)^k, Q = q^2, as "the only derived,
parameter-free, n-independent family of bar-even weight functionals" and hence
as the natural home for the convention-D residual `ce` -- which is bar-even and
so untouched by the parity argument that fixes the odd half uniquely.

THAT PROPOSAL IS WITHDRAWN. Measured exactly over Q(q), k = 1..8:

    Xi_k  =  (q^k + q^-k) / [2]_q^k          [2]_q = q + 1/q

so with x = [2]_q and q^k + q^-k = 2*T_k(x/2) (Chebyshev, verified k = 1..6),

    Xi_k  =  2*T_k(x/2) / x^k

is a RATIONAL FUNCTION OF [2]_q ALONE -- and since [2]_q^2 = h^2 + 4 exactly,
a rational function of h^2. Concretely:

    [2]^2 * Xi_2 = h^2 + 2          [2]^2 * Xi_3 = h^2 + 1

The ladder already carries h. So the family supplies NOTHING the ladder did not
already have, and it cannot be the source of `ce`.

WHY THE ORIGINAL OBSERVATION LOOKED LIKE STRUCTURE. Two things misled:

  1. The CYCLOTOMIC numerators (k = 1,2,3,4 -> 1, Phi_8, Phi_12, Phi_16) are
     real, but they are just the factorisation of 1 + q^{2k}; they are a
     property of the writing, not of the content. Registry KC20's
     "the bar-odd carrier is not a root-of-unity object" was correctly noted as
     NOT binding here (KC20 concerns the bar-ODD carrier) -- but the bar-even
     channel turns out to have nothing cyclotomic to say either.
  2. The k=2 member IS the corpus's proved loop-mean identity, which is genuine
     content. But its content is the MARKOV condition `2z - h = [2]_q*Xi_2`,
     i.e. a statement about z -- not about Xi_2, which is just (h^2+2)/[2]_q^2.
     Re-derived here: 2*z_D - h = (h^2+2)/[2]_q exactly.

THIS ALSO EXPLAINS THE EARLIER PRUNE. `qbeta_xi_kcycle_route_prune_probe.py`
found that Xi_3's coefficient came out FREE in an exact solve and read that as
"the k-cycle route does not reach Xi_3". The deeper reason is that there was
never anything at Xi_3 to reach: Xi_3 = (h^2+1)/[2]^2 is a redundant coordinate,
so any basis containing it alongside {1, h^2, [2]^2} is linearly dependent and a
free coefficient is forced. That prune's conclusion stands; its explanation is
superseded by this one.

NET, for the bar-even channel: `ce` is NOT reachable from the Markov weights'
moment structure at all, because that structure is a function of h. A derivation
of `ce` must introduce something genuinely new -- it is not hiding in the
weights. Scope-(a): this excludes the weight-moment family as the source, not
every conceivable derivation.

Exact symbolic over Q(q). NO anchors, NO c_k value, NO fit, NO wiring.
"""
import datetime, hashlib, json, os, subprocess
import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def _sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
    except Exception:
        return None


def main():
    q = sp.symbols("q", positive=True)
    Q, h, br2 = q**2, q - 1/q, q + 1/q
    x = sp.symbols("x")
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    check("xi_k_eq_qk_plus_qnegk_over_bracket2_pow_k__k_1_to_8",
          all(sp.simplify(sp.together((1 + Q**k)/(1 + Q)**k
                                      - (q**k + q**(-k))/br2**k)) == 0
              for k in range(1, 9)))
    check("bracket2_sq_eq_h_sq_plus_4", sp.simplify(br2**2 - (h**2 + 4)) == 0)
    check("xi_k_is_chebyshev_in_bracket2__k_1_to_6",
          all(sp.simplify((q**k + q**(-k))
                          - sp.expand(2*sp.chebyshevt(k, x/2)).subs(x, br2)) == 0
              for k in range(1, 7)))
    check("bracket2_sq_xi2_eq_h_sq_plus_2",
          sp.simplify(br2**2*(1 + Q**2)/(1 + Q)**2 - (h**2 + 2)) == 0)
    check("bracket2_sq_xi3_eq_h_sq_plus_1",
          sp.simplify(br2**2*(1 + Q**3)/(1 + Q)**3 - (h**2 + 1)) == 0)
    zD = q**3/(q**2 + 1)
    check("loopMean_identity_in_h_only",
          sp.simplify((2*zD - h) - (h**2 + 2)/br2) == 0)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "RETRACTION (scope-(a)). Xi_k = (q^k + q^-k)/[2]_q^k = 2*T_k([2]/2)/[2]^k "
        "is a rational function of [2]_q alone, and [2]^2 = h^2 + 4, so the whole "
        "family is a function of h^2 -- which the ladder already carries. The "
        "family is NOT a new source of bar-even structure and cannot supply the "
        "convention-D residual `ce`. The cyclotomic numerators are the "
        "factorisation of 1 + q^{2k}, a property of the writing. qou-ximf's "
        "central proposal is withdrawn; the k-cycle prune's conclusion stands "
        "with a better explanation (Xi_3 = (h^2+1)/[2]^2 is a redundant "
        "coordinate, so a free coefficient was forced). `ce` is not hiding in "
        "the weights."
        if all_passed else
        "INCONCLUSIVE -- an identity assertion failed; re-derive before citing.")

    src = open(__file__, "rb").read()
    w = {"computation": "qbeta-xi-family-collapses-to-h",
         "description": "The Xi_k moment family collapses to a rational function "
                        "of [2]_q (hence of h^2), so it carries no structure "
                        "beyond h. Retracts qou-ximf's central proposal.",
         "engine": "sympy-exact", "markov_convention": "D",
         "assertions": assertions, "verdict": verdict,
         "witness": {"scriptPath": "computations/qbeta/" + os.path.basename(__file__),
                     "scriptHash": hashlib.sha256(src).hexdigest()[:12],
                     "commitSha": _sha(),
                     "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-xi-family-collapses-to-h.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
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
        w.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            w, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(w, f, indent=2); f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
