The [transfer matrix](#def:transfer-matrix-operator)
$T_{K_1, K_2}(q)$ acts on the Gröbner--Shirshov-reduced Hecke chain,
generates a non-commutative operator algebra under composition, and
catalogues every particle interaction together with its $\Delta$
operator and composition rules.

## Action on the Gröbner--Shirshov ideal

The transfer matrix acts on the Iwahori--Hecke algebra element
$a\sigma_i + b$ (the Gröbner--Shirshov-reduced chain at generator
$\sigma_i$) by left multiplication followed by Hecke reduction:

$$
  T_{K_1, K_2}  \cdot  (a\sigma + b)
   := 
  (c\sigma + d)(a\sigma + b)
  \stackrel{T^2 = (q-q^{-1})T + 1}{\longrightarrow}
  a'\sigma + b'
$$

where:

$$
  a' = ac(q - q^{-1}) + ad + bc,
  \qquad
  b' = ac + bd.
$$

In matrix form:

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix}
  = 
  T_{K_1, K_2}(q)
   \cdot 
  \begin{pmatrix} a \\ b \end{pmatrix}
$$

The product of $k$ transfer matrices at generator $\sigma_i$
gives the full chain reduction $M_i = \prod_{j} T_j(q)$, and
the Markov-traced volume is $\hat{V}_i = z \cdot (M_i)_{11} + (M_i)_{21}$.

## The operator algebra

Transfer matrices compose: if strands $K_1$, $K_2$, $K_3$
cross in sequence at generator $\sigma_i$, the combined
operator is:

$$
  T_{K_1 K_3} \circ T_{K_1 K_2}
  = 
  T_{K_1, K_3}(q) \cdot T_{K_1, K_2}(q)
$$

(matrix multiplication).  This is **non-commutative** — the
order of crossings matters.

**The Gröbner--Shirshov ideal is the kernel:**

$$
  I_i =  \ker\!\left(
    \prod_{j} T_j(q) - M_i(q)
  \right)
$$

The ideal $I_i$ at generator $\sigma_i$ absorbs the terms
eliminated by the Hecke relation ($T^2 = (q - q^{-1})T + 1$).
The transfer matrix product $M_i(q)$ is the **quotient** — the
element surviving after modding out $I_i$.

## Interaction catalogue

Every particle interaction corresponds to a transfer matrix.
The **interaction type** is determined by the knot types of
the two strands at the crossing:

### Nuclear interactions (quark-level, Level 1)

Each quark is an unknot strand of $\mathcal{B}_3$ ([up quark](#def:up-quark)); the strands are distinguished by crossing orientation, not knot type.

| Interaction | $K_1$ | $K_2$ | $T(q)$ | Physical |
|-------------|-------|-------|--------|----------|
| $\mathfrak{u}\mathfrak{u}$ | unknot, $\sigma_i$ | unknot, $\sigma_i$ | $T_{pp}$ | proton-proton repulsion |
| $\mathfrak{d}\mathfrak{d}$ | unknot, $\sigma_i^{-1}$ | unknot, $\sigma_i^{-1}$ | $T_{nn}$ | neutron-neutron |
| $\mathfrak{u}\mathfrak{d}$ | unknot, $\sigma_i$ | unknot, $\sigma_i^{-1}$ | $T_{\mathrm{mix}}$ | proton-neutron binding |

### Electromagnetic interactions (electron-level)

| Interaction | $K_1$ | $K_2$ | Physical |
|-------------|-------|-------|----------|
| $e$-$\mathfrak{p}$ | $T_{2,3}$ | $\mathcal{B}_3$ | Electron-nucleus Coulomb |
| $e$-$e$ | $T_{2,3}$ | $T_{2,3}$ | Electron-electron repulsion |
| $\gamma$-$e$ | $\varnothing$ | $T_{2,3}$ | Photon absorption/emission |

### Photon-electron transfer matrix

The photon ($\varnothing$, empty knot) crossing with the electron
($T_{2,3}$, trefoil) gives:

$$
  T_{\gamma e}(q)
  = 
  T_{\varnothing, T_{2,3}}(q)
$$

Since the empty knot has $J_{\varnothing}(q) = 1$:
$c_{\gamma e} = J_{T_{2,3}}(q) / J_{T_{2,3}}(q) = 1$ and
$d_{\gamma e} = 0$.  Therefore:

$$
  T_{\gamma e}(q) =  T_{pp}(q)
  = 
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix}
$$

**The photon-electron transfer matrix is the same as the
proton-proton matrix.**  This is because $J_{\varnothing}(q) = 1$
(trivial Jones polynomial of the empty knot), so the photon
contributes no deformation — the crossing is purely determined
by the electron.

### Shell transitions as R-I moves

Photon absorption promotes an electron from shell $n$ to
shell $n+1$.  In the transfer matrix language, this is a
**Reidemeister I move** on the electron-nucleus Hopf link:
a curl is added to the electron trefoil, changing its writhe
by $\pm 1$ but preserving its knot type.

The R-I move at the electron-nucleus junction:

$$
  \sigma_i \mapsto \sigma_i \cdot \sigma_n
$$

adds one transfer matrix factor $T_{\gamma e}$ to the chain
at generator $\sigma_i$.  The energy change is:

$$
  \Delta E_n
  = 
  \hat{V}_i^{(n+1)} - \hat{V}_i^{(n)}
  = 
  z \cdot (T_{\gamma e} \cdot M_i^{(n)})_{11}
  + (T_{\gamma e} \cdot M_i^{(n)})_{21}
  - \hat{V}_i^{(n)}
$$

For hydrogen ($A = 1$, single electron-proton junction):
the transfer matrix at shell $n$ is $T_{\gamma e}^n$ (the
$n$-th power).  The energy:

$$
  E_n  \propto  \hat{V}(T_{\gamma e}^n)
  = 
  z \cdot (T_{\gamma e}^n)_{11} + (T_{\gamma e}^n)_{21}
$$

Since $T_{\gamma e}$ has eigenvalues
$\lambda_{\pm} = \frac{1}{2}\bigl[(q - q^{-1}) \pm \sqrt{(q - q^{-1})^2 + 4}\bigr]$, the $n$-th power grows as
$\lambda_+^n$, and the energy scales as:

$$
  E_n  \propto  \lambda_+^n
$$

The **energy difference** between shells:

$$
  \Delta E_{n \to n+1}
  = 
  \hat{V}(T_{\gamma e}^{n+1}) - \hat{V}(T_{\gamma e}^n)
  = 
  \hat{V}(T_{\gamma e}^n) \cdot (\lambda_+ - 1)
$$

This gives the photon energy for shell transitions — a
geometric series in the eigenvalue $\lambda_+$ of the
photon-electron transfer matrix.

## Interaction as Δ operator

Any interaction that changes the crossing type from
$(K_1, K_2) \to (K_1', K_2')$ is encoded by the
**interaction operator**:

$$
  \Delta_{K_1 K_2 \to K_1' K_2'}(q)
  = 
  T_{K_1', K_2'}(q) - T_{K_1, K_2}(q)
$$

This is a 2$\times$2 matrix with polynomial entries in $q$.

| Interaction | $\Delta$ operator | Physical process |
|-------------|-------------------|------------------|
| $\beta^-$ decay | $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$ | $\mathfrak{d} \to \mathfrak{u}$ crossing change |
| $\beta^+$ decay | $-\Delta_\beta = T_{\mathrm{mix}} - T_{pp}$ | $\mathfrak{u} \to \mathfrak{d}$ crossing change |
| Photon absorption | $\Delta_\gamma = T_{\gamma e}$ (appended) | R-I move adds crossing |
| Pair creation | $\Delta_{\mathrm{pair}} = T_{ee} - T_{\gamma\gamma}$ | $\gamma \to e^+ e^-$ |

For beta decay, $\Delta_\beta$ is **universal**
([beta decay matrix](#prop:beta-decay-transfer-matrix)):
the same matrix for every nucleus.

For photon absorption, the operator is not a difference but
an **extension**: a new transfer matrix factor $T_{\gamma e}$
is appended to the chain, increasing the color degree by $1$.

## Composition rules

**Sequential interactions** (two interactions in sequence at
the same generator):

$$
  \Delta_{\mathrm{total}} = \Delta_2 \cdot T_{\mathrm{between}} \cdot \Delta_1
  + \Delta_1 + \Delta_2
$$

**Parallel interactions** (interactions at different generators):

$$
  \frac{P_{\mathrm{final}}}{P_{\mathrm{initial}}}
  = 
  \prod_{i \in \mathrm{affected}} \frac{\hat{V}_i^{\mathrm{final}}}{\hat{V}_i^{\mathrm{initial}}}
$$

The generators factorize — each affected generator contributes
independently to the Skein polynomial ratio.
