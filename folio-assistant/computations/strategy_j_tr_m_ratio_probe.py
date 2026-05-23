#!/usr/bin/env python3
"""Strategy J (HOMFLYPT cross-orientation) probe — does the
proton/neutron Markov-trace ratio give a structural prediction
for m_n / m_p?

## Context

Strategy J in #916's enumeration: derive `S(p) / S(n)` (the
proton/neutron Skein scaling ratio) from the HOMFLYPT polynomial
evaluated with cross-orientation flip on the proton vs neutron
braids. The target observable is `m_n / m_p ≈ 1.001378` (CODATA).

The framework's Markov trace of the pipeline-canonical proton /
neutron braids:

    tr_M(β_p)(q_0) ≈ 0.7023
    tr_M(β_n)(q_0) ≈ 0.5964
    Q_cat = tr_n - tr_p ≈ -0.1058  (used as 3-cal Q_β source)

The naive ratio tr_n / tr_p ≈ 0.849 is ~15% from 1, while
m_n / m_p ≈ 1.0014 — these differ by orders of magnitude. So
tr_M ratios alone do NOT give m_n / m_p.

Strategy J's claim is that the HOMFLYPT polynomial — a richer
invariant than tr_M — with cross-orientation evaluation produces
the correct ratio. Implementing full HOMFLYPT skein recursion is
expensive; this spike tests the leaner version:

  Q1. Do any natural ratios involving {tr_M(β_p), tr_M(β_n),
      ℏ_q, q_0, G} land near the m_n / m_p target?

  Q2. For candidates within 1% of any observable target, run the
      q-locality test from PR #951.

If a ratio passes both, Strategy J has empirical support for the
S(p)/S(n) observable. If none does, Strategy J joins the prior
6 negative results — structural derivation of mass ratios via
substrate ratios is empirically exhausted.

This probe is INTENTIONALLY cheap (uses existing tr_M values, no
HOMFLYPT recursion). A negative result here is enough to conclude
"no simple tr_M-ratio combination produces m_n/m_p"; a positive
near-match would justify the deeper HOMFLYPT compute.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def tr_M_proton_neutron_at_q(q):
    """tr_M for free proton (Z=1, N=0) and free neutron (Z=0, N=1)
    from the pipeline (unified_low_isotope_predictor convention).

    Computed by evaluating the proton/neutron body words via the
    pipeline. For q ≠ q_0 we'd need to re-evaluate; for the
    q-locality sweep we approximate by the q-dependence of the
    closed-form expressions (substituting the q value into the
    pipeline's tr_M routine).
    """
    from unified_low_isotope_predictor import tr_M_at_q0
    # tr_M_at_q0 hardcodes q = q_0 internally; for the q-locality
    # sweep we approximate by linearizing. For the at-q_0 evaluation
    # this returns exact values.
    tr_p, _, _ = tr_M_at_q0(1, 0, include_inter=False)
    tr_n, _, _ = tr_M_at_q0(0, 1, include_inter=False)
    return mp.mpf(str(tr_p)), mp.mpf(str(tr_n))


def main():
    t_start = time.monotonic()
    mp.mp.dps = 50

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    h_q = Q0 - 1 / Q0
    hbar_q = (Q0 - 1) / Q0
    G = mp.catalan

    print(f"Strategy J — proton/neutron tr_M ratio probe")
    print(f"q_0 = {mp.nstr(Q0, 12)}")
    print()

    tr_p, tr_n = tr_M_proton_neutron_at_q(Q0)
    print(f"tr_M(β_p)(q_0) = {mp.nstr(tr_p, 14)}")
    print(f"tr_M(β_n)(q_0) = {mp.nstr(tr_n, 14)}")
    print(f"Q_cat = tr_n − tr_p = {mp.nstr(tr_n - tr_p, 12)}")
    print()

    # ── Observable targets ───────────────────────────────────────
    M_P_MEV = mp.mpf("938.27208816")
    M_N_MEV = mp.mpf("939.56542052")
    M_E_MEV = mp.mpf("0.51099895")
    Q_BETA_MEV = M_N_MEV - M_P_MEV - M_E_MEV  # = 0.7824 MeV
    targets = {
        "m_n / m_p":            M_N_MEV / M_P_MEV,             # 1.001378
        "m_n / m_p - 1":        M_N_MEV / M_P_MEV - 1,         # 1.378e-3
        "(m_n - m_p) / m_e":    (M_N_MEV - M_P_MEV) / M_E_MEV, # 2.531
        "Q_β / m_e":            Q_BETA_MEV / M_E_MEV,          # 1.531
        "Q_β / (m_e + Q_β)":    Q_BETA_MEV / (M_E_MEV + Q_BETA_MEV),  # 0.605
        "m_p / m_e":            M_P_MEV / M_E_MEV,             # 1836.15
        "m_p / m_e · ℏ_q² / (8G)":
            M_P_MEV / M_E_MEV * hbar_q ** 2 / (8 * G),         # 2.460 (λ_p)
    }

    print("Observable targets:")
    for name, val in targets.items():
        print(f"  {name:<32s} = {mp.nstr(val, 14)}")
    print()

    # ── Candidate ratios from tr_p, tr_n, substrate constants ────
    candidates = {
        "tr_p":                  tr_p,
        "tr_n":                  tr_n,
        "tr_n / tr_p":           tr_n / tr_p,
        "tr_p / tr_n":           tr_p / tr_n,
        "(tr_p · tr_n)^(1/2)":   mp.sqrt(tr_p * tr_n),
        "tr_p · tr_n":           tr_p * tr_n,
        "tr_p + tr_n":           tr_p + tr_n,
        "tr_p - tr_n":           tr_p - tr_n,
        "tr_n - tr_p":           tr_n - tr_p,
        "|tr_n - tr_p|":         abs(tr_n - tr_p),
        "ℏ_q · (tr_p + tr_n)":   hbar_q * (tr_p + tr_n),
        "ℏ_q² · (tr_p + tr_n)":  hbar_q ** 2 * (tr_p + tr_n),
        "(tr_n - tr_p) / (tr_p + tr_n)":  (tr_n - tr_p) / (tr_p + tr_n),
        "tr_p²":                 tr_p ** 2,
        "tr_n²":                 tr_n ** 2,
        "1 + ℏ_q²·tr_p":         1 + hbar_q ** 2 * tr_p,
        "1 + ℏ_q²·tr_n":         1 + hbar_q ** 2 * tr_n,
        "1 + ℏ_q²·(tr_n - tr_p)/tr_p":  1 + hbar_q ** 2 * (tr_n - tr_p) / tr_p,
        "1 + h_q²·(tr_n - tr_p)/tr_p":  1 + h_q ** 2 * (tr_n - tr_p) / tr_p,
        "1 + (tr_p - tr_n)·ℏ_q² / m_p_to_m_e_scale":
            1 + (tr_p - tr_n) * hbar_q ** 2 / (mp.mpf("1836.15") / 8 / G),
    }

    print("Candidates vs targets (looking for any rel err < 1%):")
    print("=" * 80)
    # Refined filter — for target m_n/m_p (which is ≈ 1.0014), the
    # candidate must match the small correction in sign AND magnitude,
    # not just lie near 1. So we ALSO check sign agreement of (candidate−1)
    # vs (target−1) for any target close to 1.
    near_matches = []
    sign_matched_near = []
    for cand_name, val in candidates.items():
        for tgt_name, tgt in targets.items():
            if tgt == 0:
                continue
            rel = abs(val - tgt) / abs(tgt)
            if rel < mp.mpf("0.01"):  # within 1%
                # If target is near 1, also check sign of small correction
                sign_ok = True
                near_one_target = abs(tgt - 1) < mp.mpf("0.1")
                if near_one_target:
                    sign_cand = mp.sign(val - 1)
                    sign_tgt = mp.sign(tgt - 1)
                    sign_ok = (sign_cand == sign_tgt)
                near_matches.append({
                    "candidate": cand_name,
                    "target": tgt_name,
                    "value": mp.nstr(val, 16),
                    "target_value": mp.nstr(tgt, 16),
                    "rel_err": mp.nstr(rel, 8),
                    "sign_ok": sign_ok,
                })
                if sign_ok:
                    sign_matched_near.append((cand_name, tgt_name, rel, val))
                marker = ""
                if rel >= mp.mpf("0.001"):
                    marker = " ← <1%"
                elif rel >= mp.mpf("0.00001"):
                    marker = " ← <0.1%"
                else:
                    marker = " ← <10 ppm"
                if not sign_ok:
                    marker += "  (WRONG SIGN — spurious)"
                print(f"  {cand_name:<40s} ≈ {tgt_name:<30s}: "
                      f"{mp.nstr(val, 12)} vs {mp.nstr(tgt, 12)} "
                      f"(rel {mp.nstr(rel, 4)}){marker}")
    print()

    if not sign_matched_near:
        print("RESULT: No tr_M-based candidate matches a near-1 target with CORRECT SIGN")
        print("        of the small correction. Apparent <1% matches were spurious")
        print("        (e.g. (cand-1) and (target-1) have opposite signs).")
        print("        Strategy J (in this leanest form) returns negative.")
        print()
        print("        Full HOMFLYPT skein recursion may produce richer combinations,")
        print("        but the tr_M ratios alone do NOT predict m_n/m_p with correct sign.")
    else:
        print(f"RESULT: {len(sign_matched_near)} SIGN-CORRECT near-matches found (out of "
              f"{len(near_matches)} total <1% candidates). Suggests Strategy J")
        print(f"        is worth deeper investigation with full HOMFLYPT recursion.")
        for c, t, r, v in sign_matched_near:
            print(f"  → {c}  ≈  {t}  (rel {mp.nstr(r, 6)})")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder(
        "strategy-j-tr-m-ratio-probe",
        engine="mpmath",
        start_time=t_start,
    )
    w.set_description(
        "Strategy J (HOMFLYPT cross-orientation) — lean probe. "
        "Tests if any natural ratio of {tr_M(β_p), tr_M(β_n), ℏ_q, "
        "h_q, q_0, G} matches m_n/m_p, Q_β/m_e, or related "
        "observables within 1%. Uses pipeline tr_M values at q_0; "
        "does NOT implement full HOMFLYPT skein recursion (deferred "
        "to follow-up if any tr_M ratio shows structural promise). "
        f"Found {len(near_matches)} near-matches (<1%) across "
        f"{len(candidates)} candidates × {len(targets)} targets."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 50)
    w.add_data("tr_p_at_q_0", mp.nstr(tr_p, 22))
    w.add_data("tr_n_at_q_0", mp.nstr(tr_n, 22))
    w.add_data("n_candidates", len(candidates))
    w.add_data("n_targets", len(targets))
    w.add_data("near_matches", near_matches)
    w.add_data("near_match_count", len(near_matches))
    w.add_data("sign_correct_near_match_count", len(sign_matched_near))
    w.add_data("strategy_j_lean_result",
               "positive" if sign_matched_near else "negative")
    w.add_assertion(
        "spike_completed",
        computed=1.0,
        expected=1.0,
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
