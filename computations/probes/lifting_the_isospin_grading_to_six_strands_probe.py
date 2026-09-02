#!/usr/bin/env python3
"""Lifting the `(T,S)` grading to three strands per nucleon raises the cap from
`1` to exactly `3/2` — and costs the Pauli-forced identification that made the
`n = 2` result work.

WHAT THIS TESTS
---------------
`isospin_grading_restores_the_sign_probe` (bean `qou-m896`) ran at the `n = 2`
interface, one strand per nucleon, and carried an explicit caveat: the corpus's
atom words give each nucleon **three** strands, and lifting the grading into
that construction was untested. This runs the lift.

Two questions: does the two-block structure survive, and does the cap survive?
The answers are no and no — but not in the same direction.

THE EXCHANGE OPERATOR AT SIX STRANDS
------------------------------------
Exchanging two nucleons is no longer a transposition but a **block swap** of
`{0,1,2}` with `{3,4,5}`, the positive braid

    (s3 s2 s1)(s4 s3 s2)(s5 s4 s3)

whose permutation is `[3,4,5,0,1,2]`, verified before use.

ITS SPECTRUM IS NOT TWO EIGENVALUES
-----------------------------------
Every eigenvalue across the four live `H_6` blocks is `± q^k`, exactly:

    -q^-3  = -0.731233708    L = +3 log q    x1   (3,3)
    +q^-1  = +0.900918284    L = +1 log q    x1   (4,2)
    +-q^2  = +-1.232052454   L = -2 log q    x4   (4,2)
    +-q^3  = +-1.367551837   L = -3 log q    x5   (3,3) (5,1)
    +-q^5  = +-1.684895597   L = -5 log q    x4   (4,2)
    +-q^6  = +-1.870198027   L = -6 log q    x4   (5,1)
    +q^9   = +2.557592747    L = -9 log q    x1   (6,)

Seven distinct magnitudes, exponents `{-3, -1, 2, 3, 5, 6, 9}`, and every `L` an
**integer multiple of `log q`**. The `n = 2` situation — two eigenvalues `q` and
`-1/q` whose product is `-1` — simply does not lift.

SO THE `det T = -1` CAP DOES NOT GOVERN HERE
--------------------------------------------
At `n = 2` the cap was `|L_bound| <= |L_unbound|`, i.e. ratio `<= 1`, forced by
`q . (1/q) = 1`. At six strands the bound channels have `L/log q in {3, 1}` and
the unbound ones `{-2, -3, -5, -6, -9}`, so the best achievable ratio is

    3 / 2  =  1.500000   **exactly**

**The cap rises from `1` to `3/2`.** That is a real structural gain and it is the
first thing in this arc to move it at all — every convention, every crossing
count and every level left it at `1`.

BUT `3/2` IS STILL SHORT OF BOTH TARGETS
----------------------------------------
    QCD colour   3bar/6 ratio        2        3/2 falls short by 1.33x
    nuclear      deuteron / 1S0     33.7      3/2 falls short by 22.5x

So the lift helps and does not close. It is worth knowing which of the two it
nearly reaches: the *quark* target, not the nuclear one.

AND THE IDENTIFICATION STOPS BEING FORCED
-----------------------------------------
The `n = 2` result rested on Pauli: two nucleons need a totally antisymmetric
wavefunction, so `T = 1` is the symmetric block and `T = 0` the antisymmetric
one, and the two-strand algebra has exactly those two blocks. **That
correspondence does not survive.** Here the exchange parity is *not* locked to
the magnitude — `q^2, q^3, q^5, q^6` each carry **both** signs — so "symmetric"
and "antisymmetric" no longer pick out two channels with two values.

Worse for the sign pattern: the only magnitudes carrying a single parity are

    -q^-3   antisymmetric only    L = +3 log q    BOUND
    +q^-1   symmetric only        L = +1 log q    BOUND
    +q^9    symmetric only        L = -9 log q    unbound

so the two *pure-parity bound* channels are one of each parity — **both bound**.
Reading `T=1` as the pure symmetric channel gives a bound `T=1`, which is the
very failure `qou-m896` fixed at `n = 2`. Recovering the sign pattern at six
strands requires choosing an unbound channel for `T = 1` by hand, and nothing
forces which.

WHAT THIS MEANS FOR qou-m896
----------------------------
Its result stands where it was stated — at the `n = 2` interface — and its own
caveat is now discharged with a negative answer: the grading does **not** lift
cleanly. The `3/2` cap is a genuine and previously unseen structural gain, but
it is bought by giving up the forced identification, so what replaces the `n=2`
argument is a choice rather than a derivation.

DISCIPLINE
----------
No fit. The block-swap permutation is checked before the operator is used, and
every eigenvalue is verified to be an exact integer power of `q` (assertion, not
inspection) before any `L` is quoted. Targets are external comparisons.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] isospin_grading_restores_the_sign_probe.py (the n=2 result lifted)
-- Ref: [probe] adding_crossings_cannot_break_the_degeneracy_probe.py (the n=2 cap)
-- Ref: [probe] level_three_colour_channel_probe.py (the QCD target)
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = mp.mpf(str(Q0))
LQ = float(mp.log(_Q))
WORD = [3, 2, 1, 4, 3, 2, 5, 4, 3]      # block swap {0,1,2} <-> {3,4,5}
R_QCD = 2
R_NUC = 2.224566 / 0.066


def perm_of(word, n=6):
    p = list(range(n))
    for g in word:
        i = g - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def main() -> int:
    assertions = []
    print("t7qv — lifting the (T,S) grading to three strands per nucleon")

    # ── A1. the block swap is the right operator ───────────────────────
    print("\n  1. the exchange operator at six strands")
    pm = perm_of(WORD)
    want = [3, 4, 5, 0, 1, 2]
    print(f"     (s3 s2 s1)(s4 s3 s2)(s5 s4 s3)")
    print(f"     permutation {pm}, expected {want}: {pm == want}")
    print(f"     exchanging two nucleons is a BLOCK SWAP of {{0,1,2}} with")
    print(f"     {{3,4,5}}, not a transposition — that is the whole difference.")
    ok = pm == want
    assertions.append(("A1_block_swap_permutation_is_correct", ok,
                       f"permutation {pm} == {want}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the spectrum is not two eigenvalues ────────────────────────
    print("\n  2. its spectrum: seven magnitudes, not two")
    ps, y, _c, _d, _m = load_cost("deuteron")
    live = [(tuple(p), float(w)) for p, w in zip(ps, y)
            if abs(float(w)) > 1e-30]
    tab: dict = {}
    exact = True
    for p, _w in live:
        S = [np.asarray(m, dtype=float)
             for m in build_seminormal_matrices(list(p))[0]]
        d = S[0].shape[0]
        M = np.eye(d)
        for g in WORD:
            M = M @ S[g - 1]
        for zv in np.linalg.eigvals(M):
            k = np.log(abs(zv)) / LQ
            kk = int(round(k))
            if abs(k - kk) > 1e-6:
                exact = False
            s = int(np.sign(zv.real))
            tab.setdefault((kk, s), []).append(str(p))
    print(f"     {'eigenvalue':>16s} {'L / log q':>10s} {'mult':>5s}  blocks")
    for kk, s in sorted(tab, key=lambda t: (t[0], t[1])):
        val = s * float(_Q ** kk)
        blk = ", ".join(sorted(set(tab[(kk, s)])))
        print(f"     {('+' if s > 0 else '-')}q^{kk:<3d} = {val:+12.9f} "
              f"{-kk:>10d} {len(tab[(kk, s)]):>5d}  {blk}")
    ks = sorted({kk for kk, _s in tab})
    mags = len(ks)
    print(f"     exponents present: {ks}  -> {mags} distinct magnitudes")
    print(f"     every eigenvalue is EXACTLY +-q^k (checked, not eyeballed):"
          f" {exact}")
    print(f"     the n=2 structure — two eigenvalues q and -1/q with product -1 —")
    print(f"     does not lift.")
    ok = exact and mags == 7 and set(ks) == {-3, -1, 2, 3, 5, 6, 9}
    assertions.append(("A2_spectrum_is_seven_integer_powers_of_q", ok,
                       f"exponents {ks}, all exactly integer powers: {exact}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. L values are integer multiples of log q ────────────────────
    print("\n  3. so every L is an integer multiple of log q")
    bound = sorted((-kk for kk in ks if kk < 0), reverse=True)
    unb = sorted((-kk for kk in ks if kk > 0))
    print(f"     bound   (|eig| < 1, L > 0):  L/log q in {bound}")
    print(f"     unbound (|eig| > 1, L < 0):  L/log q in {unb}")
    print(f"     log q = {LQ:.12f}, so the whole spectrum is quantised in units")
    print(f"     of it, spanning {min(-kk for kk in ks)} to {max(-kk for kk in ks)}.")
    ok = bound == [3, 1] and unb == [-9, -6, -5, -3, -2]
    assertions.append(("A3_L_values_are_integer_multiples_of_log_q", ok,
                       f"bound {bound}, unbound {unb}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the cap rises from 1 to exactly 3/2 ────────────────────────
    print("\n  4. the cap rises from 1 to exactly 3/2")
    best = max(b / abs(u) for b in bound for u in unb)
    arg = max(((b / abs(u), b, u) for b in bound for u in unb))
    print(f"     at n=2 the cap was 1, forced by q.(1/q) = 1 (qou-o8ww).")
    print(f"     here the best |L_bound|/|L_unbound| = {best:.6f} = 3/2,")
    print(f"     attained by L = {arg[1]:+d} log q (from -q^-3) against "
          f"L = {arg[2]:+d} log q (from +-q^2).")
    print(f"     The det T = -1 degeneracy does NOT govern the six-strand level.")
    print(f"     This is the first thing in the arc to move the cap at all —")
    print(f"     every convention, crossing count and level left it at 1.")
    ok = abs(best - 1.5) < 1e-12
    assertions.append(("A4_cap_rises_to_three_halves", ok,
                       f"best ratio {best:.9f} = 3/2, from L=+3 vs L=-2 log q"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. still short of both targets ────────────────────────────────
    print("\n  5. but 3/2 is short of both targets")
    print(f"     {'target':<26s} {'needs':>9s} {'short by':>10s}")
    print(f"     {'QCD colour 3bar/6':<26s} {R_QCD:>9.4f} "
          f"{R_QCD / best:>9.4f}x")
    print(f"     {'nuclear deuteron/1S0':<26s} {R_NUC:>9.4f} "
          f"{R_NUC / best:>9.4f}x")
    print(f"     the lift helps and does not close. Worth knowing WHICH it")
    print(f"     nearly reaches: the quark target, not the nuclear one.")
    ok = best < R_QCD < R_NUC
    assertions.append(("A5_three_halves_still_misses_both_targets", ok,
                       f"QCD 2 short by {R_QCD / best:.4f}x, nuclear "
                       f"{R_NUC:.2f} short by {R_NUC / best:.2f}x"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the Pauli identification does not survive ──────────────────
    print("\n  6. and the identification stops being forced")
    both = sorted(kk for kk in ks if (kk, 1) in tab and (kk, -1) in tab)
    pure = sorted((kk, s) for kk, s in tab if kk not in both)
    print(f"     magnitudes carrying BOTH exchange parities: q^k, k in {both}")
    print(f"     magnitudes carrying only one parity:")
    for kk, s in pure:
        st = "bound" if kk < 0 else "unbound"
        par = "symmetric" if s > 0 else "antisymmetric"
        print(f"       {('+' if s > 0 else '-')}q^{kk:<3d}  {par:<14s} "
              f"L = {-kk:+d} log q   {st.upper()}")
    print(f"     at n=2, Pauli FORCED the identification: T=1 symmetric, T=0")
    print(f"     antisymmetric, and the algebra had exactly those two blocks.")
    print(f"     Here parity is not locked to magnitude, so the two labels no")
    print(f"     longer pick out two channels with two values — and the only two")
    print(f"     pure-parity BOUND channels are one of each parity, so reading")
    print(f"     T=1 as the pure symmetric channel gives a BOUND T=1, the very")
    print(f"     failure qou-m896 fixed. Recovering the sign pattern here needs")
    print(f"     an unbound channel chosen BY HAND, and nothing forces which.")
    pure_bound = [(kk, s) for kk, s in pure if kk < 0]
    ok = len(both) == 4 and len(pure_bound) == 2 \
        and {s for _kk, s in pure_bound} == {1, -1}
    assertions.append(("A6_pauli_identification_does_not_survive_the_lift", ok,
                       f"{len(both)} magnitudes carry both parities; the two "
                       f"pure-parity bound channels are one of each parity"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The lift discharges qou-m896's own caveat, with a mixed answer.")
    print("  Exchanging two nucleons at three strands each is a block swap, not")
    print("  a transposition, and its spectrum is seven magnitudes +-q^k with")
    print("  k in {-3,-1,2,3,5,6,9} — every L an exact integer multiple of log q.")
    print("  The n=2 two-eigenvalue structure does not lift, so the det T = -1")
    print("  degeneracy does not govern here: the cap rises from 1 to EXACTLY")
    print("  3/2. That is the first thing in this arc to move it at all.")
    print("  But 3/2 still misses QCD's 2 by 1.33x and the nuclear 33.7 by 22.5x,")
    print("  and the gain is paid for: exchange parity is no longer locked to")
    print("  magnitude, so the Pauli-forced identification that made the n=2")
    print("  result work is gone. The two pure-parity bound channels are one of")
    print("  each parity, so a symmetric T=1 would be BOUND — the failure n=2")
    print("  had fixed. What replaces the argument at six strands is a choice,")
    print("  not a derivation.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="numpy")
        wb.set_description(
            "Discharges qou-m896's explicit caveat by lifting the (T,S) grading "
            "from the n=2 interface into the corpus's three-strands-per-nucleon "
            "construction. Exchanging two nucleons there is a BLOCK SWAP of "
            "{0,1,2} with {3,4,5} — the braid (s3 s2 s1)(s4 s3 s2)(s5 s4 s3), "
            "permutation [3,4,5,0,1,2] verified before use — not a "
            "transposition. Its spectrum across the four live H_6 blocks is "
            "seven distinct magnitudes, every eigenvalue exactly +-q^k with k in "
            "{-3,-1,2,3,5,6,9} (checked by assertion), so every L is an integer "
            "multiple of log q spanning -9 to +3. The n=2 structure of two "
            "eigenvalues q and -1/q with product -1 does NOT lift, and "
            "consequently the det T = -1 cap does not govern: bound channels "
            "have L/log q in {3,1} and unbound in {-2,-3,-5,-6,-9}, so the best "
            "|L_bound|/|L_unbound| is EXACTLY 3/2. The cap rises from 1 to 3/2 — "
            "the first thing in this arc to move it at all, every convention, "
            "crossing count and Wenzl level having left it at 1. But 3/2 still "
            "misses QCD's colour ratio of 2 by 1.33x and the nuclear 33.7 by "
            "22.5x. And the gain is paid for: exchange parity is not locked to "
            "magnitude (q^2, q^3, q^5, q^6 each carry both signs), so the "
            "Pauli-forced identification underpinning the n=2 result is gone; "
            "the only two pure-parity BOUND channels are one of each parity, so "
            "reading T=1 as the pure symmetric channel gives a bound T=1 — "
            "exactly the failure qou-m896 fixed. Recovering the sign pattern at "
            "six strands requires choosing an unbound channel by hand.")
        wb.add_data("block_swap",
                    {"word": "s3 s2 s1 s4 s3 s2 s5 s4 s3",
                     "permutation": pm, "expected": want})
        wb.add_data("spectrum",
                    {f"{'+' if s > 0 else '-'}q^{kk}": {
                        "value": f"{s * float(_Q ** kk):+.12f}",
                        "L_over_log_q": -kk,
                        "multiplicity": len(tab[(kk, s)]),
                        "blocks": sorted(set(tab[(kk, s)]))}
                     for kk, s in sorted(tab, key=lambda t: (t[0], t[1]))})
        wb.add_data("cap",
                    {"n2_cap": "1", "n6_cap": f"{best:.12f}",
                     "n6_cap_exact": "3/2",
                     "bound_L_over_log_q": bound,
                     "unbound_L_over_log_q": unb})
        wb.add_data("targets",
                    {"QCD_colour_ratio": R_QCD,
                     "QCD_short_by": f"{R_QCD / best:.6f}",
                     "nuclear_ratio": f"{R_NUC:.6f}",
                     "nuclear_short_by": f"{R_NUC / best:.6f}"})
        wb.add_data("parity_structure",
                    {"both_parities_at_q_pow": both,
                     "single_parity": [{"k": kk, "sign": s} for kk, s in pure]})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE 3/2 CAP IS OVER THE BLOCK-SWAP SPECTRUM, NOT A DERIVED "
            "PHYSICAL RATIO. It is the largest |L_bound|/|L_unbound| available "
            "from any pair of eigenvalues of this operator. Which pair a "
            "physical T=0/T=1 split would actually use is NOT determined here — "
            "that is exactly what A6 shows is no longer forced. Read 3/2 as an "
            "upper bound on what the six-strand exchange can supply, not as a "
            "prediction.")
        wb.add_caveat(
            "ONLY THE EXCHANGE OPERATOR IS LIFTED, NOT THE WHOLE CONSTRUCTION. "
            "This computes the spectrum of the nucleon block swap in H_6 with "
            "convention-D weights. It does not attach nucleon internal words, "
            "does not use the production bond, and does not recompute any "
            "binding energy. A full lift of qou-m896 would have to place the "
            "(T,S) grading inside the atom word itself, which remains untested.")
        wb.add_caveat(
            "qou-m896's RESULT IS NOT OVERTURNED — it was stated at the n=2 "
            "interface and stands there. What is discharged is its caveat: the "
            "grading does not lift cleanly. Both facts should be quoted "
            "together, since the n=2 argument's force came from the "
            "identification being Pauli-forced, and that is precisely what does "
            "not survive.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
