#!/usr/bin/env python3
"""χ^λ(T_β) as a dim-free PATH SUM over standard Young tableaux — the seminormal
trace of a *level-local* braid word without ever building V_λ.

WHY THIS EXISTS (bean qou-s7ld; measurements in
docs/audits/2026-09-07-chi-scaling-wall-level-local-path-sum.md)
---------------------------------------------------------------------------
The canonical Rust route `pyhecke_native.chi_q_via_gp` costs 1.2 ms / 26 ms /
5.6 s per λ at n = 6 / 9 / 12 and did not finish 40 of ⁵Li's 176 partitions in
3 h 35 m (bean qou-d9wf).  Measured here, the cost is NOT the T_w-basis
expansion — the atom word's support is exactly 6^A (36 / 216 / 1296 / 7776 /
46656 at n = 6 … 18) — and NOT dim V_λ.  It is `reduce_basis_to_minimal_length_complete`:
Hecke conjugation `T_w ↦ T_s T_w T_s⁻¹` spreads the 6^A chain support toward
n!, with a BFS cyclic-shift completion and an O(|support|) rescan per step.
At n = 12, λ = [12]: expansion + Hoefsmit-per-T_w (no reduction) 62 ms; direct
seminormal < 1 ms; `chi_q_via_gp` 7385 ms.

The direct seminormal trace, `chi_lambda_braid_mpfr`, is O(L · dim²) — fine
while dim is small, but Σ_λ dim_λ² = n! (1.3e12 at n = 15), so it is a
different wall of the same height.

THE STRUCTURE THAT REMOVES BOTH WALLS
-------------------------------------
`mass_at_3A_proper.atom_braid_word_3A` is a chain: nucleon k is an 11-letter
word on generators {3k+1, 3k+2}, and consecutive nucleons are joined by ONE
bond letter σ_{3k+3}.  In Young's seminormal basis ρ(σ_i) mixes a tableau T only
with s_i·T (entries i, i+1 swapped), i.e. it changes only the shape λ^{(i)} at
level i of the path ∅ ⊂ λ^{(1)} ⊂ … ⊂ λ^{(n)} = λ.  So the word factors as
T_β = F_1 F_2 ⋯ F_m with the F_j acting on PAIRWISE DISJOINT level sets, and
then

    ⟨T | F_1 ⋯ F_m | T⟩ = Π_j ⟨T | F_j | T⟩        for every SYT T

(every intermediate tableau in the matrix-product expansion is forced back to T
because no later factor can undo a change at a level it does not touch).  Hence

    χ^λ(T_β) = Σ_{T ∈ SYT(λ)} Π_j ⟨T | F_j | T⟩ ,

and ⟨T|F_j|T⟩ depends only on the boxes of the entries F_j touches (their
contents fix the Hoefsmit axial distances; row/column adjacency fixes which
swaps are standard).  The sum over SYT(λ) is therefore a transfer-matrix
contraction along the chain of shapes whose state is (shape, box of the last
entry) — the number of standard tableaux never appears.  Cost per λ is
O(#sub-shapes · #local fillings · L_seg · orbit²) with orbit ≤ 6, i.e.
milliseconds at n = 18 where the seminormal matrix has dim up to 6e5.

This is exact, not an approximation: the identity is a re-bracketing of the
trace of a product of sparse matrices.  It holds for σ, σ⁻¹ AND the averaged /
colour-weighted crossings `σ − d·I` (sign 0 with a per-position shift), because
those are still level-local.  It does NOT hold for a word in which some
generator recurs after a different generator's segment has closed over it — the
segmentation below detects that and raises rather than returning a wrong number.

CONVENTION — identical to `tools/hecke-engine/src/seminormal_mpfr.rs::build_blocks_mpfr`
--------------------------------------------------------------------------------------
Hecke relation (σ − q)(σ + q⁻¹) = 0, h = q − q⁻¹.  For entries k, k+1 in boxes
of content c_k, c_{k+1} (content = col − row), ρ = c_{k+1} − c_k:

    diagonal   a = h / (1 − q^{−2ρ})          (ρ = ±1 ⇒ a = q, −q⁻¹; no partner)
    partner    a' = h / (1 − q^{2ρ}),  b = √(a·a' + 1)   (symmetric form)
    σ⁻¹ = σ − h·I ;  averaged / weighted crossing = σ − shift·I  (default shift h/2)

Precision: all arithmetic is `mpmath.mpf` at `_precision.set_compute_dps()`
(70 dps compute); q is taken as a decimal STRING.  No float64 anywhere.

Cross-checks (`--selftest`): every partition of n = 6 / 9 against the Rust
seminormal kernel `chi_lambdas_braid_mpfr` (independent implementation, same
convention) and every partition of the committed D / T / ³He / ⁴He lossless
caches, all at the 50-dps floor.
"""
from __future__ import annotations

import json
import sys
import time
from functools import lru_cache
from pathlib import Path

import mpmath as mp

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Box = tuple[int, int]


class NotLevelLocal(ValueError):
    """The word cannot be factored into segments with disjoint generator sets."""


# ── Segmentation ─────────────────────────────────────────────────────────


def segments_of(word: list[tuple[int, int]]) -> list[dict]:
    """Factor `word` into maximal contiguous segments with pairwise-disjoint
    generator sets.

    Two occurrences of the same generator must lie in one segment, and a
    segment is contiguous in the word, so the segments are the connected
    components of the intervals [first(g), last(g)].  Each segment records its
    generator set (1-based) and its letters `(sign, gen)` in word order.
    Segments are returned sorted by their smallest generator (the diagonal
    product is order-independent; the letters inside a segment keep word
    order).
    """
    first: dict[int, int] = {}
    last: dict[int, int] = {}
    for p, (_s, g) in enumerate(word):
        first.setdefault(g, p)
        last[g] = p
    spans = sorted((first[g], last[g]) for g in first)
    merged: list[list[int]] = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    segs = []
    for s, e in merged:
        letters = [tuple(word[p]) for p in range(s, e + 1)]
        gens = sorted({g for _sg, g in letters})
        segs.append({"start": s, "end": e, "gens": gens, "letters": letters})
    # Disjointness is guaranteed by construction; check it anyway.
    seen: set[int] = set()
    for sg in segs:
        if seen & set(sg["gens"]):
            raise NotLevelLocal("segments share a generator")
        seen |= set(sg["gens"])
    segs.sort(key=lambda sg: sg["gens"][0])
    return segs


# ── Local diagonal entries ──────────────────────────────────────────────


def _content(b: Box) -> int:
    return b[1] - b[0]


def _swap_standard(b1: Box, b2: Box) -> bool:
    """Swapping consecutive entries in boxes b1, b2 keeps the tableau standard
    iff the boxes share neither a row nor a column (same row/col ⇒ adjacent)."""
    return b1[0] != b2[0] and b1[1] != b2[1]


class SegmentWeight:
    """⟨T | F_seg | T⟩ as a function of the boxes of the entries the segment
    touches, memoised on that box tuple.

    `gens` are 1-based generator indices; entries touched are
    `a .. b+1` with a = min(gens), b = max(gens).  `boxes` is the tuple of boxes
    of entries a, a+1, …, b+1 in T.
    """

    def __init__(self, gens: list[int], letters: list[tuple[int, int]],
                 q: mp.mpf, shifts: list | None):
        self.gens = gens
        self.a = gens[0]
        self.b = gens[-1]
        self.letters = letters
        self.q = q
        self.h = q - 1 / q
        # Per-letter shift for sign == 0 (default h/2); ignored otherwise.
        self.shifts = shifts if shifts is not None else [self.h / 2] * len(letters)
        self._cache: dict[tuple[Box, ...], mp.mpf] = {}

    def _orbit(self, boxes: tuple[Box, ...]) -> tuple[list[tuple[Box, ...]], dict]:
        """All standard re-fillings of the touched boxes reachable by the
        segment's swaps (BFS).  Node = tuple of boxes indexed by entry offset."""
        idx = {boxes: 0}
        nodes = [boxes]
        k = 0
        while k < len(nodes):
            t = nodes[k]
            k += 1
            for g in self.gens:
                i = g - self.a
                if _swap_standard(t[i], t[i + 1]):
                    u = list(t)
                    u[i], u[i + 1] = u[i + 1], u[i]
                    u = tuple(u)
                    if u not in idx:
                        idx[u] = len(nodes)
                        nodes.append(u)
        return nodes, idx

    def _gen_matrix(self, g: int, nodes, idx):
        """Sparse ρ(σ_g) on the orbit basis: list of (diag a, partner index or
        None, b)."""
        i = g - self.a
        q, h = self.q, self.h
        rows = []
        for t in nodes:
            rho = _content(t[i + 1]) - _content(t[i])
            a = h / (1 - q ** (-2 * rho))
            if _swap_standard(t[i], t[i + 1]):
                u = list(t)
                u[i], u[i + 1] = u[i + 1], u[i]
                j = idx[tuple(u)]
                ap = h / (1 - q ** (2 * rho))
                b = mp.sqrt(a * ap + 1)
                rows.append((a, j, b))
            else:
                rows.append((a, None, None))
        return rows

    def weight(self, boxes: tuple[Box, ...]) -> mp.mpf:
        w = self._cache.get(boxes)
        if w is not None:
            return w
        nodes, idx = self._orbit(boxes)
        mats = {g: self._gen_matrix(g, nodes, idx) for g in self.gens}
        # v = e_T ; apply letters right-to-left so v = F_seg · e_T.
        v = [mp.mpf(0)] * len(nodes)
        v[0] = mp.mpf(1)
        for pos in range(len(self.letters) - 1, -1, -1):
            sign, g = self.letters[pos]
            rows = mats[g]
            if sign > 0:
                d = mp.mpf(0)
            elif sign < 0:
                d = self.h
            else:
                d = self.shifts[pos]
            new = [None] * len(nodes)
            for r, (a, j, b) in enumerate(rows):
                x = (a - d) * v[r]
                if j is not None:
                    x += b * v[j]
                new[r] = x
            v = new
        w = v[0]
        self._cache[boxes] = w
        return w


# ── Path sum over shapes ─────────────────────────────────────────────────


def _addable(shape: tuple[int, ...], lam: tuple[int, ...]):
    """Boxes addable to `shape` staying inside `lam`, as (new_shape, box)."""
    out = []
    rows = len(shape)
    for r in range(rows + 1):
        cur = shape[r] if r < rows else 0
        if r >= len(lam) or cur >= lam[r]:
            continue
        if r > 0 and shape[r - 1] <= cur:
            continue
        new = list(shape) + ([0] if r == rows else [])
        new[r] = cur + 1
        out.append((tuple(new), (r, cur)))
    return out


def _fillings(shape: tuple[int, ...], lam: tuple[int, ...], m: int):
    """All standard placements of m further entries: yields (final_shape, boxes)."""
    if m == 0:
        yield shape, ()
        return
    for new, box in _addable(shape, lam):
        for fin, rest in _fillings(new, lam, m - 1):
            yield fin, (box,) + rest


def chi_lambda_path_sum(shape, n: int, word: list[tuple[int, int]], q: mp.mpf,
                        shifts: list | None = None,
                        _segs: list | None = None) -> mp.mpf:
    """χ^λ(T_β) for a level-local word, as the SYT path sum.  Exact identity —
    see the module docstring.  Raises NotLevelLocal if the word does not
    factor."""
    lam = tuple(shape)
    if sum(lam) != n:
        return mp.mpf(0)
    segs = _segs if _segs is not None else build_segments(word, q, shifts)
    # DP state: (shape_k, box of entry k) -> accumulated weight, at entry k.
    states: dict[tuple[tuple[int, ...], Box | None], mp.mpf] = {((), None): mp.mpf(1)}
    k = 0
    for sw in segs:
        a, b = sw.a, sw.b
        # Place entries k+1 .. a freely (untouched levels carry weight 1).
        while k < a:
            nxt: dict = {}
            for (sh, _bx), wgt in states.items():
                for new, box in _addable(sh, lam):
                    key = (new, box)
                    nxt[key] = nxt.get(key, mp.mpf(0)) + wgt
            states = nxt
            k += 1
        if k != a:
            raise NotLevelLocal(f"segment starting at generator {a} reached after entry {k}")
        # Now entry a is placed; add entries a+1 .. b+1 with the segment weight.
        m = b + 1 - a
        nxt = {}
        for (sh, bx), wgt in states.items():
            for fin, boxes in _fillings(sh, lam, m):
                w = sw.weight((bx,) + boxes)
                if w == 0:
                    continue
                key = (fin, boxes[-1])
                nxt[key] = nxt.get(key, mp.mpf(0)) + wgt * w
        states = nxt
        k = b + 1
    while k < n:
        nxt = {}
        for (sh, _bx), wgt in states.items():
            for new, box in _addable(sh, lam):
                key = (new, box)
                nxt[key] = nxt.get(key, mp.mpf(0)) + wgt
        states = nxt
        k += 1
    return sum((w for (sh, _bx), w in states.items() if sh == lam), mp.mpf(0))


def build_segments(word, q: mp.mpf, shifts: list | None = None) -> list[SegmentWeight]:
    """Segment the word once (shared across all λ)."""
    segs = []
    for sg in segments_of(word):
        seg_shifts = None
        if shifts is not None:
            seg_shifts = [shifts[p] for p in range(sg["start"], sg["end"] + 1)]
        segs.append(SegmentWeight(sg["gens"], sg["letters"], q, seg_shifts))
    # A generator index must not exceed n-1; checked by the caller via n.
    return segs


def chi_all_partitions_path_sum(n: int, word, q: mp.mpf, shifts=None,
                                shapes=None, progress=None):
    """{shape: χ^λ} for every λ ⊢ n (or the given shapes)."""
    from per_irrep_pole_atom import parts_of
    segs = build_segments(word, q, shifts)
    if max(g for _s, g in word) >= n:
        raise ValueError("generator index out of range for n")
    shapes = list(shapes) if shapes is not None else parts_of(n)
    out = {}
    t0 = time.monotonic()
    for i, sh in enumerate(shapes):
        out[tuple(sh)] = chi_lambda_path_sum(sh, n, word, q, shifts, _segs=segs)
        if progress and (i + 1) % progress == 0:
            el = time.monotonic() - t0
            print(f"     [{i+1}/{len(shapes)}] {el:.1f}s  ETA {el/(i+1)*(len(shapes)-i-1):.1f}s",
                  flush=True)
    return out


# ── Self-test ────────────────────────────────────────────────────────────


def _selftest() -> int:
    set_compute_dps()
    from derived_chi_catalogue_matrix_m import _word_for_braid_word_3a
    from per_irrep_pole_atom import parts_of
    q = mp.mpf(Q_50_DIGIT_STR)
    floor = mp.mpf(10) ** -48   # relative, against 50-dps decimal strings
    fails = 0

    # 1. Against the Rust seminormal kernel (independent implementation).
    try:
        import pyhecke_native as ph
    except ImportError:
        ph = None
        print("  [SKIP] pyhecke_native not importable — Rust cross-check skipped")
    if ph is not None:
        for Z, N in [(1, 1), (2, 1)]:
            n, word = _word_for_braid_word_3a(Z, N)
            shapes = parts_of(n)
            t0 = time.monotonic()
            mine = chi_all_partitions_path_sum(n, word, q)
            t_mine = time.monotonic() - t0
            t0 = time.monotonic()
            rust = ph.chi_lambdas_braid_mpfr([list(s) for s in shapes], list(word),
                                             Q_50_DIGIT_STR, 50)
            t_rust = time.monotonic() - t0
            worst = mp.mpf(0)
            for s, r in zip(shapes, rust):
                r = mp.mpf(r)
                rel = abs(mine[s] - r) / max(abs(r), mp.mpf(1))
                worst = max(worst, rel)
            ok = worst < floor
            fails += 0 if ok else 1
            print(f"  [{'PASS' if ok else 'FAIL'}] n={n}: {len(shapes)} λ vs Rust "
                  f"chi_lambdas_braid_mpfr, worst rel {mp.nstr(worst, 3)} "
                  f"(path-sum {t_mine*1000:.0f} ms, Rust {t_rust*1000:.0f} ms)")
            # Averaged crossings (sign 0, shift h/2) on a mixed word.
            w2 = [(0 if i % 3 == 0 else (-1 if i % 5 == 0 else 1), g) for i, (_s, g) in enumerate(word)]
            mine2 = chi_all_partitions_path_sum(n, w2, q)
            rust2 = ph.chi_lambdas_braid_mpfr([list(s) for s in shapes], list(w2),
                                              Q_50_DIGIT_STR, 50)
            worst2 = max(abs(mine2[s] - mp.mpf(r)) / max(abs(mp.mpf(r)), mp.mpf(1))
                         for s, r in zip(shapes, rust2))
            ok2 = worst2 < floor
            fails += 0 if ok2 else 1
            print(f"  [{'PASS' if ok2 else 'FAIL'}] n={n}: mixed σ/σ⁻¹/averaged word vs Rust, "
                  f"worst rel {mp.nstr(worst2, 3)}")

    # 2. Against the committed lossless caches — on BOTH intra-nucleon
    #    orderings.  A cache may have been computed on the pre-2026-09-05
    #    `grouped` word (owner ruling qou-92u9 made `borromean` canonical), so
    #    "matches grouped, not borromean" is a STALE cache, not a wrong route;
    #    only "matches neither" is a failure of this module.  The cache's
    #    `chi_lambda` strings are 50-dps, so the floor here is the recorded
    #    precision (large χ with cancellation lands ~1e-42 relative).
    from mass_at_3A_proper import atom_braid_word_3A
    cache_floor = mp.mpf(10) ** -40
    caches = {
        (1, 1): "chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json",
        (2, 1): "chi-tritium-h9-at-q0-50dps-matrix-m.witness.json",
        (1, 2): "chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json",
        (2, 2): "chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json",
        (3, 2): "chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json",
        (3, 3): "chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json",
    }
    for (Z, N), fn in caches.items():
        p = HERE / fn
        if not p.exists():
            print(f"  [SKIP] {fn} not present")
            continue
        W = json.loads(p.read_text(encoding="utf-8"))
        if str(W.get("q_0_50dps", ""))[:30] != Q_50_DIGIT_STR[:30]:
            print(f"  [SKIP] {fn}: cache q₀ {W.get('q_0_50dps','')[:20]} ≠ proton pin")
            continue
        n = 3 * (Z + N)
        verdict = {}
        dt = 0.0
        for order in ("borromean", "grouped"):
            triples = atom_braid_word_3A(Z, N, intra_order=order)
            word = [(1 if c >= 0 else -1, g + 1) for (c, _d, g) in triples]
            t0 = time.monotonic()
            mine = chi_all_partitions_path_sum(n, word, q)
            if order == "borromean":
                dt = time.monotonic() - t0
            worst = mp.mpf(0)
            for row in W["by_partition"]:
                s = tuple(row["partition"])
                r = mp.mpf(row["chi_lambda"])
                worst = max(worst, abs(mine[s] - r) / max(abs(r), mp.mpf(1)))
            verdict[order] = worst
        cnt = len(W["by_partition"])
        if verdict["borromean"] < cache_floor:
            tag, note = "PASS", "cache is on the canonical borromean word"
        elif verdict["grouped"] < cache_floor:
            tag, note = "PASS", ("cache is on the pre-2026-09-05 GROUPED word — "
                                 "STALE cache, route agrees with it on that word")
        else:
            tag, note = "FAIL", "matches NEITHER word"
            fails += 1
        print(f"  [{tag}] {fn}: {cnt} λ, worst rel borromean {mp.nstr(verdict['borromean'], 3)} / "
              f"grouped {mp.nstr(verdict['grouped'], 3)} (path-sum all λ: {dt*1000:.0f} ms) — {note}")

    # 3. Timing at n = 15 and 18 (all partitions) — the wall this replaces.
    for Z, N in [(3, 2), (3, 3)]:
        n, word = _word_for_braid_word_3a(Z, N)
        t0 = time.monotonic()
        res = chi_all_partitions_path_sum(n, word, q)
        dt = time.monotonic() - t0
        triv = res[(n,)]
        ok = abs(triv - q ** len(word)) / q ** len(word) < floor
        fails += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] n={n}: {len(res)} λ in {dt:.1f} s; "
              f"χ_[n] = q^writhe check ({mp.nstr(triv, 12)})")

    print("\nALL PASSED" if fails == 0 else f"\n{fails} FAILED")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(_selftest())
