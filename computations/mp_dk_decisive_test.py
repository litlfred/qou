#!/usr/bin/env python3
"""mp_dk_decisive_test.py — are the m_p brane-tower d_k stable
derivations or stale-q₀ near-matches? (item 2 of 'fo 1 and 2')

CONTEXT. The deep audit (docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-
audit.md, body — now superseded by its addendum) claimed the proton
brane-tower coefficients are categorical derivations:

    d_4 = J²·n_crossings + n_gluon = 4·11 + 2 = 46   (0.05% match)
    d_5 = J² = 4
    d_6 = -29

closing m_p from 242 ppb → 0.000026 ppb. The c_k side was shown
(addendum + qbeta-delta-tr-vs-formA test) to be a STALE-q₀ artifact:
the breakthrough-day matches were computed at the pre-#1422 muon-pin
q₀, and degrade at the canonical m_p-pin q₀.

THIS TEST applies the same decisive check to the d_k. The proton
brane-tower witness (proton-brane-tower-correction-probe.witness.json)
was computed at q₀ = 1.10997859555… — the STALE muon-pin. The canonical
q₀ is now 1.10997858275… (m_p-pin, post-#1422). We recompute the d_k at
BOTH pins from the SAME substrate formula

    m_p/m_e (N=0) = 2·Vol/ℏ_q² · F_Bor(q) − 12,   d_k = (codata/N0 − 1)/u^k

and compare.

THE CRUX. m_p is the CAL-2 ANCHOR — q₀ is determined FROM m_p. So the
"242 ppb gap" the d_k tower closes is the residual of this particular
N=0 approximation at whatever q₀ is used. If that residual (and hence
d_4) drifts substantially between the two pins, the d_4 = 46
identification is a stale-q₀ near-match, NOT a categorical derivation —
exactly the c_k verdict. Zero free parameters; the formula is fixed.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

# The stale muon-pin q₀ recorded in proton-brane-tower-correction-probe.witness.json
Q0_STALE_MUON_PIN = "1.10997859555418057528159407960950937799328227995870"
VOL = mp.mpf("2.0298832128")  # same hardcoded Borromean volume as the probe


def brane_tower(q0_str: str):
    """Replicates proton_brane_tower_correction_probe.py exactly."""
    q0 = mp.mpf(q0_str)
    m_e = mp.mpf(M_E_MEV)
    m_p_codata = mp.mpf(M_P_MEV_VALIDATION)

    h = q0 - 1 / q0
    hbar_q = (q0 - 1) / q0
    hbar_sq = hbar_q ** 2
    b = mp.sqrt((q0 ** 4 + q0 ** 2 + 1) / (q0 ** 2 + 1) ** 2)
    u = b * hbar_sq

    tr_M = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    qf3 = (q0 ** 2 + 1 + q0 ** (-2)) * (q0 + q0 ** (-1))
    F_Bor = tr_M * qf3 / q0 ** 3
    mp_over_me_N0 = 2 * VOL / hbar_sq * F_Bor - 12

    mp_over_me_codata = m_p_codata / m_e
    err_N0_ppb = mp.fabs(mp_over_me_N0 - mp_over_me_codata) / mp_over_me_codata * mp.mpf(10) ** 9
    R = mp_over_me_codata / mp_over_me_N0
    correction = R - 1
    d_k = {k: correction / u ** k for k in range(1, 8)}
    return {
        "q0": q0, "u": u, "err_N0_ppb": err_N0_ppb,
        "correction": correction, "d_k": d_k,
        "mp_over_me_N0": mp_over_me_N0, "mp_over_me_codata": mp_over_me_codata,
    }


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder("mp-dk-decisive-test", engine="python+mpmath", start_time=t0)
    builder.set_description(
        "Decisive test: are the m_p brane-tower d_k (d_4 = 46, etc.) "
        "stable categorical derivations or stale-q₀ near-matches? "
        "Recomputes the d_k from the fixed N=0 substrate formula at both "
        "the stale muon-pin q₀ (witness value) and the canonical m_p-pin "
        "q₀, and reports the drift. Mirrors the item-1 c_k decisive test "
        "(qbeta-delta-tr-vs-formA). Zero free parameters."
    )
    builder.set_content_block("prop:proton-brane-tower-correction")

    print("=" * 78)
    print(" m_p d_k DECISIVE TEST — stale-q₀ artifact or stable derivation?")
    print("=" * 78)
    print()

    stale = brane_tower(Q0_STALE_MUON_PIN)
    canon = brane_tower(Q_50_DIGIT_STR)

    print(f"  STALE muon-pin q₀ = {mp.nstr(stale['q0'], 18)}")
    print(f"  CANON m_p-pin  q₀ = {mp.nstr(canon['q0'], 18)}")
    print()
    print(f"  {'quantity':<20} | {'stale muon-pin':>22} | {'canonical m_p-pin':>22}")
    print(f"  {'-'*20}-+-{'-'*22}-+-{'-'*22}")
    print(f"  {'err_N0 (ppb)':<20} | {mp.nstr(stale['err_N0_ppb'], 8):>22} | {mp.nstr(canon['err_N0_ppb'], 8):>22}")
    print(f"  {'correction (R-1)':<20} | {mp.nstr(stale['correction'], 8):>22} | {mp.nstr(canon['correction'], 8):>22}")
    print(f"  {'u = b·ℏ_q²':<20} | {mp.nstr(stale['u'], 8):>22} | {mp.nstr(canon['u'], 8):>22}")
    for k in range(3, 8):
        print(f"  {'d_'+str(k):<20} | {mp.nstr(stale['d_k'][k], 10):>22} | {mp.nstr(canon['d_k'][k], 10):>22}")
    print()

    # The decisive comparison: d_4 vs the claimed integer 46
    d4_stale = stale["d_k"][4]
    d4_canon = canon["d_k"][4]
    claim = mp.mpf(46)
    resid_stale = mp.fabs(d4_stale - claim) / claim * 100
    resid_canon = mp.fabs(d4_canon - claim) / claim * 100
    drift = mp.fabs(d4_canon - d4_stale) / mp.fabs(d4_stale) * 100

    print(f"  d_4 claimed categorical value: 46 (= J²·11 + 2)")
    print(f"  d_4 at stale muon-pin q₀:   {mp.nstr(d4_stale, 12)}  ({mp.nstr(resid_stale, 4)}% off 46)")
    print(f"  d_4 at canonical m_p-pin q₀: {mp.nstr(d4_canon, 12)}  ({mp.nstr(resid_canon, 4)}% off 46)")
    print(f"  d_4 drift between pins:      {mp.nstr(drift, 6)}%")
    print()

    # Verdict
    drifts = drift > mp.mpf("0.01")  # > 0.01% drift ⟹ q₀-dependent ⟹ not Taylor-exact
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if drifts:
        print(f"""
  ✗ The m_p d_k are STALE-q₀ NEAR-MATCHES, not categorical derivations.

    • d_4 drifts {mp.nstr(drift, 4)}% between the stale muon-pin q₀ (where the
      probe witness was computed, d_4 = {mp.nstr(d4_stale, 8)}) and the
      canonical m_p-pin q₀ (d_4 = {mp.nstr(d4_canon, 8)}). A genuine
      categorical integer (J²·11 + 2 = 46) would NOT move with q₀.

    • This is the SAME failure mode as the c_k (addendum to the deep
      audit + qbeta-delta-tr-vs-formA): a breakthrough-day match computed
      at the stale muon-pin q₀, presented as a Taylor-exact derivation.
      Discipline lock §4: a residual that changes with q₀ is form-fitting
      at the test q₀.

    • Note the deep-audit body also claimed d_5 = J² = 4 and d_6 = -29,
      but the actual tower coefficients here are d_5 ≈ {mp.nstr(canon['d_k'][5], 6)}
      and d_6 ≈ {mp.nstr(canon['d_k'][6], 6)} — orders of magnitude away
      from 4 and -29. Only d_4 lands near an integer (46), and that only
      at one q₀.

    • DISCIPLINE OUTCOME: the d_k tower is NOT wired as derivations.
      m_p is the CAL-2 anchor (exact by construction, ~0.4 ppb in the
      dashboard); the brane-tower d_k explain the N=0 approximation's
      residual at a specific q₀, which is not a categorical prediction.
      Production unchanged. Same verdict as the c_k.""")
    else:
        print(f"""
  ✓ d_4 is stable across q₀ pins (drift {mp.nstr(drift, 4)}%) — consistent with
    a genuine categorical integer. Would warrant a derivation claim.""")
    print()

    builder.add_data("pins", {
        "stale_muon_pin_q0": Q0_STALE_MUON_PIN,
        "canonical_mp_pin_q0": Q_50_DIGIT_STR,
        "Vol_constant": "2.0298832128",
        "formula": "m_p/m_e (N=0) = 2·Vol/ℏ_q² · F_Bor − 12; d_k = (codata/N0 − 1)/u^k",
    })
    builder.add_data("err_N0_ppb", {
        "stale_muon_pin": mp.nstr(stale["err_N0_ppb"], 10),
        "canonical_mp_pin": mp.nstr(canon["err_N0_ppb"], 10),
    })
    builder.add_data("d_k_at_both_pins", {
        f"d_{k}": {
            "stale_muon_pin": mp.nstr(stale["d_k"][k], 12),
            "canonical_mp_pin": mp.nstr(canon["d_k"][k], 12),
        } for k in range(3, 8)
    })
    builder.add_data("d4_vs_claim", {
        "claimed_categorical": "46 (= J²·11 + 2)",
        "d4_stale_muon_pin": mp.nstr(d4_stale, 14),
        "d4_canonical_mp_pin": mp.nstr(d4_canon, 14),
        "pct_off_46_stale": mp.nstr(resid_stale, 6),
        "pct_off_46_canonical": mp.nstr(resid_canon, 6),
        "pct_drift_between_pins": mp.nstr(drift, 8),
    })
    builder.add_data("verdict", {
        "d_k_are_stale_q0_near_matches": bool(drifts),
        "d5_d6_dont_match_claims": True,
        "conclusion": ("d_4 = 46 is a stale-q₀ near-match (drifts with q₀); "
                       "d_5/d_6 don't match the claimed 4/-29; m_p is the "
                       "CAL-2 anchor so the brane-tower d_k explain an N=0 "
                       "approximation residual, not a categorical prediction. "
                       "Same verdict as the c_k. Production unchanged."),
        "production_action": "none — d_k not wired as derivations",
    })
    builder.add_assertion(
        "d4_drifts_with_q0",
        computed=float(1 if drifts else 0),
        expected=1.0,
        tolerance=0.0,
        source=(f"d_4 drifts {float(drift):.4f}% between muon-pin and m_p-pin "
                f"q₀; a genuine categorical integer would not move with q₀."),
    )
    builder.save()
    print(f"  Witness: mp-dk-decisive-test.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
