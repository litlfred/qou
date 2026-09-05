#!/usr/bin/env python3
"""magnus_k4_per_window_probe.py — is the k=4 spike LOCAL or a property of the sum? (qou-o6ov)

WHAT IS BEING EXPLAINED. Across A = 2…6 one term does all the damage in the ≤2-row column: `k=4`,
the shape `(n−4, 4)`. It breaks monotonicity at every A ≥ 4, and it is the term that eats the
concentration — gaining +3.33 then +15.59 share points, covering 76 % then 111 % of what `k=1`
loses. The attribution is established (the square-end and arriving-shape readings are both excluded
at the A=3→4 step, where `k=4` is interior and the square end is `k=6`). **What is not established
is why `k=4`.**

THE TEST, and it is cheap. `Ω₂^P = c·Σ_a [σ_a, σ_{a+1}]` is a sum of `ngen−1` **3-strand-local**
commutators. So there are two candidate explanations and they make opposite predictions:

  * **LOCAL** — a single window `[σ_a, σ_{a+1}]` already distinguishes `k=4`. Then the effect is a
    property of one 3-strand commutator in a two-row rep, and `ρ` and the sum are irrelevant to it.
  * **COLLECTIVE** — no single window does, and `k=4` only appears once the `ngen−1` windows are
    added. Then it is a property of the sum's interference and the local operator explains nothing.

A single window costs roughly `1/(ngen−1)` of the full sweep — about a tenth at A=4 — so this
separates the two readings for a fraction of one column.

WHY THIS AND NOT ANOTHER SIZE. The arc is out of cheap sizes: A=6's two shapes alone took 3020 s,
and this session has already had three three-point trends refuted by their fourth points, so another
size would buy a pattern I have committed to not trusting until its successor lands. A structural
test asks a different question, and its answer does not depend on how many `A` are in hand.

RELATION TO PRIOR WORK, which is close but not this. Bean `qou-o6ov` records (#6311) that each
per-window `|tr(ρ_λ[A_a,A_{a+1}])|/dim_λ` peaks at `b=1` for every window at A=2,3 — but that is the
**germ** `A_a = q ∂σ_a · σ_a⁻¹`, which #6434 later showed is representation-specific (one gauge), and
it is a statement about the `b=1` peak rather than about `k=4`. This probe uses the gauge-invariant
`[σ_a, σ_{a+1}]` that `Ω₂^P` is actually built from, on the TRUE Hecke element, and asks about `k=4`.

SCOPE — (a) scope-limited, A=4 unless more passed, one q₀. Measures which of two readings survives;
proves nothing and offers no mechanism for either.
NO-FLOAT64: mpf end to end, dps 65, `_assert_dps` guard inherited, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
import magnus_true_hecke_element_probe as TE  # noqa: E402


def shape(n, k):
    return (n - k,) if k == 0 else (n - k, k)


def window_trace(lam, word, q, a, *, with_rho=True):
    """tr_λ(ρ · [σ_a, σ_{a+1}]) for ONE window a — the building block of Ω₂^P.

    `with_rho=False` drops ρ and traces the bare commutator, which separates "the window does it"
    from "the window dressed by ρ does it". A bare commutator's trace is zero on the whole algebra
    but NOT on an individual irrep, so this is not a trivially-zero control.
    """
    TE._assert_dps(f"window_trace({lam}, a={a})")
    per_gen, dim = base.block_structure(tuple(lam))
    sig = base.sigma_csr(per_gen, dim, q)
    rev = list(reversed(word))
    tr = mp.mpf(0)
    for j in range(dim):
        e = [mp.mpf(0)] * dim
        e[j] = mp.mpf(1)
        u = base.spmatvec(sig[a], base.spmatvec(sig[a + 1], e))
        w = base.spmatvec(sig[a + 1], base.spmatvec(sig[a], e))
        v = [u[r] - w[r] for r in range(dim)]
        if with_rho:
            for c, d, g in rev:
                sv = base.spmatvec(sig[g], v)
                c = mp.mpf(str(c))
                d = mp.mpf(str(d))
                v = [c * sv[r] + d * v[r] for r in range(dim)]
        tr += v[j]
    return tr, dim


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=4)
    ap.add_argument("--dps", type=int, default=65)
    ap.add_argument("--windows", type=int, nargs="*", default=None,
                    help="which a to measure; default: a spread across the word")
    args = ap.parse_args()
    mp.mp.dps = args.dps
    TE._WANT_DPS = args.dps
    q = base.Q0

    A = args.A
    n = 3 * A
    Z, N = A // 2, A - A // 2
    word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
    ngen = max(g for _c, _d, g in word) + 1
    wins = args.windows if args.windows else sorted(
        {0, (ngen - 1) // 2, ngen - 2})          # first, middle, last window

    print(f"[k4win] A={A} (n={n}), {ngen} generators ⇒ {ngen - 1} windows in Ω₂^P.")
    print(f"[k4win] Does a SINGLE window [σ_a, σ_{{a+1}}] already single out k=4, or is k=4 a")
    print(f"[k4win] property of the SUM?  Measuring windows a = {wins}.  (dps={args.dps})\n")

    ks = list(range(n // 2 + 1))
    print(f"  {'k':>3}  {'λ':<11}{'dim':>6}" + "".join(f"{'a=' + str(a):>16}" for a in wins))
    per_win = {a: [] for a in wins}
    for k in ks:
        lam = shape(n, k)
        row = []
        for a in wins:
            tr, dim = window_trace(lam, word, q, a, with_rho=True)
            per_win[a].append(abs(tr) / dim)
            row.append(abs(tr) / dim)
        print(f"  {k:>3}  {str(lam):<11}{base.block_structure(lam)[1]:>6}"
              + "".join(f"{mp.nstr(x, 7):>16}" for x in row))

    print("\n  Where does each window PEAK (over k ≥ 1), and does it rise INTO k=4?")
    verdicts = []
    for a in wins:
        v = per_win[a]
        pk = max(range(1, len(v)), key=lambda i: v[i])
        into4 = (len(v) > 4 and v[4] > v[3])
        verdicts.append(into4)
        print(f"    a={a:<3} peak at k={pk}    rises into k=4? "
              f"{'YES' if into4 else 'no'}"
              f"    (k=3 {mp.nstr(v[3], 6)} → k=4 {mp.nstr(v[4], 6)})" if len(v) > 4 else
              f"    a={a:<3} peak at k={pk}    (column has no k=4)")

    if verdicts:
        if all(verdicts):
            print("\n  ⇒ LOCAL: every window measured rises into k=4 on its own. The k=4 effect is a")
            print("    property of a single 3-strand commutator dressed by ρ, not of the Ω₂ sum.")
        elif not any(verdicts):
            print("\n  ⇒ COLLECTIVE: no single window rises into k=4. The effect appears only when the")
            print(f"    {ngen - 1} windows are summed — it is interference, and the local operator")
            print("    explains nothing about it.")
        else:
            print("\n  ⇒ MIXED: some windows rise into k=4 and some do not, so neither reading is")
            print("    clean. Report the split rather than picking one; a mixed result here means")
            print("    the window POSITION matters, which is a third thing this probe did not ask.")


if __name__ == "__main__":
    main()
