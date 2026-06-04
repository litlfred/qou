"""qbeta_c8_c10_crossanchor_falsification.py — §8-guard cross-anchor test
for the c_8 / c_9 / c_10 silver-anchored closed forms (PR #1793).

## The question (Δ_λ-gate-safe — falsification, NOT a new fit)

PR #1793 found Pell-Lucas σ-action closed forms that are EXACT at the
silver ratio q = 1 + √2 (where the Hoefsmit b² = 7/8 exactly):

    c_8(q)  = c_3²·b⁴ = 4·b⁴ = 49/16   at silver
    c_9(q)  = c_3³·b² = -8·b² = -7      at silver
    c_10(q) = c_3²·b⁶ = 4·b⁶ = 343/128  at silver

with b²(q) = (q⁴ + q² + 1) / (q² + 1)²  (canonical Hoefsmit (2,1), =7/8
at silver — numerator 7q², denominator 8q²).

The §8 flip-flop guard (docs/coordination/ck-dk-canonical-registry.md)
requires a passing cross-anchor test BEFORE any c_k rung may leave the
`empirical` tier. This probe runs that test for k = 8, 9, 10 — it had
been recorded as "not cross-anchor tested".

## Two distinct sub-tests (both reported — neither alone is sufficient)

1. **Form swing** (the literal §8 "proton + muon swing < 1%"): is the
   real-q closed form anchor-STABLE? b²(q) is smooth and the anchors
   differ by ≈1.3e-8, so the swing is microscopic — the forms PASS the
   swing sub-test trivially.

2. **Production match** (the discriminator that actually matters): does
   the closed form, evaluated at the substrate q₀, REPRODUCE the Q_β SDP
   residual coefficient extracted at q₀? Per PR #1793 the q₀ SDP
   extraction gives c_8 ≈ 7649, c_9 ≈ 8.98e5, c_10 ≈ 1.05e8 (the
   `(R-1)/(b^k·ℏ^{2k})` ladder is hyper-sensitive / noise-dominated for
   k ≥ 8), while the closed forms give O(1) values. They DISAGREE by
   10³–10⁷×.

## Verdict (expected)

Passing the swing sub-test is NECESSARY but NOT SUFFICIENT for the
`canonical` tier: canonical also requires the form to reproduce the
production residual at q₀, which it fails by 10³–10⁷×. So the closed
forms are **anchor-stable real-q functions that are EXACT only at the
silver structural anchor** and do NOT track the q₀ production residual.
Tier stays `empirical — silver-anchored`; no production wire (§8).

This mirrors the c_3 [3]_q/25 rigidity finding (the real-q form is
smooth/rigid, exact at one anchor only); see
docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md
and CLAUDE.md §"Im(q) at fibre vs observable level".

Run:
    python3 folio-assistant/computations/qbeta/qbeta_c8_c10_crossanchor_falsification.py
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
from mpmath import mp, mpf  # noqa: E402

# qou_substrate path (matches qbeta_singularity_cross_anchor_probe.py).
_QS = (Path(__file__).resolve().parent.parent.parent.parent
       / "tools" / "qou-substrate" / "python")
if _QS.is_dir() and str(_QS) not in sys.path:
    sys.path.insert(0, str(_QS))
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402

# §8-guard swing threshold for the literal "proton + muon swing" sub-test.
MAX_SWING_PCT = 1.0
# A closed form "reproduces" the q₀ SDP residual if within this tolerance.
MAX_PRODUCTION_MATCH_PCT = 1.0


def b_sq(q: mpf) -> mpf:
    """Canonical Hoefsmit (2,1) parameter squared: b² = (q⁴+q²+1)/(q²+1)².

    = 7/8 exactly at q = 1+√2 (numerator 7q², denominator 8q²)."""
    return (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2


def closed_forms(q: mpf) -> dict[int, mpf]:
    """The Pell-Lucas σ-action closed forms as real-q functions.

    c_8 = c_3²·b⁴ = 4·(b²)², c_9 = c_3³·b² = -8·b², c_10 = c_3²·b⁶ = 4·(b²)³,
    with c_3 = -2 (so c_3² = 4, c_3³ = -8)."""
    bs = b_sq(q)
    return {
        8: mpf(4) * bs ** 2,
        9: mpf(-8) * bs,
        10: mpf(4) * bs ** 3,
    }


def load_sdp_extracted_q0() -> dict[int, mpf]:
    """Load the q₀ SDP-extracted c_8/c_9/c_10 (50dps) from PR #1793's witness."""
    src = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    if not src.exists():
        src = HERE.parent / "qbeta-decay-sdp-extended-ck.witness.json"
    with src.open() as f:
        raw = json.load(f)["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mpf(str(v)) for k, v in raw.items() if int(k.split("_")[1]) in (8, 9, 10)}


# Exact silver-ratio targets (Pell-Lucas-clean rationals).
SILVER_EXACT = {8: Fraction(49, 16), 9: Fraction(-7, 1), 10: Fraction(343, 128)}


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder("qbeta-c8-c10-crossanchor-falsification",
                        engine="mpmath", start_time=t0)

    q_silver = 1 + mp.sqrt(2)
    q_p = mpf(str(q_at()))
    q_m = mpf(str(q_muon_at()))
    sep = abs(q_p - q_m)

    cf_silver = closed_forms(q_silver)
    cf_p = closed_forms(q_p)
    cf_m = closed_forms(q_m)
    sdp_q0 = load_sdp_extracted_q0()

    print("=" * 78)
    print(" c_8 / c_9 / c_10 silver-anchored closed forms — cross-anchor test")
    print("=" * 78)
    print(f"  b²(silver) = {mp.nstr(b_sq(q_silver), 18)}  (target 7/8 = 0.875)")
    print(f"  b²(proton) = {mp.nstr(b_sq(q_p), 18)}")
    print(f"  b²(muon)   = {mp.nstr(b_sq(q_m), 18)}")
    print(f"  anchor separation |q_p - q_m| = {mp.nstr(sep, 6)}")
    print()

    # ── Sub-test 0: exactness at the silver structural anchor ───────────
    silver_ok = True
    print("  [silver-ratio exactness — the only validated regime]")
    for k in (8, 9, 10):
        target = mpf(SILVER_EXACT[k].numerator) / mpf(SILVER_EXACT[k].denominator)
        err = abs(cf_silver[k] - target)
        ok = err < mpf(10) ** (-40)
        silver_ok = silver_ok and ok
        print(f"    c_{k}: closed = {mp.nstr(cf_silver[k], 16):>20}  "
              f"exact = {str(SILVER_EXACT[k]):>8}  {'✓' if ok else '✗'}")
    print()

    # ── Sub-test 1: §8 literal form swing (proton ↔ muon) ───────────────
    print("  [§8 sub-test 1 — form swing proton↔muon (< 1% ⇒ anchor-stable)]")
    max_swing_pct = 0.0
    swings = {}
    for k in (8, 9, 10):
        swing_pct = float((cf_p[k] - cf_m[k]) / abs(cf_p[k]) * 100)
        swings[k] = swing_pct
        max_swing_pct = max(max_swing_pct, abs(swing_pct))
        print(f"    c_{k}: proton = {mp.nstr(cf_p[k], 12):>16}  "
              f"muon = {mp.nstr(cf_m[k], 12):>16}  swing = {swing_pct:+.3e}%")
    form_anchor_stable = max_swing_pct < MAX_SWING_PCT
    print(f"    → max |swing| = {max_swing_pct:.3e}%  "
          f"({'STABLE' if form_anchor_stable else 'UNSTABLE'})")
    print()

    # ── Sub-test 2: production match vs q₀ SDP residual ─────────────────
    print("  [§8 sub-test 2 — does the form reproduce the q₀ SDP residual?]")
    max_ratio = 0.0
    ratios = {}
    production_match = True
    for k in (8, 9, 10):
        sdp = sdp_q0[k]
        cf = cf_p[k]
        ratio = float(abs(sdp / cf)) if cf != 0 else float("inf")
        ratios[k] = ratio
        max_ratio = max(max_ratio, ratio if ratio > 1 else 1 / ratio)
        err_pct = float(abs((cf - sdp) / sdp) * 100)
        matches = err_pct < MAX_PRODUCTION_MATCH_PCT
        production_match = production_match and matches
        print(f"    c_{k}: closed(q₀) = {mp.nstr(cf, 8):>12}  "
              f"SDP(q₀) = {mp.nstr(sdp, 8):>14}  ratio = {ratio:.2e}×  "
              f"{'MATCH' if matches else 'MISS'}")
    print(f"    → forms {'REPRODUCE' if production_match else 'DO NOT reproduce'} "
          f"the q₀ SDP residual (worst ratio {max_ratio:.2e}×)")
    print()

    # ── Verdict ─────────────────────────────────────────────────────────
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    # canonical requires BOTH anchor-stability AND production match.
    canonical_eligible = form_anchor_stable and production_match
    if canonical_eligible:
        print("  ★ canonical-eligible — anchor-stable AND reproduces q₀ residual.")
    else:
        print("  EMPIRICAL — SILVER-ANCHORED (as predicted). The closed forms are")
        print(f"  anchor-stable real-q functions (swing {max_swing_pct:.1e}% < 1%,")
        print(f"  PASS sub-test 1) but DO NOT reproduce the q₀ SDP residual —")
        print(f"  they miss by up to {max_ratio:.1e}× (FAIL sub-test 2). The Pell-")
        print("  Lucas closed forms are EXACT only at the silver structural anchor")
        print("  (b² = 7/8); at the substrate q₀ the production residual lives")
        print("  10³–10⁷× away. Passing the swing test is necessary but NOT")
        print("  sufficient for `canonical`; the forms stay `empirical — silver-")
        print("  anchored`. No production wire (§8 flip-flop guard).")
        print()
        print("  Consistent with the c_3 [3]_q/25 rigidity finding and CLAUDE.md")
        print("  §Im(q) fibre-vs-observable: a smooth real-q form is exact at one")
        print("  structural anchor and rigid elsewhere; the genuine q₀ residual")
        print("  structure is not a real-q O(1) constant.")

    wb.add_assertion(
        "c8_c9_c10_closed_forms_exact_at_silver_ratio",
        computed=silver_ok,
        expected=True,
        source="Closed forms c_8=4·b⁴, c_9=-8·b², c_10=4·b⁶ equal 49/16, -7, "
               "343/128 at q=1+√2 (b²=7/8). The validated structural regime.",
    )
    wb.add_assertion(
        "c8_c9_c10_closed_forms_reproduce_q0_sdp_residual",
        computed=production_match,
        expected=False,
        source="Whether the closed forms, evaluated at the substrate q₀ (proton "
               "anchor), reproduce the Q_β SDP-extracted residual coefficients "
               "(c_8≈7649, c_9≈8.98e5, c_10≈1.05e8) within 1%. Expected False — "
               "they disagree by 10³–10⁷× (the q₀ extraction is hyper-sensitive / "
               "noise-dominated for k≥8). This is the §8 discriminator: the forms "
               "are NOT q₀ production coefficients, only silver-ratio structural "
               "identities.",
    )
    wb.add_assertion(
        "c8_c9_c10_closed_forms_anchor_stable_swing_under_1pct",
        computed=form_anchor_stable,
        expected=True,
        source="The literal §8 swing sub-test: the real-q closed forms swing "
               "<1% between proton and muon anchors (b²(q) is smooth). PASS — but "
               "necessary, not sufficient, for canonical (see the production-match "
               "assertion).",
    )

    wb.add_data("q_silver", mp.nstr(q_silver, 30))
    wb.add_data("q_proton", mp.nstr(q_p, 30))
    wb.add_data("q_muon", mp.nstr(q_m, 30))
    wb.add_data("anchor_separation", mp.nstr(sep, 12))
    wb.add_data("b_sq_silver", mp.nstr(b_sq(q_silver), 30))
    wb.add_data("b_sq_proton", mp.nstr(b_sq(q_p), 30))
    wb.add_data("b_sq_muon", mp.nstr(b_sq(q_m), 30))
    for k in (8, 9, 10):
        wb.add_data(f"c{k}_closed_silver", mp.nstr(cf_silver[k], 30))
        wb.add_data(f"c{k}_closed_proton", mp.nstr(cf_p[k], 30))
        wb.add_data(f"c{k}_closed_muon", mp.nstr(cf_m[k], 30))
        wb.add_data(f"c{k}_sdp_extracted_q0", mp.nstr(sdp_q0[k], 30))
        wb.add_data(f"c{k}_silver_exact", str(SILVER_EXACT[k]))
        wb.add_data(f"c{k}_form_swing_pct", swings[k])
        wb.add_data(f"c{k}_sdp_over_closed_ratio", ratios[k])
    wb.add_data("max_form_swing_pct", max_swing_pct)
    wb.add_data("worst_production_mismatch_ratio", max_ratio)
    wb.add_data("form_anchor_stable", form_anchor_stable)
    wb.add_data("reproduces_q0_sdp_residual", production_match)
    wb.add_data("canonical_eligible", canonical_eligible)
    wb.add_data("verdict", (
        "EMPIRICAL — SILVER-ANCHORED. The c_8/c_9/c_10 Pell-Lucas closed forms "
        f"(4·b⁴, -8·b², 4·b⁶) are anchor-stable (max swing {max_swing_pct:.2e}% "
        "< 1%, PASS §8 sub-test 1) but do NOT reproduce the q₀ SDP residual "
        f"(miss by up to {max_ratio:.2e}×, FAIL §8 sub-test 2). They are EXACT "
        "only at the silver structural anchor (b²=7/8). Necessary-but-not-"
        "sufficient: stays `empirical — silver-anchored`, no production wire. "
        "Falsification test; no fit, no production change."
    ))

    out = wb.save()
    print()
    n_pass = sum(1 for a in wb.assertions if a.passed)
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"{n_pass}/{len(wb.assertions)} passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
