#!/usr/bin/env python3
"""
probe_d_cocasimir_barparity.py — which bar-parity SECTOR does the refuted
Frobenius co-Casimir Δ_λ ansatz live in, and what does that say about its
refutation? (session 2026-07-05; follow-up to probe_d_barparity_binding.py.)

EXPLORATORY (probe_ prefix, audit-only). NOT a closure ansatz (Δ_λ gate). This
CHARACTERISES an already-refuted ansatz (co-Casimir, refuted in
`QOU/BraidKnot/DeltaLambdaRefutation.lean` / `lem:frobenius-cocasimir-refuted-deuteron`);
it proposes no new closure.

## The question

`probe_d_barparity_binding` proved the deuteron A=2 binding scalar
Σ_λ a_λ Δ_λ (a_λ = y_λ·χ^λ(β_D)) is a purely BAR-EVEN functional: the bar-odd
projection of a_λ under λ↔λ' sums to exactly 0. So a bar-even Δ_λ couples to
a^even, a bar-odd Δ_λ to a^odd, and BOTH sectors can produce nonzero binding —
neither is structurally excluded. This probe asks the concrete follow-up: which
sector does the refuted co-Casimir ansatz actually occupy, and does its known
refutation (wrong sign + magnitude) come from the sector or from the numbers?

## What the committed witness shows (rho-k-h3a-co-casimir, H_6, 11 λ⊢6)

`Delta_lambda_co_casimir` is read directly from the witness `per_lambda` rows.
Empirically it is BAR-EVEN: Δ_λ = Δ_{λ'} on every conjugate pair (e.g.
[6]=[1⁶]=1.0, [5,1]=[2,1⁴]=0.19155, [4,2]=[2,2,1,1]=0.10342). This is the
NORM-type Casimir (∝ Σ content², conjugation-invariant), NOT the linear content
sum Σ(j−i) (which WOULD be bar-odd). Recorded here to correct a natural
mis-expectation: "co-Casimir is bar-odd" is FALSE for this construction.

## The finding

- co-Casimir Δ_λ is bar-EVEN ⇒ it lives in the SAME sector as the binding
  target (a^even). Its prediction Σ a_λ Δ_λ = Σ a^even_λ Δ_λ (the bar-odd part
  of a contributes 0), reproducing the witness `co_casimir_prediction`.
- Therefore the co-Casimir refutation (Σ = +0.145 vs target −4.353: wrong sign,
  ~30× magnitude) is a SCOPE-(a) NUMERICAL failure of an ansatz that is in the
  RIGHT sector — NOT a scope-(b) sector/subspace exclusion. It corroborates
  `probe_d_barparity_binding`: bar-symmetric ansätze are not structurally
  excluded; they simply give the wrong number.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
set_compute_dps()
DPS = COMPUTE_DPS

from witness_base import WitnessBuilder  # noqa: E402


def _pkey(v):
    if isinstance(v, list):
        return tuple(int(x) for x in v)
    return tuple(int(x) for x in str(v).strip("[]").split(",") if x.strip())


def conjugate(part):
    if not part:
        return ()
    m = max(part)
    return tuple(sum(1 for a in part if a >= i) for i in range(1, m + 1))


def _l2(vals):
    return mp.sqrt(sum(v ** 2 for v in vals))


def main() -> int:
    # WitnessBuilder first so the upstream witness is hash-recorded for the
    # drift validator (`data.upstream_witness_hashes`; witness_dependency_drift.py).
    wb = WitnessBuilder("probe-d-cocasimir-barparity", engine="mpmath")
    cc = wb.add_upstream(COMP / "rho-k-h3a-co-casimir.witness.json")

    rows = {_pkey(r["partition"]): r for r in cc["data"]["per_lambda"]}
    target = mp.mpf(str(cc["data"]["target_signed"]))
    witness_pred = mp.mpf(str(cc["data"]["co_casimir_prediction"]
                               ["sum_contributions_signed"]))

    delta = {p: mp.mpf(str(rows[p]["Delta_lambda_co_casimir"])) for p in rows}
    a = {p: mp.mpf(str(rows[p]["y_chi_product_signed"])) for p in rows}  # y_λ·χ^λ(β_D)

    # (1) is co-Casimir Δ_λ bar-even or bar-odd?  max deviation from each parity.
    even_dev = max(abs(delta[p] - delta[conjugate(p)]) for p in delta)   # 0 if bar-even
    odd_dev = max(abs(delta[p] + delta[conjugate(p)]) for p in delta)    # 0 if bar-odd

    # (2) bar-parity split of the binding coefficient a_λ under λ↔λ'
    a_even = {p: (a[p] + a[conjugate(p)]) / 2 for p in a}
    a_odd = {p: (a[p] - a[conjugate(p)]) / 2 for p in a}

    # (3) co-Casimir prediction and its sector decomposition
    pred_full = sum(a[p] * delta[p] for p in a)
    pred_even = sum(a_even[p] * delta[p] for p in a)   # even-sector coupling
    pred_odd = sum(a_odd[p] * delta[p] for p in a)     # odd-sector coupling (→0 if Δ bar-even)

    is_even = even_dev < mp.mpf("1e-30")
    parity = "BAR-EVEN" if is_even else ("BAR-ODD" if odd_dev < mp.mpf("1e-30") else "MIXED")

    print("=" * 90)
    print("CO-CASIMIR Δ_λ — WHICH BAR-PARITY SECTOR, AND WHAT DOES THE REFUTATION MEAN?")
    print("=" * 90)
    print(f"  Δ_λ parity: {parity}   (‖Δ_λ − Δ_λ'‖∞ = {float(even_dev):.2e}, "
          f"‖Δ_λ + Δ_λ'‖∞ = {float(odd_dev):.2e})")
    print(f"  ‖a^even‖₂ = {mp.nstr(_l2(a_even.values()),8)}   "
          f"‖a^odd‖₂ = {mp.nstr(_l2(a_odd.values()),8)}")
    print(f"  co-Casimir prediction  Σ a_λ Δ_λ           = {mp.nstr(pred_full,10)}")
    print(f"    from EVEN sector  Σ a^even_λ Δ_λ         = {mp.nstr(pred_even,10)}")
    print(f"    from ODD  sector  Σ a^odd_λ  Δ_λ         = {float(pred_odd):.2e}  "
          f"(→0 because Δ is bar-even)")
    print(f"  witness co_casimir_prediction (cross-check)= {mp.nstr(witness_pred,10)}  "
          f"(resid {float(abs(pred_full-witness_pred)):.1e})")
    print(f"  target −B_D/m_e                            = {mp.nstr(target,10)}")
    print()
    print("  FINDING: co-Casimir is BAR-EVEN → same sector as the (bar-even) binding")
    print("  target. Its refutation (wrong sign +0.145 vs −4.353, ~30×) is SCOPE-(a)")
    print("  NUMERICAL, NOT a sector exclusion. Corroborates probe_d_barparity_binding:")
    print("  bar-symmetric ansätze are in-sector; they simply give the wrong number.")

    (wb.set_description(
         "Bar-parity SECTOR classification of the refuted Frobenius co-Casimir "
         "Δ_λ ansatz at the deuteron (H_6, 11 λ⊢6), from the committed "
         "rho-k-h3a-co-casimir witness. Finding: Delta_lambda_co_casimir is "
         "BAR-EVEN (Δ_λ=Δ_λ' on all conjugate pairs; the norm-type Casimir ∝ "
         "Σcontent², not the linear content sum which would be bar-odd). So it "
         "occupies the SAME bar-even sector as the binding target; its "
         "prediction couples only to a^even and the bar-odd sector contributes "
         "0. The co-Casimir refutation (wrong sign +0.145 vs −4.353) is "
         "therefore scope-(a) NUMERICAL, not a scope-(b) sector exclusion — "
         "corroborating probe_d_barparity_binding that bar-symmetric ansätze "
         "are not structurally excluded. Audit-only; characterises an "
         "already-refuted ansatz, proposes no closure (Δ_λ gate).")
       .set_audit_only(
           "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
       .add_parameter("compute_dps", DPS)
       .add_data("co_casimir_parity", parity)
       .add_data("delta_bar_even_max_dev", float(even_dev))
       .add_data("delta_bar_odd_max_dev", float(odd_dev))
       .add_data("a_even_l2_norm", mp.nstr(_l2(a_even.values()), 20))
       .add_data("a_odd_l2_norm", mp.nstr(_l2(a_odd.values()), 20))
       .add_data("prediction_full", mp.nstr(pred_full, 20))
       .add_data("prediction_from_even_sector", mp.nstr(pred_even, 20))
       .add_data("prediction_from_odd_sector", mp.nstr(pred_odd, 6))
       .add_data("target_signed", mp.nstr(target, 20)))
    wb.add_assertion(
        "co_casimir_delta_is_bar_even",
        computed=even_dev, expected=0.0, tolerance=1e-30,
        source="Delta_lambda_co_casimir[λ] = Delta_lambda_co_casimir[λ'] on all "
               "conjugate pairs ⇒ bar-EVEN (norm-type Casimir ∝ Σcontent²)")
    wb.add_assertion(
        "prediction_couples_only_even_sector",
        computed=abs(pred_odd), expected=0.0, tolerance=1e-30,
        source="a bar-even Δ_λ couples only to a^even; the bar-odd sector "
               "contributes 0 to Σ a_λ Δ_λ")
    wb.add_assertion(
        "prediction_matches_witness",
        computed=abs(pred_full - witness_pred), expected=0.0,
        tolerance=1e-9,
        source="reconstructed Σ a_λ Δ_λ reproduces the committed "
               "co_casimir_prediction")
    wb.save()
    print("\nwitness → probe-d-cocasimir-barparity.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
