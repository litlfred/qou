#!/usr/bin/env python3
"""NEGATIVE-RESULT probe: sweep candidate per-particle q-scalar
corrections that might close the −11.4% m_H/m_W deficit found in
`ew_higgs_mass_ratios_probe` (PR #513).

This is a hypothesis-fishing probe, not a derivation.  Run it to
quantify what kind of correction *would* be needed; then decide
whether any candidate is structural enough to keep, or whether the
underlying torus-link triplet conjecture (#513) should be retracted.

Headline result (interpret as falsification, not fit):
  - needed factor = 1.128 (3sf)
  - closest single-q candidate = q itself, residual still −1.6%
  - no candidate hits PDG within experimental error
  - sweeping ~18 candidates and picking the best is a
    multiple-comparisons fishing exercise; the apparent "f = q"
    match is not statistically meaningful with 3 EW masses
  - conclusion: conj:electroweak-higgs-torus-link-triplet is
    falsified as stated.  A per-particle correction is fitting,
    not derivation.  Do not treat any "best match" here as a
    prediction.

Refs:
  - PR #513 EW/Higgs probe finding
  - conj:electroweak-higgs-torus-link-triplet
  - prop:atom-knot-mass-derivation §"Mass identity"
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50  # module-level precision floor

Q_0 = mp.mpf('1.1099785955541805')
M_W = mp.mpf('80.379')
M_Z = mp.mpf('91.1876')
M_H = mp.mpf('125.25')


def tr_M_h2_torus(k: int, q: mp.mpf) -> mp.mpf:
    """tr_M(σ_1^{2k}) at H_2."""
    sqrt_q = mp.sqrt(q)
    z = 1 / (sqrt_q + 1 / sqrt_q)
    inv_q = 1 / q
    y_sym = (z + inv_q) / (q + inv_q)
    y_alt = 1 - y_sym
    return y_sym * q ** (2 * k) + y_alt * inv_q ** (2 * k)


def main():
    base = Path(__file__).parent
    q = Q_0

    sqrt_q = mp.sqrt(q)
    z = 1 / (sqrt_q + 1 / sqrt_q)
    h = q - 1 / q
    qint2 = q + 1 / q                  # [2]_q
    qint3 = q + 1 + 1 / q              # [3]_q (rough; the q-deformed (q²+q+1)/q)
    # Actually [n]_q proper: [n]_q = (q^n - q^{-n}) / (q - q^{-1})
    def q_int(n):
        return (q ** n - q ** (-n)) / (q - 1 / q)

    print("══════════════════════════════════════════════════════════════════════")
    print("  EW/Higgs scalar-correction probe (option (b) from PR #513)")
    print(f"  q_0 = {float(q)},  z = {float(z):.6f},  h = q-q^-1 = {float(h):.6f}")
    print("══════════════════════════════════════════════════════════════════════\n")

    tr_W = tr_M_h2_torus(2, q)
    tr_Z = tr_M_h2_torus(3, q)
    tr_H = tr_M_h2_torus(4, q)

    pred_baseline = tr_H / tr_W
    obs = M_H / M_W
    needed_factor = obs / pred_baseline   # = (1.558 / 1.381) = 1.128

    print(f"  baseline m_H/m_W = tr_M(σ_1^8)/tr_M(σ_1^4) = {float(pred_baseline):.6f}")
    print(f"  PDG  m_H/m_W                                = {float(obs):.6f}")
    print(f"  ⇒ Higgs needs a structural factor f with    f = {float(needed_factor):.6f}")
    print(f"     (corrected m_H/m_W = f · {float(pred_baseline):.6f} = PDG)\n")

    print("  ──── candidate scalar factors at q_0 ────")
    candidates = [
        ("z  (Markov parameter)",                 z),
        ("z²",                                    z * z),
        ("[2]_q                = q + 1/q",        qint2),
        ("[2]_q / 2",                             qint2 / 2),
        ("[3]_q                 = (q³-q⁻³)/(q-q⁻¹)", q_int(3)),
        ("[3]_q / 3",                             q_int(3) / 3),
        ("[4]_q / [3]_q",                         q_int(4) / q_int(3)),
        ("[4]_q / 4",                             q_int(4) / 4),
        ("(q^{1/2})·z",                           sqrt_q * z),
        ("(q²+1)/(q+1)·1/q",                      (q*q + 1) / (q + 1) / q),
        ("h + 1   = q - q^{-1} + 1",              h + 1),
        ("1 + (q-1)",                             q),
        ("1 + h/2",                               1 + h / 2),
        ("(q^{1/2} + q^{-1/2})/2 = 1/(2z)",       1 / (2 * z)),
        ("[5]_q · [3]_q / ([4]_q² )",
            q_int(5) * q_int(3) / (q_int(4) ** 2)),
        ("genus-3 fact: 1 + 2(q-1)",              1 + 2 * (q - 1)),
        ("genus-3 fact: 1 + g·h with g=3",        1 + 3 * h),
        ("scalar-vs-vector: q^{1/2}+q^{-1/2}",    sqrt_q + 1 / sqrt_q),
    ]

    print(f"  {'candidate':<40s} {'value':>12s} {'predicted m_H/m_W':>20s} {'err vs PDG':>12s}")
    best = (1e10, None)
    for label, f in candidates:
        pred = f * pred_baseline
        err = float((pred - obs) / obs * 100)
        marker = ""
        if abs(err) < abs(best[0]):
            best = (err, label)
        if abs(err) < 0.5:
            marker = " ← FIT"
        elif abs(err) < 2:
            marker = " ← close"
        print(f"  {label:<40s} {float(f):>12.6f} {float(pred):>20.6f} {err:>+11.3f}%{marker}")

    print(f"\n  Best match:  {best[1]} → err {best[0]:+.3f}%")

    # Now: does the same factor (or its absence) work for W and Z?
    # For W (vector, T(2,4)) — no factor, predicted = tr_W * 1
    # For Z (vector, T(2,6)) — no factor
    # If we apply the best factor to H but NOT to W/Z, m_Z/m_W stays unchanged.
    # Cross-check: if the best factor is f_H, the prediction is consistent ONLY
    # if W and Z don't need such a factor (i.e., m_Z/m_W stays at +2.7%).

    print("\n  ──── cross-checks ────")
    print(f"  m_Z/m_W baseline (no factor on Z): {float(tr_Z/tr_W):.6f}")
    print(f"  PDG m_Z/m_W                      : {float(M_Z/M_W):.6f}")
    print(f"  ⇒ Z does NOT need the Higgs factor (its baseline already +2.7% off PDG)")
    print(f"     the Higgs factor is a per-particle correction, not a global one")

    # Witness
    out_path = base / "ew-higgs-scalar-correction-probe.witness.json"
    witness = {
        "computation": "ew-higgs-scalar-correction-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "NEGATIVE result: hypothesis-fishing sweep of ~18 candidate "
            "q-scalar corrections that might close the −11.4% m_H/m_W "
            "deficit from PR #513.  No candidate hits PDG within "
            "experimental error; closest (f = q) leaves −1.6% residual. "
            "Multiple-comparisons sweep with 3 EW masses ⇒ any 'best "
            "match' is fitting, not derivation.  Treated as falsification "
            "evidence against conj:electroweak-higgs-torus-link-triplet "
            "as stated, not as a positive prediction."
        ),
        "result_classification": "negative",
        "interpretation": "falsification-of-PR-513-conjecture",
        "q_0": float(q),
        "needed_factor": float(needed_factor),
        "candidates": [
            {"label": label, "value": float(f),
             "predicted_m_H_over_m_W": float(f * pred_baseline),
             "err_pct": float((f * pred_baseline - obs) / obs * 100)}
            for label, f in candidates
        ],
        "best_match": {"label": best[1], "err_pct": best[0]},
        "notes": [
            "Needed factor is 1.128; no candidate matches within PDG error.",
            "Closest match (f = q) leaves −1.6% residual — not a clean hit.",
            "Sweeping 18 candidates against 3 data points (W, Z, H) is a "
            "multiple-comparisons fishing exercise; do not interpret "
            "'best_match' as a structural prediction.",
            "m_Z/m_W baseline is already +2.7% off PDG; even a perfect "
            "Higgs correction would not rescue the W/Z ratio.",
            "Recommendation: retract conj:electroweak-higgs-torus-link-triplet "
            "as currently stated.  Any future scalar/vector distinction must "
            "be derived from the Markov-trace structure on H_2 (different "
            "y_λ split per spin), not fit from a candidate basket.",
        ],
    }
    with open(out_path, "w") as f_out:
        json.dump(witness, f_out, indent=2)
    print(f"\n→ wrote {out_path}")


if __name__ == "__main__":
    main()
