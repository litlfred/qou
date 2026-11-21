#!/usr/bin/env python3
"""Isospin as a MODULE map (Furey-style) on the chirality ideal H_3 . P_+ (D-I1 = A).

Owner decision D-I1 = (A), 2026-11-15: test isospin as left multiplication by a
derived element on the left ideal cut out by the chirality idempotent P_+ of
`OneSidedWeakVertex.lean` (#7844; eigenvalue q of sigma_g, J = P_+ - P_-,
W_L = q^-1 J, W_R = q J). Plan fixed in advance in
docs/audits/2026-11-15-word-dependent-isospin-maps.md section 10. Bean qou-z08b.

ANALYSIS ONLY: writes NO witness, computes NO Q_beta value, touches no
dashboard. Exact arithmetic in Q(q) throughout (sympy DomainMatrix over
QQ(q)); no float anywhere. All multiplication goes through the corpus NF
right-multiplication table `hecke_core_symbolic.hm_sym` (basis
[], [0], [1], [0,1], [1,0], [0,1,0]); nothing is hand-coded per block.

Order (binding, no fitting):
 1. STATE RULE FIRST. Every state pair on record is tested; none is chosen:
      D2 `nucleonState` (PhotonPairNormalForm.lean): core . l0(c1) l0(c2) l1(c3),
         c = flavourShift: u -> 0, d -> -1. Slot order is not fixed by any
         rule, so p in perms(0,0,-1), n in perms(0,-1,-1): 3 x 3 = 9 pairs.
      AVG census rule (`nuc11_interleaved`): p = (0,-1/2,-1/2),
         n = (-1/2,-1/2,-1), as in the census word.
    each with and without the census gluon sigma_0^2 appended: 20 pairs.
    Letter l_g(c) = sigma_g + c h (h = q - 1/q), core = (sigma_0 sigma_1^-1)^3.
    State psi = N . P_+(sigma_g), g in {0,1}: 40 settings.
 2. CANDIDATES, fixed before any value is computed, from existing structure only:
      sigma_g, sigma_g^-1, P_+g, P_-g, J_g, W_L = q^-1 J_g, W_R = q J_g, g in {0,1}
    (W_L, W_R are scalar multiples of J; listed because #7844 names them.)
    Plus the CENTRALISER of {core, gluon} in H_3: solve for every x in it with
    x psi_p = psi_n; a unique solution would be a forced result, a family is not.
 3. TESTS per (pair, g, candidate): X psi_p = psi_n exactly; up to a scalar;
    X^2 = 1 or scalar; [X, core] = 0; [X, gluon] = 0.
 0. STRUCTURE FIRST: dim and commutativity of the corner P_+ H_3 P_+, dim of
    the left ideal H_3 P_+, dim of the centre, dim of the centraliser.

Not tested here, with reason: the flavour flip sigma -> sigma^-1 is not an
algebra map of H_3 over Q(q) (sigma^-1 satisfies (x - q^-1)(x + q) = 0, not
(x - q)(x + q^-1) = 0), so it does not restrict to a module map; it was
covered as a word map by qbeta_word_dependent_isospin_maps_probe.py.
"""
from __future__ import annotations

import itertools
import os
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "computations", "substrate"))
import hecke_core_symbolic as hcs  # noqa: E402

q, h = hcs.q, hcs.h
K = sp.QQ.frac_field(q)
R = sp.Rational
DIM = 6
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def cz(e):
    return sp.cancel(sp.together(e))


# ---- algebra: elements are NF vectors over Q(q) ---------------------------------
E = [[sp.Integer(1 if i == j else 0) for i in range(DIM)] for j in range(DIM)]
# Basis as the hm_sym TABLE indexes it: from 1, gen0 -> 1, gen1 -> 2, then
# index 2 . sigma_0 -> 3, index 1 . sigma_1 -> 4, index 4 . sigma_0 -> 5.
# So index 3 = sigma_1 sigma_0 and index 4 = sigma_0 sigma_1 (hcs.NF_BASIS
# lists them in the other order; the table is what multiplies, so it governs).
BASIS_WORDS = [[], [0], [1], [1, 0], [0, 1], [0, 1, 0]]


def rmul_letter(v, c, d, g):
    return [cz(x) for x in hcs.hm_sym(v, c, d, g)]


def rmul_word(v, word):
    for g in word:
        v = rmul_letter(v, 1, 0, g)
    return v


def mul(x, y):
    """x . y = sum_j y_j (x . w_j)."""
    out = [sp.Integer(0)] * DIM
    for j, yj in enumerate(y):
        if yj == 0:
            continue
        xw = rmul_word(x, BASIS_WORDS[j])
        out = [o + yj * a for o, a in zip(out, xw)]
    return [cz(o) for o in out]


def add(*vs, coeffs=None):
    coeffs = coeffs or [1] * len(vs)
    return [cz(sum(c * v[i] for c, v in zip(coeffs, vs))) for i in range(DIM)]


def scal(a, v):
    return [cz(a * x) for x in v]


def iszero(v):
    return all(cz(x) == 0 for x in v)


ONE = E[0]
SIG = {g: rmul_letter(ONE, 1, 0, g) for g in (0, 1)}
SIGINV = {g: rmul_letter(ONE, 1, -h, g) for g in (0, 1)}


def letter(g, c):
    return rmul_letter(ONE, 1, c * h, g)


def prod(elts):
    v = ONE
    for x in elts:
        v = mul(v, x)
    return v


def dm(cols):
    """DomainMatrix whose columns are the given vectors."""
    rows = [[K.from_sympy(cols[j][i]) for j in range(len(cols))] for i in range(DIM)]
    return DomainMatrix(rows, (DIM, len(cols)), K)


def rank(vs):
    return dm(vs).rank() if vs else 0


def parallel(a, b):
    """a = lam b for some nonzero lam (both nonzero)."""
    return (not iszero(a)) and (not iszero(b)) and rank([a, b]) == 1


# ---- chirality idempotents (OneSidedWeakVertex) ---------------------------------
QI = q + 1 / q
P = {}
for g in (0, 1):
    Pp = scal(1 / QI, add(SIG[g], scal(1 / q, ONE)))     # eigenvalue q
    Pm = add(ONE, Pp, coeffs=[1, -1])                    # eigenvalue -1/q
    P[(g, "+")], P[(g, "-")] = Pp, Pm


def structure():
    print("== 0. structure ==")
    check("basis words reduce to unit NF vectors",
          all(iszero(add(rmul_word(ONE, w), E[j], coeffs=[1, -1])) for j, w in enumerate(BASIS_WORDS)))
    for g in (0, 1):
        Pp, Pm = P[(g, "+")], P[(g, "-")]
        check(f"P+({g}) idempotent, P+P- = 0, sigma P+ = q P+",
              iszero(add(mul(Pp, Pp), Pp, coeffs=[1, -1])) and iszero(mul(Pp, Pm))
              and iszero(add(mul(SIG[g], Pp), Pp, coeffs=[1, -q])))
        corner = [mul(mul(Pp, e), Pp) for e in E]
        cdim = rank(corner)
        comm = all(iszero(add(mul(a, b), mul(b, a), coeffs=[1, -1]))
                   for a, b in itertools.combinations(corner, 2))
        check(f"corner P+({g}) H3 P+({g}) is 2-dim and commutative",
              cdim == 2 and comm, f"dim {cdim}, commutative {comm}")
        ldim = rank([mul(e, Pp) for e in E])
        check(f"left ideal H3 P+({g}) is 3-dim", ldim == 3, f"dim {ldim}")
    # centre
    cent = centraliser([SIG[0], SIG[1]])
    check("centre of H3 is 3-dim", len(cent) == 3, f"dim {len(cent)}")
    return cent


def centraliser(elts):
    """Basis of {x : x a = a x for a in elts}, via nullspace over Q(q)."""
    blocks = []
    for a in elts:
        cols = [add(mul(e, a), mul(a, e), coeffs=[1, -1]) for e in E]
        blocks.append(dm(cols))
    M = blocks[0]
    for B in blocks[1:]:
        M = M.vstack(B)
    ns = M.nullspace().to_Matrix()
    return [[cz(ns[r, i]) for i in range(DIM)] for r in range(ns.rows)]


# ---- step 1: state family (enumerated before any test) --------------------------
CORE_L = [(0, 0), (1, -1)] * 3
GLUON_L = [(0, 0), (0, 0)]
TAIL_G = (0, 0, 1)


def word_elt(letters):
    return prod([letter(g, c) for g, c in letters])


def state_pairs():
    pairs = []
    pp = sorted(set(itertools.permutations((0, 0, -1))))
    nn = sorted(set(itertools.permutations((0, -1, -1))))
    for cp in pp:
        for cn in nn:
            pairs.append((f"D2 p{cp} n{cn}", cp, cn))
    pairs.append(("AVG", (0, R(-1, 2), R(-1, 2)), (R(-1, 2), R(-1, 2), -1)))
    out = []
    for name, cp, cn in pairs:
        for glu in (False, True):
            def W(cs):
                return CORE_L + list(zip(TAIL_G, cs)) + (GLUON_L if glu else [])
            out.append((name + (" +gluon" if glu else ""), W(cp), W(cn)))
    return out


def candidates():
    cands = []
    for g in (0, 1):
        J = add(P[(g, "+")], P[(g, "-")], coeffs=[1, -1])
        cands += [(f"sigma{g}", SIG[g]), (f"sigma{g}^-1", SIGINV[g]),
                  (f"P+{g}", P[(g, "+")]), (f"P-{g}", P[(g, "-")]),
                  (f"J{g}", J), (f"W_L{g}", scal(1 / q, J)), (f"W_R{g}", scal(q, J))]
    return cands


def comm0(a, b):
    return iszero(add(mul(a, b), mul(b, a), coeffs=[1, -1]))


def main():
    cent = structure()
    core, gluon = word_elt(CORE_L), word_elt(GLUON_L)
    C = centraliser([core, gluon])
    zdim = len(cent)
    same = rank(C + cent) == len(C) == zdim
    check("centraliser of {core, gluon} equals the centre", same,
          f"dim C = {len(C)}, dim Z = {zdim}")
    C_core = centraliser([core])
    print(f"  (info) dim centraliser(core) = {len(C_core)}, "
          f"dim centraliser(gluon) = {len(centraliser([gluon]))}")

    pairs = state_pairs()
    cands = candidates()
    print(f"== 1-3. {len(pairs)} state pairs x 2 idempotents x {len(cands)} candidates ==")
    # candidate-only properties (independent of state)
    cprops = {}
    for nm, X in cands:
        X2 = mul(X, X)
        cprops[nm] = dict(invol_scalar=rank([X2, ONE]) == 1,
                          c_core=comm0(X, core), c_gluon=comm0(X, gluon))
    for nm, pr in cprops.items():
        print(f"  {nm:12s} X^2 scalar {pr['invol_scalar']!s:5s} "
              f"[X,core]=0 {pr['c_core']!s:5s} [X,gluon]=0 {pr['c_gluon']!s:5s}")

    n_exact = n_scalar = n_full = 0
    cent_unique = cent_family = cent_none = 0
    any_unique = 0
    rows = []
    degenerate = []
    for name, wp, wn in pairs:
        Np, Nn = word_elt(wp), word_elt(wn)
        for g in (0, 1):
            psp, psn = mul(Np, P[(g, "+")]), mul(Nn, P[(g, "+")])
            for nm, X in cands:
                img = mul(X, psp)
                ex = img == psn or iszero(add(img, psn, coeffs=[1, -1]))
                sc = parallel(img, psn)
                n_exact += ex
                n_scalar += sc
                if ex or sc:
                    pr = cprops[nm]
                    full = pr["invol_scalar"] and pr["c_core"] and pr["c_gluon"]
                    n_full += full
                    rows.append((name, g, nm, ex, sc, full))
            # centraliser solve: x = sum a_i C_i with x psp = psn
            cols = [mul(c, psp) for c in C]
            A = dm(cols)
            b = dm([psn])
            aug = A.hstack(b)
            rA, rAb = A.rank(), aug.rank()
            if rA != rAb:
                cent_none += 1
                verdict = "none"
            elif rA == len(C):
                cent_unique += 1
                verdict = "unique"
            else:
                cent_family += 1
                verdict = f"family dim {len(C) - rA}"
                # Classify: is psi_n already a SCALAR multiple of psi_p? Then the
                # "map" is multiplication by a number, not an isospin rotation.
                ratios = {cz(y / x) for x, y in zip(psp, psn) if cz(x) != 0}
                if parallel(psp, psn) and len(ratios) == 1:
                    lam = ratios.pop()
                    verdict += f" [psi_n = ({lam}) psi_p]"
                    degenerate.append((name, g, lam))
            # general existence in H3 (context)
            colsH = [mul(e, psp) for e in E]
            rH, rHb = rank(colsH), rank(colsH + [psn])
            gen = "exists" if rH == rHb else "none"
            any_unique += (gen == "exists" and rH == DIM)
            print(f"  {name:32s} g={g}: centraliser solve: {verdict:14s} "
                  f"| some x in H3: {gen} (affine dim {DIM - rH if gen == 'exists' else '-'})")
    print("== hits on the fixed candidate list (exact or up to scalar) ==")
    for r in rows:
        print("  ", r)
    total = len(pairs) * 2 * len(cands)
    check("fixed candidates: no exact p->n hit", n_exact == 0, f"{n_exact} of {total}")
    print(f"  (info) up-to-scalar hits: {n_scalar} of {total}; "
          f"of those also involutive/scalar-square and commuting with core+gluon: {n_full}")
    print(f"  (info) centraliser solve over {len(pairs) * 2} settings: "
          f"unique {cent_unique}, family {cent_family}, none {cent_none}")
    check("every centraliser hit is degenerate (psi_n a scalar multiple of psi_p)",
          len(degenerate) == cent_family + cent_unique,
          f"{len(degenerate)} of {cent_family + cent_unique}: "
          + ", ".join(sorted({str(d[2]) for d in degenerate})))
    print(f"  (info) settings where a unique x in all of H3 maps psi_p to psi_n: {any_unique}")
    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"\n{len(RESULTS) - nfail}/{len(RESULTS)} checks PASS")
    return nfail


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
