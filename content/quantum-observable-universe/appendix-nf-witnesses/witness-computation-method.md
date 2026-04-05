The Pauli witnesses are computed by the **hecke-engine** (versions v8/v9),
an inductive Gröbner reduction algorithm operating in the Hecke algebra
$H_A(q)$.

## Inductive construction

The engine builds the normal form strand by strand, from $A = 2$ up to the
target mass number.  At each step $A \to A + 1$:

1. **Extend**: multiply the current normal form by the transfer matrix
   entry $(c \cdot \sigma_{A-1} + d)$, where $c$ and $d$ depend on
   the crossing type (pp, nn, or pn) at strand $A$.

2. **Reduce**: apply the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$
   to eliminate all non-reduced words.

3. **Strip $I_8$**: absorb adjacency correlations $\sigma_i \sigma_{i+1}$
   into single-generator terms.

4. **Strip $I_9$**: collapse closed shell chains by absorbing $w \cdot \sigma_j$
   into its prefix $w$ when both are present.

5. **Accumulate**: update the Pauli accumulator
   $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w \cdot (-q^{-1})^{\ell(w)}$
   and the net trace $\mathrm{net} = \sum_w c_w \cdot q^{\ell(w)}$.

## Arithmetic

All intermediate computations use exact Laurent polynomials in
$\mathbb{Z}[t, t^{-1}]$ where $t = q^{1/2}$.  No floating-point
approximation is introduced until the final evaluation at $q_0$.
The denominator $2^{p_n}$ (from the doubled pn crossing convention)
is tracked separately and cancels in the Pauli ratio
$F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}| / |\mathrm{net}|$.

## Scalability

For $A \leq 12$, the full symbolic computation completes in seconds.
For medium nuclei ($A = 13$--$60$), the engine switches to $64$-bit
fixed-point evaluation at $q_0$ (denoted $f_{64}$), which avoids
the exponential growth of Laurent polynomial term counts while
preserving sufficient precision for the Pauli ratio.
