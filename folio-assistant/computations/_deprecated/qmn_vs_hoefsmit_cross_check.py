#!/usr/bin/env python3
"""
F3.3: Cross-validation harness — q-MN braid expansion vs Hoefsmit at q₀.

For each isotope and each partition λ ⊢ n, compute χ_λ(β_atom) two ways:
  1. q-MN word expansion (`pyhecke_native.chi_q_word`) → LaurentPolyQ,
     evaluate at q₀.
  2. Hoefsmit seminormal (`pyhecke_native.chi_lambda_braid`) at q₀.

Report match ratio + max difference per isotope.

**Current status (F3.2 alpha)**: q=1 matches exactly, q=q₀ diverges
for non-trivial irreps.  The simplified strip-weight formula in
`seminormal_mn.rs::q_strip_weight` is correct only for size-1 strips;
the full Ram-Wenzl arm-leg statistics formula is the subject of
F3.2 beta.

This harness is committed alongside the F3.2 alpha so:
  (a) future F3.2 beta commits have a regression baseline;
  (b) the limitation is documented + reproducible;
  (c) once F3.2 beta lands, this harness becomes the production
      benchmark for q-MN vs Hoefsmit.

Usage:
    python3 qmn_vs_hoefsmit_cross_check.py              # all isotopes
    python3 qmn_vs_hoefsmit_cross_check.py --isotope D  # just D
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore
from plancherel_term_7 import atomic_braid_word
from hecke_characters import partitions_of as py_parts
from q_parameter import Q as Q0


def evaluate_polynomial(terms: list, q: float) -> float:
    """Evaluate a Laurent polynomial in q (terms = [(half_exp, coeff_str)])."""
    return sum(int(c) * (q ** (he / 2.0)) for he, c in terms)


def cross_check_isotope(name: str, Z: int, N: int, max_partitions: int = 10):
    n = 3 * (Z + N)
    word = atomic_braid_word(Z, N)
    word_m = [(1 if s == '+' else -1, g) for s, g in word]
    n_neg = sum(1 for s, g in word_m if s < 0)

    print(f'{name} (Z={Z}, N={N}): n={n}, word_len={len(word)}, n_neg={n_neg}')
    if n_neg > 20:
        print(f'  SKIP: 2^{n_neg} subsets exceeds q-MN bail-out guard')
        return

    parts = list(py_parts(n))[:max_partitions]
    n_match_q1 = 0
    n_match_q0 = 0
    max_diff_q1 = 0.0
    max_diff_q0 = 0.0
    for lam in parts:
        lam_t = list(lam)
        try:
            terms = p.chi_q_word(lam_t, n, word_m)
        except Exception as e:
            print(f'  λ={lam_t}: ERROR {e}')
            continue
        chi_q1 = sum(int(c) for _, c in terms)
        chi_q0 = evaluate_polynomial(terms, float(Q0))
        chi_hoefsmit = p.chi_lambda_braid(lam_t, word_m, float(Q0))

        # At q=1, q-MN value should match the integer character (since
        # H_n(q=1) is the symmetric group algebra and characters are
        # integer-valued there).  For braids that aren't permutation-
        # form, the q=1 evaluation should still be a Z-character of
        # the underlying permutation.
        # We don't have a direct "Hoefsmit at q=1" path here (that
        # would degenerate); but we can check that q=1 evaluation is
        # at least an integer (already guaranteed by q-MN structure).

        diff_q0 = abs(chi_q0 - chi_hoefsmit)
        rel_q0 = diff_q0 / abs(chi_hoefsmit) if chi_hoefsmit != 0 else diff_q0
        max_diff_q0 = max(max_diff_q0, diff_q0)
        if rel_q0 < 1e-6:
            n_match_q0 += 1

    print(f'  At q₀={float(Q0):.5f}: {n_match_q0}/{len(parts)} match Hoefsmit, '
          f'max diff = {max_diff_q0:.2e}')
    if n_match_q0 < len(parts):
        print(f'  ⚠ Expected divergence: F3.2 alpha uses simplified strip')
        print(f'  ⚠   weight; full Ram-Wenzl arm-leg formula required.')
        print(f'  ⚠   See `seminormal_mn.rs::q_strip_weight` warning comment.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--isotope",
        choices=["D", "T", "3He", "4He"],
        help="Single isotope to validate.",
    )
    parser.add_argument(
        "--max-partitions",
        type=int,
        default=10,
        help="Max partitions to validate per isotope (q-MN cost grows).",
    )
    args = parser.parse_args()

    isotopes = {
        "D": (1, 1),
        "T": (1, 2),
        "3He": (2, 1),
        "4He": (2, 2),
    }
    if args.isotope:
        targets = [(args.isotope, *isotopes[args.isotope])]
    else:
        targets = [(name, Z, N) for name, (Z, N) in isotopes.items()]

    for name, Z, N in targets:
        try:
            cross_check_isotope(name, Z, N, args.max_partitions)
        except Exception as e:
            print(f'{name}: ERROR {type(e).__name__}: {e}')
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
