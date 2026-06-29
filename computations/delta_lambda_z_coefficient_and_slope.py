#!/usr/bin/env python3
"""delta_lambda_z_coefficient_and_slope.py
=========================================

Two derive-or-refute tests on the canonical residual Δ_λ(K)=B_AME/B_pred
(`delta_lambda_canonical_residual.py`), requested as the next step after the
bar-parity split (PR #3089, `delta_lambda_exponent_from_crossings.py`):

  (1) SLOPE TEST of the leading law `log_{q₀} Δ_λ ≈ 10A−5` at A ≥ 5
      (⁶Li, ⁷Li, ⁷Be — newly added to `binding_canonical.py`).
  (2) Z-CORRECTION coefficient: the proton-excess penalty (the ³He "−1.4")
      from the p≠n intra-writhe seed (proton +3 > neutron +1), tested on a
      SECOND mirror pair (⁷Li / ⁷Be) beyond T / ³He.

## (1) Result — the 10A−5 law is a LIGHT-NUCLEUS (A≤4) artifact (scope-(a))

    atom  A   log_{q₀}Δ_λ   10A−5   dev
    D     2     14.99        15     −0.01
    T     3     24.93        25     −0.07
    ³He   3     23.60        25     −1.40
    ⁴He   4     35.27        35     +0.27
    ⁶Li   6     36.12        55    −18.88   ✗
    ⁷Li   7     38.79        65    −26.21   ✗
    ⁷Be   7     37.02        65    −27.98   ✗

The slope is ≈10/nucleon ONLY for A≤4; from ⁴He→⁶Li it collapses to
≈0.4/nucleon. The producer's earlier extrapolation (⁶Li→55, ⁸Be→75) is
**REFUTED by direct compute**. This is a SCOPE-LIMITED negative (AGENTS.md
"refuted" discipline (a)): the law holds for A≤4 and does NOT continue — it is
not a structural exclusion of the crossing bookkeeping, only of the *global*
A-law reading. Root cause: `B_pred` SATURATES (≈0.7–0.8) while `B_AME` grows
~linearly, so `log Δ_λ = log B_AME − log B_pred` grows ~logarithmically; the
apparent slope-10 was a coincidence of two light-nucleus trends, broken at the
⁴He shell closure (⁶Li is only 3.7 MeV more bound than ⁴He).

## (2) Result — the proton-excess Z-correction SURVIVES (confirmed, 2 pairs)

The mirror-pair split (proton-rich member minus neutron-rich mirror, fixed A,
identical `σ+σ⁻¹` ⇒ identical leading term) isolates the bar-ODD Z-correction:

    pair        proton-rich   mirror    Δ(dev) = proton-excess penalty
    T  / ³He    ³He −1.40     T −0.07   −1.33
    ⁷Li / ⁷Be   ⁷Be −27.98    ⁷Li −26.21 −1.77

Both ≈ −1.3…−1.8 per excess proton, SAME SIGN — the bar-odd Z-correction holds
at A=7 even though the bar-even leading law has collapsed. The two channels are
independent, exactly as the writhe split predicts (Z−N drives the odd part; the
even baseline is a separate, A-saturating object).

DERIVED vs NOT (no fit — Δ_λ gate):
- **Sign DERIVED** from the 3>1 seed: proton intra-writhe (+3) > neutron (+1) ⇒
  proton excess accumulates net positive chirality ⇒ penalised. Confirmed: both
  proton-rich members sit BELOW their mirrors.
- **Magnitude NOT a single derivable number.** −1.33 (A=3) vs −1.77 (A=7) drift
  ~33%; there is no parameter-free constant the data support, and with two pairs
  a one-number "derivation" would be numerology (explicitly NOT attempted). The
  honest statement: the penalty is O(−1.5) per excess proton, sign-fixed by the
  seed, magnitude open. NOT wired.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import math
import time
from pathlib import Path

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

HERE = Path(__file__).parent
RESIDUAL = HERE / "delta-lambda-canonical-residual.witness.json"


def main() -> int:
    t0 = time.monotonic()
    q0 = float(q_at(30))
    rows = json.loads(RESIDUAL.read_text())["data"]["rows"]
    by = {r["atom"]: r for r in rows}

    # ---- (1) slope test ----------------------------------------------------
    order = sorted(rows, key=lambda r: (r["A"], r["Z"]))
    slope_rows, prev = [], None
    for r in order:
        x = r["log_q0_Delta"]
        marg = None if prev is None or r["A"] == prev["A"] else \
            round((x - prev["log_q0_Delta"]) / (r["A"] - prev["A"]), 2)
        slope_rows.append({"atom": r["atom"], "A": r["A"], "log_q0_Delta": x,
                           "law_10A_5": r["law_10A_minus_5"],
                           "dev": r["deviation_from_law"],
                           "marginal_slope_per_nucleon": marg})
        prev = r
    # law holds (|dev|<0.5) only for A<=4; refuted (|dev|>>1) for A>=5
    light_ok = all(abs(by[a]["deviation_from_law"]) < 0.5
                   for a in ("D", "T", "4He"))
    heavy_refuted = all(abs(by[a]["deviation_from_law"]) > 5
                        for a in ("6Li", "7Li", "7Be") if a in by)

    # ---- (2) Z-correction: mirror-pair proton-excess penalty ---------------
    def split(prich, nrich):
        return round(by[prich]["deviation_from_law"]
                     - by[nrich]["deviation_from_law"], 2)
    pairs = []
    if "3He" in by and "T" in by:
        pairs.append({"A": 3, "proton_rich": "3He", "mirror": "T",
                      "proton_excess_penalty": split("3He", "T")})
    if "7Be" in by and "7Li" in by:
        pairs.append({"A": 7, "proton_rich": "7Be", "mirror": "7Li",
                      "proton_excess_penalty": split("7Be", "7Li")})
    # SIGN derived from 3>1 seed: every proton-rich member sits below its mirror
    sign_ok = all(p["proton_excess_penalty"] < 0 for p in pairs)

    print(f"{'atom':>5} {'A':>2} {'log_q0Δ':>8} {'10A-5':>6} {'dev':>8} {'slope':>7}")
    for s in slope_rows:
        sl = "" if s["marginal_slope_per_nucleon"] is None else f"{s['marginal_slope_per_nucleon']:>7.2f}"
        print(f"{s['atom']:>5} {s['A']:>2} {s['log_q0_Delta']:>8.2f} "
              f"{s['law_10A_5']:>6} {s['dev']:>+8.2f} {sl:>7}")
    print("\n  proton-excess penalty (mirror-pair split, bar-odd Z-correction):")
    for p in pairs:
        print(f"    A={p['A']}: {p['proton_rich']} − {p['mirror']} = "
              f"{p['proton_excess_penalty']:+.2f} q₀-units")
    print(f"\n  10A−5 light (A≤4) ok: {light_ok}; A≥5 refuted: {heavy_refuted}")
    print(f"  Z-correction sign (proton penalised) at all pairs: {sign_ok}")

    b = WitnessBuilder("delta-lambda-z-coefficient-and-slope",
                       engine="python+canonical-binding", start_time=t0)
    (b.set_description(
        "Slope test + Z-coefficient test on the canonical residual Δ_λ. "
        "(1) SLOPE: log_q0 Δ_λ ≈ 10A−5 holds ONLY for A≤4 (slope ~10); at "
        "A≥5 (⁶Li/⁷Li/⁷Be) it collapses to ~0.4–2.7/nucleon — the global "
        "10A−5 extrapolation is REFUTED (scope-(a)): B_pred saturates while "
        "B_AME grows linearly, so log Δ_λ grows logarithmically; slope-10 was "
        "a light-nucleus coincidence broken at the ⁴He shell. (2) Z-CORRECTION: "
        "the proton-excess penalty (mirror-pair split) is −1.33 at A=3 (³He/T) "
        "and −1.77 at A=7 (⁷Be/⁷Li) — SIGN derived from the p≠n intra-writhe "
        "seed (proton +3 > neutron +1), MAGNITUDE O(−1.5) but not a single "
        "derivable constant (no fit; Δ_λ gate). NOT wired.")
     .add_data("q0", q0)
     .add_data("slope_test", {
         "rows": slope_rows,
         "law_holds_A_le_4": bool(light_ok),
         "law_refuted_A_ge_5": bool(heavy_refuted),
         "verdict": "10A−5 is a light-nucleus (A≤4) artifact; the global "
                    "A-law is refuted at A≥5 (scope-limited negative (a)).",
         "root_cause": "B_pred saturates (~0.7-0.8); B_AME ~linear ⇒ log Δ_λ "
                       "~logarithmic ⇒ slope-10 unsustainable past ⁴He shell"})
     .add_data("z_correction", {
         "mirror_pairs": pairs,
         "sign_derived_from_3gt1_seed": bool(sign_ok),
         "magnitude": "O(−1.5)/excess-proton; −1.33 (A=3) vs −1.77 (A=7), ~33% "
                      "drift ⇒ NOT a single derivable constant (no fit)",
         "interpretation": "bar-odd Z-correction survives the bar-even leading "
                           "collapse — independent channels, as the writhe split predicts"}))
    b.add_assertion("slope_10A5_refuted_at_A_ge_5",
                    computed=bool(light_ok and heavy_refuted), expected=True,
                    source="10A−5 holds for D,T,⁴He (|dev|<0.5) but fails for "
                           "⁶Li,⁷Li,⁷Be (|dev|>5) — slope collapses ~10→~1")
    b.add_assertion("proton_excess_penalty_sign_negative_both_pairs",
                    computed=bool(sign_ok), expected=True,
                    source="proton-rich member below mirror at A=3 AND A=7 "
                           "(sign derived from proton intra-writhe 3 > neutron 1)")
    out = b.save()
    print(f"  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
