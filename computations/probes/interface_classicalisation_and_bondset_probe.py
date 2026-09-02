#!/usr/bin/env python3
"""Both halves of the question qou-k12x left open.

(A) IS THERE A DERIVATION THAT FIXES THE CLASSICAL REPRESENTATIVE? YES -- and
    it is nearly degenerate, which is the part that matters.

    In the Hecke algebra sigma^2 = h.sigma + 1, so sigma^-1 = sigma - h. Any
    element written `sigma - d.1` is therefore a NORMALISED COMBINATION of the
    two crossings:

        sigma - d.1 = a.sigma + b.sigma^-1,   a + b = 1,   b = d/h.

    Reading the four interface ctypes through that identity (computed below):

        sigma              a = 1,       b = 0
        sigma_inv          a = 0,       b = 1
        averaged           a = 1/2,     b = 1/2      <- EXACTLY balanced
        averaged_weighted  a = 1/2+d/4, b = 1/2-d/4  <- tie broken by colour

    So the UNWEIGHTED averaged interface is exactly `(sigma + sigma^-1)/2` and
    has NO preferred classical representative -- the two crossings enter with
    identical weight, and any classicalisation of it is a coin flip.

    The COLOUR-WEIGHTED p-n interface does have one. delta = flavor_split_leading(q0)
    is POSITIVE (measured below), so a > b: the POSITIVE crossing dominates and
    the derived classical representative is lk = +1.

    THE MARGIN IS 0.069%. The weights are 0.5003439 : 0.4996561. So the answer
    to "is the classicalisation derived?" is yes, and the answer to "is it
    meaningful?" is: it is a 0.07%-confidence preference. Treating this
    interface as a definite +1 crossing keeps the sign and discards essentially
    all of the structure -- which is why an lk-based invariant built on it can
    be simultaneously well-defined and uninformative.

(B) WHO DISAGREES WITH THE CANONICAL BOND SET.

    qou-k12x established that the canonical braid is a CHAIN of A-1
    inter-nucleon interfaces while the contact-graph model asserts C(A,2)
    bonded pairs, agreeing only at A = 2. This leg measures how far that
    reaches, and reports an UPPER BOUND rather than a defect count -- see the
    scope note.

SCOPE. (A) is a derivation: the a/b decomposition is an algebraic identity in
the Hecke algebra and the sign of delta is measured, not chosen. Its
consequence -- that the preference is 0.069% -- is a magnitude, not an
exclusion, and it excludes nothing.

(B) is a GREP-LEVEL UPPER BOUND and is explicitly NOT a defect count. A file
matching `comb(A,2)` / `clique` may be using it for something other than the
canonical bond set, or deliberately comparing conventions. Establishing which
of them are actually wrong requires reading each one, which this unit does not
do and does not claim to have done.

Beans qou-wpr6; answers the two open halves of qou-k12x.
"""
from __future__ import annotations

import subprocess
import sys
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import mpmath as mp  # noqa: E402

import canonical_braid_crossings as C  # noqa: E402

mp.mp.dps = 50
ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    from hecke_core import h as h_val

    # NOTE: mp.mpf(float) is EXACT (binary), while mp.mpf(str(float)) is the
    # shortest round-tripping DECIMAL and is not. Going through str() here made
    # `averaged` miss exact balance by ~1e-17 and tripped this file's own
    # assertion -- the assertion doing its job. Convert from the float directly.
    h = mp.mpf(h_val)

    print("== (A) the interfaces as normalised combinations a.sigma + b.sigma^-1 ==")
    print("   (identity: sigma^-1 = sigma - h, so sigma - d.1 has b = d/h)")
    rows = {}
    for t in ("sigma", "sigma_inv", "averaged", "averaged_weighted"):
        d = mp.mpf(C.d_for_ctype(t, h_val))
        b = -d / h
        a = 1 - b
        rows[t] = (a, b)
        print(f"  {t:18s} a(sigma) = {mp.nstr(a, 12):>14s}   b(sigma^-1) = {mp.nstr(b, 12):>14s}")

    a_avg, b_avg = rows["averaged"]
    assert abs(a_avg - mp.mpf(1) / 2) < mp.mpf("1e-30"), "averaged must be exactly balanced"
    assert abs(b_avg - mp.mpf(1) / 2) < mp.mpf("1e-30"), "averaged must be exactly balanced"
    print("  -> 'averaged' is EXACTLY (sigma + sigma^-1)/2: no preferred")
    print("     classical representative exists. Classicalising it is a coin flip.")

    a_w, b_w = rows["averaged_weighted"]
    dw = mp.mpf(C.d_for_ctype("averaged_weighted", h_val))
    delta = 4 * (mp.mpf(1) / 2 + dw / h)
    margin = a_w - b_w
    print()
    print(f"  delta = flavor_split_leading(q0) = {mp.nstr(delta, 12)}  (sign {'+' if delta > 0 else '-'})")
    print(f"  a - b = delta/2 = {mp.nstr(margin, 12)}  =  {float(margin) * 100:.4f} %")
    assert delta > 0, "the derivation's direction depends on this sign"
    assert a_w > b_w, "positive crossing must dominate for lk = +1"
    print("  -> the p-n interface HAS a derived classical representative:")
    print("     the POSITIVE crossing, lk = +1, fixed by the sign of delta.")
    print(f"  -> and the preference is {float(margin) * 100:.4f} %. Well-defined,")
    print("     and almost entirely degenerate. An lk-based invariant built on")
    print("     it can be simultaneously well-defined and uninformative.")

    print()
    print("== (B) the two bond sets, and how far the disagreement reaches ==")
    print(f"  {'A':>2s} {'braid chain (A-1)':>18s} {'contact graph C(A,2)':>21s} {'ratio':>7s}")
    for A in (2, 3, 4, 5, 6, 7):
        chain, clique = A - 1, comb(A, 2)
        print(f"  {A:2d} {chain:18d} {clique:21d} {clique / chain:7.2f}")
    print("  They agree only at A = 2, and the contact graph grows ~A/2 faster.")
    print()
    print("  🛑 NOT A NEW FINDING, and the corpus RESOLVED it: see")
    print("  theta_mn_linearchain_vs_allpairs.py -- 'the mba-9b binom(A,2) is")
    print("  superseded by the linear-chain A-1 count', with the body-order")
    print("  aggregate Lean-proved (prop:linear-chain-bond-count). It also")
    print("  records the CHANNEL mapping pp->sigma, pn->averaged, nn->sigma^-1,")
    print("  which qou-k12x did not have. So the count below is not evidence of")
    print("  an unknown inconsistency -- it is a DRAIN backlog: consumers still")
    print("  using a convention the corpus already superseded.")

    # grep-level upper bound, run here so the number is reproducible
    pat = r"comb\(A, ?2\)|C\(A,2\)|clique"
    try:
        out = subprocess.run(
            ["grep", "-rlnE", pat, "--include=*.py", "computations/"],
            cwd=ROOT, capture_output=True, text=True, timeout=120,
        ).stdout
        hits = [ln for ln in out.splitlines() if ln and "_deprecated" not in ln]
        print(f"  grep-level UPPER BOUND on files touching a C(A,2)/clique bond"
              f" set: {len(hits)}")
    except Exception as e:  # pragma: no cover - environment dependent
        print(f"  (grep unavailable: {type(e).__name__})")
    print("  NOT a defect count. A match may use the count for something other")
    print("  than the canonical bond set, or may deliberately compare the two")
    print("  conventions. Deciding which are wrong needs reading each one, and")
    print("  this unit does not do that.")

    print()
    print("== VERDICT ==")
    print("  (A) The classicalisation IS derived, by the sign of the colour")
    print("      splitting -- and by 0.069 %. Both halves matter: an lk of +1")
    print("      for the p-n interface is legitimate, and reading it as a")
    print("      definite crossing throws away almost everything the element is.")
    print("      The unweighted 'averaged' interface has no representative at")
    print("      all, exactly balanced.")
    print()
    print("  (B) The canonical braid's bond set (A-1) and the contact graph's")
    print("      (C(A,2)) diverge from A = 3 onward. The reach is bounded above")
    print("      by the grep count; which consumers are actually wrong is not")
    print("      established here and should not be inferred from it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
