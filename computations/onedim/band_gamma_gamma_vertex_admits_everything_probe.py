#!/usr/bin/env python3
# polynomial_q_not_applicable: exact integer/set combinatorics on braid words;
# no q enters, so there is no symbolic-q polynomial output.
"""If the gamma-gamma vertex is read on BAND (Birman-Ko-Lee) generators instead
of adjacent Artin ones, what layouts does it admit?

Measured answer: **all of them**.  The band reading imposes NO constraint on
the strand layout whatsoever, so it does not DERIVE a non-contiguous layout --
it merely permits one, and the entire selection burden moves to the
confinement SDP.

## Why this was run

`gamma_gamma_forces_the_layout_probe.py` (15/15) showed that the corpus's
Artin-adjacent vertex `sigma_i sigma_{i+1}^{-1}` forces the contiguous layout
UNIQUELY, and left open the band reading, under which a "band vertex"
`a_{ts} a_{t's'}^{-1}` has writhe 0 and passes
`GammaGammaWordSelection.writhe_eq_zero` while not being a `GammaGammaWord`
under that file's inductive definition.

The band reading is not idle speculation: `EnumeratorSelectionDegeneracy.lean`
:110-130 states that the obstruction is *"not the strand layout ... It is the
generator set"*, counts inter-nucleon band generators in `B_9` at **27 against
the 2** an enumerator searched, and concludes *"the band presentation **is**
the right generating set"*.  Three `A = 4` cluster probes already use BKL bands
to build a complete coordination graph.  And the held literature has the same
point: `library/arxiv-0802.1072v2` sec-002 (Birman-Menasco) gives the band
presentation of `B_3` on a **cyclically ordered** generating set.

## The band generator, written out

    a_{ts} = (sigma_{t-1} ... sigma_{s+1}) sigma_s (sigma_{s+1}^{-1} ... sigma_{t-1}^{-1})

for `s < t`, joining strands `s` and `t` DIRECTLY.  `a_{s+1,s} = sigma_s`, so
the Artin generators are the adjacent bands -- a proper subset.  Built here as
an explicit Artin word (CHECK 1) so nothing is assumed about it.

## What a "band gamma-gamma vertex" is taken to be

The Artin vertex's defining structure, per `GammaGammaWordSelection.vertex`'s
own docstring, is *"one photon on strands `(i, i+1)` and one anti-photon on
`(i+1, i+2)`"* -- two crossings of OPPOSITE sign SHARING EXACTLY ONE STRAND.
The band reading keeps that and drops only adjacency:

    band vertex  =  a_{ts} a_{t's'}^{-1}   with  |{s,t} cap {s',t'}| = 1

`sigma_i sigma_{i+1}^{-1} = a_{i+1,i} a_{i+2,i+1}^{-1}` is the case where both
bands are adjacent (CHECK 3), so this is a strict generalisation and not a
different object.

## What is measured

1. The band generator's Artin expansion: `a_{s+1,s} = sigma_s`, length
   `2(t-s-1)+1`, and **writhe 1** for every `s < t` -- so a band vertex has
   writhe 0 and passes `writhe_eq_zero` (CHECK 1-2).
2. A band vertex is NOT a `GammaGammaWord`: its Artin expansion violates the
   inductive definition's sign pattern (CHECK 4).
3. **THE COLLAPSE.**  Every 3-subset of strands is the support of some band
   vertex -- exhaustively, all `C(9,3) = 84` and `C(12,3) = 220` of them
   (CHECK 5).  Take any `a < b < c` and use `a_{b,a} a_{c,b}^{-1}`, which share
   strand `b`.
4. Hence the "every nucleon carries an internal gamma-gamma vertex" demand,
   read on bands, admits **every** 3-uniform partition: 280 at `A = 3` and
   15400 at `A = 4`, against **1** under the Artin reading (CHECK 6).
5. Of those, 234 / 13969 carry a triangle (CHECK 7) -- the 3-cell is permitted,
   in abundance.

## What this means, and what it does NOT

The band reading does **not** derive a non-contiguous layout.  It removes the
only thing that was selecting one.  Under Artin the gamma-gamma half of the
`qou-ales` selection rule picks the layout uniquely and the SDP then picks the
word; under bands the gamma-gamma half is **vacuous as a layout selector** and
the whole burden falls on the confinement SDP -- reading 3, Frobenius
positivity, per the owner ruling of 2026-09-12.

So the choice between the two readings is a choice about **where the selection
happens**, not about whether a 3-cell is "allowed".  That is the shape the
question should be put in, and it is why picking the band reading BECAUSE it
yields a 3-cell would be selection against the target (AGENTS.md
"NO FITTING"): it yields a 3-cell by yielding everything.

NOT claimed: that the confinement SDP does or does not select a non-contiguous
layout (not run here); that the band reading is right or wrong; any value of
`b3` or of the binding under either reading.  Note independently that a
triangle does not by itself flip `b3` --
`single_letter_interface_forces_bond_product_probe.py` CHECK 6 measures
`b3 < 0` on a triangle whenever all three bonds are repulsive.

Read-only: writes no witness, runs no producer, reads no AME/CODATA/census.
"""
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


# ------------------------------------------------- braid words as (gen, sign)

def sigma(i, pos=True):
    return (i, pos)


def band(s, t):
    """The BKL band generator `a_{ts}`, as an explicit Artin word.

    a_{ts} = (sigma_{t-1} ... sigma_{s+1}) sigma_s (sigma_{s+1}^-1 ... sigma_{t-1}^-1)
    """
    if not s < t:
        raise ValueError("band requires s < t")
    left = [sigma(j, True) for j in range(t - 1, s, -1)]
    right = [sigma(j, False) for j in range(s + 1, t)]
    return left + [sigma(s, True)] + right


def inverse(word):
    return [(g, not p) for g, p in reversed(word)]


def writhe(word):
    return sum(1 if p else -1 for _, p in word)


def strands(word):
    """Strands touched: `sigma_j` exchanges `j` and `j+1`."""
    out = set()
    for g, _ in word:
        out |= {g, g + 1}
    return frozenset(out)


def band_strands(s, t):
    """The two strands a band JOINS (not the strands its expansion sweeps)."""
    return frozenset({s, t})


def band_vertex(s, t, s2, t2):
    """`a_{ts} a_{t's'}^{-1}` -- the band gamma-gamma vertex."""
    return band(s, t) + inverse(band(s2, t2))


def is_gamma_gamma_word(word):
    """Is this word a product of `vertex i = [(i, +), (i+1, -)]`?

    Decided against `GammaGammaWordSelection.GammaGammaWord`'s inductive
    definition directly: even length, and every even position positive with
    the next position its successor generator, negative.
    """
    if len(word) % 2:
        return False
    for j in range(0, len(word), 2):
        (g0, p0), (g1, p1) = word[j], word[j + 1]
        if not (p0 and not p1 and g1 == g0 + 1):
            return False
    return True


# ------------------------------------------------- partitions

def partitions_into_triples(elements):
    elements = tuple(sorted(elements))
    if not elements:
        yield ()
        return
    head, rest = elements[0], elements[1:]
    for pair in combinations(rest, 2):
        block = frozenset((head,) + pair)
        remaining = tuple(e for e in rest if e not in pair)
        for tail in partitions_into_triples(remaining):
            yield (block,) + tail


def block_of(partition, s):
    for idx, b in enumerate(partition):
        if s in b:
            return idx
    raise KeyError(s)


def has_triangle(partition, n, a):
    edges = set()
    for s in range(n - 1):
        j, k = block_of(partition, s), block_of(partition, s + 1)
        if j != k:
            edges.add(frozenset({j, k}))
    return any(frozenset({x, y}) in edges and frozenset({y, z}) in edges
               and frozenset({x, z}) in edges
               for x, y, z in combinations(range(a), 3))


def is_interval(block):
    v = sorted(block)
    return all(y - x == 1 for x, y in zip(v, v[1:]))


# ------------------------------------------------- main

def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    print("=" * 78)
    print("The BAND reading of the gamma-gamma vertex: what layouts does it admit?")
    print("=" * 78)

    # ---- CHECK 1: the band generator itself
    print("\n[1] the BKL band generator, as an explicit Artin word")
    adj_ok = all(band(s, s + 1) == [sigma(s, True)] for s in range(8))
    len_ok = all(len(band(s, t)) == 2 * (t - s - 1) + 1
                 for s in range(8) for t in range(s + 1, 9))
    print(f"    a_(1,0) = {band(0, 1)}")
    print(f"    a_(3,0) = {band(0, 3)}")
    print(f"    a_(7,3) = {band(3, 7)}")
    check("a_{s+1,s} == sigma_s (the Artin generators are the adjacent bands)", adj_ok)
    check("len(a_{ts}) == 2(t-s-1)+1", len_ok)

    # ---- CHECK 2: writhe
    print("\n[2] writhe")
    w1 = all(writhe(band(s, t)) == 1 for s in range(9) for t in range(s + 1, 10))
    w0 = all(writhe(band_vertex(a, b, b, c)) == 0
             for a, b, c in combinations(range(9), 3))
    check("every band generator has writhe 1 (conjugate of a single crossing)", w1)
    check("hence every band vertex has writhe 0 -- it PASSES writhe_eq_zero", w0,
          "which is why the corpus's writhe test cannot separate the two readings")

    # ---- CHECK 3: the Artin vertex is the adjacent special case
    print("\n[3] the Artin vertex is the all-adjacent band vertex")
    artin_ok = True
    for i in range(7):
        lhs = [sigma(i, True), sigma(i + 1, False)]
        rhs = band_vertex(i, i + 1, i + 1, i + 2)
        if lhs != rhs:
            artin_ok = False
    check("sigma_i sigma_{i+1}^-1 == a_{i+1,i} a_{i+2,i+1}^-1", artin_ok,
          "so the band reading is a strict generalisation, not a different object")

    # ---- CHECK 4: a non-adjacent band vertex is NOT a GammaGammaWord
    print("\n[4] but a NON-adjacent band vertex is not a GammaGammaWord")
    v_adj = band_vertex(0, 1, 1, 2)
    v_far = band_vertex(0, 2, 2, 3)
    print(f"    adjacent  a_(1,0) a_(2,1)^-1 = {v_adj}")
    print(f"    spread    a_(2,0) a_(3,2)^-1 = {v_far}")
    check("the adjacent one IS a GammaGammaWord", is_gamma_gamma_word(v_adj))
    check("the spread one is NOT", not is_gamma_gamma_word(v_far),
          "sign pattern (+,+,-,-) violates the inductive definition")

    # ---- CHECK 5: THE COLLAPSE
    print("\n[5] every 3-subset of strands is a band vertex's support")
    miss = []
    for n in (9, 12):
        for a, b, c in combinations(range(n), 3):
            # bands a_{b,a} and a_{c,b} share exactly strand b
            shared = band_strands(a, b) & band_strands(b, c)
            joined = band_strands(a, b) | band_strands(b, c)
            if len(shared) != 1 or joined != frozenset({a, b, c}):
                miss.append((n, a, b, c))
    check("all C(9,3)=84 and C(12,3)=220 triples are realised", not miss,
          f"{len(miss)} misses; witness for {{a<b<c}} is a_(b,a) a_(c,b)^-1, sharing b")

    # ---- CHECK 6-7: the admitted layouts
    print("\n[6-7] what the two readings admit")
    print(f"    {'A':>2}  {'partitions':>10}  {'Artin admits':>13}  {'band admits':>12}"
          f"  {'band w/ triangle':>17}")
    rows = {}
    for a in (2, 3, 4):
        n = 3 * a
        total = artin = band_adm = band_tri = 0
        for part in partitions_into_triples(range(n)):
            total += 1
            # Artin: every block must admit an internal ADJACENT vertex == be an interval
            if all(is_interval(b) for b in part):
                artin += 1
            # band: every block must admit an internal BAND vertex == always true
            if all(len(b) == 3 for b in part):
                band_adm += 1
                if has_triangle(part, n, a):
                    band_tri += 1
        rows[a] = (total, artin, band_adm, band_tri)
        print(f"    {a:>2}  {total:>10}  {artin:>13}  {band_adm:>12}  {band_tri:>17}")
    check("the Artin reading admits exactly ONE layout at every A",
          all(r[1] == 1 for r in rows.values()))
    check("the band reading admits EVERY layout -- no constraint at all",
          all(r[2] == r[0] for r in rows.values()),
          "; ".join(f"A={a}: {r[2]}/{r[0]}" for a, r in rows.items()))
    check("and the admitted set is mostly triangles",
          rows[3][3] == 234 and rows[4][3] == 13969,
          f"A=3: {rows[3][3]}/{rows[3][0]}; A=4: {rows[4][3]}/{rows[4][0]}")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

The band reading does NOT derive a non-contiguous layout.  It admits EVERY
layout -- 280 of 280 at A = 3, 15400 of 15400 at A = 4 -- because any three
strands `a < b < c` are the support of the band vertex `a_(b,a) a_(c,b)^-1`.
So it does not select; it removes the thing that was selecting.

That is the sharp form of the choice between the two readings, and it is not
"does the framework have a 3-cell":

    Artin reading   the gamma-gamma half of qou-ales picks the LAYOUT
                    uniquely (contiguous), and the confinement SDP then picks
                    the WORD within it.  No 3-cell.
    band reading    the gamma-gamma half is VACUOUS as a layout selector.
                    Every layout is admissible, 83.6 % / 90.7 % of them carry
                    a triangle, and the entire selection burden falls on the
                    confinement SDP alone (reading 3, Frobenius positivity,
                    owner ruling 2026-09-12).

Adopting the band reading BECAUSE it yields a 3-cell would be selection
against the target: it yields a 3-cell by yielding everything.  What would
make it a derivation is running the confinement SDP over the enlarged
candidate set and reporting what survives -- `EnumeratorSelectionDegeneracy`
counts 27 inter-nucleon band generators in B_9 against the 2 an enumerator
has searched, so that space is real and almost entirely unexplored.

NOT claimed here: that the SDP does or does not select a non-contiguous
layout; which reading is right; any binding number under either.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
