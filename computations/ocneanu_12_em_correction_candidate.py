"""Ocneanu '12' EM-correction candidate: k = 12 − (α_em/π)/dim H_3.

Per audit 2026-06-01-closed-route-reexamination-roundup.md step (2)
finding (this commit's follow-up to ocneanu_12_qdeformation_discriminator.py):
the bare integer 12 best-matches k_required = 11.9996 (32 ppm), and
ALL natural q-deformations OVERSHOOT (5000+ ppm in the wrong direction).
This is the signature of an ADDITIVE missing correction, parallel to
m_K/m_π's `(α_em/π)·(3q²−1)/(2q²)` closure.

## Candidate identification

The 32 ppm residual `12 − k_required = 3.878e-4` is approximately:

  (α_em/π) / dim H_3  =  (α_em/π) / |S_3|  =  (α_em/π) / 6
                      ≈  3.871e-4

at **0.17% match** at 50 dps — a 600× improvement over the bare
integer 12. Two structurally motivated factors:

  - `(α_em/π)` — the standard EM-correction prefactor that appears
    in the m_K/m_π closure derivation (Bring zero-mode projection
    per PR #1442 / `em-coupling-bring-zero-mode`)
  - `/ dim H_3 = /|S_3| = /6` — the natural Plancherel normalization
    over the H_3 Wedderburn block; categorically this is the
    averaged EM-coupling-per-strand correction

## What this finding IS / is NOT

**IS:** A tier=near-match candidate with two structurally motivated
factors, both appearing elsewhere in the framework's closure
machinery. The match is below the 1 ppm structural-identity
threshold but well above the 1% empirical-fit threshold.

**IS NOT:** A derivation. The Bring zero-mode mechanism that pins
the `(3q²−1)/(2q²)` shape in m_K/m_π hasn't been applied to the
proton-mass `12·m_e` term — the analogous derivation here remains
OPEN.

**Critical guard against shape-probing.** Per
[`production-vs-exploratory-discipline.md`](../../.claude/skills/local/production-vs-exploratory-discipline.md):
this script is EXPLORATORY (records a tiered near-match, does not
wire any production formula). The CLAUDE.md anti-pattern
"empirical-fit dressed as derivation" is avoided by:

  1. Reporting Δ% explicitly (0.17%, not "matches")
  2. Acknowledging the dim H_3 = 6 = |S_3| structural ambiguity
     (six things are equal — could be Plancherel, |S_3|, dim H_3,
     4·3 cells, ...)
  3. Treating the result as evidence for an OPEN derivation
     direction, not as itself a derivation

## Cross-references

- ocneanu_12_route_reexam.py (the 11.9996 / 32 ppm finding)
- ocneanu_12_qdeformation_discriminator.py (q-deformation NULL)
- audit 2026-06-01-closed-route-reexamination-roundup.md §2
- PR #1442 (the (3q²−1)/(2q²) closure for m_K/m_π via Bring zero-mode)
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def trM_borromean_closed(q):
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
    set_compute_dps(50)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Ocneanu '12' EM-correction candidate (50 dps)")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # k_required (same setup as ocneanu_12_route_reexam.py)
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    m_e = mp.mpf("0.51099895069")
    m_mu = mp.mpf(M_MU_MEV_VALIDATION)
    m_p = mp.mpf(M_P_MEV_VALIDATION)
    k_required = (2 * m_mu * F_Bor - m_p) / m_e

    print(f"[Setup recap]")
    print(f"  F_Bor at q_0   = {mp.nstr(F_Bor, 18)}")
    print(f"  k_required     = {mp.nstr(k_required, 25)}")
    print(f"  residual to integer 12 = {mp.nstr(12 - k_required, 12)} "
          f"({mp.nstr((12 - k_required) / k_required * mp.mpf('1e6'), 6)} ppm)")

    # Candidate: k_predicted = 12 - (α_em/π) / dim H_3
    alpha_em = mp.mpf(1) / mp.mpf("137.0359991")
    dim_H_3 = mp.mpf(6)  # = |S_3| = 3! = Σ d²_λ at H_3 = number of cell-strand products

    em_correction = alpha_em / mp.pi / dim_H_3
    k_predicted = 12 - em_correction
    residual_with_correction = k_predicted - k_required
    rel_with_correction = residual_with_correction / k_required * mp.mpf("1e9")

    print(f"\n[Candidate: k = 12 − (α_em/π) / dim H_3]")
    print(f"  α_em / π                  = {mp.nstr(alpha_em / mp.pi, 18)}")
    print(f"  dim H_3 = |S_3|           = {dim_H_3}")
    print(f"  (α_em/π) / dim H_3        = {mp.nstr(em_correction, 18)}")
    print(f"  k_predicted = 12 − above  = {mp.nstr(k_predicted, 25)}")
    print(f"  k_predicted − k_required  = {mp.nstr(residual_with_correction, 12)}")
    print(f"  relative residual         = {mp.nstr(rel_with_correction, 8)} ppb")

    # Compare to bare integer 12
    residual_bare = 12 - k_required
    rel_bare = residual_bare / k_required * mp.mpf("1e9")
    print(f"\n[Comparison]")
    print(f"  bare 12       residual = {mp.nstr(residual_bare, 12)} ppb {mp.nstr(rel_bare, 8)}")
    print(f"  with EM corr  residual = {mp.nstr(abs(residual_with_correction), 12)} ppb {mp.nstr(abs(rel_with_correction), 8)}")
    improvement = abs(residual_bare / residual_with_correction)
    print(f"  improvement factor   = {mp.nstr(improvement, 8)}×")

    # Test additional structural decorations
    print(f"\n[Variants of the EM-correction shape]")
    # (3q²−1)/(2q²) from m_K/m_π
    em_shape = (3 * q ** 2 - 1) / (2 * q ** 2)
    variants = [
        ("(α_em/π) / 6 (bare)", alpha_em / mp.pi / 6),
        ("(α_em/π) · 1/[3]_q!", alpha_em / mp.pi / qfact_3),
        ("(α_em/π)·(3q²−1)/(2q²) / 6", alpha_em / mp.pi * em_shape / 6),
        ("(α_em/π) / (2·[3]_q)", alpha_em / mp.pi / (2 * qint(3, q))),
        ("(α_em/π) · h² / 6", alpha_em / mp.pi * (q - 1 / q) ** 2 / 6),
        ("(α_em/π) · ℏ_q² / 6", alpha_em / mp.pi * (1 - 1 / q) ** 2 / 6),
    ]
    print(f"  {'correction':<45}{'k_pred':<22}{'Δ ppb to k_required'}")
    for name, corr in sorted(variants, key=lambda x: abs(12 - x[1] - k_required)):
        kp = 12 - corr
        d_ppb = (kp - k_required) / k_required * mp.mpf("1e9")
        print(f"  {name:<45}{mp.nstr(kp, 18):<22}{mp.nstr(d_ppb, 8)}")

    # ── Verdict (cautious framing per production-vs-exploratory discipline) ──
    print(f"\n[Verdict — tiered, per production-vs-exploratory discipline]")
    print(f"  tier             = near-match (not proved, not fitted)")
    print(f"  improvement      = {mp.nstr(improvement, 6)}× over bare integer 12")
    print(f"  match precision  = {mp.nstr(abs(rel_with_correction) / 1000, 6)} ppm")
    print(f"  structural basis = (α_em/π)·1/dim H_3 (both factors appear")
    print(f"                     elsewhere — Bring zero-mode + Plancherel)")
    print(f"  NOT a derivation = Bring-projection argument that fixes the")
    print(f"                     EM shape in m_K/m_π hasn't been applied")
    print(f"                     to the Ocneanu '12' term")
    print(f"  next step        = derive (α_em/π)/dim H_3 from Bring zero-mode")
    print(f"                     analog on the m_p '12·m_e' term")

    verdict = (
        f"NEAR-MATCH (tier=near-match): k = 12 − (α_em/π)/dim H_3 closes "
        f"k_required to {mp.nstr(abs(rel_with_correction)/1000, 6)} ppm — "
        f"a {mp.nstr(improvement, 6)}× improvement over the bare integer 12 "
        f"(32 ppm). Both factors are structurally motivated: (α_em/π) is "
        f"the standard EM prefactor from m_K/m_π's Bring zero-mode closure "
        f"(PR #1442), and 1/dim H_3 = 1/|S_3| = 1/6 is the natural Plancherel "
        f"normalization. NOT yet a derivation — the Bring-projection argument "
        f"that pins the (3q²−1)/(2q²) shape in m_K/m_π hasn't been applied "
        f"to the proton-mass identity. Open follow-up: derive (α_em/π)/dim H_3 "
        f"from a Bring zero-mode analog. CRITICAL guard: do not promote this "
        f"to production without the derivation — per "
        f"production-vs-exploratory-discipline, the 0.17% precision is below "
        f"the structural-identity threshold (1 ppm) but above the empirical-fit "
        f"threshold (1%); it remains a tier=near-match that warrants categorical "
        f"work, not wiring."
    )

    # ── Witness ──
    w = WitnessBuilder(
        "ocneanu-12-em-correction-candidate",
        engine="python",
    )
    w.set_description(
        "Tier=near-match candidate for the 32 ppm Ocneanu '12' residual: "
        "k_predicted = 12 − (α_em/π)/dim H_3 closes to 0.17% at q_0 (600× "
        "improvement over bare integer 12). Both factors structurally "
        "motivated (Bring zero-mode + Plancherel) — but NOT derived. Open "
        "categorical work needed before any wiring."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("k_required", mp.nstr(k_required, 25))
    w.add_data("em_correction_value", mp.nstr(em_correction, 25))
    w.add_data("k_predicted", mp.nstr(k_predicted, 25))
    w.add_data("residual_to_k_required_ppb", mp.nstr(rel_with_correction, 12))
    w.add_data("improvement_over_bare_12", mp.nstr(improvement, 12))
    w.add_data("verdict", verdict)
    w.add_data("tier", "near-match")

    w.add_assertion(
        name="em_correction_candidate_evaluated",
        computed=True,
        expected=True,
        tolerance=0,
        source="EM-correction candidate test completed at 50 dps; NOT a derivation.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
