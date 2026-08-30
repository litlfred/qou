#!/usr/bin/env python3
# polynomial_q_not_applicable: exact-integer Laurent knot invariant; no substrate q.
"""Exact two-variable HOMFLY of a braid closure, by skein recursion.

Why this module exists (measured, 2026-08-21). The corpus's
`computations/homflypt_engine.py` advertises "Outputs are LaurentPoly2
objects in (v, z)", and that is true only for `n_strands == 2`. Its
`n >= 3` branch (`homflypt_from_braid`, the `# For n >= 3` block)
evaluates the Ocneanu trace *numerically* at the substrate q_0 and then
stores the single float in `terms[(0, 0)]`. A consumer that reads
v-degrees off the result therefore gets `min = max = 0`, i.e. **spread
0**, with no error raised. For a Morton-Franks-Williams reading that is
worse than a crash: spread 0 gives the vacuous bound `braid index >= 1`,
which "confirms" every hypothesis.

The other candidate source is equally unusable for MFW, for a
mathematical rather than a coding reason: the corpus Markov trace is
specialised to the SU(2)/Temperley-Lieb point (convention D,
`z = q^3/(q^2+1)`, `pyhecke_native.markov_z`). That specialisation is
precisely the collapse of the `v` direction, and `v`-degree is the whole
content of MFW. So the C-vs-D convention question does **not** gate this
module -- HOMFLY is computed before any specialisation, in `Z[v^,z^]`.

## Method: descending-diagram skein recursion on braid words

HOMFLY in the Lickorish `(v, z)` convention is defined by

    v^{-1} P(L+) - v P(L-) = z P(L0),      P(unknot) = 1,

so, solving for the crossing being resolved,

    P(L+) = v^2 P(L-) + v z P(L0)
    P(L-) = v^{-2} P(L+) - v^{-1} z P(L0).

The closure of a braid word is a link diagram on which both moves are
*word* operations: switching a crossing is `sigma_i <-> sigma_i^{-1}`
(letter sign flip) and smoothing it is letter deletion. Recursion:

1. Walk the closure, in a fixed component order from fixed base points,
   recording each crossing's two encounters.
2. A crossing is **bad** if its *first* encounter is an under-crossing.
3. No bad crossings => the diagram is descending => its link is the
   `c`-component unlink => `P = delta^{c-1}` with `delta = (v^{-1}-v)/z`.
4. Otherwise resolve the first bad crossing by the identity above.

Termination is on the lexicographic pair `(word length, #bad)`: a
crossing switch leaves the diagram's shadow -- hence the whole traversal
and every earlier over/under decision -- untouched, so it makes that one
crossing good and strictly lowers `#bad`; a smoothing strictly lowers
the word length. Both branches descend, so the recursion is finite.

Coefficients are exact Python `int`s throughout; there is no floating
point anywhere in this module and no substrate constant is read.

Convention note: with the over/under rule fixed below (`sigma_i` = the
strand entering at position `i` passes **over**), `[1,1,1]` comes out as
the trefoil with positive `v`-degrees. Mirror conventions differ by
`v -> v^{-1}`, which leaves the `v`-spread -- the only quantity MFW
consumes -- invariant.
"""
from __future__ import annotations

from functools import lru_cache

# ── exact Laurent polynomials in (v, z) over Z ───────────────────────


class LP2:
    """Sparse Laurent polynomial in (v, z) with integer coefficients."""

    __slots__ = ("t",)

    def __init__(self, terms: dict[tuple[int, int], int] | None = None):
        self.t = {k: c for k, c in (terms or {}).items() if c}

    @classmethod
    def mono(cls, i: int, j: int, c: int = 1) -> "LP2":
        return cls({(i, j): c})

    @classmethod
    def one(cls) -> "LP2":
        return cls({(0, 0): 1})

    def __add__(self, o: "LP2") -> "LP2":
        r = dict(self.t)
        for k, c in o.t.items():
            r[k] = r.get(k, 0) + c
        return LP2(r)

    def __mul__(self, o: "LP2") -> "LP2":
        r: dict[tuple[int, int], int] = {}
        for (a, b), c in self.t.items():
            for (x, y), d in o.t.items():
                k = (a + x, b + y)
                r[k] = r.get(k, 0) + c * d
        return LP2(r)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, LP2) and self.t == o.t

    def v_degrees(self) -> tuple[int, int]:
        """(min, max) exponent of v. Raises on the zero polynomial."""
        if not self.t:
            raise ValueError("v-degree of the zero polynomial is undefined")
        vs = [i for (i, _) in self.t]
        return min(vs), max(vs)

    def v_spread(self) -> int:
        lo, hi = self.v_degrees()
        return hi - lo

    def __repr__(self) -> str:
        if not self.t:
            return "0"
        out = []
        for (i, j), c in sorted(self.t.items()):
            p = "" if c > 0 and out else ("" if c > 0 else "-")
            s = f"{p}{abs(c) if abs(c) != 1 or (i == 0 and j == 0) else ''}"
            if i:
                s += f"v^{i}" if i != 1 else "v"
            if j:
                s += f"z^{j}" if j != 1 else "z"
            out.append(s)
        return " + ".join(out).replace("+ -", "- ")


DELTA = LP2({(-1, -1): 1, (1, -1): -1})   # (v^{-1} - v)/z


# ── braid-closure traversal ──────────────────────────────────────────


def _step(level_letter: int, pos: int) -> tuple[int, bool | None]:
    """Pass position `pos` through one braid letter.

    Returns `(new_pos, over)` where `over` is None when this strand is
    not involved in the crossing. Convention: for `sigma_i` (letter > 0)
    the strand entering at position `i` passes OVER.
    """
    i = abs(level_letter)
    if pos == i:
        return i + 1, level_letter > 0
    if pos == i + 1:
        return i, level_letter < 0
    return pos, None


def traverse(word: tuple[int, ...], n: int) -> tuple[list[tuple[int, bool]], int]:
    """Walk every component of the closure of `word` on `n` strands.

    Returns `(encounters, n_components)` where `encounters` is the global
    ordered list of `(crossing_index, over)` pairs -- each crossing index
    appearing exactly twice -- with components taken in increasing order
    of their smallest starting position.
    """
    m = len(word)
    seen_start: set[int] = set()
    encounters: list[tuple[int, bool]] = []
    comps = 0
    for start in range(1, n + 1):
        if start in seen_start:
            continue
        comps += 1
        pos = start
        seen_start.add(start)
        while True:
            for k in range(m):
                pos, over = _step(word[k], pos)
                if over is not None:
                    encounters.append((k, over))
            if pos == start:
                break
            seen_start.add(pos)
    return encounters, comps


def first_bad(word: tuple[int, ...], n: int) -> tuple[int | None, int]:
    """Index of the first crossing first met as an under-crossing."""
    encounters, comps = traverse(word, n)
    first: dict[int, bool] = {}
    for k, over in encounters:
        if k not in first:
            first[k] = over
    for k, over in sorted(first.items()):
        if not over:
            return k, comps
    return None, comps


# ── the recursion ────────────────────────────────────────────────────


@lru_cache(maxsize=None)
def homfly_braid(word: tuple[int, ...], n: int) -> LP2:
    """Exact HOMFLY `P(closure(word); v, z)` in the Lickorish convention."""
    k, comps = first_bad(word, n)
    if k is None:
        p = LP2.one()
        for _ in range(comps - 1):
            p = p * DELTA
        return p
    switched = word[:k] + (-word[k],) + word[k + 1:]
    smoothed = word[:k] + word[k + 1:]
    if word[k] > 0:                     # resolving a positive crossing
        return (LP2.mono(2, 0) * homfly_braid(switched, n)
                + LP2.mono(1, 1) * homfly_braid(smoothed, n))
    return (LP2.mono(-2, 0) * homfly_braid(switched, n)
            + LP2.mono(-1, 1, -1) * homfly_braid(smoothed, n))


def homfly(word, n_strands: int | None = None) -> LP2:
    """Convenience wrapper: accepts any iterable braid word."""
    w = tuple(int(x) for x in word)
    n = n_strands if n_strands is not None else (max(abs(x) for x in w) + 1 if w else 1)
    return homfly_braid(w, n)


def mfw_data(word, n_strands: int | None = None) -> dict:
    """The Morton-Franks-Williams reading of a braid word.

    `braid_index_lower_bound = v_spread/2 + 1` is the MFW bound; the
    braid index of the *closure* is at least this for every braid
    representative, because the spread is a link invariant.
    """
    w = tuple(int(x) for x in word)
    n = n_strands if n_strands is not None else (max(abs(x) for x in w) + 1 if w else 1)
    P = homfly_braid(w, n)
    lo, hi = P.v_degrees()
    return {
        "word": list(w),
        "n_strands": n,
        "writhe": sum(1 if x > 0 else -1 for x in w),
        "homfly": repr(P),
        "v_min": lo,
        "v_max": hi,
        "v_spread": hi - lo,
        "braid_index_lower_bound": (hi - lo) // 2 + 1,
        "mfw_sharp_for_this_representative": (hi - lo) // 2 + 1 == n,
    }
