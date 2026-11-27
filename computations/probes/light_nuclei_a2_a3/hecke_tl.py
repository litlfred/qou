"""Ocneanu trace at convention D through the Temperley–Lieb quotient (bean qou-sv7h).

Why this is exact, not an approximation
--------------------------------------
Convention D sets z = z_D = q³/(q²+1) = q²/[2], [2] = q + q⁻¹. That is the sl₂ point of the
Ocneanu trace. With e_i a Temperley–Lieb generator (e_i² = δ e_i, δ = [2]), the assignment

    σ_i ↦ q − e_i

satisfies σ² = hσ + 1 (h = q − q⁻¹) and the braid relations, so it is an algebra map
π: H_n → TL_n(δ). The normalised TL Markov trace tr_TL(D) = δ^(loops(closure D) − n) has
tr_TL(e_n) = 1/δ, hence tr_TL(π(σ_n)) = q − 1/δ = q²/[2] = z_D. The Ocneanu trace with a given
z is unique, so tr_D = tr_TL ∘ π on every H_n. (Equivalently: z_D kills every partition with
three or more rows, which is the convention-D truncation qou-w06d works with.) Checked
against the independent ℚ(q) engine `hecke_flint` in `hecke_tl_check.py`.

Letters (same as hecke_flint): ('S', i) = σ_i ↦ q − e_i; ('I', i) = σ_i⁻¹ = σ_i − h ↦ q⁻¹ − e_i;
('A', i) = σ_i − h/2 ↦ [2]/2 − e_i.

Why it scales
-------------
An element of TL_m is a vector over Catalan(m) planar diagrams instead of m! permutations,
and a sweep can open a strand when it is first used (x ↦ x ⊗ 1) and close it after its last
use (the trace-preserving conditional expectation E, i.e. the Markov property). The width of
the sweep, not the strand count, sets the cost. `sweep_trace` takes a program of
('open',), ('close',) and letters; `atom_program` builds the γγ-bonded nucleus in a layout
where finished nucleon strands are closed (see that docstring for why this is the same link).

Arithmetic: any ring whose elements support + and * with the coefficients passed in `R`
(python-flint fmpq for exact ℚ at a rational q, arb for certified balls, fmpq_poly-free).
No float anywhere.
"""
from __future__ import annotations

import time


class Ring:
    """Scalars at a fixed q. `num` is a constructor for the scalar type (flint.fmpq or flint.arb)."""

    def __init__(self, q, num):
        one = num(1)
        self.q = q
        self.qi = one / q
        self.d = q + self.qi           # δ = [2]
        self.di = one / self.d
        self.one = one
        self.zero = num(0)
        self.half = one / 2
        self.coef = {"S": self.q, "I": self.qi, "A": self.d * self.half}


# A diagram on m strands is a tuple `t` of length 2m: points 0..m-1 on top, m..2m-1 on the
# bottom (bottom i is m+i); t[p] is the point p is joined to.

def identity(m):
    return tuple(list(range(m, 2 * m)) + list(range(m)))


def _mul_e(t, m, i):
    """D·e_i (e_i below D). Returns (new diagram, made_loop)."""
    a, b = m + i, m + i + 1
    l = list(t)
    loop = l[a] == b
    if not loop:
        u, v = l[a], l[b]
        l[u] = v
        l[v] = u
    l[a] = b
    l[b] = a
    return tuple(l), loop


def _open(t, m):
    """x ⊗ 1: append a through-strand on the right (m → m+1)."""
    def f(p):
        return p if p < m else p + 1
    l = [f(t[p]) for p in range(m)] + [2 * m + 1] + [f(t[p]) for p in range(m, 2 * m)] + [m]
    return tuple(l)


def _close(t, m, k=None):
    """Partial closure of strand k (default the last; k = 0 is the left edge), m → m−1.
    Returns (diagram, made_loop). Only the two edge strands are closed, so the arc stays planar."""
    k = m - 1 if k is None else k
    top, bot = k, m + k
    l = list(t)
    loop = l[top] == bot
    if not loop:
        u, v = l[top], l[bot]
        l[u] = v
        l[v] = u
    keep = [p for p in range(2 * m) if p not in (top, bot)]
    pos = {p: k for k, p in enumerate(keep)}
    return tuple(pos[l[p]] for p in keep), loop


def _loops_full(t, m):
    """Number of loops in the full (trace) closure: top i joined to bottom i."""
    seen = [False] * (2 * m)
    n = 0
    for s in range(2 * m):
        if seen[s]:
            continue
        n += 1
        p = s
        while True:
            seen[p] = True
            r = t[p]
            seen[r] = True
            p = r - m if r >= m else r + m  # follow the closure arc
            if seen[p]:
                break
    return n


def sweep_trace(program, R, log=None, every=200):
    """Normalised convention-D trace of a program on a growing/shrinking strand set.

    program items: ('open',) | ('close',) | ('lclose',) | (kind, i) with kind in 'S', 'I', 'A'.
    'close' / 'lclose' apply the right / left conditional expectation (the TL Markov trace is
    left-right symmetric, so both preserve the trace).
    Returns (trace value, stats). The value equals tr_D of the word read in the original layout
    whenever the program is a valid sweep of it (see atom_program).
    """
    m = 0
    x = {(): R.one}
    peak = 1
    peak_m = 0
    t0 = time.time()
    for step, item in enumerate(program):
        if item[0] == "open":
            x = {_open(t, m): c for t, c in x.items()}
            m += 1
        elif item[0] in ("close", "lclose"):
            k = m - 1 if item[0] == "close" else 0
            y = {}
            for t, c in x.items():
                u, loop = _close(t, m, k)
                c2 = c if loop else c * R.di
                y[u] = y.get(u, R.zero) + c2
            x = y
            m -= 1
        else:
            kind, i = item
            a = R.coef[kind]
            y = {}
            for t, c in x.items():
                y[t] = y.get(t, R.zero) + a * c
                u, loop = _mul_e(t, m, i)
                c2 = -c * R.d if loop else -c
                y[u] = y.get(u, R.zero) + c2
            x = y
        if len(x) > peak:
            peak, peak_m = len(x), m
        if log and step % every == 0:
            log(f"  step {step}/{len(program)} m={m} terms={len(x)} ({time.time() - t0:.1f}s)")
    tot = R.zero
    for t, c in x.items():
        k = _loops_full(t, m) - m
        f = R.one
        if k > 0:
            for _ in range(k):
                f = f * R.d
        else:
            for _ in range(-k):
                f = f * R.di
        tot = tot + c * f
    return tot, {"peak_terms": peak, "peak_width": peak_m, "final_width": m,
                 "steps": len(program), "seconds": time.time() - t0}


def word_program(n, letters):
    """The plain word on n strands (no early closing): the reference sweep."""
    return [("open",)] * n + list(letters)


# ---- the γγ-bonded nucleus as a sweep -------------------------------------------------------

def _route(bonds):
    """after[J]: bonds placed after block J (J = running max of j along the route), exactly as
    hecke_flint.atom_word does."""
    after, J = {}, 0
    for i, j in bonds:
        J = max(J, j)
        after.setdefault(J, []).append((i, j))
    return after


def atom_program(order, bonds, variant, block_fn=None, fixed_width=False):
    """Sweep program whose trace equals tr_D(hecke_flint.atom_word(order, bonds, variant)).

    Layout. The original word lives on 3A strands a₀ b₀ c₀ a₁ b₁ c₁ …, where c_J (the third
    strand of block J) is the strand later γγ bonds transport. Conjugate by the shuffle braid Π
    that slides every c to the left over (variant "over") or under ("under") the a, b strands,
    keeping the c's and the a, b's in their own order: layout c₀ … c_{A−1} | a₀ b₀ a₁ b₁ …. The
    trace is conjugation invariant, so tr(W) = tr(Π W Π⁻¹), and Π W Π⁻¹ is this program:

      * block J: c_J is routed to the right of b_J, the block acts on (a_J, b_J, c_J), c_J goes
        back to its slot;
      * bond (i, j): c_i is routed to the left of a_j, V³ acts on (c_i, a_j, b_j), c_i goes back.

    A route crosses an a/b strand with c on top iff variant == "over". Between c strands: the
    block route of c_J crosses c_{k>J} with c_J on top iff variant == "under"; the bond route of
    c_i crosses c_k on top iff (k < j) == (variant == "over"). These crossing types are the
    unique solution of the braid identity W = Π·M·Π⁻¹ found by exhaustive search over the 2⁵
    choices and checked in the free group (Artin representation, faithful) for A = 3 and 4,
    every route in this probe family, both variants, random block braids
    (`hecke_tl_check.py::artin_identity`). The blocks enter as black boxes on three adjacent
    strands, so the identity holds for the Hecke blocks by linearity.

    Births and deaths. Every c is opened at the start. a_J, b_J are opened when block J starts
    (untouched before, so x ↦ x ⊗ 1 is exact). After their last bond they are closed with the
    conditional expectation E (Markov property) as soon as they are the most recently opened
    live strands (last in, first out). Closing is exact because after that time a dead a/b
    strand is only ever crossed by c routes, all on the same side (top for "over", bottom for
    "under"), so its remaining arc can be isotoped off to the local closure E draws; nothing
    else touches it. The width is then A + (live a/b strands), not 3A.
    """
    import hecke_flint as F
    A = len(order)
    o = variant == "over"
    after = _route(bonds)
    last = {j: j for j in range(A)}
    for J, bl in after.items():
        for i, j in bl:
            last[j] = max(last[j], J)
    last_c = {i: i for i in range(A)}
    for J, bl in after.items():
        for i, j in bl:
            last_c[i] = max(last_c[i], J)
    blk = {"p": F.proton, "n": F.neutron}
    if block_fn is None:
        def block_fn(J, base):
            return [(k, i + base) for k, i in blk[order[J]](0)]
    lay = [("c", k) for k in range(A)]
    prog = [("open",)] * A
    if fixed_width:  # every strand present from the start, nothing closed (for the identity check)
        lay += [(s, k) for k in range(A) for s in "ab"]
        prog = []

    def mv(lab, tgt, top):
        """Move `lab` to position tgt; top(other) says whether lab crosses on top of other."""
        p = lay.index(lab)
        while p < tgt:
            prog.append(("S" if top(lay[p + 1]) else "I", p))
            lay[p], lay[p + 1] = lay[p + 1], lay[p]
            p += 1
        while p > tgt:
            prog.append(("I" if top(lay[p - 1]) else "S", p - 1))
            lay[p], lay[p - 1] = lay[p - 1], lay[p]
            p -= 1

    for J in range(A):
        if not fixed_width:
            for s in "ab":
                lay.append((s, J))
                prog.append(("open",))
        home = lay.index(("c", J))

        def top_blk(l, J=J):
            return (not o) if l[0] == "c" else o
        mv(("c", J), lay.index(("b", J)), top_blk)
        base = lay.index(("a", J))
        prog.extend(block_fn(J, base))
        mv(("c", J), home, top_blk)
        for i, j in after.get(J, []):
            home = lay.index(("c", i))

            def top_bond(l, j=j):
                return ((l[1] < j) == o) if l[0] == "c" else o
            mv(("c", i), lay.index(("a", j)) - 1, top_bond)
            p = lay.index(("c", i))
            prog.extend(F.V3(p))
            mv(("c", i), home, top_bond)
        if fixed_width:
            continue
        # close finished a/b strands, last in first out
        while lay[-1][0] != "c" and last[lay[-1][1]] <= J:
            lay.pop()
            prog.append(("close",))
        # close finished c strands from the left: c_i with no later bond, all c to its left
        # already closed. Nothing touches it again (later routes start at c_k, k > i, and move
        # right), so the left conditional expectation is exact.
        while lay and lay[0][0] == "c" and last_c[lay[0][1]] <= J:
            lay.pop(0)
            prog.append(("lclose",))
    return prog
