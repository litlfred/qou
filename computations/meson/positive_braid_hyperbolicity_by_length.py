#!/usr/bin/env python3
"""Exhaustive: no positive 3-braid word of length <= 8 has a hyperbolic closure.

WHY THIS MATTERS FOR OBSTRUCTION A
----------------------------------
`docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md` records that the
corpus's meson braid `M = (s0 s1)^2 s1 s0` closes to T(2,5) with Vol = 0, so
under `m(K) = m_e . Vol(K) . rho(K) / hbar_q^2` the corpus's own pion braid
gives `m_pi = 0`.  That was a statement about ONE word.

This probe asks the stronger question: is Vol = 0 forced by the LENGTH?  The
`lepton-meson-torus-knot-dictionary` fixes crossing counts (pion 6, kaon 8,
eta/phi 10) and `mesonCrossingCount`'s docstring says those are BRAID WORD
lengths, so the word is constrained to a finite set and the question is a
complete case check rather than a search.

Result: exhaustively over all 2^L positive words for L = 2..10, ZERO are
hyperbolic for L <= 8, which covers the pion (6) AND kaon (8) dictionary
lengths.  The first hyperbolic positive closures appear at L = 9.

METHOD -- THE TRAP THAT MAKES OR BREAKS THIS
--------------------------------------------
`snappy.Manifold("braid[...]")` builds the closed braid TOGETHER WITH ITS
BRAID AXIS, which is a different manifold with one extra cusp and a larger
volume.  Measured here on the controls:

    Borromean (s0 s1^-1)^3   braid[...] 4 cusps, vol 12.179299277
                             Link(braid_closure) 3 cusps, vol 7.32772475342  <- correct
    figure-eight 4_1         braid[...] 2 cusps, vol  8.1195328513
                             Link(braid_closure) 1 cusp,  vol 2.02988321282  <- correct
    pion M                   braid[...] 2 cusps, vol  4.0597664256
                             Link(braid_closure) 1 cusp,  vol 0, degenerate   <- correct

Using the `braid[...]` spec makes 54 of 64 length-6 words look "hyperbolic"
and would invert this probe's conclusion.  `Link(braid_closure=w).exterior()`
is the closed braid alone and is what the audit's original measurement used --
this probe reproduces its 208-of-2044 total exactly, which is the cross-check
that the two agree.

Emits no witness: a decision probe whose output is an argument.  Per AGENTS.md
"PROBES ARE NOT EXEMPT" it still carries the precision discipline -- the only
numeric comparison is a hyperbolicity threshold on a SnapPy volume, and the
controls are checked against their exact known values.
"""

from __future__ import annotations

import itertools
import warnings

warnings.filterwarnings("ignore")

import snappy  # noqa: E402

#: Volume below which a closure is treated as non-hyperbolic.  SnapPy returns
#: small negatives (e.g. -5.2e-8) on degenerate triangulations, so this is a
#: sign-and-magnitude guard, not a precision claim.
HYP_EPS = 1e-6

#: Randomisation attempts before declaring a closure non-hyperbolic.  A
#: hyperbolic manifold given a degenerate initial triangulation is normally
#: rescued on the first retry (both controls below succeed at attempt 1); the
#: pion word survives 30 without ever finding a positively-oriented solution.
RANDOMIZE_TRIES = 8

#: dictionary crossing counts, from `mesonCrossingCount` in
#: content/.../knots-particles-confinement/lepton-meson-torus-knot-dictionary.lean
DICTIONARY = {6: "pion   (u-bar 3 + d 3)",
              8: "kaon   (u-bar 3 + s 5)",
              10: "eta/phi (s-bar 5 + s 5)"}

#: (word, label, expected volume) -- exact known values, checked before trusting
#: anything else this probe prints.
CONTROLS = [
    ([1, -2, 1, -2, 1, -2], "Borromean (s0 s1^-1)^3", 7.32772475342),
    ([1, -2, 1, -2], "figure-eight 4_1", 2.02988321282),
]

PION = [1, 2, 1, 2, 2, 1]          # (s0 s1)^2 s1 s0, the corpus meson braid

#: All four signed generators, for the mixed-sign control sweep.
MIXED_GENS = (1, -1, 2, -2)

#: Vol.rho the pion needs at rho = 1: (m_pi/m_e) . hbar_q^2, from the audit's
#: target table.  Quoted only to ask whether the mixed-sign range BRACKETS it --
#: see the warning in the verdict about why nearest-point selection is not a
#: result.
PION_TARGET = 2.681392089


def closure_volume(word):
    """Volume of the closure of `word`, axis EXCLUDED.  None if degenerate."""
    try:
        M = snappy.Link(braid_closure=list(word)).exterior()
    except Exception:
        return None
    for _ in range(RANDOMIZE_TRIES):
        if M.solution_type() == "all tetrahedra positively oriented":
            try:
                return float(M.volume())
            except Exception:
                return None
        M.randomize()
    return None


def is_hyperbolic(word) -> bool:
    v = closure_volume(word)
    return v is not None and v > HYP_EPS


def mixed_sign_sweep():
    """Same sweep over words in {s0, s0^-1, s1, s1^-1}.

    This is the control that separates the two candidate explanations for
    `Vol = 0`: is it the LENGTH, or is it POSITIVITY?  If mixed-sign words of
    the same length are hyperbolic, length is not the culprit.
    """
    print("\n-- control: MIXED-SIGN words, same lengths --")
    print(f"{'L':>3} {'words':>7} {'hyperbolic':>11} {'frac':>8} "
          f"{'min vol':>12} {'max vol':>12}  brackets pion target?")
    out = {}
    for L in (4, 5, 6):
        words = list(itertools.product(MIXED_GENS, repeat=L))
        vols = [v for v in (closure_volume(w) for w in words)
                if v is not None and v > HYP_EPS]
        if not vols:
            print(f"{L:>3} {len(words):>7} {0:>11} {0.0:>8.4f} "
                  f"{'-':>12} {'-':>12}  no")
            out[L] = None
            continue
        lo, hi = min(vols), max(vols)
        brackets = lo <= PION_TARGET <= hi
        print(f"{L:>3} {len(words):>7} {len(vols):>11} "
              f"{len(vols)/len(words):>8.4f} {lo:>12.7f} {hi:>12.7f}  "
              f"{'YES' if brackets else 'no'}")
        out[L] = (len(vols), lo, hi, brackets)
    return out


def main() -> int:
    print("=" * 72)
    print("POSITIVE 3-BRAID CLOSURES: HYPERBOLICITY BY WORD LENGTH")
    print("=" * 72)

    print("\n-- controls (exact known volumes; axis EXCLUDED) --")
    for word, label, expect in CONTROLS:
        v = closure_volume(word)
        ok = v is not None and abs(v - expect) < 1e-9
        print(f"   {label:26} vol={v!r:20} expect={expect}  ok={ok}")
        if not ok:
            print("   !! control failed -- the closure object is wrong, stopping")
            return 1

    print("\n-- the axis trap, shown rather than asserted --")
    for word, label, _ in CONTROLS + [(PION, "pion M", None)]:
        spec = "braid[" + ",".join(map(str, word)) + "]"
        A = snappy.Manifold(spec)
        B = snappy.Link(braid_closure=list(word)).exterior()
        print(f"   {label:26} braid[...] {A.num_cusps()} cusps  "
              f"| Link(braid_closure) {B.num_cusps()} cusps")

    print("\n-- exhaustive sweep --")
    print(f"{'L':>3} {'words':>6} {'hyperbolic':>11} {'fraction':>9}   dictionary length")
    total = total_hyp = 0
    first_hyp = None
    for L in range(2, 11):
        words = list(itertools.product((1, 2), repeat=L))
        hyp = sum(1 for w in words if is_hyperbolic(w))
        total += len(words)
        total_hyp += hyp
        if hyp and first_hyp is None:
            first_hyp = L
        print(f"{L:>3} {len(words):>6} {hyp:>11} {hyp/len(words):>9.4f}   "
              f"{DICTIONARY.get(L, '')}")
    print(f"\n   total length 2-10: {total_hyp} of {total} "
          f"({total_hyp/total:.4f})")
    print("   the audit's independently-measured figure is 208 of 2044 -- "
          f"{'MATCH' if total_hyp == 208 and total == 2044 else 'MISMATCH'}")

    mixed = mixed_sign_sweep()

    print("\n" + "=" * 72)
    print("VERDICT")
    print("=" * 72)
    print(f"   First hyperbolic positive closure appears at length {first_hyp}.")
    print("   So for EVERY positive 3-braid word of length <= 8 the closure has")
    print("   Vol = 0.  That covers the pion (6) and the kaon (8) at their")
    print("   dictionary lengths, exhaustively -- a complete finite case check,")
    print("   not a sample.")
    print()
    print("   CONSEQUENCE FOR OBSTRUCTION A.  The pion's Vol = 0 is not a")
    print("   property of the particular word the corpus chose; it is forced by")
    print("   length together with positivity.  Choosing a different positive")
    print("   6-crossing word cannot fix it, and neither can choosing a")
    print("   different positive 8-crossing word for the kaon.  Either the")
    print("   meson braid admits negative crossings GEOMETRICALLY (not merely")
    print("   as normal-form coefficients via sigma^-1 = sigma - h), or the")
    print("   dictionary lengths are not braid word lengths, or the mass law")
    print("   does not read Vol off the closed braid.")
    print()
    m6 = mixed.get(6)
    if m6:
        n6, lo6, hi6, br6 = m6
        print("   AND IT IS POSITIVITY, NOT LENGTH.  At the pion's own length 6,")
        print("   positive words give 0 of 64 hyperbolic while mixed-sign words")
        print(f"   give {n6} of 4096, with volumes spanning {lo6:.7f} to {hi6:.7f}")
        print(f"   -- a range that {'DOES' if br6 else 'does not'} bracket the "
              f"pion target {PION_TARGET}.")
        print("   Mixed-sign words are already hyperbolic at length 4 (4_1).")
        print("   So the first of the three routes above is not merely possible;")
        print("   it is DEMONSTRABLY AVAILABLE at the required length.")
        print()
        print("   NOT A RESULT: bracketing a target is not hitting it, and")
        print("   choosing the nearest enumerated volume is exactly the")
        print("   per-state fit this audit exists to avoid.  What is shown is")
        print("   that the candidate space is non-empty, nothing more.")
        print()
    print("   WHAT IT DOES NOT SAY.  It does not identify the chiral limit.")
    print("   A future reader will notice that m_pi = 0 is also what QCD gives")
    print("   in the chiral limit (GMOR: m_pi^2 f_pi^2 = -2 m_q <q-bar q>, the")
    print("   pion a pseudo-Goldstone) and be tempted to read the Vol = 0 as")
    print("   that physics.  It is not: the same computation gives Vol = 0 for")
    print("   the KAON too, and the kaon is NOT a pseudo-Goldstone of the")
    print("   SU(2)xSU(2) subalgebra -- in Gell-Mann-Oakes-Renner's own")
    print("   parametrisation W_i(c) vanishes at c = -sqrt(2) for i = 1,2,3")
    print("   (pion) and not for i = 4..7 (kaon).  A mechanism that zeroes")
    print("   both is not the chiral limit; it is a degeneracy of short")
    print("   positive braids.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
