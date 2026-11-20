#!/usr/bin/env python3
"""weak_scale_w_mass_probe — can the corpus fix m_W, g and G_F for the β-decay rate?

Bean qou-99qc. Pre-registered in PREREGISTRATION.md (2d2cf79744) before this file was run.
Lean twin: QOU/QuarkState/WeakScaleFactorisation.lean (sorry-free, generic Field).

Sections
  A. corpus designations of the weak objects, read from the files (not chosen here);
  B. reach of the canonical mass channel m = m_e·Vol·ρ/ℏ_q² on those objects;
  C. dimensionless crossing couplings h, hq, h/q at q₀ (candidates for g; none selected);
  D. 𝔇_n/G_F² on both derived Q_β cells (label C, owner-scored), select neither;
  E. the corpus's CONDITIONAL N_v = v/m_p fixed point (three underived slots), labelled;
  F. comparison only: m_W, G_F, 𝔇_n — read last.

mpmath at 70 dps, proton q₀ via qou_substrate.constants.q_at(70). No float64 in any computed value.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
sys.path.insert(0, str(_ROOT / "tools/qou-substrate/python"))

import mpmath as mp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
FAILED: list = []
QOU = _ROOT / "folio/quantum-observable-universe"


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def read(rel):
    return (QOU / rel).read_text(encoding="utf-8")


# ------------------------------------------------------------------ A. designations
def designations():
    dic = read("knots-particles-confinement/knot-particle-dictionary-table1-data.md")
    skein = read("predicted-spectra/beta-decay-skein.md")
    ew = read("knots-particles-confinement/electroweak-higgs-torus-link-triplet.md")
    ewts = read("knots-particles-confinement/electroweak-higgs-torus-link-triplet.ts")
    pion = read("knots-particles-confinement/pion-mass-hyperbolic-threshold.md")
    check("A1.T35_is_beta_vertex",
          bool(re.search(r"T_\{3,5\}.*Weak force \(\$\\beta\$-decay\)", dic)) and "(\\sigma_1\\sigma_2)^5" in skein,
          "T_{3,5} = (σ1σ2)^5 is the β-decay vertex (dictionary + beta-decay-skein)")
    check("A2.W_is_T24_conjecture",
          r"W^{\pm} \;\longleftrightarrow\; T(2,4)" in ew and "export default conjecture(" in ewts,
          "W± ↔ T(2,4) appears only inside conj:electroweak-higgs-torus-link-triplet")
    check("A3.WZ_slot_free_label", "is a free label" in ew,
          "the corpus itself records the W vs Z slot as a free label")
    check("A4.volume_channel_hyperbolic_only",
          "the volume formula reaches exactly the hyperbolic sector" in pion
          and "the mass is *not derivable from volume*, not that it is zero" in pion,
          "rem:pion-mass-hyperbolic-threshold: Vol = 0 ⇒ mass not derivable from volume")
    return {"beta_vertex": "T_{3,5} = (sigma1 sigma2)^5, torus knot 10_124",
            "W_pm": "T(2,4), conjectural (conj:electroweak-higgs-torus-link-triplet; C1, C_sector open)",
            "Z": "T(2,6), conjectural", "H": "T(2,8), conjectural"}


# ------------------------------------------------------------------ B. channel reach
def torus_genus(p, r):
    return (p - 1) * (r - 1) // 2


def channel_reach():
    # Torus knots/links are Seifert-fibred: no hyperbolic structure, Vol = 0 (Thurston).
    out = {}
    for name, (p, r) in {"T(3,5)": (3, 5), "T(2,4)": (2, 4), "T(2,6)": (2, 6), "T(2,8)": (2, 8)}.items():
        out[name] = {"torus_type": f"({p},{r})", "seifert_fibred": True, "hyperbolic_volume": "0",
                     "mass_from_volume_channel": "not derivable (Vol = 0)"}
    check("B1.T35_genus4", torus_genus(3, 5) == 4, "g(T_{3,5}) = (3-1)(5-1)/2 = 4 (saturating carrier)")
    # P2: no corpus ratio ties m_W to a Vol = 0 anchor
    hits = []
    for f in QOU.rglob("*.md"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"m_\{?W\}?\s*/\s*m_\{?(e|\\mathfrak\{e\}|\\pi|p|\\mathfrak\{p\})\}?", t):
            hits.append(str(f.relative_to(_ROOT)))
    check("B2.no_mW_over_anchor_ratio", not hits, f"no m_W/m_e, m_W/m_π, m_W/m_p ratio in folio .md ({len(hits)} hits)")
    return out


# ------------------------------------------------------------------ C. couplings
def couplings(q0):
    h = q0 - 1 / q0
    return {"h": h, "hq": h * q0, "h_over_q": h / q0, "h_sq": h ** 2,
            "alphaW_if_g_eq_h": h ** 2 / (4 * mp.pi), "alphaW_if_g_eq_hq": (h * q0) ** 2 / (4 * mp.pi)}


# ------------------------------------------------------------------ D. rate per G_F²
def fermi_f(W0):
    """f(W0) = ∫_1^{W0} p W (W0 − W)² dW, F(Z,W) = 1."""
    return mp.quad(lambda W: mp.sqrt(W ** 2 - 1) * W * (W0 - W) ** 2, [1, W0])


def rate_cells(q0, me):
    b = q0 + 1 / q0
    yC = b ** 2 / (b ** 2 + 2)
    Q_C = me * (q0 + 1) * (q0 ** 2 + 1) / (2 * q0 ** 3) * yC      # label C T⁺ round trip (#8638)
    Q_S = mp.mpf("0.325433929")                                  # owner-scored cell (#8586), quoted
    check("D1.QC_value", abs(Q_C - mp.mpf("0.588715")) < mp.mpf("1e-6"), f"Q_C = {mp.nstr(Q_C, 12)} MeV")
    M2 = (q0 ** 2 - 1) ** 2
    rows = {}
    for name, Q in (("label_C_Tplus_roundtrip", Q_C), ("owner_scored", Q_S)):
        f = fermi_f(1 + Q / me)
        rows[name] = {"Q_beta_MeV": Q, "f": f, "normSq": M2,
                      "D_over_GF2_MeV5": M2 * me ** 5 * f / (2 * mp.pi ** 3)}
    return rows


# ------------------------------------------------------------------ E. conditional N_v
def qi(q, n):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def nv_conditional(q0):
    T = q0 * qi(q0, 2) / 2 * qi(q0, 4) * qi(q0, 6) * qi(q0, 8) + 1 / mp.pi
    H = qi(q0, 2) / (8 * mp.pi)
    hb = 1 - 1 / q0
    a = mp.findroot(lambda a: hb ** 2 * H * a ** 3 - H * a ** 2 + T * a - 1, 1 / T)
    return 1 / a


def main() -> int:
    q0 = C.q_at(DPS)
    me = mp.mpf(C.M_E_MEV_STR)
    mpe = mp.mpf(C.MASS_RATIO_P_E_STR)
    log(f"q0 = {mp.nstr(q0, 30)} (proton pin, {DPS} dps)")
    log("A. designations"); des = designations()
    log("B. canonical mass channel reach"); reach = channel_reach()
    log("C. couplings"); cpl = couplings(q0)
    for k, v in cpl.items():
        log(f"  {k} = {mp.nstr(v, 15)}")
    log("D. rate per G_F²"); rows = rate_cells(q0, me)
    log("E. conditional N_v (ElectroweakVevFixedPointClass, NO instance; beans qou-rpt1, qou-myxi)")
    Nv = nv_conditional(q0)
    check("E1.Nv_reproduces_corpus", abs(Nv - mp.mpf("262.418168819")) < mp.mpf("1e-8"), f"N_v = {mp.nstr(Nv, 15)}")
    v_over_me = Nv * mpe
    GF_cond_me2 = 1 / (mp.sqrt(2) * v_over_me ** 2)                 # G_F·m_e², dimensionless, conditional
    # ---------------------------------------------------- F. comparison only
    log("F. comparison (read last)")
    hbar = mp.mpf("6.582119569e-22"); tau = mp.mpf("878.4"); Dn = hbar / tau
    GF_pdg = mp.mpf("1.1663788e-11")            # MeV⁻²
    mW_pdg = mp.mpf("80370")                    # MeV
    gSM = 2 * mW_pdg * mp.sqrt(mp.sqrt(2) * GF_pdg)
    comp = {"D_n_MeV": Dn, "G_F_MeV-2": GF_pdg, "m_W_MeV": mW_pdg, "m_W_over_m_e": mW_pdg / me,
            "g_SM_from_GF_mW": gSM, "alpha2_SM": gSM ** 2 / (4 * mp.pi)}
    GF_cond = GF_cond_me2 / me ** 2
    comp["G_F_conditional_over_pdg"] = GF_cond / GF_pdg
    for k, r in rows.items():
        r["GF_required_MeV-2"] = mp.sqrt(Dn / r["D_over_GF2_MeV5"])
        r["GF_required_over_pdg"] = r["GF_required_MeV-2"] / GF_pdg
        r["rate_with_pdg_GF_over_Dn"] = GF_pdg ** 2 * r["D_over_GF2_MeV5"] / Dn
        r["rate_with_conditional_GF_over_Dn"] = GF_cond ** 2 * r["D_over_GF2_MeV5"] / Dn
        for gname in ("h", "hq", "h_over_q"):
            # m_W that the rate would need IF g were this coupling (inverting the target: comparison only)
            r[f"mW_required_if_g_eq_{gname}_over_me"] = cpl[gname] * mp.sqrt(mp.sqrt(2) / (8 * r["GF_required_MeV-2"])) / me
        log(f"  {k}: Q={mp.nstr(r['Q_beta_MeV'], 10)} f={mp.nstr(r['f'], 10)} G_F,req/G_F={mp.nstr(r['GF_required_over_pdg'], 8)} "
            f"𝔇(G_F)/𝔇_n={mp.nstr(r['rate_with_pdg_GF_over_Dn'], 8)} 𝔇(G_F,cond)/𝔇_n={mp.nstr(r['rate_with_conditional_GF_over_Dn'], 8)}")
    log(f"  N_v={mp.nstr(Nv, 15)}  G_F,cond/G_F,pdg={mp.nstr(comp['G_F_conditional_over_pdg'], 12)}  g_SM={mp.nstr(gSM, 10)}")
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("weak-scale-w-mass", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: the corpus designates the beta vertex T_{3,5} and (conjecturally) W = T(2,4); both "
                       "are torus (Vol = 0), so the canonical volume channel derives no m_W/m_e. g is not fixed by the "
                       "strand-tracked crossing. Rate per G_F^2 on both Q_beta cells; N_v route conditional. "
                       "Pre-registered at 2d2cf79744. Not wired to any scorecard.")
    wb.add_parameter("q0", C.q_str(DPS))
    wb.add_parameter("dps", DPS)
    wb.add_data("designations", des)
    wb.add_data("channel_reach", reach)
    wb.add_data("couplings_at_q0", {k: fmt(v) for k, v in cpl.items()})
    wb.add_data("rate_cells", {k: {kk: fmt(vv) for kk, vv in r.items()} for k, r in rows.items()})
    wb.add_data("conditional_Nv", {"N_v": fmt(Nv), "v_over_m_e": fmt(v_over_me), "G_F_times_me2": fmt(GF_cond_me2),
                                   "status": "conditional: ElectroweakVevFixedPointClass has no instance; "
                                             "underived slots qou-rpt1 (q[2]/2 prefactor), qou-myxi (sign, alpha_loop)"})
    wb.add_data("comparison", {k: fmt(v) for k, v in comp.items()})
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
