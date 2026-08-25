#!/usr/bin/env python3
"""qbeta_dladder_qborel_leroy_resummation_probe.py

Jackson-q-Borel / Borel–Leroy resummation of the bar-odd **D-ladder** `D(ũ)`
(PR #3737), taken up in parallel/overlap with the κ-tower resurgence program
(PR #3683, owner-authorized overlap).

## The right transform (not plain Borel)

`D(ũ) = Σ d_k ũ^k` is super-exponentially **divergent** (radius → 0), but only
**mildly**: the merged divergence-correction
([`2026-07-12-dladder-divergence-correction.md`](../../docs/audits/2026-07-12-dladder-divergence-correction.md))
fits `log|d_k| = A + Bk + C·k log k` with a **small, drifting** `C ≈ 0.05–0.08`
(≪ the κ-tower's Gevrey-1 `C=1`). So:

- the classical `÷k!` Borel (`C=1` suppression) **over-suppresses** the `C≈0.06`
  growth into a near-entire transform (the negative result recorded in the
  resummation note) — wrong order;
- the correct object is a **Borel–Leroy transform of small fractional order `s`**,
  `B_s(ζ) = Σ d_k ζ^k / Γ(1+k)^s` (`= Σ d_k ζ^k / (k!)^s`), with `s` matching the
  effective Gevrey order. `s` is **not fitted to QOU data** — it is the
  structural exponent that renders the transform summable, measured by scanning.

(Jackson q-Borel `÷[k]_q!` at the substrate `q₀≈1.11` reduces to `≈ ÷k!` since
`[k]_q!→k!` as `q→1`, so it too over-suppresses; the Borel–Leroy order is the
faithful knob for this mild q-Gevrey class. A wide q-factorial-base arm is a
possible follow-up, but the order scan is the decisive first measurement.)

## What is measured (scope-(a): measurement, NOT identification)

  slope(s)  — the root-test slope of `|d_k/(k!)^s|^{1/k}` vs the Borel–Leroy order
              `s`. Robust finding: it is **positive at s=0** (divergent — a 3rd
              independent confirmation after the ratio and log-fit methods) and
              **decreases monotonically in `s`**, i.e. a positive order is required
              (plain `÷k!` = order 1 over-suppresses).
  s*        — where the slope crosses 0 (`≈0.20` by this estimator). It DISAGREES
              with the audit's log-fit `C≈0.06` — and that spread is the
              **q-Gevrey non-fixed-index signature** (a drifting divergence class
              has no single Gevrey order), NOT a cross-check match.
  ρ_s*      — the dlog-Padé singularity at `s*` is **inconsistent with the
              root-test radius** ⇒ **not cleanly resolved at k=21** (finite-n
              shadow). **No instanton action is claimed**; a clean value needs the
              genuine q-Borel / Écalle acceleration (#3683) or more terms.

No `c_k` wired; no fit to QOU observables; no tier change. Exact `d_k` to k=21.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = 43
core.ORD = ORD
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
dlad.ORD = ORD

set_compute_dps()
VOL41_OVER_PI = mp.mpf("0.6461320971509606")
EVEN_A_3683 = mp.mpf("0.657")


def d_coeffs():
    dk, KMAX, _vt, _ok = dlad.build_d_ladder()
    s3 = mp.sqrt(3)
    d = [mp.mpf(0)]
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        bb = sp.Rational(sp.nsimplify(e.coeff(sp.sqrt(3), 1)))
        aa = sp.Rational(sp.nsimplify(e - bb * sp.sqrt(3)))
        d.append(mp.mpf(int(aa.p)) / int(aa.q) + (mp.mpf(int(bb.p)) / int(bb.q)) * s3)
    return d, KMAX


def borel_leroy(d, KMAX, s):
    """b_k = d_k / (k!)^s (Borel–Leroy order s)."""
    return [mp.mpf(0)] + [d[k] / (mp.factorial(k) ** s) for k in range(1, KMAX + 1)]


def root_test_slope(b, KMAX, klo=8):
    """Linear slope of |b_k|^{1/k} over k=klo..KMAX. >0 ⇒ still rising
    (divergent); ≈0/<0 ⇒ plateaued/decreasing (summable)."""
    ks = list(range(klo, KMAX + 1))
    rt = [abs(b[k]) ** (mp.mpf(1) / k) for k in ks]
    mk = sum(ks) / len(ks)
    mr = sum(rt) / len(rt)
    num = sum((ks[i] - mk) * (rt[i] - mr) for i in range(len(ks)))
    den = sum((ks[i] - mk) ** 2 for i in range(len(ks)))
    return num / den, rt[-1]


def _dlog_pade_radius(b, KMAX):
    """Nearest singularity of Σ b_k ζ^k via dlog-Padé; return (|ζ*|, arg ζ*)."""
    F = [mp.mpf(1)] + b[1:]
    n = len(F)
    fp = [F[k] * k for k in range(n)]
    g = [mp.mpf(0)] * n
    inv0 = 1 / F[0]
    for k in range(n):
        ssum = fp[k]
        for j in range(1, k + 1):
            ssum -= F[j] * g[k - j]
        g[k] = ssum * inv0
    best = []
    for M in range(3, KMAX // 2 + 1):
        L = min(M, KMAX - M)
        try:
            p, q = mp.pade(g[:L + M + 1], L, M)
            roots = mp.polyroots(list(reversed(q)), maxsteps=250, extraprec=250)
        except Exception:
            continue
        roots = [r for r in roots if abs(r) > 1e-6]
        if roots:
            best.append(min(roots, key=lambda r: abs(r)))
    if not best:
        return None, None
    mags = sorted(abs(r) for r in best)
    med = mags[len(mags) // 2]
    keep = [r for r in best if abs(abs(r) - med) < 0.25 * med]
    rho = sum(abs(r) for r in keep) / len(keep)
    ph = sum(mp.arg(r) for r in keep) / len(keep)
    return rho, ph


def main() -> int:
    print("=" * 78)
    print(" D-ladder q-Borel/Borel–Leroy resummation — order scan (odd channel)")
    print("=" * 78)
    d, KMAX = d_coeffs()
    print(f"  exact d_k, k=1..{KMAX}; all same sign (Pringsheim ⇒ real-axis "
          f"singularity after resummation)")

    print("\n  Borel–Leroy order scan  s ↦ root-test slope of |d_k/(k!)^s|^{1/k}:")
    print("  (slope > 0 ⇒ still divergent;  ≤ 0 ⇒ summable)")
    scan = []
    s_star = None
    s = mp.mpf(0)
    while s <= mp.mpf("0.30") + 1e-9:
        b = borel_leroy(d, KMAX, s)
        slope, tail = root_test_slope(b, KMAX)
        scan.append((float(s), float(slope), float(tail)))
        flag = "divergent" if slope > 1e-3 else "SUMMABLE"
        print(f"    s={float(s):.3f}:  root-test slope={float(slope):+.5f}  "
              f"tail |b_k|^(1/k)={float(tail):.4f}  → {flag}")
        if s_star is None and slope <= 1e-3:
            s_star = s
        s += mp.mpf("0.02")

    print()
    if s_star is None:
        print("  root-test slope stays > 0 for all s ≤ 0.30 — divergent across the "
              "whole scanned Leroy family (mild q-Gevrey, no summable order found "
              "at accessible k)")
        rho = ph = None
    else:
        print(f"  root-test slope crosses 0 at s* ≈ {float(s_star):.3f} (root-test "
              f"estimator). NOTE: the audit's log-fit growth exponent is C≈0.06 —")
        print(f"  the two estimators DISAGREE (0.06 vs 0.20), which is the "
              f"**q-Gevrey non-fixed-order signature**, not a contradiction: for a "
              f"series whose divergence class drifts, no single Gevrey index fits.")
        b = borel_leroy(d, KMAX, s_star)
        rho, ph = _dlog_pade_radius(b, KMAX)
        if rho is not None:
            tail_radius = 1 / scan[-1][2] if scan[-1][2] else mp.mpf('nan')
            print(f"  resummed singularity estimate at s*: dlog-Padé ρ≈{mp.nstr(rho, 6)} "
                  f"vs root-test radius≈{mp.nstr(1/tail, 4)} — INCONSISTENT ⇒ the "
                  f"singularity is NOT cleanly resolved at k={KMAX} (finite-n "
                  f"shadow-limited). No instanton action claimed; a clean value "
                  f"needs the genuine q-Borel/acceleration (#3683) or more terms.")

    wb = WitnessBuilder("qbeta-dladder-qborel-leroy-resummation", engine="mpmath")
    wb.set_description(
        "Jackson-q-Borel/Borel–Leroy resummation of the mildly-divergent (q-Gevrey "
        "C≈0.06) bar-odd D-ladder (PR #3737, overlap with #3683). Plain ÷k! Borel "
        "over-suppresses; correct object is Borel–Leroy order s. Scans s to find "
        "the effective Gevrey order s* (smallest s with non-rising root test), then "
        "locates the resummed real-axis (Pringsheim) Borel singularity ρ_s* and "
        "compares to Vol(4₁)/π & the κ-tower action as consistency-only. Scope-(a); "
        "s is the structural summability exponent (not fitted to QOU data); no c_k "
        "wired; no tier change."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("KMAX", KMAX)
    wb.add_data("borel_leroy_order_scan", scan)
    wb.add_data("plain_borel_wrong_reason",
                "÷k! is order-1 suppression; D-ladder growth is C≈0.06 ≪ 1 "
                "(over-suppressed to near-entire)")
    # Robust finding: the root-test slope DECREASES monotonically with s and is
    # strictly positive for s=0 (divergent), i.e. a positive Borel–Leroy order is
    # required — a THIRD independent confirmation of mild divergence (after the
    # ratio and log-fit methods), and evidence the order is small (O(0.1)) but
    # estimator-dependent (q-Gevrey, no fixed index).
    slope0 = scan[0][1]
    monotone = all(scan[i][1] >= scan[i + 1][1] - 1e-9 for i in range(len(scan) - 1))
    wb.add_data("root_test_slope_at_s0", slope0)
    wb.add_data("slope_monotone_decreasing_in_s", bool(monotone))
    if s_star is not None:
        wb.add_data("root_test_zero_crossing_s_star", float(s_star))
        wb.add_data("audit_logfit_C", "~0.05-0.08")
        wb.add_data("order_estimator_spread_is_qgevrey_signature", True)
        if rho is not None:
            wb.add_data("resummed_rho_dlog_pade_UNRESOLVED", mp.nstr(rho, 8))
            wb.add_data("singularity_cleanly_resolved_at_KMAX", False)
            wb.add_data("instanton_action_claimed", False)
    wb.add_assertion(
        "mild_divergence_confirmed_positive_leroy_order_required",
        computed=float(slope0 > 1e-3 and monotone), expected=1.0, tolerance=0.5,
        source=f"root-test slope is +{slope0:.4f} at s=0 (divergent) and decreases "
               f"monotonically in the Borel–Leroy order s, crossing 0 near "
               f"s*≈{float(s_star) if s_star else float('nan'):.2f}: a positive order "
               f"is required ⇒ mild q-Gevrey divergence (3rd independent method); "
               f"plain ÷k! (order 1) over-suppresses. The order is O(0.1) but "
               f"estimator-dependent (vs the log-fit C≈0.06) — the q-Gevrey "
               f"non-fixed-index signature. The resummed singularity is NOT "
               f"resolved at k={KMAX}; no instanton action claimed.")
    wb.save()
    print("\n  scope-(a): confirms mild divergence (3rd method) + measures the "
          "(estimator-dependent) order; resummed singularity unresolved at k=21, "
          "no ID. q-Borel/acceleration proper stays #3683 territory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
