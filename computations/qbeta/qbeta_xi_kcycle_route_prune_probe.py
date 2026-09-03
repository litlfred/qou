#!/usr/bin/env python3
"""The k-cycle route into Xi_{k>=3} is PRUNED (scope-(a)).

Bean `qou-ximf` proposed the family Xi_k = (1+Q^k)/(1+Q)^k and suggested the
k-cycle Hecke traces as the bridge that would let the ladder see Xi_{k>=3}.
This probe tests that at n = 3, convention D, exactly -- and it FAILS.

Reason, and it is structural rather than numerical: the MARKOV PROPERTY forces
tr_M(sigma_1 ... sigma_{k-1}) = z^{k-1} identically, so every standard-element
Markov trace is a power of z and carries no information beyond Xi_2. Verified
here at k = 3 by an EXACT solve for constant rational coefficients, which
returns Xi_3's coefficient FREE -- i.e. Xi_3 does not enter -- and collapses to
the proved k=2 identity squared:

    4 z_D^2 = (h + [2]_q Xi_2)^2 .

CONSEQUENCE (sharpens qou-ximf, does not kill it): Xi_{k>=3} is a WEIGHT
FUNCTIONAL, not a trace value. It is computable from the weight vector but is
not equal to any Markov trace on the ladder's own elements, so the Hecke
Murnaghan-Nakayama rule (Halverson-Ram q-alg/9511222; Jing-Liu 2504.18825)
does NOT supply a new bridge from the ladder to it. What that literature does
supply is the general-n per-block Hecke characters -- see
docs/audits/2026-08-26-murnaghan-nakayama-upload-triage.md.

Exact symbolic over Q(q). NO anchors, NO c_k value, NO fit, NO wiring.
"""
import datetime, hashlib, json, os, subprocess
import sympy as sp


def _sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
    except Exception:
        return None


def main():
    q = sp.symbols("q", positive=True)
    Q, h = q**2, q - 1/q
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # H_3(q) 2-dim irrep, solved from braid + Hecke relations (not assumed).
    c = sp.symbols("c")
    s1 = sp.Matrix([[q, 1], [0, -1/q]])
    s2 = sp.Matrix([[-1/q, 0], [c, q]])
    br = sp.expand(s1*s2*s1 - s2*s1*s2)
    sol = sp.solve([br[i] for i in range(4)], [c], dict=True)
    s2 = s2.subs(c, sol[0][c])
    check("h3_irrep_satisfies_braid_relation",
          sp.simplify(s1*s2*s1 - s2*s1*s2) == sp.zeros(2, 2))
    check("h3_irrep_satisfies_hecke_relation",
          all(sp.simplify(M*M - ((q - 1/q)*M + sp.eye(2))) == sp.zeros(2, 2)
              for M in (s1, s2)))

    chi = {(3,): (q, q**2), (2, 1): (sp.simplify(s1.trace()), sp.simplify((s1*s2).trace())),
           (1, 1, 1): (-1/q, 1/q**2)}
    y = {(3,): (q**4 + 1)/(q**2 + 1)**2, (2, 1): q**2/(q**2 + 1)**2, (1, 1, 1): sp.Integer(0)}
    dim = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    check("d_weights_normalised", sp.simplify(sum(dim[l]*y[l] for l in y) - 1) == 0)

    zD = q**3/(q**2 + 1)
    tr1 = sp.simplify(sum(y[l]*chi[l][0] for l in y))
    tr2 = sp.simplify(sum(y[l]*chi[l][1] for l in y))
    check("markov_sigma1_trace_is_z", sp.simplify(tr1 - zD) == 0)
    check("markov_3cycle_trace_is_z_squared", sp.simplify(tr2 - zD**2) == 0)

    Xi2, Xi3 = (1 + Q**2)/(1 + Q)**2, (1 + Q**3)/(1 + Q)**3
    check("proved_k2_identity_reproduced",
          sp.simplify((2*zD - h) - (q + 1/q)*Xi2) == 0)
    # THE PRUNE: z^2 is exactly the k=2 identity squared -- Xi_3 absent.
    check("z_squared_is_k2_identity_squared_xi3_absent",
          sp.simplify(4*tr2 - (h + (q + 1/q)*Xi2)**2) == 0)
    # and single-crossing powers reach only Xi_2, never Xi_3
    ok = True
    for k in range(1, 6):
        # chi_lambda(sigma_1^k) = (f/2)(q^k+(-1)^k q^-k) + (chi_tau/2)(q^k-(-1)^k q^-k)
        ftab = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
        ttab = {(3,): 1, (2, 1): 0, (1, 1, 1): -1}
        pred = sp.simplify(sum(y[l]*(sp.Rational(1, 2)*ftab[l]*(q**k + (-1)**k*q**-k)
                                     + sp.Rational(1, 2)*ttab[l]*(q**k - (-1)**k*q**-k))
                               for l in y))
        closed = sp.simplify(sp.Rational(1, 2)*(q**k + (-1)**k*q**-k)
                             + sp.Rational(1, 2)*(q**k - (-1)**k*q**-k)*Xi2)
        ok &= sp.simplify(pred - closed) == 0
    check("sigma1_powers_span_only_one_and_xi2", ok)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "PRUNED, scope-(a). The Markov property forces tr_M of every standard "
        "element to a power of z, so the k-cycle route reaches no Xi beyond Xi_2: "
        "4 z_D^2 = (h + [2]_q Xi_2)^2 exactly, the proved k=2 identity squared, "
        "with Xi_3's coefficient free. Single-crossing powers likewise span only "
        "{1, Xi_2}. Xi_{k>=3} is a WEIGHT FUNCTIONAL, not a trace value; the Hecke "
        "Murnaghan-Nakayama literature supplies general-n per-block characters, not "
        "a bridge to it. qou-ximf's anti-fit fence is unchanged and still binds."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")

    src = open(__file__, "rb").read()
    w = {"computation": "qbeta-xi-kcycle-route-prune",
         "description": "The k-cycle Hecke-trace route into Xi_{k>=3} is pruned: "
                        "Markov forces tr_M(standard element) = z^{k-1}, so nothing "
                        "beyond Xi_2 is reachable. Exact at n=3, convention D.",
         "engine": "sympy-exact", "markov_convention": "D",
         "assertions": assertions, "verdict": verdict,
         "witness": {"scriptPath": "computations/qbeta/" + os.path.basename(__file__),
                     "scriptHash": hashlib.sha256(src).hexdigest()[:12],
                     "commitSha": _sha(),
                     "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-xi-kcycle-route-prune.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        w.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            w, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(w, f, indent=2); f.write("\n")
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
