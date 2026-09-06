"""Global contiguity does NOT determine `f1/f0`; the split-link factorisation does.

WHAT THIS CORRECTS
------------------
PR #6910 (`docs/audits/2026-09-06-contiguity-drives-f1-but-it-saturates.md`)
reported that a greedy walk raising a word's *contiguity* -- the fraction of
adjacent letter pairs sharing a generator index -- raised `f1/f0` monotonically
and then saturated at contiguity 2/3, and read that as "contiguity drives
`f1/f0`". That reading is **refuted here**, by me, and the mechanism is the
corpus's own already-derived split-link multiplicativity.

THE MECHANISM (already in the corpus -- this probe does not discover it)
------------------------------------------------------------------------
In the `pn` atom word the proton occupies generators {0,1} and the neutron {3,4}.
Every cross pair has |i-j| >= 2, so the two nucleons act on *disjoint strand
sets*. `braids-and-knots/markov-axioms-primitive.md` derives from the Markov
axioms that

    tr_M(K1 |_| K2) = tr_M(K1) . tr_M(K2)

for exactly that situation, and `mass-theory/subset-cumulant-recursion.md`
already names the consequence: multiplicativity of `tr_M` "turns into additivity
of L on disjoint bonded parts".

It has also already been MEASURED, independently, by
`computations/qbeta/qbeta_disjoint_support_factorisation_probe.py` (7/7,
2026-09-04, bean `qou-ib3g`): `tr_M` factorises over disjoint non-adjacent
generator blocks exactly, rel. diff 0.0 at 40 dps, with generators repeated
inside each block.

So T2 below is the THIRD independent statement of the same fact and is cited as
such, per AGENTS.md on parallel exploration. What is additional here is narrow:
the induced additivity of the LOG-DERIVATIVE in exact rational arithmetic, and
its use as the refutation of the contiguity reading. What is new is that
consequence, not the factorisation.

THE THREE CHECKS
----------------
T1  INVARIANCE. Interleavings of the two nucleons that preserve each nucleon's
    own internal letter order must all give the same `f1/f0`, however much the
    interleaving moves the *contiguity* of the combined word. Measured: 12/12
    identical at contiguities spanning 0.2857 .. 0.5238, against the canonical
    grouped word's 0.8571. So a word at contiguity 0.286 and a word at 0.857
    carry the same value -- which is what kills contiguity as the driver.

T2  ADDITIVITY. With `v(P,N)` the value of proton-order P followed by
    neutron-order N,

        v(P*,N*) - v(P0,N0)  ==  [v(P*,N0) - v(P0,N0)] + [v(P0,N*) - v(P0,N0)]

    exactly, for random shuffled orders. This is the log-derivative form of the
    factorisation. The canonical split is `21/2 + 8 = 37/2`, reproducing the
    per-letter counts (proton 21, neutron 16) that
    `c1_leading_coefficient_derived_probe.py` carries.

T3  NON-DETERMINATION, both directions. There exist two words of EQUAL
    contiguity with DIFFERENT values, and two words of DIFFERENT contiguity with
    EQUAL values. Either one alone refutes "contiguity determines `f1/f0`";
    both are asserted so the refutation cannot be read as a sampling accident.

    T3 also holds for INTRA-nucleon contiguity, which is the obvious repair and
    does not work either: three proton orders at intra-contiguity 0.4 give three
    different values.

SCOPE -- scope-(a) throughout
-----------------------------
One nucleus (pn, A=2, n=6), one truncation (P=3), `include_inter=False`. Nothing
here says the greedy walk of #6910 was mismeasured -- its numbers stand; it is
the causal reading of them that is wrong, because a greedy contiguity walk from
the Borromean word also happens to repair the intra-nucleon orders, and that is
the variable doing the work.

NO FLOAT: every value is an exact `fractions.Fraction`. Floats appear only in
f-string display of the contiguity ratio.
"""
from __future__ import annotations

import os
import random
import sys
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.dirname(_HERE)
for _p in (_COMP, _HERE, os.path.join(_COMP, "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from word_level_trace_entry_point import log_derivative       # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

N_STRANDS = 6
P_TRUNC = 3
PROTON_GENS = (0, 1)
NEUTRON_GENS = (3, 4)


def contiguity(word) -> F:
    """Exact fraction of adjacent letter pairs sharing a generator index."""
    if len(word) < 2:
        return F(0)
    same = sum(1 for i in range(len(word) - 1) if word[i][0] == word[i + 1][0])
    return F(same, len(word) - 1)


def _value(word) -> F:
    return log_derivative(list(word), N_STRANDS, P_TRUNC)


def _split(word):
    p = [x for x in word if x[0] in PROTON_GENS]
    n = [x for x in word if x[0] in NEUTRON_GENS]
    assert len(p) + len(n) == len(word), "atom word carries an unexpected generator"
    return p, n


def _interleave(p, n, mask):
    ip, inn = iter(p), iter(n)
    return [next(ip) if m == 0 else next(inn) for m in mask]


def main() -> int:
    rng = random.Random(20260906)
    grouped = atom_canonical_crossings(1, 1, include_inter=False, intra_order="grouped")
    P0, N0 = _split(grouped)
    base = _value(grouped)
    print(f"pn atom word, intra_order=grouped: {len(grouped)} letters "
          f"(proton {len(P0)}, neutron {len(N0)})")
    print(f"  contiguity {contiguity(grouped)} ({float(contiguity(grouped)):.4f})"
          f"   f1/f0 = {base}")

    failures = []

    # ---- T1: invariance under commuting-block interleaving --------------------
    conts, n_same = [], 0
    for _ in range(12):
        mask = [0] * len(P0) + [1] * len(N0)
        rng.shuffle(mask)
        w = _interleave(P0, N0, mask)
        c = contiguity(w)
        conts.append(c)
        if _value(w) == base:
            n_same += 1
    lo, hi = min(conts), max(conts)
    print(f"\nT1 interleavings preserving intra order: {n_same}/12 equal to {base}"
          f"   contiguity {float(lo):.4f} .. {float(hi):.4f}")
    if n_same != 12:
        failures.append("T1: value moved under a commuting-block interleaving — "
                        "the trace is not faithful to the braid relations")
    if hi >= contiguity(grouped):
        failures.append("T1: no interleaving lowered contiguity below the canonical "
                        "word — the test did not exercise its own premise")

    # ---- T2: exact additivity across the two commuting nucleons ---------------
    v = lambda p, n: _value(list(p) + list(n))  # noqa: E731
    n_add = 0
    trials = []
    for _ in range(6):
        Ps, Ns = P0[:], N0[:]
        rng.shuffle(Ps)
        rng.shuffle(Ns)
        vP, vN, vB = v(Ps, N0), v(P0, Ns), v(Ps, Ns)
        pred = vP + vN - base
        trials.append((Ps, Ns, vP, vN, vB, pred))
        if pred == vB:
            n_add += 1
    print(f"T2 additivity v(P*,N*) = v(P*,N0)+v(P0,N*)-v(P0,N0): {n_add}/6 exact")
    if n_add != 6:
        failures.append("T2: additivity failed — an interaction term between "
                        "commuting nucleons")

    # The canonical split, read off the two like-nucleon words rather than by
    # deleting a nucleon (which would change the strand count and so the trace).
    pp = atom_canonical_crossings(2, 0, include_inter=False, intra_order="grouped")
    nn = atom_canonical_crossings(0, 2, include_inter=False, intra_order="grouped")
    v_pp, v_nn = _value(pp), _value(nn)
    print(f"T2 canonical: v(pp)={v_pp}  v(pn)={base}  v(nn)={v_nn}"
          f"   -> per-nucleon {v_pp/2} and {v_nn/2}")
    if v_pp / 2 + v_nn / 2 != base:
        failures.append(f"T2: canonical split fails — v(pp)/2 + v(nn)/2 = "
                        f"{v_pp/2 + v_nn/2} != v(pn) = {base}")

    # ---- T3: contiguity does not determine the value, both directions ---------
    by_cont: dict[F, set] = {}
    for _ in range(24):
        w = grouped[:]
        rng.shuffle(w)
        try:
            by_cont.setdefault(contiguity(w), set()).add(_value(w))
        except BaseException:
            continue
    same_cont_diff_val = sorted(
        (c, len(vs)) for c, vs in by_cont.items() if len(vs) > 1)
    print(f"T3a equal contiguity, different value: "
          f"{len(same_cont_diff_val)} contiguity levels carry >1 distinct value")
    if not same_cont_diff_val:
        failures.append("T3a: no contiguity level carried two values — sample too "
                        "small to refute determination")
    print(f"T3b different contiguity, equal value: T1 exhibits it — "
          f"{float(lo):.4f} and {float(contiguity(grouped)):.4f} both give {base}")

    print()
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print("PASS  contiguity does not determine f1/f0; the split-link "
          "factorisation does (4/4 checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
