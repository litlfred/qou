#!/usr/bin/env python3
"""
The per-atom braid closure EXISTS and varies with (Z, N) — correcting this
session's own §3.4.

Bean `qou-eptr`, issue #6941. The reachability probe
(`ep_decomposition_reachability_probe`) established that the *knot dictionary*
`classify_nuclear_knot(Z, N)` factors through `A = Z + N` and assigns all 13
atoms with `A >= 4` the same complement, so no Epstein-Penner invariant of the
dictionary knot can separate them. From that this session concluded that
attaching the route per-atom "would first require identifying that closure,
which the corpus does not currently do", and framed it as a modelling decision
blocked on the owner (bean `qou-imkb`).

THAT CONCLUSION WAS WRONG, and this probe is the measurement that refutes it.
`canonical_braid_crossings.atom_canonical_crossings(Z, N)` computes a per-atom
canonical braid word live, for any `(Z, N)`. The words are genuinely per-atom:
they are pairwise distinct across the sample, INCLUDING between atoms that share
a mass number and even share a word length. Tritium `(1,2)` and helium-3 `(2,1)`
are both `A = 3` with 35 crossings and differ in four positions, with different
crossing TYPES at those positions and different exponent sums (4 vs 8).

So the object the Epstein-Penner route needs — a per-atom link whose complement
could carry a per-atom decomposition — is already computable in this corpus. What
is NOT available is the KNOT TYPE of each closure: recognising the closure of a
143-crossing braid on 36 strands is a hard computation, but it is a
knot-recognition problem with a definite answer, not a modelling choice awaiting
an owner ruling. The `qou-imkb` decision governs Model B's `T1` registry and is
a separate matter.

WHAT THIS PROBE DOES NOT CLAIM. That the words are distinct does not mean their
CLOSURES are distinct links — distinct braid words routinely close to the same
link (Markov moves, conjugation), and this probe performs no knot recognition
whatsoever. Nor does it claim any closure is hyperbolic. It establishes exactly
one thing: the per-atom object exists and is a function of `(Z, N)` rather than
of `A`, so the route is not blocked where this session said it was. Whether the
closures are distinct, and whether they are hyperbolic, are the next two
questions and both are open.

Precision: braid words are exact tuples of (index, crossing-type); every count
is an exact integer. No floats anywhere, no `q`, no anchor.

-- Ref: [manuscript] docs/audits/2026-09-06-universal-triangulation-ep-route-assessment.md §3.4
-- Ref: [manuscript] docs/audits/2026-08-29-deuteron-knot-owner-decision.md
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

ATOMS = [("protium", 1, 0), ("deuterium", 1, 1), ("tritium", 1, 2),
         ("he3", 2, 1), ("he4", 2, 2), ("li6", 3, 3), ("li7", 3, 4),
         ("be9", 4, 5), ("b11", 5, 6), ("c12", 6, 6)]


def exponent_sum(word) -> int:
    """Writhe-like exponent sum: +1 per sigma, -1 per sigma_inv, 0 otherwise.
    An invariant of the WORD, not of its closure — recorded as a cheap
    discriminator between words, never as a link invariant."""
    return sum(1 if t == "sigma" else -1 if t == "sigma_inv" else 0
               for _, t in word)


def main() -> int:
    words = {}
    for name, Z, N in ATOMS:
        words[name] = tuple(atom_canonical_crossings(Z, N))

    by_A: dict[int, list[str]] = {}
    for name, Z, N in ATOMS:
        by_A.setdefault(Z + N, []).append(name)
    same_A_pairs = [(g[i], g[j]) for g in by_A.values()
                    for i in range(len(g)) for j in range(i + 1, len(g))]

    all_distinct = len(set(words.values())) == len(words)
    same_A_all_differ = all(words[a] != words[b] for a, b in same_A_pairs)

    # The sharp case: same A, same length, still different.
    sharp = [(a, b) for a, b in same_A_pairs
             if len(words[a]) == len(words[b]) and words[a] != words[b]]

    # Length is a function of A alone (the coarse part), while the WORD is not.
    len_by_A = {}
    len_is_A_function = True
    for name, Z, N in ATOMS:
        A = Z + N
        if A in len_by_A and len_by_A[A] != len(words[name]):
            len_is_A_function = False
        len_by_A[A] = len(words[name])

    checks = [
        ("per_atom_words_all_pairwise_distinct", all_distinct,
         f"all {len(words)} sampled per-atom canonical braid words differ"),
        ("same_mass_number_atoms_have_different_words", same_A_all_differ,
         "atoms sharing a mass number A still get different words, so the word "
         "is a function of (Z,N) and not of A"),
        ("tritium_and_he3_differ_despite_same_A_and_length",
         ("tritium", "he3") in sharp or ("he3", "tritium") in sharp,
         "the sharp case: A=3 both, 35 crossings both, words still differ"),
        ("tritium_he3_exponent_sums_differ",
         exponent_sum(words["tritium"]) != exponent_sum(words["he3"]),
         "and they differ in a word invariant, not merely in presentation "
         f"({exponent_sum(words['tritium'])} vs {exponent_sum(words['he3'])})"),
        ("word_length_is_a_function_of_A_alone", len_is_A_function,
         "word LENGTH does factor through A (12 crossings per nucleon), which "
         "is why length alone cannot be the discriminator"),
    ]

    print(f"{'atom':10} {'(Z,N)':8} {'A':>3} {'len':>5} {'exp_sum':>8}")
    for name, Z, N in ATOMS:
        w = words[name]
        print(f"{name:10} {str((Z, N)):8} {Z+N:>3} {len(w):>5} "
              f"{exponent_sum(w):>8}")
    print()
    print(f"distinct words: {len(set(words.values()))} / {len(words)}")
    print(f"same-A pairs checked: {len(same_A_pairs)} -> "
          f"{'all differ' if same_A_all_differ else 'SOME IDENTICAL'}")
    if sharp:
        a, b = sharp[0]
        d = [i for i, (x, y) in enumerate(zip(words[a], words[b])) if x != y]
        print(f"sharp case {a} vs {b}: differ at {len(d)} of {len(words[a])} "
              f"positions {d}")
        for i in d[:3]:
            print(f"   pos {i}: {a} {words[a][i]}  vs  {b} {words[b][i]}")
    print()

    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")

    try:
        from qou_substrate.witness import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness not emitted: {e!r})")
        return 0 if ok == len(checks) else 1

    wb = WitnessBuilder("per-atom-braid-closure", engine="python",
                        _script_path=__file__)
    for name, cond, desc in checks:
        wb.add_assertion(name, computed="1" if cond else "0", expected="1",
                         tolerance="0.5", source=desc)
    wb.add_data("atoms", [
        {"name": n, "Z": Z, "N": N, "A": Z + N,
         "n_crossings": len(words[n]), "exponent_sum": exponent_sum(words[n])}
        for n, Z, N in ATOMS])
    wb.add_data("n_distinct_words", len(set(words.values())))
    wb.add_data("n_atoms_sampled", len(words))
    wb.add_data("corrects",
                "docs/audits/2026-09-06-universal-triangulation-ep-route-"
                "assessment.md §3.4, which said identifying the per-atom "
                "closure is something 'the corpus does not currently do'. The "
                "per-atom WORD is computable and is a function of (Z,N).")
    wb.add_data("scope",
                "Distinct braid WORDS do not imply distinct CLOSURES (Markov "
                "moves, conjugation) and this probe performs no knot "
                "recognition and no hyperbolicity test. It establishes only "
                "that the per-atom object exists and depends on (Z,N) rather "
                "than A. Whether the closures are distinct links, and whether "
                "they are hyperbolic, are the next two open questions.")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "combinatorics only: no q, no Markov parameter, no anchor"})
    print("witness written")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
