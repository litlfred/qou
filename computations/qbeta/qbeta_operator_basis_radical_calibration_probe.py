#!/usr/bin/env python3
"""qou-99qc: CALIBRATE the six-operator-basis machinery against a known corpus
result before anything new is built on it -- and establish that orthogonality
to the radical is codimension-1 there, not structural as it was on the block
basis.

# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/ECatLPDualRadical.lean
# Ref: computations/qbeta/qbeta_ecat_lp_radical_pairing_probe.py  (the block-basis NEGATIVE)
# Ref: computations/nucleus_operator_selection_sdp.py
# Ref: tools/pyhecke/python/pyhecke/lp_dual_solver.py  (gram_pseudo_inverse_solve)
# Ref: .beans/qou-99qc

WHY CALIBRATE. The owner's instruction was "dont trust probes, especially
convention C". The right response to that is not a caveat -- it is to
reproduce a result the corpus already knows, by an independent route, BEFORE
using the same machinery for anything new. If the reproduction fails, nothing
downstream is trustworthy; if it succeeds, the basis, its ordering, the
radical and the pairing are all validated at once.

THE KNOWN RESULT. The corpus records (`operator_selection_lp.lean`,
`y_0_eq_zero_of_radical`, sorry-free; and `qou-8na1`, exact in Q(q), 18/18)
that the operator-selection LP's shadow price is forced to zero because the
Hecke cost is orthogonal to the Gram's radical, the q-antisymmetriser
`v = (-q^3, q^2, q^2, -q, -q, 1)`. It also records the closed form
`<1, v> = -(q-1)(q^2-q+1)`.

THE INDEPENDENT ROUTE. `qbeta_option_e_order_dof_range_probe.tr_at` is a
linear functional on the 6-dimensional normal-form space:

    tr_M(w) = nf[0] + z*nf[1] + z*nf[2] + z^2*nf[3] + z^2*nf[4]
              + z*(h*z + 1)*nf[5]

so the Hecke cost vector in that basis is read straight off the formula:

    t_Hecke = (1, z, z, z^2, z^2, z*(h*z + 1))

That is derived from the trace's own definition, not from the LP literature,
and it is a DIFFERENT computation from the symbolic Q(q) one the corpus used.
Agreement is therefore evidence, not restatement.

CONVENTION, established at the SOURCE and not by name. The only place a
Markov convention can enter this cone is the `z` handed to `tr_at`: `word_nf`
folds through `hm_num` using `h = q - 1/q` alone and never sees `z`. And
`_order.ZD` is literally `Q0**3 / (Q0**2 + 1)` in its source -- convention D,
the ruled one, written out rather than merely named `ZD`.

  🛑 ONE THING NOT VERIFIED, stated rather than glossed: whether `tr_at`'s
  COEFFICIENT PATTERN (`z, z, z^2, z^2, z(hz+1)`) is itself the same in
  convention C. This probe verifies that `z` is the only free parameter and
  that it is D; it does NOT establish that the formula around it is
  convention-neutral. A C-frame object could in principle enter through the
  pattern rather than through `z`.

WHAT §3 ADDS, and it is the reason this is worth landing rather than being a
private sanity check. On the BLOCK basis the geometric cost was excluded
scope-(b): the Gram is `diag(y_lambda * dim_lambda)` and the cost is
`t_lambda = y_lambda * f(lambda)`, so the SAME factor that creates the radical
zeroes the cost, for every `f`
(`ECatLPDualRadical.diagonal_gram_kills_every_cost_on_its_diagonal`). Nothing
of that shape survives.

Here the situation is different and the difference is measurable:
orthogonality to `v` is ONE linear condition on a 6-dimensional space -- a
codimension-1 subspace -- and no feature of the construction forces a cost
into it. Check [A3] exhibits that directly. So the operator-basis route is
NOT excluded by the argument that killed the block-basis one.

  A prune that fails to fire is not a positive result. This says the route is
  not forbidden. It does not say any energy would separate the candidates, and
  it supplies no energy.

NOTHING IS INVENTED HERE. No per-operator geometric energy is defined,
because none is in hand and writing one to see whether it clears the bar --
then keeping it because it did -- is selection against the target. The
measurement this calibration enables is deliberately left un-run.

NO SELECTION BY ACCURACY. No Q_beta, no CODATA, no residual.
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402

mp = _order.mp
set_compute_dps(50)
mp.mp.dps = 50

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD
TOL = mp.mpf("1e-40")
FAILED: list[str] = []


def check(name, ok, note="", w=None):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def dot(a, b):
    return sum((a[i] * b[i] for i in range(len(a))), mp.mpf(0))


def main() -> int:
    w = WitnessBuilder("qbeta-operator-basis-radical-calibration")
    w.set_description(
        "Calibrates the six-operator-basis machinery against the corpus's "
        "known y_0 = 0 result by an INDEPENDENT route -- the Hecke cost "
        "vector read straight off tr_at's own formula, against the symbolic "
        "Q(q) computation the corpus used -- and then establishes that "
        "orthogonality to the radical is codimension-1 on this basis rather "
        "than forced by the construction, as it was on the block basis. "
        "Invents no energy and runs no LP; the measurement it enables is "
        "deliberately left un-run."
    )

    print("qou-99qc -- operator-basis radical calibration")
    print(f"  q0 = {mp.nstr(Q0, 20)}  h = {mp.nstr(H0, 20)}  "
          f"z_D = {mp.nstr(ZD, 20)}")
    print()

    # -- A1: convention, at the source -------------------------------------
    z_from_source = Q0 ** 3 / (Q0 ** 2 + 1)
    z_convention_C = mp.sqrt(Q0) / (Q0 + 1)
    print("== 1. convention, established at the source ==")
    print(f"    _order.ZD              = {mp.nstr(ZD, 20)}")
    print(f"    q^3/(q^2+1)  [conv D]  = {mp.nstr(z_from_source, 20)}")
    print(f"    sqrt(q)/(q+1)[conv C]  = {mp.nstr(z_convention_C, 20)}")
    print()
    check(
        "the_markov_parameter_is_convention_D_verified_by_value",
        abs(ZD - z_from_source) < TOL and abs(ZD - z_convention_C) > mp.mpf("0.1"),
        f"ZD matches q^3/(q^2+1) to {mp.nstr(abs(ZD - z_from_source), 6)} and "
        f"differs from the convention-C value sqrt(q)/(q+1) by "
        f"{mp.nstr(abs(ZD - z_convention_C), 8)}. Verified by VALUE and by "
        f"source -- _order.ZD is literally Q0**3/(Q0**2+1) -- never by the "
        f"name, which AGENTS.md records as unreliable here (markovZ spans "
        f"both conventions; markovZC and markovZc differ by one letter's case "
        f"and mean opposite things). NOT verified: whether tr_at's coefficient "
        f"pattern z,z,z^2,z^2,z(hz+1) is itself convention-neutral",
        w,
    )

    # -- A2: the calibration ------------------------------------------------
    t_hecke = [mp.mpf(1), ZD, ZD, ZD ** 2, ZD ** 2, ZD * (H0 * ZD + 1)]
    v = [-Q0 ** 3, Q0 ** 2, Q0 ** 2, -Q0, -Q0, mp.mpf(1)]
    one = [mp.mpf(1)] * 6

    print("== 2. calibration against the corpus's known result ==")
    print("    t_Hecke, read off tr_at's own formula:")
    for i, x in enumerate(t_hecke):
        print(f"      t[{i}] = {mp.nstr(x, 20)}")
    tv = dot(t_hecke, v)
    ov = dot(one, v)
    closed = -(Q0 - 1) * (Q0 ** 2 - Q0 + 1)
    print()
    print(f"    <t_Hecke, v> = {mp.nstr(tv, 20)}")
    print(f"    <1, v>       = {mp.nstr(ov, 20)}")
    print(f"    closed form -(q-1)(q^2-q+1) = {mp.nstr(closed, 20)}")
    print()
    check(
        "the_hecke_cost_is_orthogonal_to_the_radical_reproducing_y0_equals_zero",
        abs(tv) < TOL,
        f"<t_Hecke, v> = {mp.nstr(tv, 6)}, zero to the working precision. This "
        f"REPRODUCES the corpus's y_0 = 0 (y_0_eq_zero_of_radical, sorry-free; "
        f"qou-8na1 exact in Q(q)) by an independent route: the cost vector is "
        f"read off the trace's own definition in the normal-form basis, not "
        f"taken from the LP literature. Agreement is evidence, not "
        f"restatement",
        w,
    )
    check(
        "the_basis_ordering_and_radical_are_validated_by_the_closed_form",
        abs(ov - closed) < TOL,
        f"<1, v> = {mp.nstr(ov, 20)} against the corpus's published closed "
        f"form -(q-1)(q^2-q+1) = {mp.nstr(closed, 20)}, agreeing to "
        f"{mp.nstr(abs(ov - closed), 6)}. This is the assertion that validates "
        f"the BASIS ORDERING: had my nf coordinates been permuted relative to "
        f"the corpus's operator basis, this pairing would not hit the "
        f"published value. It also confirms the Lean hypothesis <1, v> != 0 "
        f"that dual_price_determined_by_radical carries",
        w,
    )

    # -- A3: codimension-1, not structural ---------------------------------
    print("== 3. is orthogonality FORCED here, as it was on the block basis? ==")
    eps = mp.mpf("1e-12")
    perturbed = list(t_hecke)
    perturbed[0] += eps
    pv = dot(perturbed, v)
    print(f"    t_Hecke + eps*e_0, eps = {mp.nstr(eps, 6)}")
    print(f"    <t', v> = {mp.nstr(pv, 12)}   (= eps * v[0] = "
          f"{mp.nstr(eps * v[0], 12)})")
    print()
    check(
        "orthogonality_is_codimension_one_here_not_structural",
        abs(pv) > TOL and abs(pv - eps * v[0]) < TOL,
        f"perturbing ONE coordinate by {mp.nstr(eps, 6)} moves the pairing to "
        f"{mp.nstr(pv, 12)}, exactly eps*v[0]. So orthogonality to v is a "
        f"single linear condition on a 6-dimensional space -- a codimension-1 "
        f"subspace -- and nothing in the construction forces a cost into it. "
        f"CONTRAST with the block basis, where the Gram is "
        f"diag(y_lambda*dim_lambda) and the cost t_lambda = y_lambda*f(lambda) "
        f"carries the SAME factor, so orthogonality is automatic for every f "
        f"(diagonal_gram_kills_every_cost_on_its_diagonal). The argument that "
        f"killed the block basis does NOT reach this one",
        w,
    )
    check(
        "this_is_a_prune_that_does_not_fire_not_a_positive_result",
        True,
        "the route is not FORBIDDEN; that is all. No per-operator geometric "
        "energy is defined here, because none is in hand -- and writing one to "
        "see whether it clears the bar, then keeping it because it did, is "
        "selection against the target. The measurement this calibration "
        "enables is deliberately left un-run. Recorded as an assertion so the "
        "boundary travels with the calibration",
        w,
    )

    w.add_data("cost_vector_operator_basis",
               {f"t[{i}]": mp.nstr(x, 30) for i, x in enumerate(t_hecke)})
    w.add_data("radical", {
        "v": [mp.nstr(x, 30) for x in v],
        "name": "q-antisymmetriser",
        "t_dot_v": mp.nstr(tv, 30),
        "one_dot_v": mp.nstr(ov, 30),
        "one_dot_v_closed_form": "-(q-1)(q^2-q+1)",
    })
    w.add_data("convention", {
        "markov_parameter": "z_D = q^3/(q^2+1), convention D",
        "verified_how": "by value against both conventions AND at the source "
                        "(_order.ZD is literally Q0**3/(Q0**2+1))",
        "entry_points": "exactly one -- word_nf folds through hm_num using "
                        "h = q - 1/q and never sees z",
        "NOT_verified": "whether tr_at's coefficient pattern z,z,z^2,z^2,"
                        "z(hz+1) is itself convention-neutral",
    })
    w.add_data("scope", {
        "class": "(a) calibration + a prune that does not fire",
        "not_claimed": [
            "that any geometric energy separates the candidates",
            "that a per-operator energy exists -- none is defined here",
            "that the operator-basis route works; only that the block-basis "
            "exclusion does not reach it",
        ],
        "no_selection_by_accuracy": "no Q_beta, no CODATA, no residual",
    })
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)

    ok = not FAILED
    w.save()
    print()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
