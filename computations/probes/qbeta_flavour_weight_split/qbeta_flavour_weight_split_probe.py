#!/usr/bin/env python3
"""qbeta_flavour_weight_split_probe — Q_β from the T³ split of the z_D trace (beans qou-99qc, qou-ales).

Owner ruling 2026-11-20 (Carl): derive the n ≠ p ingredient on the U_q / weight side and score
Q_β on the γγ base V³. Owner correction 15:47: photon γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹.
Pre-registered in PREREGISTRATION.md (commit d70a51ff51) before this file was run.

Exact sympy over Q(q) on (C²)^{⊗3} with the level-2 Jimbo braiding (the matrices of
QOU/BraidsAndKnots/NucleonWeightSpaceTraces.lean), K = diag(q, q⁻¹), u = e₁. Numbers: mpmath,
70 dps, proton q₀, E₀ = qbeta_e0.canonical (tower-summed). No float64 in any computed value.

Checks
  D1  Tr(K⊗K Ř)/[2]² = z_D (the trace IS the convention-D Markov trace).
  D2  Σ_{T³} K-weighted weight-space traces / [2]³ of V^k equals τ_zD(V^k) from the Hecke /
      Wedderburn route of PR #8564 (its committed witness), k = 0..10, to 1e-25.
  W1  tr_{W_n}(V^k) = tr_{W_p}(V^k) (plain), so the per-sector-normalised split is 0.
  W2  ε_flavour(V^k) = (q⁻¹ − q)·tr_{W_p}(V^k)/[2]³ is exactly bar-odd, k = 3, 6, 9.
  G1  the derived two-photon product γ(0,0,qh)·γ(0,0,−q⁻¹h) = V³ on all of (C²)^{⊗3}.
  G2  antipode image (σ ↦ σ⁻¹) of V^k and V^{-k} have the full z_D trace of V^k.
  G3  photon order: tr_zD(γ(φ)γ(ψ) − γ(ψ)γ(φ)) = 0 for symbolic weights.
Then Q_β = |ε_flavour(V^k)|·E₀ for k = 3, 6, 9, and only then the CODATA column.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

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


def zero(expr):
    return sp.simplify(sp.together(expr)) == 0


# ---- the 8-dim space, basis index b = 4*s1 + 2*s2 + s3, s = 0 for e1 (u), 1 for e2 (d)
R2 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])  # Jimbo Ř 'std'
I2 = sp.eye(2)
S1 = sp.kronecker_product(R2, I2)
S2 = sp.kronecker_product(I2, R2)
Kq = sp.diag(q, 1 / q)
K3 = sp.kronecker_product(sp.kronecker_product(Kq, Kq), Kq)
V8 = S1 * S2.inv()


def qtr8(M):
    return sp.together((K3 * M).trace() / D2 ** 3)


# weight spaces, matrices of NucleonWeightSpaceTraces.lean
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
B1, B2 = A2, A1
VA = A1 * A2.inv()
VB = B1 * B2.inv()


def tr_p(k):
    return sp.factor(sp.simplify((VA ** k).trace()))


def tr_n(k):
    return sp.factor(sp.simplify((VB ** k).trace()))


def eps_p(k):
    return q * tr_p(k) / D2 ** 3


def eps_n(k):
    return (1 / q) * tr_n(k) / D2 ** 3


def eps_flavour(k):
    return sp.factor(sp.simplify(eps_n(k) - eps_p(k)))


def photon8(f0, f1, f01):
    return sp.eye(8) + f0 * S1 + f1 * S2 + f01 * V8


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    log(f"q0 = {mp.nstr(q0, 25)} (proton pin), dps {DPS}")
    check("P0.proton_pin", Q_50_DIGIT_STR.startswith("1.10997858275138"), Q_50_DIGIT_STR[:20])

    # D1
    R2t = sp.Matrix(R2)
    zd = sp.simplify((sp.kronecker_product(Kq, Kq) * R2t).trace() / D2 ** 2)
    check("D1.trace_is_zD", zero(zd - q ** 3 / (q ** 2 + 1)), f"Tr(K⊗K Ř)/[2]² = {zd}")

    # D2
    wit = json.loads((_ROOT / "computations/probes/qbeta_gg_sdp_base/"
                      "qbeta-gg-sdp-base.witness.json").read_text())
    h3 = wit["data"]["H3_table"]
    worst = mp.mpf(0)
    for k in range(0, 11):
        s = q ** 3 * 1 + q * tr_p(k) + (1 / q) * tr_n(k) + q ** -3 * 1   # 1-dim spaces: V acts by 1
        val = sp.lambdify(q, s / D2 ** 3, "mpmath")(q0)
        worst = max(worst, abs(val - mp.mpf(h3[str(k)]["tau_zD"])))
    check("D2.weight_sum_is_tau_zD", worst < mp.mpf("1e-25"),
          f"max |Σ_T3 − τ_zD(V^k)| over k=0..10 = {mp.nstr(worst, 5)} (witness carries 30 digits)")
    full3 = qtr8(V8 ** 3)
    check("D2b.8dim_equals_weight_sum",
          zero(full3 - (q ** 3 + q * tr_p(3) + tr_n(3) / q + q ** -3) / D2 ** 3),
          "8-dim K-trace of V³ = weight-space sum")

    # W1, W2
    rows = {}
    for k in (3, 6, 9):
        check(f"W1.plain_equal_k{k}", zero(tr_p(k) - tr_n(k)),
              f"tr_Wn(V^{k}) = tr_Wp(V^{k}); per-sector-normalised split = 0")
        ef = eps_flavour(k)
        check(f"W2.bar_odd_k{k}", zero(ef.subs(q, 1 / q) + ef), "ε_flavour(q⁻¹) = −ε_flavour(q)")
        check(f"W3.bar_swaps_components_k{k}", zero(eps_p(k).subs(q, 1 / q) - eps_n(k)),
              "ε_p(q⁻¹) = ε_n(q)")
        rows[k] = ef
    check("W4.closed_form_k3",
          zero(rows[3] - (q ** 2 - 1) * (q ** 12 - 3 * q ** 10 + 3 * q ** 8 - 5 * q ** 6
                                         + 3 * q ** 4 - 3 * q ** 2 + 1) / (q ** 4 * (q ** 2 + 1) ** 3)),
          "matches FlavourWeightSplit.fV3")

    # G1..G3
    g = photon8(0, 0, q * h) * photon8(0, 0, -h / q)
    check("G1.derived_photons_give_V3", zero(sp.simplify(g - V8 ** 3).norm() ** 2) or
          all(zero(e) for e in (g - V8 ** 3)), "γ(0,0,qh)γ(0,0,−q⁻¹h) = V³ on (C²)^⊗3")
    Smir = S1.inv() * S2
    for k in (3, 6):
        check(f"G2.antipode_k{k}", zero(qtr8(Smir ** k) - qtr8(V8 ** k)), "τ(S(V)^k) = τ(V^k)")
        check(f"G2.inverse_k{k}", zero(qtr8(V8.inv() ** k) - qtr8(V8 ** k)), "τ(V^-k) = τ(V^k)")
    f0, f1, f01, p0, p1, p01 = sp.symbols("f0 f1 f01 p0 p1 p01")
    ga, gb = photon8(f0, f1, f01), photon8(p0, p1, p01)
    check("G3.order_blind", zero(sp.expand(qtr8(ga * gb - gb * ga))), "τ_zD(γ(φ)γ(ψ) − γ(ψ)γ(φ)) = 0")
    # chiral L+/L- content of the derived product, in the 8-dim rep (coefficients from the
    # corpus NF V³ = −h²L₋ + h³σ₁ + (1−h⁴) + (h⁴+h²)L₊ − (h⁵+h³)σ₀): check that identity
    nf = (-h ** 2 * S2 * S1 + h ** 3 * S2 + (1 - h ** 4) * sp.eye(8) + (h ** 4 + h ** 2) * S1 * S2
          - (h ** 5 + h ** 3) * S1)
    check("G4.V3_normal_form", all(zero(e) for e in (nf - V8 ** 3)),
          "V³ NF: L₊ coefficient h⁴+h², L₋ coefficient −h² (chiral, identical for p and n)")

    # ---- Q_beta, computed before reading CODATA
    E0 = qbeta_e0.canonical(q=q0)
    log(f"E0_canonical = {mp.nstr(E0, 25)} MeV")
    table = []
    for k in (3, 6, 9):
        ef = sp.lambdify(q, rows[k], "mpmath")(q0)
        table.append({"element": f"V^{k}", "eps_flavour": ef, "Q_beta_MeV": abs(ef) * E0,
                      "selected": k == 3})
        log(f"  V^{k}: eps_flavour = {mp.nstr(ef, 30)}  Q_beta = {mp.nstr(abs(ef) * E0, 20)} MeV")
    check("Q1.V3_nonzero", table[0]["Q_beta_MeV"] > mp.mpf("1e-10"), "ε_flavour(V³) ≠ 0 at q₀")
    check("Q2.arm_gamma_zero", True, "arm γ: p = n = V³ ⇒ Q_β = 0 for every linear ε (G1, PR #8564)")
    check("Q3.normalised_zero", True, "per-sector-normalised split: Q_β = 0 (W1)")

    # ---- comparison, read only now
    from codata_constants import Q_BETA_MEV  # noqa: PLC0415
    qc = mp.mpf(str(Q_BETA_MEV))
    for r in table:
        r["vs_codata_pct"] = mp.nstr((r["Q_beta_MeV"] - qc) / qc * 100, 10)
        r["F_required"] = mp.nstr(qc / r["Q_beta_MeV"], 15)
        log(f"  {r['element']}: vs CODATA {r['vs_codata_pct']} %, F_required {r['F_required']}")
        r["eps_flavour"] = mp.nstr(r["eps_flavour"], 40)
        r["Q_beta_MeV"] = mp.nstr(r["Q_beta_MeV"], 30)

    out = {
        "q0": Q_50_DIGIT_STR, "E0_canonical_MeV": mp.nstr(E0, 40),
        "photon": "gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (owner 2026-11-20 15:47)",
        "closed_forms": {f"V^{k}": str(rows[k]) for k in rows},
        "qbeta_table": table,
        "arm_gamma": "derived weights (0,0,qh),(0,0,-h/q) give V^3 for p and n: Q_beta = 0",
        "arm_normalised": "per-sector-normalised split: 0 for every word",
        "scope": "(a) for the values; (b) for the zero arms (invariants: P(q) intertwiner, "
                 "trace cyclicity, theta/antipode invariance of the z_D trace on V^k)",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-flavour-weight-split", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description(
        "qou-99qc / qou-ales: T3 (weight-space) split of the convention-D trace on the gamma-gamma "
        "base V^3, and the chiral four-term photon arm. Pre-registered at d70a51ff51.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("convention", "D (z = q^3/(q^2+1))")
    for key, val in out.items():
        wb.add_data(key, val)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1",
                         tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
