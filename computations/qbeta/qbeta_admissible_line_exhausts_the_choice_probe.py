#!/usr/bin/env python3
"""The functional choice is a LINE, and every point on it is reachable.

Bean `qou-99qc`, closing enumeration. The bean asks "which functional
evaluates `Delta`" -- and the honest answer this probe establishes is that
*the Q-value does not determine the functional*, because the admissible
functionals form a one-parameter family whose value map onto `Delta` is
affine and SURJECTIVE. Any target whatsoever is hit by exactly one member.

WHY THIS MATTERS, in plain terms. Three doors have been tried:

  * Markov + admissible -- only TWO points exist (`z = q` and
    `z_D = q^3/(q^2+1)`), giving +12.470 % and -43.157 %.
  * Markov, admissibility dropped -- `tr_M` is affine in `z` on `Delta_S`,
    so exactly ONE `z` reproduces the published number, and it is `z = 1`
    (PR #6722), which is not a root of the admissibility numerator.
  * Admissible, Markov dropped -- this probe. The family is a line; CODATA
    is reached at a unique `beta*`; `beta*` is neither Markov point. So
    relaxing to general admissible traces buys a free parameter and nothing
    else: one anchor, one parameter, zero predictive content.

The fourth door -- demanding the answer not depend on the choice at all
(functional-independence, "scalar modulo the radical") -- is the one that
would remove the parameter without an anchor. It is excluded for both
candidate elements at every `q > 1`
(`qbeta_option_e_forced_class_probe.py`, `AdmissibleAgreementDeterminesClass.lean`).

So the enumeration is complete, and no principled choice reproduces CODATA.

PRECISION. Exact sympy over Q(q) throughout; the pin enters only at readout,
as an exact Rational from the 50-digit proton string. No float64 arithmetic.
"""
from __future__ import annotations

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
    Z, BE = sp.Symbol("z"), sp.Symbol("beta")
    Z_D = q**3 / (q**2 + 1)

    # ---- character basis of the trace space of H_3(q) ---------------------
    chi_3 = sp.Matrix([[q ** length(BASIS[i]) for i in range(N)]])
    chi_111 = sp.Matrix([[(-1 / q) ** length(BASIS[i]) for i in range(N)]])
    reg = sp.Matrix([[sp.simplify(reg_char(basis_vec(i))) for i in range(N)]])
    chi_21 = sp.simplify((reg - chi_3 - chi_111) / 2)

    # ---- the Markov trace, and its coordinate in that basis --------------
    TR = sp.Matrix([[sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]])
    ca, cb, cc = sp.symbols("c3 c21 c111")
    sol = sp.solve([sp.Eq(sp.expand(ca * chi_3[i] + cb * chi_21[i] + cc * chi_111[i]),
                          sp.expand(TR[i])) for i in range(N)],
                   [ca, cb, cc], dict=True)
    ok &= chk("markov_trace_decomposes_uniquely_in_the_character_basis",
              len(sol) == 1,
              "6 equations, 3 unknowns -- a unique consistent solution is "
              "itself the check that tr_M is a trace")
    A, B, C = (sp.simplify(sp.factor(sol[0][s])) for s in (ca, cb, cc))
    print(f"      tr_M(z) = ({A})*chi_(3)")
    print(f"              + ({B})*chi_(2,1)")
    print(f"              + ({C})*chi_(1^3)")

    # ---- admissibility: the (1^3) coefficient is the known numerator -----
    num_C = sp.factor(sp.numer(sp.together(C)))
    ok &= chk("admissibility_numerator_is_exactly_the_known_quadratic",
              sp.simplify(sp.expand(sp.numer(sp.together(C)))
                          - sp.expand(q**2 * (Z - q) * ((q**2 + 1) * Z - q**3))) == 0,
              f"chi_(1^3) coefficient numerator = {num_C} = "
              "q^2*(z - q)*((q^2+1)z - q^3) identically -- the admissibility "
              "condition N(q,z) = 0 of the 2026-08-29 audit, re-derived here "
              "from the character decomposition rather than assumed")
    roots_z = [sp.factor(sp.simplify(r)) for r in sp.solve(sp.Eq(C, 0), Z)]
    ok &= chk("exactly_two_admissible_markov_points",
              len(roots_z) == 2
              and any(sp.simplify(r - q) == 0 for r in roots_z)
              and any(sp.simplify(r - Z_D) == 0 for r in roots_z),
              f"admissible z = {roots_z} -- and z = 1 is NOT among them "
              f"(C at z=1 is {sp.factor(sp.simplify(C.subs(Z, 1)))} != 0)")
    ok &= chk("z_equals_one_is_inadmissible",
              sp.simplify(C.subs(Z, 1)) != 0,
              f"C(1) = {sp.factor(sp.simplify(C.subs(Z, 1)))}, nonzero for "
              "q > 1 -- the published closed form's functional leaks into the "
              "(1^3) block that the GNS/TL quotient kills")

    # ---- the ADMISSIBLE LINE: normalise phi(1) = 1 -----------------------
    # chi_(3)(1) = 1, chi_(2,1)(1) = 2 (the identity element is basis vec 0).
    phi = sp.expand((1 - 2 * BE) * chi_3 + BE * chi_21)
    ok &= chk("the_normalised_admissible_family_is_ONE_parameter",
              sp.simplify(phi[0] - 1) == 0,
              "phi_beta(1) = (1-2b)*chi_(3)(1) + b*chi_(2,1)(1) = (1-2b) + 2b "
              "= 1 for every beta -- so after normalisation the admissible "
              "trace space is a LINE, parameterised by beta")

    beta_q = sp.simplify(B.subs(Z, q))
    beta_D = sp.simplify(sp.factor(B.subs(Z, Z_D)))
    ok &= chk("the_two_markov_points_sit_at_beta_0_and_beta_D",
              beta_q == 0 and sp.simplify(beta_D) != 0,
              f"z = q  ->  beta = {beta_q} (the augmentation, chi_(3) itself); "
              f"z = z_D  ->  beta = {beta_D}")
    ok &= chk("markov_points_are_normalised_so_they_lie_ON_the_line",
              sp.simplify(A.subs(Z, q) - 1) == 0
              and sp.simplify(A.subs(Z, Z_D) + 2 * beta_D - 1) == 0,
              "a + 2b = 1 at both admissible z, so both Markov points are "
              "already normalised -- the line is the right ambient family")

    # ---- the value map on an element, and its slope ----------------------
    Delta_S = sp.Matrix([h**2 / 2, -h / 2, -h / 2, 0, 0, 0])
    aS = sp.simplify(sp.factor((chi_3 * Delta_S)[0]))
    bS = sp.simplify(sp.factor((chi_21 * Delta_S)[0]))

    # Delta_L reaches us through its Markov trace (2026-08-29 audit), so its
    # characters come by inverting the two admissible evaluations.
    trL = -(q - 1) * (q + 1) * (q**4 * Z**2 + 2 * q**3 * Z + 2 * q**2
                                - 2 * q * Z + Z**2) / (4 * q**3)
    aL = sp.simplify(sp.factor(trL.subs(Z, q)))
    bL = sp.simplify(sp.factor((trL.subs(Z, Z_D) - A.subs(Z, Z_D) * aL) / beta_D))

    ELEMS = {"Delta_S": (aS, bS), "Delta_L": (aL, bL)}
    for nm, (a_, b_) in ELEMS.items():
        print(f"      {nm}: chi_(3) = {a_}    chi_(2,1) = {b_}")
        print(f"      {nm}: slope d(value)/d(beta) = {sp.factor(sp.simplify(b_ - 2 * a_))}")

    ok &= chk("value_map_is_affine_in_beta_with_slope_b_minus_2a",
              sp.simplify(sp.expand((phi * Delta_S)[0])
                          - (aS + BE * (bS - 2 * aS))) == 0,
              "phi_beta(Delta) = chi_(3)(Delta) + beta*(chi_(2,1) - 2*chi_(3))"
              "(Delta) -- affine in beta, verified on the coordinate vector")
    ok &= chk("slope_is_nonzero_for_both_elements_at_every_q_greater_1",
              all(len([t for t in sp.real_roots(sp.Poly(sp.expand(
                  sp.numer(sp.together(b_ - 2 * a_))), q)) if sp.N(t) > 1]) == 0
                  for (a_, b_) in ELEMS.values()),
              "the slope is exactly the scalar-mod-radical residual b - 2a, "
              "whose only positive root is the degenerate q = 1 -- so on the "
              "physical branch EVERY value is reachable by exactly one beta")

    # ---- readout at the proton pin ---------------------------------------
    q0 = sp.Rational(Q_50_DIGIT_STR)
    m_e = sp.Rational(str(CONST.M_E_MEV))
    Qexp = sp.Rational(str(CONST.Q_NEUTRON_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    T = Qexp / E0

    def f(e):
        r = sp.Rational(sp.nsimplify(e, rational=True))
        return mp.mpf(r.p) / mp.mpf(r.q)

    bD0 = sp.simplify(beta_D.subs(q, q0))
    print(f"\n      T = Q_codata/E0 = {mp.nstr(f(T), 20)}")
    print(f"      beta at z = q   = 0")
    print(f"      beta at z = z_D = {mp.nstr(f(bD0), 20)}")

    rows = []
    beta_stars: list = []
    for nm, (a_, b_) in ELEMS.items():
        a0, b0 = sp.simplify(a_.subs(q, q0)), sp.simplify(b_.subs(q, q0))
        slope0 = sp.simplify(b0 - 2 * a0)
        # observable is |phi(Delta)|; solve both sign branches, keep the
        # physical one (the framework's Q_beta is positive by construction).
        bstar = [sp.simplify((sgn * T - a0) / slope0) for sgn in (1, -1)]
        beta_stars.extend(bstar)
        v_q = a0                       # beta = 0
        v_D = sp.simplify(a0 + bD0 * slope0)
        rows.append({
            "element": nm,
            "chi_3": mp.nstr(f(a0), 20), "chi_21": mp.nstr(f(b0), 20),
            "slope": mp.nstr(f(slope0), 20),
            "value_at_z_q": mp.nstr(f(v_q), 20),
            "value_at_z_D": mp.nstr(f(v_D), 20),
            "pct_z_q": mp.nstr(f((abs(v_q) - T) / T * 100), 10),
            "pct_z_D": mp.nstr(f((abs(v_D) - T) / T * 100), 10),
            "beta_star_plus": mp.nstr(f(bstar[0]), 20),
            "beta_star_minus": mp.nstr(f(bstar[1]), 20),
        })
        print(f"\n      {nm}:  value(beta=0)   = {mp.nstr(f(v_q), 14)}"
              f"   ({mp.nstr(f((abs(v_q)-T)/T*100), 8)} %)")
        print(f"      {nm}:  value(beta=b_D) = {mp.nstr(f(v_D), 14)}"
              f"   ({mp.nstr(f((abs(v_D)-T)/T*100), 8)} %)")
        print(f"      {nm}:  beta* hitting CODATA = {mp.nstr(f(bstar[0]), 14)}"
              f"  (or {mp.nstr(f(bstar[1]), 14)} on the flipped branch)")

    ok &= chk("beta_star_is_NEITHER_markov_point_for_either_element",
              all(sp.simplify(bs - m) != 0
                  for bs in beta_stars for m in (sp.Integer(0), bD0)),
              f"the {len(beta_stars)} beta values reproducing CODATA (two sign "
              "branches x two elements) are all distinct from beta = 0 (z = q) "
              f"and beta = {mp.nstr(f(bD0), 12)} (z = z_D) -- so NO admissible "
              "Markov trace reproduces the Q-value on either candidate element")

    tgt = sp.Symbol("t")
    sols_t = {nm: sp.solve(sp.Eq(a_ + BE * (b_ - 2 * a_), tgt), BE)
              for nm, (a_, b_) in ELEMS.items()}
    ok &= chk("EVERY_target_is_hit_by_exactly_one_beta_so_the_family_is_a_fit",
              all(len(v) == 1 for v in sols_t.values()),
              "solving phi_beta(Delta) = t for a SYMBOLIC target t gives "
              f"exactly one beta on each element ({ {k: len(v) for k, v in sols_t.items()} }) "
              "-- 'some other admissible functional works' is true but empty: "
              "one parameter, one anchor, zero predictive content. Removing "
              "the parameter needs functional-independence, which both "
              "elements fail at every q > 1")

    # ---- the inadmissible point that DOES land: z = 1 --------------------
    trS = q**2 / 2 - q * Z - 1 + Z / q + 1 / (2 * q**2)
    v1 = sp.simplify(trS.subs(Z, 1).subs(q, q0))
    ok &= chk("the_published_value_sits_at_the_inadmissible_z_equals_1",
              abs(f((abs(v1) - T) / T * 100)) < mp.mpf("0.2"),
              f"tr_M(z=1)(Delta_S) is {mp.nstr(f((abs(v1)-T)/T*100), 8)} % from "
              "CODATA -- the published 0.17 %, reproduced here from the "
              "character decomposition rather than from the closed form")

    # ---- witness ---------------------------------------------------------
    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "name": "qbeta-admissible-line-exhausts-the-choice",
        "description": (
            "Enumerates the functional-choice space for Q_beta = |eps(Delta)|*E0. "
            "The normalised admissible traces of H_3(q) form a ONE-PARAMETER "
            "line phi_beta = (1-2b)*chi_(3) + b*chi_(2,1); the value map onto "
            "both candidate Delta is affine with slope b - 2a, which is exactly "
            "the scalar-mod-radical residual and has no root at any q > 1. So "
            "the map is SURJECTIVE: every target is hit by exactly one beta. "
            "Two points of the line are Markov (z = q at beta = 0, z_D at "
            "beta = q^2/(q^2+1)^2), giving +12.470 % / -43.157 % on Delta_S and "
            "+39.324 % / -15.451 % on Delta_L; the beta reproducing CODATA is "
            "neither. Relaxing from Markov traces to general admissible traces "
            "therefore buys one free parameter and no content. The published "
            "0.17 % sits at z = 1, whose chi_(1^3) coefficient is nonzero."),
        "assertions": checks,
        "markov_trace_in_character_basis": {
            "chi_3": str(A), "chi_21": str(B), "chi_111": str(C)},
        "admissible_z_roots": [str(r) for r in roots_z],
        "beta_at_z_D_symbolic": str(beta_D),
        "target_T": mp.nstr(f(T), 25),
        "beta_at_z_D": mp.nstr(f(bD0), 25),
        "elements": rows,
        "caveats": [
            "Admissibility here means annihilating the (1^3) block, i.e. the "
            "GNS/TL quotient under convention D. The line is the normalised "
            "trace space of that quotient, not of H_3(q).",
            "Surjectivity is a statement about the FAMILY, not an endorsement: "
            "a beta chosen to hit the anchor is a fit with one parameter and "
            "one datum, which is why beta* is reported and not adopted.",
            "Delta_L's characters are extracted by inverting its two admissible "
            "Markov evaluations rather than from a coordinate vector; the "
            "extraction is calibrated by reproducing chi_(2,1)(Delta_S) = 0 in "
            "the sibling probe.",
            "Nothing here is wired to production. The bean's decision is "
            "unchanged by this probe -- it closes an option, it does not pick "
            "one.",
        ],
        "related": [
            "QOU.QBeta.AdmissibleAgreement.agreement_determines_class",
            "computations/qbeta/qbeta_option_e_forced_class_probe.py",
            "computations/qbeta/qbeta_published_form_is_the_inadmissible_z1_probe.py",
            "computations/qbeta/qbeta_admissible_functional_hierarchy_probe.py",
            "docs/audits/2026-09-05-qbeta-functional-decision-options.md",
        ],
        "source": "bean qou-99qc (closing enumeration)",
        "scriptFile": Path(__file__).name,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python+sympy",
        q0_anchor="proton",
        q0_anchor_reason=(
            "The character decomposition, the admissibility roots and the "
            "surjectivity argument are exact over Q(q) and pin-free; q0 enters "
            "only to evaluate T = Q_codata/E0 and print the comparison cells."),
        q0_value=Q_50_DIGIT_STR)
    out = Path(__file__).resolve().parent / (
        "qbeta-admissible-line-exhausts-the-choice.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
