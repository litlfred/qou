#!/usr/bin/env python3
"""A general-n Ocneanu/Markov trace, validated against the corpus's hand-coded
H_3 vector -- and the four-strand gamma-gamma trace set it makes measurable.

## Why this probe exists

`qbeta_gamma_gamma_submonoid_h4_probe` (PR #7295) established that the
three-strand collapse is an accident of three strands: on four strands the
gamma-gamma submonoid is free (2^k distinct elements at k vertices) and spans
21 of `H_4`'s 24 dimensions. It deliberately computed no trace, so it could say
nothing about whether any of those elements reproduces an observable, and it
said so.

That missing piece is the trace. `pyhecke.gram` carries the `H_3` vector
`TR = [1, z, z, z^2, z^2, z(hz+1)]` as a literal, and there is no general-`n`
twin anywhere in the corpus. This file builds one.

## The recursion

The Ocneanu trace is the family of functionals fixed by three properties:
`tr(1) = 1`, `tr(xy) = tr(yx)`, and the Markov property `tr_n(x T_{n-2}) =
z * tr_{n-1}(x)` for `x` in `H_{n-1}`. Those determine it, via the coset
decomposition `S_n = union_j S_{n-1} * c_j` with
`c_j = s_{n-2} s_{n-3} ... s_j` and additive lengths:

    w in S_{n-1}            ->  tr_n(T_w) = tr_{n-1}(T_w)
    w = u * c_j,  j < n-1   ->  T_w = T_u * T_{s_{n-2}} * T_b  with
                                b = s_{n-3} ... s_j in S_{n-1}, so by
                                cyclicity and the Markov property
                                tr_n(T_w) = z * tr_{n-1}(T_b * T_u)

where `T_b * T_u` is a product IN `H_{n-1}` and needs the reducer, not a table.

## Why this may be believed

Three self-tests, each of which the recursion could fail:

  * **CHECK 1** reproduces `pyhecke.gram.TR_M` -- the corpus's own hand-coded
    `H_3` vector -- exactly, symbolically in `(h, z)`, all six slots. Nothing
    else in this file is trustworthy without it.
  * **CHECK 2** is the trace property `tr(xy) = tr(yx)` on `H_4` pairs. It is
    not an input to the recursion; if the coset bookkeeping were wrong this is
    where it would show.
  * **CHECK 3** is the Markov property at `n = 4` against `n = 3`, on every
    `H_3` basis element.

## What is then measured

The four-strand gamma-gamma trace set at the convention-D parameter
`z_D = q^3/(q^2+1)`, proton pin: its range, and how densely it covers that
range. The `H_3` half of this was measured in the sibling probe and is carried
here as a control.

## 🛑 Scope, and one thing this does NOT do

**No four-strand Q_beta prediction is made, and none should be read out of
this.** `Q_beta = |eps(Delta)| * E_0` is an `H_3` construction: `E_0` and the
element-to-observable map are both three-strand objects, and nothing in the
corpus says what the four-strand analogue is. What the trace set is compared
against here is **itself at n = 3**, structurally -- not against a measured
value.

The substantive finding is an anti-fit one and it points the same way as the
sibling: the richer the gamma-gamma set becomes, the LESS a residual match can
mean. At `n = 3` the difference grid already straddled `Q_beta` with a spacing
of 1.29 %; at `n = 4` the set is larger by orders of magnitude. Selection by
residual was already forbidden and is now not even tempting.

Scope-(a). Selects nothing, wires nothing, moves no number in the corpus.
"""

from __future__ import annotations

import functools
import importlib.util
import itertools
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "computations/qbeta",
           "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

_SRC = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_gamma_gamma_submonoid_h4_probe.py")
_spec = importlib.util.spec_from_file_location("_h4", _SRC)
_h4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_h4)

# The reducer and the gamma-gamma enumeration come from the sibling probe,
# whose CHECK 1 validates the reducer against `pyhecke.gram.hm`. Re-transcribing
# either would put a second copy of the Hecke relations in the tree.
h = _h4.h
perms = _h4.perms
word_to_vec = _h4.word_to_vec
right_mul_gen = _h4.right_mul_gen
gg_words = _h4.gg_words

set_compute_dps(60)

ZERO, ONE = sp.Integer(0), sp.Integer(1)
z = sp.Symbol("z")

Q0 = Q_MP
H0 = Q0 - 1 / Q0
ZD = Q0 ** 3 / (Q0 ** 2 + 1)

KMAX = 8

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


# ------------------------------------------------------------------- trace

def length(p) -> int:
    n = len(p)
    return sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])


def perm_of_word(word, n: int):
    """The permutation of a reduced word in the `s_i`, as one-line notation."""
    p = list(range(n))
    for i in word:
        p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def coset_factor(p, n: int):
    """Factor `w = u * c_j` with `u` in `S_{n-1}` and `c_j = s_{n-2}...s_j`,
    lengths additive. Returns `(u, j)`; `j = n-1` means `c_j` is empty and `w`
    already lies in `S_{n-1}`.

    🛑 The index is SEARCHED and both conditions are checked, not read off
    `p[n-1]`. The first version of this function did read it off, on the
    plausible-sounding ground that `c_j` moves the last position to `j` -- it
    does not, because `(u * c_j)(n-1) = u(c_j(n-1))` and `u` moves it again.
    That version asserted its way out on the very first `S_3` element it was
    given, `(2,0,1)`, whose true index is `0` and whose read-off index is `1`.
    The search is `O(n)` and cannot be wrong in a way the assertions miss.
    """
    lw = length(p)
    for j in range(n - 1, -1, -1):
        q_ = list(p)
        if j < n - 1:
            # right-multiply by c_j^{-1} = s_j s_{j+1} ... s_{n-2}
            for i in range(j, n - 1):
                q_[i], q_[i + 1] = q_[i + 1], q_[i]
        u = tuple(q_)
        if u[n - 1] != n - 1:
            continue
        lc = 0 if j == n - 1 else n - 1 - j
        if length(u) + lc == lw:
            return u[:n - 1], j
    raise AssertionError(f"no coset factorisation for {p} in S_{n}")


def _mul(vec_a: dict, p_b, n: int, hv):
    """Right-multiply a vector by the basis element `T_{p_b}`, via a reduced
    word for `p_b` (bubble sort gives one)."""
    word = []
    cur = list(p_b)
    # reduced word for p_b: repeatedly move the largest out of place
    for _ in range(length(p_b)):
        for i in range(n - 1):
            if cur[i] > cur[i + 1]:
                cur[i], cur[i + 1] = cur[i + 1], cur[i]
                word.append(i)
                break
    out = dict(vec_a)
    for i in reversed(word):
        out = right_mul_gen(out, i, n, {}, hv)
    return out


@functools.lru_cache(maxsize=None)
def _tr_basis(p, n: int, hv_key: str, zv_key: str):
    """`tr_n(T_p)`. Keys are strings so the cache is hashable; the values are
    re-parsed, which is safe because they are sympy-free numerics or the two
    module symbols."""
    hv = sp.sympify(hv_key)
    zv = sp.sympify(zv_key)
    if n == 1:
        return ONE
    u, j = coset_factor(p, n)
    if j == n - 1:
        return _tr_basis(u, n - 1, hv_key, zv_key)
    # b = s_{n-3} ... s_j  (empty when j = n-2), an element of S_{n-1}
    bword = list(range(n - 3, j - 1, -1)) if j <= n - 3 else []
    pb = perm_of_word(bword, n - 1)
    # T_b * T_u, reduced in H_{n-1}
    vec = {pb: ONE}
    vec = _mul(vec, u, n - 1, hv)
    acc = ZERO
    for pp, c in vec.items():
        acc += c * _tr_basis(pp, n - 1, hv_key, zv_key)
    return sp.expand(zv * acc)


def tr(vec: dict, n: int, hv=h, zv=z):
    hk, zk = sp.srepr(sp.sympify(hv)), sp.srepr(sp.sympify(zv))
    return sp.expand(sum(c * _tr_basis(p, n, hk, zk) for p, c in vec.items()))


def main() -> int:
    w = WitnessBuilder("qbeta-ocneanu-trace-general-n")
    w.set_description(
        "A general-n Ocneanu/Markov trace built from tr(1)=1, tr(xy)=tr(yx) "
        "and the Markov property, via the S_{n-1}-coset decomposition. "
        "Validated three ways: it reproduces pyhecke.gram's hand-coded H_3 "
        "vector [1,z,z,z^2,z^2,z(hz+1)] symbolically, it satisfies the trace "
        "property on H_4 pairs, and it satisfies the Markov property at n=4 "
        "against n=3. Then measures the four-strand gamma-gamma trace set at "
        "z_D, proton pin, with n=3 as control. Scope-(a): NO four-strand "
        "Q_beta prediction is made -- E_0 and the element-to-observable map "
        "are H_3 constructions and the corpus does not define their n=4 "
        "analogue."
    )

    print("Assertions:")

    # ---------------------------------------------------------------- CHECK 1
    # Against the corpus's own H_3 vector. Nothing below is trustworthy without
    # this, and it is symbolic in BOTH h and z.
    B3 = perms(3)
    NAMES3 = [(), (0,), (1,), (1, 0), (0, 1), (0, 1, 0)]
    TR_REF = [ONE, z, z, z ** 2, z ** 2, z * (h * z + 1)]
    mine, bad = [], []
    for slot, wrd in enumerate(NAMES3):
        p = perm_of_word(wrd, 3)
        v = tr({p: ONE}, 3)
        mine.append(v)
        if sp.simplify(v - TR_REF[slot]) != 0:
            bad.append((wrd, v, TR_REF[slot]))
    check("reproduces_the_corpus_h3_trace_vector", not bad,
          f"all six slots of pyhecke.gram's TR_M, symbolic in (h, z): "
          f"{[str(x) for x in mine]}; mismatches: {bad or 'none'}", w)

    # ---------------------------------------------------------------- CHECK 2
    # The trace property. NOT an input to the recursion -- a genuine test.
    B4 = perms(4)
    pairs = [(B4[3], B4[9]), (B4[5], B4[17]), (B4[11], B4[22]),
             (B4[7], B4[13]), (B4[19], B4[23]), (B4[1], B4[20])]
    bad2 = []
    for pa, pb in pairs:
        xy = _mul({pa: ONE}, pb, 4, h)
        yx = _mul({pb: ONE}, pa, 4, h)
        if sp.simplify(tr(xy, 4) - tr(yx, 4)) != 0:
            bad2.append((pa, pb))
    check("trace_property_holds_on_h4_pairs", not bad2,
          f"tr(xy) = tr(yx) on {len(pairs)} pairs of H_4 basis elements, "
          f"symbolic in (h, z). This is not an input to the recursion -- a "
          f"coset-bookkeeping error would surface here. Failures: "
          f"{bad2 or 'none'}", w)

    # ---------------------------------------------------------------- CHECK 3
    # The Markov property, n=4 against n=3, on every H_3 basis element.
    bad3 = []
    for p3 in B3:
        p4 = tuple(list(p3) + [3])
        x_t2 = right_mul_gen({p4: ONE}, 2, 4, {}, h)
        lhs = tr(x_t2, 4)
        rhs = sp.expand(z * tr({p3: ONE}, 3))
        if sp.simplify(lhs - rhs) != 0:
            bad3.append((p3, lhs, rhs))
    check("markov_property_n4_against_n3", not bad3,
          f"tr_4(x * T_2) = z * tr_3(x) on all {len(B3)} H_3 basis elements, "
          f"symbolic in (h, z). Failures: {bad3 or 'none'}", w)

    # ------------------------------------------------------- the trace sets
    def gg_traces(n: int):
        vals, seen = [], set()
        for k in range(KMAX + 1):
            for _combo, letters in gg_words(n, k):
                lets = [(i, sp.sympify(d).subs(h, sp.Rational(str(H0))))
                        for i, d in letters]
                vec = word_to_vec(lets, n, {}, sp.Rational(str(H0)))
                key = tuple(sorted((p, str(c)) for p, c in vec.items()))
                if key in seen:
                    continue
                seen.add(key)
                t = tr(vec, n, sp.Rational(str(H0)), sp.Rational(str(ZD)))
                vals.append(mp.mpf(str(sp.N(t, 40))))
        return vals

    T3 = gg_traces(3)
    T4 = gg_traces(4)

    # ---------------------------------------------------------------- CHECK 4
    # The four-strand set is vastly larger and its range is wider.
    check("four_strand_trace_set_is_larger_and_wider",
          len(T4) > len(T3) and (max(T4) - min(T4)) > (max(T3) - min(T3)),
          f"n = 3: {len(T3)} traces in "
          f"[{mp.nstr(min(T3), 8)}, {mp.nstr(max(T3), 8)}]; "
          f"n = 4: {len(T4)} traces in "
          f"[{mp.nstr(min(T4), 8)}, {mp.nstr(max(T4), 8)}] "
          f"(k <= {KMAX} vertices, z_D at the proton pin)", w)

    # ---------------------------------------------------------------- CHECK 5
    # The anti-fit consequence: the median gap between consecutive traces.
    def median_gap(vals):
        s = sorted(set(vals))
        if len(s) < 3:
            return None
        gaps = sorted(s[i + 1] - s[i] for i in range(len(s) - 1))
        return gaps[len(gaps) // 2]
    g3, g4 = median_gap(T3), median_gap(T4)
    check("four_strand_set_is_denser_so_a_residual_match_means_less",
          g4 is not None and g3 is not None and g4 < g3,
          f"median gap between consecutive distinct traces: "
          f"n = 3 {mp.nstr(g3, 8)}, n = 4 {mp.nstr(g4, 8)} -- a factor "
          f"{mp.nstr(g3 / g4, 6)} denser. Selection by residual was already "
          f"forbidden at n = 3 (the difference grid straddled Q_beta with a "
          f"1.29 % spacing); at n = 4 it is not even tempting", w)

    # ------------------------------------------------------------------ data
    w.add_data("h3_trace_vector_symbolic", [str(x) for x in mine])
    w.add_data("recursion",
               "w in S_{n-1} -> tr_{n-1}(T_w); else w = u*c_j with "
               "c_j = s_{n-2}...s_j, and tr_n(T_w) = z * tr_{n-1}(T_b * T_u) "
               "with b = s_{n-3}...s_j, by cyclicity + the Markov property")
    for n, T in ((3, T3), (4, T4)):
        w.add_data(f"gamma_gamma_traces_n_{n}", {
            "count": len(T),
            "min": mp.nstr(min(T), 20), "max": mp.nstr(max(T), 20),
            "median_gap": mp.nstr(median_gap(T), 20),
            "k_max_vertices": KMAX})
    w.add_data("scope", "a")
    w.add_data("what_this_does_not_do", [
        "no four-strand Q_beta prediction -- E_0 and the "
        "element-to-observable map are H_3 constructions and the corpus does "
        "not define their n = 4 analogue",
        "the n = 4 trace set is compared to ITSELF at n = 3, structurally, "
        "never against a measured value",
        "growth beyond k = " + str(KMAX) + " vertices",
    ])
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("z_convention", "D, z_D = q^3/(q^2+1)")

    print()
    print(f"  H_3 trace vector: {[str(x) for x in mine]}")
    for n, T in ((3, T3), (4, T4)):
        print(f"  n = {n}: {len(T)} gamma-gamma traces in "
              f"[{mp.nstr(min(T), 8)}, {mp.nstr(max(T), 8)}], median gap "
              f"{mp.nstr(median_gap(T), 8)}")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
