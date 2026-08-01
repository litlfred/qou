#!/usr/bin/env python3
"""qbeta_3bp8_sigma12_substrate_probe.py — the RIGHT channel: substrate value
of the σ₁σ₂ Stokes entry, i.e. the deformation of the integer A_ω = 3.

Why this probe exists (channel-correctness audit). The T4/T5 corpus chain
(`qbeta_t4_stokes3_crux_probe.py`; `DeltaLambdaT5Assembly.lean`) uses the
GGM Stokes constant A_ω = 3. That 3 is the **(1,2) entry** of the q→0
Stokes matrix, GGM 2012.00062 eq (60):

    S⁺(0) = [[1, 3], [0, 1]]

The winding x-refinement proven for 4₁ (Conjecture 4 / eq 21, and GGM
2007.10190 eq 5/80) is a statement about the **(1,1) entry**,
S⁺_{σ₁σ₁}(x;q) = Ind^rot(0,x;q). So the qou-awpk / W2 winding results
(the ϑ-dependence, the bar-odd part, the −6.03 Im-ratio) are properties
of σ₁σ₁ — whose w = 1 substrate value is 0.42764420, NOT 3. Comparing
them against the T4 A_ω is a CROSS-CHANNEL comparison and cannot settle
"does A_ω deviate from 3".

This probe asks the σ₁σ₂ question directly, with no winding refinement
and no new machinery: evaluate the certified S⁺₁₂(q̃) series at the
substrate. The sandwich exemplar was DERIVED OCR-free and certified in
`qbeta_g3_ggm_stokes_41.py` (sign = −1, ᵀ on the second W,
A = [[0,1],[1,1]], B = [[0,1],[1,0]], C = [[0,1],[−1,−2]]) against all
four printed towers; its heads are re-verified here as a gate.

Computed, each with the honest ladder guard (q̃-orders 800/1200/1600;
a truncation difference ≥ 1 reports 0 digits — no else-40 sentinel):

  P1  S⁺₁₂(q̃_sub) — the substrate value of the entry whose q→0 value is
      the integer 3. Head: 3 − 15q̃ − 24q̃² + 15q̃³ + …
  P2  S⁺₁₁(q̃_sub) — re-confirmation of the honest tower 0.42764420.
  P3  the ratio S⁺₁₂/S⁺₁₁ evaluated as a RATIO OF VALUES. (The printed
      ratio SERIES 3 + 9q̃ + 75q̃² + 642q̃³ + … has coefficients growing
      ~8.7×/order — radius ≈ 0.115 — so it diverges at q̃ ≈ 0.9009 and
      must NOT be summed; the quotient of the two convergent entry
      values is the meaningful object.)
  P4  the same for S⁺₂₁, S⁺₂₂ (completeness; S⁺₂₁ q→0 = 0).

Reported against A_ω = 3 as a scope-(a) measurement: whatever the number
is, it is recorded as-is. Nothing is fitted, nothing is wired; the T5
`A_ω` field stays as it is until a derivation (not a measurement) says
otherwise. Exact integer series + mpmath evaluation only (no float64).

Run: python3 -u computations/probes/qbeta_3bp8_sigma12_substrate_probe.py \
       2>&1 | tee /tmp/qbeta_3bp8_sigma12.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

from qbeta_g3_ggm_stokes_41 import (  # noqa: E402
    W_matrix, mat_mul_series, const_mat, transpose,
    PRINTED_61, RATIO_62, RATIO_63,
)

set_compute_dps()

ORD = 1600
CUTS = (800, 1200, 1600)
# the certified sandwich exemplar (derived + certified in the g3 probe)
SGN, A_M, B_M, C_M = -1, [[0, 1], [1, 1]], [[0, 1], [1, 0]], [[0, 1], [-1, -2]]
A_OMEGA_T4 = mp.mpf(3)


def ladder_eval(coeffs, q_sub):
    """Evaluate an integer q-series at q_sub over the cut ladder; return
    (value, agree_digits, {cut: partial})."""
    partials = {}
    for c in CUTS:
        partials[c] = mp.fsum(co * q_sub ** k
                              for k, co in enumerate(coeffs[:c + 1]) if co)
    full = partials[CUTS[-1]]
    d = abs(full - partials[CUTS[-2]])
    dig = 40 if d == 0 else (int(-mp.log10(d)) if d < 1 else 0)
    return full, dig, partials


def main() -> int:
    q0 = q_at(50)
    q_sub = 1 / q0
    print("=" * 78)
    print(" qou-3bp8 — σ₁σ₂ substrate value: the deformation of A_ω = 3")
    print("=" * 78)

    # rebuild the certified sandwich at deep order
    t0 = time.time()
    Wd = W_matrix(-1, ORD)
    core = mat_mul_series(
        mat_mul_series(Wd, const_mat(B_M, ORD), ORD), transpose(Wd), ORD)
    Sd = mat_mul_series(
        mat_mul_series(const_mat(A_M, ORD), core, ORD), const_mat(C_M, ORD), ORD)
    S = {(i, j): [SGN * x // 2 for x in Sd[i][j]] for i in (0, 1) for j in (0, 1)}
    print(f"  sandwich rebuilt at q-order {ORD} [{time.time()-t0:.0f}s]")

    # gate: printed heads
    head_11_ok = S[(0, 0)][:7] == PRINTED_61
    # S12 head: ratio (62) x S11 => check S12 head directly against the
    # product of the printed ratio and printed S11 through q^3
    r12_head = [3, 9, 75, 642]
    prod = [sum(r12_head[i] * PRINTED_61[k - i] for i in range(k + 1) if k - i < 7)
            for k in range(4)]
    head_12_ok = S[(0, 1)][:4] == prod
    print(f"  gate: S₁₁ head == printed (61): {head_11_ok}")
    print(f"  gate: S₁₂ head == (62)×(61) product: {head_12_ok} "
          f"(S₁₂ head {S[(0,1)][:4]}, expected {prod})")

    print(f"\n  substrate q̃ = 1/q₀ = {mp.nstr(q_sub, 12)}; ladder {CUTS}:")
    vals, digs, parts = {}, {}, {}
    names = {(0, 0): "S⁺₁₁ (σ₁σ₁)", (0, 1): "S⁺₁₂ (σ₁σ₂ ← A_ω = 3)",
             (1, 0): "S⁺₂₁", (1, 1): "S⁺₂₂"}
    for key in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        v, d, p = ladder_eval(S[key], q_sub)
        vals[key], digs[key], parts[key] = v, d, p
        print(f"    {names[key]:<24} = {mp.nstr(v, 16):>22}  [{d:>2} agree-digits]")

    conv_ok = min(digs.values()) >= 8

    # P3: ratio of VALUES (the ratio series diverges at the substrate)
    ratio_val = vals[(0, 1)] / vals[(0, 0)]
    print(f"\n  S⁺₁₂/S⁺₁₁ as a ratio of VALUES = {mp.nstr(ratio_val, 16)}")
    print(f"    (the printed ratio SERIES 3 + 9q̃ + 75q̃² + 642q̃³ + … has "
          f"coefficients growing ~8.7×/order,")
    print(f"     radius ≈ 0.115 — it DIVERGES at q̃ = {mp.nstr(q_sub, 6)} and "
          f"must not be summed.)")

    dev_12 = vals[(0, 1)] / A_OMEGA_T4
    dev_ratio = ratio_val / A_OMEGA_T4
    print(f"\n  vs the T4/T5 constant A_ω = 3:")
    print(f"    S⁺₁₂(q̃_sub)/3       = {mp.nstr(dev_12, 12)}")
    print(f"    (S⁺₁₂/S⁺₁₁)/3       = {mp.nstr(dev_ratio, 12)}")

    verdict = (
        f"σ₁σ₂ SUBSTRATE MEASUREMENT (the channel that actually carries the "
        f"T4/T5 A_ω): S⁺₁₂(q̃_sub) = {mp.nstr(vals[(0,1)], 12)} "
        f"[{digs[(0,1)]}d], i.e. {mp.nstr(dev_12, 6)}× the q→0 integer 3; the "
        f"value-ratio S⁺₁₂/S⁺₁₁ = {mp.nstr(ratio_val, 12)} "
        f"({mp.nstr(dev_ratio, 6)}× 3). Scope-(a) MEASUREMENT of how far the "
        f"Stokes constant has deformed at the substrate — NOT a derivation of "
        f"A_ω and NOT wired; the T5 A_ω field is untouched. Channel-correctness "
        f"note: the qou-awpk/W2 winding results (ϑ-dependence, bar-odd part, "
        f"Im-ratio −6.03) belong to σ₁σ₁, whose substrate value is 0.4276, so "
        f"they are cross-channel to A_ω and cannot settle it. The x-refinement "
        f"of σ₁σ₂ is NOT proven in the literature for 4₁ — that is the honest "
        f"gap between this measurement and the winding programme."
        if conv_ok and head_11_ok and head_12_ok else
        "INCONCLUSIVE — a gate or the ladder failed; inspect the log.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-3bp8-sigma12-substrate", engine="python-int+mpmath")
    wb.set_description(
        "Substrate value of the sigma1sigma2 Stokes entry of 4_1 — the entry "
        "whose q->0 value is the integer A_omega = 3 used by the T4/T5 chain "
        "(GGM eq 60, S+(0) = [[1,3],[0,1]]). Computed from the OCR-free "
        "certified sandwich (qbeta_g3_ggm_stokes_41) at q-order 1600 with the "
        "honest ladder guard. Channel-correctness audit: the qou-awpk / W2 "
        "winding results are sigma1sigma1 (substrate value 0.4276), so they "
        "are cross-channel to A_omega; the x-refinement of sigma1sigma2 is not "
        "proven in the literature for 4_1. Scope-(a) measurement; nothing "
        "fitted, nothing wired, T5 A_omega field untouched.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("sandwich_exemplar", {"sign": SGN, "A": A_M, "B": B_M, "C": C_M,
                                      "source": "qbeta_g3_ggm_stokes_41 (derived + certified)"})
    wb.add_data("entry_values", {
        f"S{i+1}{j+1}": {"value": mp.nstr(vals[(i, j)], 20),
                         "agree_digits": digs[(i, j)],
                         "ladder": {str(c): mp.nstr(parts[(i, j)][c], 16) for c in CUTS}}
        for i in (0, 1) for j in (0, 1)})
    wb.add_data("value_ratio_S12_over_S11", mp.nstr(ratio_val, 20))
    wb.add_data("ratio_series_diverges_note",
                "the printed S12/S11 ratio series (3, 9, 75, 642, 5580, 48558, "
                "422865, ...) grows ~8.7x/order, radius ~0.115: it diverges at "
                "q_sub = 0.9009 and must not be summed; the quotient of the two "
                "convergent entry values is the meaningful object")
    wb.add_data("vs_A_omega_3", {
        "S12_over_3": mp.nstr(dev_12, 12),
        "value_ratio_over_3": mp.nstr(dev_ratio, 12),
        "A_omega_T4": "3 (q->0 integer, GGM eq 60 (1,2) entry)"})
    wb.add_data("channel_correctness", {
        "A_omega_channel": "sigma1sigma2 = (1,2) entry (q->0 value 3)",
        "x_refined_channel": "sigma1sigma1 = (1,1) entry (substrate value 0.4276)",
        "consequence": "qou-awpk/W2 winding results are cross-channel to A_omega; "
                       "the sigma1sigma2 x-refinement is not proven for 4_1 in "
                       "the literature — the honest gap"})
    wb.add_data("verdict", verdict)
    wb.add_assertion("printed_heads_gate",
                     computed=1.0 if (head_11_ok and head_12_ok) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="rebuilt sandwich reproduces the printed (61) head and "
                            "the (62)x(61) product head for S12")
    wb.add_assertion("ladder_converged",
                     computed=1.0 if conv_ok else 0.0, expected=1.0, tolerance=0.5,
                     source=f"every entry agrees to >=8 digits between q-orders "
                            f"{CUTS[-2]} and {CUTS[-1]}")
    wb.save()
    print("  witness -> computations/probes/qbeta-3bp8-sigma12-substrate.witness.json")
    return 0 if (conv_ok and head_11_ok and head_12_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
