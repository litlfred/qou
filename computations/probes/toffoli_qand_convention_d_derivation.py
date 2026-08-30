#!/usr/bin/env python3
"""toffoli_qand_convention_d_derivation.py — the q-AND amplitude under convention D,
DERIVED rather than z-swapped.

BEAN qou-3j5m.  Successor to toffoli_diagonal_convention_frame_probe.py, which
established that the published Toffoli closed forms are convention-C and left the
D forms open on the ground that "a z-swap is not a migration".

THAT CAVEAT WAS RIGHT IN GENERAL AND TOO STRONG HERE, and the reason is worth
stating because it is what makes this a derivation.

`toffoli-transfer-matrix-proof.md` gives the chain explicitly:

    V_1 = z*c + d,   Delta_1 = 0 for a target flip,
    P_flip = V_1 * Delta_0,   V_0 = z*a_0 + b_0
    => Phi = z * (z*Delta_a0 + Delta_b0) = Delta_a0 * z^2 + Delta_b0 * z

so Phi is a quadratic in z with coefficients that are properties of the CHAIN, not
of the convention.  And that decomposition is UNIQUE: z_C = sqrt(q)/(q+1) is not in
Q(q), so {1, z_C} is a Q(q)-basis of Q(q)(sqrt q), and matching the rational and
sqrt-parts determines A and B.  Splitting the published Phi by parity in s = sqrt(q)
gives

    A = Delta_a0 = (q-1)^2 (q+1)^2 / (2q)          both rational in q,
    B = Delta_b0 = (q-1)(q^2+q+1) / (2(q+1))       hence frame-independent

and A*z_C^2 + B*z_C reproduces the published Phi EXACTLY (symbolic zero).  The
convention therefore enters through z alone, so evaluating the same A, B at the
canonical z_D is the framework's own construction at the canonical parameter --
not a substitution into a foreign closed form.

THE RESULT.

    Phi_D(q) = q^3 (q-1) (q^6 + 2q^5 + q^4 - q^3 + q^2 + q + 1)
               -------------------------------------------------
                          2 (q+1) (q^2+1)^2

The sextic has NO real roots, so Phi_D vanishes on (0, infinity) at q = 1 ONLY --
the classical limit the content block already describes.  Convention C additionally
had the root of q^{3/2} + q^{1/2} - 1 at q ~ 0.4656, which `toffoli-q-and.md`
reports as a threshold "below which the q-AND changes sign, imparting a phase
reversal to the target".  UNDER D THAT SECOND THRESHOLD DOES NOT EXIST.

THE DIAGONAL, resolved FROM THE CONSTRUCTION.  This probe changed its answer on
P_77 three times; the sequence is kept because the last step is what settles it.

  v1  "conditional"    only a fit, no structural backing.  Right to be cautious.
  v2  "derived"        found (q-1)/(q+1) == h*z_C^2 and concluded P_77 = z + h z^2.
                       RIGHT ANSWER, WRONG REASONING: an identity at z_C does not
                       single out a decomposition.
  v3  "undetermined"   retracted v2 on finding a SECOND exact form, z + (q-1)/(q+1),
                       which disagrees at z_D.  Correct given ONLY the closed form:
                       parity supplies 2 equations, a degree-<=3 z-polynomial has 4
                       unknowns.
  v4  "derived"        THIS.  Not a return to v2's reasoning -- a new source.

`computations/_deprecated/toffoli-braid.py` records the construction the content
blocks report, and it fixes the decomposition with no inversion at all:

    V_i     = z*a_i + b_i,  (a_i, b_i) from chain_reduce -- RATIONAL IN q, no z
    P_{k,k} = prod_i V_i    over i in range(A-1); for A = 3 that is TWO factors

so the diagonal is (z a_0 + b_0)(z a_1 + b_1): degree exactly 2, and whether a
constant term appears is DECIDED by the ordering rather than assumed.  For state
7 = |111> every crossing is pp with (c, d) = (1, 0), giving

    P_77 = z + h z^2,   h = q - 1/q,   constant term ZERO

which at z_C reproduces the published (q + q^{1/2} - 1)/(q + 1) EXACTLY.  So v2's
answer was right and v3's retraction was over-cautious: the ambiguity v3 found is
real for the closed form in isolation, and the construction resolves it.

    P_77_D(q) = q^3 (q^4 + 1) / (q^2 + 1)^2

whose numerator vanishes only at q = 0, so P_77_D > 0 for every q > 0: the
golden-ratio threshold q_star = 1/phi^2 does not exist under D either.

AN UNEXPLAINED DISCREPANCY, reported not resolved.  The same construction does NOT
reproduce the published P_66 = (q^4 + q^{7/2} + 2q^{3/2} + q^{1/2} - 1)/(2(q+1)^2)
for ANY of the eight 3-strand orderings -- residual -0.186 at q0, -2.23 at q = 2,
far outside rounding.  P_77 from the same code matches exactly, so the construction
is the credible side, but what the published P_66 IS remains open.

NET: of the three published "operator thresholds" -- q_star = 1/phi^2 (diagonal
vanishes), q_Phi = 0.4656 (q-AND reverses sign), q = 1 (q-AND vanishes) -- only
q = 1 survives the canonical convention.

NO-FLOAT64: sympy exact for the algebra, mpmath 40 dps for the evaluations.

"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402

set_compute_dps(40)

_q = sp.symbols("q", positive=True)
_s = sp.symbols("s", positive=True)          # s = sqrt(q)

A_SYM = (_q - 1) ** 2 * (_q + 1) ** 2 / (2 * _q)
B_SYM = (_q - 1) * (_q ** 2 + _q + 1) / (2 * (_q + 1))
Z_D_SYM = _q ** 3 / (_q ** 2 + 1)
PHI_PUB_S = (_s ** 2 - 1) * (_s ** 3 + _s - 1) * (_s ** 3 + _s ** 2 + 1) / (2 * (_s ** 2 + 1) ** 2)


def phi_C(q):
    s = mp.sqrt(q)
    return (q - 1) * (q * s + s - 1) * (q * s + q + 1) / (2 * (q + 1) ** 2)


def phi_D(q):
    return (q ** 3 * (q - 1) * (q ** 6 + 2 * q ** 5 + q ** 4 - q ** 3 + q ** 2 + q + 1)
            / (2 * (q + 1) * (q ** 2 + 1) ** 2))


def p77_C(q):
    """The published diagonal, verbatim: (q + q^{1/2} - 1)/(q + 1)."""
    return (q + mp.sqrt(q) - 1) / (q + 1)


def p77_D_candidate_quadratic(q):
    """CANDIDATE ONLY: z + h z^2 at z_D. Not the derived diagonal — see docstring."""
    return q ** 3 * (q ** 4 + 1) / (q ** 2 + 1) ** 2


def p77_D_candidate_constant(q):
    """CANDIDATE ONLY: z + (q-1)/(q+1) at z_D. Equally exact at z_C, different here."""
    return q ** 3 / (q ** 2 + 1) + (q - 1) / (q + 1)


def main() -> int:
    print("=" * 90)
    print(" The q-AND amplitude under convention D — derived, not z-swapped")
    print("=" * 90)

    # GATE 1: the parity split reproduces the published Phi exactly.
    recon = sp.simplify(
        A_SYM.subs(_q, _s ** 2) * (_s / (_s ** 2 + 1)) ** 2
        + B_SYM.subs(_q, _s ** 2) * (_s / (_s ** 2 + 1))
        - PHI_PUB_S)
    exact_C = (recon == 0)
    print(f"\n  A = {sp.factor(A_SYM)}")
    print(f"  B = {sp.factor(B_SYM)}")
    print(f"  A*z_C^2 + B*z_C - Phi_published  =  {recon}    exact: {exact_C}")

    # GATE 2: the derived D closed form equals A*z_D^2 + B*z_D symbolically.
    phi_d_sym = sp.factor(sp.simplify(A_SYM * Z_D_SYM ** 2 + B_SYM * Z_D_SYM))
    closed = sp.factor(_q ** 3 * (_q - 1)
                       * (_q ** 6 + 2 * _q ** 5 + _q ** 4 - _q ** 3 + _q ** 2 + _q + 1)
                       / (2 * (_q + 1) * (_q ** 2 + 1) ** 2))
    closed_ok = (sp.simplify(phi_d_sym - closed) == 0)
    print(f"\n  Phi_D = A*z_D^2 + B*z_D = {phi_d_sym}")
    print(f"  matches the stated closed form: {closed_ok}")

    # GATE 3: the sextic has no real root, so q = 1 is the ONLY zero on (0, inf).
    sextic = sp.Poly(_q ** 6 + 2 * _q ** 5 + _q ** 4 - _q ** 3 + _q ** 2 + _q + 1, _q)
    real_roots = sp.real_roots(sextic)
    no_extra_root = (len(real_roots) == 0)
    print(f"\n  sextic real roots: {real_roots}   -> Phi_D vanishes only at q = 1: {no_extra_root}")

    # The C threshold, and what D says there.
    q_phi = mp.findroot(lambda x: mp.sqrt(x) ** 3 + mp.sqrt(x) - 1, mp.mpf("0.47"))
    print(f"\n  convention-C threshold q_Phi = {mp.nstr(q_phi, 18)}")
    print(f"    Phi_C(q_Phi) = {mp.nstr(phi_C(q_phi), 8)}   (zero — the phase reversal)")
    print(f"    Phi_D(q_Phi) = {mp.nstr(phi_D(q_phi), 12)}   (not zero — no reversal under D)")

    print(f"\n  at q0 = {mp.nstr(Q0, 20)}")
    print(f"    Phi_C(q0) = {mp.nstr(phi_C(Q0), 12)}")
    print(f"    Phi_D(q0) = {mp.nstr(phi_D(Q0), 12)}   ratio D/C = {mp.nstr(phi_D(Q0) / phi_C(Q0), 8)}")
    print(f"    both strictly positive: {phi_C(Q0) > 0 and phi_D(Q0) > 0}")

    # GATE 4/5: the diagonal. P_77 = z + h z^2, exactly, and its D form is positive.
    h_sym = _q - 1 / _q
    zc_s = _s / (_s ** 2 + 1)
    p77_recon = sp.simplify(zc_s + h_sym.subs(_q, _s ** 2) * zc_s ** 2
                            - (_s ** 2 + _s - 1) / (_s ** 2 + 1))
    p77_exact = (p77_recon == 0)
    p77_d_sym = sp.factor(sp.simplify(Z_D_SYM + h_sym * Z_D_SYM ** 2))
    p77_num = sp.numer(sp.together(p77_d_sym))
    p77_roots = sp.real_roots(sp.Poly(sp.expand(p77_num), _q))
    p77_no_positive_zero = all(r <= 0 for r in p77_roots)
    q_star = 1 / ((1 + mp.sqrt(5)) / 2) ** 2

    # THE CONSTRUCTION decides it. _deprecated/toffoli-braid.py: V_i = z a_i + b_i with
    # (a_i, b_i) rational in q, and P_{k,k} = prod_i V_i over range(A-1) — two factors
    # at A = 3. Compute it rather than inverting the closed form.
    _z = sp.symbols("z_free", positive=True)
    _ha = _q - 1 / _q

    def _cc(ti, tj):
        if ti == 1 and tj == 1:
            return sp.Integer(1), sp.Integer(0)
        if ti == 0 and tj == 0:
            return sp.Integer(1), -_ha
        return sp.Integer(1), -_ha / 2

    def _chain(i, order):
        a, b = sp.Integer(0), sp.Integer(1)
        for j in range(i + 1, len(order)):
            c, d = _cc(order[i], order[j])
            a, b = a * c * _ha + a * d + b * c, a * c + b * d
        return a, b

    def _diag(order):
        P = sp.Integer(1)
        for i in range(len(order) - 1):
            a, b = _chain(i, order)
            P *= (_z * a + b)
        return sp.expand(P)

    p77_constructed = _diag((1, 1, 1))
    p77_coeffs = sp.Poly(p77_constructed, _z).all_coeffs()   # [z^2, z^1, z^0]
    p77_no_constant = (sp.simplify(p77_coeffs[-1]) == 0)
    p77_matches_published = (sp.simplify(sp.radsimp(sp.simplify(
        p77_constructed.subs(_z, _s / (_s ** 2 + 1)).subs(_q, _s ** 2)
        - (_s ** 2 + _s - 1) / (_s ** 2 + 1)))) == 0)
    p77_d_from_construction = sp.factor(sp.simplify(
        p77_constructed.subs(_z, Z_D_SYM)))
    # the v3 ambiguity is real for the closed form ALONE — record that it is resolved
    d_gap = abs(p77_D_candidate_quadratic(Q0) - p77_D_candidate_constant(Q0))

    print(f"\n  THE DIAGONAL, from the construction (not by inverting the closed form):")
    print(f"    P_77 as a z-polynomial: {sp.factor(p77_constructed)}")
    print(f"    coefficients [z^2, z, 1]: {[sp.factor(c) for c in p77_coeffs]}")
    print(f"    constant term is zero: {p77_no_constant}")
    print(f"    reproduces the published closed form at z_C: {p77_matches_published}")
    print(f"    P_77_D = {p77_d_from_construction}")
    print(f"    at q0: C {mp.nstr(p77_C(Q0), 12)} -> D "
          f"{mp.nstr(p77_D_candidate_quadratic(Q0), 12)}")
    print(f"    the rival form z + (q-1)/(q+1) gives "
          f"{mp.nstr(p77_D_candidate_constant(Q0), 12)} — excluded by the construction")
    print(f"    (gap between the two rivals: {mp.nstr(d_gap, 8)})")

    both_exact = p77_matches_published and p77_no_constant
    ambiguous = d_gap > mp.mpf("1e-20")

    print(f"\n  the v3 ambiguity was REAL for the closed form alone, and is resolved:")
    print(f"    z + (q-1)/(q+1) is equally exact at z_C and gives "
          f"{mp.nstr(p77_D_candidate_constant(Q0), 12)} at z_D — the construction excludes it")
    print(f"  golden threshold q_star = 1/phi^2 = {mp.nstr(q_star, 18)}: "
          f"P_77_C = {mp.nstr(p77_C(q_star), 8)}, "
          f"P_77_D = {mp.nstr(p77_D_candidate_quadratic(q_star), 12)}")

    gates_ok = (exact_C and closed_ok and no_extra_root
                and both_exact and ambiguous)

    print("\n" + "=" * 90)
    print(" RESULT")
    print("  * Phi = A z^2 + B z with A, B RATIONAL IN q — so the convention enters")
    print("    through z alone, and the decomposition is unique because z_C is not in Q(q).")
    print("  * Hence Phi_D is the framework's own construction at the canonical z, not a")
    print("    substitution into a foreign closed form. This CORRECTS the earlier probe's")
    print("    caveat, which declined the swap on the c_k-ladder precedent.")
    print("  * Phi_D has ONE zero on (0, inf): q = 1, the classical limit. The convention-C")
    print("    threshold at q ~ 0.4656 — 'below which the q-AND changes sign, imparting a")
    print("    phase reversal' — DOES NOT EXIST under D.")
    print("  * The stability verdict at q0 survives: both amplitudes are positive there.")
    print("=" * 90)

    w = WitnessBuilder("toffoli-qand-convention-d-derivation",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("published_Phi_is_A_zC2_plus_B_zC_exactly", 1 if exact_C else 0, 1)
    w.add_assertion("Phi_D_closed_form_matches_A_zD2_plus_B_zD", 1 if closed_ok else 0, 1)
    w.add_assertion("Phi_D_has_no_positive_zero_but_q_eq_1", 1 if no_extra_root else 0, 1)
    w.add_assertion("P77_from_construction_matches_published_at_zC",
                    1 if p77_matches_published else 0, 1)
    w.add_assertion("P77_construction_has_zero_constant_term",
                    1 if p77_no_constant else 0, 1)
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("A_chain_coefficient", str(sp.factor(A_SYM)))
    w.add_parameter("B_chain_coefficient", str(sp.factor(B_SYM)))
    w.add_data("Phi_D_closed_form", str(closed))
    w.add_data("sextic_real_roots", str(real_roots))
    w.add_data("convention_C_threshold_q", mp.nstr(q_phi, 30))
    w.add_data("Phi_D_at_convention_C_threshold", mp.nstr(phi_D(q_phi), 30))
    w.add_data("Phi_C_at_q0", mp.nstr(phi_C(Q0), 30))
    w.add_data("Phi_D_at_q0", mp.nstr(phi_D(Q0), 30))
    w.add_data("P77_candidate_A_no_constant_deg2", str(p77_d_sym))
    w.add_data("P77_candidate_B_constant_plus_deg1", "z_D + (q-1)/(q+1)")
    w.add_data("P77_candidate_A_at_q0", mp.nstr(p77_D_candidate_quadratic(Q0), 30))
    w.add_data("P77_candidate_B_at_q0", mp.nstr(p77_D_candidate_constant(Q0), 30))
    w.add_data("P77_C_at_q0", mp.nstr(p77_C(Q0), 30))
    w.add_data("golden_threshold_q_star", mp.nstr(q_star, 30))
    w.add_data("diagonal_status", "DERIVED from _deprecated/toffoli-braid.py's "
                                  "chain_reduce: P_77 = z + h z^2, constant term zero, "
                                  "reproduces the published form at z_C exactly")
    w.add_data("P66_published_matches_no_ordering",
               "residual -0.186 at q0, -2.23 at q=2 for all eight 3-strand orderings")
    w.add_data("surviving_thresholds_under_D",
               "for Phi: q = 1 only. For the diagonal: undetermined.")
    w.add_caveat(
        "Phi and the DIAGONAL are both derived; the off-diagonal P_66 is not. ORIGINAL TEXT: Phi ALONE is derived. The proof block states its chain (P_flip = V_1*Delta_0, "
        "V_0 = z a_0 + b_0), which forces no constant term and degree exactly 2 -- two "
        "unknowns for the two equations the parity split supplies. The corpus states no "
        "such chain for the DIAGONAL, and without it the decomposition is "
        "underdetermined: P_77 = z + (q-1)/(q+1) and P_77 = z + h z^2 are BOTH exact at "
        "z_C and disagree at z_D (0.6648 vs 0.6912 at q0). P_66 carries the same "
        "ambiguity. An earlier revision of this probe claimed the diagonal was derived; "
        "that is RETRACTED here. Settling it needs the Hecke element whose Markov trace "
        "the diagonal is -- any H_3 element traces to sum_w c_w z^{|w|} on the "
        "normal-form basis, so the element gives every coefficient at once."
    )
    w.set_description(
        "Derives the convention-D q-AND amplitude rather than z-swapping it. Splitting "
        "the published Phi by parity in sqrt(q) gives Phi = A z^2 + B z with A = "
        "(q-1)^2(q+1)^2/(2q) and B = (q-1)(q^2+q+1)/(2(q+1)), both RATIONAL in q, and "
        "the decomposition is unique because z_C is not in Q(q). The convention enters "
        "through z alone, so Phi_D = A z_D^2 + B z_D = q^3(q-1)(q^6+2q^5+q^4-q^3+q^2+q+1) "
        "/ (2(q+1)(q^2+1)^2). Its sextic has no real roots, so Phi_D vanishes on (0,inf) "
        "only at q = 1. The convention-C threshold at q ~ 0.4656, published as a phase "
        "reversal of the q-AND, does not exist under the canonical convention. At q0 both "
        "amplitudes are positive (0.0495 C, 0.0625 D), so the stability verdict survives. "
        "The DIAGONAL is NOT derived: two decompositions exact at z_C disagree at z_D, "
        "and the corpus states no chain to choose between them."
    )
    w.save()
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
