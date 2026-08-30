#!/usr/bin/env python3
"""The braid's inter-nucleon crossings form a PATH, not a coordination degree.

`content/.../mass-theory/bk-coordination-multiplicity.md` sets the open
many-body multiplicity to the **per-nucleon coordination number**
`z(A) = A - 1`, defined in its own words as *"the number of nucleon-nucleon
bonds incident to one nucleon in the fully coordinated cluster"* — the degree
of a vertex in the complete graph `K_A`. `QOU/Mass/CoordinationBinding.lean`
machine-checks exactly that:
`coordination_degree : (⊤ : SimpleGraph (Fin A)).degree v = A - 1`.

The canonical atomic braid `mass_at_3A_proper.atom_braid_word_3A` supplies the
integer `A - 1` too: toggling `include_inter` shows exactly `A - 1` letters
appear at inter-nucleon generators. It is tempting to read that as the braid
DERIVING the multiplicity. This probe measures what those crossings actually
connect, and the answer is that they do not.

## Two different objects — say which one is being measured

The block's `B_K` is the **building-block census link** (`8_11` for 3H, `L6a4`
for 3He), and `Vol_n(K)` is that link's hyperbolic volume. The object measured
here is the **3A-strand word** `atom_braid_word_3A`. They are not the same
thing, and the finding below is about the second one — which is what the
`include_inter` crossing count belongs to.

That distinction matters twice over, because `atom_braid_word_3A`'s own
docstring rules out reading a topological quantity off it at all: its averaged
letters lie outside the image of `rho : B_n -> H_n(q)`, so the word is a Hecke
element rather than a braid, `tr_M` of it is a weighted sum of `2^(2A+1)` link
invariants, and *"NO TOPOLOGICAL quantity may be read off it — not a volume,
not a crossing number, not a genus"*.

This probe does not read one. What it measures is which **strand pairs** each
letter acts on, i.e. the combinatorial incidence of the word's generators — a
fact about the word, well defined whether or not the word is a braid, and not
an invariant of any link. So the result stands, and it sharpens the verdict:
the integer `A - 1` is not merely the wrong *kind* of graph count, it is not a
"topological reading" of anything.

## Method — the adjacency is DERIVED, not read off the loop

`atom_braid_word_3A` builds its word from a hard-coded
`ordering = ['p']*Z + ['n']*N` and emits an inter letter at generator `3k+2`
for `k = 0 .. A-2`. Reading the bond set off that loop would only restate the
source. Instead the incidence here is derived from the generator index alone,
using the 3-quarks-per-nucleon strand layout:

    nucleon(strand s) = s // 3         each nucleon owns strands 3k, 3k+1, 3k+2
    sigma_g swaps strands g and g+1    (0-based, per the module's convention)
    => g is INTER iff g//3 != (g+1)//3  iff  g % 3 == 2,
       and it then joins nucleon g//3 to nucleon g//3 + 1.

So the bond multiset, the degree sequence and the graph diameter all fall out
of the word's generator indices, and would register a change to the ordering
convention rather than inheriting it.

Bond TYPE is bucketed by the letter's exact Hecke shift `d`, per the module's
own encoding (`d = 0` is sigma = p-p, `d = -h` is sigma^-1 = n-n, the
intermediate averaged value is the p-n interface). The three values are
compared by ORDER as exact `mpmath.mpf`, never through `float` — AGENTS.md
NO-FLOAT64 is explicit that probes are not exempt.

## The finding

    A                     2    3    4    6    8   12   16
    inter-crossings       1    2    3    5    7   11   15    = A - 1
    distinct bonds        1    2    3    5    7   11   15    = A - 1
    max nucleon degree    1    2    2    2    2    2    2    = min(2, A-1)
    K_A degree  (z)       1    2    3    5    7   11   15    = A - 1
    K_A edges  C(A,2)     1    3    6   15   28   66  120

The braid's inter-nucleon crossing set is the **path graph** `P_A`: `A - 1`
edges joining consecutive nucleons, every degree at most 2.

**The agreement is a coincidence of two different counts.** `|E(P_A)| = A - 1`
is an EDGE count of the braid's graph; `deg_{K_A}(v) = A - 1` is a VERTEX
DEGREE of the block's graph. They are the same affine function of `A`, so **no
value of `A` can ever separate them** — six matching rows are not evidence.
What separates them is arity: an extensive total is being read as an intensive
per-nucleon degree.

The discriminating observable is the pair `(edges, degree)`, which the
handshake identity ties together and which the two graphs answer differently.
The braid answers `(A-1, <=2)`; `K_A` answers `(C(A,2), A-1)`.

Measured, the two slots part company at different places, and the gap is wider
than it first looks:

* the **degree** slot agrees exactly for `A <= 3` — `min(2, A-1) = A-1` iff
  `A <= 3` — which is precisely the two-row table (3H, 3He) the block
  calibrates on. At `A = 4`, where the block's own table already needs an extra
  factor of 2.52, `K_A` wants degree 3 and the braid can offer at most 2.
* **both** slots agree only at `A = 2`, since `|E(P_3)| = 2` against
  `C(3,2) = 3`. `P_A = K_A` iff `A <= 2`: the deuteron is the *only* nucleus
  where the braid's bond set is the fully coordinated cluster.

(An earlier draft of this docstring claimed both slots agree for `A <= 3`; the
run disagreed, and the measurement is right. The corrected statement is
strictly stronger — the block's `A = 3` calibration rests on the degree
coincidence alone, with the edge count already wrong there by one bond.)

Verdict: **scope-(a)** — this construction does not derive the coordination
multiplicity. The braid's bond set is a path, and the linear-chain ansatz built
on it is separately excluded scope-(b) at `q != 1`
(`QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff`, bean
`qou-m07y`).

Beans: `qou-m07y` (chain exclusion), `qou-h7mh` (the bond set is the repair
site), `qou-v0yw` (derive the coordination graph).

@module computations/probes/braid_inter_nucleon_adjacency_probe
"""

from __future__ import annotations

import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

_COMP = Path(__file__).resolve().parent.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))

import _path_bridge  # noqa: F401,E402  (after the bootstrap — AGENTS.md qou-0e1t)
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

QUARKS_PER_NUCLEON = 3


def nucleon_of_strand(s: int) -> int:
    """Which nucleon owns strand `s`. Three quarks per nucleon, in order."""
    return s // QUARKS_PER_NUCLEON


def bond_of_generator(g: int):
    """The nucleon pair `sigma_g` joins, or `None` if `g` is intra-nucleon.

    `sigma_g` swaps strands `g` and `g+1` (0-based). Derived from the strand
    layout — NOT read off `atom_braid_word_3A`'s emission loop.
    """
    a, b = nucleon_of_strand(g), nucleon_of_strand(g + 1)
    return None if a == b else (a, b)


def inter_bond_multiset(Z: int, N: int) -> Counter:
    """The multiset of nucleon pairs the word's inter-nucleon letters join."""
    bonds: Counter = Counter()
    for _c, _d, g in atom_braid_word_3A(Z, N):
        pair = bond_of_generator(int(g))
        if pair is not None:
            bonds[pair] += 1
    return bonds


def _inter_templates():
    """The three inter-nucleon Hecke shifts, rebuilt exactly as the word does.

    `atom_braid_word_3A` forms them inside `workdps(max(mp.dps, 60))` from the
    50-digit `q0` string, so reproducing that context reproduces the values
    bit-for-bit and lets the buckets below be decided by EXACT equality.

    Ranking the three by order instead would be wrong: a nucleus whose ordering
    realises only two of the three types has no third value to rank against, and
    the minimum is then the wrong bucket. That bug labelled the deuteron's single
    p-n bond `nn` before it was caught.
    """
    from _li_2_q_util import flavor_split_leading
    from q_parameter import Q_50_DIGIT_STR as _Q50
    with mp.workdps(max(mp.mp.dps, 60)):
        q = mp.mpf(str(_Q50))
        h = q - mp.mpf(1) / q
        delta = flavor_split_leading(q)
        return {
            "pp": mp.mpf(0),                                  # sigma
            "nn": -h,                                         # sigma^-1
            "pn": -h * (mp.mpf(1) / 2 - delta / 4),           # colour-weighted
        }


def inter_bond_types(Z: int, N: int) -> dict:
    """Label each inter bond `pp` / `pn` / `nn` from its exact Hecke shift `d`.

    `sigma = (1, 0)` is the p-p interface, `sigma^-1 = (1, -h)` the n-n one, and
    the averaged `(1, -h*(1/2 - delta/4))` the colour-weighted p-n one. Matching
    is by exact `mpf` equality against the templates — no `float`, and an
    unmatched `d` RAISES rather than falling into a default bucket, so a
    precision mismatch fails loudly instead of mislabelling a bond.
    """
    templates = _inter_templates()
    out = {}
    for _c, d, g in atom_braid_word_3A(Z, N):
        pair = bond_of_generator(int(g))
        if pair is None:
            continue
        for name, tmpl in templates.items():
            if d == tmpl:
                out[pair] = name
                break
        else:
            raise ValueError(
                f"inter shift d={mp.nstr(d, 20)} at gen {g} for (Z,N)=({Z},{N}) "
                f"matches none of {{pp: 0, nn: -h, pn: -h(1/2-delta/4)}}"
            )
    return out


def degree_sequence(bonds: Counter, A: int) -> list:
    """Per-nucleon degree in the braid's inter graph (bonds, not letters)."""
    deg = [0] * A
    for (a, b) in bonds:
        deg[a] += 1
        deg[b] += 1
    return deg


def k_complete_degree(A: int) -> int:
    """`z(A) = A - 1`, the block's per-nucleon coordination number."""
    return A - 1


def k_complete_edges(A: int) -> int:
    """`C(A,2)`, the block's total bond count."""
    return A * (A - 1) // 2


def main() -> int:
    mp.mp.dps = 65
    # N = Z self-conjugate, plus the two A = 3 mirror nuclei the block uses.
    cases = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"),
             (3, 3, "6Li"), (4, 4, "8Be"), (6, 6, "12C"), (8, 8, "16O")]

    print(f"{'atom':>5} {'A':>3} {'letters':>8} {'bonds':>6} {'A-1':>5} "
          f"{'degrees':>16} {'maxdeg':>7} {'z=A-1':>6} {'C(A,2)':>7}")
    print("-" * 80)

    rows = []
    for Z, N, name in cases:
        A = Z + N
        bonds = inter_bond_multiset(Z, N)
        letters = sum(bonds.values())
        deg = degree_sequence(bonds, A)
        rows.append((name, A, letters, len(bonds), deg, bonds))
        print(f"{name:>5} {A:>3} {letters:>8} {len(bonds):>6} {A - 1:>5} "
              f"{str(deg):>16} {max(deg):>7} {k_complete_degree(A):>6} "
              f"{k_complete_edges(A):>7}")

    print()
    ok = True

    # 1. The braid's bond SET is exactly the path P_A.
    for name, A, letters, nbonds, deg, bonds in rows:
        if set(bonds) != {(k, k + 1) for k in range(A - 1)}:
            print(f"FAIL {name}: bond set {sorted(bonds)} is not the path P_{A}")
            ok = False
        if nbonds != A - 1:
            print(f"FAIL {name}: {nbonds} bonds, expected A-1 = {A - 1}")
            ok = False
        if letters != A - 1:
            print(f"FAIL {name}: {letters} inter letters, expected A-1 (m_*=1)")
            ok = False
    print("[1] braid inter-bond set is the path P_A, |E| = A-1 ......... "
          f"{'PASS' if ok else 'FAIL'}")

    # 2. The COINCIDENCE: |E(P_A)| == deg_{K_A}(v), identically in A.
    coincide = all(nb == k_complete_degree(A) for _n, A, _l, nb, _d, _b in rows)
    print("[2] |E(P_A)| == z(A) = deg_K_A for every A tested ........... "
          f"{'PASS' if coincide else 'FAIL'}  <- the coincidence")
    ok = ok and coincide

    # 3. The SEPARATION: max braid degree is min(2, A-1), != A-1 for A >= 4.
    sep = True
    for name, A, _l, _nb, deg, _b in rows:
        if max(deg) != min(2, A - 1):
            print(f"FAIL {name}: max degree {max(deg)} != min(2, A-1)")
            sep = False
        if A >= 4 and max(deg) == k_complete_degree(A):
            print(f"FAIL {name}: braid degree reaches z at A={A}; no separation")
            sep = False
    print("[3] max braid degree = min(2, A-1) < z(A) for all A >= 4 .... "
          f"{'PASS' if sep else 'FAIL'}  <- the separation")
    ok = ok and sep

    # 4a. The DEGREE slot alone agrees exactly for A <= 3.
    deg_agree = {A for _n, A, _l, _nb, deg, _b in rows
                 if max(deg) == k_complete_degree(A)}
    deg_ok = deg_agree == {A for _n, A, _l, _nb, _d, _b in rows if A <= 3}
    print(f"[4a] degree slot agrees exactly for A <= 3; agreeing A = "
          f"{sorted(deg_agree)} .. {'PASS' if deg_ok else 'FAIL'}")
    ok = ok and deg_ok

    # 4b. BOTH slots agree only at A = 2 — P_A = K_A iff A <= 2.
    both = {A for _n, A, _l, nb, deg, _b in rows
            if nb == k_complete_edges(A) and max(deg) == k_complete_degree(A)}
    both_ok = both == {A for _n, A, _l, _nb, _d, _b in rows if A <= 2}
    print(f"[4b] BOTH slots agree only at A = 2 (P_A = K_A iff A <= 2); "
          f"agreeing A = {sorted(both)} .. {'PASS' if both_ok else 'FAIL'}")
    ok = ok and both_ok

    # 5. Mean braid degree -> 2, so B/A saturates; K_A's z = A-1 is unbounded.
    print()
    print("mean per-nucleon degree (exact rationals):")
    for name, A, _l, nb, _deg, _b in rows:
        mean = Fraction(2 * nb, A)
        print(f"   {name:>5}  braid {str(mean):>7} = {mp.nstr(mp.mpf(mean.numerator) / mean.denominator, 6):>8}"
              f"   K_A {k_complete_degree(A):>3}")
    print("   braid mean = 2(A-1)/A -> 2 (bounded)   K_A = A-1 (unbounded)")
    print("   cf. QOU.Mass.CoordinationSaturation: bounded degree => B/A constant;")
    print("       complete graph => B/A = eps(A-1)/2 unbounded, refuted by saturation.")

    # 6. Bond types, and the m_* lever.
    print()
    print("inter-bond TYPES (from the exact Hecke shift d), canonical ordering:")
    for Z, N, name in cases:
        types = inter_bond_types(Z, N)
        seq = [types[(k, k + 1)] for k in range(Z + N - 1)]
        print(f"   {name:>5}  Z={Z} N={N}  {'-'.join(seq)}")
    print("   Exactly one 'pn' per nucleus: the single p/n boundary of the")
    print("   hard-coded ordering ['p']*Z + ['n']*N. A rearrangement changes the")
    print("   multiset (qou-m07y), so this is a convention, not a nuclear fact.")

    print()
    if ok:
        print("VERDICT: scope-(a) NEGATIVE — the braid supplies a PATH EDGE COUNT, "
              "not a coordination degree.")
    else:
        print("VERDICT: CHECKS FAILED — see the FAIL lines above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
