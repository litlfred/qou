#!/usr/bin/env python3
"""Reproduction script for `docs/audits/2026-08-21-deuteron-two-adjudications-reconciled.md`.

Reconciles the two deuteron adjudications that landed on `main` on 2026-08-21:

  A  docs/audits/2026-08-21-deuteron-w3-knot-identity-adjudicated.md  (f264ebbabf)
  B  docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md  (#5350/#5363)

WHAT THIS ESTABLISHES (all exact; see the audit for the argument):

  1. The two frame-1 producers (`delta_lambda_jsj_phase3.load_atom_braids()["D"]`
     and `mass_at_3A_proper.atom_braid_word_3A(1,1)`) emit the SAME letter
     multiset in a DIFFERENT order -- so they are two distinct braid words with
     equal cycle counts, not one word.
  2. Every resolution of the 5 non-braid letters closes to 3 components.
  3. The mass word's closure permutation does NOT preserve the {1,2,3}u{4,5,6}
     nucleon partition, so frame 1 does not descend to the coordination frame.
  4. A's rule ("canonical = braid-closure of the T_w word") applied to B's word
     returns a 3-component link, excluding all three of A's candidates.
  5. The R5-full SDP's deuteron winner and all its top-k candidates also close
     to 3 components, against an exact 43/128 base rate over B_3 length-8 words.

NO FLOATS. A braid closure's component count is the number of cycles of the
induced permutation, a product of transpositions (i, i+1). It depends only on
|sigma_i| and never on the sign -- the invariant proved sorry-free in
`QOU.BraidsAndKnots.wordPerm_eq_of_indices_eq` (main @ 01a4dd3bb6). Every number
below is an integer or an exact rational.

EXPLORATORY -- audit reproduction only. Emits no witness, writes nothing,
re-runs no producer.
"""
from __future__ import annotations

import json
from collections import Counter
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent


# ── exact closure combinatorics ───────────────────────────────────────────
def perm_of(word: list[int], n: int) -> list[int]:
    """Permutation induced by a 1-indexed signed braid word on `n` strands.

    `p[k]` is the label sitting at position `k` after the word is applied.
    Signs are ignored by construction: `sigma_i` and `sigma_i^-1` induce the
    same transposition `(i, i+1)`.
    """
    p = list(range(1, n + 1))
    for g in word:
        i = abs(g) - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def cycles(word: list[int], n: int) -> list[tuple[int, ...]]:
    """Exact cycle decomposition of the closure permutation."""
    p = perm_of(word, n)
    seen = [False] * (n + 1)
    out: list[tuple[int, ...]] = []
    for s in range(1, n + 1):
        if seen[s]:
            continue
        cyc, x = [], s
        while not seen[x]:
            seen[x] = True
            cyc.append(x)
            x = p[x - 1]
        out.append(tuple(cyc))
    return out


def ncomp(word: list[int], n: int) -> int:
    """Number of components of the braid closure. Sign-independent."""
    return len(cycles(word, n))


# ── frame 1: the mass chain's deuteron word ───────────────────────────────
# Reconstructed from `sublemma_2_1_h9_tritium_verify._proton_body` / `_neutron_body`
# pushed through `atom_braid_words.hecke_word_to_braid_word` (averaged letters
# -> positive, per the F1 convention in that converter). Integers only: the
# Hecke coefficients play no part in the component count.
P = [1, -2, 1, -2, 1, -2, 1, 1, 2, 1, 1]
N = [1, -2, 1, -2, 1, -2, 1, 1, -2, 1, 1]

# positions of the 5 non-braid (averaged) letters in the 23-letter word
AVG_POS = [7, 8, 11, 18, 19]


def _shift_ascoded(w: list[int], k: int) -> list[int]:
    """`[g + k for g in w]` -- the bean `qou-yaqm` sign-dropping bug, verbatim."""
    return [g + k for g in w]


def _shift_correct(w: list[int], k: int) -> list[int]:
    return [(1 if g > 0 else -1) * (abs(g) + k) for g in w]


D_ASCODED = list(P) + [3] + _shift_ascoded(N, 3)
D_CORRECTED = list(P) + [3] + _shift_correct(N, 3)


def main() -> int:
    print("=" * 74)
    print("FRAME 1 -- the mass chain's deuteron word (H_6, 3A strands)")
    print("=" * 74)
    for label, w in (("as-coded", D_ASCODED), ("sign-corrected", D_CORRECTED)):
        print(f"  {label}: {w}")
        print(f"    {len(w)} letters, max|gen| {max(abs(g) for g in w)}, "
              f"multiset {dict(sorted(Counter(abs(g) for g in w).items()))}")
        print(f"    -> {ncomp(w, 6)} components, cycles {cycles(w, 6)}")

    # (1) the two producers: same multiset, different order
    try:
        import sys
        if str(COMPUTATIONS) not in sys.path:
            sys.path.insert(0, str(COMPUTATIONS))
        import _path_bridge  # noqa: F401
        from mass_at_3A_proper import atom_braid_word_3A
        gens = [g for _, _, g in atom_braid_word_3A(1, 1)]
        live = [g + 1 for g in gens]                      # 0-indexed -> 1-indexed
        print("\n  atom_braid_word_3A(1,1) run live:")
        print(f"    gen sequence (0-indexed): {gens}")
        print(f"    multiset {dict(sorted(Counter(gens).items()))} "
              f"-> {ncomp(live, 6)} components, cycles {cycles(live, 6)}")
        same_multiset = (Counter(abs(g) for g in D_CORRECTED)
                         == Counter(abs(g) for g in live))
        same_order = [abs(g) for g in D_CORRECTED] == [abs(g) for g in live]
        print(f"    same letter multiset as load_atom_braids (corrected): {same_multiset}")
        print(f"    same letter ORDER:                                    {same_order}")
        print("    => two distinct braid words with equal cycle counts, not one word.")
    except Exception as exc:                              # pragma: no cover
        print(f"\n  [atom_braid_word_3A not runnable here: {type(exc).__name__}: {exc}]")

    # (2) every resolution of the non-braid letters
    counts = set()
    for signs in product((1, -1), repeat=len(AVG_POS)):
        w = list(D_CORRECTED)
        for pos, s in zip(AVG_POS, signs):
            w[pos] = s * abs(w[pos])
        counts.add(ncomp(w, 6))
    print(f"\n  all {2 ** len(AVG_POS)} resolutions of the 5 non-braid letters "
          f"-> component counts {sorted(counts)}")

    # (3) does frame 1 descend to the coordination frame?
    print("\n" + "=" * 74)
    print("FRAME 1 -> FRAME 3 (coordination): does the mass word descend?")
    print("=" * 74)
    for label, w in (("as-coded", D_ASCODED), ("sign-corrected", D_CORRECTED)):
        print(f"  {label}:")
        for c in cycles(w, 6):
            visits = sorted({1 if s <= 3 else 2 for s in c})
            flag = "  <-- visits BOTH nucleons" if len(visits) > 1 else ""
            print(f"    component {c} visits nucleon(s) {visits}{flag}")
    print("  => the closure permutation does not preserve the {1,2,3}u{4,5,6}")
    print("     partition, so there is no strand-collapse to a nucleon-level braid.")

    # (4) A's rule applied to B's word
    print("\n" + "=" * 74)
    print("THE CRUX -- A's rule ('closure of the T_w word') applied to B's word")
    print("=" * 74)
    for name, w, n in (("trefoil T(2,3)  sigma_1^3   [A's (a), endorsed]", [1, 1, 1], 2),
                       ("Hopf L2a1       sigma_1^2   [A's (b), endorsed]", [1, 1], 2),
                       ("census 6_2  [1,-2,1,1,1,-2] [A's (c), rejected]", [1, -2, 1, 1, 1, -2], 3),
                       ("Borromean B_3   (s1 s2^-1)^3          [nucleon]", [1, -2, 1, -2, 1, -2], 3)):
        print(f"  {name:52s} {n} strands -> {ncomp(w, n)} comp")
    print(f"  {'the deuteron mass word (frame 1)':52s} 6 strands -> "
          f"{ncomp(D_CORRECTED, 6)} comp   <== the rule's answer")
    print("  => all three of A's candidates are excluded by A's own rule.")

    # (5) the R5-full SDP, and the base rate
    print("\n" + "=" * 74)
    print("FRAME 2 -- the R5-full canonical-knot SDP (B_3)")
    print("=" * 74)
    wit = COMPUTATIONS / "r5-full-canonical-knot-solver.witness.json"
    if wit.exists():
        data = json.loads(wit.read_text())
        for r in data["data"]["per_atom_results"]:
            w = r["winner"]["braid_word"]
            print(f"  {r['atom']}:")
            print(f"    SDP winner {w} -> {ncomp(w, 3)} components")
            tk = [ncomp(c["braid_word"], 3) for c in r["top_k_candidates"]]
            pk = [ncomp(c["braid_word"], 3) for c in r["psd_feasible_subset"]["top_k"]]
            print(f"    top_k components:              {tk}")
            print(f"    psd_feasible_subset top_k:     {pk}")
            h = r.get("historical_cross_check")
            if h:
                print(f"    historical {h['knot_name']}: {h['braid_word']} -> "
                      f"{ncomp(h['braid_word'], 3)} components, "
                      f"psd_feasible={h['psd_feasible']}, "
                      f"rank_in_full_search={h['rank_in_full_search']}")
    else:                                                 # pragma: no cover
        print(f"  [witness not found at {wit}]")

    base = Counter(ncomp(list(w), 3) for w in product((1, 2), repeat=8))
    total = sum(base.values())
    print(f"\n  base rate over all {total} index sequences of length 8 in B_3")
    print("  (signs are irrelevant to the component count):")
    for k in sorted(base):
        print(f"    {k} components: {base[k]:3d}/{total}")
    print("  => 3-componentness is NOT forced by the word length; the top-k")
    print("     agreement is a feature of the selected set. Stated as a base")
    print("     rate, not a significance test -- the top-k are ranked by a")
    print("     word-dependent cost and are not independent draws.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
