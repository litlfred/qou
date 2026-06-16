#!/usr/bin/env python3
# polynomial_q_not_applicable: pure utility module / no own witness output.
"""
KLR canonical-basis "cemetery" filter — reusable infra for any
Markov-class enumeration over braid words / Hecke elements.

Per CLAUDE.md §7b "Symmetric-crystal techniques (KLR / Kashiwara) —
authoring guidance":

> Decategorifying to KL bases for the classical limit. The transition
> from quantum braiding to macroscopic statistics is the functor
> mapping the KLR canonical basis to the Kazhdan–Lusztig basis of S_n.

This module exposes the cemetery + canonical-basis-class deduplication
pattern as a small standalone API so any compute that enumerates
braid candidates can drop in two extra lines and skip:

  (a) Demazure-trivial pure-power words σ_i^±k (the "cemetery" — they
      close to unknots / disjoint pairs and are not knot candidates).
  (b) Markov-equivalent / braid-equivalent duplicates (same Hecke-
      algebra image; same per-block χ fingerprint).

Reference implementation: `r5_full_canonical_knot_solver.py`, where
this filter compresses the B_3 search space at L_max=8 from 13088
syntactic words down to 138 canonical-basis classes (99 % compression).

API
───

  build_cemetery_fingerprints(word_to_fp, generators, L_max)
      Pre-compute the set of cemetery fingerprints — one per
      identity / single-generator pure-power word σ_g^±k.  The
      callable `word_to_fp(word) → fingerprint` takes a braid word
      (tuple of generator labels) and returns its hashable
      fingerprint; it must compose any internal evaluation +
      fingerprint-derivation in a single call.

  fingerprint_dedup(words, evaluator, fingerprint, cemetery)
      Generator: yield one canonical-basis-class representative per
      class, skipping cemetery classes.  Two callables are needed
      because the main loop wants to keep the full evaluation result
      (matrices, eigenvalues, ...) per kept candidate, while the
      cemetery fingerprints can be computed via composition once at
      setup:
        evaluator(word)        → eval_result   (full per-block matrices etc.)
        fingerprint(eval_result) → fp          (hashable dedup key)
      The evaluator is called for EVERY input word (even those that
      will be dropped as cemetery / dup), since its output is
      required to compute the fingerprint.  If your evaluation is
      expensive and you have a cheaper word→fp shortcut, filter
      cemetery upstream of fingerprint_dedup and feed it pre-pruned
      words.

Adopting in an existing enumerator
──────────────────────────────────

  Before:
    for word in product(GENERATORS, repeat=L):
        ev = evaluate(word)
        score(word, ev)

  After:
    def word_to_fp(word):
        return fingerprint(evaluate(word))
    cemetery = build_cemetery_fingerprints(word_to_fp, GENERATORS, L_max)
    for word, ev in fingerprint_dedup(
        product(GENERATORS, repeat=L),
        evaluator=evaluate,
        fingerprint=fingerprint,
        cemetery=cemetery,
    ):
        score(word, ev)

Candidate scripts identified by the cemetery-applicability survey
(2026-05-09, sub-agent run during issue #604 session):

  - universal-ilp.py            — HIGH potential, 4^6=4096 ops at n=6
  - ch-bond-writhe-lp.py        — HIGH potential, 4^4 × writhe groups
  - h2-integer-lp.py            — MEDIUM, 6^4 ≈ 1.3K combos at n=4

These use an OPS-tuple abstraction (named operators with state-update
fns) rather than raw B_n generators, so adopting requires defining
an evaluator(word) → fingerprint function appropriate to that
abstraction (typically: trace + per-state-component invariants).

@module computations/klr_canonical_basis_filter
"""
from __future__ import annotations

from typing import Callable, Iterable, Sequence


def build_cemetery_fingerprints(
    word_to_fp: Callable[[tuple], tuple],
    generators: Sequence,
    L_max: int,
    *,
    include_identity: bool = True,
) -> set:
    """Precompute fingerprints of every cemetery class.

    Cemetery classes are:
      - the identity (empty word) if include_identity
      - σ_g^k for each generator g and k ∈ [1, L_max]

    These are Demazure-trivial / canonical-basis-trivial elements
    (their Markov closure is an unknot or a disjoint union of unknots),
    so they should not be considered candidates for canonical knots.

    Args:
      word_to_fp(word) → hashable fingerprint.  Composes any internal
        evaluation + fingerprint-derivation in a single call (e.g.
        `lambda w: chi_fingerprint(evaluate_b3_braid(w, q))`).  The
        SAME hashing convention must be used inside `fingerprint_dedup`
        for cemetery membership tests to fire correctly.
      generators: list of generator labels (e.g. (1, -1, 2, -2)
        for B_3).  Used only to build single-generator pure-power
        words for the cemetery.  All generators are treated as
        independent — we DO NOT auto-fold inverse pairs.
      L_max: maximum word length to enumerate cemetery for.
      include_identity: include the empty word (identity) — default True.

    Returns: set of fingerprints to reject during the main search.
    """
    fps: set = set()
    if include_identity:
        fps.add(word_to_fp(tuple()))
    for g in generators:
        for k in range(1, L_max + 1):
            word = (g,) * k
            fps.add(word_to_fp(word))
    return fps


def fingerprint_dedup(
    words: Iterable[tuple],
    *,
    evaluator: Callable[[tuple], object],
    fingerprint: Callable[[object], tuple],
    cemetery: set,
    return_eval: bool = True,
):
    """Yield (word, eval_result) for one canonical-basis representative
    per class, skipping cemetery classes.

    Two different words sharing the same fingerprint *should* (under a
    well-chosen fingerprint) image to the same element of H_n(q_0).
    The fingerprint design is the caller's responsibility — note that
    a per-block trace tuple is **not** a complete invariant of the
    Hecke-algebra image (a 2×2 standard block has 4 independent
    matrix entries, but trace alone only pins down 1 of them); use
    full per-block matrix entries (rounded) for complete-invariant
    deduplication.  See `r5_full_canonical_knot_solver.chi_fingerprint`
    for the full-matrix recipe at H_3(q_0).  We keep the FIRST word
    seen per fingerprint.

    Args:
      words: iterable of candidate braid words (tuples of generator
        labels) — consumed once.
      evaluator(word) → eval_result: full evaluation of a word
        (e.g. per-block matrices, eigenvalues, traces).  Called for
        EVERY input word (including cemetery / dup candidates), since
        its output is needed to compute the fingerprint.  If your
        evaluation is expensive and you have a cheaper word→fp
        shortcut, drop cemetery upstream and feed pre-pruned words
        into this generator.
      fingerprint(eval_result) → hashable: dedup signature derived
        from the evaluator output.  Must be a complete invariant of
        the Hecke-algebra image at q_0 to avoid over-deduping
        legitimately distinct candidates.
      cemetery: set of fingerprints to reject (from
        `build_cemetery_fingerprints`).
      return_eval: if True (default), yield (word, eval_result);
        if False, yield word only.

    Yields: (word, eval_result) per kept canonical-basis-class
      representative, in enumeration order.
    """
    seen: set = set()
    for word in words:
        ev = evaluator(word)
        fp = fingerprint(ev)
        if fp in cemetery or fp in seen:
            continue
        seen.add(fp)
        yield (word, ev) if return_eval else word


def dedup_stats(
    words: Iterable[tuple],
    *,
    evaluator: Callable[[tuple], object],
    fingerprint: Callable[[object], tuple],
    cemetery: set,
) -> dict:
    """Run fingerprint_dedup and return aggregate statistics only.

    Useful for benchmarking compression ratio without storing the
    canonical-basis representatives.  Returns:

      {
        "n_words_considered":   …,
        "n_killed_by_cemetery": …,
        "n_killed_by_dedup":    …,
        "n_canonical_classes":  …,
        "compression_ratio":    n_words / n_canonical_classes,
      }
    """
    n_seen = n_cem = n_dup = 0
    seen: set = set()
    for word in words:
        n_seen += 1
        ev = evaluator(word)
        fp = fingerprint(ev)
        if fp in cemetery:
            n_cem += 1
            continue
        if fp in seen:
            n_dup += 1
            continue
        seen.add(fp)
    n_kept = len(seen)
    return {
        "n_words_considered": n_seen,
        "n_killed_by_cemetery": n_cem,
        "n_killed_by_dedup": n_dup,
        "n_canonical_classes": n_kept,
        "compression_ratio": n_seen / max(n_kept, 1),
    }


if __name__ == "__main__":
    # Self-check: smoke test on B_3 dummy fingerprint.
    from itertools import product

    def fake_eval(word):
        # Trivial fake fingerprint: sum of squared generator labels +
        # product of generators (not actually correct for H_3, but
        # exercises the dedup machinery).
        return sum(g * g for g in word), tuple(sorted(set(word))), len(word)

    def fake_fp(ev):
        return ev

    GENS = (1, 2, -1, -2)
    L_max = 4

    cem = build_cemetery_fingerprints(
        lambda w: fake_fp(fake_eval(w)), GENS, L_max,
    )
    print(f"  Cemetery fingerprints: {len(cem)}")

    stats = dedup_stats(
        product(GENS, repeat=L_max),
        evaluator=fake_eval,
        fingerprint=fake_fp,
        cemetery=cem,
    )
    print("  Smoke test stats:")
    for k, v in stats.items():
        print(f"    {k:32s}  {v}")
