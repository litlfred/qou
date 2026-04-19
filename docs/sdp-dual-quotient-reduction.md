# SDP-dual quotient: working in the Frobenius-active subalgebra

## The idea

For each atom braid word W, the LP/SDP dual of the confinement
feasibility problem assigns a **shadow price** to every
Frobenius-positivity constraint (one per NF basis direction in H_3,
one per Wedderburn block λ ⊢ 3A in H_{3A}).  **Zero shadow price =
inactive constraint = basis direction we can quotient out.**

The partition sum
```
tr_M(W) = Σ_{λ ⊢ 3A} w_λ · χ_λ(W) / d_λ
```
is a projection onto *all* blocks of H_{3A}.  But for a specific
atom braid word W, many blocks contribute ZERO or negligible
shadow price in the SDP dual.  Dropping those gives an exact
quotient of H_{3A} in which we work with dramatically fewer
partitions.

## Why this is principled (not truncation)

1. **Exact for zero-χ partitions.** For any braid word W and
   partition λ with χ_λ(W) = 0, the partition contributes 0 to
   tr_M.  Dropping it is exact.

2. **Exact for zero-shadow-price partitions.** The LP/SDP dual
   identifies which constraints are inactive.  If the dual's
   Lagrangian `L = objective + Σ y_λ · constraint_λ` has y_λ = 0,
   removing constraint_λ doesn't change the optimum.  The
   corresponding basis direction is a **free direction** — it
   doesn't enter the optimal solution.

3. **Controlled for small-but-nonzero shadow prices.**  If
   y_λ · w_λ · χ_λ is below some threshold, the error from
   dropping is bounded by the sum of dropped contributions.

## H_{3A} block structure

H_{3A}(q) decomposes as:
```
H_{3A}(q) = ⊕_{λ ⊢ 3A} Mat_{d_λ}(ℂ) · e_λ
```
with e_λ the Wedderburn central idempotent.  Each block is a
dim_λ × dim_λ matrix algebra.

**Feasibility cost per block:**

| Block property | SDP size | Feasible? |
|----------------|---------:|----------:|
| dim_λ small (≤ 10) | ≤ 10 × 10 | trivially |
| dim_λ medium (~100) | 100 × 100 | seconds |
| dim_λ large (~6000) | 6000 × 6000 | infeasible by dense SDP |

For n = 18 (6Li), the largest block is dim ~ 6006 — the single
infeasibility bottleneck.

## The SDP-dual quotient algorithm

```
Input: atom braid word W on 3A strands
Output: tr_M(W) computed in a reduced algebra

1. Enumerate partitions λ ⊢ 3A.
2. For each λ:
   a. Compute χ_λ(W) cheaply via Hoefsmit seminormal trace.
   b. Mark λ as ACTIVE if χ_λ(W) ≠ 0 (to numerical threshold).
3. Among active partitions, solve the (reduced-size) SDP dual.
   The dual shadow prices y_λ identify which ACTIVE partitions
   also carry non-zero weight in the confinement optimum.
4. Compute tr_M(W) = Σ_{λ: active, y_λ > 0} w_λ · χ_λ(W) / d_λ.
```

Step 2 is essentially a **pre-filter**; step 3 is the **SDP
reduction**.

## Concrete expected sizes

For 6Li (Z=3, N=3, A=6, n=18) with a typical atom braid word:

- Total partitions: 385
- Expected ACTIVE (χ_λ ≠ 0): probably 20-80, since the braid
  word is "nucleon-chain-like" and only matches irreps with
  compatible cycle / content structure
- Expected DUAL-POSITIVE (y_λ > 0): even fewer

This would reduce the 6Li partition sum from 385 to ~30 — each
of feasible SDP size.

## Connection to confinement contraction

The confinement contraction H_{3A} → H_A (treating each nucleon
as a single closed knot) is a SPECIFIC case of the SDP-dual
quotient: the active irreps of H_{3A} that couple to the
A-strand confined atom are exactly the ones whose partition λ
respects the nucleon grouping (i.e., λ is a "coarsening" of a
3A → A strand relabeling).  The SDP dual's shadow prices would
concentrate on exactly those partitions.

## Why this is especially natural for atoms

The atom braid word is NOT generic:

- 3 strands per nucleon have internal B₃ + quark-crossing + gluon
  structure
- Inter-nucleon crossings connect ONLY adjacent (3k+2, 3k+3) pairs
- No strand "jumps" across more than one nucleon

This BAND-LIMITED structure means only partitions whose Young
diagrams respect the A-block banded decomposition carry
non-zero character.  The vast majority of λ ⊢ 3A are irrelevant
for atom words — exactly what the SDP dual will identify.

## Implementation complexity

**Naive:** p(3A) characters, one per partition.  For 6Li, 385
characters.  Each costs O(dim_λ² × word_length) — dominated
by the dim_λ = 6006 partition alone.

**SDP-dual-quotient:**

- Step 2 pre-filter: compute all 385 characters but in sparse
  form (early exit if identity-block is zero, etc.).  Cost:
  ~10-100× cheaper than full character.
- Step 3 reduced SDP: work on ~30 active partitions, each dim
  ≤ 100 or so.  Reduced SDP size: ~30 × 100 × 100 = 3 × 10⁵
  entries, vs 385 × 6006² = 1.4 × 10¹⁰.  **5 orders of magnitude
  smaller.**

## Proposed prototype

Extend `atom_sdp_gluon_search.py` with:

```python
def trM_sdp_quotient(Z, N, gluons, include_inter):
    """Markov trace via SDP-dual-quotient: keep only partitions
    with non-zero shadow price at the atom-level feasibility."""
    word = atom_word_with_gluons(Z, N, gluons, include_inter)
    active = []
    for shape in partitions_of(3 * (Z + N)):
        chi = quick_character(shape, word)
        if abs(chi) > 1e-12:
            active.append((shape, chi))
    # Now the reduced partition sum — already SDP-feasible since
    # we dropped the sparse blocks.  Atom-level dual to identify
    # further zero-shadow-price partitions is a refinement.
    total = 0.0
    for shape, chi in active:
        d_q = dim_q(shape)
        d_l = ...
        w_l = d_q ** 2 / q_factorial(n)
        total += w_l * chi / d_l
    return total
```

This is already a major speedup (from p(3A) to |active|), and
adding the full SDP-dual reduction tightens it further.

## Action plan

1. **Minimal version (pre-filter only)**: compute the quick
   character pre-filter; drop zero-χ partitions.  Likely
   drops 80-95% of partitions for atom words.
2. **Full SDP-dual version**: formulate and solve the reduced
   atom-level SDP dual; drop partitions with y_λ = 0.
3. **Integrate with `atom_sdp_gluon_search`**: unlocks 4He in
   seconds, 6Li in minutes, 9Be in hours, 12C perhaps in a
   day — all currently infeasible by naïve partition sum.

The SDP-dual quotient is the right mathematical framework for
"work where the atom braid actually lives in H_{3A}" — the
small sub-algebra picked out by the Frobenius constraints.
