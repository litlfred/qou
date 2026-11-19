**Conjecture (CPT-saturation as fold-orbit closure).**
Let $\sigma \colon \mathrm{Part}(n) \to \mathrm{Part}(n)$ be the transpose involution. Define $\mathrm{CPTSat}(\mathcal{K})$ to mean $\Lambda(\mathcal{K})$ is closed under the fold.

Then the Frobenius packing-density rule is a derived consequence of crystal structure:

$$
  \boxed{\;
    \rho_F(\mathcal{K})
    \;=\;
    \begin{cases}
      m_e   & \text{if } \mathrm{CPTSat}(\mathcal{K}) \text{ is false}, \\[4pt]
      2 m_e & \text{if } \mathrm{CPTSat}(\mathcal{K}) \text{ is true}.
    \end{cases}
  \;}
$$

## Elimination of the Boolean flag

The conjecture replaces the manual Boolean flag with the structural predicate $\mathrm{CPTSat}$, derived from the Type-B fold. CPT enforcement is now structural rather than post-hoc. The semantic equivalence holds for finite $\Lambda$.

## Example: $n = 3$ Wedderburn

For the blocks of $H_3(q)$, the Boolean flag is recovered as the orbit-closure check in every case.

## Correctness of the fold involution

The Type-B Cartan datum is obtained by folding. The KLR canonical basis is bar-invariant. The bar involution matches the chirality-reversal. Thus, $\sigma$ is the intrinsic fold.
