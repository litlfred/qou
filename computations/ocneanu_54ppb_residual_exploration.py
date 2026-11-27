"""Exploration — what closes the 54 ppb Ocneanu residual?

Tasks 1, 1-alt, 2, 3 of PR #1617 all returned NULL. The 54 ppb
residual after the (α_em/π)/dim H_3 correction is the open thread.

The residual factor f(q_0) ≈ 1.001674 is what's needed:
  required_correction = (α_em/π) · f(q_0) / 6
  where f(q_0) = 1.001674...

This probe explores wider candidate bases:

A. **Special function evaluations at q_0**:
   - Bloch-Wigner dilog D(z) at substrate values
   - Mahler measure of small polynomials
   - Selberg / Apéry-like constants
   - q-Pochhammer (q; q)_∞

B. **Higher-order α_em corrections**:
   - α_em²/π (1-loop vacuum polarization)
   - α_em/(2π) (gauge halving)
   - (α_em/π) · ln(m_μ/m_e) (LBL anomalous mag.)
   - Gribov copies correction

C. **Discrete categorical sums**:
   - Σ over H_3 partitions of (κ_λ · weight)
   - Sum over Bring saturating knots

D. **Try simple combinations 1 + α·H_3-natural-quantity**:
   - 1 + (G/π)·something / 6
   - 1 + π/(something integer)
   - 1 + α_em·integer

Goal: identify f(q_0) ≈ 1.001674 as a clean substrate quantity.

## Cross-references

- merged PR #1581 + audit roundup
- PR #1617 tasks 1-4 NULL findings
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_MU_MEV_VALIDATION, M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def trM_borromean_closed(q):
    # convention D — verified by EVALUATION at q0, not by reading: computations/audits/borromean_convention_by_evaluation.py
    h = q - 1 / q
    h2 = h * h
    return (4 + h2 - 3 * h2 ** 2 - h2 ** 3) / (h2 + 4)


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfact(k, q):
    out = mp.mpf(1)
    for i in range(1, k + 1):
        out *= qint(i, q)
    return out


def main() -> int:
    set_compute_dps(70)
    q = Q_MP

    print("=" * 78)
    print("Ocneanu 54 ppb residual — wider exploration (70 dps)")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # Reproduce setup
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    m_e = mp.mpf("0.51099895069")
    m_mu = mp.mpf(M_MU_MEV_VALIDATION)
    m_p = mp.mpf(M_P_MEV_VALIDATION)
    k_required = (2 * m_mu * F_Bor - m_p) / m_e
    residual = 12 - k_required

    # Helpers for form A/B verification (used near end)
    G = mp.catalan

    # f(q_0) such that correction = (α_em/π) · f(q_0) / 6 = residual
    alpha_em = mp.mpf(1) / mp.mpf("137.035999084")
    f_target = residual / (alpha_em / mp.pi / 6)
    print(f"[Target] f(q_0) = {mp.nstr(f_target, 25)}")
    print(f"         f - 1  = {mp.nstr(f_target - 1, 18)}")

    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    G = mp.catalan

    # ── A. Special-function candidates ──
    print(f"\n[A. Special-function evaluations]")
    # Bloch-Wigner D(z) approximation: D(z) = Im(Li_2(z)) + arg(1-z)·ln|z|
    # for some z related to substrate
    candidates_A = [
        ("1 + α_em (1-loop natural)", 1 + alpha_em),
        ("1 + α_em/(4π)", 1 + alpha_em / (4 * mp.pi)),
        ("1 + α_em/π·G", 1 + alpha_em / mp.pi * G),
        ("(1+α_em)^(1/2)", mp.sqrt(1 + alpha_em)),
        ("exp(α_em/π)", mp.exp(alpha_em / mp.pi)),
        ("1 + ln(2)·h⁴", 1 + mp.log(2) * h ** 4),
        ("D(1/2)/π² (BW dilog at 1/2)", 1 + mp.clsin(2, mp.pi / 3) * mp.mpf("0.001")),
        ("1 + α_em²/(4π²)", 1 + alpha_em ** 2 / (4 * mp.pi ** 2)),
        ("1 + α_em·ln(m_μ/m_e)/(4π)",
         1 + alpha_em * mp.log(m_mu / m_e) / (4 * mp.pi)),
        ("1 + α_em·ln(2)/(2π)", 1 + alpha_em * mp.log(2) / (2 * mp.pi)),
        ("1 + α_em·ln(3)/(2π)", 1 + alpha_em * mp.log(3) / (2 * mp.pi)),
    ]

    # ── B. Empirical h²/h⁴ corrections via PSLQ ──
    # f - 1 ≈ 0.001674; h² = 0.0437; h⁴ ≈ 0.00191
    print(f"\n[B. Power-series fits — find α for f = 1 + α·h^k]")
    print(f"  h² at q_0 = {mp.nstr(h2, 12)}, h⁴ = {mp.nstr(h ** 4, 12)}")
    print(f"  f-1 = {mp.nstr(f_target - 1, 12)}")
    print(f"  (f-1)/h² = {mp.nstr((f_target - 1) / h2, 12)}  (need ≈ 0.0383)")
    print(f"  (f-1)/h⁴ = {mp.nstr((f_target - 1) / h ** 4, 12)}  (need ≈ 0.876)")
    print(f"  (f-1)/ℏ_q = {mp.nstr((f_target - 1) / hbar_q, 12)}  (need ≈ 0.0169)")
    print(f"  (f-1)/ℏ_q² = {mp.nstr((f_target - 1) / hbar_q ** 2, 12)}")
    print(f"  (f-1)/α_em = {mp.nstr((f_target - 1) / alpha_em, 12)}")
    print(f"  (f-1)/(α_em/π) = {mp.nstr((f_target - 1) / (alpha_em / mp.pi), 12)}")

    # PSLQ on (f-1) vs basis
    basis_B = {
        "h²": h2,
        "h⁴": h ** 4,
        "h⁶": h ** 6,
        "ℏ_q": hbar_q,
        "ℏ_q²": hbar_q ** 2,
        "α_em": alpha_em,
        "α_em/π": alpha_em / mp.pi,
        "α_em²": alpha_em ** 2,
        "G·h²": G * h2,
        "α_em·h²": alpha_em * h2,
        "α_em·ln(m_μ/m_e)/(4π)": alpha_em * mp.log(m_mu / m_e) / (4 * mp.pi),
    }
    f_minus_1 = f_target - 1

    print(f"\n[B.1 PSLQ pairwise on (f-1) — find ε such that f-1 = ε · candidate]")
    matches = []
    for name, val in basis_B.items():
        try:
            rel = mp.pslq([f_minus_1, val], tol=mp.mpf("1e-15"), maxcoeff=10000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = f_minus_1 - ratio * val
                if abs(check) < mp.mpf("1e-12"):
                    matches.append((name, ratio, abs(check)))
                    print(f"  f-1 ≈ ({rel[1]}/{rel[0]}) · {name} (residual {mp.nstr(abs(check), 8)})")
        except Exception:
            pass

    # ── A scoring ──
    print(f"\n[A scoring]")
    print(f"  {'name':<42}{'value':<22}{'Δ ppb to f_target':<14}")
    scored_A = []
    for name, val in candidates_A:
        delta_ppb = (val - f_target) / f_target * mp.mpf("1e9")
        scored_A.append((name, val, delta_ppb))
    scored_A.sort(key=lambda r: abs(r[2]))
    for name, val, dppb in scored_A:
        marker = ""
        if abs(dppb) < mp.mpf("10"):
            marker = " ⭐⭐ < 10 ppb"
        elif abs(dppb) < mp.mpf("100"):
            marker = " ⭐ < 100 ppb"
        print(f"  {name:<42}{mp.nstr(val, 18):<22}{mp.nstr(dppb, 6)}{marker}")

    # Direct test: residual ≈ α_em · (something small)
    print(f"\n[C. Direct α_em-decomposition tests]")
    # residual is 32 ppm in k; in correction units it's:
    # required correction = α_em/(6π) · 1.001674 = (α_em/(6π)) + (α_em/(6π))·0.001674
    # Extra piece: (α_em/(6π))·0.001674 ≈ α_em·0.001674/(6π)
    # That's small. Test: is the extra (α_em/(6π))·(α_em/π)?
    # (α_em/π) ≈ 0.00232. Ratio: 0.001674/0.00232 = 0.722
    # So 0.722·(α_em/π) ≈ residual leading correction.
    # 0.722 — anything natural?
    extra = (f_target - 1) * (alpha_em / mp.pi / 6)
    extra_over_alpha_em_pi_sq = extra / (alpha_em / mp.pi) ** 2
    print(f"  extra correction        = {mp.nstr(extra, 18)}")
    print(f"  extra / (α_em/π)²       = {mp.nstr(extra_over_alpha_em_pi_sq, 12)}")
    print(f"  extra / (α_em²/π²·6)    = {mp.nstr(extra * 6 / (alpha_em / mp.pi) ** 2, 12)}")

    # Verdict
    print(f"\n[Verdict]")
    # ── FINDING (added 2026-06-01 post-exploration) ──
    # The leading h⁴ coefficient hunt revealed TWO empirically tight forms:
    #   Form A: f = 1 + (1 - π²/80)·h⁴            → 0.003 ppb (17,584× over baseline)
    #   Form B: f = 1 + (7/8)·h⁴ + (G/(8π))·h⁶    → 0.0008 ppb (68,576× over baseline)
    # Both are EMPIRICAL near-matches; neither has clean structural derivation.
    # Reported as exploration only — see audit doc for treatment.
    pi_sq_80 = mp.pi ** 2 / 80
    correction_form_a = (alpha_em / mp.pi / 6) * (1 + (1 - pi_sq_80) * h ** 4)
    form_a_ppb = (12 - correction_form_a - k_required) / k_required * mp.mpf("1e9")
    correction_form_b = (alpha_em / mp.pi / 6) * (
        1 + mp.mpf(7) / 8 * h ** 4 + G / (8 * mp.pi) * h ** 6
    )
    form_b_ppb = (12 - correction_form_b - k_required) / k_required * mp.mpf("1e9")
    print(f"\n[FORM A] 1 + (1 - π²/80)·h⁴ : {mp.nstr(abs(form_a_ppb), 6)} ppb")
    print(f"[FORM B] 1 + (7/8)·h⁴ + (G/(8π))·h⁶ : {mp.nstr(abs(form_b_ppb), 6)} ppb")

    if matches:
        verdict = (
            f"PSLQ HIT: f-1 has structure {matches[0][0]} with ratio "
            f"{mp.nstr(matches[0][1], 6)}. Worth deeper investigation."
        )
    elif scored_A and abs(scored_A[0][2]) < mp.mpf("10"):
        verdict = (
            f"SPECIAL-FUNCTION HIT: '{scored_A[0][0]}' gives "
            f"{mp.nstr(scored_A[0][2], 6)} ppb to f_target."
        )
    elif scored_A:
        verdict = (
            f"BEST candidate: '{scored_A[0][0]}' at "
            f"{mp.nstr(scored_A[0][2], 6)} ppb — not below 10 ppb threshold."
        )
    else:
        verdict = "All scans NULL."
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "ocneanu-54ppb-residual-exploration",
        engine="python",
    )
    w.set_description(
        "Exploration probe (while user waits) for the 54 ppb residual on "
        "the (α_em/π)/dim H_3 Ocneanu near-match. Tests special-function "
        "candidates, PSLQ over higher-order α_em + h^k mixed terms, "
        "direct α_em-decomposition. Goal: identify f(q_0) ≈ 1.001674."
    )
    w.add_parameter("q_70dps", Q_50_DIGIT_STR)
    w.add_data("f_target", mp.nstr(f_target, 25))
    w.add_data("f_minus_1", mp.nstr(f_target - 1, 25))
    w.add_data("pslq_hits", len(matches))
    w.add_data("best_special_function_ppb", mp.nstr(scored_A[0][2], 8) if scored_A else "n/a")
    w.add_data("verdict", verdict)

    # Was `computed=True, expected=True` named `exploration_completed` (bean
    # `qou-26f2`): reaching save() was the whole test.  Draining it exposed
    # that every number this module's prose quotes has since drifted — see the
    # caveat.  What follows asserts what the arithmetic ACTUALLY says.

    # (1) Controls on the q-machinery the target is built from, at the one
    # argument whose values are fixed a priori: [3]_q! → 3! = 6 and the
    # Borromean closed-form trace → 1 as q → 1.
    _q1 = 1 + mp.mpf("1e-30")
    qfact3_classical_gap = abs(qfact(3, _q1) - 6)
    trM_classical_gap = abs(trM_borromean_closed(_q1) - 1)
    _classical_gap = max(qfact3_classical_gap, trM_classical_gap)
    w.add_assertion(
        name="q_brackets_reduce_to_classical_at_q_one",
        computed=mp.nstr(_classical_gap, 12),
        expected="0",
        tolerance="1e-25",
        source=f"max(|[3]_q! − 3!|, |tr_M(Borromean) − 1|) at q = 1+1e-30 = "
               f"{mp.nstr(_classical_gap, 6)}; 3! = 6 and the classical Markov "
               "trace 1 are known independently of this substrate and pin "
               "qint / qfact / trM_borromean_closed",
    )

    # (2) The Ocneanu near-match itself, which is the module's whole premise:
    # (2·m_μ·F_Bor − m_p)/m_e lands on the categorical integer 12 = 2·dim H_3.
    # 12 comes from the representation theory, not from this computation, so
    # this is the one place the exploration meets an independent number.
    k_gap = abs(k_required - 12)
    w.add_assertion(
        name="k_required_lands_on_categorical_integer_12",
        computed=mp.nstr(k_required, 20),
        expected="12",
        tolerance="1e-3",
        source=f"(2·m_μ·F_Bor − m_p)/m_e = {mp.nstr(k_required, 16)}; misses "
               f"the integer 12 = 2·dim H_3 by {mp.nstr(k_gap, 6)} "
               f"({mp.nstr(k_gap / 12 * mp.mpf('1e6'), 6)} ppm). Gate 1e-3, "
               "~2.5× the observed gap: a drift moving k off 12 by a part in "
               "10^4 breaks the near-match this module exists to close",
    )

    # (3) The two empirical forms the 2026-06-01 comment block claims reach
    # 0.003 and 0.0008 ppb. They do not — both sit at ~207 ppb here. The
    # refutation is asserted, the claim is reported; see the caveat.
    _best_form_ppb = min(abs(form_a_ppb), abs(form_b_ppb))
    w.add_assertion(
        name="empirical_h4_forms_do_not_reach_sub_ppb",
        computed=1.0 if _best_form_ppb > 1 else 0.0,
        expected=1.0,
        tolerance=0.5,
        source=f"FORM A = {mp.nstr(abs(form_a_ppb), 8)} ppb, FORM B = "
               f"{mp.nstr(abs(form_b_ppb), 8)} ppb; neither is within 1 ppb, "
               "contradicting the in-file 0.003 / 0.0008 ppb claims",
    )

    # (4) The scan's own result, which nothing asserted.
    w.add_assertion(
        name="pslq_structure_hits_on_f_minus_1",
        computed=len(matches),
        expected=0,
        tolerance=0,
        source=f"{len(matches)} PSLQ pairwise structures found for f−1; the "
               "verdict's non-hit branch depends on this being 0",
    )
    w.add_data("k_required", mp.nstr(k_required, 25))
    w.add_data("form_a_ppb", mp.nstr(form_a_ppb, 12))
    w.add_data("form_b_ppb", mp.nstr(form_b_ppb, 12))
    w.add_caveat(
        "Every figure this module's prose quotes has drifted from what it now "
        "computes, and the drain is what surfaced it. (a) The title and "
        "docstring say a '54 ppb residual'; after the plain (α_em/π)/dim H_3 "
        f"correction the residual measures "
        f"{mp.nstr((12 - alpha_em / mp.pi / 6 - k_required) / k_required * mp.mpf('1e9'), 8)} "
        "ppb. (b) The docstring sets the goal as identifying f(q_0) ≈ "
        f"1.001674; the computed f_target is {mp.nstr(f_target, 12)}, so f−1 "
        "is 4.8× the stated value. (c) The 2026-06-01 comment block reports "
        "FORM A at 0.003 ppb and FORM B at 0.0008 ppb (17,584× and 68,576× "
        f"over baseline); they measure {mp.nstr(abs(form_a_ppb), 6)} and "
        f"{mp.nstr(abs(form_b_ppb), 6)} ppb — about five orders worse, and "
        "indistinguishable from each other. The computation is "
        "self-consistent; the prose predates a substrate or CODATA movement "
        "and was never re-derived. Reported, not silently corrected."
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
