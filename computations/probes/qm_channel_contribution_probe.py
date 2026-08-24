"""Q_m channel contribution to the Higgs categorical mass formula — Path C.

Background.
  PR #1159 constructed the Higgs categorical mass formula:
     m_H = m_W · (P_4(h)/P_2(h)) · (6/5) · (1 - h^4 · 2G)
  using only P_m (bar-symmetric Markov-trace component).
  Empirical match: -0.67% from W anchor, +0.44% from Z anchor.
  Residual ~0.5% per anchor.

  PR #1181 proved the Pythagorean identity:
     P_m^2 - Q_m^2 = 1/[2]_q^2
  for ALL m, where Q_m = sinh((2m+1)η)/(2 cosh η) is the bar-anti-
  symmetric companion.

  PR #1153 claimed Q_m/P_m = tanh((2m+1)η_0) is the "EM-channel ratio":
     W (m=2): tanh(5η_0) ≈ 0.478
     Z (m=3): tanh(7η_0) ≈ 0.622
     H (m=4): tanh(9η_0) ≈ 0.734

  Path C from the residual audit:
     "if the 'true' mass formula uses BOTH P_m and Q_m components
      (not just P_m), then the residual ~0.5% might come from the
      Q_m contribution"

This probe asks honestly: is there a STRUCTURAL augmentation of the
Higgs formula involving Q_m that closes the residual?

  Hypothesis H1 (Pythagorean modulus):
    m_K_true = m_e · sqrt(P_m^2 + Q_m^2) · factor
  Hypothesis H2 (linear combo):
    m_K_true = m_e · (P_m + α Q_m) · factor
  Hypothesis H3 (q-coefficient combo):
    m_K_true = m_e · (P_m · q^a + Q_m · q^b) · factor  for various a, b

For each hypothesis we compute:
  - W (m=2), Z (m=3), H (m=4) at substrate
  - check whether the SAME structural parameter (no free α) recovers
    BOTH the W/Z agreement AND closes the H residual

Honest framing.
  If no clean STRUCTURAL augmentation works, the answer is "Q_m
  contribution is NOT the source of the residual; it must be
  elsewhere (most likely the W/Z anchor asymmetry per Path A or
  the Yekutieli MI k=3 per Path B)."
  If a clean augmentation works, that's the seed for a follow-up
  derivation (NOT a fit — needs categorical justification, like the
  Pythagorean identity itself).
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
del _sys, _Path, _bridge
import json, subprocess
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, log as mplog, tanh as mptanh, cosh as mpcosh, sinh as mpsinh, sqrt as mpsqrt

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main():
    print("=" * 80)
    print("Q_m channel contribution to the Higgs mass formula — Path C analysis")
    print("=" * 80)
    print()

    # Substrate parameters (50-dps, canonical pin)
    q_0 = mpf(Q_50_DIGIT_STR)
    eta_0 = mplog(q_0)
    h_0 = q_0 - 1 / q_0
    cosh_eta = mpcosh(eta_0)
    bracket_2q = 2 * cosh_eta  # [2]_q at substrate

    # CODATA anchors (CAL-1, CAL-2, CAL-3 NOT crossed here; these are
    # external SM anchors used as inputs to the formula, not predictions)
    m_W = mpf("80.379")  # GeV (PDG)
    m_Z = mpf("91.1876")
    m_H_measured = mpf("125.10")

    print(f"  Substrate: q_0 = {q_0}, η_0 = {float(eta_0):.6f}, h_0 = {float(h_0):.6f}")
    print(f"  [2]_q = 2 cosh η_0 = {float(bracket_2q):.6f}")
    print()
    print(f"  SM anchors: m_W = {float(m_W)} GeV, m_Z = {float(m_Z)} GeV")
    print(f"  Measured m_H = {float(m_H_measured)} GeV")
    print()

    # P_m and Q_m at substrate
    def P_m(m):
        return mpcosh((2 * m + 1) * eta_0) / bracket_2q

    def Q_m(m):
        return mpsinh((2 * m + 1) * eta_0) / bracket_2q

    P = {m: P_m(m) for m in range(1, 6)}
    Q = {m: Q_m(m) for m in range(1, 6)}

    print("  Substrate values:")
    print(f"  {'m':>3}  {'P_m':>16}  {'Q_m':>16}  {'Q/P=tanh(...)':>16}  {'P²-Q²':>16}")
    for m in range(1, 6):
        ratio = Q[m] / P[m]
        pyth = P[m] ** 2 - Q[m] ** 2
        print(f"  {m:>3}  {float(P[m]):>16.10f}  {float(Q[m]):>16.10f}  "
              f"{float(ratio):>16.10f}  {float(pyth):>16.10f}")
    print(f"\n  Verifying Pythagorean: 1/[2]_q² = {float(1/bracket_2q**2):.10f}")
    print(f"  (should match P_m² − Q_m² for ALL m)")
    print()

    # Vol(B_3)/4 = 2G (Catalan) — for the h^4 correction
    G_catalan = mpf("0.91596559417721901505")
    vol_b3_over_4 = 2 * G_catalan

    # Current categorical Higgs formula (PR #1159) — using only P_m
    def higgs_from_W_P_only(h_subs=h_0):
        return m_W * (P[4] / P[2]) * mpf(6) / 5 * (1 - h_subs ** 4 * vol_b3_over_4)

    def higgs_from_Z_P_only(h_subs=h_0):
        return m_Z * (P[4] / P[3]) * mpf(6) / 5 * (1 - h_subs ** 4 * vol_b3_over_4)

    print("=" * 80)
    print("Current formula (P-only, PR #1159) — baseline residuals")
    print("=" * 80)
    print()
    m_H_W = higgs_from_W_P_only()
    m_H_Z = higgs_from_Z_P_only()
    dev_W = float((m_H_W - m_H_measured) / m_H_measured * 100)
    dev_Z = float((m_H_Z - m_H_measured) / m_H_measured * 100)
    print(f"  m_H from W anchor:  {float(m_H_W):.4f} GeV  (deviation: {dev_W:+.3f}%)")
    print(f"  m_H from Z anchor:  {float(m_H_Z):.4f} GeV  (deviation: {dev_Z:+.3f}%)")
    print(f"  W/Z asymmetry:      {float((m_H_Z - m_H_W) / m_H_W * 100):+.3f}%")
    print()

    # =====================================================================
    # Hypothesis H1 (Pythagorean modulus): replace P_m → sqrt(P_m² + Q_m²)
    # =====================================================================
    print("=" * 80)
    print("Hypothesis H1: replace P_m → R_m := sqrt(P_m² + Q_m²)")
    print("  (Pythagorean modulus — the 'full magnitude' of the P/Q complex)")
    print("=" * 80)
    print()

    def R_m(m):
        return mpsqrt(P[m] ** 2 + Q[m] ** 2)

    R = {m: R_m(m) for m in range(1, 6)}
    print(f"  R_m at substrate:")
    for m in range(1, 6):
        print(f"    R_{m} = {float(R[m]):.10f}    (P_{m} = {float(P[m]):.10f})")
    print()
    m_H_W_H1 = m_W * (R[4] / R[2]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    m_H_Z_H1 = m_Z * (R[4] / R[3]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    dev_W_H1 = float((m_H_W_H1 - m_H_measured) / m_H_measured * 100)
    dev_Z_H1 = float((m_H_Z_H1 - m_H_measured) / m_H_measured * 100)
    print(f"  m_H from W (H1):    {float(m_H_W_H1):.4f} GeV  ({dev_W_H1:+.3f}%)")
    print(f"  m_H from Z (H1):    {float(m_H_Z_H1):.4f} GeV  ({dev_Z_H1:+.3f}%)")
    print(f"  W/Z asymmetry:      {float((m_H_Z_H1 - m_H_W_H1) / m_H_W_H1 * 100):+.3f}%")
    print()

    # =====================================================================
    # Hypothesis H2 (linear combo with structural α = 1)
    # =====================================================================
    print("=" * 80)
    print("Hypothesis H2: replace P_m → P_m + Q_m  (= e^{(2m+1)η}/[2]_q)")
    print("  (Right-shift identity from PR #1185 P_plus_Q theorem)")
    print("=" * 80)
    print()

    def S_m(m):
        return P[m] + Q[m]  # = exp((2m+1)η_0) / [2]_q

    S = {m: S_m(m) for m in range(1, 6)}
    print(f"  S_m := P_m + Q_m = e^{{(2m+1)η_0}}/[2]_q at substrate:")
    for m in range(1, 6):
        print(f"    S_{m} = {float(S[m]):.10f}")
    print()
    m_H_W_H2 = m_W * (S[4] / S[2]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    m_H_Z_H2 = m_Z * (S[4] / S[3]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    dev_W_H2 = float((m_H_W_H2 - m_H_measured) / m_H_measured * 100)
    dev_Z_H2 = float((m_H_Z_H2 - m_H_measured) / m_H_measured * 100)
    print(f"  m_H from W (H2):    {float(m_H_W_H2):.4f} GeV  ({dev_W_H2:+.3f}%)")
    print(f"  m_H from Z (H2):    {float(m_H_Z_H2):.4f} GeV  ({dev_Z_H2:+.3f}%)")
    print()

    # =====================================================================
    # Hypothesis H3 (geometric mean: sqrt(P_m · (P_m+Q_m)))
    # =====================================================================
    print("=" * 80)
    print("Hypothesis H3: replace P_m → sqrt(P_m · S_m)  (geometric mean)")
    print("=" * 80)
    print()
    PSm = {m: mpsqrt(P[m] * S[m]) for m in range(1, 6)}
    print(f"  sqrt(P_m · S_m) at substrate:")
    for m in range(1, 6):
        print(f"    sqrt(P_{m}·S_{m}) = {float(PSm[m]):.10f}")
    print()
    m_H_W_H3 = m_W * (PSm[4] / PSm[2]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    m_H_Z_H3 = m_Z * (PSm[4] / PSm[3]) * mpf(6) / 5 * (1 - h_0 ** 4 * vol_b3_over_4)
    dev_W_H3 = float((m_H_W_H3 - m_H_measured) / m_H_measured * 100)
    dev_Z_H3 = float((m_H_Z_H3 - m_H_measured) / m_H_measured * 100)
    print(f"  m_H from W (H3):    {float(m_H_W_H3):.4f} GeV  ({dev_W_H3:+.3f}%)")
    print(f"  m_H from Z (H3):    {float(m_H_Z_H3):.4f} GeV  ({dev_Z_H3:+.3f}%)")
    print()

    # =====================================================================
    # Comparative summary + honest verdict
    # =====================================================================
    print("=" * 80)
    print("Comparative summary")
    print("=" * 80)
    print()
    print(f"  {'Hypothesis':<35} {'W-anchor':>12} {'Z-anchor':>12} {'W/Z gap':>10}")
    print(f"  {'-'*35} {'-'*12} {'-'*12} {'-'*10}")
    print(f"  {'baseline (P-only, PR #1159)':<35} {dev_W:>+11.3f}% {dev_Z:>+11.3f}% "
          f"{float((m_H_Z - m_H_W)/m_H_W*100):>+9.3f}%")
    print(f"  {'H1: P → sqrt(P²+Q²)':<35} {dev_W_H1:>+11.3f}% {dev_Z_H1:>+11.3f}% "
          f"{float((m_H_Z_H1 - m_H_W_H1)/m_H_W_H1*100):>+9.3f}%")
    print(f"  {'H2: P → P+Q':<35} {dev_W_H2:>+11.3f}% {dev_Z_H2:>+11.3f}% "
          f"{float((m_H_Z_H2 - m_H_W_H2)/m_H_W_H2*100):>+9.3f}%")
    print(f"  {'H3: P → sqrt(P·(P+Q))':<35} {dev_W_H3:>+11.3f}% {dev_Z_H3:>+11.3f}% "
          f"{float((m_H_Z_H3 - m_H_W_H3)/m_H_W_H3*100):>+9.3f}%")
    print()

    # Honest verdict logic
    print("=" * 80)
    print("Honest verdict")
    print("=" * 80)
    print()
    best_hyp = None
    best_max_dev = abs(max(dev_W, dev_Z, key=abs))
    for name, dvw, dvz in [
        ("H1 (Pythagorean modulus)", dev_W_H1, dev_Z_H1),
        ("H2 (linear sum P+Q)", dev_W_H2, dev_Z_H2),
        ("H3 (geometric mean)", dev_W_H3, dev_Z_H3),
    ]:
        max_dev = max(abs(dvw), abs(dvz))
        if max_dev < best_max_dev:
            best_max_dev = max_dev
            best_hyp = name
    if best_hyp is None:
        print(f"  ✗ NONE of H1/H2/H3 improves on the P-only baseline.")
        print(f"    Max baseline deviation: {abs(max(dev_W, dev_Z, key=abs)):.3f}%")
        print()
        print("  Implication: Q_m contribution is NOT the source of the residual.")
        print("  The Path C hypothesis (Higgs residual closure via Q_m) FAILS.")
        print("  The residual likely lives elsewhere — most plausibly the")
        print("  W/Z anchor asymmetry itself (Path A: substrate-derivation of v)")
        print("  or the Yekutieli MI k=3 tessellation (Path B).")
    else:
        print(f"  Best structural candidate: {best_hyp}")
        print(f"    Max deviation: {best_max_dev:.3f}% (vs baseline "
              f"{abs(max(dev_W, dev_Z, key=abs)):.3f}%)")
        print()
        if best_max_dev < 0.1:
            print(f"  ⚠ Match < 0.1% is suspicious — check this is not a")
            print(f"    numerical coincidence. Categorical derivation needed.")
        elif best_max_dev < abs(max(dev_W, dev_Z, key=abs)) / 2:
            print(f"  Substantial improvement (>2x) over baseline. Worth")
            print(f"  pursuing categorical justification, but still a")
            print(f"  hypothesis until structurally derived.")
        else:
            print(f"  Marginal improvement. Probably not the right structural")
            print(f"  augmentation. Path A or B remain more promising.")
    print()

    # ===========================================================================
    # Cross-checks: the PR #1153 EM-channel-ratio claim Q_m/P_m = tanh((2m+1)η_0)
    # ===========================================================================
    print("=" * 80)
    print("Sanity check: PR #1153 EM-channel-ratio claim Q_m/P_m = tanh((2m+1)η_0)")
    print("=" * 80)
    print()
    print(f"  {'particle':<8} {'m':>3} {'Q/P (computed)':>16} {'tanh((2m+1)η_0)':>18}")
    for label, m in [("(none)", 1), ("W", 2), ("Z", 3), ("H", 4)]:
        ratio = float(Q[m] / P[m])
        tanh_val = float(mptanh((2 * m + 1) * eta_0))
        match = "✓" if abs(ratio - tanh_val) < 1e-10 else "✗"
        print(f"  {label:<8} {m:>3} {ratio:>16.10f} {tanh_val:>18.10f}  {match}")
    print()
    print("  (Confirms the PR #1153 / PR #1185 EM-channel-ratio identity.)")
    print()

    # Witness
    witness = {
        "compute": "qm_channel_contribution_probe",
        "description": (
            "Tests whether augmenting the Higgs categorical mass formula "
            "(PR #1159) with a Q_m channel contribution (the bar-anti-"
            "symmetric companion of P_m) closes the ~0.5% residual. "
            "Tests three structural hypotheses (Pythagorean modulus, linear "
            "sum P+Q, geometric mean) at substrate η_0."
        ),
        "substrate": {
            "q_0": str(q_0),
            "eta_0": str(eta_0),
            "h_0": str(h_0),
            "bracket_2_q": str(bracket_2q),
        },
        "p_q_values": {
            f"m={m}": {"P_m": float(P[m]), "Q_m": float(Q[m])}
            for m in range(1, 6)
        },
        "baseline_p_only": {
            "m_H_from_W": float(m_H_W),
            "m_H_from_Z": float(m_H_Z),
            "deviation_W_percent": dev_W,
            "deviation_Z_percent": dev_Z,
        },
        "hypotheses": {
            "H1_pythagorean_modulus": {
                "formula": "m_H = m_anchor · sqrt(P_4²+Q_4²) / sqrt(P_anchor²+Q_anchor²) · 6/5 · (1 - h^4·2G)",
                "m_H_from_W": float(m_H_W_H1),
                "m_H_from_Z": float(m_H_Z_H1),
                "deviation_W_percent": dev_W_H1,
                "deviation_Z_percent": dev_Z_H1,
            },
            "H2_linear_sum_P_plus_Q": {
                "formula": "m_H = m_anchor · (P_4+Q_4) / (P_anchor+Q_anchor) · 6/5 · (1 - h^4·2G)",
                "m_H_from_W": float(m_H_W_H2),
                "m_H_from_Z": float(m_H_Z_H2),
                "deviation_W_percent": dev_W_H2,
                "deviation_Z_percent": dev_Z_H2,
            },
            "H3_geometric_mean": {
                "formula": "m_H = m_anchor · sqrt(P_4·(P_4+Q_4)) / sqrt(P_anchor·(P_anchor+Q_anchor)) · 6/5 · (1 - h^4·2G)",
                "m_H_from_W": float(m_H_W_H3),
                "m_H_from_Z": float(m_H_Z_H3),
                "deviation_W_percent": dev_W_H3,
                "deviation_Z_percent": dev_Z_H3,
            },
        },
        "verdict": (
            f"best structural candidate: {best_hyp}, max deviation "
            f"{best_max_dev:.3f}%" if best_hyp
            else "NONE of H1/H2/H3 improves on the P-only baseline; "
                 "Path C (Q_m closes residual) FAILS"
        ),
        "implication": (
            "If no Q_m augmentation closes the residual, the residual "
            "lives elsewhere — most plausibly the W/Z anchor asymmetry "
            "(Path A: substrate-derivation of v) or Yekutieli MI k=3 "
            "tessellation (Path B). See "
            "docs/audits/2026-05-24-higgs-residual-research-path.md."
        ),
        "status": "exploratory",
        "tags": [
            "qm-channel-contribution",
            "higgs-residual-path-c",
            "pythagorean-augmentation",
            "structural-hypothesis-test",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "qm-channel-contribution-probe.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"  Witness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
