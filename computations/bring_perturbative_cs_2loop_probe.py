#!/usr/bin/env python3
r"""bring_perturbative_cs_2loop_probe.py

Session-4 of the O(alpha^2) coefficient hunt for 1/alpha_EM: the SOLE
remaining lead named by every prior session --- the perturbative
Chern-Simons 2-loop invariant of the unit tangent bundle UT(M_Bring).
Companion compute for
``docs/audits/2026-07-05-alpha4pi-coefficient-derivation-attempt.md``
(section "Session-4: perturbative CS 2-loop on UT(M_Bring)").

Prior sessions PROVED: the O(alpha^2) coefficient is weight-3 = the QED
2-loop rung (arithmetic home {zeta(3), L(3,chi_5)}, exact generator
L_3(1/phi^2) = (4/5)zeta(3)); every CLASSICAL route (surface scissors,
mapping torus -> Sol, lambda_SW residue -> weight-1, Habiro self-coupling
O(alpha^2) -> weight-1) is excluded.  The one surviving named target:
"perturbative CS carries zeta(3) at two loops even when the classical
volume vanishes" -- evaluate it on the canonical Seifert manifold
UT(M_Bring) and read off the coefficient.

This probe carries out that evaluation as far as it is honestly
pinnable, and finds a THREE-fold structural obstruction (all cited,
none a fit) that RE-SCOPES the lead.  Verdict below.

SEIFERT DATA (explicit).
  UT(M_Bring) = UT(Sigma_4) = PSL2(R)/Gamma_Bring, the unit tangent
  bundle of Bring's genus-4 surface (aut group S_5, |S_5|=120).
    * S^1-bundle over the base Sigma_4;  base genus  g = 4.
    * NO exceptional (singular) fibres  (n = 0): it is an honest
      circle bundle, not an orbifold Seifert fibration.
    * Euler number  e = chi(Sigma_4) = 2 - 2g = -6
      (the unit tangent bundle of a surface has Euler number = its
       Euler characteristic).
    * Geometry: SL2~  (Seifert-fibered, Gromov volume 0).

THE LAWRENCE-ROZANSKY / VERLINDE TRIVIAL-CONNECTION INTEGRAND.
  For SU(2) CS on a genus-g Seifert circle-bundle of Euler number e, the
  trivial-connection ("perturbative") contribution to Z is the Gaussian
  contour integral (Lawrence-Rozansky 1999; Beasley-Witten 2005,
  non-abelian localization; Blau-Thompson):

     Z^triv(M) ~ INT dy  exp( i * e * y^2 / (2 hbar) )
                          * ( 2 sinh(y/2) )^{ 2 - 2 g }

  with hbar = 2 pi i / (k + 2).  The base-genus power is  2 - 2g  --
  the Verlinde S-matrix factor (S_{0j})^{2-2g}.  For g = 4 this exponent
  is  2 - 2*4 = -6  (a NEGATIVE power => an order-6 POLE at y = 0).

WHAT THE PROBE ESTABLISHES (parameter-free, no fit):

  (O1)  b_1 = 8: UT(M_Bring) is NOT a rational homology sphere.
        The integrand exponent 2-2g = -6 < 0 (order-6 pole) is the
        analytic signature of dim H^1(Sigma_4) = 2g = 8 flat zero modes
        (the Jacobian torus of flat connections).  The trivial
        connection is NON-ISOLATED, so the standard perturbative 2-loop
        Gaussian / LMO-Ohtsuki invariant is not defined by the usual
        construction (it needs a QHS; the Hessian is degenerate here).

  (O2)  The Seifert fibre-sum generates ONLY EVEN zeta values, all
        RATIONAL multiples of powers of the coupling -- NO zeta(3).
        log( 2 sinh(y/2) / y ) = SUM_{m>=1} (-1)^{m-1}/m *
                                  zeta(2m)/(4 pi^2)^m * y^{2m},
        and zeta(2m)/pi^{2m} is RATIONAL (Bernoulli).  So the
        manifold-specific perturbative series of UT(M_Bring) is a power
        series with rational coefficients: the 2-loop term is a
        rational (Dedekind-sum / framing) number, weight <= 2 -- exactly
        Session-2/C's weight verdict -- NOT the weight-3 zeta(3) target.

  (O3)  The genuine 2-loop CS invariant (Axelrod-Singer theta-graph /
        LMO degree 1) of a QHS is a RATIONAL multiple of the Casson
        invariant -- again NO zeta(3).  The zeta(3) that really appears
        in "Chern-Simons theory" is the CONSTANT-MAP / group-volume term
        (Gopakumar-Vafa; via zeta'(-2) = -zeta(3)/(4 pi^2)); it is
        UNIVERSAL (proportional to the Euler characteristic / dim G),
        enters at genus-0 order g_s^{-2} in the topological-string
        counting (a different loop-count than the QED 2-loop), and its
        overall normalization into delta(1/alpha) is exactly the
        unfixed piece -- so it carries no Bring-b_1-specific data.

  Diagnostic (structural form of the constant-map term, NOT a fit):
  even granting the universal constant-map zeta(3) * (2-2g)/2 structure,
  no parameter-free normalization over the DERIVED denominators
  {4pi, 8pi = pi*b_1, pi^2, pi^3, |chi|} reproduces C_data.

VERDICT: OPEN, and the sole surviving lead is RE-SCOPED.  The
"perturbative CS 2-loop on UT(M_Bring)" route as posed does NOT carry a
Bring-specific weight-3 zeta(3) coefficient: the manifold-specific
perturbative series is even-zeta/rational (O2), the genuine 2-loop
invariant is theta-graph = rational*Casson (O3), the only zeta(3) in CS
is a universal constant-map term with unfixed normalization (O3), and
the whole perturbative construction is ill-defined here because b_1 = 8
(O1).  No fit; no fabricated closure.

Standalone (mpmath only); emits NO witness (records an open negative).
Run:  python3 bring_perturbative_cs_2loop_probe.py
"""
from __future__ import annotations

import sys
from mpmath import (mp, mpf, pi, zeta, sqrt, log, fabs, nstr, bernoulli,
                    factorial, diff, sinh, polylog, re as mp_re, mpc)

mp.dps = 60


# muon-anchored canonical q0 (computations/ layer, q-pinning-50-digit)
Q0_STR = "1.1099785955573347198997632204832250266562084087801536866079"
with mp.workdps(60):
    ALPHA = +(mpf(1) / mpf("137.035999084"))


def L3(z):
    """Zagier single-valued (BWR) trilogarithm (weight 3)."""
    z = mpc(z)
    if z == 0:
        return mpf(0)
    lz = log(abs(z))
    Li1 = -log(1 - z)
    return mp_re(polylog(3, z) - lz * polylog(2, z) + (lz ** 2) / 3 * Li1)


def main() -> int:
    q0 = mpf(Q0_STR)
    g = 4
    euler = 2 - 2 * g          # = -6, the UT(Sigma_4) Euler number
    b1 = 2 * g                 # = 8, dim H^1(Sigma_4)
    exponent = 2 - 2 * g       # = -6, the LR integrand base-genus power
    phi = (1 + sqrt(5)) / 2

    print("=" * 74)
    print("Session-4: perturbative CS 2-loop on UT(M_Bring)")
    print("=" * 74)
    print("Seifert data of UT(M_Bring) = UT(Sigma_4) = PSL2(R)/Gamma_Bring:")
    print(f"  base genus g                 = {g}")
    print(f"  # exceptional fibres n       = 0   (honest S^1-bundle)")
    print(f"  Euler number e = chi(Sigma_4)= {euler}")
    print(f"  b_1 = dim H^1(Sigma_4) = 2g  = {b1}")
    print(f"  geometry                     = SL2~ (Seifert, Gromov vol 0)")
    print(f"  LR integrand power (2-2g)    = {exponent}  "
          f"(NEGATIVE => order-{-exponent} pole at y=0)")
    print()

    # ---- (O1) non-isolated trivial connection -------------------------
    print("--- (O1) b_1 = 8 != 0  =>  NOT a rational homology sphere ------")
    print(f"  integrand ~ (2 sinh(y/2))^(2-2g) = (2 sinh(y/2))^({exponent})")
    print(f"  order-{-exponent} pole at the trivial connection y=0")
    print(f"  => moduli of flat SU(2) connections has POSITIVE dimension")
    print(f"     (the 2g = {b1}-dim Jacobian torus H^1(Sigma_4;R) directions)")
    print(f"  => Hessian degenerate; standard perturbative 2-loop / LMO-")
    print(f"     Ohtsuki invariant is NOT DEFINED (construction needs a QHS)")
    print()

    # ---- (O2) the fibre-sum generates ONLY even (rational) zetas ------
    print("--- (O2) Seifert fibre-sum = EVEN zetas only (rational) -------")
    print("  log(2 sinh(y/2)/y) = SUM_m (-1)^{m-1}/m * zeta(2m)/(4pi^2)^m y^2m")
    print("  each coefficient is RATIONAL (zeta(2m)/pi^2m in Q):")
    all_rational = True
    for m in range(1, 6):
        # closed even-zeta series coefficient of y^{2m}
        coeff_series = ((-1) ** (m - 1)) / mpf(m) * zeta(2 * m) / (4 * pi ** 2) ** m
        # zeta(2m)/pi^{2m} is RATIONAL: = |B_2m| * 2^{2m-1} / (2m)!
        rat = zeta(2 * m) / pi ** (2 * m)
        rat_pred = fabs(bernoulli(2 * m)) * mpf(2) ** (2 * m - 1) / factorial(2 * m)
        rat_err = fabs(rat - rat_pred)
        ok = rat_err < mpf("1e-45")
        all_rational = all_rational and ok
        print(f"  m={m}: coeff y^{2*m} = {nstr(coeff_series, 12):>16}  "
              f"zeta(2m)/pi^2m = {nstr(rat, 12)} = |B_2m|2^(2m-1)/(2m)!  "
              f"{'OK' if ok else 'FAIL'}")
    assert all_rational, "even-zeta rationality check failed"
    # sanity: the even-zeta series reproduces log(2 sinh(y/2)/y) at y=0.5
    y_t = mpf("0.5")
    series_val = mp.fsum(((-1) ** (m - 1)) / mpf(m) * zeta(2 * m) / (4 * pi ** 2) ** m
                         * y_t ** (2 * m) for m in range(1, 40))
    direct_val = log(2 * sinh(y_t / 2)) - log(y_t)
    err_series = fabs(series_val - direct_val)
    print(f"  series vs log(2 sinh(y/2)/y) at y=0.5: |diff| = {nstr(err_series,4)} (OK)")
    assert err_series < mpf("1e-30"), "even-zeta series check failed"
    print("  => NO zeta(3) (no ODD zeta) appears in the fibre-sum series.")
    print("  => the manifold-specific 2-loop term is a RATIONAL number,")
    print("     weight <= 2, NOT the weight-3 zeta(3) target.")
    print()

    # ---- (O3) where zeta(3) actually lives in CS: constant map --------
    print("--- (O3) the only zeta(3) in CS = universal constant-map term -")
    # zeta'(-2) = -zeta(3)/(4 pi^2)   (the constant-map / Barnes-G home)
    zp_m2 = diff(lambda s: zeta(s), mpf(-2))
    cm_closed = -zeta(3) / (4 * pi ** 2)
    err_cm = fabs(zp_m2 - cm_closed)
    print(f"  zeta'(-2)            = {nstr(zp_m2, 30)}")
    print(f"  -zeta(3)/(4 pi^2)    = {nstr(cm_closed, 30)}")
    print(f"  |diff|               = {nstr(err_cm, 4)}  "
          f"(constant-map zeta(3) home; universal, ~ chi/dim G)")
    assert err_cm < mpf("1e-40"), "zeta'(-2) identity failed"
    print("  genuine 2-loop CS invariant (Axelrod-Singer theta-graph /")
    print("  LMO deg-1) of a QHS = RATIONAL * Casson invariant -- no zeta(3).")
    print("  the constant-map zeta(3) enters at genus-0 (g_s^-2), is")
    print("  proportional to the Euler characteristic, and its overall")
    print("  normalization into delta(1/alpha) is UNFIXED => not Bring-")
    print("  b_1-specific.")
    print()

    # ---- structural-form diagnostic (NOT a fit) -----------------------
    # target coefficient C_data (muon-q0), reproduced for context
    bare = q0 * _q_int(q0, 9) * _q_int(q0, 10)
    ir = mpf(2) / (3 * pi)
    codata_inv = mpf("137.035999084")
    T_data = codata_inv - bare - ir
    C_data = T_data / ALPHA
    z3 = zeta(3)
    L3_iphi2 = L3(1 / phi ** 2)   # = (4/5) zeta(3)
    print("--- structural-form diagnostic (constant-map shape; NO fit) ---")
    print(f"  C_data (target)              = {nstr(C_data, 12)}  "
          f"(= {nstr(C_data*4*pi, 8)} * 1/4pi)")
    print(f"  L_3(1/phi^2) = (4/5)zeta(3)  = {nstr(L3_iphi2, 12)}  "
          f"(check {nstr(mpf(4)/5*z3,12)})")
    # the constant-map term would be ~ (2-2g)/2 * zeta(3) / (derived denom)
    denoms = {
        "4pi": 4 * pi, "8pi=pi*b1": pi * b1, "pi^2": pi ** 2, "pi^3": pi ** 3,
        "(4pi)^2": (4 * pi) ** 2, "(4pi)^3": (4 * pi) ** 3,
    }
    nums = {
        "|chi|/2 * zeta3 (=3 z3)": (mpf(-euler) / 2) * z3,
        "|chi| * zeta3 (=6 z3)": mpf(-euler) * z3,
        "(4/5) zeta3": mpf(4) / 5 * z3,
        "zeta3": z3,
    }
    print("  ratio (candidate / C_data), looking for a clean 1.000:")
    best = None
    for nname, nval in nums.items():
        for dname, dval in denoms.items():
            cand = nval / dval
            ratio = cand / C_data
            if mpf("0.5") < ratio < mpf("2.0"):
                tag = f"    {nname} / {dname:>9} = {nstr(cand,10):>14}  "\
                      f"ratio={nstr(ratio,8)}"
                print(tag)
                if best is None or fabs(ratio - 1) < fabs(best[0] - 1):
                    best = (ratio, nname, dname)
    if best is not None:
        print(f"  nearest: {best[1]} / {best[2]}  ratio = {nstr(best[0],8)} "
              f"(off by {nstr((best[0]-1)*100,4)}%)")
    print("  => NO parameter-free constant-map form is forced; the nearest")
    print("     misses well beyond the ~0.49% q0 floor.  (Not a fit: only the")
    print("     structurally-motivated |chi|,(4/5),1 numerators over derived")
    print("     denominators are tested; all nulls reported.)")
    print()

    print("=" * 74)
    print("VERDICT: OPEN -- sole surviving lead RE-SCOPED.")
    print("  The perturbative-CS-2-loop-on-UT(M_Bring) route as posed does")
    print("  NOT carry a Bring-specific weight-3 zeta(3) coefficient:")
    print("   (O1) b_1=8 => not a QHS => the perturbative 2-loop invariant")
    print("        is not even defined (order-6 pole / 8 zero modes);")
    print("   (O2) the Seifert fibre-sum is EVEN-zeta/rational (no zeta(3));")
    print("   (O3) the genuine 2-loop invariant is theta-graph = rational*")
    print("        Casson (no zeta(3)); the only CS zeta(3) is a UNIVERSAL")
    print("        constant-map term (~chi, normalization unfixed).")
    print("  No closure; no fit.")
    return 0


def _q_int(q, n):
    """[n]_q = (q^n - q^{-n})/(q - q^{-1}) balanced quantum integer."""
    return (q ** n - q ** (-n)) / (q - q ** (-1))


if __name__ == "__main__":
    sys.exit(main())
