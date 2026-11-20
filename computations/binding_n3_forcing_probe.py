#!/usr/bin/env python3
"""
binding_n3_forcing_probe.py — is the n=3 body-order term of
`conj:binding-manybody-eq-jet-filtration` FORCED by its two stated anchors?

The conjecture's "Anchors" paragraph says the body-order series
`B(K) = Σ_{n≥2} m_e·a_D^(n)` is "pinned at two body orders already derived
without fitting": the n=2 deuteron bond and the n=4 magic-shell term
`prop:magic-A-binding-formula` (`B(⁴He) = ρ_F·m_e·A·Vol(L6a4)`, ρ_F=2, +5.87%).
It then asserts that the n=3 term is the genuine three-body contribution.

QUESTION (bean qou-hh9q): does that pinning FORCE the n=3 term, so that A=3 is
a genuine test — or does n=3 retain freedom the two anchors do not fix?

This probe does NOT fit anything to A=3 data. It (i) counts unknowns against
anchor equations, (ii) exhibits the residual solution family explicitly, and
(iii) measures how much a monotone-filtration side constraint narrows it.
Where a number is obtained by inverting data it is printed as EXTRACTION.

EXPLORATORY — no production wiring, no fitted constant, no witness consumed
downstream. mpmath end-to-end (no float64 anywhere), proton q₀ pin.
Audit: docs/audits/2026-08-26-n3-body-order-forcing.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
sys.path.insert(0, str(HERE / "substrate"))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — PROTON pin (owner 2026-08-07)
from experimental_constants import M_E_MEV  # noqa: E402 — CAL-1 registry
from _li_2_q_util import flavor_split_leading  # noqa: E402
from coulomb_energy import (  # noqa: E402
    R0_FM, HBAR_C_MEV_FM, alpha_em_hbar_c_mev_fm,
)

Q0 = Q_MP
ALPHA_HC = mp.mpf(str(alpha_em_hbar_c_mev_fm()))
# Equivalent uniform-sphere radius from the measured ³He rms charge radius
# 1.9661 fm: R = sqrt(5/3)·r_rms, back-solved to an r₀ (coulomb_energy.py header).
MEAS_R0_3HE = mp.sqrt(mp.mpf(5) / 3) * mp.mpf("1.9661") / mp.mpf(3) ** (mp.mpf(1) / 3)
M_E = mp.mpf(str(M_E_MEV))

# AME2020 binding energies (MeV) — the comparison boundary, not model input.
B_AME = {"2H": mp.mpf("2.224566"), "3H": mp.mpf("8.481821"),
         "3He": mp.mpf("7.718058"), "4He": mp.mpf("28.295661")}
Z_OF = {"2H": 1, "3H": 1, "3He": 2, "4He": 2}
A_OF = {"2H": 2, "3H": 3, "3He": 3, "4He": 4}


# ---------------------------------------------------------------- na-Stokes a_D
def qint(k: int) -> "mp.mpf":
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - Q0 ** (-1))


def qfac(n: int) -> "mp.mpf":
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def partitions(n: int, m: int | None = None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def dimq(lam) -> "mp.mpf":
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def a_D(n: int) -> "mp.mpf":
    """na-Stokes SW jet period a_D^(n) = S(n)/n, S(n) = Σ_{λ⊢n} dim_q λ."""
    return mp.fsum([dimq(l) for l in partitions(n)]) / n


# --------------------------------------------------- derived n=2 deuteron bond
def alpha_E0() -> "mp.mpf":
    """α = E₀ = m_e/(q₀(q₀−1)) — the per-bond energy scale."""
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    return _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)


def L_pn() -> "mp.mpf":
    """Convention-D colour-weighted p–n bond, writhe-normalised.
    Mirrors mass_binding_dashboard._bond_type_L['pn'] in exact mpmath
    (the dashboard casts to float at return; this does not)."""
    h = Q0 - 1 / Q0
    z = Q0 ** 3 / (Q0 ** 2 + 1)
    delta = mp.mpf(str(flavor_split_leading(Q0)))
    t = mp.mpf(1) / 2 - delta / 4
    d_pn = -h * t
    de_pn = 2 * t - 1
    return -mp.log(z + d_pn) - de_pn / 2 * mp.log(1 - h)


def pct(x, ref) -> "mp.mpf":
    return (x - ref) / ref * 100


def line(c="-", n=78):
    print(c * n)


def main() -> int:
    mp.mp.dps = max(mp.mp.dps, 60)
    print("=" * 78)
    print("Is the n=3 body-order term FORCED by the n=2 and n=4 anchors?")
    print("bean qou-hh9q · proton q₀ pin · mpmath end-to-end")
    print("=" * 78)
    print(f"q₀   = {mp.nstr(Q0, 20)}   (proton pin, q_parameter.Q_50_DIGIT_STR)")
    print(f"m_e  = {mp.nstr(M_E, 12)} MeV   (CAL-1)")

    aD = {n: a_D(n) for n in (2, 3, 4)}
    print("\na_D^(n) = S(n)/n, the DERIVED extensive kernel (no freedom):")
    for n in (2, 3, 4):
        print(f"   a_D^({n}) = {mp.nstr(aD[n], 12)}")

    # ---------------------------------------------------------------- READING U
    line("=")
    print("READING U — the conjecture's DISPLAYED equation: B(K)=Σ_n m_e·a_D^(n)")
    print("            (no weight; this is what the .md formula and the Lean")
    print("             class BindingManyBodyJetFiltration.term_eq state)")
    line()
    print("Free parameters: 0.  n=3 is FORCED — and the reading is testable now.")
    print(f"{'iso':>5} {'A':>2} {'B_pred':>12} {'B_AME':>12} {'err':>10}")
    for iso in ("2H", "3H", "4He"):
        A = A_OF[iso]
        pred = M_E * mp.fsum([aD[n] for n in range(2, A + 1)])
        print(f"{iso:>5} {A:>2} {mp.nstr(pred, 8):>12} {mp.nstr(B_AME[iso], 8):>12}"
              f" {mp.nstr(pct(pred, B_AME[iso]), 4):>9}%")
    print("\n⇒ REFUTED at the deuteron itself, scope (a): the unweighted series")
    print("  under-binds ²H by 4.35× and ⁴He by 12.4×. The corpus therefore does")
    print("  NOT work with reading U — it works with reading W below, in which a")
    print("  weight w_n is inserted that the displayed equation does not contain.")

    # ------------------------------------- the K-dependence is never realised
    line("=")
    print("A THIRD READING, AND WHY IT IS NOT LIVE")
    line()
    print("The displayed equation writes the period as a_D^(n)(K) — K-DEPENDENT,")
    print("a residue sum over the hyperbolic components of THAT braid. Under that")
    print("literal reading there are no weights and n=3 WOULD be forced, with no")
    print("free parameter at all: the A=3 braid's own residue sum would supply it.")
    print("\nBut no such object exists in the corpus. Every a_D in computations/")
    print("takes the body order alone — measured, 10 producers, signature a_D(n):")
    print("   theta_wn_kernel_derive_or_refute, theta_wn_jetfilt_linkvolume,")
    print("   binding_fewbody_bondcount, binding_wn_kernel_derive_refute,")
    print("   binding_wn_derive_or_refute, bk_crossing_coordination,")
    print("   binding_manybody_jet_filtration, binding_wn_multianchor_tower_refute,")
    print("   binding_wn_frobenius_dual_probe  (+ this probe, same signature)")
    print("and each returns S(n)/n, a function of n and q with no knot argument.")
    print("So the K-dependence in the displayed equation is not realised anywhere,")
    print("and w_n(K) was introduced in the scope note precisely to restore it.")
    print("⇒ 'forced but not yet computed' is NOT a live third option; there is no")
    print("  per-knot n=3 residue sum to evaluate.")

    # ---------------------------------------------------------------- READING W
    line("=")
    print("READING W — the SCOPE NOTE's form: B(K)=Σ_{n=2}^{A} m_e·a_D^(n)·w_n,")
    print("            w_n shared across K (K-independent body-order weights).")
    line()
    print("Unknowns through A=4:  w_2, w_3, w_4          → 3")
    print("Anchor equations stated by the conjecture:")
    print("   (n=2) the derived deuteron bond            → 1")
    print("   (n=4) the magic-shell ⁴He closed form      → 1")
    print("                                             ────")
    print("   3 unknowns − 2 equations  =  1 FREE PARAMETER")
    print("\n⇒ NOT FORCED.  Exactly one free parameter survives the two anchors,")
    print("  and w_3 is (a coordinate on) it.")

    # anchor values
    alpha = alpha_E0()
    Lpn = L_pn()
    B2_derived = alpha * Lpn
    print("\n--- anchor n=2, the DERIVED single p–n bond (not AME) ---")
    print(f"   α = E₀ = m_e/(q₀(q₀−1)) = {mp.nstr(alpha, 12)} MeV")
    print(f"   L_pn (convention D, colour-weighted, writhe-norm) = {mp.nstr(Lpn, 12)}")
    print(f"   B₂^derived = α·L_pn = {mp.nstr(B2_derived, 10)} MeV")
    print(f"   vs B_AME(²H) = {mp.nstr(B_AME['2H'], 10)} MeV  "
          f"→ {mp.nstr(pct(B2_derived, B_AME['2H']), 4)}%  (overshoot)")

    G = mp.catalan
    vol_L6a4 = 8 * G
    rho_F = mp.mpf(2)
    B4_magic = rho_F * M_E * 4 * vol_L6a4
    print("\n--- anchor n=4, the magic-shell closed form ---")
    print(f"   Vol(L6a4) = 8G = {mp.nstr(vol_L6a4, 12)}")
    print(f"   B(⁴He) = ρ_F·m_e·A·8G, ρ_F=2 → {mp.nstr(B4_magic, 10)} MeV")
    print(f"   vs B_AME(⁴He) = {mp.nstr(B_AME['4He'], 10)} MeV  "
          f"→ {mp.nstr(pct(B4_magic, B_AME['4He']), 4)}%")
    print("   ⚠ ρ_F = 2 is NOT derived. magic-A-binding-formula-context.md:")
    print('     "The categorical derivation of the integer 2 — vs. [2]_q,')
    print('      2cos(π/3), or another natural candidate — is not closed in this')
    print('      proposition; the value is consumed as an input hypothesis."')

    # w_2 from each candidate n=2 anchor
    w2_derived = B2_derived / (M_E * aD[2])
    w2_ame = B_AME["2H"] / (M_E * aD[2])
    print("\n--- what the n=2 anchor pins ---")
    print(f"   w_2 from the DERIVED bond  = {mp.nstr(w2_derived, 10)}")
    print(f"   w_2 from AME B(²H)         = {mp.nstr(w2_ame, 10)}   ← EXTRACTION")
    print(f"   the two differ by {mp.nstr(pct(w2_derived, w2_ame), 4)}%.")
    print("   The corpus's w_2 = 4.353 (2026-07-11 audits) is the AME one, i.e.")
    print("   an EXTRACTION — not the derived anchor the conjecture cites.")
    return_state = (aD, alpha, B2_derived, B4_magic, w2_derived, w2_ame)

    # ------------------------------------------------- the residual 1-parameter family
    line("=")
    print("THE RESIDUAL FAMILY — both anchors held EXACTLY, w_3 free")
    line()
    print("With w_2 fixed by the n=2 anchor, the n=4 anchor is ONE equation in")
    print("TWO unknowns:   m_e(a₂w₂ + a₃w₃ + a₄w₄) = B_magic(⁴He)")
    print("so for every w₃ there is exactly one w₄ =")
    print("      (B_magic/m_e − a₂w₂ − a₃w₃)/a₄ ,")
    print("and the ⁴He and ²H anchors are satisfied identically along the family.")
    print("The A=3 PREDICTION along that family is")
    print("      B(³H)_pred(w₃) = m_e(a₂w₂ + a₃w₃),")
    print("an unbounded straight line in w₃ ⇒ every real B(³H) is reachable.")

    for tag, w2 in (("derived-anchor w₂", w2_derived), ("AME-anchor w₂", w2_ame)):
        print(f"\n  family with {tag} = {mp.nstr(w2, 8)}:")
        print(f"   {'w_3':>10} {'→ w_4':>12} {'B(³H)_pred':>14}")
        for w3 in (mp.mpf(0), w2, 2 * w2, 4 * w2, 8 * w2):
            w4 = (B4_magic / M_E - aD[2] * w2 - aD[3] * w3) / aD[4]
            b3 = M_E * (aD[2] * w2 + aD[3] * w3)
            print(f"   {mp.nstr(w3, 6):>10} {mp.nstr(w4, 6):>12} {mp.nstr(b3, 6):>13} MeV")
    print("\n  Every row above satisfies BOTH stated anchors exactly.")
    print("  ⇒ the anchors constrain only the COMBINATION a₃w₃ + a₄w₄, never w₃.")

    # ---------------------------------------- robustness: the OTHER n=4 reading
    line("=")
    print("ROBUSTNESS — the count is 1 either way the n=4 anchor is read")
    line()
    print("Reading (i)  B_magic is the ⁴He TOTAL  (what the .md compares to AME):")
    print("   1 equation on a₂w₂+a₃w₃+a₄w₄ ⇒ w₃ free.            → 1 parameter")
    print("Reading (ii) B_magic is the n=4 TERM alone, m_e·a₄·w₄ = B_magic:")
    w4_termreading = B4_magic / (M_E * aD[4])
    print(f"   w₄ = B_magic/(m_e·a₄) = {mp.nstr(w4_termreading, 8)} pinned,")
    print("   but then NOTHING mentions w₃ at all ⇒ w₃ free.     → 1 parameter")
    print("\n  The free-parameter count is invariant under the reading. Good:")
    print("  the answer does not hinge on resolving that ambiguity.")

    # ------------------------------------------- does ANY side constraint bite?
    line("=")
    print("CAN A STRUCTURAL SIDE CONSTRAINT FORCE w₃?  (measured, not asserted)")
    line()
    print("The conjecture's only structural statement about the weights is that")
    print('they GROW with body order (the "ρ·A scale rule", an output of the')
    print("q-difference recursion). Take the strongest honest reading of that:")
    print("   (P) positivity      w₃ > 0, w₄ > 0")
    print("   (M) monotone growth w₂ ≤ w₃ ≤ w₄")
    print("and ask what interval of w₃ survives, both anchors still exact.")

    for tag, w2 in (("derived-anchor w₂", w2_derived), ("AME-anchor w₂", w2_ame)):
        S = B4_magic / M_E - aD[2] * w2          # = a₃w₃ + a₄w₄
        w3_lo_P, w3_hi_P = mp.mpf(0), S / aD[3]  # w₄>0
        w3_lo_M, w3_hi_M = w2, S / (aD[3] + aD[4])
        b3 = lambda w3: M_E * (aD[2] * w2 + aD[3] * w3)
        print(f"\n  {tag} = {mp.nstr(w2, 8)}   (S = a₃w₃+a₄w₄ = {mp.nstr(S, 8)})")
        print(f"    (P) alone : w₃ ∈ ({mp.nstr(w3_lo_P,6)}, {mp.nstr(w3_hi_P,6)})"
              f"  → B(³H) ∈ ({mp.nstr(b3(w3_lo_P),6)}, {mp.nstr(b3(w3_hi_P),6)}) MeV")
        if w3_lo_M <= w3_hi_M:
            print(f"    (P)+(M)   : w₃ ∈ [{mp.nstr(w3_lo_M,6)}, {mp.nstr(w3_hi_M,6)}]"
                  f"  → B(³H) ∈ [{mp.nstr(b3(w3_lo_M),6)}, {mp.nstr(b3(w3_hi_M),6)}] MeV")
            width = b3(w3_hi_M) - b3(w3_lo_M)
            print(f"      surviving B(³H) window width = {mp.nstr(width, 6)} MeV"
                  f"  = {mp.nstr(width / B_AME['3H'] * 100, 4)}% of B_AME(³H)")
        else:
            print("    (P)+(M)   : EMPTY — monotone growth is inconsistent with the")
            print("                two anchors, i.e. the anchors themselves force")
            print("                w₃ > w₄ (weights must DECREASE at n=4).")

    # ------------------------------------------------- Coulomb correction, shown
    line("=")
    print("THE A=3 COMPARISON DATUM — Coulomb correction computed, not inherited")
    line()
    print("E_C(Z,A) = (3/5)·Z(Z−1)·α_EM·ℏc/R,  R = r₀·A^(1/3)")
    print("computations/coulomb_energy.py — α_EM DERIVED from q₀ (not CODATA),")
    print(f"and the canonical r₀ is the DERIVED pion Compton length ƛ_π = ℏc/m_π")
    print(f"   R0_FM = {mp.nstr(R0_FM, 10)} fm   (the empirical 1.2 fm is retained")
    print("           in that module only as R0_FM_EMPIRICAL, for comparison).")
    print("Only ³He carries Coulomb (Z=2); ³H has Z=1 so E_C = 0 identically.")

    # Three geometries, so the reader sees the correction's own spread.
    def ec_at(r0, Z, A):
        if Z < 2:
            return mp.mpf(0)
        return (mp.mpf(3) / 5 * Z * (Z - 1) * ALPHA_HC
                / (mp.mpf(str(r0)) * mp.mpf(A) ** (mp.mpf(1) / 3)))

    geoms = [("ƛ_π  (canonical, derived)", R0_FM),
             ("1.2 fm (empirical, legacy)", mp.mpf("1.2")),
             ("measured ³He charge radius", MEAS_R0_3HE)]
    print(f"\n   {'geometry':>28} {'E_C(³He)':>11} {'B_str(³H)':>11}"
          f" {'B_str(³He)':>11} {'CSB split':>11}")
    b3_variants = []
    for tag, r0 in geoms:
        e = ec_at(r0, 2, 3)
        bh, bhe = B_AME["3H"], B_AME["3He"] + e
        b3_variants.append(((bh + bhe) / 2, tag))
        print(f"   {tag:>28} {mp.nstr(e, 6):>11} {mp.nstr(bh, 6):>11}"
              f" {mp.nstr(bhe, 6):>11} {mp.nstr(bh - bhe, 4):>11}")
    raw_split = B_AME["3H"] - B_AME["3He"]
    print(f"\n   raw (uncorrected) split = {mp.nstr(raw_split, 6)} MeV "
          f"= {mp.nstr(raw_split / B_AME['3H'] * 100, 4)}% of B(³H) — nearly all EM.")
    print("   ⚠ HONEST NOTE ON THE SIGN. At the canonical derived r₀ the")
    print("     correction OVERSHOOTS: ³He ends up the MORE bound partner, so the")
    print("     residual charge-symmetry breaking comes out ≈ −1%, not the +2.73%")
    print("     the 2026-07-11 audits quote (they used a larger R / smaller E_C).")
    print("     The measured-radius row restores ³H as the more bound partner.")
    print("     This ±1% spread does NOT touch the verdict below: it is two orders")
    print("     of magnitude smaller than the surviving w₃ window measured above.")
    ec = {"3H": mp.mpf(0), "3He": ec_at(R0_FM, 2, 3)}
    bstrong = {iso: B_AME[iso] + ec[iso] for iso in ("3H", "3He")}
    b3_strong = (bstrong["3H"] + bstrong["3He"]) / 2
    print(f"\n   mirror-average B_strong(A=3), canonical geometry = "
          f"{mp.nstr(b3_strong, 8)} MeV")
    print(f"   spread across the three geometries = "
          f"{mp.nstr(max(v for v, _ in b3_variants) - min(v for v, _ in b3_variants), 4)} MeV")

    # --------------------------------------------------------- THE EXTRACTION
    line("=")
    print("WHAT THE A=3 DATUM GIVES — an EXTRACTION, explicitly labelled")
    line()
    print("Because w₃ is free, solving for the w₃ that reproduces B_strong(A=3)")
    print("is INVERSION OF THE DATUM, not a prediction tested against it. The")
    print("banned move would be to report the resulting agreement as a success.")
    for tag, w2 in (("derived-anchor w₂", w2_derived), ("AME-anchor w₂", w2_ame)):
        w3_x = (b3_strong / M_E - aD[2] * w2) / aD[3]
        S = B4_magic / M_E - aD[2] * w2
        w4_x = (S - aD[3] * w3_x) / aD[4]
        mono = "YES" if (w2 <= w3_x <= w4_x) else "NO"
        print(f"\n  {tag}:")
        print(f"    w₃ = {mp.nstr(w3_x, 10)}   [EXTRACTION from B_strong(A=3)]")
        print(f"    w₄ = {mp.nstr(w4_x, 10)}   [then forced by the n=4 anchor]")
        print(f"    monotone w₂ ≤ w₃ ≤ w₄ ? {mono}   "
              f"(w₂={mp.nstr(w2,6)}, w₃={mp.nstr(w3_x,6)}, w₄={mp.nstr(w4_x,6)})")
    print("\n  Residual after the extraction is exactly 0 by construction —")
    print("  3 unknowns, 3 equations. No agreement is being demonstrated.")

    # ------------------------- is `multi-link emit` the n=3 term?  (coordinator)
    line("=")
    print("IS THE DASHBOARD'S `multi-link emit` THE n=3 TERM?  — NO, structurally")
    line()
    print("A live dashboard run shows E_multilink takes A=3 from err 1.38/1.44 to")
    print("1.06/1.07 — it behaves like a three-body term where one is wanted. It is")
    print("parameter-free (the bar-odd, q↦q⁻¹-antisymmetric part of the")
    print("inter-nucleon binding defect tr_free−tr_atom; mass_binding_dashboard.py")
    print(":601-614), so the near-miss is not a fit. But a body-order n=3 term is")
    print("IDENTICALLY ZERO on a two-body system, and this one is not:")
    try:
        from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
        print(f"\n   {'iso':>5} {'E_multilink (MeV)':>20}")
        for (Z, N, nm) in ((1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He")):
            ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
            tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=mp.mpf(1) / Q0, dps=50)
            eml = alpha * abs(((tf - ta) - (tfi - tai)) / 2)
            print(f"   {nm:>5} {mp.nstr(eml, 10):>20}"
                  + ("   ← must be 0 for an n=3 term" if nm == "2H" else ""))
        print("\n   E_multilink(²H) ≠ 0 ⇒ it is NOT the n=3 body-order term.")
    except Exception as exc:                                   # pragma: no cover
        print(f"   [tr_m_atom_zn unavailable: {exc}]")
    print("   It may still be a real object; it is not THIS one. Treat with the")
    print("   caution its neighbour B_vol earned (DEPRECATED 2026-08-08, postdiction")
    print("   near-match, not derived) until its provenance is separately traced.")
    print("   Recomputed here in exact mpmath — the dashboard casts these traces to")
    print("   float64 before a near-cancelling subtraction, which is a defect in")
    print("   that file (not this one); the four values survive it unchanged.")

    # --------------------------------------------- how conditional are the anchors
    line("=")
    print("CONDITIONALITY OF THE ANCHORS (beyond the free parameter)")
    line()
    print("n=2  B_sym is tagged DERIVED* — KVC-CONDITIONAL: ln|tr_M| is Vol only")
    print("     via `vol-through-tau`, conditional on the OPEN Volume Conjecture")
    print("     `conj:kashaev-volume-conjecture`. So the n=2 anchor is derived")
    print("     CONDITIONAL ON THE VOLUME CONJECTURE, not outright.")
    print("n=4  ρ_F = 2 is consumed as an input hypothesis (above).")
    print("E_C  also DERIVED*: α_EM is derived but conditional on an open Witten-κ")
    print("     Gram-determinant `sorry`; R = ƛ_π·A^(1/3) is a saturation")
    print("     assumption (the fitted exponent is 0.97/0.43/0.53/0.31 at A=2,3,3,4)")
    print("     and coefficient-exactly-1 is a selection among four mass scales.")
    print("\n⇒ 'pinned at two body orders already derived without fitting' overstates")
    print("  both anchors. Neither is unconditional, and one free parameter remains")
    print("  regardless.")

    line("=")
    print("VERDICT")
    line()
    print("NOT FORCED. The two stated anchors leave exactly ONE free parameter,")
    print("and w₃ is a coordinate on it, so A=3 CANNOT test the n=3 term — it")
    print("defines it. Scope (a): this is a statement about what the anchors")
    print("determine, not a refutation of the conjecture.")
    print("Rigidity would have to come from the DERIVED q-difference kernel")
    print("R(q,x); that kernel is open (2026-07-11 audits), so nothing currently")
    print("supplies it.")
    return return_state


if __name__ == "__main__":
    main()
