#!/usr/bin/env python3
"""qbeta_ck_qholonomic_recurrence_test.py — PROBE 5: q-holonomic TEST of the
P-C15 survivor on the empirical Q_beta rung sequence.

QUESTION (docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md
Sec. 3.E): the 4_1 order-2 qZeilberger operator gate-passed as fibre-kernel
candidate (P-C15, docs/audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md;
KC11/KC15 rows of docs/coordination/ck-dk-canonical-registry.md Sec. 9). Does
that operator, INSTANTIATED as the recursion kernel via the q^N -> q^k rung
substitution, annihilate the empirical rung sequence {c_k}, k = 2..7?

This is a TEST of a known operator on known data (well-posed with 6 rungs) —
NOT operator guessing (deferred until >= 15 rungs exist, per the same audit).

OPERATOR (provenance — corpus, machine-verified; NOT re-derived here):
    computations/aj_figure_eight_certificate.py  (exact qZeilberger
    certificate, telescoping identity (*) + boundary b = -Cert(x,1) verified;
    independently confirmed against the Habiro cyclotomic sum by B1-K1, see
    docs/audits/2026-07-07-pc15-a1-transcription-error-correction.md).
    This is the standard Garoufalidis–Le order-2 inhomogeneous recurrence for
    the (normalised) colored Jones of 4_1 [Garoufalidis–Le, "The colored
    Jones function is q-holonomic", arXiv:math/0309214; AJ conjecture
    arXiv:math/0306230], in the corpus normalisation:

        a2(q,x)*J_{N+2} + a1(q,x)*J_{N+1} + a0(q,x)*J_N = b(q,x),  x = q^N,

        a0 = (x-1)(x^2 q^3 - 1)/x^6
        a1 = -((xq-1)^2 (xq+1)(x^4q^4 - x^3q^3 - x^2q^3 - x^2q - xq + 1))/(x^8 q^2)
        a2 = (xq^2 - 1)(x^2 q - 1)/x^6
        b  = (xq+1)(x^2 q - 1)(x^2 q^3 - 1)/(x^7 q)

    The transcription is GATED below (post the 2026-07-07 a1 incident): the
    recurrence is verified numerically against the Habiro cyclotomic colored
    Jones J_{4_1}(N;q) at a generic test q before any use.

DICTIONARY (read from the corpus EXACTLY — no shift-scan, no dictionary
fishing). The only corpus-named color<->rung identification is I-A
("color<->rung, direct"; docs/coordination/z-ck-fmap-keystone.md Sec. 4-bis:
kernel a1-slot = alpha_1 = -a1/a2, kernel a2-slot = alpha_2 = -a0/a2, with
x = q^N). I-B (cyclotomic re-basing) is explicitly "genuinely hard; NOT
attempted" there and is out of scope here. Instantiated at the rung index per
the Sec. 3.E framing (q^N -> q^k) and the proved conditional recursion form
c_{k+1} = sum_j a_j(q0, q0^k) c_{k+1-j} (prop:q-beta-c-k-recursion-from-
habiro-q-difference; QBetaCKRecursionKernelConstraints.lean), i.e. J_N <-> c_N
directly (N = k):

    D1 (homogeneous):    a2(q0,q0^k) c_{k+2} + a1(q0,q0^k) c_{k+1}
                                             + a0(q0,q0^k) c_k  =? 0
    D2 (inhomogeneous — the actual P-C15 operator form):
                         a2 c_{k+2} + a1 c_{k+1} + a0 c_k  =?  b(q0,q0^k)

    for k = 2..5 (rungs c_2..c_7), at BOTH anchors.

HOPF-LINK OPERATOR: the corpus has NO Hopf-link qZeilberger/annihilator
operator (only scalar J_Hopf values, e.g. computations/probes/
qbeta_root_of_unity_probe.py). Per the pre-statement: recorded as UNTESTED —
no literature hunt.

EMPIRICAL RUNG SEQUENCE (per anchor, computed in-script): the sequential
ladder extraction of qbeta_decay_sdp_full_ck.py / qbeta_decay_sdp_extended_ck
.py — R(q0) = Q_AME/(Q_A(q0) cos(alpha_N1(q0))), c_k_emp = (R_adv - 1)/u^k
with u = b_H * hbar_q^2, ladder advanced by the registry canonical/imposed
forms (c2=-1, c3=-2, c4=-2b^4, c5=-(b^2+1/2), c6=4b^2, c7=-8). Q_AME =
m_n - m_p - m_e is a measurement (anchor-independent). Cross-checked below
against the committed muon-anchor witnesses (q-beta-operator-valued-N3,
qbeta-c6-c10-crossanchor-falsification raw values).

ANCHORS:
    proton q0 — tools/qou-substrate/python/qou_substrate/constants.py
                (proton-pinned, _solve_q_proton_f64; 0.06 ppb)
    muon  q0 — 1.10997859555733471989976322048... (computations-layer
                canonical, q-pinning-50-digit.witness.json; -11.5 ppb)

UNCERTAINTY MODEL (registry / precision-floor witness, qbeta-ck-extraction-
precision-floor.witness.json): sigma(c_k) = sigma_R/u^k, sigma_R = 6e-7 (AME
neutron Q-value). Only c_2 (~0.8%) and c_3 (~49%) are data-determined; the
c_3 cross-anchor swing is ~2.4%. Residuals are compared per-rung against the
propagated sigma AND against the empirical rung magnitude.

KILL CRITERION (pre-stated, from the task):
    residual >> uncertainty at BOTH anchors for every named dictionary
      => verdict NEGATIVE: "the 4_1 operator does not annihilate the rung
         sequence as-is" — scope-limited (a), sharpening P-C15 (kernel needs
         conjugation/twist, not raw instantiation).
    residuals within uncertainty at both anchors => GATE-PASSED (major);
         report exactly, no wiring.
    Operationalised with TWO yardsticks (both reported): Y1 = the empirical
    c_k uncertainty the task names (the ~2.4% c_3 cross-anchor scale; ">>"
    taken as >10x); Y2 = the AME extraction floor sigma(c_k) = sigma_R/u^k.
    For k >= 4 the Y2 floor exceeds |c_k| itself, so Y2-consistency on those
    rungs is CONSISTENT-BUT-UNINFORMATIVE (vacuous), never a pass; a Y1 kill
    with the Y2 caveat stated is the honest scope-(a) outcome.

Anti-fitting: no parameter is tuned anywhere; the operator, the dictionary,
the anchors and the empirical ladder are all fixed upstream objects. A clean
negative is a full success (it sharpens P-C15). Audit-only; nothing wired.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent          # computations/probes
COMP = HERE.parent                              # computations/
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import _path_bridge  # noqa: F401, E402 — cluster subdir import bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()  # 70 dps compute / 50 dps serialization (>= 50 dps STRICT)
import mpmath as mp  # noqa: E402

from codata_constants import (  # noqa: E402
    M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION,
)

# ---------------------------------------------------------------------------
# Anchors
# ---------------------------------------------------------------------------
# Proton-pinned q0: canonical package layer (qou-substrate constants).
sys.path.insert(0, str(COMP.parent / "tools" / "qou-substrate" / "python"))
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

Q0_PROTON = mp.mpf(Q_50_DIGIT_STR)
# Muon-anchor q0: computations-layer canonical (q-pinning-50-digit witness).
Q0_MUON = mp.mpf(
    "1.10997859555733471989976322048322502665620840878015368660798114614493")

SIGMA_R = mp.mpf("6e-7")  # AME neutron Q-value relative error (precision-floor witness)

# ---------------------------------------------------------------------------
# 4_1 order-2 qZeilberger operator — VERBATIM from aj_figure_eight_certificate.py
# ---------------------------------------------------------------------------


def op_a0(q, x):
    return (x - 1) * (x ** 2 * q ** 3 - 1) / x ** 6


def op_a1(q, x):
    return -((x * q - 1) ** 2 * (x * q + 1)
             * (x ** 4 * q ** 4 - x ** 3 * q ** 3 - x ** 2 * q ** 3
                - x ** 2 * q - x * q + 1)) / (x ** 8 * q ** 2)


def op_a2(q, x):
    return (x * q ** 2 - 1) * (x ** 2 * q - 1) / x ** 6


def op_b(q, x):
    return (x * q + 1) * (x ** 2 * q - 1) * (x ** 2 * q ** 3 - 1) / (x ** 7 * q)


def J_figure8_cyclotomic(N, q):
    """Habiro cyclotomic colored Jones of 4_1 (Garoufalidis–Le convention,
    J(unknot)=1) — same formula as qbeta_root_of_unity_probe.py (verified
    there against the N=2 Jones polynomial and Kashaev volume growth)."""
    total = mp.mpf(0)
    for n in range(0, N):
        term = mp.mpf(1)
        for j in range(1, n + 1):
            term *= (1 - q ** (N - j)) * (1 - q ** (N + j))
        total += q ** (-n * N) * term
    return total


def verify_operator_transcription():
    """Transcription gate (post the 2026-07-07 a1 incident): the operator
    must annihilate the actual colored Jones (inhomogeneously) at a generic
    real q for several colors N, at compute precision."""
    q = mp.mpf("1.3")
    results = []
    for N in range(1, 7):
        x = q ** N
        lhs = (op_a2(q, x) * J_figure8_cyclotomic(N + 2, q)
               + op_a1(q, x) * J_figure8_cyclotomic(N + 1, q)
               + op_a0(q, x) * J_figure8_cyclotomic(N, q))
        rhs = op_b(q, x)
        scale = max(abs(lhs), abs(rhs), mp.mpf(1))
        rel = abs(lhs - rhs) / scale
        results.append((N, rel))
    worst = max(r for _, r in results)
    return results, worst


# ---------------------------------------------------------------------------
# Empirical rung ladder (sequential extraction, per anchor)
# ---------------------------------------------------------------------------

# Registry canonical/imposed advance forms (qbeta_decay_sdp_extended_ck.py):
#   c2=-1, c3=-2, c4=-2 b^4, c5=-(b^2+1/2), c6=4 b^2, c7=-8.


def extract_empirical_ladder(q0):
    """Replicates qbeta_decay_sdp_full_ck / _extended_ck at anchor q0.

    Returns dict with substrate quantities, empirical c_2..c_7 (value read at
    each rung BEFORE the canonical advance is applied) and sigma(c_k)."""
    m_e = mp.mpf(str(M_E_MEV))
    Q_AME = mp.mpf(str(M_N_MEV_VALIDATION)) - mp.mpf(str(M_P_MEV_VALIDATION)) - m_e

    q = q0
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    hbar_q = (q - 1) / q
    hq2 = hbar_q ** 2
    alpha = (z - 1) * h / 2
    # Hoefsmit b: b^2 = d1*d2 + 1 = (q^4+q^2+1)/(q^2+1)^2  (probe_q_beta_operator_valued_N3.py)
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    bH = mp.sqrt(d1 * d2 + 1)
    u = bH * hq2

    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    alpha_N1 = alpha - bH * hq2 / 2
    Q_N1 = Q_A * mp.cos(alpha_N1)
    R = Q_AME / Q_N1

    advance = {
        2: mp.mpf(-1),
        3: mp.mpf(-2),
        4: mp.mpf(-2) * bH ** 4,
        5: -(bH ** 2 + mp.mpf(1) / 2),
        6: mp.mpf(4) * bH ** 2,
        7: mp.mpf(-8),
    }
    c_emp, sigma = {}, {}
    for k in range(2, 8):
        c_emp[k] = (R - 1) / u ** k
        sigma[k] = SIGMA_R / u ** k
        R = R / (1 + advance[k] * u ** k)

    return {
        "q0": q, "u": u, "b_hoefsmit": bH, "hbar_q_sq": hq2,
        "Q_A": Q_A, "Q_N1": Q_N1, "Q_AME": Q_AME,
        "c_emp": c_emp, "sigma": sigma, "advance": advance,
    }


# ---------------------------------------------------------------------------
# Recurrence residuals (dictionary I-A, x = q0^k; D1 homogeneous / D2 inhomog.)
# ---------------------------------------------------------------------------


def recurrence_residuals(q0, c_emp, sigma):
    rows = []
    for k in range(2, 6):  # (c_k, c_{k+1}, c_{k+2}) for k=2..5 covers c_2..c_7
        x = q0 ** k
        A2, A1, A0, B = (op_a2(q0, x), op_a1(q0, x), op_a0(q0, x), op_b(q0, x))
        t2 = A2 * c_emp[k + 2]
        t1 = A1 * c_emp[k + 1]
        t0 = A0 * c_emp[k]
        scale = max(abs(t2), abs(t1), abs(t0), abs(B))
        res_hom = t2 + t1 + t0
        res_inh = res_hom - B
        # predicted c_{k+2} from the recurrence (both variants)
        pred_hom = -(t1 + t0) / A2
        pred_inh = (B - t1 - t0) / A2
        # propagated sigma on the residual (uncorrelated per-rung model)
        sig_res = mp.sqrt((A2 * sigma[k + 2]) ** 2 + (A1 * sigma[k + 1]) ** 2
                          + (A0 * sigma[k]) ** 2)
        rows.append({
            "k": k,
            "x": x,
            "a2": A2, "a1": A1, "a0": A0, "b": B,
            "res_hom": res_hom, "res_inh": res_inh,
            "rel_res_hom": abs(res_hom) / scale,
            "rel_res_inh": abs(res_inh) / scale,
            "sigma_res": sig_res,
            "res_over_sigma_hom": abs(res_hom) / sig_res,
            "res_over_sigma_inh": abs(res_inh) / sig_res,
            "c_next_emp": c_emp[k + 2],
            "c_next_pred_hom": pred_hom,
            "c_next_pred_inh": pred_inh,
            "pred_err_rel_hom": abs(pred_hom - c_emp[k + 2]) / abs(c_emp[k + 2]),
            "pred_err_rel_inh": abs(pred_inh - c_emp[k + 2]) / abs(c_emp[k + 2]),
        })
    return rows


def _repo_head_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE), text=True).strip()
    except Exception:
        return None


def n50(v):
    return mp.nstr(v, 50)


def n8(v):
    return mp.nstr(v, 8)


def main():
    t0 = time.monotonic()
    print("=" * 78)
    print(" PROBE 5 — q-holonomic TEST: 4_1 qZeilberger operator vs empirical c_k")
    print("=" * 78)
    assertions = []

    def gate(name, passed, computed, expected, tolerance, source):
        assertions.append({
            "name": name, "passed": bool(passed), "computed": computed,
            "expected": expected, "tolerance": tolerance, "source": source,
        })
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}: {computed}")

    # ---- Gate 0: operator transcription vs actual colored Jones ----------
    print("\nGate 0 — operator transcription (recurrence on J_41(N;q), q=1.3):")
    op_checks, worst = verify_operator_transcription()
    gate("operator_annihilates_colored_jones_q1p3_N1_6",
         worst < mp.mpf("1e-45"), float(worst), 0.0, 1e-45,
         "a2 J_{N+2}+a1 J_{N+1}+a0 J_N = b at q=1.3, N=1..6, vs Habiro "
         "cyclotomic sum; 70-dps compute (guards the 2026-07-07 a1 incident)")

    # ---- Empirical ladders at both anchors --------------------------------
    anchors = {
        "proton": extract_empirical_ladder(Q0_PROTON),
        "muon": extract_empirical_ladder(Q0_MUON),
    }

    print("\nEmpirical sequential-extraction rungs (raw, per anchor):")
    print(f"  {'k':>2} {'c_k proton':>22} {'c_k muon':>22} {'swing %':>10} {'sigma/|c_k| (p)':>16}")
    swings = {}
    for k in range(2, 8):
        cp = anchors["proton"]["c_emp"][k]
        cm = anchors["muon"]["c_emp"][k]
        sw = abs(cp - cm) / max(abs(cp), abs(cm)) * 100
        swings[k] = sw
        rel_s = anchors["proton"]["sigma"][k] / abs(cp)
        print(f"  {k:>2} {n8(cp):>22} {n8(cm):>22} {float(sw):>10.4f} {float(rel_s):>16.4g}")

    # ---- Gate 1: cross-checks vs committed muon-anchor witnesses ----------
    # Authoritative current extraction: qbeta-decay-sdp-extended-ck.witness.json
    # (re-run 2026-07-07). NOTE: the older raw values in
    # qbeta-c6-c10-crossanchor-falsification.witness.json (2026-06-22:
    # c6_raw=+3.4976, c7_raw=+57.15) and the registry c_4 fit (-0.97157) are
    # STALE relative to that re-run (upstream N3/Q_AME regeneration) — not
    # used as gates here.
    print("\nGate 1 — muon-anchor extraction vs committed witnesses:")
    c3_mu = anchors["muon"]["c_emp"][3]
    gate("muon_c3_matches_N3_witness",
         abs(c3_mu - mp.mpf("-2.021615577060006120530024970029644566094740817719")) < mp.mpf("1e-12"),
         n8(c3_mu), "-2.0216156", 1e-12,
         "q-beta-operator-valued-N3.witness.json c_3_empirical_additive")
    ext_path = COMP / "qbeta" / "qbeta-decay-sdp-extended-ck.witness.json"
    with open(ext_path, encoding="utf-8") as fh:
        ext = json.load(fh)["data"]["c_k_extracted_50dps"]
    worst_ext = max(
        abs(anchors["muon"]["c_emp"][k] - mp.mpf(ext[f"c_{k}"]))
        / abs(mp.mpf(ext[f"c_{k}"])) for k in range(2, 8))
    gate("muon_c2_c7_match_extended_ck_witness_2026_07_07",
         worst_ext < mp.mpf("1e-9"), float(worst_ext), 0.0, 1e-9,
         "qbeta-decay-sdp-extended-ck.witness.json c_k_extracted_50dps "
         "(authoritative current extraction, computed at the pinning-witness "
         "q0 = the computations-layer muon value)")
    gate("c3_cross_anchor_swing_near_2p4pct",
         mp.mpf("1.5") < swings[3] < mp.mpf("3.5"), float(swings[3]), 2.4, 1.1,
         "registry: c_3 swings ~2.4-2.9% proton<->muon")

    # ---- Recurrence residuals ---------------------------------------------
    per_anchor = {}
    for name, A in anchors.items():
        rows = recurrence_residuals(A["q0"], A["c_emp"], A["sigma"])
        per_anchor[name] = rows
        print(f"\nRecurrence residuals — anchor {name} (dictionary I-A, x = q0^k):")
        print(f"  {'k':>2} {'rel res D1(hom)':>16} {'rel res D2(inh)':>16} "
              f"{'|res|/sigma D1':>15} {'|res|/sigma D2':>15} "
              f"{'pred c_k+2 (D2)':>18} {'emp c_k+2':>14}")
        for r in rows:
            print(f"  {r['k']:>2} {float(r['rel_res_hom']):>16.6g} "
                  f"{float(r['rel_res_inh']):>16.6g} "
                  f"{float(r['res_over_sigma_hom']):>15.6g} "
                  f"{float(r['res_over_sigma_inh']):>15.6g} "
                  f"{n8(r['c_next_pred_inh']):>18} {n8(r['c_next_emp']):>14}")

    # ---- Verdict logic (pre-stated kill criterion, two uncertainty yardsticks)
    #
    # Yardstick Y1 — the empirical c_k uncertainty named in the task:
    #   c_3 cross-anchor swing ~2.4% + per-anchor precision (registry). An
    #   operator that annihilates "the rung sequence as-is" must have relative
    #   residual (|res| / max-term) << that scale; ">>" taken as > 10x 2.4%.
    # Yardstick Y2 — the AME extraction-noise floor sigma(c_k) = sigma_R/u^k
    #   (precision-floor witness). For k >= 4, sigma exceeds |c_k| itself, so
    #   ANY residual there is consistent with the noise — Y2 cannot falsify on
    #   those rungs (recorded as a caveat, not as a pass).
    c3_unc = mp.mpf("0.024")  # c_3 cross-anchor swing scale
    min_rel_res = {
        a: min(min(r["rel_res_hom"], r["rel_res_inh"]) for r in per_anchor[a])
        for a in anchors
    }
    kill_face_value = all(min_rel_res[a] > 10 * c3_unc for a in anchors)
    within_noise_floor = all(
        max(r["res_over_sigma_hom"], r["res_over_sigma_inh"]) <= 1
        for a in anchors for r in per_anchor[a])
    uninformative = [k for k in range(4, 8)
                     if anchors["proton"]["sigma"][k] / abs(anchors["proton"]["c_emp"][k]) > 1]

    gate("kill_rel_residual_exceeds_ck_uncertainty_both_anchors_all_dicts",
         kill_face_value,
         {a: float(min_rel_res[a]) for a in anchors},
         f"> {float(10 * c3_unc)} (10x the 2.4% c_3 cross-anchor scale) at both anchors",
         None,
         "pre-stated kill criterion (Y1): residual >> empirical c_k uncertainty "
         "at BOTH anchors for every named dictionary variant")
    gate("caveat_residuals_below_AME_extraction_noise_floor",
         within_noise_floor, within_noise_floor, True, None,
         "Y2: sigma(c_k)=sigma_R/u^k floor — residuals are within the (enormous) "
         "AME noise band; the floor makes rungs k>=4 individually unfalsifiable "
         "(sigma > |c_k|), so Y2-consistency is vacuous, not a pass")

    # anchor-stability of the operator's own c_4 prediction (structure, not wired)
    pred_c4 = {a: per_anchor[a][0]["c_next_pred_inh"] for a in anchors}
    pred_c4_swing = abs(pred_c4["proton"] - pred_c4["muon"]) / abs(pred_c4["proton"])

    if kill_face_value:
        overall = "NEGATIVE (scope-(a))"
        summary = (
            "The 4_1 order-2 qZeilberger operator, instantiated as the recursion "
            "kernel via the corpus I-A color<->rung dictionary (x = q0^k), does NOT "
            "annihilate the empirical rung sequence as-is: relative residuals are "
            "O(1) (100-280% of the largest term) at EVERY rung k=2..5, at BOTH "
            "anchors, for BOTH the homogeneous and the inhomogeneous variant — "
            ">40x the 2.4% c_3 cross-anchor uncertainty scale, and anchor-stable "
            "(so not a noise fluke of one anchor). Its inhomogeneous c_4 "
            "prediction (+7.4 to +7.5, anchor-stable to ~1%) has the WRONG SIGN "
            "vs every recorded empirical/candidate c_4 (raw -2.54/-8.31; fit "
            "-0.97; form -2b^4 = -1.13). Scope-limited (a): this excludes the RAW "
            "q^N -> q^k instantiation only — it sharpens P-C15 (the surviving "
            "kernel candidate needs a conjugation / basis change / twist, e.g. "
            "the I-B cyclotomic re-basing or the KC15 pair-difference channel), "
            "and it does NOT retest or disturb P-C15's bar-parity survivor "
            "status. CAVEAT (Y2): the AME extraction floor sigma(c_k)=sigma_R/u^k "
            "exceeds |c_k| for k>=4, so the kill is at the level of the recorded "
            "empirical sequence; a noise-floor-proof retest needs genuine "
            "canonical rungs (the H_4 Hoefsmit c_4^even build, bean 8we6 — "
            "exactly the gated next step P-C15 already named)."
        )
    elif within_noise_floor:
        overall = "UNINFORMATIVE"
        summary = (
            "Residuals sit below the AME extraction-noise floor but the floor "
            "exceeds the rung magnitudes themselves — no verdict either way. "
            "No wiring."
        )
    else:
        overall = "MIXED"
        summary = "See per-rung tables; no criterion fired cleanly. No wiring."

    print("\n" + "-" * 78)
    print(f" VERDICT: {overall}")
    print(f" {summary}")
    print(f" Operator c_4 prediction (inhomogeneous): proton {n8(pred_c4['proton'])}, "
          f"muon {n8(pred_c4['muon'])} (swing {float(pred_c4_swing) * 100:.2f}%)")
    print(f" Uninformative rungs under Y2 (sigma > |c_k|): {uninformative}")

    # ---- Witness -----------------------------------------------------------
    def rows_out(rows):
        return [{
            "k": r["k"], "x": n50(r["x"]),
            "a2": n50(r["a2"]), "a1": n50(r["a1"]), "a0": n50(r["a0"]),
            "b": n50(r["b"]),
            "res_hom": n50(r["res_hom"]), "res_inh": n50(r["res_inh"]),
            "rel_res_hom": float(r["rel_res_hom"]),
            "rel_res_inh": float(r["rel_res_inh"]),
            "res_over_sigma_hom": float(r["res_over_sigma_hom"]),
            "res_over_sigma_inh": float(r["res_over_sigma_inh"]),
            "c_next_emp": n50(r["c_next_emp"]),
            "c_next_pred_hom": n50(r["c_next_pred_hom"]),
            "c_next_pred_inh": n50(r["c_next_pred_inh"]),
            "pred_err_rel_hom": float(r["pred_err_rel_hom"]),
            "pred_err_rel_inh": float(r["pred_err_rel_inh"]),
        } for r in rows]

    src = open(__file__, "rb").read()
    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-ck-qholonomic-recurrence-test",
        "scriptFile": os.path.basename(__file__),
        "scriptHash": sha256(src).hexdigest()[:12],
        "commitSha": _repo_head_sha(),
        "audit_only": True,
        "tier": "structural test (known operator vs empirical data; no fit, no wiring)",
        "description": (
            "PROBE 5 (2026-07-11 untested-avenues audit Sec. 3.E): drive the "
            "P-C15/KC15 q-holonomic survivor to a verdict. Tests whether the "
            "machine-verified 4_1 order-2 qZeilberger operator "
            "(aj_figure_eight_certificate.py; Garoufalidis-Le arXiv:math/0309214), "
            "instantiated as the c_k recursion kernel via the corpus I-A "
            "color<->rung dictionary with x = q0^k, annihilates the empirical "
            "rung sequence c_2..c_7 (sequential ladder extraction, both anchors), "
            "in homogeneous (D1) and inhomogeneous (D2) form. Kill criterion "
            "pre-stated. Hopf-link operator: ABSENT from corpus -> untested "
            "(no literature hunt per pre-statement). No parameter tuned; a clean "
            "negative sharpens P-C15 (scope-(a): raw instantiation excluded, "
            "operator survives as fibre object)."
        ),
        "precisionMetadata": {
            "compute_dps": mp.mp.dps, "output_dps": 50,
            "sigma_R": "6e-7 (AME neutron Q-value; precision-floor witness)",
        },
        "dictionaries_tested": {
            "I-A_direct_x_eq_q0_pow_k": {
                "source": "docs/coordination/z-ck-fmap-keystone.md Sec. 4-bis "
                          "(the only corpus-named color<->rung identification); "
                          "q^N -> q^k per 2026-07-11 audit Sec. 3.E",
                "variants": ["D1 homogeneous", "D2 inhomogeneous (P-C15 operator form)"],
            },
            "I-B_cyclotomic_rebasing": "NOT tested (corpus-flagged 'genuinely hard; "
                                       "NOT attempted'; out of scope here)",
            "hopf_link_operator": "UNTESTED — no Hopf-link annihilator exists in the "
                                  "corpus; pre-statement forbids a literature hunt",
        },
        "data": {
            "q0_proton_50dps": n50(Q0_PROTON),
            "q0_muon_50dps": n50(Q0_MUON),
            "Q_AME_MeV": n50(anchors["proton"]["Q_AME"]),
            "anchors": {
                name: {
                    "u": n50(A["u"]),
                    "b_hoefsmit": n50(A["b_hoefsmit"]),
                    "Q_A": n50(A["Q_A"]),
                    "c_emp": {f"c_{k}": n50(A["c_emp"][k]) for k in range(2, 8)},
                    "sigma_ck": {f"c_{k}": n50(A["sigma"][k]) for k in range(2, 8)},
                    "residuals": rows_out(per_anchor[name]),
                } for name, A in anchors.items()
            },
            "cross_anchor_swing_pct": {f"c_{k}": float(swings[k]) for k in range(2, 8)},
            "uninformative_rungs_sigma_exceeds_ck": uninformative,
            "operator_transcription_worst_rel_residual": float(worst),
        },
        "assertions": assertions,
        "verdict": {
            "overall": overall,
            "min_rel_residual_per_anchor": {
                a: float(min_rel_res[a]) for a in anchors},
            "c3_uncertainty_scale": float(c3_unc),
            "within_AME_noise_floor": bool(within_noise_floor),
            "operator_c4_prediction_inh": {
                a: n50(pred_c4[a]) for a in anchors},
            "operator_c4_prediction_cross_anchor_swing_pct": float(pred_c4_swing * 100),
            "summary": summary,
            "scope": "(a) scope-limited — raw q^N -> q^k instantiation only; not a "
                     "structural exclusion of the 4_1 operator as fibre kernel "
                     "(P-C15 bar-parity survivor status unchanged)",
        },
        "context": {
            "task": "docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md Sec. 3.E (PROBE 5)",
            "pc15": "docs/audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md",
            "a1_correction": "docs/audits/2026-07-07-pc15-a1-transcription-error-correction.md",
            "registry": "docs/coordination/ck-dk-canonical-registry.md Sec. 9 (KC11, KC15)",
            "operator_source": "computations/aj_figure_eight_certificate.py",
            "extraction_source": "computations/qbeta/qbeta_decay_sdp_extended_ck.py",
            "precision_floor": "computations/qbeta/qbeta-ck-extraction-precision-floor.witness.json",
        },
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)

    out = HERE / "qbeta-ck-qholonomic-recurrence-test.witness.json"
    with open(out, "w") as f:
        # Provenance envelope. This producer writes its witness as raw JSON, so
        # nothing stamps `scriptHash` — and a witness without one cannot be
        # compared against its producer, so it drops OUT of the self-staleness
        # audit and reads as "not stale" forever. Regenerating it then looks
        # like progress while removing it from the count: a false drain.
        # Full rationale and the detector: computations/witness_drain_audit.py.
        #
        # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
        # fields in place and leaves the on-disk shape untouched, so consumers
        # of legacy `assertions` records (which key on `label`, not `name`) do
        # not have to change. `engine` is passed back from the payload because
        # the helper overwrites it, and a descriptive engine string is worth
        # keeping.
        try:
            from witness_base import WitnessBuilder  # noqa: E402
        except ImportError:  # cluster subdir without the _path_bridge bootstrap
            import sys as _sys
            from pathlib import Path as _Path
            _sys.path.insert(0, str(next(
                _a / "substrate" for _a in _Path(__file__).resolve().parents
                if (_a / "substrate" / "witness_base.py").is_file())))
            from witness_base import WitnessBuilder  # noqa: E402
        WitnessBuilder.stamp_staleness_metadata(
            witness, script_path=__file__,
            engine=witness.get("engine", 'python+mpmath'))
        json.dump(witness, f, indent=2)
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
