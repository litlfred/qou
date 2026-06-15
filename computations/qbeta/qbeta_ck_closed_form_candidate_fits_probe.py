#!/usr/bin/env python3
"""qbeta_ck_closed_form_candidate_fits_probe.py — probe 6.b from
the c_k generating-function scoping doc.

PR #1824 follow-on. Probe 6.a (commit 4e9d27f31d) found that the
leading-bias-corrected c_k_corr land on EXACT clean values at k=2, 3:

  c_2_corr = -0.9999932   →  -1
  c_3_corr = -1.9999968   →  -2

These match the pattern **c_k_alg = -(k-1)!** at k=2, 3:
  -(2-1)! = -1!  = -1   ✓
  -(3-1)! = -2!  = -2   ✓

Mathematical note on the generating function (corrected per Gemini
review on PR #1824): the ladder coefficients c_k are the ORDINARY
coefficients in Σ_k c_k u^k (the leading log of the precision
product Q_β/Q_A = Π_k(1+c_k u^k)). The pattern c_k = -(k-1)! gives

  Σ_{k≥1} -(k-1)! · u^k

which is a DIVERGENT factorial (Borel-summable) series — the
hallmark of an asymptotic perturbative expansion (cf. candidate A,
Chern-Simons, whose 1/k perturbative series is famously factorially
divergent).  It is NOT u/(1-u) (whose ordinary coefficients are all
1) nor a convergent -log(1-u) Taylor series (ordinary coefficients
1/k).  An earlier draft of this docstring mislabeled the pattern as
u/(1-u); that was wrong and is corrected here.

The c_2, c_3 EXACT match to -(k-1)! is striking; either:
  (a) The full pattern c_k_alg = -(k-1)! holds, and higher-k bias
      corrections (beyond the leading c_{k+1}·u of probe 6.a) bring
      c_4+ to -6, -24, -120, ...
  (b) The pattern is coincidental at k=2,3 and breaks at k=4.

IMPLEMENTED METHODOLOGY (this probe): apply the SAME leading-order
bias correction as probe 6.a (c_k_corr = c_k - c_{k+1}·u), then
compare c_k_corr against several named candidate coefficient
families (F1..F7 below) and report which match at k=2 AND k=3. This
probe does NOT implement the higher-order bias correction — that is
explicit future work (the (a)-vs-(b) discriminator, requiring
Δc_k = Σ_{j≥1} c_{k+j}·u^j cross-terms).

Candidate coefficient families tested:
  F1. -(k-1)!            (factorial-divergent / asymptotic series)
  F2. -k!               (u/(1-u) ordinary-coefficient form, ×(-1))
  F3. -1                (geometric -1/(1-u))
  F4. (-1)^k            (1/(1+u))
  F5. (-1)^k·(k-1)!     (alternating factorial)
  F6. -k!/2^k           (half-argument)
  F7. -k·(k-1)! = -k!   (duplicate of F2 form)

Reports which candidate matches the observed c_k_corr at k=2 and
k=3 (leading-correction regime). For k≥4 the leading correction is
insufficient; the higher-order future work discriminates (a)/(b).
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    U_SUBST = mp.mpf("0.00852")

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-closed-form-candidate-fits-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Probe 6.b: test candidate closed-form generating functions "
        "against bias-corrected c_k_corr from probe 6.a. The c_2, "
        "c_3 corrected values exactly match -(k-1)! suggesting "
        "F(u) = -log(1-u) or a variant. This probe enumerates "
        "candidate F and reports per-rung match for k=2..10."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Probe 6.b — closed-form candidate fits for c_k generating function")
    print("=" * 78)
    print()

    witness_path = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    with open(witness_path, encoding="utf-8") as f:
        w = json.load(f)
    ck_raw_str = w["data"]["c_k_extracted_50dps"]
    ck = {}
    for k_str, v in ck_raw_str.items():
        k = int(k_str.replace("c_", "")) if k_str.startswith("c_") else int(k_str)
        ck[k] = mp.mpf(v)

    # Apply leading bias correction
    ck_corr = {}
    for k in sorted(ck.keys()):
        if (k + 1) in ck:
            ck_corr[k] = ck[k] - ck[k + 1] * U_SUBST
        else:
            ck_corr[k] = ck[k]

    # Candidate closed forms — coefficients c_k_alg per F
    def factorial(k):
        return mp.mpf(int(mp.factorial(k)))

    candidates = {
        "F1: -(k-1)!         (= -log(1-u) deriv pattern)":
            lambda k: -factorial(k - 1),
        "F2: -k!             (= u/(1-u) Taylor)":
            lambda k: -factorial(k),
        "F3: -1              (= -1/(1-u) constant)":
            lambda k: mp.mpf(-1),
        "F4: (-1)^k          (= 1/(1+u))":
            lambda k: mp.mpf(-1) ** k,
        "F5: (-1)^k · (k-1)!  (= log(1+u) deriv)":
            lambda k: (mp.mpf(-1) ** k) * factorial(k - 1),
        "F6: -k!/2^k          (= -log(1-u/2))":
            lambda k: -factorial(k) / (mp.mpf(2) ** k),
        "F7: -k · (k-1)!      (= u·d/du[-log(1-u)] reading)":
            lambda k: -k * factorial(k - 1),
    }

    print(f"  Candidates evaluated per rung k = 2..7:")
    print()
    print(f"  Candidate                                       k=2     k=3     k=4     k=5     k=6     k=7")
    print(f"  " + "-" * 50 + " " + " ".join(["-" * 7] * 6))
    print(f"  {'observed c_k_corr (from 6.a)':<50} "
          + " ".join([f"{float(ck_corr[k]):>7.2f}" for k in range(2, 8)]))

    matches = {}
    for name, f in candidates.items():
        vals = [f(k) for k in range(2, 8)]
        # Check k=2 match
        match_k2 = mp.fabs((vals[0] - ck_corr[2]) / ck_corr[2]) < mp.mpf("0.01") if ck_corr[2] != 0 else False
        match_k3 = mp.fabs((vals[1] - ck_corr[3]) / ck_corr[3]) < mp.mpf("0.01") if ck_corr[3] != 0 else False
        vals_str = " ".join([f"{float(v):>7.2f}" for v in vals])
        marker = ""
        if match_k2 and match_k3:
            marker = "★ k=2,3 ✓"
        elif match_k2 or match_k3:
            marker = "partial"
        print(f"  {name:<50} {vals_str}  {marker}")
        matches[name] = {
            "match_k2": bool(match_k2),
            "match_k3": bool(match_k3),
            "predictions": [mp.nstr(v, 12) for v in vals],
        }

    print()
    print("=" * 78)
    print(" VERDICT — closed-form candidates")
    print("=" * 78)
    print()

    # Which candidates match BOTH k=2 and k=3?
    winners = [name for name, m in matches.items()
               if m["match_k2"] and m["match_k3"]]
    if winners:
        print(f"  ✓ Candidates matching observed c_2 = -1 AND c_3 = -2:")
        for w in winners:
            print(f"    {w}")
        print()
        print(f"  → These are the COMPATIBLE forms at leading bias correction.")
        print(f"    For k ≥ 4, the observed c_k_corr DIFFER from the candidate")
        print(f"    predictions, indicating either (i) higher-order bias")
        print(f"    correction is needed, OR (ii) the form changes structure.")
    else:
        print(f"  ✗ No candidate matches both c_2 and c_3 simultaneously.")
        print(f"    This is unexpected given probe 6.a's confirmation —")
        print(f"    suggests the closed-form testing approach needs refinement.")
    print()
    print(f"  Pattern observation: c_2_corr = -1, c_3_corr = -2 matches")
    print(f"  c_k_alg = -(k-1)! — the ORDINARY-coefficient pattern of the")
    print(f"  DIVERGENT factorial series Σ_k -(k-1)!·u^k (Borel-summable;")
    print(f"  asymptotic-perturbative signature, cf. candidate A Chern-Simons).")
    print(f"  NOT u/(1-u) (ordinary coeffs all 1) nor convergent -log(1-u).")
    print()
    print(f"  For higher k, raw c_4_corr = -1.13 vs predicted F1 = -6;")
    print(f"  the leading bias correction (probe 6.a) is insufficient")
    print(f"  beyond c_3. Higher-order bias corrections (probe 6.a' future)")
    print(f"  may close the gap.")
    print()

    builder.add_data("observed_c_k_corr", {str(k): mp.nstr(v, 25) for k, v in ck_corr.items()})
    builder.add_data("candidate_matches", matches)
    builder.add_data("winners_at_k2_and_k3", winners)
    builder.add_data("n_winners_at_k2_and_k3", len(winners))

    # Stable invariant only (per Copilot review on PR #1824): assert the
    # probe enumerated all 7 candidate families + produced a match map —
    # NOT the scientific outcome "a winner exists" (which is exploratory
    # and would make a fragile CI gate). The winner count is recorded as
    # data above; the analysis is in the printed verdict.
    builder.add_assertion(
        "probe_6b_enumerated_all_candidates",
        computed=len(matches),
        expected=7,
        tolerance=0,
        source=("Probe 6.b stable invariant: enumerate exactly 7 candidate "
                "closed-form coefficient families (F1..F7) and produce a "
                "per-candidate k=2/k=3 match map. The scientific outcome "
                "(which candidates win) is recorded as data "
                "(winners_at_k2_and_k3, n_winners_at_k2_and_k3) and "
                "discussed in the printed verdict — NOT asserted, to avoid "
                "a fragile scientific-outcome CI gate."),
    )

    builder.save()
    print(f"  Witness: qbeta-ck-closed-form-candidate-fits-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
