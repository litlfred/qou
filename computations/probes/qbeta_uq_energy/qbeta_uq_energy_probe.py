#!/usr/bin/env python3
"""qou-99qc: Q_beta as an energy from U_q(gl2) structure outside H_n.

Pre-registered in PREREGISTRATION.md (same directory), committed before this probe ran.

Candidates: (a) Cartan / Bohr charge of T+, (b) twist / Casimir (central), (c) four strands
with the lepton doublet, (d) E0 as the K-grading unit.  Exact sympy over Q(q), then mpmath at
70 dps at the proton q0.  CODATA is read only in the last block.  No float64 in any computed
value.  Lean companion: QOU/QuarkState/CartanEnergyTransport.lean.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from sympy.physics.quantum import TensorProduct as TP  # noqa: E402

import qbeta_e0  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
FAILED: list = []
q = sp.symbols("q", positive=True)
h = q - 1 / q
D2 = q + 1 / q


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def zero(M):
    return all(sp.simplify(e) == 0 for e in M)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = TP(out, m)
    return sp.Matrix(out)


def main() -> int:
    # doublet: u = e0 (T3 = +1/2), d = e1
    K = sp.diag(q, 1 / q)
    Ki = sp.diag(1 / q, q)
    E = sp.Matrix([[0, 1], [0, 0]])
    F = sp.Matrix([[0, 0], [1, 0]])
    I2 = sp.eye(2)
    # coproduct Delta(K) = K(x)K, Delta(E) = E(x)K + 1(x)E, Delta(F) = F(x)1 + K^-1(x)F
    K3 = kron(K, K, K)
    K3i = kron(Ki, Ki, Ki)
    E2 = kron(E, K) + kron(I2, E)
    F2 = kron(F, I2) + kron(Ki, F)
    E3 = kron(E2, K) + kron(sp.eye(4), E)
    F3 = kron(F2, I2) + kron(kron(Ki, Ki), F)

    log("(a) Cartan / Bohr")
    check("C1.adK_three_strand", zero(K3 * E3 * K3i - E3 - (q ** 2 - 1) * E3),
          "K^(x)3 T+ K^(x)-3 - T+ = (q^2-1) T+ : the derived amplitude is Ad_K(T+) - T+")
    check("C1b.uq_relation", zero(E3 * F3 - F3 * E3 - (K3 - K3i) / (q - 1 / q)),
          "[E,F] = (K-K^-1)/(q-q^-1) on V^(x)3 (coproduct is a homomorphism)")

    log("(b) Casimir / twist: central")
    Cas = F3 * E3 + (q * K3 + K3i / q) / (q - 1 / q) ** 2
    check("C4.casimir_commutes_Tplus", zero(Cas * E3 - E3 * Cas), "[C, T+] = 0")
    # isospin-1/2 proton: weight-(2,1) vector killed by T+; neutron = T- of it
    idx_p = [i for i in range(8) if sp.simplify(K3[i, i] - q) == 0]
    sub = sp.Matrix.hstack(*[sp.eye(8)[:, i] for i in idx_p])
    ns = (E3 * sub).nullspace()
    p_half = sub * ns[0]
    n_half = F3 * p_half
    c_p = sp.simplify((Cas * p_half)[[i for i in range(8) if p_half[i] != 0][0]] /
                      p_half[[i for i in range(8) if p_half[i] != 0][0]])
    check("C4b.p_half_eigen", zero(Cas * p_half - c_p * p_half), f"C p_1/2 = c p_1/2, c = {c_p}")
    check("C4c.n_half_same_eigen", zero(Cas * n_half - c_p * n_half),
          "C n_1/2 = c n_1/2 with the same c (eigenvalue transport, Lean eigen_eq_of_commute)")
    check("C4d.Tplus_n_nonzero", not zero(E3 * n_half), "T+ n_1/2 != 0, so transport applies")
    # doublet (lepton strand): Casimir equal on e- and nu
    Cas1 = F * E + (q * K + Ki / q) / (q - 1 / q) ** 2
    check("C4e.lepton_casimir_scalar", zero(Cas1 - Cas1[0, 0] * I2),
          "C on the doublet is a scalar: e- and nu carry the same Casimir (so the same twist)")

    log("(c) four strands")
    K4 = kron(K3, K)
    X4 = kron(E3, F)  # charged-current exchange: quark T+ with lepton T-
    check("C2.exchange_commutes_K4", zero(K4 * X4 - X4 * K4),
          "(K^(x)4)(T+ (x) F) = (T+ (x) F)(K^(x)4): grouplike charges q^2 * q^-2 = 1")
    w = lambda nu: q ** (2 * nu - 4)  # K^(x)4 eigenvalue with nu up-strands of four
    check("C3.same_weight_space", sp.simplify(w(1 + 1) - w(2 + 0)) == 0,
          "n(x)nu (u-count 1+1) and p(x)e- (2+0) share K^(x)4 eigenvalue 1: one weight space (2,2)")
    eps_l = sp.simplify((1 / q - q) / D2)
    check("C5.lepton_split", sp.simplify(eps_l + h / D2) == 0, f"eps_lepton = (q^-1 - q)/[2] = {eps_l}")
    # #8586 three-strand split on V^3
    P = q ** 12 - 3 * q ** 10 + 3 * q ** 8 - 5 * q ** 6 + 3 * q ** 4 - 3 * q ** 2 + 1
    eps_q = (q ** 2 - 1) * P / (q ** 4 * (q ** 2 + 1) ** 3)  # = eps_n - eps_p on V^3 (#8586, Lean)
    me_s = sp.symbols("m_e", positive=True)
    E00 = me_s / (q * (q - 1))
    check("C5b.lepton_split_E0", sp.simplify(-eps_l * E00 - me_s * (q + 1) / (q * (q ** 2 + 1))) == 0,
          "|eps_lepton| E0 = m_e (q+1)/(q(q^2+1)) (Lean epsLepton_E0); = m_e only at q = 1")
    # eps_q < 0 on (1, 23/20] is proved (#8586); the additive-sector reading
    # (eps_n + eps_nu) - (eps_p + eps_e) = eps_q - eps_l
    released_add = sp.simplify(eps_q - eps_l)  # (eps_n + eps_nu) - (eps_p + eps_e), mass = +trace*E0

    log("(d) E0 as the K-grading unit: E0 * g = m_e ?")
    gaps = {"h": h, "q-1": q - 1, "q^2-1": q ** 2 - 1, "q(q-1)": q * (q - 1)}
    gap_ok = {k: sp.simplify(E00 * g - me_s) == 0 for k, g in gaps.items()}
    check("D1.only_qq-1", gap_ok == {"h": False, "q-1": False, "q^2-1": False, "q(q-1)": True},
          "E0 g = m_e identically only for g = q(q-1) = K-gap between q^2 and q (no doublet carries it)")

    # ---- numbers at q0, before CODATA
    q0 = mp.mpf(Q_50_DIGIT_STR)
    lam = mp.log(q0)
    hq = q0 - 1 / q0
    me = qbeta_e0._inputs(q0)[1]
    scales = {"m_e": me, "E0_order_zero": qbeta_e0.order_zero(q=q0), "E0_tower": qbeta_e0.canonical(q=q0)}
    f = lambda expr: sp.lambdify(q, expr, "mpmath")(q0)
    rows = []
    for sname, S in scales.items():
        rows.append({"cell": f"a1 h*{sname}", "MeV": hq * S})
        rows.append({"cell": f"a2 2ln(q)*{sname}", "MeV": 2 * lam * S})
    rows.append({"cell": "ref #8586 |eps_flavour(V^3)|*E0_tower (scored)", "MeV": abs(f(eps_q)) * scales["E0_tower"]})
    for sname in ("E0_order_zero", "E0_tower"):
        rows.append({"cell": f"c lepton |eps_l|*{sname}", "MeV": abs(f(eps_l)) * scales[sname]})
        rows.append({"cell": f"c additive (eps_q - eps_l)*{sname}, mass=+trace",
                     "MeV": f(released_add) * scales[sname]})
    rows.append({"cell": "c four-strand K-weighted split (any X)", "MeV": mp.mpf(0)})
    rows.append({"cell": "b twist / Casimir n vs p", "MeV": mp.mpf(0)})
    rows.append({"cell": "c linear Cartan energy, one coefficient", "MeV": mp.mpf(0)})
    for r in rows:
        log(f"  {r['cell']:58s} {mp.nstr(r['MeV'], 20)} MeV")
    ratios = {k: mp.nstr(scales["E0_order_zero"] * f(g) / me, 25) for k, g in gaps.items()}
    ratios["2ln q"] = mp.nstr(scales["E0_order_zero"] * 2 * lam / me, 25)
    log(f"  E0*g/m_e: {ratios}")
    check("N2.additive_sign_conflict", f(eps_q) < 0 and f(eps_l) < 0,
          "eps_q < 0 and eps_l < 0: under mass = +trace*E0 (the only sign giving Q > 0) the "
          "neutron is lighter than the proton AND the electron lighter than the neutrino")
    check("N1.lepton_E0_not_me", abs(abs(f(eps_l)) * scales["E0_order_zero"] - me) > mp.mpf("1e-3"),
          "lepton-strand split x E0 differs from m_e at q0 (electron mass not reproduced)")

    # ---- comparison, read only now
    from codata_constants import Q_BETA_MEV  # noqa: PLC0415
    qc = mp.mpf(str(Q_BETA_MEV))
    for r in rows:
        r["vs_codata_pct"] = mp.nstr((r["MeV"] - qc) / qc * 100, 8) if r["MeV"] != 0 else "-100"
        r["MeV"] = mp.nstr(r["MeV"], 30)
        log(f"  {r['cell']:58s} vs CODATA {r['vs_codata_pct']} %")

    out = {
        "q0": Q_50_DIGIT_STR,
        "closed_forms": {"eps_lepton": str(eps_l), "eps_quark_V3_8586": str(eps_q),
                         "lepton_split_times_E0": "m_e (q+1)/(q(q^2+1))",
                         "additive_released_over_E0": str(released_add),
                         "Ad_K": "K T+ K^-1 - T+ = (q^2-1) T+",
                         "casimir_p_half": str(c_p)},
        "E0_gap_ratios_over_me": ratios,
        "table": rows,
        "scope": "(b) for the zero rows: invariants centrality (twist/Casimir), grouplike K with "
                 "E(x)F of charge 1 (four strands), linearity of a one-coefficient Cartan energy; "
                 "(a) for the nonzero rows, which all carry an unforced scale and log/linear choice",
        "selected": "none",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-uq-energy", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: Q_beta as an energy from U_q(gl2) outside H_n (Cartan, twist, "
                       "four strands, E0). Pre-registered in PREREGISTRATION.md.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("convention", "D (z = q^3/(q^2+1)) = Tr(K^n .)/[2]^n")
    for key, val in out.items():
        wb.add_data(key, val)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0",
                         source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
