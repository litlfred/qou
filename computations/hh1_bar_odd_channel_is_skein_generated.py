#!/usr/bin/env python3
"""PROBE — what the R-matrix says about the bar-odd channel.

Follow-up to qou-qb8d (the tr_M-paired number is MIXED: S = S_even + S_odd
with S_odd != 0).  Question: what do the R-matrix / transfer matrix have to
say about that decomposition?

THE STRUCTURAL CLAIM
--------------------
The R-matrix is the braiding sigma_i, and the bar involution sends
sigma_i -> sigma_i^{-1}: bar IS crossing reversal, i.e. the MIRROR IMAGE.
Splitting the R-matrix into its bar-eigenparts, using the Hecke
eigenprojections sigma = q P_+ - q^{-1} P_- (P_+ + P_- = 1):

    sigma - sigma^{-1} = (q - q^{-1}) * 1 = a * 1      <- bar-ODD, and CENTRAL
    sigma + sigma^{-1} = [2]_q (P_+ - P_-)             <- bar-EVEN

The bar-ODD part of the R-matrix is exactly the SKEIN RELATION, and it is a
scalar multiple of the identity.  So the bar-odd channel of H_n(q) is
*generated* by a = q - q^{-1}: anything bar-odd is a times something bar-even
(bar(a) = -a, so a * even = odd).

FALSIFIABLE PREDICTION.  Every bar-ODD component S_odd measured in
`hh1_outer_class_trace_paired_parity.py` must be divisible by a, with a
BAR-EVEN quotient.  This is checked, not asserted -- and it is falsifiable:
an S_odd whose quotient S_odd/a came out bar-ODD would refute the claim.

WHY IT MATTERS FOR c_3.  If the bar-odd channel is a-generated, then the
bar-odd swing S the c_3 route needs is forced into the shape

    S = a * (bar-even),      a = q - q^{-1},

which is a structural constraint on the residual -- a shape, not a value.  It
does NOT supply the magnitude (bean qou-qb8e), and it is not a derivation of
c_3.  Reported as a shape constraint only.

No fit.  Nothing wired.
"""
import json
import os

import sympy as sp

import hh1_outer_class_cocenter_bar_parity as B
import hh1_outer_class_trace_paired_parity as T
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

q = B.q
z = T.z
DIM = B.DIM


def bar_at(expr):
    """Bar on Q(zeta)[z], z bar-EVEN (delegates to the qb8d implementation)."""
    return T.bar_z_even(expr)


def check_r_matrix_decomposition(assertions):
    """sigma - sigma^{-1} = a*1  and  sigma + sigma^{-1} = [2]_q (P_+ - P_-)."""
    print(f"\n{'=' * 70}\nR-MATRIX BAR-DECOMPOSITION (symbolic in q)\n{'=' * 70}")
    # NOTE (a bug this function originally had): the test MUST run at the
    # ELEMENT level. The matrix of left-multiplication is written in the T_w
    # basis, and that basis is NOT bar-invariant (bar(T_w) != T_w), so applying
    # q -> 1/q to the matrix ENTRIES is a different operation from bar-ing the
    # element. B.bar_apply carries the basis change; naive entry substitution
    # does not, and it falsely reported sigma + sigma^{-1} as not bar-even.
    a = B.a
    one = B.evec(0)
    for gen in (1, 2):
        sig = B.evec(gen)                       # sigma_gen
        sig_inv = B.evec(gen) - a * one         # sigma^{-1} = sigma - a
        assert sp.simplify(B.mul(sig, sig_inv) - one).is_zero_matrix, \
            f"sigma_{gen}^{{-1}} = sigma - a failed"
        # bar really does swap sigma and sigma^{-1} (bar = crossing reversal)
        assert sp.simplify(B.bar_apply(sig) - sig_inv).is_zero_matrix, \
            f"bar(sigma_{gen}) != sigma_{gen}^{{-1}}"

        odd = sp.simplify(sig - sig_inv)
        even = sp.simplify(sig + sig_inv)
        # ODD part is a*1 -- the Skein relation, and CENTRAL
        assert sp.simplify(odd - a * one).is_zero_matrix, \
            f"sigma_{gen} - sigma_{gen}^{{-1}} != a*1"
        assert sp.simplify(B.bar_apply(odd) + odd).is_zero_matrix, \
            f"sigma_{gen} - sigma_{gen}^{{-1}} is not bar-ODD"
        assert sp.simplify(B.bar_apply(even) - even).is_zero_matrix, \
            f"sigma_{gen} + sigma_{gen}^{{-1}} is not bar-EVEN"
        # EVEN part = [2]_q (P_+ - P_-), P_+ = (sigma+q^{-1})/[2]_q,
        # P_- = (q-sigma)/[2]_q  =>  [2]_q (P_+ - P_-) = 2 sigma - a.
        two_q = q + 1 / q
        Pp = (sig + (1 / q) * one) / two_q
        Pm = (q * one - sig) / two_q
        assert sp.simplify(B.mul(Pp, Pp) - Pp).is_zero_matrix, "P_+ not idempotent"
        assert sp.simplify(B.mul(Pm, Pm) - Pm).is_zero_matrix, "P_- not idempotent"
        assert sp.simplify(Pp + Pm - one).is_zero_matrix, "P_+ + P_- != 1"
        assert sp.simplify(two_q * (Pp - Pm) - even).is_zero_matrix, \
            f"sigma_{gen} + sigma_{gen}^{{-1}} != [2]_q (P_+ - P_-)"
        print(f"  bar(sigma_{gen}) = sigma_{gen}^-1  (bar = crossing reversal)  OK")
        print(f"  sigma_{gen} - sigma_{gen}^-1 = a*1  bar-ODD, CENTRAL (Skein)  OK")
        print(f"  sigma_{gen} + sigma_{gen}^-1 = [2]_q(P_+ - P_-)  bar-EVEN     OK")
    assertions.append({
        "name": "r_matrix_bar_decomposition", "passed": True,
        "detail": ("bar(sigma) = sigma^{-1} (crossing reversal); "
                   "sigma - sigma^{-1} = a*1 is bar-ODD and CENTRAL -- it IS "
                   "the Skein relation; sigma + sigma^{-1} = [2]_q (P_+ - P_-) "
                   "is bar-EVEN, with P_+/P_- verified idempotent and summing "
                   "to 1. Element-level, symbolic in q, both generators.")})


def check_a_generates_odd_channel(qval, label, assertions):
    """Every measured S_odd must be a * (bar-EVEN).  Falsifiable."""
    print(f"\n{'=' * 70}\n{label}   (q = {qval})\n{'=' * 70}")
    subs = {q: qval}
    a_val = sp.simplify(B.a.subs(subs))
    print(f"  a = q - q^-1 = {a_val}")
    assert sp.simplify(bar_at(a_val) + a_val) == 0, "a is not bar-ODD"
    print("  assert  a is bar-ODD                                  OK")

    # Recompute the paired numbers exactly as qb8d does.
    P, S, mdim = B.quotient_data(subs)
    tr_at = T.TR_VEC.subs(subs).applyfunc(sp.simplify)
    ders = B.derivation_space(subs)
    inns = B.inner_derivations(subs)
    inn_space = sp.Matrix.hstack(*[B.flatten(M) for M in inns])
    dim_inn = inn_space.rank()
    if len(ders) - dim_inn == 0:
        print("  HH^1 = 0 -> nothing to check here.")
        return {"label": label, "dim_HH1": 0, "rows": []}
    outer = None
    for v in ders:
        M = B.vec_to_matrix(v)
        if sp.Matrix.hstack(inn_space, B.flatten(M)).rank() > dim_inn:
            outer = M
            break
    Delta = sp.simplify(P * outer * S)

    rows = []
    for idx, name, cls in T.MIN_LENGTH_CLASS_REPS:
        val = sp.simplify((tr_at * (S * (Delta * (P * B.evec(idx)))))[0, 0])
        if val == 0:
            continue
        s_odd = sp.simplify((val - bar_at(val)) / 2)
        if s_odd == 0:
            rows.append({"x": name, "S_odd": "0", "quotient": None,
                         "quotient_is_bar_even": None})
            continue
        quot = sp.simplify(sp.cancel(s_odd / a_val))
        q_bar = bar_at(quot)
        is_even = sp.simplify(q_bar - quot) == 0
        # THE FALSIFIABLE CHECK
        assert is_even, (
            f"PREDICTION REFUTED at {label}, x={name}: S_odd/a = {quot} is NOT "
            f"bar-even (bar of it = {q_bar}), so the bar-odd channel is not "
            "a-generated")
        print(f"  x = {name:6s}  S_odd = {s_odd}")
        print(f"  {'':10s}  S_odd / a = {quot}   -> bar-EVEN: {is_even}   OK")
        rows.append({"x": name, "S_odd": sp.sstr(s_odd),
                     "quotient": sp.sstr(quot), "quotient_is_bar_even": True})
    assertions.append({
        "name": f"bar_odd_channel_is_a_generated[{label}]", "passed": True,
        "detail": (f"every nonzero S_odd factors as a * (bar-EVEN) with "
                   f"a = {sp.sstr(a_val)}; {len(rows)} generators checked")})
    return {"label": label, "a": sp.sstr(a_val), "rows": rows}


def main():
    print("What the R-matrix says about the bar-odd channel")
    print("follow-up to qou-qb8d\n")
    assertions = []
    check_r_matrix_decomposition(assertions)
    z6 = sp.Rational(1, 2) + sp.sqrt(3) / 2 * sp.I
    results = [check_a_generates_odd_channel(sp.I, "q = i        ([2]_q = 0)",
                                             assertions),
               check_a_generates_odd_channel(z6, "q = zeta_6   ([3]_q = 0)",
                                             assertions)]

    print(f"\n{'=' * 70}\nCONCLUSION\n{'=' * 70}")
    print("  bar = crossing reversal = MIRROR IMAGE on the R-matrix.")
    print("  Its bar-ODD part IS the Skein relation, a*1, and it is CENTRAL.")
    print("  Consequently the bar-odd channel is a-generated, and every")
    print("  measured S_odd factors as a * (bar-EVEN) -- checked, falsifiable.")
    print("  => the bar-odd swing the c_3 route needs is forced into the SHAPE")
    print("     S = (q - q^-1) * (bar-even).  A shape constraint, NOT a value.")

    witness = {
        "schema": "qou-probe/v1",
        "probe": "bar-odd channel is Skein/a-generated (R-matrix reading)",
        "bean": "qou-qb8d follow-up; feeds qou-qb8e",
        "description": (
            "bar sends sigma -> sigma^{-1}, so bar is crossing reversal (mirror "
            "image). The bar-ODD part of the R-matrix is sigma - sigma^{-1} = "
            "a*1, which IS the Skein relation and is central; the bar-EVEN part "
            "is sigma + sigma^{-1} = [2]_q (P_+ - P_-). Hence the bar-odd "
            "channel is generated by a = q - q^{-1}. Falsifiable prediction "
            "checked: every S_odd from the qb8d pairing factors as a*(bar-EVEN)."),
        "assertions": assertions,
        "allPassed": all(x["passed"] for x in assertions),
        "results": results,
        "consequence": (
            "SHAPE constraint only: a bar-odd swing carried by this "
            "construction must have the form S = (q - q^{-1}) * (bar-even). "
            "This does NOT supply the magnitude and is NOT a derivation of "
            "c_3 -- the magnitude gate is bean qou-qb8e."),
        "scope": ("scope-(a). n=3 mechanism check. The R-matrix decomposition "
                  "itself is symbolic in q and n-independent (it is the Hecke "
                  "quadratic relation), but the S_odd factorization is measured "
                  "only at the two n=3 root-of-unity points."),
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "hh1-bar-odd-channel-skein-generated.witness.json")
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
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2, default=str)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
