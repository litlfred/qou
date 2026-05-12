This section lists **every** transfer matrix for each knot pair,
including trivial and degenerate cases.  All matrices are
$2 \times 2$ over $\mathbb{Z}[q^{\pm 1/2}]$.

Write $H_A = q - q^{-1}$ for the Hecke amplitude.

---

## 1. Trivial transfer matrices

### 1a. Unknot--unknot (vacuum--vacuum)

Knots: $K_1 = T_{1,0}$, $K_2 = T_{1,0}$.

Jones polynomials: $J_{T_{1,0}}(q) = 1$, $J_{T_{1,0} \# T_{1,0}}(q) = 1$.

Crossing coefficients: $c = 1$, $d = 0$.

$$
  \boxed{
    T_{\nu\nu}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

**This is the simplest non-identity transfer matrix.**
Even "empty" crossings (two unknotted strands) produce a
non-trivial Hecke reduction.

### 1b. Identity (no crossing)

When two strands do not cross at generator $\sigma_i$,
the transfer matrix is the $2 \times 2$ identity:

$$
  \boxed{
    T_{\varnothing}(q) = 
    \begin{pmatrix}
      1 & 0 \\
      0 & 1
    \end{pmatrix}
    =  \mathbb{I}
  }
$$

This is the $c = 0, d = 1$ case: the strand contributes
nothing to the Hecke chain at that generator.

---

## 2. Nuclear transfer matrices (proton--neutron pairs)

These are the three matrices governing all nuclear
interactions.  Every nuclear Skein polynomial is a product
of these.

### 2a. Proton--proton ($\mathfrak{p}$-$\mathfrak{p}$)

Knots: $K_1 = T_{2,3}$ (up quark), $K_2 = T_{2,3}$ (up quark).

Crossing coefficients: $c = 1$, $d = 0$.

$$
  \boxed{
    T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

**Explicit entries:**

| Entry | Formula |
|:-----:|---------|
| $(1,1)$ | $q - q^{-1}$ |
| $(1,2)$ | $1$ |
| $(2,1)$ | $1$ |
| $(2,2)$ | $0$ |
| $\det$ | $-1$ |
| $\mathrm{tr}$ | $q - q^{-1}$ |

**Eigenvalues:**

$$
  \lambda_{\pm} =  \frac{(q - q^{-1}) \pm \sqrt{(q-q^{-1})^2 + 4}}{2}
$$

Note: $\lambda_+ \cdot \lambda_- = -1$ (determinant), $\lambda_+ + \lambda_- = q - q^{-1}$ (trace).

### 2b. Neutron--neutron ($\mathfrak{n}$-$\mathfrak{n}$)

Knots: $K_1 = T_{2,3}^{\sigma}$ (down quark), $K_2 = T_{2,3}^{\sigma}$ (down quark).

Crossing coefficients: $c = 1$, $d = -(q - q^{-1})$.

$$
  \boxed{
    T_{nn}(q) = 
    \begin{pmatrix}
      0 & 1 \\
      1 & -(q - q^{-1})
    \end{pmatrix}
  }
$$

**Explicit entries:**

| Entry | Formula |
|:-----:|---------|
| $(1,1)$ | $0$ |
| $(1,2)$ | $1$ |
| $(2,1)$ | $1$ |
| $(2,2)$ | $-(q - q^{-1})$ |
| $\det$ | $-1$ |
| $\mathrm{tr}$ | $-(q - q^{-1})$ |

**Relation to $T_{pp}$:**

$$
  T_{nn}(q) =  T_{pp}(q) -  (q - q^{-1}) \cdot \mathbb{I}
$$

### 2c. Mixed ($\mathfrak{p}$-$\mathfrak{n}$, proton--neutron)

Knots: $K_1 = T_{2,3}$ (up quark), $K_2 = T_{2,3}^{\sigma}$ (down quark).

Crossing coefficients: $c = 1$, $d = -\dfrac{q - q^{-1}}{2}$.

$$
  \boxed{
    T_{\mathrm{mix}}(q) = 
    \begin{pmatrix}
      \dfrac{q - q^{-1}}{2}
        & 1 \\[6pt]
      1 & -\dfrac{q - q^{-1}}{2}
    \end{pmatrix}
  }
$$

**Explicit entries:**

| Entry | Formula |
|:-----:|---------|
| $(1,1)$ | $\dfrac{q - q^{-1}}{2}$ |
| $(1,2)$ | $1$ |
| $(2,1)$ | $1$ |
| $(2,2)$ | $-\dfrac{q - q^{-1}}{2}$ |
| $\mathrm{tr}$ | $0$ |

**Midpoint property:**

$$
  T_{\mathrm{mix}}(q) =  \tfrac{1}{2}\bigl(T_{pp}(q) + T_{nn}(q)\bigr)
$$

This midpoint property is the reason beta decay has a
universal matrix (the step from $T_{nn}$ to $T_{\mathrm{mix}}$
equals the step from $T_{\mathrm{mix}}$ to $T_{pp}$).

---

## 3. Electromagnetic transfer matrices

### 3a. Photon--electron ($\gamma$-$e$)

Knots: $K_1 = \varnothing$ (empty knot / photon), $K_2 = T_{2,3}$ (trefoil / electron).

Since $J_{\varnothing}(q) = 1$: $c = 1$, $d = 0$.

$$
  \boxed{
    T_{\gamma e}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

The photon (empty knot, $J = 1$) contributes no deformation.
The crossing is entirely determined by the electron.

### 3b. Electron--electron ($e$-$e$)

Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,3}$.

Same as proton--proton (both are trefoils):

$$
  \boxed{
    T_{ee}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

### 3c. Photon--photon ($\gamma$-$\gamma$)

Knots: $K_1 = T_{1,0}$, $K_2 = T_{1,0}$.

Same as unknot--unknot:

$$
  \boxed{
    T_{\gamma\gamma}(q) =  T_{\nu\nu}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

### 3d. Photon--positron ($\gamma$-$e^+$)

Knots: $K_1 = T_{1,0}$, $K_2 = T_{2,3}^{\sigma}$.

Since $J_{T_{1,0}}(q) = 1$: $c = 1$, $d = 0$.

$$
  \boxed{
    T_{\gamma e^+}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

The unknot is invisible to the transfer matrix regardless
of the partner's chirality.

### 3e. Electron--positron ($e^-$-$e^+$)

Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,3}^{\sigma}$.

Same as mixed nuclear crossing (trefoil meets mirror trefoil):

$$
  \boxed{
    T_{e^-e^+}(q) =  T_{\mathrm{mix}}(q) = 
    \begin{pmatrix}
      \dfrac{q - q^{-1}}{2}
        & 1 \\[6pt]
      1 & -\dfrac{q - q^{-1}}{2}
    \end{pmatrix}
  }
$$

---

## 4. Higher-generation transfer matrices

### 4a. Unknot--trefoil (general: any partner with unknot)

For any knot $K$ paired with the unknot $T_{1,0}$, the
connected sum $T_{1,0} \# K = K$ gives $c = 1$ via
$J_{T_{1,0} \# K} = J_{T_{1,0}} \cdot J_K = J_K$.

In the nuclear context (Hecke product), the unknot
likewise contributes $c = 1$, $d = 0$ because
$J_{T_{1,0}}(q) = 1$ makes the unknot strand
act as the identity on the Hecke chain.  Therefore:

$$
  \boxed{
    T_{T_{1,0}, K}(q) =  T_{pp}(q)
    \quad\text{for every knot } K
  }
$$

**The unknot is universally invisible.**

### 4b. Cinquefoil--cinquefoil ($\mathfrak{b}$-$\mathfrak{b}$)

Knots: $K_1 = T_{2,5}$, $K_2 = T_{2,5}$.

Crossing coefficients: $c = 1$ (same chirality), $d = 0$.

$$
  \boxed{
    T_{\mathfrak{b}\mathfrak{b}}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

**All same-chirality identical-knot pairs give $T_{pp}$.**

### 4c. Trefoil--cinquefoil ($\mathfrak{u}$-$\mathfrak{b}$)

Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,5}$.

Same-chirality pair interacting via connected sum:
$J_{T_{2,3} \# T_{2,5}} = J_{T_{2,3}} \cdot J_{T_{2,5}}$,
so $c = 1$, $d = 0$.

$$
  \boxed{
    T_{\mathfrak{u}\mathfrak{b}}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

### 4d. $T_{3,4}$--$T_{3,4}$ (Hopf${}^2$--Hopf${}^2$, color binding)

Knots: $K_1 = T_{3,4}$, $K_2 = T_{3,4}$.

Same chirality, same knot: $c = 1$, $d = 0$.

$$
  \boxed{
    T_{\mathfrak{t}\mathfrak{t}}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

### 4e. Knot--mirror knot (any $K$ with $K^{\sigma}$)

For a knot $K$ paired with its mirror $K^{\sigma}$ via
**connected sum**, $J_{K \# K^{\sigma}} = J_K \cdot J_{K^{\sigma}}$
gives $c = 1$, $d = 0$, so $T_{K,K^{\sigma}} = T_{pp}$.

However, for **nucleon crossings** (the physically relevant
case), the composition is via the Hecke product, not the
connected sum.  The Hecke product yields the non-trivial
nuclear coefficients $(c, d) \neq (1, 0)$ listed in Section 2
— this is precisely the origin of the distinct $T_{nn}$ and
$T_{\mathrm{mix}}$ matrices.

---

## 5. Summary: classification of all transfer matrices

Every transfer matrix in the paper falls into one of three
classes:

| Class | $c$ | $d$ | Matrix | Occurs when |
|-------|-----|-----|--------|-------------|
| **Type I** (fundamental) | $1$ | $0$ | $T_{pp}$ | Same-chirality pair, or unknot with anything |
| **Type II** (heavy) | $1$ | $-(q - q^{-1})$ | $T_{nn}$ | Mirror-chirality pair (down--down type) |
| **Type III** (mixed) | $1$ | $-\frac{q - q^{-1}}{2}$ | $T_{\mathrm{mix}}$ | Cross-chirality pair (up--down type) |

The identity matrix $\mathbb{I}$ (no crossing) is the
degenerate $c = 0$, $d = 1$ case.

**Key identities:**

$$
  T_{\mathrm{mix}} = \tfrac{1}{2}(T_{pp} + T_{nn})
$$

$$
  T_{nn} = T_{pp} - (q - q^{-1})  \mathbb{I}
$$

$$
  T_{\gamma e} = T_{ee} = T_{\gamma\gamma} = T_{\nu\nu}
  = T_{\mathfrak{b}\mathfrak{b}} = T_{\mathfrak{t}\mathfrak{t}} = T_{pp}
$$
