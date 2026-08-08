#!/usr/bin/env python3
"""qbeta_3bp8_w2_direct_sheet_probe.py — W2 of bean qou-3bp8: the effective
winding-refined Stokes coefficient at the CORPUS SHEET by direct summation.

The entirety finding (this PR; Lean `summable_winding_of_sq_dominated`)
showed the winding generating function F(w) = Σ_e I₄₁(0,e)(q̃)·wᵉ is entire
on ℂ*: the substrate values decay super-exponentially past the
pre-asymptotic hump (measured: 2·10⁻⁵ / 2·10⁻¹⁶ / 3.5·10⁻³² / 1.9·10⁻⁵³ at
e = 40/60/80/100, tracking the quadratic lead ≈ e²/8). The #4433 "radius
exactly 1 ⇒ corpus sheet outside the annulus" reading was a pre-asymptotic
artifact (e ≤ 28 window) — no analytic continuation is needed: the corpus
sheet w = e^𝔲 is reached by DIRECT two-sided summation.

This probe computes, at the T4 sheets ϑ_muon ≈ 0.0585920, ϑ_proton ≈ 0.2031325
(T4-inverted, DERIVED from the canonical q₀ via `qbeta_t4_anchors` rather than
typed — bean qou-vbw1; fixed inputs, NOT re-fitted), under the two radial sheet
conventions of #4433
(w = q₀·e^{iϑ} and w = q₀²·e^{2iϑ}, u = 2 log m convention):

  W2a  A_eff(𝔲) = Σ_{|e| ≤ E} I(0,e)(q̃)·wᵉ with per-e internal-order
       ladder certification and the winding tail recorded (terms decay
       super-exponentially by e ≈ 45–60 at these radii);
  W2b  the parameter-free tests of the qou-awpk route, now with the
       honest full sum: (i) deviation of A_eff from the w = 1 tower value
       0.42764420; (ii) sign structure of Im A_eff between the two sheets;
       (iii) the ratio Im A_eff(ϑ_p)/Im A_eff(ϑ_μ) against the observed
       S(proton)/S(muon) = −4.0751256.

Anti-laundering scope (STRICT): every input is fixed upstream (I(0,e)
exact engine, q₀, T4 ϑ values); nothing is fitted, nothing is wired;
whatever the numbers say is recorded as-is. σ₁σ₁ channel only (the
literature-proven x-refinement). Exact-int + mpmath only (no float64,
owner directive). Scope-(a).

Run (~20–40 min):
  python3 -u computations/probes/qbeta_3bp8_w2_direct_sheet_probe.py \
      2>&1 | tee /tmp/qbeta_3bp8_w2.log
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

from _awpk_fast_index import eval_I41_at  # noqa: E402
from qbeta_g3_fourone_index_assembly_corrected import e2_window_for  # noqa: E402
from qbeta_t4_anchors import theta_t4, S_ANCHORS  # noqa: E402

set_compute_dps()

E_SUM = 64            # winding window: at |w| = q₀² the terms peak O(30)
                      # near e ≈ 30–40 and fall below 1e-10 by e ≈ 55–60
                      # (I(0,60)·q₀^{120} ≈ 5.6e-11); E = 64 adds margin.
TOWER_REF = mp.mpf("0.42764420131745803633")   # honest w=1 tower (13d, #4433/g3)
# T4 sheets — DERIVED from the canonical q₀ (bean qou-vbw1), not typed. The
# former 8-digit literals 0.05894648 / 0.20323503 were inverted at a q₀ that
# was a unit conflation (h = q₀ − 1/q₀ read as 2·ln q₀). Still A_ω-conditioned.
THETA_MUON = theta_t4("muon")
THETA_PROTON = theta_t4("proton")
S_MUON = mp.mpf(S_ANCHORS["muon"])
S_PROTON = mp.mpf(S_ANCHORS["proton"])


def ord_for(e: int) -> int:
    """Internal x-order for I(0,e): past the lead (≈ T(⌈e/2⌉) q̃-orders) the
    series needs ~600 more q̃-orders to converge; ladder-certified below."""
    lead = ((abs(e) + 1) // 2) * (((abs(e) + 1) // 2) + 1) // 2
    # floor 2400: small-e values need x-order ~2400 for >=13-digit agreement
    # against order-400 (the 1600-vs-1200 ladder gives only ~7 digits; the
    # first W2 run tripped its own >=8-digit assertion on e=0,3 this way
    # while the values were already known good to 26+ digits from #4433).
    return max(2400, 2 * (lead + 700) + 200)


def main() -> int:
    q0 = q_at(50)
    q = 1 / q0
    x = mp.sqrt(q)
    print("=" * 78)
    print(" qou-3bp8 W2 — A_eff at the corpus sheet by DIRECT summation (entire GF)")
    print("=" * 78)

    # ---- W2a: per-winding values with ladder certification ----
    print(f"\n[W2a] I(0,e)(q̃), e = 0..{E_SUM}, adaptive internal order:")
    vals = {}
    digits = {}
    t0 = time.time()
    for e in range(0, E_SUM + 1):
        od = ord_for(e)
        v1 = eval_I41_at(0, e, x, od, e2_window_for(od, 0, e))
        od2 = od - 400
        v2 = eval_I41_at(0, e, x, od2, e2_window_for(od2, 0, e))
        d = abs(v1 - v2)
        dg = 40 if d == 0 else (int(-mp.log10(d)) if d < 1 else 0)
        vals[e] = v1
        digits[e] = dg
        if e % 8 == 0 or e == E_SUM:
            print(f"    e={e:>2}: {mp.nstr(v1, 12):>20}  [{dg:>2} agree-digits, "
                  f"ord {od}]  [{time.time()-t0:6.0f}s]")
    conv_ok = min(digits.values()) >= 8

    # ---- W2b: sheet evaluations ----
    sheets = {"muon": THETA_MUON, "proton": THETA_PROTON}
    conventions = {
        "q0_e_itheta": lambda th: q0 * mp.e ** (1j * th),
        "q0sq_e_2itheta": lambda th: (q0 ** 2) * mp.e ** (2j * th),
    }
    print(f"\n[W2b] A_eff(𝔲) = Σ_(|e|≤{E_SUM}) I(0,e)·wᵉ at the T4 sheets:")
    results = {}
    tails = {}
    for cname, wfun in conventions.items():
        results[cname] = {}
        tails[cname] = {}
        for aname, th in sheets.items():
            w = wfun(th)
            val = vals[0] + mp.fsum(
                vals[e] * (w ** e + w ** (-e)) for e in range(1, E_SUM + 1))
            tail = abs(vals[E_SUM]) * (abs(w) ** E_SUM + abs(w) ** (-E_SUM))
            results[cname][aname] = val
            tails[cname][aname] = tail
            print(f"    {cname:>15} {aname:>7}: Re = {mp.nstr(mp.re(val), 12):>16}  "
                  f"Im = {mp.nstr(mp.im(val), 12):>16}  |tail| ≈ {mp.nstr(tail, 2)}")

    ratio_obs = S_PROTON / S_MUON
    tests = {}
    for cname in conventions:
        im_mu = mp.im(results[cname]["muon"])
        im_pr = mp.im(results[cname]["proton"])
        re_mu = mp.re(results[cname]["muon"])
        re_pr = mp.re(results[cname]["proton"])
        flip = (im_mu > 0 > im_pr) or (im_pr > 0 > im_mu)
        tests[cname] = {
            "im_ratio_p_over_mu": mp.nstr(im_pr / im_mu, 10) if im_mu != 0 else "inf",
            "sign_flip_im": bool(flip),
            "abs_dev_from_tower_muon": mp.nstr(abs(results[cname]["muon"]) / TOWER_REF, 10),
            "abs_dev_from_tower_proton": mp.nstr(abs(results[cname]["proton"]) / TOWER_REF, 10),
            "re_ratio_p_over_mu": mp.nstr(re_pr / re_mu, 10) if re_mu != 0 else "inf",
        }
        print(f"    (iii) {cname}: Im-ratio p/μ = {tests[cname]['im_ratio_p_over_mu']} "
              f"(observed S_p/S_μ = {mp.nstr(ratio_obs, 8)}); sign flip: "
              f"{tests[cname]['sign_flip_im']}")

    # w = 1 cross-check against the honest tower value
    w1_val = vals[0] + 2 * mp.fsum(vals[e] for e in range(1, E_SUM + 1))
    w1_dev = abs(w1_val - TOWER_REF)
    print(f"\n    w=1 cross-check: Σ = {mp.nstr(w1_val, 15)} vs tower "
          f"{mp.nstr(TOWER_REF, 15)} (|Δ| = {mp.nstr(w1_dev, 3)})")
    w1_ok = w1_dev < mp.mpf("1e-10")

    verdict = (
        "W2 COMPLETE: the corpus-sheet effective winding Stokes coefficient "
        "computed by DIRECT two-sided summation (entire GF, no continuation). "
        "All comparisons parameter-free and recorded as-is; nothing wired. "
        "Interpretation in the audit doc."
        if (conv_ok and w1_ok) else
        "W2 INCONCLUSIVE — a certification failed; inspect the log.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-3bp8-w2-direct-sheet", engine="python-int+mpmath")
    wb.set_description(
        "W2 of qou-3bp8: effective winding-refined Stokes coefficient of 4_1 "
        "at the corpus sheets, by DIRECT two-sided summation — justified by "
        "the entirety result (Lean summable_winding_of_sq_dominated; measured "
        "super-exponential decay past the pre-asymptotic hump). Supersedes "
        "the #4433 'outside the annulus' framing (pre-asymptotic artifact). "
        "Per-winding ladder certification, w=1 tower cross-check, and the "
        "parameter-free qou-awpk tests (deviation from constant, Im sign "
        "structure, ratio vs S_p/S_mu = -4.0751). Nothing fitted or wired; "
        "sigma1sigma1 channel; exact-int + mpmath only. Scope-(a).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("per_winding_values", {str(e): mp.nstr(vals[e], 20) for e in vals})
    wb.add_data("per_winding_agree_digits", {str(e): digits[e] for e in digits})
    wb.add_data("sheet_results", {
        c: {a: {"re": mp.nstr(mp.re(results[c][a]), 16),
                "im": mp.nstr(mp.im(results[c][a]), 16),
                "tail_bound": mp.nstr(tails[c][a], 3)} for a in sheets}
        for c in conventions})
    wb.add_data("tests", tests)
    wb.add_data("observed_ratio", mp.nstr(ratio_obs, 10))
    wb.add_data("w1_crosscheck", {"sum": mp.nstr(w1_val, 20),
                                  "tower_ref": mp.nstr(TOWER_REF, 20),
                                  "abs_diff": mp.nstr(w1_dev, 4)})
    wb.add_data("t4_inputs_not_refit", {
        "theta_muon": mp.nstr(THETA_MUON, 10), "theta_proton": mp.nstr(THETA_PROTON, 10),
        "S_muon": mp.nstr(S_MUON, 10), "S_proton": mp.nstr(S_PROTON, 10)})
    wb.add_data("verdict", verdict)
    wb.add_assertion("per_winding_ladder_converged",
                     computed=1.0 if conv_ok else 0.0, expected=1.0, tolerance=0.5,
                     source=f"every I(0,e), e<={E_SUM}, agrees to >=8 digits "
                            f"between adaptive order and order-400")
    wb.add_assertion("w1_matches_honest_tower",
                     computed=1.0 if w1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="two-sided sum at w=1 matches the honest deep tower "
                            "0.42764420131745803633 to <=1e-10")
    wb.save()
    print("  witness -> computations/probes/qbeta-3bp8-w2-direct-sheet.witness.json")
    return 0 if (conv_ok and w1_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
