<!-- FILE_START: tm-worked-examples-intro.md -->
Before applying the transfer-matrix construction at scale, we make its mechanics concrete on the smallest tractable nuclei, where each evaluation can be followed step by step. The worked examples that follow carry this out for the light nuclei, from hydrogen through carbon.
<!-- FILE_END: tm-worked-examples-intro.md -->

<!-- FILE_START: tm-worked-examples.md -->
These examples work the complete transfer matrix computation
for small nuclei by hand, from scratch, with every step shown.
The point of doing so is twofold: the light nuclei are small
enough that the abstract construction can be verified by eye,
and walking through them makes the $\binom{A}{2}$ cost of the
method concrete — one transfer-matrix multiplication per
nucleon pair.

Recall: $z = 1/(q^{1/2} + q^{-1/2})$.

---

## Example 1: Hydrogen ($A = 1$, $Z = 1$)

Hydrogen is included to fix the empty-product convention: with
one proton there are no nucleon pairs, hence zero generators and
zero transfer matrix multiplications.

$$
  P_{{}^1\mathrm{H}}(q) =  1 \quad\text{(empty product)}
$$

Hydrogen has no nuclear Skein polynomial — its mass comes
entirely from the proton's internal knot structure (Borromean
rings) and the electron shell.

---

## Example 2: Deuterium ($A = 2$, $Z = 1$, $N = 1$)

Deuterium is the first case with any braiding at all: one proton
$\mathfrak{p}$ and one neutron $\mathfrak{n}$, ordered as
$[\mathfrak{p}, \mathfrak{n}]$.  This single pair gives one
generator $\sigma_0$, at which there is one crossing, of the
mixed $\mathfrak{p}$-$\mathfrak{n}$ type.  The transfer matrix at
$\sigma_0$ is therefore the single mixed factor:

$$
  M_0(q) =  T_{\mathrm{mix}}(q)
  = 
  \begin{pmatrix}
    \frac{q - q^{-1}}{2}
      & 1 \\[4pt]
    1 & -\frac{q - q^{-1}}{2}
  \end{pmatrix}
$$

Taking the Markov trace of $M_0$ against the weight $z$ gives
the traced volume:

$$
  \hat{V}_0(q)
  = 
  z \cdot (M_0)_{11} + (M_0)_{21}
  = 
  z \cdot \frac{q - q^{-1}}{2}
  + 
  1
$$

Since there is only the one generator, the nuclear Skein
polynomial is this single factor:

$$
  P_{{}^2\mathrm{H}}(q) =  \hat{V}_0(q)
$$

The polynomial has degree $\leq 3$ in $q^{1/2}$, and the whole
computation is the single multiplication $\binom{2}{2} = 1$.

---

## Example 3: Helium-3 ($A = 3$, $Z = 2$, $N = 1$)

Helium-3 is the first case with a genuine product of transfer
matrices.  Its two protons and one neutron are ordered as
$[\mathfrak{p}_0, \mathfrak{p}_1, \mathfrak{n}_2]$, giving two
generators, $\sigma_0$ and $\sigma_1$.

### Generator $\sigma_0$

Two crossings: $(0, 1)$ and $(0, 2)$.

See [Table 1](#tbl:tm-worked-examples-table1-data).

Product (decreasing $j$, per notation convention):

$$
  M_0(q) =  T_{pp}(q) \cdot T_{\mathrm{mix}}(q)
$$

(Here $j = 2$ contributes $T_{\mathrm{mix}}$ and $j = 1$
contributes $T_{pp}$; since these specific matrices commute,
the product equals $T_{\mathrm{mix}} \cdot T_{pp}$ as well.)

**Step-by-step multiplication:**

$$
  M_0 = 
  \begin{pmatrix}
    q-q^{-1} & 1 \\
    1 & 0
  \end{pmatrix}
  \cdot
  \begin{pmatrix}
    \frac{q-q^{-1}}{2} & 1 \\
    1 & -\frac{q-q^{-1}}{2}
  \end{pmatrix}
$$

$$
  (M_0)_{11} = 
    (q-q^{-1})\!\cdot\!\frac{q-q^{-1}}{2}
    +  1
$$

$$
  (M_0)_{21} = 
    \frac{q-q^{-1}}{2}
$$

$$
  (M_0)_{12} = 
    (q-q^{-1})
    -  \frac{q-q^{-1}}{2}
$$

$$
  (M_0)_{22} =  1
$$

**Traced volume:**

$$
  \hat{V}_0(q) =  z \cdot (M_0)_{11} + (M_0)_{21}
$$

### Generator $\sigma_1$

One crossing: $(1, 2)$.

See [Table 2](#tbl:tm-worked-examples-table2-data).

$$
  M_1(q) =  T_{\mathrm{mix}}(q)
$$

**Traced volume:**

$$
  \hat{V}_1(q) =  z \cdot (T_{\mathrm{mix}})_{11} + (T_{\mathrm{mix}})_{21}
$$

### Nuclear Skein polynomial

$$
  P_{{}^3\mathrm{He}}(q) =  \hat{V}_0(q) \cdot \hat{V}_1(q)
$$

**Computation count:** $\binom{3}{2} = 3$ transfer matrix
multiplications (2 at $\sigma_0$, 1 at $\sigma_1$).

---

## Example 4: Helium-4 ($A = 4$, $Z = 2$, $N = 2$)

Helium-4 shows the full triangular pattern.  Its two protons and
two neutrons, ordered as
$[\mathfrak{p}_0, \mathfrak{p}_1, \mathfrak{n}_2, \mathfrak{n}_3]$,
give three generators $\sigma_0$, $\sigma_1$, $\sigma_2$, carrying
three, two and one crossings respectively.

### Generator $\sigma_0$ (3 crossings)

See [Table 3](#tbl:tm-worked-examples-table3-data).

$$
  M_0(q) =  T_{pp} \cdot T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}
$$

### Generator $\sigma_1$ (2 crossings)

See [Table 4](#tbl:tm-worked-examples-table4-data).

$$
  M_1(q) =  T_{\mathrm{mix}} \cdot T_{\mathrm{mix}} =  T_{\mathrm{mix}}^2
$$

### Generator $\sigma_2$ (1 crossing)

See [Table 5](#tbl:tm-worked-examples-table5-data).

$$
  M_2(q) =  T_{nn}
$$

### Nuclear Skein polynomial

$$
  P_{{}^4\mathrm{He}}(q) =  \hat{V}_0(q) \cdot \hat{V}_1(q) \cdot \hat{V}_2(q)
$$

**Computation count:** $\binom{4}{2} = 6$ transfer matrix
multiplications (3 at $\sigma_0$, 2 at $\sigma_1$, 1 at $\sigma_2$).

---

## Example 5: Tritium beta decay (${}^3\mathrm{H} \to {}^3\mathrm{He}$)

${}^3\mathrm{H}(\mathfrak{p}, \mathfrak{n}, \mathfrak{n}) \to {}^3\mathrm{He}(\mathfrak{p}, \mathfrak{p}, \mathfrak{n})$.

Converting nucleon: position 1 ($\mathfrak{n} \to \mathfrak{p}$).

### Parent (${}^3\mathrm{H}$)

**Generator $\sigma_0$** (crossings with nucleons 1 and 2):

See [Table 6](#tbl:tm-worked-examples-table6-data).

$M_0^{\mathrm{par}} = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}$

**Generator $\sigma_1$** (crossing with nucleon 2):

See [Table 7](#tbl:tm-worked-examples-table7-data).

$M_1^{\mathrm{par}} = T_{nn}$

### Daughter (${}^3\mathrm{He}$)

**Generator $\sigma_0$:**

See [Table 8](#tbl:tm-worked-examples-table8-data).

$M_0^{\mathrm{dau}} = T_{pp} \cdot T_{\mathrm{mix}}$

**Generator $\sigma_1$:**

See [Table 9](#tbl:tm-worked-examples-table9-data).

$M_1^{\mathrm{dau}} = T_{\mathrm{mix}}$

### Change at each generator

At $\sigma_0$: only the $(0,1)$ crossing changes
($T_{\mathrm{mix}} \to T_{pp}$, shift by $+\Delta_\beta$).

$$
  \Delta M_0 = T_{\mathrm{mix}} \cdot \Delta_\beta
$$

At $\sigma_1$: the $(1,2)$ crossing changes
($T_{nn} \to T_{\mathrm{mix}}$, shift by $+\Delta_\beta$).

$$
  \Delta M_1 = \Delta_\beta
$$

### $Q$-value

$$
  \ln \frac{P_{{}^3\mathrm{He}}}{P_{{}^3\mathrm{H}}}
  = 
  \ln \frac{\hat{V}_0^{\mathrm{dau}}}{\hat{V}_0^{\mathrm{par}}}
  + 
  \ln \frac{\hat{V}_1^{\mathrm{dau}}}{\hat{V}_1^{\mathrm{par}}}
$$

Each term is computable from the explicit matrices above and
the universal $\Delta_\beta$.

---

## Quick-reference: computation count

See [Table 10](#tbl:tm-worked-examples-table10-data).
<!-- FILE_END: tm-worked-examples.md -->

