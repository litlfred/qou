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

THE DIAGONAL, now derived too.  An earlier revision of this probe reported P_77 as
CONDITIONAL, because the z-linear fit `z + (q-1)/(q+1)` had no structural backing --
the proof block's V_1 table gives d = 0 for the pp pair, so that constant was
unexplained.  It is not a constant.  Measured:

    (q - 1)/(q + 1)  ==  h * z_C^2      with h = q - 1/q,

exactly -- because h*z_C^2 = ((q^2-1)/q)(q/(q+1)^2) = (q^2-1)/(q+1)^2.  So

    P_77  =  1*z  +  h*z^2

with BOTH coefficients in Q(q), verified symbolically against the published closed
form.  That is the same shape as Phi = B*z + A*z^2: a z-polynomial with rational
coefficients and no constant term, which is what a 1-jet amplitude built from
V = z*(.) + (.) must be, and what any Markov trace on the H_3 normal-form basis is
(tr_M(w) = z^|w|, so any Hecke element traces to a z-polynomial whose coefficients
are its NF expansion -- convention-independent by construction).

    P_77_D(q) = q^3 (q^4 + 1) / (q^2 + 1)^2

whose numerator vanishes only at q = 0.  So P_77_D > 0 for EVERY q > 0: the
golden-ratio threshold q_star = 1/phi^2, where the published diagonal vanishes, does
not exist under D either.

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


def p77_D(q):
    """Derived: P_77 = z + h z^2 at the canonical z_D, h = q - 1/q."""
    return q ** 3 * (q ** 4 + 1) / (q ** 2 + 1) ** 2


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

    print(f"\n  P_77 = 1*z + h*z^2,  h = {sp.factor(h_sym)}")
    print(f"    reconstruction against the published form: {p77_recon}   exact: {p77_exact}")
    print(f"    P_77_D = {p77_d_sym}")
    print(f"    numerator real roots {p77_roots} -> positive for every q > 0: "
          f"{p77_no_positive_zero}")
    print(f"    at q_star = 1/phi^2 = {mp.nstr(q_star, 18)}:")
    print(f"      P_77_C = {mp.nstr(p77_C(q_star), 8)}   (zero — the golden-ratio threshold)")
    print(f"      P_77_D = {mp.nstr(p77_D(q_star), 12)}   (not zero)")
    print(f"    at q0: P_77_C = {mp.nstr(p77_C(Q0), 12)}   P_77_D = {mp.nstr(p77_D(Q0), 12)}")

    gates_ok = (exact_C and closed_ok and no_extra_root
                and p77_exact and p77_no_positive_zero)

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
    w.add_assertion("published_P77_is_z_plus_h_z2_exactly", 1 if p77_exact else 0, 1)
    w.add_assertion("P77_D_positive_for_all_q_gt_0", 1 if p77_no_positive_zero else 0, 1)
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("A_chain_coefficient", str(sp.factor(A_SYM)))
    w.add_parameter("B_chain_coefficient", str(sp.factor(B_SYM)))
    w.add_data("Phi_D_closed_form", str(closed))
    w.add_data("sextic_real_roots", str(real_roots))
    w.add_data("convention_C_threshold_q", mp.nstr(q_phi, 30))
    w.add_data("Phi_D_at_convention_C_threshold", mp.nstr(phi_D(q_phi), 30))
    w.add_data("Phi_C_at_q0", mp.nstr(phi_C(Q0), 30))
    w.add_data("Phi_D_at_q0", mp.nstr(phi_D(Q0), 30))
    w.add_data("P77_D_closed_form", str(p77_d_sym))
    w.add_data("P77_h_coefficient", str(sp.factor(h_sym)))
    w.add_data("golden_threshold_q_star", mp.nstr(q_star, 30))
    w.add_data("P77_D_at_golden_threshold", mp.nstr(p77_D(q_star), 30))
    w.add_data("P77_C_at_q0", mp.nstr(p77_C(Q0), 30))
    w.add_data("P77_D_at_q0", mp.nstr(p77_D(Q0), 30))
    w.add_data("surviving_thresholds_under_D", "q = 1 only (Phi vanishes; classical limit)")
    w.add_caveat(
        "Both entries are DERIVED, not z-swapped: each is a z-polynomial with Q(q) "
        "coefficients and no constant term (Phi = B z + A z^2, P_77 = z + h z^2), "
        "reconstructed symbolically against the published closed forms, so the "
        "convention enters through z alone. An earlier revision reported P_77 as "
        "conditional because the constant (q-1)/(q+1) looked unstructured; it is "
        "h*z_C^2 exactly. NOT covered here: the off-diagonal P_66, whose published form "
        "carries q^{7/2} and which this probe does not decompose."
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
        "amplitudes are positive (0.0495 C, 0.0625 D), so the stability verdict survives."
    )
    w.save()
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
