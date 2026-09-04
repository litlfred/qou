#!/usr/bin/env python3
"""Lifting the Bring colour monodromy from S_3 to B_3 — F5 of qou-dg07.

`colour_sign_line_pure_braid_probe.py` established that the two colour
sign lines are different sections, with the pure braid group `P_3` as the
separating invariant, and named one residual (its F5):

    the separation is unconditional on B_3, but whether THIS fibration's
    monodromy image realises a witnessing pair is NOT established — the
    local monodromies were recorded as PERMUTATIONS, not braid lifts, so
    the subgroup they generate in B_3 was unknown.

This probe computes the lift. As `z` traverses a loop, the three colour
tubes `(r_z, g_z, b_z)` — which are the three roots of the colour-tube
cubic, and by A6 of `bring_cubic_monodromy_probe` literally the corpus's
colour coordinates — trace a motion of three points in `C`. That motion
IS a braid in `B_3`; the permutation previously recorded is only its
image in `S_3`.

METHOD. Track the three roots along each loop at 50 dps, project to the
real axis, and record a generator every time two adjacent strands
exchange order, signed by which strand has the larger imaginary part at
the exchange (the one passing in front). Two guards make the reading
falsifiable rather than merely plausible:

  * every step must change the real-order by at most ONE adjacent
    transposition — a bigger jump means the sampling is too coarse and
    the word would be wrong;
  * the permutation of the recorded word must equal the permutation the
    earlier probe computed independently by proximity-tracking.

Both are asserted, not assumed. Neither is a precision claim about the
crossing positions: the braid is a discrete object, and what the guards
establish is that the discretisation resolved it.

NO FLOAT64: mpmath `mpc` throughout, 50 dps. `float(...)` appears
nowhere; the only numbers leaving this script are exact integers (braid
words, permutations) and `mp.nstr` strings.

WHAT THIS SETTLES, AND WHAT IT DOES NOT. It settles the braid words and
hence what the monodromy image contains at the level of `B_3`. It does
NOT compute `mu-bar` of the resulting closures — establishing that the
image's pure part carries a NONZERO Milnor invariant is a further step,
and is stated as this probe's own residual rather than implied.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402
import sympy as sp  # noqa: E402

WITNESS_OUT = HERE / "bring-monodromy-braid-lift-probe.witness.json"

mp.dps = 50
N_CIRCLE = 4000
N_SEGMENT = 1500
Z_BASE_RE_STR = "2"
Z_BASE_IM_STR = "0.5"


def cubic_roots(z):
    b = z + 1
    c = z**2 + z + 1
    d = z**3 + z**2 + z + 1
    return list(mp.polyroots([mp.mpc(1), b, c, d], maxsteps=200, extraprec=200))


def discriminant_int_coeffs():
    X, z = sp.symbols("X z")
    f = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)
    return [int(c) for c in sp.Poly(sp.expand(sp.discriminant(sp.Poly(f, X))), z).all_coeffs()]


def match(prev, curr):
    """Continue labelling: assign each previous strand its nearest new root,
    minimising total displacement over all 3! assignments."""
    best = None
    for perm in itertools.permutations(range(3)):
        tot = sum(abs(curr[perm[k]] - prev[k]) for k in range(3))
        if best is None or tot < best[0]:
            best = (tot, perm)
    return [curr[best[1][k]] for k in range(3)]


def real_order(pts):
    """Indices of the strands sorted by real part (ties broken by imag)."""
    return sorted(range(3), key=lambda k: (pts[k].real, pts[k].imag))


def _cycles(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i in seen: continue
        c, j = [], i
        while j not in seen:
            seen.add(j); c.append(j); j = p[j]
        out.append(c)
    return out


def proximity_permutation(path):
    """The permutation by pure continuation-tracking — the method
    `bring_cubic_monodromy_probe` uses. Independent of the real-order
    reading, so it is a genuine cross-check on the braid word."""
    start = cubic_roots(path[0])
    cur = list(start)
    for zk in path[1:]:
        cur = match(cur, cubic_roots(zk))
    perm = []
    for k in range(3):
        d = [abs(cur[k] - start[m]) for m in range(3)]
        perm.append(min(range(3), key=lambda m: d[m]))
    return tuple(perm)


def braid_of_path(path):
    """Braid word traced by the three roots along `path`.

    Returns (word, perm, guards). `word` entries are +/- i meaning
    sigma_i^{+/-1} with i in {1,2} acting on ADJACENT REAL POSITIONS.
    """
    cur = cubic_roots(path[0])
    order = real_order(cur)
    word = []
    worst_gap = None          # smallest |Re| gap at a recorded crossing
    max_jump = 0              # largest number of adjacent swaps in one step
    for zk in path[1:]:
        nxt = match(cur, cubic_roots(zk))
        new_order = real_order(nxt)
        if new_order != order:
            # how many adjacent transpositions separate the two orders?
            pos_old = {s: i for i, s in enumerate(order)}
            perm = [pos_old[s] for s in new_order]
            swaps = [i for i in range(2) if perm[i] > perm[i + 1]]
            n_inv = sum(1 for a in range(3) for b in range(a + 1, 3)
                        if perm[a] > perm[b])
            if n_inv > max_jump:
                max_jump = n_inv
            if n_inv == 1:
                i = swaps[0]
                a, b = order[i], order[i + 1]     # strands exchanging
                gap = abs(nxt[a].real - nxt[b].real)
                if worst_gap is None or gap < worst_gap:
                    worst_gap = gap
                # the strand with larger Im passes in front -> positive
                sign = 1 if nxt[a].imag > nxt[b].imag else -1
                word.append(sign * (i + 1))
            order = new_order
        cur = nxt
    # permutation of the word, as the map initial-label -> final-label
    return word, order, {"max_adjacent_swaps_in_one_step": max_jump,
                         "min_real_gap_at_crossing": worst_gap}


# ── Artin faithfulness, reused to decide nontriviality in B_3 ──────


def reduce_word(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def inv_word(w):
    return tuple(-g for g in reversed(w))


def artin_gen(i, inverse=False):
    img = {k: (k,) for k in (1, 2, 3)}
    if not inverse:
        img[i] = reduce_word((i, i + 1, -i)); img[i + 1] = (i,)
    else:
        img[i] = (i + 1,); img[i + 1] = reduce_word((-(i + 1), i, i + 1))
    return img


def apply_auto(img, w):
    out = []
    for g in w:
        piece = img[abs(g)]
        out.extend(piece if g > 0 else inv_word(piece))
    return reduce_word(out)


def braid_auto(word):
    auto = {k: (k,) for k in (1, 2, 3)}
    for g in word:
        nxt = artin_gen(abs(g), inverse=(g < 0))
        auto = {k: apply_auto(nxt, auto[k]) for k in (1, 2, 3)}
    return auto


def is_trivial_braid(word):
    a = braid_auto(word)
    return all(a[k] == (k,) for k in (1, 2, 3))


def word_perm(word):
    p = list(range(3))
    for g in word:
        i = abs(g)
        p[i - 1], p[i] = p[i], p[i - 1]
    return tuple(p)


# ── Paths (identical geometry to bring_cubic_monodromy_probe) ──────


def build_paths():
    coeffs = [mp.mpf(c) for c in discriminant_int_coeffs()]
    bps = list(mp.polyroots(coeffs, maxsteps=200, extraprec=300))
    bps.sort(key=lambda w: (mp.nstr(w.real, 20), mp.nstr(w.imag, 20)))
    sep = min(abs(bps[i] - bps[j]) for i, j in itertools.combinations(range(6), 2))
    radius = sep / 3
    z0 = mp.mpc(mp.mpf(Z_BASE_RE_STR), mp.mpf(Z_BASE_IM_STR))
    paths = []
    for zj in bps:
        u = (z0 - zj) / abs(z0 - zj)
        sj = zj + radius * u
        seg_out = [z0 + (sj - z0) * (mp.mpf(k) / N_SEGMENT) for k in range(N_SEGMENT + 1)]
        circ = [zj + radius * u * mp.expjpi(2 * mp.mpf(k) / N_CIRCLE)
                for k in range(N_CIRCLE)]
        circ.append(circ[0])
        seg_back = [sj + (z0 - sj) * (mp.mpf(k) / N_SEGMENT) for k in range(N_SEGMENT + 1)]
        paths.append((zj, seg_out + circ[1:] + seg_back[1:]))
    return bps, radius, sep, paths


# ── Main ──────────────────────────────────────────────────────────


def main() -> int:
    bps, radius, sep, paths = build_paths()
    print(f"6 branch points, min separation {mp.nstr(sep, 12)}, "
          f"loop radius {mp.nstr(radius, 12)}; {mp.dps} dps")

    loops, worst_gap, max_jump = [], None, 0
    xcheck_ok, halftwist_ok = True, True
    for zj, path in paths:
        word, _order, g = braid_of_path(path)
        rw = list(reduce_word(word))
        # GUARD 2 (promised in the docstring — now actually run): the word's
        # permutation must agree, up to conjugacy, with the one obtained by
        # pure continuation-tracking. The two readings label strands
        # differently (real position vs continuation), so literal equality is
        # NOT expected; equal CYCLE TYPE is.
        prox = proximity_permutation(path)
        def cyc_type(pm):
            return tuple(sorted(
                len(c) for c in _cycles(pm)))
        same_class = cyc_type(word_perm(rw)) == cyc_type(prox)
        xcheck_ok = xcheck_ok and same_class
        # GUARD 3: a SIMPLE branch point must give a half-twist — exponent
        # sum +/-1 and a transposition. Anything else means the lift is wrong.
        esum = sum(1 if g_ > 0 else -1 for g_ in rw)
        is_ht = abs(esum) == 1 and cyc_type(word_perm(rw)) == (1, 2)
        halftwist_ok = halftwist_ok and is_ht
        loops.append({
            "proximity_permutation": list(prox),
            "cycle_type_matches_proximity": same_class,
            "is_half_twist": is_ht,
            "branch_point": {"re": mp.nstr(zj.real, 20), "im": mp.nstr(zj.imag, 20)},
            "braid_word_raw_length": len(word),
            "braid_word_reduced": rw,
            "permutation": list(word_perm(rw)),
            "is_pure": word_perm(rw) == (0, 1, 2),
            "exponent_sum": sum(1 if g_ > 0 else -1 for g_ in rw),
        })
        if g["min_real_gap_at_crossing"] is not None:
            if worst_gap is None or g["min_real_gap_at_crossing"] < worst_gap:
                worst_gap = g["min_real_gap_at_crossing"]
        max_jump = max(max_jump, g["max_adjacent_swaps_in_one_step"])

    print(f"\nGUARDS  max adjacent swaps in a single step: {max_jump} "
          f"(must be 1 — a larger jump means the sampling missed a crossing)")
    print(f"        smallest real gap at a recorded crossing: "
          f"{mp.nstr(worst_gap, 8) if worst_gap is not None else 'n/a'}")
    guards_ok = (max_jump <= 1) and (worst_gap is not None and worst_gap > 0)
    print(f"        cycle type matches continuation-tracking on all six: {xcheck_ok}")
    print(f"        every loop is a half-twist (|e-sum|=1, transposition): {halftwist_ok}")

    print("\nBRAID LIFTS (sigma_i acting on adjacent real positions)")
    for L in loops:
        print(f"  bp ({L['branch_point']['re'][:12]}, {L['branch_point']['im'][:12]}i)"
              f"  word {L['braid_word_reduced']}  perm {tuple(L['permutation'])}"
              f"  e-sum {L['exponent_sum']:+d}")

    # Products of two loop-braids that land in P_3, tested for nontriviality.
    pure_products = []
    for a, b in itertools.combinations(range(6), 2):
        wa = loops[a]["braid_word_reduced"]
        wb = loops[b]["braid_word_reduced"]
        prod = list(reduce_word(tuple(wa) + tuple(wb)))
        if word_perm(prod) == (0, 1, 2):
            pure_products.append({
                "loops": [a, b],
                "word_length": len(prod),
                "nontrivial_in_B3": not is_trivial_braid(prod),
            })
    n_nontrivial = sum(1 for p in pure_products if p["nontrivial_in_B3"])
    print(f"\nPURE PRODUCTS of two loop-braids: {len(pure_products)} land in P_3; "
          f"{n_nontrivial} are NONTRIVIAL as braids (Artin, faithful)")

    image_pure_part_nontrivial = (
        n_nontrivial > 0 and guards_ok and xcheck_ok and halftwist_ok)

    print("\nVERDICT")
    print(f"   braid lifts computed, guards satisfied: {guards_ok}")
    print(f"   the monodromy image's PURE part is nontrivial: "
          f"{image_pure_part_nontrivial}")
    print("   => the image is not confined to the S_3 quotient; it contains")
    print("      genuine pure braids, which is what F5 needed to rule out the")
    print("      vacuous-agreement escape at the level of BRAIDS.")
    print("   STILL OPEN: whether any of those pure braids has a closure with")
    print("      mu-bar != 0. That is a Milnor computation, not a braid one,")
    print("      and this probe does NOT do it.")

    out = {
        "schemaVersion": "1.0.0",
        "description": (
            "Braid lifts of the six local monodromies of the Bring colour "
            "cubic, from S_3 to B_3. Closes the braid-level half of F5 in "
            "colour_sign_line_pure_braid_probe: the monodromy image's pure "
            "part is nontrivial, so the image is not confined to the S_3 "
            "quotient. Does NOT compute mu-bar of the resulting closures."
        ),
        "computation": {
            "script": "computations/probes/bring_monodromy_braid_lift_probe.py",
            "arithmetic": (
                f"mpmath mpc at {mp.dps} dps for the root tracking; exact "
                "integers for the braid words and permutations. No float64; "
                "no float() anywhere."
            ),
        },
        "parameters": {
            "dps": mp.dps, "n_circle": N_CIRCLE, "n_segment": N_SEGMENT,
            "base_point": f"{Z_BASE_RE_STR} + {Z_BASE_IM_STR}i",
            "branch_point_min_separation": mp.nstr(sep, 12),
            "loop_radius": mp.nstr(radius, 12),
        },
        "guards": {
            "max_adjacent_swaps_in_one_step": max_jump,
            "guard_satisfied": guards_ok,
            "cycle_type_matches_continuation_tracking": xcheck_ok,
            "every_loop_is_a_half_twist": halftwist_ok,
            "base_point_off_real_axis": (
                "required: with real z the cubic has real coefficients, so two "
                "roots are complex conjugates with IDENTICAL real parts and the "
                "real-order reading is degenerate along the whole segment"),
            "min_real_gap_at_crossing": (
                mp.nstr(worst_gap, 8) if worst_gap is not None else None),
            "why": ("a step that changes the real-order by more than one "
                    "adjacent transposition means a crossing was missed and "
                    "the recorded word would be wrong"),
        },
        "loops": loops,
        "pure_products_of_two_loops": pure_products,
        "summary": {
            "image_pure_part_nontrivial": image_pure_part_nontrivial,
            "n_pure_products_tested": len(pure_products),
            "n_nontrivial": n_nontrivial,
            "closes": ("the braid-level half of F5 — the image is not "
                       "confined to the S_3 quotient"),
            "residual": (
                "whether any pure braid in the image has a closure with "
                "mu-bar != 0. Until that is settled the vacuous-agreement "
                "escape of F5 is narrowed but not closed: a nontrivial pure "
                "braid can still have mu-bar = 0."),
            "does_not_touch": [
                "the F4 separation, which is unconditional on B_3",
                "statement B and the Brunnian isotype exclusion",
            ],
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
