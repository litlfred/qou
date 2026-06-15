"""qbeta_c6_c10_crossanchor_falsification.py — §8-guard cross-anchor test
for the c_6..c_10 silver-anchored closed forms, against the BIAS-CORRECTED
q₀ extraction (PR #1824).

## The question (Δ_λ-gate-safe — falsification, NOT a new fit)

PR #1793 derived Pell-Lucas σ-action closed forms, EXACT at the silver
ratio q = 1+√2 (where Hoefsmit b² = 7/8 exactly):

    c_6(q)  = c_3²·b²  = 4·b²  → 7/2     at silver
    c_7(q)  = c_3³     = -8    → -8       at silver
    c_8(q)  = c_3²·b⁴  = 4·b⁴  → 49/16    at silver
    c_9(q)  = c_3³·b²  = -8·b² → -7       at silver
    c_10(q) = c_3²·b⁶  = 4·b⁶  → 343/128  at silver

with b²(q) = (q⁴ + q² + 1) / (q² + 1)²  (canonical Hoefsmit (2,1)).

The §8 flip-flop guard requires a passing cross-anchor test before any
rung leaves the `empirical` tier. This probe runs it for c_6..c_10
against the **bias-corrected** q₀ extraction from PR #1824
(`qbeta-ck-truncation-bias-correction-probe.witness.json`,
`ck_bias_corrected_leading`) — which SUPERSEDES the raw extraction that
the first cut of this probe (PR #1833) used.

## The applied-vs-free distinction (the honest framing)

The canonical extraction (`qbeta_decay_sdp_extended_ck.py`) **applies**
closed forms at rungs c_2..c_7 to advance R, then extracts c_8, c_9, c_10
**freely** (no closed form imposed). So:

  - **c_6, c_7 are APPLIED**: the bias correction RECOVERING them
    (3.011 ≈ 4·b², -8.021 ≈ -8) is a self-consistency check on the
    bias-correction method, NOT an independent validation of the forms.
  - **c_8 is the FIRST FREE RUNG**: its bias-corrected value (-0.215) is
    the first genuine test of the Pell-Lucas continuation — and it does
    NOT match the predicted 4·b⁴ ≈ +2.27 (wrong sign). The pattern
    BREAKS at c_8.

## Verdict (expected)

The closed forms are anchor-stable real-q functions, EXACT at the silver
structural anchor. The bias-corrected extraction confirms them only where
they are assumed (c_6, c_7) and the Pell-Lucas pattern BREAKS at the first
free rung (c_8). Tier stays `empirical — silver-anchored`; no production
wire (§8). Consistent with the c_3 [3]_q/25 rigidity finding and
CLAUDE.md §"Im(q) at fibre vs observable level".

Run:
    python3 folio-assistant/computations/qbeta/qbeta_c6_c10_crossanchor_falsification.py
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

MAX_SWING_PCT = 1.0          # §8 literal swing sub-test
MAX_PRODUCTION_MATCH_PCT = 1.0  # "reproduces the q₀ residual" tolerance

# Which rungs the canonical extraction APPLIES (vs extracts freely).
APPLIED_RUNGS = {6, 7}
FREE_RUNGS = {8, 9, 10}

# Exact silver-ratio targets (Pell-Lucas-clean rationals).
SILVER_EXACT = {
    6: Fraction(7, 2), 7: Fraction(-8, 1), 8: Fraction(49, 16),
    9: Fraction(-7, 1), 10: Fraction(343, 128),
}


def b_sq(q: mpf) -> mpf:
    """Canonical Hoefsmit (2,1) parameter squared: b² = (q⁴+q²+1)/(q²+1)².
    = 7/8 exactly at q = 1+√2 (numerator 7q², denominator 8q²)."""
    return (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2


def closed_forms(q: mpf) -> dict[int, mpf]:
    """Pell-Lucas σ-action closed forms as real-q functions (c_3 = -2)."""
    bs = b_sq(q)
    return {
        6: mpf(4) * bs,
        7: mpf(-8),
        8: mpf(4) * bs ** 2,
        9: mpf(-8) * bs,
        10: mpf(4) * bs ** 3,
    }


def _rung_key(k: str) -> int:
    """Normalize a rung key to its int, tolerating 'c'/'c_' prefixes.

    Upstream witnesses use bare numeric keys ('6'), but some artifacts use
    'c6' / 'c_6' — normalize so a key-format change upstream doesn't crash us.
    """
    s = str(k).strip()
    if s and (s[0] in "cC"):
        s = s[1:].lstrip("_")
    return int(s)


def load_extractions() -> tuple[dict[int, mpf], dict[int, mpf]]:
    """Return (bias_corrected, raw) c_6..c_10 from PR #1824's witness."""
    src = HERE / "qbeta-ck-truncation-bias-correction-probe.witness.json"
    if not src.exists():
        raise FileNotFoundError(
            f"Missing {src.name} (expected at {src}).\n"
            "It is produced by `qbeta_ck_truncation_bias_correction_probe.py` "
            "(PR #1824, same directory). Run that script first, or `git pull` "
            "origin/main if it should already be on this branch."
        )
    with src.open() as f:
        data = json.load(f)["data"]
    want = (6, 7, 8, 9, 10)
    corr = {_rung_key(k): mpf(str(v))
            for k, v in data["ck_bias_corrected_leading"].items()
            if _rung_key(k) in want}
    raw = {_rung_key(k): mpf(str(v))
           for k, v in data["ck_extracted"].items()
           if _rung_key(k) in want}
    return corr, raw


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder("qbeta-c6-c10-crossanchor-falsification",
                        engine="mpmath", start_time=t0)

    q_silver = 1 + mp.sqrt(2)
    q_p = mpf(str(q_at()))
    q_m = mpf(str(q_muon_at()))
    sep = abs(q_p - q_m)

    cf_silver = closed_forms(q_silver)
    cf_p = closed_forms(q_p)
    cf_m = closed_forms(q_m)
    corr, raw = load_extractions()

    print("=" * 78)
    print(" c_6..c_10 silver-anchored closed forms — cross-anchor test")
    print("   (vs PR #1824 BIAS-CORRECTED q₀ extraction)")
    print("=" * 78)
    print(f"  b²(silver) = {mp.nstr(b_sq(q_silver), 16)} (= 7/8)   "
          f"b²(proton) = {mp.nstr(b_sq(q_p), 16)}")
    print(f"  anchor separation |q_p - q_m| = {mp.nstr(sep, 6)}")
    print()

    # ── Sub-test 0: exactness at the silver structural anchor ───────────
    print("  [silver-ratio exactness — the validated structural regime]")
    silver_ok = True
    for k in (6, 7, 8, 9, 10):
        target = mpf(SILVER_EXACT[k].numerator) / mpf(SILVER_EXACT[k].denominator)
        ok = abs(cf_silver[k] - target) < mpf(10) ** (-40)
        silver_ok = silver_ok and ok
        print(f"    c_{k:<2}: closed = {mp.nstr(cf_silver[k], 14):>16}  "
              f"exact = {str(SILVER_EXACT[k]):>8}  {'✓' if ok else '✗'}")
    print()

    # ── Sub-test 1: §8 literal form swing (proton ↔ muon) ───────────────
    print("  [§8 sub-test 1 — form swing proton↔muon (< 1% ⇒ anchor-stable)]")
    max_swing_pct = 0.0
    swings = {}
    for k in (6, 7, 8, 9, 10):
        if cf_p[k] == 0:
            swing_pct = 0.0
        else:
            swing_pct = float((cf_p[k] - cf_m[k]) / abs(cf_p[k]) * 100)
        swings[k] = swing_pct
        max_swing_pct = max(max_swing_pct, abs(swing_pct))
    form_anchor_stable = max_swing_pct < MAX_SWING_PCT
    print(f"    max |swing| over c_6..c_10 = {max_swing_pct:.3e}%  "
          f"({'STABLE' if form_anchor_stable else 'UNSTABLE'})")
    print()

    # ── Sub-test 2: production match vs the BIAS-CORRECTED q₀ residual ───
    print("  [§8 sub-test 2 — does the form reproduce the bias-corrected q₀ residual?]")
    print(f"    {'rung':<5}{'closed(q₀)':>14}{'corrected':>16}{'raw':>16}  role     match")
    match_pct = {}
    pattern_breaks_at = None
    free_match = True
    for k in (6, 7, 8, 9, 10):
        cf = cf_p[k]
        c = corr[k]
        err_pct = float(abs((cf - c) / c) * 100) if c != 0 else float("inf")
        match_pct[k] = err_pct
        matches = err_pct < MAX_PRODUCTION_MATCH_PCT
        role = "APPLIED" if k in APPLIED_RUNGS else "FREE"
        if k in FREE_RUNGS:
            free_match = free_match and matches
            if not matches and pattern_breaks_at is None:
                pattern_breaks_at = k
        print(f"    c_{k:<3}{mp.nstr(cf, 6):>14}{mp.nstr(c, 6):>16}"
              f"{mp.nstr(raw[k], 6):>16}  {role:<8} "
              f"{'MATCH' if matches else 'MISS'} ({err_pct:.2g}%)")
    print()

    # ── Verdict ─────────────────────────────────────────────────────────
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"  Silver exactness: {'✓ all c_6..c_10' if silver_ok else '✗'}")
    print(f"  Form anchor-stability (swing {max_swing_pct:.1e}% < 1%): "
          f"{'✓ STABLE' if form_anchor_stable else '✗'}")
    print(f"  APPLIED rungs c_6/c_7 recovered by bias correction "
          f"({match_pct[6]:.2g}%, {match_pct[7]:.2g}%) — self-consistency, NOT")
    print(f"    independent validation (these forms are imposed in the extraction).")
    if pattern_breaks_at is not None:
        print(f"  ★ Pell-Lucas pattern BREAKS at the first FREE rung c_{pattern_breaks_at}:")
        print(f"    closed = {mp.nstr(cf_p[pattern_breaks_at], 6)} vs bias-corrected "
              f"= {mp.nstr(corr[pattern_breaks_at], 6)} "
              f"({match_pct[pattern_breaks_at]:.2g}% off).")
    print()
    print("  → EMPIRICAL — SILVER-ANCHORED. The closed forms are exact only at the")
    print("  silver structural anchor; the free-rung extraction (c_8+) does not")
    print("  continue the pattern even after bias correction. Anchor-stable but not")
    print("  q₀ production coefficients. No production wire (§8 flip-flop guard).")

    wb.add_assertion(
        "c6_c10_closed_forms_exact_at_silver_ratio",
        computed=silver_ok, expected=True,
        source="Closed forms equal 7/2, -8, 49/16, -7, 343/128 at q=1+√2.",
    )
    wb.add_assertion(
        "c6_c7_applied_forms_recovered_by_bias_correction",
        computed=(match_pct[6] < MAX_PRODUCTION_MATCH_PCT
                  and match_pct[7] < MAX_PRODUCTION_MATCH_PCT), expected=True,
        source="The bias-corrected extraction recovers the c_6=4·b² and c_7=-8 "
               "forms that the extraction IMPOSES (self-consistency of the "
               "bias-correction method; NOT an independent validation).",
    )
    wb.add_assertion(
        "pell_lucas_pattern_survives_into_free_rungs_c8plus",
        computed=free_match, expected=False,
        source="Whether the Pell-Lucas closed forms reproduce the bias-corrected "
               "FREE-rung extraction (c_8,c_9,c_10 — not imposed by the extraction) "
               "within 1%. Expected False: c_8 corrected ≈ -0.215 vs predicted "
               "4·b⁴ ≈ +2.27 (wrong sign) — the pattern breaks at the first free "
               "rung. The forms are silver-ratio structural identities, not q₀ "
               "production coefficients.",
    )
    wb.add_assertion(
        "c6_c10_closed_forms_anchor_stable_swing_under_1pct",
        computed=form_anchor_stable, expected=True,
        source="The real-q closed forms swing <1% between proton and muon anchors "
               "(b²(q) smooth). Necessary but not sufficient for canonical.",
    )

    wb.add_data("q_silver", mp.nstr(q_silver, 30))
    wb.add_data("q_proton", mp.nstr(q_p, 30))
    wb.add_data("q_muon", mp.nstr(q_m, 30))
    wb.add_data("b_sq_proton", mp.nstr(b_sq(q_p), 30))
    wb.add_data("pattern_breaks_at_free_rung", pattern_breaks_at)
    for k in (6, 7, 8, 9, 10):
        wb.add_data(f"c{k}_closed_proton", mp.nstr(cf_p[k], 24))
        wb.add_data(f"c{k}_bias_corrected_q0", mp.nstr(corr[k], 24))
        wb.add_data(f"c{k}_raw_q0", mp.nstr(raw[k], 24))
        wb.add_data(f"c{k}_silver_exact", str(SILVER_EXACT[k]))
        wb.add_data(f"c{k}_match_pct_vs_corrected", match_pct[k])
        wb.add_data(f"c{k}_role", "applied" if k in APPLIED_RUNGS else "free")
        wb.add_data(f"c{k}_form_swing_pct", swings[k])
    wb.add_data("max_form_swing_pct", max_swing_pct)
    wb.add_data("form_anchor_stable", form_anchor_stable)
    wb.add_data("free_rungs_match_pattern", free_match)
    if pattern_breaks_at is not None:
        break_clause = (
            f"the Pell-Lucas pattern BREAKS at the first FREE rung "
            f"c_{pattern_breaks_at} (closed {mp.nstr(cf_p[pattern_breaks_at], 4)} "
            f"vs corrected {mp.nstr(corr[pattern_breaks_at], 4)})"
        )
    else:
        break_clause = (
            "the FREE rungs c_8..c_10 all matched the bias-corrected extraction "
            "(no break detected — unexpected; re-examine)"
        )
    wb.add_data("verdict", (
        "EMPIRICAL — SILVER-ANCHORED. Against PR #1824's bias-corrected q₀ "
        "extraction: the c_6/c_7 forms (which the extraction IMPOSES) are "
        f"recovered (self-consistency, {match_pct[6]:.2g}%/{match_pct[7]:.2g}%), "
        f"but {break_clause}. The forms are anchor-stable (swing "
        f"{max_swing_pct:.2e}% < 1%) and EXACT only at the silver structural "
        "anchor; they are not q₀ production coefficients. Stays empirical — "
        "silver-anchored, no production wire (§8). Falsification test; no fit, "
        "no production change."
    ))

    out = wb.save()
    print()
    n_pass = sum(1 for a in wb.assertions if a.passed)
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"{n_pass}/{len(wb.assertions)} passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
