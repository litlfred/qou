#!/usr/bin/env python3
"""Term-4 co-Casimir table: Σ_{λ⊢3A} 1/dim_q(λ) at q₀, with the convention pinned.

WHY THIS PRODUCER EXISTS (bean `qou-nk3h`, 2026-08-26).

`unified_low_isotope_predictor.term4_frobenius` and `mass_formula_6term` both
read `probe-term4-conventions.witness.json` for this table. That witness **had
never existed in this repository** —

    git log --oneline --diff-filter=AD --all -- '*probe-term4-conventions*'
    (empty)

— and no producer wrote it. Both loaders swallowed the miss on two paths with no
warning, so both had *always* taken their fallback. In the predictor that meant
T4 was the constant `m_e · 2.05 = 1.0475 MeV` for every isotope from D to ¹⁶O,
under a docstring claiming an algebraic per-3A trace with "coverage A ∈ {1..7}
exactly". This file supplies the table that claim always assumed.

THE CONVENTION IS MEASURED, NOT CHOSEN.

`dim_q(λ) = [n]_q! / ∏_{x∈λ} [h_x]_q` is the quantum hook-length formula, and
all ten live `dim_q` implementations in `computations/` agree on that shape. Two
axes are genuinely free, and both move the answer:

  * the q-integer normalisation — balanced `[h]_q = (q^h − q^{-h})/(q − q^{-1})`
    against unbalanced `[h]_q = (q^h − 1)/(q − 1)`;
  * the row cap — all λ ⊢ 3A, or only those with ≤ N rows.

The row cap is not a detail: capping at 6 rows removes the column partition
`(1^{3A})`, which contributes exactly 1, and at A = 7 halves the sum
(2.0599 → 1.0299).

Three independent facts already in the corpus pin both axes to **balanced,
uncapped**, so no judgement call is being made here — each is an assertion below:

  1. The consumer's own docstring quotes "at A=7 the actual value is 2.060, at
     A=6 it is 2.088". Balanced/uncapped gives 2.0599 and 2.0881. Unbalanced
     gives 2.0337/2.0506; the ≤6-row cap gives 1.0299/1.0440. Neither matches.
  2. The legacy constant `FROB_N3 = m_e·(2 + 1/[2]_q)` equals the A = 1 case
     exactly: with balanced `[2]_q = q + q⁻¹`, `2 + 1/[2]_q = 2.497290545604916`,
     which is this table's `n=3` entry to every digit computed.
  3. `dim_q((n)) = dim_q((1ⁿ)) = 1` for the two extreme blocks (convention-free:
     a single row's hooks are exactly n, n−1, …, 1, so the hook product *is*
     `[n]_q!`). Hence Σ → 2 from above, which is the asymptotic the consumer's
     fallback constant 2.05 was estimating.

NOT A FIT. No experimental input, no free parameter: a finite combinatorial sum
over partitions, evaluated at the substrate q₀ (proton pin, per the 2026-08-07
owner directive). mpmath end to end at 60 dps; no float64 anywhere in the
arithmetic, per AGENTS.md §NO-FLOAT64 (probes are not exempt).

Output: probe-term4-conventions.witness.json
  data.sigma_inv_dim_q_at_q0 = {"n=3": …, "n=6": …, …, "n=24": …}
"""
from __future__ import annotations

import _path_bridge  # noqa: F401 — Phase 6 bridge
from _precision import set_compute_dps  # noqa: E402 — before any mpmath value

set_compute_dps(60)

from mpmath import mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

Q0 = Q_MP

# A = 1..8. A ≤ 7 is what the consumers index (n = 3A ≤ 21); A = 8 is computed
# so the "decays monotonically toward 2" claim is checked one rung past the
# table rather than assumed.
A_MAX = 8


def partitions(n: int, max_part: int | None = None):
    """Every partition of `n` as a weakly-decreasing tuple."""
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, max_part), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    """Hook length of every cell of `lam`."""
    if not lam:
        return []
    conj = [sum(1 for r in lam if r >= j + 1) for j in range(lam[0])]
    return [lam[i] - (j + 1) + conj[j] - (i + 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def q_int_balanced(h: int) -> mp.mpf:
    """`[h]_q = (q^h − q^{-h})/(q − q^{-1})` at q₀ — the pinned normalisation."""
    return (Q0 ** h - Q0 ** (-h)) / (Q0 - Q0 ** (-1))


def q_factorial(n: int) -> mp.mpf:
    val = mp.mpf(1)
    for k in range(1, n + 1):
        val *= q_int_balanced(k)
    return val


def inv_dim_q(lam: tuple[int, ...], n_fac_q: mp.mpf) -> mp.mpf:
    """`1/dim_q(λ) = ∏[h_x]_q / [n]_q!` — formed as the reciprocal directly, so
    no division by a near-zero dim_q is ever performed."""
    prod = mp.mpf(1)
    for h in hook_lengths(lam):
        prod *= q_int_balanced(h)
    return prod / n_fac_q


def sigma_inv_dim_q(n: int) -> tuple[mp.mpf, int]:
    """Σ_{λ⊢n} 1/dim_q(λ) at q₀, over ALL partitions (no row cap)."""
    n_fac_q = q_factorial(n)
    total = mp.mpf(0)
    count = 0
    for lam in partitions(n):
        total += inv_dim_q(lam, n_fac_q)
        count += 1
    return total, count


def main() -> int:
    print(f"  Σ_(λ⊢3A) 1/dim_q(λ) at q₀ = {mp.nstr(Q0, 20)}  (dps={mp.dps})")
    print(f"  [h]_q = (q^h − q^-h)/(q − q^-1); all partitions, no row cap")
    print()
    print(f"  {'A':>2} {'n=3A':>5} {'#λ':>5} {'Σ 1/dim_q':>24}")
    print("  " + "-" * 40)

    table: dict[str, str] = {}
    values: dict[int, mp.mpf] = {}
    counts: dict[int, int] = {}
    for A in range(1, A_MAX + 1):
        n = 3 * A
        s, c = sigma_inv_dim_q(n)
        values[A] = s
        counts[A] = c
        table[f"n={n}"] = mp.nstr(s, 50)
        print(f"  {A:>2} {n:>5} {c:>5} {mp.nstr(s, 20):>24}")

    # --- the three corpus pins, as assertions ---
    # 1. A=1 must reproduce the legacy FROB_N3 shape 2 + 1/[2]_q exactly.
    legacy_a1 = 2 + 1 / q_int_balanced(2)
    # 2. the consumer docstring's quoted values.
    # 3. the extreme blocks are 1, so the sum decays to 2 from above.
    n21 = 21
    nf21 = q_factorial(n21)
    row_dim = 1 / inv_dim_q((n21,), nf21)
    col_dim = 1 / inv_dim_q(tuple([1] * n21), nf21)
    monotone_from = min(
        (values[A] - values[A + 1] for A in range(3, A_MAX)), default=mp.mpf(0))

    print()
    print(f"  pin 1  A=1 vs legacy 2 + 1/[2]_q : {mp.nstr(values[1], 20)} vs "
          f"{mp.nstr(legacy_a1, 20)}")
    print(f"  pin 2  A=6 -> 2.088 , A=7 -> 2.060: {mp.nstr(values[6], 6)} , "
          f"{mp.nstr(values[7], 6)}")
    print(f"  pin 3  dim_q((21)) = {mp.nstr(row_dim, 6)} , "
          f"dim_q((1^21)) = {mp.nstr(col_dim, 6)}")

    w = (
        WitnessBuilder("probe-term4-conventions", engine="python+mpmath")
        .set_description(
            "Σ_{λ⊢3A} 1/dim_q(λ) at the substrate q₀ for A = 1..8, the "
            "term-4 Frobenius co-Casimir table consumed by "
            "unified_low_isotope_predictor.term4_frobenius and "
            "mass_formula_6term. dim_q is the quantum hook-length formula "
            "[n]_q!/∏[h_x]_q with the BALANCED q-integer "
            "[h]_q = (q^h − q^-h)/(q − q^-1), summed over ALL partitions of "
            "3A with no row cap. Both of those choices are pinned by existing "
            "corpus values rather than selected here — see the assertions. "
            "Parameter-free: a finite combinatorial sum at q₀, no "
            "experimental input."
        )
        .set_content_block("prop:frobenius-codim-universal")
        .add_parameter("q_0", mp.nstr(Q0, 50))
        .add_parameter("q_int_convention", "balanced (q^h - q^-h)/(q - q^-1)")
        .add_parameter("row_cap", "none — all partitions of 3A")
        .add_parameter("A_max", A_MAX)
        .add_data("sigma_inv_dim_q_at_q0", table)
        .add_data("n_partitions", {f"n={3*A}": counts[A]
                                   for A in range(1, A_MAX + 1)})
    )

    w.add_assertion(
        name="A1_reproduces_legacy_frob_n3",
        computed=mp.nstr(values[1] - legacy_a1, 10),
        expected=mp.mpf(0), tolerance=mp.mpf("1e-40"),
        source=("the legacy FROB_N3 = m_e·(2 + 1/[2]_q) is exactly the A=1 case "
                "of this sum under the balanced normalisation — pin 1 for the "
                "q-integer convention"),
    )
    w.add_assertion(
        name="A6_matches_consumer_docstring_2p088",
        computed=mp.nstr(values[6], 10), expected=mp.mpf("2.088"), tolerance=mp.mpf("5e-4"),
        source=("unified_low_isotope_predictor.term4_frobenius docstring: "
                "'at A=6 it is 2.088' — pin 2; the unbalanced normalisation "
                "gives 2.0506 and a 6-row cap gives 1.0440, so this value "
                "discriminates both axes"),
    )
    w.add_assertion(
        name="A7_matches_consumer_docstring_2p060",
        computed=mp.nstr(values[7], 10), expected=mp.mpf("2.060"), tolerance=mp.mpf("5e-4"),
        source=("same docstring: 'at A=7 the actual value is 2.060' — pin 2"),
    )
    w.add_assertion(
        name="extreme_block_row_dim_q_is_one",
        computed=mp.nstr(row_dim - 1, 10), expected=mp.mpf(0), tolerance=mp.mpf("1e-40"),
        source=("dim_q((n)) = 1: a single row's hooks are n, n-1, …, 1, so the "
                "hook product IS [n]_q! — convention-free, pin 3"),
    )
    w.add_assertion(
        name="extreme_block_column_dim_q_is_one",
        computed=mp.nstr(col_dim - 1, 10), expected=mp.mpf(0), tolerance=mp.mpf("1e-40"),
        source="dim_q((1^n)) = 1 by conjugation symmetry of the hook multiset",
    )
    w.add_assertion(
        name="decays_monotonically_toward_two",
        computed=mp.nstr(monotone_from, 10), expected=mp.mpf(1), tolerance=mp.mpf(1),
        source=("Σ is strictly decreasing for A ≥ 3 (min successive difference "
                "> 0), approaching 2 from above since the two extreme blocks "
                "contribute 1 each — the behaviour the consumer's fallback "
                "constant 2.05 was estimating"),
    )

    w.add_caveat(
        "A ≥ 9 is not tabulated. p(27) = 3010 and the cost grows quickly; the "
        "consumers index A ≤ 7, and A = 8 is included only to check the "
        "monotone-decay assertion one rung past the table. A consumer above "
        "A = 8 still falls back to its asymptotic constant."
    )
    w.add_caveat(
        "This table does NOT validate that term 4 belongs in the binding "
        "formula, only that the quantity the formula names is computed as "
        "named. unified_low_isotope_predictor's other terms are unaffected, "
        "and its B_pred remains far from AME (bean qou-syit)."
    )

    out = w.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
