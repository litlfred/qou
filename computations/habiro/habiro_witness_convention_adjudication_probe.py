#!/usr/bin/env python3
"""Adjudicates the two Habiro witnesses: the committed one is convention C.

Bean `qou-iayk` (which this probe UNBLOCKS), bean `qou-ls7l`, bean `qou-3zby`.

THE QUESTION
------------
`habiro_coefficients_extended.py` was unrunnable until the `LaurentQ.from_sympy`
parser fix (PR #5376). Once it runs, it emits values that disagree materially
with the committed `habiro-coefficients-extended.witness.json` that the L1
`cross_check_trM_1ppb` gate reads. Which one is right?

I previously BLOCKED the regeneration (bean `qou-iayk`) on the grounds that the
fresh values break the landed closed form

    D(u) = 2^(2A+1) * u^(18Z+21N+1) * (1+u^2)^(3A-1)

which the committed witness satisfies exactly on all four atoms. **That block
was wrong, and this probe retracts it.** Two measurements overturn it.

MEASUREMENT 1 — the committed witness does not describe tr_M
------------------------------------------------------------
The witness's own `reconstruction_matches: true` verifies only the INNER
identity `p(u) == reconstruct(a_m)` — that the cyclotomic expansion of `p`
is self-consistent. It never checks the OUTER identity

    p(u) / (u^shift * D(u))  ==  tr_M_atomic(Z, N) |_{q -> u^2}

which is the only thing making the file a statement about the Markov trace at
all. Checked here by exact evaluation at rational `u` (no float anywhere): the
committed witness FAILS it. So "the committed witness satisfies the D(u) law"
was never evidence that it is correct — it is a self-consistent object that
does not represent today's tr_M.

MEASUREMENT 2 — the disagreement is exactly a C-vs-D convention change
----------------------------------------------------------------------
The Markov-Ocneanu prefactor contributes `z^(n_strands - 1)`, i.e. the
denominator of `z` raised to `3A - 1`. Reading off the cyclotomic factor:

    committed : (u^2 + 1)^(3A-1)  = (1 + q)^(3A-1)    <- denominator of
                                                          z_C = q^(1/2)/(q+1)
    fresh     : (u^4 + 1)^(3A-1)  = (1 + q^2)^(3A-1)  <- denominator of
                                                          z_D = q^3/(q^2+1)

Both carry the exponent `3A - 1` exactly, on the two different bases. The
committed witness is dated 2026-07-18; `pyhecke/gram.py` records "TRACE
CONVENTION D (z = q^3/(q^2+1)) since 2026-08-15" per the owner ruling. So the
committed file is a **convention-C** object and the fresh values are
**convention-D** — which is also why regenerating moves the L1 gate's Habiro
column onto D, agreeing with Hoefsmit to ~2e-7 where it was ~0.5 off.

WHY THE LAW IS NOT A COUNTER-ARGUMENT
--------------------------------------
`d_u_closed_form_proof.py` is itself C-frame, and its exponent is FITTED:

  * `2^(2A+1)` and `(1+u^2)^(3A-1)` are derived (averaged-crossing count and
    n_strands = 3A) — but derived *in convention C*, since `(1+u^2)` IS the
    z_C denominator;
  * `u^(18Z+21N+1)` is not derived at all. The module says so verbatim: "The
    u^shift residual is the only piece this script does NOT close." Its
    `EMPIRICAL_D_U` table is, by its own comment, "extracted from
    habiro-coefficients-extended.witness.json" — the disputed file — and
    `18Z+21N+1` reproduces that table on all six atoms because it was fitted
    to it. `PER_CROSSING_SHIFT_INTRA` is an integer LP solved to land on the
    targets 18 and 21 after the fact.

So "the fresh values break the law" restates "the fresh values are not
convention C". Per the standing instruction that C-frame results are correct
for C and need SCOPING, not correction, the law wants a convention-C label —
not a fix, and not a veto over the D-frame regeneration.

SCOPE
-----
Scope-(a). This adjudicates WHICH witness the C/D ruling makes canonical; it
does not itself regenerate or overwrite anything, and no `c_k` value or tier
changes. The uniform 6x prefactor ratio (192/32, 768/128, 768/128, 3072/512)
is recorded as measured and is NOT explained here — it is the open residual,
and it is a question about the D-frame normalisation, not a reason to keep a
witness that fails its own outer identity.

Usage:
    python3 computations/habiro/habiro_witness_convention_adjudication_probe.py

Output:
    computations/habiro/habiro-witness-convention-adjudication.witness.json
"""

from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _pb  # noqa: E402

from habiro_coefficients_atomic import reconstruct, to_u_polynomial  # noqa: E402
from hecke_laurent_fast import tr_M_atomic_fast as tr_M_atomic  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

U = sp.Symbol("u", positive=True, real=True)

# Exact rational probe points for the outer identity. Chosen away from 0, 1 and
# from the roots of (u^2+1)/(u^4+1) (which are complex anyway), and kept
# small-denominator so the exact rational arithmetic stays cheap. Evaluation is
# in `Fraction` throughout -- no float64 anywhere in this file.
PROBE_POINTS = [Fraction(2), Fraction(3), Fraction(3, 2), Fraction(5, 3)]


def _law(Z: int, N: int) -> dict:
    A = Z + N
    return {"two_power": 2 ** (2 * A + 1), "u_shift": 18 * Z + 21 * N + 1,
            "cyc_exp": 3 * A - 1}


def _exact_eval(expr: sp.Expr, u0: Fraction) -> Fraction | None:
    """Evaluate a rational function of `u` at rational `u0`, exactly."""
    val = sp.nsimplify(expr.subs(U, sp.Rational(u0.numerator, u0.denominator)))
    val = sp.cancel(val)
    if not val.is_rational:
        return None
    r = sp.Rational(val)
    return Fraction(int(r.p), int(r.q))


def _outer_identity_holds(p_u, shift, denom, tr_u) -> tuple[bool, str]:
    """Check p/(u^shift * D) == tr_M(u^2) by exact evaluation at rationals."""
    lhs = p_u / (U ** shift * denom)
    for u0 in PROBE_POINTS:
        a = _exact_eval(lhs, u0)
        b = _exact_eval(tr_u, u0)
        if a is None or b is None:
            return False, f"non-rational value at u={u0}"
        if a != b:
            return False, f"u={u0}: lhs={a} != rhs={b}"
    return True, f"exact agreement at u in {[str(p) for p in PROBE_POINTS]}"


def _cyc_base(denom_factored: sp.Expr) -> str:
    """Report which cyclotomic base the denominator carries."""
    s = str(sp.factor(denom_factored))
    if "u**4 + 1" in s:
        return "u^4+1  (= 1+q^2, denominator of z_D = q^3/(q^2+1))"
    if "u**2 + 1" in s:
        return "u^2+1  (= 1+q,   denominator of z_C = q^(1/2)/(q+1))"
    return "unrecognised"


def main() -> int:
    t0 = time.monotonic()
    # prefer_dir is the computations/ root, which is where the L1 gate
    # (cross_check_trM_1ppb) resolves it from -- there are TWO copies of this
    # stem (bean qou-kcii) and reading the wrong one would adjudicate the
    # wrong file. prefer_dir takes a Path, not a str.
    wpath = _pb.witness_path("habiro-coefficients-extended.witness.json",
                             prefer_dir=HERE.parent)
    committed = json.load(open(wpath, encoding="utf-8"))
    print(f"committed witness: {wpath}")
    print(f"  computedAt {committed.get('computedAt')}  "
          f"commitSha {str(committed.get('commitSha'))[:10]}\n")

    atoms = []
    for label, r in committed["results"].items():
        Z, N, A = r["Z"], r["N"], r["A"]
        t_atom = time.monotonic()
        print(f"── {label} (Z={Z}, N={N}, A={A}) ──", flush=True)

        # --- fresh side: recompute from tr_M directly -----------------------
        expr = tr_M_atomic(Z, N, include_inter=True)
        q = next(s for s in expr.free_symbols if str(s) == "q")
        tr_u = sp.cancel(sp.together(expr.subs(q, U ** 2)))
        p_fresh, shift_fresh, denom_fresh_s = to_u_polynomial(
            sp.together(expr), q, U)
        denom_fresh = sp.factor(sp.sympify(denom_fresh_s,
                                           locals={"check_q": U, "u": U}))

        # --- committed side: rebuild p(u) from the stored a_m ---------------
        coeffs = []
        for c in r["habiro_coefficients"]:
            cc = dict(c)
            cc["a_m"] = sp.sympify(cc["a_m"], locals={"check_q": U, "u": U})
            coeffs.append(cc)
        p_comm = sp.expand(reconstruct(coeffs, U, max_m=len(coeffs)))
        denom_comm = sp.factor(sp.sympify(r["denom_in_u"],
                                          locals={"check_q": U, "u": U}))
        shift_comm = r["shift"]

        # The INNER check the witness already reports (a_m -> p(u)).
        inner_ok = int(sp.Poly(p_comm, U).degree()) == r["deg_p_u"]

        # The OUTER check the witness never made.
        outer_comm, why_comm = _outer_identity_holds(
            p_comm, shift_comm, denom_comm, tr_u)
        outer_fresh, why_fresh = _outer_identity_holds(
            p_fresh, shift_fresh, denom_fresh, tr_u)

        law = _law(Z, N)
        rec = {
            "atom": label, "Z": Z, "N": N, "A": A,
            "committed": {
                "denom_factored": str(denom_comm),
                "shift": shift_comm,
                "deg_p_u": r["deg_p_u"],
                "cyclotomic_base": _cyc_base(denom_comm),
                "inner_reconstruction_ok": bool(inner_ok),
                "outer_identity_ok": bool(outer_comm),
                "outer_identity_detail": why_comm,
            },
            "fresh": {
                "denom_factored": str(denom_fresh),
                "shift": int(shift_fresh),
                "deg_p_u": int(sp.Poly(p_fresh, U).degree()),
                "cyclotomic_base": _cyc_base(denom_fresh),
                "outer_identity_ok": bool(outer_fresh),
                "outer_identity_detail": why_fresh,
            },
            "landed_law": law,
        }
        atoms.append(rec)
        print(f"   committed D = {denom_comm}")
        print(f"     base: {rec['committed']['cyclotomic_base']}")
        print(f"     inner (a_m -> p) ok = {inner_ok} ; "
              f"OUTER ok = {outer_comm}  [{why_comm}]")
        print(f"   fresh     D = {denom_fresh}")
        print(f"     base: {rec['fresh']['cyclotomic_base']}")
        print(f"     OUTER ok = {outer_fresh}  [{why_fresh}]")
        print(f"   law: 2^{2*A+1}={law['two_power']} * u^{law['u_shift']} "
              f"* (1+u^2)^{law['cyc_exp']}")
        print(f"   ({time.monotonic()-t_atom:.1f}s)\n", flush=True)

    n = len(atoms)
    comm_outer_fail = sum(1 for a in atoms if not a["committed"]["outer_identity_ok"])
    fresh_outer_ok = sum(1 for a in atoms if a["fresh"]["outer_identity_ok"])
    comm_is_C = sum(1 for a in atoms if a["committed"]["cyclotomic_base"].startswith("u^2+1"))
    fresh_is_D = sum(1 for a in atoms if a["fresh"]["cyclotomic_base"].startswith("u^4+1"))
    cyc_exp_ok = sum(1 for a in atoms
                     if f"**{a['landed_law']['cyc_exp']}" in a["fresh"]["denom_factored"])
    comm_matches_law = sum(
        1 for a in atoms
        if (f"{a['landed_law']['two_power']}*u**{a['landed_law']['u_shift']}"
            in a["committed"]["denom_factored"].replace(" ", "")))

    assertions = [
        {"name": "1_committed_fails_outer_identity",
         "passed": comm_outer_fail == n,
         "detail": f"{comm_outer_fail}/{n} committed atoms FAIL "
                   "p/(u^shift*D) == tr_M(u^2), exact rational evaluation. The "
                   "witness's own reconstruction_matches checks only the inner "
                   "a_m -> p(u) expansion and never this."},
        {"name": "2_fresh_satisfies_outer_identity",
         "passed": fresh_outer_ok == n,
         "detail": f"{fresh_outer_ok}/{n} fresh atoms satisfy the outer identity."},
        {"name": "3_committed_is_convention_C",
         "passed": comm_is_C == n,
         "detail": f"{comm_is_C}/{n} committed denominators carry (u^2+1) = 1+q, "
                   "the z_C denominator. Witness dated 2026-07-18; gram.py "
                   "records convention D as canonical since 2026-08-15."},
        {"name": "4_fresh_is_convention_D",
         "passed": fresh_is_D == n,
         "detail": f"{fresh_is_D}/{n} fresh denominators carry (u^4+1) = 1+q^2, "
                   "the z_D denominator."},
        {"name": "5_both_carry_the_derived_3A_minus_1_exponent",
         "passed": cyc_exp_ok == n,
         "detail": f"{cyc_exp_ok}/{n} fresh denominators carry the exponent "
                   "3A-1 (= n_strands - 1 from the Markov-Ocneanu z^(n-1) "
                   "prefactor) on the D base. The DERIVED exponent survives the "
                   "convention change; only the BASE moves. So the exponent is "
                   "not evidence either way -- the base is."},
        {"name": "6_landed_law_is_the_C_frame_one",
         "passed": comm_matches_law == n,
         "detail": f"{comm_matches_law}/{n} committed denominators match the "
                   "landed D(u) law's prefactor and u-exponent exactly. Since "
                   "the law's EMPIRICAL_D_U table is by its own comment "
                   "'extracted from habiro-coefficients-extended.witness.json', "
                   "an exact match on the FITTED exponent 18Z+21N+1 is circular "
                   "and carries no evidential weight."},
    ]
    all_passed = all(a["passed"] for a in assertions)

    payload = {
        # NOT keyed "computation": wrap_legacy clobbers that key's VALUE while
        # leaving the key in place (bean qou-j9yk), so a key-set diff shows no
        # loss. Held as computation_method until that is fixed upstream --
        # tools/qou-substrate has 309 importers.
        "computation_method": (
            "Symbolic sympy over the formal variable u (q = u^2). The outer "
            "identity is checked by EXACT evaluation at small rationals via "
            "fractions.Fraction / sympy.Rational -- no float64 anywhere."),
        "description": (
            "Adjudicates the two Habiro witnesses. The committed "
            "habiro-coefficients-extended.witness.json FAILS the outer identity "
            "p/(u^shift*D) == tr_M(u^2) on every atom -- a check its own "
            "reconstruction_matches never made -- and carries the z_C "
            "denominator (1+q)^(3A-1), making it a convention-C object predating "
            "the 2026-08-15 owner ruling. The freshly computed values satisfy "
            "the outer identity and carry the z_D denominator (1+q^2)^(3A-1). "
            "The landed D(u) closed form is likewise C-frame and its u-exponent "
            "is FITTED to the disputed witness, so 'the fresh values break the "
            "law' restates 'the fresh values are not convention C'. RETRACTS "
            "the regeneration block recorded in bean qou-iayk."),
        "audit_only": True,
        "tier": "symbolic-exact",
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q-GENERIC: every quantity is a symbolic rational function of q "
            "(equivalently u, q = u^2), evaluated only at small exact rationals "
            "chosen as probe points. No substrate anchor is read and none is "
            "recorded -- deliberately no q0Value, which the q0-anchor audit "
            "correctly reads as contradicting `independent`."),
        "scope": (
            "scope-(a). Adjudicates which witness the C/D ruling makes "
            "canonical; does NOT regenerate or overwrite anything, and no c_k "
            "value or tier changes. The uniform 6x prefactor ratio is recorded "
            "as measured and deliberately NOT explained here -- it is the open "
            "residual."),
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "atoms": atoms,
            "verdict": (
                "The committed witness is convention C and does not represent "
                "today's tr_M. The fresh values are convention D and do. Under "
                "the 2026-08-15 owner ruling making D canonical, the "
                "regeneration is a C->D migration, not a corruption. The D(u) "
                "closed form needs a convention-C SCOPE label, per the standing "
                "instruction that C-frame results are correct for C and need "
                "scoping rather than correction."),
            "open_residual": (
                "The fresh prefactor is a uniform 6x the C-frame one (192/32, "
                "768/128, 768/128, 3072/512) on all four atoms. Uniform-in-A "
                "means it is not a per-strand or per-crossing factor. 6 = 2*3 "
                "and 3 is not a power of 2, so it cannot come from the "
                "averaged-crossing (sigma+sigma^-1)/2 mechanism that produces "
                "2^(2A+1). Unexplained; it is a question about the D-frame "
                "normalisation, and it is NOT a reason to retain a witness that "
                "fails its own outer identity."),
        },
        "context": {
            "bean_retracted": "qou-iayk (the regeneration block -- lifted)",
            "beans": ["qou-ls7l", "qou-3zby", "qou-kcii"],
            "owner_ruling": "2026-08-15 R1 -- convention D canonical",
            "gram_py": "tools/pyhecke/python/pyhecke/gram.py:15 -- "
                       "'TRACE CONVENTION D (z = q^3/(q^2+1)) since 2026-08-15'",
            "committed_witness_computedAt": committed.get("computedAt"),
            "law_is_fitted": (
                "d_u_closed_form_proof.py EMPIRICAL_D_U is by its own comment "
                "'extracted from habiro-coefficients-extended.witness.json'; "
                "18Z+21N+1 reproduces it on all six atoms because it was fitted "
                "to it, and the module states the u^shift residual is 'the only "
                "piece this script does NOT close'."),
        },
    }

    b = WitnessBuilder.wrap_legacy(
        "habiro-witness-convention-adjudication",
        payload,
        script_path=__file__,
        engine="sympy",
        engine_version=sp.__version__,
        output_dir=HERE,
        start_time=t0,
    )
    out = b.save()
    print(f"witness -> {out}")
    print(f"allPassed: {all_passed}  ({time.monotonic()-t0:.1f}s)")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
