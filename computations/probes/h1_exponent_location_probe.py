#!/usr/bin/env python3
"""H1 location test — where does the 10A−5 exponent live?

Formalize-first step 1 of the 9b work-plan
(docs/workplans/2026-06-13-9b-derive-10a-minus-5-workplan.md, PR #2217).

H1 proposed that the exponent in Δ_λ(K) ≈ q₀^(10A−5) is a constant
weight-5-per-chain-object crossing/jet bookkeeping of the canonical
trace difference  B_pred = E₀·(tr_M(W_free) − tr_M(W_atom)).  If so,
the FRAMEWORK side must carry it:  ord(B_pred) ≡ log_{q₀} B_pred must
fall by ≈ 10 q₀-units per added nucleon (trace-diff ~ q₀^{−10A+…}).

This probe decomposes the witnessed exponent identically:

    ord(Δ_λ) = ord(B_AME) − ord(B_pred),        ord(X) := ln X / ln q₀,

(E₀ is A-independent, so it cancels from every per-nucleon slope) and
measures which side carries the 10/nucleon increment. All inputs are
read from `delta-lambda-canonical-residual.witness.json` — no new
physics computation, no fit.

Result (assertions encode it): the trace side moves only +1.2…+2.9
q₀-units per nucleon — wrong magnitude AND wrong sign for H1 — while
ord(B_AME) moves +11.5…+12.8.  The 10A−5 law is the experimental
binding curve's growth (base q₀¹⁰ ≈ 2.84 per nucleon) minus the slowly
varying trace factor, NOT a crossing-count identity of the canonical
words.  H1 verdict: **forbidden at the proposed location** — deriving
10A−5 from W_free/W_atom combinatorics would require deriving B_AME
itself.

EXPLORATORY / DIAGNOSTIC — nothing wired; the near-match tier of the
source observation is unchanged (if anything, this sharpens it toward
the fitted end of the tier).

Ref: docs/audits/2026-06-09-delta-lambda-canonical-residual.md
Ref: docs/audits/2026-06-13-9b-h1-exponent-location-refuted.md
Ref: docs/workplans/2026-06-13-9b-derive-10a-minus-5-workplan.md
"""
from __future__ import annotations

# Path bridge (probes cluster — subdirectory refactor Phase 1).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
SOURCE = COMPUTATIONS / "delta-lambda-canonical-residual.witness.json"


def main() -> int:
    set_compute_dps()
    src = json.loads(SOURCE.read_text())["data"]
    q0 = mp.mpf(repr(src["q0"]))
    lnq0 = mp.log(q0)

    def ord_q0(x) -> mp.mpf:
        return mp.log(mp.mpf(repr(x))) / lnq0

    w = WitnessBuilder("h1-exponent-location", engine="mpmath")
    w.set_description(
        "H1 location test (9b work-plan step 1): decomposes the "
        "witnessed Δ_λ ≈ q₀^(10A−5) exponent as ord(B_AME) − "
        "ord(B_pred) per isotope and measures which side carries the "
        "10-per-nucleon increment. Framework trace side: +1.2…+2.9 "
        "q₀-units/nucleon (wrong magnitude and sign for H1); "
        "experimental B_AME side: +11.5…+12.8. Verdict: H1 forbidden "
        "at the proposed location — the exponent is not a "
        "crossing-count identity of the canonical trace difference. "
        "Diagnostic only; nothing wired."
    )
    w.set_content_block("conj:canonical-knot-id-sdp")

    rows = {r["atom"]: r for r in src["rows"]}
    print(f"{'atom':4s} {'A':>2s} {'ord(B_AME)':>11s} {'ord(B_pred)':>12s} "
          f"{'diff':>8s} {'witness':>8s}")
    ords = {}
    for atom in ("D", "T", "3He", "4He"):
        r = rows[atom]
        oa = ord_q0(r["B_AME_MeV"])
        op = ord_q0(r["B_pred_canonical_MeV"])
        diff = oa - op
        ords[atom] = (r["A"], oa, op)
        print(f"{atom:4s} {r['A']:>2d} {mp.nstr(oa, 7):>11s} "
              f"{mp.nstr(op, 7):>12s} {mp.nstr(diff, 7):>8s} "
              f"{r['log_q0_Delta']:>8.3f}")
        w.add_data(f"{atom}_ord_B_AME", mp.nstr(oa, 20))
        w.add_data(f"{atom}_ord_B_pred", mp.nstr(op, 20))
        w.add_assertion(
            name=f"{atom}_decomposition_matches_witness_exponent",
            computed=float(diff),
            expected=float(r["log_q0_Delta"]),
            tolerance=2e-3,
            source="ord(Δ_λ) = ord(B_AME) − ord(B_pred); algebraic "
                   "consistency with the source witness",
        )

    # Per-nucleon slopes along the N ≥ Z chain D → T → ⁴He (³He is the
    # known Z-dependent outlier and is excluded from the slope test).
    print("per-nucleon slopes (D→T, T→4He):")
    for label, idx in (("ord(B_AME)", 1), ("ord(B_pred)", 2)):
        s1 = (ords["T"][idx] - ords["D"][idx]) / (3 - 2)
        s2 = (ords["4He"][idx] - ords["T"][idx]) / (4 - 3)
        print(f"  {label:12s} {mp.nstr(s1, 5):>8s} {mp.nstr(s2, 5):>8s}")
        w.add_data(f"slope_{label.replace('(', '_').replace(')', '')}_DT",
                   mp.nstr(s1, 12))
        w.add_data(f"slope_{label.replace('(', '_').replace(')', '')}_T4He",
                   mp.nstr(s2, 12))
        if label == "ord(B_pred)":
            for nm, s in (("DT", s1), ("T4He", s2)):
                w.add_assertion(
                    name=f"trace_side_slope_{nm}_nowhere_near_minus_10",
                    computed=bool(mp.mpf(0) < s < mp.mpf(4)),
                    expected=True,
                    tolerance=0,
                    source="H1 requires ≈ −10 q₀-units/nucleon on the "
                           "framework trace side; measured slope is "
                           "small and POSITIVE — H1 forbidden at the "
                           "proposed location",
                )
        else:
            for nm, s in (("DT", s1), ("T4He", s2)):
                w.add_assertion(
                    name=f"B_AME_side_slope_{nm}_carries_the_increment",
                    computed=bool(mp.mpf(10) < s < mp.mpf(14)),
                    expected=True,
                    tolerance=0,
                    source="the ~10–13/nucleon growth lives in the "
                           "experimental binding curve, not the "
                           "canonical trace difference",
                )

    w.add_data(
        "verdict",
        "H1 FORBIDDEN at the proposed location: the canonical trace "
        "difference contributes +1.2…+2.9 q₀-units/nucleon (and toward "
        "0 with A), so no crossing/jet bookkeeping of W_free vs W_atom "
        "can yield the 10A−5 exponent; the increment is carried by "
        "B_AME's empirical growth. Deriving 10A−5 from word "
        "combinatorics is equivalent to deriving the binding curve "
        "itself. The 2026-06-09 observation stays near-match tier, "
        "now characterised as: B_AME ≈ E₀·q₀^(10A−5)·(trace factor "
        "drifting q₀^{+1..+3}/nucleon toward 1).",
    )
    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
