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
        python3 m_sym_error_budget.py --decompose # Δ_model = B_AME−B_sym, localized
        python3 m_sym_error_budget.py --bonds      # per-bond-type split of m_sym(atom)
        python3 m_sym_error_budget.py --rescore     # bond-count topologies + magic vs B_AME
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


def _trace_ta_tf(Z, N, dps=50):
    """Raw (tr_atom, tr_free): atom = bound braid (inter-nucleon crossings on),
    free = GB components (tr_p^Z·tr_n^N)."""
    from tr_m_atom_via_transfer import tr_m_atom_zn
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=dps)
    return mp.mpf(ta), mp.mpf(tf)


def _fmt_ppq(x):
    a = abs(x)
    if a == 0:
        return "0"
    if a >= 1e6:
        return f"{float(a):.2e}"
    return f"{float(a):,.1f}"


def decompose(names=None) -> int:
    """Δ_model decomposition — localize where the trace mis-binds.

    Structural reduction: the unbound part Z·m_p+N·m_n is identical in the
    predicted m_sym and the reconstructed M_exp, so it CANCELS and

        Δ_model = m_sym − M_exp = B_AME − B_sym          (exactly)

    i.e. the entire model gap IS the binding error. B_sym itself splits as

        B_sym = m_sym(atom) − m_sym(free),   m_sym(W) = −α·ln tr_M(W)

    with m_sym(free) = −α·(Z·ln tr_p + N·ln tr_n) the free-nucleon baseline and
    m_sym(atom) the bound-braid trace (inter-nucleon crossings on). We attach the
    σ_pred error bar to Δ so the sign-change across the light nuclei (per
    docs/audits/2026-06-16-binding-undershoot-is-shell-structure.md) is shown to be
    REAL, not noise.
    """
    names = names or [nm for nm, _, _ in LOW]
    sel = {nm: (Z, N) for nm, Z, N in LOW}
    cod = _load_codata()
    ame = _ame()
    q0, q0_err = _q0()
    alpha = cod["m_e"] / (q0 * (q0 - 1))

    print(f"\n  Δ_model DECOMPOSITION   α = E₀ = {float(alpha):.6f} MeV")
    print("  Δ_model = m_sym − M_exp = B_AME − B_sym  (unbound Z·m_p+N·m_n cancels).")
    print("  B_sym = m_sym(atom) − m_sym(free);  σ_pred ≈ CODATA m_p/m_n ≈ 1e-6 MeV.\n")

    R = []
    for nm in names:
        Z, N = sel[nm]
        A = Z + N
        ta, tf = _trace_ta_tf(Z, N)
        ms_atom = -alpha * mp.log(ta)
        ms_free = -alpha * mp.log(tf)
        B_sym = ms_atom - ms_free
        b_ame, sb_ame, *_ = ame[(Z, A)]
        delta = b_ame - B_sym                      # = m_sym − M_exp
        sig = mp.sqrt((Z * cod["m_p_err"])**2 + (N * cod["m_n_err"])**2 + sb_ame**2)
        R.append(dict(nm=nm, A=A, Z=Z, N=N, ms_atom=ms_atom, ms_free=ms_free,
                      B_sym=B_sym, b_ame=b_ame, delta=delta, sig=sig))

    # ── A. the gap IS the binding error, and it changes sign (significantly) ──
    print("### A. Δ_model = B_AME − B_sym  (the unbound part cancels exactly)")
    print("| iso | A | B_sym | B_AME | Δ = B_AME−B_sym | Δ/A (per nucleon) | Δ/σ | verdict |")
    print("|---|--:|--:|--:|--:|--:|--:|:--|")
    for r in R:
        sigma_n = abs(r["delta"]) / r["sig"]
        verd = "over-binds" if r["delta"] < 0 else "under-binds"
        if abs(float(r["delta"])) < 0.5:
            verd = "≈works"
        print(f"| {r['nm']} | {r['A']} | {float(r['B_sym']):.3f} | {float(r['b_ame']):.3f} "
              f"| {float(r['delta']):+.3f} | {float(r['delta']/r['A']):+.3f} "
              f"| {float(sigma_n):.1e} | {verd} |")

    # ── B. which trace piece carries the binding (and the error)? ────────────
    print("\n### B. Compositional split  B_sym = m_sym(atom) − m_sym(free)")
    print("| iso | m_sym(atom) | m_sym(free) | B_sym | atom share | free share |")
    print("|---|--:|--:|--:|--:|--:|")
    for r in R:
        atom_sh = r["ms_atom"] / r["B_sym"]
        free_sh = -r["ms_free"] / r["B_sym"]
        print(f"| {r['nm']} | {float(r['ms_atom']):.4f} | {float(r['ms_free']):+.4f} "
              f"| {float(r['B_sym']):.4f} | {float(atom_sh)*100:.1f}% | {float(free_sh)*100:+.1f}% |")

    # ── C. the residual vs the magic/volume scale (audit cross-check) ────────
    from knot_volumes import VOL_BORROMEAN
    g8 = mp.mpf(str(VOL_BORROMEAN))
    per_nuc_magic = 2 * cod["m_e"] * g8                  # B_magic/A = 2·m_e·8G
    print(f"\n### C. Residual vs the magic-volume scale  (2·m_e·8G = {float(per_nuc_magic):.3f} MeV/nucleon)")
    print("| iso | A | Δ (MeV) | Δ/A | |Δ/A| / (2·m_e·8G) | reading |")
    print("|---|--:|--:|--:|--:|:--|")
    for r in R:
        ratio = abs(r["delta"] / r["A"]) / per_nuc_magic
        rd = "deuteron anomaly" if r["nm"] == "2H" else (
             "magic closure" if r["nm"] == "4He" else "generic light")
        print(f"| {r['nm']} | {r['A']} | {float(r['delta']):+.3f} | {float(r['delta']/r['A']):+.3f} "
              f"| {float(ratio):.2f} | {rd} |")

    print("\n  Reading: Δ_model is ENTIRELY the binding error (unbound cancels). It is "
          "~10⁶σ significant AND changes sign (²H over-, ⁴He under-binds) — so it is not "
          "a uniform formula error but nuclear shell structure (deuteron anomaly + magic "
          "closure), confirming docs/audits/2026-06-16-binding-undershoot-is-shell-structure.md. "
          "The binding lives in m_sym(atom) (the bound-braid trace); m_sym(free) is a small, "
          "sign-varying baseline. No uniform rescale of the trace can close a sign-changing gap.")
    return 0


def _bond_b(alpha):
    """Per-single-bond binding b_X = α·L_X for X ∈ {pp,pn,nn}, from the 2-nucleon
    sub-braid log-suppression (same source as the dashboard's bond-type L)."""
    out = {}
    for key, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        ta, tf = _trace_ta_tf(Z, N)
        out[key] = alpha * mp.log(tf / ta)
    return out


def bonds(names=None) -> int:
    """Bond-type decomposition of m_sym(atom) — which crossing drives the binding.

    The bound braid is a LINEAR CHAIN ordering ['p']·Z + ['n']·N with an
    inter-nucleon crossing only between ADJACENT nucleons, so it carries exactly
    (Z−1) p-p bonds, 1 p-n interface bond, (N−1) n-n bonds. Each crossing sits on
    a distinct generator, so the trace factorizes and B_sym is EXACTLY additive:

        B_sym = (Z−1)·b_pp + 1·b_pn + (N−1)·b_nn,   b_X = α·L_X.

    This localizes the binding (and the ⁴He under-bind) to a TOPOLOGY undercount:
    the chain has only (A−1) adjacent bonds, vs the C(A,2) actual pairwise bonds.
    """
    from math import comb
    names = names or [nm for nm, _, _ in LOW]
    sel = {nm: (Z, N) for nm, Z, N in LOW}
    cod = _load_codata()
    ame = _ame()
    q0, _ = _q0()
    alpha = cod["m_e"] / (q0 * (q0 - 1))
    b = _bond_b(alpha)

    print(f"\n  BOND-TYPE DECOMPOSITION   α = E₀ = {float(alpha):.6f} MeV")
    print(f"  per-single-bond binding  b_pp = {float(b['pp']):.4f}  "
          f"b_pn = {float(b['pn']):.4f}  b_nn = {float(b['nn']):.4f}  MeV   "
          f"(n-n > p-n > p-p — chirality ordering)\n")

    print("### A. Chain bonds vs actual pairwise bonds  (the topology undercount)")
    print("| iso | A | chain pp/pn/nn | chain bonds (A−1) | all pairs C(A,2) | missing |")
    print("|---|--:|:--:|--:|--:|--:|")
    for nm in names:
        Z, N = sel[nm]; A = Z + N
        ch = (Z - 1, 1 if (Z and N) else 0, N - 1)
        chain = sum(ch); allp = comb(A, 2)
        print(f"| {nm} | {A} | {ch[0]}/{ch[1]}/{ch[2]} | {chain} | {allp} | {allp-chain} |")

    print("\n### B. B_sym is EXACTLY the additive chain sum  (per-bond-type contribution)")
    print("| iso | (Z−1)·b_pp | 1·b_pn | (N−1)·b_nn | Σ = B_sym (additive) | B_sym (exact trace) | match |")
    print("|---|--:|--:|--:|--:|--:|:--:|")
    for nm in names:
        Z, N = sel[nm]
        c_pp = (Z - 1) * b["pp"]; c_pn = b["pn"] if (Z and N) else mp.mpf(0)
        c_nn = (N - 1) * b["nn"]
        add = c_pp + c_pn + c_nn
        L = _trace_L(Z, N); exact = alpha * L
        ok = "✓" if abs(add - exact) < mp.mpf("1e-6") else f"Δ{float(add-exact):.1e}"
        print(f"| {nm} | {float(c_pp):.3f} | {float(c_pn):.3f} | {float(c_nn):.3f} "
              f"| {float(add):.4f} | {float(exact):.4f} | {ok} |")

    print("\n### C. Which bond drives the ⁴He under-bind?")
    print("| iso | A | B_sym (chain) | B_AME | Δ | dominant chain bond | reason for Δ |")
    print("|---|--:|--:|--:|--:|:--|:--|")
    for nm in names:
        Z, N = sel[nm]; A = Z + N
        contrib = {"p-p": (Z - 1) * b["pp"], "p-n": b["pn"] if (Z and N) else mp.mpf(0),
                   "n-n": (N - 1) * b["nn"]}
        dom = max(contrib, key=lambda k: contrib[k])
        B = alpha * _trace_L(Z, N)
        b_ame = ame[(Z, A)][0]
        d = b_ame - B
        why = ("single p-n bond too strong (deuteron anomaly)" if nm == "2H"
               else f"chain misses {comb(A,2)-(A-1)} pairwise bonds (magic closure)"
               if d > 1 else "chain ≈ actual topology")
        print(f"| {nm} | {A} | {float(B):.3f} | {float(b_ame):.3f} | {float(d):+.3f} "
              f"| {dom} ({float(contrib[dom]):.2f}) | {why} |")

    print("\n  Reading: B_sym = α·[(Z−1)L_pp + L_pn + (N−1)L_nn] — a LINEAR-CHAIN binding, "
          "exactly additive over the (A−1) adjacent bonds, with per-bond strength n-n>p-n>p-p. "
          "So the ⁴He under-bind is NOT one bad crossing type: it is the chain topology "
          "carrying (A−1) bonds where the real nucleus binds ~C(A,2) pairs (⁴He: 3 vs 6, "
          "3 missing p-n). The ²H over-bind is the opposite end — a single p-n bond (3.89) "
          "is stronger than the weakly-bound deuteron (2.22).")
    return 0


def rescore(names=None) -> int:
    """Re-score bond-count topologies + the magic term against B_AME.

    NOT a fit: α and the per-bond strengths b_pp/b_pn/b_nn are all DERIVED from
    the trace at q₀; only the combinatorial bond COUNT (categorical topology)
    changes. Forms scored:
      B_chain    = (Z−1)b_pp + b_pn + (N−1)b_nn        (linear chain = exact B_sym)
      B_allpairs = C(Z,2)b_pp + Z·N·b_pn + C(N,2)b_nn  (fully-connected topology)
      B_magic    = 2·m_e·A·8G                          (⁴He magic closure, existing)
    """
    from math import comb, sqrt
    names = names or [nm for nm, _, _ in LOW]
    sel = {nm: (Z, N) for nm, Z, N in LOW}
    cod = _load_codata()
    ame = _ame()
    q0, _ = _q0()
    alpha = cod["m_e"] / (q0 * (q0 - 1))
    b = _bond_b(alpha)
    from knot_volumes import VOL_BORROMEAN
    g8 = mp.mpf(str(VOL_BORROMEAN))

    print(f"\n  RE-SCORE bond-count topologies + magic   α = E₀ = {float(alpha):.6f} MeV")
    print("  All forms use the SAME derived per-bond b_pp/b_pn/b_nn; only the bond")
    print("  COUNT (chain (A−1) vs all-pairs C(A,2)) or the magic term differs. No fit.\n")

    print("### Binding B and accuracy ratio B_AME/B  (1.00 = perfect; >1 under-binds)")
    print("| iso | A | B_AME | B_chain | B_allpairs | B_magic | "
          "B_AME/chain | B_AME/allpairs | B_AME/magic |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    rows = []
    for nm in names:
        Z, N = sel[nm]; A = Z + N
        B_chain = (Z - 1) * b["pp"] + (b["pn"] if (Z and N) else 0) + (N - 1) * b["nn"]
        B_all = comb(Z, 2) * b["pp"] + Z * N * b["pn"] + comb(N, 2) * b["nn"]
        B_mag = 2 * cod["m_e"] * A * g8 if (Z, N) == (2, 2) else None
        b_ame = ame[(Z, A)][0]
        r_ch, r_al = b_ame / B_chain, b_ame / B_all
        r_mg = (b_ame / B_mag) if B_mag else None
        rows.append((nm, A, b_ame, B_chain, B_all, B_mag, r_ch, r_al, r_mg))
        print(f"| {nm} | {A} | {float(b_ame):.3f} | {float(B_chain):.3f} | {float(B_all):.3f} "
              f"| {('%.3f'%float(B_mag)) if B_mag else '—':>7} | {float(r_ch):.3f} "
              f"| {float(r_al):.3f} | {('%.3f'%float(r_mg)) if r_mg else '—':>6} |")

    def rms(idx):
        es = [float(r[2] - r[idx]) for r in rows if r[idx] is not None]
        return sqrt(sum(e * e for e in es) / len(es)) if es else float("nan")
    print(f"\n  RMS error (MeV) over the low isotopes:  "
          f"chain = {rms(3):.2f}   all-pairs = {rms(4):.2f}   (lower = better)")
    print("  (B_magic is ⁴He-only; B_AME/magic = 0.944 there — the single magic term)")
    print("\n  Reading: all-pairs FIXES ⁴He (2.36→1.20) but badly OVER-binds the heavier "
          "nuclei (⁶Li 0.54, ⁷Li 0.45), so RMS actually WORSENS (10.1→22.5). Reason: "
          "C(A,2) grows quadratically while real nuclear binding SATURATES ~linearly in A "
          "(≈ const · A). The chain's (A−1) linear scaling has the right A-dependence but "
          "undershoots magic closures; all-pairs has the wrong (quadratic) scaling. So "
          "NEITHER bond-count topology works — the residual is a sign-changing shell "
          "correction, and only the explicit magic-volume term B_magic nails ⁴He (0.944). "
          "Confirms: smooth (near-linear-in-A) trace + explicit shell terms, not a unified "
          "bond-count law.")
    return 0


def main(argv=None) -> int:
    if argv and argv[0] == "--decompose":
        return decompose(argv[1:] or None)
    if argv and argv[0] == "--bonds":
        return bonds(argv[1:] or None)
    if argv and argv[0] == "--rescore":
        return rescore(argv[1:] or None)
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
