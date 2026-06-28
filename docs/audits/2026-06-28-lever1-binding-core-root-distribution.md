# Lever-1 fibre kernel, Stage 9: the binding cores are generic bar-symmetric residues (mixed unit-circle root split)

**Date:** 2026-06-28
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)` for the binding genfun)
**Compute:** [`computations/substrate/lever1_binding_core_root_distribution.py`](../../computations/substrate/lever1_binding_core_root_distribution.py)
**Witness:** [`computations/substrate/lever1-binding-core-root-distribution.witness.json`](../../computations/substrate/lever1-binding-core-root-distribution.witness.json)
**Predecessor:** Stage 8 [`2026-06-28-lever1-binding-core-bar-symmetric-irreducible.md`](2026-06-28-lever1-binding-core-bar-symmetric-irreducible.md).
**Closes (this session's algebraic line):** the lever-1 binding-correction characterization Stages 6–9.

## What this stage does

The cores `R_m` (m=6..11) are palindromic, irreducible over ℚ, pairwise coprime, substrate-positive
(Stage 8). The remaining decidable fingerprint is their **unit-circle root distribution**: a
"q-special-function" core (cyclotomic / Salem / Lehmer type) has all — or all-but-one-pair — of its
roots on `|q|=1`; a generic bar-even residue has a mix of on-circle and off-circle `z ↔ 1/z` pairs.

The count is **exact** (no numerics): for a self-reciprocal `R_m` of degree `2n`, the Dickson
substitution `y = q + 1/q` gives `R_m(q) = q^n·Q(y)` with `deg Q = n`; a root is on `|q|=1` iff its
`y ∈ [−2,2]` is real, so `#on-circle = 2·#(real roots of Q in (−2,2))`, counted by sympy's Sturm-based
`count_roots`.

## Result

| m | deg `R_m` | on-circle | off-circle | % on | `R_m(1)` factorization |
|---|---:|---:|---:|---:|---|
| 6 | 8 | 4 | 4 | 50% | 2²·7 |
| 7 | 10 | 6 | 4 | 60% | 2⁴ |
| 8 | 14 | 6 | 8 | 43% | 2·17 |
| 9 | 28 | 14 | 14 | 50% | 2⁴·7·11 |
| 10 | 34 | 24 | 10 | 71% | 2⁴·83 |
| 11 | 46 | 32 | 14 | 70% | 2⁶·3·47 |

Two facts:

1. **Mixed root distribution.** Every core has a substantial fraction of roots **off** the unit circle
   (in reciprocal `z ↔ 1/z` groups). No core is cyclotomic-type (already known: irreducible
   non-cyclotomic) and none is Salem-type (which would have exactly one off-circle reciprocal pair).
   The on-circle fraction (43%–71%) is irregular. These are **generic bar-symmetric residues**.

2. **No combinatorial law in `R_m(1)`.** The values 28, 16, 34, 1232, 1328, 9024 factor as
   `2²·7, 2⁴, 2·17, 2⁴·7·11, 2⁴·83, 2⁶·3·47` — a high power of 2 times scattered primes (17, 83, 47)
   with no recognizable pattern, consistent with generic (not special-function) content.

## Interpretation and scope (AGENTS.md refuted-claim discipline)

- **Positive, derived (exact on m=6..11):** the on/off-unit-circle split and the `R_m(1)`
  factorizations. The cores are **generic** bar-even irreducible polynomials — not cyclotomic, not
  Salem, not a recognizable q-special-function.
- **(a)-scoped, NOT a (b)-exclusion:** "the binding correction has no finite special-function closed
  form" is the cumulative reading of Stages 6–9, supported through m=11; it is not a proved theorem.

## Net conclusion of the algebraic-characterization line (Stages 6–9)

Across four disciplined, no-fit, falsifiable stages the binding-correction structure is now fully
mapped on the **algebraic (real-q, exact-data) side**:

```
S(m) = Σ_{λ⊢m} dim_q(λ)              (binding period; q=1 → involution numbers)
     = q-involution skeleton  S(m−1) + [m−1]_q S(m−2)   (seed-exact, drifts beyond)
       + correction  D(m)
D(m) = (q−1)²                         · universal O(h²) fibre prefactor          [Stage 7]
     × ∏_d Φ_d(q)^{e}                 · cyclotomic tower, odd-d rule Φ_d | D(d+1) [Stage 7]
     × R_m(q)                         · pairwise-coprime, irreducible, bar-symmetric,
                                        substrate-positive cores of growing degree [Stage 8]
                                        with a mixed unit-circle root split — generic
                                        bar-even residues, NOT a special function     [Stage 9]
```

Stages 3–6 already excluded any finite low-order q-difference operator and any single low-order
q-hypergeometric element. Stage 9 closes the remaining "is the residue a recognizable special object?"
question: **no** — it is genuine cyclotomic-completion (Habiro-ring) content. Further *algebraic*
probing of the real-q tower has diminishing returns; the residue is what it is.

**Where the genuine closure lives.** The element that would *derive* (rather than describe) this tower
is the binding-τ keystone — the owner-gated abelianised `λ_SW`-holonomy / SW-residue construction on
the color `E_q` (the `tr B` / Gauss–Manin monodromy side, recorded in this bean and
`docs/audits/2026-06-24-lever1-trB-geometric-target.md`). The algebraic side has now supplied that
construction with a complete, exact, parameter-free **target**: a `(q−1)²·Φ_d`-tower times a tower of
pairwise-coprime bar-symmetric generic cores, with the per-`m` degrees, root splits, and `R_m(1)`
values all pinned. That is the productive hand-off.

## Next steps (none purely algebraic remaining at low cost)

- **Owner-gated:** the `λ_SW` holonomy derivation (the real closure; see the bean + #2722 coordination).
- **Optional algebraic:** extend the towers to `m ≥ 12` to test whether the off-circle fraction or the
  degree law stabilises — incremental, unlikely to change the "generic residue" conclusion.
