#!/usr/bin/env python3
"""qbeta_ck_basis_constrained_pslq.py — PROBE 4: basis-constrained PSLQ
per coefficient (docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md §3.D).

TWO-STAGE, FORMALIZE-FIRST (compute-author.md §3.3; the PSLQ ENTROPY BOUND
of PR #1805: a PSLQ relation among n terms of integer height ≤ H is
meaningful ONLY if the target carries

        D_eff  >  n · log10(2·H)   (+ margin)

reliable digits; below that, ANY relation found is guaranteed-spurious
lattice noise).

STAGE 1 (entropy audit, mandatory) — determine the ACTUAL effective
precision of the empirical c_3 / c_4 by tracing the extraction chain:

    c_3_emp = (Q_β_CODATA / Q_N2 − 1) / u³ ,   u = b·ℏ_q² ≈ 0.008517
    c_4_emp = (Q_β_CODATA / Q_N3 − 1) / u⁴

(producers: computations/qbeta/qbeta_ck_k_gt_3_habiro_extension_scoping.py
lines 139-157; cache computations/qbeta/qbeta-ck-cache.witness.json).
The division by u³ ≈ 6.18e-7 (u⁴ ≈ 5.26e-9) AMPLIFIES the relative
experimental error of Q_β by ~1/(|c_k|·u^k). Error channels propagated:

  (a) experimental Q_β:  σ_rel ≈ 7.8e-7 (0.78 ppm; docs/precision-goals.md
      §L2 table — the "7.8 ppb" figure in circulation is the 100× TARGET
      σ_exp/100, not σ_exp). We audit BOTH readings — the kill must
      survive the most optimistic one.
  (b) q₀ pin:  empirical dc_3/dq ≈ 4.6e6 (registry §3, PR #1821) ×
      pin precision (proton 0.06 ppb, muon 22 ppb).
  (c) observed inter-producer spread of "empirical c_3" at the same
      anchor family (cache −2.02019 vs hopf-profile muon −2.0097):
      ~0.5% — an extraction-convention systematic.

If D_eff < the MINIMAL budget (n = 4 terms, H ≤ 100 ⇒ 4·log10(200) ≈ 9.2
digits, before margin): STOP — verdict ENTROPY-BLOCKED. That is the
formalize-first result; running PSLQ on noise is forbidden.

STAGE 2 (only if Stage 1 passes) — mpmath.pslq per coefficient per anchor
against the arithmetic-dictated basis ONLY (GSWZ + Garoufalidis–Zagier;
4₁ trace field ℚ(√−3), Vol(4₁) = 2·Cl₂(π/3) = 6Λ(π/3) so Λ(π/3) is NOT separately
included):

    {1, √3, π², Vol(4₁), ζ(3)}

ANCHOR GATE: a relation counts only if the SAME integer relation holds at
BOTH anchors within precision; one-anchor relations are near-match tier.
A found relation is NEVER a derivation and nothing is wired (§8 flip-flop
guard).

Honest outcomes: ENTROPY-BLOCKED, or "coefficients remain empirical under
the arithmetic basis". Both are full successes of the discipline.
"""

import json
import math
import os
import subprocess
from datetime import datetime, timezone

import mpmath as mp
# Path bridge (bean qou-9ugp): `q_parameter` lives in computations/substrate/,
# and the anchor must be read from it (not from qou_substrate.constants) or the
# witness gets no q0 stamp. Idempotent.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402

mp.mp.dps = 60  # ≥ 50 dps discipline

# ---------------------------------------------------------------------------
# Canonical inputs (traced to producers — see docstring)
# ---------------------------------------------------------------------------
# Both pins read BY NAME (bean qou-9ugp, 2026-09-03). `Q0_CANONICAL` was the
# literal 1.1099785955573… — the RETIRED self-certified muon pin A, superseded
# 2026-08-22 by the live CODATA-2022 lepton-ratio derivation (+0.0769 ppb);
# `Q0_PROTON` was the 50-digit proton string re-typed by hand. Two pins are
# read on purpose here (the manifest files this stem `ambiguous`).
Q0_CANONICAL = mp.mpf(mp.nstr(q_muon_at(50), 50, strip_zeros=False))
Q0_PROTON = Q_MP
M_E_MEV = mp.mpf("0.51099895069")
# Q_β reference used by the cache extraction (qbeta-ck-cache Q_codata)
Q_BETA_CODATA_MEV = mp.mpf("0.78233341")

# experimental relative uncertainty of Q_β (two readings audited)
SIGMA_Q_REL_ACTUAL = mp.mpf("7.8e-7")      # 0.78 ppm — precision-goals.md §L2
SIGMA_Q_REL_OPTIMISTIC = mp.mpf("7.8e-9")  # 7.8 ppb — the 100× target read as σ

# q₀ pin precisions (relative) — AGENTS.md §q₀ anchor convention
PIN_REL_PROTON = mp.mpf("0.06e-9")   # 0.06 ppb
PIN_REL_MUON = mp.mpf("22e-9")       # 22 ppb

# Empirical c_3 readouts on record (inter-producer spread evidence).
#
# THESE ARE THREE DIFFERENT PRODUCERS' READOUTS, NOT INTERCHANGEABLE VALUES.
# Only `C3_EMP_CACHE` is extracted at `Q0_CANONICAL`; pairing either of the
# others with that pin measures a producer difference, not an anchor slope
# (bean `qou-t39x` — that mismatch is where the corpus's "4.6e6" came from).
#
# `C3_EMP_MUON_HOPF` is a SUPERSEDED readout (pre-#1422) and is retained on
# purpose: the inter-producer spread below is a real measurement of how far
# apart two producers' "empirical c_3" got, and deleting it would delete the
# evidence. It must never enter an arithmetic slope.
C3_EMP_PROTON = mp.mpf("-2.06934257711516783787971951725")  # root-of-unity probe
C3_EMP_MUON_HOPF = mp.mpf("-2.0097")                         # hopf-profile probe (SUPERSEDED; spread only)
C3_EMP_CACHE = mp.mpf("-2.02018812814143945582016855395")    # ck-cache, extracted AT Q0_CANONICAL
# 🛑 CONVENTION-C VALUE. `ladder_chain` below is convention D (z = q^3/(q^2+1),
# line ~119), so this constant and that function are in DIFFERENT FRAMES and the
# self-check comparing them is RED by construction, by ~972.362 -- which is the
# C->D extraction shift, not a numerical defect. Corroboration: the D-frame muon
# c_3 is -974.3821470795362 in
# computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json
# (`result.c3.D_muon`), matching this producer's own c3_reproduced_canonical on
# every printed digit.
#
# Do NOT "reconcile" this against anchor_slope_dc3_dq: c3 is computed from q
# alone in ladder_chain and the slope is an independent OUTPUT field, so there is
# no reconciliation to perform (bean qou-v6wz records that diagnosis; it is
# withdrawn, see the bean).
#
# Do NOT widen the tolerance or re-baseline -- AGENTS.md forbids it explicitly.
# Going green requires the convention-D c_k ladder, i.e. bean qou-cds1, which is
# blocked on the N=1 eigenphase alpha (qou-pdix). Until then the RED is the gate
# working: it reports that the C-frame cached c_3 is not reproducible under the
# canonical convention.

MARGIN_DIGITS = 3.0  # confidence margin beyond the raw entropy floor


def ladder_chain(q):
    """Reproduce the c_3/c_4 extraction chain at anchor q (the producer's
    exact convention — qbeta_ck_k_gt_3_habiro_extension_scoping.py)."""
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    alpha = (z - 1) * h / 2
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)
    hbar_q = (q - 1) / q
    u = b * hbar_q ** 2
    Q_A = M_E_MEV * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)
    alpha_eff = alpha - b * hbar_q ** 2 / 2
    Q_N1 = Q_A * mp.cos(alpha_eff)
    Q_N2 = Q_N1 * (1 - u ** 2)  # c_2 = -1 CANONICAL
    c3 = (Q_BETA_CODATA_MEV / Q_N2 - 1) / u ** 3
    Q_N3 = Q_N2 * (1 + c3 * u ** 3)
    c4 = (Q_BETA_CODATA_MEV / Q_N3 - 1) / u ** 4
    return {"u": u, "Q_N2": Q_N2, "Q_N3": Q_N3, "c3": c3, "c4": c4}


def eff_digits(value, err):
    """Effective significant digits of value under absolute error err."""
    if err <= 0:
        return float("inf")
    r = mp.fabs(value) / err
    return float(mp.log10(r)) if r > 1 else 0.0


def main():
    print("=" * 78)
    print(" PROBE 4 — basis-constrained PSLQ: STAGE 1 entropy audit")
    print("=" * 78)

    # -----------------------------------------------------------------
    # Extraction-chain reproduction (validates we audit the real chain)
    # -----------------------------------------------------------------
    chain = ladder_chain(Q0_CANONICAL)
    u, c3, c4 = chain["u"], chain["c3"], chain["c4"]
    c3_cache_delta = mp.fabs(c3 - C3_EMP_CACHE)
    print(f"\n  extraction chain at canonical q₀:")
    print(f"    u = b·ℏ_q²     = {mp.nstr(u, 20)}")
    print(f"    u³             = {mp.nstr(u ** 3, 8)}")
    print(f"    u⁴             = {mp.nstr(u ** 4, 8)}")
    print(f"    c_3 reproduced = {mp.nstr(c3, 25)}")
    print(f"    c_3 cache      = {mp.nstr(C3_EMP_CACHE, 25)}")
    print(f"    |delta|        = {mp.nstr(c3_cache_delta, 5)}")
    print(f"    c_4 reproduced = {mp.nstr(c4, 15)}")
    print(f"      NOTE: c_4 ≡ 0 BY CONSTRUCTION when c_3 is extracted exactly")
    print(f"      against the same Q reference — the nonzero 'empirical c_4'")
    print(f"      (−0.972, qbeta_1ppq_achieved) exists only as the truncation")
    print(f"      residual of a ROUNDED c_3. Direct confirmation of the")
    print(f"      registry's 'c_4 = CODATA-residual fit / artifact' tier:")
    print(f"      c_4 has NO independent empirical content to feed PSLQ.")

    # -----------------------------------------------------------------
    # Error propagation — the extraction amplifier
    # -----------------------------------------------------------------
    # exact partials: dc3/d(eps_Q) = (Q/Q_N2)/u³ ; dc4/d(eps_Q) = (Q/Q_N3)/u⁴
    dc3_dQ = (Q_BETA_CODATA_MEV / chain["Q_N2"]) / u ** 3
    dc4_dQ = (Q_BETA_CODATA_MEV / chain["Q_N3"]) / u ** 4
    # Empirical anchor slope dc3/dq from the two recorded anchors.
    #
    # 🛑 THIS PAIRED TWO DIFFERENT PRODUCERS' READOUTS (fixed 2026-08-29, bean
    # `qou-t39x`). It read `C3_EMP_MUON_HOPF`, the hopf-profile probe's value,
    # against `Q0_CANONICAL` — but this file's OWN readout at that pin is
    # `C3_EMP_CACHE`, defined three lines above it. The mismatch is the entire
    # source of the number:
    #
    #     proton readout vs HOPF readout   ->  4657409.9      <- the "4.6e6"
    #     proton readout vs CACHE (same pin) ->  3838405.9    <- the real slope
    #
    # and the print below then reported the artifact as agreeing with the
    # registry's (then also stale) "≈ 4.6e6" — two errors corroborating each
    # other. `C3_EMP_CACHE` is the value extracted AT `Q0_CANONICAL`, so it is
    # the only one that makes this a slope rather than a producer difference.
    #
    # `C3_EMP_MUON_HOPF` stays defined: the inter-producer spread below is a
    # DELIBERATE measurement and needs it. It just must not enter a slope.
    slope_c3 = (C3_EMP_PROTON - C3_EMP_CACHE) / (Q0_PROTON - Q0_CANONICAL)
    print(f"\n  amplifiers:")
    print(f"    dc_3/d(rel Q err) = 1/u³·(Q/Q_N2) = {mp.nstr(dc3_dQ, 6)}")
    print(f"    dc_4/d(rel Q err) = 1/u⁴·(Q/Q_N3) = {mp.nstr(dc4_dQ, 6)}")
    print(f"    dc_3/dq (empirical, cross-anchor) = {mp.nstr(slope_c3, 4)}"
          f"   (registry §3, corrected PR #5765: ≈ 3.84e6)")

    scenarios = []
    for (label, sigma_q) in [
        ("actual sigma(Q)=0.78ppm", SIGMA_Q_REL_ACTUAL),
        ("optimistic sigma(Q)=7.8ppb", SIGMA_Q_REL_OPTIMISTIC),
    ]:
        for (anchor, pin_rel, c3_anchor) in [
            ("proton", PIN_REL_PROTON, C3_EMP_PROTON),
            ("muon", PIN_REL_MUON, C3_EMP_CACHE),
        ]:
            dq = pin_rel * Q0_CANONICAL
            err_c3_Q = sigma_q * dc3_dQ
            err_c3_pin = mp.fabs(slope_c3) * dq
            err_c3 = mp.sqrt(err_c3_Q ** 2 + err_c3_pin ** 2)
            err_c4 = sigma_q * dc4_dQ  # pin channel omitted (Q-channel already >1)
            d3 = eff_digits(c3_anchor, err_c3)
            d4 = eff_digits(c4, err_c4)
            scenarios.append({
                "scenario": label, "anchor": anchor,
                "err_c3_from_Q": mp.nstr(err_c3_Q, 4),
                "err_c3_from_pin": mp.nstr(err_c3_pin, 4),
                "err_c3_total": mp.nstr(err_c3, 4),
                "eff_digits_c3": round(d3, 2),
                "err_c4_from_Q": mp.nstr(err_c4, 4),
                "eff_digits_c4": round(d4, 2),
            })

    print(f"\n  effective digits (D_eff = log10(|c_k|/err)):")
    print(f"    {'scenario':<28} {'anchor':<7} {'err(c3)':>10} "
          f"{'D_eff(c3)':>10} {'err(c4)':>10} {'D_eff(c4)':>10}")
    for s in scenarios:
        print(f"    {s['scenario']:<28} {s['anchor']:<7} "
              f"{s['err_c3_total']:>10} {s['eff_digits_c3']:>10} "
              f"{s['err_c4_from_Q']:>10} {s['eff_digits_c4']:>10}")

    # observed inter-producer spread corroboration
    spread = mp.fabs(C3_EMP_CACHE - C3_EMP_MUON_HOPF)
    d_spread = eff_digits(C3_EMP_CACHE, spread)
    print(f"\n  corroboration — inter-producer spread of 'empirical c_3' at the")
    print(f"  muon-family anchor: |{mp.nstr(C3_EMP_CACHE, 7)} - "
          f"({mp.nstr(C3_EMP_MUON_HOPF, 6)})| = {mp.nstr(spread, 3)}"
          f"  ⇒ ~{d_spread:.1f} stable digits")

    # -----------------------------------------------------------------
    # Entropy budget vs requirement
    # -----------------------------------------------------------------
    budgets = []
    for (n_terms, height, note) in [
        (4, 100, "MINIMAL basis (kill threshold per task spec)"),
        (6, 10, "full basis {1,√3,π²,Vol(4₁),ζ(3)} + target, H=10"),
        (6, 100, "full basis + target, H=100"),
    ]:
        d_req = n_terms * math.log10(2 * height)
        budgets.append({
            "n_terms": n_terms, "height_bound": height,
            "digits_required": round(d_req, 2),
            "digits_required_with_margin": round(d_req + MARGIN_DIGITS, 2),
            "note": note,
        })
    print(f"\n  PSLQ entropy requirement (D > n·log10(2H) + margin {MARGIN_DIGITS}):")
    for b in budgets:
        print(f"    n={b['n_terms']}, H≤{b['height_bound']:<4} ⇒ "
              f"{b['digits_required']:>6} digits "
              f"(+margin: {b['digits_required_with_margin']})   {b['note']}")

    d_eff_best = max(s["eff_digits_c3"] for s in scenarios)
    d_req_min = budgets[0]["digits_required"]
    entropy_blocked = d_eff_best < d_req_min
    # max basis size the data could support at H=10
    n_max_h10 = int(d_eff_best // math.log10(20))
    print(f"\n  best-case D_eff(c_3) across all scenarios/anchors = {d_eff_best}")
    print(f"  minimal requirement (n=4, H=100)                  = {d_req_min}")
    print(f"  deficit                                            = "
          f"{round(d_req_min - d_eff_best, 2)} digits")
    print(f"  max basis size supportable at H=10                 = {n_max_h10} term(s)")
    # Q_β precision that WOULD be needed for the minimal budget on c_3
    sigma_needed = mp.mpf(10) ** (-d_req_min) * mp.fabs(c3) / dc3_dQ
    print(f"  sigma(Q_β) needed for minimal budget on c_3        = "
          f"{mp.nstr(sigma_needed, 3)} (relative) vs actual 7.8e-7")

    verdict = "ENTROPY-BLOCKED" if entropy_blocked else "STAGE-1-PASS"
    print(f"\n  STAGE 1 VERDICT: {verdict}")

    stage2 = None
    if not entropy_blocked:
        stage2 = run_stage2()  # never reached under current data — kept honest
    else:
        print("  Stage 2 PSLQ NOT RUN — running PSLQ on noise is forbidden")
        print("  (compute-author.md §3.3 / PR #1805 precedent).")

    # -----------------------------------------------------------------
    # Witness
    # -----------------------------------------------------------------
    vol41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    out = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-ck-basis-constrained-pslq",
        "scriptFile": "qbeta_ck_basis_constrained_pslq.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            check=True).stdout.strip(),
        "description": (
            "PROBE 4 (2026-07-11 avenues audit §3.D): basis-constrained PSLQ for the "
            "empirical Q_β ladder coefficients c_3/c_4 against the arithmetic-dictated "
            "basis {1, √3, π², Vol(4₁), ζ(3)} (4₁ trace field ℚ(√−3)). Two-stage "
            "formalize-first: STAGE 1 is a mandatory entropy audit of the ACTUAL "
            "effective precision of the empirical coefficients, traced through the "
            "extraction chain c_3 = (Q_CODATA/Q_N2 − 1)/u³, which amplifies the "
            "relative Q_β error by 1/u³ ≈ 1.6e6 (c_4: 1/u⁴ ≈ 1.9e8). STAGE 2 (PSLQ) "
            "runs only if the effective digits exceed the PSLQ entropy bound "
            "D > n·log10(2H) + margin (PR #1805 discipline). No c_k value proposed; "
            "nothing wired."
        ),
        "precisionMetadata": {"compute_dps": 60},
        "data": {
            "q0_canonical": mp.nstr(Q0_CANONICAL, 50),
            "q0_proton": mp.nstr(Q0_PROTON, 50),
            "Q_beta_codata_MeV": mp.nstr(Q_BETA_CODATA_MEV, 12),
            "u_substrate": mp.nstr(u, 30),
            "u_cubed": mp.nstr(u ** 3, 10),
            "u_fourth": mp.nstr(u ** 4, 10),
            "c3_reproduced_canonical": mp.nstr(c3, 30),
            "c3_cache_value": mp.nstr(C3_EMP_CACHE, 30),
            "c3_proton_on_record": mp.nstr(C3_EMP_PROTON, 30),
            "c3_muon_hopf_on_record": mp.nstr(C3_EMP_MUON_HOPF, 8),
            "c4_reproduced_canonical": mp.nstr(c4, 20),
            "c4_artifact_note": (
                "c_4 is exactly 0 by construction when c_3 is extracted exactly "
                "against the same Q_beta reference (Q_N3 = Q_CODATA identically); "
                "the quoted empirical c_4 = -0.972 is the truncation residual of a "
                "rounded c_3 — no independent empirical content exists for PSLQ. "
                "Confirms registry rung-4 tier 'empirical_fit / artifact'."
            ),
            "amplifier_dc3_dQrel": mp.nstr(dc3_dQ, 8),
            "amplifier_dc4_dQrel": mp.nstr(dc4_dQ, 8),
            "anchor_slope_dc3_dq": mp.nstr(slope_c3, 6),
            "sigma_Q_rel_actual": mp.nstr(SIGMA_Q_REL_ACTUAL, 3),
            "sigma_Q_rel_optimistic_reading": mp.nstr(SIGMA_Q_REL_OPTIMISTIC, 3),
            "error_scenarios": scenarios,
            "inter_producer_spread_c3": mp.nstr(spread, 4),
            "inter_producer_stable_digits": round(d_spread, 2),
            "entropy_budgets": budgets,
            "margin_digits": MARGIN_DIGITS,
            "best_case_eff_digits_c3": d_eff_best,
            "minimal_requirement_digits": d_req_min,
            "digit_deficit": round(d_req_min - d_eff_best, 2),
            "max_supportable_basis_terms_at_H10": n_max_h10,
            "sigma_Q_rel_needed_for_minimal_budget": mp.nstr(sigma_needed, 3),
            "arithmetic_basis_not_run": {
                "1": "1", "sqrt3": mp.nstr(mp.sqrt(3), 30),
                "pi^2": mp.nstr(mp.pi ** 2, 30),
                "Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)": mp.nstr(vol41, 30),
                "zeta(3)": mp.nstr(mp.zeta(3), 30),
            },
        },
        "assertions": [
            {
                "name": "extraction_chain_reproduces_cache_c3",
                "computed": float(c3_cache_delta),
                "expected": 0.0,
                "passed": bool(c3_cache_delta < mp.mpf("1e-8")),
                # String, not the float literal. This probe hand-builds its
                # assertion dicts and `json.dump`s them (it imports
                # WitnessBuilder only for the provenance stamp), so it never
                # constructs an `Assertion` and
                # `qou_substrate.witness._tolerance_literal` — which converts a
                # declared tolerance to its literal at `Assertion.to_dict` —
                # never runs. "1e-08" is exactly what that helper returns for
                # this value, so a later migration to `add_assertion` is a
                # no-op on the artifact. `stage1_entropy_verdict_is_blocked`
                # below keeps its `0.0`: the helper returns None for an
                # integral-valued float and the ratchet excuses it by design.
                "tolerance": "1e-08",
                # This `source` named THREE axes of sameness -- chain, Q_codata,
                # q0 -- and the mismatch that makes the assertion fail is on a
                # FOURTH it did not mention: the Markov convention. So the
                # failure read as a defect in the extraction chain when it is a
                # frame difference between two artifacts (bean `qou-580o`).
                "source": ("same chain + same Q_codata + same q0 as "
                           "qbeta-ck-cache.witness.json (cache prints Q_codata "
                           "rounded to 0.78233341) -- but NOT the same Markov "
                           "convention, which is why this assertion fails. This "
                           "probe computes at z_D = q**3/(q**2+1) (convention D, "
                           "canonical per owner ruling R1 2026-08-15; see the z "
                           "binding above), while qbeta-ck-cache.witness.json "
                           "declares markov_convention='C' and its c_3 is "
                           "reachable only via --historical-convention-C. The "
                           "two numbers are one formula under two different z, "
                           "not two evaluations of one quantity. Re-deriving the "
                           "ladder under D is bean `qou-cds1`; this assertion is "
                           "left FAILING on purpose -- it is the frame "
                           "disagreement reporting itself, and silencing it "
                           "would ratify one frame."),
            },
            {
                "name": "stage1_entropy_verdict_is_blocked",
                "computed": d_eff_best,
                "expected": d_req_min,
                "passed": entropy_blocked,  # honest expected outcome: BLOCKED
                "tolerance": 0.0,
                "source": ("PSLQ entropy bound (PR #1805): D_eff must exceed "
                           "n·log10(2H); pre-registered kill criterion — pass "
                           "means the kill fired and Stage 2 was NOT run"),
            },
        ],
        "verdict": {
            "stage1": verdict,
            "stage2_run": stage2 is not None,
            "stage2": stage2,
            "conclusion": (
                "ENTROPY-BLOCKED: the empirical c_3 carries at most ~2 reliable "
                "digits per anchor (c_4: zero) because the extraction divides the "
                "Q_β experimental error by u³ (×1.6e6) / u⁴ (×1.9e8); even the "
                "minimal 4-term H≤100 basis needs ~9.2 digits. PSLQ was NOT run — "
                "any relation it returned would be lattice noise. The coefficients "
                "remain empirical under the arithmetic basis; no value proposed, "
                "nothing wired. Closing this avenue requires either sigma(Q_β) "
                "improved by ~9 orders of magnitude or a canonical (non-extracted) "
                "high-precision c_3 producer — i.e. the open keystone F(q) itself."
                if entropy_blocked else
                "Stage 1 passed; see stage2 results."
            ),
        },
    }
    out["allPassed"] = all(a["passed"] for a in out["assertions"])

    here = os.path.dirname(os.path.abspath(__file__))
    wpath = os.path.join(here, "qbeta-ck-basis-constrained-pslq.witness.json")
    with open(wpath, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added.
        #
        # q0 anchor (bean qou-v6wz): this witness IS q0-dependent -- it carries
        # `q0_canonical` and `c3_reproduced_canonical` (computed at the muon
        # canonical pin) AND `q0_proton` / `anchor_slope_dc3_dq` (the proton
        # readout and the cross-anchor slope). Both pins are read on purpose
        # (see Q0_CANONICAL / Q0_PROTON above), so the manifest files this stem
        # `ambiguous`. The prior `q0_anchor=False` (= stamp `independent`) was
        # WRONG: it declared layer-freedom on a witness that reads q0 twice, so
        # the q0-anchor-flip audit skipped it entirely (an audit-escape). Stamp
        # `ambiguous` -- the manifest's own classification -- with NO bare
        # q0Value (the pin is undetermined; the values actually used live in
        # data.q0_canonical / data.q0_proton).
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        out.setdefault("scriptFile", _os.path.basename(__file__))
        # Convention stamp. This witness records `c3_reproduced_canonical`
        # around -974.38, which registry §9g identifies as the convention-D
        # muon c_3 -- a number that is MEANINGLESS without its frame, and whose
        # whole history here is an undisclosed C->D flip that rode inside a
        # Lambda/Cl_2 naming commit and was not regenerated (bean `qou-580o`).
        # It carried no convention stamp at all until now, which is the
        # `qou-ng7j` coverage gap biting on the one artifact where the frame is
        # the entire content. Bare token + separate reason, matching the
        # `q0Anchor` / `q0AnchorReason` shape this module already uses.
        out["markov_convention"] = "D"
        out["markov_convention_reason"] = (
            "z = q**3/(q**2 + 1) at the binding above; convention D, canonical "
            "per owner ruling R1 (2026-08-15). NOT a proposed c_3: qou-cds1 "
            "records -974.38 as a sensitivity measurement and says explicitly "
            "'do not wire it anywhere'. The failing assertion "
            "extraction_chain_reproduces_cache_c3 is the frame disagreement "
            "with the C-framed qbeta-ck-cache.witness.json, not a chain defect."
        )
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None,
            q0_anchor="ambiguous",
            q0_anchor_reason=(
                "reads BOTH pins on purpose: c3_reproduced_canonical is at the "
                "muon canonical pin (data.q0_canonical) while the proton readout "
                "and cross-anchor slope (data.q0_proton, "
                "data.anchor_slope_dc3_dq) are at the proton pin. The witness "
                "carries both signatures, so the pin is undetermined and the "
                "manifest files this stem ambiguous; the values actually used "
                "are in data.q0_canonical / data.q0_proton. NOT q0-independent "
                "(bean qou-v6wz)."
            ))
        json.dump(out, f, indent=2)
    print(f"\n  witness → {wpath}")
    return out


def run_stage2():
    """STAGE 2 — per-coefficient, per-anchor PSLQ against the arithmetic
    basis {1, √3, π², Vol(4₁), ζ(3)}. GATED: called only if Stage 1 passes
    the entropy bound. Anchor gate: a relation counts only if the SAME
    integer vector recurs at both anchors."""
    basis = [mp.mpf(1), mp.sqrt(3), mp.pi ** 2,
             2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3))), mp.zeta(3)]
    results = {}
    anchors = {"proton": C3_EMP_PROTON, "muon": C3_EMP_CACHE}
    for name, c3_val in anchors.items():
        vec = [c3_val] + basis
        rel = mp.pslq(vec, maxcoeff=100, maxsteps=10 ** 5)
        results[name] = [int(x) for x in rel] if rel else None
    anchor_stable = (results["proton"] is not None
                     and results["proton"] == results["muon"])
    return {"per_anchor": results, "anchor_stable": anchor_stable,
            "tier": "near-match at best; NEVER a derivation; NOT wired"}


if __name__ == "__main__":
    main()
