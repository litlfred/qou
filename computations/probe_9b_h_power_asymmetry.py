#!/usr/bin/env python3
"""PROBE 1-b (step-9b follow-up) — h-power re-parametrization of the
10A−5 residual law + derived p/n-asymmetry factor for the ³He outlier.

EXPLORATORY PROBE — derive-or-refute; NOT wired to production; introduces
NO new constants (every exponent below is read off the Phase-5q closed
form's own structural quantities; nothing is fitted).

Context. PROBE 1 (probe_9b_laurent_degree_10a5.py, audit
docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md) surfaced two
observation-tier facts about the trace-canonical residual
Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5):

  (O1)  h(q₀) = q₀^(−15.0002)  — so the per-chain-unit "5" of the resolved
        counting law 10A−5 = 5(2A−1) equals −(1/3)·log_{q₀} h to 1.4e-5,
        and the whole law re-parametrizes as
            Δ_λ(K) ≈ h(q₀)^(−(2A−1)/3).
        (NOT h^(−(2A−1)): the correct h-exponent carries the 1/3.)
  (O2)  the ³He −1.40 outlier is dominated by the p/n trace asymmetry
        log_{q₀}(tr_n/tr_p) = −1.3718, with the interface-sign swap
        (−0.938) and the AME mirror (+0.904) nearly cancelling.

MODELS TESTED (owner request 2026-07-03: "est Δ_λ(K) ≈
h(q₀)^(−(2A−1))·(p/n-asymmetry factor) against T/³He/⁴He"):

  M0  law:      log_{q₀}Δ_λ = 10A−5                       (baseline)
  M1  h-form:   log_{q₀}Δ_λ = −log_{q₀}h · (2A−1)/3       (exact re-param)
  M2  antisym:  M1 + log_{q₀}(tr_n/tr_p)·(Z−N)
  M3  p-excess: M1 + log_{q₀}(tr_n/tr_p)·[Z>N]

All inputs are read from the committed PROBE 1 witness
(probe-9b-laurent-degree-10a5.witness.json): measured log_{q₀}Δ_λ per
atom and the exponent dictionary. κ = log_{q₀}(tr_n/tr_p) is a DERIVED
quantity of the closed form (Phase 5l per-nucleon traces), not a fit.

RESULT (see witness): M3 collapses the ³He residual +1.40 → +0.033 while
leaving D (+0.011) and T (+0.066) intact; ⁴He (−0.272) is unchanged (Z=N,
no asymmetry available) and remains the largest residual. M2 is REFUTED
scope-(a): the antisymmetric (Z−N) factor breaks T (+1.44). M3 is
NEAR-MATCH tier, unwired: the [Z>N] gate is an observation (consistent
with O2's swap/mirror near-cancellation on the mirror pair), not a
derived rule — deriving or refuting the gate from the interface algebra
is the follow-up.

Run:  python3 -u computations/probe_9b_h_power_asymmetry.py
Witness: probe-9b-h-power-asymmetry.witness.json (audit-only)

Ref: docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md
Ref: docs/audits/2026-06-29-delta-lambda-residual-synthesis.md
Ref: docs/audits/2026-06-09-delta-lambda-canonical-residual.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

from qou_substrate import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
PROBE1_WITNESS = HERE / "probe-9b-laurent-degree-10a5.witness.json"

# Residual bounds asserted below (q0-units). M3's worst atom is 4He at
# -0.272 (inherited from the baseline law; Z=N so the asymmetry factor
# cannot act); every asymmetry-bearing atom must sit under 0.07.
M3_BOUND_ASYM_ATOMS = 0.07
M3_BOUND_ALL = 0.35


def main() -> int:
    src = json.loads(PROBE1_WITNESS.read_text())
    d = src["data"]
    ed = d["exponent_dictionary_q0_units"]
    H = -ed["log_q0_h"]                      # 15.000206  (−log_q₀ h)
    kappa = ed["log_q0_tr_n_over_tr_p"]      # −1.371810  (derived, not fitted)

    w = WitnessBuilder("probe-9b-h-power-asymmetry", engine="python-stdlib")
    w.set_audit_only(
        "docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md")
    w.add_parameter("minus_log_q0_h", H)
    w.add_parameter("kappa_log_q0_trn_over_trp", kappa)
    w.add_parameter("source_witness", PROBE1_WITNESS.name)

    rows = []
    for r in d["isotope_rows"]:
        A, Z, N = r["A"], r["Z"], r["N"]
        m = r["log_q0_Delta_lambda"]
        models = {
            "M0_law_10A_minus_5": 10 * A - 5,
            "M1_h_form": H * (2 * A - 1) / 3,
            "M2_antisym_ZminusN": H * (2 * A - 1) / 3 + kappa * (Z - N),
            "M3_proton_excess_gate": H * (2 * A - 1) / 3
            + (kappa if Z > N else 0.0),
        }
        rows.append({
            "atom": r["atom"], "A": A, "Z": Z, "N": N,
            "measured_log_q0_Delta_lambda": m,
            "residuals_model_minus_measured":
                {k: v - m for k, v in models.items()},
        })
        print(f"{r['atom']:5} A={A} Z-N={Z-N:+d}  measured {m:9.4f}  " +
              "  ".join(f"{k.split('_')[0]} {v - m:+7.4f}"
                        for k, v in models.items()))
    w.add_data("isotope_rows", rows)

    res3 = {r["atom"]: r["residuals_model_minus_measured"] for r in rows}
    w.add_assertion(
        name="m3_collapses_3He_outlier",
        computed=abs(res3["3He"]["M3_proton_excess_gate"]),
        expected=0.0, tolerance=M3_BOUND_ASYM_ATOMS,
        source="³He residual under M3 (was +1.40 under the bare law); "
               "κ is the derived closed-form trace asymmetry, not a fit",
    )
    w.add_assertion(
        name="m3_all_atoms_within_bound",
        computed=max(abs(v["M3_proton_excess_gate"]) for v in res3.values()),
        expected=0.0, tolerance=M3_BOUND_ALL,
        source="max |residual| over D/T/³He/⁴He under M3 (⁴He −0.272 "
               "dominates; Z=N so the gate cannot act there)",
    )
    w.add_assertion(
        name="m2_antisym_refuted_on_T",
        computed=abs(res3["T"]["M2_antisym_ZminusN"]),
        expected=1.44, tolerance=0.02,
        source="scope-(a): the antisymmetric (Z−N) factor breaks the "
               "T residual to ≈+1.44 — mirror-symmetric application of "
               "the asymmetry is refuted; only the proton-excess side "
               "carries it (consistent with the PROBE 1 swap/mirror "
               "near-cancellation)",
    )
    w.add_data("verdict", {
        "tier": "near-match (unwired)",
        "M1": "exact re-parametrization of the resolved 5(2A−1) law via "
              "h(q₀)=q₀^(−15.0002); the h-exponent is −(2A−1)/3, NOT "
              "−(2A−1)",
        "M2": "REFUTED scope-(a) — breaks T",
        "M3": "NEAR-MATCH — residuals D +0.011 / T +0.066 / ³He +0.033 / "
              "⁴He −0.272; open: derive-or-refute the [Z>N] gate from the "
              "interface algebra; ⁴He residual untouched (Z=N)",
    })
    w.set_description(
        "h-power re-parametrization of the 10A−5 residual law plus the "
        "derived p/n trace-asymmetry factor, tested on D/T/³He/⁴He from "
        "the committed PROBE 1 witness; no new constants.")
    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
