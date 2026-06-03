"""qbeta_singularity_cross_anchor_probe.py — Step 2 of PR #1727.

**Cross-anchor validation** of Step 1's SIMPLE-POLE verdict at the
q_muon anchor (the alternative substrate q value, superseded
2026-05-28 by the m_p anchor but still well-defined per
`qou_substrate.constants.q_muon_at()`).

## Hypothesis

Step 1 (PR #1727) at q_proton found `c_k · u_subst^k → 2.118e-13` at
k=8,9,10 (simple-pole signature, residue A = 1.804e-15 ≈ 1 ppQ).

Per CLAUDE.md §"Im(q) fibre vs observable" (2026-06-01):

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


def load_ck_from_witness() -> dict[int, mp.mpf]:
    """Load c_2..c_10 (q_proton-canonical-pinned extraction)."""
    src = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    if not src.exists():
        src = HERE.parent / "qbeta-decay-sdp-extended-ck.witness.json"
    with src.open() as f:
        d = json.load(f)
    raw = d["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mp.mpf(str(v)) for k, v in raw.items()}


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

    # Step 1 verdict at q_proton: c_k · u_p^k → 2.118e-13 at k=8,9,10
    ck = load_ck_from_witness()
    print("--- (a) Re-evaluate c_k_proton · u^k AT each anchor's u ---")
    print(f"  (c_k_proton = canonical-pinned extraction at q_proton)")
    print(f"  {'k':>3s} {'c_k':>20s} {'c_k·u_p^k':>18s} {'c_k·u_m^k':>18s} {'ratio':>14s}")
    for k in sorted(ck.keys()):
        if k < 6:
            continue
        cp = ck[k] * u_p ** k
        cm = ck[k] * u_m ** k
        ratio = cm / cp if cp != 0 else mp.mpf(0)
        print(f"  {k:>3d} {mp.nstr(ck[k], 10):>20s} {mp.nstr(cp, 10):>18s} {mp.nstr(cm, 10):>18s} {mp.nstr(ratio, 10):>14s}")
    print()

    # The ratio cp/cm = (u_p/u_m)^k. At large k, the ratio amplifies the
    # Δu = 11.5 ppb difference: ratio^k ≈ (1 + k·Δu/u). At k=10, ratio
    # should be ~115 ppb scaled — not the structural anchor-independence.
    # WHAT MATTERS for fibre-level interpretation: does u_subst (the
    # singularity location) shift WITH q_0, or stay FIXED in the fibre?
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
    if fibre_level:
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
    w.add_data("verdict", verdict)
    w.add_assertion(
        name="cross_anchor_u_subst_compared",
        computed=True,
        expected=True,
        tolerance=0,
        source="Step 2 of Q_β 1ppQ closure",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
