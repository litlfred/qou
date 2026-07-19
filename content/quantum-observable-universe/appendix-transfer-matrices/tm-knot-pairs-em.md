## 3. Electromagnetic transfer matrices

**3a. Photon--electron ($\gamma$-$e$)**
Knots: $K_1 = \varnothing$ (photon), $K_2 = T_{2,3}$ (electron).
Since $J_{\varnothing}(q) = 1$: $c = 1$, $d = 0$.

$$
  T_{\gamma e}(q) = T_{pp}(q) = \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
$$

The photon contributes no deformation.

**3b. Electron--electron ($e$-$e$)**
Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,3}$.

$$
  T_{ee}(q) = T_{pp}(q) = \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
$$

**3c. Photon--photon ($\gamma$-$\gamma$)**
Knots: $K_1 = \varnothing$, $K_2 = \varnothing$.

$$
  T_{\gamma\gamma}(q) = T_{\nu\nu}(q) = \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
$$

**3d. Photon--positron ($\gamma$-$e^+$)**
Knots: $K_1 = \varnothing$, $K_2 = T_{2,3}^{\sigma}$.

$$
  T_{\gamma e^+}(q) = T_{pp}(q) = \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
$$

**3e. Electron--positron ($e^-$-$e^+$)**
Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,3}^{\sigma}$.

$$
  T_{e^-e^+}(q) = T_{\mathrm{mix}}(q) = \begin{pmatrix} \frac{q - q^{-1}}{2} & 1 \\ 1 & -\frac{q - q^{-1}}{2} \end{pmatrix}
$$

## 4. Higher-generation transfer matrices

**4a. Unknot--trefoil (general: any partner with unknot)**
For any knot $K$ paired with the unknot $T_{1,0}$, the connected sum gives $c = 1$. In the nuclear context, the unknot contributes $c = 1, d = 0$. Therefore $T_{T_{1,0}, K}(q) = T_{pp}(q)$ for every knot $K$. The unknot is universally invisible. The same applies to the photon.

**4b. Cinquefoil--cinquefoil ($\mathfrak{b}$-$\mathfrak{b}$)**
Knots: $K_1 = T_{2,5}$, $K_2 = T_{2,5}$.
$c = 1, d = 0$. Thus $T_{\mathfrak{b}\mathfrak{b}}(q) = T_{pp}(q)$. All same-chirality identical-knot pairs give $T_{pp}$.

**4c. Trefoil--cinquefoil ($\mathfrak{u}$-$\mathfrak{b}$)**
Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,5}$.
$c = 1, d = 0$. Thus $T_{\mathfrak{u}\mathfrak{b}}(q) = T_{pp}(q)$.

**4d. $T_{3,4}$--$T_{3,4}$ (Hopf${}^2$--Hopf${}^2$, color binding)**
Knots: $K_1 = T_{3,4}$, $K_2 = T_{3,4}$.
$c = 1, d = 0$. Thus $T_{\mathfrak{t}\mathfrak{t}}(q) = T_{pp}(q)$.

**4e. Knot--mirror knot (any $K$ with $K^{\sigma}$)**
Via connected sum, $T_{K,K^{\sigma}} = T_{pp}$. But for nucleon crossings (via Hecke product), non-trivial coefficients arise. This distinguishes $T_{nn}$ and $T_{\mathrm{mix}}$.

## 5. Summary: classification of all transfer matrices

Every transfer matrix falls into one of three classes. See [Table 4](#tbl:tm-knot-pairs-table4-data). The identity matrix $\mathbb{I}$ is the degenerate $c = 0$, $d = 1$ case. Key identities: $T_{\mathrm{mix}} = \frac{1}{2}(T_{pp} + T_{nn})$, $T_{nn} = T_{pp} - (q - q^{-1}) \mathbb{I}$, and $T_{\gamma e} = T_{ee} = T_{\gamma\gamma} = T_{\nu\nu} = T_{\mathfrak{b}\mathfrak{b}} = T_{\mathfrak{t}\mathfrak{t}} = T_{pp}$.
