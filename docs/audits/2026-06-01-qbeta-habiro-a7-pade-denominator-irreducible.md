# a_7 Padé denominator — irreducible cubic, no categorical match (2026-06-01)

> Follow-up to the [Option D audit](2026-06-01-qbeta-habiro-option-d-followup.md)
> finding (iii): a_7's coefficient sequence (110, 84, 63, 48, 34, 24, 17, 12)
> is reproduced by a Padé [3/3] rational approximant with denominator
> `D(u) = 10u³ − 24u² + 405u − 552`. This audit investigates the
> categorical interpretation of D(u).
>
> Branch: `claude/brave-mendel-FPxFl` (PR #1579).

## TL;DR

**NEGATIVE — D(u) is irreducible over ℚ with no clean categorical match in the standard candidate set (cyclotomic / binomial / Chebyshev / standard Hecke). Categorical identification of a_7 remains OPEN.**

The honest result: the Padé denominator does NOT factor cleanly, its roots are not on the unit circle, and it doesn't match any natural candidate from the framework's standard categorical-object library.

## What we found

### Algebraic properties of D(u) = 10u³ − 24u² + 405u − 552

| Property | Value |
|---|---|
| Degree | 3 (cubic) |
| Coefficient GCD | 1 (primitive over ℤ[u]) |
| Factorization over ℚ | **irreducible** |
| Rational roots | none (rational root theorem) |
| Discriminant | −2,450,171,592 (negative → 1 real + 2 complex conjugates) |
| Galois group | **S_3** (discriminant non-square) |
| GCD with `Φ_n` for n ∈ {1,2,3,4,5,6,8,12,24} | trivial (= 1) |
| Roots (numerical) | real ≈ 1.4116; complex ≈ 0.4942 ± 6.2338i |

The large imaginary part (≈6.23) of the complex conjugate roots is striking: they are NOT on the unit circle, so the roots are **not roots of unity** and the polynomial is **not cyclotomic-related**.

### Special-value evaluations

| u | D(u) |
|---|---|
| 0 | −552 |
| 1 | −161 = −7 · 23 |
| −1 | −991 (prime) |
| 2 | 242 = 2 · 11² |
| 1/2 | −1417/4 = −13 · 109 / 4 |

None of these are obvious special-value matches (e.g., D(1) ≠ 0, so u=1 is not a root).

### Coefficient-pattern analysis of a_7

The a_7 absolute coefficients `[110, 84, 63, 48, 34, 24, 17, 12]` were checked against:

- **Binomial coefficients C(n, k)**: only `84 = C(9, 3)` matches, and `12 = C(12, 1)`, `17 = C(17, 1)` — isolated coincidences, no systematic pattern.
- **Colored partitions** p_{b=2}, p_{b=3}, p_{b=4} — confirmed NO match in the prior audit ([`qbeta_habiro_a7_partition_check.py`](../../computations/qbeta/qbeta_habiro_a7_partition_check.py)).
- **Sequence differences**: first differences `[26, 21, 15, 14, 10, 7, 5]`, second differences `[5, 6, 1, 4, 3, 2]` — no clean pattern.
- **Sum at u=1**: `a_7(1) = -(110+84+63+48+34+24+17+12) = −392 = −2³ · 7²`.

The factor `7²` is mildly suggestive (number of partitions of 5? p(5) = 7), but the `2³ · 7²` combination doesn't match any standard categorical evaluation.

## What categorical interpretations FAIL

Tested and ruled out:

1. **Cyclotomic factor product** — gcd with all `Φ_n` for n ∈ {1, 2, 3, 4, 5, 6, 8, 12, 24} is trivial.
2. **Chebyshev polynomials** (T_3, U_3) — coefficient patterns don't match.
3. **Standard q-Pochhammer ratios** — none of `(u; u)_k / (u; u)_j` for small j, k produce cubic D with integer coefficients matching this pattern.
4. **Burau matrix characteristic polynomial at H_4(q)** — the Burau matrix at H_4 is 3×3, but its char.poly has coefficients in ℤ[q, q⁻¹], not pure ℤ[u] with the magnitudes in D.
5. **q-binomial coefficients** — none match the cubic with these specific coefficients.

## What MIGHT still be in scope

Untested categorical candidates (each would need a separate probe):

1. **Hecke character at a specific complex H_4(q) representation** — possibly a 3-dimensional representation evaluated at a specific braid word.
2. **Markov trace of a 4-strand braid** in a specific basis — the cubic could be the minimal polynomial of a Markov trace value.
3. **Hoefsmit matrix eigenvalue polynomial** — the Hoefsmit basis of H_n(q) is the canonical orthogonal basis; eigenvalues of certain operators may produce this cubic.
4. **Galois-conjugate triple from a degree-3 extension of ℚ(q)** — the S_3 Galois group suggests a non-abelian splitting field, possibly arising in a specific algebraic-number-theoretic context.
5. **A genuinely non-cyclotomic categorical invariant** that the framework doesn't currently capture (e.g., a quantum modular form's denominator polynomial).

## Implications for the framework

The partition-function and cyclotomic identifications surfaced earlier this session live at the SHELLS of the Habiro ladder where the structure is most symmetric:

- m = 8 (top-shared shell): **partition function p(n) — convention-stable**
- m = 6 boundary (telescoping transition): **cyclotomic prefactor Φ_1·Φ_2** (n-p signature)
- m = 8 → 4 (deuteron strand-doubling): **Φ_8² = Φ_4(u²)²** (D-n signature)

The a_7 Padé denominator sits at the m = 7 shell — between the partition top (m=8) and the cyclotomic boundary (m=6). Its irreducibility over ℚ may indicate that **the m=7 shell is precisely where the categorical structure is least cleanly separable into orthogonal pieces** — the "transition layer" where partition counting and isospin-cyclotomic interleave non-trivially.

This is a *negative finding with structural import*: the cleanest categorical layers are m=8 (partitions) and m=6 (cyclotomic); m=7 is genuinely harder.

## Open follow-ups

1. **Test for Hecke character match** at a specific H_4(q) representation with the cubic. Requires generating the explicit character polynomials for all H_4 partitions and comparing.
2. **Bring-curve period polynomial** — if the substrate's Bring-anchored structure produces degree-3 period polynomials, D(u) might come from there.
3. **Symbolic Galois search** — what's the discriminant's factorization? D = -2,450,171,592 = -2³ · 3 · 7 · ... (compute primes). Galois extension structure might point to a categorical context.

## Cross-references

- Parent audit: [Option D follow-up](2026-06-01-qbeta-habiro-option-d-followup.md)
- a_8 partition match: [a_8 partition-function match](2026-06-01-qbeta-habiro-a8-partition-function-match.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) PROBE NEW
