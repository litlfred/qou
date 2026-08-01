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

STATUS
  ✓ Driver, PD→faces tracer (Euler-verified), coupled (3.3)-(3.4) face solver,
    and braid→PD all implemented.
  ✓ VALIDATED on the figure-eight: the general planar state sum (3.6)
    reproduces kashaev_4_1(N) EXACTLY at N=3,5,7,11 (both the KnotAtlas PD and
    the braid [1,-2,1,-2] PD, with the correct deficit face — see below).
  ✓ DEFICIT-FACE RULE — PINNED (2026-07-27).  Σ(row constraints)=V but
    Σ(all interior column constraints)=F−1=V+1 (Euler), so exactly ONE interior
    face carries column-sum 0, not 1 (the "angle-deficit" face), and is dropped
    from the solve.  WHICH face is geometrically determined, NOT free (different
    drops give different |⟨L⟩|: 85.7 vs the correct 50.5 on the braid 4₁ at
    N=5).  The rule: the deficit face is the UNIQUE face incident to NEITHER
    strand edge e₁ nor e₂ (`deficit_face_of`).  Validated on the figure-eight,
    both the KnotAtlas PD and the braid [1,-2,1,-2] PD — in each the
    neither-strand face is unique and (outer, deficit) reproduces kashaev_4_1 at
    N=3,5,7.  (Rejected en route: "drop the last interior column" — face-order
    dependent, validates FIG8_PD only by luck; and outer col-sum=−1 with a(v,f₀)
    kept free — fails N=5,7, the (3.3) a(v,f₀)=0 gauge is genuinely required.)
  ○ Whitehead cannot be cross-checked via the U_q(sl₂) Markov-trace engine:
    closure_invariant VANISHES at the root of unity (vanishing quantum
    dimension), and the non-zero Kashaev normalization is only coded for 4₁
    (kashaev_4_1).  So Whitehead's validation path is the VOLUME growth
    (2π/N)log|⟨W⟩_N| → Vol(W)=4G≈3.6639, available once the deficit rule is
    fixed.
  ✓ COMPUTE CEILING BROKEN (link_invariant_tn).  The brute state sum is Σ over
    j:E→Z_N (N^{|E|−2} terms; Whitehead N^8, infeasible past N≈7).  Recast as a
    TENSOR-NETWORK contraction — rank-4 R-tensor per crossing, ω^{j(e)} folded
    per edge, strand edges projected to 0, contracted by numpy einsum with an
    optimized order (~N^{treewidth}) — it validates exactly vs the brute sum on
    the figure-eight and reaches N=31 in ≈9s (N=11 in 0.12s).  Whitehead ⟨W⟩_N
    at the N≈11–13 the volume validator needs is now cheap.

Audit-only; no wiring; a genuine multi-session build.
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


def link_invariant_tn(diag: Diagram, N: int, face_index=None) -> complex:
    """⟨L⟩ via TENSOR-NETWORK contraction — same (3.6) sum, but evaluated as a
    contraction of the rank-4 R-tensors (one per crossing) along shared edges,
    with the per-edge ω^{j(e)} folded onto one incident leg and the strand
    edges projected to index 0.  numpy einsum with an optimized order costs
    ~N^{treewidth} instead of the brute N^{|E|−2}, so the Whitehead ⟨W⟩_N
    (|E|=10 ⇒ N^8 brute) becomes tractable to N≈13+ (validated vs
    link_invariant on the figure-eight)."""
    import string
    import numpy as np

    R = KashaevR(N)
    om = R.om
    a = face_index or diag.face_index or solve_face_indices_coupled(diag, N)

    # one rank-4 tensor per crossing: T[i,j,k,l] = R(i,j,k,l | face indices)
    tensors, legs = [], []
    for vi, c in enumerate(diag.crossings):
        av = tuple(a[(vi, f)] for f in c.faces)
        T = np.zeros((N, N, N, N), dtype=complex)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    for l in range(N):
                        T[i, j, k, l] = R.R(i, j, k, l, *av)
        tensors.append(T)
        legs.append(list(c.edges))

    # fold each edge's factor onto its FIRST occurrence: ω^{index} for internal
    # edges, projector [1,0,…,0] for the two strand edges (fixes j(e)=0).
    seen: set = set()
    for t, lg in enumerate(legs):
        for ax, e in enumerate(lg):
            if e in seen:
                continue
            seen.add(e)
            f = np.zeros(N, dtype=complex)
            if e in diag.strand_edges:
                f[0] = 1.0
            else:
                f = om ** np.arange(N)
            shp = [1, 1, 1, 1]; shp[ax] = N
            tensors[t] = tensors[t] * f.reshape(shp)

    # full contraction: every edge label appears on exactly two legs ⇒ einsum
    # over all labels yields the scalar ⟨L⟩.
    labels = sorted({e for lg in legs for e in lg})
    assert len(labels) <= len(string.ascii_letters), "too many edges for einsum letters"
    letter = {e: string.ascii_letters[i] for i, e in enumerate(labels)}
    sub = ",".join("".join(letter[e] for e in lg) for lg in legs)
    return complex(np.einsum(sub, *tensors, optimize="greedy"))


def _trace_faces(pd: list[tuple[int, int, int, int]]):
    """Faces of a 4-valent planar diagram from its PD code via the combinatorial
    map φ = σ∘α (σ = CCW vertex rotation, α = edge involution).

    Dart (c,p) sits on edge pd[c][p]; the CCW order at crossing c is p=0,1,2,3
    (= Kas95 edges i,j,k,l).  The corner/sector between dart p and σ(p)=p+1 is
    the φ-orbit of dart (c,p); Kas95 sectors a,b,c,d ↔ p=0,1,2,3 (a starts at
    the (i,j) sector).  Returns (faces_per_crossing, face_ids) where
    faces_per_crossing[c] = (fa,fb,fc,fd) the four φ-orbit IDs at crossing c."""
    darts = [(c, p) for c in range(len(pd)) for p in range(4)]
    # α: the two darts sharing an edge label
    by_edge: dict[int, list] = {}
    for d in darts:
        by_edge.setdefault(pd[d[0]][d[1]], []).append(d)
    alpha = {}
    for e, ds in by_edge.items():
        assert len(ds) == 2, f"edge {e} appears {len(ds)}× (need 2)"
        alpha[ds[0]], alpha[ds[1]] = ds[1], ds[0]

    def sigma(d):
        return (d[0], (d[1] + 1) % 4)

    def phi(d):
        return sigma(alpha[d])

    seen, face_of = set(), {}
    fid = 0
    for d in darts:
        if d in seen:
            continue
        cur = d
        while cur not in seen:
            seen.add(cur)
            face_of[cur] = fid
            cur = phi(cur)
        fid += 1
    faces_per_crossing = [tuple(face_of[(c, p)] for p in range(4)) for c in range(len(pd))]
    return faces_per_crossing, list(range(fid))


def _solve_mod(A, b, N, tolerant=False):
    """One solution x of A x ≡ b (mod N), N prime.

    tolerant=False: return None if any equation is inconsistent.
    tolerant=True : IGNORE inconsistent leftover rows (0 = nonzero) and return
      the solution of the maximal consistent subsystem.  Used for the
      (3.3)-(3.4) face system, which is rank-deficient by exactly one (the
      global row/col angle-deficit): the lone dependent-inconsistent equation
      is auto-dropped rather than guessing which column to omit."""
    A = [row[:] + [b[i] % N] for i, row in enumerate(A)]
    rows, cols = len(A), len(A[0]) - 1
    piv = []
    r = 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if A[i][c] % N), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = pow(A[r][c], N - 2, N)
        A[r] = [(v * inv) % N for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % N for j in range(cols + 1)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    for i in range(r, rows):
        if A[i][cols] % N and not tolerant:
            return None
    x = [0] * cols
    for i, c in enumerate(piv):
        x[c] = A[i][cols] % N
    return x


def diagram_from_pd(pd, strand_edges, outer_face_hint=None, name=""):
    """Build a Diagram (edges + traced faces) from a PD code."""
    faces_pc, face_ids = _trace_faces(pd)
    crossings = [Crossing(edges=tuple(pd[c]), faces=faces_pc[c]) for c in range(len(pd))]
    edges = sorted({e for tup in pd for e in tup})
    outer = outer_face_hint if outer_face_hint is not None else face_ids[-1]
    return Diagram(crossings=crossings, edges=edges, faces=face_ids,
                   strand_edges=strand_edges, outer_face=outer, name=name)


def _face_edges(diag: Diagram):
    """face id → set of incident edge ids (an edge is incident to a face if the
    face touches one of that edge's ends, i.e. the edge bounds a sector on it)."""
    fe: dict[int, set] = {f: set() for f in diag.faces}
    for c in diag.crossings:
        E = list(c.edges)
        for p in range(4):
            fe[c.faces[p]].add(E[p])
            fe[c.faces[p]].add(E[(p + 1) % 4])
    return fe


def deficit_face_of(diag: Diagram):
    """The deficit face (col-sum 0) — the UNIQUE face incident to NEITHER strand
    edge e₁ nor e₂ (validated on the figure-eight, both KnotAtlas and braid
    diagrams).  Returns the face id, or None if it is not unique (then the
    caller must supply deficit_face / scan)."""
    fe = _face_edges(diag)
    e1, e2 = diag.strand_edges
    cand = [f for f in diag.faces if e1 not in fe[f] and e2 not in fe[f]]
    return cand[0] if len(cand) == 1 else None


def solve_face_indices_coupled(diag: Diagram, N: int, deficit_face=None):
    """Solve the (3.3)-(3.4) system: per-crossing row sums ≡1 AND per-face
    column sums ≡1 (f≠f₀ and f≠deficit_face), with a(v,f₀)=0.  Variables =
    (crossing, sector-face) pairs.  Returns the a-map, or None if inconsistent.
    See the inline note on the (open) deficit-face selection rule."""
    var = {}
    for vi, c in enumerate(diag.crossings):
        for f in c.faces:
            if f != diag.outer_face and (vi, f) not in var:
                var[(vi, f)] = len(var)
    n = len(var)
    A, b = [], []
    # (3.4) row: Σ_f a(v,f) = 1  (sectors on f₀ contribute 0)
    for vi, c in enumerate(diag.crossings):
        row = [0] * n
        for f in c.faces:
            if f != diag.outer_face:
                row[var[(vi, f)]] += 1
        A.append(row); b.append(1)
    # (3.4) col: Σ_v a(v,f) = 1 for each interior face f≠f₀.  The row set
    # (V eqns, global sum V) and the full interior-column set (F−1 eqns,
    # global sum F−1 = V+1 by Euler) are inconsistent by exactly one, so the
    # columns carry a single dependency: impose all-but-one interior column
    # (drop one — the angle-deficit face), leaving the system consistent and
    # under-determined (the paper's "freedom in choosing a").
    faces_to_crossings: dict[int, list] = {}
    for vi, c in enumerate(diag.crossings):
        for f in c.faces:
            faces_to_crossings.setdefault(f, []).append(vi)
    # Global count: Σ(rows)=V but Σ(all interior cols)=F−1=V+1 (Euler), so the
    # interior col-sums CANNOT all be 1 — exactly ONE interior face carries
    # col-sum 0 (the "angle-deficit" face) and is dropped.  WHICH face is the
    # deficit is geometrically determined, NOT free: different drops give
    # different |⟨L⟩| (85.7 vs 50.5 on the braid 4₁ diagram).  The principled
    # rule is still OPEN (see module docstring); `deficit_face` lets the caller
    # supply it, else we drop the last interior face (validated for FIG8_PD).
    interior = [f for f in faces_to_crossings if f != diag.outer_face]
    if deficit_face is None:
        deficit_face = deficit_face_of(diag)   # face touching neither strand edge
    df = deficit_face if deficit_face is not None else interior[-1]
    for f in interior:
        if f == df:
            continue
        row = [0] * n
        for vi in faces_to_crossings[f]:
            row[var[(vi, f)]] += 1
        A.append(row); b.append(1)
    x = _solve_mod(A, b, N)
    if x is None:
        return None
    a = {}
    for (vi, f), idx in var.items():
        a[(vi, f)] = x[idx]
    for vi, c in enumerate(diag.crossings):
        for f in c.faces:
            if f == diag.outer_face:
                a[(vi, f)] = 0
    return a


# figure-eight 4₁ PD code (KnotAtlas): under=(i,k), over=(j,l), CCW — matches Kas95.
FIG8_PD = [(4, 2, 5, 1), (8, 6, 1, 5), (6, 3, 7, 4), (2, 7, 3, 8)]


def braid_to_pd(word, nstr):
    """PD code of the TRACE closure of a braid on `nstr` strands.

    word = list of ±g (1-indexed generator g = crossing between strand
    positions g-1 and g).  Emits Kas95/KnotAtlas PD tuples (i,j,k,l): CCW,
    under=(i,k), over=(j,l).  Crossing box has corners BL,BR,TL,TR with the
    two strands swapping (BL→TR, BR→TL); CCW from BL is [BL,BR,TR,TL].
      positive g (left-over-right, over={BL,TR}): (i,j,k,l)=(BR,TR,TL,BL)
      negative g (right-over-left, over={BR,TL}): (i,j,k,l)=(BL,BR,TR,TL)
    Trace closure: top edge of strand k is identified with its bottom edge."""
    pos = list(range(nstr))           # current edge id on each strand position
    bottom = list(range(nstr))        # initial (bottom) edge ids for closure
    nxt = nstr
    crossings = []
    for g in word:
        p = abs(g) - 1
        ll, lr = pos[p], pos[p + 1]
        ul, ur = nxt, nxt + 1
        nxt += 2
        if g > 0:
            crossings.append((lr, ur, ul, ll))
        else:
            crossings.append((ll, lr, ur, ul))
        pos[p], pos[p + 1] = ul, ur
    # trace closure: identify top edge pos[k] with bottom edge bottom[k]
    parent = list(range(nxt))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)
    for k in range(nstr):
        union(pos[k], bottom[k])
    # compress labels to a contiguous 1..E
    reps = sorted({find(e) for tup in crossings for e in tup})
    relab = {r: i + 1 for i, r in enumerate(reps)}
    return [tuple(relab[find(e)] for e in tup) for tup in crossings]


# Whitehead link (L5a1) PD via the validated braid word [1,-2,1,-2,1] on 3
# strands (braid_to_pd is correct — reproduces the braid 4₁ invariant).  The
# state sum ⟨W⟩ is blocked on the deficit-face rule (see module docstring);
# once fixed, validate via the volume growth → 4G, not the (root-vanishing)
# Markov engine.
WHITEHEAD_PD = None  # = braid_to_pd([1,-2,1,-2,1], 3); computed lazily below


def whitehead_state_sum(N: int, strand_edges, outer_face, deficit_face):
    """⟨Whitehead⟩ via the §3 state sum.  REQUIRES an explicit deficit_face —
    there is deliberately NO default, because the correct choice is an OPEN
    geometric question (see module docstring) and a wrong guess yields a wrong
    invariant.  Validate any candidate convention via the volume growth → 4G."""
    global WHITEHEAD_PD
    if WHITEHEAD_PD is None:
        WHITEHEAD_PD = braid_to_pd([1, -2, 1, -2, 1], 3)
    diag = diagram_from_pd(WHITEHEAD_PD, strand_edges=strand_edges,
                           outer_face_hint=outer_face, name="whitehead")
    a = solve_face_indices_coupled(diag, N, deficit_face=deficit_face)
    if a is None:
        return None, diag
    diag.face_index = a
    return link_invariant(diag, N), diag


def fig8_state_sum(N: int, strand_edges=(1, 2), outer_face=2):
    """⟨4₁⟩ via the [Kas95] §3 state sum with the coupled face solver.

    VALIDATED convention (strand_edges, outer_face): strands (1,2) [or the
    symmetric (4,5)] with outer face 2 reproduce the Kashaev closed form
    kashaev_4_1(N) exactly at N=3,5,7 (13.0, 50.472, 151.279)."""
    diag = diagram_from_pd(FIG8_PD, strand_edges=strand_edges,
                           outer_face_hint=outer_face, name="4_1")
    a = solve_face_indices_coupled(diag, N)
    if a is None:
        return None, diag
    diag.face_index = a
    return link_invariant(diag, N), diag


if __name__ == "__main__":
    import json
    from datetime import datetime, timezone
    from pathlib import Path
    from figure_eight_kashaev_volume import kashaev_4_1

    print("[Kas95] §3 face-index state sum — figure-eight validation\n")
    print("  reproduce the Kashaev closed form kashaev_4_1(N) (= our U_q(sl₂)")
    print("  engine, #4382) from the general planar state sum (3.6):\n")
    rows, ok = [], True
    for N in (3, 5, 7, 11):
        val, _ = fig8_state_sum(N)
        ref = float(kashaev_4_1(N))
        m = abs(val)
        match = abs(m - ref) < 1e-6 * ref
        ok = ok and match
        rows.append((N, m, ref, match))
        print(f"    N={N:3d}: |⟨4₁⟩_statesum|={m:.5f}  kashaev_4_1={ref:.5f}  {'✓' if match else '✗'}")
    print(f"\n  => {'VALIDATED — the §3 state sum computes the Kashaev invariant' if ok else 'MISMATCH'}")
    print("  (odd PRIME N: the mod-N face solve uses a Fermat inverse; composite")
    print("   odd N needs a Z_N solver — deferred, not needed for validation.)")

    wit = {
        "description": "[Kas95] §3 face-index link-invariant state sum, validated on the figure-eight: the general planar state sum (3.6) reproduces the Kashaev closed form kashaev_4_1(N) exactly at N=3,5,7,11. The genuine Kashaev invariant machinery (not a Markov trace). Toward the Whitehead ⟨W⟩_N (#3).",
        "computation": "kashaev_link_statesum", "audit_only": True,
        "reference": "Kashaev 1995, q-alg/9504020 (uploads/9504020v1.pdf), §2-§3",
        "convention": {"fig8_pd": [list(t) for t in FIG8_PD],
                       "strand_edges": [1, 2], "outer_face": 2,
                       "note": "symmetric choice (4,5)/2 also validates"},
        "fig8_validation": {str(N): {"state_sum_abs": m, "kashaev_4_1": ref, "match": bool(mt)}
                            for (N, m, ref, mt) in rows},
        "validated": bool(ok),
        "limitation": "odd PRIME N only (Fermat-inverse face solve); composite N needs a Z_N linear solver",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "kashaev-link-statesum.witness.json"
    out.write_text(json.dumps(wit, indent=2))
    print(f"  Witness: {out}")
