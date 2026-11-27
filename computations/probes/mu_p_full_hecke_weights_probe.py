#!/usr/bin/env python3
"""mu-p residual: projector insertions on 4_1 under the FULL Ocneanu trace on H_3 (symbolic z).

Bean qou-6gf9 (C3 of the compute-accuracy epic qou-myts). Follows PR #9445
(``mu_p_projector_insertion_w_order_probe.py``), which used the SU(2) Markov
weights (y_111 = 0).  Companion Lean:
``folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuPFullHeckeWeights.lean``.

Question
--------
Does any covariant observable of photon-projector insertions
``e_i = (q - s_i)/[2]_q`` into ``4_1 = (s1 s2^-1)^2`` have vanishing O(w^0) and
O(w^1) terms and a FORCED w^2 coefficient, once the Markov trace runs over all of
H_3 with y_111 != 0?  The Ocneanu parameter z is kept SYMBOLIC.  Convention D
(owner ruling 2026-08-15) is y_111 = 0 and stays canonical; this is a comparison
family only.  No value of z is chosen to fit anything: choosing z because it
fits would be selection against the target.

Method (all EXACT; sympy over Q(q, z), then exact power series)
-----------------------------------------------------------------
1. Solve tr(1) = 1, tr(s1) = z, tr(s1 s2) = z^2 for the weights y_3, y_21,
   y_111 in Q(q, z).  (H_3 has 3 classes and 3 irreducibles.)
2. Correlator = (y_21 tr_3(e..word) + y_111 chi_sign(e..word)) / tr_M(4_1).
   e_i kills (3) and is 1 on (111); chi_sign(4_1) = 1.
3. Observables (same four as #9445): pair <e1>+<e2>, S1 (all singles),
   D (all doubles), C (connected doubles).  Closed forms in Q(q, z).
4. Bar-covariant z families, q = e^h:
   general  z = sinh h (1 + 2c/h + 2 k1 h + 2 k3 h^3)
   SU(N)    z = q^N/[N]_q = sinh h (1 + coth(N h)),  i.e. c = 1/(2N),
            k1 = N/6, k3 = -N^3/90.
   Taylor to h^4 (= w^2), check odd orders vanish, convert with
   h^2 = w - w^2/12 + O(w^3).

The only numerics are 80-dps mpmath evaluations in the comparison section.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402

q, z = sp.symbols("q z")
h, N, c, k1, k3 = sp.symbols("h N c k1 k3")

I3 = sp.eye(3)
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, q - 1 / q]])
A2 = sp.Matrix([[0, 1, 0], [1, q - 1 / q, 0], [0, 0, q]])
A2I = A2.inv()
TWO_Q = q + 1 / q
E1 = (q * I3 - A1) / TWO_Q
E2 = (q * I3 - A2) / TWO_Q
WORD = [A1, A2I, A1, A2I]
PROJ = {"e1": E1, "e2": E2}


def log(msg: str) -> None:
    print(msg, flush=True)


def solve_weights() -> dict:
    y3, y21, y111 = sp.symbols("y3 y21 y111")

    def tr(m, triv, sgn):
        return y3 * triv + y21 * (m.trace() - triv) + y111 * sgn

    eqs = [tr(I3, 1, 1) - 1, tr(A1, q, -1 / q) - z, tr(A1 * A2, q**2, 1 / q**2) - z**2]
    sol = sp.solve(eqs, [y3, y21, y111], dict=True)[0]
    return {"y3": sp.factor(sol[y3]), "y21": sp.factor(sol[y21]), "y111": sp.factor(sol[y111])}


def main() -> int:
    W = solve_weights()
    Y3, Y21, Y111 = W["y3"], W["y21"], W["y111"]
    log(f"  y3   = {Y3}\n  y21  = {Y21}\n  y111 = {Y111}")
    su2_roots = sp.solve(sp.numer(sp.together(Y111)), z)
    z_su2 = q**3 / (q**2 + 1)
    su2_is_root = any(sp.simplify(r - z_su2) == 0 for r in su2_roots)
    # Markov property spot-check beyond the defining equations: tr(s1^-1 s2) = tr(s1^-1) z
    def trw(m, triv, sgn):
        return sp.simplify(Y3 * triv + Y21 * (m.trace() - triv) + Y111 * sgn)
    A1I = A1.inv()
    markov_extra = sp.simplify(trw(A1I * A2, 1, 1) - trw(A1I, 1 / q, -q) * z) == 0

    word = sp.prod(WORD, start=I3)
    Z = sp.factor(Y3 + Y21 * (word.trace() - 1) + Y111)

    def corr(ins: dict) -> sp.Expr:
        m = sp.eye(3)
        for j, letter in enumerate(WORD):
            for e in ins.get(j, []):
                m = m * e
            m = m * letter
        return sp.factor(sp.simplify((Y21 * m.trace() + Y111) / Z))

    singles = {(n, k): corr({k: [e]}) for k in range(4) for n, e in PROJ.items()}
    slot_indep = all(sp.simplify(singles[(n, k)] - singles[(n, 0)]) == 0 for n in PROJ for k in range(4))
    s1 = sum(singles.values())
    d_full = 0
    c_conn = 0
    keys = list(singles)
    for a in keys:
        for b in keys:
            if a[1] > b[1]:
                continue
            ins: dict = {}
            ins.setdefault(a[1], []).append(PROJ[a[0]])
            ins.setdefault(b[1], []).append(PROJ[b[0]])
            cc = corr(ins)
            d_full += cc
            c_conn += cc - singles[a] * singles[b]
    obs = {
        "pair": sp.factor(singles[("e1", 0)] + singles[("e2", 0)]),
        "S1": sp.factor(s1),
        "D": sp.factor(d_full),
        "C": sp.factor(c_conn),
    }
    log("  closed forms in Q(q,z) done")
    factor_z_minus_q = all(sp.simplify(v.subs(z, q)) == 0 for v in obs.values())
    at_one = {k: sp.factor(v.subs(q, 1)) for k, v in obs.items()}
    # SU(2) cross-check against #9445's pair correlator
    s_ = q + 1 / q
    pair_su2_ok = sp.simplify(obs["pair"].subs(z, z_su2) - (s_**4 - 6 * s_**2 + 7) / (s_**4 - 5 * s_**2 + 5)) == 0

    # ---- general bar-covariant family, exact truncated series --------------
    order = 9
    sh = sp.series(sp.sinh(h), h, 0, order).removeO()
    qh = sp.series(sp.exp(h), h, 0, order).removeO()
    zg = sp.expand(sh * (1 + 2 * c / h + 2 * k1 * h + 2 * k3 * h**3))
    gen = {}
    odd_vanish = True
    for k, v in obs.items():
        num, den = sp.fraction(sp.together(v))
        nn = sp.expand(num.subs({z: zg, q: qh}))
        dd = sp.expand(den.subs({z: zg, q: qh}))
        ser = sp.series(nn / dd, h, 0, 5).removeO()
        cs = [sp.factor(ser.coeff(h, i)) for i in range(5)]
        odd_vanish &= sp.simplify(cs[1]) == 0 and sp.simplify(cs[3]) == 0
        gen[k] = (cs[0], sp.factor(cs[2]), sp.factor(cs[4] - cs[2] / 12))
        log(f"  general family {k}: done")
    sun = {k: tuple(sp.factor(x.subs({c: 1 / (2 * N), k1: N / 6, k3: -N**3 / 90})) for x in v)
           for k, v in gen.items()}
    at_two = {k: [sp.nsimplify(x.subs(N, 2)) for x in v] for k, v in sun.items()}
    pr9445 = {"S1": [-4, 80, -812], "D": [-11, 217, sp.Rational(-8811, 4)],
              "C": [-21, 617, sp.Rational(-41051, 4)], "pair": [-1, 20, -203]}
    su2_table_ok = all(at_two[k] == pr9445[k] for k in pr9445)

    # O(1)=O(w)=0 loci in the SU(N) family
    loci = {k: sp.solve([v[0], v[1]], N, dict=True) for k, v in sun.items()}
    loci_n = {k: sorted({sp.nsimplify(s[N]) for s in sol}) for k, sol in loci.items()}
    only_degenerate = all(set(v) <= {1, -1} for v in loci_n.values())
    delta = sp.factor(sun["D"][1] * sun["S1"][2] - sun["S1"][1] * sun["D"][2])
    mat = sp.Matrix([[1, 0, 0], list(sun["S1"]), list(sun["D"]), list(sun["C"])]).T
    rank_generic = mat.rank(simplify=True)

    # general family: O(1)=O(w)=0 for pair pins c and k1; O(w^2) left free in k3
    p0, p1, p2 = gen["pair"]
    c_sol = sp.solve(p0, c)
    k1_sol = sp.solve(p1.subs(c, c_sol[0]), k1)
    w2_free = sp.factor(p2.subs({c: c_sol[0], k1: k1_sol[0]}))
    w2_is_deformation = sp.simplify(w2_free - 2 * (k3 + sp.Rational(1, 90))) == 0

    # ---- comparison section (empirical inputs live ONLY here) -------------
    q_p = q_at(80)
    q_mu = q_muon_at(80)
    alpha = 1 / mp.mpf(_codata.codata("inverse fine-structure constant").value_str)
    target = -3 * alpha / (4 * mp.pi)
    k3_needed = (45 * target - 1) / 90
    delta_k3_needed = k3_needed + mp.mpf(1) / 90

    print("=" * 78)
    print(" mu-p: projector insertions on 4_1, full Ocneanu trace on H_3, symbolic z")
    print("=" * 78)
    print(f"  tr_M(4_1) = {Z}")
    for k, v in obs.items():
        print(f"  {k:5s} = {v}")
        print(f"         q=1: {at_one[k]}")
    print(f"  every observable vanishes at z = q: {factor_z_minus_q}")
    for k, v in sun.items():
        print(f"  SU(N) {k:5s} (O1, Ow, Ow2) = {v};  O1=Ow=0 at N in {loci_n[k]}")
    print(f"  Delta(N) = {delta}; rank over Q(N) = {rank_generic}")
    print(f"  general family: O1=0 -> c = {c_sol}; then Ow=0 -> k1 = {k1_sol}; Ow2 = {w2_free}")
    print(f"  [comparison] k3 that would hit -3a/4pi: {mp.nstr(k3_needed, 20)} "
          f"(= trivial-trace value -1/90 shifted by {mp.nstr(delta_k3_needed, 12)})")

    wb = WitnessBuilder("mu-p-full-hecke-weights", engine="sympy+mpmath")
    wb.set_description(
        "Photon-projector insertion correlators on 4_1 = (s1 s2^-1)^2 under the full Ocneanu Markov trace "
        "on H_3 with symbolic z (y_111 != 0; comparison family to convention D). Exact Q(q,z) closed forms, "
        "SU(N) and general bar-covariant w-Taylor data, and the non-forcing of the w^2 coefficient (qou-6gf9)."
    )
    wb.add_data("weights", {k: str(v) for k, v in W.items()})
    wb.add_data("observables_Qqz", {k: {"closed_form": str(v), "at_q_eq_1": str(at_one[k])}
                                     for k, v in obs.items()})
    wb.add_data("trM_41", str(Z))
    wb.add_data("general_family_w_taylor", {k: [str(x) for x in v] for k, v in gen.items()})
    wb.add_data("suN_family_w_taylor", {k: [str(x) for x in v] for k, v in sun.items()})
    wb.add_data("suN_O1_Ow_zero_loci", {k: [str(x) for x in v] for k, v in loci_n.items()})
    wb.add_data("suN_delta", str(delta))
    wb.add_data("general_pair_w2_on_O1_Ow_zero", str(w2_free))
    wb.add_data("comparison", {
        "q_p": fmt(q_p),
        "target_w2_coeff_minus_3alpha_over_4pi": fmt(target),
        "k3_that_would_hit_target": fmt(k3_needed),
        "note": "alpha is CODATA-2022 here; diagnostic only. Choosing k3 (i.e. z) to hit it would be "
                "selection against the target and is not done. Never an input to the algebra or the Lean.",
    })
    wb.add_assertion(name="weights_are_ocneanu_and_su2_point_kills_y111",
                     computed=str(su2_is_root and markov_extra), expected="True",
                     source="exact sympy over Q(q,z)")
    wb.add_assertion(name="su2_specialisation_reproduces_pr9445",
                     computed=str(pair_su2_ok and su2_table_ok and slot_indep), expected="True",
                     source="closed form and Taylor table of PR #9445")
    wb.add_assertion(name="every_observable_has_factor_z_minus_q",
                     computed=str(factor_z_minus_q), expected="True", source="exact Q(q,z)")
    wb.add_assertion(name="bar_covariant_families_are_even_in_h",
                     computed=str(odd_vanish), expected="True", source="exact series to h^4")
    wb.add_assertion(name="suN_O1_Ow_vanish_only_at_degenerate_N_pm1",
                     computed=str(only_degenerate), expected="True", source="solve over Q(N)")
    wb.add_assertion(name="suN_coefficient_matrix_rank3",
                     computed=str(rank_generic), expected="3", source="rank over Q(N)")
    wb.add_assertion(name="general_family_w2_equals_twice_k3_deformation_of_trivial_trace",
                     computed=str(w2_is_deformation), expected="True",
                     source="O1=Ow=0 pins c=1/2, k1=1/6 (the z=q values); Ow2 = 2(k3 + 1/90)")
    out_path = wb.save(q0_comparison(muon=fmt(q_mu), proton=fmt(q_p),
                                     reason="algebra is pin-free; comparison evaluates alpha only", dps=80))
    ok = all(a.passed for a in wb.assertions)
    print(f"\n  Witness written -> {out_path} (assertions={len(wb.assertions)}, allPassed={ok})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
