#!/usr/bin/env python3
"""The Borromean trace with z SYMBOLIC — and the first non-circular measurement
of the Markov parameter from the mass channel.

BEAN `qou-cds1`. Owner-requested (2026-08-31): "re-derive the Borromean trace
with z symbolic".

WHY IT WAS NEEDED. `m_p_substrate_identity_50dps.trM_borromean(q)` returns a
closed form in `h = q - 1/q` ALONE, with no z parameter: convention D was
substituted before the formula was written down. So `y_(1^3) = 0` is baked into
`F_Bor -> canonical_mass`, and any attempt to MEASURE the two-row cap through
that route measures its own assumption. Re-deriving with z free removes exactly
that circularity.

THE CONTROL, and it is the reason this file can be trusted: at z = z_D the
symbolic form must reproduce `BorromeanMarkovTrace.lean`'s closed form
`(4 + h^2 - 3h^4 - h^6)/(h^2 + 4)`. It does, with symbolic difference EXACTLY
zero -- not to a tolerance, identically.

A CORRECTION TO THE JOINT-DETERMINACY FRAMING (PR #6144). That PR solved a 3x3
system treating `(y_3, y_21, y_111)` as three unknowns fixed by three
independent functionals, and concluded the cap is "jointly determined". True as
linear algebra, but it is NOT how the weights behave: for a NORMALISED MARKOV
TRACE the 3x3 Markov system already consumes all freedom, so the weights are a
ONE-PARAMETER family in z. `y_(1^3)` is a function of z alone. The mass and
decay channels therefore do not measure three independent weights -- they each
determine THE SAME single parameter, and the system is OVER-determined rather
than jointly determined. That is a sharper statement and a harder test.

THE THREE DETERMINATIONS OF ONE PARAMETER. The q0 pin used here is the MUON
pin, because it is the only convention-free one: q0 comes from
`m_mu/m_e = Vol(4_1)/hbar_q^2`, pure geometry, with no trace anywhere in it.
The proton pin cannot be used -- it is fixed THROUGH `F_Bor`, so it presupposes
the convention this file is testing.

    z from the CAP    (y_(1^3) = 0, derived)     0.6126880506382724
    z from MASS       (measured m_p, this file)  0.6128126508361218
    z from DECAY      (measured Q_beta)          0.998500302563013

SO THE ANOMALY IS LOCALISED TO THE DECAY CHANNEL. Mass lands within 0.0203 % of
the derived cap; decay misses by 63 %. Whatever is wrong, it is not the
convention -- an independent, non-circular measurement puts z essentially where
the cap puts it.

WHAT IS *NOT* CLAIMED, and the sensitivity is why. The mass channel is a WEAK
probe of z: d ln(tr_M)/d ln z = 0.00119 against the decay channel's 1.206, a
factor of 1012. So a tr_M residual of 2.42e-7 opens out to 2.03e-4 in z. The
agreement is real but must be quoted with that leverage attached; this file
does NOT claim the mass channel confirms the cap to 1e-7.

AND THE MASS RESIDUAL IS NOT ZERO. 2.42e-7 relative in tr_M is roughly 21x the
known mu-p substrate tension (11.5 ppb), so it is not obviously that tension and
is not obviously experimental. Identifying it is open, and this file states it
as a residual rather than absorbing it.

Anchor: MUON pin, deliberately and exceptionally -- see above. This is the
E1/E2 comparison carve-out of the 2026-08-30 directive: the file's purpose is
to test a convention, which the proton pin presupposes.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "hecke"),
                str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from hecke_character_symbolic import q_character_on_braid_word as chi  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

PARTS = [(3,), (2, 1), (1, 1, 1)]
Q = sp.Symbol("q", positive=True)
Z = sp.Symbol("z")


def borromean_symbolic():
    """(tr_M(beta_Bor)(z, q), {lambda: y_lambda(z)}, {lambda: chi^lambda(beta_Bor)})."""
    bor = [(0, "sigma"), (1, "sigma_inv")] * 3          # (s0 s1^-1)^3
    X = {lam: sp.cancel(sp.together(chi(lam, bor, Q))) for lam in PARTS}
    # the 3x3 normalised-Markov system: (tr 1, tr s0, tr s0s1) = (1, z, z^2)
    classes = {"1": [], "s0": [(0, "sigma")], "s0s1": [(0, "sigma"), (1, "sigma")]}
    target = {"1": sp.Integer(1), "s0": Z, "s0s1": Z ** 2}
    M = [[sp.cancel(sp.together(chi(lam, w, Q))) for lam in PARTS]
         for w in classes.values()]
    sol = sp.Matrix(M).solve(sp.Matrix([target[c] for c in classes]))
    Y = {lam: sp.cancel(sp.together(sol[i])) for i, lam in enumerate(PARTS)}
    trM = sp.cancel(sp.together(sum(Y[lam] * X[lam] for lam in PARTS)))
    return trM, Y, X


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    trM, Y, X = borromean_symbolic()
    h = Q - 1 / Q
    zD_sym = Q ** 3 / (Q ** 2 + 1)

    print("[1] chi^lambda(beta_Bor)")
    for lam in PARTS:
        print(f"    chi^{str(lam):<10} = {sp.factor(X[lam])}")
    check("chi^(3) = chi^(1^3) = 1 (mass sees y_3 + y_(1^3))",
          sp.simplify(X[(3,)] - 1) == 0 and sp.simplify(X[(1, 1, 1)] - 1) == 0)

    print("\n[2] the weights are a ONE-parameter family in z")
    for lam in PARTS:
        print(f"    y_{str(lam):<10} = {sp.simplify(Y[lam])}")
    roots = sp.solve(sp.numer(sp.together(Y[(1, 1, 1)])), Z)
    check("y_(1^3)(z) = 0 has exactly the two known roots {q, z_D}",
          len(roots) == 2 and any(sp.simplify(r - zD_sym) == 0 for r in roots),
          f"roots = {[sp.simplify(r) for r in roots]}")

    print(f"\n[3] tr_M(beta_Bor)(z, q) =\n    {sp.factor(trM)}")

    # THE CONTROL — symbolic, not numeric.
    lean = (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)
    resid = sp.simplify(sp.cancel(sp.together(trM.subs(Z, zD_sym) - lean)))
    check("CONTROL: at z = z_D this IS BorromeanMarkovTrace.lean's closed form",
          resid == 0, f"symbolic difference = {resid}")

    # --- the non-circular measurement, at the MUON pin ---
    from qou_substrate import constants as C  # noqa: E402
    r_mu = mp.mpf(C.MASS_RATIO_MU_E_STR)
    r_p = mp.mpf(str(getattr(C, "MASS_RATIO_P_E_STR", C.MASS_RATIO_P_E)))
    vol41 = 2 * mp.clsin(2, mp.pi / 3)
    q0 = 1 / (1 - mp.sqrt(vol41 / r_mu))          # NO trace convention anywhere
    zD = q0 ** 3 / (q0 ** 2 + 1)

    f = sp.lambdify(Z, trM.subs(Q, sp.Float(str(q0), 50)), "mpmath")
    df = sp.lambdify(Z, sp.diff(trM, Z).subs(Q, sp.Float(str(q0), 50)), "mpmath")

    b2, b3 = q0 + 1 / q0, q0 ** 2 + 1 + 1 / q0 ** 2
    trM_req = ((r_p / 2 + 6) / r_mu) / (b2 * b3 / q0 ** 3)
    z_mass = mp.findroot(lambda zz: f(zz) - trM_req, zD)

    z_decay = mp.mpf("0.998500302563013")
    print(f"\n[4] THREE determinations of ONE parameter (muon pin, q0 = {mp.nstr(q0, 18)})")
    print(f"    z from the CAP  (y_(1^3)=0, derived) = {mp.nstr(zD, 18)}")
    print(f"    z from MASS     (measured m_p)       = {mp.nstr(z_mass, 18)}"
          f"   rel {mp.nstr(abs(z_mass - zD) / zD * 100, 6)} %")
    print(f"    z from DECAY    (measured Q_beta)    = {mp.nstr(z_decay, 18)}"
          f"   rel {mp.nstr(abs(z_decay - zD) / zD * 100, 6)} %")
    check("MASS lands within 0.05 % of the derived cap",
          abs(z_mass - zD) / zD < mp.mpf("5e-4"),
          f"{mp.nstr(abs(z_mass - zD) / zD * 100, 6)} %")
    check("DECAY does NOT (the anomaly is localised there, not in the convention)",
          abs(z_decay - zD) / zD > mp.mpf("0.5"),
          f"{mp.nstr(abs(z_decay - zD) / zD * 100, 6)} %")

    # sensitivity — how much the mass agreement is worth
    sens_mass = df(zD) * zD / f(zD)
    sens_decay = (2 * q0 / (q0 ** 2 + 1)) * zD / ((-q0 ** 2 + 2 * q0 * zD + 1) / (q0 ** 2 + 1))
    ratio = abs(sens_decay / sens_mass)
    print(f"\n[5] SENSITIVITY — what the agreement is worth")
    print(f"    d ln tr_M / d ln z = {mp.nstr(sens_mass, 8)}   (mass)")
    print(f"    d ln g    / d ln z = {mp.nstr(sens_decay, 8)}   (decay)")
    print(f"    mass is {mp.nstr(ratio, 6)}x LESS sensitive to z")
    check("the mass channel is >100x less sensitive to z than decay "
          "(so quote its agreement WITH this leverage)", ratio > 100,
          f"{mp.nstr(ratio, 6)}x")

    wb = WitnessBuilder("qbeta-z-symbolic-borromean-crosscheck", engine="sympy+mpmath")
    wb.set_description(
        "The Borromean Markov trace re-derived with the Ocneanu parameter z SYMBOLIC, "
        "removing the circularity in the committed closed form (which has convention D "
        "substituted and carries no z). Controls exactly against "
        "BorromeanMarkovTrace.lean at z = z_D. Then measures z from the mass channel "
        "at the CONVENTION-FREE muon pin: it lands 0.0203 % from the derived cap while "
        "the decay channel misses by 63 %, localising the Q_beta anomaly to the decay "
        "channel rather than to the convention. Corrects PR #6144's joint-determinacy "
        "framing: the weights are a ONE-parameter family, so the system is "
        "over-determined, not jointly determined.")
    wb.add_data("trM_symbolic_in_z", str(sp.factor(trM)))
    wb.add_data("y_lambda_of_z", {str(k): str(sp.simplify(v)) for k, v in Y.items()})
    wb.add_data("chi_lambda_borromean", {str(k): str(sp.factor(v)) for k, v in X.items()})
    wb.add_data("control_symbolic_difference_vs_lean", str(resid))
    wb.add_data("q0_muon_pin", mp.nstr(q0, 30))
    wb.add_data("z_from_cap_derived", mp.nstr(zD, 25))
    wb.add_data("z_from_mass_measured", mp.nstr(z_mass, 25))
    wb.add_data("z_from_decay_measured", mp.nstr(z_decay, 25))
    wb.add_data("mass_vs_cap_rel_pct", mp.nstr(abs(z_mass - zD) / zD * 100, 10))
    wb.add_data("decay_vs_cap_rel_pct", mp.nstr(abs(z_decay - zD) / zD * 100, 10))
    wb.add_data("sensitivity_dln_trM_dln_z", mp.nstr(sens_mass, 12))
    wb.add_data("sensitivity_dln_g_dln_z", mp.nstr(sens_decay, 12))
    wb.add_data("mass_is_less_sensitive_by", mp.nstr(ratio, 10))
    wb.add_data("residual_not_absorbed",
                "tr_M residual 2.42e-7 relative is ~21x the mu-p substrate tension "
                "(11.5 ppb), so it is not obviously that tension and not obviously "
                "experimental. Stated as a residual, not absorbed.")
    wb.add_data("why_muon_pin",
                "the proton pin is fixed THROUGH F_Bor and therefore presupposes the "
                "convention under test; the muon pin is m_mu/m_e = Vol(4_1)/hbar_q^2, "
                "pure geometry, no trace. E1/E2 carve-out of the 2026-08-30 directive.")
    wb.add_data("free_parameters", 0)
    wb.add_data("q0Anchor", "muon")
    for c in checks:
        wb.add_assertion(c["name"], computed=1 if c["passed"] else 0,
                         expected=1, tolerance=0, source=c["detail"] or None)
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
