#!/usr/bin/env python3
"""m_sym error budget — predicted vs experimental, decomposed to source.

Companion to `/dashboard-low`. The dashboard prints the *value* of the
symmetric binding form `B_sym = α·ln(tr_free/tr_atom)` and the bare ratio
`B_AME / B_sym`. This script instead attaches an **error bar** to the
predicted mass `m_sym = Z·m_p + N·m_n − B_sym` and to the experimental
mass, and decomposes each bar to its inputs, so you can see *where* the
error comes from and how far it sits from the 1-ppQ (1e-15 relative) goal.

Everything is evaluated from the ONE canonical Jones–Markov transfer trace
`tr_m_atom_zn` at q₀, α = E₀ (same provenance as the dashboard).

  m_sym(K) = Z·m_p + N·m_n − α·L(K),   α = m_e/(q₀(q₀−1)),  L = ln(tr_f/tr_a)

PREDICTION error sources (σ_pred):
  δ_mp      Z·σ(m_p)            CODATA proton mass, enters the unbound part
  δ_mn      N·σ(m_n)            CODATA neutron mass, enters the unbound part
  δ_me      (B_sym/m_e)·σ(m_e)  CODATA electron mass, enters α (∝ m_e)
  δ_q0      |dB_sym/dq₀|·σ(q₀)  substrate anchor, enters α AND the trace L
  δ_cmp     α·|L₅₀ − L₈₀|       trace compute floor (dps 50 vs 80)

EXPERIMENT error sources (σ_exp), two reconstructions:
  recon     M = Z·m_p+N·m_n−B_AME : sqrt((Zσmp)²+(Nσmn)²+σB_AME²)
  direct    CODATA nuclear mass (²H–⁴He) / AME atomic mass in u (all)

EXPLORATORY — no production rewire, no fit, no witness emitted.

Usage:  python3 m_sym_error_budget.py            # low group (²H–⁷Li)
        python3 m_sym_error_budget.py 6Li 7Li    # explicit isotopes
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

mp.mp.dps = 60

PPQ = mp.mpf(10) ** 15                       # 1 = 1e-15 relative
U_TO_MEV = mp.mpf("931.49410372")            # CODATA 2022 atomic mass unit
U_TO_MEV_REL_ERR = mp.mpf("2.9e-10")         # rel. unc. of the eV-per-u conv.

LOW = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1),
       ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4)]


def _load_codata():
    """CODATA masses + 1σ uncertainties (MeV).

    Central values + nucleon/electron σ come from the LIVE codata_constants
    module (exactly what the canonical dashboard consumes), so α/E₀ match.
    Direct nuclear masses (m_D … m_4He) come from the validation witness.
    """
    import codata_constants as c
    m = lambda x: mp.mpf(str(x))
    d = json.loads((HERE / "codata-2022-validation-masses.witness.json").read_text())
    v = d["data"]
    g = lambda k: mp.mpf(v[k])
    return {
        "m_e": m(c.M_E_MEV),                "m_e_err": m(c.M_E_MEV_ERR),
        "m_p": m(c.M_P_MEV_VALIDATION),     "m_p_err": m(c.M_P_MEV_VALIDATION_ERR),
        "m_n": m(c.M_N_MEV_VALIDATION),     "m_n_err": m(c.M_N_MEV_VALIDATION_ERR),
        # direct CODATA nuclear masses (where published) + 1σ
        "M": {"2H": (g("m_D_MeV"), g("m_D_MeV_err")),
              "3H": (g("m_T_MeV"), g("m_T_MeV_err")),
              "3He": (g("m_3He_MeV"), g("m_3He_MeV_err")),
              "4He": (g("m_4He_MeV"), g("m_4He_MeV_err"))},
    }


def _ame():
    """(Z,A) → (B_total MeV, σB MeV, M_atomic MeV, σM_atomic MeV, M_atomic_u_relerr)."""
    d = json.loads((HERE / "data" / "ame2020.json").read_text())
    rows = d["entries"].values() if isinstance(d["entries"], dict) else d["entries"]
    out = {}
    for r in rows:
        Z, A = r["Z"], r["A"]
        b = r.get("binding_energy_total_keV")
        if b is None:
            continue
        sb = (r.get("binding_energy_per_A_unc_keV") or 0.0) * A / 1000.0  # MeV
        mu = mp.mpf(str(r["atomic_mass_micro_u"])) * mp.mpf("1e-6")       # u
        smu = mp.mpf(str(r.get("atomic_mass_unc_micro_u") or 0.0)) * mp.mpf("1e-6")
        out[(Z, A)] = (mp.mpf(str(b)) / 1000.0, mp.mpf(str(sb)),
                       mu * U_TO_MEV, smu * U_TO_MEV, (smu / mu if mu else mp.mpf(0)))
    return out


def _q0():
    from q_parameter import Q
    try:
        from qou_substrate.constants import Q_ERR
        qerr = mp.mpf(str(Q_ERR))
    except Exception:
        qerr = mp.mpf("3.2e-12")
    return mp.mpf(str(Q)), qerr


def _trace_L(Z, N, q=None, dps=50):
    from tr_m_atom_via_transfer import tr_m_atom_zn
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=dps, q=q)
    return mp.log(mp.mpf(tf) / mp.mpf(ta))


def _fmt_ppq(x):
    a = abs(x)
    if a == 0:
        return "0"
    if a >= 1e6:
        return f"{float(a):.2e}"
    return f"{float(a):,.1f}"


def main(argv=None) -> int:
    names = argv if argv else [nm for nm, _, _ in LOW]
    sel = {nm: (Z, N) for nm, Z, N in LOW}
    cod = _load_codata()
    ame = _ame()
    q0, q0_err = _q0()
    alpha = cod["m_e"] / (q0 * (q0 - 1))

    print(f"\n  m_sym ERROR BUDGET   α = E₀ = {float(alpha):.6f} MeV"
          f"   q₀ = {float(q0):.13f} ± {float(q0_err):.1e}")
    print(f"  CODATA 1σ (MeV): m_e ±{float(cod['m_e_err']):.1e}  "
          f"m_p ±{float(cod['m_p_err']):.1e}  m_n ±{float(cod['m_n_err']):.1e}"
          f"   |   1 ppQ = 1e-15 relative\n")

    rows = []
    for nm in names:
        Z, N = sel[nm]
        A = Z + N
        L = _trace_L(Z, N)
        B_sym = alpha * L
        m_unb = Z * cod["m_p"] + N * cod["m_n"]
        m_sym = m_unb - B_sym

        # ---- prediction error budget --------------------------------------
        d_mp = Z * cod["m_p_err"]
        d_mn = N * cod["m_n_err"]
        d_me = (B_sym / cod["m_e"]) * cod["m_e_err"]
        # q₀ path (substrate anchor). q₀ enters B_sym = α·L through α in closed
        # form: α = m_e/(q₀²−q₀) ⇒ dα/dq₀ = −m_e(2q₀−1)/(q₀²−q₀)². We take the
        # α-path analytically (exact); the trace-L path dL/dq₀ is of the same
        # order and also ≪ δ_mp, and the canonical trace pins q≡q₀ (its custom-q
        # path only admits canonical crossings), so it is not separately
        # differenced. δ_q0 is ~10³× below δ_mp either way — see note below.
        dalpha_dq0 = -cod["m_e"] * (2 * q0 - 1) / (q0 * (q0 - 1)) ** 2
        d_q0 = abs(L * dalpha_dq0) * q0_err
        # compute floor: production trace (dps 50) vs a deliberately coarse
        # dps-30 recompute. The trace only ever RAISES global dps, so we
        # save/restore mp.mp.dps to actually exercise the coarse path.
        _save = mp.mp.dps
        mp.mp.dps = 30
        L_coarse = _trace_L(Z, N, dps=30)
        mp.mp.dps = _save
        d_cmp = alpha * abs(L - L_coarse)
        sig_pred = mp.sqrt(d_mp**2 + d_mn**2 + d_me**2 + d_q0**2 + d_cmp**2)

        # ---- experiment error budget --------------------------------------
        b_ame, sb_ame, m_atom, sm_atom, m_u_relerr = ame[(Z, A)]
        # reconstruction M = Z·m_p + N·m_n − B_AME (dashboard's experimental col)
        m_exp_rec = m_unb - b_ame
        sig_exp_rec = mp.sqrt(d_mp**2 + d_mn**2 + sb_ame**2)
        # direct CODATA nuclear mass where published, else atomic−Z·m_e
        if nm in cod["M"]:
            m_exp_dir, sig_exp_dir = cod["M"][nm]
        else:
            m_exp_dir = m_atom - Z * cod["m_e"]
            sig_exp_dir = mp.sqrt(sm_atom**2 + (Z * cod["m_e_err"])**2)

        # ---- model discrepancy (the elephant) -----------------------------
        delta = m_sym - m_exp_dir

        rows.append(dict(nm=nm, A=A, Z=Z, N=N, L=L, B_sym=B_sym, m_sym=m_sym,
                         m_unb=m_unb, d_mp=d_mp, d_mn=d_mn, d_me=d_me, d_q0=d_q0,
                         d_cmp=d_cmp, sig_pred=sig_pred, m_exp_rec=m_exp_rec,
                         sig_exp_rec=sig_exp_rec, m_exp_dir=m_exp_dir,
                         sig_exp_dir=sig_exp_dir, m_u_relerr=m_u_relerr,
                         delta=delta, b_ame=b_ame, sb_ame=sb_ame))

    # ── Table 1: headline budget (MeV + ppQ) ──────────────────────────────
    print("### 1. m_sym mass: prediction vs experiment, with error bars")
    print("| iso | m_sym (MeV) | σ_pred (MeV) | σ_pred (ppQ) | M_exp (MeV) | "
          "σ_exp (MeV) | σ_exp (ppQ) | Δ_model (MeV) | Δ_model (ppQ) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        spp = r["sig_pred"] / r["m_sym"] * PPQ
        epp = r["sig_exp_dir"] / r["m_exp_dir"] * PPQ
        dpp = abs(r["delta"]) / r["m_exp_dir"] * PPQ
        print(f"| {r['nm']} | {float(r['m_sym']):.6f} | {float(r['sig_pred']):.2e} "
              f"| {_fmt_ppq(spp)} | {float(r['m_exp_dir']):.6f} | "
              f"{float(r['sig_exp_dir']):.2e} | {_fmt_ppq(epp)} | "
              f"{float(r['delta']):+.4f} | {_fmt_ppq(dpp)} |")

    # ── Table 2: prediction error decomposition (MeV) ─────────────────────
    print("\n### 2. PREDICTION error decomposition  σ_pred (MeV, added in quadrature)")
    print("| iso | δ m_p | δ m_n | δ m_e (α) | δ q₀ (subst.) | δ compute | σ_pred | dominant |")
    print("|---|--:|--:|--:|--:|--:|--:|:--|")
    for r in rows:
        parts = {"m_p": r["d_mp"], "m_n": r["d_mn"], "m_e": r["d_me"],
                 "q₀": r["d_q0"], "compute": r["d_cmp"]}
        dom = max(parts, key=lambda k: parts[k])
        print(f"| {r['nm']} | {float(r['d_mp']):.2e} | {float(r['d_mn']):.2e} "
              f"| {float(r['d_me']):.2e} | {float(r['d_q0']):.2e} "
              f"| {float(r['d_cmp']):.1e} | {float(r['sig_pred']):.2e} | {dom} |")

    # ── Table 3: experiment error decomposition ───────────────────────────
    print("\n### 3. EXPERIMENT error: reconstruction vs direct, and the unit-conversion ceiling")
    print("| iso | M_exp recon (MeV) | σ recon (MeV) | M_exp direct (MeV) | "
          "σ direct (MeV) | σ direct (ppQ) | intrinsic mass-in-u (ppQ) | σ B_AME (MeV) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        epp = r["sig_exp_dir"] / r["m_exp_dir"] * PPQ
        upp = r["m_u_relerr"] * PPQ
        print(f"| {r['nm']} | {float(r['m_exp_rec']):.6f} | {float(r['sig_exp_rec']):.2e} "
              f"| {float(r['m_exp_dir']):.6f} | {float(r['sig_exp_dir']):.2e} "
              f"| {_fmt_ppq(epp)} | {_fmt_ppq(upp)} | {float(r['sb_ame']):.1e} |")

    # ── The three walls, summarised for the lightest isotope ──────────────
    r = rows[0]
    print(f"\n### 4. Where 1 ppQ stands for {r['nm']}  (1 ppQ = {float(r['m_sym']/PPQ):.2e} MeV absolute)")
    walls = [
        ("model error  (m_sym − M_exp)", abs(r["delta"]) / r["m_exp_dir"]),
        ("CODATA input (σ_pred)", r["sig_pred"] / r["m_sym"]),
        ("experiment in MeV (σ_exp direct)", r["sig_exp_dir"] / r["m_exp_dir"]),
        ("experiment in u (intrinsic)", r["m_u_relerr"]),
        ("compute floor (dps 50 vs 80)", r["d_cmp"] / r["m_sym"]),
    ]
    print("| wall | relative size | = ppQ | × above 1 ppQ |")
    print("|:--|--:|--:|--:|")
    for label, rel in walls:
        print(f"| {label} | {float(rel):.2e} | {_fmt_ppq(rel*PPQ)} | {float(rel*PPQ):.2e} |")
    print("\n  Reading: 1 ppQ on m_sym is met ONLY in the compute sense (dps floor, "
          "bottom row). Accuracy is capped first by model error, then CODATA inputs, "
          "then the experiment itself — each many orders above 1 ppQ.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:] or None))
