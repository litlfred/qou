# F3.2 — q-deformed Murnaghan-Nakayama: Implementation Roadmap

This document specifies the algorithmic content needed to upgrade
`seminormal_mn::chi_lambda_mn_qdef_stub` from a NaN-returning
placeholder to a production-grade q-deformed character recursion.

## What we're building

A function `chi_lambda_mn_qdef(λ, β, q) → q-polynomial` that computes
the Hecke character `χ^λ(T_β)` in time `O(n² · word_len)` per
character, vs. the seminormal multiplication's `O(dim_λ² · word_len)`.

At n = 18 this is ~10⁴× faster.  Crucially, the algorithm works
**directly with braid words**, not just permutations, so it applies
to atomic braids without conversion overhead.

## The core formula (Ram 1991 Theorem 4.1)

For a braid `β = σ_{i_1}^{ε_1} ... σ_{i_k}^{ε_k} ∈ B_n` with image
`T_β ∈ H_n(q)`, the character on `S^λ` is

```
χ^λ(T_β; q) = Σ over q-border-strip-tableaux T of shape λ filled by
              the cycle structure of π(β),
              of the q-deformed weight w_q(T)
```

where:

- `π(β) ∈ S_n` is the underlying permutation (forgetful map B_n → S_n).
- A **q-border-strip-tableau** is a sequence of partitions
  `∅ = μ⁰ ⊂ μ¹ ⊂ μ² ⊂ ... ⊂ μ^r = λ` where each `μ^j / μ^{j-1}` is a
  border strip of size = the j-th cycle length.
- The q-weight `w_q(T) = ∏_j q-weight(μ^{j-1} → μ^j)` factorizes
  over each step.

The q-weight of a single border-strip step μ → μ ∪ s (where s is a
strip of size k, height h, with arm-leg statistics):

```
weight(μ → μ ∪ s) = (-1)^h · q^{(k - 1 - h - h')}
                  + (q − q^{-1}) · (correction term for non-minimal-length factors)
```

where `h'` is a "co-height" (Ram 1991 §3, see also Aiston-Morton 1996
for the skein-theoretic interpretation).

## What's needed in code

### 1. q-arithmetic backend

The q-weights are Laurent polynomials in `q^{1/2}`.  Two options:

**Option A — Symbolic Laurent polynomials in q^{1/2}**
- New struct `LaurentPolyQ { terms: Vec<(i32, BigInt)> }` where the
  i32 is `2 × (exponent in q)` (so we can represent half-integer
  powers as integers).
- Operations: `+`, `-`, `*`, scalar mul, `pow`.
- Result: chi values are exact polynomials, can be evaluated at any q.
- Cost: ~4-8× slower than `f64` per arithmetic op (BigInt manipulation).

**Option B — `rug::Float` (mpfr) at fixed q**
- Substitute q early; arithmetic is on real numbers.
- Result: chi values are decimal numbers at fixed precision.
- Cost: ~30× slower than `f64` (matches existing `seminormal_mpfr`).

Recommendation: implement **A** as the canonical path
(matches user directive "symbolic in q OR high precision > 50"), with
**B** as a fast specialization for fixed-q evaluations.

### 2. Border-strip arm-leg statistics

The q-weight depends on more than just height.  Specifically, for a
border strip s of shape μ \ ν inside a partition λ, we need:

- `height(s) = (number of rows touched) - 1`
- `arm(s) = sum over cells (i,j) ∈ s of (number of cells of s
   strictly to the right in row i)`
- `leg(s) = sum over cells (i,j) ∈ s of (number of cells of s
   strictly below in column j)`

Arm-leg can be computed in O(|s|) for each strip from the cell list.

### 3. Cycle decomposition of π(β)

Forgetful map `π: B_n → S_n` sends σ_i to the transposition (i, i+1).
For a positive braid word β = σ_{i_1} ... σ_{i_k}, π(β) is the
product of transpositions; cycle decomposition is standard O(n + k).

For a mixed-sign braid word (positive and inverse generators), the
permutation is the same since σ_i and σ_i^{-1} have the same image
(both project to the transposition (i, i+1)).

But the q-character depends on the SIGNS — not just the permutation.
The q-deformation in Ram 1991 handles positive braids; for inverses,
use the Hecke relation σ^{-1} = σ - h to expand inverses, generating
sums of terms each with positive braid words.

### 4. Recursive q-MN

Pseudocode:

```rust
fn chi_q_mn(λ: &Partition, μ: &CycleType, signs: &[Sign], q: &LaurentPolyQ)
    -> LaurentPolyQ
{
    if μ.is_empty() {
        return if λ.is_empty() { 1 } else { 0 };
    }
    let head = μ[0];
    let mut total = LaurentPolyQ::zero();
    for s in q_removable_border_strips(λ, head) {
        let weight = q_weight_of_strip(&s, q, signs);  // q-Laurent polynomial
        let λ_minus = remove_strip(λ, &s);
        total += weight * chi_q_mn(&λ_minus, &μ[1..], &signs[1..], q);
    }
    total
}
```

Memoization key: `(λ, μ_offset, signs_offset)`.

### 5. Cross-validation

At `q = 1` (substitute into the LaurentPolyQ result), the q-MN
character must equal the classical MN character.  Test by sampling
random partitions and braids on small n (n ≤ 6).

At `q = q_0 ≈ 1.10998`, the q-MN character must equal the Hoefsmit
seminormal character to f64 precision.  Test by direct comparison
on n = 9 (T, ³He) and n = 12 (⁴He) atomic braids.

## Estimated effort

| Sub-task | Lines | Days |
|---|---|---|
| `LaurentPolyQ` arithmetic with BigInt coefficients | ~250 | 1 |
| Border-strip arm-leg statistics + q-weight | ~120 | 0.5 |
| Permutation cycle decomposition | ~50 | 0.25 |
| Recursive q-MN with memoization | ~100 | 0.5 |
| Inverse-generator handling (Hecke relation expansion) | ~150 | 1 |
| Cross-validation tests | ~150 | 0.5 |
| PyO3 export + wrapper | ~50 | 0.25 |
| Production benchmarks (n = 9, 12, 18) | minor | 0.5 |
| **Total** | **~870 lines** | **~4.5 days** |

## Alternative algorithms

If the Ram-Wenzl recursion proves too cumbersome for inverse
generators, alternatives:

| Algorithm | Pros | Cons |
|---|---|---|
| **Ram 1991 q-MN** (this design) | Direct, O(n²) per character | Inverse generators need expansion |
| **Aiston-Morton skein** | Polynomial-in-c (crossings) | Computes HOMFLY, not partition-resolved |
| **Jucys-Murphy elements** | Algebraic, exact | Still O(dim²) for general elements |
| **Frobenius / Hall-Littlewood** | Symmetric-function machinery | Heavy combinatorial overhead |

Ram-Wenzl is the strongest match for our use case.

## References

- **Ram 1991** "A Frobenius formula for the characters of the Hecke
  algebras", *Invent. Math.* 106. Theorem 4.1 is the central formula.
- **Wenzl 1988** "Hecke algebras of type A_n and subfactors",
  *Invent. Math.* 92. Original q-deformed seminormal forms.
- **Aiston-Morton 1996** "Idempotents of Hecke algebras of type A",
  *J. Knot Theory Ramif.* 7. Skein-theoretic alternatives.
- **Geck-Pfeiffer 2000** "Characters of finite Coxeter groups and
  Iwahori-Hecke algebras". Comprehensive reference.
