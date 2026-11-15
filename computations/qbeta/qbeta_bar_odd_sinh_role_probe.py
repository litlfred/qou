#!/usr/bin/env python3
"""Is there a STRUCTURAL symmetry that makes the Q_beta element Delta = n - p odd?

Bean `qou-hlx8`. ANALYSIS ONLY: writes NO witness, does not touch the dashboard.

Anti-fit guard (from the bean): a bar-odd projection of the ruled trace may only be
used if it is motivated structurally BEFORE its value is computed. The structural
motivation would be a symmetry S of the algebra with S(n) = p (then S(Delta) = -Delta
and the S-odd part of the trace is canonical). This probe tests every composite of

    bar   : sigma -> sigma^-1 = sigma - h, scalars h -> -h   (KL bar involution)
    rev   : reverse the word (the anti-involution sigma_i -> sigma_i)
    swap  : sigma_0 <-> sigma_1 (the diagram flip)
    chi   : sigma -> -sigma^-1 = h - sigma (eigenline swap at the same q, qou-hlx6)

on the gamma-gamma-selected nucleon words (`nuc11_interleaved`, census letters),
EXACTLY in sympy, at the element level and at the trace level (z_D). It does NOT
compute any Q_beta value or residual: if no symmetry maps n to p, there is nothing
structural to project onto, and computing |odd part| * E_0 would be the selection
the guard forbids.

Also checked (trace level, exact): the measured identity
    tr^{z(q)}(bar x)(q) = tr^{z(1/q)}(x)(1/q)
holds because (i) tr_z(L v) = tr_{z-h, -h}(v) for ANY z (Lean:
`QOU.QBeta.BarMarkov.trM_barNF`), and (ii) z_D(1/q) = z_D(q) - h (`zD_bar_stable`);
convention C is checked NOT to satisfy (ii).
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

_spec = importlib.util.spec_from_file_location(
    "_census", os.path.join(HERE, "qbeta_delta_candidate_census_probe.py"))
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
hm, h = _census.hm, _census.h

q = sp.Symbol("q", positive=True)
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


ONE, ZERO = sp.Integer(1), sp.Integer(0)
U = lambda g: (ONE, ZERO, g)
D = lambda g: (ONE, -h, g)
UD = lambda g: (ONE, -h / 2, g)
CORE = [U(0), D(1)] * 3
GLUON = [U(0), U(0)]
P_TAIL = [U(0), UD(0), UD(1)]
N_TAIL = [UD(0), UD(0), D(1)]
N_WORD = CORE + N_TAIL + GLUON
P_WORD = CORE + P_TAIL + GLUON


def nf(letters):
    v = [ONE] + [ZERO] * 5
    for c, d, g in letters:
        v = hm(v, c, d, g)
    return [sp.expand(x) for x in v]


def tr(v, zz):
    basis = [ONE, zz, zz, zz ** 2, zz ** 2, zz * (h * zz + 1)]
    return sp.expand(sum(c * t for c, t in zip(v, basis)))


def s_bar(ls):
    # bar(c s + d(h)) = c(-h) (s - h) + d(-h); census c are constants
    return [(c, sp.expand(-h * c + sp.sympify(d).subs(h, -h)), g) for c, d, g in ls]


def s_rev(ls):
    return list(reversed(ls))


def s_swap(ls):
    return [(c, d, 1 - g) for c, d, g in ls]


def s_chi(ls):
    # eigenline swap sigma -> -sigma^-1 = h - sigma (automorphism at the SAME q; qou-hlx6)
    return [(-c, sp.expand(h * c + d), g) for c, d, g in ls]


OPS = {"bar": s_bar, "rev": s_rev, "swap": s_swap, "chi": s_chi}


def apply(names, ls):
    for nm in names:
        ls = OPS[nm](ls)
    return ls


def is_zero(vec):
    return all(sp.simplify(x) == 0 for x in vec)


def main() -> int:
    nfp, nfn = nf(P_WORD), nf(N_WORD)
    zD = q ** 3 / (q ** 2 + 1)
    zDh = lambda e: sp.simplify(sp.sympify(e).subs(h, q - 1 / q))
    print("ELEMENT LEVEL: does any composite S of {bar, rev, swap} send n to +/-p?")
    any_hit = False
    odd_hits = []
    for r in range(0, 5):
        for names in itertools.permutations(OPS, r):
            sn = nf(apply(names, N_WORD))
            hit_p = is_zero([a - b for a, b in zip(sn, nfp)])
            hit_mp = is_zero([a + b for a, b in zip(sn, nfp)])
            sd = [a - b for a, b in zip(sn, nf(apply(names, P_WORD)))]
            dd = [a - b for a, b in zip(nfn, nfp)]
            odd = is_zero([a + b for a, b in zip(sd, dd)])
            even = is_zero([a - b for a, b in zip(sd, dd)])
            self_n = is_zero([a + b for a, b in zip(sn, nfn)])
            lab = "+".join(names) or "id"
            print(f"    S={lab:16s} S(n)=p:{hit_p!s:5} S(n)=-p:{hit_mp!s:5} "
                  f"S(D)=-D:{odd!s:5} S(D)=D:{even!s:5} S(n)=-n:{self_n!s:5}")
            if names and (hit_p or hit_mp):
                any_hit = True
            if names and odd:
                odd_hits.append((lab, self_n))
    check("no_composite_symmetry_maps_n_to_p", not any_hit)
    check("every_Delta_odd_symmetry_is_the_length_parity",
          bool(odd_hits) and all(sn_ for _, sn_ in odd_hits),
          f"Delta-odd symmetries {[l for l, _ in odd_hits]} all send n -> -n (and p -> -p): "
          "they are sigma -> -sigma, h -> -h, i.e. q -> -q, under which every census "
          "letter is odd, so every 11-letter word is odd. Not an n <-> p map.")
    fq = zDh(tr([a - b for a, b in zip(nfn, nfp)], zD))
    check("trace_of_Delta_is_odd_under_q_to_minus_q",
          sp.simplify(fq.subs(q, -q) + fq) == 0)

    print("\nTRACE LEVEL at z_D (rev and swap preserve the Markov trace, so only")
    print("bar can change the value; test tr^{z_D}(S n) vs tr^{z_D}(p)):")
    trp = zDh(tr(nfp, zD.subs(q, q)).subs(h, q - 1 / q))
    trace_hit = False
    for r in range(0, 5):
        for names in itertools.permutations(OPS, r):
            tsn = zDh(tr(nf(apply(names, N_WORD)), zD))
            eq = sp.simplify(tsn - trp) == 0
            eqm = sp.simplify(tsn + trp) == 0
            if names and (eq or eqm):
                trace_hit = True
            print(f"    S={'+'.join(names) or 'id':16s} tr(Sn)=tr(p):{eq!s:5} tr(Sn)=-tr(p):{eqm!s:5}")
    check("no_symmetry_matches_traces_either", not trace_hit)

    print("\nLETTER-LEVEL bar images (what bar does to the quark letters)")
    for lab, L in (("u=s", U(0)), ("d=s^-1", D(0)), ("ud=s-h/2", UD(0))):
        b = s_bar([L])[0]
        print(f"    bar({lab}) = s + ({b[1]})")
    check("bar_swaps_u_d_fixes_ud",
          s_bar([U(0)])[0][1] == -h and s_bar([D(0)])[0][1] == 0
          and sp.expand(s_bar([UD(0)])[0][1] + h / 2) == 0)
    print("    p tail (u, ud, ud) -> bar -> (d, ud, ud); n tail is (ud, ud, d):")
    print("    same letter MULTISET, different ORDER/GENERATOR placement, and the core")
    print("    (s0 s1^-1)^3 and gluon s0 s0 are NOT bar-invariant (bar(core) = (s0^-1 s1)^3).")

    print("\nMARKOV PARAMETER bar-stability:  z(1/q) == z(q) - h ?")
    zC = sp.sqrt(q) / (q + 1)
    for lab, zz in (("z_D = q^3/(q^2+1)", zD), ("z_C = sqrt q/(q+1)", zC)):
        ok = sp.simplify(zz.subs(q, 1 / q) - (zz - (q - 1 / q))) == 0
        print(f"    {lab:22s}: {ok}")
    check("zD_is_bar_stable", sp.simplify(zD.subs(q, 1 / q) - zD + (q - 1 / q)) == 0)
    check("zC_is_not_bar_stable", sp.simplify(zC.subs(q, 1 / q) - zC + (q - 1 / q)) != 0)

    print("\nE_0 under q -> 1/q (order zero, m_e = 1):")
    E0 = 1 / (q * (q - 1))
    print(f"    E0(1/q) / E0(q) = {sp.factor(sp.simplify(E0.subs(q, 1 / q) / E0))}")
    check("E0_order_zero_is_minus_q3_covariant",
          sp.simplify(E0.subs(q, 1 / q) + q ** 3 * E0) == 0,
          "E0 = q^{-3/2} / (2 sinh(lambda/2)), lambda = ln q")

    ok = all(r[1] for r in RESULTS)
    print(f"\n{sum(r[1] for r in RESULTS)}/{len(RESULTS)} checks pass")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
