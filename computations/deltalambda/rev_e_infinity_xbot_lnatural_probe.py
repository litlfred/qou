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

## What it does NOT settle

M5 certifies `pe <= PEMAX` and `T <= N`.  Two lemmas are still open, and until both land the
cut in M6 is conditional on them and must not be quoted as the unconditional bound:

  1. tail (all T): rows above the support never help, so `T > N` cannot exceed the `N`-row max;
  2. all pe: frames beyond `PEMAX` add nothing, because frame `pe + 1` with `u_0 = 0` is frame
     `pe` shifted and deep wall rows pay `ln q0 (pe - j)` each.

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
check("M6 the G1-free cut is enumerable for pe <= PEMAX, T <= N", CUT <= ENUM_LIMIT,
      f"cut {CUT} against the limit {ENUM_LIMIT} (the relaxation bound gives 48).  CONDITIONAL "
      f"on the tail lemma (T > {NROWS}) and the all-pe lemma (pe > {PEMAX}); both open")

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {"script": "computations/deltalambda/rev_e_infinity_xbot_lnatural_probe.py"},
    "bean": "qou-as81",
    "anchor": "physical_proton",
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
    "open_gaps": [
        f"tail lemma: blocks longer than N = {NROWS} rows never exceed the N-row maximum",
        f"all-pe lemma: frames pe > {PEMAX} add nothing over pe <= {PEMAX}",
    ],
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
