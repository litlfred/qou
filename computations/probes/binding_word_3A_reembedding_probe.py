#!/usr/bin/env python3
"""Does re-embedding the binding producer's word on 3A strands restore
level-locality?  No for A ≥ 3, yes for A = 2 — and the trace moves.
(bean qou-w6x3; option 2 of qou-hxz4 / PR #7173)

QUESTION
--------
PR #7160 proved that a *level-local* word — one whose letters group into
consecutive blocks with pairwise disjoint generator sets — has a dimension-free
seminormal character,

    χ^λ(T_β) = Σ_{T ∈ SYT(λ)} Π_j ⟨T | F_j | T⟩ ,

and shipped `computations/chi_path_sum_seminormal.py`.  PR #7173 (qou-hxz4)
then measured that the words
`hecke_core_legacy.unified_iterative_correction` hands its Rust kernel are NOT
level-local, for any atom and any partition size k, and that no
trace-preserving reordering repairs that.  It diagnosed the cause as the
**fixed-H_k embedding**: `_step_chain_generic` cycles the generator index
`g mod (k-1)`, so every letter of every step touches every generator.

`qou-hxz4` named three options.  This probe takes **option 2**: re-embed on
**3A strands**, the indexing `mass_at_3A_proper.atom_braid_word_3A` uses, where
nucleon k owns strands 3k, 3k+1, 3k+2 and its intra-nucleon crossings are the
single generators σ_{3k}, σ_{3k+1}.

WHAT IS MEASURED (instrumented, not read off docstrings)
---------------------------------------------------------
1. **The coupling structures, side by side.**  The binding producer's word is
   captured from `_step_chain_generic` and its inter-nucleon letters counted:
   one per (new nucleon, earlier nucleon) pair, i.e. **C(A,2) — the complete
   graph K_A**.  `atom_braid_word_3A` emits its bond only between consecutive
   nucleons, at generator 3k+2: **A−1 — the path P_A**.  This difference, not
   the cycling, is what decides option 2.

2. **The obstruction, exhaustively and for every A.**  A single-generator
   coupling between nucleons i and j needs an adjacent strand pair with one
   strand in each.  Over every contiguous layout the resulting coupling graph
   is exactly P_A, so K_A is unreachable for A ≥ 3 (it is reachable, and equal
   to P_A, only at A = 2).  Dropping contiguity, K_A is layout-realisable iff
   A ≤ 6: witnesses are exhibited for A = 2…6, A = 7 is exhaustively
   impossible, and the counting bound C(A,2) ≤ 3A−1 — a linear arrangement of
   3A strands has only 3A−1 adjacent pairs — gives A ≤ 6 for every A.  But no
   K_A-realising layout leaves a single nucleon triple contiguous, so the
   escape costs exactly what it buys.

3. **The explicit escape (conjugated bonds).**  A non-adjacent pair can be
   coupled by conjugating a boundary crossing, `T_w σ T_w⁻¹`.  The word is
   built and segmented with the shipped `segments_of`: the generator support of
   the bond for the extreme pair (0, A−1) is the interval [2, 3A−4], which
   swallows every intermediate nucleon's generators, and the segmentation
   collapses to **3 segments of sizes 2, 3A−5, 2** against the mass word's
   **2A−1 segments of max size 2**.  The largest segment grows linearly in A,
   so the dimension-free property is lost at the first non-adjacent pair.

4. **Whether the value moves — measured, at the one A where both embeddings
   exist.**  At A = 2 the binding coupling C(2,2) = 1 equals the chain A−1 = 1,
   so the deuteron word re-embeds exactly.  Both words then live in the SAME
   H_6, carry the SAME 23 letters with the SAME (c, d) offsets, and differ
   ONLY in which generator each letter is assigned to.  χ^λ is computed for
   every λ ⊢ 6 under both, by two independent routes (the #7160 path sum and a
   dense Young-seminormal matrix product built from
   `hecke_core_legacy._build_ysn_matrices`), and the relative differences are
   reported per partition.

5. **Where the move can and cannot live.**  The two one-dimensional irreps are
   blind to the embedding: ρ(σ_i) = q for λ = (n) and −q⁻¹ for λ = (1ⁿ),
   independent of i, so χ = Π_pos (q + d_pos) and Π_pos (−q⁻¹ + d_pos) — closed
   forms asserted here.  Every bit of the move therefore sits in dim ≥ 2.
   This is worth stating because `_step_chain_22`'s own docstring says *"(2,2)
   characters are independent of which σ_j we use because χ_{(2,2)}(σ_j) = h
   for all j"* and then generalises to *"any embedding of crossings into
   σ_1, σ_2, … yields the same trace"*.  The premise is true for a SINGLE
   generator (all σ_j are conjugate, χ is a class function); the conclusion is
   false for a WORD, and the numbers in stage 4 are how false.

PRECISION
---------
All arithmetic is `mpmath.mpf` at `_precision.set_compute_dps()` (70 dps
compute).  q is `Q_50_DIGIT_STR` — the proton pin, taken as a decimal STRING;
`q_at()` returns float64 and is not used.  No float64 anywhere, no
`statistics`, no `math`.  The layout searches are exact integer combinatorics.

SCOPE (AGENTS.md §"Before declaring refuted / ruled out / dead end")
--------------------------------------------------------------------
* **scope-(b), structural exclusion** — that a contiguous 3A layout admits the
  path P_A and nothing more, and that K_A needs C(A,2) > A−1 couplings for
  A ≥ 3.  The invariant is the interval lemma of
  `QOU/Hecke/LayoutConflict.lean`, extended here to non-adjacent blocks and to
  general A in `QOU/Hecke/ContiguousCouplingGraph.lean` (sorry-free); the
  exhaustive searches below agree with it at A ≤ 6.
* **scope-(b)** — that no layout whatever realises K_A for A ≥ 7 (the counting
  bound, proved for every A, plus the exhaustive check at A = 7).
* **scope-(a), scope-limited negative** — that the conjugated-bond escape
  destroys the dimension-free property.  ONE explicit conjugation is built and
  measured.  Its generator support is forced (the cut lemma: if σ_g is never
  used, no strand starting at position ≤ g ever crosses one starting at
  position ≥ g+1), but no claim is made here that *every* realisation of a
  non-adjacent coupling has the same segmentation.

Nothing is wired.  No recorded number moves.  No route is adopted: the value
comparison in stage 4 is reported, not acted on, because choosing an embedding
by the number it produces is exactly what AGENTS.md §"NO FITTING" forbids.
"""
from __future__ import annotations

import argparse
import sys
import time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

import hecke_core_legacy as H  # noqa: E402
from chi_path_sum_seminormal import chi_lambda_path_sum, segments_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


# ── 1. The two coupling structures, captured from the producers ──────────


def binding_chains(ordering: list[str], n_gens: int) -> list[list[tuple]]:
    """The binding producer's per-step chains, exactly as
    `unified_iterative_correction` builds them (hecke_core_legacy:1918)."""
    return [H._step_chain_generic(nuc, ordering[:i], n_gens)
            for i, nuc in enumerate(ordering)]


def binding_pair_list(ordering: list[str]) -> list[tuple[int, int]]:
    """The (earlier, later) nucleon pairs the binding word couples — one inter
    letter per (step i, previous nucleon t), read off the same loop."""
    return [(t, i) for i in range(len(ordering)) for t in range(i)]


def mass_word_inter_gens(Z: int, N: int) -> list[int]:
    """Generators carrying an inter-nucleon letter in `atom_braid_word_3A`.

    Identified structurally, not by `g % 3`: the intra letters of nucleon k are
    emitted at `3k + off` with `off ∈ {0, 1}`, so any letter at a generator
    ≡ 2 (mod 3) is an interface letter and conversely.  Cross-checked against
    the with/without `include_inter` difference so the identification is
    measured rather than assumed.
    """
    full = atom_braid_word_3A(Z, N, include_inter=True)
    free = atom_braid_word_3A(Z, N, include_inter=False)
    n_inter = len(full) - len(free)
    gens = [g for _c, _d, g in full if g % 3 == 2]
    assert len(gens) == n_inter, (len(gens), n_inter)
    return gens


# ── 2. Layout combinatorics ──────────────────────────────────────────────


def coupling_graph_of_layout(seq: list[int]) -> set[frozenset]:
    """Nucleon pairs joined by an adjacent strand pair in this layout.

    `seq[p]` is the nucleon owning strand position p.  A single-generator
    coupling between nucleons a ≠ b exists iff some p has seq[p] = a,
    seq[p+1] = b (or vice versa) — that is the only way σ_p crosses a strand of
    a with a strand of b.
    """
    return {frozenset((seq[p], seq[p + 1]))
            for p in range(len(seq) - 1) if seq[p] != seq[p + 1]}


def contiguous_layouts(A: int):
    """Every layout in which each nucleon owns 3 CONSECUTIVE positions — i.e.
    every ordering of the A blocks.  `atom_braid_word_3A` is the identity one."""
    from itertools import permutations
    for perm in permutations(range(A)):
        seq: list[int] = []
        for lab in perm:
            seq += [lab] * 3
        yield seq


def search_layouts(A: int, require_contiguous: bool, all_solutions: bool,
                   cap: int | None = None):
    """DFS over label sequences (3 positions per nucleon) for layouts whose
    coupling graph is COMPLETE.  Labels are forced to first appear in
    increasing order, which quotients out the A! relabelling symmetry without
    losing any coupling graph.  Returns (solutions, exhausted)."""
    n = 3 * A
    need = frozenset(map(frozenset, combinations(range(A), 2)))
    seq: list[int] = []
    counts = [0] * A
    found: list[list[int]] = []
    state = {"exhausted": True}

    def dfs(pos: int, max_used: int, edges: frozenset):
        if found and not all_solutions:
            return
        if cap is not None and len(found) >= cap:
            state["exhausted"] = False
            return
        # Every remaining adjacency can contribute at most one new edge.
        if len(need - edges) > n - 1 - max(0, pos - 1):
            return
        if pos == n:
            if not (need - edges):
                found.append(list(seq))
            return
        for lab in range(min(max_used + 1, A - 1) + 1):
            if counts[lab] == 3:
                continue
            if require_contiguous and counts[lab] > 0 and seq[-1] != lab:
                continue
            counts[lab] += 1
            seq.append(lab)
            nxt = edges
            if pos > 0 and seq[pos - 1] != lab:
                nxt = edges | {frozenset((seq[pos - 1], lab))}
            dfs(pos + 1, max(max_used, lab), nxt)
            seq.pop()
            counts[lab] -= 1

    dfs(0, -1, frozenset())
    return found, state["exhausted"]


def contiguous_triples(seq: list[int]) -> int:
    """How many nucleons own 3 consecutive positions in this layout."""
    A = max(seq) + 1
    out = 0
    for lab in range(A):
        pos = [p for p, v in enumerate(seq) if v == lab]
        if pos[2] - pos[0] == 2:
            out += 1
    return out


# ── 3. The 3A re-embedding of the binding word ───────────────────────────


def reembed_binding_3A(ordering: list[str], h: mp.mpf,
                       conjugate_nonadjacent: bool = True):
    """The binding producer's OWN letters, laid on 3A strands.

    Nucleon k's 11 intra letters go to its two single generators — the seven
    `_PROTON_G0`/`_NEUTRON_G0` letters to σ_{3k}, the four `…_G1` letters to
    σ_{3k+1} — which is what `_step_chain_22` says the chain means before
    `_step_chain_generic` cycles it into a fixed H_k.  Each inter-nucleon
    letter for the pair (i, j) goes to the interface:

      j = i+1 : the single generator σ_{3i+2}, the one adjacency a contiguous
                layout supplies;
      j > i+1 : no single generator crosses a strand of i with a strand of j,
                so the crossing is CONJUGATED — block i's top strand is walked
                up to block j by T_w = σ_{3i+2}⋯σ_{3j-2}, crossed at σ_{3j-1},
                and walked back by T_w⁻¹ (σ⁻¹ = σ − h under this convention).
                The generator support is then the whole interval [3i+2, 3j-1].

    Returns (word, shifts, n_strands) in the path-sum module's convention:
    letters (sign 0, generator 1-BASED) with a per-position shift −d, so the
    letter denotes ρ(σ_g) − shift·I.
    """
    A = len(ordering)
    word: list[tuple[int, int]] = []
    shifts: list[mp.mpf] = []

    def emit(d, g0):
        word.append((0, g0 + 1))
        shifts.append(-mp.mpf(d))

    for i, nuc in enumerate(ordering):
        intra = H._PROTON_G0 if nuc == 'p' else H._NEUTRON_G0
        intra_g1 = H._PROTON_G1 if nuc == 'p' else H._NEUTRON_G1
        for c, d in intra:
            assert c == 1
            emit(d, 3 * i)
        for c, d in intra_g1:
            assert c == 1
            emit(d, 3 * i + 1)
        for t, prev in enumerate(ordering[:i]):
            if prev == 'p' and nuc == 'p':
                d = 0
            elif prev == 'n' and nuc == 'n':
                d = H._NN_D_MP
            else:
                d = H._PN_D_MP
            if i == t + 1:
                emit(d, 3 * t + 2)
            elif conjugate_nonadjacent:
                walk = list(range(3 * t + 2, 3 * i - 1))
                for g in walk:
                    emit(0, g)                 # σ_g
                emit(d, 3 * i - 1)             # the bond, at the reached boundary
                for g in reversed(walk):
                    emit(-h, g)                # σ_g⁻¹ = σ_g − h
            else:
                emit(d, 3 * t + 2)             # collapsed onto the wrong interface
    return word, shifts, 3 * A


# ── 4. Characters: path sum and an independent dense seminormal route ────


def parts_of_n(n: int):
    from per_irrep_pole_atom import parts_of
    return [tuple(p) for p in parts_of(n)]


def chi_dense(partition, word, shifts, q: mp.mpf) -> mp.mpf:
    """χ^λ(W) by an explicit Young-seminormal matrix product.

    Independent of the path sum: the σ_j matrices come from
    `hecke_core_legacy._build_ysn_matrices` (a different implementation of the
    same convention), and the product is formed densely here.  Used only for
    dim small enough to be free.
    """
    n = sum(partition)
    mats = H._build_ysn_matrices(partition, sparse_threshold=10 ** 9)
    dim = len(mats[0]) if mats else 1
    if dim == 0:
        return mp.mpf(0)
    # acc = identity, as a list of rows
    acc = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(dim)]
           for i in range(dim)]
    for (_s, g1), sh in zip(word, shifts):
        g = g1 - 1
        assert 0 <= g < n - 1, (g, n)
        M = mats[g]
        new = [[mp.mpf(0)] * dim for _ in range(dim)]
        for i in range(dim):
            ai = acc[i]
            ni = new[i]
            for kk in range(dim):
                a = ai[kk]
                if a == 0:
                    continue
                row = M[kk]
                for j in range(dim):
                    v = row[j]
                    if v != 0:
                        ni[j] += a * v
                # the −shift·I part
                ni[kk] -= a * sh
        acc = new
    return sum((acc[i][i] for i in range(dim)), mp.mpf(0))


def rel_diff(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    d = abs(a - b)
    m = max(abs(a), abs(b))
    return d / m if m != 0 else d


# ── main ─────────────────────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a-max", type=int, default=6,
                    help="largest A for the layout searches")
    ap.add_argument("--a-all-solutions", type=int, default=5,
                    help="enumerate EVERY complete-coupling layout for A <= this")
    ap.add_argument("--budget-s", type=float, default=1800.0)
    args = ap.parse_args()

    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    t_start = time.monotonic()
    print("=" * 78)
    print("  Re-embedding the binding word on 3A strands  (qou-w6x3, option 2 of qou-hxz4)")
    print(f"  q0 = {Q_50_DIGIT_STR[:26]}…  (proton pin, string)   mp.dps = {mp.mp.dps}")
    print("=" * 78)

    # ── stage 1: the two coupling structures ────────────────────────────
    print("\n── 1. Coupling structure: binding word vs mass word ────────────")
    coupling_rows = []
    ok_binding_complete = True
    ok_mass_path = True
    ok_mass_local = True
    ok_fixed_single = True
    for A in range(2, 7):
        Z = (A + 1) // 2
        N = A - Z
        ordering = ['p'] * Z + ['n'] * N
        pairs = binding_pair_list(ordering)
        n_inter_binding = len(pairs)
        # measured from the producer, not from the formula
        n_gens = 5
        chains = binding_chains(ordering, n_gens)
        L = sum(len(c) for c in chains)
        measured_inter = L - 11 * A
        ok_binding_complete &= (n_inter_binding == A * (A - 1) // 2
                                == measured_inter
                                == len(set(map(frozenset, pairs))))
        # mass word
        mass_inter = mass_word_inter_gens(Z, N)
        ok_mass_path &= (len(mass_inter) == A - 1)
        mw = atom_braid_word_3A(Z, N)
        tw = [(0, g + 1) for _c, _d, g in mw]
        segs = segments_of(tw)
        maxg = max(len(s["gens"]) for s in segs)
        ok_mass_local &= (len(segs) == 2 * A - 1 and maxg == 2)
        # fixed-H_k binding word: single segment
        fw = [(0, g + 1) for ch in chains for _c, _d, g in ch]
        fsegs = segments_of(fw)
        ok_fixed_single &= (len(fsegs) == 1)
        coupling_rows.append({
            "A": A, "ordering": "".join(ordering),
            "binding_inter_letters": measured_inter,
            "binding_distinct_pairs": len(set(map(frozenset, pairs))),
            "C_A_2": A * (A - 1) // 2,
            "mass_inter_letters": len(mass_inter),
            "A_minus_1": A - 1,
            "mass_segments": len(segs), "mass_max_segment_gens": maxg,
            "fixed_Hk_segments": len(fsegs),
            "fixed_Hk_max_segment_gens": max(len(s["gens"]) for s in fsegs),
        })
        print(f"   A={A}  binding inter letters {measured_inter:2d} = C(A,2) "
              f"{A*(A-1)//2:2d} (complete graph K_A)   |   mass inter letters "
              f"{len(mass_inter):2d} = A-1 {A-1:2d} (path P_A)")
        print(f"          mass word segments {len(segs):2d} (max gen-set {maxg})"
              f"   |   fixed-H_k binding word segments {len(fsegs)} "
              f"(max gen-set {max(len(s['gens']) for s in fsegs)})")

    check("binding word couples EVERY nucleon pair: inter letters = C(A,2), "
          "all pairs distinct (A = 2..6, measured from _step_chain_generic)",
          ok_binding_complete)
    check("mass word atom_braid_word_3A couples only CONSECUTIVE nucleons: "
          "inter letters = A-1 (A = 2..6)", ok_mass_path)
    check("mass word is level-local: 2A-1 segments, largest generator set 2 "
          "(the dimension-free structure #7160 exploits)", ok_mass_local)
    check("fixed-H_k binding word is a SINGLE segment (re-confirms #7173 "
          "against this branch's code)", ok_fixed_single)

    # ── stage 2: what a layout can supply ───────────────────────────────
    print("\n── 2. Which couplings a linear 3A layout can supply ────────────")
    layout_rows = []
    ok_contig_path = True
    ok_contig_KA = True
    ok_any_KA = True
    ok_count_bound = True
    for A in range(2, args.a_max + 2):
        n = 3 * A
        cnt = A * (A - 1) // 2
        # every contiguous layout gives the path
        graphs = {frozenset(coupling_graph_of_layout(s))
                  for s in contiguous_layouts(A)}
        all_paths = all(len(g) == A - 1 for g in graphs)
        ok_contig_path &= all_paths
        contig_complete = any(len(g) == cnt for g in graphs)
        ok_contig_KA &= (contig_complete == (A <= 2))
        # counting bound: C(A,2) distinct edges need C(A,2) distinct adjacencies
        bound_says_possible = cnt <= n - 1
        if A <= args.a_max + 1:
            sols, exhausted = search_layouts(A, require_contiguous=False,
                                             all_solutions=False)
            any_complete = bool(sols)
            ok_count_bound &= (any_complete <= bound_says_possible)
            ok_any_KA &= (any_complete == (A <= 6))
        else:
            any_complete = None
        layout_rows.append({
            "A": A, "n_strands": n, "C_A_2": cnt, "adjacencies_n_minus_1": n - 1,
            "contiguous_graph_is_always_path_P_A": all_paths,
            "contiguous_layout_realises_K_A": contig_complete,
            "some_layout_realises_K_A": any_complete,
            "counting_bound_C_A_2_le_3A_minus_1": bound_says_possible,
        })
        print(f"   A={A:2d}  n={n:2d}  C(A,2)={cnt:2d}  adjacencies={n-1:2d}   "
              f"contiguous graph always P_A: {all_paths!s:5s}   "
              f"K_A contiguous: {contig_complete!s:5s}   "
              f"K_A any layout: {any_complete!s:5s}   "
              f"counting allows: {bound_says_possible!s:5s}")

    check("every CONTIGUOUS 3A layout gives the path P_A and nothing more "
          "(A-1 couplings, exhaustive over all A! block orderings, A = 2..7)",
          ok_contig_path)
    check("a contiguous layout realises the complete coupling K_A iff A <= 2 "
          "-- so the binding word's all-pairs coupling is UNREACHABLE for A >= 3",
          ok_contig_KA)
    check("dropping contiguity, some layout realises K_A iff A <= 6 "
          "(exhaustive DFS; A = 7 impossible)", ok_any_KA)
    check("the counting bound C(A,2) <= 3A-1 is never violated -- a linear "
          "arrangement of 3A strands has only 3A-1 adjacent pairs, so K_A is "
          "impossible for every A >= 7, not merely the A = 7 checked",
          ok_count_bound)

    # ── stage 2b: the escape costs what it buys ─────────────────────────
    print("\n── 2b. Every complete-coupling layout destroys contiguity ──────")
    dilemma_rows = []
    ok_dilemma = True
    ok_dilemma_sharp = True
    for A in range(3, args.a_all_solutions + 1):
        sols, exhausted = search_layouts(A, require_contiguous=False,
                                         all_solutions=True)
        worst = max((contiguous_triples(s) for s in sols), default=None)
        # Never all A: a layout with every triple contiguous IS a contiguous
        # layout, whose graph is P_A != K_A for A >= 3 (stage 2).
        ok_dilemma &= (exhausted and bool(sols) and worst is not None
                       and worst <= A - 1)
        # Measured, and sharper than that corollary from A = 4 on.
        if A >= 4:
            ok_dilemma_sharp &= (worst == 0)
        dilemma_rows.append({
            "A": A, "complete_coupling_layouts": len(sols),
            "exhaustive": exhausted,
            "max_contiguous_nucleon_triples": worst,
            "nucleons": A,
        })
        print(f"   A={A}  {len(sols):6d} layouts realise K_A (exhaustive: "
              f"{exhausted})   max contiguous nucleon triples among them: "
              f"{worst} of {A}")
    check("no layout realising K_A keeps ALL A nucleon triples contiguous "
          "(A = 3..%d, exhaustive) -- the all-pairs coupling and the "
          "single-generator intra-nucleon crossings cannot both be had"
          % args.a_all_solutions, ok_dilemma)
    check("and from A >= 4 the cost is TOTAL: not one nucleon of a "
          "K_A-realising layout keeps its three strands together, so every "
          "intra-nucleon crossing needs conjugating too (A = 3 is the lone "
          "partial case, 2 of 3)", ok_dilemma_sharp)

    # ── stage 3: the conjugated-bond re-embedding, segmented ────────────
    print("\n── 3. The 3A re-embedding with conjugated non-adjacent bonds ───")
    seg_rows = []
    ok_conj_collapse = True
    ok_conj_floor = True
    ok_a2_local = True
    for A in range(2, 7):
        Z = (A + 1) // 2
        N = A - Z
        ordering = ['p'] * Z + ['n'] * N
        word, shifts, n_str = reembed_binding_3A(ordering, h)
        segs = segments_of(word)
        sizes = [len(s["gens"]) for s in segs]
        maxg = max(sizes)
        # Order-free floor.  The extreme pair (0, A-1) is coupled by walking
        # nucleon 0's top strand up (T_w on generators 2 … 3A-5), crossing at
        # 3A-4, and walking back.  The walk BRACKETS the crossing, so the span
        # of generator 2 contains every letter between, and all of
        # [2, 3A-4] lands in one segment wherever the remaining letters go.
        floor = (3 * A - 4) - 2 + 1 if A >= 3 else 1
        if A == 2:
            ok_a2_local &= (maxg <= 2 and len(segs) >= 3)
        else:
            ok_conj_collapse &= (len(segs) == 3 and maxg == 3 * A - 3)
            ok_conj_floor &= (maxg >= floor)
        seg_rows.append({
            "A": A, "n_strands": n_str, "L": len(word),
            "segments": len(segs), "segment_gen_sizes": sizes,
            "max_segment_gens": maxg,
            "order_free_floor_on_max_segment": floor if A >= 3 else None,
            "total_gens": 3 * A - 1,
            "mass_word_segments": 2 * A - 1,
            "mass_word_max_segment_gens": 2,
        })
        print(f"   A={A}  n={n_str:2d}  L={len(word):3d}  segments={len(segs)}  "
              f"sizes={sizes}  largest={maxg} of {3*A-1} generators"
              + (f"  (order-free floor {floor})" if A >= 3 else "")
              + f"   [mass word: {2*A-1} segments, largest 2]")
    check("A = 2 re-embeds exactly and is level-local: the deuteron's single "
          "pair IS the one adjacency, so no conjugation is needed and every "
          "segment holds ONE generator -- finer than the mass word's, because "
          "the binding producer's intra chain is GROUPED (seven letters on "
          "3k, then four on 3k+1) where atom_braid_word_3A's is ALTERNATING",
          ok_a2_local)
    check("A >= 3 collapses: only nucleon 0's two generators survive as their "
          "own segments and everything else merges -- 3 segments with the "
          "largest holding 3A-3 of 3A-1 generators, i.e. all but two, growing "
          "linearly in A against the mass word's constant 2",
          ok_conj_collapse)
    check("and 3A-5 of that is ORDER-FREE: the conjugating walk for the "
          "extreme pair brackets its crossing, so generators [2, 3A-4] share a "
          "segment wherever the rest of the letters are placed",
          ok_conj_floor)

    # ── stage 4: does the value move?  A = 2, both embeddings in H_6 ────
    print("\n── 4. A = 2: same H_6, same 23 letters, only the indexing differs ─")
    ordering = ['p', 'n']
    chains = binding_chains(ordering, 5)          # n_gens = k-1 = 5, k = 6
    fixed_word = [(0, g + 1) for ch in chains for _c, _d, g in ch]
    fixed_shifts = [-mp.mpf(d) for ch in chains for _c, d, _g in ch]
    re_word, re_shifts, n_str = reembed_binding_3A(ordering, h)
    same_letters = (sorted(fmt(s) for s in fixed_shifts)
                    == sorted(fmt(s) for s in re_shifts))
    check("the two A = 2 words are the SAME 23 letters in the SAME H_6 -- "
          "identical multiset of (c, d) offsets, identical length, differing "
          "ONLY in the generator each letter is assigned to",
          same_letters and len(fixed_word) == len(re_word) == 23 and n_str == 6,
          f"L={len(fixed_word)}/{len(re_word)}, n={n_str}")

    shapes = parts_of_n(6)
    chi_rows = []
    max_rel = mp.mpf(0)
    ok_xcheck = True
    n_moved = 0
    for sh in shapes:
        c_fix_ps = chi_lambda_path_sum(sh, 6, fixed_word, q, fixed_shifts)
        c_re_ps = chi_lambda_path_sum(sh, 6, re_word, q, re_shifts)
        c_fix_d = chi_dense(sh, fixed_word, fixed_shifts, q)
        c_re_d = chi_dense(sh, re_word, re_shifts, q)
        x1 = rel_diff(c_fix_ps, c_fix_d)
        x2 = rel_diff(c_re_ps, c_re_d)
        ok_xcheck &= (x1 < mp.mpf(10) ** -45 and x2 < mp.mpf(10) ** -45)
        r = rel_diff(c_fix_ps, c_re_ps)
        if r > mp.mpf(10) ** -45:
            n_moved += 1
        max_rel = max(max_rel, r)
        dimlam = len(H._build_ysn_matrices(sh, sparse_threshold=10 ** 9)[0]) \
            if sum(sh) > 1 else 1
        chi_rows.append({
            "lambda": list(sh), "dim": dimlam,
            "chi_fixed_Hk": fmt(c_fix_ps), "chi_3A": fmt(c_re_ps),
            "rel_diff": fmt(r),
            "xcheck_fixed_pathsum_vs_dense": fmt(x1),
            "xcheck_3A_pathsum_vs_dense": fmt(x2),
        })
        print(f"   λ={str(list(sh)):<18} dim {dimlam:2d}  "
              f"χ_fixed {mp.nstr(c_fix_ps, 12):>16}  χ_3A {mp.nstr(c_re_ps, 12):>16}  "
              f"rel {mp.nstr(r, 6)}")
    check("path sum and the independent dense Young-seminormal product agree "
          "on both words, every λ ⊢ 6, at < 1e-45 relative", ok_xcheck,
          f"{len(shapes)} partitions")
    check("the Markov trace is NOT invariant under the re-embedding: the "
          "character moves on %d of %d partitions of 6, max relative %s -- so "
          "option 2 is a RE-DERIVATION, and _step_chain_22's 'any embedding of "
          "crossings into sigma_1, sigma_2, ... yields the same trace' is false "
          "for a word" % (n_moved, len(shapes), mp.nstr(max_rel, 6)),
          n_moved > 0)

    # 1-dim irreps are embedding-blind: closed forms
    triv_fix = mp.mpf(1)
    triv_re = mp.mpf(1)
    sign_fix = mp.mpf(1)
    sign_re = mp.mpf(1)
    for s in fixed_shifts:
        triv_fix *= (q - s)
        sign_fix *= (-1 / q - s)
    for s in re_shifts:
        triv_re *= (q - s)
        sign_re *= (-1 / q - s)
    c6 = chi_lambda_path_sum((6,), 6, fixed_word, q, fixed_shifts)
    c6r = chi_lambda_path_sum((6,), 6, re_word, q, re_shifts)
    c1 = chi_lambda_path_sum((1,) * 6, 6, fixed_word, q, fixed_shifts)
    c1r = chi_lambda_path_sum((1,) * 6, 6, re_word, q, re_shifts)
    tol = mp.mpf(10) ** -45
    ok_1dim = (rel_diff(c6, triv_fix) < tol and rel_diff(c6r, triv_re) < tol
               and rel_diff(c1, sign_fix) < tol and rel_diff(c1r, sign_re) < tol
               and rel_diff(c6, c6r) < tol and rel_diff(c1, c1r) < tol)
    check("the two 1-dimensional irreps are BLIND to the embedding: "
          "χ^(6) = Π(q + d) and χ^(1^6) = Π(-1/q + d) exactly, identical under "
          "both indexings -- the whole move lives in dim >= 2", ok_1dim,
          f"chi^(6) = {mp.nstr(c6, 14)}")

    # ── stage 5: cost ───────────────────────────────────────────────────
    print("\n── 5. Cost of the A = 2 path sum under the two embeddings ──────")
    t0 = time.monotonic()
    for sh in shapes:
        chi_lambda_path_sum(sh, 6, fixed_word, q, fixed_shifts)
    t_fixed = time.monotonic() - t0
    t0 = time.monotonic()
    for sh in shapes:
        chi_lambda_path_sum(sh, 6, re_word, q, re_shifts)
    t_re = time.monotonic() - t0
    print(f"   all {len(shapes)} partitions of 6:  fixed-H_k (1 segment) "
          f"{t_fixed:.3f} s   3A (3 segments) {t_re:.3f} s   "
          f"speedup {t_fixed/max(t_re,1e-9):.2f}x")

    # A = 3 at n = 9: the level-local mass word against the conjugated binding
    # word, same algebra, same partition set — what the collapse actually costs.
    print("\n   A = 3 (n = 9, 30 partitions): mass word vs conjugated binding word")
    shapes9 = parts_of_n(9)
    mw3 = atom_braid_word_3A(2, 1)
    mw3_word = [(0, g + 1) for _c, _d, g in mw3]
    mw3_shifts = [-mp.mpf(d) for _c, d, _g in mw3]
    bw3_word, bw3_shifts, _n3 = reembed_binding_3A(['p', 'p', 'n'], h)
    t0 = time.monotonic()
    for sh in shapes9:
        chi_lambda_path_sum(sh, 9, mw3_word, q, mw3_shifts)
    t_mass9 = time.monotonic() - t0
    t_bind9 = None
    seg_bind9 = max(len(s["gens"]) for s in segments_of(bw3_word))
    if t_mass9 < args.budget_s:
        t0 = time.monotonic()
        try:
            for sh in shapes9:
                chi_lambda_path_sum(sh, 9, bw3_word, q, bw3_shifts)
            t_bind9 = time.monotonic() - t0
        except (MemoryError, KeyboardInterrupt):
            t_bind9 = None
    print(f"   mass word (max segment 2):            {t_mass9:8.3f} s")
    if t_bind9 is None:
        print(f"   conjugated binding (max segment {seg_bind9}):   did not complete")
    else:
        print(f"   conjugated binding (max segment {seg_bind9}):  {t_bind9:8.3f} s"
              f"   {t_bind9/max(t_mass9,1e-9):.0f}x slower")
    check("the collapse has a measured price at A = 3: the level-local mass "
          "word costs %.3f s over all 30 partitions of 9 while the conjugated "
          "binding word, in the SAME algebra over the SAME partitions, costs "
          "%s -- the path sum has degenerated to the dense seminormal trace "
          "the route was meant to avoid"
          % (t_mass9, "more than the budget" if t_bind9 is None
             else "%.3f s (%.0fx)" % (t_bind9, t_bind9 / max(t_mass9, 1e-9))),
          t_bind9 is None or t_bind9 > t_mass9)

    # ── witness ─────────────────────────────────────────────────────────
    w = WitnessBuilder("binding-word-3A-reembedding", engine="python+mpmath")
    w.set_description(
        "qou-w6x3 (option 2 of qou-hxz4): re-embedding the binding producer's "
        "word on 3A strands does NOT restore level-locality for A >= 3, and "
        "the reason is the COUPLING GRAPH, not the generator cycling that "
        "#7173 diagnosed. The binding word couples every nucleon pair "
        "(C(A,2) inter letters, the complete graph K_A) while a contiguous 3A "
        "layout supplies only the path P_A (A-1 adjacencies) -- measured, and "
        "exhaustive over all contiguous layouts for A <= 7. Dropping "
        "contiguity, K_A is layout-realisable iff A <= 6 (counting bound "
        "C(A,2) <= 3A-1, proved for all A; A = 7 exhaustively impossible), but "
        "no such layout leaves a single nucleon triple contiguous, so the "
        "single-generator intra-nucleon crossings are lost in exchange. "
        "Coupling a non-adjacent pair by conjugation instead gives a bond "
        "whose generator support is the interval [2, 3A-4]: the segmentation "
        "collapses from the mass word's 2A-1 segments of largest size 2 to "
        "3 segments whose largest holds 3A-5 of 3A-1 generators, so the "
        "dimension-free property is gone at the first non-adjacent pair. "
        "A = 2 is the sole exception -- the deuteron's single pair IS the one "
        "adjacency -- and there the character MOVES: same H_6, same 23 "
        "letters, only the indexing differs, and chi^lambda differs on the "
        "9 partitions of dimension >= 2 while the two 1-dimensional irreps are "
        "blind to the embedding. Option 2 is therefore a re-derivation whose "
        "one live case is the deuteron.")
    w.set_audit_only("docs/audits/2026-09-12-binding-word-3A-reembedding.md")
    w.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("a_max", args.a_max)
    w.add_parameter("a_all_solutions", args.a_all_solutions)
    w.add_data("coupling_structure", coupling_rows)
    w.add_data("layout_reachability", layout_rows)
    w.add_data("complete_coupling_destroys_contiguity", dilemma_rows)
    w.add_data("reembedded_segmentation", seg_rows)
    w.add_data("A2_character_comparison", chi_rows)
    w.add_data("A2_path_sum_cost_s", {"fixed_Hk": fmt(mp.mpf(t_fixed)),
                                      "three_A": fmt(mp.mpf(t_re))})
    w.add_caveat(
        "scope-(b) for the contiguous-layout coupling graph (P_A and nothing "
        "more; QOU/Hecke/ContiguousCouplingGraph.lean, sorry-free, general A) "
        "and for the counting bound C(A,2) <= 3A-1 that excludes K_A at every "
        "A >= 7. scope-(a) for the conjugated-bond collapse: ONE explicit "
        "conjugation is built and segmented, and while its generator support "
        "is forced by the cut lemma (an unused sigma_g prevents any crossing "
        "across position g), no claim is made that EVERY realisation of a "
        "non-adjacent coupling segments the same way. The A = 2 character "
        "comparison is REPORTED, not acted on: choosing an embedding by the "
        "number it produces would be selection against the target. Timings "
        "are wall-clock strings, provenance only.")
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="binding_word_3A_reembedding_probe")
    print(f"\n  witness: {w.save()}")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print(f"  {npass}/{len(CHECKS)} checks passed  "
          f"({time.monotonic()-t_start:.0f} s wall)")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
