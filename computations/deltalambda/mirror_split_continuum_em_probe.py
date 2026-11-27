#!/usr/bin/env python3
"""
mirror_split_continuum_em_probe.py — the κ closure via the CONTINUUM EM object:
test whether the framework's categorical EM supplies the 8-pair mirror-split
systematics  split ≈ 0.84·α·ΔZ(Z−1)·(3/5)·ℏc/R(A)  (R = r₀·A^{1/3}), i.e. the
honest open object of docs/coordination/binding-scale-is-hyperbolic-volume.md §3,
superseding BOTH the A=3-only fixed κ = 1/3 (fails ⁷Li/⁷Be by 2.2×,
2026-07-13-mirror-split-s3-em-functional-attempt.md calibration constraint) AND
the A-independent pairwise tanh(ln q₀) route.

FORMALIZE-FIRST DECOMPOSITION (compute-author §3.3) — every factor traced:

    split_pred(A, Z_lo, Z_hi)
        = (3/5) · α_EM · [Z_hi(Z_hi−1) − Z_lo(Z_lo−1)] · ℏc / R(A),
    R(A) = λ̄_π · A^{1/3},   λ̄_π = ℏ/(m_π c)   ⇒   ℏc/R(A) = m_π / A^{1/3},

so in MeV, with NO empirical length constant anywhere:

    split_pred = (3/5) · α_EM · ΔZ(Z−1) · m_π / A^{1/3}.

Factor → corpus source → tier:
  • α_EM       → prop:alpha-em-categorical-trace-ratio, α = 1/(q₀[9]_q[10]_q)
                 (bare, −0.155% vs CODATA; the +2/(3π) archimedean correction
                 → −4.2 ppm is partially open). Tier: DERIVED (bare). The
                 0.155% is far below the 7% systematics scatter — insensitive
                 (asserted below).
  • ΔZ(Z−1)/2  → exact discrete-proton pair count. This is the general-A
                 orbit form of the S₃-functional D1 (S2, CLOSED): the charge
                 bilinear Σ_{i<j} q_i q_j on Z unit protons = C(Z,2) exactly;
                 for a T_z mirror (Z_hi = Z_lo+1) the difference is exactly
                 Z_lo (verified in exact ints below). Tier: EXACT.
  • 3/5        → uniform-sphere electrostatic self-energy — classical
                 Euclidean archimedean-side geometry, standard, not fitted to
                 these data. Tier: MODEL ASSUMPTION (uniform charge density),
                 honestly flagged; NOT a categorical derivation.
  • m_π        → CAL-3 (M_PI_PM_MEV_VALIDATION; the orthogonal meson scale of
                 the three-calibration discipline). Tier: CALIBRATION INPUT —
                 permitted, no fourth calibration introduced.
  • A^{1/3}    → radius law from VOLUME EXTENSIVITY: the derived log-trace
                 bond sum B = Σ_bonds ε (#2089) + the Lean-proved chain bond
                 count M_n = n−1 + the ledger identification B = m_e·Vol make
                 the categorical volume extensive, Vol ∝ A; a fixed volume per
                 nucleon ⇒ R ∝ Vol^{1/3} ∝ A^{1/3}. WEAK STEP (named): the
                 hyperbolic volume of the link complement is a topological
                 invariant, NOT a Euclidean spatial volume — equating "spatial
                 nuclear volume ∝ categorical Vol" is an archimedean
                 identification the corpus does not derive (and the ⁴He Vol₄
                 single-volume reading is NEGATIVE, vol4 falsification probe).
                 Tier: CONDITIONAL/PARTIAL.
  • R(A) = 1·λ̄_π·A^{1/3}  → THE UNDERIVED STEP. The packing radius equal to
                 the pion Compton wavelength at coefficient EXACTLY 1 is a
                 SELECTION among the framework's four mass scales (m_e, m_μ,
                 m_π, m_p — table printed below: only m_π lands at ≈1; the
                 others miss by 270×, 1.3×, 0.15×), physically the Yukawa-
                 range identification. It is NOT derived from the categorical
                 EM. Tier: UNDERIVED (the single remaining gap).

RESULT SHAPE: with the pion-Compton radius the prediction has ZERO fitted
constants; the overall coefficient is PREDICTED to be 1 and measured as
mean(split_AME/split_pred) over the 8 mirror pairs (A = 3…39). The success
criterion (per the task): matching the SCALING across A — the thing the fixed
1/3 fails — separately from the absolute normalization.

ANTI-FIT: nothing is tuned; the one number the construction leaves open (the
packing coefficient) is NOT fitted to 0.838-anything — it is set to 1 by the
Yukawa selection and the measured mean is reported as a check. Because that
selection (and the volume→radius step) are underived, the classification is
(ii) PARTIAL regardless of the numbers. EXPLORATORY — scope-limited (a),
no production wiring, no content-block change.

Data/benchmark: the 8 T_z mirror pairs of mirror_nuclei_coulomb_systematics.py
(split/ΔE_C = 0.838 ± 0.059 against the r₀ = 1.2 fm canonical Coulomb).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_HERE, _COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    _ame_binding_mev,
    M_E_MEV,
    M_PI_PM_MEV_VALIDATION,
)
from experimental_constants import ALPHA_EM_INV  # noqa: E402
# Canonical shared Coulomb (r₀ = 1.2 fm) — consistency cross-check only
from coulomb_energy import mirror_displacement_mev, R0_FM  # noqa: E402
# Superseded candidates, via the sibling probes' exact code paths
from mirror_split_milnor_one_third_probe import per_block, E0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q0 = Q_MP

# CODATA masses for the scale-selection table (MeV) — printing/selection only
M_MU_MEV = mp.mpf("105.6583755")
M_P_MEV = mp.mpf("938.27208943")
HBAR_C_MEV_FM = mp.mpf("197.3269804")   # printout of λ̄_π in fm only; NOT in pred

# The 8 T_z mirror pairs of mirror_nuclei_coulomb_systematics.py (same data).
PAIRS = [("3H/3He", 1, 2, 3), ("7Li/7Be", 3, 4, 7), ("11B/11C", 5, 6, 11),
         ("13C/13N", 6, 7, 13), ("15N/15O", 7, 8, 15), ("23Na/23Mg", 11, 12, 23),
         ("27Al/27Si", 13, 14, 27), ("39K/39Ca", 19, 20, 39)]


def qint(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced q-integer [n]_q = (q^n − q^{−n})/(q − q^{−1})."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def alpha_derived(q: mp.mpf) -> mp.mpf:
    """Bare derived α_EM = 1/(q·[9]_q·[10]_q) — prop:alpha-em-categorical-trace-ratio."""
    return 1 / (q * qint(9, q) * qint(10, q))


def split_ame(Z1: int, Z2: int, A: int) -> mp.mpf:
    return mp.mpf(str(_ame_binding_mev(Z1, A))) - mp.mpf(str(_ame_binding_mev(Z2, A)))


def pred_continuum(A: int, Z_lo: int, Z_hi: int, alpha: mp.mpf, m_scale: mp.mpf) -> mp.mpf:
    """split_pred = (3/5)·α·ΔZ(Z−1)·m_scale/A^{1/3}  (MeV; m_scale = ℏc/λ̄)."""
    dZZ = Z_hi * (Z_hi - 1) - Z_lo * (Z_lo - 1)
    return mp.mpf(3) / 5 * alpha * dZZ * m_scale / mp.cbrt(A)


def main() -> int:
    print("=== Mirror split via the continuum categorical EM: "
          "(3/5)·α·ΔZ(Z−1)·m_π/A^{1/3} (zero length constants) ===\n")

    # ── factor 1: derived α_EM (bare trace-ratio form) ───────────────────────
    a_der = alpha_derived(q0)
    a_codata = 1 / mp.mpf(str(ALPHA_EM_INV))
    a_rel = a_der / a_codata - 1
    print(f"α_EM derived (bare 1/(q₀[9]_q[10]_q)) : 1/{float(1/a_der):.6f}")
    print(f"α_EM CODATA                           : 1/{ALPHA_EM_INV}")
    print(f"relative difference: {float(a_rel):+.3e}  "
          f"(≪ the 7% systematics scatter — insensitive)\n")

    # ── factor 2: exact charge pair combinatorics (general-A orbit form of D1) ─
    combi_ok = all((Z2 * (Z2 - 1) - Z1 * (Z1 - 1)) == 2 * Z1
                   for _, Z1, Z2, _A in PAIRS)
    print(f"pair combinatorics ΔZ(Z−1)/2 = Z_lo exactly for all T_z mirrors: "
          f"[{'PASS' if combi_ok else 'FAIL'}] (exact ints; charge bilinear "
          f"Σ q_iq_j = C(Z,2), the S2-closed orbit count at general A)\n")

    # ── factor 3: the length scale — λ̄_π (CAL-3), with the selection table ──
    lam_pi_fm = HBAR_C_MEV_FM / M_PI_PM_MEV_VALIDATION
    print(f"radius law R(A) = λ̄_π·A^(1/3),  λ̄_π = ℏc/m_π = {float(lam_pi_fm):.5f} fm")
    print(f"  (⇒ ℏc/R(A) = m_π/A^(1/3): the pion CAL-3 mass IS the inverse length —")
    print(f"   no empirical r₀; the empirical r₀ = {R0_FM} fm is NOT used in pred)\n")

    # ── the 8-pair table, zero fitted constants ──────────────────────────────
    m_pi = M_PI_PM_MEV_VALIDATION
    print(f"  {'pair':<11}{'A':>3}{'split_AME':>10}{'pred':>9}{'ratio':>8}"
          f"{'  [canonical ΔE_C ratio 0.838-benchmark]':>20}")
    rows, ratios = [], []
    for nm, Z1, Z2, A in PAIRS:
        s = split_ame(Z1, Z2, A)
        p = pred_continuum(A, Z1, Z2, a_der, m_pi)
        c = mp.mpf(str(mirror_displacement_mev(Z2, Z1, A)))  # canonical r₀=1.2 path
        r = s / p
        rows.append((nm, A, float(s), float(p), float(r), float(s / c)))
        ratios.append(r)
        print(f"  {nm:<11}{A:>3}{float(s):>10.3f}{float(p):>9.3f}{float(r):>8.3f}"
              f"{float(s / c):>14.3f}")

    mean_r = sum(ratios) / len(ratios)
    rms = mp.sqrt(sum((r - mean_r) ** 2 for r in ratios) / len(ratios))
    print(f"\n  split_AME/split_pred = {float(mean_r):.3f} ± {float(rms):.3f} "
          f"({float(100 * rms / mean_r):.0f}% scatter)")
    print(f"  ⇒ SCALING: flat across A=3–39 (same {float(100*rms/mean_r):.0f}% scatter as the")
    print(f"    canonical-r₀ systematics — the Z(Z−1)/A^(1/3) shape is carried);")
    print(f"  ⇒ NORMALIZATION: with the pion-Compton radius the predicted coefficient")
    print(f"    is 1 (zero fitted constants) and measures {float(mean_r):.3f} — "
          f"|mean−1| = {float(abs(mean_r-1)):.3f}.")
    print(f"    Mild A-trend {rows[0][4]:.2f}→{rows[-1][4]:.2f}: the known light-nucleus")
    print(f"    deviation from R ∝ A^(1/3) (same trend as the systematics audit).\n")

    # consistency with the canonical shared Coulomb path (algebraic rescale)
    scale_check = (mp.mpf(str(R0_FM)) / lam_pi_fm) * (a_der / a_codata)
    resc_ok = all(abs(mp.mpf(str(rw[4])) / (mp.mpf(str(rw[5])) / scale_check) - 1) < mp.mpf("1e-3")
                  for rw in rows)
    print(f"consistency: pred = canonical ΔE_C(r₀=1.2)·(r₀/λ̄_π)·(α_der/α_CODATA) "
          f"[{'PASS' if resc_ok else 'FAIL'}]\n")

    # ── scale-selection table (why m_π and not another framework mass) ──────
    print("length-scale selection — required coefficient mean(split/pred) if the")
    print("packing radius were the Compton length of each framework mass scale:")
    sel = {}
    for lbl, m in [("m_e (CAL-1)", M_E_MEV), ("m_mu (CAL-2 proxy)", M_MU_MEV),
                   ("m_pi (CAL-3)", m_pi), ("m_p (phys-obs pin)", M_P_MEV)]:
        rs = [split_ame(Z1, Z2, A) / pred_continuum(A, Z1, Z2, a_der, m)
              for _, Z1, Z2, A in PAIRS]
        sel[lbl] = float(sum(rs) / len(rs))
        print(f"  {lbl:<20}: coefficient needed = {sel[lbl]:>9.3f}"
              f"{'   ← ≈ 1, selected (Yukawa range)' if abs(sel[lbl]-1) < 0.1 else ''}")
    print("  Selection entropy: 2 bits (4 candidates); the pion is also the a-priori")
    print("  standard Yukawa-range scale. Still a SELECTION, not a derivation.\n")

    # ── supersession: fixed κ=1/3 and tanh(ln q₀), both A-independent ───────
    B_pp = E0 * (per_block(2, 0, False) - per_block(2, 0, True))
    pred_13 = B_pp / 3
    pred_tanh = mp.tanh(mp.log(q0)) * B_pp
    print("superseded candidates (both A-independent — no Z(Z−1)/A^(1/3) scaling):")
    print(f"  {'pair':<11}{'split_AME':>10}{'cont ratio':>11}{'κ=1/3 ratio':>12}"
          f"{'tanh ratio':>11}")
    worst_cont, a7_13, a7_cont = mp.mpf(0), None, None
    for (nm, Z1, Z2, A), rw in zip(PAIRS, rows):
        s = mp.mpf(str(rw[2]))
        r13, rt = s / pred_13, s / pred_tanh
        worst_cont = max(worst_cont, abs(mp.mpf(str(rw[4])) - 1))
        if A == 7:
            a7_13, a7_cont = r13, mp.mpf(str(rw[4]))
        print(f"  {nm:<11}{rw[2]:>10.3f}{rw[4]:>11.3f}{float(r13):>12.3f}{float(rt):>11.3f}")
    print(f"\n  fixed κ=1/3 at ⁷Li/⁷Be: {float(a7_13):.2f}× (the calibration-constraint")
    print(f"  failure); continuum at ⁷Li/⁷Be: {float(a7_cont):.3f} (within "
          f"{float(100*abs(a7_cont-1)):.0f}%). tanh route: no A-scaling at all.")
    print(f"  worst continuum |ratio−1| across all 8 pairs: {float(worst_cont):.3f}\n")

    # ── verdict ──────────────────────────────────────────────────────────────
    print("VERDICT: (ii) PARTIAL — the SCALING is carried by derived/exact factors")
    print("(α_EM derived, ΔZ(Z−1)/2 exact, A^(1/3) conditional on volume extensivity")
    print("with the hyperbolic→Euclidean identification the named weak step); the")
    print("NORMALIZATION lands at coefficient ≈ 1 with zero fitted constants ONLY")
    print("under the underived packing identification R = 1·λ̄_π·A^(1/3) (Yukawa")
    print("selection among 4 framework scales) + the uniform-sphere 3/5 model factor.")
    print("Supersedes fixed κ=1/3 and pairwise tanh(ln q₀) on scaling grounds.")
    print("Not derived ⇒ not wired: no production change.")

    # ── witness ──────────────────────────────────────────────────────────────
    ok = True
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-split-continuum-em", engine="mpmath")
            wb.set_description(
                "kappa closure via the continuum categorical EM: split_pred = "
                "(3/5)·alpha·dZ(Z-1)·m_pi/A^(1/3) with ZERO fitted constants — alpha "
                "from the derived trace-ratio 1/(q0[9]_q[10]_q), exact discrete-proton "
                "pair count, and the pion-Compton radius law R(A)=lambda_pi·A^(1/3) "
                "(CAL-3 length; hbar·c/R = m_pi/A^(1/3), no empirical r0). Across the 8 "
                "T_z mirror pairs A=3-39: split_AME/split_pred = %.3f ± %.3f — scaling "
                "flat (supersedes the A=3-only fixed 1/3, which fails 7Li/7Be by %.1fx, "
                "and the A-independent tanh(ln q0) route) and the coefficient is "
                "consistent with the predicted 1. PARTIAL: the packing identification "
                "R = 1·lambda_pi·A^(1/3) (Yukawa selection among the 4 framework mass "
                "scales) and the volume->radius extensivity step are underived; the 3/5 "
                "is the uniform-sphere model factor. Exploratory scope-(a), no wiring."
                % (float(mean_r), float(rms), float(a7_13)))
            wb.add_data("pairs", [
                {"pair": nm, "A": A, "split_AME_MeV": s, "pred_MeV": p,
                 "ratio": r, "ratio_canonical_r0": rc}
                for (nm, _Z1, _Z2, A), (nm2, A2, s, p, r, rc) in zip(PAIRS, rows)])
            wb.add_data("ratio_mean", float(mean_r))
            wb.add_data("ratio_rms_scatter", float(rms))
            wb.add_data("alpha_derived", float(a_der))
            wb.add_data("alpha_rel_diff_vs_codata", float(a_rel))
            wb.add_data("lambda_pi_fm", float(lam_pi_fm))
            wb.add_data("scale_selection_required_coefficients", sel)
            wb.add_data("B_pp_MeV", float(B_pp))
            wb.add_data("superseded_fixed_one_third_A7_ratio", float(a7_13))
            wb.add_data("superseded_tanh_A3_ratio",
                        float(mp.mpf(str(rows[0][2])) / pred_tanh))
            wb.add_data("benchmark_canonical_r0", "split/dE_C = 0.838 ± 0.059 "
                        "(mirror-nuclei-coulomb-systematics)")
            asserts = [
                ("pair_combinatorics_exact", int(combi_ok), 1,
                 "dZ(Z-1)/2 = Z_lo exactly (ints) for all 8 T_z mirror pairs — the "
                 "general-A orbit form of the S2-closed charge bilinear"),
                ("scaling_flat_across_A", int(rms / mean_r < mp.mpf("0.15")), 1,
                 f"RMS/mean of split/pred = {float(rms/mean_r):.3f} < 0.15 across "
                 "A=3-39 — the Z(Z-1)/A^(1/3) scaling is matched (the criterion "
                 "fixed 1/3 fails)"),
                ("coefficient_one_pion_compton",
                 int(abs(mean_r - 1) < mp.mpf("0.05")), 1,
                 f"|mean ratio - 1| = {float(abs(mean_r-1)):.3f} < 0.05 with zero "
                 "fitted constants (packing coefficient predicted 1 by the Yukawa "
                 "selection — the selection itself is the underived step)"),
                ("supersedes_fixed_one_third_and_tanh",
                 int(a7_13 > 2 and abs(a7_cont - 1) < mp.mpf("0.15")), 1,
                 f"at 7Li/7Be: fixed 1/3 errs {float(a7_13):.2f}x (>2) while the "
                 f"continuum ratio {float(a7_cont):.3f} is within 15%; tanh route "
                 "has no A-dependence at all"),
                ("derived_alpha_insensitive",
                 int(abs(a_rel) < mp.mpf("0.005") and resc_ok), 1,
                 "bare derived alpha within 0.5% of CODATA and pred consistent with "
                 "the canonical coulomb_energy path under the algebraic rescale "
                 "(r0/lambda_pi)·(alpha_der/alpha_codata)"),
            ]
            for name, comp, exp, src in asserts:
                ok = ok and (comp == exp)
                wb.add_assertion(name=name, computed=str(comp), expected=str(exp),
                                 tolerance=0, source=src)
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
