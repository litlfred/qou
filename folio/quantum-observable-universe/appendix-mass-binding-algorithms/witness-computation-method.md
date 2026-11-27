An inductive Gröbner–Shirshov reduction is the natural vehicle for the Pauli witnesses. It runs entirely in exact Laurent arithmetic over $\mathbb{Z}[\check{q}, \check{q}^{-1}]$, preventing floating-point error accumulation during algebraic reduction, and grows the braid one strand at a time in lockstep with the mass-number induction in $H_A(q)$.

## Crossing convention

All computations use the unimodular $(1, -h_{\mathrm{A}})$ crossing convention, writing $h_{\mathrm{A}} = q - q^{-1}$ for the Hecke relation's discriminant:

| Crossing type | $(c, d)$ | Source |
|:---:|:---:|:---|
| $\mathfrak{p}\mathfrak{p}$ (proton–proton) | $(1, 0)$ | positive crossing $\sigma$ |
| $\mathfrak{n}\mathfrak{n}$ (neutron–neutron) | $(1, -h_{\mathrm{A}})$ | negative crossing $\sigma^{-1} = \sigma - (q - q^{-1})$ |
| $\mathfrak{p}\mathfrak{n}$ (mixed) | $(1, -h_{\mathrm{A}}/2)$ | averaged $\tfrac{1}{2}(\sigma + \sigma^{-1})$ |

This yields $\det T_{nn} = -1$ (unimodular), consistent with the Iwahori–Hecke inverse relation.

## Inductive construction

The engine builds the normal form strand by strand, from $A = 2$ up to the target mass number. At each step $A \to A + 1$:

1. **Extend**: multiply the current normal form by the transfer matrix entry $(c \cdot \sigma_{A-1} + d)$, where $c$ and $d$ are the crossing coefficients from the table above.
2. **Reduce**: apply the Iwahori–Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ to eliminate all non-reduced words.
3. **Strip $I_8$** (the adjacency-correlation ideal): absorb adjacency correlations $\sigma_i \sigma_{i+1}$ into single-generator terms.
4. **Strip $I_9$** (the closed-shell-chain ideal): collapse closed shell chains by absorbing $w \cdot \sigma_j$ into its prefix $w$ when both are present.
5. **Accumulate**: update the Pauli accumulator $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w \cdot (-q^{-1})^{\ell(w)}$ and the net trace $\mathrm{net} = \sum_w c_w \cdot q^{\ell(w)}$.

Steps 3 and 4 project the expanded terms to keep the support bounded: quotienting each extended word through the adjacency and chain-collapse ideals absorbs structurally determined words back into the per-generator transfer-matrix factorization, avoiding the $A!$ dimension growth of $H_A(q)$.

## Arithmetic

Intermediate computations use exact Laurent polynomials in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$, where $\check{q} = q^{1/2}$ is the spinor information rate. No real-number specialization enters until final evaluation at $q_0$. The denominator $2^{p_n}$ (from the averaged $\mathfrak{p}\mathfrak{n}$ crossing) is tracked separately and cancels in the Pauli ratio $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}| / |\mathrm{net}|$.

## Scalability

For $A \leq 12$, the symbolic Laurent polynomial reduction completes directly. For medium and heavy nuclei ($A \geq 13$), factored $2 \times 2$ monotone transfer-matrix evaluation at $q_0$ is carried out in arbitrary-precision arithmetic ($\ge 80$ decimal digits, zero IEEE-754 binary64 rounding), avoiding exponential polynomial expansion while preserving full numerical precision.
