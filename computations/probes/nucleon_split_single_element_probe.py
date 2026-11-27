#!/usr/bin/env python3
"""Exact + 80-dps check of the single-element theorem for the n-p split (compute-accuracy C1).

Lean: ``QOU.QBeta.NucleonSplitSingleElement``
(``folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitSingleElement.lean``).
Audit: ``docs/audits/2026-11-27-nucleon-split-single-element-theorem.md``. Bean ``qou-myts``.

What it does, in order:

1. EXACT over Q(q) (sympy): the intertwiner P satisfies P*A_i = B_i*P for the four letters
   sigma1, sigma2, sigma1^-1, sigma2^-1; for a fixed list of elements (V^3, V^6, the two-photon
   product with all six photon weights symbolic, and words with inverse letters) the plain
   traces on W_n and W_p agree, and the two-term traces are tau_p = q t, tau_n = (q^-1 - c/3) t.
   This re-checks the Lean statements on concrete elements; it is not the proof.
2. 80 dps at the proton and muon q0: t(V^3); the linear-map split S*(tau_n - tau_p) with the
   corpus's mass-channel scale S = 2 m_mu [3]_q!/q^3 (sign check); the Gibbs-map cell
   E*(2 log q - log(1 - c q/3)) at c = 0 for both corpus E0 forms.
3. DIAGNOSTIC ONLY, adopts nothing: the coupling c that the Gibbs map would need to reach the
   CODATA m_n - m_p or Q_beta. Printed so the size of the gap is visible; it is not a value of c.

No float64: sympy rationals for (1), mpmath at 80 dps for (2)-(3). CODATA values enter only the
comparison lines.

Run:  python3 -u computations/probes/nucleon_split_single_element_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)

import sympy as sp  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

DPS = 80
LEAN_MODULE = "QOU.QBeta.NucleonSplitSingleElement"

M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
M_MU = mpf(_codata.codata("muon mass energy equivalent in MeV").value_str)
# comparison only
M_P_EXP = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
M_N_EXP = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
DM_NP_EXP = M_N_EXP - M_P_EXP
QBETA_EXP = DM_NP_EXP - M_E

# ---------------------------------------------------------------- 1. exact over Q(q)
q, c = sp.symbols("q c", positive=True)
h = q - 1 / q
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
A1i = sp.Matrix([[1 / q, 0, 0], [0, -h, 1], [0, 1, 0]])
A2i = sp.Matrix([[-h, 1, 0], [1, 0, 0], [0, 0, 1 / q]])
B1, B2, B1i, B2i = A2, A1, A2i, A1i
P = sp.Matrix([[q ** -2, 1 / q, 0], [1 / q, 0, 1 / q], [0, 1 / q, 1]])
GA = {"s1": A1, "s2": A2, "s1i": A1i, "s2i": A2i}
GB = {"s1": B1, "s2": B2, "s1i": B1i, "s2i": B2i}


def rho(gens, word):
    m = sp.eye(3)
    for letter in word:
        m = m * gens[letter]
    return m


def zero(m):
    return all(sp.simplify(e) == 0 for e in m)


exact = {}
exact["A1_inverse"] = zero(A1 * A1i - sp.eye(3)) and zero(A2 * A2i - sp.eye(3))
exact["intertwine_all_letters"] = all(zero(P * GA[k] - GB[k] * P) for k in GA)

V = ["s1", "s2i"]
phi = sp.symbols("f0 f1 f01 g0 g1 g01")


def photon(gens, a, b, d):
    return sp.eye(3) + a * gens["s1"] + b * gens["s2"] + d * gens["s1"] * gens["s2i"]


elements = {
    "V3": (rho(GA, V * 3), rho(GB, V * 3)),
    "V6": (rho(GA, V * 6), rho(GB, V * 6)),
    "photon_pair_symbolic": (
        photon(GA, *phi[:3]) * photon(GA, *phi[3:]),
        photon(GB, *phi[:3]) * photon(GB, *phi[3:]),
    ),
    "mixed_word_s1_s2i_s2i_s1i_s2": (
        rho(GA, ["s1", "s2i", "s2i", "s1i", "s2"]),
        rho(GB, ["s1", "s2i", "s2i", "s1i", "s2"]),
    ),
}
Kp, Kn = q * sp.eye(3), sp.eye(3) / q
QPp, QPn = sp.zeros(3), sp.Rational(-1, 3) * sp.eye(3)
for name, (MA, MB) in elements.items():
    t = (MA).trace()
    exact[f"{name}_trace_n_eq_p"] = sp.simplify(MB.trace() - t) == 0
    tp = ((Kp + c * QPp) * MA).trace()
    tn = ((Kn + c * QPn) * MB).trace()
    exact[f"{name}_tauP_eq_q_t"] = sp.simplify(tp - q * t) == 0
    exact[f"{name}_tauN_eq"] = sp.simplify(tn - (1 / q - c / 3) * t) == 0

tV3 = sp.factor(sp.simplify(elements["V3"][0].trace()))

# ---------------------------------------------------------------- 2. 80 dps
def qint(n, x):
    return (x ** n - x ** (-n)) / (x - 1 / x)


def at_anchor(q0):
    t = sp.lambdify(q, tV3, "mpmath")(q0)
    qd2 = q0 + 1 / q0
    # linear map: mass-channel scale per unit trace (audit 2026-11-20 §3), applied to the
    # [2]^3-normalised two-term traces at c = 0; the sign is the point, not the magnitude
    S = 2 * M_MU * qint(2, q0) * qint(3, q0) / q0 ** 3
    lin = S * (1 / q0 - q0) * t / qd2 ** 3
    e_ord0 = qbeta_e0.order_zero(q=q0, m_e=M_E)
    e_twr = qbeta_e0.canonical(q=q0, m_e=M_E)
    out = {"q0": q0, "t_V3": t, "S_mass_channel": S, "linear_split_c0": lin}
    for tag, E in (("ord0", e_ord0), ("twr", e_twr)):
        gibbs = 2 * E * mp.log(q0)
        # diagnostic: c needed so that E(2 log q - log(1 - c q/3)) hits a target
        c_dm = 3 * (1 - q0 ** 2 * mp.exp(-DM_NP_EXP / E)) / q0
        c_qb = 3 * (1 - q0 ** 2 * mp.exp(-QBETA_EXP / E)) / q0
        out[f"E0_{tag}"] = E
        out[f"gibbs_cell_c0_{tag}"] = gibbs
        out[f"gibbs_vs_dm_np_{tag}"] = gibbs / DM_NP_EXP - 1
        out[f"gibbs_vs_qbeta_{tag}"] = gibbs / QBETA_EXP - 1
        out[f"diag_c_for_dm_np_{tag}"] = c_dm
        out[f"diag_c_for_qbeta_{tag}"] = c_qb
    return out


def main():
    wb = WitnessBuilder("nucleon-split-single-element", engine="sympy+mpmath")
    wb.set_description(
        "Exact Q(q) re-check of the single-element theorem (QOU.QBeta.NucleonSplitSingleElement) "
        "on V^3, V^6, a symbolic two-photon product and a word with inverse letters, plus 80-dps "
        "linear-map sign and Gibbs-map cell at both q0 anchors; the coupling c needed by the "
        "Gibbs map is printed as a diagnostic only."
    )
    ok = True
    for k, v in exact.items():
        print(f"[exact] {k}: {v}")
        wb.add_assertion(f"exact_{k}", computed=bool(v), expected=True)
        ok &= bool(v)
    print(f"[exact] tr_W(V^3) = {tV3}")
    res = {}
    for name, q0 in (("proton", q_at(DPS)), ("muon", q_muon_at(DPS))):
        r = at_anchor(mpf(q0))
        res[name] = {k: fmt(v) for k, v in r.items()}
        print(f"\n[{name}] q0 = {mp.nstr(r['q0'], 20)}  t(V^3) = {mp.nstr(r['t_V3'], 20)}")
        print(f"  linear map, c=0: m_n - m_p = {mp.nstr(r['linear_split_c0'], 12)} MeV  (< 0: wrong sign)")
        for tag in ("ord0", "twr"):
            print(f"  Gibbs c=0, E0_{tag} = {mp.nstr(r[f'E0_{tag}'], 15)}: 2E0 log q = "
                  f"{mp.nstr(r[f'gibbs_cell_c0_{tag}'], 12)} MeV "
                  f"[vs dm_np {mp.nstr(100 * r[f'gibbs_vs_dm_np_{tag}'], 6)} %, "
                  f"vs Q_beta {mp.nstr(100 * r[f'gibbs_vs_qbeta_{tag}'], 6)} %]")
            print(f"    DIAGNOSTIC c needed: dm_np {mp.nstr(r[f'diag_c_for_dm_np_{tag}'], 10)}, "
                  f"Q_beta {mp.nstr(r[f'diag_c_for_qbeta_{tag}'], 10)}  (not adopted)")
        sign_ok = r["linear_split_c0"] < 0 and r["gibbs_cell_c0_ord0"] > 0
        wb.add_assertion(f"{name}_linear_neg_gibbs_pos", computed=bool(sign_ok), expected=True)
        ok &= bool(sign_ok)
    wb.add_data("lean_module", LEAN_MODULE)
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc", "qou-wxhi"])
    wb.add_data("trace_V3_exact", str(tV3))
    wb.add_data("anchors", res)
    wb.add_data("codata_comparison_only", {"dm_np": fmt(DM_NP_EXP), "qbeta": fmt(QBETA_EXP)})
    path = wb.save({"q0Anchor": "comparison"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
