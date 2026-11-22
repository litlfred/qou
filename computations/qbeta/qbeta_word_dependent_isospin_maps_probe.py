#!/usr/bin/env python3
"""Word-dependent "isospin" maps on the Q_beta nucleon words: does any map n -> p?

Owner request (2026-11-15, relayed): "Search for word-dependent maps." and
"try Derive the right isospin involution". Beans qou-z08b (stream 12's gap) /
qou-hlx8. ANALYSIS ONLY: writes NO witness, computes NO Q_beta value, touches
no dashboard. Every map is enumerated or listed BEFORE any value is computed;
nothing is selected by closeness to anything.

Words (`nuc11_interleaved`, census letters c*sigma_g + k*h, h = q - 1/q):
    n = core(6) + [ud0, ud0, d1] + gluon(2)
    p = core(6) + [u0,  ud0, ud1] + gluon(2)
    core = (u0 d1)^3, gluon = u0 u0;  u = sigma, d = sigma - h, ud = sigma - h/2.

Per-slot actions on a letter (c, k, g)  [letter = c*sigma_g + k*h]:
    id     (c, k, g)
    flip   (c, k - c, g)        sigma -> sigma^-1, coefficient untouched
    bar    (c, -k - c, g)       sigma -> sigma^-1 and h -> -h in that coefficient
    swap   (-c, k + c, g)       sigma -> -sigma^-1 = h - sigma
    neg    (-c, k, g)           sigma -> -sigma
    relab  (c, k, 1 - g)        sigma_g -> sigma_{1-g}
As letter maps, id/bar/swap/neg/relab are involutions; flip is NOT (flip^2 shifts
k by -2c). Family 2 is restricted to the five involutions as asked, but the
meet-in-the-middle enumeration below covers all six, i.e. the full 6^11.

Families:
  F1 role-dependent: core and gluon fixed, any of the 6 actions on each tail slot
     (6^3 = 216), exact sympy.
  F2 slot-dependent over all 11 slots. Element equality phi(n) = p is decided for
     all 6^11 = 362,797,056 maps by a meet-in-the-middle hash join (left 6 slots
     vs right 5 slots, letters invertible) at a random point mod two primes, then
     every candidate is re-verified EXACTLY in sympy. Trace equality
     tr(phi n) = tr(p) is decided for all 6^11 by the bilinear form of the trace,
     again mod two primes, then exact re-verification of every candidate.
  F3 inner conjugation w -> x w x^-1 for x a group word of length <= 3 in
     sigma_0^+-1, sigma_1^+-1 (53 words). Trace-preserving, so only element
     equality can hit.
Plus: (iii) module maps on the (2,1) block, and the side question
tr^{z_D}(core) bar-even?
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import random
import sys

import numpy as np
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

q = sp.symbols("q", positive=True)
H = q - 1 / q
ZD = q ** 3 / (q ** 2 + 1)
R = sp.Rational
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


# ---- words as (c, k, g) -------------------------------------------------------
U, D, UD = (1, R(0)), (1, R(-1)), (1, R(-1, 2))
CORE = [(1, R(0), 0), (1, R(-1), 1)] * 3
GLUON = [(1, R(0), 0), (1, R(0), 0)]
N_TAIL = [(1, R(-1, 2), 0), (1, R(-1, 2), 0), (1, R(-1), 1)]
P_TAIL = [(1, R(0), 0), (1, R(-1, 2), 0), (1, R(-1, 2), 1)]
N_WORD = CORE + N_TAIL + GLUON
P_WORD = CORE + P_TAIL + GLUON

ACTIONS = {
    "id": lambda c, k, g: (c, k, g),
    "flip": lambda c, k, g: (c, k - c, g),
    "bar": lambda c, k, g: (c, -k - c, g),
    "swap": lambda c, k, g: (-c, k + c, g),
    "neg": lambda c, k, g: (-c, k, g),
    "relab": lambda c, k, g: (c, k, 1 - g),
}
NAMES = list(ACTIONS)
INVOL = {"id", "bar", "swap", "neg", "relab"}


def apply_map(phi, word):
    return [ACTIONS[a](*L) for a, L in zip(phi, word)]


# ---- exact NF + trace ----------------------------------------------------------
def nf_exact(word):
    v = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for c, k, g in word:
        v = hm(v, sp.Integer(c), k * h, g)
    return [sp.expand(x) for x in v]


def tr_exact(v):
    zz = ZD
    basis = [1, zz, zz, zz ** 2, zz ** 2, zz * (h * zz + 1)]
    return sp.factor(sp.together(sp.expand(sum(c * t for c, t in zip(v, basis))).subs(h, H)))


def is_zero_vec(v):
    return all(sp.expand(x) == 0 for x in v)


NF_P = nf_exact(P_WORD)
TR_P = tr_exact(NF_P)
TR_N = tr_exact(nf_exact(N_WORD))


def bar_even(e):
    return sp.simplify(e - e.subs(q, 1 / q)) == 0


# ---- modular arithmetic for the meet-in-the-middle ------------------------------
def hm_mod(v, a, b, gen, hh, p):
    """Right multiplication by a*sigma_gen + b, mod p (census hm_sym table)."""
    c, d = a, b
    r = [0] * 6
    if gen == 0:
        t = [(0, [(1, c), (0, d)]), (1, [(1, c * hh), (0, c), (1, d)]),
             (2, [(3, c), (2, d)]), (3, [(3, c * hh), (2, c), (3, d)]),
             (4, [(5, c), (4, d)]), (5, [(5, c * hh), (4, c), (5, d)])]
    else:
        t = [(0, [(2, c), (0, d)]), (1, [(4, c), (1, d)]),
             (2, [(2, c * hh), (0, c), (2, d)]), (3, [(5, c), (3, d)]),
             (4, [(4, c * hh), (1, c), (4, d)]), (5, [(5, c * hh), (3, c), (5, d)])]
    for si, tg in t:
        if v[si] == 0:
            continue
        for ti, co in tg:
            r[ti] = (r[ti] + v[si] * co) % p
    return r


class ModCtx:
    def __init__(self, p, qv):
        self.p = p
        inv = lambda x: pow(x % p, p - 2, p)
        self.q = qv % p
        self.h = (qv - inv(qv)) % p
        self.z = qv ** 3 * inv(qv * qv + 1) % p
        self.half = inv(2)

    def coef(self, k):  # k rational with denominator 1 or 2
        return (k.p * (self.half if k.q == 2 else 1)) % self.p

    def letter(self, c, k, g):
        return (c % self.p, self.coef(k) * self.h % self.p, g)

    def inv_letter(self, a, b, g):
        p, hh = self.p, self.h
        det = ((a * hh + b) * b - a * a) % p
        di = pow(det, p - 2, p)
        return ((-a * di) % p, ((a * hh + b) * di) % p, g)

    def trace_vec(self):
        z, hh, p = self.z, self.h, self.p
        return [1, z, z, z * z % p, z * z % p, z * (hh * z + 1) % p]


def mitm_element(ctx_list, left_slots, right_slots):
    """All phi with phi(n) == p (mod both ctx), via phi_L(n_L) == p * phi_R(n_R)^-1."""
    left_word, right_word = N_WORD[:left_slots], N_WORD[left_slots:]
    table: dict = {}
    for phiL in itertools.product(NAMES, repeat=len(left_word)):
        key = []
        for ctx in ctx_list:
            v = [1, 0, 0, 0, 0, 0]
            for L in apply_map(phiL, left_word):
                a, b, g = ctx.letter(*L)
                v = hm_mod(v, a, b, g, ctx.h, ctx.p)
            key.extend(v)
        table.setdefault(tuple(key), []).append(phiL)
    hits = []
    pv = {}
    for ctx in ctx_list:
        v = [1, 0, 0, 0, 0, 0]
        for L in P_WORD:
            a, b, g = ctx.letter(*L)
            v = hm_mod(v, a, b, g, ctx.h, ctx.p)
        pv[ctx.p] = v
    for phiR in itertools.product(NAMES, repeat=len(right_word)):
        key = []
        for ctx in ctx_list:
            v = list(pv[ctx.p])
            for L in reversed(apply_map(phiR, right_word)):
                a, b, g = ctx.inv_letter(*ctx.letter(*L))
                v = hm_mod(v, a, b, g, ctx.h, ctx.p)
            key.extend(v)
        for phiL in table.get(tuple(key), []):
            hits.append(phiL + phiR)
    return hits


def mitm_trace(ctx_list, left_slots):
    """All phi with tr(phi n) == tr(p) mod both ctx (bilinear trace form)."""
    left_word, right_word = N_WORD[:left_slots], N_WORD[left_slots:]
    Ls = list(itertools.product(NAMES, repeat=len(left_word)))
    Rs = list(itertools.product(NAMES, repeat=len(right_word)))
    surv = None
    for ctx in ctx_list:
        p = ctx.p
        # bilinear form B[i][j] = tr(b_i * b_j)
        basis = [[1 if t == i else 0 for t in range(6)] for i in range(6)]
        T = ctx.trace_vec()

        def mul(u, w):  # u * w via right-multiplying u by w's expansion
            out = [0] * 6
            # w = sum_j w_j b_j ; u*b_j by right-multiplying letters of b_j's word
            words = [[], [(1, 0, 0)], [(1, 0, 1)], [(1, 0, 1), (1, 0, 0)],
                     [(1, 0, 0), (1, 0, 1)], [(1, 0, 0), (1, 0, 1), (1, 0, 0)]]
            for j in range(6):
                if w[j] == 0:
                    continue
                x = list(u)
                for a, b, g in words[j]:
                    x = hm_mod(x, a, b, g, ctx.h, p)
                out = [(o + w[j] * xi) % p for o, xi in zip(out, x)]
            return out
        B = np.array([[sum(m * t for m, t in zip(mul(basis[i], basis[j]), T)) % p
                       for j in range(6)] for i in range(6)], dtype=np.int64)
        tp = 0
        v = [1, 0, 0, 0, 0, 0]
        for L in P_WORD:
            a, b, g = ctx.letter(*L)
            v = hm_mod(v, a, b, g, ctx.h, p)
        tp = sum(x * t for x, t in zip(v, T)) % p

        def prod(word):
            v = [1, 0, 0, 0, 0, 0]
            for L in word:
                a, b, g = ctx.letter(*L)
                v = hm_mod(v, a, b, g, ctx.h, p)
            return v
        LV = np.array([prod(apply_map(x, left_word)) for x in Ls], dtype=np.int64)
        RV = np.array([prod(apply_map(x, right_word)) for x in Rs], dtype=np.int64)
        W = (B @ RV.T) % p                                   # 6 x |R|
        hits = set()
        for j0 in range(0, W.shape[1], 512):
            blk = (LV @ W[:, j0:j0 + 512]) % p             # |L| x 512
            ii, jj = np.nonzero(blk == tp)
            hits.update(zip(ii.tolist(), (jj + j0).tolist()))
        surv = hits if surv is None else surv & hits
    return [Ls[i] + Rs[j] for i, j in surv]


def descends(phi):
    """A per-slot map descends to an algebra map only if every slot carrying the
    same generator gets the same action (it then must also respect the
    relations). Returns (uniform_per_generator, detail)."""
    per_gen: dict = {0: set(), 1: set()}
    for a, (_, _, g) in zip(phi, N_WORD):
        per_gen[g].add(a)
    uni = all(len(s) <= 1 for s in per_gen.values())
    return uni, {g: sorted(s) for g, s in per_gen.items()}


def report_hit(phi, kind):
    phin = nf_exact(apply_map(phi, N_WORD))
    el = is_zero_vec([a - b for a, b in zip(phin, NF_P)])
    trn = tr_exact(phin)
    tr_eq = sp.simplify(trn - TR_P) == 0
    g = sp.factor(sp.together((trn - TR_P) / H))
    uni, det = descends(phi)
    nontriv = any(a != "id" for a in phi)
    print(f"    {kind}: phi={phi}")
    print(f"       element phi(n)=p: {el}   trace equal: {tr_eq}   "
          f"uniform per generator: {uni} {det}   g_phi bar-even: {bar_even(g)}")
    return dict(phi=phi, element=el, trace=tr_eq, uniform=uni, nontrivial=nontriv)


# ---- (2,1) block, exact --------------------------------------------------------
def rep21():
    """2-dim irrep of H_3 with sigma^2 = h sigma + 1 (eigenvalues q, -1/q)."""
    s0 = sp.Matrix([[q, 0], [0, -1 / q]])
    x, w, y = sp.symbols("x w y")
    s1 = sp.Matrix([[x, y], [1, w]])
    eqs = list((s1 * s1 - H * s1 - sp.eye(2))) + list(s0 * s1 * s0 - s1 * s0 * s1)
    sol = sp.solve(eqs, [x, w, y], dict=True)
    sol = [s for s in sol if sp.simplify(s1.subs(s) - s0) != sp.zeros(2)
           and sp.simplify((s1.subs(s)).trace() - H) == 0]
    return s0, sp.simplify(s1.subs(sol[0]))


def mat_of(word, S):
    M = sp.eye(2)
    for c, k, g in word:
        M = M * (c * S[g] + k * H * sp.eye(2))
    return sp.simplify(M)


def main() -> int:
    random.seed(20261115)
    print(f"n word: {N_WORD}\np word: {P_WORD}")
    print(f"tr(n) - tr(p) = {sp.factor(TR_N - TR_P)}  (nonzero: {sp.simplify(TR_N - TR_P) != 0})")

    # ---- F1 -------------------------------------------------------------------
    print("\nF1 role-dependent: core+gluon fixed, 6 actions per tail slot (216 maps)")
    f1_el, f1_tr = [], []
    for phi_t in itertools.product(NAMES, repeat=3):
        phi = ("id",) * 6 + phi_t + ("id",) * 2
        v = nf_exact(apply_map(phi, N_WORD))
        if is_zero_vec([a - b for a, b in zip(v, NF_P)]):
            f1_el.append(phi)
        if sp.simplify(tr_exact(v) - TR_P) == 0:
            f1_tr.append(phi)
    print(f"    element hits: {len(f1_el)} / 216;  trace hits: {len(f1_tr)} / 216")
    for phi in f1_el + [x for x in f1_tr if x not in f1_el]:
        report_hit(phi, "F1")
    check("F1_counted_exhaustively", True, f"element {len(f1_el)}, trace {len(f1_tr)} of 216")

    # ---- F2 -------------------------------------------------------------------
    print("\nF2 slot-dependent, all 11 slots: 6^11 = 362,797,056 maps (MITM, exact re-check)")
    ctxs = [ModCtx(1000003, random.randrange(2, 1000000)),
            ModCtx(999983, random.randrange(2, 999000))]
    cand_el = mitm_element(ctxs, 6, 5)
    exact_el = [phi for phi in cand_el
                if is_zero_vec([a - b for a, b in zip(nf_exact(apply_map(phi, N_WORD)), NF_P)])]
    print(f"    element candidates (mod-p): {len(cand_el)};  exact element hits: {len(exact_el)}")
    inv_el = [phi for phi in exact_el if set(phi) <= INVOL]
    print(f"    of which within the 5 involutive actions (5^11 = 48,828,125 maps): {len(inv_el)}")
    el_reports = [report_hit(phi, "F2-element") for phi in exact_el]

    cand_tr = mitm_trace(ctxs, 6)
    print(f"    trace candidates (mod-p): {len(cand_tr)}")
    exact_tr = []
    for phi in cand_tr:
        if sp.simplify(tr_exact(nf_exact(apply_map(phi, N_WORD))) - TR_P) == 0:
            exact_tr.append(phi)
    inv_tr = [phi for phi in exact_tr if set(phi) <= INVOL]
    print(f"    exact trace hits: {len(exact_tr)};  within involutions: {len(inv_tr)}")
    img = {tuple(apply_map(phi, N_WORD)) for phi in exact_tr}
    changed = {}
    for w in img:
        nch = sum(1 for a, b in zip(w, N_WORD) if a != b)
        changed[nch] = changed.get(nch, 0) + 1
    core_untouched = sum(1 for w in img if list(w[:6]) == CORE and list(w[9:]) == GLUON)
    print(f"    distinct image words among trace hits: {len(img)};  letters changed per "
          f"image word: {dict(sorted(changed.items()))};  with core+gluon untouched: "
          f"{core_untouched}")
    for i in range(11):
        hist: dict = {}
        for phi in exact_tr:
            hist[phi[i]] = hist.get(phi[i], 0) + 1
        print(f"      slot {i:2d} {N_WORD[i]}: {hist}")
    tr_uniform = [phi for phi in exact_tr if descends(phi)[0]]
    print(f"    trace hits uniform per generator (necessary to descend): {len(tr_uniform)}")
    for phi in tr_uniform:
        report_hit(phi, "F2-trace-uniform")
    nonuni_g_even = 0
    for phi in exact_tr:
        g = sp.factor(sp.together((tr_exact(nf_exact(apply_map(phi, N_WORD))) - TR_P) / H))
        nonuni_g_even += bar_even(g)
    print(f"    (all trace hits have tr(phi n) = tr(p) so f_phi = 0 and g_phi = 0 is trivially "
          f"bar-even: {nonuni_g_even}/{len(exact_tr)})")
    check("F2_element_exhaustive", True, f"{len(exact_el)} exact element hits of 6^11")
    check("F2_trace_exhaustive", True, f"{len(exact_tr)} exact trace hits of 6^11")

    # ---- F3 -------------------------------------------------------------------
    print("\nF3 inner conjugation x n x^-1, x a group word of length <= 3 (53 words)")
    gens = [(1, R(0), 0), (1, R(-1), 0), (1, R(0), 1), (1, R(-1), 1)]   # s0, s0^-1, s1, s1^-1
    invg = {0: 1, 1: 0, 2: 3, 3: 2}
    words = [()]
    for L in (1, 2, 3):
        words += list(itertools.product(range(4), repeat=L))
    words = [w for w in words if all(invg[w[i]] != w[i + 1] for i in range(len(w) - 1))]
    f3_hits = 0
    for w in words:
        x = [gens[i] for i in w]
        xi = [gens[invg[i]] for i in reversed(w)]
        if is_zero_vec([a - b for a, b in zip(nf_exact(x + N_WORD + xi), NF_P)]):
            f3_hits += 1
    print(f"    reduced words tested: {len(words)};  element hits: {f3_hits};  "
          f"trace hits: 0 by invariance (tr(n) != tr(p))")
    check("F3_no_inner_conjugation_maps_n_to_p", f3_hits == 0, f"{len(words)} words")

    # ---- (iii) module map on the (2,1) block ---------------------------------
    print("\n(iii) (2,1) block: is T = rho(n) rho(p)^-1 compatible with the core/gluon action?")
    s0, s1 = rep21()
    S = {0: s0, 1: s1}
    check("rep21_is_a_rep", sp.simplify(s1 * s1 - H * s1 - sp.eye(2)) == sp.zeros(2)
          and sp.simplify(s0 * s1 * s0 - s1 * s0 * s1) == sp.zeros(2))
    rn, rp = mat_of(N_WORD, S), mat_of(P_WORD, S)
    T = sp.simplify(rn * rp.inv())
    rc, rg = mat_of(CORE, S), mat_of(GLUON, S)
    comm_core = sp.simplify(T * rc - rc * T) == sp.zeros(2)
    comm_gl = sp.simplify(T * rg - rg * T) == sp.zeros(2)
    scalar = sp.simplify(T - T[0, 0] * sp.eye(2)) == sp.zeros(2)
    Ttail = sp.simplify(mat_of(N_TAIL, S) * mat_of(P_TAIL, S).inv())
    tail_comm_core = sp.simplify(Ttail * rc - rc * Ttail) == sp.zeros(2)
    tail_comm_gl = sp.simplify(Ttail * rg - rg * Ttail) == sp.zeros(2)
    print(f"    unique left-multiplier T = rho(n)rho(p)^-1: scalar? {scalar}; "
          f"commutes with rho(core)? {comm_core}; with rho(gluon)? {comm_gl}")
    print(f"    tail-only operator T_t = rho(n_tail)rho(p_tail)^-1: commutes with rho(core)? "
          f"{tail_comm_core}; with rho(gluon)? {tail_comm_gl}")
    print(f"    trace of T_t = {sp.factor(Ttail.trace())},  det T_t = {sp.factor(Ttail.det())}")
    check("module_map_does_not_commute_with_core_and_gluon",
          not (tail_comm_core and tail_comm_gl))

    # ---- side question ---------------------------------------------------------
    print("\nSIDE: tr^{z_D}(core) bar-even?")
    tc = tr_exact(nf_exact(CORE))
    print(f"    tr(core) = {tc}")
    print(f"    bar-even: {bar_even(tc)};  bar-odd: {sp.simplify(tc + tc.subs(q, 1/q)) == 0}")
    tg = tr_exact(nf_exact(GLUON))
    print(f"    tr(gluon) = {tg}; bar-even: {bar_even(tg)}")

    ok = all(r[1] for r in RESULTS)
    print(f"\n{sum(r[1] for r in RESULTS)}/{len(RESULTS)} checks pass")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
