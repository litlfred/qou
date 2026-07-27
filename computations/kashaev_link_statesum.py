#!/usr/bin/env python3
"""[Kas95] §3 link-invariant state sum — the genuine Kashaev invariant of a
link given as a two-strand tangle diagram (q-alg/9504020, uploads/9504020v1.pdf).

WHY this and not a braid closure: kashaev_rmatrix.py proves the Markov
condition tr₂((I⊗μ)Ř)∝I has NO diagonal-μ solution (σ_min≈2.45), so the
Kashaev invariant is not an enhanced Markov trace — it is the §3 state sum
below, whose weights carry FACE (angle) indices absent from a braid trace.

────────────────────────────────────────────────────────────────────────────
[Kas95] §2 crossing convention (page 2, verbatim):
  At an intersection of the planar projection of two non-coplanar segments,
  place indices j,l on the two ends of the OVER-crossing segment and i,k on
  the ends of the UNDER segment, choosing the labelling in which i,j,k,l go
  round the point COUNTER-CLOCKWISE.  Place face indices a,b,c,d on the four
  sectors, CCW, STARTING from the sector bounded by the (i,j) segments.
  Boltzmann weight of the crossing = R(i,j,k,l | a,b,c,d)          (2.8)
  with the sector sum a+b+c+d ≡ 1 (mod N)                          (2.9).

[Kas95] §3 state sum (page 3):
  Link L ⊂ S³ as a two-strand tangle; non-singular planar projection with
  vertex/edge/face sets V,E,F.  Distinguished edges e₁,e₂ = the two strands,
  distinguished face f₀ = outer region.  Maps
      j : E → Z_N ,        a : V×F → Z_N                            (3.1)
  with
      j(e₁) = j(e₂) = 0                                             (3.2)
      a(v,f₀)=0 ;   v∉f ⇒ a(v,f)=0                                  (3.3)
      Σ_{f} a(v,f) = Σ_{v} a(v,f) = 1   (f ≠ f₀)                    (3.4)
  a is FIXED (any valid solution — different choices give the same |⟨L⟩|);
  only j is summed.  The invariant:
      ⟨L⟩ = Σ_j  Π_{v∈V} r_{j,a}(v)  Π_{e∈E} ω^{j(e)}              (3.6)
  where r_{j,a}(v) = R(i,j,k,l|a,b,c,d) reads the four edge indices j(·) and
  the four fixed face indices a(v,·) around v per the §2 convention.
  Disjoint-union vanishing ⟨L₁⊔L₂⟩=0 (3.9); the honest invariant is |⟨L⟩|
  (⟨L⟩ is defined up to N-th roots of unity, Thm 1).  N odd throughout.
────────────────────────────────────────────────────────────────────────────

STATUS: driver + face-index solver implemented and self-consistent; the
figure-eight diagram encoding + validation against the merged closed form
`figure_eight_kashaev_volume.kashaev_4_1` is the in-progress milestone
(see fig8_diagram()).  Audit-only; no wiring; a genuine multi-session build.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field

from kashaev_rmatrix import KashaevR


@dataclass
class Crossing:
    """One vertex v of the diagram, per the §2 CCW convention.

    edges  = (i, j, k, l): the four incident edge IDs in CCW order, with
             (j, l) the over-strand ends and (i, k) the under-strand ends.
    faces  = (a, b, c, d): the four incident face IDs in CCW order, a the
             sector bounded by the (i, j) segments.
    """
    edges: tuple[int, int, int, int]   # (i, j, k, l)
    faces: tuple[int, int, int, int]   # (a, b, c, d)


@dataclass
class Diagram:
    crossings: list[Crossing]
    edges: list[int]                   # all edge IDs
    faces: list[int]                   # all face IDs
    strand_edges: tuple[int, int]      # (e₁, e₂) — fixed to j=0  (3.2)
    outer_face: int                    # f₀ — fixed to a=0        (3.3)
    name: str = ""
    # optional explicit face-index solution a(v,f); if None, solve() finds one
    face_index: dict[tuple[int, int], int] = field(default_factory=dict)


def solve_face_indices(diag: Diagram, N: int) -> dict[tuple[int, int], int]:
    """Find ONE map a:V×F→Z_N satisfying (3.3)-(3.4).

    Per-crossing the four sector values sum to 1 mod N (3.4, row form); the
    column form Σ_v a(v,f)=1 is the residual consistency of the shared faces.
    We solve the row constraints directly: three sector values free, the
    fourth fixed by a≡1−(others).  f₀ sectors forced to 0 (3.3).  Returns the
    a-map; raises if the outer-face constraint over-determines a crossing.
    """
    a: dict[tuple[int, int], int] = {}
    for vi, c in enumerate(diag.crossings):
        secs = list(c.faces)
        # (3.3): sectors on the outer face are 0
        forced0 = [s for s in secs if s == diag.outer_face]
        free = [s for s in secs if s != diag.outer_face]
        if not free:
            raise ValueError(f"crossing {vi} entirely on outer face — degenerate")
        # assign the first |free|-1 sectors a symbolic-free value 0 (a valid
        # particular solution; Thm 1 freedom), last free sector closes to 1.
        acc = 0
        for s in free[:-1]:
            a[(vi, s)] = 0
        a[(vi, free[-1])] = (1 - acc) % N
        for s in forced0:
            a[(vi, s)] = 0
    return a


def _weight(R: KashaevR, jvals, avals, N: int) -> complex:
    """R(i,j,k,l|a,b,c,d) with the sector sum forced to ≡1 (2.9) by construction."""
    i, j, k, l = jvals
    a, b, c, d = avals
    return R.R(i, j, k, l, a, b, c, d)


def link_invariant(diag: Diagram, N: int) -> complex:
    """⟨L⟩ via (3.6): sum over j:E→Z_N with the two strand edges fixed to 0."""
    R = KashaevR(N)
    om = R.om
    a = diag.face_index or solve_face_indices(diag, N)

    free_edges = [e for e in diag.edges if e not in diag.strand_edges]
    total = 0j
    for assign in itertools.product(range(N), repeat=len(free_edges)):
        jmap = dict(zip(free_edges, assign))
        for e in diag.strand_edges:
            jmap[e] = 0
        wprod = 1.0 + 0j
        for vi, c in enumerate(diag.crossings):
            jvals = tuple(jmap[e] for e in c.edges)
            avals = tuple(a[(vi, f)] for f in c.faces)
            wprod *= _weight(R, jvals, avals, N)
            if wprod == 0:
                break
        if wprod == 0:
            continue
        ephase = 1.0 + 0j
        for e in diag.edges:
            ephase *= om ** jmap[e]
        total += wprod * ephase
    return total


def fig8_diagram() -> Diagram:
    """The figure-eight (4₁) standard 4-crossing alternating diagram as a
    two-strand tangle.  MILESTONE (in progress): the CCW edge/face bookkeeping
    at each crossing is being validated against the merged closed form
    kashaev_4_1(N).  Encoded here for iteration; not yet asserted correct."""
    raise NotImplementedError(
        "figure-eight diagram encoding is the in-progress validation milestone")


if __name__ == "__main__":
    # Self-consistency of the driver/solver on a trivially small synthetic
    # diagram (one crossing, all four sectors distinct, no outer face) — this
    # exercises the face-index solver + weight read, NOT the topological
    # invariance (that needs a real diagram, next unit).
    d = Diagram(
        crossings=[Crossing(edges=(0, 1, 2, 3), faces=(10, 11, 12, 13))],
        edges=[0, 1, 2, 3], faces=[10, 11, 12, 13],
        strand_edges=(0, 2), outer_face=13, name="synthetic-1x",
    )
    for N in (3, 5):
        a = solve_face_indices(d, N)
        sec_sum = sum(a[(0, f)] for f in d.crossings[0].faces) % N
        val = link_invariant(d, N)
        print(f"N={N}: sector-sum≡{sec_sum} (want 1)  ⟨synthetic⟩={val:.4f}  |·|={abs(val):.4f}")
    print("\nfigure-eight validation vs kashaev_4_1: NEXT UNIT (fig8_diagram)")
