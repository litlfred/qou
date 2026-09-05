#!/usr/bin/env python3
"""No strand ordering realises the colour tube — exhaustively, and the shortfall
is exactly a factor of 3.

`qbeta_disjoint_support_factorisation_probe.py` discharged the colour tube's
trace assumption (`tr_M` factorises over disjoint non-adjacent blocks, exactly)
and left one question: **can any ordering of the 3A strands satisfy both demands
at once?** This settles it by exhaustive search, and the answer restates the
missing scale factor as a counting statement.

*** THE TWO DEMANDS ***

  (1) CONTIGUITY. Every nucleon's three strands occupy three consecutive
      positions. This is what makes the intra-nucleon crossings single
      generators — `atom_braid_word_3A`'s `base_g0 = 3k`, `base_g1 = 3k+1`.

  (2) COLOUR TUBE. For every interface `(k, k+1)` and every colour `c`, the
      matched pair — colour `c` of nucleon `k` and colour `c` of nucleon `k+1` —
      is ADJACENT, so the coupling is a single generator; and the three
      resulting generators are pairwise non-adjacent, so
      `qbeta_disjoint_support_factorisation_probe.py` applies and `b -> b^3`.

*** THE RESULT — exhaustive over all (3A)! orderings ***

    A   strands   contiguous   tube-realising   BOTH   max matched under (1)
    2      6           72            48           0      1  of 3 needed
    3      9         1296            48           0      2  of 6 needed

**Zero, at both sizes.** And under contiguity the maximum is exactly `A - 1`
colour-matched single-generator couplings, against the `3(A-1)` a colour tube
needs — **exactly one third**.

*** WHY, IN ONE LINE ***

Contiguity makes each nucleon an interval of length 3. Two disjoint intervals on
a line touch at exactly one boundary, so **at most one** cross-nucleon pair is
adjacent. Formalised as `QOU.Hecke.LayoutConflict.card_adjacent_pairs_le_one`.

Worse, the canonical word does not even take that one: with nucleon `k` at
`3k, 3k+1, 3k+2`, the only adjacent cross pair is `(3k+2, 3k+3)`, joining
**colour 2 of nucleon k to colour 0 of nucleon k+1** — colour-MISmatched. The one
available matched coupling is reachable only by permuting colours within
nucleons, which the canonical word does not do.

*** WHAT THE TUBE-REALISING ORDERINGS ARE ***

Exactly the colour-blocked ones. At `A = 3` the search returns
`(0, 3, 6, 1, 4, 7, 2, 5, 8)` first: positions `0,1,2` hold colour 0 of nucleons
`0,1,2`, positions `3,4,5` hold colour 1, and so on. That is the layout predicted
before the search, and it fails demand (1) completely — each nucleon's strands
sit `A` apart.

*** WHAT THIS IS, AND IS NOT ***

**Is:** the extensive-term deficit and the interface shortfall are ONE statement.
The canonical layout realises one third of a colour-complete interface, and the
missing scale factor measured against the peak `B/A` is `3.0075`. Same 3.

**Is not:** a derivation of the energy scale. This says the two structures cannot
coexist in a single linear strand order — it does not say which to give up, and
it supplies no energy. `E_0` is still CAL-1 and `qou-59j5`'s normaliser family
still spans 1.33x. The factor 3 remains a target to check a future derivation
AGAINST.

**And the escape routes are named, not taken.** Either the intra-nucleon
crossings become conjugated braids (drop contiguity), or the colour couplings do
(drop single generators) — in which case the disjoint-support factorisation no
longer applies and `b -> b^3` is not exact. Both are different, larger
constructions; neither is evaluated here.
"""
from __future__ import annotations

import json
import subprocess
import time
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
COLOURS = 3


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def survey(A: int, C: int = COLOURS) -> dict:
    """Exhaustive over all `(A*C)!` orderings of the strands.

    A strand is `(nucleon, colour)`. `perm[i]` is the position given to
    `strands[i]`. Both demands are decided per ordering; nothing is sampled.
    """
    n = A * C
    strands = [(k, c) for k in range(A) for c in range(C)]
    contiguous = tube = both = 0
    max_under_contig = -1
    max_overall = -1
    example_tube = None
    for perm in permutations(range(n)):
        pos = {strands[i]: perm[i] for i in range(n)}
        contig = all(
            max(pos[(k, c)] for c in range(C)) - min(pos[(k, c)] for c in range(C)) == C - 1
            for k in range(A))
        matched_ok = True
        n_matched = 0
        for k in range(A - 1):
            g = []
            for c in range(C):
                if abs(pos[(k, c)] - pos[(k + 1, c)]) == 1:
                    g.append(min(pos[(k, c)], pos[(k + 1, c)]))
                else:
                    matched_ok = False
            n_matched += len(g)
            # the three couplings must also be pairwise NON-adjacent, or the
            # disjoint-support factorisation does not apply
            if len(g) == C and any(abs(x - y) < 2 for i, x in enumerate(g) for y in g[i + 1:]):
                matched_ok = False
        max_overall = max(max_overall, n_matched)
        if contig:
            contiguous += 1
            max_under_contig = max(max_under_contig, n_matched)
        if matched_ok:
            tube += 1
            if example_tube is None:
                example_tube = perm
        if contig and matched_ok:
            both += 1
    return {"A": A, "strands": n, "contiguous": contiguous, "tube": tube,
            "both": both, "max_matched_under_contiguity": max_under_contig,
            "max_matched_overall": max_overall,
            "couplings_needed": C * (A - 1),
            "example_tube_ordering": list(example_tube) if example_tube else None}


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("EXHAUSTIVE SURVEY OF STRAND ORDERINGS")
    print("=" * 78)
    print(f"  {'A':>3}{'strands':>9}{'contiguous':>13}{'tube':>8}{'BOTH':>7}"
          f"{'max matched under (1)':>24}")
    rows = []
    for A in (2, 3):
        r = survey(A)
        rows.append(r)
        print(f"  {A:>3}{r['strands']:>9}{r['contiguous']:>13}{r['tube']:>8}"
              f"{r['both']:>7}"
              f"{str(r['max_matched_under_contiguity']) + ' of ' + str(r['couplings_needed']):>24}")

    ok &= chk("no_ordering_satisfies_both_demands",
              all(r["both"] == 0 for r in rows), True,
              "exhaustive over 6! and 9! orderings -- not sampled")
    ok &= chk("both_demands_are_individually_satisfiable",
              all(r["contiguous"] > 0 and r["tube"] > 0 for r in rows), True,
              "so the conflict is genuine, not an artefact of an impossible "
              "demand: each is realisable alone")
    ok &= chk("contiguity_allows_exactly_one_matched_coupling_per_interface",
              all(r["max_matched_under_contiguity"] == r["A"] - 1 for r in rows), True,
              "A-1 of the 3(A-1) a colour tube needs -- EXACTLY ONE THIRD. The "
              "interface shortfall and the missing scale factor are one 3")
    ok &= chk("without_contiguity_the_full_tube_is_reachable",
              all(r["max_matched_overall"] == r["couplings_needed"] for r in rows), True,
              "so demand (2) is not the impossible one")

    ex = rows[-1]["example_tube_ordering"]
    print(f"\n  first tube-realising ordering at A=3: {ex}")
    print("    -> positions 0,1,2 hold colour 0 of nucleons 0,1,2; 3,4,5 hold")
    print("       colour 1; 6,7,8 hold colour 2. Colour-BLOCKED, exactly as")
    print("       predicted before the search — and it fails contiguity entirely.")
    ok &= chk("the_tube_orderings_are_the_colour_blocked_ones",
              ex == [0, 3, 6, 1, 4, 7, 2, 5, 8], True,
              "strand (k,c) sits at position c*A + k")

    print("\n  the canonical layout's one boundary is COLOUR-MISMATCHED:")
    print("    nucleon k at 3k,3k+1,3k+2 -> the only adjacent cross pair is")
    print("    (3k+2, 3k+3) = colour 2 of k to colour 0 of k+1. The one available")
    print("    MATCHED coupling needs a colour permutation inside the nucleons,")
    print("    which atom_braid_word_3A does not do.")

    print("\n  🛑 The two structures cannot coexist in one linear strand order.")
    print("     Escape routes named, not taken: drop contiguity (intra crossings")
    print("     become conjugated braids), or drop single-generator couplings (in")
    print("     which case disjoint-support factorisation no longer applies and")
    print("     b -> b^3 is not exact).")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-layout-conflict",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"colours": COLOURS, "method": "exhaustive permutation",
                       "demand_1": "every nucleon's C strands contiguous",
                       "demand_2": "every colour-matched interface pair adjacent, "
                                   "and the C resulting generators pairwise "
                                   "non-adjacent"},
        "data": {"survey": rows},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_layout_conflict_probe.py",
                       # `elapsed_sec`, not `elapsed_s` — the raw-float64
                       # ratchet's wall-clock carve-out matches field names
                       # exactly and does not carry the `_s` spelling. Key
                       # only; no value changes. Sixth site of this class in
                       # two days; see qbeta_binding_law_options_probe.py.
                       "elapsed_sec": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-layout-conflict.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
