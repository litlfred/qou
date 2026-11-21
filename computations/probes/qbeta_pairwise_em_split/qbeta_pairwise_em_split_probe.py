#!/usr/bin/env python3
"""qbeta_pairwise_em_split_probe.py — does a pairwise charge energy escape the β no-go?

Bean qou-99qc. Pre-registered in PREREGISTRATION.md (this directory). Lean twin:
QOU.QuarkState.PairwiseChargeEnergyBeta (sorry-free). Everything is exact in Q(q) (sympy);
numbers at the proton q0 with mpmath at 70 dps. Nothing is fitted; no weight is solved for.

Arms
  A  uniform pairwise  w·Σ_{i<j}Q_iQ_j + s·ΣQ_i²  on n⊗ν vs p⊗e⁻  (symbolic in w, s)
  B  intra-nucleon w_N, nucleon–lepton w_L, self s_q, s_ℓ         (symbolic)
  C  the corpus two-term insertion on the Borromean V³ = (σ₀σ₁⁻¹)³ (= γ(0,0,qh)·γ(0,0,−q⁻¹h),
     the ruled photon 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹), with the derived quantum-trace weighting,
     extended by one spectator lepton strand (premise E1) normalised by [2]_q⁴ (premise E2):
       C1 covariant all-pairs, raw      C2 covariant all-pairs, connected (≡ 0)
       C3 adjacent Q12+Q23+Q34, raw     C4 adjacent, connected          (C3/C4: non-covariant)
     plus the corpus's own nucleon-only all-pairs raw term (deltaT_allPairs_raw_eq).
  MeV values are m_e·t with BOTH signs (the corpus does not fix the sign).

-- Ref: [leitner2026] bean qou-99qc; PR #8676; issue #8524
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for p in ("tools/qou-substrate/python", "computations", "schemas/witness-schema"):
    sys.path.insert(0, str(ROOT / p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at, M_E_MEV_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

DPS = 70
mp.mp.dps = DPS + 10
Q0 = q_at(DPS + 10)
ME = mp.mpf(M_E_MEV_STR)
MN_MINUS_MP_CODATA = mp.mpf("1.29333251")  # MeV, CODATA 2022 (comparison only)
QBETA_CODATA = mp.mpf("0.78233")           # MeV (comparison only)

q = sp.symbols("q", positive=True)
R = sp.Rational
h = q - 1 / q
Mx = sp.Matrix
A1 = Mx([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = Mx([[0, 1, 0], [1, h, 0], [0, 0, q]])
B1 = Mx([[0, 1, 0], [1, h, 0], [0, 0, q]])
B2 = Mx([[q, 0, 0], [0, 0, 1], [0, 1, h]])
VP = (A1 * A2.inv()) ** 3
VN = (B1 * B2.inv()) ** 3
P = q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1

# single-strand charges; proton basis uud, udu, duu; neutron basis udd, dud, ddu
CH = {"p": [(R(2, 3), R(2, 3), R(-1, 3)), (R(2, 3), R(-1, 3), R(2, 3)), (R(-1, 3), R(2, 3), R(2, 3))],
      "n": [(R(2, 3), R(-1, 3), R(-1, 3)), (R(-1, 3), R(2, 3), R(-1, 3)), (R(-1, 3), R(-1, 3), R(2, 3))]}


def diag_op(nuc, f):
    return sp.diag(*[f(c) for c in CH[nuc]])


def at_q0(expr):
    f = sp.lambdify(q, expr, "mpmath")
    with mp.workdps(DPS + 10):
        return f(Q0)


def nstr(x, n=30):
    return mp.nstr(x, n)


checks = []


def check(name, ok, src):
    checks.append((name, bool(ok), src))
    print(("PASS " if ok else "FAIL ") + name)


# ── Arm A ─────────────────────────────────────────────────────────────────────────────
w, s, wN, wL, sq, sl = sp.symbols("w s w_N w_L s_q s_l")


def pair(L):
    return sum(L[i] * L[j] for i in range(len(L)) for j in range(i + 1, len(L)))


nnu = [R(2, 3), R(-1, 3), R(-1, 3), 0]
pe = [R(2, 3), R(2, 3), R(-1, 3), -1]
splitA = sp.expand(w * pair(nnu) + s * sum(x**2 for x in nnu) - w * pair(pe) - s * sum(x**2 for x in pe))
check("A: uniform split = (2w - 4s)/3", sp.simplify(splitA - (2 * w - 4 * s) / 3) == 0,
      "PairwiseChargeEnergyBeta.uniform_split_SM")
check("A: pair sums n⊗ν = -1/3, p⊗e⁻ = -1", pair(nnu) == R(-1, 3) and pair(pe) == -1, "arith")

# ── Arm B ─────────────────────────────────────────────────────────────────────────────
qn, qp = nnu[:3], pe[:3]
EB = lambda Lq, cl: wN * pair(Lq) + wL * cl * sum(Lq) + sq * sum(x**2 for x in Lq) + sl * cl**2  # noqa: E731
splitB = sp.expand(EB(qn, 0) - EB(qp, -1))
check("B: split = w_L - w_N/3 - s_q/3 - s_l", sp.simplify(splitB - (wL - wN / 3 - sq / 3 - sl)) == 0,
      "PairwiseChargeEnergyBeta.twoWeight_split_SM")
nucB = sp.expand(EB(qn, 0).subs(wL, 0) - EB(qp, 0).subs(wL, 0)).subs(sl, 0)
check("B: nucleon-only n - p = -w_N/3 - s_q/3", sp.simplify(nucB - (-wN / 3 - sq / 3)) == 0,
      "PairwiseChargeEnergyBeta.nucleon_em_split_SM")

# ── Arm C ─────────────────────────────────────────────────────────────────────────────
D4 = (q + 1 / q) ** 4
D3 = (q + 1 / q) ** 3
allp = {nuc: diag_op(nuc, lambda c, cl=cl: pair(list(c) + [cl])) for nuc, cl in (("n", 0), ("p", -1))}
adj = {nuc: diag_op(nuc, lambda c, cl=cl: c[0] * c[1] + c[1] * c[2] + c[2] * cl) for nuc, cl in (("n", 0), ("p", -1))}
V = {"n": VN, "p": VP}
KW = {"n": (1 / q) * q, "p": q * (1 / q)}  # nucleon K-weight × lepton K-weight (ν: q, e⁻: q⁻¹)


def tr(X, nuc, connected):
    t = (X * V[nuc]).trace()
    if connected:
        t -= X.trace() / 3 * V[nuc].trace()
    return KW[nuc] * t


def split4(ops, connected):
    return sp.factor(sp.simplify((tr(ops["n"], "n", connected) - tr(ops["p"], "p", connected)) / D4))


C1 = split4(allp, False)
C2 = split4(allp, True)
C3 = split4(adj, False)
C4 = split4(adj, True)
check("C1 covariant raw = -2P/(3q^2(q^2+1)^4)", sp.simplify(C1 - (-2 * P / (3 * q**2 * (q**2 + 1) ** 4))) == 0,
      "PairwiseChargeEnergyBeta.covariant_raw_split")
check("C2 covariant connected = 0", C2 == 0, "PairwiseChargeEnergyBeta.covariant_connected_split")
check("C3 adjacent raw closed form",
      sp.simplify(C3 - (3 * q**10 - 10 * q**8 + 13 * q**6 - 8 * q**4 + 4 * q**2 - 1) / (3 * (q**2 + 1) ** 4)) == 0,
      "PairwiseChargeEnergyBeta.adjacent_raw_split")
check("allPairs4 scalars", allp["n"] == R(-1, 3) * sp.eye(3) and allp["p"] == -sp.eye(3),
      "PairwiseChargeEnergyBeta.allPairs4_nNu/_pE")
# corpus nucleon-only all-pairs raw (3 strands, [2]^3): t(W_n) - t(W_p)
Nraw = sp.factor(sp.simplify(((1 / q) * (R(-1, 3) * VN.trace()) - q * 0) / D3))
check("nucleon all-pairs raw = P/(3q^4(q^2+1)^3)", sp.simplify(Nraw - P / (3 * q**4 * (q**2 + 1) ** 3)) == 0,
      "NucleonWeightSpaceQTrace.deltaT_allPairs_raw_eq")
check("q=1 values: C1 = 1/8, nucleon raw = -1/8", C1.subs(q, 1) == R(1, 8) and Nraw.subs(q, 1) == R(-1, 8), "arith")

rows = {}
for name, ex in (("C1_covariant_raw_beta", C1), ("C2_covariant_connected_beta", C2),
                 ("C3_adjacent_raw_beta", C3), ("C4_adjacent_connected_beta", C4),
                 ("N_nucleon_allpairs_raw_n_minus_p", Nraw)):
    t0 = at_q0(ex) if ex != 0 else mp.mpf(0)
    rows[name] = {"exact": str(ex), "t_at_q0": nstr(t0, DPS),
                  "plus_me_t_MeV": nstr(ME * t0, 40), "minus_me_t_MeV": nstr(-ME * t0, 40)}
    print(f"{name:36s} t(q0) = {nstr(t0, 20):>28s}   ±m_e·t = {nstr(ME * t0, 15)} MeV")

P0 = at_q0(P)
trV0 = at_q0(-P / q**6)
check("trV3(q0) > 0 (so the static pair term has a definite sign)", trV0 > 0, "trace_borromeanV3A")
nuc_plus = ME * at_q0(Nraw)
print(f"m_e·t nucleon all-pairs raw = {nstr(nuc_plus, 15)} MeV vs CODATA m_n-m_p {MN_MINUS_MP_CODATA}"
      f" ({nstr(100 * nuc_plus / MN_MINUS_MP_CODATA, 6)} %)")
beta_plus = ME * at_q0(C1)
print(f"m_e·t β covariant raw       = {nstr(beta_plus, 15)} MeV vs CODATA Q_β {QBETA_CODATA}"
      f" ({nstr(100 * beta_plus / QBETA_CODATA, 6)} %)")

n_fail = sum(1 for _, ok, _ in checks if not ok)
wb = WitnessBuilder("qbeta-pairwise-em-split", engine="sympy+mpmath", output_dir=HERE)
for name, ok, src in checks:
    wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
wb.save({
    "q0Anchor": "proton",
    "q0AnchorReason": "qou_substrate.constants.q_at (proton pin), owner directive 2026-08-07",
    "q0": nstr(Q0, DPS),
    "m_e_MeV": str(ME),
    "dps": DPS,
    "lean_module": "QOU.QuarkState.PairwiseChargeEnergyBeta",
    "armA_uniform_split": "(2w - 4s)/3 ; zero iff w = 2s",
    "armB_two_weight_split": "w_L - w_N/3 - s_q/3 - s_l ; nucleon-only -w_N/3 - s_q/3",
    "armC": rows,
    "P_at_q0": nstr(P0, DPS),
    "trV3_at_q0": nstr(trV0, DPS),
    "comparison_only": {"m_n_minus_m_p_CODATA_MeV": str(MN_MINUS_MP_CODATA), "Q_beta_CODATA_MeV": str(QBETA_CODATA),
                        "nucleon_raw_plus_sign_MeV": nstr(nuc_plus, 30),
                        "beta_covariant_raw_plus_sign_MeV": nstr(beta_plus, 30)},
    "premises": ["E1 spectator lepton strand (not in corpus)", "E2 [2]_q^4 normalisation (n=4 extension)",
                 "overall sign of m_e·t not fixed by corpus (pre-registered +, compute -)",
                 "coupling w not derived (NeutronProtonEMSign)"],
    "n_checks": len(checks), "n_fail": n_fail,
})
sys.exit(1 if n_fail else 0)
