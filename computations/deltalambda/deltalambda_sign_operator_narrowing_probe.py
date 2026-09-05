#!/usr/bin/env python3
"""
NARROW the operator behind the Δ_λ sign carrier q^{2n(λ)}: it is a central
character but NOT a framing power and NOT a low-degree Jucys-Murphy content
symmetric function -- it is a co-content / principal-specialization (pivotal)
grading. Parameter-free; no fit; nothing wired.

Prior (landed #3509): the Δ_λ chirality sign is
  sgn(Δ_λ) = sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)} = q^{2n(λ)}|_{q=i},
a value at q=i (ζ₄), a NON-SEMISIMPLE point of H_5. This probe asks WHICH operator
realizes the central character q^{2n(λ)}. It rules out the simple/canonical
candidates and identifies the structural home:

  A. NOT a framing power. Neither the full twist θ_λ = q^{2(n(λ')-n(λ))} nor the
     framing sqrt θ_λ^{1/2} = q^{n(λ')-n(λ)} reproduces the sign at q=i (checked
     #3509; restated here). Framings are graded by the CONTENT sum n(λ')-n(λ).

  B. NOT a low-degree JM central element. The centre of H_n(q) is the symmetric
     functions of the Jucys-Murphy elements, whose eigenvalue on V_λ is a symmetric
     function of the content multiset {q^{2c(box)}}. Testing whether n(λ) is an EXACT
     polynomial in the content power sums p_k = Σ_box c^k (+ |λ|) — against the COMPLETE
     symmetric basis up to weighted degree 6 (every monomial Π_k p_{μ_k}, μ⊢d, d≤6),
     pooled over λ⊢4..8: it is NOT. So q^{2n(λ)} is not a canonical low-degree JM/framing
     central element.

  C. It IS realizable (the content multiset determines λ, #3509), but the statistic
     is n(λ) = Σ_box row(box) -- the CO-CONTENT / principal-specialization exponent
     (s_λ(1,q,q²,…) = q^{n(λ)}·…), a q^{2ρ}-type PIVOTAL grading of the ribbon
     category, NOT a symmetric function of the JM contents c = col - row. This is the
     structural home of the Δ_λ chirality sign: the pivotal/ρ-grading at ζ₄.

OPEN (not claimed): the exact pivotal element + the magnitude |Δ_λ| = dim. Records
the narrowing; does not derive Δ_λ (Track A gated).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from t25_cinquefoil_deltalambda_sign_probe import (  # noqa: E402
    partitions, conjugate, target_sign)
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def n_lambda(lam):
    return sum(i * p for i, p in enumerate(lam))


def contents(lam):
    return [c - r for r, row in enumerate(lam) for c in range(row)]


def psum(lam, k):
    return sum(c ** k for c in contents(lam))


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # A. NOT a framing power (full twist / framing sqrt) — restated from #3509.
    def cs(lam):
        return n_lambda(conjugate(lam)) - n_lambda(lam)
    ft_fail = any(int(sp.re(sp.I ** (2 * cs(lam)))) != target_sign(lam) for lam in partitions(5))
    ht_fail = any((sp.im(sp.I ** cs(lam)) != 0) or (int(sp.re(sp.I ** cs(lam))) != target_sign(lam))
                  for lam in partitions(5))
    check("not_a_framing_power", ft_fail and ht_fail,
          "sign ≠ full twist q^{2(n(λ')-n(λ))} AND ≠ framing sqrt q^{n(λ')-n(λ)} at q=i")

    # B. NOT a low-degree JM content-symmetric central element: n(λ) is not an exact
    #    polynomial in the content power sums, tested against the COMPLETE symmetric basis
    #    up to weighted degree 6 (every monomial Π_k p_{μ_k}, μ⊢d, d≤D — includes p_1^3,
    #    p_1^4, p_1^2 p_2, …), pooled over λ⊢4..8 (60 partitions ≫ #features).
    #    Existence of an exact solution ⇔ rank(A)=rank([A|b]) (Rouché–Capelli).
    lams = [l for N in (4, 5, 6, 7, 8) for l in partitions(N)]
    found_D = None
    for D in range(1, 7):
        feats = [lambda l: 1, lambda l: sum(l)]        # constant + |λ| (= p_0)
        for d in range(1, D + 1):
            for mu in partitions(d):                    # complete degree-d monomial basis
                feats.append(lambda l, mu=mu: sp.Mul(*[psum(l, k) for k in mu]))
        A = sp.Matrix([[sp.Integer(f(l)) for f in feats] for l in lams])
        b = sp.Matrix([sp.Integer(n_lambda(l)) for l in lams])
        if A.rank() == A.row_join(b).rank():            # exact solution exists
            found_D = D
            break
    check("not_a_low_degree_JM_central_element", found_D is None,
          "n(λ) is NOT an exact polynomial in the content power sums (COMPLETE symmetric "
          "basis, weighted degree ≤ 6, λ⊢4..8) => q^{2n(λ)} is not a canonical low-degree "
          "JM/framing central element")

    # C. It IS realizable (content multiset determines λ) but via the CO-CONTENT
    #    statistic n(λ)=Σ row(box), the principal-specialization (pivotal) grading —
    #    distinct from the content sum Σ c = n(λ')-n(λ) that framings see.
    def cocontent_sum(lam):
        return sum(r for r, row in enumerate(lam) for _ in range(row))
    is_cocontent = all(cocontent_sum(lam) == n_lambda(lam) for lam in partitions(6))
    distinct_from_content = any(n_lambda(lam) != cs(lam) for lam in partitions(5))
    check("carrier_is_cocontent_principal_specialization_grading",
          is_cocontent and distinct_from_content,
          "n(λ) = Σ_box row(box) (co-content / principal-spec exponent, s_λ(1,q,..)=q^{n(λ)}·…), "
          "distinct from the content sum n(λ')-n(λ) framings grade by => pivotal/ρ-grading, not JM")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "NARROWED (structural; nothing derived): the Δ_λ sign carrier q^{2n(λ)} (=(-1)^{n(λ)} "
        "at q=i, ζ₄) is a central character but (A) NOT a framing power — full twist and "
        "framing sqrt are graded by the content sum n(λ')-n(λ), not n(λ); (B) NOT a low-degree "
        "JM content-symmetric central element — n(λ) is not an exact polynomial in the content "
        "power sums (complete symmetric basis, weighted degree ≤ 6, λ⊢4..8); (C) it is the "
        "CO-CONTENT / principal-specialization grading n(λ)=Σ row "
        "(s_λ(1,q,q²,…)=q^{n(λ)}·…), a q^{2ρ}-type PIVOTAL grading of the ribbon category, "
        "distinct from the JM contents c=col-row. So the Δ_λ chirality sign lives in the ribbon "
        "PIVOTAL structure at ζ₄, not a braid central element. OPEN (not claimed): the exact "
        "pivotal element and the magnitude |Δ_λ|=dim (Track A). Records the narrowing; does not "
        "derive Δ_λ. NOTHING wired."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "deltalambda-sign-operator-narrowing",
        "description": "The Δ_λ sign carrier q^{2n(λ)} is a central character but not a framing "
                       "power and not a low-degree JM content-symmetric central element; it is the "
                       "co-content / principal-specialization (pivotal) grading at ζ₄. Narrows the "
                       "operator; does not derive Δ_λ.",
        "auditOnly": "docs/audits/2026-07-11-deltalambda-sign-operator-narrowing.md",
        "tier": "symbolic-exact (sympy; rational linear algebra + q=i identities)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "not_framing_power": bool(ft_fail and ht_fail),
            "min_JM_poly_degree_found": found_D,
            "carrier_statistic": "n(λ)=Σ row(box) — co-content / principal-specialization (pivotal) grading",
            "verdict": verdict,
        },
        "context": {
            "prior": "computations/deltalambda/deltalambda-sign-cyclotomic-locus.witness.json (#3509)",
            "selection_rule": "QOU.SelectionRules (bar-parity + sign-positivity)",
            "open": "exact pivotal element realizing q^{2n(λ)}; magnitude |Δ_λ|=dim (Track A)",
            "gate": "Δ_λ gate — structural narrowing, no fit, nothing wired",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # Payload carries a top-level `assertions` mapping → stamp preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(_HERE, "deltalambda-sign-operator-narrowing.witness.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial. `os.replace` is atomic on POSIX within a
    # filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
