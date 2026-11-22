#!/usr/bin/env python3
"""
Probe — the residual SHAPE of the normalised bond-counting law against AME 2020.

CONTEXT. #6656 (qou-hfjc) showed the link-invariant normalisation of the
convention-D Ocneanu trace is forced (nu = q^-2, mu = [2]_q) and equalises
every single-crossing bond to q/(q^2+1), so #6611's additive law becomes

    B_norm = (A - 1) · eps,    eps = E_0 · ln[2]_q = 2.9242463 MeV   (derived)

and the (N-Z) asymmetry of the un-normalised law — measured by #6611 to have
the WRONG sign — is a writhe artifact that vanishes. #6611's shape analysis
(residual correlates -0.804 with (N-Z)^2/A^2, -0.178 with A^(-1/3)) was done on
the UN-normalised law and is therefore partly that artifact. This probe redoes
it on the normalised law, with the un-normalised law as a control.

Note on qou-ib3g (#6668): its "per-nucleon coefficient at N = Z,
E_0·0.698581 = 2.92425 MeV" is this eps exactly — the un-normalised pp/nn
average -ln(z z')/2 = ln[2]_q equals the normalised weight identically — so its
factor 3.0075 (peak B/A at A = 62 over eps) applies to the normalised law
unchanged. Nothing here re-derives or re-measures it.

WHAT IS MEASURED (2548 measured AME nuclides, #6611's selection and helpers):
  1. control: the un-normalised segregated-chain residual r_U = B_exp/(E_0·S)
     and its three SEMF-shape correlations reproduce #6611's numbers;
  2. the normalised residual r_N = B_exp/(eps·(A-1)) and the same correlations,
     plus a pairing shape delta/sqrt(A) (+1 even-even, -1 odd-odd, 0 odd-A);
  3. a SHAPE TEST, stated as #6611's decision frame §5.2 stated it: does the
     residual have the SEMF shape a_V - a_S A^(-1/3) - a_C Z^2/A^(4/3)
     - a_A (N-Z)^2/A^2 (+ pairing)? A least-squares projection of r_N onto
     [1, A^(-1/3), Z^2/A^(4/3), (N-Z)^2/A^2, delta/sqrt(A)] is reported as
     coefficient RATIOS to the volume term and as R^2, compared with the
     textbook SEMF ratios (a_S/a_V ~ 1.13, a_C/a_V ~ 0.045, a_A/a_V ~ 1.50 for
     a_V = 15.75, a_S = 17.8, a_C = 0.711, a_A = 23.7, a_P = 11.18 MeV).
     THIS IS A DIAGNOSTIC OF THE DATA'S SHAPE, NOT A MODEL: none of the
     coefficients is wired anywhere, and they are reported to be checked
     AGAINST, never searched on;
  4. the kappa scan of #6611 repeated on the normalised law:
     B ~ eps·(A-1) + kappa·eps·(N-Z), to locate the linear-asymmetry optimum the
     data want relative to the normalised zero.

Arithmetic: mpmath 50 dps; AME values loaded from decimal strings; the 5x5
normal equations solved with mp.lu_solve. No float64 anywhere.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

import cyclic_triple_bond_cross_term_probe as ct  # noqa: E402
from binding_log_free_energy import M_E_MEV  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

mp.mp.dps = 50
Q, H, Z_D, TOL = ct.Q, ct.H, ct.Z_D, ct.TOL
Z_INV = Z_D - H
M_E = mp.mpf(str(M_E_MEV))
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
EPS = E0 * mp.log((Q ** 2 + 1) / Q)
ROOT = Path(__file__).resolve().parents[2]
AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"

# textbook SEMF (Weizsäcker, MeV) — for the SHAPE comparison only
SEMF = {"a_V": mp.mpf("15.75"), "a_S": mp.mpf("17.8"), "a_C": mp.mpf("0.711"),
        "a_A": mp.mpf("23.7"), "a_P": mp.mpf("11.18")}


def _pct(vals, num, den=100):
    v = sorted(vals)
    return v[min(len(v) - 1, len(v) * num // den)]


def _corr(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = mp.sqrt(sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys))
    return num / den


def lstsq(X, y):
    """least squares via normal equations, exact mp arithmetic; returns (coef, R²)."""
    n, k = len(X), len(X[0])
    XtX = mp.matrix(k, k)
    Xty = mp.matrix(k, 1)
    for i in range(k):
        for j in range(k):
            XtX[i, j] = sum(X[r][i] * X[r][j] for r in range(n))
        Xty[i] = sum(X[r][i] * y[r] for r in range(n))
    c = mp.lu_solve(XtX, Xty)
    yhat = [sum(c[i] * X[r][i] for i in range(k)) for r in range(n)]
    my = sum(y) / n
    ss_res = sum((y[r] - yhat[r]) ** 2 for r in range(n))
    ss_tot = sum((y[r] - my) ** 2 for r in range(n))
    return [c[i] for i in range(k)], 1 - ss_res / ss_tot


def main() -> int:
    checks: list[tuple[str, bool]] = []
    # the three production bond energies (un-normalised), from the production word
    W = atom_braid_word_3A(2, 2)
    Ls = [ct.letter(W[i][0], W[i][1]) for i in ct.bond_positions(W, 4)]  # pp, pn, nn
    b_pp, b_pn, b_nn = (ct.aff_tr(L) for L in Ls)
    e_pp, e_pn, e_nn = -mp.log(b_pp), -mp.log(b_pn), -mp.log(b_nn)
    checks.append(("un-normalised pp/nn average −ln(z z')/2 = ln[2]_q = ε/E₀ (why qou-ib3g's coefficient is ε)",
                   abs((e_pp + e_nn) / 2 - mp.log((Q ** 2 + 1) / Q)) < TOL))
    print(f"  E_0 = {mp.nstr(E0, 10)} MeV   ε = E_0·ln[2]_q = {mp.nstr(EPS, 10)} MeV   "
          f"un-normalised bond energies −ln b: pp {mp.nstr(e_pp, 6)}  pn {mp.nstr(e_pn, 6)}  nn {mp.nstr(e_nn, 6)}\n")

    rows = []
    for ent in json.loads(AME.read_text())["entries"]:
        Z, N, A = ent["Z"], ent["N"], ent["A"]
        bpa = ent.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not bpa or ent.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B > 0:
            rows.append((A, Z, N, B))
    print(f"  {len(rows)} measured AME nuclides")

    def S_unnorm(Z, N):
        return (Z - 1) * e_pp + e_pn + (N - 1) * e_nn

    r_U = [B / (E0 * S_unnorm(Z, N)) for (A, Z, N, B) in rows]
    r_N = [B / (EPS * (A - 1)) for (A, Z, N, B) in rows]

    def delta(A, Z, N):
        if Z % 2 == 0 and N % 2 == 0:
            return mp.mpf(1)
        if Z % 2 == 1 and N % 2 == 1:
            return mp.mpf(-1)
        return mp.mpf(0)

    shapes = {
        "(N-Z)^2/A^2  [asymmetry]": [(mp.mpf(N - Z) / A) ** 2 for (A, Z, N, B) in rows],
        "A^(-1/3)     [surface]  ": [mp.mpf(A) ** (-mp.mpf(1) / 3) for (A, Z, N, B) in rows],
        "Z^2/A^(4/3)  [Coulomb]  ": [mp.mpf(Z * Z) / mp.mpf(A) ** (mp.mpf(4) / 3) for (A, Z, N, B) in rows],
        "delta/sqrt(A) [pairing] ": [delta(A, Z, N) / mp.sqrt(A) for (A, Z, N, B) in rows],
    }

    print("\n  residual correlations (B_exp / B_pred against the SEMF shapes)")
    print(f"    {'shape':<28}{'un-normalised (#6611 control)':>32}{'normalised (bond counting)':>30}")
    cU, cN = {}, {}
    for nm, xs in shapes.items():
        cU[nm] = _corr(xs, r_U)
        cN[nm] = _corr(xs, r_N)
        print(f"    {nm:<28}{mp.nstr(cU[nm], 6):>32}{mp.nstr(cN[nm], 6):>30}")
    checks.append(("control: un-normalised asymmetry correlation reproduces #6611's −0.804 (to 3 dp)",
                   abs(cU["(N-Z)^2/A^2  [asymmetry]"] - mp.mpf("-0.804")) < mp.mpf("0.0015")))
    checks.append(("control: un-normalised surface correlation reproduces #6611's −0.178 (to 3 dp)",
                   abs(cU["A^(-1/3)     [surface]  "] - mp.mpf("-0.178")) < mp.mpf("0.0015")))
    aN, sN, cN_ = (cN["(N-Z)^2/A^2  [asymmetry]"], cN["A^(-1/3)     [surface]  "], cN["Z^2/A^(4/3)  [Coulomb]  "])
    checks.append(("normalised law: the asymmetry shape is still the dominant residual correlation",
                   abs(aN) > abs(sN) and abs(aN) > abs(cN_)))

    # ---- shape test: SEMF projection of the normalised residual ------------
    print("\n  SHAPE TEST — least-squares projection of r_N = B_exp/(ε(A−1)) onto the SEMF basis (diagnostic only)")
    X = [[mp.mpf(1), shapes["A^(-1/3)     [surface]  "][i], shapes["Z^2/A^(4/3)  [Coulomb]  "][i],
          shapes["(N-Z)^2/A^2  [asymmetry]"][i], shapes["delta/sqrt(A) [pairing] "][i]] for i in range(len(rows))]
    coef, r2 = lstsq(X, r_N)
    c0 = coef[0]
    names = ["volume", "surface", "Coulomb", "asymmetry", "pairing"]
    semf_ratio = {"surface": -SEMF["a_S"] / SEMF["a_V"], "Coulomb": -SEMF["a_C"] / SEMF["a_V"],
                  "asymmetry": -SEMF["a_A"] / SEMF["a_V"], "pairing": SEMF["a_P"] / SEMF["a_V"]}
    print(f"    R² = {mp.nstr(r2, 6)}   volume coefficient c_V = {mp.nstr(c0, 6)}  "
          f"(→ B ≈ {mp.nstr(c0 * EPS, 5)} MeV per bond at saturation; #6668's peak-based factor is 3.0075)")
    print(f"    {'term':<12}{'coef/c_V (data)':>18}{'SEMF a_i/a_V':>16}")
    ratio_ok = []
    for i, nm in enumerate(names[1:], start=1):
        rr = coef[i] / c0
        print(f"    {nm:<12}{mp.nstr(rr, 6):>18}{mp.nstr(semf_ratio[nm], 6):>16}")
        ratio_ok.append((nm, rr, semf_ratio[nm]))
    checks.append(("shape test: all four correction coefficients have the SEMF sign (surface, Coulomb, asymmetry < 0; pairing > 0)",
                   all((rr < 0) == (sr < 0) for _, rr, sr in ratio_ok)))
    checks.append(("shape test: R² of the SEMF projection exceeds 0.9 (the residual HAS the SEMF shape)",
                   r2 > mp.mpf("0.9")))
    # the same projection on the un-normalised control, for the contrast
    coefU, r2U = lstsq(X, r_U)
    print(f"    (control, un-normalised: R² = {mp.nstr(r2U, 6)}, c_V = {mp.nstr(coefU[0], 6)}, "
          f"asymmetry/c_V = {mp.nstr(coefU[3] / coefU[0], 6)})")
    checks.append(("normalised law needs a SMALLER asymmetry correction than the un-normalised one (|coef ratio| falls)",
                   abs(coef[3] / c0) < abs(coefU[3] / coefU[0])))

    # ---- kappa scan on the normalised law -----------------------------------
    print("\n  κ scan on the normalised law:  B ~ ε·(A−1) + κ·ε·(N−Z)   [diagnostic]")
    best = None
    for k100 in range(-40, 41, 5):
        k = mp.mpf(k100) / 100
        v = [B / (EPS * ((A - 1) + k * (N - Z))) for (A, Z, N, B) in rows if (A - 1) + k * (N - Z) > 0]
        p = _pct(v, 95) / _pct(v, 5)
        if best is None or p < best[1]:
            best = (k, p)
        if k100 % 10 == 0:
            print(f"      κ = {mp.nstr(k, 4):>6}   p5–p95 {mp.nstr(p, 7)}")
    print(f"      optimum near κ = {mp.nstr(best[0], 4)}   (normalised law has κ = 0 exactly; #6611's data optimum was ≈ −0.15)")
    checks.append(("κ scan: the data optimum is negative (neutron-rich LESS bound per bond), as #6611 found", best[0] < 0))
    checks.append(("κ scan: κ = 0 (the normalised law) beats the un-normalised κ_derived = +0.22 on p5–p95",
                   _pct([B / (EPS * (A - 1)) for (A, Z, N, B) in rows], 95) / _pct([B / (EPS * (A - 1)) for (A, Z, N, B) in rows], 5)
                   < (lambda v: _pct(v, 95) / _pct(v, 5))([B / (EPS * ((A - 1) + mp.mpf("0.22") * (N - Z))) for (A, Z, N, B) in rows if (A - 1) + mp.mpf("0.22") * (N - Z) > 0])))

    ok = 0
    print()
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
