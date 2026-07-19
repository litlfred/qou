## Example 8: Bismuth-210 ($A = 210$, $Z = 83$, $N = 127$)

${}^{210}\mathrm{Bi} \to {}^{210}\mathrm{Po}$ ($\beta^-$). The heaviest nucleus in the verification table, requiring $\binom{210}{2} = 21{,}945$ multiplications.

See [Table 6](#tbl:tm-heavy-atom-examples-table6-data). Both parent counts sit one above a magic number. The daughter's neutron count $N' = 126$ hits a magic closure.

209 generators, each carrying up to 209 crossings at $\sigma_0$. At generator $\sigma_i$:
- $j < 83$: $T_{pp}$
- $83 \leq j < 210$: $T_{\mathrm{mix}}$ if $i < 83$, $T_{nn}$ if $i \geq 83$

The converting neutron (position 83) affects $\sigma_0$ through $\sigma_{83}$. The daughter gains a closed neutron shell at $N' = 126$. The proton count moves from $n_{\mathrm{out}} = 1$ to $n_{\mathrm{out}} = 2$.

See [Table 7](#tbl:tm-heavy-atom-examples-table7-data). The computation is exact. Every jet order through the $209$-jet is included in the product.

## Summary: shell structure across the periodic table

See [Table 8](#tbl:tm-heavy-atom-examples-table8-data).

Transitions that create or destroy a closed sub-link at a magic number have the largest matrix-element corrections. ${}^{137}\mathrm{Cs}$ has the smallest residual (9%) because the daughter ${}^{137}\mathrm{Ba}$ is one neutron short of the $n = 82$ closure.

The shell correction is the discrete structure of the Skein polynomial already present in the framework. Quantitative computation requires deriving the magic numbers from $q$ and determining the shell energy scale $\lambda_{\mathrm{shell}}$.
