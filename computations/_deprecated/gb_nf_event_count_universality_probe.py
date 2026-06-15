#!/usr/bin/env python3
"""
Test the conjecture: GB-NF Hecke-quadratic event count is universal at
2·|S_n| = 2·n! for words in H_n(q).

For the proton's 11-crossing word in H_3, the event count was 12 = 2·|S_3|.
Test on:
  - Various words in H_3 of different lengths
  - Words in H_4, H_5 to check the generalization
  - Trivial / empty words (should give 0, falsifies universality)
  - Identity-equivalent words (e.g., σ_i σ_i^{-1})

If the count varies with word, the proton's 12 is COINCIDENTAL with PR #546's
1/12 leading coefficient. If it stabilizes at 2·n! for "long enough" words,
there's a structural saturation theorem.

Output: gb-nf-event-count-universality.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from gb_filtration_jet_tracker import HeckeElement  # noqa: E402


def reduce_and_count(n: int, word: list) -> dict:
    """Reduce `word` in H_n(q) and return event-count diagnostics."""
    E = HeckeElement.identity(n)
    for i in word:
        if i > 0:
            E = E.right_mul_T(i)
        else:
            E = E.right_mul_T_inv(-i)
    n_quadratic = sum(1 for ev in E.jet_log if ev.relation == "hecke-quadratic")
    n_ascending = sum(1 for ev in E.jet_log if ev.relation == "ascending")
    n_steps = len(E.jet_log)
    cert = E.filtration_certificate()
    filtration_shape = {grade: len(cert[grade]) for grade in cert}
    return {
        "n": n,
        "word": word,
        "word_length": len(word),
        "n_steps": n_steps,
        "n_quadratic_events": n_quadratic,
        "n_ascending_events": n_ascending,
        "filtration_shape": {str(k): v for k, v in filtration_shape.items()},
        "n_terms": sum(filtration_shape.values()),
    }


def main() -> int:
    print("=" * 96)
    print("  GB-NF Hecke-quadratic event count — universality test")
    print("  Conjecture: count = 2·|S_n| = 2·n! for H_n words")
    print("=" * 96)

    # H_3 test cases
    print(f"\n  H_3 (|S_3| = 6, 2·|S_3| = 12):")
    print(f"  {'word':<35} {'len':>4} {'#quad':>6} {'#asc':>6} {'#terms':>7}")
    print("  " + "-" * 64)

    h3_cases = [
        ("trivial", []),
        ("σ_1", [1]),
        ("σ_1²", [1, 1]),
        ("σ_1 σ_1⁻¹", [1, -1]),
        ("σ_1 σ_2 σ_1", [1, 2, 1]),
        ("(σ_1 σ_2)²", [1, 2, 1, 2]),
        ("(σ_1 σ_2)³ (Borromean)", [1, 2, 1, 2, 1, 2]),
        ("σ_1⁵", [1] * 5),
        ("σ_1¹⁰", [1] * 10),
        ("σ_1⁷ σ_2⁴ (proton intra)", [1] * 7 + [2] * 4),
        ("σ_2⁷ σ_1⁴ (mirror)", [2] * 7 + [1] * 4),
        ("σ_1 σ_2 σ_1 σ_2 σ_1", [1, 2, 1, 2, 1]),
        ("σ_1¹⁵", [1] * 15),
        ("σ_1²⁰", [1] * 20),
        ("trefoil σ_1³", [1, 1, 1]),
        ("figure-8 (σ_1 σ_2⁻¹)²", [1, -2, 1, -2]),
    ]

    h3_results = []
    for name, word in h3_cases:
        r = reduce_and_count(3, word)
        r["name"] = name
        h3_results.append(r)
        print(f"  {name:<35} {r['word_length']:>4} {r['n_quadratic_events']:>6} {r['n_ascending_events']:>6} {r['n_terms']:>7}")

    # H_4 test cases
    print(f"\n  H_4 (|S_4| = 24, 2·|S_4| = 48):")
    print(f"  {'word':<35} {'len':>4} {'#quad':>6} {'#asc':>6} {'#terms':>7}")
    print("  " + "-" * 64)
    h4_cases = [
        ("σ_1 σ_2 σ_3", [1, 2, 3]),
        ("σ_1 σ_2 σ_3 σ_2 σ_1", [1, 2, 3, 2, 1]),
        ("σ_1 σ_2 σ_3 σ_3 σ_2 σ_1", [1, 2, 3, 3, 2, 1]),
        ("σ_1¹⁰", [1] * 10),
        ("σ_1⁵ σ_2⁵", [1] * 5 + [2] * 5),
        ("σ_1⁷ σ_2⁴ σ_3⁵ (extended proton)", [1] * 7 + [2] * 4 + [3] * 5),
        ("(σ_1 σ_2 σ_3)⁴", [1, 2, 3] * 4),
        ("(σ_1 σ_2 σ_3 σ_2)³", [1, 2, 3, 2] * 3),
    ]
    h4_results = []
    for name, word in h4_cases:
        r = reduce_and_count(4, word)
        r["name"] = name
        h4_results.append(r)
        print(f"  {name:<35} {r['word_length']:>4} {r['n_quadratic_events']:>6} {r['n_ascending_events']:>6} {r['n_terms']:>7}")

    # Saturation analysis
    print(f"\n  Saturation analysis:")
    print(f"    H_3 quadratic counts: {sorted(set(r['n_quadratic_events'] for r in h3_results))}")
    print(f"    Counts == 12 in H_3:  {sum(1 for r in h3_results if r['n_quadratic_events'] == 12)} / {len(h3_results)}")
    print(f"    Counts == 0 in H_3:   {sum(1 for r in h3_results if r['n_quadratic_events'] == 0)} / {len(h3_results)}")
    print(f"    H_4 quadratic counts: {sorted(set(r['n_quadratic_events'] for r in h4_results))}")
    print(f"    Counts == 48 in H_4:  {sum(1 for r in h4_results if r['n_quadratic_events'] == 48)} / {len(h4_results)}")

    # Honest verdict
    h3_unique_counts = sorted(set(r["n_quadratic_events"] for r in h3_results))
    if len(h3_unique_counts) > 1:
        print(f"\n  VERDICT: Conjecture 'event count = 2·|S_n| universally' is FALSE.")
        print(f"    H_3 quadratic counts vary across words: {h3_unique_counts}")
        print(f"    The proton's 12 is NOT the universal count — it's specific to that word.")
        print(f"    Coincidence with PR #546's 1/12 leading coefficient is suspect.")
    else:
        print(f"\n  VERDICT: H_3 event count is UNIFORM at {h3_unique_counts[0]}.")

    witness = {
        "computation": "gb-nf-event-count-universality",
        "description": (
            "Tests the conjecture that GB-NF Hecke-quadratic event "
            "count equals 2·|S_n| = 2·n! universally across words in "
            "H_n(q). Compares against the proton's 12 = 2·|S_3| match "
            "with PR #546's leading-coefficient denominator."
        ),
        "reference_blocks": [
            "prop:gb-spectral-sequence",
            "prop:graded-markov-trace-from-gs-filtration",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "h3_results": h3_results,
        "h4_results": h4_results,
        "h3_quadratic_count_distinct_values": h3_unique_counts,
        "conjecture_universal_event_count": (
            "FALSE" if len(h3_unique_counts) > 1 else "consistent at " + str(h3_unique_counts[0])
        ),
    }
    out = HERE / "gb-nf-event-count-universality.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
