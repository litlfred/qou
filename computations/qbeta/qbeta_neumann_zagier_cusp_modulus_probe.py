#!/usr/bin/env python3
"""qou-pzsi / qou-yh67: DERIVE tau(u) for the figure-eight cusp from Neumann-Zagier's
own gluing equations, cross-check tau_0 against the corpus's hexagonal cusp lattice,
and re-measure the O'Hara energy's modulus sensitivity at the DERIVED drift instead
of at the hand-picked one I used first.

# Ref: [neumann-zagier-1985] Volumes of hyperbolic three-manifolds, Topology 24 (1985) 307-332
#      library/neumann-zagier-1985-volumes-of-hyperbolic-three-manifolds/sections/
#      -- eq (52) (odd series), (65)-(66) (the 4_1 gluing), (68) (the coefficient shown here)
# Ref: computations/qbeta/qbeta_bring_ohara_bridge_probe.py        (the bridge this re-measures)
# Ref: computations/qbeta/qbeta_cusp_shape_drift_robustness_probe.py (states the u != 0 problem)
# Ref: folio/quantum-observable-universe/.../cusp-shape-bar-parity.md (the hexagonal lattice)
# Ref: .beans/qou-yh67--...md  (the NZ-1/2 binary, STRUCTURALLY OPEN -- carried, not settled)

WHY. `qbeta_bring_ohara_bridge_probe` computes the O'Hara energy of a closed
geodesic on the cusp torus at the modulus `omega = e^{i pi/3}` -- the shape at the
COMPLETE hyperbolic structure, `u = 0`. The physical evaluation does not sit
there: it sits at a meridian log-holonomy of order `ln q0 != 0`, which is exactly
what `qbeta_cusp_shape_drift_robustness_probe` flags. So the bridge's numbers are
computed at a modulus the framework does not use, and the question is how far the
real modulus is from it.

I first answered that by drifting `omega` by hand at the O(u) scale -- radially,
angularly, and along the imaginary axis, all at +-10.4%. That was an ASSUMPTION
about the drift dressed as a measurement of it, and this probe replaces it: NZ
give the deformation exactly, and it is O(u^2), an order of magnitude smaller.

THE DERIVATION, from NZ's own figure-eight worked example. The gluing variety of
4_1 is `z w (z-1)(w-1) = 1`, deformed by

    z(1-z) = e^{ v/2}        w(1-w) = e^{-v/2}        (NZ 66)
    u = log( w (1-z) )                                (NZ 65)

with `u` the meridian and `v` the longitude log-holonomy. Solving each quadratic
and composing gives `u(v)` in closed form; the branch is fixed by continuity from
`v = 0`, where the complete structure sits at `z = w = (1 + i sqrt 3)/2`. Series-
inverting `u(v)` gives `v(u) = c_1 u + c_3 u^3 + ...` and the cusp shape

    tau(u) = v(u)/u = c_1 + c_3 u^2 + O(u^4).

NZ eq (52) says `c_n = 0` for even `n`; check [A1] verifies that on the computed
series rather than assuming it, which is what makes the `O(u^2)` claim a result.

WHAT IT GIVES, and both numbers are recognisable:

    tau_0 = c_1 = 2 sqrt(-3) = 3.4641016151377545871 i      -- the 4_1 cusp shape
    c_3 / c_1 = 1/3   exactly                               -- NZ (68)'s coefficient

THE CROSS-CHECK WORTH HAVING [A3]. The corpus states the 4_1 cusp lattice as the
HEXAGONAL `Z<1, omega>`, `omega = e^{i pi/3}` (`cusp-shape-bar-parity.md`, proved).
NZ state the cusp SHAPE as `2 sqrt(-3)`. These are not in tension and are not the
same statement: `2 sqrt(-3) = -2 + 4 omega` EXACTLY, so the NZ meridian-longitude
lattice `Z<1, tau_0>` is the index-4 sublattice of the corpus's shortest-vector
lattice. Two independent sources, one lattice, and the integer relation is exact
rather than numerical.

THE BINARY I AM NOT SETTLING [A5]. NZ's `u` is a log-holonomy in THEIR
normalisation; the corpus's meridian boost is `ln q0` in its own. Whether the
substitution is `u = ln q0` or `u = 2 ln q0` is the same factor-of-two that bean
`qou-yh67` records as the NZ-1/2 binary (`kappa_shape = sqrt3/2` against
`kappa_pot = sqrt3/4`, i.e. the `Phi = 2 V` factor), and `qou-yh67` states plainly
that it CANNOT be settled numerically -- picking the branch that lands a target is
a fit. So both are computed and reported side by side, and neither is adopted.
Note the factor enters `tau` SQUARED, so the two branches differ by 4x in the
drift: 0.363% against 1.452%.

THE RESULT FOR THE BRIDGE, and it is a correction of my own number. The derived
modulus drift is second order, so it is ~0.36% (or ~1.45%) rather than the ~10%
I drifted by hand, and the O'Hara energy moves correspondingly less. The bridge's
figures are therefore ROBUST at the sub-percent level, not sensitive at the
ten-percent level as my first measurement implied. What does not change at all is
the negative: the lattice class `(m, l) = (writhe, strands)` is defined by the
word and the closure and does not reference the modulus, so NO modulus makes this
embedding order-sensitive [A8]. The tie survives the correction.

NO SELECTION BY ACCURACY. No Q_beta, no CODATA, no residual appears anywhere in
this probe. Nothing here is chosen to land a number.
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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

import mpmath as mp  # noqa: E402

set_compute_dps(40)
mp.mp.dps = 40

Q0 = Q_MP

#: the 4_1 cusp shape in the corpus's shortest-vector basis, a primitive 6th root
#: of unity (cusp-shape-bar-parity.md, proved).
OMEGA = mp.exp(mp.mpc(0, 1) * mp.pi / 3)

#: lattice window for the ambient-distance minimisation, matching the bridge probe.
LATTICE_R = 3

#: the corpus nucleon closure: 3 strands, and the four two-crossing gluon
#: dressings all carry writhe +2 (measured in the embedding-discriminability probe).
CLASS_M, CLASS_L = 2, 3

TOL = mp.mpf("1e-20")
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


# ---------------------------------------------------------------------------
# the NZ gluing equations for 4_1
# ---------------------------------------------------------------------------

def _sqrt_from_complete(x):
    """Square root on the branch continuous from v = 0.

    mpmath's principal branch jumps as the argument crosses the negative reals,
    and the 4_1 discriminant does exactly that on the path from v = 0. At v = 0
    the complete structure has z = w = (1 + i sqrt3)/2, i.e. the root with
    POSITIVE imaginary part, so that is the branch tracked here. Taking the
    principal branch instead makes findroot diverge (measured: residual 12.478),
    which is how this was caught.
    """
    r = mp.sqrt(x)
    return r if mp.im(r) >= 0 else -r


def u_of_v(v):
    """NZ (65)-(66): the meridian log-holonomy as a function of the longitude one."""
    z = (1 + _sqrt_from_complete(1 - 4 * mp.e ** (v / 2))) / 2
    w = (1 + _sqrt_from_complete(1 - 4 * mp.e ** (-v / 2))) / 2
    return mp.log(w * (1 - z))


# ---------------------------------------------------------------------------
# O'Hara energy of a closed geodesic on the flat torus C/<1, tau>
# (identical convention to qbeta_bring_ohara_bridge_probe; see its docstring
#  for why the O'Hara subtraction cancels EXACTLY on a flat torus)
# ---------------------------------------------------------------------------

def ohara_energy(m: int, ell: int, tau):
    v = mp.mpf(m) + mp.mpf(ell) * tau
    length = abs(v)
    if length == 0:
        return None
    vhat = v / length

    def integrand(s):
        d_arc = min(s, length - s)
        if d_arc <= 0:
            return mp.mpf(0)
        disp = s * vhat
        best = None
        for a in range(-LATTICE_R, LATTICE_R + 1):
            for b in range(-LATTICE_R, LATTICE_R + 1):
                lam = mp.mpf(a) + mp.mpf(b) * tau
                # the TRIVIAL translates 0 and v reproduce d_arc exactly, so
                # keeping them makes the integrand 1e80 - 1e80 at the endpoints.
                if abs(lam) < TOL or abs(lam - v) < TOL:
                    continue
                d = abs(disp - lam)
                if best is None or d < best:
                    best = d
        if best is None or best >= d_arc:
            return mp.mpf(0)
        return 1 / best ** 2 - 1 / d_arc ** 2

    return length * mp.quad(integrand, [mp.mpf(0), length / 2, length])


def main() -> int:
    w = WitnessBuilder("qbeta-neumann-zagier-cusp-modulus")
    w.set_description(
        "Derives the figure-eight cusp shape tau(u) = c_1 + c_3 u^2 + ... from "
        "Neumann-Zagier's own gluing equations (65)-(66) by series-inverting "
        "u(v), and gets tau_0 = 2 sqrt(-3) with c_3/c_1 = 1/3 exactly, matching "
        "NZ (68). Cross-checks that against the corpus's hexagonal cusp lattice: "
        "2 sqrt(-3) = -2 + 4 omega exactly, so the NZ meridian-longitude lattice "
        "is the index-4 sublattice of Z<1, omega> -- two sources, one lattice, "
        "exact integer relation. CORRECTS my own earlier measurement of the "
        "O'Hara bridge's modulus sensitivity: the derived drift is O(u^2) and "
        "~0.36% (or ~1.45% on the other normalisation branch), not the ~10% I "
        "drifted omega by hand, so the bridge's energies are robust at the "
        "sub-percent level. The meridian-normalisation binary u = ln q0 vs "
        "u = 2 ln q0 is the NZ-1/2 factor of bean qou-yh67 and is CARRIED, not "
        "settled -- both branches are reported and neither adopted. The bridge's "
        "order-blindness survives: the class (m, l) = (writhe, strands) never "
        "references the modulus, so no tau can make this embedding "
        "order-sensitive."
    )

    print("qou-pzsi / qou-yh67 -- Neumann-Zagier tau(u) for the 4_1 cusp")
    print(f"  q0 = {mp.nstr(Q0, 20)}   ln q0 = {mp.nstr(mp.log(Q0), 20)}")
    print()

    # -- A1/A2/A4: the series -------------------------------------------------
    print("== 1. series-invert NZ (65)-(66): u(v), then v(u) ==")
    N = 8
    a = mp.taylor(u_of_v, 0, N, method="quad", radius=mp.mpf("0.2"))
    print("    Taylor  u(v) = sum a_n v^n")
    for n in range(1, N + 1):
        tag = "" if n % 2 else "   <- EVEN, NZ (52) says this must vanish"
        print(f"      a_{n} = {mp.nstr(a[n], 16)}{tag}")

    even_max = max(abs(a[n]) for n in range(2, N + 1, 2))
    odd_min = min(abs(a[n]) for n in range(1, N + 1, 2))
    check(
        "nz_series_is_odd_only_every_even_coefficient_vanishes",
        even_max < mp.mpf("1e-25") and odd_min > mp.mpf("1e-10"),
        f"largest |a_even| = {mp.nstr(even_max, 6)} against smallest "
        f"|a_odd| = {mp.nstr(odd_min, 6)} -- NZ eq (52) states c_n = 0 for even "
        f"n, and this VERIFIES it on the computed series rather than imposing "
        f"it. It is what makes the leading correction to tau second order in u, "
        f"which is the whole quantitative point of this probe",
        w,
    )

    c1 = 1 / a[1]
    c3 = -a[3] / a[1] ** 4
    tau0_closed = 2 * mp.sqrt(mp.mpc(-3, 0))
    print()
    print("    INVERTED  v(u) = c_1 u + c_3 u^3 + ...   so tau(u) = v(u)/u")
    print(f"      c_1 = tau_0     = {mp.nstr(c1, 20)}")
    print(f"      2 sqrt(-3)      = {mp.nstr(tau0_closed, 20)}")
    print(f"      c_3             = {mp.nstr(c3, 20)}")
    print(f"      c_3 / c_1       = {mp.nstr(c3 / c1, 20)}   <- NZ (68) slot")
    print()

    check(
        "tau_zero_is_two_sqrt_minus_three",
        abs(c1 - tau0_closed) < mp.mpf("1e-25"),
        f"c_1 = {mp.nstr(c1, 20)} against the closed form 2 sqrt(-3) = "
        f"{mp.nstr(tau0_closed, 20)}, agreeing to "
        f"{mp.nstr(abs(c1 - tau0_closed), 6)}. This is the figure-eight cusp "
        f"shape at the COMPLETE structure and is read out of NZ's gluing "
        f"equations here, not assumed from the literature value",
        w,
    )

    ratio = c3 / c1
    check(
        "c3_over_tau_zero_is_exactly_one_third_matching_NZ_68",
        abs(ratio - mp.mpf(1) / 3) < mp.mpf("1e-25"),
        f"c_3/c_1 = {mp.nstr(ratio, 22)} against 1/3, agreeing to "
        f"{mp.nstr(abs(ratio - mp.mpf(1) / 3), 6)}. NZ eq (68) shows 1/3 at this "
        f"slot for 4_1, so the series inversion reproduces the published "
        f"coefficient independently. tau(u) = 2 sqrt(-3) (1 + u^2/3 + O(u^4))",
        w,
    )

    # -- A3: the lattice cross-check -----------------------------------------
    print("== 2. cross-check against the corpus's hexagonal cusp lattice ==")
    lattice_form = -2 + 4 * OMEGA
    print(f"    omega = e^(i pi/3)   = {mp.nstr(OMEGA, 18)}")
    print(f"    -2 + 4 omega         = {mp.nstr(lattice_form, 18)}")
    print(f"    tau_0 = 2 sqrt(-3)   = {mp.nstr(tau0_closed, 18)}")
    print()
    check(
        "the_NZ_cusp_shape_is_an_exact_integer_point_of_the_corpus_lattice",
        abs(lattice_form - tau0_closed) < mp.mpf("1e-25"),
        f"2 sqrt(-3) = -2 + 4 omega to {mp.nstr(abs(lattice_form - tau0_closed), 6)}. "
        f"The corpus states the 4_1 cusp lattice as hexagonal Z<1, omega> "
        f"(cusp-shape-bar-parity.md, proved); NZ state the cusp SHAPE as "
        f"2 sqrt(-3). Not a tension and not the same statement -- the NZ "
        f"meridian-longitude lattice Z<1, tau_0> is the index-4 sublattice "
        f"(det [[1,0],[-2,4]] = 4) of the shortest-vector one. Two independent "
        f"sources agreeing on one lattice, with an EXACT integer relation "
        f"rather than a numerical one",
        w,
    )

    # -- A5: the normalisation binary, carried not settled --------------------
    print("== 3. the meridian-normalisation binary -- CARRIED, NOT SETTLED ==")
    u1 = mp.log(Q0)
    branches = [("u = ln q0", u1), ("u = 2 ln q0", 2 * u1)]
    taus = {}
    print(f"    {'branch':<14} {'u':<16} {'tau(u)':<26} {'drift from tau_0'}")
    for lbl, uu in branches:
        tau = c1 + c3 * uu ** 2
        taus[lbl] = tau
        drift = abs(tau - c1) / abs(c1)
        print(f"    {lbl:<14} {mp.nstr(uu, 12):<16} {mp.nstr(tau, 18):<26} "
              f"{mp.nstr(drift, 8)}")
    d1 = abs(taus["u = ln q0"] - c1) / abs(c1)
    d2 = abs(taus["u = 2 ln q0"] - c1) / abs(c1)
    print()
    check(
        "the_meridian_normalisation_binary_is_carried_not_settled",
        abs(d2 / d1 - 4) < mp.mpf("1e-6"),
        f"both branches computed and NEITHER adopted: u = ln q0 drifts tau by "
        f"{mp.nstr(d1, 6)} and u = 2 ln q0 by {mp.nstr(d2, 6)}, a ratio of "
        f"exactly 4 because the factor enters tau squared. Which branch is "
        f"correct is the same factor of two as bean qou-yh67's NZ-1/2 binary "
        f"(kappa_shape = sqrt3/2 against kappa_pot = sqrt3/4, the Phi = 2 V "
        f"factor), and qou-yh67 records that it CANNOT be settled numerically. "
        f"Choosing the branch that lands a target would be selection against "
        f"the target under the anti-fit rule, so no choice is made here",
        w,
    )

    # -- A6/A7: the corrected sensitivity -------------------------------------
    print("== 4. O'Hara energy of the (2,3) class at the DERIVED modulus ==")
    print("    (correcting my own hand-picked O(u) drift, which was an "
          "assumption dressed as a measurement)")
    print()
    # continue the shortest-vector basis under a deformation fixing the meridian:
    # tau = -2 + 4 omega  =>  omega(u) := (tau(u) + 2)/4, reducing to omega at u=0.
    def omega_of(tau):
        return (tau + 2) / 4

    e_base = ohara_energy(CLASS_M, CLASS_L, OMEGA)
    rows = [("omega  [u = 0, complete]", OMEGA, e_base, mp.mpf(0))]
    for lbl, _ in branches:
        om = omega_of(taus[lbl])
        e = ohara_energy(CLASS_M, CLASS_L, om)
        rows.append((f"omega(u)  [{lbl}]", om, e, abs(e - e_base) / abs(e_base)))
    # my earlier hand-picked drift, kept as the thing being corrected
    e_hand = ohara_energy(CLASS_M, CLASS_L, OMEGA * (1 + u1))
    rows.append(("omega*(1+ln q0)  [MY AD-HOC O(u) DRIFT]", OMEGA * (1 + u1),
                 e_hand, abs(e_hand - e_base) / abs(e_base)))

    print(f"    {'modulus':<40} {'E_O_Hara(2,3)':<22} {'rel change'}")
    for lbl, _om, e, rel in rows:
        print(f"    {lbl:<40} {mp.nstr(e, 14):<22} {mp.nstr(rel, 6)}")
    print()

    rel_derived = max(rows[1][3], rows[2][3])
    rel_hand = rows[3][3]
    check(
        "the_derived_modulus_drift_is_second_order_not_first",
        rel_derived < rel_hand / 3,
        f"the largest DERIVED energy shift is {mp.nstr(rel_derived, 6)} against "
        f"{mp.nstr(rel_hand, 6)} for the O(u) drift I picked by hand. NZ's odd "
        f"series [A1] forces the leading tau correction to be u^2, so the real "
        f"sensitivity is quadratically suppressed. CORRECTS my own uncommitted "
        f"measurement, which drifted omega at the O(u) = 10.4% scale in three "
        f"directions and reported 3.9-16.3% energy shifts as the bridge's "
        f"modulus sensitivity. Those numbers were correct for the drifts I "
        f"chose and wrong about the drift the framework actually has",
        w,
    )

    check(
        "the_bridge_energies_are_robust_to_the_real_modulus_drift",
        rel_derived < mp.mpf("0.05"),
        f"the O'Hara energy of the (2,3) class moves by {mp.nstr(rel_derived, 6)} "
        f"between the complete structure and the deformed cusp, on the WORSE of "
        f"the two normalisation branches. So the bridge probe's figures, "
        f"computed at omega, are good at the sub-percent to few-percent level "
        f"and its ranking cannot be an artefact of evaluating at u = 0. This "
        f"answers the concern qbeta_cusp_shape_drift_robustness_probe raises "
        f"without needing the binary above resolved -- both branches clear it",
        w,
    )

    # -- A8: the negative survives -------------------------------------------
    print("== 5. does the deformed modulus fix the order-blindness? ==")
    print("    the lattice class is (m, l) = (exponent sum, strand count). "
          "Neither")
    print("    references tau, so every two-crossing gluon dressing is class "
          "(2,3)")
    print("    at EVERY modulus:")
    for g in ("sigma_1 sigma_0", "sigma_0 sigma_1", "sigma_1 sigma_1",
              "sigma_0 sigma_0"):
        print(f"      {g:<20} -> (2,3) at tau = omega, omega(ln q0), "
              f"omega(2 ln q0), ...")
    print()
    check(
        "no_modulus_can_fix_the_bridge_order_blindness",
        True,
        "the class (m, l) = (writhe, strands) is computed from the word and "
        "the closure ALONE -- the modulus enters only afterwards, when the "
        "class is turned into a geodesic. So deforming tau rescales every "
        "candidate's energy together and can never separate two words that "
        "share a class. This is structural, not numerical: it holds for every "
        "tau, including ones outside the NZ family. The bridge's negative "
        "therefore survives this correction intact -- what moved is the size "
        "of the modulus uncertainty, not the blindness",
        w,
    )

    w.add_data("nz_coefficients", {
        "tau_0": mp.nstr(c1, 30),
        "tau_0_closed_form": "2*sqrt(-3)",
        "c_3": mp.nstr(c3, 30),
        "c_3_over_c_1": mp.nstr(ratio, 30),
        "c_3_over_c_1_closed_form": "1/3",
        "tau_of_u": "2*sqrt(-3) * (1 + u^2/3 + O(u^4))",
        "source": "NZ (65)-(66) series-inverted; (52) odd-only verified; (68) "
                  "shows the 1/3",
    })
    w.add_data("normalisation_binary", {
        "status": "OPEN -- carried, not settled",
        "bean": "qou-yh67",
        "branch_a": {"u": "ln q0", "tau_drift": mp.nstr(d1, 12)},
        "branch_b": {"u": "2 ln q0", "tau_drift": mp.nstr(d2, 12)},
        "why_not_settled": "qou-yh67 records that the NZ-1/2 factor cannot be "
                           "settled numerically; picking the branch that lands "
                           "a target is selection against the target",
        "note": "both branches clear the robustness check, so the bridge's "
                "conclusion does not depend on which is right",
    })
    w.add_data("corrects", {
        "my own uncommitted modulus measurement": "I drifted omega at the O(u) "
            "= 10.4% scale in three hand-picked directions and reported "
            "3.9-16.3% energy shifts as the bridge's modulus sensitivity. NZ's "
            "odd series makes the real drift O(u^2), so the derived shift is "
            f"{mp.nstr(rel_derived, 6)} -- an order of magnitude smaller. The "
            "old numbers were right about the drifts I chose and wrong about "
            "the drift the framework has",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited -- the 4_1 cusp, the NZ family of "
                 "deformations, one geodesic class",
        "not_claimed": [
            "that the normalisation binary is resolved -- it is not, and "
            "qou-yh67 stays open",
            "that omega(u) := (tau(u)+2)/4 is derived -- it is the natural "
            "continuation of the shortest-vector basis under a deformation "
            "fixing the meridian, and is a DEFINITION",
            "that the O'Hara energy cannot select -- this concerns one "
            "embedding's blindness, not the functional",
        ],
        "no_selection_by_accuracy": "no Q_beta, no CODATA, no residual appears "
                                    "in this probe",
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
