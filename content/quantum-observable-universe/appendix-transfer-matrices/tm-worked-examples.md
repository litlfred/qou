These examples work the complete transfer matrix computation for small nuclei by hand. The light nuclei are small enough that the abstract construction can be verified by eye. Walking through them makes the $\binom{A}{2}$ cost concrete: one transfer-matrix multiplication per nucleon pair.

Recall: $z = 1/(q^{1/2} + q^{-1/2})$.

## Example 1: Hydrogen ($A = 1$, $Z = 1$)

Hydrogen fixes the empty-product convention. With one proton there are no nucleon pairs, hence zero generators and zero transfer matrix multiplications.

$$
  P_{{}^1\mathrm{H}}(q) = 1 \quad\text{(empty product)}
$$

Hydrogen has no nuclear Skein polynomial. Its mass comes entirely from the proton's internal knot structure and the electron shell.

## Example 2: Deuterium ($A = 2$, $Z = 1$, $N = 1$)

Deuterium is the first case with braiding: one proton and one neutron, ordered as $[\mathfrak{p}, \mathfrak{n}]$. This single pair gives one generator $\sigma_0$ with one mixed $\mathfrak{p}$-$\mathfrak{n}$ crossing. The transfer matrix is:

$$
  M_0(q) = T_{\mathrm{mix}}(q) = \begin{pmatrix} \frac{q - q^{-1}}{2} & 1 \\[4pt] 1 & -\frac{q - q^{-1}}{2} \end{pmatrix}
$$

Taking the Markov trace against $z$ gives the traced volume:

$$
  \hat{V}_0(q) = z \cdot (M_0)_{11} + (M_0)_{21} = z \cdot \frac{q - q^{-1}}{2} + 1
$$

The nuclear Skein polynomial is this single factor:

$$
  P_{{}^2\mathrm{H}}(q) = \hat{V}_0(q)
$$

The polynomial has degree $\leq 3$ in $q^{1/2}$, taking $\binom{2}{2} = 1$ multiplication.

## Example 3: Helium-3 ($A = 3$, $Z = 2$, $N = 1$)

Helium-3 is the first case with a genuine product of transfer matrices. Its nucleons are $[\mathfrak{p}_0, \mathfrak{p}_1, \mathfrak{n}_2]$, giving generators $\sigma_0$ and $\sigma_1$.

At generator $\sigma_0$, there are two crossings: $(0, 1)$ and $(0, 2)$. See [Table 1](#tbl:tm-worked-examples-table1-data). The product in decreasing $j$ is:

$$
  M_0(q) = T_{pp}(q) \cdot T_{\mathrm{mix}}(q)
$$

The traced volume is $\hat{V}_0(q) = z \cdot (M_0)_{11} + (M_0)_{21}$.

At generator $\sigma_1$, there is one crossing: $(1, 2)$. See [Table 2](#tbl:tm-worked-examples-table2-data).

$$
  M_1(q) = T_{\mathrm{mix}}(q)
$$

The traced volume is $\hat{V}_1(q) = z \cdot (T_{\mathrm{mix}})_{11} + (T_{\mathrm{mix}})_{21}$.

The nuclear Skein polynomial is:

$$
  P_{{}^3\mathrm{He}}(q) = \hat{V}_0(q) \cdot \hat{V}_1(q)
$$

This requires $\binom{3}{2} = 3$ multiplications.

## Example 4: Helium-4 ($A = 4$, $Z = 2$, $N = 2$)

Helium-4 shows the full triangular pattern. Nucleons $[\mathfrak{p}_0, \mathfrak{p}_1, \mathfrak{n}_2, \mathfrak{n}_3]$ give generators $\sigma_0, \sigma_1, \sigma_2$ carrying three, two, and one crossings.

- $\sigma_0$ (3 crossings): $M_0(q) = T_{pp} \cdot T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}$ (See [Table 3](#tbl:tm-worked-examples-table3-data))
- $\sigma_1$ (2 crossings): $M_1(q) = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}$ (See [Table 4](#tbl:tm-worked-examples-table4-data))
- $\sigma_2$ (1 crossing): $M_2(q) = T_{nn}$ (See [Table 5](#tbl:tm-worked-examples-table5-data))

The nuclear Skein polynomial is:

$$
  P_{{}^4\mathrm{He}}(q) = \hat{V}_0(q) \cdot \hat{V}_1(q) \cdot \hat{V}_2(q)
$$

This requires $\binom{4}{2} = 6$ multiplications.

