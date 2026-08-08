#!/usr/bin/env python3
"""qbeta_awpk_perwinding_stokes_41_probe.py — bean qou-awpk (route 2 of qou-qnnq):
per-WINDING-CLASS Stokes constants of 4₁, extracted exactly, and the effective
Stokes coefficient at the observed ϑ sheets.

Context. GGM ("Peacock patterns", 2012.00062) show the Borel singularities of
the CS/Kashaev asymptotic series sit on a LATTICE of translates, with a separate
integer Stokes constant at each point — not the single constant A_ω = 3 the
corpus's T4/T5 chain (qbeta_t4_stokes3_crux_probe.py; S_K = A_ω·κ·(ln²q₀−ϑ_K²))
carries. The proven-for-4₁ dictionary (GGM eq 21 / 2007.10190 eq 5/80) x-refines
the geometric Stokes entry by the winding number e:

    S⁺_{σ₁σ₁}(w; q̃) = Σ_e I_{4₁}(0,e)(q̃) · wᵉ ,     S⁺_{σ₁σ₁}(1; q̃) = rotated index
                                                     = 1 −8q̃ −9q̃² +18q̃³ +46q̃⁴ +…

so the per-winding Stokes data at the lattice points over ι = Vol(4₁)/π are
EXACTLY the 3d-index coefficients I(0,e), and the observed sheet enters as the
meridian holonomy w = e^𝔲 (corpus 𝔲-coordinate u = 2 log m, m = q₀e^{iϑ_K}).

What this probe does (all exact integer series; mpmath only for evaluation):

  C1  compute I(0,e) per winding e via the VALIDATED DGG eq (4.18) flux-sum
      engine (qbeta_g3_fourone_index_assembly_corrected / tranche-1 I_Δ) and
      certify the e-sum against the printed rotated index through q̃⁶ — closing
      the "e-sum numerical reproduction deferred" item of the corrected
      assembly probe (its truncation subtlety is handled by higher internal
      order + explicit e- and internal-order stability guards).
  C2  certify amphichirality I(0,e) = I(0,−e) coefficient-wise.
  C3  record the per-winding table I(0,e) — the qou-awpk extraction.
  S1  evaluate each I(0,e)(q̃_sub) at the substrate q̃_sub = 1/q₀ with a
      truncation-stability guard (deep order, background-run discipline).
  S2  form A_eff(𝔲) = Σ_e I(0,e)(q̃_sub)·wᵉ at the observed sheets
      ϑ_muon ≈ 0.0586, ϑ_proton ≈ 0.2031 (T4 back-solved, now DERIVED from
      the canonical q₀ via qbeta_t4_anchors — see qou-vbw1) under FOUR
      sheet conventions w ∈ {e^{iϑ}, e^{2iϑ}, q₀e^{iϑ}, q₀²e^{2iϑ}}, and test:
        (i)   does A_eff differ from the u=0 tower value (constant-A_ω check)?
        (ii)  is Im A_eff ≡ 0 on unit-modulus sheets (amphichiral bar-even
              structure — radial deformation REQUIRED for any bar-odd part)?
        (iii) does the bar-odd part Im A_eff flip sign between the two sheets,
              and how does the ratio compare to S(proton)/S(muon) = −4.0751?

Anti-laundering scope (STRICT): (iii) is a parameter-free COMPARISON — every
input (I(0,e), q₀, the T4 ϑ values) is fixed upstream; nothing is fitted and
nothing is wired. Whatever the numbers say is recorded as-is, per-convention.
The σ₁σ₁ entry is the one with a literature-proven x-refinement; the T4 integer
3 lives in the σ₁σ₂ channel whose x-refinement is NOT proven in-repo — this
probe therefore tests the winding-dependence MECHANISM on the proven channel,
not the σ₁σ₂ constant itself. Scope-(a); no c_k wired; no fit.

Run (deep layer ~5-10 min on the exact-int canonical-chamber engine):
  python3 -u computations/probes/qbeta_awpk_perwinding_stokes_41_probe.py \
      2>&1 | tee /tmp/qbeta_awpk_perwinding.log
Fast certification-only run: pass --cert-only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qbeta_t4_anchors import theta_t4, S_ANCHORS  # noqa: E402

from qbeta_g3_fourone_index_assembly_corrected import (  # noqa: E402
    assemble_I41, e2_window_for,
)

set_compute_dps()

# printed rotated index (GGM eq 61 / 2007.10190 eq 80) — the e-sum target
ROTATED = {0: 1, 1: -8, 2: -9, 3: 18, 4: 46, 5: 90, 6: 62}
Q_CERT = 6            # q̃-order of the exact certification (printed data depth)
ORD_CERT = 96         # internal x-order for certification assemblies (x = q̃^½)
E_CERT = 14           # winding window for the e-sum certification
# Substrate layer runs on the exact-integer canonical-chamber engine
# (_awpk_fast_index.CanonicalTetEngine — NO floats in series arithmetic, owner
# directive 2026-07-31; mpmath point evaluation only). Index coefficients grow
# ~e^{c√k}, so at q̃ ≈ 0.9009 the tail only turns over near q̃-order ~600 —
# q̃-order 400 is PRE-ASYMPTOTIC and its partial sums are meaningless. The
# convergence certificate is INTERNAL-ORDER stability across this ladder:
DEEP_ORDERS = (1600, 2400, 3200)       # x-orders; agree-digits between the last
                                       # two is the certificate
E_SUB = 28            # winding window for substrate A_eff. NOT 8: the winding
                      # sum's terms only turn over near e ≈ 8–16 (lead(e) ≈
                      # T(⌈e/2⌉) ≈ e²/8, so |I(0,e)(q̃)·w^e| peaks where
                      # 2e·ln q₀ ≈ (e²/8)·ln q₀ — at e ≈ 16 for |w| = q₀²);
                      # truncating at the hump would silently bias A_eff.
                      # Per-sheet last-winding tail magnitudes are recorded.

# T4 back-solved sheet angles — now DERIVED from the canonical q₀ rather than
# typed as 8-digit literals (bean qou-vbw1). The old literals 0.05894648 /
# 0.20323503 were inverted at a q₀ that turned out to be a unit conflation
# (h = q₀ − 1/q₀ read as 2·ln q₀); see qbeta_t4_anchors for the full note.
# These remain A_ω-CONDITIONED readings, not independent determinations.
THETA_MUON = theta_t4("muon")
THETA_PROTON = theta_t4("proton")
S_MUON = mp.mpf(S_ANCHORS["muon"])
S_PROTON = mp.mpf(S_ANCHORS["proton"])


def xser_eval(xser, xval):
    """Evaluate an absolute-x-exponent integer series dict at x = xval."""
    return mp.fsum(c * xval ** k for k, c in xser.items() if c)


def xser_to_q(xser):
    """x = q̃^½ series → q̃ series; requires even exponents (integer q̃-powers)."""
    out = {}
    for k, c in xser.items():
        if k % 2:
            raise ValueError(f"odd x-exponent {k} (coeff {c})")
        out[k // 2] = out.get(k // 2, 0) + c
    return {p: c for p, c in out.items() if c}


def main() -> int:
    cert_only = "--cert-only" in sys.argv
    print("=" * 78)
    print(" qou-awpk — per-winding Stokes constants of 4₁ + effective A at ϑ sheets")
    print("=" * 78)

    # ---------------- C1/C2/C3: exact per-winding extraction ----------------
    print(f"\n[C] per-winding I(0,e), internal x-order {ORD_CERT}, |e| ≤ {E_CERT}:")
    t0 = time.time()
    Ie = {}
    for e in range(0, E_CERT + 1):
        Ie[e] = assemble_I41(0, e, ORD_CERT)
        print(f"    e={e:>2}: {len(Ie[e])} terms   [{time.time()-t0:5.1f}s]")
    # C2: amphichirality on explicitly assembled negatives
    amph_ok = all(assemble_I41(0, -e, ORD_CERT) == Ie[e] for e in (1, 2, 3))
    print(f"    amphichiral I(0,e) = I(0,−e) (e = 1,2,3, full order): {amph_ok}")

    # C1: e-sum vs printed rotated index, with e-window + internal-order stability
    def esum_q(ie_map, emax):
        acc = {}
        for e in range(-emax, emax + 1):
            src = ie_map[abs(e)]
            for k, c in src.items():
                acc[k] = acc.get(k, 0) + c
        return xser_to_q({k: c for k, c in acc.items() if c})

    total = esum_q(Ie, E_CERT)
    total_smaller = esum_q(Ie, E_CERT - 3)
    cert_ok = all(total.get(p, 0) == ROTATED[p] for p in range(Q_CERT + 1))
    ewin_stable = all(total.get(p, 0) == total_smaller.get(p, 0)
                      for p in range(Q_CERT + 1))
    got = " ".join(f"{'+' if total.get(p,0)>=0 else ''}{total.get(p,0)}q^{p}"
                   for p in range(Q_CERT + 1))
    print(f"\n    Σ_e I(0,e) = {got}")
    print(f"    printed    = +1q^0 -8q^1 -9q^2 +18q^3 +46q^4 +90q^5 +62q^6")
    print(f"    exact match: {cert_ok}   e-window stable (E={E_CERT} vs {E_CERT-3}): "
          f"{ewin_stable}")

    # C3: the per-winding table (q̃-coefficients where integer powers exist)
    per_winding = {}
    for e in range(0, min(E_SUB, E_CERT) + 1):
        try:
            qc = xser_to_q(Ie[e])
            per_winding[e] = {str(p): qc.get(p, 0) for p in range(0, 11)}
        except ValueError:
            per_winding[e] = {"note": "half-integer q̃-powers present"}
    print("\n    per-winding table I(0,e) (q̃^0..q̃^10):")
    for e, row in per_winding.items():
        if "note" in row:
            print(f"      e={e}: {row['note']}")
        else:
            print(f"      e={e}: {[row[str(p)] for p in range(11)]}")

    wb = WitnessBuilder("qbeta-awpk-perwinding-stokes-41", engine="python-int+mpmath")
    wb.set_description(
        "Bean qou-awpk (route 2 of qou-qnnq): per-winding-class Stokes data of "
        "4_1 extracted exactly via the proven GGM x-refined dictionary "
        "S+_sigma1sigma1(w;q) = Sum_e I_41(0,e)(q) w^e on the validated DGG "
        "eq-(4.18) flux-sum engine. Closes the 'e-sum numerical reproduction "
        "deferred' item of qbeta-g3-fourone-index-assembly-corrected (exact "
        "match to the printed rotated index through q^6, e-window stable), "
        "certifies amphichirality per winding, and evaluates the effective "
        "Stokes coefficient A_eff(u) = Sum_e I(0,e)(q_sub) w^e at the observed "
        "T4 sheets under four sheet conventions. Parameter-free comparison "
        "against S(proton)/S(muon) = -4.0751; per-convention results recorded "
        "as-is. Sigma1sigma1 channel only (the literature-proven x-refinement); "
        "no c_k wired; no fit; scope-(a).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("source",
                "GGM 2012.00062 (peacock lattice) + GGM 2007.10190 eq 5/80 "
                "(rotated index dictionary) + DGG 1112.5179 eq 4.18 (flux sum); "
                "engine: qbeta_g3_fourone_index_assembly_corrected (validated)")
    wb.add_data("per_winding_I0e_qcoef", per_winding)
    wb.add_data("esum_reproduction", {
        "computed": {str(p): total.get(p, 0) for p in range(Q_CERT + 1)},
        "printed": {str(p): ROTATED[p] for p in ROTATED},
        "internal_x_order": ORD_CERT, "e_window": E_CERT})
    wb.add_assertion("esum_reproduces_rotated_index",
                     computed=1.0 if cert_ok else 0.0, expected=1.0, tolerance=0.5,
                     source=f"Sum_e I(0,e) == 1-8q-9q^2+18q^3+46q^4+90q^5+62q^6 "
                            f"exactly (internal x-order {ORD_CERT}, |e|<={E_CERT})")
    wb.add_assertion("e_window_stable",
                     computed=1.0 if ewin_stable else 0.0, expected=1.0, tolerance=0.5,
                     source=f"e-sum identical for E={E_CERT} vs E={E_CERT-3} through q^{Q_CERT}")
    wb.add_assertion("amphichiral_per_winding",
                     computed=1.0 if amph_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="I(0,e) == I(0,-e) exactly at full order for e=1,2,3")

    if cert_only:
        wb.add_data("substrate_layer", "skipped (--cert-only)")
        wb.save()
        print("\n  [--cert-only] witness saved; substrate layer skipped.")
        return 0 if (cert_ok and ewin_stable and amph_ok) else 1

    # ---------------- S1: substrate evaluation per winding ----------------
    from _awpk_fast_index import eval_I41_at  # exact-int canonical-chamber engine

    q0 = q_at(50)
    t = mp.log(q0)
    q_sub = mp.e ** (-t)          # q̃ on the unit-disc side, = 1/q₀ ≈ 0.9009
    x_sub = mp.sqrt(q_sub)
    print(f"\n[S1] substrate q̃ = 1/q₀ = {mp.nstr(q_sub, 12)}; "
          f"internal-order ladder {DEEP_ORDERS} (exact-int engine):")
    Ie_deep_val = {}
    Ie_conv_digits = {}
    Ie_partials = {}
    t0 = time.time()
    for e in range(0, E_SUB + 1):
        ladder = {}
        for od in DEEP_ORDERS:
            ladder[od] = eval_I41_at(0, e, x_sub, od, e2_window_for(od, 0, e))
        full = ladder[DEEP_ORDERS[-1]]
        # honest certificate: digits of agreement between the two deepest
        # internal orders; a diff >= 1 counts as 0 digits (no else-40 sentinel
        # — a pre-asymptotic value must not report as converged).
        d = abs(full - ladder[DEEP_ORDERS[-2]])
        if d == 0:
            digits = 40
        elif d < 1:
            digits = int(-mp.log10(d))
        else:
            digits = 0
        Ie_deep_val[e] = full
        Ie_conv_digits[e] = digits
        Ie_partials[e] = {str(od): mp.nstr(v, 18) for od, v in ladder.items()}
        print(f"    e={e}: I(0,e)(q̃_sub) = {mp.nstr(full, 15):>22}  "
              f"[{digits:>2} agree-digits {DEEP_ORDERS[-2]} vs {DEEP_ORDERS[-1]}]  "
              f"[{time.time()-t0:6.1f}s]")
        print(f"          order ladder {Ie_partials[e]}")
    conv_ok = min(Ie_conv_digits.values()) >= 6
    tower_val = Ie_deep_val[0] + 2 * mp.fsum(Ie_deep_val[e] for e in range(1, E_SUB + 1))
    print(f"    Σ_e I(0,e)(q̃_sub) [|e|≤{E_SUB}] = {mp.nstr(tower_val, 15)}")

    # -------- S1b: honest deep tower S⁺₁₁(q̃_sub) via the certified sandwich --
    # The g3 witness value 0.2584… carries stable_digits=40 — the else-40
    # SENTINEL (its 90%-truncation diff was >= 1), so it is unverified. Deep
    # re-evaluation here with the honest ladder guard, using the sandwich
    # exemplar DERIVED and certified in qbeta_g3_ggm_stokes_41 (sign=-1,
    # transpose on the second W, A=[[0,1],[1,1]], B=[[0,1],[1,0]],
    # C=[[0,1],[-1,-2]]), head re-verified against the printed (61) here.
    from qbeta_g3_ggm_stokes_41 import (
        W_matrix, mat_mul_series, const_mat, transpose, PRINTED_61,
    )
    TOWER_ORD = 1600
    TOWER_CUTS = (800, 1200, 1600)
    print(f"\n[S1b] deep tower S⁺₁₁(q̃_sub) via certified sandwich, "
          f"q̃-order {TOWER_ORD}:")
    Am, Bm, Cm, sgn_s = [[0, 1], [1, 1]], [[0, 1], [1, 0]], [[0, 1], [-1, -2]], -1
    Wd = W_matrix(-1, TOWER_ORD)
    core = mat_mul_series(
        mat_mul_series(Wd, const_mat(Bm, TOWER_ORD), TOWER_ORD),
        transpose(Wd), TOWER_ORD)
    Sd = mat_mul_series(
        mat_mul_series(const_mat(Am, TOWER_ORD), core, TOWER_ORD),
        const_mat(Cm, TOWER_ORD), TOWER_ORD)
    s11_deep = [sgn_s * x // 2 for x in Sd[0][0]]
    head_ok = s11_deep[:7] == PRINTED_61
    tower_ladder = {c: mp.fsum(co * q_sub ** k
                               for k, co in enumerate(s11_deep[:c + 1]) if co)
                    for c in TOWER_CUTS}
    tower_full = tower_ladder[TOWER_CUTS[-1]]
    dtw = abs(tower_full - tower_ladder[TOWER_CUTS[-2]])
    tower_digits = 40 if dtw == 0 else (int(-mp.log10(dtw)) if dtw < 1 else 0)
    print(f"    head == printed (61): {head_ok}")
    print(f"    ladder {{ {', '.join(f'{c}: {mp.nstr(v, 15)}' for c, v in tower_ladder.items())} }}")
    print(f"    S⁺₁₁(q̃_sub) = {mp.nstr(tower_full, 15)} [{tower_digits} agree-digits]")
    print(f"    g3 witness claimed 0.2584362672614084 [stable_digits=40 = SENTINEL]")
    print(f"    per-winding e-sum |e|≤{E_SUB}: {mp.nstr(tower_val, 15)} "
          f"(e-tail = winding sum minus tower: {mp.nstr(tower_val - tower_full, 6)})")
    tower_ok = head_ok and tower_digits >= 8

    # ---------------- S2: effective A at the observed sheets ----------------
    ln_q0 = t
    sheets = {
        "muon": THETA_MUON,
        "proton": THETA_PROTON,
    }
    conventions = {
        "unit_e_itheta": lambda th: mp.e ** (1j * th),
        "unit_e_2itheta": lambda th: mp.e ** (2j * th),
        "q0_e_itheta": lambda th: q0 * mp.e ** (1j * th),
        "q0sq_e_2itheta": lambda th: (q0 ** 2) * mp.e ** (2j * th),
    }
    print(f"\n[S2] A_eff(𝔲) = Σ_e I(0,e)(q̃_sub)·wᵉ at the T4 sheets "
          f"(ϑ_μ={THETA_MUON}, ϑ_p={THETA_PROTON}):")
    s2 = {}
    unit_im_max = mp.mpf(0)
    for cname, wfun in conventions.items():
        s2[cname] = {}
        for aname, th in sheets.items():
            w = wfun(th)
            val = Ie_deep_val[0] + mp.fsum(
                Ie_deep_val[e] * (w ** e + w ** (-e)) for e in range(1, E_SUB + 1))
            # tail estimate: last winding's contribution magnitude
            tail = abs(Ie_deep_val[E_SUB]) * (abs(w) ** E_SUB + abs(w) ** (-E_SUB))
            s2[cname][aname] = {
                "w": mp.nstr(w, 12), "re": mp.nstr(mp.re(val), 12),
                "im": mp.nstr(mp.im(val), 12), "abs": mp.nstr(abs(val), 12),
                "tail_last_winding": mp.nstr(tail, 3),
            }
            if cname.startswith("unit"):
                unit_im_max = max(unit_im_max, abs(mp.im(val)))
        a_mu = s2[cname]["muon"]
        a_pr = s2[cname]["proton"]
        print(f"    {cname:>16}: muon Re={a_mu['re']:>14} Im={a_mu['im']:>14} | "
              f"proton Re={a_pr['re']:>14} Im={a_pr['im']:>14}")

    # structural check (ii): unit-modulus sheets are exactly bar-even
    unit_bar_even = unit_im_max < mp.mpf("1e-30")
    print(f"\n    (ii) Im A_eff ≡ 0 on unit-modulus sheets (amphichiral): "
          f"{unit_bar_even} (max |Im| = {mp.nstr(unit_im_max, 3)})")

    # radius diagnostic: |I(0,e)(q̃_sub)|^{1/e} — if this tends to 1 the
    # winding sum has radius of convergence 1 in w, and every radial sheet
    # (|w| = q₀ or q₀²) lies OUTSIDE the convergence annulus: its partial
    # sums are then divergent exhibits, NOT the analytic continuation. Note
    # also q₀ = 1.1100 already exceeds q̃^{-1/2} = 1.0535, the natural
    # index-annulus boundary.
    radius_diag = {str(e): mp.nstr(abs(Ie_deep_val[e]) ** (mp.mpf(1) / e), 8)
                   for e in range(4, E_SUB + 1, 4) if Ie_deep_val[e] != 0}
    print(f"    radius diagnostic |I(0,e)|^(1/e): {radius_diag}")

    # test (iii): sign flip + ratio. The radial conventions lie outside the
    # empirical convergence annulus (see radius diagnostic), so their rows are
    # DIVERGENT-PARTIAL-SUM EXHIBITS, recorded for the region-of-validity
    # finding — no physical conclusion is drawn from them. On the CONVERGENT
    # domain (|w| = 1) the sum is exactly bar-even, so the winding-refined
    # σ₁σ₁ Stokes cannot supply a bar-odd part by naive summation at any ϑ:
    # a bar-odd S requires lateral/analytically-continued data.
    ratio_obs = S_PROTON / S_MUON
    iii = {}
    for cname in ("q0_e_itheta", "q0sq_e_2itheta"):
        im_mu = mp.mpf(s2[cname]["muon"]["im"])
        im_pr = mp.mpf(s2[cname]["proton"]["im"])
        flip = (im_mu > 0 > im_pr) or (im_pr > 0 > im_mu)
        ratio = im_pr / im_mu if im_mu != 0 else mp.inf
        iii[cname] = {"im_muon": mp.nstr(im_mu, 12), "im_proton": mp.nstr(im_pr, 12),
                      "sign_flip": bool(flip), "ratio_pred": mp.nstr(ratio, 8),
                      "ratio_observed": mp.nstr(ratio_obs, 8),
                      "validity": "OUTSIDE convergence annulus — divergent "
                                  "partial sum, not the analytic continuation; "
                                  "exhibit only"}
        print(f"    (iii) {cname} [outside annulus — exhibit only]: sign flip "
              f"{flip}; Im-ratio p/μ = {mp.nstr(ratio, 8)} vs observed "
              f"S_p/S_μ = {mp.nstr(ratio_obs, 8)}")

    # test (i): deviation of |A_eff| from the u=0 tower value per sheet
    dev = {c: {a: mp.nstr(mp.mpf(s2[c][a]["abs"]) / tower_val, 10)
               for a in sheets} for c in conventions}
    print(f"\n    (i) |A_eff| / A_eff(u=0) per convention/sheet: {dev}")

    wb.add_data("substrate", {
        "q_tilde_sub": mp.nstr(q_sub, 20), "deep_order_ladder": list(DEEP_ORDERS),
        "engine": "exact-int canonical-chamber (_awpk_fast_index; no floats "
                  "in series arithmetic per owner directive 2026-07-31)",
        "per_winding_values": {str(e): mp.nstr(Ie_deep_val[e], 20)
                               for e in Ie_deep_val},
        "per_winding_agree_digits": {str(e): Ie_conv_digits[e]
                                     for e in Ie_conv_digits},
        "per_winding_partial_sums": Ie_partials,
        "guard_note": "agree-digits = |order-ladder last two evaluations|; a "
                      "difference >= 1 reports 0 digits (the naive else-40 "
                      "sentinel of the earlier guard pattern silently passes "
                      "diverging sums)",
        "tower_esum": mp.nstr(tower_val, 20)})
    wb.add_data("deep_tower_S11", {
        "value": mp.nstr(tower_full, 25),
        "agree_digits": tower_digits,
        "q_order": TOWER_ORD,
        "ladder": {str(c): mp.nstr(v, 20) for c, v in tower_ladder.items()},
        "head_matches_printed_61": bool(head_ok),
        "g3_witness_value_unverified": "0.2584362672614084 with stable_digits=40 "
                                       "— the else-40 SENTINEL (90%-truncation "
                                       "diff >= 1); superseded by this honest "
                                       "ladder evaluation",
        "e_tail_at_E_SUB": mp.nstr(tower_val - tower_full, 8)})
    wb.add_data("sheet_evaluations", s2)
    wb.add_data("test_ii_unit_sheets_bar_even",
                {"holds": bool(unit_bar_even),
                 "meaning": "amphichirality forces Im A_eff = 0 for |w| = 1: the "
                            "bar-odd part REQUIRES radial (ln q0) deformation — "
                            "matches the corpus structure u = ln q0 + i*theta"})
    wb.add_data("test_iii_sign_flip_and_ratio", iii)
    wb.add_data("test_i_deviation_from_constant_A", dev)
    wb.add_data("t4_inputs_not_refit", {
        "theta_muon": THETA_MUON, "theta_proton": THETA_PROTON,
        "S_muon": mp.nstr(S_MUON, 10), "S_proton": mp.nstr(S_PROTON, 10),
        "source": "qbeta_t4_stokes3_crux_probe.py (back-solved under constant "
                  "A_omega=3; used here as fixed sheet coordinates)"})
    wb.add_assertion("substrate_per_winding_converged",
                     computed=1.0 if conv_ok else 0.0, expected=1.0, tolerance=0.5,
                     source=f"every I(0,e)(q_sub), e<=E_SUB, agrees to >=6 digits "
                            f"between internal x-orders {DEEP_ORDERS[-2]} and "
                            f"{DEEP_ORDERS[-1]} (exact-int engine; diff>=1 counts "
                            f"as 0 digits, no else-40 sentinel)")
    wb.add_assertion("unit_sheets_exactly_bar_even",
                     computed=1.0 if unit_bar_even else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="max |Im A_eff| < 1e-30 on unit-modulus sheet "
                            "conventions (amphichiral structural check)")
    wb.add_assertion("deep_tower_honest_ladder",
                     computed=1.0 if tower_ok else 0.0, expected=1.0,
                     tolerance=0.5,
                     source=f"S+11 deep series head == printed (61) AND ladder "
                            f"agreement >= 8 digits at q-orders "
                            f"{TOWER_CUTS[-2]} vs {TOWER_CUTS[-1]} (supersedes "
                            f"the g3 witness sentinel-guarded value)")
    ok = (cert_ok and ewin_stable and amph_ok and conv_ok and unit_bar_even
          and tower_ok)
    wb.add_data("verdict", (
        "PER-WINDING EXTRACTION CERTIFIED: Sum_e I(0,e) reproduces the printed "
        "rotated index exactly (deferred item closed); per-winding table "
        "recorded; unit-modulus sheets are exactly bar-even (radial deformation "
        "required for bar-odd, matching u = ln q0 + i*theta). Effective-A "
        "results at the T4 sheets recorded per-convention in "
        "test_iii_sign_flip_and_ratio / test_i — parameter-free comparisons, "
        "nothing wired; interpretation deferred to the audit doc."
        if ok else "INCONCLUSIVE — an assertion failed; inspect the log."))
    wb.save()
    print(f"\n  all assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-awpk-perwinding-stokes-41.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
