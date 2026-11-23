#!/usr/bin/env python3
"""Chirality and CPT through B3 -> PSL(2,Z), Chester-Arsiwalla-Kauffman 2025.

Pre-registration: PREREG.md (same directory). Exact arithmetic only:
integer matrices, sympy Rationals, sympy rational functions. No floats.

Index convention: their sigma_1, sigma_2 = our sigma_0, sigma_1.
A word is a tuple of (i, e) with i in {1, 2} and e = +1 or -1.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
import random
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- words ---
def inv(w):
    return tuple((i, -e) for (i, e) in reversed(w))

def C(w):          # mirror: switch every crossing, order kept (Eq. 8)
    return tuple((i, -e) for (i, e) in w)

def P(w):          # vertical-axis reflection (Eq. 9 + the sigma1 sigma2 example)
    return tuple((3 - i, -e) for (i, e) in w)

def T(w):          # horizontal-axis reflection = group inverse (Eq. 10)
    return inv(w)

def CPT(w):
    return T(P(C(w)))

def reduce_free(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def show(w, ours=False):
    if not w:
        return "1"
    off = 1 if ours else 0
    return "".join(f"s{i - off}" + ("" if e == 1 else "^-1") for i, e in w)

# --------------------------------------------------- PSL(2,Z) map (theirs) ---
t_ = sp.Matrix([[1, 1], [0, 1]])
r_ = sp.Matrix([[0, -1], [1, 0]])
GEN_THEIRS = {1: t_, 2: r_ * t_ * r_}              # sigma2 -> r t r = -[[1,0],[-1,1]]
GEN_STD = {1: t_, 2: sp.Matrix([[1, 0], [-1, 1]])}  # standard SL(2,Z) lift
I2 = sp.eye(2)
J = sp.Matrix([[1, 0], [0, -1]])

def img(w, gens):
    M = sp.eye(2)
    for i, e in w:
        M = M * (gens[i] if e == 1 else gens[i].inv())
    return M

def psl_norm(M):
    a, b, c, d = M
    if c < 0 or (c == 0 and d < 0):
        M = -M
    return M

def psl_eq(A, B):
    return A == B or A == -B

def psl_type(M):
    tr = abs(M.trace())
    if psl_eq(M, I2):
        return "identity"
    return "elliptic" if tr < 2 else ("parabolic" if tr == 2 else "hyperbolic")

# ------------------------------------------------- Rademacher function Psi ---
def dedekind(h, k):
    def saw(x):
        if x.denominator == 1:
            return Fraction(0)
        return x - (x.numerator // x.denominator) - Fraction(1, 2)
    return sum((saw(Fraction(r, k)) * saw(Fraction(h * r, k)) for r in range(1, k)),
               Fraction(0))

def sgn(x):
    return (x > 0) - (x < 0)

def psi(M):
    a, b, c, d = (int(x) for x in M)
    if c == 0:
        phi = Fraction(b, d)
    else:
        phi = Fraction(a + d, c) - 12 * sgn(c) * dedekind(a, abs(c))
    return phi - 3 * sgn(c * (a + d))

def random_sl2(rng, n=6):
    M = sp.eye(2)
    for _ in range(n):
        g = rng.choice([t_, t_.inv(), GEN_STD[2], GEN_STD[2].inv(), r_])
        M = M * g
    return M

def selftest_psi():
    rng = random.Random(20261122)   # fixed seed: reproducible, not a parameter
    tests = 0
    for _ in range(300):
        A = random_sl2(rng, 5)
        X = random_sl2(rng, 5)
        B = X * A * X.inv()
        assert psi(A) == psi(B), ("Psi not class-invariant", A, X)
        assert psi(A) == psi(-A), ("Psi not even under -1", A)
        tests += 1
    assert psi(t_) == 1 and psi(t_.inv()) == -1
    return tests

def conj_search(A, B, bound=6):
    """Explicit X in SL(2,Z), entries in [-bound,bound], with X A X^-1 = +-B."""
    rng = range(-bound, bound + 1)
    for a, b, c in itertools.product(rng, rng, rng):
        for d in rng:
            if a * d - b * c != 1:
                continue
            X = sp.Matrix([[a, b], [c, d]])
            if psl_eq(X * A * X.inv(), B):
                return X
    return None

def chirality(M):
    Mm = J * M * J                     # image of the mirror word C(w)
    p, pm = psi(M), psi(Mm)
    if p != pm:
        return "chiral", f"Psi={p} vs mirror Psi={pm}", None
    if psl_eq(M, Mm):
        return "achiral", "image equals its mirror image", None
    X = conj_search(M, Mm)
    if X is not None:
        return "achiral", "explicit conjugator found", [int(x) for x in X]
    return "undetermined", f"Psi equal ({p}), no conjugator with entries <= 6", None

# ------------------------------------------- faithful reduced Burau of B3 ---
tb = sp.symbols("t")
BUR = {1: sp.Matrix([[-tb, 1], [0, 1]]), 2: sp.Matrix([[1, 0], [tb, -tb]])}

def burau(w):
    M = sp.eye(2)
    for i, e in w:
        M = M * (BUR[i] if e == 1 else BUR[i].inv())
    return M.applyfunc(sp.cancel)

def b3_eq(w1, w2):
    return (burau(w1) - burau(w2)).applyfunc(sp.cancel) == sp.zeros(2)

# ------------------------------------------------------------- closures ---
def components(w, n=3):
    perm = list(range(n))
    for i, _ in w:
        perm[i - 1], perm[i] = perm[i], perm[i - 1]
    seen, comps = set(), 0
    for s in range(n):
        if s not in seen:
            comps += 1
            x = s
            while x not in seen:
                seen.add(x)
                x = perm[x]
    return comps

# ------------------------------------------------------------------ main ---
def analyse(name, w, n_strands=3):
    M = psl_norm(img(w, GEN_THEIRS))
    ch, why, X = chirality(M)
    cw = CPT(w)
    Mc = psl_norm(img(cw, GEN_THEIRS))
    return {
        "object": name,
        "word_ours": show(w, ours=True),
        "word_theirs": show(w),
        "closure_components_in_B%d" % n_strands: components(w, n_strands),
        "psl_image": [int(x) for x in M],
        "psl_type": psl_type(M),
        "abs_trace": int(abs(M.trace())),
        "psi": str(psi(M)),
        "chirality_psl": ch,
        "chirality_reason": why,
        "conjugator_to_mirror": X,
        "C": show(C(w)), "P": show(P(w)), "T": show(T(w)),
        "CPT_word_theirs": show(cw),
        "CPT_invariant_word": cw == w,
        "CPT_invariant_B3": b3_eq(cw, w),
        "CPT_invariant_PSL": psl_eq(Mc, M),
        "CPT_image_psl": [int(x) for x in Mc],
        "their_chirality_rule_s1_sign": sorted({e for i, e in w if i == 1}) or None,
    }

def main():
    out = {"schema": "qcd-chirality-psl2z/v1", "prereg": "PREREG.md"}
    s1, s2 = (1, 1), (2, 1)
    s1i, s2i = (1, -1), (2, -1)

    # 1. the map
    tt, RR = GEN_THEIRS[1], GEN_THEIRS[2]
    out["map"] = {
        "sigma2_image_rtr": [int(x) for x in RR],
        "braid_relation_SL_theirs": tt * RR * tt == RR * tt * RR,
        "braid_relation_PSL_theirs": psl_eq(tt * RR * tt, RR * tt * RR),
        "braid_relation_SL_standard": GEN_STD[1] * GEN_STD[2] * GEN_STD[1]
                                      == GEN_STD[2] * GEN_STD[1] * GEN_STD[2],
        "Delta_image_SL_theirs": [int(x) for x in img((s1, s2, s1), GEN_THEIRS)],
        "Delta2_image_SL_theirs": [int(x) for x in img((s1, s2, s1) * 2, GEN_THEIRS)],
        "Delta2_image_SL_standard": [int(x) for x in img((s1, s2, s1) * 2, GEN_STD)],
        "Delta4_image_SL_standard": [int(x) for x in img((s1, s2, s1) * 4, GEN_STD)],
        "mirror_is_J_conjugation": all(
            psl_eq(J * img((g,), GEN_THEIRS) * J, img(C((g,)), GEN_THEIRS))
            for g in (s1, s2)),
        "PC_is_conjugation_by_Delta_in_B3": all(
            b3_eq(P(C((g,))), (s1, s2, s1, g, s1i, s2i, s1i)) for g in (s1, s2)),
    }
    out["psi_selftest_cases"] = selftest_psi()

    # 2-4. objects
    objs = [
        ("electron (ruling) s0 s1 s0 = Delta", (s1, s2, s1), 3),
        ("electron backup trefoil s0^3", (s1, s1, s1), 2),
        ("photon term 1", (), 3),
        ("photon term s0", (s1,), 3),
        ("photon term s1", (s2,), 3),
        ("photon term s0 s1^-1 (chiral vertex)", (s1, s2i), 3),
        ("up quark: unknot strand (no crossings)", (), 1),
        ("REFERENCE: their e_L^- = s1^-1 s2 (theirs)", (s1i, s2), 3),
    ]
    out["objects"] = [analyse(n, w, k) for n, w, k in objs]
    out["electron_CPT_is_Delta_inverse_in_B3"] = b3_eq(CPT((s1, s2, s1)), (s1i, s2i, s1i))
    out["electron_C_P_T_each_Delta_inverse_in_B3"] = [
        b3_eq(f((s1, s2, s1)), (s1i, s2i, s1i)) for f in (C, P, T)]

    # 5. their claim
    letters = [s1, s1i, s2, s2i]
    len2 = [(a, b) for a in letters for b in letters]
    out["claim_len2"] = {
        "n_words": len(len2),
        "invariant_word_level": [show(w) for w in len2 if CPT(w) == w],
        "invariant_B3_level": [show(w) for w in len2 if b3_eq(CPT(w), w)],
        "invariant_PSL_level": [show(w) for w in len2
                                if psl_eq(img(CPT(w), GEN_THEIRS), img(w, GEN_THEIRS))],
    }
    ext = {}
    for L in range(0, 5):
        words = [w for w in itertools.product(letters, repeat=L) if reduce_free(w) == w]
        inv_b3 = [w for w in words if b3_eq(CPT(w), w)]
        inv_psl = [w for w in words
                   if psl_eq(img(CPT(w), GEN_THEIRS), img(w, GEN_THEIRS))]
        ext[L] = {"reduced_words": len(words),
                  "CPT_invariant_B3": len(inv_b3),
                  "CPT_invariant_PSL_only": len(inv_psl) - len(inv_b3),
                  "examples_B3": [show(w) for w in inv_b3[:8]],
                  "examples_PSL_not_B3": [show(w) for w in inv_psl if w not in inv_b3][:8]}
    out["claim_extended_reduced_words"] = ext

    # 6. Hecke compatibility
    q, h = sp.symbols("q h", nonzero=True)
    tm = GEN_STD[1]
    hecke_res = (tm * tm - (q - 1 / q) * tm - I2).applyfunc(sp.simplify)
    sols = sp.solve(list(hecke_res), q, dict=True)
    x = sp.symbols("x")
    out["hecke"] = {
        "min_poly_of_t": str(sp.factor((tm - x * I2).det())),
        "t^2-(q-1/q)t-1 entries": [str(e) for e in hecke_res],
        "q_solving_all_entries": [str(s) for s in sols],
        "sigma_inverse_satisfies_Hecke_with": "h -> -h",
        "check_sigma_inverse": str(sp.expand(
            # sigma^-1 = sigma - h; (sigma-h)^2 - (-h)(sigma-h) - 1 reduced by sigma^2=h sigma+1
            sp.expand((x - h) ** 2 + h * (x - h) - 1).subs(x ** 2, h * x + 1))),
        "note_TC": "T after C = word reversal; a linear anti-automorphism of H_n(q) at fixed q (standard fact, not computed here)",
    }
    # photon CPT, termwise (group-ring / word level only)
    out["photon_CPT_termwise_theirs"] = {
        show(w): show(CPT(w)) for w in [(), (s1,), (s2,), (s1, s2i)]}

    src = open(os.path.abspath(__file__), "rb").read()
    out["scriptHash"] = hashlib.sha256(src).hexdigest()[:12]
    path = os.path.join(HERE, "chirality-psl2z.witness.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(json.dumps(out, indent=1, default=str))

if __name__ == "__main__":
    main()
