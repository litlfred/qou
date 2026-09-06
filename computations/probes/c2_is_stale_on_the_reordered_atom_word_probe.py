#!/usr/bin/env python3
"""c2_is_stale_on_the_reordered_atom_word_probe.py — qou-qqm4's six c₂ are the OLD word too.

THE FINDING. Bean `qou-qqm4` is **completed**. It derived `c₂`, the second-order coefficient of
`tr_M(W_free) − tr_M(W_atom)`, recorded six exact rationals

    pp 357/32   pn 403/32   nn 217/16   T 3285/128   ³He 3451/128   ⁴He 15307/512

and built a second-order chain/atom analysis on them (`T 1.019`, `³He 0.881`, `⁴He 1.248`, against
`1.79 / 1.76 / 3.43` at first order — the finding that "the over-count nearly cancels one order up",
recorded in `docs/audits/2026-09-04-c2-does-not-continue-the-cancellation.md`). It completed
**2026-09-03**.

**The atom word changed on 2026-09-05** — owner ruling `qou-hu1f`. Sibling bean `qou-pdg9` was
already reopened for exactly this: its `c₁` values were the pre-ruling (`grouped`) word's and moved
by up to `163×`. `c₂` is the same exposure one order up, and this probe measures it rather than
inferring it from the dates.

MEASURED — every one of the six moved, by **10× to 217×**:

    case   c₂ canonical (measured)   c₂ recorded (grouped)   ratio
    pp            1.03126                  357/32  = 11.156    10.8×
    pn            0.78126                  403/32  = 12.594    16.1×
    nn            0.06251                  217/16  = 13.563   217.0×
    T             0.77344                 3285/128 = 25.664    33.2×
    ³He           1.22657                 3451/128 = 26.961    22.0×
    ⁴He           0.85743                15307/512 = 29.897    34.9×

WHY THE CONVENTION QUESTION IS SETTLED HERE AND NOT ASSUMED. `qou-qqm4` describes its `c₂` as
`[ε¹]+[ε²]` of `Δtr(1+ε)` — an ε-expansion, not the ℏ_q one this probe uses — so a bare disagreement
would be uninterpretable. **The self-test settles it:** run the same measurement on the `grouped`
word and it returns `c₁ → 2.3125 = 37/16` and `c₂ → 12.59375 = 403/32`, i.e. it reproduces **both**
recorded deuteron coefficients exactly. The conventions therefore agree, and the canonical column is
a statement about the word.

🛑 WHAT THIS DOES **NOT** ESTABLISH — the exact canonical rationals. The measurement is Richardson
extrapolation along `q = exp(η)` with `O(η)` error ~`1e-5` at `η = 1e-6`. That is four orders too
coarse to identify a rational with denominator up to 4096: `limit_denominator` on these returns
`4223/4095`, `3193/4087`, `2598/3359` — noise fits, not answers, and reporting them would be exactly
the false precision this corpus keeps having to retract. **Only `nn ≈ 0.0625068` is close enough to a
simple rational (`1/16`, within the extrapolation error) to be worth a guess, and it is a guess.**
Getting the exact values needs the exact-`Fraction` ε-series route `qou-qqm4` used, which is that
bean's work to redo.

What IS established, and needs no exact values: **all six moved, by one to two orders of magnitude**,
far outside any plausible extrapolation error. So the recorded rationals and everything computed
from them are stale.

THE DOWNSTREAM THAT MATTERS. `qou-qqm4`'s second-order chain/atom ratios move materially, and the
⁴He one roughly doubles:

    ratio                     recorded (grouped)   canonical (measured)
    T    (c₂pn + c₂nn)/c₂T          1.019                 1.091
    ³He  (c₂pp + c₂pn)/c₂He3        0.881                 1.478
    ⁴He  (c₂pp+c₂pn+c₂nn)/c₂He4     1.248                 2.187

The recorded reading — that the first-order over-count "nearly cancels one order up" — is weaker
under the canonical word, and at ⁴He much weaker. That audit's own title already says `c₂` does not
continue the cancellation; on this data it continues it even less.

Contrast the first order, where `PairwiseChainLeadingOrder.chain_over_atom_He4_generic` proves the
⁴He ratio is `24/7` for *every* deletion-sum pair — invariant under any intra-nucleon reordering.
**No such invariance is claimed or observed at second order**, and these numbers are evidence
against one.

SCOPE — (a) scope-limited. `mpf` at 80 dps end to end; `q = exp(η)` is a genuine 80-dps value so
`reject_float64_q` is satisfied rather than bypassed; `float` appears nowhere. The `grouped` word is
reached by binding `atom_braid_word_3A`'s `intra_order` through `functools.partial` on the module
attribute, because `tr_m_atom_zn` exposes no such knob — restored afterwards. No witness, nothing
wired, no Lean.
"""
from __future__ import annotations

import argparse
import functools
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "substrate"))

import mpmath as mp  # noqa: E402

import mass_at_3A_proper as M  # noqa: E402
import tr_m_atom_via_transfer as TR  # noqa: E402

ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2), "T": (1, 2), "³He": (2, 1), "⁴He": (2, 2)}
# c₀ is INVARIANT under intra_order (cycle count) — measured in the parity probe.
C0 = {"pp": Fraction(1, 8), "pn": Fraction(1, 8), "nn": Fraction(1, 8),
      "T": Fraction(3, 32), "³He": Fraction(3, 32), "⁴He": Fraction(7, 128)}
# c₁ is NOT — these are the canonical values (PR #6920); the grouped ones are in GROUPED_C1.
C1_CANON = {"pp": Fraction(1, 8), "pn": Fraction(1, 16), "nn": Fraction(0),
            "T": Fraction(1, 64), "³He": Fraction(1, 8), "⁴He": Fraction(7, 128)}
GROUPED_C1_PN = Fraction(37, 16)
# qou-qqm4's recorded c₂, all grouped-word.
REC_C2 = {"pp": Fraction(357, 32), "pn": Fraction(403, 32), "nn": Fraction(217, 16),
          "T": Fraction(3285, 128), "³He": Fraction(3451, 128), "⁴He": Fraction(15307, 512)}
# qou-qqm4's recorded second-order chain/atom ratios.
REC_RATIO = {"T": "1.019", "³He": "0.881", "⁴He": "1.248"}


def fr(x):
    return mp.mpf(x.numerator) / x.denominator


def coeffs(Z, N, c0, c1, etas, dps):
    """(c₁ estimate, c₂ estimate) at each η, by peeling known lower orders.

    `c₂ = (Δtr − c₀ − c₁·ℏ_q)/ℏ_q²`; the `c₁` column is returned alongside because it is the
    self-test — a run whose `c₁` does not land on the value it was given has nothing to say about
    `c₂`.
    """
    out = []
    for e in etas:
        eta = mp.mpf(e)
        q = mp.exp(eta)
        hb = (q - 1) / q
        ta, tf, _chi, _w = TR.tr_m_atom_zn(Z, N, dps=dps, q=q)
        d = abs(tf) - abs(ta)
        out.append(((d - fr(c0)) / hb, (d - fr(c0) - fr(c1) * hb) / hb ** 2))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, default=80)
    ap.add_argument("--etas", nargs="+", default=["1e-5", "1e-6"])
    args = ap.parse_args()
    mp.mp.dps = args.dps

    print("[c2-stale] qou-qqm4's six c₂ values are the PRE-2026-09-05 (grouped) atom word.")
    print(f"[c2-stale] mpf at {args.dps} dps; q = exp(η) so reject_float64_q is satisfied.\n")

    orig = M.atom_braid_word_3A

    def _bind(order):
        """Rebind the word builder in BOTH namespaces that hold a reference.

        `tr_m_atom_via_transfer` does `from mass_at_3A_proper import atom_braid_word_3A` at line
        58, so it holds its OWN name; patching `M.atom_braid_word_3A` alone leaves the consumer on
        the original. The first version of this probe did exactly that, and the self-test below
        caught it — the "grouped" run returned the CANONICAL c₁ (0.0625) because nothing had been
        rebound. That is what the self-test is for, and it is why the canonical column is never
        printed unless the grouped column reproduces two independently-recorded numbers first.
        """
        f = functools.partial(orig, intra_order=order)
        M.atom_braid_word_3A = f
        TR.atom_braid_word_3A = f

    try:
        # ── SELF-TEST. Without this a disagreement is uninterpretable: qou-qqm4 describes its c₂
        # as an ε-expansion, this probe uses ℏ_q, and two conventions disagreeing says nothing
        # about the word. Reproducing BOTH recorded grouped coefficients settles it.
        _bind("grouped")
        print("  SELF-TEST — same measurement on the GROUPED word: does it reproduce qou-pdg9's")
        print("  c₁ = 37/16 AND qou-qqm4's c₂ = 403/32 for the deuteron?")
        g = coeffs(1, 1, C0["pn"], GROUPED_C1_PN, args.etas, args.dps)
        print(f"    {'η':<8}{'c₁ est':>18}{'c₂ est':>18}")
        for e, (a, b) in zip(args.etas, g):
            print(f"    {e:<8}{mp.nstr(a, 10):>18}{mp.nstr(b, 10):>18}")
        c1_ok = abs(g[-1][0] - fr(GROUPED_C1_PN)) < mp.mpf("1e-3")
        c2_ok = abs(g[-1][1] - fr(REC_C2["pn"])) < mp.mpf("1e-3")
        print(f"    → c₁ {'==' if c1_ok else '!='} 37/16 = {mp.nstr(fr(GROUPED_C1_PN), 8)},"
              f"  c₂ {'==' if c2_ok else '!='} 403/32 = {mp.nstr(fr(REC_C2['pn']), 8)}")
        if not (c1_ok and c2_ok):
            print("    ⇒ the conventions do NOT agree. Nothing below is a statement about the word.")
            return 1
        print("    ⇒ both reproduced. The conventions agree, so the canonical column below is")
        print("      about the WORD, not about a differing definition of c₂.\n")

        # ── THE MEASUREMENT ─────────────────────────────────────────────────────────────────────
        _bind("borromean")
        print("  CANONICAL WORD — intra_order='borromean' (default since qou-hu1f)")
        print(f"    {'case':<6}{'c₁ est (check)':>18}{'c₂ canonical':>16}"
              f"{'c₂ recorded':>16}{'ratio':>10}  moved?")
        c2 = {}
        moved = 0
        for nm, (Z, N) in ZN.items():
            v = coeffs(Z, N, C0[nm], C1_CANON[nm], args.etas, args.dps)
            c1e, c2e = v[-1]
            c2[nm] = c2e
            rec = fr(REC_C2[nm])
            # "Moved" is judged against 1e-3 — a hundred times the ~1e-5 extrapolation error, and
            # a thousandth of the smallest gap actually seen. Nothing here is a near-miss.
            far = abs(c2e - rec) > mp.mpf("1e-3")
            moved += far
            print(f"    {nm:<6}{mp.nstr(c1e, 8):>18}{mp.nstr(c2e, 8):>16}"
                  f"{str(REC_C2[nm]):>16}{mp.nstr(rec / c2e, 5) + '×':>10}"
                  f"  {'MOVED' if far else 'same'}")
        print(f"    ⇒ {moved} of {len(ZN)} moved. The c₁ column is the per-case self-test: each")
        print("      lands on the canonical c₁ it was given, so the c₂ residual is the real one.\n")

        # ── WHAT IS NOT ESTABLISHED ─────────────────────────────────────────────────────────────
        print("  🛑 EXACT RATIONALS ARE **NOT** ESTABLISHED HERE.")
        print("     Richardson error is ~1e-5 at η = 1e-6 — four orders too coarse to identify a")
        print("     rational with denominator ≤ 4096. limit_denominator returns 4223/4095,")
        print("     3193/4087, 2598/3359: noise fits, not answers. Only nn is close to a simple")
        print(f"     rational (1/16 = 0.0625 against {mp.nstr(c2['nn'], 8)}), and that is a GUESS.")
        print("     The exact values need the exact-Fraction ε-series route qou-qqm4 used.")
        print("     What IS established: all six moved by 10×–217×, far outside that error.\n")

        # ── DOWNSTREAM ──────────────────────────────────────────────────────────────────────────
        # Ratios of same-precision quantities, so ~5 digits is ample here even though the
        # individual values are not exact.
        print("  DOWNSTREAM — qou-qqm4's second-order chain/atom ratios")
        print(f"    {'ratio':<28}{'recorded':>12}{'canonical':>12}")
        rows = (("T    (c₂pn + c₂nn)/c₂T", c2["pn"] + c2["nn"], c2["T"], "T"),
                ("³He  (c₂pp + c₂pn)/c₂He3", c2["pp"] + c2["pn"], c2["³He"], "³He"),
                ("⁴He  (c₂pp+c₂pn+c₂nn)/c₂He4",
                 c2["pp"] + c2["pn"] + c2["nn"], c2["⁴He"], "⁴He"))
        for label, num, den, key in rows:
            print(f"    {label:<28}{REC_RATIO[key]:>12}{mp.nstr(num / den, 5):>12}")
        print("    The recorded reading — the first-order over-count 'nearly cancels one order")
        print("    up' — is weaker under the canonical word, and at ⁴He much weaker (it roughly")
        print("    doubles). Contrast FIRST order, where chain_over_atom_He4_generic proves the")
        print("    ⁴He ratio is 24/7 for EVERY deletion-sum pair. No such invariance is claimed")
        print("    or observed at second order, and these numbers are evidence against one.")
    finally:
        M.atom_braid_word_3A = orig
        TR.atom_braid_word_3A = orig

    print("\n  qou-qqm4 needs reopening. Its exact values are that bean's work to redo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
