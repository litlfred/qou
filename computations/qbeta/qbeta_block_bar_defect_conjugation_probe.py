#!/usr/bin/env python3
"""The ladder phase's bar-defect, resolved per Wedderburn block — and where the
Kohno-Drinfeld conjugate-partition duality actually lives.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_phase_block_resolution_probe.py
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean

BUILDS ON, DOES NOT REPEAT, the master identity of
`qbeta_phase_block_resolution_probe`, which is exact for every z:

    2*alpha  =  sum_lambda [ a_lambda - y_lambda(z) ] * chi^lambda(Delta)
                +  net(dC)

with `a_lambda` (counit coefficients), `chi^lambda(Delta)` (block characters of
the neutron-proton NF difference) and `net(dC)` (commutator floor) all z-free,
and the convention entering at the single factor `y_lambda(z)`.

THE QUESTION. `qou-cds1` entry 12 established that bar-parity is SILENT on the
free constant `K(delta)` in the N=1 factor, because `delta = h^2/2` is
bar-invariant, and closed with: "Closing K needs a genuinely different input."
Two candidate inputs are tested here, both structural, neither numerical:

  (A) does resolving the defect PER BLOCK restore a parity handle?
  (B) is the bar involution the Kohno-Drinfeld conjugate-partition duality
      `lambda <-> lambda'`, which would make the C-frame cancellation a theorem
      rather than a coincidence?

THE BAR ACTION IS ON (q, z) JOINTLY. `z` is a function of `q`; holding it fixed
under `bar` is the meaningless test this bean already recorded and discarded. So
`zbar` is carried as an INDEPENDENT symbol and specialised only at the end, by
the two conditions `MarkovZFullBarCondition.lean` proves:

    bar-even  (C):   zbar = z
    full-bar  (D):   zbar = z - h

RESULT 1 — the defect decomposes, and the two conventions differ in KIND.
Writing d_lambda for the bar-defect `bar(B_lambda) + B_lambda` of each block's
contribution:

    bar-even (C)   d_(3)   z-DEPENDENT       d_(1^3) = -(d_(3) + d_floor)
                   d_(2,1) = 0               SUM = 0   for EVERY bar-even z
    full-bar (D)   d_(3)   z-FREE  (h^2/2)*r
                   d_(2,1) = 0
                   d_(1^3) z-FREE  (h^2/2)/r      r = (q^2+q+1)/(q^2-q+1)
                   d_floor z-FREE  -2q^2h^2/(q^4+q^2+1)
                                             SUM = h^2  for EVERY full-bar z

So the C-frame's bar-oddness — the property the entire C ladder's bare cosine
rests on — is a CANCELLATION BETWEEN THE SYMMETRIC AND ANTISYMMETRIC BLOCKS,
not a property any block has. Under D the cancellation is destroyed, and the
per-block defects become CONSTANTS: the z-dependence cancels inside each block
instead of between blocks.

  Consequence: no choice of z within the full-bar class changes the D defect,
  at block resolution or in aggregate. The "choose a better z" repair direction
  is now closed from a second, parity-based direction, independent of the
  anchor-based two-constraint filter in `qbeta_ladder_alpha_form_filter_probe`.

RESULT 2 — (A) is REFUTED, and it was this probe's own hypothesis. Each
`d_lambda` is itself bar-invariant (a bar-defect always is: bar(bar(X)+X) =
X+bar(X)). So entry 12's silence survives block resolution verbatim — per-block
bar-parity constrains a per-block `K` exactly as little as aggregate bar-parity
constrains `K`. Block resolution is NOT the different input entry 12 asked for.

RESULT 3 — (B) is HALF right, and the failing half localises to one scalar.

    bar(chi^lambda(Delta)) = chi^{lambda'}(Delta)     EXACT, all three blocks,
                                                      convention-free
    bar(a_lambda)         != a_{lambda'}
    bar(y_lambda)         != y_{lambda'}

The characters DO carry the Kohno-Drinfeld duality. The weights do not — but
every one of the three residuals is proportional to the SAME factor `(z+zbar)`,
and solving the three simultaneously returns the unique bar action `zbar = -z`.
So:

    y_lambda is conjugation-equivariant  <=>  z is bar-ODD

Neither convention is that: C has `zbar = z` (bar-even), D has `zbar = z-h`.
Therefore the C-frame's bar-oddness is NOT conjugate-partition equivariance —
this probe's hypothesis (B) in its strong form is REFUTED.

RESULT 4 — a distinguished fourth value, and it is excluded. The unique bar-odd
member of the full-bar class is `z = h/2`: it satisfies `bar(z) = z - h` AND
`bar(z) = -z`, so at `z = h/2` the Markov weights ARE conjugation-equivariant.
It is nonetheless excluded twice over, which is why it is recorded and not
pursued:

  * the two-row cap admits exactly {q, z_D} (`qou-06wh`, proved complete), and
    h/2 is neither;
  * the anchor filter needs z(q0) ~ 0.4991 with slope ~ +400; h/2 gives 0.1045
    with slope 0.9058.

NOT CLAIMED. No `c_k`. No value for `K`. No Q_beta number moves; L2 stays at
1279 ppb. Nothing here says a D-frame resummation is impossible — only that
neither block resolution nor conjugate-partition equivariance supplies the
input entry 12 identified as missing, and that the z-direction is closed.
Scope (a) throughout.

NO FLOAT64: sympy exact symbolic; mpmath mpf at 50 dps for the reported
numerics only.
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

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, L, LEFT, N, ONE, R, basis_vec, h, length, net, q, reg_char,
)

set_compute_dps(50)

Z = sp.Symbol("z")
ZB = sp.Symbol("zbar")
LABELS = ["(3)", "(2,1)", "(1,1,1)"]
CONJ = {0: 2, 1: 1, 2: 0}          # (3) <-> (1^3); (2,1) self-conjugate


def BAR(e):
    """bar: q -> 1/q AND z -> zbar. Never hold z fixed — it is a function of q."""
    return sp.simplify(sp.together(sp.sympify(e).subs({q: 1 / q, Z: ZB},
                                                      simultaneous=True)))


def main() -> int:
    w = WitnessBuilder("qbeta-block-bar-defect-conjugation", engine="sympy+mpmath")
    w.set_description(
        "The ladder phase's bar-defect resolved per Wedderburn block: z-dependent "
        "and cancelling under the bar-even (C) condition, z-FREE and non-cancelling "
        "under the full-bar (D) condition; and bar = partition conjugation on the "
        "block characters but not on the Markov weights, the residual being (z+zbar)."
    )
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- Delta, blocks, characters -----------------------------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]

    comms = [LEFT[i] * basis_vec(j) - LEFT[j] * basis_vec(i)
             for i in range(N) for j in range(N)]
    comm_basis = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    P = sp.Matrix.hstack(*(list(centre) + list(comm_basis)))
    coords = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((coords[i] * centre[i] for i in range(3)), sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)
    chi_d = [sp.simplify(sp.factor(f(delta))) for f in CHI]

    av = sp.symbols("a0 a1 a2")
    sol = sp.solve([sp.Eq(sum(av[k] * CHI[k](v) for k in range(3)), net(v))
                    for v in centre], av, dict=True)
    A = [sp.simplify(sp.factor(sol[0][av[k]])) for k in range(3)]

    # Ocneanu weights. TR[5] = z*(h*z+1), NOT z^3 — the sigma_0 sigma_1 sigma_0
    # Markov weight (docs/audits/2026-05-19-trm5-markov-bug.md).
    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]
    yv = sp.symbols("y0 y1 y2")
    solY = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)),
                           TR[i]) for i in (0, 1, 3)], yv, dict=True)
    Y = [sp.simplify(sp.factor(solY[0][yv[k]])) for k in range(3)]
    floor = sp.factor(sp.simplify(net(dC)))

    B = [sp.simplify((A[k] - Y[k]) * chi_d[k]) for k in range(3)]
    check("master_identity_reproduces_two_alpha_CONTROL",
          sp.simplify(sum(B) + floor - h * (Z - 1)) == 0,
          "(2a = h(z-1), symbolic in z — the prior probe's identity, re-verified)")

    d = [sp.simplify(sp.factor(BAR(B[k]) + B[k])) for k in range(3)]
    d_floor = sp.simplify(BAR(floor) + floor)

    # ---- RESULT 1: the two bar conditions differ in KIND ---------------------
    subC, subD = {ZB: Z}, {ZB: Z - h}
    dC_ = [sp.simplify(sp.factor(x.subs(subC))) for x in d]
    dD_ = [sp.simplify(sp.factor(x.subs(subD))) for x in d]
    dfC = sp.simplify(d_floor.subs(subC))
    dfD = sp.simplify(d_floor.subs(subD))

    check("bar_even_C_the_block_defects_ARE_z_dependent",
          (Z in dC_[0].free_symbols) and (Z in dC_[2].free_symbols),
          "(so C's bar-oddness is a CANCELLATION between blocks)")
    check("bar_even_C_they_sum_to_zero_for_EVERY_bar_even_z",
          sp.simplify(sum(dC_) + dfC) == 0)
    check("full_bar_D_every_block_defect_is_z_FREE",
          all(Z not in x.free_symbols for x in dD_) and Z not in dfD.free_symbols,
          "(the z-dependence cancels INSIDE each block, not between blocks)")
    check("full_bar_D_they_sum_to_h_squared_for_EVERY_full_bar_z",
          sp.simplify(sum(dD_) + dfD - h**2) == 0)
    check("the_2_1_block_never_contributes_in_either_condition",
          sp.simplify(chi_d[1]) == 0 and sp.simplify(dC_[1]) == 0
          and sp.simplify(dD_[1]) == 0,
          "(chi^(2,1)(Delta) = 0 identically: the phase is blind to the 2-dim block)")

    r = sp.factor(sp.simplify(dD_[0] / (h**2 / 2)))
    check("the_two_D_defects_are_reciprocal_multiples_of_h_squared_over_2",
          sp.simplify(dD_[0] - (h**2 / 2) * r) == 0
          and sp.simplify(dD_[2] - (h**2 / 2) / r) == 0
          and sp.simplify(r - (q**2 + q + 1) / (q**2 - q + 1)) == 0,
          f"(r = {r})")

    # ---- RESULT 2: block resolution does NOT restore a parity handle --------
    def barq(e):
        return sp.simplify(sp.together(sp.sympify(e).subs(q, 1 / q)))

    check("every_D_block_defect_is_itself_bar_INVARIANT",
          all(sp.simplify(barq(x) - x) == 0 for x in dD_ + [dfD]),
          "(so entry 12's silence on K survives block resolution — REFUTES this "
          "probe's own hypothesis (A))")

    # ---- RESULT 3: where the Kohno-Drinfeld duality lives -------------------
    check("bar_acts_as_partition_CONJUGATION_on_the_block_characters",
          all(sp.simplify(BAR(chi_d[k]) - chi_d[CONJ[k]]) == 0 for k in range(3)),
          "(bar chi^(3) = chi^(1,1,1), bar chi^(2,1) = chi^(2,1) — exact, "
          "convention-free)")
    check("it_does_NOT_act_so_on_the_counit_coefficients",
          any(sp.simplify(BAR(A[k]) - A[CONJ[k]]) != 0 for k in range(3)))

    resid = [sp.simplify(sp.factor(BAR(Y[k]) - Y[CONJ[k]])) for k in range(3)]
    check("every_weight_residual_carries_the_SAME_factor_z_plus_zbar",
          all(sp.simplify(sp.cancel(x / (Z + ZB))).is_rational_function(Z, ZB)
              and sp.simplify(x.subs(ZB, -Z)) == 0 for x in resid),
          "(so the obstruction to conjugation-equivariance is ONE scalar)")
    zb_sol = sp.solve([sp.numer(sp.together(x)) for x in resid], ZB, dict=True)
    check("the_UNIQUE_bar_action_making_the_weights_equivariant_is_zbar_eq_minus_z",
          len(zb_sol) == 1 and sp.simplify(zb_sol[0][ZB] + Z) == 0,
          "(i.e. z bar-ODD — which is neither C nor D, so C's bar-oddness is "
          "NOT conjugate-partition equivariance: hypothesis (B) REFUTED)")

    # ---- RESULT 4: z = h/2, distinguished and excluded ----------------------
    zh = h / 2
    check("z_eq_h_over_2_is_the_bar_ODD_member_of_the_full_bar_class",
          sp.simplify(barq(zh) - (zh - h)) == 0 and sp.simplify(barq(zh) + zh) == 0)
    check("z_eq_h_over_2_is_EXCLUDED_by_the_two_row_cap",
          sp.simplify(zh - q) != 0 and sp.simplify(zh - q**3 / (q**2 + 1)) != 0,
          "(qou-06wh proves the cap's admissible set is exactly {q, z_D})")

    # ---- numerics (reported, not load-bearing) ------------------------------
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    dq = mp.mpf("1e-25")

    def slope(e):
        f = sp.lambdify(q, e, "mpmath")
        return (f(q0 + dq) - f(q0 - dq)) / (2 * dq)

    hh = ev(h**2)
    rows = []
    print("\n  per-block bar-defect at q0, in units of h^2 (full-bar / D):")
    for k, lbl in enumerate(LABELS):
        frac = ev(dD_[k]) / hh
        rows.append({"block": lbl, "defect_D": str(dD_[k]),
                     "defect_D_over_h2": fmt(frac),
                     "defect_C_is_z_dependent": bool(Z in dC_[k].free_symbols),
                     "chi_of_delta": str(chi_d[k])})
        print(f"    {lbl:<9} {fmt(frac)[:16]:>18}")
    print(f"    {'floor':<9} {fmt(ev(dfD) / hh)[:16]:>18}")
    print(f"    r(q0) = {mp.nstr(ev(r), 12)}")
    print(f"\n  z = h/2 at q0: value {mp.nstr(ev(zh), 12)} "
          f"(filter needs 0.499104480185), slope {mp.nstr(slope(zh), 12)} "
          f"(filter needs +400.289678821)")

    w.add_data("bar_conditions", {
        "bar_even_C": "zbar = z", "full_bar_D": "zbar = z - h",
        "C_blocks_z_dependent_sum_zero": True,
        "D_blocks_z_free_sum_h_squared": True,
        "r": str(sp.factor(r)),
    })
    w.add_data("blocks", rows)
    w.add_data("floor", {"expr": str(floor), "defect_D": str(dfD),
                         "defect_D_over_h2": fmt(ev(dfD) / hh)})
    w.add_data("conjugation", {
        "characters_equivariant": True,
        "counit_coefficients_equivariant": False,
        "weights_equivariant_iff": "zbar = -z  (z bar-ODD)",
        "weight_residual_common_factor": "z + zbar",
    })
    w.add_data("z_eq_h_over_2", {
        "in_full_bar_class": True, "bar_odd": True,
        "value_at_q0": fmt(ev(zh)), "slope_at_q0": fmt(slope(zh)),
        "excluded_by": "two-row cap (qou-06wh: admissible set exactly {q, z_D}) "
                       "and the anchor filter (needs 0.4991 / +400.29)",
    })
    w.add_data("q0_anchor", {
        "pin": "physical_proton",
        "source": "q_parameter.Q_50_DIGIT_STR",
        "registered_in": "computations/q0_anchor_manifest.json (physical_proton)",
        "load_bearing": False,
        "note": "All 14 assertions are symbolic and anchor-free; q0 enters only "
                "the reported numerics. Registered explicitly rather than left "
                "to the unlisted-stem default, per the 2026-08-30 owner ruling: "
                "proton unless the producer is an explicit proton-vs-muon "
                "comparison (E1) or the ideal CAL layer (E2). It is neither.",
    })
    w.add_data("scope", {
        "tier": "scope-(a)",
        "c_k_produced": False, "K_determined": False, "q_beta_ppb": 1279,
        "hypothesis_A_block_resolution_restores_parity_handle": "REFUTED",
        "hypothesis_B_bar_is_conjugate_partition_equivariance": "REFUTED "
            "(holds on characters, fails on weights unless z is bar-odd)",
    })

    passed = sum(ok)
    print(f"\n  {passed}/{len(ok)} checks passed")
    w.save()
    return 0 if passed == len(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
