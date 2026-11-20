**Algorithm (Wedderburn decomposition of $H_n(q)$).**
*Decompose the Hecke algebra into its isotypic components indexed
by partitions $\lambda \vdash n$, yielding the Frobenius pairing
$\mathrm{tr}_M = \sum_\lambda y_\lambda(q)\, \chi^\lambda$ used by
Step 3.*

### Input

- *Braid index $n \in \mathbb{N}_{\geq 1}$ and substrate
  parameter $q \in R$.*

### Output

- *List of pairs $\{(\lambda, d_\lambda, y_\lambda(q))\}_{\lambda \vdash n}$
  where $d_\lambda = \dim_R V^\lambda$ (Hoefsmit-block dimension)
  and $y_\lambda(q)$ is the Wenzl–Markov $q$-weight.*

### Algorithm

```
1. Enumerate partitions λ ⊢ n.
2. For each λ:
   a. Compute d_λ (Frobenius hook-length formula at q = 1, then
      q-deform via [hook]_q).
   b. Compute y_λ(q) via the Wenzl bridge
      (`prop:wenzl-bridge-applicability-qou`).
   c. Cache the Hoefsmit irrep ρ^λ on H_n(q).
3. Return the decomposition.
```

### Correctness conditions

1. *[Markov-trace normalization for $H_n(q)$](#prop:wedderburn-trace-identity)
   gives the canonical sum $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$.*
2. *[Applicability of the Wenzl-bridge $y_\lambda$ formula in QOU](#prop:wenzl-bridge-applicability-qou)
   asserts that the Wenzl bridge applies in the QOU setting,
   giving a closed-form recursion for $y_\lambda(q)$.*
3. *[The Wedderburn--Artin mass sum is the inverse non-commutative Fourier transform on $H_n(q)$](#prop:wedderburn-as-noncomm-fourier)
   establishes the algebra-level isomorphism as a non-commutative
   Fourier transform.*
4. *The $q=1$ dimension of step 2a — the Frame–Robinson–Thrall hook-length
   formula $d_\lambda = n!/\prod_{c} h_\lambda(c)$ — is machine-checked in Lean
,
   so the block dimensions entering $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$
   are exact integers, not floating-point.*

### Complexity

*$O(p(n))$ partitions, each requiring $O(n^2)$ hook-length / cell
products. For $n \leq 9$ (nucleon-scale): at most 30 partitions.*

### Python API entry point

```python
from pyhecke import wedderburn_weight, partitions_of, partition_dimension

for lam in partitions_of(n):
    y_lam = wedderburn_weight(lam, q)
    d_lam = partition_dimension(lam)
```

*The per-partition heavy lifting lives in the submodule
[`pyhecke.wedderburn`](../../../tools/pyhecke/python/pyhecke/wedderburn.py).*

### Witness contract

*Canonical witness:
[`wedderburn-lp-ew-wiring.witness.json`](../../../computations/wedderburn-lp-ew-wiring.witness.json).
Records the per-partition $(d_\lambda, y_\lambda(q))$ table, the
chosen $q$, and the upstream Hoefsmit cell-content table from
`prop:hoefsmit-ew-cell-content` for cross-checking.*

### Notes

*The Wedderburn decomposition is the **most expensive step** in the chain for $n > 6$, as $y_\lambda(q)$ involves nested $[k]_q$ factors. The native Rust core caches partitions across braid-trace calls.*
