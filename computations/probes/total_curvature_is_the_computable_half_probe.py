#!/usr/bin/env python3
# polynomial_q_not_applicable: integer linking numbers, permutation cycles and
# exact integer Kauffman-bracket coefficients of the canonical closure.  No q,
# no float, nothing evaluated at q0.
"""Total curvature is the computable half of the serpenoid tower, and Milnor's
theorem prices it from data the substrate fixes exactly. The other half is the
twist, and nothing here touches it.

WHY THIS, AND FROM WHAT PICTURE
-------------------------------
The owner's serpenoid image: a swimming snake beside the drawn family of its
osculating circles. A serpenoid is *defined* by sinusoidal curvature in
arclength, so `rho = 1/kappa` blows up at every inflection and repeats, and the
drawn family is a scale-indexed pencil that "reads as a tower". The owner's
follow-up asked whether anything in the framework plays the role of what DRIVES
the oscillation -- Reeb flow, saddle points.

Milnor's proof of Fary-Milnor answers the second question exactly, and it is
worth having in front of you because it is the same statement the tower makes:

    integral kappa ds  =  (1/4) integral_{S^2} mu(v) dv  =  pi * <mu>

where `mu(v)` is the NUMBER OF CRITICAL POINTS of the height function
`s -> <gamma(s), v>` and `<mu>` its average over directions (Crofton). Total
curvature IS the averaged count of the oscillations. Every direction is a
Morse function on the curve; its critical points are the turning points the
snake makes in that projection; average the count and you have the curvature.
The Reeb graph of `<gamma, v>` is the graph whose nodes are those critical
points. So "the oscillations happen at the saddle points" is not an analogy
for the curvature -- under Crofton it is the curvature, integrated.

Then Milnor: `mu(v) >= 2 b` for almost every `v`, where `b` is the bridge
number, so

    inf over the isotopy class of  integral kappa ds  =  2 pi b(L),

and Fary-Milnor is the case `b >= 2 <=> knotted`, giving `> 4 pi`.

WHAT THE SUBSTRATE FIXES EXACTLY
--------------------------------
Two permutation-level data, both exact integers:

  * the component count `mu = A + 1` (measured by probe: `slq2_label_admits_even_a_only_probe`
    and `atom_closure_milnor_indeterminacy_probe`, and verified below at A=2,3,4,6;
    carried as a hypothesis `hmu : mu = A + 1` in `QOU/Mass/SLq2LabelParity.lean:77`
    and `QOU/Mass/TorusKnotPages.lean:82` — bean `qou-d5hn`), and
  * the KNOT TYPE OF EACH COMPONENT, read off here by an exact-integer Kauffman
    bracket on the sub-braid that remains when the other strands are deleted.

Bridge number is additive-or-better over components, `b(L) >= sum_i b(K_i)`,
with `b = 1` for an unknot and `b >= 2` for anything knotted. So

    inf integral kappa ds  >=  2 pi ( mu + #knotted components ) ,     (proved)

and from the `3A`-strand braid presentation, `<= 2 pi * 3A`.

WHAT IS MEASURED HERE, PER NUCLEUS, PER CLASSICAL BRANCH
--------------------------------------------------------
The canonical word is not a braid: `2A + 1` of its letters are Hecke
`averaged` elements strictly between `sigma` and `sigma^-1`
(`bonded_pair_linking_from_canonical_braid_probe`). A curve needs a link, so
each averaged letter is resolved BOTH ways and everything is reported per
branch. For each branch:

  * components (cycles of the closure permutation) and pairwise linking;
  * the Jones polynomial of EACH COMPONENT on its own;
  * the Jones polynomial of each CONSECUTIVE PAIR, compared with the
    `(2, 2 lk)`-torus link a round chain of unknots would give.

A component with non-trivial Jones is knotted, and Fary-Milnor then forces its
own total curvature above `4 pi` on every realisation. A component with
trivial Jones is reported as "Jones-trivial" -- for sub-braids of this size
that is the unknot, but the probe says which it has checked.

THE PENCIL, EXPLICITLY -- AND WHICH OF ITS SHADOWS SURVIVE ISOTOPY
-------------------------------------------------------------------
"Pencil" above is used in the loose sense and it is worth being exact.

*In the plane.* Tait-Kneser: along an arc on which the curvature is monotone
and non-zero, the osculating circles are nested and pairwise disjoint. So they
foliate an annular region, and their centres trace the evolute. The serpenoid
has one such nest per quarter-wave: from the smallest circle at a vertex
(curvature extremum, evolute cusp) opening out to the tangent line at the
inflection, reversing at every vertex, repeating with the period. That nest is
a pencil in the sense of a one-parameter family of circles foliating a region;
it is a LINEAR pencil (`C_1 + lambda C_2`: elliptic through two base points,
hyperbolic/Apollonian, parabolic) only in the degenerate concentric case, i.e.
for a circle. On the region it foliates it gives coordinates `(s, theta)`:
which circle, where on it -- singular exactly at the vertices and inflections.
This lives on a CURVE. The substrate's object is an isotopy class, so the
osculating pencil is not defined on it at all.

*In space, on a curve.* The osculating circle of a space curve lies in the
osculating plane `span(T, N)`. The family along the curve does not foliate
anything, but it fixes a framing -- the Frenet normal -- whose twist is the
torsion integral, `Tw_N = (1/2pi) integral tau ds`, so that

    Lk(K, K_N) = Wr + (1/2pi) integral tau ds   is an integer.

The curvature pencil is blind to `tau`; the framing it induces is not. That is
the same datum the hull-exit analysis says the substrate lacks.

*In the complement, invariantly.* Two pencils survive isotopy, and both exist
for every component found here BECAUSE the components are torus knots:

  (i)  the Milnor open book of `T(2, 2g+1)`: pages = Seifert surfaces of genus
       `g`, binding = the knot, all pages sharing the knot as base locus,
       monodromy of order `2(2g+1)`, Seifert form unimodular (`det V = 1`,
       verified below) so `H_1(page)` is self-dual under it -- a frame with a
       dual frame;
  (ii) the Seifert circle fibration: the orbits of the `(2, 2g+1)`-weighted
       circle action, circles foliating the complement with two exceptional
       fibres of orders `2` and `2g+1` and the knot itself a regular fibre.
       These orbits are the Reeb orbits of the weighted contact form, they are
       transverse to the pages of (i), and the binding is a Reeb orbit
       (Thurston-Winkelnkemper / Giroux).

So the complement carries two circle-valued coordinates -- the page angle
across (i) and the fibre angle along (ii) -- and (ii) is the closest honest
analogue of the plane pencil: a foliation by circles with a singular axis (the
two exceptional fibres) in place of the evolute. What "drives the oscillation"
in this picture is the monodromy of (i): a morsification of `z^2 + w^(2g+1)`
has `2g` Morse saddles, one vanishing cycle each, and the monodromy is the
product of their Dehn twists.

*Frobenius duality, three senses, and which apply.* In this corpus the
Frobenius pairing is the trace making the observable algebra self-dual
(`QOU.frobenius_relation`: comultiplication dual to multiplication under it).
On the page, the corresponding self-duality is the unimodular Seifert form.
On the algebra, it is the non-degenerate Markov-Gram form on `TL_n`, whose
exact inverse the corpus already has (`pyhecke.tl`). What is NOT established
is any map from the `TL_n` frame to the complement's frame: that would pass
through the skein module of the complement, which the substrate does not
compute. The claim stops there.

*Computed per component (section F below).* Bennequin surface from the
sub-braid: `chi = k - c = -5` for EVERY multi-strand component on both
branches (2 strands, 7 crossings, or 3 strands, 8 crossings), so its genus is
`3` throughout. On the `sigma` branch every component is `T(2,7)`, of genus
`3`, so the Bennequin surface is of MINIMAL genus -- and a fibered knot has a
unique minimal-genus Seifert surface up to isotopy, its fibre. So on that
branch the Bennequin surface IS the page. (Most of those sub-braids are
positive as written, which would give the same conclusion by Stallings; a few
carry one `sigma^-1` that does not cancel freely, and for them the argument
is the genus one, not positivity -- the probe counts both.) On the `sigma^-1`
branch the words are mixed and the Bennequin surface is not minimal
(`3 > g` for `T(2,5)`, `T(2,3)`); the page there is a smaller surface the
braid does not exhibit.

WHAT IT DOES NOT DO
-------------------
It does not produce the twist. `Lk = Tw + Wr` and the hull-exit analysis
(`the_hull_exit_is_a_fractional_twist_probe`, `the_twist_is_absent_where_it_
is_needed_probe`) put the missing ingredient in `Tw`, which is a torsion
integral; the osculating circle sees `kappa` and is blind to `tau`. This probe
establishes what the curvature half is worth, and that it is not the half
that is missing.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))
import _path_bridge  # noqa: F401,E402

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

ISOTOPES = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"), (3, 3, "6Li")]

# ══════════════════════════════════════════════════════════════════
# §1  Laurent polynomials in A as {exponent: int}; delta = -A^2 - A^-2
# ══════════════════════════════════════════════════════════════════
DELTA = {2: -1, -2: -1}


def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0:
            del r[e]
    return r


def pmul(p, q):
    r: dict[int, int] = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}


def pshift(p, k, sign=1):
    return {e + k: sign * c for e, c in p.items()}


def ppow(p, n):
    r = {0: 1}
    for _ in range(n):
        r = pmul(r, p)
    return r


def pstr(p, var="A"):
    if not p:
        return "0"
    out = []
    for e in sorted(p, reverse=True):
        c = p[e]
        s = ("+" if c > 0 else "-") + (str(abs(c)) if abs(c) != 1 or e == 0 else "")
        out.append(s + (f"{var}^{e}" if e not in (0, 1) else (var if e == 1 else "")))
    return " ".join(out).lstrip("+")


def as_t(p):
    """Rewrite in t = A^-4 when every exponent is a multiple of 4."""
    if any(e % 4 for e in p):
        return None
    return {-e // 4: c for e, c in p.items()}


# ══════════════════════════════════════════════════════════════════
# §2  Temperley-Lieb diagrams and the Kauffman bracket of a braid closure
# ══════════════════════════════════════════════════════════════════
def tl_identity(k):
    return tuple(list(range(k, 2 * k)) + list(range(k)))


def tl_gen(k, i):
    m = list(tl_identity(k))
    m[i], m[i + 1] = i + 1, i
    m[k + i], m[k + i + 1] = k + i + 1, k + i
    return tuple(m)


def _walk(adj, start, boundary):
    """Follow the unique path from `start`; return its far endpoint and the
    set of vertices visited."""
    prev, cur, seen = None, start, {start}
    while True:
        nxt = [x for x in adj[cur] if x != prev]
        if not nxt:
            return cur, seen
        nxt = nxt[0]
        if nxt in seen:
            return nxt, seen
        seen.add(nxt)
        if nxt in boundary:
            return nxt, seen
        prev, cur = cur, nxt


def tl_compose(D, E, k):
    """Stack E below D. Returns (diagram, number of closed loops)."""
    # vertices: D-top 0..k-1, middle k..2k-1 (D-bottom = E-top), E-bottom 2k..3k-1
    adj: dict[int, list[int]] = {v: [] for v in range(3 * k)}
    for p in range(2 * k):
        q = D[p]
        if p < q:
            adj[p].append(q); adj[q].append(p)
    for p in range(2 * k):
        q = E[p]
        if p < q:
            adj[p + k].append(q + k); adj[q + k].append(p + k)
    boundary = set(range(k)) | set(range(2 * k, 3 * k))
    seen_all: set[int] = set()
    out = [None] * (2 * k)
    for p in sorted(boundary):
        if p in seen_all:
            continue
        q, seen = _walk(adj, p, boundary)
        seen_all |= seen
        a = p if p < k else p - k
        b = q if q < k else q - k
        out[a], out[b] = b, a
    loops = 0
    for p in range(k, 2 * k):
        if p in seen_all:
            continue
        _, seen = _walk(adj, p, set())
        seen_all |= seen
        loops += 1
    return tuple(out), loops


def tl_closure_loops(D, k):
    adj = {p: [D[p]] for p in range(2 * k)}
    for j in range(k):
        adj[j].append(k + j)
        adj[k + j].append(j)
    seen, loops = set(), 0
    for p in range(2 * k):
        if p in seen:
            continue
        loops += 1
        prev, cur = None, p
        while cur not in seen:
            seen.add(cur)
            nxt = [x for x in adj[cur] if x != prev]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
    return loops


def bracket_closure(k, word):
    """Kauffman bracket <closure(beta)>, unknot-normalised, exact in A.
    word: list of (i, sign) with sign = +1 for sigma_i, -1 for sigma_i^-1."""
    cur = {tl_identity(k): {0: 1}}
    for i, sign in word:
        nxt: dict = {}
        for D, poly in cur.items():
            for coef, gen in ((sign, tl_identity(k)), (-sign, tl_gen(k, i))):
                D2, loops = tl_compose(D, gen, k)
                p2 = pmul(pshift(poly, coef), ppow(DELTA, loops))
                nxt[D2] = padd(nxt.get(D2, {}), p2)
        cur = {D: p for D, p in nxt.items() if p}
    total: dict[int, int] = {}
    for D, poly in cur.items():
        total = padd(total, pmul(poly, ppow(DELTA, tl_closure_loops(D, k) - 1)))
    return total


def jones_closure(k, word):
    """V(closure) as a Laurent polynomial in A (t = A^-4), unknot = 1."""
    w = sum(s for _, s in word)
    return pshift(bracket_closure(k, word), -3 * w, (-1) ** (w % 2))


# ══════════════════════════════════════════════════════════════════
# §3  The canonical closure: branches, components, sub-braids, linking
# ══════════════════════════════════════════════════════════════════
def resolve(Z, N, avg_sign):
    """Resolved crossings of the GROUPED chain word (named since 2026-09-05).

    The chain form this probe rests on -- every generator occurring in
    exactly one contiguous run, so the closure is a linear connected sum of
    (2,k) torus links -- is a property of the word's ASSEMBLY, not of the
    chain topology. `atom_braid_word_3A` now defaults to the Borromean
    `(sigma_0 sigma_1^-1)^3` intra core, which interleaves gens 3k and 3k+1
    and so is NOT one run per generator: each nucleon block becomes the
    Borromean braid rather than a torus link. This probe therefore asks for
    the word whose property it is testing.

    The INTER-nucleon structure is a chain either way -- blocks overlap in
    one strand -- so connected-sum multiplicativity, and with it every
    log-ratio quantity, is unaffected (bean `qou-hu1f`; proved in
    `QOU.Mass.IntraOrdering.chainRatio_eq_of_intra`).
    """
    return [(g, 1 if kind == "sigma" else (-1 if kind == "sigma_inv" else avg_sign))
            for g, kind in atom_canonical_crossings(Z, N, intra_order="grouped")]


def components(n, word):
    pos = list(range(n))
    for g, _ in word:
        pos[g], pos[g + 1] = pos[g + 1], pos[g]
    end_at = {s: p for p, s in enumerate(pos)}      # strand s ends at position p
    comp, cyc, c = {}, [], 0
    for s in range(n):
        if s in comp:
            continue
        cur, cycle = s, []
        while cur not in comp:
            comp[cur] = c
            cycle.append(cur)
            cur = end_at[cur]
        cyc.append(cycle)
        c += 1
    return comp, cyc


def sub_braid(n, word, keep):
    """Delete every strand not in `keep`; return (k, sub-word)."""
    keep = set(keep)
    pos = list(range(n))
    sub = []
    for g, sign in word:
        a, b = pos[g], pos[g + 1]
        if a in keep and b in keep:
            r = sum(1 for p in range(g) if pos[p] in keep)
            sub.append((r, sign))
        pos[g], pos[g + 1] = b, a
    return len(keep), sub


def linking(n, word, comp):
    pos = list(range(n))
    twice: dict = {}
    for g, sign in word:
        a, b = comp[pos[g]], comp[pos[g + 1]]
        if a != b:
            key = (min(a, b), max(a, b))
            twice[key] = twice.get(key, 0) + sign
        pos[g], pos[g + 1] = pos[g + 1], pos[g]
    assert all(v % 2 == 0 for v in twice.values())
    return {k: v // 2 for k, v in twice.items()}


TORUS = {  # Jones polynomials in t of the (2, 2k+1) torus knots, one chirality
    3: {1: 1, 3: 1, 4: -1},
    5: {2: 1, 4: 1, 5: -1, 6: 1, 7: -1},
    7: {3: 1, 5: 1, 6: -1, 7: 1, 8: -1, 9: 1, 10: -1},
}


def name_knot(Vt):
    if Vt == {0: 1}:
        return "unknot"
    for k, V in TORUS.items():
        if Vt == V:
            return f"T(2,{k})"
        if Vt == {-e: c for e, c in V.items()}:
            return f"T(2,{k}) mirror"
    return "other knot"


# ══════════════════════════════════════════════════════════════════
# §F  The invariant pencil: Bennequin surfaces and Seifert forms (exact)
# ══════════════════════════════════════════════════════════════════
def free_reduce(sw):
    """Cancel adjacent sigma_i sigma_i^-1 pairs only; no braid relation used."""
    out = []
    for i, s in sw:
        if out and out[-1][0] == i and out[-1][1] == -s:
            out.pop()
        else:
            out.append((i, s))
    return out


def det_int(M):
    """Exact determinant of an integer matrix (Gaussian elimination over Q)."""
    from fractions import Fraction
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    det = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            A[c], A[p] = A[p], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            for k in range(c, n):
                A[r][k] -= f * A[c][k]
    assert det.denominator == 1
    return int(det)


def seifert_T2(n):
    """Seifert matrix of T(2,n) from its 2-strand positive braid: (n-1)x(n-1),
    -1 on the diagonal, +1 on the superdiagonal."""
    m = n - 1
    return [[(-1 if i == j else (1 if j == i + 1 else 0)) for j in range(m)]
            for i in range(m)]


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def inv_unimodular(V):
    from fractions import Fraction
    n = len(V)
    A = [[Fraction(V[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)]
         for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        A[c] = [x / piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    inv = [[A[i][n + j] for j in range(n)] for i in range(n)]
    assert all(x.denominator == 1 for row in inv for x in row)
    return [[int(x) for x in row] for row in inv]


def monodromy_order(V, cap):
    Vt = [list(col) for col in zip(*V)]
    M = mat_mul(inv_unimodular(V), Vt)
    n = len(V)
    ident = [[int(i == j) for j in range(n)] for i in range(n)]
    P = ident
    for r in range(1, cap + 1):
        P = mat_mul(P, M)
        if P == ident:
            return r
    return None


def alexander_is_torus(V, n):
    """|det(V - t V^T)| == (t^n + 1)/(t + 1) at n+1 integer points (degree n-1)."""
    from fractions import Fraction
    m = len(V)
    Vt = [list(col) for col in zip(*V)]
    for t in range(2, n + 3):
        D = det_int([[V[i][j] - t * Vt[i][j] for j in range(m)] for i in range(m)])
        target = Fraction(t ** n + 1, t + 1)
        if target.denominator != 1 or abs(D) != int(target):
            return False
    return True


TORUS_GENUS = {"T(2,3)": 1, "T(2,5)": 2, "T(2,7)": 3}


# ══════════════════════════════════════════════════════════════════
# §4  Main
# ══════════════════════════════════════════════════════════════════
def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])

    print("\n" + "=" * 68)
    print("§0  BRACKET SELF-TEST")
    print("=" * 68)
    tests = {
        "unknot  sigma_1 on 2 strands": (2, [(0, 1)]),
        "unlink  identity on 2 strands": (2, []),
        "trefoil sigma_1^3": (2, [(0, 1)] * 3),
        "figure-eight s1 s2^-1 s1 s2^-1": (3, [(0, 1), (1, -1), (0, 1), (1, -1)]),
        "Hopf    sigma_1^2": (2, [(0, 1)] * 2),
        "T(2,5)  sigma_1^5": (2, [(0, 1)] * 5),
    }
    V_fig8 = {2: 1, 1: -1, 0: 1, -1: -1, -2: 1}
    for name, (k, w) in tests.items():
        V = jones_closure(k, w)
        Vt = as_t(V)
        shown = pstr(Vt, "t") if Vt is not None else pstr(V, "A")
        print(f"  {name:34s} V = {shown}")
        if "trefoil" in name:
            check("trefoil Jones is T(2,3) or its mirror", name_knot(Vt).startswith("T(2,3)"))
        elif "T(2,5)" in name:
            check("sigma_1^5 Jones is T(2,5) or its mirror", name_knot(Vt).startswith("T(2,5)"))
        elif "figure" in name:
            check("figure-eight Jones is t^2 - t + 1 - t^-1 + t^-2", Vt == V_fig8)
        elif "unknot" in name:
            check("unknot Jones = 1", Vt == {0: 1})
        elif "unlink" in name:
            check("2-unlink Jones = -A^2 - A^-2", V == DELTA)
        elif "Hopf" in name:
            check("Hopf Jones is not expressible in integer powers of t", Vt is None and len(V) == 2)

    summary = {}
    for Z, N, name in ISOTOPES:
        A_, n = Z + N, 3 * (Z + N)
        print("\n" + "=" * 68)
        print(f"§{name}   A = {A_}, n = {n}")
        print("=" * 68)
        kinds = Counter(k for _, k in atom_canonical_crossings(Z, N))
        n_avg = kinds["averaged"] + kinds["averaged_weighted"]
        print(f"  letters {sum(kinds.values())}: {dict(kinds)}   "
              f"(averaged = {n_avg} = 2A+1: {n_avg == 2 * A_ + 1})")
        rec = {}
        for avg_sign, bname in ((1, "sigma"), (-1, "sigma^-1")):
            word = resolve(Z, N, avg_sign)
            comp, cyc = components(n, word)
            mu = len(cyc)
            lk = linking(n, word, comp)
            print(f"\n  branch averaged -> {bname}:  mu = {mu}   cycles "
                  f"{[len(c) for c in cyc]}")
            print(f"    linking: {dict(sorted(lk.items()))}")
            path = all((a + 1 == b) for (a, b) in lk) and len(lk) == mu - 1
            print(f"    linking graph is the path P_{mu}: {path}")
            knots, knotted = [], []
            for ci, cycle in enumerate(cyc):
                k, sw = sub_braid(n, word, cycle)
                V = jones_closure(k, sw)
                Vt = as_t(V)
                nm = name_knot(Vt) if Vt is not None else "other knot"
                knots.append(nm)
                print(f"    component {ci}: {k} strands, {len(sw):2d} own crossings, "
                      f"V = {pstr(Vt, 't') if Vt is not None else pstr(V, 'A')}   -> {nm}")
                if nm != "unknot":
                    knotted.append(ci)
            chain_ok = True
            for (a, b), l in sorted(lk.items()):
                k, sw = sub_braid(n, word, cyc[a] + cyc[b])
                V = jones_closure(k, sw)
                Vtor = jones_closure(2, [(0, 1 if l > 0 else -1)] * (2 * abs(l)))
                same = (V == Vtor)
                chain_ok &= same
                print(f"    pair ({a},{b}) lk={l:+d}: {'= T(2,%d)' % (2*abs(l)) if same else 'not the (2,%d)-torus link' % (2*abs(l))}")
            nk = len(knotted)
            rec[bname] = dict(mu=mu, path=path, knotted=knotted, knots=knots, chain=chain_ok,
                              bound=mu + nk)
            print(f"    Milnor:  inf ∫κ ds ≥ 2π·b(L) ≥ 2π·(μ + #knotted) = 2π·({mu}+{nk})"
                  f" = 2π·{mu + nk}   and ≤ 2π·{n}")
            if knotted:
                print(f"    Fary-Milnor: components {knotted} are knotted "
                      f"({', '.join(knots[i] for i in knotted)}) → each has ∫κ > 4π")
        summary[name] = rec
        both = list(rec.values())
        check(f"{name}: mu = A+1 = {A_ + 1} on both branches", all(r["mu"] == A_ + 1 for r in both))
        check(f"{name}: linking graph is a path on both branches", all(r["path"] for r in both))
        check(f"{name}: every multi-strand component is a (2,odd)-torus knot on both branches",
              all(all(nm.startswith("T(2,") for nm in r["knots"] if nm != "unknot") for r in both)
              and all(len(r["knotted"]) == A_ for r in both))

    print("\n" + "=" * 68)
    print("§F  THE INVARIANT PENCIL: BENNEQUIN SURFACES AND SEIFERT FORMS")
    print("=" * 68)
    chi_all, pos_sigma, nonmin_inv, min_sigma = [], [], [], []
    for Z, N, name in ISOTOPES:
        n = 3 * (Z + N)
        for avg_sign, bname in ((1, "sigma"), (-1, "sigma^-1")):
            word = resolve(Z, N, avg_sign)
            comp, cyc = components(n, word)
            for ci, cycle in enumerate(cyc):
                k, sw = sub_braid(n, word, cycle)
                if k == 1:
                    continue
                c = len(sw)
                chi_all.append(k - c)
                red = free_reduce(sw)
                positive = all(s == 1 for _, s in red)
                V = jones_closure(k, sw)
                Vt = as_t(V)
                nm = name_knot(Vt) if Vt is not None else "?"
                g_knot = TORUS_GENUS.get(nm.replace(" mirror", ""))
                g_benn = (c - k + 1) // 2
                if bname == "sigma":
                    pos_sigma.append(positive)
                    min_sigma.append(g_knot is not None and g_benn == g_knot)
                else:
                    nonmin_inv.append(g_knot is not None and g_benn > g_knot)
                print(f"  {name:4s} {bname:8s} comp {ci}: k={k} c={c} chi={k - c:+d} "
                      f"g_Bennequin={g_benn}  {'positive' if positive else 'mixed'}"
                      f" (reduced len {len(red)})  -> {nm}, g={g_knot}")
    check("Bennequin chi = k - c = -5 for every multi-strand component on both branches",
          all(x == -5 for x in chi_all))
    print(f"\n  sigma branch: {sum(pos_sigma)} of {len(pos_sigma)} sub-braids positive as "
          f"written; Bennequin genus = g(T(2,7)) = 3 in {sum(min_sigma)} of {len(min_sigma)}")
    check("sigma branch: Bennequin surface has minimal genus for every component "
          "(fibered knot => it is isotopic to the page)", all(min_sigma))
    check("sigma branch: positivity is NOT universal as written (the page claim rests "
          "on genus, not on Stallings)", not all(pos_sigma) and sum(pos_sigma) > 0)
    check("sigma^-1 branch: the Bennequin surface is never minimal (genus 3 > g)",
          all(nonmin_inv))
    print("\n  Seifert forms of the torus knots that occur (exact integer arithmetic):")
    for nn in (3, 5, 7):
        V = seifert_T2(nn)
        d = det_int(V)
        Vt = [list(col) for col in zip(*V)]
        di = det_int([[V[i][j] - Vt[i][j] for j in range(len(V))] for i in range(len(V))])
        order = monodromy_order(V, 4 * nn)
        alex = alexander_is_torus(V, nn)
        print(f"    T(2,{nn}): genus {(nn - 1) // 2}, det V = {d}, det(V - V^T) = {di}, "
              f"Alexander = (t^{nn}+1)/(t+1): {alex}, monodromy order {order}")
        check(f"T(2,{nn}): Seifert form unimodular, Alexander (t^n+1)/(t+1), monodromy order 2n",
              d == 1 and di == 1 and alex and order == 2 * nn)

    print("\n" + "=" * 68)
    print("§Σ  WHAT THE CURVATURE HALF IS WORTH")
    print("=" * 68)
    print("  A   mu   #knotted   inf ∫κ ≥      components (sigma branch)")
    for Z, N, name in ISOTOPES:
        A_ = Z + N
        r = summary[name]["sigma"]
        print(f"  {A_}   {r['mu']}    {len(r['knotted'])}          2π·{r['bound']:<3d}      {r['knots']}")
    print("\n  bound = 2π(μ + #knotted) = 2π(2A + 1): extensive, slope 4π per nucleon."
          "\n  Observed, not explained; it is a theorem about every realisation of the"
          "\n  closure, not a substrate observable.")
    check("lower bound is 2π(2A+1) on both branches for every isotope",
          all(summary[nm][b]["bound"] == 2 * (Z + N) + 1
              for Z, N, nm in ISOTOPES for b in summary[nm]))
    check("no consecutive pair is a (2,2lk)-torus link: the round-chain picture is refuted",
          all(not summary[nm][b]["chain"] for Z, N, nm in ISOTOPES for b in summary[nm]))

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Total curvature as the computable half of the serpenoid tower. Milnor: "
            "inf over the isotopy class of the total curvature equals 2*pi*b(L), and "
            "b(L) >= mu + #knotted components. The canonical closure has mu = A+1 "
            "components (exact integer permutation cycle count, probe-derived at "
            "A=2,3,4,6; carried as hypothesis hmu : mu = A+1 in SLq2LabelParity.lean:77 "
            "and TorusKnotPages.lean:82, bean qou-d5hn) of which A are (2,odd)-torus "
            "knots on both classical branches (exact-integer Kauffman bracket), so inf "
            "total curvature >= 2*pi*(2A+1): extensive with slope 4*pi per nucleon. Under "
            "Crofton, curvature = pi * (mean number of critical points of the height "
            "functions), which is the precise form of 'the oscillations happen at "
            "the saddle points'. The twist is not produced here.")
        for nm, rec in summary.items():
            for b, r in rec.items():
                tag = f"{nm}_{b.replace('^', '')}"
                wb.add_data(f"{tag}_mu", str(r["mu"]))
                wb.add_data(f"{tag}_components", str(r["knots"]))
                wb.add_data(f"{tag}_curvature_bound_over_2pi", str(r["bound"]))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "The canonical word is a Hecke element, not a braid: its 2A+1 averaged "
            "letters have no crossing sign. Everything geometric here is per "
            "classical branch. A link-theoretic statement about the un-resolved "
            "object does not exist, and this probe does not make one.")
        wb.add_caveat(
            "Knot types are read from the Jones polynomial. Jones distinguishes the "
            "(2,odd)-torus knots from the unknot unconditionally (non-trivial "
            "polynomial => knotted); naming a component T(2,k) from its Jones "
            "polynomial alone is an identification, safe at these crossing numbers.")
        wb.add_caveat(
            "The lower bound 2*pi*(2A+1) is a theorem about every geometric "
            "realisation of the closure. It is NOT a substrate observable and it "
            "is NOT connected to binding by anything here. Its extensivity is "
            "noted because the theta_lambda gate needed an extensive channel; "
            "that is an observation about shape, not a mechanism.")
        wb.add_caveat(
            "This is the curvature half. The hull-exit analysis puts the missing "
            "ingredient in the twist, a torsion integral the osculating circle "
            "is blind to. Nothing here supplies it.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
