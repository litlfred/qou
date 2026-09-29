#!/usr/bin/env python3
# polynomial_q_not_applicable: exact integer/set combinatorics on the strand
# path; no q enters, so there is no symbolic-q polynomial output.
"""Is the contiguous strand layout a MODELLING CHOICE or is it DERIVED?
Measured answer: it is derived, it is UNIQUE, and the deriving hypothesis is
the corpus's own gamma-gamma vertex definition.

## Why this was asked

`nonlinear_layout_sources_probe.py` measured that the contiguous layout
`nucleon k -> strands (3k, 3k+1, 3k+2)` is corpus-uniform (61 references
across 41 files) and found nowhere downstream that a NON-contiguous one could
come from.  `NoThreeCellOnTheChain.lean` then proves that a linear layout
carries no triangle, hence no 3-cell -- but it takes `LinearLayout` as a
HYPOTHESIS.  So the open question was upstream: what, if anything, forces the
layout?  Owner ruling `qou-ales` (2026-09-08) names the selection rule --
gamma-gamma production plus the confinement SDP, never census -- so that is
where the answer had to come from.

## The hypothesis being tested, stated before it was run

`QOU/Mass/GammaGammaWordSelection.lean` defines the pair-production vertex as

    vertex i = [sigma_i, sigma_{i+1}^{-1}]

-- ADJACENT Artin generators.  A crossing `sigma_j` exchanges strands `j` and
`j+1`, so `vertex i` touches exactly the three strands `{i, i+1, i+2}`.
A nucleon's internal word is `beta_Bor = (sigma_0 sigma_1^{-1})^3`, i.e. three
such vertices, and it is INTERNAL to a nucleon exactly when the strands it
touches all belong to that nucleon's own block.  If the nucleon's braiding
reached a strand of another block, that is not an internal word -- it is an
inter-nucleon bond.

CLAIM: that single demand forces the block to be an interval, forces the whole
partition, and therefore forces the coordination graph to be a path.

## What is measured

Exhaustively, over EVERY partition of the `3A` strands into `A` unordered
blocks of three (A = 2, 3, 4 -- 10, 280 and 15400 partitions):

1. a 3-element block admits an internal gamma-gamma vertex IFF it is an
   interval `{a, a+1, a+2}`  (CHECK 2);
2. the all-interval partitions number exactly ONE, the contiguous layout
   (CHECK 3) -- so the layout is not merely constrained, it is determined;
3. every all-interval partition's block quotient is the path `P_A`
   (CHECK 4), which is the `LinearLayout` hypothesis of
   `NoThreeCellOnTheChain.lean`, now supplied rather than assumed;
4. NO all-interval partition carries a triangle, while non-interval ones do
   (CHECK 5) -- so the missing 3-cell is downstream of the gamma-gamma
   definition, not of an arbitrary convention;
5. the interleaved "residue" partition `{k, k+A, k+2A}` -- the natural
   candidate for a non-linear layout -- has block quotient the CYCLE `C_A`,
   a triangle at A = 3 (CHECK 6).  It is excluded because NO block of it is
   an interval, so under the Artin-adjacent reading not one of its nucleons
   can carry an internal gamma-gamma word.

## Scope of the negative (AGENTS.md "Before declaring refuted")

This is a scope-(b) STRUCTURAL exclusion with a named invariant: a `sigma_j`
crossing joins only CONSECUTIVE strands, so a set of three strands closed
under a gamma-gamma vertex is an interval, and intervals of length three
tiling `[0, 3A)` are unique.  It excludes a non-contiguous layout from the
ARTIN-ADJACENT reading of the gamma-gamma vertex -- which is the reading
`GammaGammaWordSelection.lean` encodes.

It does NOT exclude a band-generator reading.  A band generator
`a_{ts} = (sigma_{t-1}...sigma_{s+1}) sigma_s (sigma_{s+1}^{-1}...sigma_{t-1}^{-1})`
crosses two NON-adjacent strands and has writhe 1, so a "band vertex"
`a_{ts} a_{t's'}^{-1}` has writhe 0 and would pass `writhe_eq_zero` -- while
NOT being a `GammaGammaWord` under the corpus's inductive definition.  Under a
band reading the non-contiguous layouts reopen.  Which reading the physics
means is a DEFINITIONAL question and is not decided here; picking the reading
that yields a 3-cell would be selection against the target (AGENTS.md
"NO FITTING").

Read-only: writes no witness, runs no producer, reads no AME/CODATA/census.
"""
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


# ---------------------------------------------------------------- geometry

def vertex_strands(i):
    """Strands touched by the gamma-gamma vertex `sigma_i sigma_{i+1}^{-1}`.

    `sigma_j` exchanges strands `j` and `j+1`; the vertex uses generators
    `i` and `i+1`, so the union is `{i, i+1, i+2}`.
    """
    return frozenset({i, i + 1, i + 2})


def is_interval(block):
    """Is this set of strands a run of consecutive integers?"""
    s = sorted(block)
    return all(b - a == 1 for a, b in zip(s, s[1:]))


def admits_internal_vertex(block, n):
    """Does some gamma-gamma vertex live entirely inside `block`?

    Decided by brute force over every generator index, not by the interval
    test -- otherwise CHECK 2 would be checking the interval test against
    itself.
    """
    return any(vertex_strands(i) <= set(block) for i in range(n - 1))


# ---------------------------------------------------------------- partitions

def partitions_into_triples(elements):
    """Every partition of `elements` into unordered blocks of three.

    Canonical: the smallest remaining element is always placed first, so each
    partition is generated exactly once.
    """
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
    for idx, block in enumerate(partition):
        if s in block:
            return idx
    raise KeyError(s)


def quotient_edges(partition, n):
    """Simple-graph edges of the block quotient of the strand path `P_n`."""
    edges = set()
    for s in range(n - 1):
        a, b = block_of(partition, s), block_of(partition, s + 1)
        if a != b:
            edges.add(frozenset({a, b}))
    return edges


def has_triangle(edges, a_blocks):
    for t in combinations(range(a_blocks), 3):
        x, y, z = t
        if (frozenset({x, y}) in edges and frozenset({y, z}) in edges
                and frozenset({x, z}) in edges):
            return True
    return False


def is_path_graph(edges, a_blocks):
    """Is this simple graph a path on all `a_blocks` vertices?"""
    if len(edges) != a_blocks - 1:
        return False
    deg = {v: 0 for v in range(a_blocks)}
    for e in edges:
        for v in e:
            deg[v] += 1
    if a_blocks == 1:
        return not edges
    if sorted(deg.values()) != [1, 1] + [2] * (a_blocks - 2):
        return False
    # connected?
    seen, stack = {0}, [0]
    adj = {v: set() for v in range(a_blocks)}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    while stack:
        for w in adj[stack.pop()]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == a_blocks


def is_cycle_graph(edges, a_blocks):
    if a_blocks < 3 or len(edges) != a_blocks:
        return False
    deg = {v: 0 for v in range(a_blocks)}
    for e in edges:
        for v in e:
            deg[v] += 1
    return all(d == 2 for d in deg.values())


def contiguous_layout(a_blocks):
    return tuple(frozenset({3 * k, 3 * k + 1, 3 * k + 2}) for k in range(a_blocks))


def residue_layout(a_blocks):
    return tuple(frozenset({k, k + a_blocks, k + 2 * a_blocks})
                 for k in range(a_blocks))


# ---------------------------------------------------------------- main

def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    print("=" * 78)
    print("Does gamma-gamma production force the strand layout?")
    print("=" * 78)

    # ---- CHECK 1: the vertex's strand support
    print("\n[1] the gamma-gamma vertex sigma_i sigma_{i+1}^{-1} touches 3 consecutive strands")
    ok = all(vertex_strands(i) == frozenset({i, i + 1, i + 2}) for i in range(12))
    check("vertex i touches exactly {i, i+1, i+2}", ok,
          f"vertex(0) = {sorted(vertex_strands(0))}, vertex(4) = {sorted(vertex_strands(4))}")

    # ---- CHECK 2: internal vertex <=> interval, exhaustive over 3-subsets
    print("\n[2] a 3-strand block admits an internal vertex IFF it is an interval")
    mismatches, tested = [], 0
    for n in (6, 9, 12):
        for block in combinations(range(n), 3):
            tested += 1
            if admits_internal_vertex(block, n) != is_interval(block):
                mismatches.append((n, block))
    check("admits_internal_vertex == is_interval on every 3-subset", not mismatches,
          f"{tested} subsets over n = 6, 9, 12; {len(mismatches)} mismatches")

    # ---- CHECKS 3-5: exhaustive partition census
    print("\n[3-5] exhaustive census of 3-uniform partitions of the strand path")
    census = {}
    for a_blocks in (2, 3, 4):
        n = 3 * a_blocks
        total = all_interval = interval_is_path = tri_all = tri_any = 0
        gg_ok = 0
        interval_partitions = []
        for part in partitions_into_triples(range(n)):
            total += 1
            edges = quotient_edges(part, n)
            tri = has_triangle(edges, a_blocks)
            if tri:
                tri_any += 1
            every_block_interval = all(is_interval(b) for b in part)
            every_block_gg = all(admits_internal_vertex(b, n) for b in part)
            if every_block_gg:
                gg_ok += 1
            if every_block_interval:
                all_interval += 1
                interval_partitions.append(part)
                if is_path_graph(edges, a_blocks):
                    interval_is_path += 1
                if tri:
                    tri_all += 1
        census[a_blocks] = dict(total=total, all_interval=all_interval,
                                interval_is_path=interval_is_path,
                                tri_all=tri_all, tri_any=tri_any, gg_ok=gg_ok,
                                parts=interval_partitions)
        print(f"    A = {a_blocks} (n = {n}): {total} partitions; "
              f"all-interval {all_interval}; gg-internal-everywhere {gg_ok}; "
              f"carrying a triangle {tri_any}")

    check("the all-interval partition is UNIQUE at every A",
          all(c["all_interval"] == 1 for c in census.values()),
          "; ".join(f"A={a}: {c['all_interval']}" for a, c in census.items()))

    check("it IS the contiguous layout",
          all(set(c["parts"][0]) == set(contiguous_layout(a))
              for a, c in census.items()),
          "blocks (3k, 3k+1, 3k+2)")

    check("'every block admits an internal gamma-gamma vertex' selects the SAME single partition",
          all(c["gg_ok"] == 1 for c in census.values()),
          "; ".join(f"A={a}: {c['gg_ok']}" for a, c in census.items()))

    check("every all-interval partition's block quotient is the path P_A",
          all(c["interval_is_path"] == c["all_interval"] for c in census.values()),
          "supplies the LinearLayout hypothesis of NoThreeCellOnTheChain.lean")

    check("NO all-interval partition carries a triangle",
          all(c["tri_all"] == 0 for c in census.values()),
          "; ".join(f"A={a}: {c['tri_all']} of {c['all_interval']}" for a, c in census.items()))

    check("non-interval partitions DO carry triangles (the exclusion has content)",
          census[3]["tri_any"] > 0 and census[4]["tri_any"] > 0,
          f"A=3: {census[3]['tri_any']} of {census[3]['total']}; "
          f"A=4: {census[4]['tri_any']} of {census[4]['total']}")

    # ---- CHECK 6: the residue layout
    print("\n[6] the interleaved (residue) layout {k, k+A, k+2A}")
    for a_blocks in (3, 4, 5):
        n = 3 * a_blocks
        part = residue_layout(a_blocks)
        edges = quotient_edges(part, n)
        cyc = is_cycle_graph(edges, a_blocks)
        tri = has_triangle(edges, a_blocks)
        any_interval = any(is_interval(b) for b in part)
        any_gg = any(admits_internal_vertex(b, n) for b in part)
        print(f"    A = {a_blocks}: quotient has {len(edges)} edges, "
              f"cycle C_A = {cyc}, triangle = {tri}, "
              f"any block an interval = {any_interval}, "
              f"any block gg-internal = {any_gg}")
        check(f"A={a_blocks}: residue layout's quotient is the cycle C_{a_blocks}", cyc)
        check(f"A={a_blocks}: NO block of the residue layout admits an internal vertex",
              not any_gg)
    check("at A = 3 the residue layout's cycle IS a triangle",
          has_triangle(quotient_edges(residue_layout(3), 9), 3),
          "so a 3-cell is combinatorially reachable -- it is the gamma-gamma "
          "demand, not the braid group, that excludes it")

    # ---- summary
    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

The contiguous layout is DERIVED, and it is UNIQUE.  Under the corpus's own
Artin-adjacent gamma-gamma vertex, demanding that every nucleon carry an
internal pair-production word admits exactly ONE strand partition at each A --
the contiguous one already in use.  Its block quotient is the path, which is
the hypothesis `NoThreeCellOnTheChain.lean` assumes; so the absence of a
3-cell now rests on the gamma-gamma definition rather than on a convention.

The exclusion has content: triangles are combinatorially available (the
interleaved layout's quotient is the cycle C_A, a triangle at A = 3), and are
ruled out only because no block of such a layout is an interval.

Scope (b), invariant: a `sigma_j` crossing joins CONSECUTIVE strands only, so
a 3-strand set closed under a gamma-gamma vertex is an interval, and length-3
intervals tile [0, 3A) uniquely.  NOT excluded: a band-generator reading of
the vertex, under which the non-contiguous layouts reopen.  That reading is a
definitional question and is deliberately left open here.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
