#!/usr/bin/env python3
"""
qbeta_which_algebra_the_decay_channel_lives_in_probe.py — qou-879g answered from
the corpus, and the obstruction it exposes in the Q_beta ansatz.

# Ref: folio/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md
# Ref: folio/quantum-observable-universe/observations/algebraic-gns-embedding.md
# Ref: computations/qbeta/qbeta_d_frame_tl_quotient_phase_probe.py
# Ref: computations/qbeta/qbeta_net_trace_invariance_probe.py

THE QUESTION AND WHY THE BEAN WAS PREMATURE. I opened qou-879g asking whether the
convention-D decay channel lives in H_3(q) or in its Temperley-Lieb quotient,
and called it an owner decision. The four-path corpus grep says the corpus has
already decided it. `prf:algebraic-gns-embedding` reads, verbatim:

  "Under the production convention D this ideal is NOT trivial: tr_M = sum_lambda
   y_lambda chi^lambda with y_lambda = 0 exactly when l(lambda) >= 3, so N is the
   sum of those Wedderburn blocks -- THE TEMPERLEY-LIEB RADICAL -- and the GNS
   space is the Temperley-Lieb quotient H_inf(q)/rad = TL_inf(q), NOT H_inf(q)
   itself. (Under the excised convention C every y_lambda was non-zero and N
   collapsed to 0.)"

So the answer is TL, and it is already in the corpus. That is the discipline
working: the bean was opened without running the grep first.

WHAT THAT DOES NOT SETTLE, AND IS THE POINT OF THIS PROBE. The GNS construction
quotients by the radical of the TRACE form. It says nothing about whether the
Q_beta ansatz's functional survives the quotient -- and a functional descends to
H/J only if it ANNIHILATES J. So the real question is not which algebra, but
whether `net` is a functional on the algebra the corpus picked. Measured here:

  * tr_M at z_D annihilates the (1,1,1) block          -> the trace descends
  * the augmentation sigma -> q annihilates it         -> the COUNIT descends
  * `net`, the coordinate sum, does NOT                -> it does not descend

Consequence, and it is sharp: the Q_beta ansatz evaluates a functional that is
not defined on the space the framework's own GNS proof says the theory lives in.
And it WOULD BE defined there if it were the counit the corpus calls it. The
step-8 mislabelling (`epsNPq` is the coordinate sum, not the Frobenius counit)
is therefore not cosmetic -- it is exactly what makes the ansatz incompatible
with convention D's GNS structure.

A SECOND FINDING, INTERNAL TO THAT BLOCK. `prop:algebraic-gns-embedding` states
a FAITHFUL *-representation of H_inf(q). Its own proof establishes the embedding
of H_inf(q)/rad and qualifies faithfulness as holding "in the trace-quotient".
Under convention D the radical is nonzero, so the representation is NOT faithful
on H_inf(q) and the statement over-claims relative to its proof. Verified here at
n = 3 by exhibiting a nonzero element the trace form cannot see.

NO fit, NO wiring, no value proposed. Scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, LEFT, L, R, ONE, basis_vec, vec, net, reg_char, length,
)

set_compute_dps(50)

Z = sp.Symbol("z")
Z_C = sp.sqrt(q) / (q + 1)
Z_D = q**3 / (q**2 + 1)


def main() -> int:
    w = WitnessBuilder("qbeta-which-algebra-decay-channel", engine="sympy+mpmath")
    w.set_description(
        "The corpus's GNS proof already places the convention-D theory in the "
        "Temperley-Lieb quotient. Measured here: the trace and the augmentation "
        "descend to it; the coordinate sum `net` that the Q_beta ansatz "
        "evaluates does not."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- the (1,1,1) central idempotent -------------------------------------
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI, DIMS = [chi3, chi21, chi111], [1, 2, 1]
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    cf = sp.symbols("c0 c1 c2")
    gen = sum((cf[i] * centre[i] for i in range(3)), sp.zeros(N, 1))
    sol = sp.solve([sp.Eq(CHI[mu](gen), DIMS[mu] if mu == 2 else 0)
                    for mu in range(3)], cf, dict=True)
    check("the_1cubed_central_idempotent_is_unique", len(sol) == 1)
    e111 = sp.simplify(sum((sol[0][cf[i]] * centre[i] for i in range(3)),
                           sp.zeros(N, 1)))
    Le = sum((e111[i] * LEFT[i] for i in range(N)), sp.zeros(N, N))
    check("it_is_idempotent_and_nonzero",
          sp.simplify(Le * e111 - e111).is_zero_matrix
          and not sp.simplify(e111).is_zero_matrix)

    # J_(1,1,1) = e·H is 1-dimensional (the block is 1x1), so J = span{e}.
    J = [sp.simplify(Le * basis_vec(i)) for i in range(N)]
    Jm = sp.Matrix.hstack(*J)
    check("the_1cubed_ideal_is_one_dimensional",
          len(Jm.columnspace()) == 1,
          "(the block is 1x1, so J = span{e} and descent is a single test)")

    # ---- who descends? -------------------------------------------------------
    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]

    def tr_M(v, zval):
        return sp.simplify(sum(v[i] * TR[i] for i in range(N)).subs(Z, zval))

    check("the_TRACE_descends_under_D",
          all(sp.simplify(tr_M(j, Z_D)) == 0 for j in J),
          "(tr_M^{z_D} annihilates the whole ideal — this IS the corpus's "
          "Temperley-Lieb radical, at n=3)")
    check("the_trace_does_NOT_descend_under_C_CONTROL",
          any(sp.simplify(tr_M(j, Z_C)) != 0 for j in J),
          "(matches the GNS proof's parenthetical: under the excised "
          "convention C the radical collapses to 0)")
    check("the_AUGMENTATION_descends",
          all(sp.simplify(chi3(j)) == 0 for j in J),
          "(sigma -> q is the (3)-block character and kills every other "
          "block's ideal — so the Frobenius counit IS a functional on TL)")
    check("the_COORDINATE_SUM_does_NOT_descend",
          any(sp.simplify(net(j)) != 0 for j in J),
          f"(net(e) = {sp.factor(sp.simplify(net(e111)))} != 0)")

    # ---- what that costs the Q_beta ansatz ----------------------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)).is_zero_matrix)
    check("delta_has_a_nonzero_1cubed_component",
          not sp.simplify(Le * delta).is_zero_matrix,
          "(so the non-descent is not vacuous here — the ansatz's own element "
          "meets the ideal)")
    check("epsNPq_is_NOT_well_defined_on_the_quotient",
          sp.simplify(net(delta) - net(delta - Le * delta)) != 0,
          "(two representatives of the same TL class, two different values)")

    # ---- the proposition over-claims relative to its own proof ---------------
    check("the_GNS_representation_is_NOT_faithful_on_H_3_under_D",
          all(sp.simplify(tr_M(sp.simplify(Le * basis_vec(i)), Z_D)) == 0
              for i in range(N))
          and not sp.simplify(e111).is_zero_matrix,
          "(a NONZERO element the trace form cannot see; "
          "`prop:algebraic-gns-embedding` states a faithful embedding of "
          "H_inf(q), while its own proof qualifies faithfulness as holding "
          "'in the trace-quotient')")

    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    w.add_data("e_1cubed_coords", [str(sp.factor(sp.simplify(e111[i])))
                                   for i in range(N)])
    w.add_data("net_of_e_1cubed_symbolic",
               str(sp.factor(sp.simplify(net(e111)))))
    w.add_data("net_of_e_1cubed_at_q0", fmt(ev(sp.simplify(net(e111)))))
    w.add_data("net_of_delta", fmt(ev(sp.simplify(net(delta)))))
    w.add_data("net_of_projected_delta",
               fmt(ev(sp.simplify(net(delta - Le * delta)))))
    w.add_data("corpus_answer",
               "Temperley-Lieb quotient — already stated in "
               "prf:algebraic-gns-embedding; qou-879g was premature")
    w.add_data("markov_convention", "D canonical, C carried as control")
    w.add_data("assertion_notes", notes)

    verdict = (
        "ANSWERED FROM THE CORPUS, not by a new decision: "
        "prf:algebraic-gns-embedding already states that under production "
        "convention D the radical of the Markov trace is the >=3-row blocks -- "
        "the Temperley-Lieb radical -- and the GNS space is TL_inf(q), NOT "
        "H_inf(q). So qou-879g was premature and is answered TL. Verified here "
        "at n=3: the trace annihilates the (1,1,1) ideal under D and does not "
        "under C, exactly as that proof's parenthetical says. "
        "WHAT THAT EXPOSES: descent to a quotient is annihilation of the ideal, "
        "and the augmentation sigma -> q annihilates it while the COORDINATE "
        "SUM does not. Delta has a nonzero (1,1,1) component, so `epsNPq` takes "
        "different values on two representatives of one TL class -- the Q_beta "
        "ansatz evaluates a functional that is NOT defined on the space the "
        "framework's own GNS proof places the theory in. It would be defined "
        "there if it were the counit the corpus calls it, so the step-8 "
        "mislabelling is the obstruction, not a naming quibble. "
        "SEPARATELY: prop:algebraic-gns-embedding states a FAITHFUL embedding "
        "of H_inf(q) while its proof establishes it for H_inf/rad and qualifies "
        "faithfulness 'in the trace-quotient'; under D the radical is nonzero, "
        "witnessed here by a nonzero element the trace form cannot see, so the "
        "statement over-claims relative to its own proof. Scope-(a)."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
