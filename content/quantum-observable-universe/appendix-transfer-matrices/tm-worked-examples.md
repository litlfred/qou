These examples work the complete transfer matrix computation for small nuclei by hand. The light nuclei are small enough that the abstract construction can be verified by eye. Walking through them makes the $\binom{A}{2}$ cost concrete: one transfer-matrix multiplication per nucleon pair.

Recall: $z = q^3/(q^2+1) = q^2/[2]_q$ (convention D; the excised convention C wrote $1/(q^{1/2}+q^{-1/2})$). **The worked numerals below have not been regenerated** — they were computed under convention C and are wrong by the $22.7\,\%$ convention gap in $z$ (2026-08-09).

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

## Example 5: Tritium beta decay (${}^3\mathrm{H} \to {}^3\mathrm{He}$)

Converting nucleon: position 1 ($\mathfrak{n} \to \mathfrak{p}$).

Parent (${}^3\mathrm{H}$):
- $\sigma_0$: $M_0^{\mathrm{par}} = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}$ (See [Table 6](#tbl:tm-worked-examples-table6-data))
- $\sigma_1$: $M_1^{\mathrm{par}} = T_{nn}$ (See [Table 7](#tbl:tm-worked-examples-table7-data))

Daughter (${}^3\mathrm{He}$):
- $\sigma_0$: $M_0^{\mathrm{dau}} = T_{pp} \cdot T_{\mathrm{mix}}$ (See [Table 8](#tbl:tm-worked-examples-table8-data))
- $\sigma_1$: $M_1^{\mathrm{dau}} = T_{\mathrm{mix}}$ (See [Table 9](#tbl:tm-worked-examples-table9-data))

Change at each generator:
At $\sigma_0$, only $(0,1)$ changes ($T_{\mathrm{mix}} \to T_{pp}$): $\Delta M_0 = T_{\mathrm{mix}} \cdot \Delta_\beta$.
At $\sigma_1$, $(1,2)$ changes ($T_{nn} \to T_{\mathrm{mix}}$): $\Delta M_1 = \Delta_\beta$.

The $Q$-value is:

$$
  \ln \frac{P_{{}^3\mathrm{He}}}{P_{{}^3\mathrm{H}}} = \ln \frac{\hat{V}_0^{\mathrm{dau}}}{\hat{V}_0^{\mathrm{par}}} + \ln \frac{\hat{V}_1^{\mathrm{dau}}}{\hat{V}_1^{\mathrm{par}}}
$$

## Quick-reference: computation count

See [Table 10](#tbl:tm-worked-examples-table10-data).
