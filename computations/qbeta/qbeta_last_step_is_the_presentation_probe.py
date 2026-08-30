#!/usr/bin/env python3
"""
qbeta_last_step_is_the_presentation_probe.py — qou-xzrj: the final step does not
close, and it does not shrink into something new. It collapses back onto the
audit's own step-4 presentation choice.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_net_is_tau_against_all_ones_probe.py
# Ref: docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md

WHERE THIS PICKS UP. Six tranches derived every factor of the representation
except one identity: `commutator-part(Omega) = -dim(V_(2,1)) * dC`, where
Omega = sum_w T_w. This probe attacks that identity and reports three things,
TWO OF WHICH CUT AGAINST MY OWN EARLIER FRAMING.

## 1. A NAMING ERROR OF MINE, corrected here

I wrote `Omega_(2,1)` for what is actually Omega's COMMUTATOR part. They are not
the same: `chi^(2,1)(Omega) = 2q - 2/q = 2h`, which is NONZERO, so Omega's
(2,1)-component is not traceless and is strictly larger than its commutator
part. The identity was always between commutator parts and is unaffected; the
label was wrong and would have misled a later reader into expecting a
block-component statement.

## 2. THE ALIGNMENT IS MUCH WEAKER THAN I TREATED IT

I reported that `y0 ∥ dC` is "a real 2-condition constraint" and that Delta
"satisfies a real constraint". Measured: the set

    { x : commutator-part(x) is parallel to dC }

is a subspace of dimension 4 of 6 -- codimension 2, TWO THIRDS of the algebra.
So landing in it is not a coincidence worth remarking on, and the fact that w_0
also aligns is unsurprising rather than suggestive. I over-read this across
three tranches. The content was never the parallelism; it is the RATIO.

## 3. AND THE RATIO IS CONTINGENT ON DELTA'S PRESENTATION

The corpus builds Delta from typed-crossing words with a mixed crossing
`t = h/2` (step 4 of the fitting-finding audit, which the bean itself flags as
CHOSEN rather than derived). Varying only that parameter:

    t = h/2  (corpus)   parallel: YES    ratio = -2   = -dim(V_(2,1))
    t = h/3             parallel: NO
    t = h               parallel: NO
    t = 0               parallel: NO

At any other `t` the parallelism FAILS OUTRIGHT -- not merely a different ratio,
no proportionality at all. So `t = h/2` is what makes the entire pairing
representation exist, and the clean `-dim` is its signature.

## THE CONCLUSION, and it is a location rather than a closure

The last step is **not an independent gap**. Deriving
`commutator-part(Omega) = -dim * dC` is exactly as hard as deriving `t = h/2`,
which IS the step-4 presentation postulate. The chain of six tranches therefore
reduces step 8's postulate to step 4's, and does not eliminate it.

That is worth having -- a postulate reduced to an earlier, already-named one is
progress, and it says where to push -- but it is NOT a derivation of `net`, and
this file does not claim one. Scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

E = (0, 1, 2)
S0 = (1, 0, 2)
S1 = (0, 2, 1)


def compose(p, r):
    return tuple(p[r[i]] for i in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


BASIS = [E, S0, S1, compose(S0, S1), compose(S1, S0), compose(compose(S0, S1), S0)]
IDX = {w: i for i, w in enumerate(BASIS)}
N = 6


def main() -> int:
    q = sp.symbols("q", positive=True)
    h = q - 1 / q

    def left_gen(s):
        M = sp.zeros(N, N)
        for j, w in enumerate(BASIS):
            sw = compose(s, w)
            if length(sw) > length(w):
                M[IDX[sw], j] += 1
            else:
                M[IDX[w], j] += h
                M[IDX[sw], j] += 1
        return M

    L = [left_gen(S0), left_gen(S1)]
    ONE = sp.eye(N)
    REG = [ONE, L[0], L[1], L[0] * L[1], L[1] * L[0], L[0] * L[1] * L[0]]

    def bv(i):
        v = sp.zeros(N, 1)
        v[i] = 1
        return v

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi13(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i])
                               for i in range(N)))

    def chireg(v):
        return sp.simplify(sum(v[i] * sp.trace(REG[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((chireg(v) - chi3(v) - chi13(v)) / 2)

    comms = [REG[i] * bv(j) - REG[j] * bv(i) for i in range(N) for j in range(N)]
    cb = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * bv(i) - REG[i] * L[0] * bv(0)),
                           sp.simplify(L[1] * bv(i) - REG[i] * L[1] * bv(0)))
          for i in range(N)]
    ctr = sp.Matrix.hstack(*zc).nullspace()
    Pm = sp.Matrix.hstack(*(list(ctr) + list(cb)))
    Pinv = Pm.inv()

    def comm_part(v):
        c = Pinv * v
        return sp.simplify(sum((c[3 + k] * cb[k] for k in range(3)),
                               sp.zeros(N, 1)))

    def delta_at(t):
        p = sp.expand(L[0] * (L[1] - t * ONE) * bv(0))
        n = sp.expand((L[0] - t * ONE) * (L[1] - h * ONE) * bv(0))
        return sp.expand(n - p)

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 78)
    print(" qou-xzrj — the last step IS the step-4 presentation")
    print("=" * 78)

    allones = sp.Matrix([1] * N)
    Ocomm = comm_part(allones)
    dC = comm_part(delta_at(h / 2))

    # ---- 1. my naming error
    c21O = sp.simplify(chi21(allones))
    check("CORRECTION_Omega_2_1_component_is_NOT_traceless",
          sp.simplify(sp.together(c21O - 2 * h)) == 0 and c21O != 0,
          f"chi^(2,1)(Omega) = {sp.simplify(c21O)} = 2h, NONZERO. So what I "
          f"called `Omega_(2,1)` in the previous probe is Omega's COMMUTATOR "
          f"part, strictly smaller than its (2,1)-component. Identity "
          f"unaffected; the label was wrong")

    # ---- 2. the alignment is codimension 2, i.e. a 4-dim subspace
    cd = Pinv * dC
    dirn = [sp.simplify(cd[3]), sp.simplify(cd[4]), sp.simplify(cd[5])]
    xs = sp.symbols("x0:6")
    cx = Pinv * sp.Matrix(list(xs))
    conds = [sp.simplify(cx[3 + i] * dirn[j] - cx[3 + j] * dirn[i])
             for i, j in ((0, 1), (0, 2), (1, 2))]
    Ac, _ = sp.linear_eq_to_matrix([sp.Eq(c, 0) for c in conds], list(xs))
    dim_par = N - Ac.rank()
    check("DEFLATION_the_parallel_set_is_FOUR_of_six_dimensions",
          dim_par == 4,
          f"dim = {dim_par}/6, codim {Ac.rank()}. TWO THIRDS of the algebra has "
          f"its commutator part parallel to dC, so landing there is NOT a "
          f"coincidence. I over-read this across three tranches: the content "
          f"was never the parallelism, only the RATIO")

    # ---- 3. the ratio is presentation-contingent
    rows = []
    for lbl, tv in (("h/2 (corpus)", h / 2), ("h/3", h / 3),
                    ("h", h), ("0", sp.Integer(0))):
        d = comm_part(delta_at(tv))
        if all(sp.simplify(e) == 0 for e in d):
            rows.append((lbl, None, "dC = 0"))
            continue
        nz = next(i for i in range(N) if sp.simplify(d[i]) != 0)
        r = sp.simplify(sp.factor(Ocomm[nz] / d[nz]))
        par = all(sp.simplify(sp.together(Ocomm[i] - r * d[i])) == 0
                  for i in range(N))
        rows.append((lbl, par, sp.simplify(r)))
    print(f"\n    {'mixed crossing t':18s} {'parallel':>9s}   ratio")
    for lbl, par, r in rows:
        print(f"    {lbl:18s} {str(par):>9s}   {r}")

    corpus = rows[0]
    others = rows[1:]
    check("the_corpus_presentation_gives_parallel_and_ratio_minus_dim",
          corpus[1] is True and sp.simplify(corpus[2] + 2) == 0,
          "t = h/2 gives parallel with ratio exactly -2 = -dim(V_(2,1))")
    check("EVERY_OTHER_PRESENTATION_FAILS_PARALLELISM_OUTRIGHT",
          all(o[1] is not True for o in others),
          "not merely a different ratio -- no proportionality at all. So "
          "t = h/2 is what makes the whole pairing representation EXIST, and "
          "the clean -dim is its signature")

    print("\n  CONCLUSION: the last step is NOT an independent gap. Deriving")
    print("  comm(Omega) = -dim * dC is exactly as hard as deriving t = h/2,")
    print("  which IS the step-4 presentation postulate. Six tranches reduce")
    print("  step 8's postulate to step 4's; they do not eliminate it.")

    wb = WitnessBuilder("qbeta-last-step-is-the-presentation", engine="sympy")
    wb.set_description(
        "qou-xzrj: the final identity comm(Omega) = -dim*dC does not close and "
        "does not shrink -- it collapses onto the audit's step-4 presentation "
        "choice t = h/2. Varying only that parameter destroys the parallelism "
        "outright (h/3, h, 0 all fail), so t = h/2 is what makes the pairing "
        "representation exist. Also corrects two of my own earlier claims: "
        "chi^(2,1)(Omega) = 2h is nonzero so `Omega_(2,1)` was a mislabel for "
        "its commutator part; and the parallel set is a 4-of-6 dimensional "
        "subspace, so the alignment is far weaker than I reported. Scope-(a).")
    wb.add_data("chi21_Omega", str(sp.simplify(c21O)))
    wb.add_data("parallel_subspace_dim", str(dim_par))
    wb.add_data("ratio_at_corpus_presentation", str(corpus[2]))
    wb.add_data("presentations_tested",
                [f"{l}:parallel={p}" for l, p, _ in rows])
    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
