#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a3_precision_order_decomposition_probe.py — HOW to improve A=3 binding precision:
localize where the ~4.6% miss on B(³H)/B(²H) lives, and rule out the routine
"compute higher cluster orders" route (formalize-first pruning).

Context (frame-independent framing, from the μ₃ frame-robustness finding, PR #4491)
----------------------------------------------------------------------------------
The corpus model's A=3 prediction of the physical ratio ρ_strong(3)=B(³H)/B(²H)=3.8128 is

    model = ρ_grad_G(3) + c₃ = 3.3420 + 0.297 = 3.6390,   miss Δ = 0.17377 (4.56% of ρ).

The dominant term ρ_grad_G(3)=[3]_q (the graded coinvariant dimension) is EXACT (derived, no
error, 87.6% of the ratio). c₃=0.297 is the DERIVED leading (h⁴) Borromean 3-body cluster
(BorromeanMagnitudeLift #4364). So ALL of the 4.56% error lives in the subleading many-body
cluster. The precision question is sharp: can the missing 0.17377 be supplied by HIGHER cluster
ORDERS (h⁶, h⁸, …) of the same 3-body object, or does it need a NEW leading-order channel?

THE ORDER-SEPARATION (exact)
----------------------------
Write the categorical 3-body cluster as c₃·(1 + a₁h² + a₂h⁴ + …), h = q−q⁻¹. A higher-order
closure of the miss needs

    a₁ ≈ Δ / (c₃ · h²) = 0.17377 / (0.297 · 0.043706) ≈ 13.4,

i.e. an h⁶ coefficient THIRTEEN TIMES the natural O(1) size. A bounded-coefficient expansion
(|aₖ| ≤ 2, the physical expectation) has an entire higher-order TAIL bounded by
c₃·2·h²/(1−h²) ≈ 0.027 — only ~0.7% of the ratio, ≪ the 4.56% miss. So:

  ROUTINE higher-order refinement (O(1) coefficients) CANNOT close the A=3 miss — it supplies at
  most ~0.7%. Closing it needs EITHER (i) a NEW leading-order (h⁴) 3-body channel of size
  ~0.585·c₃, OR (ii) an ANOMALOUSLY LARGE (~13) h⁶ coefficient — which is itself a fit red-flag
  (cf. the Q_β c₃ 1/u³ hypersensitivity, `2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`).

CONSEQUENCE FOR PRECISION STRATEGY (honest)
-------------------------------------------
  * Improving A=3 precision is NOT a "compute more cluster orders" problem — that route is
    order-separated out (this probe).
  * It IS the Δ_λ closure problem: the missing leading-order channel is a per-partition
    magnitude the Δ_λ gate must supply. A=3 ratio precision is Δ_λ-GATED, not q₀-limited (the
    overall scale cancels in the ratio).
  * Report precision on the frame-INDEPENDENT physical ratio B(A)/B(²H), not the
    convention-relative residual μ_k (which amplifies the miss ~8× and is baseline-class-
    relative, PR #4491). The honest current A=3 accuracy is ~4.6%, improvable only by a derived
    Δ_λ term — the probed 0-fit candidates (weight/width/level) do not supply it (three walls,
    `2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`).

STRICT anti-fit: ρ_strong, c₃, AME consumed only as fixed targets; the required a₁≈13.4 is a
DIAGNOSTIC of what a higher-order closure would need, NOT a fitted coefficient wired anywhere.
Exact (mpmath). EXPLORATORY — audit + witness only; no fit, nothing wired.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

JET_WITNESS = HERE / "deltalambda-jet-filtration-magnitude.witness.json"
Q0 = mp.mpf(str(json.loads(JET_WITNESS.read_text())["parameters"]["q0"]))

RHO3 = mp.mpf("3.8128")          # ρ_strong(3) = B(³H)/B(²H), physical (frame-independent)
C3 = mp.mpf("0.297")             # derived leading (h⁴) Borromean 3-body cluster, #4364
COEFF_BOUND = mp.mpf(2)          # |a_k| ≤ 2, the O(1) physical expectation for cluster coeffs


def main() -> int:
    h = Q0 - 1 / Q0
    h2 = h * h
    rg3 = 1 + Q0 + Q0 ** 2                          # ρ_grad_G(3) = [3]_q, EXACT
    model = rg3 + C3
    miss = RHO3 - model                             # the still-missing part of the ratio

    # order-separation: the h⁶ coefficient a higher-order closure would need
    a1_required = miss / (C3 * h2)
    # bounded (|a_k| ≤ B) higher-order tail: c₃·B·(h² + h⁴ + …) = c₃·B·h²/(1−h²)
    bounded_tail_max = C3 * COEFF_BOUND * h2 / (1 - h2)
    # what fraction of the physical ratio each piece is
    frac_baseline = rg3 / RHO3
    frac_c3 = C3 / RHO3
    frac_miss = miss / RHO3

    higher_order_route_ruled_out = bool(bounded_tail_max < miss)      # tail can't close it
    required_coeff_anomalous = bool(a1_required > 10)                 # ≫ O(1)

    result = {
        "substrate": {"q0": mp.nstr(Q0, 40), "h": mp.nstr(h, 12), "h2": mp.nstr(h2, 12)},
        "physical_ratio_decomposition": {
            "rho_strong3_BH3_over_BH2": mp.nstr(RHO3, 8),
            "rho_grad_G3_exact": mp.nstr(rg3, 10),
            "rho_grad_frac_of_ratio": mp.nstr(frac_baseline, 6),
            "c3_leading_cluster_h4": mp.nstr(C3, 6),
            "c3_frac_of_ratio": mp.nstr(frac_c3, 6),
            "miss": mp.nstr(miss, 10),
            "miss_frac_of_ratio_pct": mp.nstr(100 * frac_miss, 6),
            "note": "the EXACT graded baseline is 87.6% of the ratio; the derived leading cluster "
                    "is 7.8%; ALL 4.56% of the error is in the subleading many-body cluster.",
        },
        "order_separation": {
            "miss_over_c3": mp.nstr(miss / C3, 8),
            "h2_natural_next_order_size": mp.nstr(h2, 8),
            "required_h6_coefficient_a1": mp.nstr(a1_required, 8),
            "required_a1_vs_O1": mp.nstr(a1_required, 6) + " (≈13× the O(1) natural size)",
            "coeff_bound_used": mp.nstr(COEFF_BOUND, 4),
            "bounded_tail_max_close": mp.nstr(bounded_tail_max, 8),
            "bounded_tail_frac_of_ratio_pct": mp.nstr(100 * bounded_tail_max / RHO3, 6),
            "higher_order_route_ruled_out": higher_order_route_ruled_out,
            "required_coeff_anomalous": required_coeff_anomalous,
        },
        "verdict": {
            "classification": "scope-(a): the ROUTINE higher-cluster-order route to A=3 precision is "
                              "ORDER-SEPARATED OUT. A bounded (|a_k|≤2) cluster tail closes ≤0.7% of "
                              "the ratio, ≪ the 4.56% miss; a higher-order closure would need an "
                              "h⁶ coefficient a₁≈13.4 (a fit red-flag, cf. Q_β c₃ 1/u³ "
                              "hypersensitivity). Precision needs a NEW leading-order (h⁴) 3-body "
                              "channel — the Δ_λ closure — not a finer expansion.",
            "precision_is_delta_lambda_gated": True,
            "precision_not_q0_limited": "the overall scale cancels in the ratio B(³H)/B(²H); A=3 "
                                        "ratio precision is a categorical (Δ_λ) question, not a q₀ "
                                        "or CAL-2-floor question.",
            "reporting_recommendation": "report A=3 precision as ~4.6% on the frame-INDEPENDENT "
                                        "physical ratio, not as a '1.6× gap' on the convention-"
                                        "relative residual μ₃ (which amplifies it ~8×, PR #4491).",
            "anti_fit": "a₁≈13.4 is a DIAGNOSTIC of what a higher-order closure would need, never a "
                        "fitted/wired coefficient. ρ_strong/c₃/AME consumed only as targets. "
                        "Nothing wired.",
        },
    }

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "a3-precision-order-decomposition",
        "description": (
            "HOW to improve A=3 binding precision. The corpus model predicts B(³H)/B(²H)=3.8128 to "
            "4.56%; the dominant graded baseline ρ_grad_G(3)=[3]_q is EXACT (87.6% of the ratio) and "
            "the derived leading Borromean cluster c₃=0.297 is 7.8%, so ALL the error is subleading. "
            "Order-separation: closing the 0.17377 miss by higher cluster orders needs an h⁶ "
            "coefficient a₁≈13.4 (13× the O(1) natural size); a bounded (|a_k|≤2) tail closes ≤0.7% "
            "of the ratio ≪ 4.56%. So the routine higher-order route is RULED OUT — precision needs "
            "a new leading-order (h⁴) 3-body channel (the Δ_λ closure) or an anomalous fit-flag "
            "coefficient. A=3 ratio precision is Δ_λ-gated, NOT q₀-limited (scale cancels in the "
            "ratio). Report precision on the frame-independent physical ratio, not the μ₃ residual "
            "(which amplifies ~8×). scope-(a); anti-fit STRICT; nothing wired; exact (mpmath)."),
        "audit_only": True,
        "tier": "scope-(a) precision-route pruning (order-separation of the higher-cluster route); no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": {
            "axis": "Δ_λ / A=3 binding precision — how to improve it",
            "builds_on": "PR #4491 (μ₃ frame-robustness, frame-independent ratio), #4364 (c₃ leading "
                         "cluster), three-walls audit, Q_β c₃ hypersensitivity (2026-07-12)",
            "no_fit": True,
        },
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)],
            cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "a3-precision-order-decomposition.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        # q0_anchor was `False` -- the declaration "this witness carries no
        # q0-dependent field" (see WitnessBuilder.stamp_staleness_metadata).
        # It is not true of this producer: it reads q0 out of the
        # jet-filtration witness at module scope and records it under
        # `result.substrate.q0`, and every q-integer below is a function of
        # it. The false declaration DELETED the anchor stamp on every run,
        # turning a visible Q0_FLIP into a silent Q0_ANCHOR_MISSING.
        # Resolving (the default) is correct now that the upstream
        # jet-filtration probe resolves its own pin rather than freezing it.
        witness, script_path=__file__, engine=None)
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")

    print("=== HOW to improve A=3 binding precision — order decomposition ===")
    print(f"physical ratio B(³H)/B(²H) = {mp.nstr(RHO3,8)}")
    print(f"  ρ_grad_G(3)=[3]_q (EXACT)   = {mp.nstr(rg3,8)}  ({mp.nstr(100*frac_baseline,5)}% of ratio)")
    print(f"  c₃ leading cluster (h⁴)     = {mp.nstr(C3,6)}  ({mp.nstr(100*frac_c3,5)}% of ratio)")
    print(f"  MISSING                     = {mp.nstr(miss,8)}  ({mp.nstr(100*frac_miss,5)}% of ratio)")
    print()
    print(f"order-separation: a higher-order closure needs h⁶ coeff a₁ ≈ {mp.nstr(a1_required,6)} "
          f"(= {mp.nstr((miss/C3)/h2,5)}× the natural h² size)")
    print(f"  bounded (|a_k|≤2) tail closes ≤ {mp.nstr(bounded_tail_max,6)} "
          f"({mp.nstr(100*bounded_tail_max/RHO3,4)}% of ratio) ≪ miss {mp.nstr(miss,5)}")
    print(f"  ⇒ routine higher-order route RULED OUT: {higher_order_route_ruled_out}; "
          f"required coeff anomalous (>10): {required_coeff_anomalous}")
    print()
    print("VERDICT: A=3 precision is Δ_λ-gated (needs a new LEADING-order channel), not a "
          "higher-cluster-order refinement. Report % on the physical ratio, not the μ₃ residual.")
    print(f"witness -> {out.name}")

    assert higher_order_route_ruled_out, "bounded higher-order tail must be < the miss"
    assert required_coeff_anomalous, "required h⁶ coefficient must be anomalous (≫ O(1))"
    assert frac_baseline > mp.mpf("0.87"), "graded baseline must dominate the ratio"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
