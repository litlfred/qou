"""The bar-oddness of the decay trace IS the convention-D condition.

*** NOT NEW. CORRECTED before this probe's first push was reported as a finding. ***
(R1) and (R3) below are a RE-DERIVATION, by a different route, of results the
corpus already holds sorry-free in Lean:

    QOU.QBeta.eigenphase_barOdd_of_barEven      bar(z)=z    => bar(2a)+2a = 0
    QOU.QBeta.eigenphase_bar_defect_of_fullBar  bar(z)=z-h  => bar(2a)+2a = h^2
    (MarkovZFullBarCondition.lean; recorded in
     qbeta_phase_bar_parity_completeness_probe, which states the consequence
     directly: "a_odd = a - h^2/4")

The second theorem IS (R3): for any e, e + bar(e) = 2*even(e), so
bar(2a)+2a = h^2 says even(alpha) = h^2/4. And since 2*alpha = net(Delta) -
tr_M(Delta) with even(net) = h^2/2, "even(alpha) = h^2/4" and "even(tr_M) = 0"
are the SAME statement -- so (R1) is that theorem transported through (D1),
not an independent result.

What this probe adds is only the ROUTE: it reaches the same place from the decay
element Delta and the trace, rather than from z's own bar parity, and it states
the equivalence as an iff with bar(z) left free. Two routes to one result is
worth keeping as corroboration; claiming it twice is not. (R2) -- that
eps = net(Delta) splits as h^2/2 (even) - h (odd) -- is elementary arithmetic
and is recorded here for the record, not as a discovery.

An attack on the c_3-odd / Q_beta bar-parity sector, using the Riesz decomposition
merged in PR #5869 (`net(x) = sum_lambda a_lambda chi^lambda(x) + tr_M(x y_0)`,
`y_0 = mu dC`) and the two-row D-frame trace.

WHAT IS DERIVED (exact, symbolic in q and z; no anchor, no fit, nothing wired).

  (R1)  tr_M^z(Delta) is bar-ODD  <=>  bar(z) = z - h.

        Delta = NF(neutron) - NF(proton) has T_w coordinates
        [h^2/2, -h/2, -h/2, 0, 0, 0], so tr_M^z(Delta) = h^2/2 - h z. Under the
        bar involution q -> 1/q we have h -> -h, so

            even part = ( (h^2/2 - h z) + (h^2/2 + h bar z) ) / 2
                      = h ( h - z + bar z ) / 2

        which vanishes IDENTICALLY iff bar(z) = z - h. That is exactly the full
        bar condition QOU.QBeta / markov_z_full_bar_condition_probe proves holds
        for z_D and FAILS for z_C. So this is not a new coincidence: it is the D
        condition seen from the decay element rather than from z itself, and it
        says the two statements are the SAME statement.

        Measured both ways: at z_D the bar-even part of tr_M(Delta) is exactly 0;
        at z_C it is (q-1)^2 (q+1)^2 / (2 q^2), nonzero.

  (R2)  eps = net(Delta) splits exactly, and both halves are clean:

            eps          = h^2/2 - h
            eps_bar-even = h^2/2
            eps_bar-odd  = -h

        eps is the input to Q_A = |eps m_e / (q(q-1))|, so the decay amplitude's
        baseline has a definite and elementary parity decomposition.

  (R3)  Under D the ladder phase's bar-even part is CONVENTION-FREE:

            alpha       = (net(Delta) - tr_M^z(Delta)) / 2 = (z-1) h / 2
            alpha_even  = h^2 / 4          exactly, and carries no z
            alpha_odd   = everything convention-dependent

        This follows from (R1) + (R2): net contributes h^2/2 to the even part and
        tr_M^D contributes 0, so alpha_even = h^2/4 with the z dependence living
        entirely in the odd sector.

WHY THIS IS AN ATTACK VECTOR AND NOT A RESULT ABOUT c_3.  alpha is the ladder's
ONLY convention-carrying ingredient (measured in
qbeta_ladder_convention_dependence_is_one_phase_probe: Q_A, hbar_q, the Hoefsmit
b and all four rungs are z-free). (R3) then localises the convention dependence
one level further -- into alpha's bar-ODD half alone. Anything asking where a
convention could enter a bar-even quantity has its answer here: under D, it
cannot enter alpha's even part at all.

WHAT THIS DOES NOT DO. It derives no c_k, proposes no value, and does not touch
the c_3 extraction (which qbeta_c3_experimental_uncertainty_probe shows carries
sigma(c_3) = 1.16 anyway). It is a parity statement about the decay element and
the phase, scope (a) throughout.

The identity 2*alpha = net(Delta) - tr_M^z(Delta) used in (R3) is NOT new here:
it is (D1) of qbeta_d_frame_rung_one_rederivation_probe (PR #5864), with the
identification credited there to a sibling on PR #5337.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# `_path_bridge` lives in computations/, one level up from this cluster dir, so
# that directory must be on sys.path BEFORE the import — otherwise the script is
# unrunnable standalone (AGENTS.md; computations/audits/path_bridge_bootstrap_audit.py).
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

q, z, zbar = sp.symbols("q z zbar", positive=True)
h = q - 1 / q


def bar(e):
    return sp.simplify(sp.together(e.subs(q, 1 / q)))


def parity(e):
    b = bar(e)
    return sp.simplify((e + b) / 2), sp.simplify((e - b) / 2)


def main() -> int:
    wb = WitnessBuilder("qbeta-bar-parity-of-the-decay-trace", engine="sympy")
    wb.set_description(
        "tr_M^z(Delta) is bar-ODD if and only if bar(z) = z - h, i.e. the "
        "bar-oddness of the decay trace IS the convention-D condition. "
        "Consequently eps splits as h^2/2 (even) - h (odd), and under D the "
        "ladder phase's bar-even part is exactly h^2/4, carrying no z: all of "
        "alpha's convention content is bar-ODD. Scope (a); nothing wired.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n      {note}")

    net = sp.simplify(h**2 / 2 - h)
    trM = sp.simplify(h**2 / 2 - h * z)
    zD = q**3 / (q**2 + 1)
    zC = sp.sqrt(q) / (q + 1)

    print("=" * 76)
    print(" bar-parity of the decay trace")
    print("=" * 76)
    print()

    # (R1) the equivalence, done symbolically with bar(z) left free
    even_free = sp.simplify(((h**2 / 2 - h * z) + (h**2 / 2 + h * zbar)) / 2)
    check("bar_oddness_iff_full_bar_condition",
          sp.simplify(even_free.subs(zbar, z - h)) == 0 and sp.simplify(even_free) != 0,
          f"with bar(z) left free the even part is {sp.factor(even_free)}, which "
          f"vanishes identically iff bar(z) = z - h -- the full bar condition. Not "
          f"a coincidence: the same statement as the D condition, read off Delta")

    eD, oD = parity(sp.simplify(trM.subs(z, zD)))
    eC, oC = parity(sp.simplify(trM.subs(z, zC)))
    check("trace_is_bar_odd_at_zD_and_not_at_zC",
          sp.simplify(eD) == 0 and sp.simplify(eC) != 0,
          f"bar-even part of tr_M(Delta): at z_D it is {sp.factor(eD)}; at z_C it "
          f"is {sp.factor(eC)}. D kills it exactly; C does not")

    check("corpus_identity_bar_zD_equals_zD_minus_h",
          sp.simplify(bar(zD) - (zD - h)) == 0
          and sp.simplify(bar(zC) - (zC - h)) != 0,
          "cross-check against the corpus: bar(z_D) = z_D - h holds and the same "
          "identity fails for z_C (markov_z_full_bar_condition_probe)")

    # (R2) eps splits cleanly
    ee, eo = parity(net)
    check("eps_splits_as_h2_over_2_and_minus_h",
          sp.simplify(ee - h**2 / 2) == 0 and sp.simplify(eo + h) == 0,
          f"eps = net(Delta) = {sp.factor(net)} splits exactly: bar-even = h^2/2, "
          f"bar-odd = -h. eps is the input to Q_A")

    # (R3) alpha's even part under D is h^2/4 and z-free
    alpha = sp.simplify((net - trM) / 2)
    aD = sp.simplify(alpha.subs(z, zD))
    ae, ao = parity(aD)
    check("alpha_even_is_h2_over_4_and_z_free_under_D",
          sp.simplify(ae - h**2 / 4) == 0 and sp.simplify(ao) != 0,
          f"alpha = (net - tr_M)/2 = (z-1)h/2; at z_D its bar-even part is "
          f"{sp.factor(ae)} = h^2/4 exactly, carrying NO z, while the odd part "
          f"{sp.factor(ao)} carries all of it. alpha is the ladder's only "
          f"convention-carrying ingredient, so this localises the convention "
          f"dependence to alpha's bar-ODD half alone")

    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    wb.add_data("eps_bar_even", str(sp.factor(ee)))
    wb.add_data("eps_bar_odd", str(sp.factor(eo)))
    wb.add_data("trM_bar_even_at_zD", str(sp.factor(eD)))
    wb.add_data("trM_bar_even_at_zC", str(sp.factor(eC)))
    wb.add_data("alpha_bar_even_at_zD", str(sp.factor(ae)))
    wb.add_data("alpha_bar_odd_at_zD", str(sp.factor(ao)))

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
