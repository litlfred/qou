"""The published Q_beta ladder's ENTIRE convention dependence is one phase.

Written for `qou-cds1` (re-derive the c_k ladder under convention D). It
reports a NEGATIVE on a lead of my own and one sharpening of the open problem.
Nothing here is a derivation of the D-frame ladder.

WHAT I THOUGHT I HAD, AND WHY IT IS WRONG.  The ladder's constant
b = sqrt(q^4+q^2+1)/(q^2+1) satisfies b^2 = [3]_q z_D^2/q^4 exactly, while the
convention-C analogue fails -- which looked like evidence that b is a
convention-D object and that the rungs were already D-natural. It is not
evidence of anything. Resolving both sides into quantum integers:

    b   = sqrt([3]_q) / [2]_q        (Hoefsmit off-diagonal, axial distance 2)
    z_D = q^2 / [2]_q
    z_C = 1 / [2]_sqrt(q)

so substituting z_D = q^2/[2]_q into the identity returns b^2 = [3]_q/[2]_q^2,
which IS b. The identity is a restatement of the definition of z_D and carries
no information about b at all. Recorded because the failure mode -- a relation
that looks structural because two independently-defined objects share a
cyclotomic factor -- is the one this repo's da-arity-conflation criterion is
about, and I walked into it.

WHAT IS ACTUALLY TRUE.  b is a HOEFSMIT constant: it is built from the H_3
seminormal representation and contains NO Markov parameter. So b is neither a
C object nor a D object -- it is convention-INDEPENDENT. And so is every other
ingredient of the published ladder except one:

    Q_A   = |eps * m_e / (q(q-1))|,  eps = w*h - h,  w = h/2   -- z-free
    hbar_q = (q-1)/q                                           -- z-free
    b                                                          -- z-free
    rungs 1 - b^2 hbar^4, 1 - 2b^3 hbar^6, ...                 -- z-free
    alpha = (z - 1) h / 2                                      -- THE ONLY z

THE SHARPENED OPEN QUESTION.  AGENTS.md and QOU.QBeta.decayLadder_zC_threeRow_ne_zero
state that the D-frame ladder must be RE-DERIVED and that substituting z_D is
not a valid move. But the published formula's only z-dependence is the phase,
so a substitution would change exactly that phase and nothing else. Both cannot
be the whole story. The resolution has to be that the RUNGS' DERIVATION used
the three-row C-frame trace somewhere that has been integrated out of the final
formula -- because under D the trace is two-row (y_(1^3)(z_D) = 0). Locating
that step IS the re-derivation, and this probe does not locate it.

NOT NEW, and verified as not new: the D-frame H_3 weights below reproduce
computations/y-lambda-symbolic-witness.json (markov_convention: D) exactly.
This probe recomputes them from the regular representation as an independent
check on that committed witness, not as a new result.

Scope (a) throughout. Nothing wired; no value proposed for any c_k.
"""

from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
from pathlib import Path

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import json  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

q, z = sp.symbols("q z", positive=True)
h = q - 1 / q


def br(n, v):
    """[n]_v = v^(n-1) + v^(n-3) + ... + v^-(n-1)."""
    return sum(v ** (n - 1 - 2 * k) for k in range(n))


# --- H_3(q) regular representation in the T_w basis -------------------------
E, S0, S1 = (0, 1, 2), (1, 0, 2), (0, 2, 1)


def comp(p, r):
    return tuple(p[r[i]] for i in range(3))


def ln(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


BASIS = [E, S0, S1, comp(S0, S1), comp(S1, S0), comp(comp(S0, S1), S0)]
IDX = {w: i for i, w in enumerate(BASIS)}
N = 6


def left_gen(s):
    M = sp.zeros(N, N)
    for j, w in enumerate(BASIS):
        sw = comp(s, w)
        if ln(sw) > ln(w):
            M[IDX[sw], j] += 1
        else:
            M[IDX[w], j] += h
            M[IDX[sw], j] += 1
    return M


def d_frame_weights():
    """(y_(3), y_(2,1), y_(1^3)) of the H_3 Markov trace at z_D."""
    L = [left_gen(S0), left_gen(S1)]
    TRV = [sp.Integer(1), z, z, z**2, z**2, z * (h * z + 1)]
    chi3 = [q ** ln(w) for w in BASIS]
    chi111 = [(-1 / q) ** ln(w) for w in BASIS]
    mats = {E: sp.eye(N), S0: L[0], S1: L[1], comp(S0, S1): L[0] * L[1],
            comp(S1, S0): L[1] * L[0], comp(comp(S0, S1), S0): L[0] * L[1] * L[0]}
    chireg = [sp.expand(sp.trace(mats[w])) for w in BASIS]
    chi21 = [sp.simplify((chireg[i] - chi3[i] - chi111[i]) / 2) for i in range(N)]
    y3, y21, y111 = sp.symbols("y3 y21 y111")
    sol = sp.solve(
        [sp.Eq(TRV[i], y3 * chi3[i] + y21 * chi21[i] + y111 * chi111[i])
         for i in range(N)],
        [y3, y21, y111], dict=True)
    assert len(sol) == 1, "the Wedderburn solve must be determined"
    zD = q**3 / (q**2 + 1)
    s = sol[0]
    return (sp.simplify(s[y3].subs(z, zD)),
            sp.simplify(s[y21].subs(z, zD)),
            sp.simplify(s[y111].subs(z, zD)))


def main() -> int:
    wb = WitnessBuilder("qbeta-ladder-convention-dependence-is-one-phase",
                        engine="sympy")
    wb.set_description(
        "NEGATIVE plus a sharpening for qou-cds1. b^2 = [3]_q z_D^2/q^4 is a "
        "RESTATEMENT of z_D = q^2/[2]_q and says nothing about b; b is a "
        "convention-independent Hoefsmit constant sqrt([3]_q)/[2]_q. Every "
        "ingredient of the published ladder is z-free except the phase "
        "alpha = (z-1)h/2. Reproduces the committed D-frame H_3 weights as an "
        "independent check. Scope (a); nothing wired.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n      {note}")

    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    zD = q**3 / (q**2 + 1)
    zC = sp.sqrt(q) / (q + 1)

    print("=" * 76)
    print(" qou-cds1 — the ladder's convention dependence, located")
    print("=" * 76)
    print()

    # 1. b IS the Hoefsmit off-diagonal at axial distance 2 -> z-free.
    hoef = sp.sqrt(br(1, q) * br(3, q)) / br(2, q)
    check("b_is_the_hoefsmit_constant_sqrt3_over_2",
          sp.simplify(b - hoef) == 0,
          "b = sqrt([3]_q)/[2]_q exactly -- a seminormal-representation "
          "constant containing NO Markov parameter, so b is convention-"
          "INDEPENDENT, not a D object as I first read it")

    # 2. Both conventions are 'one over a quantum 2', in different variables.
    check("zD_is_q2_over_bracket2_q",
          sp.simplify(zD - q**2 / br(2, q)) == 0,
          "z_D = q^2/[2]_q")
    check("zC_is_one_over_bracket2_sqrtq",
          sp.simplify(zC - 1 / br(2, sp.sqrt(q))) == 0,
          "z_C = 1/[2]_sqrt(q) -- same shape, variable sqrt(q) not q")

    # 3. THE RETRACTION: the identity carries no information about b.
    lead = sp.simplify(b**2 - br(3, q) * zD**2 / q**4)
    substituted = sp.simplify(br(3, q) * (q**2 / br(2, q))**2 / q**4
                              - br(3, q) / br(2, q)**2)
    check("my_lead_is_a_restatement_not_a_finding",
          lead == 0 and substituted == 0,
          "b^2 = [3]_q z_D^2/q^4 holds, AND substituting z_D = q^2/[2]_q "
          "returns b^2 = [3]_q/[2]_q^2, which is b's own definition. The "
          "identity is the definition of z_D rewritten -- RETRACTED as a lead")

    # 4. Independent check on the committed D-frame weights.
    y3, y21, y111 = d_frame_weights()
    wit = HERE.parent / "y-lambda-symbolic-witness.json"
    rec = {tuple(w["partition"]): w["y_lambda_symbolic"]
           for w in json.loads(wit.read_text())["tables_by_n"]["3"]["weights"]}
    agree = all(
        # sympify must be given the SAME positive-assumption symbol, or it
        # mints a fresh q and nothing ever simplifies to 0 (caught by this
        # assertion failing while the printed values were identical).
        sp.simplify(mine - sp.sympify(rec[part], locals={"q": q})) == 0
        for mine, part in ((y3, (3,)), (y21, (2, 1)), (y111, (1, 1, 1))))
    check("reproduces_the_committed_D_frame_weights",
          agree,
          f"y_(3) = {sp.factor(y3)}, y_(2,1) = {sp.factor(y21)}, "
          f"y_(1^3) = {y111} -- all three match "
          f"y-lambda-symbolic-witness.json (markov_convention: D). NOT NEW; "
          f"an independent recomputation from the regular representation")

    # 5. The surviving weight is a clean quantum integer, and normalisation holds.
    check("surviving_weight_is_one_over_bracket2_squared",
          sp.simplify(y21 - 1 / br(2, q) ** 2) == 0
          and sp.simplify(y3 * 1 + y21 * 2 + y111 * 1 - 1) == 0,
          "y_(2,1)(z_D) = 1/[2]_q^2 and tr_M^D(T_e) = 1 exactly. The trace is "
          "TWO-ROW under D: tr_M^D = ([2]_{q^2} chi^(3) + chi^(2,1))/[2]_q^2")

    # 6. The sharpening: exactly one ingredient of the ladder carries z.
    hbar = (q - 1) / q
    eps = (h / 2) * h - h
    QA = sp.Abs(_qbeta_e0.order_zero_scaled(eps, q))          # m_e factored out; it is z-free
    rungs = [1 - b**2 * hbar**4, 1 - 2 * b**3 * hbar**6,
             1 - 2 * b**4 * b**4 * hbar**8,
             1 - (b**2 + sp.Rational(1, 2)) * b**5 * hbar**10]
    zfree = all(z not in e.free_symbols for e in [QA, hbar, b] + rungs)
    alpha = (z - 1) * h / 2
    check("convention_dependence_is_exactly_one_phase",
          zfree and z in alpha.free_symbols,
          "Q_A, hbar_q, b and all four rungs are z-FREE; alpha = (z-1)h/2 is "
          "the only z. So a z-substitution would change the phase and nothing "
          "else -- which is why 're-derive, do not z-swap' must mean the "
          "RUNGS' DERIVATION used the three-row trace somewhere already "
          "integrated out of the formula. Locating that step IS qou-cds1, and "
          "this probe does NOT locate it")

    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    wb.add_data("b_quantum_integer_form", "sqrt([3]_q)/[2]_q")
    wb.add_data("zD_quantum_integer_form", "q^2/[2]_q")
    wb.add_data("zC_quantum_integer_form", "1/[2]_sqrt(q)")
    wb.add_data("y_2_1_at_zD", str(sp.factor(y21)))
    wb.add_data("y_3_at_zD", str(sp.factor(y3)))
    wb.add_data("y_1_1_1_at_zD", str(y111))

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
