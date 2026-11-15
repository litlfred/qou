#!/usr/bin/env python3
"""The partition function behind the corpus b3 -- and what its sign actually is.

Bean `qou-rwhv` left one step undone after the 2026-08-30 identity
`b3_corpus == -phi^T_3(mu - 1)`: exhibit the trace-side partition function Xi
whose cluster (Mayer) expansion has the corpus's b3 as its third Ursell
coefficient -- polymer set, weight, compatibility relation, ensemble -- or show
that none does. This probe does both halves of that and measures the sign
consequence, which reverses the 2026-08-30 reading.

THE PARTITION FUNCTION (it exists, and it is the obvious one)
-------------------------------------------------------------
Sites = the nucleons of a fixed nucleus S. Pair weight on a bond e = the trace
of its interface letter, `mu_e = z_D + d_e` in (0,1). Mayer variable
`g_e = mu_e - 1`. Hard-core activity `z_i` per site (each nucleon present at
most once). Then

    Xi_S(z) = SUM_{T subset S} z^T Z_T,     Z_T = PROD_{e inside T} mu_e,

and `Z_T = tr_M(W_atom(T)) / tr_M(W_free(T))` by connected-sum multiplicativity
of the Markov trace (`MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`), which
Sec.3 re-measures on the LIVE alternating-core word to 1e-40. The multilinear
logarithm of Xi is the Ursell series, `ln Xi_S = SUM_T z^T phi^T_T`
(exponential formula; Sec.2 verifies it symbolically through n = 4, and
`d^3 ln Xi / dz1 dz2 dz3 |_0 = phi^T_3` exactly). So the Mayer/Ursell
vocabulary is not an analogy here: this is a hard-core lattice gas on the
nucleon sites, grand-canonical over the SUB-CLUSTERS of one nucleus, and its
third Ursell coefficient is exactly what the 2026-08-30 identity says.

WHY THE IDENTITY HOLDS AT n = 3 AND FAILS AT n = 4 (Sec.1, exact)
-----------------------------------------------------------------
The corpus cumulants are BOOLEAN-lattice inversions (inclusion-exclusion over
subsets) of `W = 1 - Z`; the Ursell functions are PARTITION-lattice inversions
(the cluster property `Z_S = SUM_pi PROD_B phi^T_B`) of Z. For a
bond-multiplicative Z:

    Boolean inversion of Z at S  =  SUM over spanning edge sets with NO ISOLATED
                                    VERTEX of PROD g_e
    Ursell function at S         =  SUM over CONNECTED spanning edge sets

and `b_S^corpus = -(Boolean inversion of Z)`. The two graph classes coincide
while |S| <= 3 and first differ at |S| = 4 by the three perfect matchings --
which is the whole content of "400/400 at n=3, 200/200 mismatches at n=4".
Measured here in exact Fraction arithmetic for n = 2..5 with the disconnected
remainder enumerated explicitly (0, 0, 3, 40 terms).

THE SIGN, AND THE REVERSAL (Sec.3)
----------------------------------
The log-derived binding is `B = -alpha ln(Xi/Xi_free)`, so its Mayer
coefficients are `-phi^T_T` at EVERY order: pair `-phi^T_2 = 1 - mu > 0`, triple
`-phi^T_3`. The corpus's uniform minus (`b2 = -phi2`, `b3 = -phi3`) IS the Mayer
expansion. The Ursell alternation `(-1)^(n-1) phi^T_n >= 0` on (0,1) then makes
the third Mayer coefficient <= 0 -- strictly < 0 for every triple, uniform or
not (Lean `UrsellPartitionFunctionB3.b3corpus_neg`). So:

  * `MayerThreeBodySign`'s negative b3 is NOT a missing (-1)^(n-1). It is the
    classical sign. The 2026-08-30 "restore the alternation" prescription
    `b_n = (-1)^(n-1) phi^T_n` is, exactly, the same expansion at NEGATIVE
    activity `z -> -z` (Lean `restored_eq_neg_activity`; checked here
    symbolically). No ensemble at positive activity produces `+phi^T_3`.
  * The `2/3` threshold was an artefact of leaving `P3 >= 0` free. With `P3` the
    bond product, `b3 = -(1-f)^2 (f+2) < 0` for every f in (0,1).
  * Within the Mayer vocabulary a positive third coefficient at positive
    activity needs an ATTRACTIVE channel, a bond factor above 1 (g > 0). Every
    interface letter of the production word has trace `z_D + d < 1` (measured).
    That is scope-(a): a property of the letters in use, not a theorem.
  * The FIXED-A nucleus is the canonical ensemble, whose partition function is
    the top coefficient `Z_S`, and `ln Z_S` is exactly pairwise -- the connected
    three-body part of the derived binding is 0 (`PairwiseCumulantVanishing`;
    re-measured here, `ln Z_012 - ln Z_01 - ln Z_12 = 0` to 1e-40). `phi^T_3`
    enters the log only through the grand-canonical sum over sub-clusters.

The magnitude `2.2511` MeV recorded on 2026-08-30 is `+phi^T_3` at a
deuteron-pinned scale under the negative-activity reading; it is reproduced
here for continuity and reported as such, not as a postdiction of a derived
quantity. What the Mayer expansion actually gives at the live chain bonds is
reported in MeV with its (wrong) sign against AME b3(3H) and b3(3He).

PER-BLOCK CHARACTERS (Sec.4). Bond multiplicativity holds for the Markov trace,
not for the individual Wedderburn characters chi_lambda -- measured on 2H, the
per-block ratio `chi(atom)/chi(free)` differs from `mu_pn` by O(1). So there is
no per-block partition function with these Ursell functions; the object the
identification applies to is `tr_M`, and only `tr_M`.

NO FITTING. No parameter is chosen; no per-A dispatch; no census. Exact where
the claim is algebraic (Fraction / sympy), 200-bit MPFR where it is numerical,
proton pin (`Q_50_DIGIT_STR`), convention D (`z = q^3/(q^2+1)`).

-- Ref: [jansen2022cluster] https://doi.org/10.1007/s10955-022-02992-6
Bean `qou-rwhv`; audit
`docs/audits/2026-09-12-ursell-partition-function-for-b3.md`; Lean
`QOU/MassTheory/UrsellPartitionFunctionB3.lean`.
"""
from __future__ import annotations

import datetime
import json
import os
import random
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import gmpy2  # noqa: E402
import sympy as sp  # noqa: E402
from gmpy2 import mpfr  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

RANDOM_SEED = 12
N_TRIALS = {2: 100, 3: 200, 4: 100, 5: 20}
TOL = mpfr("1e-40")


# ---------------------------------------------------------------- exact layer
def _prod(it):
    r = Fraction(1)
    for x in it:
        r *= x
    return r


def edge_subsets(n):
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        yield [edges[i] for i in range(len(edges)) if mask >> i & 1]


def is_connected(E_, verts):
    verts = list(verts)
    parent = {v: v for v in verts}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for i, j in E_:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
    return len({find(v) for v in verts}) == 1


def support(E_):
    return {v for e in E_ for v in e}


def graph_sum(g, n, keep):
    """SUM over edge sets E on [n] satisfying `keep(E)` of PROD g_e."""
    return sum((_prod(g[e] for e in E_) for E_ in edge_subsets(n)
                if keep(E_)), Fraction(0))


def ursell_connected(g, n):
    """phi^T_n as the connected-spanning-graph sum (Jansen-Kolesnikov p.5)."""
    return graph_sum(g, n, lambda E_: is_connected(E_, range(n)))


def no_isolated_vertex_sum(g, n):
    return graph_sum(g, n, lambda E_: support(E_) == set(range(n)))


def disconnected_no_isolated_sum(g, n):
    return graph_sum(g, n, lambda E_: support(E_) == set(range(n))
                     and not is_connected(E_, range(n)))


def Z(f, S):
    """Canonical partition function of the cluster S: product of its bond factors."""
    return _prod(f[e] for e in combinations(sorted(S), 2))


def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for smaller in set_partitions(rest):
        for i, block in enumerate(smaller):
            yield smaller[:i] + [[first] + block] + smaller[i + 1:]
        yield [[first]] + smaller


def ursell_cluster_property(f, S, memo):
    """phi^T_S DEFINED by Z_S = SUM_{pi in Pi(S)} PROD_{B in pi} phi^T_B."""
    S = tuple(sorted(S))
    if S in memo:
        return memo[S]
    if len(S) == 1:
        memo[S] = Fraction(1)
        return memo[S]
    tot = Fraction(0)
    for pi in set_partitions(S):
        if len(pi) == 1:
            continue
        tot += _prod(ursell_cluster_property(f, B, memo) for B in pi)
    memo[S] = Z(f, S) - tot
    return memo[S]


def boolean_inversion(F, S):
    """Inclusion-exclusion over the subset lattice: SUM_{T subset S} (-1)^{|S-T|} F(T)."""
    S = tuple(sorted(S))
    tot = Fraction(0)
    for k in range(len(S) + 1):
        for T in combinations(S, k):
            tot += (-1) ** (len(S) - k) * F(T)
    return tot


def corpus_cumulant(f, S, memo):
    """QOU.Mass.PairwiseCumulantVanishing's recursion on W = 1 - Z:
    b_S = W(S) - SUM_{T strictly inside S, |T| >= 2} b_T."""
    S = tuple(sorted(S))
    if S in memo:
        return memo[S]
    if len(S) < 2:
        memo[S] = Fraction(0)
        return memo[S]
    W_S = 1 - Z(f, S)
    inner = Fraction(0)
    for k in range(2, len(S)):
        for T in combinations(S, k):
            inner += corpus_cumulant(f, T, memo)
    memo[S] = W_S - inner
    return memo[S]


def section1_exact():
    rng = random.Random(RANDOM_SEED)
    rows = []
    for n, trials in N_TRIALS.items():
        ok_bool = ok_cluster = ok_corpus = ok_split = 0
        n_disc = None
        for _ in range(trials):
            f = {e: Fraction(rng.randint(1, 9999), 10000)
                 for e in combinations(range(n), 2)}
            g = {e: f[e] - 1 for e in f}
            S = tuple(range(n))
            bZ = boolean_inversion(lambda T: Z(f, T), S)
            phi_c = ursell_connected(g, n)
            phi_p = ursell_cluster_property(f, S, {})
            b_corp = corpus_cumulant(f, S, {})
            niv = no_isolated_vertex_sum(g, n)
            disc = disconnected_no_isolated_sum(g, n)
            ok_bool += bZ == niv
            ok_cluster += phi_c == phi_p
            ok_corpus += b_corp == -bZ
            ok_split += bZ - phi_c == disc
        n_disc = sum(1 for E_ in edge_subsets(n)
                     if support(E_) == set(range(n))
                     and not is_connected(E_, range(n)))
        rows.append({
            "n": n, "trials": trials,
            "boolean_inversion_eq_no_isolated_vertex_sum": ok_bool,
            "connected_sum_eq_cluster_property": ok_cluster,
            "corpus_b_eq_minus_boolean_inversion": ok_corpus,
            "boolean_minus_ursell_eq_disconnected_remainder": ok_split,
            "disconnected_isolated_free_graphs": n_disc,
            "corpus_b_eq_minus_ursell": n_disc == 0,
        })
    return rows


# ------------------------------------------------------------ symbolic layer
def section2_symbolic():
    out = {}
    # n = 3
    z1, z2, z3 = sp.symbols("z1 z2 z3")
    f12, f13, f23 = sp.symbols("f12 f13 f23")
    g12, g13, g23 = f12 - 1, f13 - 1, f23 - 1
    phi3 = g12 * g13 * g23 + g12 * g13 + g12 * g23 + g13 * g23
    Xi = (1 + z1 + z2 + z3 + z1 * z2 * f12 + z1 * z3 * f13 + z2 * z3 * f23
          + z1 * z2 * z3 * f12 * f13 * f23)
    U = (z1 + z2 + z3 + z1 * z2 * g12 + z1 * z3 * g13 + z2 * z3 * g23
         + z1 * z2 * z3 * phi3)
    D3 = sp.expand(6 * Xi - (6 + 6 * U + 3 * U ** 2 + U ** 3))
    _q, r3 = sp.reduced(D3, [z1 ** 2, z2 ** 2, z3 ** 2], z1, z2, z3, f12, f13, f23)
    L = sp.log(Xi)
    d3 = sp.simplify(sp.diff(L, z1, z2, z3).subs({z1: 0, z2: 0, z3: 0}) - phi3)
    d2 = sp.simplify(sp.diff(L, z1, z2).subs({z1: 0, z2: 0, z3: 0}) - g12)
    # negative activity: the "restored" coefficients
    mayer_binding = -(U - (z1 + z2 + z3))
    restored = (z1 * z2 * (-g12) + z1 * z3 * (-g13) + z2 * z3 * (-g23)
                + z1 * z2 * z3 * phi3)
    neg_act = sp.expand(restored - mayer_binding.subs(
        {z1: -z1, z2: -z2, z3: -z3}, simultaneous=True))
    # n = 4
    zs = sp.symbols("w1 w2 w3 w4")
    fs = {e: sp.Symbol(f"h{e[0] + 1}{e[1] + 1}") for e in combinations(range(4), 2)}
    gs = {e: fs[e] - 1 for e in fs}

    def zprod(T):
        return sp.prod([zs[i] for i in T]) if T else sp.Integer(1)

    def Zs(T):
        return sp.prod([fs[e] for e in combinations(sorted(T), 2)]) if len(T) >= 2 else sp.Integer(1)

    memo = {}

    def phi(T):
        T = tuple(sorted(T))
        if T in memo:
            return memo[T]
        if len(T) == 1:
            memo[T] = sp.Integer(1)
            return memo[T]
        tot = sp.Integer(0)
        for pi in set_partitions(T):
            if len(pi) == 1:
                continue
            tot += sp.prod([phi(B) for B in pi])
        memo[T] = sp.expand(Zs(T) - tot)
        return memo[T]

    subsets = [T for k in range(1, 5) for T in combinations(range(4), k)]
    Xi4 = 1 + sum(zprod(T) * Zs(T) for T in subsets)
    U4 = sum(zprod(T) * phi(T) for T in subsets)
    D4 = sp.expand(24 * Xi4 - (24 + 24 * U4 + 12 * U4 ** 2 + 4 * U4 ** 3 + U4 ** 4))
    _q4, r4 = sp.reduced(D4, [w ** 2 for w in zs], *zs, *fs.values())
    phi4_conn = sum(sp.prod([gs[e] for e in E_]) for E_ in edge_subsets(4)
                    if is_connected(E_, range(4)))
    out.update({
        "n3_exponential_formula_remainder_mod_z_sq": str(r3),
        "n3_d3_logXi_at_0_minus_phi3": str(d3),
        "n3_d2_logXi_at_0_minus_g12": str(d2),
        "n3_restored_minus_mayerBinding_at_negative_activity": str(neg_act),
        "n4_exponential_formula_remainder_mod_z_sq": str(r4),
        "n4_cluster_property_phi4_minus_connected_sum":
            str(sp.expand(phi((0, 1, 2, 3)) - phi4_conn)),
    })
    return out


# ---------------------------------------------------------- framework layer
def s(v, n=25):
    m, e, _ = gmpy2.digits(mpfr(v), 10, n)
    neg = m.startswith("-")
    m = m.lstrip("-")
    body = ("0." + "0" * (-e) + m) if e <= 0 else (m[:e] + "." + m[e:])
    return ("-" if neg else "") + body


def chain_word(order, active):
    """Production chain word (live alternating core, `E.nucleon_word`), with the
    interface letter at 3k+2 present iff k in `active`."""
    w = []
    for k, sp_ in enumerate(order):
        w += E.nucleon_word(E.B_P if sp_ == "p" else E.B_N, 3 * k, 3 * k + 1)
        if k in active and k < len(order) - 1:
            w.append((1, E.bond_d(order[k], order[k + 1]), 3 * k + 2))
    return w


def chi_block(n, shape, word):
    rows, dim = E.sigmas(shape)
    ops = [E._op(rows[g], mpfr(c), d) for c, d, g in word]
    return E._rows_partial(ops, dim, 0, dim)


def section3_framework():
    Q = E.Q
    zD = Q ** 3 / (Q ** 2 + 1)
    alpha = mpfr(str(M_E_MEV)) / (Q * (Q - 1))
    ame = {"D": mpfr(str(AME_B_DEUTERON_MEV_VALIDATION)),
           "3H": mpfr(str(AME_B_TRITIUM_MEV_VALIDATION)),
           "3He": mpfr(str(AME_B_HE3_MEV_VALIDATION))}
    mu = {"pp": zD + E.bond_d("p", "p"), "pn": zD + E.bond_d("p", "n"),
          "nn": zD + E.bond_d("n", "n")}

    # (a) Z_S = tr(atom)/tr(free) = PROD mu on the live word, A = 2..4
    ratio_rows = []
    ok_mult = True
    for order in ("pn", "pnn", "ppn", "ppnn"):
        n = 3 * len(order)
        tf = E.trM(n, chain_word(order, set()))
        ta = E.trM(n, chain_word(order, set(range(len(order) - 1))))
        expect = mpfr(1)
        for k in range(len(order) - 1):
            expect *= mu["".join(sorted(order[k:k + 2], reverse=True))]
        dev = abs(ta / tf - expect)
        ok_mult &= dev < TOL
        ratio_rows.append({"atom": order, "n_strands": n, "tr_free": s(tf),
                           "tr_atom": s(ta), "Z_S": s(ta / tf),
                           "prod_mu": s(expect), "abs_dev": s(dev, 5)})

    # (b) sub-cluster partition functions of the A = 3 chains, Ursell phi3,
    #     corpus b3, the log cumulant, and MeV
    a3 = []
    ok_log = ok_sign = True
    for order in ("pnn", "ppn"):
        Z01 = E.trM(6, chain_word(order[:2], {0})) / E.trM(6, chain_word(order[:2], set()))
        Z12 = E.trM(6, chain_word(order[1:], {0})) / E.trM(6, chain_word(order[1:], set()))
        Z02 = mpfr(1)   # no interface letter joins nucleons 0 and 2 in the chain
        Z012 = E.trM(9, chain_word(order, {0, 1})) / E.trM(9, chain_word(order, set()))
        phi3 = Z012 - Z01 - Z12 - Z02 + 2          # Boolean inversion = Ursell at n = 3
        g01, g12 = Z01 - 1, Z12 - 1
        b3_corpus = (1 - Z012) - (1 - Z01) - (1 - Z12) - (1 - Z02)
        log_cum = gmpy2.log(Z012) - gmpy2.log(Z01) - gmpy2.log(Z12)
        ok_log &= abs(log_cum) < TOL
        ok_sign &= (phi3 > 0) and (b3_corpus < 0) and abs(b3_corpus + phi3) < TOL
        nm = "3H" if order == "pnn" else "3He"
        ame_b3 = ame[nm] - 3 * ame["D"]
        scale_D = ame["D"] / (1 - mu["pn"])
        a3.append({
            "atom": nm, "bonds": [order[:2], order[1:]],
            "Z_01": s(Z01), "Z_12": s(Z12), "Z_012": s(Z012),
            "Z_012_minus_Z01_Z12": s(Z012 - Z01 * Z12, 5),
            "phi_T_3_chain": s(phi3), "equals_g01_g12": bool(abs(phi3 - g01 * g12) < TOL),
            "b3_corpus_W_units": s(b3_corpus),
            "log_binding_3body_cumulant": s(log_cum, 5),
            "mayer_third_coeff_alpha_scaled_MeV": s(-alpha * phi3, 12),
            "mayer_third_coeff_deuteron_pinned_MeV": s(-scale_D * phi3, 12),
            "negative_activity_coeff_alpha_scaled_MeV": s(alpha * phi3, 12),
            "negative_activity_coeff_deuteron_pinned_MeV": s(scale_D * phi3, 12),
            "ame_b3_MeV": s(ame_b3, 12),
            "abs_ratio_alpha_scaled_to_ame": s(alpha * phi3 / ame_b3, 8),
            "abs_ratio_deuteron_pinned_to_ame": s(scale_D * phi3 / ame_b3, 8),
        })

    # (c) the 2026-08-30 uniform-triangle figures (both typings), reproduced
    #     and re-labelled: the "restored" MeV is the negative-activity coefficient
    tri = {}
    for label, fpn in (("chi_typing_f_pn_eq_z_D", zD), ("probe2_typing_f_pn", mu["pn"])):
        g = fpn - 1
        phi3_tri = g ** 3 + 3 * g ** 2
        scale_D = ame["D"] / (1 - fpn)
        tri[label] = {
            "f_pn": s(fpn), "phi_T_3_triangle": s(phi3_tri),
            "b3_corpus_triangle": s(-phi3_tri),
            "deuteron_pinned_MeV_mayer_sign": s(-scale_D * phi3_tri, 12),
            "deuteron_pinned_MeV_negative_activity": s(scale_D * phi3_tri, 12)}
    tri["reading"] = ("the 2026-08-30 '2.2511' (chi) and '2.7439' (probe-2) MeV are the "
                      "negative-activity coefficients; the Mayer sign is the negative of each")

    # (d) no attractive Mayer channel among the production letters
    letters = {k: s(v) for k, v in mu.items()}
    ok_attr = all(0 < v < 1 for v in mu.values())

    # (e) per-block: chi_lambda(atom)/chi_lambda(free) vs mu_pn on 2H
    ps, _ws = E.weights(6)
    wa, wf = chain_word("pn", {0}), chain_word("pn", set())
    blocks = []
    worst = mpfr(0)
    for shape in ps:
        ca, cf = chi_block(6, shape, wa), chi_block(6, shape, wf)
        r = ca / cf if cf != 0 else None
        dev = abs(r - mu["pn"]) if r is not None else None
        if dev is not None:
            worst = max(worst, dev)
        blocks.append({"partition": list(shape), "chi_atom": s(ca), "chi_free": s(cf),
                       "ratio": s(r) if r is not None else None,
                       "abs_dev_from_mu_pn": s(dev, 6) if dev is not None else None})
    return {
        "q0": Q_50_DIGIT_STR, "z_D": s(zD), "alpha_MeV": s(alpha, 15),
        "interface_letter_traces": letters, "all_letters_below_one": ok_attr,
        "trace_ratio_is_bond_product": ratio_rows, "ok_multiplicative": ok_mult,
        "A3_chains": a3, "ok_log_pairwise": ok_log, "ok_sign": ok_sign,
        "uniform_triangle_2026_08_30": tri,
        "per_block_2H": blocks, "per_block_worst_dev": s(worst, 6),
        "per_block_not_multiplicative": bool(worst > mpfr("1e-3")),
    }


def main() -> int:
    print("Sec.1  EXACT: Boolean vs partition-lattice cumulants of a bond-multiplicative Z")
    ex = section1_exact()
    print(f"    {'n':>2}{'trials':>8}{'bool=noIso':>12}{'conn=cluster':>14}"
          f"{'b=-bool':>10}{'split':>8}{'#disc':>7}")
    for r in ex:
        print(f"    {r['n']:>2}{r['trials']:>8}"
              f"{r['boolean_inversion_eq_no_isolated_vertex_sum']:>12}"
              f"{r['connected_sum_eq_cluster_property']:>14}"
              f"{r['corpus_b_eq_minus_boolean_inversion']:>10}"
              f"{r['boolean_minus_ursell_eq_disconnected_remainder']:>8}"
              f"{r['disconnected_isolated_free_graphs']:>7}")
    print("    -> corpus b_n = -phi^T_n exactly while no disconnected isolated-vertex-free"
          " graph exists (n <= 3); at n = 4 the remainder is the 3 matchings")

    print("\nSec.2  SYMBOLIC: ln Xi = SUM z^T phi^T_T (exponential formula), n = 3 and 4")
    sy = section2_symbolic()
    for k, v in sy.items():
        print(f"    {k:60s} {v}")

    print("\nSec.3  FRAMEWORK: live alternating-core word, proton pin, convention D")
    fw = section3_framework()
    print(f"    z_D = {fw['z_D'][:22]}   alpha = {fw['alpha_MeV']} MeV")
    print(f"    interface letter traces mu: {fw['interface_letter_traces']}")
    print(f"    {'atom':>5} {'Z_S = tr(atom)/tr(free)':>26} {'prod mu':>26} {'|dev|':>8}")
    for r in fw["trace_ratio_is_bond_product"]:
        print(f"    {r['atom']:>5} {r['Z_S'][:26]:>26} {r['prod_mu'][:26]:>26} {r['abs_dev']:>8}")
    for r in fw["A3_chains"]:
        print(f"    {r['atom']}  bonds {r['bonds']}")
        print(f"       Z_01 {r['Z_01'][:20]}  Z_12 {r['Z_12'][:20]}  Z_012 {r['Z_012'][:20]}"
              f"   Z_012 - Z_01 Z_12 = {r['Z_012_minus_Z01_Z12']}")
        print(f"       phi^T_3 = {r['phi_T_3_chain'][:20]}   corpus b3 = {r['b3_corpus_W_units'][:20]}"
              f"   ln-cumulant = {r['log_binding_3body_cumulant']}")
        print(f"       Mayer 3rd coeff:  alpha-scaled {r['mayer_third_coeff_alpha_scaled_MeV']} MeV"
              f"   deuteron-pinned {r['mayer_third_coeff_deuteron_pinned_MeV']} MeV")
        print(f"       AME b3 = {r['ame_b3_MeV']} MeV   |ratio| alpha {r['abs_ratio_alpha_scaled_to_ame']}"
              f"  D-pinned {r['abs_ratio_deuteron_pinned_to_ame']}   (SIGN WRONG at both)")
    for label, t in fw["uniform_triangle_2026_08_30"].items():
        if label == "reading":
            continue
        print(f"    uniform triangle {label}: f_pn = {t['f_pn'][:12]}, phi^T_3 = "
              f"{t['phi_T_3_triangle'][:14]}, Mayer sign {t['deuteron_pinned_MeV_mayer_sign']} MeV, "
              f"negative activity {t['deuteron_pinned_MeV_negative_activity']} MeV")
    print(f"    per-block 2H: worst |chi_atom/chi_free - mu_pn| = {fw['per_block_worst_dev']}"
          f"  -> multiplicativity is a tr_M fact, not a per-block one")

    assertions = [
        {"name": "Boolean inversion of a bond-multiplicative Z is the no-isolated-vertex graph sum (n=2..5)",
         "passed": all(r["boolean_inversion_eq_no_isolated_vertex_sum"] == r["trials"] for r in ex)},
        {"name": "connected-graph sum equals the cluster-property definition of phi^T (n=2..5)",
         "passed": all(r["connected_sum_eq_cluster_property"] == r["trials"] for r in ex)},
        {"name": "corpus b_n = -(Boolean inversion of Z) (n=2..5)",
         "passed": all(r["corpus_b_eq_minus_boolean_inversion"] == r["trials"] for r in ex)},
        {"name": "Boolean - Ursell = disconnected isolated-vertex-free remainder: 0,0,3,40 terms",
         "passed": all(r["boolean_minus_ursell_eq_disconnected_remainder"] == r["trials"] for r in ex)
         and [r["disconnected_isolated_free_graphs"] for r in ex] == [0, 0, 3, 40]},
        {"name": "exponential formula holds mod (z_i^2) at n=3 and n=4; d^3 ln Xi|0 = phi^T_3",
         "passed": sy["n3_exponential_formula_remainder_mod_z_sq"] == "0"
         and sy["n4_exponential_formula_remainder_mod_z_sq"] == "0"
         and sy["n3_d3_logXi_at_0_minus_phi3"] == "0"
         and sy["n4_cluster_property_phi4_minus_connected_sum"] == "0"},
        {"name": "the 'restored alternation' equals the Mayer binding at negative activity",
         "passed": sy["n3_restored_minus_mayerBinding_at_negative_activity"] == "0"},
        {"name": "live word: tr(atom)/tr(free) = PROD mu_bond to 1e-40 at A=2,3,4",
         "passed": fw["ok_multiplicative"]},
        {"name": "A=3 chains: ln-binding 3-body cumulant is 0 to 1e-40 (canonical ensemble is pairwise)",
         "passed": fw["ok_log_pairwise"]},
        {"name": "A=3 chains: phi^T_3 > 0 and corpus b3 = -phi^T_3 < 0 (the Mayer sign)",
         "passed": fw["ok_sign"]},
        {"name": "every production interface letter has trace in (0,1): no attractive Mayer channel",
         "passed": fw["all_letters_below_one"]},
        {"name": "per-block chi ratios on 2H are NOT the bond factor: the identification is tr_M-only",
         "passed": fw["per_block_not_multiplicative"]},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The partition function whose Mayer expansion has the corpus b3 as its "
            "third Ursell coefficient is the hard-core lattice gas on the nucleon "
            "sites with pair weight mu_e = tr(interface letter), grand-canonical over "
            "the sub-clusters of a fixed nucleus: Xi_S(z) = SUM_T z^T PROD_{e in T} mu_e, "
            "ln Xi_S = SUM_T z^T phi^T_T. The corpus cumulants are Boolean-lattice "
            "inversions of 1 - Z and equal -phi^T_n exactly while n <= 3 (no disconnected "
            "isolated-vertex-free graph below 4 vertices); at n = 4 they differ by the 3 "
            "perfect matchings. The Mayer coefficients of B = -alpha ln(Xi/Xi_free) are "
            "-phi^T_T at every order, so the corpus's negative b3 IS the classical sign; "
            "the 2026-08-30 'restore (-1)^(n-1)' prescription is the same expansion at "
            "negative activity and names no ensemble. Fixed-A (canonical) binding "
            "-alpha ln Z_S is exactly pairwise. No production letter has trace > 1, so "
            "no attractive Mayer channel is present (scope a)."),
        "convention": "D (z = q^3/(q^2+1)), canonical per owner ruling R1 2026-08-15",
        "precision": {"exact_layer": "fractions.Fraction / sympy, no tolerance",
                      "framework_layer": f"gmpy2 MPFR {E.BITS} bits, tolerance 1e-40"},
        "exact": ex,
        "symbolic": sy,
        "framework": fw,
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(a) for the identification and the letter measurement; (b) for the sign: "
            "invariant = the Ursell alternation (-1)^(n-1) phi^T_n >= 0 on bond factors in "
            "(0,1), Lean QOU.MassTheory.UrsellPartitionFunctionB3.b3corpus_neg. Excludes a "
            "positive connected 3-body coefficient in the Mayer expansion of -ln Xi at "
            "positive activity for ANY bond triple in (0,1). Does not exclude an attractive "
            "channel (a letter with trace > 1) or a non-Mayer assembly."),
        "source": "Jansen & Kolesnikov, J. Stat. Phys. 189:33 (2022), library/s10955-022-02992-6/",
        "lean": "QOU/MassTheory/UrsellPartitionFunctionB3.lean",
        "bean": "qou-rwhv",
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python",
        q0_anchor="proton", q0_value=Q_50_DIGIT_STR,
        q0_anchor_reason="proton pin per owner directive 2026-08-07; every framework "
                         "number is evaluated at Q_50_DIGIT_STR")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "ursell-partition-function-for-b3.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
