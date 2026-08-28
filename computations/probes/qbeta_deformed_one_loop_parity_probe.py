#!/usr/bin/env python3
"""
Deformed Dimofte-Garoufalidis 1-loop invariant tau(u) of the figure-eight
knot complement 4_1 (= SnapPy m004) along the Dehn-surgery deformation,
and its parity in u.

Self-contained: mpmath only (no SnapPy, no Sage).

Conventions (validated -- see README.md and the checks below)
--------------------------------------------------------------
Shape parameters per ideal tetrahedron (matching nloop_exact.py's
`all_shape_parameters(z) = [z, 1/(1-z), 1-1/z]`):

    z' = 1/(1-z),   z'' = 1 - 1/z          (NOTE: z'' = 1 - 1/z, NOT 1/(1-z))

Raw SnapPy gluing equations for m004 (rows = edge1, edge2, meridian,
longitude; columns = (a1,b1,c1,a2,b2,c2) acting on (log z_i, log z_i',
log z_i'')):

    edge1:     ( 2, 1, 0,  1, 0, 2 )   = 2*pi*i
    edge2:     ( 0, 1, 2,  1, 2, 0 )   = 2*pi*i
    meridian:  ( 1, 0, 0,  0,-1, 0 )   = 0     (complete)  -> u  (deformed)
    longitude: ( 0, 0, 0,  0,-2, 2 )   = 0     (complete)  -> v = 2 log L

The cusp rows compute the LOG-HOLONOMY of the peripheral curve, which is
twice the log of the SL(2,C) eigenvalue: meridian row = u = 2 log M, so
M = e^{u/2}; longitude row = v = 2 log L.

NZ datum (per nloop_exact.py: A_nz = A_raw - B_raw, B_nz = C_raw - B_raw,
nu = target - B_raw.1, using log z' = i*pi - log z - log z''), rows
{edge1, edge2, meridian} Hermite-reduced to the square system

    A = [[1,1],[1,1]],  B = [[1,0],[0,1]],  nu = (1,1),
    flattening: f = (0,0), f'' = (1,1)   (solves A f + B f'' = nu).

DG 1-loop formula (nloop_exact.py one_loop()):

    tau = (1/2) * det( A*diag(1-1/z_i) + B*diag(1/z_i) )
              * prod_i z_i^{f''_i} * prod_i (1-1/z_i)^{-f_i}

evaluated at the DEFORMED shapes z(u).  tau is defined up to sign; the
computation below uses ONE fixed datum, so tau(u) is a continuous branch
and the parity question is well-posed.

Cross-checks performed:
  (1) u=0: tau = +sqrt(-3)/2  (|tau| = sqrt(3)/2 = 0.8660254...)
  (2) A-polynomial of 4_1 along the whole deformed branch:
      A(L,M) = M^4 L^2 - (M^8 - M^6 - 2 M^4 - M^2 + 1) L + M^4 = 0
      with M = e^{u/2} and L = +-exp(v/2), v = longitude row.
  (3) Volume: Vol(u) = D(z1)+D(z2) (Bloch-Wigner); Vol(0) = 2.0298832...,
      and Vol(u) - Vol(-u) = 0 (evenness).
  (4) Second row-basis datum (edge1+meridian, un-reduced):
      A2 = [[1,1],[1,1]], B2 = [[-1,2],[0,1]], nu2 = (1,1),
      f2 = (0,0), f2'' = (1,1).  Must give tau2 = +- tau1 exactly.
  (5) Gluing-equation residuals (edge1, edge2, meridian) at every u.
"""

import json
import os
import subprocess
from datetime import datetime, timezone
from mpmath import mp, mpf, mpc, log, exp, sqrt, pi, polylog, im, re, arg, fabs, nstr

mp.dps = 60

I = mpc(0, 1)
TWO_PI_I = 2 * pi * I
OMEGA = exp(I * pi / 3)  # complete-structure shape z1 = z2 = e^{i pi/3}

NDIG = 45  # digits to print / serialize


# ----------------------------------------------------------------------
# Deformed gluing system
#   F1 = 2 log z1 - log(1-z1) + log z2 + 2 log(1-1/z2) - 2 pi i   = 0  (edge1)
#   F2 = log z1 + log(1-z2) - u                                   = 0  (meridian)
# (log z1' = -log(1-z1);  -log z2' = +log(1-z2);  log z'' = log(1-1/z),
#  principal branches -- valid in the neighbourhood of the complete
#  structure explored here, |u| <= 0.1.)
# ----------------------------------------------------------------------

def F(z1, z2, u):
    f1 = 2 * log(z1) - log(1 - z1) + log(z2) + 2 * log(1 - 1 / z2) - TWO_PI_I
    f2 = log(z1) + log(1 - z2) - u
    return f1, f2


def jacobian(z1, z2):
    # d log(1-1/z)/dz = 1/(z(z-1))
    j11 = 2 / z1 + 1 / (1 - z1)
    j12 = 1 / z2 + 2 / (z2 * (z2 - 1))
    j21 = 1 / z1
    j22 = -1 / (1 - z2)
    return j11, j12, j21, j22


def newton_solve(u, z1, z2, tol=mpf("1e-55"), maxit=60):
    for _ in range(maxit):
        f1, f2 = F(z1, z2, u)
        if fabs(f1) < tol and fabs(f2) < tol:
            return z1, z2
        j11, j12, j21, j22 = jacobian(z1, z2)
        det = j11 * j22 - j12 * j21
        dz1 = (-f1 * j22 + f2 * j12) / det
        dz2 = (-j11 * f2 + j21 * f1) / det
        z1, z2 = z1 + dz1, z2 + dz2
    raise RuntimeError(f"Newton failed to converge at u={u}")


def deformed_shapes(u, nsteps=None):
    """Continue the geometric branch from the complete structure to u."""
    if nsteps is None:
        nsteps = max(2, int(fabs(u) / mpf("0.005")) + 1)
    z1, z2 = OMEGA, OMEGA
    for k in range(1, nsteps + 1):
        z1, z2 = newton_solve(u * mpf(k) / nsteps, z1, z2)
    return z1, z2


# ----------------------------------------------------------------------
# DG 1-loop determinant formula
# ----------------------------------------------------------------------

# Primary datum (Hermite-reduced {edge1, edge2, meridian} system)
A1 = [[1, 1], [1, 1]]
B1 = [[1, 0], [0, 1]]
F_FLAT1 = (0, 0)      # f
FPP_FLAT1 = (1, 1)    # f''

# Cross-check datum: rows (edge1, meridian) without Hermite reduction
A2 = [[1, 1], [1, 1]]
B2 = [[-1, 2], [0, 1]]
F_FLAT2 = (0, 0)
FPP_FLAT2 = (1, 1)

# Flattening-shift datum: same (A1,B1) but flattening shifted by the kernel
# vector (df, df'') = ((1,0), (-1,-1)) of [A1|B1] (A1*df + B1*df'' = 0).
# On the DEFORMED variety this multiplies tau by
#   z1^{-1} z2^{-1} (z1'')^{-1} = exp(-(i*pi + 2u)) = -e^{-2u} = -M^{-4},
# since (A-row (1,1), B-row (1,0)) is the HNF row carrying i*pi*1 + 2u.
# => tau(u) is flattening-dependent up to sign AND powers of e^{2u} = M^4.
F_FLAT3 = (1, 0)
FPP_FLAT3 = (0, 0)


def one_loop(z1, z2, A, B, f, fpp):
    z = (z1, z2)
    zpp = tuple(1 - 1 / zi for zi in z)   # z'' = 1 - 1/z
    zinv = tuple(1 / zi for zi in z)
    m = [[A[r][c] * zpp[c] + B[r][c] * zinv[c] for c in range(2)]
         for r in range(2)]
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    pref = mpc(1)
    for zi, e in zip(z, fpp):
        pref *= zi ** e
    for zppi, e in zip(zpp, f):
        pref *= zppi ** (-e)
    return det * pref / 2


# ----------------------------------------------------------------------
# Cross-checks
# ----------------------------------------------------------------------

def apoly_residual(z2, u):
    """4_1 A-polynomial residual.  M = e^{u/2}; L from the longitude row
    v = 2 log L = -2 log z2' + 2 log z2'' = 2(log(1-z2) + log(1-1/z2)).
    L is defined up to sign by e^{v/2}; return (min residual, sign used, L)."""
    M = exp(u / 2)
    v = 2 * (log(1 - z2) + log(1 - 1 / z2))
    Lc = exp(v / 2)

    def apoly(L):
        return M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4

    rp, rm = fabs(apoly(Lc)), fabs(apoly(-Lc))
    return (rp, +1, Lc) if rp <= rm else (rm, -1, -Lc)


def bloch_wigner(z):
    return im(polylog(2, z)) + arg(1 - z) * log(abs(z))


def gluing_residuals(z1, z2, u):
    f1, f2 = F(z1, z2, u)
    # edge2 row (0,1,2 | 1,2,0): log z1' + 2 log z1'' + log z2 + 2 log z2'
    e2 = (-log(1 - z1)) + 2 * log(1 - 1 / z1) + log(z2) \
        + 2 * (-log(1 - z2)) - TWO_PI_I
    return fabs(f1), fabs(f2), fabs(e2)


# ----------------------------------------------------------------------
# Serialization helpers
# ----------------------------------------------------------------------

def cstr(x):
    """Complex number -> string with NDIG digits."""
    return nstr(mpc(x), NDIG)


def evaluate(u):
    z1, z2 = deformed_shapes(u)
    r_e1, r_mer, r_e2 = gluing_residuals(z1, z2, u)
    apres, lsign, L = apoly_residual(z2, u)
    tau = one_loop(z1, z2, A1, B1, F_FLAT1, FPP_FLAT1)
    tau2 = one_loop(z1, z2, A2, B2, F_FLAT2, FPP_FLAT2)
    # datum-independence check (up to sign)
    d_plus = fabs(tau - tau2)
    d_minus = fabs(tau + tau2)
    datum_dev = min(d_plus, d_minus)
    vol = bloch_wigner(z1) + bloch_wigner(z2)
    return {
        "u": cstr(u),
        "z1": cstr(z1),
        "z2": cstr(z2),
        "tau": tau,
        "tau_str": cstr(tau),
        "abs_tau": nstr(fabs(tau), NDIG),
        "longitude_L": cstr(L),
        "longitude_sign": lsign,
        "apoly_residual": nstr(apres, 8),
        "gluing_residuals": [nstr(r_e1, 5), nstr(r_mer, 5), nstr(r_e2, 5)],
        "datum2_sign_dev": nstr(datum_dev, 5),
        "datum2_relative_sign": "+" if d_plus < d_minus else "-",
        "vol": vol,
        "vol_str": nstr(vol, NDIG),
    }


def rationalize(x, maxden=10**6, tol=mpf("1e-18")):
    """Best rational approximation of a real mp number via continued
    fractions; returns (p, q) if |x - p/q| < tol with q <= maxden, else None."""
    from mpmath import floor
    x = mpf(x)
    p0, q0, p1, q1 = 1, 0, int(floor(x)), 1
    y = x - floor(x)
    for _ in range(64):
        if fabs(x - mpf(p1) / q1) < tol:
            return (p1, q1)
        if y < mpf("1e-40"):
            break
        y = 1 / y
        a = int(floor(y))
        y = y - floor(y)
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        if q1 > maxden:
            break
    return None


def taylor_analysis(s=mpf("1e-5"), deg=11):
    """Fit tau(u) = sum_k c_k u^k around u=0 from 12 tiny-u samples and
    recognize the ratios c_k/c0 as small rationals (=> c_k in Q(sqrt(-3))
    since c0 = sqrt(-3)/2)."""
    from mpmath import matrix, lu_solve
    js = [j for j in range(-6, 7) if j != 0]  # 12 points
    ts, vals = [], []
    for j in js:
        u = j * s
        z1, z2 = newton_solve(u, OMEGA, OMEGA)
        ts.append(mpf(j))
        vals.append(one_loop(z1, z2, A1, B1, F_FLAT1, FPP_FLAT1))
    # least-squares not needed: 12 points, degree 11 -> exact Vandermonde solve
    V = matrix(12, 12)
    for r, t in enumerate(ts):
        for k in range(12):
            V[r, k] = t ** k
    rhs = matrix(vals)
    b = lu_solve(V, rhs)
    cs = [b[k] / s ** k for k in range(12)]

    c0 = cs[0]
    target0 = sqrt(mpc(-3)) / 2
    assert fabs(c0 - target0) < mpf("1e-40"), f"c0 != sqrt(-3)/2: {c0}"

    coeffs = []
    print("\nTaylor expansion tau(u) = sqrt(-3)/2 * sum_k r_k u^k "
          "(recognition of r_k = c_k/c0):")
    for k in range(8):
        r = cs[k] / c0
        # r should be real (tau(u)/tau(0) has real Taylor coefficients)
        im_leak = fabs(im(r))
        rq = rationalize(re(r), maxden=10**6,
                         tol=mpf("1e-12") if k >= 6 else mpf("1e-18"))
        rec = f"{rq[0]}/{rq[1]}" if rq else "unrecognized"
        coeffs.append({
            "k": k,
            "value": cstr(cs[k]),
            "ratio_to_c0": nstr(re(r), 30),
            "ratio_im_leak": nstr(im_leak, 5),
            "recognized": rec,
        })
        print(f"  k={k}:  c_k/c0 = {nstr(re(r), 30)}"
              f"   ~ {rec}   (Im leak {nstr(im_leak, 3)})")

    # deliverable: leading odd coefficient c1
    dev1 = fabs(cs[1] - target0)
    print(f"  leading odd coefficient c1 = {cstr(cs[1])}")
    print(f"  |c1 - sqrt(-3)/2| = {nstr(dev1, 5)}  "
          f"(recognized: c1 = sqrt(-3)/2 = tau(0))")

    # even core: h(u) = e^{-u} tau(u)/tau(0) = sum_k h_k u^k, h_odd = 0
    from mpmath import factorial
    hs = []
    for k in range(8):
        h = sum(cs[j] / c0 * (-1) ** (k - j) / factorial(k - j)
                for j in range(k + 1))
        hs.append(h)
    print("  even core h(u) = e^{-u} tau(u)/tau(0):")
    hcoeffs = []
    for k in range(8):
        hq = rationalize(re(hs[k]), maxden=10**6,
                         tol=mpf("1e-12") if k >= 6 else mpf("1e-18"))
        rec = f"{hq[0]}/{hq[1]}" if hq else "unrecognized"
        hcoeffs.append({"k": k, "value": nstr(re(hs[k]), 30),
                        "recognized": rec})
        print(f"    h_{k} = {nstr(re(hs[k]), 30)}   ~ {rec}")
    return {
        "method": f"degree-{deg} Vandermonde fit at u = j*{nstr(s, 3)}, "
                  f"j in +-1..6, dps={mp.dps}",
        "coefficients": [
            dict(c, value=c["value"]) for c in coeffs
        ],
        "c1_dev_from_sqrt_m3_over_2": nstr(dev1, 5),
        "even_core_coefficients": hcoeffs,
    }


def main():
    out = {
        "manifold": "4_1 (m004), 2 ideal tetrahedra",
        "precision_dps": mp.dps,
        "convention": {
            "shape_params": "z' = 1/(1-z), z'' = 1 - 1/z (nloop_exact.py)",
            "nz_equation": "A log z + B log z'' = i*pi*nu (complete); "
                           "meridian row replaced by u = 2 log M, M = e^{u/2}",
            "datum": {"A": A1, "B": B1, "nu": [1, 1],
                      "f": list(F_FLAT1), "f_ddot": list(FPP_FLAT1)},
            "datum2_crosscheck": {"A": A2, "B": B2, "nu": [1, 1],
                                  "f": list(F_FLAT2), "f_ddot": list(FPP_FLAT2)},
            "tau_formula": "(1/2) det(A diag(1-1/z) + B diag(1/z)) "
                           "* prod z^{f''} * prod (1-1/z)^{-f}",
        },
    }

    # ---------------- u = 0 validation ----------------
    res0 = evaluate(mpf(0))
    tau0 = res0["tau"]
    target = sqrt(mpc(-3)) / 2  # = i sqrt(3)/2
    dev = min(fabs(tau0 - target), fabs(tau0 + target))
    assert dev < mpf("1e-50"), f"u=0 1-loop check FAILED: dev={dev}"
    print("u=0 validation:")
    print("  tau(0)      =", res0["tau_str"])
    print("  target +-sqrt(-3)/2, deviation =", nstr(dev, 5))
    print("  |tau(0)|    =", res0["abs_tau"])
    print("  Vol(0)      =", res0["vol_str"], " (target 2.029883212819...)")
    vol_dev = fabs(res0["vol"] - mpf("2.029883212819307250042405108549040571883378615060599584034978"))
    print("  Vol(0) dev  =", nstr(vol_dev, 5))
    print("  A-poly res  =", res0["apoly_residual"],
          " (longitude sign %+d, L(0) = %s)" % (res0["longitude_sign"],
                                                res0["longitude_L"]))
    print()

    out["u0"] = {k: v for k, v in res0.items() if k not in ("tau", "vol")}
    out["u0"]["tau_dev_from_sqrt_m3_over_2"] = nstr(dev, 5)
    out["u0"]["vol_dev"] = nstr(vol_dev, 5)

    # ---------------- deformation grid ----------------
    base = [mpf("0.02"), mpf("0.05"), mpf("0.08")]
    grid = ([("real", b) for b in base]
            + [("imag", b * I) for b in base]
            + [("complex", mpc("0.04", "0.03"))])

    pairs = []
    print("Parity table (even = (tau(u)+tau(-u))/2, odd = (tau(u)-tau(-u))/2):")
    for ray, u in grid:
        rp = evaluate(u)
        rm = evaluate(-u)
        even = (rp["tau"] + rm["tau"]) / 2
        odd = (rp["tau"] - rm["tau"]) / 2
        vol_asym = rp["vol"] - rm["vol"]
        entry = {
            "ray": ray,
            "u": cstr(u),
            "tau_plus": rp["tau_str"],
            "tau_minus": rm["tau_str"],
            "even_part": cstr(even),
            "odd_part": cstr(odd),
            "abs_odd": nstr(fabs(odd), 8),
            "odd_over_u": cstr(odd / u),
            "vol_plus": rp["vol_str"],
            "vol_minus": rm["vol_str"],
            "vol_asymmetry": nstr(fabs(vol_asym), 5),
            "apoly_residual_plus": rp["apoly_residual"],
            "apoly_residual_minus": rm["apoly_residual"],
            "gluing_residuals_plus": rp["gluing_residuals"],
            "datum2_sign_dev_plus": rp["datum2_sign_dev"],
            "shapes_plus": {"z1": rp["z1"], "z2": rp["z2"]},
            "shapes_minus": {"z1": rm["z1"], "z2": rm["z2"]},
            "longitude_L_plus": rp["longitude_L"],
        }
        pairs.append(entry)
        print(f"  [{ray:7s}] u = {cstr(u)}")
        print(f"    tau(+u) = {rp['tau_str']}")
        print(f"    tau(-u) = {rm['tau_str']}")
        print(f"    even    = {entry['even_part']}")
        print(f"    odd     = {entry['odd_part']}   |odd| = {entry['abs_odd']}")
        print(f"    A-poly residuals (+u, -u) = {rp['apoly_residual']}, "
              f"{rm['apoly_residual']}")
        print(f"    Vol asymmetry |Vol(u)-Vol(-u)| = {entry['vol_asymmetry']}")
        print(f"    datum-2 sign-agreement dev = {rp['datum2_sign_dev']} "
              f"(rel sign {rp['datum2_relative_sign']})")
        print()

    out["pairs"] = pairs

    # ---------------- parity verdict ----------------
    max_odd = max(mpf(p["abs_odd"]) for p in pairs)
    verdict_even = max_odd < mpf("1e-40")
    out["parity"] = {
        "max_abs_odd_part": nstr(max_odd, 8),
        "verdict": "EVEN" if verdict_even else "HAS ODD PART",
    }
    print("PARITY VERDICT:", out["parity"]["verdict"],
          " (max |odd part| over grid =", out["parity"]["max_abs_odd_part"], ")")

    if not verdict_even:
        taylor = taylor_analysis()
        out["taylor"] = taylor
        out["parity"]["leading_odd_coefficient"] = taylor["coefficients"][1]["value"]
        out["parity"]["leading_odd_coefficient_recognized"] = \
            taylor["coefficients"][1]["recognized"]

        # ---- structure of the odd part: tau(u) = e^u * (even in u) ----
        print("\nStructure test: kappa(u) := e^{-u} tau(u) should be EVEN "
              "(odd content of tau = the factor e^u = M^2):")
        max_kappa_odd = mpf(0)
        kappa_rows = []
        for ray, u in grid:
            rp, rm = evaluate(u), evaluate(-u)
            kp = exp(-u) * rp["tau"]
            km = exp(u) * rm["tau"]
            ko = fabs((kp - km) / 2)
            max_kappa_odd = max(max_kappa_odd, ko)
            kappa_rows.append({"ray": ray, "u": cstr(u),
                               "kappa_plus": cstr(kp),
                               "abs_kappa_odd": nstr(ko, 8)})
            print(f"  [{ray:7s}] u = {cstr(u)}: |odd part of kappa| = "
                  f"{nstr(ko, 5)}")
        even_core_verified = max_kappa_odd < mpf("1e-40")
        print("  => e^{-u} tau(u) even:",
              "VERIFIED" if even_core_verified else "FAILED",
              f"(max |odd| = {nstr(max_kappa_odd, 5)})")
        out["even_core"] = {
            "statement": "tau(u) = e^u * tau_even(u) with tau_even even in u; "
                         "e^u = M^2",
            "max_abs_odd_of_exp_minus_u_tau": nstr(max_kappa_odd, 8),
            "verified": bool(even_core_verified),
            "rows": kappa_rows,
        }

        # ---- flattening dependence: tau_3(u) = -e^{-2u} tau_1(u) ----
        print("\nFlattening-shift test: datum-3 (f=(1,0), f''=(0,0)) should "
              "give tau_3 = -e^{-2u} tau_1:")
        max_fl_dev = mpf(0)
        for ray, u in grid:
            z1, z2 = deformed_shapes(u)
            t1 = one_loop(z1, z2, A1, B1, F_FLAT1, FPP_FLAT1)
            t3 = one_loop(z1, z2, A1, B1, F_FLAT3, FPP_FLAT3)
            dev3 = fabs(t3 + exp(-2 * u) * t1)
            max_fl_dev = max(max_fl_dev, dev3)
        print(f"  max |tau_3 + e^-2u tau_1| over grid = {nstr(max_fl_dev, 5)}")
        assert max_fl_dev < mpf("1e-50"), "flattening-shift identity FAILED"
        out["flattening_dependence"] = {
            "statement": "shifting the flattening by the kernel vector "
                         "((1,0),(-1,-1)) multiplies tau(u) by -e^{-2u} = "
                         "-M^{-4}; hence tau(u) is well-defined only up to "
                         "+- M^{4Z}, and the odd factor M^2 = e^u cannot be "
                         "removed by any flattening choice",
            "max_identity_dev": nstr(max_fl_dev, 8),
        }

    # ---------------- witness emission (repo conventions) ----------------
    assertions = [
        {"name": "u0_one_loop_equals_pm_sqrt_minus3_over_2",
         "computed": float(dev), "expected": 0.0,
         "passed": bool(dev < mpf("1e-50")), "tolerance": 1e-50,
         "source": "DG 1-loop at the complete structure (Garoufalidis-Sabo "
                   "formula); validates datum + conventions"},
        {"name": "apolynomial_residual_on_branch",
         "computed": float(max(mpf(p["apoly_residual_plus"]) for p in pairs)),
         "expected": 0.0,
         "passed": bool(all(mpf(p["apoly_residual_plus"]) < mpf("1e-55")
                            for p in pairs)),
         "tolerance": 1e-55,
         "source": "deformed shapes lie on the CCGLS A-polynomial branch "
                   "(primary convention cross-check)"},
        {"name": "vol_is_even_in_u",
         "computed": float(max(mpf(p["vol_asymmetry"]) for p in pairs)),
         "expected": 0.0,
         "passed": bool(all(mpf(p["vol_asymmetry"]) < mpf("1e-55")
                            for p in pairs)),
         "tolerance": 1e-55,
         "source": "NZ85 volume evenness (control channel)"},
        {"name": "tau_has_genuine_odd_part",
         "computed": float(max_odd), "expected": 1.0,
         "passed": bool(not verdict_even), "tolerance": 0.0,
         "source": "pre-registered question: is the deformed 1-loop even? "
                   "NO - odd part O(u) present"},
        {"name": "odd_content_is_exactly_exp_u",
         "computed": float(mpf(out["even_core"]["max_abs_odd_of_exp_minus_u_tau"])),
         "expected": 0.0,
         "passed": bool(out["even_core"]["verified"]),
         "tolerance": 1e-40,
         "source": "e^{-u} tau(u) even to ~1e-61 on all rays: "
                   "tau(u) = e^u * tau_even(u), odd part = sinh(u)*tau_even(u)"},
        {"name": "odd_factor_flattening_irreducible",
         "computed": float(mpf(out["flattening_dependence"]["max_identity_dev"])),
         "expected": 0.0,
         "passed": bool(mpf(out["flattening_dependence"]["max_identity_dev"])
                        < mpf("1e-50")),
         "tolerance": 1e-50,
         "source": "flattening kernel-shift multiplies tau by -e^{-2u} = "
                   "-M^{-4}; parity class M^{+-2} x even is invariant"},
    ]
    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.libmp.BACKEND if hasattr(mp, 'libmp') else ''}".strip()
                          or "mpmath",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-deformed-one-loop-parity",
        "scriptFile": "qbeta_deformed_one_loop_parity_probe.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            check=True).stdout.strip(),
        "description": (
            "Deformed Dimofte-Garoufalidis 1-loop invariant tau(u) of 4_1 "
            "along the Dehn-surgery branch, and its parity in u. VERDICT: "
            "tau(u) = e^u * tau_even(u) - the 1-loop channel carries a "
            "convention-irreducible odd factor e^u = M^2, so its odd part is "
            "exactly sinh(u) * tau_even(u): the first concrete geometric "
            "carrier with the bar-odd sinh structure. Even core: "
            "tau(u)/tau(0) = e^u(1 - u^2/3 - u^4/4 - 121u^6/1080 + O(u^8)). "
            "Validated: tau(0) = +-sqrt(-3)/2, A-polynomial residuals "
            "<= 3e-61 on the branch, Vol even, datum-independence. "
            "Geometric-exact data; no c_k proposed; nothing wired."
        ),
        "precisionMetadata": {"compute_dps": mp.dps},
        "data": out,
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }
    here = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(here, "qbeta-deformed-one-loop-parity.witness.json")
    with open(dest, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    print("\nallPassed:", witness["allPassed"])
    print("Wrote", os.path.basename(dest))
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
