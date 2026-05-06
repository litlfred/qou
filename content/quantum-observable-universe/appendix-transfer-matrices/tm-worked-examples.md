These examples show the complete transfer matrix computation
for small nuclei from scratch.  Every step is shown.

Recall: $z = 1/(q^{1/2} + q^{-1/2})$.

---

## Example 1: Hydrogen ($A = 1$, $Z = 1$)

One proton, no nucleon pairs.  There are **zero** generators
and **zero** transfer matrix multiplications.

$$
  P_{{}^1\mathrm{H}}(q) =  1 \quad\text{(empty product)}
$$

Hydrogen has no nuclear Skein polynomial — its mass comes
entirely from the proton's internal knot structure (Borromean
rings) and the electron shell.

---

## Example 2: Deuterium ($A = 2$, $Z = 1$, $N = 1$)

One proton $\mathfrak{p}$, one neutron $\mathfrak{n}$.

**Nucleon ordering:** $[\mathfrak{p}, \mathfrak{n}]$.

**Generators:** one generator $\sigma_0$.

**Crossings at $\sigma_0$:** one crossing, type
$\mathfrak{p}$-$\mathfrak{n}$ = mixed.

**Transfer matrix product:**

$$
  M_0(q) =  T_{\mathrm{mix}}(q)
  = 
  \begin{pmatrix}
    \frac{q - q^{-1}}{2}
      & 1 \\[4pt]
    1 & -\frac{q - q^{-1}}{2}
  \end{pmatrix}
$$

**Markov-traced volume:**

$$
  \hat{V}_0(q)
  = 
  z \cdot (M_0)_{11} + (M_0)_{21}
  = 
  z \cdot \frac{q - q^{-1}}{2}
  + 
  1
$$

**Nuclear Skein polynomial:**

$$
  P_{{}^2\mathrm{H}}(q) =  \hat{V}_0(q)
$$

This is a single factor — no product needed.  The polynomial
has degree $\leq 3$ in $q^{1/2}$.

**Computation count:** $\binom{2}{2} = 1$ transfer matrix
multiplication.

---

## Example 3: Helium-3 ($A = 3$, $Z = 2$, $N = 1$)

Two protons, one neutron.

**Nucleon ordering:** $[\mathfrak{p}_0, \mathfrak{p}_1, \mathfrak{n}_2]$.

**Generators:** $\sigma_0$ and $\sigma_1$.

### Generator $\sigma_0$

Two crossings: $(0, 1)$ and $(0, 2)$.

| Crossing | Pair | Type | Transfer matrix |
|----------|------|------|-----------------|
| $(0, 1)$ | $\mathfrak{p}_0$-$\mathfrak{p}_1$ | pp | $T_{pp}$ |
| $(0, 2)$ | $\mathfrak{p}_0$-$\mathfrak{n}_2$ | mix | $T_{\mathrm{mix}}$ |

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

| Crossing | Pair | Type | Transfer matrix |
|----------|------|------|-----------------|
| $(1, 2)$ | $\mathfrak{p}_1$-$\mathfrak{n}_2$ | mix | $T_{\mathrm{mix}}$ |

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

Two protons, two neutrons.

**Nucleon ordering:** $[\mathfrak{p}_0, \mathfrak{p}_1, \mathfrak{n}_2, \mathfrak{n}_3]$.

**Generators:** $\sigma_0$, $\sigma_1$, $\sigma_2$.

### Generator $\sigma_0$ (3 crossings)

| Crossing | Pair | Type | Matrix |
|----------|------|------|--------|
| $(0, 1)$ | $\mathfrak{p}$-$\mathfrak{p}$ | pp | $T_{pp}$ |
| $(0, 2)$ | $\mathfrak{p}$-$\mathfrak{n}$ | mix | $T_{\mathrm{mix}}$ |
| $(0, 3)$ | $\mathfrak{p}$-$\mathfrak{n}$ | mix | $T_{\mathrm{mix}}$ |

$$
  M_0(q) =  T_{pp} \cdot T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}
$$

### Generator $\sigma_1$ (2 crossings)

| Crossing | Pair | Type | Matrix |
|----------|------|------|--------|
| $(1, 2)$ | $\mathfrak{p}$-$\mathfrak{n}$ | mix | $T_{\mathrm{mix}}$ |
| $(1, 3)$ | $\mathfrak{p}$-$\mathfrak{n}$ | mix | $T_{\mathrm{mix}}$ |

$$
  M_1(q) =  T_{\mathrm{mix}} \cdot T_{\mathrm{mix}} =  T_{\mathrm{mix}}^2
$$

### Generator $\sigma_2$ (1 crossing)

| Crossing | Pair | Type | Matrix |
|----------|------|------|--------|
| $(2, 3)$ | $\mathfrak{n}$-$\mathfrak{n}$ | nn | $T_{nn}$ |

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

| Crossing | Parent type | Matrix |
|----------|------------|--------|
| $(0, 1)$ | $\mathfrak{p}$-$\mathfrak{n}$ = mix | $T_{\mathrm{mix}}$ |
| $(0, 2)$ | $\mathfrak{p}$-$\mathfrak{n}$ = mix | $T_{\mathrm{mix}}$ |

$M_0^{\mathrm{par}} = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}}$

**Generator $\sigma_1$** (crossing with nucleon 2):

| Crossing | Parent type | Matrix |
|----------|------------|--------|
| $(1, 2)$ | $\mathfrak{n}$-$\mathfrak{n}$ = nn | $T_{nn}$ |

$M_1^{\mathrm{par}} = T_{nn}$

### Daughter (${}^3\mathrm{He}$)

**Generator $\sigma_0$:**

| Crossing | Daughter type | Matrix |
|----------|-------------|--------|
| $(0, 1)$ | $\mathfrak{p}$-$\mathfrak{p}$ = pp | $T_{pp}$ |
| $(0, 2)$ | $\mathfrak{p}$-$\mathfrak{n}$ = mix | $T_{\mathrm{mix}}$ |

$M_0^{\mathrm{dau}} = T_{pp} \cdot T_{\mathrm{mix}}$

**Generator $\sigma_1$:**

| Crossing | Daughter type | Matrix |
|----------|-------------|--------|
| $(1, 2)$ | $\mathfrak{p}$-$\mathfrak{n}$ = mix | $T_{\mathrm{mix}}$ |

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

| Nucleus | $A$ | $Z$ | $N$ | Generators | $\binom{A}{2}$ multiplications | $\deg P \leq$ |
|---------|-----|-----|-----|:----------:|:------------------------------:|:-------------:|
| ${}^1\mathrm{H}$ | $1$ | $1$ | $0$ | $0$ | $0$ | — |
| ${}^2\mathrm{H}$ | $2$ | $1$ | $1$ | $1$ | $1$ | $3$ |
| ${}^3\mathrm{H}$, ${}^3\mathrm{He}$ | $3$ | — | — | $2$ | $3$ | $8$ |
| ${}^4\mathrm{He}$ | $4$ | $2$ | $2$ | $3$ | $6$ | $15$ |
| ${}^{12}\mathrm{C}$ | $12$ | $6$ | $6$ | $11$ | $66$ | $143$ |
| ${}^{14}\mathrm{C}$ | $14$ | $6$ | $8$ | $13$ | $91$ | $195$ |
| ${}^{56}\mathrm{Fe}$ | $56$ | $26$ | $30$ | $55$ | $1540$ | $3135$ |
| ${}^{210}\mathrm{Bi}$ | $210$ | $83$ | $127$ | $209$ | $21945$ | $44099$ |

All computable in milliseconds on modern hardware.
