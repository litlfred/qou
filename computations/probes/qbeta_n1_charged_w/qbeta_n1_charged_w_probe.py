#!/usr/bin/env python3
"""qbeta_n1_charged_w_probe — N1: charged W exchange, n → p e⁻ ν̄ amplitude M(q), rate 𝔇_n(q).

Bean qou-99qc (N1). Pre-registered in PREREGISTRATION.md (commit 5ab8166249) before this file was run.
Lean twin: QOU/QuarkState/ChargedCurrentW.lean (sorry-free).

Exact sympy over Q(q) for the algebra; mpmath at 70 dps, proton q₀, for numbers. No float64 in any computed
value. CODATA / τ_n / G_F enter only in the final comparison block.

Assumption (flagged, as qou-g0jn PRE-REG 3): the lepton is a fourth strand carrying a second copy of the
doublet V, ν = u, e⁻ = d; n → p e⁻ ν̄ is read by crossing symmetry as n ν → p e⁻.
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
FAILED: list = []

q = sp.symbols("q", positive=True)
h = q - 1 / q
b2 = q + 1 / q


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def zero(e):
    return sp.simplify(sp.together(e)) == 0


# ---------------------------------------------------------------- V^{⊗n}, Jimbo Ř, u = 0, d = 1
def R2(a, b):
    if a == b:
        return {(a, b): q}
    if (a, b) == (0, 1):
        return {(1, 0): sp.Integer(1)}
    return {(0, 1): sp.Integer(1), (1, 0): h}


def act(i, state, sign=1):
    out = {}
    for s, c in state.items():
        for (x, y), w in R2(s[i], s[i + 1]).items():
            t = list(s); t[i] = x; t[i + 1] = y; t = tuple(t)
            out[t] = sp.expand(out.get(t, 0) + c * w)
        if sign < 0:
            out[s] = sp.expand(out.get(s, 0) - h * c)
    return out


def jimbo_E(n):
    """Δ^{(n-1)}(E) = Σ_i 1⊗…⊗E_i⊗K⊗…⊗K, E d = u, K u = q u."""
    def app(s):
        out = {}
        for i in range(n):
            if s[i] == 1:
                t = list(s); t[i] = 0
                c = sp.Integer(1)
                for j in range(i + 1, n):
                    c *= q if s[j] == 0 else 1 / q
                out[tuple(t)] = c
        return out
    return app


def run_exact():
    out = {}
    # A. one crossing, strand-tracked: R = P·Ř
    def strand_tracked(sign):
        M = {}
        for a, b in itertools.product([0, 1], repeat=2):
            st = act(0, {(a, b): sp.Integer(1)}, sign)
            for (x, y), c in st.items():
                M[(a, b, y, x)] = c   # swap the output labels: strand identity
        return M
    Rp, Rm = strand_tracked(1), strand_tracked(-1)
    vp, vm = Rp.get((1, 0, 0, 1), 0), Rm.get((1, 0, 0, 1), 0)   # d ν → u e⁻
    check("A1.beta_vertex_pos", zero(vp - h), f"positive crossing d ν → u e⁻ = {sp.simplify(vp)} = h")
    check("A2.beta_vertex_neg", zero(vm), f"negative crossing d ν → u e⁻ = {vm} (chiral)")
    vrev = Rm.get((0, 1, 1, 0), 0)
    check("A3.reverse_neg", zero(vrev + h), f"negative crossing u e⁻ → d ν = {sp.simplify(vrev)} = −h")
    out["A"] = {"pos_d_nu_to_u_e": str(sp.simplify(vp)), "neg_d_nu_to_u_e": str(vm),
                "neg_u_e_to_d_nu": str(sp.simplify(vrev))}

    # B. lepton passage through n nucleon strands: coefficient c_n·Δ^{(n)}(E), sector by sector
    gen = {}
    for n in (2, 3, 4, 5):
        for nu in range(0, n):
            src = [s for s in itertools.product([0, 1], repeat=n) if s.count(0) == nu]
            ratios = set()
            for s in src:
                st = {s + (0,): sp.Integer(1)}
                for i in reversed(range(n)):
                    st = act(i, st)
                E = jimbo_E(n)(s)
                for t, c in E.items():
                    ratios.add(sp.simplify(st.get((1,) + t, 0) / c))
                extra = [k for k, v in st.items() if k[0] == 1 and k[1:] not in E and v != 0]
                assert not extra
            ratios = list(ratios)
            nd = n - nu
            ok = len(ratios) == 1 and zero(ratios[0] - h * q ** (nd - 1))
            gen[f"n{n}_Nu{nu}"] = str(ratios)
            check(f"B.passage_n{n}_Nu{nu}", ok, f"block = {ratios} · Δ(E); expected h·q^(N_d−1), N_d={nd}")
    out["B_general"] = gen
    out["B_rule"] = "lepton ν passing n nucleon strands leftward with positive crossings: n ν → p e⁻ block = h·q^(N_d−1)·Δ^(n)(E)"

    # C. |M|² on the three-quark weight space
    Eu = sp.Matrix([[0, 1, q], [1, 0, 1], [1 / q, 1, 0]])
    Fd = sp.Matrix([[0, 1, 1 / q], [1, 0, 1], [q, 1, 0]])
    A = (h * q) * Eu
    G = sp.simplify(A.T * A)
    check("C1.AtA", all(zero(e) for e in (G - (h * q) ** 2 * Fd * Eu)), "AᵀA = (hq)²·T⁻T⁺")
    v1, v2, w = sp.Matrix([-q, 1, 0]), sp.Matrix([-q ** 2, 0, 1]), sp.Matrix([q ** -2, q ** -1, 1])
    m_half = [sp.simplify((v.T * G * v)[0] / (v.T * v)[0]) for v in (v1, v2)]
    m_32 = sp.simplify((w.T * G * w)[0] / (w.T * w)[0])
    check("C2.normSq_half", all(zero(m - (q ** 2 - 1) ** 2) for m in m_half), f"|M|²(isospin ½) = {m_half[0]}")
    check("C3.normSq_32", zero(m_32 - (q ** 2 - 1) ** 2 * b2 ** 2), f"|M|²(isospin 3/2) = {sp.factor(m_32)}")
    Mmir = sp.simplify((h / q) ** 2)
    check("C4.mirror_ratio", zero((q ** 2 - 1) ** 2 / Mmir - q ** 4), "|M_pos|²/|M_mirror|² = q⁴")
    # bar parity of |M|²: f(1/q) vs f(q)
    M2 = (q ** 2 - 1) ** 2
    bar = sp.simplify(M2.subs(q, 1 / q))
    check("C5.bar", zero(bar - Mmir) and not zero(bar - M2), f"bar(|M|²) = {bar} = mirror, ≠ |M|² (no definite bar parity)")
    dlog = sp.simplify(sp.diff(sp.log(M2), q) * q)
    check("C6.dlog", zero(dlog - 4 * q ** 2 / (q ** 2 - 1)), f"d ln|M|²/d ln q = {dlog}")
    check("C7.q_to_1", sp.limit(M2 / (q - 1) ** 2, q, 1) == 4, "|M|² ~ 4(q−1)² ~ h² as q → 1")
    out["C"] = {"M_amp": "(q^2-1)·T⁺ = h·q·T⁺", "normSq_isospin_half": str(m_half[0]),
                "normSq_isospin_3/2": str(sp.factor(m_32)), "normSq_mirror": str(Mmir),
                "bar_of_normSq": str(bar), "dlog_normSq_dlogq": str(dlog)}
    return out


def fermi_f(W0):
    """f(W0) = ∫_1^{W0} p W (W0 − W)² dW, F(Z,W) = 1 (Coulomb correction omitted)."""
    return mp.quad(lambda W: mp.sqrt(W ** 2 - 1) * W * (W0 - W) ** 2, [1, W0])


def numbers():
    q0 = mp.mpf(C.Q_50_DIGIT_STR)
    me = mp.mpf(C.M_E_MEV_STR)
    hq, b2q = q0 - 1 / q0, q0 + 1 / q0
    M2 = (q0 ** 2 - 1) ** 2
    M2mir = (hq / q0) ** 2
    E0z = qbeta_e0.order_zero(q=q0)
    yC = b2q ** 2 / (b2q ** 2 + 2)
    Q_C = E0z * hq * b2q / 2 * yC
    Q_C_closed = me * (q0 + 1) * (q0 ** 2 + 1) / (2 * q0 ** 3) * yC
    check("N1.QC_closed_form", abs(Q_C - Q_C_closed) < mp.mpf(10) ** (-60), "E₀·(h[2]/2)·y_C = m_e(q+1)(q²+1)/(2q³)·y_C")
    check("N2.QC_bean_value", abs(Q_C - mp.mpf("0.588715")) < mp.mpf("1e-6"), f"Q_C = {mp.nstr(Q_C, 12)} (bean 0.588715)")
    Q_scored = mp.mpf("0.325433929")   # owner-scored cell D1 = A (#8586), quoted, not recomputed here
    rows = {}
    for name, Q in (("label_C_Tplus_roundtrip", Q_C), ("owner_scored_D1A", Q_scored)):
        W0 = 1 + Q / me
        f = fermi_f(W0)
        dl = mp.diff(lambda x: mp.log(fermi_f(1 + x / me)), Q) * Q
        rate_over_G2 = M2 * me ** 5 * f / (2 * mp.pi ** 3)        # 𝔇 / G², MeV⁵
        rows[name] = dict(Q_beta_MeV=Q, W0=W0, f=f, f_sargent=W0 ** 5 / 30, dlnf_dlnQ=dl,
                          normSq=M2, D_over_G2_MeV5=rate_over_G2)
    # q-dependence of the rate along the label-C curve, at fixed G
    def D_C(x):
        x = mp.mpf(x); hb = x + 1 / x
        Q = me * (x + 1) * (x ** 2 + 1) / (2 * x ** 3) * hb ** 2 / (hb ** 2 + 2)
        return (x ** 2 - 1) ** 2 * fermi_f(1 + Q / me)
    dlnD = mp.diff(lambda x: mp.log(D_C(x)), q0) * q0
    return rows, dict(q0=q0, me=me, M2=M2, M2mir=M2mir, dlnD_dlnq_labelC=dlnD,
                      dlnM2_dlnq=4 * q0 ** 2 / (q0 ** 2 - 1))


def main() -> int:
    log("exact block")
    out = run_exact()
    log("numbers at proton q0 (before any comparison value is read)")
    rows, base = numbers()
    log(f"q0 = {mp.nstr(base['q0'], 25)}; |M|² = (q²−1)² = {mp.nstr(base['M2'], 20)}; mirror {mp.nstr(base['M2mir'], 20)}")
    log(f"d ln|M|²/d ln q = {mp.nstr(base['dlnM2_dlnq'], 12)}; d ln 𝔇/d ln q along label C = {mp.nstr(base['dlnD_dlnq_labelC'], 12)}")
    # ---- comparison only
    hbar = mp.mpf("6.582119569e-22")         # MeV·s (exact SI)
    tau = mp.mpf("878.4")
    Dn = hbar / tau
    GF = mp.mpf("1.1663788e-11")             # MeV⁻² (CODATA), comparison only
    Qcod = mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR) - base["me"]
    for k, r in rows.items():
        r["implied_Lambda_MeV"] = (r["D_over_G2_MeV5"] / Dn) ** (mp.mpf(1) / 4)
        r["Lambda_over_GF_scale"] = r["implied_Lambda_MeV"] * mp.sqrt(GF)
        r["Q_beta_vs_codata_pct"] = (r["Q_beta_MeV"] - Qcod) / Qcod * 100
        r["rate_with_imported_GF_over_Dn"] = GF ** 2 * r["D_over_G2_MeV5"] / Dn
        log(f"  {k}: Q={mp.nstr(r['Q_beta_MeV'], 10)} f={mp.nstr(r['f'], 10)} (Sargent {mp.nstr(r['f_sargent'], 8)}) "
            f"dlnf/dlnQ={mp.nstr(r['dlnf_dlnQ'], 6)} Λ={mp.nstr(r['implied_Lambda_MeV'], 8)} MeV "
            f"Λ·√G_F={mp.nstr(r['Lambda_over_GF_scale'], 8)} 𝔇(G_F)/𝔇_n={mp.nstr(r['rate_with_imported_GF_over_Dn'], 8)}")
    f_cod = fermi_f(1 + Qcod / base["me"])
    table = {k: {kk: fmt(vv) for kk, vv in r.items()} for k, r in rows.items()}
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-n1-charged-w", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc N1: charged W exchange of the strand-tracked crossing; n nu -> p e- block of "
                       "the lepton passage = h q T+; |M|^2 = (q^2-1)^2 on isospin 1/2; rate family. "
                       "Pre-registered at 5ab8166249. Not wired to any scorecard.")
    wb.add_parameter("q0", C.Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("lepton_assumption", "fourth strand, second copy of V, nu = u, e- = d")
    wb.add_data("exact", out)
    wb.add_data("table", table)
    wb.add_data("at_q0", {k: fmt(v) for k, v in base.items()})
    wb.add_data("comparison", {"D_n_MeV": fmt(Dn), "tau_n_s": "878.4", "G_F_MeV-2": fmt(GF),
                               "Q_beta_codata_MeV": fmt(Qcod), "f_at_codata_Q": fmt(f_cod)})
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
