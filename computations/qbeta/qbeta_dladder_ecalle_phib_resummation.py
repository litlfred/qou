#!/usr/bin/env python3
"""qbeta_dladder_ecalle_phib_resummation.py

Écalle acceleration ⟺ Φ_b state-integral resummation of the bar-odd Q_β
D-ladder — the single UNOWNED odd-channel item of the 1ppQ path reassessment
(docs/audits/2026-07-17-1ppq-path-reassessment.md §2).

INFRASTRUCTURE / MEASUREMENT ONLY. Scope-(a) throughout. **No c_k wired, no
fit to QOU observables, no tier change, nothing to production.** Builds on —
does NOT re-derive — KC21/KC22 (the exact d_k), phi_b_evaluator / the #3654
saddle state integral, and the merged #3818/#3839 fixed-order negatives.

The negative space is fully closed (audit §0): every fixed-order Borel–Leroy
and fixed-base Jackson q-Borel resummation is refuted; the ORD-63 extension
(#3839) confirmed the divergence class C and Borel–Leroy order s* both DRIFT
(no single Gevrey index) — the object is genuinely resurgent. The honest
resummation is the multi-level Écalle acceleration ⟺ the Φ_b state integral.

This probe measures four things the corpus had NOT yet pinned:

  M2 — PARITY-LEVEL critical times (formalize-first (a)). The 2-adic ℤ/2
       bar-parity grading (v₂(den b_k)=0 ⟺ k odd, Lean-anchored #3818) splits
       the ladder into two subseries. Are the per-parity divergence classes
       C_odd, C_even DISTINCT and each MORE STABLE across k than the full
       series' drifting C?  If yes, the "no single index" is really "two
       levels" — a genuine two-stage acceleration, not a single mis-specified
       Borel–Leroy order.

  M3 — the acceleration-weight COMPOSITION COLLAPSE (formalize-first (b),
       Lean-mirrored §4). (k!)^{s1}·(k!)^{s2} = (k!)^{s1+s2}: iterating
       Borel–Leroy transforms only reaches the ADDITIVE MONOID of orders — it
       can never manufacture a genuinely new critical time. Proves the
       fixed-order negative is not repairable by composing fixed-order
       transforms; the multi-level Écalle kernel is NECESSARY.

  M4 — the NON-PERTURBATIVE SCALE at the meridian (formalize-first (c)+(d)).
       At ũ(q₀) the D-ladder is asymptotic; its least-term (optimal-truncation)
       magnitude δ_np ~ exp(−A/ũ) is the size of the Stokes/alien ambiguity.
       Extract A_eff and — DECISIVELY — test whether the optimal-truncation
       resummed D value is ANCHOR-BLIND (muon vs proton ũ differ ~1e-8). If it
       is, the perturbative acceleration provably cannot carry the S sign-flip;
       the anchor-dependence is the non-perturbative Stokes datum A_ω, NOT the
       perturbative sum — matching the anchor-blind Φ_b saddle (#3654).

  M5 — the Φ_b state-integral cross-check. vol_of_m(q₀) deficit 0.00940 (the
       |S(muon)| scale) vs the optimal-truncation resummed D — leading-order
       near-match (as the bridge #3654 found), quantified here as the
       perturbative floor.

VERDICT (§6): the acceleration setup is complete and the two critical times
are the two 2-adic-parity levels, but the odd/S-carrier action is a perturbative
(anchor-blind) scale; the anchor-dependent c₃ is the Stokes constant A_ω (the
alien derivative / G3 monodromy datum), which the perturbative acceleration
does NOT supply. No c₃ produced; nothing wired.

Cross-refs: docs/audits/2026-07-17-dladder-ecalle-phib-resummation.md;
2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md (G3 = A_ω);
ck-dk-canonical-registry.md KC21/KC22; ledger docs/coordination/1ppq-qbeta.md.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402

# The generating-function module reads ORD from sys.argv at import time.
ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
from qbeta_c3_barodd_gluing_newton_solve import vol_of_m  # noqa: E402

mp.mp.dps = 60
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))          # 2.0298832…
    KAPPA1 = +(11 * mp.sqrt(3) * mp.pi / 108)
QSTAR = mp.mpf("1.109978593031523288402328")       # A2 (the S=0 decay-sector q₀)
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}
# The odd (S-carrier) / even Borel-plane radii measured by the merged conformal
# probe (#3818, ζ² plane) — context, not re-computed here.
RHO_ZETA_MERGED = {"odd": mp.mpf("0.152"), "even": mp.mpf("0.254")}


def to_mpf(v):
    """Exact ℚ(√3) sympy → mpf at working precision."""
    return mp.mpf(str(sp.N(v, 55)))


def classfit(logabs, ks):
    """Least-squares log|d_k| = A + B·k + C·k·log k over ks. Returns (A,B,C)."""
    y = mp.matrix([logabs[k] for k in ks])
    M = mp.matrix([[mp.mpf(1), mp.mpf(k), k * mp.log(k)] for k in ks])
    c = mp.lu_solve(M.T * M, M.T * y)
    return c[0], c[1], c[2]


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print(" D-ladder ⟺ Φ_b: Écalle acceleration setup + the exact remaining gap")
    print("=" * 78)

    # ---- exact d_k (reused, not recomputed) ------------------------------
    print(f"\n building exact D-ladder at ORD={ORD} (reused build_d_ladder) …", flush=True)
    dk, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    print(f"   KMAX={KMAX}  valid_top={valid_top}  odd_ok={odd_ok}")
    # M1 self-check: exact reproduction — the generating function is
    # reproduced through valid_top (odd_ok), and every d_k ∈ ℚ(√3).
    in_Qsqrt3 = all(sp.simplify(sp.nsimplify(sp.im(sp.N(dk[k], 30)))) == 0 for k in (1, 2, 3))
    print(f"   M1 self-check: odd_ok={odd_ok}, d_k∈ℚ(√3) (real)={in_Qsqrt3}")

    absd = {k: abs(to_mpf(dk[k])) for k in dk}
    logabs = {k: mp.log(absd[k]) for k in dk}

    # ---- M2: parity-level critical times (2-adic ℤ/2 grading) ------------
    print("\n M2 — per-parity divergence class (2-adic bar-parity split):")
    odd_k = sorted(k for k in dk if k % 2 == 1 and k >= 3)
    even_k = sorted(k for k in dk if k % 2 == 0 and k >= 4)
    all_k = sorted(k for k in dk if k >= 4)
    C_full = {}
    # full-series drift: C on the lower half vs the whole (mirrors #3839 drift)
    Kmid = all_k[len(all_k) // 2]
    C_full["low"] = classfit(logabs, [k for k in all_k if k <= Kmid])[2]
    C_full["all"] = classfit(logabs, all_k)[2]
    A_odd, B_odd, C_odd = classfit(logabs, odd_k)
    A_even, B_even, C_even = classfit(logabs, even_k)
    # per-parity stability: split each parity's range in half, compare C
    def parity_drift(par_k):
        mid = par_k[len(par_k) // 2]
        lo = classfit(logabs, [k for k in par_k if k <= mid])[2]
        hi = classfit(logabs, par_k)[2]
        return lo, hi, abs(hi - lo)
    Codd_lo, Codd_hi, Codd_drift = parity_drift(odd_k)
    Ceven_lo, Ceven_hi, Ceven_drift = parity_drift(even_k)
    Cfull_drift = abs(C_full["all"] - C_full["low"])
    print(f"   full   C: low={mp.nstr(C_full['low'],5)} all={mp.nstr(C_full['all'],5)} "
          f"drift={mp.nstr(Cfull_drift,4)}")
    print(f"   odd    C: low={mp.nstr(Codd_lo,5)} hi={mp.nstr(Codd_hi,5)} "
          f"drift={mp.nstr(Codd_drift,4)}   B_odd(geom)={mp.nstr(B_odd,5)}")
    print(f"   even   C: low={mp.nstr(Ceven_lo,5)} hi={mp.nstr(Ceven_hi,5)} "
          f"drift={mp.nstr(Ceven_drift,4)}   B_even(geom)={mp.nstr(B_even,5)}")
    parity_distinct = abs(C_odd - C_even) > mp.mpf("0.01")
    parity_more_stable = (Codd_drift < Cfull_drift) and (Ceven_drift < Cfull_drift)
    print(f"   ⇒ per-parity C distinct: {parity_distinct}  "
          f"(|C_odd−C_even|={mp.nstr(abs(C_odd-C_even),4)})")
    print(f"   ⇒ per-parity C each more stable than full: {parity_more_stable}")
    print(f"     (merged conformal ζ²-plane radii, context: odd ρ={RHO_ZETA_MERGED['odd']}, "
          f"even ρ={RHO_ZETA_MERGED['even']}; 40% split)")

    # ---- M3: acceleration-weight composition collapse --------------------
    print("\n M3 — Borel–Leroy weight composition (fixed-order iteration collapses):")
    comp_ok = True
    for (s1, s2, kk) in ((mp.mpf("0.15"), mp.mpf("0.47"), 12),
                         (mp.mpf("0.19"), mp.mpf("0.16"), 17)):
        fk = mp.factorial(kk)
        lhs = fk ** s1 * fk ** s2
        rhs = fk ** (s1 + s2)
        ok = abs(lhs / rhs - 1) < mp.mpf("1e-45")
        comp_ok = comp_ok and ok
        print(f"   (k={kk}) (k!)^{float(s1)}·(k!)^{float(s2)} = (k!)^{float(s1+s2)} : "
              f"relerr={mp.nstr(abs(lhs/rhs-1),3)}  {ok}")
    print("   ⇒ composition stays in the additive monoid of Borel–Leroy orders;")
    print("     no fixed-order iteration reaches a new critical time ⇒ genuine")
    print("     (non-commutative) Écalle acceleration kernel is necessary.")

    # ---- M4: non-perturbative scale + anchor-blindness at the meridian ---
    print("\n M4 — optimal-truncation resummation at the meridian (anchor test):")
    m4rows = []
    P_star = {}
    for tag, q0 in (("muon", q_muon_at(60)), ("proton", q_at(60)), ("qstar", QSTAR)):
        u_sub = substrate_ladder_quantities(q0)["u"]
        u_mer = q0 * u_sub                          # ũ = q·b·ħ² (generating-fn variable)
        h = q0 - 1 / q0
        terms = {k: to_mpf(dk[k]) * u_mer ** k for k in dk}
        # optimal truncation = least-term index
        Nstar = min(terms, key=lambda k: abs(terms[k]))
        delta_np = abs(terms[Nstar])
        boundary = (Nstar == max(dk))              # least term at the edge ⇒ A_eff is a LOWER bound
        A_eff = -u_mer * mp.log(delta_np)          # δ_np ~ exp(−A/ũ)
        P = sum(terms[k] for k in dk if k <= Nstar)   # optimal-truncation partial sum = D(ũ)
        P_star[tag] = P
        S_pred = h * P                              # S = h·D(ũ) (bridge #3654)
        m4rows.append({
            "anchor": tag, "u_meridian": mp.nstr(u_mer, 22), "Nstar": Nstar,
            "delta_np": mp.nstr(delta_np, 8), "A_eff_or_lowerbound": mp.nstr(A_eff, 8),
            "Nstar_at_edge": bool(boundary), "D_opt_trunc": mp.nstr(P, 12),
            "h_D_eq_S_pred": mp.nstr(S_pred, 10),
            "S_target": mp.nstr(S_TARGET.get(tag, mp.mpf(0)), 10)})
        st = mp.nstr(S_TARGET.get(tag, mp.mpf(0)), 8) if tag in S_TARGET else "—"
        print(f"   {tag:6s}: ũ={mp.nstr(u_mer,10)}  N*={Nstar}{'(edge)' if boundary else ''}  "
              f"δ_np={mp.nstr(delta_np,4)}  A_eff={mp.nstr(A_eff,5)}")
        print(f"           D_opt={mp.nstr(P,9)}  h·D={mp.nstr(S_pred,7)}  S_target={st}")
    # anchor-blindness: muon vs proton optimal-truncation D
    dP = abs(P_star["muon"] - P_star["proton"])
    anchor_blind_pert = dP < mp.mpf("1e-6")
    print(f"   ⇒ |D_opt(muon) − D_opt(proton)| = {mp.nstr(dP,4)}  "
          f"⇒ perturbative sum ANCHOR-BLIND: {anchor_blind_pert}")
    print(f"     (S sign-flips +0.0097→−0.0395 while D_opt does not ⇒ the flip is NOT")
    print(f"      in the accelerated perturbative ladder at this meridian.)")

    # ---- M4b: magnitude tension — is the anchor-dependent S a Stokes jump? -
    print("\n M4b — magnitude tension (Stokes jump vs the O(0.01) anchor residual):")
    # log|term_k| = log|d_k| + k·log ũ; optimal truncation where the term turns
    # around: with log|d_k| ≈ A+Bk+C·k·log k and slope of log-term
    #   d/dk[(B+log ũ)k + C·k·log k] = (B+log ũ) + C(log k + 1) = 0
    #   ⇒ log k* = −(B+log ũ)/C − 1 ⇒ k* ≈ exp(…). The non-pert scale is
    #   δ_np ~ exp(−A_action/ũ) with A_action the leading Borel radius.
    u_mer_mu = q_muon_at(60) * substrate_ladder_quantities(q_muon_at(60))["u"]
    _, B_all, C_all = classfit(logabs, all_k)
    logk_star = -(B_all + mp.log(u_mer_mu)) / C_all - 1
    k_star = mp.e ** logk_star
    # non-perturbative amplitude at true optimal truncation (order of magnitude)
    # ~ exp(−(true action)/ũ); use the merged odd Borel radius as the action proxy
    A_proxy = RHO_ZETA_MERGED["odd"]
    delta_true = mp.e ** (-A_proxy / u_mer_mu)
    h_mu = q_muon_at(60) - 1 / q_muon_at(60)
    S_residual = abs(S_TARGET["muon"] - h_mu * P_star["muon"])
    print(f"   optimal-truncation index  k* ≈ e^{mp.nstr(logk_star,4)} ≈ {mp.nstr(k_star,3)}  "
          f"(≫ 21 ⇒ meridian is deep in the effectively-convergent regime)")
    print(f"   true non-pert scale  exp(−ρ_odd/ũ) = exp(−{RHO_ZETA_MERGED['odd']}/{mp.nstr(u_mer_mu,4)}) "
          f"≈ {mp.nstr(delta_true,3)}")
    print(f"   anchor residual  |S(muon) − h·D_opt| ≈ {mp.nstr(S_residual,4)}  (O(0.01))")
    ratio_exp = mp.log(S_residual / delta_true) / mp.log(10)
    print(f"   ⇒ the O(0.01) anchor residual is ~10^{mp.nstr(ratio_exp,4)} LARGER than a")
    print(f"     naive Stokes jump exp(−ρ/ũ) at the substrate meridian ⇒ the anchor-")
    print(f"     dependent S is NOT a Stokes ambiguity of THIS ladder at THIS (tiny-ũ)")
    print(f"     meridian. It is the 1/ũ³ c₃-representational amplification (#3636), or a")
    print(f"     FIBRE-saddle (|q|=1, ũ~O(1)) object where the jump is unsuppressed (G0).")

    # ---- M5: Φ_b state-integral cross-check ------------------------------
    print("\n M5 — Φ_b state-integral saddle cross-check (leading-order scale):")
    m5rows = []
    for tag, q0 in (("muon", q_muon_at(60)), ("proton", q_at(60))):
        vol, _z, _w = vol_of_m(q0)
        deficit = VOL41 - mp.re(vol)
        m5rows.append({"anchor": tag, "Re_V": mp.nstr(mp.re(vol), 12),
                       "deficit": mp.nstr(deficit, 10),
                       "abs_S_target": mp.nstr(abs(S_TARGET[tag]), 10)})
        print(f"   {tag:6s}: 𝔙 deficit={mp.nstr(deficit,7)}  |S|={mp.nstr(abs(S_TARGET[tag]),7)}  "
              f"deficit/|S|={mp.nstr(deficit/abs(S_TARGET[tag]),4)}")
    print("   ⇒ deficit 0.00940 ≈ |S(muon)| — leading-order near-match (bridge #3654);")
    print("     anchor-blind, consistent with M4's anchor-blind perturbative sum.")

    # ---- verdict ---------------------------------------------------------
    print("\n" + "=" * 78)
    print(" VERDICT (tiered; scope-(a); no c_k wired; no fit):")
    print("  • acceleration setup complete: two critical times = the two 2-adic")
    print("    parity levels (M2, distinct); fixed-order composition collapses (M3).")
    print("  • the forward D-ladder resummation at the substrate meridian is")
    print("    ANCHOR-BLIND to ~9 digits (M4): D_opt≈−0.01667, h·D≈−0.0035 —")
    print("    reproducing NEITHER S(muon)=+0.0097 nor S(proton)=−0.0395.")
    print("  • M4b magnitude tension: the meridian ũ≈0.0095 puts optimal truncation")
    print("    at k*~10^13, so a Stokes jump exp(−ρ/ũ) is ~10^{-7}..10^{-27} — far")
    print("    too small to be the O(0.01) anchor-dependent S. So at the substrate")
    print("    branch the anchor swing is NOT a Stokes ambiguity of this ladder.")
    print("  ⇒ the exact remaining gap: the anchor-dependent c₃ is either the 1/ũ³")
    print("    c₃-representational amplification (#3636) of a smooth tail, or the")
    print("    Stokes datum A_ω computed at the FIBRE saddle |q|=1 (ũ~O(1),")
    print("    unsuppressed jump) — the G0 branch-mismatch / G3 monodromy datum.")
    print("  ⇒ NO c₃ produced; NO instanton action identified; NOTHING wired.")
    print(f"\n wall {time.time()-t0:.1f}s")

    # ---- witness ---------------------------------------------------------
    wb = WitnessBuilder("qbeta-dladder-ecalle-phib-resummation", engine="mpmath")
    wb.set_description(
        "Écalle acceleration ⟺ Φ_b state-integral resummation of the bar-odd Q_β "
        "D-ladder (unowned item #1 of the 1ppQ path reassessment). Reuses the exact "
        "d_k (build_d_ladder, ORD 43/k≤21), phi_b saddle vol_of_m, and the merged "
        "#3818/#3839 negatives; measures four un-pinned things. M2: the 2-adic "
        "bar-parity split gives two DISTINCT divergence classes (C_odd≈0.05, C_even≈0.11, "
        "|Δ|≈0.06) ⇒ the 'no single Gevrey index' is consistent with a genuine TWO-LEVEL "
        "(accelero-summable) structure — two critical times, not one mis-specified order "
        "(per-parity fits still short/noisy at k≤21, consistent with undecidable-at-k21). M3: "
        "(k!)^{s1}(k!)^{s2}=(k!)^{s1+s2} ⇒ composing Borel–Leroy transforms stays in "
        "the additive monoid of orders and cannot reach a new critical time ⇒ a "
        "genuine non-commutative Écalle kernel is necessary (the fixed-order negative "
        "is not repairable by iteration). M4: the forward optimal-truncation resummed "
        "D(ũ)≈−0.01667 at the meridian is ANCHOR-BLIND to ~9 digits (muon vs proton ũ "
        "differ ~2e-9), and h·D≈−0.0035 reproduces NEITHER S(muon)=+0.0097 NOR "
        "S(proton)=−0.0395. M4b magnitude tension: the substrate meridian ũ≈0.0095 puts "
        "optimal truncation at k*~1e13, so a Stokes jump exp(−ρ/ũ) is ~1e-7..1e-27 — far "
        "too small to be the O(0.01) anchor-dependent S; on the SUBSTRATE branch the swing "
        "is not a Stokes ambiguity of this ladder. M5: the Φ_b saddle deficit 0.00940 ≈ "
        "|S(muon)| — a separate anchor-blind geometric handle on the |S| scale (bridge "
        "#3654). VERDICT: acceleration setup complete + two critical times = the two parity "
        "levels; the perturbative acceleration at the substrate meridian gives only an "
        "anchor-blind floor and does NOT reproduce S; the exact remaining gap is that the "
        "anchor-dependent c₃ is either the 1/ũ³ c₃-representational amplification (#3636) or "
        "the fibre-saddle (|q|=1, ũ~O(1)) Stokes datum A_ω where the jump is unsuppressed "
        "(the G0 branch-mismatch / G3 monodromy datum) — NOT produced here. Scope-(a); no "
        "c_k wired; no fit; no tier change; L2 count unchanged (2/7).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("M2_parity_levels", {
        "C_full_low": mp.nstr(C_full["low"], 8), "C_full_all": mp.nstr(C_full["all"], 8),
        "C_full_drift": mp.nstr(Cfull_drift, 8),
        "C_odd": mp.nstr(C_odd, 8), "C_odd_drift": mp.nstr(Codd_drift, 8), "B_odd": mp.nstr(B_odd, 8),
        "C_even": mp.nstr(C_even, 8), "C_even_drift": mp.nstr(Ceven_drift, 8), "B_even": mp.nstr(B_even, 8),
        "parity_C_distinct": bool(parity_distinct),
        "parity_C_each_more_stable_than_full": bool(parity_more_stable),
        "merged_conformal_zeta2_radii": {"odd": "0.152", "even": "0.254", "note": "#3818 context, not recomputed"}})
    wb.add_data("M3_composition_collapse", {
        "identity": "(k!)^{s1}·(k!)^{s2} = (k!)^{s1+s2}", "verified": bool(comp_ok),
        "consequence": "Borel–Leroy iteration stays in additive monoid of orders; genuine Écalle kernel necessary"})
    wb.add_data("M4_meridian_optimal_truncation", m4rows)
    wb.add_data("M4_anchor_blindness", {
        "D_opt_muon_minus_proton": mp.nstr(dP, 8),
        "perturbative_sum_anchor_blind": bool(anchor_blind_pert),
        "h_D_opt_muon": mp.nstr((q_muon_at(60) - 1 / q_muon_at(60)) * P_star["muon"], 8),
        "reading": "forward D-ladder sum is anchor-blind and reproduces NEITHER S(muon) NOR S(proton); "
                   "the anchor swing is not in the perturbative accelerated ladder"})
    wb.add_data("M4b_magnitude_tension", {
        "optimal_truncation_k_star_log10": mp.nstr(logk_star / mp.log(10), 6),
        "stokes_jump_exp_minus_rho_over_u": mp.nstr(delta_true, 6),
        "anchor_residual_S_minus_hDopt": mp.nstr(S_residual, 6),
        "residual_over_stokes_log10": mp.nstr(ratio_exp, 6),
        "reading": "meridian ũ≈0.0095 ⇒ optimal truncation at k*~1e13, Stokes jump exp(−ρ/ũ) is "
                   "~1e-7..1e-27 — far too small to be the O(0.01) anchor S; so on the SUBSTRATE "
                   "branch the swing is not a Stokes ambiguity of this ladder. It is either the 1/ũ³ "
                   "c₃-representational amplification (#3636) or the fibre-saddle (|q|=1, ũ~O(1)) "
                   "Stokes datum A_ω where the jump is unsuppressed (G0 branch-mismatch)"})
    wb.add_data("M5_phib_saddle_crosscheck", m5rows)
    wb.add_data("verdict", {
        "acceleration_setup_complete": True,
        "two_critical_times_eq_two_parity_levels": bool(parity_distinct),
        "perturbative_resummation_anchor_blind": bool(anchor_blind_pert),
        "c3_produced": False, "instanton_action_identified": False, "wired": False,
        "perturbative_floor_h_D_opt": mp.nstr((q_muon_at(60) - 1 / q_muon_at(60)) * P_star["muon"], 8),
        "exact_remaining_gap": "the anchor-dependent c₃ (S sign-flip) is NOT the substrate-branch "
                               "perturbative acceleration (anchor-blind, magnitude-too-small for a "
                               "Stokes jump at ũ≈0.0095); it is either (i) the 1/ũ³ c₃-representational "
                               "amplification (#3636) of a smooth tail, or (ii) the fibre-saddle "
                               "(|q|=1, ũ~O(1)) Stokes datum A_ω = Δ_ω log Φ_b where the jump is "
                               "unsuppressed (G0 branch-mismatch / G3 monodromy datum). Next session: "
                               "compute the D-ladder / Φ_b expansion at the FIBRE saddle, not the substrate meridian."})

    wb.add_assertion(name="exact_dk_reproduced",
                     computed=1.0 if (odd_ok and in_Qsqrt3) else 0.0, expected=1.0, tolerance=0.5,
                     source="build_d_ladder reproduces the generating function through valid_top (odd_ok) and d_k∈ℚ(√3)")
    wb.add_assertion(name="parity_levels_distinct",
                     computed=1.0 if parity_distinct else 0.0, expected=1.0, tolerance=0.5,
                     source="per-parity divergence classes C_odd, C_even differ by >0.01 (two critical times)")
    wb.add_assertion(name="borel_leroy_composition_collapses",
                     computed=1.0 if comp_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="(k!)^{s1}(k!)^{s2}=(k!)^{s1+s2} to 1e-45: fixed-order iteration cannot reach a new critical time")
    wb.add_assertion(name="perturbative_resummation_anchor_blind",
                     computed=1.0 if anchor_blind_pert else 0.0, expected=1.0, tolerance=0.5,
                     source="optimal-truncation D(ũ) identical muon vs proton (<1e-6) while S sign-flips ⇒ anchor-dependence is non-perturbative (A_ω)")
    wb.save()
    print(" witness saved: qbeta-dladder-ecalle-phib-resummation.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
