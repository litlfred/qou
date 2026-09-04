#!/usr/bin/env python3
"""Independent verification of the Bring colour-monodromy braid lift, by a
different route — the full-twist consistency check and SL(2,Z) generation.

Bean `qou-xhih` (Front 1 of `qou-icj2`). A sibling branch (PR #6449, bean
`qou-dg07`) has already lifted the six local monodromies of the Bring
colour cubic

    f(X, z) = X^3 + (z+1) X^2 + (z^2+z+1) X + (z^3+z^2+z+1)

from `S_3` to `B_3` — `computations/probes/bring_monodromy_braid_lift_probe.py`
— and concluded (`colour_mu_bar_monodromy_probe.py`, audit
`docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md` §10–§11)
that the image is all of `B_3`, by exhibiting `sigma_1 = g_0^{-1}` and
`sigma_2^{-1} = g_0^{-1} g_1 g_0` as words in the loop lifts. Per the
parallel-work policy this probe does NOT re-derive that; it VERIFIES it by a
route that shares as little as possible with theirs, and adds a consistency
check neither of their probes has.

WHAT IS DIFFERENT HERE.

  * Braid reader. The sibling reads crossings off the REAL-AXIS projection,
    and its first version was wrong precisely because that projection is
    degenerate for real `z` (conjugate roots share a real part). This probe
    projects the three roots onto a GENERIC direction `e^{i theta}`,
    `theta = 37/100` rad (exact rational, stored), so that degeneracy cannot
    recur at any real `z`: the u-coordinates of a conjugate pair differ by
    `2 Im(w) sin(theta)`.
  * Base point `z_0 = 5/2 + 3i/4` — off the real axis (as theirs), and
    different from theirs (`2 + i/2`), so the lassos are different loops and
    the lifts are expected to agree only UP TO CONJUGACY in `B_3`.
  * Conjugacy is decided in two layers: a NECESSARY condition (equal
    exponent sum, equal `S_3` cycle type, equal characteristic polynomial of
    the reduced Burau matrix over `Q(t)`), and a SUFFICIENT one — an explicit
    conjugator `c` with `c w c^{-1} = s`, found by search over words of
    length <= 6 and checked by equality of Artin automorphisms of `F_3`
    (faithful). Where the sufficient check succeeds, conjugacy is PROVED.

THE NEW CHECK (neither sibling probe has it). The six lassos, multiplied in
the angular order seen from the base point, form a loop homotopic to a
large circle enclosing all six branch points. That circle's braid is
computed INDEPENDENTLY by direct transport around `|z - z_0| = 4`, and by
fact A5 of `bring_cubic_monodromy_probe` (unramified at infinity) its
permutation must be trivial; at large `|z|` the roots are `z * (roots of
Y^3 + Y^2 + Y + 1)`, so one turn of `z` turns all three roots once and the
braid must be a FULL TWIST `Delta^{+-2}`, `Delta^2 = (sigma_1 sigma_2)^3`.
The probe asserts (Artin action) that

    (product of the six lifts, in angular order)  ==  (large-circle braid)
                                                  ==  Delta^{2k}, k = +-1,

which constrains the six words jointly in a way that per-loop half-twist
checks cannot: any single wrong word breaks it. The same product test is
then applied to the SIBLING's six words, in the angular order from THEIR
base point, which tests their words without re-reading them.

GENERATION, BY SL(2,Z) INSTEAD OF WORD SEARCH. Reduced Burau at `t = -1`,

    sigma_1 |-> A = [[1, 1], [0, 1]],    sigma_2 |-> B = [[1, 0], [-1, 1]],

is checked to satisfy `ABA = BAB` and `(ABA)^2 = -I`, so it is the standard
surjection `rho : B_3 -> SL(2,Z)` with `rho(Delta^2) = -I` and kernel
`<Delta^4>` (a standard fact, IMPORTED not verified: Magnus 1934; Milnor,
*Introduction to Algebraic K-theory*, §10). The images of the six lifts are
shown to generate `SL(2,Z)` by exhibiting `S = [[0,-1],[1,0]]` and
`T = [[1,1],[0,1]]` as explicit products (BFS). Then for `H = <lifts>`:

    rho(H) = SL(2,Z)  and  Delta^2 in H  (from the full-twist check)
    ==>  for any g in B_3 pick h in H with rho(h) = rho(g);
         g h^{-1} in ker rho = <Delta^4> <= <Delta^2> <= H,  so  g in H.
    ==>  H = B_3.

This reproduces the sibling's "image is B_3" conclusion without using
their two generator words, and states exactly which external fact it
rests on (the kernel of `rho`).

WHAT THIS DOES NOT TOUCH. Statement B of the audit (that the baryon state
occupies the sign isotype) has its premise unchanged; nothing here is a
`mu-bar` computation; and the sheets-are-colour-tubes identification (A6)
is consumed, not re-derived.

NO FLOAT64. mpmath `mpc` at 50 dps for the transport; exact integers for
words, permutations and matrices; sympy over `Q(t)` for Burau. `float(`
appears nowhere; the witness carries strings and integers only.

Sign convention (stated, since it decides the sign of everything below):
strands are ordered by `u = Re(w e^{-i theta})`; when the strands in
adjacent positions `i, i+1` exchange, the letter is `sigma_i^{+1}` if the
strand that was on the LEFT (smaller `u`) has the larger `v = Im(w e^{-i theta})`
at the exchange — i.e. passes IN FRONT — and `sigma_i^{-1}` otherwise. This
is the sibling's convention with the real axis rotated to `e^{i theta}`.
Under it a counter-clockwise half-turn of two roots is `sigma^{-1}`, so a
positively oriented loop around a simple branch point is expected to give
exponent sum `-1`, and a positively oriented turn of all three roots gives
`Delta^{-2}`.

Artin-representation and free-reduction helpers are re-implemented below
with the same semantics as the sibling's (`artin_gen`, `apply_auto`,
`braid_auto`) so that "equal in B_3" means the same thing in both probes.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
import time
from collections import deque
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

WITNESS_OUT = HERE / "bring-monodromy-full-twist-probe.witness.json"

mp.dps = 50
N_CIRCLE = 4000          # samples on each small loop around a branch point
N_SEGMENT = 1500         # samples on each radial segment
N_BIG_CIRCLE = 8000      # samples on the large circle
N_BIG_SEGMENT = 2000     # samples on the segment out to the large circle
THETA = Fraction(37, 100)              # projection direction, exact
Z_BASE = (Fraction(5, 2), Fraction(3, 4))   # base point, exact
R_BIG = 4                              # large-circle radius, exact
CONJUGATOR_MAX_LEN = 6
SL2Z_BFS_MAX_DEPTH = 8

# The sibling's six reduced loop words and base point, copied from
# `bring-monodromy-braid-lift-probe.witness.json` on
# origin/claude/colour-sign-line-canonical-2026-09-03 (PR #6449), loops
# indexed by the same (Re, Im)-sorted branch-point order used below.
SIBLING_WORDS = [
    (-1,),
    (2, -1, -2),
    (2, -1, -2),
    (-1,),
    (2, 1, -2, -1, -2),
    (-1, -2, 1),
]
SIBLING_BASE = (Fraction(2), Fraction(1, 2))
SIBLING_PROBE = "computations/probes/bring_monodromy_braid_lift_probe.py"


def _mpf(fr: Fraction):
    return mp.mpf(fr.numerator) / fr.denominator


# ── the cubic and its branch points ───────────────────────────────


def cubic_roots(z):
    return list(mp.polyroots([mp.mpc(1), z + 1, z**2 + z + 1,
                              z**3 + z**2 + z + 1],
                             maxsteps=200, extraprec=200))


def discriminant_int_coeffs():
    X, z = sp.symbols("X z")
    f = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)
    return [int(c) for c in
            sp.Poly(sp.expand(sp.discriminant(sp.Poly(f, X))), z).all_coeffs()]


def branch_points():
    coeffs = [mp.mpf(c) for c in discriminant_int_coeffs()]
    bps = list(mp.polyroots(coeffs, maxsteps=200, extraprec=300))
    bps.sort(key=lambda w: (w.real, w.imag))
    return bps


# ── transport with the same guard as bring_cubic_monodromy_probe ──


def match(prev, curr):
    best = None
    for perm in itertools.permutations(range(3)):
        tot = sum(abs(curr[perm[k]] - prev[k]) for k in range(3))
        if best is None or tot < best[0]:
            best = (tot, perm)
    return [curr[best[1][k]] for k in range(3)]


def min_sep(pts):
    return min(abs(pts[i] - pts[j]) for i, j in itertools.combinations(range(3), 2))


# ── the generic-direction braid reader ────────────────────────────

EMITH = None   # e^{-i theta}, set in main after mp.dps


def proj(w):
    t = w * EMITH
    return t.real, t.imag


def u_order(pts):
    return sorted(range(3), key=lambda k: proj(pts[k])[0])


def braid_of_path(path):
    """Braid word of the three roots along `path`, read through the
    projection onto e^{i theta}. Letters +-i mean sigma_i^{+-1}, i in {1,2},
    acting on adjacent u-positions. Returns (word, guards)."""
    cur = cubic_roots(path[0])
    order = u_order(cur)
    word = []
    worst_gap = None
    max_jump = 0
    worst_ratio = mp.mpf(0)
    for zk in path[1:]:
        raw = cubic_roots(zk)
        nxt = match(cur, raw)
        ratio = max(abs(nxt[k] - cur[k]) for k in range(3)) / min_sep(nxt)
        if ratio > worst_ratio:
            worst_ratio = ratio
        new_order = u_order(nxt)
        if new_order != order:
            pos_old = {s: i for i, s in enumerate(order)}
            perm = [pos_old[s] for s in new_order]
            n_inv = sum(1 for a in range(3) for b in range(a + 1, 3)
                        if perm[a] > perm[b])
            max_jump = max(max_jump, n_inv)
            if n_inv == 1:
                i = [k for k in range(2) if perm[k] > perm[k + 1]][0]
                a, b = order[i], order[i + 1]          # a was on the left
                ua, va = proj(nxt[a])
                ub, vb = proj(nxt[b])
                gap = abs(ua - ub)
                if worst_gap is None or gap < worst_gap:
                    worst_gap = gap
                sign = 1 if va > vb else -1            # left strand in front => +
                word.append(sign * (i + 1))
            order = new_order
        cur = nxt
    return word, {"max_adjacent_swaps_in_one_step": max_jump,
                  "min_u_gap_at_crossing": worst_gap,
                  "worst_step_over_separation": worst_ratio}


# ── free reduction, Artin action (re-implemented after the sibling) ─


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


def braids_equal(u, v):
    return braid_auto(u) == braid_auto(v)


def word_perm(word):
    p = list(range(3))
    for g in word:
        i = abs(g)
        p[i - 1], p[i] = p[i], p[i - 1]
    return tuple(p)


def cycle_type(p):
    seen, out = set(), []
    for i in range(3):
        if i in seen:
            continue
        n, j = 0, i
        while j not in seen:
            seen.add(j); n += 1; j = p[j]
        out.append(n)
    return tuple(sorted(out))


def exp_sum(w):
    return sum(1 if g > 0 else -1 for g in w)


DELTA2 = (1, 2, 1, 2, 1, 2)


def delta_power(k):
    return DELTA2 * k if k >= 0 else inv_word(DELTA2) * (-k)


def which_full_twist(word, kmax=4):
    for k in range(-kmax, kmax + 1):
        if braids_equal(word, delta_power(k)):
            return k
    return None


def find_conjugator(w, s, max_len=CONJUGATOR_MAX_LEN):
    """Search c with |c| <= max_len and c w c^{-1} = s in B_3 (Artin)."""
    target = braid_auto(s)
    seen = set()
    frontier = [()]
    for _ in range(max_len + 1):
        nxt = []
        for c in frontier:
            if c in seen:
                continue
            seen.add(c)
            if braid_auto(c + tuple(w) + inv_word(c)) == target:
                return c
            for g in (1, -1, 2, -2):
                cc = reduce_word(c + (g,))
                if cc not in seen:
                    nxt.append(cc)
        frontier = nxt
    return None


# ── reduced Burau over Q(t) ───────────────────────────────────────

T_SYM = sp.symbols("t")


def burau_gen(g):
    t = T_SYM
    if abs(g) == 1:
        M = sp.Matrix([[-t, 1], [0, 1]])
    else:
        M = sp.Matrix([[1, 0], [t, -t]])
    return M if g > 0 else M.inv()


def burau(word):
    M = sp.eye(2)
    for g in word:
        M = M * burau_gen(g)
    return sp.simplify(M)


def burau_charpoly_str(word):
    lam = sp.symbols("lambda")
    cp = sp.factor(sp.simplify(burau(word).charpoly(lam).as_expr()))
    return sp.sstr(cp)


# ── SL(2,Z) at t = -1 ─────────────────────────────────────────────


def mat_mul(a, b):
    return (a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3])


def mat_inv(a):
    # det = 1
    return (a[3], -a[1], -a[2], a[0])


A_MAT = (1, 1, 0, 1)      # sigma_1
B_MAT = (1, 0, -1, 1)     # sigma_2
I_MAT = (1, 0, 0, 1)
S_MAT = (0, -1, 1, 0)
T_MAT = (1, 1, 0, 1)


def sl2_of_word(word):
    M = I_MAT
    for g in word:
        base = A_MAT if abs(g) == 1 else B_MAT
        M = mat_mul(M, base if g > 0 else mat_inv(base))
    return M


def bfs_sl2(gens, targets, max_depth):
    """BFS over the group generated by `gens` (matrices with names);
    returns {target: word-in-generators} for those found."""
    start = I_MAT
    parent = {start: None}
    frontier = deque([(start, 0)])
    found = {}
    alts = []
    for name, M in gens:
        alts.append((name, M))
        alts.append((name + "^-1", mat_inv(M)))
    while frontier:
        M, d = frontier.popleft()
        for tname, tM in targets.items():
            if M == tM and tname not in found:
                # reconstruct
                path, cur = [], M
                while parent[cur] is not None:
                    prev, gname = parent[cur]
                    path.append(gname); cur = prev
                found[tname] = list(reversed(path))
        if len(found) == len(targets):
            break
        if d >= max_depth:
            continue
        for gname, gM in alts:
            N = mat_mul(M, gM)
            if N not in parent:
                parent[N] = (M, gname)
                frontier.append((N, d + 1))
    return found


# ── geometry ──────────────────────────────────────────────────────


def lasso(z0, zj, radius, n_seg, n_circ):
    u = (z0 - zj) / abs(z0 - zj)
    sj = zj + radius * u
    seg_out = [z0 + (sj - z0) * (mp.mpf(k) / n_seg) for k in range(n_seg + 1)]
    circ = [zj + radius * u * mp.expjpi(2 * mp.mpf(k) / n_circ)
            for k in range(n_circ)]
    circ.append(circ[0])
    seg_back = [sj + (z0 - sj) * (mp.mpf(k) / n_seg) for k in range(n_seg + 1)]
    return seg_out + circ[1:] + seg_back[1:]


def big_loop(z0, R, n_seg, n_circ):
    p0 = z0 + R
    seg_out = [z0 + (p0 - z0) * (mp.mpf(k) / n_seg) for k in range(n_seg + 1)]
    circ = [z0 + R * mp.expjpi(2 * mp.mpf(k) / n_circ) for k in range(n_circ)]
    circ.append(circ[0])
    seg_back = [p0 + (z0 - p0) * (mp.mpf(k) / n_seg) for k in range(n_seg + 1)]
    return seg_out + circ[1:] + seg_back[1:]


def seg_point_dist(a, b, p):
    """Distance from p to segment [a, b]."""
    ab = b - a
    t = ((p - a) * mp.conj(ab)).real / abs(ab) ** 2
    t = max(mp.mpf(0), min(mp.mpf(1), t))
    return abs(a + t * ab - p)


def angular_order(z0, bps):
    """Loop indices sorted by the argument of (bp - z0) measured relative to
    the direction from z0 to the centroid of the branch points, so that the
    ordering does not wrap through +-pi."""
    c = sum(bps) / len(bps)
    ref = (c - z0) / abs(c - z0)
    rel = [mp.arg((b - z0) / ref) for b in bps]
    idx = sorted(range(len(bps)), key=lambda j: rel[j])
    return idx, rel


def fail(msg):
    print(f"\nASSERTION FAILED: {msg}")
    raise SystemExit(1)


# ── main ──────────────────────────────────────────────────────────


def main() -> int:
    global EMITH
    t_start = time.monotonic()
    EMITH = mp.expj(-_mpf(THETA))
    z0 = mp.mpc(_mpf(Z_BASE[0]), _mpf(Z_BASE[1]))
    bps = branch_points()
    sep = min(abs(bps[i] - bps[j]) for i, j in itertools.combinations(range(6), 2))
    radius = sep / 3
    print(f"Bring colour cubic: 6 branch points, min separation {mp.nstr(sep, 12)}, "
          f"lasso radius {mp.nstr(radius, 12)}; base point {Z_BASE[0]} + {Z_BASE[1]} i; "
          f"projection direction theta = {THETA} rad; {mp.dps} dps")

    # Clearance: no lasso segment enters another branch point's disc; the
    # base point lies outside every disc; the large circle encloses all six.
    clearance = None
    for j, zj in enumerate(bps):
        for m, zm in enumerate(bps):
            if m == j:
                continue
            d = seg_point_dist(z0, zj, zm)
            if clearance is None or d < clearance:
                clearance = d
    if not clearance > radius:
        fail(f"segment clearance {mp.nstr(clearance, 8)} <= lasso radius")
    max_dist = max(abs(zj - z0) for zj in bps)
    if not max_dist < R_BIG:
        fail(f"large circle R={R_BIG} does not enclose all branch points ({mp.nstr(max_dist, 8)})")
    print(f"  segment clearance from other branch points {mp.nstr(clearance, 8)} "
          f"(> radius: True); farthest branch point from z0 {mp.nstr(max_dist, 8)} (< R={R_BIG})")

    # 1. the six lifts
    print("\n1. SIX LASSO LIFTS (projection e^{i theta}; + = left strand passes in front)")
    loops = []
    worst = {"max_adjacent_swaps_in_one_step": 0, "min_u_gap_at_crossing": None,
             "worst_step_over_separation": mp.mpf(0)}
    for j, zj in enumerate(bps):
        word, g = braid_of_path(lasso(z0, zj, radius, N_SEGMENT, N_CIRCLE))
        rw = reduce_word(word)
        worst["max_adjacent_swaps_in_one_step"] = max(
            worst["max_adjacent_swaps_in_one_step"], g["max_adjacent_swaps_in_one_step"])
        if g["min_u_gap_at_crossing"] is not None and (
                worst["min_u_gap_at_crossing"] is None
                or g["min_u_gap_at_crossing"] < worst["min_u_gap_at_crossing"]):
            worst["min_u_gap_at_crossing"] = g["min_u_gap_at_crossing"]
        worst["worst_step_over_separation"] = max(
            worst["worst_step_over_separation"], g["worst_step_over_separation"])
        perm = word_perm(rw)
        es = exp_sum(rw)
        ct = cycle_type(perm)
        loops.append({
            "branch_point": {"re": mp.nstr(zj.real, 20), "im": mp.nstr(zj.imag, 20)},
            "braid_word_raw_length": len(word),
            "braid_word_reduced": list(rw),
            "permutation": list(perm),
            "cycle_type": list(ct),
            "exponent_sum": es,
            "is_half_twist": (abs(es) == 1 and ct == (1, 2)),
        })
        print(f"  loop {j}  bp ({loops[-1]['branch_point']['re'][:10]}, "
              f"{loops[-1]['branch_point']['im'][:10]}i)  word {list(rw)}  "
              f"perm {perm}  e-sum {es:+d}")
    if worst["max_adjacent_swaps_in_one_step"] > 1:
        fail("a step changed the u-order by more than one adjacent transposition")
    if worst["min_u_gap_at_crossing"] is None or not worst["min_u_gap_at_crossing"] > 0:
        fail("degenerate projection: zero u-gap at a recorded crossing")
    if not worst["worst_step_over_separation"] < mp.mpf(1) / 2:
        fail("continuation guard: a root moved more than half the root separation in one step")
    if not all(L["is_half_twist"] for L in loops):
        fail("not every lasso lift is a half-twist of exponent sum +-1")
    esums = sorted(set(L["exponent_sum"] for L in loops))
    if esums != [-1]:
        fail(f"exponent sums {esums}; expected all -1 under the stated convention")
    print(f"  guards: max adjacent swaps/step {worst['max_adjacent_swaps_in_one_step']}, "
          f"min u-gap at crossing {mp.nstr(worst['min_u_gap_at_crossing'], 6)}, "
          f"worst step/separation {mp.nstr(worst['worst_step_over_separation'], 6)}")
    print("  all six are half-twists with exponent sum -1: True")

    # Partition of the loops by S_3 image — invariant under relabelling, so
    # comparable across probes with different strand labellings.
    def partition(perms):
        groups = {}
        for j, p in enumerate(perms):
            groups.setdefault(tuple(p), []).append(j)
        return sorted(groups.values())
    my_part = partition([L["permutation"] for L in loops])
    sib_part = partition([list(word_perm(w)) for w in SIBLING_WORDS])
    ref_path = HERE / "bring-cubic-monodromy-probe.witness.json"
    ref_part = None
    if ref_path.exists():
        ref = json.loads(ref_path.read_text())
        ref_part = partition([L["permutation"] for L in ref["numeric"]["loops"]])
    print(f"  loop partition by S_3 image: mine {my_part}; sibling {sib_part}; "
          f"bring_cubic_monodromy_probe (A7) {ref_part}")
    if my_part != sib_part or (ref_part is not None and my_part != ref_part):
        fail("loop partition by permutation disagrees between probes")

    # 1b. per-loop conjugacy with the sibling's words
    print("\n1b. PER-LOOP COMPARISON WITH PR #6449's WORDS (up to conjugacy in B_3)")
    conj_rows = []
    all_conj = True
    for j, L in enumerate(loops):
        w, s = tuple(L["braid_word_reduced"]), SIBLING_WORDS[j]
        nec = (exp_sum(w) == exp_sum(s)
               and cycle_type(word_perm(w)) == cycle_type(word_perm(s))
               and burau_charpoly_str(w) == burau_charpoly_str(s))
        c = find_conjugator(w, s)
        literal = braids_equal(w, s)
        row = {
            "loop": j, "mine": list(w), "sibling": list(s),
            "equal_in_B3": literal,
            "necessary_condition": nec,
            "burau_charpoly_mine": burau_charpoly_str(w),
            "burau_charpoly_sibling": burau_charpoly_str(s),
            "conjugator_c_with_c_mine_cinv_eq_sibling": (list(c) if c is not None else None),
            "conjugate_in_B3_proved": c is not None,
        }
        conj_rows.append(row)
        all_conj = all_conj and nec and (c is not None)
        print(f"  loop {j}: mine {list(w)} vs sibling {list(s)}  equal {literal}  "
              f"necessary {nec}  conjugator {list(c) if c is not None else 'NOT FOUND (len<=%d)' % CONJUGATOR_MAX_LEN}")
    if not all_conj:
        fail("some loop lift is not (provably) conjugate to the sibling's")
    print("  all six lifts are conjugate in B_3 to the sibling's, with explicit conjugators: True")

    # 2. the full-twist check
    print("\n2. FULL-TWIST CHECK: product of the six lifts vs the large circle")
    big_word, gbig = braid_of_path(big_loop(z0, R_BIG, N_BIG_SEGMENT, N_BIG_CIRCLE))
    big_rw = reduce_word(big_word)
    if gbig["max_adjacent_swaps_in_one_step"] > 1:
        fail("large circle: a step changed the u-order by more than one adjacent transposition")
    if not gbig["worst_step_over_separation"] < mp.mpf(1) / 2:
        fail("large circle: continuation guard violated")
    big_perm = word_perm(big_rw)
    k_big = which_full_twist(big_rw)
    print(f"  large circle |z - z0| = {R_BIG}, ccw: word length {len(big_rw)}, "
          f"perm {big_perm}, exponent sum {exp_sum(big_rw):+d}, "
          f"equals Delta^(2k) with k = {k_big}")
    if big_perm != (0, 1, 2):
        fail("large-circle permutation is not trivial (contradicts A5, unramified at infinity)")
    if k_big is None or abs(k_big) != 1:
        fail(f"large-circle braid is Delta^(2k) with k = {k_big}; expected |k| = 1")

    order, rel = angular_order(z0, bps)
    prod_inc = reduce_word(sum((tuple(loops[j]["braid_word_reduced"]) for j in order), ()))
    prod_dec = reduce_word(sum((tuple(loops[j]["braid_word_reduced"]) for j in reversed(order)), ()))
    inc_ok = braids_equal(prod_inc, big_rw)
    dec_ok = braids_equal(prod_dec, big_rw)
    # Shrinking the large circle onto the star of lasso segments traverses the
    # lassos in INCREASING angular order (ccw sweep from the cut direction,
    # which points away from the hull), first-traversed first. That order is
    # the theoretically forced one and is asserted; the reverse order is
    # reported, not asserted. How many of the 720 orderings give the same
    # element measures how discriminating the joint check is.
    print(f"  angular order of the lassos from z0 (increasing): {order}")
    print(f"  product in increasing order == large circle: {inc_ok}; "
          f"in decreasing order: {dec_ok}")
    if not inc_ok:
        fail("the six lifts, in increasing angular order, do not multiply to the large-circle braid")
    k_prod = which_full_twist(prod_inc)
    if k_prod != k_big:
        fail("six-lift product and large circle are different full-twist powers")
    my_words = [tuple(L["braid_word_reduced"]) for L in loops]

    def n_orderings_giving(words, target_word):
        tgt = braid_auto(target_word)
        n = 0
        for pi in itertools.permutations(range(6)):
            if braid_auto(reduce_word(sum((words[j] for j in pi), ()))) == tgt:
                n += 1
        return n
    n_ord_mine = n_orderings_giving(my_words, big_rw)
    print(f"  => the six lifts multiply (order {order}) to Delta^(2k), k = {k_prod}; "
          f"{n_ord_mine} of 720 orderings give this element")

    # the same test on the sibling's words, from THEIR base point
    zs = mp.mpc(_mpf(SIBLING_BASE[0]), _mpf(SIBLING_BASE[1]))
    s_order, _ = angular_order(zs, bps)
    s_inc = reduce_word(sum((SIBLING_WORDS[j] for j in s_order), ()))
    s_dec = reduce_word(sum((SIBLING_WORDS[j] for j in reversed(s_order)), ()))
    ks_inc, ks_dec = which_full_twist(s_inc), which_full_twist(s_dec)
    n_ord_sib = n_orderings_giving(list(SIBLING_WORDS), delta_power(k_big))
    print(f"  sibling's words, angular order from their base point {s_order}: "
          f"increasing product = Delta^(2k) k={ks_inc}; decreasing k={ks_dec}; "
          f"{n_ord_sib} of 720 orderings give Delta^(2k), k={k_big}")
    if ks_inc != k_big:
        fail("the sibling's six words do NOT multiply to the full twist in angular order")
    print(f"  => PR #6449's six words pass the full-twist consistency check: True")

    # how many DISTINCT elements of B_3 the six words are (sibling reports
    # four distinct reduced WORDS; elements can coincide)
    def n_distinct(words):
        autos = []
        for w in words:
            a = braid_auto(w)
            if a not in autos:
                autos.append(a)
        return len(autos)
    nd_mine, nd_sib = n_distinct(my_words), n_distinct(list(SIBLING_WORDS))
    sib_4_eq_0 = braids_equal(SIBLING_WORDS[4], SIBLING_WORDS[0])
    print(f"  distinct B_3 elements among the six lifts: mine {nd_mine}, sibling {nd_sib} "
          f"(sibling loop 4 word equals loop 0 word in B_3: {sib_4_eq_0})")
    # With two distinct lifts a, b (three loops each), the angular order
    # interleaves them and the full twist is (ab)^3 -- the B_3 lift of
    # rem:holonomy-trefoil's (H_1 H_2)^3 = id, which holds only in S_3.
    a_w, b_w = my_words[1], my_words[0]
    ab3 = reduce_word((a_w + b_w) * 3)
    ab3_is_full_twist = which_full_twist(ab3)
    classes_in_order = ["a" if braids_equal(my_words[j], a_w) else
                        ("b" if braids_equal(my_words[j], b_w) else "?") for j in order]
    print(f"  two distinct lifts a = {list(a_w)} (loops 1,2,5), b = {list(b_w)} (loops 0,3,4); "
          f"angular order reads {''.join(classes_in_order)}; (ab)^3 = Delta^(2k) with k = {ab3_is_full_twist}")
    if nd_mine != 2 or ab3_is_full_twist != k_big or classes_in_order != list("ababab"):
        fail("expected exactly two distinct lifts, interleaved in angular order, with (ab)^3 the full twist")

    # 3. SL(2,Z)
    print("\n3. GENERATION VIA rho : B_3 -> SL(2,Z)  (reduced Burau at t = -1)")
    ABA = mat_mul(mat_mul(A_MAT, B_MAT), A_MAT)
    BAB = mat_mul(mat_mul(B_MAT, A_MAT), B_MAT)
    braid_rel = ABA == BAB
    delta2_img = mat_mul(ABA, ABA)
    delta4_img = mat_mul(delta2_img, delta2_img)
    det = lambda m: m[0] * m[3] - m[1] * m[2]
    print(f"  A = {A_MAT}, B = {B_MAT}: ABA == BAB: {braid_rel}; det A, det B = {det(A_MAT)}, {det(B_MAT)}")
    print(f"  rho(Delta^2) = {delta2_img} (= -I: {delta2_img == (-1, 0, 0, -1)}); "
          f"rho(Delta^4) = I: {delta4_img == I_MAT}")
    if not (braid_rel and delta2_img == (-1, 0, 0, -1) and delta4_img == I_MAT):
        fail("the t=-1 Burau matrices do not satisfy the braid relation / Delta^2 -> -I")
    # cross-check the t=-1 specialisation against the symbolic Burau of Delta^2
    sym_d2 = burau(DELTA2).subs(T_SYM, -1)
    if tuple(int(x) for x in sym_d2) != delta2_img:
        fail("symbolic Burau at t=-1 disagrees with the integer matrices")
    gens = [(f"g{j}", sl2_of_word(loops[j]["braid_word_reduced"])) for j in range(6)]
    for name, M in gens:
        if det(M) != 1:
            fail(f"{name} has determinant {det(M)}")
    found = bfs_sl2(gens, {"S": S_MAT, "T": T_MAT, "-I": (-1, 0, 0, -1)}, SL2Z_BFS_MAX_DEPTH)
    for tname in ("S", "T", "-I"):
        w = found.get(tname)
        print(f"  {tname:2s} = {' '.join(w) if w else 'NOT FOUND'}  "
              f"(depth {len(w) if w else '-'})")
        if w is None:
            fail(f"{tname} not reached within depth {SL2Z_BFS_MAX_DEPTH}")
    # verify the products literally
    name_to_mat = dict(gens)
    for tname, target in (("S", S_MAT), ("T", T_MAT), ("-I", (-1, 0, 0, -1))):
        M = I_MAT
        for tok in found[tname]:
            base = name_to_mat[tok.replace("^-1", "")]
            M = mat_mul(M, mat_inv(base) if tok.endswith("^-1") else base)
        if M != target:
            fail(f"reconstructed product for {tname} does not evaluate to it")
    print("  S and T generate SL(2,Z), so rho(<lifts>) = SL(2,Z).")
    print("  With Delta^2 in <lifts> (step 2) and ker rho = <Delta^4> (imported: Magnus;")
    print("  Milnor, Intro. to Algebraic K-theory, §10), <lifts> = B_3.")

    elapsed = time.monotonic() - t_start
    print("\nVERDICT")
    print("  six lifts are half-twists of exponent sum -1, conjugate loop-by-loop to")
    print("  PR #6449's words with explicit conjugators: True")
    print(f"  large-circle braid = Delta^(2k), k = {k_big}; six-lift product (angular order) equals it: True")
    print("  PR #6449's words pass the same product test: True")
    print("  rho(<lifts>) = SL(2,Z) with explicit S, T: True  =>  <lifts> = B_3")
    print("  (agrees with #6449's word-search conclusion by an independent route)")
    print("  NOT touched: statement B's premise; mu-bar; the A6 sheets=colour identification")
    print(f"  runtime {mp.nstr(mp.mpf(int(elapsed * 1000)) / 1000, 6)} s")

    out = {
        "schemaVersion": "1.0.0",
        "description": (
            "Independent verification of the S_3 -> B_3 lift of the Bring colour "
            "monodromy (PR #6449, bring_monodromy_braid_lift_probe) by a different "
            "route: generic-direction projection, different base point, per-loop "
            "conjugacy with explicit conjugators, the full-twist consistency check "
            "(six-lift product == large-circle braid == Delta^{2k}), and generation "
            "of B_3 via surjection onto SL(2,Z) plus Delta^2 in the image. "
            "Statement B's premise is unchanged; no mu-bar computed."
        ),
        "computation": {
            "script": "computations/probes/bring_monodromy_full_twist_probe.py",
            "arithmetic": (
                f"mpmath mpc at {mp.dps} dps for root transport; exact integers for "
                "words, permutations, SL(2,Z) matrices; sympy over Q(t) for Burau "
                "characteristic polynomials. No float64; no float()."
            ),
            "runtime_seconds": mp.nstr(mp.mpf(int(elapsed * 1000)) / 1000, 6),
        },
        "parameters": {
            "dps": mp.dps,
            "n_circle": N_CIRCLE, "n_segment": N_SEGMENT,
            "n_big_circle": N_BIG_CIRCLE, "n_big_segment": N_BIG_SEGMENT,
            "projection_theta_rad": str(THETA),
            "base_point": f"{Z_BASE[0]} + {Z_BASE[1]} i",
            "large_circle_radius": R_BIG,
            "lasso_radius": mp.nstr(radius, 12),
            "branch_point_min_separation": mp.nstr(sep, 12),
            "segment_clearance": mp.nstr(clearance, 12),
            "sign_convention": (
                "strands ordered by u = Re(w e^{-i theta}); on an adjacent exchange the "
                "letter is sigma_i^{+1} if the strand that was on the left has the larger "
                "v = Im(w e^{-i theta}) (passes in front), else sigma_i^{-1}. A ccw "
                "half-turn is sigma^{-1}; a ccw turn of all three roots is Delta^{-2}."
            ),
        },
        "guards": {
            "max_adjacent_swaps_in_one_step": worst["max_adjacent_swaps_in_one_step"],
            "min_u_gap_at_crossing": mp.nstr(worst["min_u_gap_at_crossing"], 10),
            "worst_step_over_separation": mp.nstr(worst["worst_step_over_separation"], 10),
            "large_circle_max_adjacent_swaps": gbig["max_adjacent_swaps_in_one_step"],
            "large_circle_worst_step_over_separation": mp.nstr(gbig["worst_step_over_separation"], 10),
            "why_generic_direction": (
                "with real z the cubic has real coefficients and two roots are conjugate "
                "with equal real parts, which degenerates a real-axis reading (PR #6449 "
                "§10.1 defect 2); projected onto e^{i theta} their u-coordinates differ by "
                "2 Im(w) sin(theta), so that degeneracy cannot occur"
            ),
        },
        "loops": loops,
        "loop_partition_by_permutation": {
            "mine": my_part, "sibling": sib_part, "bring_cubic_monodromy_probe": ref_part,
            "agree": True,
        },
        "comparison_with_pr6449": {
            "sibling_probe": SIBLING_PROBE,
            "sibling_base_point": f"{SIBLING_BASE[0]} + {SIBLING_BASE[1]} i",
            "sibling_projection": "real axis",
            "rows": conj_rows,
            "all_conjugate_with_explicit_conjugator": True,
            "note": (
                "different base point and projection => lifts agree only up to "
                "conjugacy; equal Burau characteristic polynomial is a NECESSARY "
                "condition only, the explicit conjugator (checked by Artin action, "
                "faithful) is the proof"),
        },
        "full_twist_check": {
            "large_circle_word": list(big_rw),
            "large_circle_permutation": list(big_perm),
            "large_circle_exponent_sum": exp_sum(big_rw),
            "large_circle_is_delta_2k_with_k": k_big,
            "angular_order_from_base_point": order,
            "relative_angles_rad": [mp.nstr(a, 12) for a in rel],
            "increasing_order_product_equals_large_circle": inc_ok,
            "decreasing_order_product_equals_large_circle": dec_ok,
            "six_lift_product_is_delta_2k_with_k": k_prod,
            "n_of_720_orderings_giving_large_circle_element": n_ord_mine,
            "distinct_B3_elements_among_six_lifts": nd_mine,
            "lift_a_loops_1_2_5": list(a_w),
            "lift_b_loops_0_3_4": list(b_w),
            "angular_order_classes": "".join(classes_in_order),
            "ab_cubed_is_delta_2k_with_k": ab3_is_full_twist,
            "holonomy_trefoil_lift": (
                "rem:holonomy-trefoil's (H_1 H_2)^3 = id holds in S_3 only; in B_3 the "
                "cube of the product of the two distinct lifts is the full twist "
                "Delta^{-2}, not the identity"),
            "sibling_words_angular_order_from_their_base": s_order,
            "sibling_words_product_k_increasing": ks_inc,
            "sibling_words_product_k_decreasing": ks_dec,
            "sibling_words_n_of_720_orderings_giving_delta_2k": n_ord_sib,
            "sibling_words_pass": True,
            "sibling_distinct_B3_elements_among_six": nd_sib,
            "sibling_loop4_equals_loop0_in_B3": sib_4_eq_0,
            "why_k_is_minus_one": (
                "at large |z| the roots are z*(roots of Y^3+Y^2+Y+1) (fact A5), so one "
                "ccw turn of z turns all three roots once ccw; under the stated sign "
                "convention that is Delta^{-2}. Trivial permutation = unramified at infinity."),
        },
        "sl2z_generation": {
            "burau_t_minus_1": {"sigma_1": list(A_MAT), "sigma_2": list(B_MAT)},
            "braid_relation_holds": braid_rel,
            "rho_delta2": list(delta2_img), "rho_delta4_is_identity": delta4_img == I_MAT,
            "lift_images": {name: list(M) for name, M in gens},
            "S_as_product_of_lifts": found["S"],
            "T_as_product_of_lifts": found["T"],
            "minus_I_as_product_of_lifts": found["-I"],
            "bfs_max_depth": SL2Z_BFS_MAX_DEPTH,
            "imported_fact": (
                "ker(B_3 -> SL(2,Z)) = <Delta^4> (Magnus 1934; Milnor, Introduction to "
                "Algebraic K-theory, §10). Not verified here."),
            "argument": (
                "rho(H) = SL(2,Z) and Delta^2 in H: for g in B_3 pick h in H with "
                "rho(h) = rho(g); g h^{-1} in <Delta^4> <= <Delta^2> <= H; so H = B_3."),
            "conclusion": "the monodromy image is B_3 (independent of #6449's generator words)",
        },
        "summary": {
            "verifies": [
                "PR #6449 loop lifts are half-twists of exponent sum -1 (loop-by-loop conjugate)",
                "PR #6449 six words multiply to Delta^{-2} in angular order (new joint check)",
                "image = B_3, by SL(2,Z) surjection + Delta^2 in image (new route)",
            ],
            "does_not_touch": [
                "statement B's premise (the baryon occupies the sign isotype) — unchanged",
                "mu-bar of any closure — see colour_mu_bar_monodromy_probe (#6449)",
                "the A6 identification of the sheets with the colour tubes — consumed",
            ],
            "scope": (
                "(a)-free positive result: exact group-theoretic conclusion conditional "
                "on the numerically read words, which are guarded (one adjacent swap "
                "per step, positive u-gap, step < separation/2) and now jointly "
                "constrained by the full-twist identity"),
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
