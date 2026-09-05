#!/usr/bin/env python3
"""magnus_tworow_column_true_element_probe.py — the rescoped bean, first measurement. (qou-o6ov)

WHY THIS IS NOW THE WHOLE PROBLEM. Under convention D (owner ruling 2026-08-09) `y_λ = 0` for
`ℓ(λ) > 2`, so `P(A) = Σ_λ y_λ tr(ρ_λ Ω₂^P)` runs over **≤2-row shapes only** — exactly
`⌊n/2⌋+1` of them, measured at n = 3…12 (#6822). The two-row column used to be one handle among
several (hooks via reduced Burau, sl₃/Kostka, the κ decomposition); it is now the entire object,
and everything off it carries weight zero.

That also makes it cheap. The ≤2-row shapes `(n−k, k)` have small dimensions — at n=12 the largest
is `(7,5)` at 297, against 792 for `(4,3,3,2)` in the full census — so the complete column at
A = 2, 3, 4 costs less than a single level of the old full census.

WHAT IS BEING ASKED, and it is narrower than the bean's original claim. Does

    |tr_{(n−k,k)}(ρ · Ω₂^P)| / dim_{(n−k,k)}

decay in `k = b(λ)`? The full-census envelope does **not** decay for the true element (#6822: it
peaks at b=3, total range 2.41× against the braid's 1427×), so the surviving statement has to be
made on this column or not at all.

THE CORRECTION THIS PROBE CARRIES, which every pre-#6822 number in the arc lacks. `ρ` is the
**Hecke element**, not a braid: `atom_braid_word_3A` returns triples `(c, d, g)` denoting
`c·σ_g + d·1`, and the arc's `[int(t[2]) for t in ...]` applied a bare `σ_g` — the wrong operator
for 19 of 35 letters (54 %) at A=3. Both elements are computed here so the column can be compared
directly rather than across sessions.

ALREADY VISIBLE AT n=9 (from #6822's census), and it is why this probe exists:

    k:            0        1         2          3          4
    ρ_true:     0.0    1.7705    0.17667    0.048021   0.067981   <- rises at the LAST entry
    ρ_bare:     0.0   29.001     3.7573     1.0488     0.18386    <- monotone

So the true element already fails monotonicity on the column at n=9, at the squarest shape. This
probe establishes whether that is an n=9 accident or systematic, by measuring A = 2, 3, 4.

Reports both `|tr|/dim` and the y-weighted mass `|c_λ| = y_λ·|tr|` — the second is what the sum
actually weights by, and #6822 measured it monotone where `|tr|/dim` was not, so the two must be
reported separately.

SCOPE — (a) scope-limited, three sizes at one q₀. Measures; proves nothing.
NO-FLOAT64: mpf end to end, dps 65, `_assert_dps` guard, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from magnus_true_hecke_element_probe import sweep, classify  # noqa: E402
import magnus_true_hecke_element_probe as TE  # noqa: E402


def _qint(m, q):
    """[m]_q = (q^m − q^−m)/(q − q^−1), mpf throughout. [0]_q = 0, [1]_q = 1."""
    if m == 0:
        return mp.mpf(0)
    return (q ** m - q ** (-m)) / (q - 1 / q)


def two_row_shapes(n):
    """(n−k, k) for k = 0 … ⌊n/2⌋ — exactly the shapes carrying nonzero y_λ under convention D."""
    out = []
    for k in range(n // 2 + 1):
        out.append((n - k,) if k == 0 else (n - k, k))
    return out


def monotone_report(name, ks, vals):
    """Say WHERE it breaks, not just whether — a bare False hides which shape is anomalous."""
    breaks = [(ks[i + 1], vals[i], vals[i + 1])
              for i in range(len(vals) - 1) if vals[i + 1] > vals[i]]
    if not breaks:
        return f"    {name}: strictly decreasing in k  ✓"
    lines = [f"    {name}: NOT decreasing — {len(breaks)} rise(s) ✗"]
    for k, lo, hi in breaks:
        lines.append(f"        at k={k}:  {mp.nstr(lo, 7)}  ->  {mp.nstr(hi, 7)}"
                     f"   (×{mp.nstr(hi / lo, 4) if lo > 0 else 'inf'})")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3, 4])
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps            # AFTER imports (#6710 trap)
    TE._WANT_DPS = args.dps

    q = base.Q0
    print("[2rowcol] Under convention D the <=2-row column IS the sum (y_lam = 0 off it).")
    print("[2rowcol] Does |tr_(n-k,k)(rho.Om2^P)|/dim decay in k, for the TRUE Hecke element?")
    print(f"[2rowcol] rho_bare = bare sigma_g per letter (the whole pre-#6822 arc); "
          f"rho_true = c*sigma_g + d*1.  (dps={args.dps})")

    for A in args.A:
        n = 3 * A
        Z, N = A // 2, A - A // 2
        word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
        ngen = max(g for _c, _d, g in word) + 1
        ns, ni, na = classify(word, q)
        # y_lambda_at() sets mp.mp.dps INTERNALLY (measured: it leaves it at 50). That is the
        # #6710 trap in its live form — the _assert_dps guard in sweep() caught it here rather
        # than letting the column be computed at an unrequested precision. Restore immediately;
        # do not move this call below the sweeps and assume it is inert.
        yl = y_lambda_at(n, q)
        mp.mp.dps = args.dps

        print(f"\n{'=' * 78}\n  A={A}  (n={n}) — {len(word)} letters: "
              f"σ {ns}, σ⁻¹ {ni}, averaged {na}  ⇒ bare form wrong on {ni + na}")
        shapes = two_row_shapes(n)
        print(f"  {len(shapes)} two-row shapes = floor(n/2)+1; full census is p({n}) partitions\n")
        print(f"  {'k':>3}  {'λ':<12}{'dim':>6}{'|tr|/dim BARE':>16}{'|tr|/dim TRUE':>16}"
              f"{'y_λ':>13}{'|c_λ| TRUE':>14}")

        ks, vb, vt, cb, ct = [], [], [], [], []
        for k, lam in enumerate(shapes):
            tb, _fb, dim = sweep(lam, word, q, ngen, true_coeffs=False)
            tt, _ft, _ = sweep(lam, word, q, ngen, true_coeffs=True)
            ab, at = abs(tb) / dim, abs(tt) / dim
            y = yl.get(lam)
            y = abs(mp.mpf(str(y))) if y is not None else mp.mpf(0)
            ks.append(k); vb.append(ab); vt.append(at)
            cb.append(y * abs(tb)); ct.append(y * abs(tt))
            print(f"  {k:>3}  {str(lam):<12}{dim:>6}{mp.nstr(ab, 7):>16}{mp.nstr(at, 7):>16}"
                  f"{mp.nstr(y, 6):>13}{mp.nstr(y * abs(tt), 7):>14}")

        # k=0 is the trivial rep, where Ω₂ vanishes identically (#6387, Lean sorry-free).
        # It is a proved zero, not a data point about decay, so monotonicity is asked from k=1.
        print(f"\n  MONOTONICITY in k, from k=1 (k=0 is the proved trivial-rep zero, #6387):")
        print(monotone_report("|tr|/dim  BARE", ks[1:], vb[1:]))
        print(monotone_report("|tr|/dim  TRUE", ks[1:], vt[1:]))
        print(monotone_report("y-weighted |c_λ| BARE", ks[1:], cb[1:]))
        print(monotone_report("y-weighted |c_λ| TRUE", ks[1:], ct[1:]))

        # WHERE THE DECAY ACTUALLY LIVES. If |tr|/dim rises at some k while the y-weighted mass
        # falls, the y-weight is carrying the decay. Quantify it: the product decreases exactly
        # when the weight ratio y_k/y_{k+1} exceeds the trace rise. The MARGIN between them is
        # the quantity a proof would have to bound, and it is a ratio of two things we can get
        # at separately — y_λ has a closed form (SU(2) q-dimensions), the trace does not.
        print("\n  MARGIN at each k where |tr|/dim RISES (TRUE element):")
        any_margin = False
        for i in range(1, len(vt) - 1):
            if vt[i + 1] > vt[i] and vt[i] > 0:
                any_margin = True
                trace_rise = vt[i + 1] / vt[i]
                yk = yl.get(shapes[i]); yk1 = yl.get(shapes[i + 1])
                yk = abs(mp.mpf(str(yk))) if yk is not None else mp.mpf(0)
                yk1 = abs(mp.mpf(str(yk1))) if yk1 is not None else mp.mpf(0)
                if yk1 > 0:
                    wr = yk / yk1
                    print(f"    k={i}->{i + 1}:  trace rises ×{mp.nstr(trace_rise, 5)},  "
                          f"y falls ×{mp.nstr(wr, 5)}  ⇒  margin ×{mp.nstr(wr / trace_rise, 5)}"
                          f"  ({'weight WINS' if wr > trace_rise else 'weight LOSES'})")
        if not any_margin:
            print("    (none — |tr|/dim does not rise on this column)")

        # THE WEIGHT RATIO IN CLOSED FORM, and it is the point. Under convention D the two-row
        # y_λ are SU(2) quantum dimensions, so the shape (n−k, k) carries q-dimension
        # [n−2k+1]_q and the ratio between adjacent k should be exactly
        #
        #       y_k / y_{k+1}  =  [n−2k+1]_q / [n−2k−1]_q
        #
        # CHECKED here rather than assumed — if it holds, the protection against a trace bump is
        # an explicit q-integer ratio with no dependence on ρ at all, which is what makes the
        # rescoped question tractable: bound the trace rise, and the weight side is already known.
        print("\n  WEIGHT RATIO vs the closed form [n−2k+1]_q/[n−2k−1]_q (SU(2) q-dimensions):")
        print(f"    {'k→k+1':>8}{'measured y_k/y_k+1':>22}{'[n−2k+1]/[n−2k−1]':>21}{'rel':>12}")
        for i in range(0, len(shapes) - 1):
            yk = yl.get(shapes[i]); yk1 = yl.get(shapes[i + 1])
            yk = abs(mp.mpf(str(yk))) if yk is not None else mp.mpf(0)
            yk1 = abs(mp.mpf(str(yk1))) if yk1 is not None else mp.mpf(0)
            if yk1 == 0:
                continue
            meas = yk / yk1
            cf = base.q_int(n - 2 * i + 1, q) / base.q_int(n - 2 * i - 1, q) \
                if hasattr(base, "q_int") else _qint(n - 2 * i + 1, q) / _qint(n - 2 * i - 1, q)
            rel = abs(meas - cf) / cf
            print(f"    {str(i) + '→' + str(i + 1):>8}{mp.nstr(meas, 12):>22}"
                  f"{mp.nstr(cf, 12):>21}{mp.nstr(rel, 3):>12}")
        print("    NOTE the profile: the ratio is LARGEST at the square end (k → ⌊n/2⌋) and falls")
        print("    toward q² at the long end — so the weight protection is strongest exactly where")
        print("    the trace bump occurs. That is not a coincidence to wave at; it is the thing to")
        print("    prove against.")

        tb_, tt_ = sum(cb), sum(ct)
        if tt_ > 0:
            print(f"\n  mass share at k=1:   BARE {mp.nstr(100 * cb[1] / tb_, 5)} %"
                  f"    TRUE {mp.nstr(100 * ct[1] / tt_, 5)} %")
            rng_b = max(vb[1:]) / min(vb[1:]) if min(vb[1:]) > 0 else mp.inf
            rng_t = max(vt[1:]) / min(vt[1:]) if min(vt[1:]) > 0 else mp.inf
            print(f"  |tr|/dim range k>=1: BARE {mp.nstr(rng_b, 6)}×"
                  f"      TRUE {mp.nstr(rng_t, 6)}×")

    print(f"\n{'=' * 78}")
    print("  A rise in the TRUE column at the squarest shape, repeated across A, would mean the")
    print("  rescoped claim needs stating on k <= k_max(n) rather than on the whole column — or")
    print("  on the y-weighted mass, which weights the square end down by y_λ.")


if __name__ == "__main__":
    main()
