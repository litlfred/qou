#!/usr/bin/env python3
"""
qbeta_dladder_parity_split_arithmetic_normalized_probe.py — W9 first increment: the two
proved arithmetic gradings as CHANNEL SPLITTERS for the D-ladder's divergence class
(1ppq reassessment Option 1; bean qou-dri7; complements Track 1 of the three-front attack).

Context. The bar-odd D-ladder d_k = a_k + b_k·√3 (exact, k ≤ 21 at default ORD) is
super-exponentially divergent with NO single Gevrey index — the log-fit gives C ≈ 0.06
while the Borel–Leroy zero-crossing gives s* ≈ 0.20, and the drift is the corpus's
q-Gevrey signature (2026-07-13 D-ladder audit; third confirmation by the Leroy scan).
Every estimator so far ran on the MIXED ladder. But the corpus has PROVED two arithmetic
gradings on d_k:

  (G2) the 2-adic bar-parity grading — v₂(den b_k) = 0 ⟺ k odd (2 the unique graded
       prime, Lean-anchored);
  (G3) the 3-adic denominator growth — v₃(den d_k) ~ 1.5·k (Ohtsuki–Habiro 3-smoothness,
       NOT parity-graded).

Hypothesis (fit-free, decided here): the "no single Gevrey index" drift of the mixed
ladder is (at least partly) the superposition artifact of arithmetically distinct
channels/scales — the same mixed-scale mechanism the binding-side analysis exhibited
(e^{√n} sub-scale inside Gevrey-1/2, merged #3694). Two decidable splits, neither run by
Track 1 (which extends k with the SAME mixed estimators) nor #3683 (even channel):

  E1  PARITY SPLIT (from G2): local Gevrey index C_k = Δln|d_k|/Δln k! measured WITHIN
      each parity channel (step-2 differences, no cross-parity mixing).
  E2  ARITHMETIC NORMALIZATION (from G3): e_k = d_k · 3^{v₃(den d_k)} — multiply out the
      exact 3-power denominator (the proved ~1.5k structure) and re-measure the local
      index of |e_k| (numerator-scale growth vs denominator-scale artifact).

Outputs the local-index tables + drift statistics per channel/normalization vs mixed.
Scope-(a): no instanton action claimed (k ≤ 21 cannot resolve the singularity — the
07-13 audit's honest boundary stands); no c_k value, no wiring, no tier change; the
c₃ flip-flop discipline untouched. Anti-fit: both splits are forced by PROVED gradings,
not chosen post-hoc.

Audit: docs/audits/2026-07-17-dladder-parity-split-arithmetic-normalized.md
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE), str(HERE.parent), str(HERE.parent / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import _path_bridge as _pb  # noqa: E402, F401
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402

import mpmath as mp  # noqa: E402
mp.mp.dps = 60


def _vp(x, p):
    """p-adic valuation of a sympy Rational's denominator (0 for integers)."""
    d = int(sp.Rational(x).q)
    v = 0
    while d % p == 0:
        d //= p
        v += 1
    return v


def local_index(ks, vals):
    """local Gevrey index C_k between consecutive listed k: Δln|v| / Δln k!."""
    out = {}
    for (k1, v1), (k2, v2) in zip(list(zip(ks, vals))[:-1], list(zip(ks, vals))[1:]):
        num = mp.log(abs(v2)) - mp.log(abs(v1))
        den = mp.log(mp.factorial(k2)) - mp.log(mp.factorial(k1))
        out[k2] = float(num / den)
    return out


def drift(d):
    vs = [d[k] for k in sorted(d)][2:]  # drop the first two (transient)
    return max(vs) - min(vs) if vs else float('nan')


def main() -> int:
    print("=== W9: parity-split + 3-adic-normalized D-ladder estimators ===\n")
    dk, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    assert odd_ok, "odd-order residuals must vanish (build_d_ladder over-determination)"
    data = []
    for k in sorted(dk):
        e = sp.expand(sp.nsimplify(dk[k]))
        a = sp.Rational(e.coeff(sp.sqrt(3), 0))
        b = sp.Rational(e.coeff(sp.sqrt(3), 1))
        val = mp.mpf(int(a.p)) / int(a.q) + (mp.mpf(int(b.p)) / int(b.q)) * mp.sqrt(3)
        data.append((k, a, b, val))
    data.sort()
    ks = [k for k, *_ in data]
    kmax = ks[-1]
    print(f"exact d_k loaded: k = {ks[0]}..{kmax} ({len(data)} rungs)")

    # sanity: G2 (2-adic parity grading) reproduced on this data
    g2 = all((_vp(b, 2) == 0) == (k % 2 == 1) for k, a, b, v in data if k >= 2 and b != 0)
    # G3: v3 grows on both parities
    v3 = {k: max(_vp(a, 3), _vp(b, 3)) for k, a, b, v in data}
    g3_slope = (v3[kmax] - v3[ks[0]]) / (kmax - ks[0])
    print(f"G2 parity grading reproduced: {'PASS' if g2 else 'FAIL'}; "
          f"G3 v₃ slope ≈ {g3_slope:.2f} (audit: ~1.5)")

    # mixed control
    mixed = local_index(ks, [v for *_, v in data])
    # E1: parity split
    odd = [(k, v) for k, a, b, v in data if k % 2 == 1]
    even = [(k, v) for k, a, b, v in data if k % 2 == 0]
    ci_odd = local_index([k for k, _ in odd], [v for _, v in odd])
    ci_even = local_index([k for k, _ in even], [v for _, v in even])
    # E2: 3-adic normalization
    e_norm = [(k, v * mp.mpf(3) ** v3[k]) for k, a, b, v in data]
    ci_norm = local_index([k for k, _ in e_norm], [v for _, v in e_norm])
    # E1+E2 combined
    no3 = {k: v * mp.mpf(3) ** v3[k] for k, a, b, v in data}
    ci_norm_odd = local_index([k for k, _ in odd], [no3[k] for k, _ in odd])
    ci_norm_even = local_index([k for k, _ in even], [no3[k] for k, _ in even])

    print(f"\n  {'k':>3} {'mixed C_k':>10} {'odd-ch':>8} {'even-ch':>8} "
          f"{'3-norm':>8} {'3norm-odd':>10} {'3norm-even':>10}")
    for k in ks[2:]:
        row = [mixed.get(k), ci_odd.get(k), ci_even.get(k), ci_norm.get(k),
               ci_norm_odd.get(k), ci_norm_even.get(k)]
        print(f"  {k:>3} " + " ".join(f"{v:>8.3f}" if isinstance(v, float) else " " * 8
                                       for v in row))

    drifts = {"mixed": drift(mixed), "odd": drift(ci_odd), "even": drift(ci_even),
              "norm3": drift(ci_norm), "norm3_odd": drift(ci_norm_odd),
              "norm3_even": drift(ci_norm_even)}
    print("\n  local-index drift (max−min over the stable window):")
    for name, v in drifts.items():
        print(f"    {name:>10}: {v:.3f}")
    best = min((v, n) for n, v in drifts.items())
    stabilized = best[1] != "mixed" and best[0] < 0.5 * drifts["mixed"]
    print(f"\n  ⇒ best channel: {best[1]} (drift {best[0]:.3f} vs mixed "
          f"{drifts['mixed']:.3f}) — "
          f"{'SPLIT RESOLVES ≥half the drift (superposition mechanism supported)' if stabilized else 'no split halves the drift at k≤21 (drift is not explained by these gradings alone at accessible order)'}")

    ok = g2 and len(data) >= 15
    print(f"\n### Probe integrity: {'PASS' if ok else 'FAIL'} (finding recorded as data, "
          f"scope-(a); no action claimed)")

    wb = WitnessBuilder("qbeta-dladder-parity-split-arithmetic-normalized", engine="sympy+mpmath")
    wb.set_description(
        "W9 first increment (1ppq Option 1, bean qou-dri7): the two PROVED arithmetic "
        "gradings of the bar-odd D-ladder (2-adic bar-parity; 3-adic ~1.5k denominator "
        "growth) used as channel splitters / normalizers for the divergence-class "
        "estimators, on the exact k<=21 rungs. Complements Track 1 (extension, same mixed "
        "estimators) and #3683 (even channel). Local Gevrey-index tables per channel "
        "(parity-split, 3-power-normalized, combined) vs mixed control + drift stats; "
        "decides whether the 'no single Gevrey index' drift is a superposition artifact "
        "of the arithmetic channels at accessible order. Fit-free (splits forced by "
        "proved gradings); no instanton action claimed; no c_k value; no wiring; "
        "scope-(a).")
    wb.add_data("k_range", [ks[0], kmax])
    wb.add_data("g2_parity_reproduced", bool(g2))
    wb.add_data("g3_v3_slope", float(g3_slope))
    wb.add_data("local_index_mixed", {str(k): v for k, v in mixed.items()})
    wb.add_data("local_index_odd", {str(k): v for k, v in ci_odd.items()})
    wb.add_data("local_index_even", {str(k): v for k, v in ci_even.items()})
    wb.add_data("local_index_norm3", {str(k): v for k, v in ci_norm.items()})
    wb.add_data("local_index_norm3_odd", {str(k): v for k, v in ci_norm_odd.items()})
    wb.add_data("local_index_norm3_even", {str(k): v for k, v in ci_norm_even.items()})
    wb.add_data("drifts", drifts)
    wb.add_data("best_channel", best[1])
    wb.add_data("split_resolves_half_drift", bool(stabilized))
    wb.add_assertion(
        name="parity_split_arithmetic_normalized_estimators_computed",
        computed=str(int(ok)), expected="1", tolerance=0,
        source=("exact d_k k=%d..%d; G2 parity grading reproduced; per-channel local "
                "Gevrey-index tables computed (drifts: %s); finding: best channel %s, "
                "halves-mixed-drift=%s. Scope-(a), fit-free, nothing wired."
                % (ks[0], kmax, {n: round(v, 3) for n, v in drifts.items()},
                   best[1], stabilized)))
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
