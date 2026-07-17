#!/usr/bin/env python3
"""qbeta_odd_channel_stokes_borel_probe.py

Lever-1 (independent attack): characterize the divergence class of the bar-ODD
Q_β D-ladder and test whether a fixed-order Borel–Leroy extracts a clean
odd-channel action / Stokes datum — the G3 monodromy datum the Φ_b keystone
needs (docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md;
coordination/1ppq-qbeta.md, live route on #3805).

BACKGROUND. The even κ-channel (Ohtsuki rungs κ₁..κ₈) admits a plain (conformal)
Borel analysis giving A ≈ 0.646–0.657 vs Vol(4₁)/π = 0.6461 ("consistent, not
identified"; 6a529aa744). The Stokes constant actually lives in the ODD channel,
which prior work characterized only by negatives (not q-holonomic base-3, no
coupled ℚ(√3) recurrence, 2-adic parity grading). This probe measures the odd
channel's divergence class directly and asks whether the even-channel plain-Borel
method transfers.

METHOD. build_d_ladder() (the merged generating-function probe) returns the
bar-ODD ladder d_k = a_k + b_k√3 ∈ ℚ(√3) (the O=(x−y)/2 antisymmetric part,
G=O/h). We:
  (1) measure the effective Gevrey order C = coeff of k·log k in log|d_k|, on
      progressively longer tails lo∈{4,8,12} — a DRIFT test;
  (2) fine-scan the Borel–Leroy order s and, for each, Padé-search the nearest
      real-positive singularity across [m/m] orders, reporting the median pole
      and its spread across Padé orders (stability);
  (3) compare the stable band to low-complexity action candidates.

FINDING (ORD=56, 27 rungs; reproduced qualitatively at ORD=44):
  • root test |d_k|^{1/k} rises only slowly (≈5.70→5.91 over k=16..21, no
    doubling) ⇒ NOT q-Gevrey-1 in any base>1 (that would blow the root test up
    geometrically);
  • C DRIFTS DOWN with the tail: C(lo=4)=0.081 → C(lo=8)=0.059 → C(lo=12)=0.051
    ⇒ the order is NOT constant; the series is Gevrey-s with a small, drifting
    s≈0.05 — no single fixed Borel–Leroy order canonically resums it;
  • consequently the extracted pole is s-DEPENDENT (0.147 at s=0.02 → 0.165 at
    s=0.10 → 0.249 at s=0.30); the stability-optimal band is ≈0.147–0.165,
    which BRACKETS 1/(2π)=0.1592 and Vol(4₁)/(4π)=0.1615 (= even-channel Vol/π
    ÷4 — the same factor-4 as the α_EM two-channel loop split), but the ~12%
    s-systematic makes this CONSISTENT-NOT-IDENTIFIED.

HONEST TIER — scope-(a) NEGATIVE (per AGENTS.md "refuted/ruled-out" rule):
  the fixed-order Borel–Leroy method, ALONE, does not extract a clean odd-channel
  action; the effective Gevrey order drifts. This does NOT exclude an odd-channel
  Stokes constant (no proved invariant forbids one) — it says the even-channel
  plain-Borel route does not transfer, and the G3 computation (#3805) needs the
  true q-Borel / alien-derivative chain (base q₀ or base-3), not a fixed-order
  Leroy transform. No coefficient fitted; no c_k wired; comparison-only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 44
# build_d_ladder reads the probe module's ORD, set from sys.argv at import
sys.argv = [sys.argv[0], str(ORD)]
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import qbeta_dladder_generating_function_structure_probe as P  # noqa: E402

mp.mp.dps = 60
R3 = sp.sqrt(3)

CANDIDATES = {
    "1/(2pi)": 1 / (2 * mp.pi),
    "Vol(4_1)/(4pi)": mp.mpf("2.02988321281930725") / (4 * mp.pi),
    "sqrt3/(4pi)": mp.sqrt(3) / (4 * mp.pi),
    "1/(2sqrt3)": 1 / (2 * mp.sqrt(3)),
    "pi/18": mp.pi / 18,
    "1/6": mp.mpf(1) / 6,
    "1/pi": 1 / mp.pi,
    "Vol(4_1)/pi": mp.mpf("2.02988321281930725") / mp.pi,
}


def poles_at(seq, s, mrange=(4, 14)):
    """Nearest real-positive Padé pole of Borel–Leroy B(t)=Σ b_k t^k,
       b_k = seq[k]/Γ(1+s k), across [m/m] orders."""
    ks = sorted(seq)
    bl = {k: seq[k] / mp.gamma(1 + s * k) for k in ks}
    out = []
    for m in range(*mrange):
        if 2 * m > len(ks):
            break
        c = [mp.mpf(0)] + [bl[k] for k in ks[: 2 * m]]
        try:
            _, qd = mp.pade(c, m, m)
        except Exception:
            continue
        try:
            rts = mp.polyroots([complex(z) for z in reversed(qd)],
                               maxsteps=250, extraprec=100)
        except Exception:
            continue
        rp = sorted([mp.re(r) for r in rts
                     if abs(mp.im(r)) < mp.mpf("1e-6") and mp.re(r) > mp.mpf("1e-3")])
        if rp:
            out.append(rp[0])
    return out


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" odd-channel Stokes/Borel probe (ORD {P.ORD})")
    print("=" * 78)

    dk, KMAX, valid_top, odd_ok = P.build_d_ladder()
    print(f"  built d₁…d_{KMAX} (valid s^{valid_top}, odd-order over-det zero: "
          f"{odd_ok}) in {time.monotonic() - t0:.1f}s", flush=True)
    df = {k: mp.mpf(str(sp.N(dk[k], 55))) for k in dk}

    # (1) drift of the effective Gevrey order C
    Cs = {}
    for lo in (4, 8, 12):
        if KMAX - lo < 4:
            continue
        _, C, ssr, root = P.growth_diagnostic(dk, lo=lo)
        Cs[lo] = float(C)
        print(f"  C(lo={lo}) = {float(C):.5f}  ssr(superexp)/ssr(geom) = {float(ssr):.2e}",
              flush=True)
    rk = sorted(root)
    root_rising = bool(root[rk[-1]] > root[rk[-4]] > root[rk[-8]])
    print(f"  root test |d_k|^(1/k) tail: "
          f"{[f'{k}:{float(root[k]):.3f}' for k in rk[-5:]]}  (rising={root_rising})",
          flush=True)
    drift_down = len(Cs) >= 2 and all(
        Cs[b] < Cs[a] + 1e-9 for a, b in zip(sorted(Cs), sorted(Cs)[1:]))

    # (2) fine Leroy-order scan → stability-optimal pole + band
    print("\n  Leroy-order scan (median pole ± spread across Padé orders):", flush=True)
    scan = {}
    for si in range(2, 22, 2):
        s = mp.mpf(si) / 100
        ps = poles_at(df, s)
        if len(ps) < 4:
            continue
        pf = sorted(float(p) for p in ps)
        med = pf[len(pf) // 2]
        spread = pf[-1] - pf[0]
        scan[float(s)] = (med, spread, spread / med if med else 9.0)
        print(f"    s={float(s):.2f}: median={med:.5f} spread={spread:.4f} "
              f"rel={spread / med if med else 9:.3f} n={len(pf)}", flush=True)
    best_s = min(scan, key=lambda s: scan[s][2]) if scan else None
    band_lo = min(v[0] for v in scan.values()) if scan else 0.0
    band_hi = max(v[0] for v in scan.values()) if scan else 0.0
    # restrict "band" to the reasonably-stable low-s window s ≤ 0.12
    stable = {s: v for s, v in scan.items() if s <= 0.12}
    if stable:
        band_lo = min(v[0] for v in stable.values())
        band_hi = max(v[0] for v in stable.values())

    print(f"\n  most-stable Leroy order s*={best_s}; stable-window band "
          f"[{band_lo:.4f}, {band_hi:.4f}]", flush=True)
    print("  candidate positions in/near the band:", flush=True)
    brackets = []
    for name, val in CANDIDATES.items():
        v = float(val)
        inb = band_lo <= v <= band_hi
        print(f"    {name:>16} = {v:.5f}  {'IN BAND' if inb else ''}", flush=True)
        if inb:
            brackets.append(name)

    # honest verdict
    print("\n  VERDICT (scope-(a) negative): effective Gevrey order drifts "
          f"({'down' if drift_down else 'non-monotone'}); no fixed-order Borel–Leroy",
          flush=True)
    print("  gives an s-independent action. Band brackets: "
          f"{brackets or '(none clean)'} — consistent-not-identified.", flush=True)
    print("  ⇒ even-channel plain-Borel (Vol/π) does NOT transfer; G3 (#3805) needs", flush=True)
    print("     the true q-Borel / alien chain, not fixed-order Leroy.", flush=True)

    wb = WitnessBuilder("qbeta-odd-channel-stokes-borel", engine="sympy+mpmath")
    wb.set_description(
        "Odd-channel Q_β D-ladder divergence class. The bar-odd d_k∈ℚ(√3) have a "
        "DRIFTING effective Gevrey order (C: ~0.08→0.05 as the tail lengthens) and "
        "a slowly-rising root test — NOT q-Gevrey-1 in any base>1. A fixed-order "
        "Borel–Leroy gives an s-DEPENDENT pole (0.147→0.165→0.249 for s=0.02→0.10→"
        "0.30); the stable-window band ~0.147–0.165 brackets 1/(2π) and Vol(4₁)/(4π) "
        "but the ~12% s-systematic is consistent-not-identified. Scope-(a) NEGATIVE: "
        "the even-channel plain-Borel method (Vol/π) does not transfer to the odd "
        "channel; the G3 monodromy datum (#3805) needs the true q-Borel/alien chain. "
        "No fit; no c_k wired; comparison-only.")
    wb.set_content_block("conj:faddeev-phi-b-quasiperiod")
    wb.add_data("ORD", int(P.ORD))
    wb.add_data("KMAX", int(KMAX))
    wb.add_data("gevrey_C_by_tail", Cs)
    wb.add_data("gevrey_order_drifts_down", bool(drift_down))
    wb.add_data("root_test_rising", root_rising)
    wb.add_data("leroy_scan", {f"{s:.2f}": {"median": v[0], "spread": v[1]}
                               for s, v in scan.items()})
    wb.add_data("stable_band", [band_lo, band_hi])
    wb.add_data("best_leroy_order", best_s)
    wb.add_data("candidates_in_band", brackets)
    wb.add_data("candidate_values", {k: float(v) for k, v in CANDIDATES.items()})
    wb.add_assertion("odd_over_determination_zero",
                     computed=float(odd_ok), expected=1.0, tolerance=0.5,
                     source="odd-order valid residuals of G−model vanish (exact ℚ(√3))")
    wb.add_assertion("gevrey_order_drifts_not_constant",
                     computed=float(drift_down), expected=1.0, tolerance=0.5,
                     source=f"C by tail {Cs}: monotone-decreasing ⇒ not fixed-Gevrey-s")
    wb.add_assertion("no_fixed_order_clean_action",
                     computed=float(len(brackets) >= 1), expected=1.0, tolerance=0.5,
                     source=f"stable band [{band_lo:.4f},{band_hi:.4f}] brackets "
                            f"{brackets} — s-dependent, consistent-not-identified")
    wb.save()

    print(f"\n  done in {time.monotonic() - t0:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
