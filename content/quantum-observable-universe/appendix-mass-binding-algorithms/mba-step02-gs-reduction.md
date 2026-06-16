**Algorithm (Gröbner–Shirshov reduction to Hecke normal form).**
*Quotient a braid-word $w \in B_n$ by the Hecke relation
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ to produce its canonical
representative $\mathrm{NF}(w) \in H_n(q)$.*

### Input

- *Braid word $w \in B_n$ (output of Step 1 / `alg:categorical-action`).*
- *Substrate parameter $q \in R$ (symbolic or pinned to $q_0$).*

### Output

- *Hecke normal form $\mathrm{NF}(w) = \sum_{i} c_i(q)\, T_{w_i}$ as
  an $R$-linear combination of basis elements $T_{w_i}$ indexed by
  permutations $w_i \in S_n$ (the standard $H_n(q)$ basis), with
  coefficients $c_i(q) \in R[q, q^{-1}]$.*

### Algorithm

```
1. Initialize NF ← w (read as a formal product of σ_i^{±1}).
2. Repeat until no rewrite rule applies:
   a. Apply braid relations σ_iσ_jσ_i = σ_jσ_iσ_j (|i-j| = 1)
      to canonicalise commuting / braided pairs.
   b. Apply the Hecke relation σ_i² = (q - q^{-1})σ_i + 1
      to eliminate self-squares, generating two summands.
   c. For σ_i^{-1}: rewrite σ_i^{-1} = σ_i − (q − q^{-1}) using
      the same Hecke quotient.
3. Collect like terms; output as Σ c_i(q) · T_{w_i}.
```

### Correctness conditions

*Correctness rests on two upstream definitions.*

1. *[`def:hecke-normal-form`](#def:hecke-normal-form) defines
   $H_n(q)$ as the quotient of the group algebra $R[B_n]$ by the
   Hecke ideal $\langle \sigma_i^2 - (q-q^{-1})\sigma_i - 1 \rangle$.
   The standard $T_w$ basis is then well-defined.*
2. *[`def:categorical-action`](#def:categorical-action) ensures
   that the braiding $c_{V,V}$ in $\mathbf{C}$ obeys the Hecke
   relation (the categorical specialisation that makes $\rho_n$
   factor through $H_n(q)$).*

*Confluence of the rewriter is structural: any two reduction
orders end at the same normal form by the Diamond Lemma applied
to the Hecke and braid relations (both are linear quadratic and
mutually compatible).*

### Complexity

*Worst case: exponential in $n$ (the partition count for $H_n(q)$).
Polynomial in $|w|$ after caching cycle-equivalent words. For
nucleon-scale knots ($n \leq 9$, $|w| \leq 24$) the reducer
finishes in milliseconds on the Rust core.*

### Python / Rust API entry point

```python
# Per-particle Hecke normal forms (the user-facing surface):
from pyhecke import (
    build_nucleon_nf, build_atom_nf, build_atom_nf_exact,
)

nf_proton  = build_nucleon_nf("proton")
nf_atom    = build_atom_nf(Z=2, N=2)        # ⁴He
nf_exact   = build_atom_nf_exact(Z=2, N=2)  # symbolic
```

*The Rust core is at [`tools/hecke-engine/src/gb_nf_reducer.rs`](../../../tools/hecke-engine/src/gb_nf_reducer.rs)
(canonical implementation, called via the `pyhecke-native` PyO3
wheel from the builders above).*

### Witness contract

*Canonical witness:
[`hecke-core-symbolic-migration.witness.json`](../../../computations/hecke-core-symbolic-migration.witness.json).
Records the input braid, the output basis-decomposition vector,
the chosen $q$ evaluation, and a hash of the rewriter source for
reproducibility. Per-particle assemblies are captured in
`markov-trace-assembly-{proton,neutron,deuteron}.derivation.json`
(consumed by Step 3).*

### Notes

*The reducer is the **single source** of Hecke normal forms in the
QOU pipeline; every downstream algorithm consumes `NF(w)`, not the
raw braid word. Treating the normal form as the canonical object
(rather than the braid) is what makes the rest of the chain
$q$-rational.*
