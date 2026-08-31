#!/usr/bin/env python3
"""
nontracial_weight_does_not_restore_rank_probe — the two obstructions on the
binding pairing are INDEPENDENT. Making the state non-tracial (what KMS demands)
leaves the Temperley-Lieb blindness exactly as it was; moving off the canonical
z restores rank but leaves the state a trace. Both knobs must move.

Bean `qou-brng` (with `qou-unqc`), arc `bk-crossing-mass-binding`. Closes the
tempting move left open by #6395 and #6397.

## The two obstructions, from two directions

**#6395 (KMS).** `E_bind = E_0 ln(tr_free/tr_atom)` puts the Markov trace in the
partition-function slot, but a tracial state has trivial modular dynamics and is
KMS only at `beta = 0`. No character-of-a-grading flow gives finite `beta`
against a trace, on `H_n(q)` or on `gr` alike. **The licensing state cannot be
`tr_M`; it must be a NON-TRACIAL weight** -- the live route being
`phi(x) = tr_M(h x)` for positive `h`, with modular flow
`sigma_t(x) = h^{it} x h^{-it}`.

**#6397 (rank).** `<g,g>_{vw} = tr_M(T_v T_w)` has rank `C_n = dim TL_n` at the
canonical `z_D = q^3/(q^2+1)`, exactly and for all `q`, so the pairing is blind
to `n! - C_n` of the algebra. Any `z` off that isolated point is full rank.

## The tempting move, and why it fails

Both point at `tr_M`, so it is natural to hope ONE change fixes both: take
`phi(x) = tr_M(h x)` with `h` outside the centre, and hope the new pairing
`<x,y> = phi(xy) = tr_M(h x y)` is both non-tracial AND non-degenerate.

**It is not.** For INVERTIBLE `h` the map `x |-> h x` is a bijection of `H_n`, so

    radical of  tr_M(h x y)   =   h^{-1} . (radical of tr_M(x y))

-- the same dimension. Twisting by an invertible element permutes the algebra; it
cannot shrink a radical, for the same reason a change of basis cannot change a
rank (#6397 §1).

Measured at the canonical `z_D`:

    h = 1        (the plain Markov trace)        rank  5, 14
    h = T_1      (non-central, invertible)       rank  5, 14
    h = T_1 + 2  (non-central, invertible)       rank  5, 14

`T_1` is invertible in `H_n(q)` because `T_1^2 = h T_1 + 1` gives
`T_1 (T_1 - h) = 1`, and it is non-central for `n >= 3`. So these ARE the
non-tracial weights the KMS argument asks for, and they leave the blindness
untouched.

## The conclusion, and it is a conjunction

The two requirements are **orthogonal**, and neither implies the other:

  * changing `z` restores the rank -- but the Markov trace at ANY `z` is still a
    TRACE, so it does nothing for KMS;
  * a non-tracial `phi(x) = tr_M(h x)` gives finite-temperature modular dynamics
    -- but with invertible `h` it does nothing for the rank.

So a pairing that could source binding must satisfy BOTH, simultaneously: an `h`
outside the centre AND a `z` off the isolated TL point. Neither #6395's route
nor #6397's route is sufficient alone, and this probe exists so nobody spends a
tranche discovering that.

## Scope

Scope **(a)**. No SDP is run, no binding energy computed, and no candidate
`(h, z)` pair is proposed. What is established is that the search space is a
conjunction rather than either of two alternatives.

What is NOT established: the non-invertible case. An `h` that is a
non-unit (a projector, say) certainly changes the radical -- but it can only make
it LARGER, since `x |-> h x` is then not surjective. That direction is not
measured here and is not expected to help; saying so is not the same as having
checked it.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin, convention D.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import importlib.util as _ilu  # noqa: E402
from itertools import permutations  # noqa: E402
from math import comb, factorial  # noqa: E402  # float64-ok: exact int, never float

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -35


def _walk():
    """Reuse the verified Hecke/Markov arithmetic (calibrated at n=3 against
    `pyhecke.gram_matrix_mp` to 4.94e-51 inside that probe)."""
    p = _Path(__file__).resolve().parent / "gg_gram_tower_walk_probe.py"
    if not p.exists():
        raise SystemExit("gg_gram_tower_walk_probe.py not found (landed in #6396)")
    spec = _ilu.spec_from_file_location("_ggwalk", p)
    m = _ilu.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def catalan(k):
    return comb(2 * k, k) // (k + 1)


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    m = _walk()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    hq = q0 - 1 / q0
    zD = q0**3 / (q0**2 + 1)

    def elt_mul(a, b, n):
        """General element x general element."""
        out = {}
        for bw, bc in b.items():
            for k, c in m.mul(a, bw, n, hq).items():
                out[k] = out.get(k, mp.mpf(0)) + c * bc
        return out

    def gram_h(n, z, helt):
        """<x,y> = tr_M(h . x y) on the length-ordered NF basis."""
        B = sorted(permutations(range(n)), key=lambda w: (m.inv_count(w), w))
        memo = {}
        G = [[mp.mpf(0)] * len(B) for _ in B]
        for i, v in enumerate(B):
            hv = elt_mul(helt, {v: mp.mpf(1)}, n)
            for j, w in enumerate(B):
                G[i][j] = m.tr_M(m.mul(hv, w, n, hq), n, hq, z, memo)
        return G

    print("nontracial_weight_does_not_restore_rank_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 20)}   z_D = {fmt(zD, 14)}   [convention D]")
    print()
    print("TWO OBSTRUCTIONS, from two directions:")
    print("  #6395 (KMS)  the licensing state cannot be tr_M -- it must be a")
    print("               NON-TRACIAL weight phi(x) = tr_M(h x).")
    print("  #6397 (rank) <g,g> = tr_M(T_v T_w) has rank C_n at the canonical")
    print("               z_D, so it is blind to n! - C_n of the algebra.")
    print()
    print("THE TEMPTING MOVE: both point at tr_M, so hope ONE change fixes both --")
    print("take h outside the centre and get non-traciality AND full rank at once.")
    print()

    print("THE TEST — rank of <x,y> = tr_M(h . x y) at the canonical z_D")
    print("-" * 78)
    # T_1 is invertible: T_1^2 = h T_1 + 1  =>  T_1 (T_1 - h) = 1. Checked, not
    # asserted, before it is used as an "invertible" witness.
    n_chk = 3
    t1 = m.t_word(m.s_i(n_chk, 1), n_chk, hq)
    inv = dict(t1)
    idn = tuple(range(n_chk))
    inv[idn] = inv.get(idn, mp.mpf(0)) - hq
    prod = elt_mul(t1, inv, n_chk)
    off = mp.fsum(abs(c) for w, c in prod.items() if w != idn)
    print(f"  invertibility of T_1 checked: T_1 (T_1 - h) = 1 ?  "
          f"identity coeff {fmt(prod.get(idn, mp.mpf(0)), 10)}, "
          f"off-identity mass {fmt(off, 6)}")
    assert abs(prod.get(idn, mp.mpf(0)) - 1) < mp.mpf(10) ** -40 and \
        off < mp.mpf(10) ** -40, "T_1 must be invertible with inverse T_1 - h"
    print()
    print(f"{'h':>40} {'n=3':>6} {'n=4':>6}   {'C_n = 5 / 14':>14}")
    ranks = {}
    for label in ("1 (the plain Markov trace)",
                  "T_1 (non-central, invertible)",
                  "T_1 + 2 (non-central, invertible)"):
        rs = []
        for n in (3, 4):
            i_n = tuple(range(n))
            if label.startswith("1 "):
                he = {i_n: mp.mpf(1)}
            else:
                he = dict(m.t_word(m.s_i(n, 1), n, hq))
                if "+ 2" in label:
                    he[i_n] = he.get(i_n, mp.mpf(0)) + 2
            r, _, _ = m.rank_and_radical(gram_h(n, zD, he), TOL)
            rs.append(r)
        ranks[label] = rs
        print(f"{label:>40} {rs[0]:>6} {rs[1]:>6}")
    print()
    base = ranks["1 (the plain Markov trace)"]
    assert base == [catalan(3), catalan(4)], "the plain form must be rank C_n"
    for label, rs in ranks.items():
        assert rs == base, f"twisting by {label} must not change the rank"
    print("  IDENTICAL.  Twisting by a non-central INVERTIBLE element does not")
    print("  move the rank by one.")
    print()
    print("  The reason, and it is the same one as #6397 section 1: for")
    print("  invertible h the map x |-> h x is a BIJECTION of H_n, so")
    print("      radical of tr_M(h x y)  =  h^{-1} . (radical of tr_M(x y))")
    print("  -- same dimension.  A unit permutes the algebra; it cannot shrink a")
    print("  radical, exactly as a change of basis cannot change a rank.")
    print()

    print("THE CONCLUSION — a CONJUNCTION, not two alternatives")
    print("-" * 78)
    print("  * changing z restores the rank -- but the Markov trace at ANY z is")
    print("    still a TRACE, so it does nothing for KMS;")
    print("  * a non-tracial phi(x) = tr_M(h x) gives finite-temperature modular")
    print("    dynamics -- but with invertible h it does nothing for the rank.")
    print()
    print("  Neither route is sufficient alone.  A pairing that could source")
    print("  binding must satisfy BOTH simultaneously: an h OUTSIDE THE CENTRE")
    print("  and a z OFF the isolated TL point.  This probe exists so that nobody")
    print("  spends a tranche discovering that.")
    print()
    print("WHAT IS NOT ESTABLISHED")
    print("-" * 78)
    print("  * The NON-INVERTIBLE case.  An h that is not a unit (a projector,")
    print("    say) certainly changes the radical -- but x |-> h x is then not")
    print("    surjective, so it can only make the radical LARGER.  That")
    print("    direction is not measured here and is not expected to help;")
    print("    saying so is not the same as having checked it.")
    print("  * No candidate (h, z) pair is proposed, no SDP is run, and no")
    print("    binding energy is computed.  What is established is the SHAPE of")
    print("    the search space, not a point in it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
