<!-- FILE_START: witness-computation-method.md -->
An inductive Gröbner–Shirshov reduction is the natural vehicle for the Pauli witnesses. It runs entirely in exact Laurent arithmetic, preventing floating-point error accumulation during reduction. It grows the braid one strand at a time, ensuring its strand-count induction runs in lockstep with the mass-number induction that the witnesses track. The Pauli witnesses are computed by the **hecke-engine** (versions v8/v9), which realizes this reduction in the Iwahori–Hecke algebra $H_A(q)$.

## Crossing convention

All computations use the unimodular $(1, -\mathrm{HA})$ crossing convention, writing $\mathrm{HA} = q - q^{-1}$ for the Hecke relation's discriminant:

| Crossing type | $(c, d)$ | Source |
|:---:|:---:|:---|
| $\mathfrak{p}\mathfrak{p}$ (proton–proton) | $(1, 0)$ | positive crossing $\sigma$ |
| $\mathfrak{n}\mathfrak{n}$ (neutron–neutron) | $(1, -\mathrm{HA})$ | negative crossing $\sigma^{-1} = \sigma - (q - q^{-1})$ |
| $\mathfrak{p}\mathfrak{n}$ (mixed) | $(1, -\mathrm{HA}/2)$ | averaged $\tfrac{1}{2}(\sigma + \sigma^{-1})$ |

This yields $\det T_{nn} = -1$ (unimodular), consistent with the Iwahori–Hecke inverse relation.

## Inductive construction

The engine builds the normal form strand by strand, from $A = 2$ up to the target mass number. At each step $A \to A + 1$:

1. **Extend**: multiply the current normal form by the transfer matrix entry $(c \cdot \sigma_{A-1} + d)$, where $c$ and $d$ are the crossing coefficients from the table above.
2. **Reduce**: apply the Iwahori–Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ to eliminate all non-reduced words.
3. **Strip $I_8$** (the adjacency-correlation ideal): absorb adjacency correlations $\sigma_i \sigma_{i+1}$ into single-generator terms.
4. **Strip $I_9$** (the closed-shell-chain ideal): collapse closed shell chains by absorbing $w \cdot \sigma_j$ into its prefix $w$ when both are present.
5. **Accumulate**: update the Pauli accumulator $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w \cdot (-q^{-1})^{\ell(w)}$ and the net trace $\mathrm{net} = \sum_w c_w \cdot q^{\ell(w)}$.

Steps 3 and 4 perform the reduction loop's core work. They project the expanded terms to keep the term count bounded. Quotienting each freshly extended word through the adjacency and chain-collapse ideals absorbs structurally-determined words back into the per-generator transfer-matrix factorization. Thus, the surviving support never grows to the full $A!$ dimension of $H_A(q)$. This bounded growth enables the symbolic loop to reach $A = 12$ before falling back to fixed-point $f_{64}$ evaluation.

## Arithmetic

Intermediate computations use exact Laurent polynomials in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$, where $\check{q} = q^{1/2}$ is the spinor information rate. No floating-point approximation enters until final evaluation at $q_0$. The denominator $2^{p_n}$ (from the averaged pn crossing convention) is tracked separately and cancels in the Pauli ratio $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}| / |\mathrm{net}|$.

## Scalability

For $A \leq 12$, the full symbolic computation completes in seconds. For medium nuclei ($A = 13$–$60$), the engine switches to $64$-bit fixed-point evaluation at $q_0$ (denoted $f_{64}$). This avoids the exponential growth of Laurent polynomial term counts while maintaining sufficient precision for the Pauli ratio.
<!-- FILE_END: witness-computation-method.md -->
