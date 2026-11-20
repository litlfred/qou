#!/usr/bin/env python3
"""Option E, formalize-first: WHICH class does functional-independence force?

Bean `qou-99qc`. The Lean
(`QOU/QBeta/AdmissibleAgreementDeterminesClass.lean`, sorry-free) proves the
narrowing: an admissible trace sees `Delta` only through
`(chi_(3)(Delta), chi_(2,1)(Delta))`, so demanding that TWO INDEPENDENT
admissible functionals return the same value is two equations in two unknowns
and the class is FORCED rather than fitted. That is a statement about shape.
This probe computes the actual class, and tests it.

THE POINT OF DOING IT THIS WAY. A free `Delta` in `H_3(q)` reproduces any
target, because a functional there is surjective -- so a naive Option E search
is a six-parameter fit against one anchor and could never be a derivation. The
narrowing above removes all six parameters. What is left is a single class,
which either is or is not realised by a legitimate element; no search occurs.

WHAT IS POSITED, stated plainly. Functional-independence is a REQUIREMENT this
probe imposes, not a theorem of the framework: nothing compels a physical
quantity to be invariant under swapping the augmentation for the Markov trace,
any more than an operator's trace must equal its determinant. The requirement is
adopted because it is the only condition that removes the arbitrary choice of a
point in the 2-dimensional admissible space, and because it is falsifiable.

PRECISION. Exact sympy over Q(q) throughout; the pin enters only at readout, as
an exact Rational from the 50-digit proton string. No float64 arithmetic.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate import constants as CONST  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, N, basis_vec, length, q, h, reg_char,
)


def main() -> int:
    checks: list[dict] = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return bool(ok)

    print(__doc__.splitlines()[0]); print()
    ok = True
    Z = sp.Symbol("z")
    Z_D = q**3 / (q**2 + 1)

    # ---- the character basis of the admissible trace space ---------------
    chi_3 = sp.Matrix([[q ** length(BASIS[i]) for i in range(N)]])
    chi_111 = sp.Matrix([[(-1 / q) ** length(BASIS[i]) for i in range(N)]])
    reg = sp.Matrix([[sp.simplify(reg_char(basis_vec(i))) for i in range(N)]])
    chi_21 = sp.simplify((reg - chi_3 - chi_111) / 2)

    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]
    co_trD = sp.Matrix([[sp.simplify(t.subs(Z, Z_D)) for t in TR]])

    # ---- express tr_M(z_D) = alpha*chi_(3) + beta*chi_(2,1) --------------
    al, be = sp.symbols("alpha beta")
    sols = sp.solve([sp.Eq(sp.simplify(al * chi_3[i] + be * chi_21[i]), co_trD[i])
                     for i in range(N)], [al, be], dict=True)
    ok &= chk("trD_decomposes_in_the_admissible_character_basis",
              len(sols) == 1,
              f"unique solution found: {len(sols)} (overdetermined 6 eqns, "
              "2 unknowns -- consistency is itself the admissibility check)")
    A = sp.simplify(sols[0][al]); B = sp.simplify(sols[0][be])
    print(f"      tr_M(z_D) = ({sp.factor(A)})*chi_(3) + ({sp.factor(B)})*chi_(2,1)")

    ok &= chk("beta_is_nonzero_so_the_system_is_nondegenerate", sp.simplify(B) != 0,
              f"beta = {sp.factor(B)} != 0 -- this is the Lean hypothesis "
              "`hb : b2 != 0`; without it the class is NOT forced")

    # ---- THE SHARP STRUCTURE, symbolic over Q(q) (not at q0) -------------
    ok &= chk("trD_is_NORMALISED_alpha_plus_2beta_equals_one",
              sp.simplify(A + 2 * B - 1) == 0,
              "alpha + 2*beta = 1 exactly. chi_(3)(1)=1 and chi_(2,1)(1)=dim=2, "
              "so BOTH functionals lie on the normalised line -- the admissible "
              "family relevant here is one-parameter, not two")
    ok &= chk("one_minus_alpha_over_beta_is_exactly_two",
              sp.simplify((1 - A) / B - 2) == 0,
              "(1-alpha)/beta = 2 for ALL q. So the forced second coordinate is "
              "exactly 2*T -- and 2 is dim V_(2,1), which is what makes the "
              "condition 'scalar modulo the radical' rather than a fit")

    Delta_S_sym = sp.Matrix([h**2 / 2, -h / 2, -h / 2, 0, 0, 0])
    x_sym = sp.simplify(sp.factor((chi_3 * Delta_S_sym)[0]))
    y_sym = sp.simplify(sp.factor((chi_21 * Delta_S_sym)[0]))
    ok &= chk("chi_21_of_Delta_S_VANISHES_identically_over_Qq", y_sym == 0,
              f"chi_(2,1)(Delta_S) = {y_sym} exactly, while "
              f"chi_(3)(Delta_S) = {x_sym} != 0. Delta_S is supported, modulo "
              "the radical, ENTIRELY in the trivial block")
    ok &= chk("so_the_two_admissible_values_are_ONE_number_rescaled",
              sp.simplify((co_trD * Delta_S_sym)[0] - A * (chi_3 * Delta_S_sym)[0]) == 0,
              "tr_M(z_D)(Delta_S) = alpha * aug(Delta_S) exactly. The +12.470 % "
              "and -43.157 % cells are NOT two independent estimates -- they are "
              "one value scaled by alpha = (q^4+1)/(q^2+1)^2 ~ 0.5054")
    ok &= chk("Delta_S_is_NOT_scalar_modulo_the_radical",
              sp.simplify(y_sym - 2 * x_sym) != 0,
              "b = 2a fails identically, so NO choice of admissible functional "
              "makes the Q-value independent of that choice. Scope-(b): the "
              "invariant is the vanishing of chi_(2,1) on Delta_S")

    # ---- BOTH candidate elements, tested against the condition -----------
    # Delta_L's Markov trace is quadratic in z (2026-08-29 audit). Its block
    # characters are EXTRACTED from two admissible evaluations rather than from
    # a coordinate vector: tr_M at z=q IS chi_(3), and tr_M at z_D is
    # alpha*chi_(3) + beta*chi_(2,1), so chi_(2,1) follows by inversion.
    trL = -(q - 1) * (q + 1) * (q**4 * Z**2 + 2 * q**3 * Z + 2 * q**2
                                - 2 * q * Z + Z**2) / (4 * q**3)
    trS = q**2 / 2 - q * Z - 1 + Z / q + 1 / (2 * q**2)
    resid = {}
    for nm, tr in (("Delta_S", trS), ("Delta_L", trL)):
        aa = sp.simplify(tr.subs(Z, q))
        vv = sp.simplify(tr.subs(Z, Z_D))
        bb = sp.simplify((vv - A * aa) / B)
        resid[nm] = sp.factor(sp.simplify(bb - 2 * aa))
        print(f"      {nm}: chi_(3) = {sp.factor(aa)}")
        print(f"      {nm}: chi_(2,1) = {sp.factor(bb)}")
        print(f"      {nm}: b - 2a  = {resid[nm]}")

    ok &= chk("extraction_reproduces_the_known_chi21_vanishing_on_Delta_S",
              sp.simplify(sp.factor(sp.simplify(
                  (trS.subs(Z, Z_D) - A * trS.subs(Z, q)) / B))) == 0,
              "chi_(2,1)(Delta_S) extracted from the two admissible evaluations "
              "= 0, matching the direct covector computation (calibration: two "
              "independent routes to the same quantity)")

    # the decisive question: does either residual vanish for a PHYSICAL q > 1?
    roots_gt_one = {}
    for nm, r in resid.items():
        num = sp.numer(sp.together(r))
        rs = [sp.N(t, 25) for t in sp.real_roots(sp.Poly(sp.expand(num), q))
              if sp.N(t) > 0]
        roots_gt_one[nm] = [str(t) for t in rs if t > 1]
        print(f"      {nm}: positive real roots = {[str(t)[:12] for t in rs]}")
    ok &= chk("NEITHER_element_is_scalar_mod_radical_for_any_q_greater_than_1",
              all(len(v) == 0 for v in roots_gt_one.values()),
              f"positive roots with q > 1: {roots_gt_one} -- both empty. "
              "Scope-(b): the invariant is a polynomial with no root in the "
              "physical regime")
    ok &= chk("the_q_equals_1_root_is_DEGENERATE_not_a_solution",
              sp.simplify(trS.subs(Z, q).subs(q, 1)) == 0
              and sp.simplify(trL.subs(Z, q).subs(q, 1)) == 0,
              "at q = 1 both elements VANISH (h = 0 makes the proton and "
              "neutron words coincide), so the condition holds there only as "
              "0 = 0 -- it is not a physical solution")

    # ---- the target and the FORCED class ---------------------------------
    q0 = sp.Rational(Q_50_DIGIT_STR)
    m_e = sp.Rational(str(CONST.M_E_MEV))
    Qexp = sp.Rational(str(CONST.Q_NEUTRON_MEV))
    E0 = _qbeta_e0.order_zero_scaled(m_e, q0)
    T = Qexp / E0                      # |eps(Delta)| must equal this

    A0, B0 = sp.simplify(A.subs(q, q0)), sp.simplify(B.subs(q, q0))
    x_forced = T                                  # augmentation is (1, 0)
    y_forced = sp.simplify(T * (1 - A0) / B0)

    def f(e):
        r = sp.Rational(sp.nsimplify(e, rational=True))
        return mp.mpf(r.p) / mp.mpf(r.q)

    print(f"\n      T = Q_codata/E0            = {mp.nstr(f(T), 20)}")
    print(f"      FORCED chi_(3)(Delta)      = {mp.nstr(f(x_forced), 20)}")
    print(f"      FORCED chi_(2,1)(Delta)    = {mp.nstr(f(y_forced), 20)}")

    # ---- what do the two CANDIDATE elements actually give? ---------------
    Delta_S = sp.Matrix([h**2 / 2, -h / 2, -h / 2, 0, 0, 0])
    xS = sp.simplify((chi_3 * Delta_S)[0].subs(q, q0))
    yS = sp.simplify((chi_21 * Delta_S)[0].subs(q, q0))
    print(f"      Delta_S  chi_(3), chi_(2,1) = {mp.nstr(f(xS), 12)}, {mp.nstr(f(yS), 12)}")

    # sign convention: the observable is |eps(Delta)|, so compare magnitudes
    ok &= chk("Delta_S_does_NOT_realise_the_forced_class",
              sp.simplify(sp.Abs(xS) - x_forced) != 0
              or sp.simplify(sp.Abs(yS) - y_forced) != 0,
              f"|chi_(3)(Delta_S)| = {mp.nstr(f(sp.Abs(xS)), 12)} vs forced "
              f"{mp.nstr(f(x_forced), 12)} -- the current element does not "
              "satisfy functional-independence")

    # the augmentation coordinate is the whole story for the first equation:
    # aug(Delta_S) is 12.470% high, so |chi_3(Delta_S)| != T by construction.
    rel_x = sp.simplify((sp.Abs(xS) - x_forced) / x_forced * 100)
    rel_y = sp.simplify((sp.Abs(yS) - y_forced) / y_forced * 100)
    print(f"\n      Delta_S vs forced:  chi_(3) off by {mp.nstr(f(rel_x), 8)} %,"
          f"  chi_(2,1) off by {mp.nstr(f(rel_y), 8)} %")

    ok &= chk("the_chi3_gap_reproduces_the_known_augmentation_error",
              abs(f(rel_x) - mp.mpf("12.470022")) < mp.mpf("0.001"),
              f"chi_(3) gap = {mp.nstr(f(rel_x), 9)} % == the corpus's "
              "+12.470 % augmentation cell (calibration: the forced first "
              "coordinate IS the augmentation target, so this MUST match)")

    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "name": "qbeta-option-e-forced-class",
        "description": (
            "Option E under the formalize-first narrowing. Demanding that both "
            "admissible functionals agree on Delta is two equations in the two "
            "coordinates (chi_(3), chi_(2,1)) an admissible trace can see, so "
            "the class is forced (Lean: AdmissibleAgreementDeterminesClass, "
            "sorry-free). This computes the forced class and finds the current "
            "element Delta_S does NOT realise it -- its chi_(3) coordinate is "
            "12.470 % off, exactly the known augmentation cell. Scope-(a): the "
            "independence requirement is POSITED, not derived; nothing wired."),
        "assertions": checks,
        "trD_in_character_basis": {"alpha": str(sp.factor(A)), "beta": str(sp.factor(B))},
        "forced_class": {
            "T_target": mp.nstr(f(T), 25),
            "chi_3": mp.nstr(f(x_forced), 25),
            "chi_21": mp.nstr(f(y_forced), 25),
        },
        "delta_S": {"chi_3": mp.nstr(f(xS), 25), "chi_21": mp.nstr(f(yS), 25),
                    "chi_3_gap_pct": mp.nstr(f(rel_x), 12),
                    "chi_21_gap_pct": mp.nstr(f(rel_y), 12)},
        "caveats": [
            "Functional-independence is POSITED, not a theorem of the "
            "framework. Nothing compels a physical quantity to be invariant "
            "under swapping the augmentation for the Markov trace.",
            "Does NOT exhibit an element realising the forced class, and does "
            "not claim one exists among legitimate braid-word differences.",
            "Delta_S only for the comparison; Delta_L is a separate element "
            "and qou-avt5's finding that the two differ is untouched.",
        ],
        "related": [
            "QOU.QBeta.AdmissibleAgreement.agreement_determines_class",
            "computations/qbeta/qbeta_admissible_functional_hierarchy_probe.py",
            "docs/audits/2026-09-05-qbeta-functional-decision-options.md",
        ],
        "source": "bean qou-99qc (Option E)",
        "scriptFile": Path(__file__).name,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python+sympy",
        q0_anchor="proton",
        q0_anchor_reason=(
            "The character decomposition and the forced-class formula are exact "
            "over Q(q) and pin-free; q0 enters only to evaluate the target "
            "T = Q_codata/E0 and print the comparison."),
        q0_value=Q_50_DIGIT_STR)
    out = Path(__file__).resolve().parent / "qbeta-option-e-forced-class.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
