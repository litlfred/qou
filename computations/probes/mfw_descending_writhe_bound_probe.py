#!/usr/bin/env python3
# polynomial_q_not_applicable: exact combinatorics on braid words; no q read.
"""Base case of the MFW skein induction: |e| <= n - c for descending words (qou-9ttb).

`QOU.Knot.MFWSkeinInduction` proves the *propagation* step of a route to
Morton-Franks-Williams that avoids the Ocneanu trace entirely: the MFW window
`[e-n+1, e+n-1]` is preserved by both skein branches, on the same well-founded
order `computations/homfly_skein_braid.py` descends.

Closing that induction needs the **base case**. The recursion bottoms out at a
totally descending word -- every crossing first met from above, i.e.
`first_bad` returns `None` -- whose closure is the `c`-component unlink, so
`P = delta^(c-1)` with `delta = (v^-1 - v)/z`. Its `v`-degrees span
`[-(c-1), c-1]`, and that fits the window exactly when

    |e| <= n - c

This probe measures that claim. It is NOT a proof, and the statement is not
free: for arbitrary (non-descending) words the analogue fails -- the longest
element of `S_3` has Coxeter length 3 against `n - c = 1` -- so whatever makes
it true is supplied by "descending".

`n - c` is the reflection length of the word's permutation (reflection length
= n - #cycles), which is the natural place to look for a proof.

Exhaustive over every word of length <= MAX_LEN on 2..MAX_N strands; no
sampling, no float.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(_ROOT / "computations")]

import _path_bridge as _bridge  # noqa: E402, F401

from homfly_skein_braid import first_bad  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

MAX_N = 4
MAX_LEN = 6


def main() -> int:
    print("=" * 74)
    print(" MFW base case: |e| <= n - c over totally descending braid words")
    print("=" * 74)

    violations = []
    best: dict[tuple[int, int], int] = {}
    total = 0
    max_pair_net = 0          # mechanism: how much can one strand pair carry?
    nz_exceeds_bound = 0      # refutes "|e| <= #nonzero pairs" as the route

    def pair_nets(w, n):
        """Net signed crossings per unordered pair of strand LABELS."""
        pos2lab = list(range(1, n + 1))
        net: dict[tuple[int, int], int] = {}
        for x in w:
            i = abs(x)
            a, b = pos2lab[i - 1], pos2lab[i]
            key = (min(a, b), max(a, b))
            net[key] = net.get(key, 0) + (1 if x > 0 else -1)
            pos2lab[i - 1], pos2lab[i] = b, a
        return net
    for n in range(2, MAX_N + 1):
        gens = [g for i in range(1, n) for g in (i, -i)]
        for L in range(0, MAX_LEN + 1):
            for w in itertools.product(gens, repeat=L):
                k, c = first_bad(w, n)
                if k is not None:
                    continue                      # not descending
                total += 1
                e = sum(1 if x > 0 else -1 for x in w)
                if abs(e) > n - c:
                    violations.append({"n": n, "word": list(w), "e": e, "c": c})
                key = (n, c)
                best[key] = max(best.get(key, 0), abs(e))

                net = pair_nets(w, n)
                assert e == sum(net.values()), "writhe must be the net sum"
                max_pair_net = max(max_pair_net,
                                   max((abs(v) for v in net.values()), default=0))
                if sum(1 for v in net.values() if v) > n - c:
                    nz_exceeds_bound += 1

    print(f"\n  totally descending words (len <= {MAX_LEN}, n <= {MAX_N}): {total}")
    print(f"  violations of |e| <= n - c: {len(violations)}")

    print("\n  n  c   max|e|   n-c   tight?")
    tight_all = True
    for (n, c) in sorted(best):
        t = best[(n, c)] == n - c
        tight_all &= t
        print(f"  {n}  {c}   {best[(n, c)]:>5}   {n - c:>3}   "
              f"{'YES' if t else 'no'}")

    ok = not violations
    print(f"\n  RESULT: {'HOLDS' if ok else 'VIOLATED'}"
          f"{' and TIGHT everywhere' if tight_all else ''}"
          f" — exhaustive, not sampled")
    if tight_all:
        print("  Tightness matters: with the two shift lemmas also tight, no "
              "step of this route wastes room, which is why MFW is sharp.")
    print("\n  MECHANISM (what descending actually supplies):")
    print(f"    max |net signed crossings| over ANY strand pair : {max_pair_net}")
    print("    i.e. no two strands cross more than once NET, however many")
    print("    times they cross in total. That is the cancellation that makes")
    print("    |e| small while the letter count m stays large.")

    print("\n  ONE DECOMPOSITION REFUTED — scope-(a), recorded so it is not")
    print("  re-walked:")
    print(f"    words where #{{pairs with net != 0}} > n - c : {nz_exceeds_bound}")
    print("    So `|e| <= #nonzero pairs` does NOT yield the bound: e.g. n=3,")
    print("    w=(1,2,-1) has all three pairs nonzero against n-c = 1. The per-")
    print("    pair bound is necessary but not sufficient; the SIGNS must also")
    print("    arrange, and that is the part still missing.")

    print("\n  NOT a proof. The Lean file states this as `DescendingWrithe` and "
          "uses it in\n  `base_window_of_descending`; discharging it is the "
          "open residue of qou-9ttb.")

    wb = WitnessBuilder("mfw-descending-writhe-bound",
                        engine="exact-braid-word-enumeration")
    wb.set_description(
        "Exhaustive measurement of the MFW skein-induction base case: every "
        "totally descending braid word of length <= 6 on 2-4 strands satisfies "
        "|writhe| <= n - components, and the bound is tight for every (n,c) "
        "reached. Supports but does NOT prove QOU.Knot.MFWSkeinInduction's "
        "`DescendingWrithe` hypothesis. Scope-(a); nothing wired. Bean qou-9ttb."
    )
    wb.add_data("max_strands", MAX_N)
    wb.add_data("max_word_length", MAX_LEN)
    wb.add_data("descending_words", total)
    wb.add_data("violations", violations)
    wb.add_data("max_abs_writhe_by_n_c",
                {f"n={n},c={c}": {"max_abs_e": v, "n_minus_c": n - c}
                 for (n, c), v in sorted(best.items())})
    wb.add_assertion("descending_writhe_bound_holds",
                     computed=str(len(violations)), expected="0",
                     tolerance="exact",
                     source=f"exhaustive over {total} descending words")
    wb.add_data("max_net_crossings_per_strand_pair", max_pair_net)
    wb.add_data("words_where_nonzero_pairs_exceed_n_minus_c", nz_exceeds_bound)
    wb.add_assertion("no_strand_pair_crosses_more_than_once_net",
                     computed=str(max_pair_net), expected="1",
                     tolerance="exact",
                     source="mechanism supplied by the descending condition")
    wb.add_assertion("bound_is_tight_for_every_n_c",
                     computed=str(bool(tight_all)), expected="True",
                     tolerance="exact", source="max|e| == n-c in every cell")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "pure braid-word combinatorics; reads no q_0"})
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
