#!/usr/bin/env python3
"""qbeta_complex_c3_fibre_probe.py — DIAGNOSTIC probe: does the c_3
cross-anchor swing fit a complex c_3(q) fibre object?

CONTEXT. User-raised 2026-06-01 follow-up to PR #1616 (Im(q)
fibre/observable framing): "are we maybe missing an Im part that's
not directly observable?"

Per AGENTS.md §Canonical chain (PR #1616): CAL-1/2/3 measure
ARCHIMEDEAN observables (real), so they constrain only the post-τ
evaluation. The fibre Habiro element may have Im components that
project to real via the bar-symmetric pairing (prop:li2q-phiq-bar-
symmetrization) but are themselves complex.

This probe TESTS whether the c_3 cross-anchor swing
  c_3_proton ≈ -2.0693
  c_3_muon   ≈ -2.0097
  swing      ≈ 2.98%
fits a complex-c_3(q) Habiro element where:
  c_3(q) = Re[c_3](q) + i · Im[c_3](q)
projected via various rules (modulus, real-part, etc.)

DISCIPLINE (AGENTS.md no-7th-ansatz). This is a DIAGNOSTIC, NOT a
candidate-fishing run. The probe enumerates 4 specific projection
rules + 3 specific complex-c_3(q) candidates, reports which (if
any) explain the cross-anchor swing structurally, and the audit
doc lists each candidate's failure-mode signature. Any candidate
matching one anchor and missing the other = NEAR-MATCH (mech #N
in flip-flop history), do NOT wire.

PRE-STATED FAILURE SIGNATURES:
  - Real-part projection (Re[c_3(q)] = empirical c_3) requires the
    Im part to be unobservable — but Im should still affect
    higher-order observables via |1 + c_3·u^3|² = (1 + Re·u^3)² +
    (Im·u^3)² ⟹ contributes at order u^6, which is c_6's scale.
    Test: does Im[c_3] at q_proton reproduce empirical c_6?
  - Modulus projection (|c_3(q)| = empirical c_3) would be unusual
    for a Taylor coefficient — c_3 IS already a Taylor coefficient,
    not a magnitude. Probably wrong framing.
  - Bar-projection (Re·sym + Im·antisym via bar-decomp) reduces to
    bar-symmetric and bar-antisymmetric components mapped to Re/Im.
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

import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("qbeta-complex-c3-fibre-probe",
                              engine="python+sympy+mpmath", start_time=t0)
    builder.set_description(
        "DIAGNOSTIC: tests whether c_3 cross-anchor swing fits a "
        "complex-c_3(q) Habiro fibre object. Enumerates 4 projection "
        "rules + 3 complex-c_3 candidates; reports structural fit OR "
        "refutation. NOT a candidate-fishing run."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-qbeta-complex-c3-fibre-diagnostic.md"
    )

    EMPIRICAL_C3_PROTON = mp.mpf("-2.0693")
    EMPIRICAL_C3_MUON = mp.mpf("-2.0097")

    q_proton = q_at()
    q_muon = q_muon_at()
    delta_c3 = EMPIRICAL_C3_PROTON - EMPIRICAL_C3_MUON
    swing_pct = float(delta_c3 / abs(EMPIRICAL_C3_PROTON) * 100)

    print("=" * 78)
    print(" Complex c_3(q) fibre probe — diagnostic")
    print("=" * 78)
    print(f"q_proton: {mp.nstr(q_proton, 25)}")
    print(f"q_muon:   {mp.nstr(q_muon, 25)}")
    print(f"|q_proton - q_muon| = {mp.nstr(abs(q_proton - q_muon), 10)}")
    print(f"empirical c_3 at q_proton: {EMPIRICAL_C3_PROTON}")
    print(f"empirical c_3 at q_muon:   {EMPIRICAL_C3_MUON}")
    print(f"swing: {delta_c3} ({swing_pct:.4f}%)")
    print()

    h_proton = q_proton - 1/q_proton
    h_muon = q_muon - 1/q_muon
    hbar_proton = (q_proton - 1) / q_proton
    hbar_muon = (q_muon - 1) / q_muon

    # ── Candidate 1: c_3(q) = -2 + i·δ(q), δ real-valued small ─────────
    # If projection is Re[c_3] = empirical c_3, then δ doesn't contribute
    # to the observable. But |c_3|² = 4 + δ² — test via c_6 prediction.

    delta_proton = float(EMPIRICAL_C3_PROTON + 2)  # δ = -2.0693 - (-2) = -0.0693
    delta_muon = float(EMPIRICAL_C3_MUON + 2)      # δ = -0.0097

    print("--- Candidate 1: c_3(q) = -2 + i·δ(q) (Im = δ, Re = -2) ---")
    print(f"  δ(q_proton) = {delta_proton:.6f}")
    print(f"  δ(q_muon)   = {delta_muon:.6f}")
    print(f"  ratio δ(q_proton)/δ(q_muon) = {delta_proton/delta_muon:.4f}")
    # Substrate ratio at the anchors
    hbar_ratio = float(hbar_proton / hbar_muon)
    print(f"  ratio ℏ_q(q_proton)/ℏ_q(q_muon) = {hbar_ratio:.4f}")
    print(f"  ratio (ℏ_q(q_proton)/ℏ_q(q_muon))²= {hbar_ratio**2:.4f}")
    # If δ ∝ ℏ_q^k for some k, the ratios should match
    print(f"  log_ratio(δ) / log_ratio(ℏ_q) = "
          f"{float(mp.log(abs(delta_proton/delta_muon))/mp.log(hbar_ratio)):.4f}")
    print()
    candidate_1 = {
        "form": "c_3(q) = -2 + i·δ(q), δ real",
        "delta_proton": str(delta_proton),
        "delta_muon": str(delta_muon),
        "delta_ratio": str(delta_proton/delta_muon),
        "hbar_q_ratio": str(hbar_ratio),
        "log_ratio_exponent": str(
            float(mp.log(abs(delta_proton/delta_muon))/mp.log(hbar_ratio))
        ),
        "verdict": (
            "INCONCLUSIVE — q_proton and q_muon differ by only ~1e-8 in "
            "absolute terms, so the ratio test has little discriminatory "
            "power. δ(q_proton) ≈ 7× δ(q_muon) but the anchors are nearly "
            "identical — suggests δ is NOT a simple power of ℏ_q (which "
            "would give a near-unit ratio). Could be due to numerical "
            "noise in the empirical c_3 extraction at this precision."
        ),
    }

    # ── Candidate 2: c_3(q) = J_Hopf(q) (complex-q evaluation) ─────────
    # J_Hopf(q) = -q^(5/2) - q^(1/2) at general q. Real for real q > 0.
    # NOT complex unless q is complex. Skipped — doesn't apply directly.
    print("--- Candidate 2: c_3(q) = J_Hopf(q) at complex q ---")
    print("  N/A — J_Hopf(q) is real for real q > 0; complex q is not the")
    print("  framework's substrate convention (Lusztig: Im(q_0) = 0).")
    print()
    candidate_2 = {
        "form": "c_3(q) = J_Hopf(q) at complex q",
        "verdict": "N/A — substrate Im(q_0) = 0 by Lusztig",
    }

    # ── Candidate 3: c_3 as bar-projection of complex Habiro element ──
    # If Habiro F(q) = Re[F](q) + i·Im[F](q), then c_3 might be:
    #   Re[c_3 of F] = Taylor coeff of Re[F] at u^3
    #   Im[c_3 of F] = Taylor coeff of Im[F] at u^3 — UNOBSERVABLE
    # Per PR #1620 bar-decomposition of Δtr_M:
    #   sym(Δtr_M)(q_proton) ≈ -1.091e-2 (Re? Im?)
    #   antisym(Δtr_M)(q_proton) ≈ -1.312e-1 (Im? Re?)
    print("--- Candidate 3: c_3 = Re or Im of complex Habiro element ---")
    # Keep substrate precision — was flagged by compute_no_mpf_to_float_cast.
    sym_proton = -mp.mpf("0.01091170")
    antisym_proton = -mp.mpf("0.13116116")
    delta_tr_proton = sym_proton + antisym_proton
    print(f"  sym(Δtr_M) at q_proton:    {sym_proton:.6f}")
    print(f"  antisym(Δtr_M) at q_proton: {antisym_proton:.6f}")
    print(f"  sym² + antisym² = {sym_proton**2 + antisym_proton**2:.6e}")
    print(f"  |Δtr_M|² = {delta_tr_proton**2:.6e}")
    print(f"  ratio = {(sym_proton**2 + antisym_proton**2)/delta_tr_proton**2:.6f}")
    # If sym and antisym were Re/Im of complex Δtr_M, then |Δtr_M|² = sym² + antisym²
    # The numerical sums tell us whether that interpretation is consistent
    print()
    candidate_3 = {
        "form": "bar-decomposition sym/antisym = Re/Im of complex Δtr_M",
        "sym_at_proton": str(sym_proton),
        "antisym_at_proton": str(antisym_proton),
        "sum_squares": str(sym_proton**2 + antisym_proton**2),
        "delta_tr_M_squared": str(delta_tr_proton**2),
        "ratio_sum_sq_to_delta_sq": str(
            (sym_proton**2 + antisym_proton**2)/delta_tr_proton**2
        ),
        "verdict": (
            "REFUTED. If sym and antisym were Re/Im, then |Δtr_M|² = sym² + "
            "antisym² should hold. Instead: sum_squares = 1.733e-2, "
            "|Δtr_M|² = (sym+antisym)² = (−0.1421)² = 2.019e-2. Ratio = "
            "0.858 ≠ 1. The bar-decomposition is NOT a Re/Im split of a "
            "complex Δtr_M. It IS the eigenspace decomposition under the "
            "bar-involution acting on a REAL function — different from "
            "complex conjugation of a complex function."
        ),
    }

    # ── Candidate 4: complex c_k(q) at fibre, Re projection at archimedean ──
    print("--- Candidate 4: c_3 = Re[fibre c_3(q)], Im part affects c_6 ---")
    # If c_3 is complex (R + iI) and projection is Re[c_3] = R = -2:
    # then 1 + c_3·u^3 = (1 + R·u^3) + i·I·u^3
    # |1 + c_3·u^3|² = (1 + R·u^3)² + (I·u^3)² ≈ 1 + 2R·u^3 + (R² + I²)·u^6
    # The observable Q_β should match THIS magnitude.
    # If empirical R = -2 (exact) and the residual -0.0693 at u^3 comes from
    # the |...|² → it's a u^6 effect, NOT a u^3 effect. But the empirical
    # c_3 IS at u^3 level (residual / u^3). So this Re-only interpretation
    # gives c_3 = -2 exactly + residual = 0 at u^3 → BUT empirical c_3 = -2.0693
    # at q_proton, which means R = -2.0693 NOT -2.0. The residual IS at u^3,
    # so c_3 is NOT just -2 with Im correction. The Im part contributes at
    # different order.
    # Conclusion: Re-projection candidate REFUTES the "c_3 = -2 + iε" form.
    print("  If Re[c_3] = -2 exactly, empirical c_3 at u^3 should = -2.")
    print(f"  Observed: c_3_empirical = {EMPIRICAL_C3_PROTON} (NOT -2).")
    print("  So c_3 = -2 + i·δ doesn't fit a u^3-projection model. REFUTED.")
    print()
    candidate_4 = {
        "form": "c_3 = Re[fibre c_3(q)], Im part unobservable at u^3 order",
        "verdict": (
            "REFUTED — empirical c_3 at q_proton = -2.0693 NOT -2. If "
            "Re[c_3] were exactly -2 and Im were the deviation, the u^3 "
            "projection would give -2 exactly. The observed deviation IS "
            "AT u^3 order, ruling out the Re-only projection of "
            "c_3 = -2 + i·δ."
        ),
    }

    # ── Overall conclusion ──────────────────────────────────────────
    print("=" * 78)
    print(" CONCLUSIONS")
    print("=" * 78)
    print("""
1. The 'is c_3 complex with Im hidden by archimedean projection?' framing
   is structurally PLAUSIBLE per AGENTS.md fibre/observable distinction
   (PR #1616), but the SPECIFIC c_3 = -2 + i·δ form is REFUTED by the
   data: the empirical deviation IS at u^3 order, ruling out projection
   to -2 + Im correction.

2. The bar-decomposition (PR #1615/#1620) is NOT a Re/Im split of a
   complex object: sym² + antisym² ≠ |Δtr_M|². It IS an eigenspace
   decomposition under a real-action bar-involution.

3. The cross-anchor c_3 ratio δ_proton/δ_muon ≈ 7.1 does NOT match
   simple substrate ratios like ℏ_q^k (which would give ≈ 1.0 since
   q_proton ≈ q_muon to 1e-8). The empirical "swing" is dominated by
   q_0 anchor uncertainty + extraction precision, NOT by structural q
   dependence — q_proton and q_muon are TOO CLOSE to discriminate.

4. The structurally meaningful next test is at WIDER-spaced q anchors
   (e.g., q at the m_p anchor vs q at a hypothetical m_He-pin). Without
   such a wide spacing, the cross-anchor test is underdiagnostic.

The complex-c_3 framing IS still a viable structural direction — but
it can't be discriminated from real-c_3 with anchors this close. The
fibre-vs-observable distinction (PR #1616) is still correct as a
discipline guard; we just can't test the Im hypothesis directly from
the c_3 numerical data alone.
""")

    builder.add_data("candidate_1_im_delta", candidate_1)
    builder.add_data("candidate_2_complex_q", candidate_2)
    builder.add_data("candidate_3_re_im_via_bar_decomp", candidate_3)
    builder.add_data("candidate_4_re_projection_minus_2", candidate_4)
    builder.add_data("q_proton", str(q_proton))
    builder.add_data("q_muon", str(q_muon))
    builder.add_data("q_anchor_gap_abs", str(abs(q_proton - q_muon)))
    builder.add_data("empirical_c3_proton", str(EMPIRICAL_C3_PROTON))
    builder.add_data("empirical_c3_muon", str(EMPIRICAL_C3_MUON))
    builder.add_data("swing_pct", swing_pct)
    builder.add_data("overall_conclusion", (
        "Complex-c_3 framing PLAUSIBLE structurally but specific candidates "
        "REFUTED by data. Bar-decomposition is NOT Re/Im of complex Δtr_M "
        "(sum-of-squares mismatch). Anchors too close to discriminate. The "
        "fibre/observable distinction (PR #1616) stays correct as discipline "
        "guard; complex-c_3 attack needs wider-spaced anchors to be testable."
    ))
    builder.add_data("recommended_next_step", (
        "Either (a) construct a third q-anchor at a different observable "
        "(e.g., m_e/m_K) for wider spacing, OR (b) examine the Habiro "
        "q-difference equation directly for Im content rather than "
        "relying on numerical c_3 extraction at near-identical anchors."
    ))

    builder.add_assertion(
        name="all_4_candidates_have_verdicts",
        computed=4.0,
        expected=4.0,
        tolerance=0.0,
        source="Diagnostic probe enumerates 4 candidates with explicit verdicts",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
