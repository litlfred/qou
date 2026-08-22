#!/usr/bin/env python3
"""Probe: λ_scale substrate form `5/2 − h²·G + O(h^4)`.

Tests the hypothesis that the Borromean baryon λ_scale (≈2.4599534)
has the substrate form `p(4)/2 − h²·Vol(B_3)/8 + O(h^4)` where
p(4) = 5 is the partition count at level n=4.

Probes:
  1. Confirm 5/2 − h²·G match at 5.6 ppm for proton.
  2. Test the neutron: same form with same constants?
  3. Solve for the h^4 coefficient from the residual.
  4. Test the **generation prediction** at the Σ baryon
     (m_Σ ≈ 1189-1197 MeV): does p(5)/2 = 7/2 fit?
  5. Try alternative leading rationals near 2.46:
     49/20, p(n)/k for various n, k.
  6. Try the Skein-correction interpretation:
     λ_p · Vol(B_3)/ℏ_q² + S(p) = m_p/m_e → solve for S(p).

Emits witness for downstream review.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import M_K_PM_MEV_VALIDATION, M_MU_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

mp.mp.dps = 80

# Substrate constants
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
Q = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
H = Q - mp.mpf(1) / Q
HBAR_Q = (Q - mp.mpf(1)) / Q
G = mp.catalan
# Exact closed form Vol(𝓑₃) = 8·G (PR #843).  Retained `VOL_B3_LIT`
# alias for back-compat with downstream consumers, now derived from
# the exact form rather than the Adams 1985 truncated literal
# (CAL-4 audit, 2026-05-22).
VOL_B3_FROM_G = 8 * G
VOL_B3_LIT = VOL_B3_FROM_G
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 33 digits, correct to 29 (qou-ckbv)
VOL_41 = 2 * mp.clsin(2, mp.pi / 3)

# CODATA validation (CAL-1: m_e MeV; comparison only)
from experimental_constants import M_E_MEV as _M_E_MEV  # noqa: E402
M_E = mp.mpf(repr(_M_E_MEV))
from experimental_constants import M_P_MEV as _M_P_MEV  # noqa: E402
M_P = mp.mpf(repr(_M_P_MEV))
from experimental_constants import Q_NEUTRON_MEV as _Q_NEUTRON_MEV  # noqa: E402
M_N = M_P + mp.mpf(repr(_Q_NEUTRON_MEV)) + M_E  # m_n derived via 3-input scheme
# Σ baryons (PDG):
M_SIGMA_PLUS = mp.mpf("1189.37")
M_SIGMA_0 = mp.mpf("1192.642")
M_SIGMA_MINUS = mp.mpf("1197.449")
M_LAMBDA = mp.mpf("1115.683")
# Mesons (for cross-checks if needed)
M_PION = mp.mpf(M_PI_PM_MEV_VALIDATION)
M_K = mp.mpf(M_K_PM_MEV_VALIDATION)

# Targets
LAM_P = (M_P / M_E) * HBAR_Q**2 / VOL_B3_LIT
LAM_N = (M_N / M_E) * HBAR_Q**2 / VOL_B3_LIT
LAM_SIGMA_PLUS = (M_SIGMA_PLUS / M_E) * HBAR_Q**2 / VOL_B3_LIT
LAM_SIGMA_0 = (M_SIGMA_0 / M_E) * HBAR_Q**2 / VOL_B3_LIT
LAM_LAMBDA = (M_LAMBDA / M_E) * HBAR_Q**2 / VOL_B3_LIT


def ppm(x, ref):
    return float((x - ref) / ref * mp.mpf("1e6"))


def main() -> int:
    w = WitnessBuilder("lambda-scale-substrate-probe", engine="mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Probe of the substrate-form hypothesis λ_scale = p(4)/2 − h²·G + "
        "O(h^4) for the Borromean baryon mass formula. Tests proton, "
        "neutron, Σ baryons, Λ baryon at MPFR 80 dps. Verifies the 5.6 "
        "ppm match for proton; solves for higher-order corrections; "
        "tests generation predictions (p(n)/2 for n=4,5,6); checks "
        "Skein S(B) interpretation. NO FITTING — all targets are "
        "computed from CODATA via the Borromean formula."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("q_0", mp.nstr(Q, 25))
    w.add_parameter("h", mp.nstr(H, 25))
    w.add_parameter("G_catalan", mp.nstr(G, 25))
    w.add_parameter("Vol_B3_literature", mp.nstr(VOL_B3_LIT, 25))
    w.add_parameter("Vol_B3_from_8G", mp.nstr(VOL_B3_FROM_G, 25))

    # ── Probe 1: 5/2 − h²·G match for proton ──────────────────
    form_5_2 = mp.mpf(5) / 2 - H**2 * G
    p1 = {
        "lambda_p_target": mp.nstr(LAM_P, 25),
        "5/2 - h²·G": mp.nstr(form_5_2, 25),
        "diff_absolute": mp.nstr(form_5_2 - LAM_P, 15),
        "diff_ppm": ppm(form_5_2, LAM_P),
    }
    w.add_data("probe_1_5_2_minus_h2_G_proton", p1)
    w.add_assertion("probe_1_proton_within_10ppm", computed=abs(p1["diff_ppm"]),
                    expected=0.0, tolerance=10.0, unit="ppm",
                    source="5/2 − h²·G vs λ_p_target")

    # ── Probe 2: Same form for neutron ────────────────────────
    # Hypothesis: neutron has the SAME 5/2 − h²·G but different S(B) Skein
    form_5_2_for_n = mp.mpf(5) / 2 - H**2 * G  # same value
    # If λ_n = 5/2 − h²·G + ΔS(n)·ℏ_q²/Vol(B_3), solve for ΔS:
    delta_S_n = (LAM_N - form_5_2_for_n) * VOL_B3_LIT / HBAR_Q**2
    p2 = {
        "lambda_n_target": mp.nstr(LAM_N, 25),
        "5/2 - h²·G (same as proton)": mp.nstr(form_5_2_for_n, 25),
        "Δ in λ (n - common form)": mp.nstr(LAM_N - form_5_2_for_n, 15),
        "ΔS(n) implied (× m_e MeV)": mp.nstr(delta_S_n * M_E, 8) + " MeV",
        "interpretation": (
            "If λ has common substrate value 5/2 − h²·G + small, "
            "the p/n split lives in S(B) Skein. ΔS(n) - ΔS(p) "
            "should equal the Δm_pn ≈ 1.293 MeV / m_e."
        ),
    }
    w.add_data("probe_2_neutron_common_form", p2)

    # ── Probe 3: Solve h^4 coefficient from residual ──────────
    # Ansatz: λ_p = 5/2 - h²·G - h^4·c4 + O(h^6)
    c4 = -(LAM_P - mp.mpf(5)/2 + H**2 * G) / H**4
    p3 = {
        "ansatz": "λ_p = 5/2 - h²·G - h^4·c4 + O(h^6)",
        "c4_solved": mp.nstr(c4, 15),
        "c4_simple_candidates": {
            "G/2": mp.nstr(G/2, 8),
            "G/h": mp.nstr(G/H, 8),
            "[2]_q²·G / 8": mp.nstr((Q + 1/Q)**2 * G / 8, 8),
            "(1+G)/2": mp.nstr((1 + G)/2, 8),
        },
        "interpretation": (
            f"c4 = {float(c4):+.6f}. Compare to simple candidates: "
            "if c4 ≈ G, then λ_p ≈ 5/2 − h²·G − h^4·G + O(h^6) = "
            "5/2 − G·(h² + h^4 + ...) ≈ 5/2 − G·h²/(1−h²)."
        ),
    }
    w.add_data("probe_3_h4_correction", p3)

    # ── Probe 3b: Test 5/2 − G·h²/(1−h²) ──────────────────────
    form_geometric_h2 = mp.mpf(5)/2 - G * H**2 / (1 - H**2)
    p3b = {
        "form": "5/2 − G·h²/(1−h²)  (geometric series)",
        "value": mp.nstr(form_geometric_h2, 25),
        "diff_ppm": ppm(form_geometric_h2, LAM_P),
    }
    w.add_data("probe_3b_geometric_series", p3b)

    # ── Probe 4: Generation prediction at Σ baryons ───────────
    # Hypothesis: λ_Σ = p(5)/2 − h²·G' + O(h^4) with p(5) = 7
    # Predicted λ_Σ = 7/2 − h²·G = 3.5 - 0.040 = 3.460
    lam_sigma_pred_7over2 = mp.mpf(7)/2 - H**2 * G
    # Vs. observed:
    mass_pred_sigma = lam_sigma_pred_7over2 * VOL_B3_LIT / HBAR_Q**2 * M_E
    p4 = {
        "hypothesis": "λ_Σ = 7/2 − h²·G (2nd-generation prediction)",
        "lam_sigma_predicted": mp.nstr(lam_sigma_pred_7over2, 12),
        "lam_sigma_plus_target": mp.nstr(LAM_SIGMA_PLUS, 12),
        "lam_sigma_0_target": mp.nstr(LAM_SIGMA_0, 12),
        "lam_lambda_target": mp.nstr(LAM_LAMBDA, 12),
        "mass_predicted_MeV": mp.nstr(mass_pred_sigma, 8),
        "mass_sigma_plus_codata_MeV": mp.nstr(M_SIGMA_PLUS, 8),
        "mass_sigma_0_codata_MeV": mp.nstr(M_SIGMA_0, 8),
        "ratio_pred_to_sigma_plus": float(mass_pred_sigma / M_SIGMA_PLUS),
        "ratio_pred_to_sigma_0": float(mass_pred_sigma / M_SIGMA_0),
        "interpretation": (
            "If p(n)/2 generation hypothesis holds with p(5) = 7, "
            "λ_Σ_pred = 7/2 − h²·G = ~3.46. Observed Σ baryon λ values: "
            f"Σ+ → {float(LAM_SIGMA_PLUS):.4f}, Σ⁰ → {float(LAM_SIGMA_0):.4f}, "
            f"Λ → {float(LAM_LAMBDA):.4f}. Pattern fits IF λ_Σ is in the "
            "range 3.1 to 3.5; observed ~3.12 (Σ+), so prediction 3.46 "
            "is off by ~10%. Likely the generation hypothesis needs "
            "refinement OR Σ has additional Skein contribution."
        ),
    }
    w.add_data("probe_4_generation_sigma", p4)

    # ── Probe 5: Alternative leading rationals ────────────────
    # Test small denominators that give ≈ 2.5
    alternatives = []
    for num in range(1, 30):
        for den in range(1, 15):
            rat = mp.mpf(num) / den
            if abs(rat - mp.mpf("2.5")) < mp.mpf("0.05"):
                test = rat - H**2 * G
                diff_p = ppm(test, LAM_P)
                if abs(diff_p) < 100:
                    alternatives.append({
                        "leading": f"{num}/{den}",
                        "value": float(rat),
                        "test_with_h2G": mp.nstr(test, 12),
                        "diff_p_ppm": diff_p,
                    })
    p5 = {
        "search": "leading rational L close to 5/2, test L − h²·G vs λ_p",
        "matches_within_100ppm": alternatives[:5],
    }
    w.add_data("probe_5_alternative_rationals", p5)

    # ── Probe 6: Vol(B_3) = 8G hypothesis at higher precision ─
    # If Vol(B_3) IS exactly 8G, the formula closes via this identity
    p6 = {
        "Vol_B3_literature": mp.nstr(VOL_B3_LIT, 25),
        "8G_catalan": mp.nstr(8 * G, 25),
        "difference": mp.nstr(VOL_B3_LIT - 8*G, 12),
        "rel_diff_ppm": ppm(VOL_B3_LIT, 8*G),
        "note": (
            "If Vol(B_3) = 8G exactly, the formula `λ = 5/2 − h²·G` "
            "becomes `λ = 5/2 − h²·Vol(B_3)/8`. The numerical values "
            "differ at the 7th decimal — likely the literature value's "
            "precision floor, not a structural difference. SnapPy "
            "high-precision computation would clarify."
        ),
    }
    w.add_data("probe_6_Vol_B3_vs_8G", p6)

    # ── Probe 7: Try the muon (CAL-2 sanity) ──────────────────
    # For muon: m_μ/m_e = Vol(4_1)/ℏ_q² (no λ_scale, no Skein)
    # If we forced the same formula structure:
    lam_mu_implied = (mp.mpf(M_MU_MEV_VALIDATION) / M_E) * HBAR_Q**2 / VOL_41
    p7 = {
        "muon_check": "m_μ/m_e = Vol(4_1)/ℏ_q² × λ_μ + S(μ)",
        "lambda_mu_target": mp.nstr(lam_mu_implied, 25),
        "should_be_unity": "yes (CAL-2 anchor)",
        "5/2 - h²·G test for muon": mp.nstr(mp.mpf(5)/2 - H**2 * G, 12),
        "interpretation": (
            "The muon has λ ≈ 1 by CAL-2 (definition of q_0). The Borromean "
            "formula does not apply to leptons; this is a sanity check that "
            "the 5/2 − h²·G value is NOT universal — it's specific to baryons "
            "with B_3 topology."
        ),
    }
    w.add_data("probe_7_muon_sanity", p7)

    w.add_caveat(
        "Probe-only — does not modify production compute paths. "
        "Findings inform the open R&D on λ_scale substrate derivation."
    )

    out = w.save()
    print(f"Witness emitted: {out.name}")
    print()
    print("Summary:")
    print(f"  λ_p target           = {float(LAM_P):.10f}")
    print(f"  5/2 − h²·G           = {float(form_5_2):.10f}  ({ppm(form_5_2, LAM_P):+.2f} ppm)")
    print(f"  5/2 − G·h²/(1-h²)    = {float(form_geometric_h2):.10f}  ({ppm(form_geometric_h2, LAM_P):+.2f} ppm)")
    print(f"  c4 (h^4 coeff)       = {float(c4):+.6f}")
    print(f"  Compare G ≈ 0.91597, G/2 ≈ 0.45798")
    print()
    print(f"  λ_n target           = {float(LAM_N):.10f}")
    print(f"  λ_Σ+ target          = {float(LAM_SIGMA_PLUS):.10f}  (prediction p(5)/2 − h²·G = {float(lam_sigma_pred_7over2):.4f})")
    print(f"  λ_Σ⁰ target          = {float(LAM_SIGMA_0):.10f}")
    print(f"  λ_Λ target           = {float(LAM_LAMBDA):.10f}")
    print()
    print(f"  Vol(B_3) vs 8G       = {float(VOL_B3_LIT):.10f} vs {float(8*G):.10f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
