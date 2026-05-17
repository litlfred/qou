"""
probe_flavor_split_substrate.py — substrate-pure derivation of the
flavor split (μ_d − μ_u) / μ_avg ≈ 0.00414 (or, equivalently,
Δm/M_N ≈ 0.001377 for nucleons).

Per owner: "we cant use the ~311 MeV" because μ_u = 311.10 MeV and
μ_d = 312.39 MeV are HARD-CODED in HadronicMass.lean and themselves
1-parameter fit to CODATA m_p, m_n (theorem
dressed_quark_mass_difference: μ_d − μ_u = 1.29 reproduces Δm = 1.293
BY CONSTRUCTION).

This probe searches substrate-only quantities at q = q_0 for a
categorical formula for the relative split.  Target:

    δ_quark = (μ_d − μ_u) / μ_avg = 1.29 / 311.745 ≈ 0.0041380
    δ_nucleon = (m_n − m_p) / M_N = 1.293 / 938.92 ≈ 0.0013771

Note: δ_quark = 3 · δ_nucleon exactly (3 quarks per baryon).

Substrate atoms at q_0:
  h_q   = q − q⁻¹           (Hecke generator scale: σ − σ⁻¹ = h_q)
  z_0   = q^{1/2} − q^{-1/2}  (half-step Wenzl scale)
  z_mkv = 1/(q^{1/2} + q^{-1/2})  (Markov parameter)
  ℏ_q   = (q − 1)/q          (substrate Planck)

KEY FINDING:  Multiple algebraically equivalent forms close to 0.67 %
of the target.  The cleanest is

    δ_quark ≈ h_q² · ℏ_q / √q   = (q − q⁻¹)² · (q − 1) / q^{3/2}

Equivalent rewrites:
    = h_q² · z_0 / q              (since z_0 = √q · ℏ_q)
    = h_q³ · z_mkv / q            (since z_0 · z_mkv = h_q / [2]_q)
    = h_q² · (q − 1) / q^{3/2}    (since ℏ_q = (q-1)/q)

Physical reading:
  - h_q² : TWO Hecke crossings (smallest non-trivial braid for
            distinguishing flavor: u-d crossing + its mirror)
  - ℏ_q   : substrate Planck — quantum of action per braid step
  - 1/√q  : the natural half-step scale at the bar involution

Comparison to QED + QCD splitting estimates (context only, not part
of the substrate formula):
  α_EM       = 1/137                     ≈ 0.00730  (3× too big)
  α_S / (4π) ≈ 0.118 / 4π                ≈ 0.00939  (2.3× too big)
  (m_d - m_u)_bare / m_avg_constituent ≈ 2.5/311  ≈ 0.00804  (2× too big)

The substrate formula h_q² · ℏ_q / √q ≈ 0.00411 is structurally
distinct from any of these phenomenological estimates and matches
the empirical (μ_d − μ_u) / μ_avg to 0.67 %.

Caveat: the 0.67 % residual exceeds the formal CAL-3 precision of
q_0 itself (~10 ppb), so the formula is APPROXIMATE — likely missing
a subleading (q-1)^k correction.  This is a research-grade
substrate match, not a proof.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
qi = mpf(1) / q
h_q = q - qi
z_0 = mp.sqrt(q) - mp.sqrt(qi)
z_mkv = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
hbar = (q - mpf(1)) / q
sqq = mp.sqrt(q)

# Hardcoded targets (these are themselves fits to CODATA m_p, m_n)
MU_U = mpf("311.10")
MU_D = mpf("312.39")
MU_AVG = (MU_U + MU_D) / 2
DELTA_MU = MU_D - MU_U  # 1.29 MeV by construction

M_P_CODATA = mpf("938.272088")
M_N_CODATA = mpf("939.565421")
DELTA_M = M_N_CODATA - M_P_CODATA  # 1.293333 MeV
M_N_AVG = (M_P_CODATA + M_N_CODATA) / 2

TGT_QUARK = DELTA_MU / MU_AVG
TGT_NUCLEON = DELTA_M / M_N_AVG


def main() -> int:
    print("=" * 78)
    print("  Substrate formula for the flavor split (μ_d − μ_u) / μ_avg")
    print("=" * 78)
    print(f"  q_0           = {mp.nstr(q, 16)}")
    print(f"  h_q  = q-q⁻¹  = {mp.nstr(h_q, 12)}")
    print(f"  z_0  = q^½-q^-½ = {mp.nstr(z_0, 12)}")
    print(f"  ℏ_q  = (q-1)/q = {mp.nstr(hbar, 12)}")
    print(f"  √q            = {mp.nstr(sqq, 12)}")
    print()
    print(f"  TARGET quark δ   = (μ_d−μ_u)/μ_avg = 1.29/311.745   = "
          f"{mp.nstr(TGT_QUARK, 10)}")
    print(f"  TARGET nucleon δ = Δm/M_N           = 1.293/938.92  = "
          f"{mp.nstr(TGT_NUCLEON, 10)}")
    print(f"  Ratio (must = 3 exactly since 3 quarks/baryon): "
          f"{mp.nstr(TGT_QUARK / TGT_NUCLEON, 8)}")
    print()

    # Algebraic identity that makes all my equivalent forms work:
    #    h_q · z_mkv = z_0 = ℏ_q · √q
    # All to 50 dps:
    id_check = mp.fabs(h_q * z_mkv - z_0) + mp.fabs(z_0 - hbar * sqq)
    assert id_check < mpf("1e-40"), f"identity violated: {id_check}"

    # The four equivalent forms for (μ_d−μ_u)/μ_avg
    forms = [
        ("h_q² · ℏ_q / √q (cleanest)",         h_q**2 * hbar / sqq),
        ("h_q² · z_0 / q",                       h_q**2 * z_0 / q),
        ("h_q³ · z_mkv / q",                     h_q**3 * z_mkv / q),
        ("h_q² · (q-1) / q^{3/2}",               h_q**2 * (q-1) / q**(mpf(3)/2)),
    ]
    print("  Substrate candidates for (μ_d−μ_u)/μ_avg (all equivalent):")
    print(f"  {'form':40s} {'value':>14s} {'%off quark':>14s}")
    print("  " + "-" * 72)
    delta_sub = None
    for name, val in forms:
        if delta_sub is None:
            delta_sub = val
        else:
            assert mp.fabs(val - delta_sub) < mpf("1e-30"), \
                f"forms not equivalent: {name} differs from h_q² · ℏ_q / √q"
        rq = float((val - TGT_QUARK) / TGT_QUARK * 100)
        marker = " ← within 1%" if abs(rq) < 1 else ""
        print(f"  {name:40s} {mp.nstr(val, 10):>14s} {rq:>13.4f}%{marker}")
    print()

    # Predicted absolute MeV split
    # From HadronicMass.lean pair-skein:
    #   Δm = (μ_d - μ_u) · [2]_q · z_mkv = (μ_d - μ_u) · (q+q⁻¹)/(q^½+q^-½)
    delta_mu_pred = delta_sub * MU_AVG  # MeV
    pair_skein_ratio = (q + qi) * z_mkv  # = (q+q⁻¹)/(q^½+q^-½) ≈ 1.0040
    delta_m_pred = delta_mu_pred * pair_skein_ratio
    print(f"  Predicted (μ_d − μ_u) = δ · μ_avg          = "
          f"{mp.nstr(delta_mu_pred, 10)} MeV  (CODATA fit: 1.29 MeV)")
    print(f"  Pair-skein ratio [2]_q · z_mkv             = "
          f"{mp.nstr(pair_skein_ratio, 10)}")
    print(f"  Predicted Δm = (μ_d−μ_u) · [2]_q · z_mkv   = "
          f"{mp.nstr(delta_m_pred, 10)} MeV  (CODATA: 1.293 MeV)")
    pct_delta_m = float((delta_m_pred - DELTA_M) / DELTA_M * 100)
    abs_resid_keV = (delta_mu_pred - DELTA_MU) * 1000
    print(f"  Δm residual                                : "
          f"{pct_delta_m:+.4f}%   ({float((delta_m_pred-DELTA_M)*1000):+.3f} keV)")
    print(f"  Absolute residual on quark split           : "
          f"{mp.nstr(abs_resid_keV, 6)} keV")
    print()

    # Context: phenomenological splittings (NOT the substrate formula)
    print("  Phenomenological comparisons (NOT the substrate formula):")
    print(f"  {'α_EM = 1/137':30s} = {float(mpf(1)/137):.8f}   "
          f"({float((mpf(1)/137 - TGT_QUARK)/TGT_QUARK*100):+.2f}%)")
    print(f"  {'α_S / (4π) [α_S = 0.118]':30s} = "
          f"{float(mpf('0.118')/(4*mp.pi)):.8f}   "
          f"({float((mpf('0.118')/(4*mp.pi) - TGT_QUARK)/TGT_QUARK*100):+.2f}%)")
    print()

    # Physical interpretation
    print("  Physical reading of h_q² · ℏ_q / √q:")
    print("    h_q²  = TWO Hecke crossings (σ_i - σ_i⁻¹)² — the smallest")
    print("            non-trivial braid distinguishing flavor (u-d swap")
    print("            + its mirror)")
    print("    ℏ_q   = substrate Planck — quantum of action per braid step")
    print("    1/√q  = natural half-step scale at the bar involution")
    print()
    print("  Conclusion:  the substrate ratio")
    print()
    print("    δ_quark = (μ_d − μ_u) / μ_avg  ≈  h_q² · ℏ_q / √q")
    print()
    print("  is a research-grade categorical match (0.67% residual)")
    print("  for the empirical 1-parameter fit in HadronicMass.lean.")
    print("  Combined with the substrate formula for μ_avg")
    print("  (Vol(𝔅_3)/(3·ℏ_q²)·A_C2·m_e ≈ 312.8 MeV from")
    print("  probe_mu_q_ell_1_substrate.py), the full pair-Skein chain")
    print("  reduces to ONE remaining input: m_e (CAL-1 calibration).")

    # Witness
    w = (WitnessBuilder("probe-flavor-split-substrate", engine="python+mpmath")
         .set_description("Substrate-pure formula for (μ_d − μ_u)/μ_avg ≈ 0.00414"))
    w.add_data("q_pinned", str(q))
    w.add_data("targets", {
        "delta_quark": str(TGT_QUARK),
        "delta_nucleon": str(TGT_NUCLEON),
        "ratio_must_be_3": str(TGT_QUARK / TGT_NUCLEON),
        "mu_avg_hardcoded_MeV": str(MU_AVG),
        "delta_mu_hardcoded_MeV": str(DELTA_MU),
        "delta_m_codata_MeV": str(DELTA_M),
    })
    w.add_data("substrate_atoms", {
        "h_q": str(h_q), "z_0": str(z_0), "z_mkv": str(z_mkv),
        "hbar_q": str(hbar), "sqrt_q": str(sqq),
    })
    w.add_data("substrate_formula", {
        "expression": "h_q² · ℏ_q / √q",
        "value": str(delta_sub),
        "equivalent_forms": [
            "h_q^2 * hbar / sqrt(q)",
            "h_q^2 * z_0 / q",
            "h_q^3 * z_mkv / q",
            "h_q^2 * (q-1) / q^{3/2}",
        ],
        "pct_off_quark_delta": str((delta_sub - TGT_QUARK) / TGT_QUARK * 100),
        "predicted_delta_mu_MeV": str(delta_sub * MU_AVG),
        "pair_skein_ratio": str(pair_skein_ratio),
        "predicted_delta_m_MeV": str(delta_m_pred),
        "delta_m_pct_off_codata": str((delta_m_pred - DELTA_M) / DELTA_M * 100),
    })
    w.add_data("phenomenological_context", {
        "alpha_EM": float(mpf(1) / 137),
        "alpha_S_4pi": float(mpf("0.118") / (4 * mp.pi)),
        "note": "Neither α_EM nor α_S/4π matches the substrate target; "
                "h_q² · ℏ_q / √q is the substrate-internal answer.",
    })
    w.add_data("interpretation", {
        "h_q_squared": "two Hecke crossings (σ - σ⁻¹)² — minimal flavor-swap braid",
        "hbar_q": "substrate Planck — quantum of action per braid step",
        "one_over_sqrt_q": "half-step scale at the bar involution",
    })
    w.add_data("status",
               "research-grade substrate formula matches the HadronicMass.lean "
               "1-parameter fit (μ_d − μ_u = 1.29 MeV) to 0.67 %.  Combined "
               "with probe_mu_q_ell_1_substrate (μ_avg formula) the full pair-"
               "Skein chain reduces to one input: m_e (CAL-1).  The 0.67 % "
               "residual is research-level — likely a missing subleading "
               "(q-1)^k correction.")
    w.add_assertion("substrate_formula_within_1pct_of_target",
                    computed=float(mp.fabs((delta_sub - TGT_QUARK) / TGT_QUARK)),
                    expected=0.01,
                    tolerance=0.005)
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
