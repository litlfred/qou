#!/usr/bin/env python3
"""Does every central primitive idempotent of `H_n(q)` touch `T_e`?

Bean `qou-09e0` (front 5 of epic `qou-v2om`), continuing `qou-wjbd` / `wpdb`.

## Why this one fact decides the front

The corpus reads, at six sites,

    Z^(k)(A) = span{ e_lambda : gbDepth(lambda) = k },

equivalently `Z cap F_k = V_{k+c}`, where `V_j := span{e_lambda : gbDepth <= j}`
and `c` is a shift.  `docs/audits/2026-08-26-no-shift-rescues-the-word-partition-
bridge.md` excluded all three corpus readings of `J^bullet` and every shift of the
surviving one, and left the front at:

    a candidate filtration must put a SECOND central element in F_1.

The accompanying audit answers that in the negative for a precisely delimited
class of filtrations, and the argument needs exactly one algebra fact:

    tau(e_lambda) != 0   for every lambda |- n,

where `tau(sum_w a_w T_w) := a_e` is the canonical symmetrizing trace of
`H_n(q)`: in the AGENTS.md section 7a convention `sigma^2 = (q - q^-1) sigma + 1`
one has `tau(T_u T_v) = delta_{u, v^-1}`, so `{T_{w^-1}}` is the dual basis of
`{T_w}` and `tau` is symmetrizing.  Equivalently: `T_e` lies in the support of
EVERY central primitive idempotent.

This is standard (`tau(e_lambda) = d_lambda / c_lambda`, `c_lambda` the Schur
element, nonzero at generic `q`), but it is the load-bearing hypothesis of a
scope-(b) exclusion, so it is measured rather than cited.

## The measurement, and why it needs no idempotents

Splitting `Z` into its primitive idempotents needs eigenvalues, hence factoring.
That is avoidable.  In the idempotent basis the bilinear form

    B(x, y) := tau(x y)     restricted to Z

has matrix `diag(tau(e_lambda))`, because `e_lambda e_mu = delta e_lambda`.  So

    B non-degenerate on Z   <==>   tau(e_lambda) != 0 for every lambda,

and the whole question is a single exact rank computation on the `p(n) x p(n)`
Gram matrix of `B` against any basis of `Z`.  No labelling, no factoring, no
choice of idempotent basis.

## Arithmetic

Exact throughout; there is no floating point anywhere in this file, per
AGENTS.md section "PROBES ARE NOT EXEMPT".  Two independent exact backends:
`Fraction` over QQ and the prime field F_p with p = 2^61 - 1, each at several
specialisations of `q`.

## Why specialising `q` is legitimate here (the bound goes the right way)

Every entry of the Gram matrix is a Laurent polynomial in `q`, so for any
specialisation `q0`,

    rank B(q0) <= rank B(q)   over QQ(q).

This script reports FULL rank at specialisations, and full rank at a
specialisation therefore forces full rank generically.  That is the direction
the exclusion needs, so no genericity has to be assumed anywhere.  (`dim Z =
p(n)`, also reported, is pinned exactly by the same inequality against the
classical lower bound.)

Usage:
  python3 -u docs/audits/scripts/central_idempotent_unit_coefficient.py
"""
from __future__ import annotations

import itertools
import json
import os
import sys
from fractions import Fraction

# ---------------------------------------------------------------- symmetric group

def perms(n):
    return list(itertools.permutations(range(1, n + 1)))


def length(w):
    n = len(w)
    return sum(1 for a in range(n) for b in range(a + 1, n) if w[a] > w[b])


def right_mul_s(w, i):
    """w * s_i : swap POSITIONS i, i+1 (0-indexed i)."""
    v = list(w)
    v[i], v[i + 1] = v[i + 1], v[i]
    return tuple(v)


def left_mul_s(w, i):
    """s_i * w : swap VALUES i+1, i+2 (0-indexed i)."""
    a, b = i + 1, i + 2
    return tuple(b if x == a else a if x == b else x for x in w)


def reduced_word(w):
    """A reduced word for `w`: bubble down to the identity by length-decreasing
    right multiplications, then reverse."""
    v = list(w)
    out = []
    changed = True
    while changed:
        changed = False
        for i in range(len(v) - 1):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                out.append(i)
                changed = True
                break
    out.reverse()
    return out


def partitions(n):
    def go(m, cap):
        if m == 0:
            yield ()
            return
        for k in range(min(m, cap), 0, -1):
            for rest in go(m - k, k):
                yield (k,) + rest
    return list(go(n, n))


# --------------------------------------------------------------- exact backends

class QQ:
    name = "QQ (Fraction)"
    P = None
    zero = Fraction(0)
    one = Fraction(1)

    @staticmethod
    def coerce(x):
        return Fraction(x)

    @staticmethod
    def inv(x):
        return Fraction(1, 1) / x


class Fp:
    P = (1 << 61) - 1
    name = "F_p (p = 2^61 - 1)"
    zero = 0
    one = 1

    @classmethod
    def coerce(cls, x):
        f = Fraction(x)
        return (f.numerator % cls.P) * pow(f.denominator % cls.P, cls.P - 2, cls.P) % cls.P

    @classmethod
    def inv(cls, x):
        return pow(x, cls.P - 2, cls.P)


# -------------------------------------------------------------- the algebra H_n(q)

class Hecke:
    """`H_n(q)` in the Groebner-Shirshov normal-form basis `{T_w}`.

    AGENTS.md section 7a: `sigma_i^2 = (q - q^-1) sigma_i + 1`, hence

        T_w T_s = T_ws                      if l(ws) > l(w)
        T_w T_s = (q - q^-1) T_w + T_ws     if l(ws) < l(w)
    """

    def __init__(self, n, qval, F):
        self.n, self.F = n, F
        self.q = F.coerce(qval)
        self.delta = self.q - F.inv(self.q)
        self.W = sorted(perms(n), key=lambda w: (length(w), w))
        self.idx = {w: i for i, w in enumerate(self.W)}
        self.e = tuple(range(1, n + 1))
        self.rw = {w: reduced_word(w) for w in self.W}

    def _norm(self, d):
        P = self.F.P
        if P is None:
            return {k: v for k, v in d.items() if v != 0}
        return {k: v % P for k, v in d.items() if v % P != 0}

    def rmul_s(self, x, i):
        out = {}
        for w, c in x.items():
            ws = right_mul_s(w, i)
            if length(ws) > length(w):
                out[ws] = out.get(ws, self.F.zero) + c
            else:
                out[w] = out.get(w, self.F.zero) + self.delta * c
                out[ws] = out.get(ws, self.F.zero) + c
        return self._norm(out)

    def lmul_s(self, x, i):
        out = {}
        for w, c in x.items():
            sw = left_mul_s(w, i)
            if length(sw) > length(w):
                out[sw] = out.get(sw, self.F.zero) + c
            else:
                out[w] = out.get(w, self.F.zero) + self.delta * c
                out[sw] = out.get(sw, self.F.zero) + c
        return self._norm(out)

    def mul(self, x, y):
        """x * y, by expanding y over the basis and right-multiplying."""
        out = {}
        for v, cy in y.items():
            piece = dict(x)
            for i in self.rw[v]:
                piece = self.rmul_s(piece, i)
            for w, c in piece.items():
                out[w] = out.get(w, self.F.zero) + c * cy
        return self._norm(out)

    def tau(self, x):
        """The canonical symmetrizing trace: the coefficient of `T_e`."""
        return x.get(self.e, self.F.zero)

    def vec(self, x):
        v = [self.F.zero] * len(self.W)
        for w, c in x.items():
            v[self.idx[w]] = c
        return v

    def elt(self, v):
        return self._norm({self.W[i]: v[i] for i in range(len(v)) if v[i] != 0})


# ------------------------------------------------------------------ linear algebra

def rref(rows, ncols, F):
    P = F.P
    mat = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        sel = next((rr for rr in range(r, len(mat)) if mat[rr][c] != 0), None)
        if sel is None:
            continue
        mat[r], mat[sel] = mat[sel], mat[r]
        inv = F.inv(mat[r][c])
        mat[r] = ([x * inv for x in mat[r]] if P is None
                  else [(x * inv) % P for x in mat[r]])
        for rr in range(len(mat)):
            if rr != r and mat[rr][c] != 0:
                f = mat[rr][c]
                mat[rr] = ([a - f * b for a, b in zip(mat[rr], mat[r])] if P is None
                           else [(a - f * b) % P for a, b in zip(mat[rr], mat[r])])
        piv.append(c)
        r += 1
        if r == len(mat):
            break
    return piv, mat[:r]


def rank(rows, ncols, F):
    return len(rref(rows, ncols, F)[0])


def nullspace(rows, ncols, F):
    piv, red = rref(rows, ncols, F)
    pivset = set(piv)
    basis = []
    for fc in (c for c in range(ncols) if c not in pivset):
        v = [F.zero] * ncols
        v[fc] = F.one
        for i, pc in enumerate(piv):
            x = red[i][fc]
            if x != 0:
                v[pc] = (-x) % F.P if F.P is not None else -x
        basis.append(v)
    return basis


# ---------------------------------------------------------------------- the centre

def centre_basis(H):
    """Basis of `Z(H_n(q))` in the `T_w` basis: the nullspace of
    `x |-> T_si x - x T_si` for every `i`."""
    F, N = H.F, len(H.W)
    rows = []
    for i in range(H.n - 1):
        M = [[F.zero] * N for _ in range(N)]
        for j, w in enumerate(H.W):
            col = {}
            for ww, c in H.lmul_s({w: F.one}, i).items():
                col[ww] = col.get(ww, F.zero) + c
            for ww, c in H.rmul_s({w: F.one}, i).items():
                col[ww] = col.get(ww, F.zero) - c
            for ww, c in col.items():
                M[H.idx[ww]][j] = (c % F.P) if F.P is not None else c
        rows.extend(M)
    return nullspace(rows, N, F)


def dual_basis_check(H):
    """Sanity check on the convention: `tau(T_u T_v) = delta_{u, v^-1}`."""
    bad = []
    for u in H.W:
        uinv = tuple(sorted(range(1, H.n + 1), key=lambda k: u[k - 1]))
        for v in H.W:
            t = H.tau(H.mul({u: H.F.one}, {v: H.F.one}))
            want = H.F.one if v == uinv else H.F.zero
            if t != want:
                bad.append((u, v, t))
    return bad


def run(n, qval, F):
    H = Hecke(n, qval, F)
    zb = centre_basis(H)
    p = len(partitions(n))
    # Gram matrix of B(x, y) = tau(x y) restricted to Z
    zel = [H.elt(b) for b in zb]
    G = [[H.tau(H.mul(a, b)) for b in zel] for a in zel]
    r = rank(G, len(zel), F)
    return {
        "n": n,
        "q": str(qval),
        "field": F.name,
        "dim_Z": len(zb),
        "p_n": p,
        "dim_Z_eq_p_n": len(zb) == p,
        "rank_trace_form_on_Z": r,
        "trace_form_nondegenerate_on_Z": r == len(zb),
        "all_idempotents_touch_T_e": r == len(zb),
    }


def main():
    out = {
        "probe": "central_idempotent_unit_coefficient",
        "bean": "qou-09e0",
        "question": ("is tau(e_lambda) != 0 for every central primitive idempotent "
                     "of H_n(q)? equivalently: is the symmetrizing trace form "
                     "non-degenerate on Z(H_n(q))?"),
        "convention": "AGENTS.md 7a, sigma^2 = (q - q^-1) sigma + 1; tau = coefficient of T_e",
        "arithmetic": "exact only (Fraction over QQ, and F_p with p = 2^61-1); no float64 anywhere",
        "specialisation_direction": (
            "rank B(q0) <= rank B(q) generically, so FULL rank at a specialisation "
            "forces full rank generically -- the direction this exclusion needs"),
        "runs": [],
    }
    # convention self-check at n = 3
    Hc = Hecke(3, Fraction(7, 3), QQ)
    bad = dual_basis_check(Hc)
    out["dual_basis_selfcheck_n3"] = {
        "claim": "tau(T_u T_v) = delta_{u, v^{-1}}",
        "violations": len(bad),
        "ok": len(bad) == 0,
    }
    print(f"[selfcheck] tau(T_u T_v) = delta_(u,v^-1) at n=3: "
          f"{'OK' if not bad else str(len(bad)) + ' VIOLATIONS'}")

    for n in (2, 3, 4, 5):
        for F, qs in ((QQ, [Fraction(7, 3), Fraction(2), Fraction(11, 5)]),
                      (Fp, [Fraction(7, 3), Fraction(5)])):
            for qv in qs:
                r = run(n, qv, F)
                out["runs"].append(r)
                print(f"n={n:<2} q={str(qv):<6} {F.name:<22} "
                      f"dim Z={r['dim_Z']:<3}(p(n)={r['p_n']:<3}) "
                      f"rank(trace form|Z)={r['rank_trace_form_on_Z']:<3} "
                      f"=> every e_lambda touches T_e: {r['all_idempotents_touch_T_e']}")
                sys.stdout.flush()

    ok = (all(r["dim_Z_eq_p_n"] for r in out["runs"])
          and all(r["all_idempotents_touch_T_e"] for r in out["runs"])
          and out["dual_basis_selfcheck_n3"]["ok"])
    out["verdict"] = (
        "CONFIRMED: at every n and every specialisation tested, the symmetrizing "
        "trace form is non-degenerate on Z(H_n(q)); equivalently tau(e_lambda) != 0 "
        "for every lambda |- n, i.e. T_e is in the support of every central "
        "primitive idempotent." if ok else "FAILED -- see runs")
    print("\n" + out["verdict"])

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "central-idempotent-unit-coefficient.witness.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)
        fh.write("\n")
    print(f"wrote {path}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
