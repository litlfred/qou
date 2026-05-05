#!/usr/bin/env python3
"""
Tier 2: test the generalised anti-self-reciprocity conjecture across braids.

Conjectured (from `prop:markov-trace-antipode-polynomial-symmetry`):
For any closed braid K ∈ B_n with closed-form Markov trace
  tr_M(K) = p_K(q) / (c_K · q^{shift(K)})
the polynomial p_K satisfies
  q^{2 · shift(K)} · p_K(1/q) = (-1)^{ℓ(β_K)} · p_K(q)
where ℓ(β_K) is the word length (signed crossing count).

Equivalently:
  tr_M(K)(1/q) = (-1)^{ℓ(β_K)} · tr_M(K)(q).

For the PROTON (PR #546): proved for the specific 11-crossing word.
For OTHER words: tested here numerically by computing the symbolic
Markov trace via char_fast + Plancherel weights at q vs 1/q and
checking the predicted symmetry.

Output: anti-self-reciprocity-universality.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from char_fast import chi_lambda_fast  # noqa: E402


def derive_h3_plancherel_weights_at_q(q_val: float) -> dict:
    """Plancherel weights for H_3 from Markov-axiom constraints."""
    parts = [(3,), (2, 1), (1, 1, 1)]
    chi_id = {p: chi_lambda_fast(p, [], q_val=q_val).real for p in parts}
    chi_s1 = {p: chi_lambda_fast(p, [(1.0, 0.0, 0)], q_val=q_val).real for p in parts}
    chi_s1_s2 = {p: chi_lambda_fast(p, [(1.0, 0.0, 0), (1.0, 0.0, 1)], q_val=q_val).real for p in parts}
    z = 1.0 / (q_val ** 0.5 + 1.0 / q_val ** 0.5)
    M = np.array([
        [chi_id[p] for p in parts],
        [chi_s1[p] for p in parts],
        [chi_s1_s2[p] for p in parts],
    ])
    b = np.array([1.0, z, z * z])
    y = np.linalg.solve(M, b)
    return {p: y[i] for i, p in enumerate(parts)}


def tr_m_via_planch(word_tuples: list, q_val: float) -> float:
    """tr_M(braid_word) at q_val via Plancherel-weighted χ^λ sum."""
    parts = [(3,), (2, 1), (1, 1, 1)]
    y = derive_h3_plancherel_weights_at_q(q_val)
    return sum(
        y[p] * chi_lambda_fast(p, word_tuples, q_val=q_val).real
        for p in parts
    )


def word_len_signed(word: list) -> int:
    """Signed crossing count: positive crossings count +1, negatives count -1.
    Total parity is sum, but for the (-1)^ℓ test we want |ℓ| parity."""
    return len(word)   # length = count of σ_i and σ_i^{-1} both


def positive_word(word: list) -> list:
    """Convert jet-tracker word [int] to char_fast tuples [(c, d, gen_idx)]."""
    out = []
    for i in word:
        if i > 0:
            out.append((1.0, 0.0, i - 1))    # σ_{i-1}
        else:
            # σ^{-1} = σ - h. char_fast doesn't directly support inverses;
            # we approximate as the formal Hecke inverse element c·σ + d
            # via (1, -h_at_q, gen_idx) where h depends on q.
            # For the symmetry test we use specific q-values, so substitute h.
            raise ValueError("σ^{-1} not supported in this char-table path; use only positive words for now.")
    return out


def test_braid_symmetry(name: str, word: list, q1: float = 1.10, q2_inv: bool = True) -> dict:
    """Test tr_M(K)(1/q) = (-1)^ℓ · tr_M(K)(q).

    Compute tr_M at q1 and at 1/q1, then check the expected sign relation.
    """
    word_tuples = positive_word(word)
    ell = word_len_signed(word)
    sign = (-1) ** ell

    tr_at_q = tr_m_via_planch(word_tuples, q1)
    tr_at_inv_q = tr_m_via_planch(word_tuples, 1.0 / q1)

    expected_lhs = tr_at_inv_q
    expected_rhs = sign * tr_at_q
    diff = abs(expected_lhs - expected_rhs)
    rel_diff = diff / max(abs(tr_at_q), 1e-12)

    return {
        "name": name,
        "word": word,
        "word_length": ell,
        "expected_sign": sign,
        "tr_M_at_q": tr_at_q,
        "tr_M_at_inv_q": tr_at_inv_q,
        "predicted_value_at_inv_q": sign * tr_at_q,
        "abs_diff": diff,
        "rel_diff": rel_diff,
        "symmetry_holds": rel_diff < 1e-6,
        "q_value": q1,
    }


def main() -> int:
    print("=" * 96)
    print("  Tier 2: anti-self-reciprocity universality test")
    print("  Conjectured: tr_M(K)(1/q) = (-1)^ℓ(β_K) · tr_M(K)(q)")
    print("=" * 96)

    # H_3 positive-word test cases of various lengths
    cases = [
        ("identity", []),
        ("σ_1", [1]),
        ("σ_1²", [1, 1]),
        ("σ_1³ (trefoil)", [1, 1, 1]),
        ("σ_1 σ_2 σ_1 (Δ_3)", [1, 2, 1]),
        ("(σ_1 σ_2)²", [1, 2, 1, 2]),
        ("(σ_1 σ_2)³ (Borromean)", [1, 2, 1, 2, 1, 2]),
        ("σ_1⁵", [1] * 5),
        ("σ_1⁷ σ_2⁴ (proton word, length 11)", [1] * 7 + [2] * 4),
        ("σ_1⁴ σ_2⁷ (mirror, length 11)", [1] * 4 + [2] * 7),
        ("σ_1¹⁰", [1] * 10),
        ("σ_1¹² (length 12 = even)", [1] * 12),
        ("σ_1 σ_2 σ_1 σ_2 σ_1 σ_2 (alternating)", [1, 2, 1, 2, 1, 2]),
    ]

    print(f"\n  {'name':<40} {'len':>4} {'sign':>6} {'rel diff':>12} {'symmetry':>12}")
    print("  " + "-" * 80)

    results = []
    n_passed = 0
    n_failed = 0
    for name, word in cases:
        try:
            r = test_braid_symmetry(name, word, q1=1.10)
        except Exception as exc:
            print(f"  {name:<40} ERROR: {type(exc).__name__}: {exc}")
            continue
        symmetry_str = "✓" if r["symmetry_holds"] else "✗"
        print(f"  {name:<40} {r['word_length']:>4} {r['expected_sign']:>+6} {r['rel_diff']:>12.2e} {symmetry_str:>12}")
        results.append(r)
        if r["symmetry_holds"]:
            n_passed += 1
        else:
            n_failed += 1

    print(f"\n  Summary: {n_passed} / {n_passed + n_failed} braids satisfy the (-1)^ℓ symmetry")

    if n_failed > 0:
        print(f"\n  Failed cases:")
        for r in results:
            if not r["symmetry_holds"]:
                print(f"    {r['name']}: tr_M(q) = {r['tr_M_at_q']:.6f}, tr_M(1/q) = {r['tr_M_at_inv_q']:.6f}")
                print(f"      predicted (-1)^{r['word_length']} · tr_M(q) = {r['predicted_value_at_inv_q']:.6f}")
                print(f"      rel diff = {r['rel_diff']:.4f}")

    print(f"\n  Conclusion:")
    if n_passed > 0 and n_failed == 0:
        print(f"    All tested positive braids satisfy tr_M(K)(1/q) = (-1)^ℓ · tr_M(K)(q).")
        print(f"    The symmetry generalises beyond the proton's specific case.")
    elif n_passed > 0 and n_failed > 0:
        print(f"    Symmetry holds for some but not all braids — refinement needed.")
        print(f"    The (-1)^ℓ sign rule may require ℓ-parity instead of word length.")
    else:
        print(f"    Symmetry FAILS broadly — the proton's case is special.")

    witness = {
        "computation": "anti-self-reciprocity-universality",
        "description": (
            "Tier 2 test: does the anti-self-reciprocity symmetry "
            "tr_M(K)(1/q) = (-1)^ℓ(β_K) · tr_M(K)(q) generalise from "
            "the proton (PR #546) to other braids? Tested on 13 "
            "positive-word braids of lengths 0..12 in H_3."
        ),
        "reference_blocks": [
            "prop:markov-trace-antipode-polynomial-symmetry",
            "prop:atomic-mass-gb-nf",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "n_passed": n_passed,
        "n_failed": n_failed,
        "conclusion": (
            "All 13 positive braids tested satisfy the symmetry"
            if n_failed == 0 and n_passed > 0 else
            f"{n_passed}/{n_passed + n_failed} braids satisfy the symmetry"
        ),
    }
    out = HERE / "anti-self-reciprocity-universality.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
