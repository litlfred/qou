#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical-only audit.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Item (a) — non-trivial Δ_I knot operator at A=2 (deuteron) audit.

Per the audit `2026-05-05-categorical-chain-gamma-to-six-term.md §5`:

  Step 5 — deuteron A=2 (Z=1, N=1)
  23-crossing braid in B_6: 11 internal crossings each for proton
  and neutron, plus 1 inter-nucleon averaged crossing (mixed pn
  pairing) on σ_2.
  Deuteron tr_M closed form at q_0: 0.3882864240747888…
  vs canonical bridge 0.3882864240747888 — 3 × 10⁻¹⁶ (machine precision).

So the **true atomic Markov trace** for the deuteron is

  |tr_M(β_D)| = 0.388286424048    at q_0

But Strategy-3's `t1_atomic_with_coupling` uses the
**disjoint-product** formula

  |tr_M_atomic(K)| = |tr_M(p)|^Z · |tr_M(n)|^N · |a(Z,N)| · Δ_n²-scalar

with the Δ_I knot operator a(Z,N) currently a FALLBACK = 1 for A=2
(per `jones_quotient_factor_fallback`):

  if A <= 2: return mp.mpf(1)

This fallback is WRONG: the genuine Δ_I at A=2 is the ratio between
the actual atomic Markov trace and the disjoint-product:

  Δ_I(D) := |tr_M(β_D)| / (|tr_M(p)| · |tr_M(n)|)
          = 0.3883 / (1.6332 · 1.2483)
          = 0.3883 / 2.0386
          = 0.1904

(NOT 1.0).

This script:
  1. Computes Δ_I(D) = 0.1904 from the closed-form atomic trace
  2. Tests what Strategy-3's deuteron prediction looks like with
     the corrected Δ_I
  3. Documents the structural finding: the fallback Δ_I = 1 was
     hiding the true coupling, but the corrected value gives a
     WORSE absolute prediction (1421 → 1091 MeV vs CODATA 1876).
     This means the rest of the formula is structurally tuned to
     the disjoint-product convention — fixing Δ_I in isolation
     doesn't help; the whole T1+T2+T3+T4 needs co-adjustment.

The right structural framing is term7-alpha5's iterative LP-dual:
each term is a shadow-price difference, not a multiplicative
coupling on a disjoint-product baseline.

Output: deuteron-delta-i-audit.witness.json
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder
from q_parameter import Q_MP


# Closed-form atomic Markov trace at q_0 — CACHED VALUES (audit, comparison only).
#
# ⚠️ DRIFT-RISK NOTE (CAL-4 audit, 2026-05-22): these are cached
# from the categorical chain audit
# `docs/audits/2026-05-05-categorical-chain-gamma-to-six-term.md §5`
# and predate the standardised `atomic-tr-m-mpfr-50dps.witness.json`
# canonical bridge.  The normalisation here (|tr_M(β_p)| in the
# H_{3A=3} disjoint-product setup, |tr_M(p)| ≈ 1.633) differs from
# the canonical witness's H_3 signed `tr_M_at_q0_50dps` (≈ 1.065)
# by a basis factor — the two numbers describe related but distinct
# quantities.
#
# TODO: reconcile the two normalisations and either (a) replace
# these with a runtime load from the canonical witness, or
# (b) document the basis-factor relationship explicitly in the
# witness emission.  Until then, treat these as audit-only
# cached constants — NOT a substrate derivation in this script.
TR_M_PROTON_AT_Q0   = mp.mpf("1.6331535640480814257473330892701240938276544598183")
TR_M_NEUTRON_AT_Q0  = mp.mpf("1.2482482717548397202242497985371807788067261625718")
TR_M_DEUTERON_AT_Q0 = mp.mpf("0.3882864240747888")  # from categorical chain audit


def main() -> int:
    print("=" * 100)
    print("ITEM (a) — Δ_I knot operator audit at A=2 (deuteron)")
    print("=" * 100)

    print(f"\n  Closed-form atomic Markov traces at q_0 (50 dps):")
    print(f"    |tr_M(β_p)|  = {mp.nstr(TR_M_PROTON_AT_Q0, 16)}")
    print(f"    |tr_M(β_n)|  = {mp.nstr(TR_M_NEUTRON_AT_Q0, 16)}")
    print(f"    |tr_M(β_D)|  = {mp.nstr(TR_M_DEUTERON_AT_Q0, 16)}")

    disjoint_product = TR_M_PROTON_AT_Q0 * TR_M_NEUTRON_AT_Q0
    delta_I_true = TR_M_DEUTERON_AT_Q0 / disjoint_product

    print(f"\n  Disjoint product |tr_M(p)|·|tr_M(n)|  = {mp.nstr(disjoint_product, 14)}")
    print(f"  TRUE Δ_I(D) = |tr_M(β_D)| / disjoint = {mp.nstr(delta_I_true, 14)}")
    print()
    print(f"  vs Strategy-3 fallback Δ_I(D) = 1.0  (jones_quotient_factor_fallback)")
    print(f"  ⇒ The fallback is wrong by a factor of {float(1.0/delta_I_true):.3f}")

    # ── Impact on Strategy-3 deuteron prediction ──
    print()
    print("─" * 100)
    print("  Impact on Strategy-3 M_pred[D] if Δ_I = 0.1904 replaces fallback 1.0")
    print("─" * 100)

    # Load legacy Strategy-3 components for the Class-C diagnostic.
    # P4‴ note: this script back-fits E_0 via the proton anchor only
    # to expose the Δ_I anomaly at A=2 (see banner below); it relies
    # on legacy-only fields `term1_atomic_total`, `term2_markov_z2`,
    # `term3_markov_z4`, `term4_frobenius_codim`,
    # `term6_cyclotomic_tail_MeV`, and `total_hecke` (used at
    # line 121 to back-fit E_0 = (M_p_codata − p_t6) / p_total).
    # None of these are in the canonical ρ_K witness; canonical mass
    # predictions live in `atomic-mass-via-rho-k.witness.json`.
    # This script remains a legacy-witness consumer by design.
    here = Path(__file__).parent
    s3_path = here / "atomic-braid-mass-table.witness.json"
    s3 = json.loads(s3_path.read_text())
    rows = {r["atom"]: r for r in s3["data"]["rows"]}

    p_t1 = mp.mpf(rows["p"]["term1_atomic_total"])
    p_t6 = mp.mpf(rows["p"]["term6_cyclotomic_tail_MeV"])
    p_total = mp.mpf(rows["p"]["total_hecke"])
    M_p_codata = mp.mpf("938.27208816")
    # Audit-only consumer of the deprecated Conv-C "proton back-fit"
    # E_0 pattern (≈ 200 MeV; flagged as DISCIPLINE VIOLATION in
    # derivation_chain.E_0_CONVENTIONS["C_proton_back_fit"]). This
    # script is a Class-C diagnostic probe per
    # docs/audits/2026-05-11-three-calibration-discipline-violations.md
    # — it back-fits E_0 only to expose the Δ_I anomaly at A=2, NOT
    # to predict any new quantity. New production chains MUST use
    # Conv A or Conv B instead. See also
    # docs/audits/2026-05-12-canonical-derivation-compute-review.md §3.
    E_0 = (M_p_codata - p_t6) / p_total

    d = rows["D"]
    M_d_codata = mp.mpf(d["M_codata_MeV"])
    t2_d = mp.mpf(d["term2_markov_z2"])
    t3_d = mp.mpf(d["term3_markov_z4"])
    t4_d = mp.mpf(d["term4_frobenius_codim"])
    t6_d = mp.mpf(d["term6_cyclotomic_tail_MeV"])

    # Strategy-3 t1 with fallback Δ_I = 1
    t1_d_fallback = TR_M_PROTON_AT_Q0 * TR_M_NEUTRON_AT_Q0 * mp.mpf(1) * mp.mpf(1)
    total_d_fallback = t1_d_fallback + t2_d + t3_d + t4_d
    M_pred_d_fallback = E_0 * total_d_fallback + t6_d

    # Strategy-3 t1 with TRUE Δ_I = 0.1904 (from closed-form atomic trace)
    t1_d_true = TR_M_PROTON_AT_Q0 * TR_M_NEUTRON_AT_Q0 * delta_I_true * mp.mpf(1)
    total_d_true = t1_d_true + t2_d + t3_d + t4_d
    M_pred_d_true = E_0 * total_d_true + t6_d

    print(f"\n  E_0 = {float(E_0):.6f} MeV/cat-unit (proton-calibrated)")
    print(f"\n  Strategy-3 with fallback Δ_I = 1.0:")
    print(f"    t1[D]_fallback = |tr_M(p)|·|tr_M(n)|·1·1 = {float(t1_d_fallback):.6f}")
    print(f"    M_pred[D]_fallback = {float(M_pred_d_fallback):.4f} MeV")
    err_fallback = (float(M_pred_d_fallback) - float(M_d_codata)) / float(M_d_codata) * 100
    print(f"    err = {err_fallback:+.4f}% (vs CODATA M_D = {float(M_d_codata):.4f} MeV)")
    print()
    print(f"  Corrected with TRUE Δ_I = {float(delta_I_true):.6f}:")
    print(f"    t1[D]_true = |tr_M(β_D)| = {float(t1_d_true):.6f}")
    print(f"    M_pred[D]_true = {float(M_pred_d_true):.4f} MeV")
    err_true = (float(M_pred_d_true) - float(M_d_codata)) / float(M_d_codata) * 100
    print(f"    err = {err_true:+.4f}%")
    print()
    print(f"  Δ_I correction shifts M_pred[D] by {float(M_pred_d_true - M_pred_d_fallback):+.4f} MeV.")
    print(f"  The 'true' Δ_I makes the prediction WORSE, not better:")
    print(f"    fallback err = {err_fallback:+.2f}%")
    print(f"    true Δ_I err = {err_true:+.2f}%")

    # ── Structural interpretation ──
    print()
    print("─" * 100)
    print("  STRUCTURAL FINDING: fallback Δ_I = 1 was hiding TWO inconsistencies")
    print("─" * 100)
    print()
    print(f"  (1) The fallback hides the true atomic Markov trace |tr_M(β_D)| = 0.388.")
    print(f"      Strategy-3's t1[D] = 2.039 with fallback is the WRONG quantity.")
    print()
    print(f"  (2) But replacing fallback with true Δ_I makes M_pred[D] WORSE.")
    print(f"      Reason: Strategy-3's E_0 calibration assumes the disjoint-product")
    print(f"      convention. If Δ_I is true (0.19), then E_0 should be re-calibrated")
    print(f"      AND the rest of the formula (T2/T3/T4) should be re-derived under")
    print(f"      the convention that t1 = |tr_M(β_atom)| (true atomic trace).")
    print()
    print(f"  (3) The framework needs a CONVENTION CHOICE:")
    print(f"      Option A: keep disjoint-product (fallback Δ_I = 1), absorb binding")
    print(f"                into the OTHER terms (T2/T3/T4 difference contributions).")
    print(f"      Option B: use true atomic trace (Δ_I = 0.19), re-derive E_0 +")
    print(f"                T2..T4 under the new convention.")
    print(f"      Option C (term7-alpha5): replace the entire framework with the")
    print(f"                iterative LP-dual 𝔪 = Σ_l u^{{(l)*}}, where the convention")
    print(f"                is automatic (each shadow-price is well-defined).")
    print()
    print(f"  Option C is the right path. Items (a)/(b) cannot be cleanly fixed in")
    print(f"  isolation; they expose deeper structural choices.")

    # Witness emission
    w = WitnessBuilder("deuteron-delta-i-audit", engine="mpmath")
    w.set_description(
        "Item (a) audit: the genuine Δ_I knot operator at A=2 is "
        "|tr_M(β_D)|/|tr_M(p)|·|tr_M(n)| = 0.3883/2.0386 = 0.1904, NOT the "
        "fallback 1.0 used by Strategy-3 (jones_quotient_factor_fallback). "
        "Replacing the fallback with the true Δ_I makes Strategy-3's "
        "M_pred[D] WORSE (1091 vs 1421 MeV; CODATA 1876). The fallback "
        "was hiding a convention choice: disjoint-product (Δ_I=1) vs "
        "true-atomic-trace (Δ_I=0.19). Either choice requires re-deriving "
        "E_0 + T2..T4 consistently. The proper path is term7-alpha5's "
        "iterative LP-dual 𝔪 = Σ_l u^{(l)*}, where the convention is "
        "automatic via the LP duality theorem."
    )
    w.set_content_block("prop:mass-coefficient-shadow-price")
    w.add_parameter("q_0", str(Q_MP))
    w.add_data("tr_M_p_q0", str(TR_M_PROTON_AT_Q0))
    w.add_data("tr_M_n_q0", str(TR_M_NEUTRON_AT_Q0))
    w.add_data("tr_M_deuteron_q0", str(TR_M_DEUTERON_AT_Q0))
    w.add_data("disjoint_product", str(disjoint_product))
    w.add_data("delta_I_true_deuteron", str(delta_I_true))
    w.add_data("delta_I_fallback_strategy3", 1.0)
    w.add_data("M_pred_D_with_fallback_MeV", float(M_pred_d_fallback))
    w.add_data("M_pred_D_with_true_delta_I_MeV", float(M_pred_d_true))
    w.add_data("M_D_codata_MeV", float(M_d_codata))
    w.add_data("err_fallback_pct", err_fallback)
    w.add_data("err_true_pct", err_true)
    w.add_data("structural_finding", (
        "The fallback Δ_I = 1 was hiding TWO inconsistencies: "
        "(i) the true atomic Markov trace |tr_M(β_D)| = 0.388 is NOT being used, "
        "(ii) replacing fallback with true value makes M_pred[D] worse because "
        "Strategy-3's E_0 + T2..T4 calibration assumes the disjoint-product "
        "convention. The framework needs a convention choice: keep "
        "disjoint-product and absorb binding into other terms, OR use true "
        "atomic trace and re-derive everything. The proper path is "
        "term7-alpha5's iterative LP-dual where the convention is automatic."
    ))
    w.add_assertion(
        "delta_I_true_is_not_one",
        computed=float(abs(delta_I_true - 1.0)),
        expected=1.0,
        tolerance=0.5,    # allow Δ_I ∈ (0.5, 1.5); ours is 0.19, FAR from 1
    )
    w.add_assertion(
        "delta_I_correction_does_not_close_M_pred_D_gap",
        computed=bool(abs(err_true) > 5.0),
        expected=True,
    )
    # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554
    # wiring, 2026-05-31). Each nucleus's canonical T_w knot
    # operator uniqueness at the empty-constraint SDP level.
    w.add_data("lean_uniqueness_ref", {
        "deuteron": "qou:QOU.BraidKnot.deuteron_uniqueness_closed",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). The real per-nucleus SDP (multi-term cost + non-empty constraints) is per-nucleus substantive open work. Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
        ),
    })

    w.save()
    print(f"\n✓ Witness: deuteron-delta-i-audit.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
