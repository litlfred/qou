"""The bottom edge's INTEGER program is L-natural-concave, so its maximum is certified exactly.

Bean `qou-as81`.  Follow-up to `rev_e_infinity_xbot_relaxation_probe.py` (PR #7419), whose R6
is red by design: the concave relaxation bounds `sup Xbot` by `B_bot = 3.37605`, 1.563x the
enumerated maximum `2.15980`, and that bound leaves the G1-free cut at 48, above the enumerable
limit of 32.  The relaxation is loose because a REAL displacement can collect a small positive
gain on arbitrarily many rows, which no integer block can.  This probe stops relaxing.

## The structure

For a frame `pe` and a block of `N` rows, `G(u)` (the relaxation probe's objective at `lam = 0`)
splits exactly as

    G(u) = sum_j phi_j(u_j) + sum_{j < j'} psi_{jj'}(u_j' - u_j)

    phi_j(x)     = R(b_j) - R(b_j + x) + W(h_j) - W(h_j - x) - ln q0 * w_j * x - (ln q0 / 2) x^2
    psi_{jj'}(d) = eps(g_{jj'}) - eps(g_{jj'} + d)

with `b_j = b0(pe, j)`, `h_j = b0(pe, N) - b_j`, `g_{jj'} = b_j' - b_j`, `w_j` the wall's linear
weight.  Every `phi_j` and every `psi_{jj'}` is concave in ONE variable, and the domain (where
every `eps` argument is positive, and `u >= 0`) is cut out by box and difference constraints.
That is the L-natural-concave form (Murota, *Discrete Convex Analysis*, SIAM 2003, Sect. 7.1:
a separable concave function plus concave functions of pairwise differences).

The theorem that makes this a certificate rather than a search: for an L-natural-concave
`g : Z^n -> R u {-inf}`, a point `u` of its domain is a GLOBAL maximiser iff

    g(u) >= g(u + chi_S)  and  g(u) >= g(u - chi_S)    for every subset S

(Murota 2003, Ch. 7, the L-natural optimality criterion, stated there for L-natural-convex
minimisation).  And the best `+-chi_S`
move is an s-t minimum cut, because the gain of `u + chi_S` is a supermodular set function with
pairwise interactions (its pair part is submodular-as-a-cost exactly when `psi` is concave at
integers, which M3 measures).  So the integer maximum for a fixed `(pe, N)` is certified by two
max-flow computations at the optimum.

## What it checks

  M1  the split form equals the committed `G` on random integer points (it IS the same function)
  M2  appending undisplaced rows above the block leaves `G` unchanged, so `N` rows covers every
      block of length `T <= N`
  M3  every `phi_j` and `psi_{jj'}` is concave at the integers the ascent can visit
  M4  the min-cut move equals brute force over all `2^n` subsets, both signs, on small blocks
  M5  steepest ascent from `u = 0` reaches a point no `+-chi_S` move improves, for every frame
      `pe = 0..PEMAX` at `N` rows: the exact integer maximum for that `(pe, N)`
  M6  with that maximum as `B_bot`, the G1-free cut is enumerable (<= 32) — what R6 asks

  M7  the tail lemma (every block length `T`), M7b a direct min-cut check at `T = N + 4, N + 12`
  M8  the shift identity `G_{pe+1}(0, u) = G_pe(u)`
  M9  the wall inequality that makes frames beyond `PEMAX` add nothing

## The two lemmas

M5 alone certifies `pe <= PEMAX` and `T <= N`.  The cut in M6 needs every `T` and every `pe`.
Write the program on the whole infinite frame (rows above the block are undisplaced, which M2
shows is the same function), so a block is a finitely supported `u >= 0`.

**Tail lemma (M7).**  Let `w` be the certified `N`-row optimum, padded with zeros.  By the
L-natural criterion it suffices that no `+chi_S` move improves `w` for any finite `S` (a `-chi_S`
move touching a zero row leaves the domain).  Split `S = L u H` with `L` below row `N` and
`H != {}` at or above it (`N >= pe`, so `H` lies on the gap-2 lattice).  With
`p-(g) = eps(g - 1) - eps(g)` and `p+(g) = eps(g) - eps(g + 1) <= p-(g)` (convexity of `eps`):

    gain(S) = gain(L) + sum_{j in H} [eps(b_j + 1) - (ln q0)/2]
              + sum_{j in H, x < j, x not in H} (p+ or p-)(gap_xj)  -  sum_{j in H, y > j, y not in H} p-(gap_jy)

(a pair with one end in `L` and one in `H` is counted `-p-` in `gain(L)` and `0` in `gain(S)`,
hence the `p-` option below).  On the bi-infinite gap-2 lattice with `w = 0`, the two cross sums
are equal: `sum_{j in H} sum_{x not in H} sgn(j - x) P(|j - x|)` vanishes, since summed over all
`x` it is zero for each `j` and the `x in H` part is antisymmetric.  What is left is the
difference between this frame's rows below `N` and the lattice's: the gap-1 wall rows and the
rows `w` displaces, each contributing at most `p-(gap - w_x)`.  Every term decreases with `j`, so

    gain(S) <= gain(L) + |H| [eps(b_N + 1) + cbar_N - (ln q0)/2] ,

and M7 measures the bracket negative at every frame (`gain(L) <= 0` is M5).  If `gain(L)` is
`-inf`, the offending pair lies below `N` and makes `gain(S)` `-inf` too.

**All-pe lemma (M8, M9).**  Rows `j >= 1` of frame `pe + 1` sit one position above rows `j - 1`
of frame `pe`, with the same gaps and wall weights `pe + 1 - j`.  The bottom row's pair term
`eps(b) - eps(b + x)` plus the shifted one-body sum `sum_{k=1..x} eps(b + k)` is exactly the
unshifted one-body sum `sum_{k=0..x-1} eps(b + k)`, so `G_{pe+1}(0, u) = G_pe(u)` (M8).  Raising
the bottom row by `x >= 1` gains at most `x eps(1)` in its one-body term, pays `ln q0 (pe + 1) x`
on the wall, and only loses on its pairs (they close).  When `eps(1) < ln q0 (pe + 1)`, zeroing
it never lowers `G`, so `sup` over frame `pe + 1` equals `sup` over frame `pe`.  M9 checks this
at `pe + 1 = PEMAX + 1`; it holds for every larger `pe` too.  (`eps(1) / ln q0 = 16.0002`, so
the inequality first holds at `pe + 1 = 17`.)

Both lemmas use only that `eps` is decreasing and convex, the L-natural criterion, and the
certified `N`-row optima.  With them the cut in M6 holds for every frame and block length.

-- Ref: [murota2003] Discrete Convex Analysis, SIAM, 2003, Ch. 7 (L-natural optimality criterion)
"""

from __future__ import annotations

import functools
import json
import os
import random
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

# The relaxation probe's definitions, executed rather than re-derived: M1 compares against the
# `G` that probe certifies, so it has to be that `G`.  Only the prelude runs (no stage, no
# checkpoint store); the split is asserted.
_SRC = os.path.join(_HERE, "rev_e_infinity_xbot_relaxation_probe.py")
_TEXT = open(_SRC).read()
_MARK = 'print("the BOTTOM edge'
if _MARK not in _TEXT:
    raise SystemExit(f"banner {_MARK!r} not found in {_SRC} — refusing to guess a split")
_NS: dict = {"__name__": "_xbot_relaxation_defs", "__file__": _SRC}
exec(_TEXT[:_TEXT.index(_MARK)], _NS)  # noqa: S102 — deliberate, and the split is asserted

mp = _NS["mp"]
# The relaxation probe's working precision, restated here because a prelude run
# through exec() is invisible to the import-time / never-raises dps audits. The
# assert keeps the two in step: change the relaxation probe and this fails.
assert mp.dps == 25, f"relaxation probe dps moved to {mp.dps}; update this probe"
mp.dps = 25
G, R, W, epsx = _NS["G"], _NS["R"], _NS["W"], _NS["epsx"]
b0_of, lin_w = _NS["b0_of"], _NS["lin_w"]
LNQ, LNQ_HALF, TOL = _NS["LNQ"], _NS["LNQ_HALF"], _NS["TOL"]
E_INF_7335, B_TOP_CERT = _NS["E_INF_7335"], _NS["B_TOP_CERT"]
_sc, _ap_value = _NS["_sc"], _NS["_ap_value"]
Q_50_DIGIT_STR = _NS["Q_50_DIGIT_STR"]

PEMAX = int(os.environ.get("REV_XBOTL_PEMAX", "20"))
NROWS = int(os.environ.get("REV_XBOTL_N", "40"))
# The run lengths `cut_for` scans — the same 1..2999 window as the relaxation probe's R6, so the
# two cuts are comparable.  A full scan is ~1 h (xrun grows ~quadratically); lower it only for a
# smoke run, and the witness records what was used.
ELLMAX = int(os.environ.get("REV_XBOTL_ELLMAX", "3000"))
ENUM_LIMIT = 32                                  # the cut R6 needs (blocks enumerable below it)
GAIN_TOL = mp.mpf(10) ** -18                     # a move counts as improving above this
NEG_INF = mp.mpf("-inf")

# The enumerated maximum (BMAX = 10, BUMAX = 3) recorded by the relaxation probe's R4.
_REL_WIT = os.path.join(_HERE, "rev-e-infinity-xbot-relaxation.witness.json")
def _find(o, key):
    if isinstance(o, dict):
        if key in o:
            return o[key]
        o = list(o.values())
    if isinstance(o, list):
        for x in o:
            r = _find(x, key)
            if r is not None:
                return r
    return None


_ENUM = _find(json.load(open(_REL_WIT)), "enumerated_max_Xbot")
INT_SUP_ENUM = mp.mpf(_ENUM) if _ENUM is not None else None

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


# --------------------------------------------------------------------------------------------
# The split
# --------------------------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def phi(pe: int, n: int, j: int, x: int) -> mp.mpf:
    """One-body piece of row `j` at integer displacement `x`; `-inf` off the domain."""
    if x < 0:
        return NEG_INF
    b = b0_of(pe, j)
    h = b0_of(pe, n) - b
    if h - x <= 0:
        return NEG_INF
    x = mp.mpf(x)
    return (R(b) - R(b + x) + W(mp.mpf(h), pe, n) - W(h - x, pe, n)
            - LNQ * lin_w(pe, j) * x - LNQ_HALF * x * x)


@functools.lru_cache(maxsize=None)
def psi(pe: int, j: int, jp: int, d: int) -> mp.mpf:
    """Pair piece of rows `j < jp` at difference `d = u_jp - u_j`; `-inf` off the domain."""
    g = b0_of(pe, jp) - b0_of(pe, j)
    if g + d <= 0:
        return NEG_INF
    return epsx(mp.mpf(g)) - epsx(mp.mpf(g + d))


def G_split(u, pe: int) -> mp.mpf:
    n = len(u)
    tot = mp.fsum(phi(pe, n, j, u[j]) for j in range(n))
    for j in range(n):
        for jp in range(j + 1, n):
            tot += psi(pe, j, jp, u[jp] - u[j])
    return tot


# --------------------------------------------------------------------------------------------
# The best +-chi_S move as an s-t minimum cut, in mpf throughout
# --------------------------------------------------------------------------------------------
def _maxflow(cap, s: int, t: int):
    """Edmonds-Karp on a dense capacity matrix of mpf (and +inf).  Returns (flow, source side)."""
    n = len(cap)
    res = [row[:] for row in cap]
    flow = mp.mpf(0)
    while True:
        par = [-1] * n
        par[s] = s
        q = [s]
        for v in q:
            for w in range(n):
                if par[w] < 0 and res[v][w] > 0:
                    par[w] = v
                    q.append(w)
        if par[t] < 0:
            return flow, [v for v in range(n) if par[v] >= 0]
        f = mp.inf
        w = t
        while w != s:
            f = min(f, res[par[w]][w])
            w = par[w]
        if f == mp.inf:
            raise ValueError("an infinite-capacity s-t path: the move problem is unbounded")
        w = t
        while w != s:
            res[par[w]][w] -= f
            res[w][par[w]] += f
            w = par[w]
        flow += f


def best_move(u, pe: int, sign: int, force: int | None = None):
    """max over S of G(u + sign chi_S) - G(u), and an S attaining it.  With `force = v` the max
    is over S containing v only (an infinite cost on x_v = 0), which is how M5 measures the best
    NON-EMPTY move: the plain min cut always has the empty set at gain 0 to fall back on.

    Minimise the cost E(x) = -gain over x in {0,1}^n (x_j = 1 iff j in S).  Node j on the SINK
    side means x_j = 1.  A unary cost c x_j is an edge s->j of capacity c (c >= 0) or the
    constant c plus an edge j->t of capacity -c (c < 0).  A pair term with E(0,0) = E(1,1) = 0,
    E(0,1) = A, E(1,0) = B is the edge j->j' (A) plus j'->j (B) when both are >= 0; otherwise it
    is reparametrised through the unaries, which needs exactly A + B >= 0 — i.e. concavity of
    `psi` at the integers involved (M3)."""
    n = len(u)
    unary = [mp.mpf(0)] * n
    pair = []
    base_phi = [phi(pe, n, j, u[j]) for j in range(n)]
    for j in range(n):
        new = phi(pe, n, j, u[j] + sign)
        unary[j] = mp.inf if new == NEG_INF else -(new - base_phi[j])
    for j in range(n):
        for jp in range(j + 1, n):
            d0 = u[jp] - u[j]
            p0 = psi(pe, j, jp, d0)
            # x_j = 0, x_jp = 1 moves the difference by +sign; x_j = 1, x_jp = 0 by -sign
            pa, pb = psi(pe, j, jp, d0 + sign), psi(pe, j, jp, d0 - sign)
            A = mp.inf if pa == NEG_INF else -(pa - p0)
            B = mp.inf if pb == NEG_INF else -(pb - p0)
            if A + B < 0:
                raise ValueError(f"pair ({j},{jp}) is not concave at d = {d0}: A + B = {A + B}")
            pair.append((j, jp, A, B))
    s, t = n, n + 1
    cap = [[mp.mpf(0)] * (n + 2) for _ in range(n + 2)]
    const = mp.mpf(0)

    def add_unary(v, c):
        nonlocal const
        if c >= 0:
            cap[s][v] += c
        else:
            const += c
            cap[v][t] += -c

    for j in range(n):
        add_unary(j, unary[j])
    if force is not None:
        cap[force][t] = mp.inf
    for j, jp, A, B in pair:
        if A >= 0 and B >= 0:
            cap[j][jp] += A
            cap[jp][j] += B
        elif A < 0:          # A x_jp - A x_j + (A + B) x_j (1 - x_jp)
            add_unary(jp, A)
            add_unary(j, -A)
            cap[jp][j] += A + B
        else:                # B x_j - B x_jp + (A + B)(1 - x_j) x_jp
            add_unary(j, B)
            add_unary(jp, -B)
            cap[j][jp] += A + B
    try:
        flow, src_side = _maxflow(cap, s, t)
    except ValueError:
        if force is None:
            raise
        return NEG_INF, []          # every S containing `force` leaves the domain
    S = [v for v in range(n) if v not in src_side]
    return -(flow + const), S


def apply_move(u, S, sign):
    return [x + sign if j in S else x for j, x in enumerate(u)]


def steepest_ascent(pe: int, n: int, max_steps: int = 200):
    u = [0] * n
    steps = 0
    while True:
        gp, Sp = best_move(u, pe, +1)
        gm, Sm = best_move(u, pe, -1)
        if max(gp, gm) <= GAIN_TOL:
            margin = max(best_move(u, pe, sg, force=v)[0] for sg in (+1, -1) for v in range(n))
            return u, steps, gp, gm, margin
        u = apply_move(u, Sp, +1) if gp >= gm else apply_move(u, Sm, -1)
        steps += 1
        if steps > max_steps:
            raise RuntimeError(f"no convergence at pe = {pe} after {max_steps} steps")


# --------------------------------------------------------------------------------------------
print("the bottom edge's INTEGER program is L-natural-concave — exact maximum by min cut")
print(f"  q0 = {mp.nstr(mp.mpf(Q_50_DIGIT_STR), 20)} (proton pin);  mp.dps = {mp.dps}")
print(f"  frames pe = 0..{PEMAX}, N = {NROWS} rows")
print(flush=True)

random.seed(7)


def _random_feasible(pe: int, n: int, top: int = 4):
    """A random integer point of the domain, built top-down so each row respects the row above."""
    for _ in range(200):
        u = [random.randint(0, top) for _ in range(n)]
        if G_split(u, pe) != NEG_INF:
            return u
    return [0] * n


print("M1  the split form equals the committed G")
_m1 = mp.mpf(0)
_m1n = 0
for _ in range(60):
    _pe = random.randint(0, 8)
    _n = random.randint(2, 9)
    _u = _random_feasible(_pe, _n)
    _a, _b = G([mp.mpf(x) for x in _u], _pe), G_split(_u, _pe)
    if _a == NEG_INF or _b == NEG_INF:
        continue
    _m1 = max(_m1, abs(_a - _b))
    _m1n += 1
check("M1 the split form is the committed G", _m1n >= 30 and _m1 < TOL,
      f"{_m1n} random integer points, pe 0..8, n 2..9: max |G - G_split| = {mp.nstr(_m1, 4)}")

print("M2  undisplaced rows above the block change nothing")
_m2 = mp.mpf(0)
for _ in range(30):
    _pe = random.randint(0, 8)
    _n = random.randint(2, 8)
    _u = _random_feasible(_pe, _n)
    _g0 = G_split(_u, _pe)
    if _g0 == NEG_INF:
        continue
    for _k in (1, 3, 7):
        _m2 = max(_m2, abs(G_split(_u + [0] * _k, _pe) - _g0))
check("M2 zero-padding leaves G unchanged", _m2 < TOL,
      f"max |G(u, 0^k) - G(u)| = {mp.nstr(_m2, 4)} for k = 1, 3, 7 — so an N-row program covers "
      f"every block of length T <= N")

print("M3  discrete concavity of every piece")
_m3 = mp.inf
for _pe in range(0, PEMAX + 1, 4):
    for _j in range(0, 12):
        for _x in range(1, 8):
            _a, _b, _c = (phi(_pe, NROWS, _j, _x + e) for e in (-1, 0, 1))
            if NEG_INF not in (_a, _b, _c):
                _m3 = min(_m3, 2 * _b - _a - _c)
        for _jp in range(_j + 1, 12):
            for _d in range(-6, 7):
                _a, _b, _c = (psi(_pe, _j, _jp, _d + e) for e in (-1, 0, 1))
                if NEG_INF not in (_a, _b, _c):
                    _m3 = min(_m3, 2 * _b - _a - _c)
check("M3 every piece is concave at the integers", _m3 > 0,
      f"min second difference 2f(x) - f(x-1) - f(x+1) over the sampled pieces = {mp.nstr(_m3, 6)}")

print("M4  the min-cut move against brute force")
_m4 = mp.mpf(0)
_m4n = 0
for _ in range(25):
    _pe = random.randint(0, 6)
    _n = random.randint(3, 9)
    _u = _random_feasible(_pe, _n, top=3)
    _g0 = G_split(_u, _pe)
    if _g0 == NEG_INF:
        continue
    for _sg in (+1, -1):
        _cut, _S = best_move(_u, _pe, _sg)
        _bf = max((G_split(apply_move(_u, [v for v in range(_n) if (m >> v) & 1], _sg), _pe) - _g0)
                  for m in range(1 << _n))
        _cut_S = G_split(apply_move(_u, _S, _sg), _pe) - _g0
        _m4 = max(_m4, abs(_cut - _bf), abs(_cut_S - _bf))
        _m4n += 1
check("M4 the min-cut move is the best move", _m4n >= 30 and _m4 < TOL,
      f"{_m4n} (point, sign) cases, n <= 9, all 2^n subsets: max |cut - brute force| = "
      f"{mp.nstr(_m4, 4)}, and the returned S attains it")

print("M5  steepest ascent to a certified integer maximum, per frame")
_m5 = []
for _pe in range(0, PEMAX + 1):
    _u, _st, _gp, _gm, _mg = steepest_ascent(_pe, NROWS)
    _v = G_split(_u, _pe)
    _supp = [j for j, x in enumerate(_u) if x]
    _m5.append({"pe": _pe, "max": mp.nstr(_v, 22), "steps": _st,
                "best_plus_gain": mp.nstr(_gp, 6), "best_minus_gain": mp.nstr(_gm, 6),
                "best_nonempty_gain": mp.nstr(_mg, 8),
                "argmax_bottom_up": _u[:max(_supp) + 1] if _supp else []})
    print(f"    pe = {_pe:2d}: max {mp.nstr(_v, 22)}  steps {_st}  "
          f"best non-empty move {mp.nstr(_mg, 6)}  "
          f"u = {_m5[-1]['argmax_bottom_up']}", flush=True)
B_INT = max(mp.mpf(r["max"]) for r in _m5)
MARGIN = max(mp.mpf(r["best_nonempty_gain"]) for r in _m5)
_top_supp = max(len(r["argmax_bottom_up"]) for r in _m5)
check("M5 every frame reaches a point no +-chi_S move improves",
      all(mp.mpf(r["best_plus_gain"]) <= GAIN_TOL and mp.mpf(r["best_minus_gain"]) <= GAIN_TOL
          for r in _m5) and MARGIN < -GAIN_TOL and _top_supp < NROWS,
      f"pe = 0..{PEMAX} at N = {NROWS} rows: max over frames {mp.nstr(B_INT, 22)}.  The best "
      f"NON-EMPTY move at any optimum gains {mp.nstr(MARGIN, 6)}, so the certificate does not rest "
      f"on rounding (the gains are evaluated at mp.dps = {mp.dps}).  The deepest "
      f"support is {_top_supp} rows, well inside N.  By Murota's L-natural optimality theorem "
      f"each is the exact integer maximum for its (pe, N)"
      + (f"; the BMAX = 10 enumeration recorded {mp.nstr(INT_SUP_ENUM, 22)}"
         if INT_SUP_ENUM is not None else ""))

print("M7  tail lemma: rows above N never help (every block length T)")


def pminus(g) -> mp.mpf:
    """`eps(g - 1) - eps(g)`: what a pair at gap `g` loses when it closes by one.  `eps` is convex
    and decreasing, so this is positive, decreasing in `g`, and at least the matching gain
    `eps(g) - eps(g + 1)` of the pair opening by one."""
    return epsx(mp.mpf(g - 1)) - epsx(mp.mpf(g))


def tail_bound(pe: int, w, n: int) -> mp.mpf:
    """`eps(b_n + 1) + cbar_n`, the bound on what one row `j >= n` adds to any move.

    Argument (written out in the module docstring, section "The two lemmas").  Pad the certified
    point `w` with zeros; take any move `S = L u H`, `L` below row `n`, `H` at or above it.  The
    move's gain is the gain of `L` alone plus, for each `j` in `H`, its one-body change
    `eps(b_j + 1) - (ln q0)/2` and its cross pairs.  Against the bi-infinite gap-2 lattice the
    cross pairs cancel EXACTLY (the sum over pairs with one end in `H` is antisymmetric), so what
    survives is the difference between this frame's rows below `n` and the lattice's: the wall
    rows (gap 1, not on the lattice) and the rows `w` displaces.  Each costs at most
    `pminus(gap - w_x)`, and every term decreases with `j`, so row `n` is the worst case."""
    bn = b0_of(pe, n)
    tot = epsx(mp.mpf(bn + 1))
    for x in range(n):
        wx = w[x] if x < len(w) else 0
        if x < pe or wx > 0:
            tot += pminus(bn - b0_of(pe, x) - wx)
    return tot


_m7 = []
for r in _m5:
    _w = list(r["argmax_bottom_up"])
    _tb = tail_bound(r["pe"], _w, NROWS)
    _m7.append((r["pe"], _tb))
_m7worst = max(t for _, t in _m7)
check("M7 the tail lemma holds at every certified frame",
      all(r["pe"] <= NROWS for r in _m5) and _m7worst < LNQ_HALF,
      f"per-row bound eps(b_N + 1) + cbar_N <= {mp.nstr(_m7worst, 8)} against (ln q0)/2 = "
      f"{mp.nstr(LNQ_HALF, 8)} at N = {NROWS}, pe = 0..{PEMAX}.  So any move touching a row >= N "
      f"gains strictly less than the same move without those rows, which M5 already showed is "
      f"<= 0: the N-row maximum is the maximum over EVERY block length")

# Direct cross-check on longer blocks: the padded optimum is still certified by min cut.
_m7b = mp.mpf("-inf")
for _pe in (0, 3, PEMAX):
    _w = list(_m5[_pe]["argmax_bottom_up"])
    for _extra in (4, 12):
        _n = NROWS + _extra
        _u = _w + [0] * (_n - len(_w))
        for _sg in (+1, -1):
            _m7b = max(_m7b, best_move(_u, _pe, _sg)[0])
check("M7b longer blocks agree: no move improves the padded optimum at T = N + 4, N + 12",
      _m7b <= GAIN_TOL,
      f"best +-chi_S gain at pe in (0, 3, {PEMAX}), T in (N + 4, N + 12): {mp.nstr(_m7b, 6)}")

print("M8  frame pe + 1 with an undisplaced bottom row IS frame pe")
_m8 = mp.mpf(0)
_m8n = 0
for _ in range(40):
    _pe = random.randint(0, 12)
    _n = random.randint(2, 8)
    _u = _random_feasible(_pe, _n)
    _a = G_split(_u, _pe)
    if _a == NEG_INF:
        continue
    _m8 = max(_m8, abs(G_split([0] + _u, _pe + 1) - _a))
    _m8n += 1
check("M8 G_{pe+1}(0, u) = G_pe(u)", _m8n >= 20 and _m8 < TOL,
      f"{_m8n} random points, pe 0..12: max difference {mp.nstr(_m8, 4)}.  Rows j >= 1 of frame "
      f"pe + 1 sit one position above rows j - 1 of frame pe with the same gaps and wall weights, "
      f"and the bottom row's pair term eps(b) - eps(b + x) plus the one-body sum over b + 1..b + x "
      f"is exactly the one-body sum over b..b + x - 1")

print("M9  all-pe lemma: displacing the bottom row of a deep wall never pays")
_eps1 = epsx(mp.mpf(1))
_wall = LNQ * (PEMAX + 1)
check("M9 eps(1) < ln q0 * (PEMAX + 1)", _eps1 < _wall,
      f"eps(1) = {mp.nstr(_eps1, 10)} < ln q0 * {PEMAX + 1} = {mp.nstr(_wall, 10)}.  In frame "
      f"pe + 1 >= {PEMAX + 1}, raising the bottom row by x >= 1 gains at most x eps(1) in its "
      f"one-body term, pays ln q0 (pe + 1) x on the wall, and only loses on its pairs (they close).  "
      f"So zeroing it never lowers G, and with M8 sup(frame pe + 1) = sup(frame pe) for every "
      f"pe >= {PEMAX}: the frames beyond PEMAX add nothing")
LEMMAS_OK = all(o for n, o, _ in CHECKS if n.startswith(("M7", "M8", "M9")))

print("M6  the G1-free cut with the certified integer maximum")
_XR: dict[int, mp.mpf] = {}


def xrun(ell: int) -> mp.mpf:
    if ell not in _XR:
        _XR[ell] = _sc(_ap_value([-1] * ell, False))
    return _XR[ell]


def cut_for(b_top, b_bot) -> int:
    th = E_INF_7335 - b_top - b_bot
    return max(ell for ell in range(1, ELLMAX) if xrun(ell) > th)


CUT = cut_for(B_TOP_CERT, B_INT)
_th = E_INF_7335 - B_TOP_CERT - B_INT
print(f"    B_bot = {mp.nstr(B_INT, 22)}  threshold {mp.nstr(_th, 8)}  "
      f"xrun({CUT}) = {mp.nstr(xrun(CUT), 8)}  xrun({CUT + 1}) = {mp.nstr(xrun(CUT + 1), 8)}")
check("M6 the G1-free cut is enumerable for every frame and block length",
      CUT <= ENUM_LIMIT and LEMMAS_OK,
      f"cut {CUT} against the limit {ENUM_LIMIT} (the relaxation bound gives 48).  Unconditional "
      f"in T and pe: M7 covers T > {NROWS}, M8 + M9 cover pe > {PEMAX}")

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {"script": "computations/deltalambda/rev_e_infinity_xbot_lnatural_probe.py"},
    "bean": "qou-as81",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key
    # above is a near-miss spelling they cannot see).
    "q0Anchor": "proton",
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The bottom edge's integer program is L-natural-concave (separable concave plus concave "
        "functions of pairwise differences, over a box-and-difference domain), so a point that "
        "no +-chi_S move improves is the global integer maximum (Murota 2003, Ch. 7), and the "
        "best move is an s-t minimum cut.  This replaces the concave relaxation's 1.563x bound "
        "with the exact integer maximum for every certified (pe, N)."),
    "params": {"PEMAX": PEMAX, "N": NROWS, "ELLMAX": ELLMAX, "gain_tol": mp.nstr(GAIN_TOL, 4)},
    "frames_M5": _m5,
    "B_bot_integer": mp.nstr(B_INT, 22),
    "cut_M6": {"cut": CUT, "limit": ENUM_LIMIT, "threshold": mp.nstr(_th, 22),
               "relaxation_cut": 48},
    "lemmas": {
        "tail_M7": {"per_row_bound_worst": mp.nstr(_m7worst, 12), "against": mp.nstr(LNQ_HALF, 12),
                    "per_frame": [{"pe": a, "bound": mp.nstr(b, 10)} for a, b in _m7]},
        "all_pe_M8_M9": {"eps1": mp.nstr(_eps1, 12), "wall_cost": mp.nstr(_wall, 12),
                         "shift_identity_max_err": mp.nstr(_m8, 4)},
    },
    "open_gaps": [] if LEMMAS_OK else ["tail lemma or all-pe lemma check failed; see checks"],
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
}
_out = os.path.join(_HERE, "rev-e-infinity-xbot-lnatural.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")
_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
