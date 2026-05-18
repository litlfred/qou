"""Cross-anchor Δ_coupling test — FALSIFIES the pp-nn correlation hypothesis.

Per user direction (1ppb workplan v1 §"Phase 1' cross-anchor verification"):
test the refined closed-form

  Δ_coupling(Z, N) = (A - 2) · E_0 · log(1/h)
                   + 2 · (Z-1)_+ · (N-1)_+ · z² · E_0 · h²

at the single-magic anchors (2,1) ³He = D+p and (1,2) T = D+n where the
hypothesis predicts the correlation term = 0 (since (Z-1)(N-1) = 0).

## Method

(a) Read Δ_cat per atom from `magic-shell-empirical-instantiation.witness.json`
    (on main — proton, neutron, deuteron, tritium, ³He, ⁴He).
(b) Compositional extraction of Δ_coupling at each anchor:
      Δ_coupling(2,2) = Δ_cat(⁴He) − 2·Δ_cat(³He)
      Δ_coupling(2,1) = Δ_cat(³He) − Δ_cat(D) − Δ_cat(p)
      Δ_coupling(1,2) = Δ_cat(T)  − Δ_cat(D) − Δ_cat(n)
(c) Predict from refined formula; compare; report gap.

## Result (substantive — falsifies the hypothesis)

  anchor       predicted    extracted    gap%
  (2,2) DM     13.1945      13.1969      -0.018%   ★ (correlation hypothesis holds)
  (2,1) SM      6.5516       6.0252      +8.737%   ⚠ FALSIFIED
  (1,2) SM      6.5516       6.8211      -3.950%   ⚠ FALSIFIED

At doubly-magic (2,2) the refined form holds to <0.02%. At single-magic
the hypothesis is empirically refuted — the leading form alone misses
by 4-9% in OPPOSITE directions, with a Z↔N asymmetry of +0.796 MeV
(extracted(1,2) − extracted(2,1)) that the symmetric (A-2) factor
cannot capture.

## Decomposition implied by the 3-anchor system

Forcing the data to fit
  Δ_coupling = leading + pp·(Z-1) + nn·(N-1) + corr·(Z-1)(N-1)
gives:
  pp_term  ≈ -0.527 MeV   (single-magic σ_pp channel)
  nn_term  ≈ +0.269 MeV   (single-magic σ_nn channel)
  corr     ≈ +6.903 MeV   (doubly-magic σ_pp·σ_nn correlation)
  leading  = 6.5516 MeV   (categorical baseline at A=3)

The Z↔N asymmetry (pp_term ≠ nn_term) reflects the proton-neutron
mass asymmetry baked into the Hecke operator weights. The dominant
"correlation" contribution at doubly-magic is ~70× larger than my
original z²·E_0·h² hypothesis (~0.091 MeV), so the apparent (2,2)
match was a coincidence — the refined formula was wrong in its
decomposition even though the (2,2) value was right.

## What this tells us

- The substrate-derivation chain for Δ_coupling needs additional
  ingredients beyond the (A-2)·E_0·log(1/h) leading form and the
  pp-nn correlation 2·z²·E_0·h².
- Specifically, single-magic anchors require Z↔N-asymmetric
  contributions tied to the proton-vs-neutron operator differences.
- The doubly-magic correlation is much larger than 2·z²·E_0·h² and
  needs a different substrate primitive.

Promotion of `conj:delta-coupling-substrate-form` to a proposition
is BLOCKED by this finding. The conjecture needs to be reformulated
to include the Z↔N-asymmetric terms.

## Output

`delta-coupling-cross-anchor-falsification.witness.json`

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 90)
    print("  Cross-anchor Δ_coupling test — falsifies pp-nn correlation hypothesis")
    print("=" * 90)
    print()

    # Load Δ_cat from main's witness
    d = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    data = d.get('data', d)
    delta_cat: dict[str, mp.mpf] = {}
    for k, v in data['per_atom_delta_cat'].items():
        val_str = v.get('delta_cat_MeV_50dps', v.get('delta_cat_MeV', '0'))
        delta_cat[k] = mp.mpf(val_str)

    print("  Δ_cat per atom (from magic-shell-empirical-instantiation.witness.json):")
    for k, v in delta_cat.items():
        print(f"    Δ_cat({k:>8}) = {float(v):>+9.4f} MeV")
    print()

    # Compositional extractions
    extracted = {
        (2, 2): delta_cat['he4'] - 2 * delta_cat['he3'],
        (2, 1): delta_cat['he3'] - delta_cat['deuteron'] - delta_cat['proton'],
        (1, 2): delta_cat['tritium'] - delta_cat['deuteron'] - delta_cat['neutron'],
    }

    # Substrate constants
    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf("0.51099895069")
    E_0 = m_e / (q0 * (q0 - 1))
    h = q0 - 1 / q0
    z = 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    # Refined formula prediction
    def predict(Z: int, N: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        A = Z + N
        leading = (A - 2) * E_0 * mp.log(1 / h)
        corr = 2 * max(Z - 1, 0) * max(N - 1, 0) * z**2 * E_0 * h**2
        return leading, corr, leading + corr

    print(f"  {'anchor':>14} {'leading':>10} {'corr':>10} {'predicted':>12} {'extracted':>12} {'gap%':>9}")
    print("  " + "-" * 75)
    results = []
    for (Z, N) in [(2, 2), (2, 1), (1, 2)]:
        leading, corr, predicted = predict(Z, N)
        ext = extracted[(Z, N)]
        gap_pct = float((predicted - ext) / ext * 100) if ext != 0 else float('inf')
        within_threshold = abs(gap_pct) < 1.0
        flag = " ★ <1%" if within_threshold else " ⚠ FALSIFIED"
        typ = "doubly" if Z >= 2 and N >= 2 else "single"
        print(f"  ({Z},{N}) {typ:>6} {float(leading):>10.4f} {float(corr):>10.4f} "
              f"{float(predicted):>12.4f} {float(ext):>12.4f} {gap_pct:>+8.3f}%{flag}")
        results.append({
            "Z": Z, "N": N, "A": Z + N,
            "anchor_type": typ,
            "leading_MeV": float(leading),
            "correlation_MeV": float(corr),
            "predicted_MeV": float(predicted),
            "extracted_MeV": float(ext),
            "gap_pct": gap_pct,
            "within_1_pct": within_threshold,
        })
    print()

    # Hypothesis verdict
    refuted = any(not r["within_1_pct"] for r in results if r["anchor_type"] == "single")
    print("  HYPOTHESIS VERDICT:")
    if refuted:
        print("    REFUTED at single-magic anchors. Specifically:")
        for r in results:
            if r["anchor_type"] == "single" and not r["within_1_pct"]:
                print(f"      ({r['Z']},{r['N']}) gap = {r['gap_pct']:+.2f}% (above 1% threshold)")
    else:
        print("    Confirmed across all 3 anchors.")
    print()

    # Z↔N asymmetry
    ext_21 = extracted[(2, 1)]
    ext_12 = extracted[(1, 2)]
    z_n_asymmetry = ext_12 - ext_21
    print(f"  Z↔N asymmetry at single-magic anchors:")
    print(f"    extracted(1,2) - extracted(2,1) = {float(z_n_asymmetry):+.4f} MeV")
    print(f"    The symmetric (A-2)·E_0·log(1/h) leading form predicts ZERO asymmetry.")
    print(f"    The empirical asymmetry suggests a Z↔N-asymmetric contribution from")
    print(f"    the proton-vs-neutron Hecke operator weights — NOT captured by my")
    print(f"    refined formula. The (2,2) doubly-magic match was a coincidence.")
    print()

    # Decomposition (force-fit pp_term, nn_term, corr from 3 anchors)
    # extracted = leading + pp·(Z-1) + nn·(N-1) + corr·(Z-1)(N-1)
    # System:
    #   (2,1): 6.0252 = 6.5516 + pp  →  pp = -0.5264
    #   (1,2): 6.8211 = 6.5516 + nn  →  nn = +0.2695
    #   (2,2): 13.1969 = 6.5516 · 2 + pp + nn + corr  →  corr = ...
    leading_22, _, _ = predict(2, 2)
    leading_21 = predict(2, 1)[0]
    leading_12 = predict(1, 2)[0]
    pp_term = ext_21 - leading_21
    nn_term = ext_12 - leading_12
    corr_term = extracted[(2, 2)] - leading_22 - pp_term - nn_term
    print("  Decomposition implied by the 3-anchor system:")
    print(f"    pp_term  ≈ {float(pp_term):+.4f} MeV  (single-magic σ_pp channel)")
    print(f"    nn_term  ≈ {float(nn_term):+.4f} MeV  (single-magic σ_nn channel)")
    print(f"    corr     ≈ {float(corr_term):+.4f} MeV  (doubly-magic σ_pp·σ_nn correlation)")
    print(f"    leading  = {float(leading_21):.4f} MeV  (categorical baseline at A=3)")
    print()
    print(f"    [Note: corr ≈ 6.9 MeV vs my hypothesised 2·z²·E_0·h² ≈ 0.091 MeV.")
    print(f"     The refined formula's apparent (2,2) match was COINCIDENCE.]")
    print()

    builder = (
        WitnessBuilder("delta-coupling-cross-anchor-falsification", engine="mpmath")
        .set_description(
            "Cross-anchor Δ_coupling test using Δ_cat data from "
            "magic-shell-empirical-instantiation.witness.json on main. "
            "REFUTES the pp-nn correlation hypothesis shipped earlier "
            "on PR #671 (probe_delta_coupling_pp_nn_correlation): single-"
            "magic anchors (2,1) and (1,2) miss the leading-form "
            "prediction by 4-9% in OPPOSITE directions, with a Z↔N "
            "asymmetry that the symmetric (A-2) factor cannot capture. "
            "The doubly-magic (2,2) match was coincidence; the actual "
            "decomposition involves single-magic asymmetric pp/nn terms "
            "plus a much larger correlation term (~70× larger than "
            "hypothesised). conj:delta-coupling-substrate-form needs "
            "reformulation."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-delta-coupling-substrate-derivation.md"
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_data("delta_cat_inputs_MeV", {k: float(v) for k, v in delta_cat.items()})
        .add_data("results", results)
        .add_data("z_n_asymmetry_MeV", float(z_n_asymmetry))
        .add_data("forced_decomposition", {
            "pp_term_MeV": float(pp_term),
            "nn_term_MeV": float(nn_term),
            "correlation_MeV": float(corr_term),
            "leading_at_A_3_MeV": float(leading_21),
        })
        .add_assertion(
            name="single_magic_anchors_falsify_refined_formula",
            computed=refuted,
            expected=True,
            unit="boolean",
            source=(
                "Single-magic gaps: (2,1)=+8.74%, (1,2)=-3.95%, both above "
                "1% threshold. The refined pp-nn correlation formula "
                "(probe_delta_coupling_pp_nn_correlation) is empirically "
                "wrong at single-magic anchors."
            ),
        )
        .add_caveat(
            "This probe REFUTES a hypothesis shipped earlier on the same "
            "PR (#671). The doubly-magic (2,2) 0.04% match in the prior "
            "probe was coincidence; the structural decomposition is "
            "richer than the symmetric (A-2) form. The conj:delta-coupling-"
            "substrate-form content block remains a conjecture (was never "
            "promoted to proposition) — this finding now constrains its "
            "next iteration. Honest empirical signal preserved."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
