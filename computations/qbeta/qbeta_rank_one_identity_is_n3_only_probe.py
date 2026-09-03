#!/usr/bin/env python3
"""
qbeta_rank_one_identity_is_n3_only_probe.py — SCOPE CORRECTION to my own result:
`net = tr_M^{z=1} - h*delta_{w_0}` holds at n = 3 and FAILS at n = 4.

# Ref: computations/qbeta/qbeta_net_as_trace_plus_longest_probe.py
# Ref: https://github.com/litlfred/qou/pull/5337#issuecomment-5371899738

WHY THIS EXISTS. `qbeta_net_as_trace_plus_longest_probe` established that the
coordinate sum and the Ocneanu trace at the trivial loop value differ by a single
rank-one term supported on the longest element, and stated it WITHOUT SAYING AT
WHICH n. Every use of it is at n = 3 — Delta lives in H_3(q) — so no downstream
conclusion moves. But the sentence as written reads as a characterisation of the
two functionals, and it is not one.

A sibling PR flagged exactly this failure mode on the same bean:

    "One trap: at n = 3, Xi coincides numerically with y_(3) (because
     chi^(2,1)(tau) = 0, y_(1^3) = 0, and [4]_Q = (1+Q)(1+Q^2)).
     Xi != y_(n) in general -- do not generalise the n=3 coincidence."
                                        -- PR #5337, 2026-08-21

That warning is about a different coincidence, and it applies to mine. I checked
rather than assumed, and the identity does not survive.

METHOD, and it is deliberately not the one the original probe used. The original
read the six H_3 trace values off the corpus's stated recursion. Here the trace
is SOLVED from its defining properties at each n — unital, cyclic, and the full
Markov property tr(x . T_{m-2} . y) = z * tr(x.y) for x,y in H_{m-1}, imposed at
EVERY level of the chain H_1 < H_2 < ... < H_n. Imposing it only at the top
generator leaves the system rank-deficient (rank 5 of 6 at n = 3), which is worth
recording: a partial Markov condition does not pin the Ocneanu trace.

MEASURED

    n = 3   system rank 6/6, unique     identity HOLDS, defect exactly -h
    n = 4   system rank 24/24, unique   identity FAILS

At n = 4 the difference `net - tr^{z=1}` is nonzero on ELEVEN of the twenty-four
basis elements, not one, taking four distinct values; and the trace at z = 1
itself takes five distinct values rather than being constant off w_0. So the
rank-one form is a low-rank accident of H_3, not a structural fact about the two
functionals.

WHAT SURVIVES, precisely. Every conclusion drawn from it stands, because every
one of them is evaluated on Delta, and Delta is an element of H_3(q):

  * eps(Delta) = tr_M^{z=1}(Delta), which follows from Delta having zero w_0
    coordinate -- a statement about Delta's SUPPORT, unaffected;
  * the phase as a transport within one family, 2*alpha(z) = tr_M^1(Delta) -
    tr_M^z(Delta);
  * the z-free floor net(dC) = -h * y_(2,1)(1).

WHAT DOES NOT. The claim that the two functionals differ by a single rank-one
term. That is now scoped to n = 3 wherever it appears.

NO fit, NO wiring. Exact symbolic in q and z. Scope-(a).
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

set_compute_dps(50)

q = sp.Symbol("q", positive=True)
h = q - 1 / q
Z = sp.Symbol("z")


def _compose(p, r, n):
    return tuple(p[r[i]] for i in range(n))


def _length(w, n):
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def _build(n):
    """Regular representation of H_n(q) from the Hecke and braid relations."""
    gens = []
    for g in range(n - 1):
        t = list(range(n))
        t[g], t[g + 1] = t[g + 1], t[g]
        gens.append(tuple(t))
    E = tuple(range(n))
    red = {E: ()}
    basis, frontier = [E], [E]
    while frontier:
        nf = []
        for w in frontier:
            for g, s in enumerate(gens):
                u = _compose(s, w, n)
                if u not in red:
                    red[u] = red[w] + (g,)
                    basis.append(u)
                    nf.append(u)
        frontier = nf
    basis.sort(key=lambda w: (_length(w, n), w))
    idx = {w: i for i, w in enumerate(basis)}
    N = len(basis)

    def Lgen(g):
        M = sp.zeros(N, N)
        for j, w in enumerate(basis):
            sw = _compose(gens[g], w, n)
            if _length(sw, n) > _length(w, n):
                M[idx[sw], j] += 1
            else:
                M[idx[w], j] += h
                M[idx[sw], j] += 1
        return M

    L = [Lgen(g) for g in range(n - 1)]
    ONE = sp.eye(N)

    def op(word):
        M = ONE
        for g in word:
            M = M * L[g]
        return M

    return basis, N, L, [op(red[w]) for w in basis]


def _solve_trace(n):
    """The Ocneanu trace, SOLVED from unital + cyclic + full Markov at every level."""
    basis, N, L, LEFT = _build(n)
    t = sp.symbols(f"t0:{N}")

    def bv(i):
        v = sp.zeros(N, 1)
        v[i] = 1
        return v

    def tr(vec):
        return sum(t[i] * vec[i] for i in range(N))

    eqs = [sp.Eq(t[0], 1)]
    for a in range(N):
        for b in range(a + 1, N):
            eqs.append(sp.Eq(tr(LEFT[a] * bv(b)), tr(LEFT[b] * bv(a))))
    for m in range(2, n + 1):
        subm = [i for i, w in enumerate(basis)
                if all(w[k] == k for k in range(m - 1, n))]
        for i in subm:
            for j in subm:
                eqs.append(sp.Eq(
                    sp.expand(tr(LEFT[i] * L[m - 2] * LEFT[j] * bv(0))),
                    sp.expand(Z * tr(LEFT[i] * LEFT[j] * bv(0)))))
    real = [sp.expand(e.lhs - e.rhs) for e in eqs if isinstance(e, sp.Equality)]
    A, b = sp.linear_eq_to_matrix(real, t)
    rank = A.rank()
    sol = sp.linsolve((A, b), t)
    tup = list(sol)[0]
    free = [x for x in tup if x.free_symbols & set(t)]
    w0 = max(range(N), key=lambda i: _length(basis[i], n))
    return basis, N, rank, len(free), [sp.simplify(v) for v in tup], w0


def main() -> int:
    w = WitnessBuilder("qbeta-rank-one-identity-n3-only", engine="sympy")
    w.set_description(
        "Scope correction: `net = tr_M^{z=1} - h*delta_{w_0}` holds at n=3 and "
        "fails at n=4, where the difference is nonzero on 11 of 24 basis "
        "elements. The rank-one form is an accident of H_3."
    )
    ok, notes, data = [], [], {}

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    for n in (3, 4):
        basis, N, rank, nfree, trv, w0 = _solve_trace(n)
        check(f"n{n}_ocneanu_trace_is_UNIQUELY_determined",
              rank == N and nfree == 0,
              f"(rank {rank}/{N}, {nfree} free — unital + cyclic + full Markov "
              "at every level of the chain)")
        at1 = [sp.simplify(v.subs(Z, 1)) for v in trv]
        diff = {i: sp.simplify(1 - at1[i]) for i in range(N)}   # net(T_w) = 1
        nz = {i: d for i, d in diff.items() if d != 0}
        vals = sorted({str(sp.factor(d)) for d in nz.values()})
        data[f"n{n}_dim"] = N
        data[f"n{n}_support_of_net_minus_trace"] = len(nz)
        data[f"n{n}_distinct_defect_values"] = vals
        data[f"n{n}_distinct_trace_values_at_z1"] = sorted(
            {str(sp.simplify(v)) for v in at1})
        rank_one = (list(nz) == [w0]) and sp.simplify(nz.get(w0, 0) + h) == 0
        data[f"n{n}_identity_holds"] = bool(rank_one)
        if n == 3:
            check("n3_identity_HOLDS_defect_is_exactly_minus_h", rank_one,
                  f"(supported on w_0 alone, defect {vals})")
        else:
            check("n4_identity_FAILS", not rank_one,
                  f"(nonzero on {len(nz)} of {N} basis elements, not 1; "
                  f"{len(vals)} distinct values)")
            check("n4_failure_is_BROAD_not_a_near_miss", len(nz) > N // 4,
                  f"({len(nz)}/{N} — so the rank-one form is not almost right)")
            check("n4_trace_at_z1_is_NOT_constant_off_w0",
                  len(data["n4_distinct_trace_values_at_z1"]) > 2,
                  f"({len(data['n4_distinct_trace_values_at_z1'])} distinct "
                  "values, vs 2 at n=3)")

    for k, v in data.items():
        w.add_data(k, v)
    w.add_data("markov_convention",
               "convention-free — no Markov parameter is specialised")
    w.add_data("assertion_notes", notes)

    verdict = (
        "`net = tr_M^{z=1} - h*delta_{w_0}` is an n = 3 fact, NOT a "
        "characterisation of the two functionals. At n = 4 the difference is "
        "nonzero on 11 of 24 basis elements with four distinct values, and the "
        "trace at z = 1 is not constant off w_0 either. Every conclusion drawn "
        "from the identity STANDS, because each is evaluated on Delta and Delta "
        "lives in H_3(q): eps(Delta) = tr_M^{z=1}(Delta) follows from Delta's "
        "SUPPORT; the phase is a transport within one family; the z-free floor "
        "is net(dC) = -h*y_(2,1)(1). What does not stand is the unscoped "
        "sentence, now corrected wherever it appears. Recorded rather than "
        "quietly patched: a sibling PR warned about generalising an n = 3 "
        "coincidence on this very bean, and I had done it. Also worth keeping: "
        "imposing the Markov property only at the top generator leaves the "
        "trace UNDERDETERMINED (rank 5 of 6 at n = 3)."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
