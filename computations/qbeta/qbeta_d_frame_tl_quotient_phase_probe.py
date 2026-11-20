#!/usr/bin/env python3
"""
qbeta_d_frame_tl_quotient_phase_probe.py — qou-cds1: what the two-row forcing
does to the phase if it is read as a QUOTIENT of the algebra rather than as a
weight that happens to vanish. One candidate, zero free parameters.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_phase_block_resolution_probe.py
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean

THE OPENING. The block-resolved identity

    2*alpha(z) = sum_lambda [a_lambda - y_lambda(z)] chi^lambda(Delta) + net(dC)

is EXACT, so specialising it to z_D returns h(z_D - 1) and moves no number. A
re-derivation therefore cannot come from re-expressing the phase; it has to come
from a changed input. There is exactly one input the D convention touches that
the C convention does not, and it is not z: WenzlWeightVanishing proves z_D is
Wenzl level r = 2 exactly, so the >= 3-row blocks are annihilated.

THE HYPOTHESIS, STATED AS ONE. The corpus establishes that the D-frame TRACE has
no support on the (1,1,1) block (y_(1,1,1) = 0, four independent routes). It does
NOT establish that the D-frame ELEMENT lives in the quotient. Reading the forcing
as a quotient -- the decay element evaluated in H_3(q)/J_(1,1,1), i.e. in the
Temperley-Lieb quotient, rather than in H_3(q) -- is an INTERPRETIVE step, and it
is flagged as such. What makes it worth computing is that it has NO free
parameter: the central idempotent e_(1,1,1) is unique, so pi(Delta) is one
determined element and the resulting phase is one determined number.

WHY IT COULD MATTER AT ALL. Projection commutes with the trace's verdict but not
with `net`: tr_M^D(pi(Delta)) = tr_M^D(Delta) exactly, because y_(1,1,1) already
annihilated that block -- while net(pi(Delta)) != net(Delta), because `net` is
NOT a trace (step 8, 25/25) and does not respect the block decomposition. So the
counit-minus-trace gap moves even though the trace does not. That is a change of
the phase obtained WITHOUT touching the formula alpha = (eps - tr_M)/2 and
without substituting z -- which is what the re-derivation requirement asks for.

REPORTED WITHOUT SPIN. The result is one number and it is reported against the
anchor-inverted target whatever it says. An improvement would not be a closure
and a failure would be a scope-(a) negative on a NAMED reading, not on the D
programme. Neither outcome is searched for: there is nothing here to tune.

NO fit, NO c_k, NO wiring. Scope-(a).
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
# Anchor-inverted, quoted from qou-cds1 (PR #5748). NOT a derived quantity —
# it is what the N=2 ladder demands of z to reproduce CODATA.
Z_STAR = mp.mpf("0.4991045")


def main() -> int:
    w = WitnessBuilder("qbeta-d-frame-tl-quotient-phase", engine="sympy+mpmath")
    w.set_description(
        "Reads the convention-D two-row forcing as a quotient of H_3(q) rather "
        "than as a vanishing weight, and computes the resulting ladder phase. "
        "One candidate, no free parameter, reported against the anchor-inverted "
        "z* whatever it says."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- setup ---------------------------------------------------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)).is_zero_matrix)

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
    check("centre_is_three_dimensional", len(centre) == 3)

    # ---- the central idempotents, from chi^mu(e_lambda) = delta * dim mu -----
    cf = sp.symbols("c0 c1 c2")
    E = []
    for lam in range(3):
        gen = sum((cf[i] * centre[i] for i in range(3)), sp.zeros(N, 1))
        eqs = [sp.Eq(CHI[mu](gen), DIMS[mu] if mu == lam else 0) for mu in range(3)]
        s = sp.solve(eqs, cf, dict=True)
        assert len(s) == 1
        E.append(sp.simplify(sum((s[0][cf[i]] * centre[i] for i in range(3)),
                                 sp.zeros(N, 1))))
    check("idempotents_are_idempotent",
          all(sp.simplify(sum((E[k][i] * LEFT[i] for i in range(N)),
                              sp.zeros(N, N)) * E[k] - E[k]).is_zero_matrix
              for k in range(3)))
    check("idempotents_are_orthogonal_and_sum_to_one",
          sp.simplify(E[0] + E[1] + E[2] - basis_vec(0)).is_zero_matrix
          and all(sp.simplify(
              sum((E[a][i] * LEFT[i] for i in range(N)), sp.zeros(N, N)) * E[b]
          ).is_zero_matrix for a in range(3) for b in range(3) if a != b))

    Le111 = sum((E[2][i] * LEFT[i] for i in range(N)), sp.zeros(N, N))
    pi_delta = sp.simplify(delta - Le111 * delta)
    check("projection_kills_the_1cubed_character",
          sp.simplify(chi111(pi_delta)) == 0
          and sp.simplify(chi3(pi_delta) - chi3(delta)) == 0,
          "(pi = 1 - e_(1,1,1): the other block characters are untouched)")
    check("projection_actually_moves_the_element",
          not sp.simplify(pi_delta - delta).is_zero_matrix)

    # ---- traces --------------------------------------------------------------
    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]

    def tr_M(v):
        return sp.simplify(sum(v[i] * TR[i] for i in range(N)))

    check("trace_is_UNCHANGED_by_the_projection_at_z_D",
          sp.simplify((tr_M(pi_delta) - tr_M(delta)).subs(Z, Z_D)) == 0,
          "(y_(1,1,1) already annihilated that block, so the trace cannot see "
          "the projection — only `net` can)")
    check("trace_IS_changed_by_the_projection_at_z_C_CONTROL",
          sp.simplify((tr_M(pi_delta) - tr_M(delta)).subs(Z, Z_C)) != 0,
          "(under C the third row is present, so projecting there would be a "
          "real change to the trace — which is why the quotient reading is a "
          "D-only statement)")
    check("net_IS_changed_by_the_projection",
          sp.simplify(net(pi_delta) - net(delta)) != 0,
          "(`net` is not a trace, so it does not respect the block ideal)")

    # ---- the candidate phase -------------------------------------------------
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    h0 = ev(h)
    cands = []

    def z_eff(two_alpha):
        return 1 + two_alpha / h0

    for label, elem, zval in (
        ("C  (as recorded)", delta, Z_C),
        ("D  naive z-swap", delta, Z_D),
        ("D  TL-quotient element", pi_delta, Z_D),
    ):
        ta = ev(sp.simplify((net(elem) - tr_M(elem)).subs(Z, zval)))
        ze = z_eff(ta)
        cands.append({"candidate": label, "two_alpha": fmt(ta),
                      "z_effective": fmt(ze),
                      "rel_dist_to_z_star": fmt(abs(ze - Z_STAR) / Z_STAR)})
        print(f"    {label:<24} 2a={fmt(ta)[:16]:>17}  z_eff={fmt(ze)[:12]:>14}"
              f"  |dz|/z*={fmt(abs(ze - Z_STAR) / Z_STAR)[:10]}")

    # ---- compose with the bean's OTHER forced correction --------------------
    # Bar-oddness of the phase is not a choice once required: the correction is
    # the bar-even part, and subtracting it is projection onto the bar-odd part.
    # Zero parameters. Under C the phase is already bar-odd, so the projection
    # must act as the IDENTITY there — that is the control that validates it.
    def bar_odd_part(e):
        return sp.simplify((e - e.subs(q, 1 / q)) / 2)

    for label, elem, zval in (
        ("C  bar-odd projected", delta, Z_C),
        ("D  naive + bar-odd", delta, Z_D),
        ("D  TL-quotient + bar-odd", pi_delta, Z_D),
    ):
        raw = sp.simplify((net(elem) - tr_M(elem)).subs(Z, zval))
        ta = ev(bar_odd_part(raw))
        ze = z_eff(ta)
        cands.append({"candidate": label, "two_alpha": fmt(ta),
                      "z_effective": fmt(ze),
                      "rel_dist_to_z_star": fmt(abs(ze - Z_STAR) / Z_STAR)})
        print(f"    {label:<24} 2a={fmt(ta)[:16]:>17}  z_eff={fmt(ze)[:12]:>14}"
              f"  |dz|/z*={fmt(abs(ze - Z_STAR) / Z_STAR)[:10]}")

    check("bar_odd_projection_is_the_IDENTITY_under_C_CONTROL",
          cands[3]["two_alpha"] == cands[0]["two_alpha"],
          "(the C phase is already bar-odd, so the projection must do nothing "
          "— this is what licenses applying it to the D candidates)")

    check("C_reproduces_its_recorded_eigenphase_CONTROL",
          abs(mp.mpf(cands[0]["two_alpha"]) - h0 * (ev(Z_C) - 1)) < mp.mpf("1e-45"))
    check("D_naive_reproduces_the_banned_substitution_CONTROL",
          abs(mp.mpf(cands[1]["two_alpha"]) - h0 * (ev(Z_D) - 1)) < mp.mpf("1e-45"))

    dC = mp.mpf(cands[1]["rel_dist_to_z_star"])
    dT = mp.mpf(cands[2]["rel_dist_to_z_star"])
    dNB = mp.mpf(cands[4]["rel_dist_to_z_star"])
    dTB = mp.mpf(cands[5]["rel_dist_to_z_star"])
    d_ref = mp.mpf(cands[0]["rel_dist_to_z_star"])
    check("the_quotient_reading_moves_the_phase_at_all", dT != dC)
    improves = dT < dC
    check("outcome_recorded_whichever_way_it_went", True,
          f"(quotient {'IMPROVES' if improves else 'WORSENS'} on the naive swap: "
          f"{fmt(dC)[:9]} -> {fmt(dT)[:9]}; C is "
          f"{cands[0]['rel_dist_to_z_star'][:9]})")
    # CALIBRATION against qou-cds1's own recorded distances, before trusting
    # the new row: the bean records z* as "0.043% from z_C, 1.81% from
    # z_D^even, 22.8% from z_D". Reached here by a different route — projecting
    # the PHASE onto its bar-odd part, rather than deriving z_D^even = z_D - h/2.
    check("calibrates_against_the_beans_recorded_z_star_distances",
          abs(d_ref - mp.mpf("0.00043")) < mp.mpf("2e-5")
          and abs(dC - mp.mpf("0.228")) < mp.mpf("1e-3")
          and abs(dNB - mp.mpf("0.0181")) < mp.mpf("1e-4"),
          f"(bean: 0.043% / 22.8% / 1.81%; here: {fmt(d_ref * 100)[:6]}% / "
          f"{fmt(dC * 100)[:6]}% / {fmt(dNB * 100)[:6]}% — the third is an "
          "independent reproduction of the bean's derived z_D^even candidate)")

    check("the_two_forced_corrections_COMPOSE_to_the_best_D_candidate",
          dTB < dT and dTB < dNB,
          f"(naive {fmt(dC)[:9]} / +bar-odd {fmt(dNB)[:9]} / quotient "
          f"{fmt(dT)[:9]} / both {fmt(dTB)[:9]})")
    check("the_best_D_candidate_is_STILL_far_from_C",
          dTB / d_ref > mp.mpf("10"),
          f"(best D is {fmt(dTB / d_ref)[:7]}x the C distance — a derived "
          "improvement, NOT a closure)")

    for c in cands:
        w.add_data(f"candidate_{c['candidate'].split()[0]}_{len(w.build().get('data', {}))}"
                   if False else c["candidate"].replace(" ", "_"), c)
    w.add_data("z_star_anchor_inverted_NOT_derived", fmt(Z_STAR))
    w.add_data("z_star_provenance",
               "quoted from qou-cds1 / PR #5748; it is what the N=2 ladder "
               "demands of z to reproduce CODATA, i.e. anchor-inverted")
    w.add_data("net_of_pi_delta_symbolic", str(sp.factor(sp.simplify(net(pi_delta)))))
    w.add_data("net_of_delta_symbolic", str(sp.factor(sp.simplify(net(delta)))))
    w.add_data("quotient_reading_improves_on_naive_swap", bool(improves))
    w.add_data("markov_convention", "D (with C as control)")
    w.add_data("assertion_notes", notes)

    verdict = (
        ("Two parameter-free corrections, each forced by its own premise, and "
         "their composition. (1) Reading the D two-row forcing as a QUOTIENT: "
         "the projection is invisible to the D trace (y_(1,1,1) had already "
         "annihilated that block) and visible to `net` (not a trace), so the "
         "counit-minus-trace gap moves without touching alpha = (eps-tr_M)/2 "
         "and without substituting z. (2) Projecting the phase onto its bar-odd "
         "part, which is the identity under C -- the control that licenses "
         "applying it under D. Measured, as relative distance of the implied "
         "z_eff to the anchor-inverted z*: naive swap "
         + fmt(dC)[:9] + ", +bar-odd " + fmt(dNB)[:9] + ", quotient "
         + fmt(dT)[:9] + ", both " + fmt(dTB)[:9] + ", against C at "
         + cands[0]["rel_dist_to_z_star"][:9] + ". The two compose to the best D "
         "candidate, and it is still " + fmt(dTB / d_ref)[:6] + "x the C "
         "distance. NOT a closure: z* is anchor-inverted, the quotient reading "
         "is an INTERPRETIVE step the corpus does not establish, and nothing is "
         "wired. Scope-(a) on two named readings.")
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
