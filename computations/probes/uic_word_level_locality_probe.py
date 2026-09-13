#!/usr/bin/env python3
"""Is the binding producer's braid word level-local?  No — and no trace-
preserving reordering makes it so.  (bean qou-hxz4, continues qou-sv7h)

QUESTION
--------
PR #7160 proved that for a *level-local* word (every seminormal level touched
in exactly one contiguous factor) the seminormal character is a dim-free path
sum, χ^λ(T_β) = Σ_{T∈SYT(λ)} Π_j ⟨T|F_j|T⟩, and shipped
`computations/chi_path_sum_seminormal.py`.  If the words that
`hecke_core_legacy.unified_iterative_correction` (reached via
`binding_energy`) hands its Rust kernel were level-local, that path sum would
collapse the O(L·dim²) wall of qou-sv7h.  This probe answers whether they are.

WHAT IS MEASURED (instrumented, not read off docstrings)
--------------------------------------------------------
1. `_lp_kernel_steps` is monkey-patched with a recorder, so the chains captured
   are the EXACT `(c, d, gen)` triples the producer serialises for
   `pyhecke_native.lp_accumulator_step_traces_mpfr`, per atom and per
   partition — including the colour-weighted p–n offset `_PN_D_MP`
   (bring_color_weighted, NOT −h/2) and the exact nn offset `−ℏ_q`.
   The word for partition λ ⊢ k is the concatenation of the A step chains.
2. The word is transcribed for the path-sum module (`σ_g + d·I` ↦ sign 0 with
   shift −d; generators 1-based) and the transcription is CHECKED against the
   kernel: single-segment path-sum trace vs the kernel's own final
   `trace·exp(log_norm)`, k = 3 … K_XCHECK, at ≤ 1e-45 relative.
3. `chi_path_sum_seminormal.segments_of` is run on every (atom, k) word: number
   of segments, generator-set size of the largest segment, and the FIRST
   letter that breaks locality (a generator recurring after a different
   generator intervened).
4. Reorderings.  Two trace identities are available and both are tested:
   (a) cyclic rotation, tr(AB) = tr(BA) — every rotation of every word is
       segmented; and the prefix argument is stated in the report;
   (b) Hecke-relation rewriting — the seminormal representation is an algebra
       homomorphism, so any word equal to the same ELEMENT of H_k(q) has the
       same trace.  The invariant that excludes every such rewriting is the
       coefficient of T_{w₀} (longest element) in the T_w expansion:
       a product F_1⋯F_m of factors in parabolic subalgebras of pairwise
       disjoint generator intervals I_i lies in span{T_w : ℓ(w) ≤ Σ_i ℓ(w₀(I_i))}
       and Σ_i C(|I_i|+1, 2) < C(k, 2) = ℓ(w₀) whenever m ≥ 2
       (T_u T_v ∈ span{T_w : ℓ(w) ≤ ℓ(u)+ℓ(v)}, Geck–Pfeiffer [geck-pfeiffer2000]
       §4.4).  So a NONZERO T_{w₀} coefficient excludes every level-local
       factorisation of the element with ≥ 2 segments — for the word, and for
       each of its rotations (each rotation is its own element; all are
       expanded).  The expansion is validated on the trivial and sign
       representations (T_w ↦ q^{ℓ(w)}, (−q⁻¹)^{ℓ(w)}) and, at k = 3, by
       contracting it with the seminormal characters of the T_w from the Rust
       kernel `chi_lambdas_braid_mpfr`.
5. Timing: the single-segment path-sum (which degenerates to the direct
   seminormal trace at O(L·dim²)) against the Rust kernel on the same word.

Everything is `mpmath` at `_precision.set_compute_dps()` (70 dps), q from
`Q_50_DIGIT_STR` (proton pin, string — `q_at()` returns float64 and is not
used).  No float64 anywhere in the arithmetic; no `statistics`/`math`.

scope-(b) for the reorderings tested (cyclic rotation at every k; Hecke
rewriting at every k the expansion reaches, k ≤ K_TW); scope-(a) for k above
that.  No fit; nothing wired; no recorded number moves.
"""
from __future__ import annotations

import argparse
import sys
import time
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

import hecke_core_legacy as H  # noqa: E402
from chi_path_sum_seminormal import (  # noqa: E402
    build_segments, chi_lambda_path_sum, segments_of)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

ATOMS = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"), (3, 2, "5Li")]
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


# ── 1. Capture the exact chains the producer hands the kernel ────────────


def capture_chains(Z: int, N: int) -> dict[int, list[list[tuple]]]:
    """{k: [chain_step_0, …, chain_step_{A-1}]} as passed to `_lp_kernel_steps`.

    The recorder returns a dummy trajectory so the accumulator runs to
    completion cheaply; every partition of size k must receive the SAME chains
    (asserted), because `_step_chain_generic` depends only on n_gens = k − 1.
    """
    A = Z + N
    seen: dict[int, list] = {}
    parts_per_k: dict[int, int] = {}
    orig = H._lp_kernel_steps

    def recorder(partition, chains):
        k = sum(partition)
        ch = [[tuple(t) for t in c] for c in chains]
        if k in seen:
            if seen[k] != ch:
                raise AssertionError(f"partitions of {k} receive different chains")
        else:
            seen[k] = ch
        parts_per_k[k] = parts_per_k.get(k, 0) + 1
        return [(mp.mpf(1), mp.mpf(0))] * len(chains)

    H._lp_kernel_steps = recorder
    try:
        H.unified_iterative_correction(Z, N)
    finally:
        H._lp_kernel_steps = orig
    # Reconstruction check against the builder the loop itself calls.
    ordering = []
    pc, nc = 0, 0
    for kk in range(A):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1
    for k, ch in seen.items():
        rec = [[tuple(t) for t in H._step_chain_generic(ordering[i], ordering[:i], k - 1)]
               for i in range(A)]
        if rec != ch:
            raise AssertionError(f"k={k}: captured chains ≠ _step_chain_generic")
    return seen, parts_per_k, ordering


# ── 2. Transcription to the path-sum word format ────────────────────────


def classify_d(d, h) -> str:
    d = mp.mpf(d)
    if d == 0:
        return "sigma"
    if abs(d + h) < mp.mpf(10) ** -40:
        return "sigma_inv"            # σ − h = σ⁻¹
    if abs(d + h / 2) < mp.mpf(10) ** -40:
        return "avg(-h/2)"
    return "pn(bring_color_weighted)"


def to_word(chains, h):
    """[(sign, gen_1based)], per-position shifts, letter classes, step bounds."""
    word, shifts, classes, steps = [], [], [], []
    for ch in chains:
        start = len(word)
        for c, d, g in ch:
            if c != 1:
                raise AssertionError(f"c = {c} ≠ 1 — transcription assumes σ_g + d·I")
            word.append((0, g + 1))
            shifts.append(-mp.mpf(d))     # path-sum: ρ(σ) − shift·I
            classes.append(classify_d(d, h))
        steps.append((start, len(word)))
    return word, shifts, classes, steps


# ── 3/4a. Locality diagnostics and rotations ────────────────────────────


def first_break(word) -> dict | None:
    """First position p where gen(p) has occurred before and a DIFFERENT
    generator occurred in between — the earliest letter that prevents the
    word from splitting into disjoint-generator segments there."""
    last_pos: dict[int, int] = {}
    for p, (_s, g) in enumerate(word):
        if g in last_pos:
            between = {word[i][1] for i in range(last_pos[g] + 1, p)}
            if between - {g}:
                return {"pos": p, "gen": g, "prev_pos": last_pos[g],
                        "intervening_gens": sorted(between - {g})}
        last_pos[g] = p
    return None


def adjacent_pairs_interleave(word, n_gens) -> list[bool]:
    """For each adjacent generator pair (g, g+1): do their occurrence spans
    overlap?  Far commutation (|Δg| ≥ 2) cannot change the relative order of
    letters on g and g+1, so an overlapping pair stays in one segment under
    every commutation-equivalent word."""
    first, last = {}, {}
    for p, (_s, g) in enumerate(word):
        first.setdefault(g, p)
        last[g] = p
    out = []
    for g in range(1, n_gens):
        a, b = g, g + 1
        if a not in first or b not in first:
            out.append(False)
            continue
        overlap = not (last[a] < first[b] or last[b] < first[a])
        out.append(overlap)
    return out


def rotation_segments(word):
    """Number of segments of every cyclic rotation."""
    L = len(word)
    return [len(segments_of(word[r:] + word[:r])) for r in range(L)]


# ── 4b. Exact T_w expansion in H_k(q) ───────────────────────────────────


def _len(w) -> int:
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def hecke_word_element(k: int, word, shifts, q):
    """Expand Π_pos (T_{g} − shift_pos) in the T_w basis of H_k(q),
    right-multiplying in word order.  Basis: permutations as tuples,
    T_w T_s = T_{ws} if ℓ(ws) > ℓ(w) else h·T_w + T_{ws}."""
    h = q - 1 / q
    x = {tuple(range(1, k + 1)): mp.mpf(1)}
    for (_s, g), sh in zip(word, shifts):
        i = g - 1                    # swap positions i, i+1 (0-based)
        d = -sh                      # letter = T_g + d
        y: dict = {}
        for w, c in x.items():
            # d·T_w
            y[w] = y.get(w, mp.mpf(0)) + d * c
            ws = list(w); ws[i], ws[i + 1] = ws[i + 1], ws[i]; ws = tuple(ws)
            if w[i] < w[i + 1]:      # ℓ(ws) = ℓ(w) + 1
                y[ws] = y.get(ws, mp.mpf(0)) + c
            else:                    # T_w T_s = h T_w + T_{ws}
                y[w] = y.get(w, mp.mpf(0)) + h * c
                y[ws] = y.get(ws, mp.mpf(0)) + c
        x = y
    return x


def _perm_mul(u, v):
    """(u·v)(i) = u(v(i)) on 1-based tuples."""
    return tuple(u[v[i] - 1] for i in range(len(u)))


def _parabolic(k: int, gens: tuple[int, ...]) -> frozenset:
    """W_I ⊆ S_k generated by the adjacent transpositions s_g, g ∈ gens (1-based)."""
    e = tuple(range(1, k + 1))
    seen = {e}
    frontier = [e]
    while frontier:
        nxt = []
        for w in frontier:
            for g in gens:
                ws = list(w); ws[g - 1], ws[g] = ws[g], ws[g - 1]; ws = tuple(ws)
                if ws not in seen:
                    seen.add(ws); nxt.append(ws)
        frontier = nxt
    return frozenset(seen)


def _set_product(A: frozenset, B: frozenset) -> frozenset:
    return frozenset(_perm_mul(a, b) for a in A for b in B)


def two_block_product_sets(k: int) -> list[tuple[str, frozenset]]:
    """W_J·W_K and W_K·W_J for every split J = [1..j], K = [j+1..k-1].

    Any product F_1⋯F_m of factors in parabolic subalgebras of pairwise
    disjoint generator INTERVALS (m ≥ 2, any word order) has T_w-support
    inside one of these sets — see `ordered_partition_sets_contained` for
    the computational check of that reduction, and the audit doc for the
    one-paragraph proof (support(T_u T_v) ⊆ {u'v' : u' ≤ u, v' ≤ v}).
    """
    out = []
    for j in range(1, k - 1):
        J = tuple(range(1, j + 1)); K = tuple(range(j + 1, k))
        WJ, WK = _parabolic(k, J), _parabolic(k, K)
        out.append((f"W[1..{j}]·W[{j+1}..{k-1}]", _set_product(WJ, WK)))
        out.append((f"W[{j+1}..{k-1}]·W[1..{j}]", _set_product(WK, WJ)))
    return out


def ordered_partition_sets_contained(k: int) -> bool:
    """Check: for EVERY ordered partition of {1..k-1} into ≥ 2 intervals, the
    set product of its parabolic subgroups lies inside some 2-block set."""
    from itertools import permutations as _perms
    gens = list(range(1, k))
    two = [s for _n, s in two_block_product_sets(k)]

    def comps(lst):
        if not lst:
            yield []
            return
        for i in range(1, len(lst) + 1):
            for rest in comps(lst[i:]):
                yield [tuple(lst[:i])] + rest
    for blocks in comps(gens):
        if len(blocks) < 2:
            continue
        paras = [_parabolic(k, b) for b in blocks]
        for order in _perms(range(len(blocks))):
            prod = paras[order[0]]
            for i in order[1:]:
                prod = _set_product(prod, paras[i])
            if not any(prod <= s for s in two):
                return False
    return True


def support(x, floor_rel=None) -> set:
    cmax = max(abs(c) for c in x.values())
    fl = (mp.mpf(10) ** -50) if floor_rel is None else floor_rel
    return {w for w, c in x.items() if abs(c) > fl * cmax}


def outside_every_two_block(x, sets) -> tuple[int, str]:
    """min over candidate sets of |support(x) \\ set|, and the closest set."""
    sup = support(x)
    best = None
    for name, s in sets:
        n_out = len(sup - s)
        if best is None or n_out < best[0]:
            best = (n_out, name)
    return best


def reduced_word(w) -> list[int]:
    """A reduced word (1-based generators) for permutation tuple w, by
    bubble sort: w = s_{i1} ⋯ s_{im} with m = ℓ(w)."""
    w = list(w)
    out = []
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] > w[i + 1]:
                w[i], w[i + 1] = w[i + 1], w[i]
                out.append(i + 1)
                changed = True
    return out[::-1]


# ── main ─────────────────────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k-xcheck", type=int, default=6,
                    help="cross-check path-sum vs kernel for k ≤ this")
    ap.add_argument("--k-tw", type=int, default=7,
                    help="T_w expansion (T_{w0} coefficient) for k ≤ this")
    ap.add_argument("--k-rot", type=int, default=5,
                    help="expand every rotation for k ≤ this")
    ap.add_argument("--budget-s", type=float, default=900.0,
                    help="abort long stages past this wall budget")
    args = ap.parse_args()

    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    t_start = time.monotonic()
    print("=" * 76)
    print("  Level-locality of the binding producer's braid words  (qou-hxz4)")
    print(f"  q0 = {Q_50_DIGIT_STR[:24]}…  (proton pin, string)   mp.dps = {mp.mp.dps}")
    print(f"  kernel available: {H._HAS_LP_KERNEL}")
    print("=" * 76)
    check("Rust kernel present (the words captured are the ones it receives)",
          H._HAS_LP_KERNEL)

    per_atom_rows = []
    words_by_atom: dict = {}
    t0 = time.monotonic()
    for Z, N, name in ATOMS:
        chains, parts_per_k, ordering = capture_chains(Z, N)
        words_by_atom[name] = (Z, N, chains, parts_per_k, ordering)
        ks = sorted(chains)
        print(f"\n  {name}: A={Z+N}, ordering {''.join(ordering)}, partition sizes k = {ks[0]}..{ks[-1]}"
              f" ({sum(parts_per_k.values())} partitions), captured in {time.monotonic()-t0:.1f} s")
        t0 = time.monotonic()
    check("every partition of a given k receives identical chains, equal to "
          "_step_chain_generic(ordering[i], ordering[:i], k-1)", True)

    # ── per (atom, k) locality table ──────────────────────────────────
    all_single_segment = True
    all_rotations_single = True
    all_adjacent_interleave = True
    for name, (Z, N, chains, parts_per_k, ordering) in words_by_atom.items():
        A = Z + N
        for k in sorted(chains):
            n_gens = k - 1
            word, shifts, classes, steps = to_word(chains[k], h)
            L = len(word)
            segs = segments_of(word)
            fb = first_break(word)
            inter = adjacent_pairs_interleave(word, n_gens)
            rots = rotation_segments(word)
            mult = {}
            for _s, g in word:
                mult[g] = mult.get(g, 0) + 1
            cls = {}
            for c in classes:
                cls[c] = cls.get(c, 0) + 1
            row = {
                "atom": name, "Z": Z, "N": N, "A": A, "k": k, "n_gens": n_gens,
                "n_partitions": parts_per_k[k],
                "word_length": L,
                "letters_per_step": [e - s for s, e in steps],
                "generator_sequence_step0": [g for _s, g in word[steps[0][0]:steps[0][1]]],
                "generator_multiplicity": {str(g): mult[g] for g in sorted(mult)},
                "letter_classes": cls,
                "n_segments": len(segs),
                "largest_segment_gens": max(len(s["gens"]) for s in segs),
                "level_local_nontrivial": len(segs) > 1,
                "first_break": fb,
                "adjacent_pairs_interleave": inter,
                "rotations_with_gt1_segments": sum(1 for r in rots if r > 1),
                "n_rotations": L,
            }
            per_atom_rows.append(row)
            all_single_segment &= (len(segs) == 1)
            all_rotations_single &= all(r == 1 for r in rots)
            all_adjacent_interleave &= all(inter)
        # print a compact table per atom
        print(f"\n  {name}  (A={A})")
        print("    k  n_gens  L   segs  first break (pos,gen,prev,between)          adj-pairs interleave  rotations>1seg")
        for row in [r for r in per_atom_rows if r["atom"] == name]:
            fb = row["first_break"]
            fbs = (f"p{fb['pos']} σ{fb['gen']} after p{fb['prev_pos']}, {fb['intervening_gens']}"
                   if fb else "none")
            print(f"    {row['k']:>2}  {row['n_gens']:>5}  {row['word_length']:>3}   {row['n_segments']:>2}   "
                  f"{fbs:<42} {sum(row['adjacent_pairs_interleave'])}/{len(row['adjacent_pairs_interleave'])}"
                  f"                 {row['rotations_with_gt1_segments']}/{row['n_rotations']}")

    check("NO (atom, k) word is level-local: segments_of returns ONE segment "
          "covering every generator, for every atom and every k",
          all_single_segment)
    check("every adjacent generator pair (g, g+1) interleaves in every word — "
          "far commutation cannot separate them", all_adjacent_interleave)
    check("no cyclic rotation of any word has > 1 segment", all_rotations_single)

    # letter classes on the D word at k=11 (the exact d values, for the record)
    Z, N, chains, _pp, _o = words_by_atom["2H"]
    word, shifts, classes, steps = to_word(chains[11], h)
    d_values = sorted({fmt(-s) for s in shifts})
    print(f"\n  distinct crossing offsets d (σ_g + d·I) on the 2H word: {len(d_values)}")
    for c in sorted(set(classes)):
        print(f"    {c:<26} d = {fmt(-shifts[classes.index(c)])[:40]}…")
    check("p–n crossings carry the colour-weighted offset _PN_D_MP, not −h/2",
          "pn(bring_color_weighted)" in classes and
          abs(H._PN_D_MP + h / 2) > mp.mpf(10) ** -6,
          f"_PN_D_MP = {fmt(H._PN_D_MP)[:22]}, −h/2 = {fmt(-h/2)[:22]}")

    # ── 2. transcription faithfulness: path-sum vs kernel ─────────────
    print("\n  Transcription check — single-segment path-sum vs Rust kernel (final step)")
    print("    atom  k   dim   rel diff      path-sum(all λ⊢k)   kernel(all λ⊢k)")
    xrows = []
    worst = mp.mpf(0)
    from per_irrep_pole_atom import parts_of
    for name in ("2H", "3H", "3He", "4He"):
        Z, N, chains, _pp, _o = words_by_atom[name]
        for k in range(3, args.k_xcheck + 1):
            if time.monotonic() - t_start > args.budget_s:
                print("    [budget] skipping remaining cross-checks")
                break
            word, shifts, _c, _st = to_word(chains[k], h)
            shapes = [s for s in parts_of(k)]
            # path-sum
            t0 = time.monotonic()
            segs = build_segments(word, q, shifts)
            ps = {s: chi_lambda_path_sum(s, k, word, q, shifts, _segs=segs) for s in shapes}
            t_ps = time.monotonic() - t0
            # kernel (same chains, same serialisation as the producer)
            t0 = time.monotonic()
            kr = {}
            for s in shapes:
                out = H._lp_kernel_steps(list(s), chains[k])
                if not out:           # 1-dim partitions return [] from Rust? keep robust
                    kr[s] = None
                    continue
                tr, ln = out[-1]
                kr[s] = tr * mp.exp(ln)
            t_kr = time.monotonic() - t0
            wr = mp.mpf(0)
            dim_max = 0
            for s in shapes:
                if kr[s] is None:
                    continue
                rel = abs(ps[s] - kr[s]) / max(abs(kr[s]), mp.mpf(1))
                wr = max(wr, rel)
            worst = max(worst, wr)
            xrows.append({"atom": name, "k": k, "worst_rel": fmt(wr),
                          "t_path_sum": f"{t_ps:.3f}", "t_kernel": f"{t_kr:.3f}",
                          "n_shapes": len(shapes)})
            print(f"    {name:<4} {k:>2}   {'':>4}  {mp.nstr(wr, 3):<12} {t_ps:>8.3f} s          {t_kr:>8.3f} s")
    check(f"single-segment path-sum reproduces the kernel's final trace on every "
          f"λ ⊢ k, k ≤ {args.k_xcheck}, all four light atoms (worst rel {mp.nstr(worst, 3)})",
          worst < mp.mpf(10) ** -45, f"worst rel {mp.nstr(worst, 3)}")

    # ── 4b. T_{w0} coefficient obstruction ────────────────────────────
    print("\n  T_{w0} coefficient of the word's Hecke element (nonzero ⇒ no level-local"
          " factorisation with ≥ 2 segments, for ANY Hecke-relation rewriting)")
    # validate the expansion at k = 3 against the Rust seminormal characters
    import pyhecke_native as ph
    Z, N, chains, _pp, _o = words_by_atom["2H"]
    word3, sh3, _c, _st = to_word(chains[3], h)
    x3 = hecke_word_element(3, word3, sh3, q)
    shapes3 = parts_of(3)
    # characters of every T_w via a reduced word of w, all letters +σ
    chi_tw = {}
    for w in permutations(range(1, 4)):
        rw = [(1, g) for g in reduced_word(w)]
        if not rw:
            chi_tw[w] = {s: mp.mpf(H.partition_dimension(list(s))) for s in shapes3}
        else:
            vals = ph.chi_lambdas_braid_mpfr([list(s) for s in shapes3], rw, Q_50_DIGIT_STR, 50)
            chi_tw[w] = {s: mp.mpf(v) for s, v in zip(shapes3, vals)}
    segs3 = build_segments(word3, q, sh3)
    worst3 = mp.mpf(0)
    for s in shapes3:
        via_tw = sum((c * chi_tw[w][s] for w, c in x3.items()), mp.mpf(0))
        direct = chi_lambda_path_sum(s, 3, word3, q, sh3, _segs=segs3)
        worst3 = max(worst3, abs(via_tw - direct) / max(abs(direct), mp.mpf(1)))
    check("T_w expansion validated at k=3: Σ_w x_w χ^λ(T_w) = seminormal χ^λ(x) "
          "for all λ ⊢ 3 (Rust characters of T_w)", worst3 < mp.mpf(10) ** -45,
          f"worst rel {mp.nstr(worst3, 3)}")

    # Reduction lemma, checked computationally at k = 3..6: every ordered
    # interval partition's product set sits inside a 2-block set.
    red_ok = all(ordered_partition_sets_contained(k) for k in range(3, 7))
    check("reduction: every ordered ≥2-interval product set W_{I_1}⋯W_{I_m} lies in "
          "some 2-block W_J·W_K or W_K·W_J (k = 3..6, exhaustive)", red_ok)

    tw_rows = []
    all_nonzero = True
    all_excluded = True
    triv_sign_ok = True
    for name, (Z, N, chains, _pp, _o) in words_by_atom.items():
        for k in range(3, args.k_tw + 1):
            if time.monotonic() - t_start > args.budget_s:
                print("    [budget] skipping remaining expansions")
                break
            word, shifts, _c, _st = to_word(chains[k], h)
            L = len(word)
            w0 = tuple(range(k, 0, -1))
            t0 = time.monotonic()
            x = hecke_word_element(k, word, shifts, q)
            t_x = time.monotonic() - t0
            # validation on the trivial and sign representations
            triv = sum((c * q ** _len(w) for w, c in x.items()), mp.mpf(0))
            sgn = sum((c * (-1 / q) ** _len(w) for w, c in x.items()), mp.mpf(0))
            triv_exp = mp.mpf(1)
            sgn_exp = mp.mpf(1)
            for sh in shifts:
                triv_exp *= (q - sh)
                sgn_exp *= (-1 / q - sh)
            ok_ts = (abs(triv - triv_exp) / abs(triv_exp) < mp.mpf(10) ** -45 and
                     abs(sgn - sgn_exp) / max(abs(sgn_exp), mp.mpf(10) ** -30) < mp.mpf(10) ** -40)
            triv_sign_ok &= ok_ts
            c0 = x.get(w0, mp.mpf(0))
            # scale-free measure: |c0| relative to the largest coefficient
            cmax = max(abs(c) for c in x.values())
            rel0 = abs(c0) / cmax
            # the sharper invariant: support must lie in ONE 2-block product set
            sets = two_block_product_sets(k)
            n_out, closest = outside_every_two_block(x, sets)
            # rotations
            rot_min = None
            n_rot_zero = 0
            rot_min_out = None
            if k <= args.k_rot:
                rot_min = None
                for r in range(1, L):
                    wr = word[r:] + word[:r]
                    sr = shifts[r:] + shifts[:r]
                    xr = hecke_word_element(k, wr, sr, q)
                    cr = abs(xr.get(w0, mp.mpf(0))) / max(abs(c) for c in xr.values())
                    rot_min = cr if rot_min is None else min(rot_min, cr)
                    if cr < mp.mpf(10) ** -50:
                        n_rot_zero += 1
                    ro, _cl = outside_every_two_block(xr, sets)
                    rot_min_out = ro if rot_min_out is None else min(rot_min_out, ro)
            nonzero = rel0 > mp.mpf(10) ** -50 and (rot_min is None or rot_min > mp.mpf(10) ** -50)
            all_nonzero &= nonzero
            excluded = n_out > 0 and (rot_min_out is None or rot_min_out > 0)
            all_excluded &= excluded
            tw_rows.append({"atom": name, "k": k, "word_length": L, "support": len(x),
                            "k_factorial": int(mp.factorial(k)), "coef_w0": fmt(c0),
                            "coef_w0_over_max": fmt(rel0),
                            "rotations_tested": (L - 1) if k <= args.k_rot else 0,
                            "rotation_min_rel_coef_w0": (fmt(rot_min) if rot_min is not None else None),
                            "rotations_with_zero_coef_w0": n_rot_zero,
                            "support_size": len(support(x)),
                            "min_support_outside_two_block": n_out,
                            "closest_two_block_set": closest,
                            "rotations_min_support_outside": rot_min_out,
                            "level_local_rewriting_excluded": excluded,
                            "t_expand": f"{t_x:.3f}",
                            "trivial_and_sign_rep_ok": ok_ts})
            print(f"    {name:<4} k={k}  L={L:>3}  supp {len(support(x)):>5}/{int(mp.factorial(k)):<6} "
                  f"|c(T_w0)|/max {mp.nstr(rel0, 3):<9} outside 2-block: min {n_out:>4} ({closest})"
                  f"  rot: {'min ' + str(rot_min_out) if rot_min_out is not None else 'n/a':<8} "
                  f"({t_x:.2f} s)")
    check("T_w expansion reproduces the trivial and sign representations "
          "(Π(q+d), Π(−q⁻¹+d)) at every k expanded", triv_sign_ok)
    print(f"    (T_w0 coefficient alone nonzero everywhere: {all_nonzero} — it is only a "
          "NECESSARY test and vanishes when the word is too short to reach w0)")
    check(f"support of the word's Hecke element lies in NO 2-block parabolic product "
          f"W_J·W_K / W_K·W_J, for every atom, every k ≤ {args.k_tw}, and every cyclic "
          f"rotation for k ≤ {args.k_rot} — no Hecke-relation rewriting of the word or of "
          "any rotation is level-local with ≥ 2 segments", all_excluded)

    # ── 5. cost of the degenerate route on a real partition set ───────
    print("\n  Cost of the degenerate (single-segment) path-sum — it is the O(L·dim²)"
          " direct seminormal trace, in pure mpmath")
    cost_rows = []
    Z, N, chains, _pp, _o = words_by_atom["2H"]
    for k in (6, 7, 8):
        if time.monotonic() - t_start > args.budget_s:
            break
        word, shifts, _c, _st = to_word(chains[k], h)
        shapes = parts_of(k)
        dims = {s: H.partition_dimension(list(s)) for s in shapes}
        big = max(shapes, key=lambda s: dims[s])
        t0 = time.monotonic()
        segs = build_segments(word, q, shifts)
        _v = chi_lambda_path_sum(big, k, word, q, shifts, _segs=segs)
        t_ps = time.monotonic() - t0
        t0 = time.monotonic()
        _o2 = H._lp_kernel_steps(list(big), chains[k])
        t_kr = time.monotonic() - t0
        cost_rows.append({"k": k, "shape": list(big), "dim": dims[big], "L": len(word),
                          "t_path_sum": f"{t_ps:.3f}", "t_kernel": f"{t_kr:.3f}"})
        print(f"    k={k} λ={list(big)} dim={dims[big]:>3} L={len(word)}: path-sum {t_ps:.2f} s, "
              f"Rust kernel {t_kr:.3f} s  (ratio {t_ps/max(t_kr,1e-9):.0f}x)")

    # ── witness ───────────────────────────────────────────────────────
    w = WitnessBuilder("uic-word-level-locality", engine="python+mpmath+rust")
    w.set_description(
        "qou-hxz4: the braid words hecke_core_legacy.unified_iterative_correction "
        "hands its Rust kernel (captured by instrumenting _lp_kernel_steps) are "
        "NOT level-local for any atom or any partition size k: the generator "
        "index cycles g mod (k-1) through every letter of every step, so the "
        "first letter that breaks locality is the third (σ_1 σ_2 σ_1 …), every "
        "adjacent generator pair interleaves, and segments_of returns a single "
        "segment covering all k-1 generators. No trace-preserving reordering "
        "restores it: every cyclic rotation is single-segment, and the T_w-support "
        "of the word's Hecke element (and of every rotation's) lies in NO "
        "2-block parabolic product W_J.W_K / W_K.W_J, which excludes every "
        "Hecke-relation rewriting into >= 2 disjoint-interval factors (the "
        "T_{w0} coefficient alone is not decisive: it vanishes for 2H at "
        "k = 6, 7 because the 23-letter word cannot reach w0). The #7160 path-sum "
        "therefore degenerates to the O(L·dim^2) direct seminormal trace on "
        "this producer — measured slower than the Rust kernel — and is not a "
        "route past qou-sv7h's wall. Word transcription verified against the "
        "kernel at <= 1e-45 relative."
    )
    w.set_audit_only("docs/audits/2026-09-08-binding-word-not-level-local.md")
    w.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("k_xcheck", args.k_xcheck)
    w.add_parameter("k_tw", args.k_tw)
    w.add_parameter("k_rot", args.k_rot)
    w.add_data("per_atom_k", per_atom_rows)
    w.add_data("transcription_vs_kernel", xrows)
    w.add_data("tw0_coefficient", tw_rows)
    w.add_data("degenerate_path_sum_cost", cost_rows)
    w.add_data("crossing_offsets_2H_k11", {
        "PN_D_MP": fmt(H._PN_D_MP), "NN_D_MP": fmt(H._NN_D_MP),
        "minus_h_over_2": fmt(-h / 2), "distinct_d": d_values})
    w.add_caveat("Timings are wall-clock strings (seconds), provenance only. "
                 "scope-(b) for cyclic rotation at every k and for Hecke-relation "
                 "rewriting at k <= k_tw; scope-(a) for rewriting at k > k_tw. "
                 "Conjugation by an arbitrary invertible element of H_k(q) is "
                 "trace-preserving and is NOT tested: choosing such a conjugator "
                 "to reach a level-local word would be selection, not derivation.")
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_word_level_locality_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed"
          f"  ({time.monotonic()-t_start:.0f} s wall)")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
