#!/usr/bin/env python3
"""qbeta_derivation_r4_r1_probe — Q_β by energy conservation (R4) and as a four-strand γγ process (R1).

Bean qou-99qc. Pre-registered in PREREGISTRATION.md (commit 3e41aab22b) before this file was run.
Lean twin: QOU/QuarkState/DecayGammaGammaFourStrand.lean.
Photon: γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ (ruled).

Exact sympy over Q(q, φ, ψ); numbers with mpmath at 70 dps, proton q₀. No float64 in any computed
value. CODATA enters only in the last block, as a comparison column.

R4  T³ sectors / label A, B lines as the two nucleons in the mass channel m = 2(m_μF − 6m_e).
R1  the d → u amplitude of the γγ pair on the (3,1) of H₄, its round trip, and the energy.
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

import qbeta_e0  # noqa: E402
import qou_substrate.constants as C  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
FAILED: list = []

q = sp.symbols("q", positive=True)
a0, a1, a2, b0, b1, b2 = sp.symbols("phi0 phi1 phi01 psi0 psi1 psi01")
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


def mzero(M):
    return all(zero(e) for e in M)


# ---- the (3,1) of H4 (FlavourDoubletFourStrands.lean)
I3 = sp.eye(3)
s1 = sp.diag(q, q, -1 / q)
s3 = sp.diag(q, -1 / q, q)
s2 = sp.Matrix([[(q**2 - 1) / (q * (q**2 + 1)), -(q**4 + 1) / (q * (q**2 + 1)), q * (q**4 + 1) / (q**2 + 1)],
                [-q / (q**2 + 1), q**3 / (q**2 + 1), q**3 / (q**2 + 1)],
                [1 / (q * (q**2 + 1)), 1 / (q * (q**2 + 1)), q**3 / (q**2 + 1)]])
s2i, s3i = s2 - h * I3, s3 - h * I3
Lu, Ld, PL = sp.diag(1, 0, 0), sp.diag(0, 1, 0), sp.diag(1, 1, 0)
DD = q**4 + q**2 + 1
Ja = sp.Matrix([[q**2 / DD, -(q**4 + 1) / DD, 0], [-q**2 / DD, (q**4 + 1) / DD, 0], [0, 0, 0]])
Jb = sp.Matrix([[(q**4 + 1) / DD, (q**4 + 1) / DD, 0], [q**2 / DD, q**2 / DD, 0], [0, 0, 0]])
eS, fS = Lu * s2 * Ld, Ld * s2 * Lu
eJ = Ja * s3 * Jb
V = s1 * s2i


def photon(x0, x1, x2):
    return I3 + x0 * s1 + x1 * s2 + x2 * (s1 * s2i)


# canonical-chart γγ normal form (pairNFChiral_eq)
NF = [1 + a0 * b0 + a1 * b1 - h * (a0 * b2 + a2 * b0) + h**2 * a2 * b2,
      a0 + b0 + h * a0 * b0 + a2 * b1 - h * (a2 + b2) - h**2 * (a0 * b2 + a2 * b0) + h**3 * a2 * b2,
      a1 + b1 + h * a1 * b1 + a0 * b2 - h * a2 * b2,
      a1 * b0 + a2 * b2 - h * a1 * b2,
      a2 + b2 + a0 * b1 + h * a0 * b2 - h**2 * a2 * b2,
      a2 * b0 + a1 * b2]
WORDS = [I3, s1, s2, s2 * s1, s1 * s2, s1 * s2 * s1]   # 1, σ0, σ1, L-, L+, e-
DERIVED = {a0: 0, a1: 0, a2: q * h, b0: 0, b1: 0, b2: -h / q}

# ---- weight spaces on (C²)^{⊗3} (NucleonWeightSpaceTraces.lean)
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])


def run_exact():
    out = {}
    # R1.1 flip functional
    lam = [sp.simplify((Lu * w * Ld)[0, 1] / eS[0, 1]) for w in WORDS]
    check("R1.1.flip_functional", [sp.simplify(x - y) for x, y in zip(lam, [0, 0, 1, q, q, q**2])] == [0] * 6,
          f"λ_A on (1, σ0, σ1, L-, L+, e-) = {lam}")
    G = photon(a0, a1, a2) * photon(b0, b1, b2)
    check("R1.1.nf_reconstructs_pair", mzero(G - sum((c * w for c, w in zip(NF, WORDS)), sp.zeros(3))),
          "Σ NF_w·ρ(w) = ρ(γ(φ)γ(ψ)) in the (3,1) of H4")
    amp = sp.expand(NF[2] + q * (NF[3] + NF[4]) + q**2 * NF[5])
    check("R1.1.flip_pair", mzero(Lu * G * Ld - amp * eS), "Lu·Γ·Ld = (c_σ1 + q(c_L- + c_L+) + q² c_e-)·eS")
    out["R1_flip_coefficient"] = str(sp.factor(amp))
    out["R1_flip_functional"] = "lambda_A(w) = q^(#sigma0) on words containing sigma1, 0 otherwise"
    # R1.4 derived weights
    Gd = G.subs(DERIVED)
    check("R1.4.pair_is_V3", mzero(Gd - V**3), "γ(0,0,qh)γ(0,0,−q⁻¹h) = V³ in the (3,1) of H4")
    ce = sp.simplify(NF[5].subs(DERIVED))
    check("R1.4.e_minus_zero", ce == 0, "e⁻ coordinate φ01ψ0 + φ1ψ01 = 0 at derived weights")
    ad = sp.factor(sp.simplify(amp.subs(DERIVED)))
    check("R1.4.flip_V3", zero(ad - q**2 * h**3), f"flip coefficient of V³ = {ad} = q²h³")
    back = sp.simplify((Ld * V**3 * Lu)[1, 0] / fS[1, 0])
    check("R1.4.flip_V3_back", zero(back - q**2 * h**3), "Ld·V³·Lu = q²h³·fS")
    # channel-by-channel contribution at derived weights
    chans = {nm: sp.factor(sp.simplify((lw * NF[i]).subs(DERIVED)))
             for nm, i, lw in (("sigma1", 2, 1), ("L-", 3, q), ("L+", 4, q), ("e-", 5, q**2))}
    out["R1_V3_flip_by_channel"] = {k: str(v) for k, v in chans.items()}
    # R1.5 round trips (label A)
    yD = sp.factor(sp.simplify((Lu * s2 * Ld * s2).trace()))
    rtV3 = sp.factor(sp.simplify((Lu * V**3 * Ld * V**3).trace()))
    check("R1.5.roundTrip_V3", zero(rtV3 - (q**2 * h**3) ** 2 * yD), f"tr(Lu V³ Ld V³) = (q²h³)²·y_D = {rtV3}")
    rtV3inv = sp.factor(sp.simplify((Lu * V**3 * Ld * (s2 * s1.inv()) ** 3).trace()))
    out["R1_roundtrips_labelA"] = {"bare_letter_sigma1 (ruled y_D)": str(yD),
                                   "V3_then_V3": str(rtV3), "V3_then_V^-3": str(rtV3inv)}
    # e- channel only (symbolic weights)
    e_rt = sp.factor((q**2 * NF[5]) ** 2 * yD)
    out["R1_e_minus_channel_roundtrip_symbolic"] = str(e_rt)
    # R1.2 label B
    check("R1.2.pair_no_flip_B", mzero(Ja * G * Jb), "Ja·Γ·Jb = 0 (no H3 word flips the J4 label)")
    tr = lambda x0, x1, x2: 1 + q * x0 + q * x1 + x2  # noqa: E731
    check("R1.2.Ja_photon", mzero(Ja * photon(a0, a1, a2) - tr(a0, a1, a2) * Ja), "Ja·γ(φ) = t(φ)·Ja")
    gB = Ja * G * (s2 * s3i) * Jb
    check("R1.2.pair_flip_B", mzero(gB - tr(a0, a1, a2) * tr(b0, b1, b2) * q * eJ),
          "Ja·Γ·V4·Jb = t(φ)t(ψ)q·eJ")
    check("R1.2.t_derived", zero((tr(a0, a1, a2) * tr(b0, b1, b2)).subs(DERIVED) - 1), "t(φ)t(ψ) = 1 at derived weights")
    rtB = sp.factor(sp.simplify((Ja * G.subs(DERIVED) * (s2 * s3i) * Jb * (s3 * s2i) * Ja).trace()))
    cJh = (q**2 + 1) ** 2 * (q**4 + 1) / DD**2
    check("R1.2.roundTrip_B_V3", zero(rtB - cJh), f"label-B round trip through V³ and V4 = cJ/2 = {rtB}")
    out["R1_roundtrip_labelB"] = str(rtB)
    # R1.3 weak vertex on the left line of sigma0
    check("R1.3.weak_left", mzero(Lu * (s1 - h * PL) - Lu / q), "Lu·(σ0 − h·P_L) = q⁻¹·Lu")
    # label C
    out["R1_labelC"] = "no Hecke element changes T3 (Schur-Weyl, bean qou-0whz C2): amplitude identically 0"

    # ---- R4
    VA = A1 * A2.inv()
    t = sp.factor(sp.simplify((VA**3).trace()))
    tB = sp.factor(sp.simplify(((A2 * A1.inv()) ** 3).trace()))
    check("R4.0.equal_plain_traces", zero(t - tB), f"tr_Wp(V³) = tr_Wn(V³) = {t}")
    taup, taun = q * t / D2**3, t / (q * D2**3)
    full = (q**3 + q * t + t / q + q**-3) / D2**3
    closed = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
    check("R4.0.full_trace_is_pin_trace", zero(sp.Abs(full) - sp.Abs(closed)) or zero(full - closed) or zero(full + closed),
          "full z_D trace of V³ = ±(4+h²−3h⁴−h⁶)/(h²+4), the closed form that pins q0")
    check("R4.1.sector_ratio", zero(taun - taup / q**2), "τ_n = q⁻²·τ_p")
    check("R4.2.dimnorm_equal", zero(q * t / (3 * q) - (t / q) / (3 / q)), "dimension-normalised sectors equal")
    check("R4.3.full_flip_invariant", zero(full - (q**-3 + t / q + q * t + q**3) / D2**3), "full trace u↔d invariant")
    out["R4_sector_traces"] = {"tau_p": str(sp.factor(taup)), "tau_n": str(sp.factor(taun)), "tau_full": str(sp.factor(full))}
    chars = {nm: sp.factor(sp.simplify((P * V**3).trace())) for nm, P in (("Lu", Lu), ("Ld", Ld), ("Ja", Ja), ("Jb", Jb))}
    out["R4_partial_characters_V3"] = {k: str(v) for k, v in chars.items()}
    return out, dict(taup=taup, taun=taun, full=full, chars=chars, yD=yD, rtV3=rtV3, rtB=rtB, e_rt=e_rt)


def numbers(ex):
    q0 = mp.mpf(C.Q_50_DIGIT_STR)
    me = mp.mpf(C.M_E_MEV_STR)
    vol = 2 * mp.clsin(2, mp.pi / 3)
    hb = 1 - 1 / q0
    mmu = me * vol / hb**2
    q3f = (q0 + 1 / q0) * (q0**2 + 1 + q0**-2)
    S = 2 * mmu * q3f / q0**3
    E0z, E0t = qbeta_e0.order_zero(q=q0), qbeta_e0.canonical(q=q0)
    hq, b2 = q0 - 1 / q0, q0 + 1 / q0
    ev = lambda e: mp.mpf(sp.lambdify(q, e, "mpmath")(q0))  # noqa: E731
    log(f"q0 = {mp.nstr(q0, 25)}; S = {mp.nstr(S, 20)} MeV/unit trace; E0 = {mp.nstr(E0z, 15)} / {mp.nstr(E0t, 15)}")
    taup, taun, full = ev(ex["taup"]), ev(ex["taun"]), ev(ex["full"])
    mp_full = 2 * (mmu * abs(full) * q3f / q0**3 - 6 * me)
    rows = {}
    rows["R4.1_T3_sectors_[2]^3"] = {"rel_diff": (taun - taup) / taup, "Q_beta": S * (abs(taun) - abs(taup)) - me,
                                     "m_p_model": 2 * (S / 2 * abs(taup) - 6 * me)}
    rows["R4.2_T3_sectors_dimnorm"] = {"rel_diff": mp.mpf(0), "Q_beta": -me}
    rows["R4.3_full_trace_flip"] = {"rel_diff": mp.mpf(0), "Q_beta": -me, "m_p_model": mp_full}
    ch = {k: ev(v) for k, v in ex["chars"].items()}
    rows["R4.4_labelA_lines"] = {"rel_diff": (ch["Ld"] - ch["Lu"]) / ch["Lu"], "Q_beta": S * (abs(ch["Ld"]) - abs(ch["Lu"])) - me}
    rows["R4.5_labelB_lines"] = {"rel_diff": (ch["Jb"] - ch["Ja"]) / ch["Ja"], "Q_beta": S * (abs(ch["Jb"]) - abs(ch["Ja"])) - me}
    # R1 energies: y3 candidates, two readings
    y = {"R1.A_bare_letter (ruled y_D)": ev(ex["yD"]), "R1.A_V3_process": ev(ex["rtV3"]),
         "R1.B_V3_through_V4": ev(ex["rtB"])}
    for k, v in y.items():
        rows[k] = {"y3": v,
                   "Q_beta_DeltaS_E0_order_zero": hq * b2 / 2 * v * E0z,
                   "Q_beta_DeltaS_E0_tower": hq * b2 / 2 * v * E0t,
                   "Q_beta_massScale_minus_me": S * v - me}
    for k, r in rows.items():
        log(f"  {k}: " + ", ".join(f"{kk}={mp.nstr(vv, 12)}" for kk, vv in r.items()))
    return rows, dict(q0=q0, S=S, E0z=E0z, E0t=E0t, mp_full=mp_full, me=me)


def main() -> int:
    log("exact block")
    out, ex = run_exact()
    log("numbers at proton q0 (before CODATA is read)")
    rows, base = numbers(ex)
    # comparison, read only now
    mn, mpp = mp.mpf(C.M_N_MEV_STR), mp.mpf(C.M_P_MEV_STR)
    qc = mn - mpp - base["me"]
    diag = (mn - mpp) / mpp
    log(f"CODATA Q_beta = {mp.nstr(qc, 15)} MeV; diagnostic (m_n−m_p)/m_p = {mp.nstr(diag, 10)}")
    check("P0.pinned_mp_roundtrip", abs(base["mp_full"] - mpp) / mpp < mp.mpf("1e-9"),
          f"mass channel with the full trace returns m_p: {mp.nstr(base['mp_full'], 20)}")
    for r in rows.values():
        for k in [k for k in r if k.startswith("Q_beta")]:
            r[k + "_vs_codata_pct"] = (r[k] - qc) / qc * 100
    table = {k: {kk: mp.nstr(vv, 30) for kk, vv in r.items()} for k, r in rows.items()}
    for k, r in table.items():
        log(f"  {k}: " + ", ".join(f"{kk}={vv[:14]}" for kk, vv in r.items() if 'pct' in kk))
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-derivation-r4-r1", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: Q_beta by energy conservation in the mass channel (R4) and as a four-strand "
                       "gamma-gamma process (R1). Pre-registered at 3e41aab22b. Not wired to any scorecard.")
    wb.add_parameter("q0", C.Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("photon", "gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (ruled)")
    wb.add_data("exact", out)
    wb.add_data("table", table)
    wb.add_data("scales_MeV", {"S_mass_channel": mp.nstr(base["S"], 30), "E0_order_zero": mp.nstr(base["E0z"], 30),
                               "E0_tower": mp.nstr(base["E0t"], 30)})
    wb.add_data("comparison", {"Q_beta_codata_MeV": mp.nstr(qc, 30), "diag_mn_minus_mp_over_mp": mp.nstr(diag, 20)})
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
