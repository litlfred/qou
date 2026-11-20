#!/usr/bin/env python3
"""R2/R5 (bean qou-99qc): the n<->p flip as the U_q(gl2) raising operator T+ = Delta^2(E).

Pre-registered in PREREGISTRATION.md (same directory). Lean twin:
QOU/QuarkState/IsospinRaisingRoundTrip.lean (sorry-free, generic field).

Model: V = K^2 (u: T3 = +1/2, d: T3 = -1/2), Jimbo R-check on V(x)V, coproduct
Delta(E) = E(x)K + 1(x)E, Delta(F) = F(x)1 + K^-1(x)F. sigma1 = R(x)1, sigma2 = 1(x)R on V^(x)3.
W- = weight space of n (one u), W+ = weight space of p (two u).

  eps_C(X) = tr_{W-}(F E X) / tr_{W-}(F E)

On Delta_S (QBetaChiralityReduction) every block trace reads y3 = tau(J), so
Q_beta = (h[2]/2) * y3 * E0. This probe re-derives every identity exactly over Q(q)
(sympy) and evaluates at the proton pin with mpmath (70 dps). CODATA is a comparison
row only; no variant is selected by its residual (AGENTS.md NO FITTING).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import _path_bridge  # noqa: E402,F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at, M_E_MEV_STR  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402

DPS = 70
Q_BETA_CODATA_STR = "0.78233341"  # comparison only


def model():
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    E = sp.Matrix([[0, 1], [0, 0]]); F = sp.Matrix([[0, 0], [1, 0]])
    K = sp.diag(q, 1 / q); Ki = K.inv(); I2 = sp.eye(2)
    kp = sp.kronecker_product
    R = sp.zeros(4); R[0, 0] = q; R[3, 3] = q; R[2, 1] = 1; R[1, 2] = 1; R[2, 2] = h
    return q, h, E, F, K, Ki, I2, kp, R


def exact():
    q, h, E, F, K, Ki, I2, kp, R = model()
    b2 = q + 1 / q
    checks = []
    z4 = sp.zeros(4)
    dE2 = kp(E, K) + kp(I2, E); dF2 = kp(F, I2) + kp(Ki, F); dK2 = kp(K, K)
    for nm, X in (("E", dE2), ("F", dF2), ("K", dK2)):
        checks.append((f"R commutes with Delta({nm}) on VxV", sp.simplify(R * X - X * R) == z4))
    checks.append(("R quadratic (R-q)(R+1/q)=0",
                   sp.simplify((R - q * sp.eye(4)) * (R + sp.eye(4) / q)) == z4))
    S1 = kp(R, I2); S2 = kp(I2, R)
    dE = kp(E, K, K) + kp(I2, E, K) + kp(I2, I2, E)
    dF = kp(F, I2, I2) + kp(Ki, F, I2) + kp(Ki, Ki, F)
    dK = kp(K, K, K)
    z8 = sp.zeros(8)
    for nm, X in (("E", dE), ("F", dF), ("K", dK)):
        for sn, S in (("s1", S1), ("s2", S2)):
            checks.append((f"{sn} commutes with Delta2({nm})", sp.simplify(S * X - X * S) == z8))
    idx = lambda t: 4 * t[0] + 2 * t[1] + t[2]  # 0 = u, 1 = d
    Wm = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
    Wp = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    r = lambda M, a, b: sp.Matrix(3, 3, lambda i, j: sp.simplify(M[idx(a[i]), idx(b[j])]))
    s1m, s2m, s1p, s2p = r(S1, Wm, Wm), r(S2, Wm, Wm), r(S1, Wp, Wp), r(S2, Wp, Wp)
    Em, Fp = r(dE, Wp, Wm), r(dF, Wm, Wp)
    Id = sp.eye(3)
    FE = sp.simplify(Fp * Em); EF = sp.simplify(Em * Fp)
    checks.append(("(FE-[2]^2)(FE-1)=0 on W-", sp.simplify((FE - b2**2 * Id) * (FE - Id)) == sp.zeros(3)))
    Bp = s1m * (s2m - h / 2 * Id); Bn = (s1m - h / 2 * Id) * (s2m - h * Id)
    D = sp.simplify(Bn - Bp); J1 = (2 * s1m - h * Id) / b2
    Bpp = s1p * (s2p - h / 2 * Id); Bnp = (s1p - h / 2 * Id) * (s2p - h * Id)
    Dp = sp.simplify(Bnp - Bpp); J1p = (2 * s1p - h * Id) / b2
    trFE = sp.factor(sp.simplify(FE.trace()))
    y3C = sp.factor(sp.simplify((FE * J1).trace() / FE.trace()))
    y3C_p = sp.factor(sp.simplify((EF * J1p).trace() / EF.trace()))
    tauD = sp.factor(sp.simplify((FE * D).trace() / FE.trace()))
    checks.append(("y3C = (q^2+1)^2/(q^4+4q^2+1)", sp.simplify(y3C - (q**2 + 1)**2 / (q**4 + 4 * q**2 + 1)) == 0))
    checks.append(("eps_C(Delta_S) = -(h[2]/2) y3C", sp.simplify(tauD + h * b2 / 2 * y3C) == 0))
    checks.append(("from p: tr_W+(EF J)/tr(EF) = y3C", sp.simplify(y3C_p - y3C) == 0))
    P12 = (b2**2 * Id - FE) / (b2**2 - 1)
    checks.append(("isospin-1/2 part: tr(P12 FE Delta_S) = 0", sp.simplify((P12 * FE * D).trace()) == 0))
    y3_noflip = sp.factor(sp.simplify(J1.trace() / 3))
    # quantum trace over all of V^(x)3 (closure by cup/cap): weights q^(2 T3)
    qtr = lambda Xuuu, Xp, Xm, Xddd: q**3 * Xuuu + q * Xp.trace() + Xm.trace() / q + Xddd / q**3
    J1uuu = (2 * q - h) / b2  # sigma = q on uuu and ddd
    y3_qtr = sp.factor(sp.simplify(qtr(J1uuu, J1p, J1, J1uuu) / qtr(1, Id, Id, 1)))
    zD = (q**4 + 1) / (q**2 + 1)**2
    checks.append(("quantum trace of J = convention-D y3 (Jones)", sp.simplify(y3_qtr - zD) == 0))
    variants = {
        "C_round_trip_T+ (pre-registered)": y3C,
        "C_isospin_half_projection": sp.Integer(0),
        "weight_restricted_no_flip": y3_noflip,
        "quantum_trace_all_weights (= z_D, label A)": zD,
    }
    return checks, variants, q, {"s1m": s1m, "s2m": s2m, "s1p": s1p, "s2p": s2p, "E": Em, "F": Fp, "trFE": trFE}


def main() -> int:
    checks, variants, qs, mats = exact()
    for n, ok in checks:
        print(("PASS " if ok else "FAIL ") + n)
    for k, v in mats.items():
        print(k, v.tolist() if hasattr(v, "tolist") else v)
    mp.mp.dps = DPS
    q0 = mp.mpf(q_at(DPS)) if not isinstance(q_at(DPS), mp.mpf) else q_at(DPS)
    me = mp.mpf(M_E_MEV_STR)
    h = q0 - 1 / q0; b2 = q0 + 1 / q0
    E0 = me / (q0 * (q0 - 1)); E0t = E0 / (1 - ((q0 - 1) / q0) ** 2)
    codata = mp.mpf(Q_BETA_CODATA_STR)
    rows = {}
    for name, ex in variants.items():
        y3 = mp.mpf(sp.lambdify(qs, ex, "mpmath")(q0)) if ex != 0 else mp.mpf(0)
        Q0 = h * b2 / 2 * y3 * E0; Qt = h * b2 / 2 * y3 * E0t
        rows[name] = {"y3_exact": str(ex), "y3_q0": fmt(y3), "Qbeta_E0_order0_MeV": fmt(Q0),
                      "Qbeta_E0_tower_MeV": fmt(Qt),
                      "vs_codata_order0_pct": fmt(100 * (Q0 / codata - 1), 8),
                      "vs_codata_tower_pct": fmt(100 * (Qt / codata - 1), 8)}
        print(f"{name}: y3={mp.nstr(y3, 15)}  Q0={mp.nstr(Q0, 12)} ({mp.nstr(100*(Q0/codata-1), 6)} %)"
              f"  Qtower={mp.nstr(Qt, 12)} ({mp.nstr(100*(Qt/codata-1), 6)} %)")
    print("y3 that CODATA would need (comparison only): order0", mp.nstr(codata / (h * b2 / 2 * E0), 12),
          " tower", mp.nstr(codata / (h * b2 / 2 * E0t), 12))
    all_ok = all(ok for _, ok in checks)
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("qbeta-r2-isospin-raising-round-trip", engine="mpmath")
        wb.set_description(
            "R2/R5 of bean qou-99qc. The n<->p flip is the U_q(gl2) raising operator T+ = Delta^2(E) "
            "on V^(x)3, which commutes with the H3 action (Schur-Weyl). eps_C(X) = "
            "tr_W-(F E X)/tr_W-(F E) gives y3 = (q^2+1)^2/(q^4+4q^2+1) = [2]^2/([2]^2+2). "
            "The full quantum trace (closure of every strand by pair creation/annihilation) "
            "gives the convention-D y3 (q^4+1)/(q^2+1)^2. The isospin-1/2 projection gives 0: "
            "Delta_S lives in the (3) block only.")
        wb.add_data("q0_anchor", "proton")
        wb.add_data("q0", fmt(q0))
        wb.add_data("E0_order0_MeV", fmt(E0)); wb.add_data("E0_tower_MeV", fmt(E0t))
        wb.add_data("variants", rows)
        wb.add_data("codata_comparison_only_MeV", Q_BETA_CODATA_STR)
        for n, ok in checks:
            wb.add_assertion(name=n, computed=str(int(bool(ok))), expected="1", tolerance=0, source="sympy exact Q(q)")
        wb.add_caveat("Normalisation eps_C(1)=1 is a remaining choice (same convention as D), not derived.")
        wb.add_caveat("The identification 'n->p = T+' is the physical posit of label C; E0 is posited (bean qou-mkm8).")
        wb.add_caveat("Not wired to the scorecard. CODATA is a comparison row only.")
        out = wb.save()
        print("witness:", out)
    except Exception as exc:  # pragma: no cover
        print("witness not written:", exc)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
