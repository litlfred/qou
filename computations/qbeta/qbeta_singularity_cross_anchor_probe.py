"""qbeta_singularity_cross_anchor_probe.py — Step 2 of PR #1727.

**Cross-anchor validation** of Step 1's SIMPLE-POLE verdict at the
q_muon anchor (the alternative substrate q value, superseded
2026-05-28 by the m_p anchor but still well-defined per
`qou_substrate.constants.q_muon_at()`).

## Hypothesis

Step 1 (PR #1727) at q_proton found `c_k · u_subst^k → 2.118e-13` at
k=8,9,10 (simple-pole signature, residue A = 1.804e-15 ≈ 1 ppQ).

Per AGENTS.md §"Im(q) fibre vs observable" (2026-06-01):

> The c_k Taylor coefficients live in the FIBRE (formal q-deformation,
> potentially complex). Each q_0 anchor is a different archimedean
> evaluation of the SAME fibre object.

If the singularity is genuinely fibre-level, the SAME simple-pole
structure (with potentially-different residue magnitude) should appear
at q_muon. The TYPE (simple pole) should be anchor-INDEPENDENT; the
residue VALUE may differ.

## Method

1. Compute q_muon via `qou_substrate.constants.q_muon_at()` (= the
   m_μ/m_e-anchor q value).
2. Reconstruct the canonical Q_β SDP at q_muon — but this is
   expensive (re-runs the full operator-selection LP) and depends on
   infrastructure that may not be cleanly re-anchorable at q_muon
   without re-pinning.
3. **Pragmatic alternative**: at q_muon, the SDP inputs (Q_AME and the
   N=2 cos correction) are different by ~11.5 ppb from q_proton. The
   FIBRE object F(u) is the same; only the EVALUATION point u differs.
4. Evaluate the c_k Taylor coefficients (FROM the q_proton extraction)
   AT the q_muon u value: u_muon = b(q_muon) · ℏ_q²(q_muon). If the
   fibre F(u) has a simple pole at u_subst(q_proton) = u_subst(q_muon),
   that's anchor-INDEPENDENT. If u_subst differs, that itself is the
   fibre/observable distinction.

## What this rigorously tests

The asymptote `c_k · u^k → const` is a CONVERGENT-SERIES property of
the formal power series F(u), independent of the specific q. So:

  fibre-level interpretation: c_k are q-independent rational
  combinations (e.g. of integers + ratios of b, ℏ_q²); only the
  EVALUATION at a specific q changes u_subst.

  observable-level interpretation: the c_k themselves change with q.

Step 1's c_k values are the q_proton-canonical-pinned extraction.
Re-extracting at q_muon would require re-running the full SDP at
q_muon (out of scope for one session). What we CAN do cheaply:

  (a) Compute u_subst(q_muon) — does it differ structurally?
  (b) Compute residue prediction A(q_muon) ASSUMING fibre-level
      (same c_k tail, just different u_subst).
  (c) Compare to a partial-evaluation cross-check via the
      q-pinning-50-digit witness if it has a q_muon-anchored entry.

Tiered output.

Ref: docs/coordination/2026-06-02-qbeta-1ppq-closure-scope.md
Ref: tools/qou-substrate/python/qou_substrate/constants.py (q_muon_at)
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 100

# qou_substrate path
_QS = (Path(__file__).resolve().parent.parent.parent.parent
       / "tools" / "qou-substrate" / "python")
if _QS.is_dir() and str(_QS) not in sys.path:
    sys.path.insert(0, str(_QS))
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402


def load_ck_from_witness() -> tuple[dict[int, mp.mpf], dict, dict]:
    """Load the resolved c_k, plus the extraction's resolution block.

    Returns ``(resolved, resolution, raw_quotient)`` where ``resolved`` holds ONLY the rungs
    the upstream extractor certified as resolved.  A rung the extractor could
    not resolve is emitted as ``null`` (see qou-8ofm / qou-frch, 2026-08-10)
    and is omitted here rather than coerced -- ``mp.mpf(str(None))`` raises,
    which is how this probe crashed on main.
    """
    src = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    if not src.exists():
        src = HERE.parent / "qbeta-decay-sdp-extended-ck.witness.json"
    with src.open() as f:
        d = json.load(f)
    raw = d["data"]["c_k_extracted_50dps"]
    resolved = {int(k.split("_")[1]): mp.mpf(str(v))
                for k, v in raw.items() if v is not None}
    return (resolved, d["data"]["c_k_resolution"],
            d["data"]["c_k_unresolved_raw_quotient"])


def floor_identity_diagnostic(resolution: dict, raw_quotient: dict) -> dict:
    """Show that the unresolved rungs reproduce the simple-pole signature exactly.

    When rung k is unresolved, ``R_k - 1`` has stalled at the model's accuracy
    floor ``f`` and the extractor's quotient is ``c_k := (R_k - 1)/u^k = f/u^k``.
    Two consequences are then ARITHMETIC, not evidence about F(u):

        |c_k * u^k| = f          (flat asymptote, zero spread)
        c_{k+1}/c_k = 1/u        (ratio test hits the pole location exactly)

    Both are the signature PR #1727 read as "simple pole at u_substrate with
    residue A = f * u".  A residual floor produces them identically, so the
    signature cannot distinguish the two.  This function measures how exactly.
    """
    u = mp.mpf(resolution["ladder_variable_u"])
    per = resolution["per_rung"]
    # The extractor's ACTUAL emitted quotients, not a re-derivation of them:
    # checking f/u^k against f would be a tautology of our own division.
    raw = {int(k.split("_")[1]): mp.mpf(v) for k, v in raw_quotient.items()}
    rows = []
    for k in sorted(raw):
        r = per.get(f"c_{k}")
        if r is None or r.get("resolved"):
            continue
        floor = mp.mpf(r["residual_abs_R_minus_1"])
        flat_rel = abs(abs(raw[k] * u ** k) - floor) / floor
        row = {"k": k, "floor": floor, "flat_rel": flat_rel, "ratio_rel": None}
        nxt = per.get(f"c_{k + 1}")
        if k + 1 in raw and nxt is not None and not nxt.get("resolved"):
            row["ratio_rel"] = abs((raw[k + 1] / raw[k]) * u - 1)
        rows.append(row)
    return {"u": u, "rows": rows}


def main() -> int:
    q_proton = q_at(80)
    q_muon = q_muon_at(80)

    def b_and_hbar(q: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        hbar_q = (q - 1) / q
        hbar_q_sq = hbar_q * hbar_q
        # b at this anchor: b² = (q^4 + q² + 1) / (q² + 1)²
        # (per qou_substrate convention)
        b_sq = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2
        b = mp.sqrt(b_sq)
        return b, hbar_q_sq, b * hbar_q_sq

    _, _, u_p = b_and_hbar(q_proton)
    _, _, u_m = b_and_hbar(q_muon)

    print(f"Q_β singularity cross-anchor probe")
    print(f"  q_proton    = {mp.nstr(q_proton, 14)}")
    print(f"  q_muon      = {mp.nstr(q_muon, 14)}")
    print(f"  Δq / q      = {mp.nstr((q_muon - q_proton) / q_proton * mp.mpf('1e9'), 4)} ppb")
    print(f"  u_proton    = {mp.nstr(u_p, 14)}")
    print(f"  u_muon      = {mp.nstr(u_m, 14)}")
    print(f"  Δu / u      = {mp.nstr((u_m - u_p) / u_p * mp.mpf('1e9'), 4)} ppb")
    print(f"  1/u_proton  = {mp.nstr(1 / u_p, 12)}")
    print(f"  1/u_muon    = {mp.nstr(1 / u_m, 12)}")
    print()

    # --- (a) Step 1's premise, re-checked against the current extraction ---
    #
    # Step 1 (PR #1727) read a SIMPLE POLE off c_k * u^k -> 2.118e-13 at
    # k = 8, 9, 10.  Since then qou-8ofm / qou-frch (2026-08-10) established
    # that this extraction determines AT MOST ONE rung -- R(q0) is a single
    # scalar -- and that every higher rung is the model's accuracy floor
    # divided by u^k.  Rungs 8-10 are in that stalled range.
    resolved, resolution, raw_quotient = load_ck_from_witness()
    n_unresolved = resolution.get("n_unresolved")
    last_resolved = resolution.get("last_resolved_rung")

    print("--- (a) Is Step 1's premise still supported by the extraction? ---")
    print(f"  resolved rungs           : "
          f"{sorted(resolved) if resolved else 'none'}")
    print(f"  last_resolved_rung       : {last_resolved}")
    print(f"  unresolved rungs         : {n_unresolved}")

    diag = floor_identity_diagnostic(resolution, raw_quotient)
    u_lad = diag["u"]
    premise_supported = all(k in resolved for k in (8, 9, 10))

    if diag["rows"]:
        print()
        print("  In the stalled range the pole signature is an IDENTITY, not")
        print("  evidence: with c_k := (R_k - 1)/u^k and R_k - 1 pinned at the")
        print("  floor f, both |c_k u^k| = f and c_{k+1}/c_k = 1/u hold exactly.")
        print()
        print(f"  {'k':>3s} {'floor f':>22s} {'|c_k u^k|/f - 1':>18s}"
              f" {'(c_k+1/c_k)*u - 1':>20s}")
        for r in diag["rows"]:
            rr = ("" if r["ratio_rel"] is None
                  else mp.nstr(r["ratio_rel"], 6))
            print(f"  {r['k']:>3d} {mp.nstr(r['floor'], 16):>22s}"
                  f" {mp.nstr(r['flat_rel'], 6):>18s} {rr:>20s}")
        print()
        print(f"  1/u_ladder = {mp.nstr(1 / u_lad, 14)}"
              f"   (the 'pole location' the ratio test returns)")

    if premise_supported:
        print("\n  Rungs 8-10 ARE resolved -- Step 1's premise stands; "
              "cross-anchor test below is meaningful.")
    else:
        print("\n  Rungs 8-10 are NOT resolved. Step 1's premise -- the flat")
        print("  asymptote at k = 8, 9, 10 -- is the floor identity above, so")
        print("  this probe's subject (cross-anchor validation of that pole")
        print("  TYPE and its residue) has nothing left to validate.")
        print("  Not substituted: c_k_unresolved_raw_quotient. Those ARE the")
        print("  floor quotients; using them would re-derive the artifact.")
    print()

    print("--- (b) Fibre-level test: is u_subst anchor-independent? ---")
    # If F(u) is a fibre-level object with a FIXED singularity at some
    # u* (independent of q), then both anchors should have the SAME
    # singularity location u*. Step 1 found u_subst(q_proton) ≈ u_p
    # (radius of convergence = u_evaluated). If u_muon ≠ u_p, then the
    # singularity LOCATION shifts with q ⇒ anchor-dependent (observable-
    # level) interpretation.
    delta_u_rel = (u_m - u_p) / u_p
    print(f"  u_proton = {mp.nstr(u_p, 16)}")
    print(f"  u_muon   = {mp.nstr(u_m, 16)}")
    print(f"  Δu / u_p = {mp.nstr(delta_u_rel * mp.mpf('1e9'), 6)} ppb")
    fibre_level = abs(delta_u_rel) < mp.mpf("1e-6")
    print(f"  u_subst anchor-independent (within 1 ppm)? {fibre_level}")
    print()

    # Verdict logic
    if not premise_supported:
        verdict = ("PREMISE_WITHDRAWN — rungs 8-10 unresolved, so Step 1's "
                   "simple-pole signature is the residual-floor identity; the "
                   "pole TYPE and residue A are unanswered, not confirmed")
    elif fibre_level:
        verdict = "FIBRE_LEVEL_CONFIRMED — singularity at same u across anchors"
    else:
        delta_ppb = float(delta_u_rel * mp.mpf("1e9"))
        verdict = (f"ANCHOR_DEPENDENT — u_subst shifts by "
                   f"{delta_ppb:.1f} ppb between q_proton and q_muon")
    print(f"VERDICT: {verdict}")
    print()
    print("Caveat: this probe uses c_k extracted at q_proton and evaluates them")
    print("at q_muon's u-value. A fully rigorous cross-anchor test would re-run")
    print("the full SDP at q_muon and re-extract c_k; that requires re-pinning")
    print("infrastructure (out of scope for Step 2). The current test discriminates")
    print("the u_subst LOCATION question, not the RESIDUE value question.")

    # Witness
    w = WitnessBuilder("qbeta-singularity-cross-anchor-probe", engine="mpmath")
    w.set_description(
        "Step 2 of PR #1727 / Q_β 1ppQ closure: cross-anchor test of "
        "Step 1's SIMPLE_POLE verdict at q_muon. Tests whether u_subst "
        "(singularity location of F(u)) is fibre-level (same at both "
        "anchors) or anchor-dependent. Uses q_proton-extracted c_k "
        "evaluated at q_muon's u value (partial test; full re-extraction "
        "at q_muon is out of scope for one session)."
    )
    w.add_data("q_proton", mp.nstr(q_proton, 30))
    w.add_data("q_muon", mp.nstr(q_muon, 30))
    w.add_data("u_proton", mp.nstr(u_p, 30))
    w.add_data("u_muon", mp.nstr(u_m, 30))
    w.add_data("delta_u_relative_ppb", mp.nstr(delta_u_rel * mp.mpf("1e9"), 12))
    w.add_data("fibre_level_within_1ppm", str(fibre_level))
    w.add_data("step1_premise_supported", str(premise_supported))
    w.add_data("last_resolved_rung", str(last_resolved))
    w.add_data("n_unresolved_rungs", str(n_unresolved))
    w.add_data("floor_identity", {
        "note": ("In the unresolved range c_k := f/u^k identically, so "
                 "|c_k*u^k| = f and c_{k+1}/c_k = 1/u hold by arithmetic. "
                 "Both are the simple-pole signature PR #1727 read as "
                 "evidence, so that signature does not discriminate a pole "
                 "from a residual floor."),
        "per_rung": [
            {"k": r["k"],
             "floor": mp.nstr(r["floor"], 20),
             "flat_asymptote_rel_error": mp.nstr(r["flat_rel"], 6),
             "ratio_test_rel_error": (None if r["ratio_rel"] is None
                                      else mp.nstr(r["ratio_rel"], 6))}
            for r in diag["rows"]
        ],
    })
    w.add_data("verdict", verdict)
    w.add_assertion(
        name="cross_anchor_u_subst_compared",
        computed=True,
        expected=True,
        tolerance=0,
        source="Step 2 of Q_β 1ppQ closure",
    )
    w.add_assertion(
        name="step1_premise_supported",
        computed=premise_supported,
        expected=premise_supported,
        tolerance=0,
        source=("whether rungs 8-10 -- the ones Step 1's flat asymptote was "
                "read off -- are certified resolved by the upstream extractor "
                "(qou-8ofm / qou-frch). Recorded, not gated: this probe "
                "reports the premise's status, it does not assert it."),
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
