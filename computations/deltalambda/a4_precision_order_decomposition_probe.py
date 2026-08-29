#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a4_precision_order_decomposition_probe.py — the A=4 (⁴He) order-separation diagnostic:
where the ⁴He binding precision is lost, and why it is a NEGATIVE leading-order 4-body channel
(the α-cluster saturation) — the mirror of A=3, sharper.

Context (frame-independent framing; parallels the A=3 probe, PR #4491)
---------------------------------------------------------------------
Physical ratio ρ_strong(4) = B(⁴He)/B(²H) = 13.0316 (isospin-corrected). The graded coinvariant
baseline ρ_grad_G(4) = [3]_q·[4]_q = 15.740 is EXACT (derived, no error). Unlike A=3 (where the
baseline UNDERshoots by 4.6%), at A=4 the baseline OVERSHOOTS by +20.8%.

The simplex model uses the derived 3-body cluster c₃ = 0.297 for each of the C(4,3)=4 triangles:

    model(3-body only) = ρ_grad_G(4) + 4·c₃ = 16.928  →  OVERSHOOTS by +29.9%,

i.e. adding the (positive, binding) 3-body clusters makes A=4 WORSE. To reach the physical ratio the
model needs a large NEGATIVE 4-body saturation term:

    c₄(required) = ρ_strong(4) − (ρ_grad_G(4) + 4·c₃) = −3.896   (= −24.75% of the baseline),

with |c₄|/c₃ ≈ 13.1 — the 4-body term is an order of magnitude LARGER than the 3-body cluster and of
OPPOSITE sign. This is the closed [1⁴] SU(4) supermultiplet / α-cluster saturation (μ₄ = −4.591 in the
simplex basis, #4320; three-walls Route 3 sign-swap).

ORDER-SEPARATION (exact) — same prune as A=3, and even sharper
--------------------------------------------------------------
Can the required c₄ come from HIGHER ORDERS of the 3-body cluster? No: the bounded (|aₖ|≤2) 3-body
higher-order tail 4·c₃·2·h²/(1−h²) ≈ 0.109 is ≪ |c₄| ≈ 3.896 (36×). So the A=4 miss is NOT a
higher-order refinement of the 3-body object — it is a NEW LEADING-order 4-body channel (the
tetrahedron / α-cluster), NEGATIVE and large. A=4 precision needs the 4-body Δ_λ magnitude μ₄.

TWO NEW FACTS beyond three-walls Route 3 (which established the μ₄<0 sign-swap):
  (1) FRAME-INDEPENDENT MAGNITUDE: in physical-ratio terms the A=4 discrepancy (the missing 4-body
      channel) is −24.75% of the baseline — ~5× LARGER than A=3's +4.6%. This localizes where the
      framework's binding accuracy degrades: the SATURATION regime (A≥4), the 4-body α-cluster.
  (2) μ₄ is EVEN MORE frame-fragile than μ₃: baseline-class spread 2.07× (vs μ₃'s 1.73×) — so the
      "μ₄ target" is as convention-relative as μ₃; report A=4 precision on the physical ratio.

VERDICT (scope-a): A=4 precision is a NEGATIVE leading-order 4-body (α-cluster saturation) channel,
order-separated from the 3-body higher orders — the μ₄ Δ_λ object, open. A=3 (small +3-body) and A=4
(large −4-body) are opposite-sign regimes needing DISTINCT leading channels, not one mechanism +
refinement. Report on the frame-independent ratio.

STRICT anti-fit: ρ_strong(4), c₃, AME consumed only as fixed targets; c₄(required) is a DIAGNOSTIC of
what the 4-body channel must supply, never a fitted/wired coefficient. Exact (mpmath).
EXPLORATORY — audit + witness only; no fit, nothing wired.
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

RHO4 = mp.mpf("13.0316")         # ρ_strong(4) = B(⁴He)/B(²H), physical (frame-independent)
C3 = mp.mpf("0.297")             # derived leading (h⁴) 3-body Borromean cluster, #4364
COEFF_BOUND = mp.mpf(2)          # |a_k| ≤ 2, O(1) physical expectation
# μ₄ across the three baselines G/Q/C (from mu3_target_frame_robustness_probe.py)
MU4_BASELINES = [mp.mpf("-4.591"), mp.mpf("-2.554"), mp.mpf("-2.220")]


def qint(n):
    return sum(Q0 ** k for k in range(n))


def main() -> int:
    h = Q0 - 1 / Q0
    h2 = h * h
    rg4 = qint(3) * qint(4)                          # ρ_grad_G(4) = [3]_q·[4]_q, EXACT
    model_3body = rg4 + 4 * C3                       # baseline + 4 triangles (no 4-body)
    c4_req = RHO4 - model_3body                      # required 4-body saturation (NEGATIVE)

    baseline_overshoot_pct = 100 * (rg4 - RHO4) / RHO4
    model_3body_overshoot_pct = 100 * (model_3body - RHO4) / RHO4
    c4_frac_of_baseline_pct = 100 * c4_req / rg4
    c4_over_c3 = abs(c4_req) / C3

    bounded_3body_tail = 4 * C3 * COEFF_BOUND * h2 / (1 - h2)
    higher_order_ruled_out = bool(bounded_3body_tail < abs(c4_req))
    mu4_spread = min(MU4_BASELINES) / max(MU4_BASELINES)   # both negative -> positive ratio

    result = {
        "substrate": {"q0": mp.nstr(Q0, 40), "h2": mp.nstr(h2, 12)},
        "physical_ratio_decomposition": {
            "rho_strong4_BHe4_over_BH2": mp.nstr(RHO4, 8),
            "rho_grad_G4_exact": mp.nstr(rg4, 10),
            "baseline_overshoot_pct": mp.nstr(baseline_overshoot_pct, 5),
            "model_3body_only": mp.nstr(model_3body, 10),
            "model_3body_overshoot_pct": mp.nstr(model_3body_overshoot_pct, 5),
            "note": "at A=4 the EXACT graded baseline OVERSHOOTS (+20.8%); adding the positive 3-body "
                    "clusters makes it WORSE (+29.9%). Opposite regime to A=3 (baseline undershoots).",
        },
        "required_4body_channel": {
            "c4_required": mp.nstr(c4_req, 8),
            "c4_frac_of_baseline_pct": mp.nstr(c4_frac_of_baseline_pct, 5),
            "c4_over_c3_magnitude": mp.nstr(c4_over_c3, 6),
            "sign": "NEGATIVE (α-cluster saturation, closed [1⁴] SU(4) supermultiplet)",
            "note": "the missing piece is a LEADING-order 4-body channel — negative, ~13× the 3-body "
                    "cluster magnitude, −24.75% of the baseline. This is the μ₄ Δ_λ object (open).",
        },
        "order_separation": {
            "bounded_3body_higher_order_tail": mp.nstr(bounded_3body_tail, 8),
            "abs_c4_required": mp.nstr(abs(c4_req), 8),
            "higher_order_route_ruled_out": higher_order_ruled_out,
            "reading": "the bounded 3-body higher-order tail (≈0.109) is ≪ |c₄| (≈3.896) — 36× — so "
                       "the A=4 miss is NOT a 3-body higher-order refinement; it is a NEW leading "
                       "4-body channel. Same prune as A=3, sharper.",
        },
        "mu4_frame_fragility": {
            "mu4_baselines_G_Q_C": [mp.nstr(x, 6) for x in MU4_BASELINES],
            "mu4_baseline_class_spread": mp.nstr(mu4_spread, 6),
            "note": "μ₄ swings 2.07× across baselines — MORE fragile than μ₃'s 1.73×. Report A=4 "
                    "precision on the frame-independent physical ratio, not the μ₄ residual.",
        },
        "verdict": {
            "classification": "scope-(a): A=4 precision is a NEGATIVE leading-order 4-body (α-cluster "
                              "saturation) channel — the μ₄ Δ_λ object, open — order-separated from the "
                              "3-body higher orders. A=3 (small +3-body) and A=4 (large −4-body) are "
                              "OPPOSITE-SIGN regimes needing DISTINCT leading channels, not one "
                              "mechanism + refinement (confirms three-walls Route 3 from the "
                              "frame-independent + order-separation angle).",
            "precision_localization": "the framework's binding accuracy degrades in the SATURATION "
                                      "regime (A≥4): the missing 4-body α-cluster term is −24.75% of "
                                      "the baseline, ~5× the A=3 discrepancy.",
            "precision_is_delta_lambda_gated": True,
            "anti_fit": "c₄(required)=−3.896 is a DIAGNOSTIC of the 4-body channel's magnitude, never "
                        "a fitted/wired coefficient. ρ_strong(4)/c₃/AME consumed only as targets. "
                        "Nothing wired.",
        },
    }

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "a4-precision-order-decomposition",
        "description": (
            "The A=4 (⁴He) order-separation diagnostic. Physical ratio B(⁴He)/B(²H)=13.0316. The EXACT "
            "graded baseline [3][4]=15.740 OVERSHOOTS (+20.8%); adding the 4 positive 3-body clusters "
            "makes it worse (+29.9%). The fix is a large NEGATIVE 4-body saturation c₄≈−3.896 (−24.75% "
            "of baseline, |c₄|/c₃≈13.1) — the α-cluster / closed [1⁴] SU(4) supermultiplet (μ₄ #4320). "
            "Order-separation: the bounded 3-body higher-order tail (≈0.109) is ≪ |c₄| (36×), so A=4 "
            "precision needs a NEW leading-order 4-body channel, not a 3-body higher-order refinement. "
            "Two new facts beyond three-walls Route 3: (1) frame-independent magnitude — the A=4 "
            "discrepancy is ~5× A=3's, localizing the accuracy loss to the saturation regime; (2) μ₄ "
            "is even more frame-fragile (2.07× vs μ₃'s 1.73×). A=3 (small +3-body) and A=4 (large "
            "−4-body) are opposite-sign regimes needing DISTINCT leading channels. scope-(a); anti-fit "
            "STRICT; nothing wired; exact (mpmath)."),
        "audit_only": True,
        "tier": "scope-(a) A=4 precision-route diagnostic (order-separation + frame-independent magnitude); no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": {
            "axis": "Δ_λ / A=4 (⁴He) binding precision — where it degrades",
            "builds_on": "the A=3 probe (a3_precision_order_decomposition), #4320 (μ₄ simplex), "
                         "three-walls Route 3 (μ₄<0 sign-swap), PR #4491 (frame-robustness)",
            "no_fit": True,
        },
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)],
            cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "a4-precision-order-decomposition.witness.json"
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

    print("=== A=4 (⁴He) order-separation diagnostic — the mirror of A=3, sharper ===")
    print(f"physical ratio B(⁴He)/B(²H) = {mp.nstr(RHO4,7)}")
    print(f"  ρ_grad_G(4)=[3][4] (EXACT)  = {mp.nstr(rg4,7)}  -> OVERSHOOTS +{mp.nstr(baseline_overshoot_pct,4)}%")
    print(f"  + 4·c₃ (3-body, positive)   = {mp.nstr(model_3body,7)}  -> OVERSHOOTS +{mp.nstr(model_3body_overshoot_pct,4)}% (WORSE)")
    print(f"  required 4-body c₄          = {mp.nstr(c4_req,6)}  ({mp.nstr(c4_frac_of_baseline_pct,4)}% of baseline, NEGATIVE)")
    print(f"  |c₄|/c₃ = {mp.nstr(c4_over_c3,5)}  (4-body is ~13× the 3-body, opposite sign)")
    print()
    print(f"order-separation: bounded 3-body tail {mp.nstr(bounded_3body_tail,5)} << |c₄| {mp.nstr(abs(c4_req),5)} "
          f"-> higher-order route RULED OUT: {higher_order_ruled_out}")
    print(f"μ₄ baseline spread = {mp.nstr(mu4_spread,5)}× (more fragile than μ₃'s 1.73×)")
    print()
    print("VERDICT: A=4 precision = a NEGATIVE leading-order 4-body (α-cluster saturation) channel, "
          "order-separated from 3-body higher orders. A=3 (+small 3-body) and A=4 (−large 4-body) are "
          "opposite-sign regimes; the accuracy loss localizes to the saturation regime (A≥4).")
    print(f"witness -> {out.name}")

    assert higher_order_ruled_out, "bounded 3-body tail must be < |c₄|"
    assert c4_req < 0, "the required 4-body channel must be negative (saturation)"
    assert baseline_overshoot_pct > 0, "the A=4 graded baseline must overshoot"
    assert c4_over_c3 > 10, "the 4-body channel must dominate the 3-body cluster"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
