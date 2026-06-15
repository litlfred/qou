#!/usr/bin/env python3
"""delta_lambda_exponent_from_crossings.py
==========================================

Derive-or-refute: where does the Δ_λ q₀-exponent **10A−5 = 5(2A−1)** come from?
(`docs/audits/2026-06-09-delta-lambda-canonical-residual.md` named this the
admissible non-fit next step: "categorical derivation of 10A−5 from
crossing/jet bookkeeping of W_free vs W_atom".)

## Result: the slope "10" IS the non-averaged crossing count per nucleon

Classifying the canonical atom braid `atom_braid_word_3A(Z,N)` by Hecke
crossing type (d = 0 → σ; d = −h/2 → color-averaged p-n interface; d = −h →
σ⁻¹), the counts are exactly linear in A:

    n_crossings        = 12A − 1
    averaged (p-n)     = 2A + 1          ← the bar-symmetric (σ+σ⁻¹)/2 interfaces
    σ + σ⁻¹ (non-avg)  = 10A − 2          ← exactly 10 per nucleon

The color-averaged interfaces carry **d = −h/2 = (σ + σ⁻¹)/2**, which is
**bar-symmetric (q ↔ q⁻¹ invariant)** and therefore contributes **zero net
q-power**. So only the non-averaged σ / σ⁻¹ crossings enter the q₀-exponent,
and their count is `10A − 2`. The observed Δ_λ exponent is

    10A − 5 = (σ + σ⁻¹) − 3,            for A ≥ 2,

i.e. the **slope 10 of the exponent = the number of non-averaged crossings
each nucleon contributes to the bound braid** — derived from the crossing
bookkeeping, not fitted. (Verified for D, T, ³He, ⁴He; T and ³He share
σ+σ⁻¹ = 28 ⇒ the SAME leading exponent 25, as the q₀^(10A−5) law requires.)

## What is NOT yet derived (honest)

  * **The constant −3** (boundary offset): `10A−5 = (σ+σ⁻¹) − 3`. A single
    constant; plausibly the 3 strands of the seed nucleon (H₃ base), but not
    derived here.
  * **Why exactly 10 non-averaged crossings per nucleon** (6σ + 3σ⁻¹ = 9 for a
    free nucleon → +1 per nucleon from binding): the per-nucleon "10" is read
    off the construction, not yet derived from the 𝓑₃ / Bring structure.
  * **The Z-dependent correction** (the ³He −1.40 deviation): it is NOT the
    writhe — ³He and ⁴He share writhe = σ−σ⁻¹ = 8 but deviate −1.40 vs +0.27.
    It tracks PROTON excess (Z−N): D=0, T=−1, ³He=+1(outlier), ⁴He=0. Open.

This sharpens the keystone from "derive 10A−5" to "derive the −3 offset, the
per-nucleon 10, and the proton-excess correction" — the slope is done.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import time
from collections import Counter

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 30


def classify(Z, N):
    from mass_at_3A_proper import atom_braid_word_3A
    w = atom_braid_word_3A(Z, N)
    c = Counter()
    for (_, d, _) in w:
        d = round(float(d), 4)
        if abs(d) < 1e-9:
            c["sig"] += 1
        elif abs(d + 0.1045) < 1e-3:
            c["avg"] += 1     # -h/2 color-averaged p-n interface (bar-symmetric)
        elif abs(d + 0.2091) < 1e-3:
            c["inv"] += 1     # -h sigma_inv
        else:
            c["other"] += 1
    return c, len(w)


def main() -> int:
    t0 = time.monotonic()
    # observed q0-exponent deviations from delta-lambda-canonical-residual audit
    dev = {"D": -0.011, "T": -0.066, "3He": -1.404, "4He": 0.272}
    znd = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

    rows = []
    ok_slope = True
    for name in ("D", "T", "3He", "4He"):
        Z, N = znd[name]
        A = Z + N
        c, tot = classify(Z, N)
        sig, avg, inv = c["sig"], c["avg"], c["inv"]
        nonavg = sig + inv
        writhe = sig - inv
        match = (nonavg == 10 * A - 2) and (nonavg - 3 == 10 * A - 5) and (tot == 12 * A - 1) and (avg == 2 * A + 1)
        ok_slope = ok_slope and match
        rows.append({"atom": name, "Z": Z, "N": N, "A": A, "n_cross": tot,
                     "sigma": sig, "averaged": avg, "sigma_inv": inv,
                     "non_averaged": nonavg, "writhe": writhe,
                     "exponent_pred_10A_5": 10 * A - 5,
                     "nonavg_minus_3": nonavg - 3,
                     "q0_exp_dev_observed": dev[name],
                     "Z_minus_N": Z - N})
        print(f"  {name:>4} A={A}: σ={sig} avg={avg} σ⁻¹={inv} | non-avg={nonavg} (10A-2={10*A-2}) "
              f"| (non-avg)-3={nonavg-3} vs 10A-5={10*A-5} | writhe={writhe} dev={dev[name]:+.3f}  {'OK' if match else 'X'}")

    builder = WitnessBuilder("delta-lambda-exponent-from-crossings",
                             engine="python+combinatorial", start_time=t0)
    (builder
     .set_description(
        "Crossing-bookkeeping derivation of the Δ_λ q₀-exponent slope. The "
        "non-averaged crossings σ+σ⁻¹ of atom_braid_word_3A = 10A-2 (exactly 10 "
        "per nucleon); the color-averaged p-n interfaces (d=-h/2=(σ+σ⁻¹)/2, "
        "count 2A+1) are bar-symmetric ⇒ 0 net q-power. So 10A-5 = (σ+σ⁻¹)-3, "
        "i.e. the exponent SLOPE 10 = non-averaged crossings per nucleon "
        "(derived, not fit). Open: the -3 offset, the per-nucleon 10 from 𝓑₃, "
        "and the proton-excess Z-correction (³He -1.40; NOT writhe — ³He/⁴He "
        "share writhe 8). Sharpens docs/audits/2026-06-09-delta-lambda-"
        "canonical-residual.md.")
     .add_data("rows", rows)
     .add_data("identities", {"n_cross": "12A-1", "averaged": "2A+1",
                              "non_averaged_sigma_plus_inv": "10A-2",
                              "exponent": "10A-5 = (σ+σ⁻¹) - 3  [A≥2]"})
     .add_data("open", {"offset_minus_3": "boundary constant (H₃ seed?), not derived",
                        "per_nucleon_10": "from 𝓑₃/Bring structure, not derived",
                        "Z_correction": "proton-excess (³He); NOT writhe; open"})
     .add_data("discipline", "combinatorial crossing count; derive-or-refute; "
                             "slope derived, offset+Z-correction open; NOT wired"))
    builder.add_assertion("nonavg_crossings_eq_10A_minus_2_all_atoms",
                          computed=bool(ok_slope), expected=True,
                          source="σ+σ⁻¹ = 10A-2 and (σ+σ⁻¹)-3 = 10A-5 for D,T,³He,⁴He")
    # T and ³He share the leading exponent (same non-averaged count) — the q-law constraint
    cT, _ = classify(1, 2)
    cHe3, _ = classify(2, 1)
    builder.add_assertion("T_and_3He_share_nonavg_count_28",
                          computed=bool((cT["sig"] + cT["inv"]) == (cHe3["sig"] + cHe3["inv"]) == 28),
                          expected=True,
                          source="both A=3 ⇒ same leading exponent 25, Z-split is sub-leading")
    out = builder.save()
    print(f"\n  slope 10 = non-averaged crossings/nucleon: {'DERIVED' if ok_slope else 'FAILED'}")
    print(f"  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
