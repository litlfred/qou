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

SCOPE.  Derived for Phi, on the strength of the proof block's own chain plus
uniqueness.  For the diagonal P_77 the same uniqueness argument gives the unique
z-linear form P_77 = z + (q-1)/(q+1), but the proof block does not state that the
diagonal HAS that form -- its V_1 table gives d = 0 for the pp pair -- so the D
diagonal is reported here as CONDITIONAL on that shape, not derived.  Flagged, not
glossed.

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

    gates_ok = exact_C and closed_ok and no_extra_root

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
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("A_chain_coefficient", str(sp.factor(A_SYM)))
    w.add_parameter("B_chain_coefficient", str(sp.factor(B_SYM)))
    w.add_data("Phi_D_closed_form", str(closed))
    w.add_data("sextic_real_roots", str(real_roots))
    w.add_data("convention_C_threshold_q", mp.nstr(q_phi, 30))
    w.add_data("Phi_D_at_convention_C_threshold", mp.nstr(phi_D(q_phi), 30))
    w.add_data("Phi_C_at_q0", mp.nstr(phi_C(Q0), 30))
    w.add_data("Phi_D_at_q0", mp.nstr(phi_D(Q0), 30))
    w.add_caveat(
        "DERIVED for Phi, on the proof block's own chain (Phi = z*(z*Delta_a0 + "
        "Delta_b0)) plus uniqueness of the decomposition over Q(q). For the DIAGONAL "
        "P_77 the same uniqueness gives P_77 = z + (q-1)/(q+1) as the unique z-linear "
        "form, but the proof block does not state that the diagonal has that shape -- "
        "its V_1 table gives d = 0 for the pp pair -- so the D-frame diagonal is NOT "
        "derived here and is not reported as such."
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
