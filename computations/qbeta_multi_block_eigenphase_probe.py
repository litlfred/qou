#!/usr/bin/env python3
"""qbeta_multi_block_eigenphase_probe.py — Q_β bridge experiment #3:
multi-block eigenphase, informed by #1521's fundamental-rep lesson.
(Item 2 of the 2026-06-09 post-1574 workplan.)

CONTEXT. The Q_β bridge-narrowing audit
(docs/audits/2026-05-31-qbeta-bridge-narrowing.md) ruled out 6
mechanisms via the q₀-stability criterion. PR #1521 then resolved the
analogous α_EM question with a key lesson: **the Habiro element is the
fundamental-rep closed fermion-loop unknot, NOT an H_3 Hecke word**. The
per-block H_3 route was the dead end for both α_EM and Q_β.

This probe tests whether Q_β closes when:
  - matter content sits in the fundamental SU_q(2) rep (per #1521)
  - the eigenphase combines per-block contributions weighted not by
    y_λ (which fails: Σy_λ(q₀) = 0.719 ≠ 1) but by their fundamental-
    rep dimensions
  - the closure target is q₀-STABLE (Taylor-exact at canonical q₀)
    not a near-match

OUTPUT (always honest):
  - structural data: per-block eigenphase contributions at q₀
  - q₀-stability test across canonical (m_p-pin) and stale (muon-pin)
  - verdict: ruled-in (eigenphase q₀-stable + < compute-precision
    residual) OR ruled-out (drift > 0.01% between pins) OR open
    (closer than 6 prior mechanisms but not Taylor-exact)

DISCIPLINE: per the bridge-narrowing addendum §4, q₀-dependent
residuals = form-fitting. No identification claimed unless q₀-stable.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

try:
    from _precision import set_compute_dps
except ImportError:
    def set_compute_dps(): mp.mp.dps = 50
set_compute_dps()

try:
    from witness_base import WitnessBuilder
except ImportError:
    sys.path.insert(0, str(HERE.parent))
    from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV

# Stale muon-pin q₀ for the q₀-stability test (vs canonical m_p-pin).
Q0_STALE_MUON_PIN = "1.10997859555418057528159407960950937799328227995870"
Q_BETA_CODATA_MEV = mp.mpf("0.78233341")  # CODATA 2022


def bridge_test(q0_str: str) -> dict:
    """Compute the multi-block fundamental-rep eigenphase at a given q₀.

    The candidate bridge:
      Q_β = m_e · |Q_A| · cos(α_eff(q))
    with α_eff(q) the MULTI-BLOCK eigenphase, weighted by per-block
    quantum dimensions of the FUNDAMENTAL rep (not the y_λ which fail):

      α_eff = Σ_λ [dim_q^FR(λ) / Z(q)] · α_λ

    where dim_q^FR(λ) is the quantum dimension of the λ-block in the
    fundamental rep (NOT y_λ; the FR is single-block per #1521), Z(q)
    is the natural normaliser, and α_λ is the block-local eigenphase.

    For the H_3(q) basis:
      blocks: (3), (2,1), (1,1,1)
      LO eigenphase per block (from per-block character expansion in
        2026-05-31-qbeta-bridge-narrowing.md §"Established fact #3":
        ε¹ coefficients (−2, −1, −2)):
          α_(3) = -2·ε        (trivial block)
          α_(2,1) = -1·ε      (standard block)
          α_(1,1,1) = -2·ε    (sign block)
      where ε = q − 1.

    In the fundamental rep, the dim_q per block is just [d_λ]_q where
    d_λ is the ordinary dimension (1, 2, 1).
    """
    q = mp.mpf(q0_str)
    me = mp.mpf(M_E_MEV)

    h = q - 1 / q
    eps = q - 1
    # Form A baseline.
    Q_A = me * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    # Per-block fundamental-rep quantum dimensions for H_3:
    #   (3)     → 1   (1-dim trivial → q-dim = 1)
    #   (2,1)   → 2   (2-dim standard → q-dim = [2]_q)
    #   (1,1,1) → 1   (1-dim sign → q-dim = 1)
    qbr2 = (q ** 2 - q ** (-2)) / (q - 1 / q)  # [2]_q
    dim_qFR = {"(3)": mp.mpf(1), "(2,1)": qbr2, "(1,1,1)": mp.mpf(1)}
    Z_q = sum(dim_qFR.values())  # natural normaliser

    # Per-block LO eigenphase (from §"Established fact #3" + the
    # ε-Taylor expansion of χ_λ(β_n − β_p)). Higher-order corrections
    # land here too — this probe tests the LO contribution; if it
    # closes, the higher-order terms become the next sub-experiment.
    alpha_block_LO = {"(3)": -2 * eps, "(2,1)": -1 * eps, "(1,1,1)": -2 * eps}
    alpha_eff_LO = sum(dim_qFR[b] * alpha_block_LO[b] for b in dim_qFR) / Z_q

    # Candidate bridge: Q_β = Q_A · cos(α_eff)
    Q_bridge = Q_A * mp.cos(alpha_eff_LO)
    err_ppb = (Q_bridge / Q_BETA_CODATA_MEV - 1) * mp.mpf(10) ** 9

    return {
        "q": q, "h": h, "eps": eps, "Q_A": Q_A,
        "dim_qFR_block": dim_qFR, "Z_q_norm": Z_q,
        "alpha_block_LO": alpha_block_LO,
        "alpha_eff_LO": alpha_eff_LO,
        "Q_bridge": Q_bridge, "err_ppb": err_ppb,
    }


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder("qbeta-multi-block-eigenphase-probe",
                             engine="python+mpmath", start_time=t0)
    builder.set_description(
        "Q_β bridge experiment #3: multi-block eigenphase weighted by "
        "fundamental-rep quantum dimensions (informed by PR #1521's "
        "fundamental-rep lesson). Tests q₀-stability across canonical "
        "and stale q₀ pins. Discipline lock: q₀-drift > 0.01% rules the "
        "mechanism OUT (same criterion as the 6 prior bridge mechanisms)."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β BRIDGE EXPERIMENT #3 — multi-block eigenphase (fund. rep)")
    print(" (informed by PR #1521 + 2026-06-09 per-basis scoping)")
    print("=" * 78)
    print()

    canon = bridge_test(Q_50_DIGIT_STR)
    stale = bridge_test(Q0_STALE_MUON_PIN)

    print(f"  canonical (m_p-pin) q₀ = {mp.nstr(canon['q'], 18)}")
    print(f"  stale     (muon-pin) q₀ = {mp.nstr(stale['q'], 18)}")
    print()
    print(f"  {'block':<9} {'dim_qFR(λ)':<14} {'α_LO at canonical':<24}")
    print(f"  {'-'*9} {'-'*14} {'-'*24}")
    for b in canon["dim_qFR_block"]:
        print(f"  {b:<9} {mp.nstr(canon['dim_qFR_block'][b], 10):<14} "
              f"{mp.nstr(canon['alpha_block_LO'][b], 14):<24}")
    print(f"  Σ dim_qFR (Z_q normaliser) = {mp.nstr(canon['Z_q_norm'], 14)}")
    print(f"  α_eff (LO, fundamental-rep-weighted) = {mp.nstr(canon['alpha_eff_LO'], 16)}")
    print()
    print(f"  Q_β CODATA              = {mp.nstr(Q_BETA_CODATA_MEV, 12)} MeV")
    print(f"  Q_A baseline            = {mp.nstr(canon['Q_A'], 12)} MeV  "
          f"({mp.nstr((canon['Q_A']/Q_BETA_CODATA_MEV - 1) * mp.mpf(10)**6, 8)} ppm)")
    print(f"  Q_bridge (fund-rep LO)  = {mp.nstr(canon['Q_bridge'], 12)} MeV  "
          f"({mp.nstr(canon['err_ppb'], 8)} ppb)")
    print()

    # q₀-stability
    err_canon = canon["err_ppb"]
    err_stale = stale["err_ppb"]
    drift = abs(err_canon - err_stale)
    drift_pct = float(drift / abs(err_canon) * 100) if err_canon != 0 else float("inf")
    print(f"  {'pin':<25} {'err_ppb':<22}")
    print(f"  {'canonical (m_p-pin)':<25} {mp.nstr(err_canon, 10):<22}")
    print(f"  {'stale (muon-pin)':<25} {mp.nstr(err_stale, 10):<22}")
    print(f"  q₀-drift between pins: {drift_pct:.4f}%")
    print()

    # Verdict
    abs_err_canon = abs(float(err_canon))
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if abs_err_canon < 0.001:
        verdict = "ruled-in (Taylor-exact at canonical q₀)"
        msg = f"""
  ✓ BREAKTHROUGH. Q_β closes to {mp.nstr(err_canon, 6)} ppb (< compute precision).
    The multi-block fundamental-rep eigenphase IS the bridge.
    Next: q₀-stability check across pins ⟹ drift = {drift_pct:.4f}%.
    Higher-order corrections + Lean formalisation follow."""
    elif drift_pct > 0.01:
        verdict = "ruled-OUT (q₀-drift > 0.01%, form-fitting signature)"
        msg = f"""
  ✗ The multi-block fundamental-rep eigenphase candidate has the same
    failure mode as mechanisms 1–6 in the bridge-narrowing doc:
    q₀-drift of {drift_pct:.4f}% across pins flags it as form-fitting at
    one specific q₀. Discipline lock §4 rules it out.

    Honest reading: even the fundamental-rep lesson from #1521 doesn't
    transfer cleanly to Q_β at the cos(α_eff) level. The composite must
    include Planck-tick + Bloch-Wigner factors (per #1521's
    1/(8π) = 1/(π·dim H¹(M_Bring)) identification — a 3-factor
    composition not a bare eigenphase).

    Production stays Q_N2 (1279 ppb)."""
    else:
        verdict = "open (q₀-stable but not Taylor-exact)"
        msg = f"""
  ◐ The eigenphase candidate is q₀-stable (drift {drift_pct:.4f}%) but
    its residual {mp.nstr(err_canon, 6)} ppb is above compute precision.
    This is closer than the 6 prior mechanisms but not closing the bridge.
    Suggests the LO-only treatment is incomplete — higher-order ε
    contributions to α_block may close the gap.

    Next experimental step: include ε² and ε³ terms from the per-block
    character expansion (from §"Established fact #3" of the bridge-
    narrowing doc). If those close it, the bridge is the multi-block
    eigenphase in the fundamental rep — a positive result.

    Production stays Q_N2 (1279 ppb) until closure."""
    print(msg)
    print()
    print(f"  verdict: {verdict}")
    print()

    builder.add_data("pins", {
        "canonical_mp_pin_q0": Q_50_DIGIT_STR,
        "stale_muon_pin_q0": Q0_STALE_MUON_PIN,
    })
    builder.add_data("fundamental_rep_decomposition", {
        "dim_qFR_block": {b: mp.nstr(v, 30) for b, v in canon["dim_qFR_block"].items()},
        "Z_q_normaliser": mp.nstr(canon["Z_q_norm"], 30),
        "alpha_block_LO_canonical": {
            b: mp.nstr(v, 30) for b, v in canon["alpha_block_LO"].items()
        },
        "alpha_eff_LO_canonical": mp.nstr(canon["alpha_eff_LO"], 30),
        "alpha_eff_LO_stale": mp.nstr(stale["alpha_eff_LO"], 30),
    })
    builder.add_data("residuals", {
        "Q_codata_MeV": mp.nstr(Q_BETA_CODATA_MEV, 18),
        "Q_A_MeV": mp.nstr(canon["Q_A"], 18),
        "Q_bridge_canonical_MeV": mp.nstr(canon["Q_bridge"], 18),
        "Q_bridge_stale_MeV": mp.nstr(stale["Q_bridge"], 18),
        "err_canonical_ppb": mp.nstr(canon["err_ppb"], 12),
        "err_stale_ppb": mp.nstr(stale["err_ppb"], 12),
        "q0_drift_pct": drift_pct,
    })
    builder.add_data("verdict", {
        "classification": verdict,
        "q0_stable": drift_pct < 0.01,
        "taylor_exact_at_canonical": abs_err_canon < 0.001,
        "production_action": "Q_β stays at Q_N2 (1279 ppb)" if abs_err_canon >= 0.001
                              else "wire fund-rep eigenphase as Q_β bridge",
    })
    builder.add_assertion(
        "q0_stability_test_completed",
        computed=1.0, expected=1.0, tolerance=0.0,
        source="probe completes regardless of pass/fail; discipline lock applied",
    )
    builder.save()
    print(f"  Witness: qbeta-multi-block-eigenphase-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
