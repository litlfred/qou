<!-- FILE_START: tm-knot-pairs-intro.md -->
Every interaction in this framework is a crossing between two
knotted strands, and the knot polynomial that records such a
crossing is an unbounded object whose degree grows with the
complexity of the knots involved. A transfer matrix trades that
unbounded data for a fixed-size operator: to each pair of knots one
assigns a single $2 \times 2$ matrix over $\mathbb{Z}[q^{\pm 1/2}]$,
compressing the polynomial content of the interaction into four
Laurent-polynomial entries obtained from the Hecke reduction of the
crossing. The payoff is composition — because every crossing now
carries a matrix of the same shape, a chain of crossings becomes an
ordinary matrix product, and interactions of very different physical
character can be multiplied, compared, and iterated on equal footing.
This is what makes the Hecke reduction the right tool: it collapses
the full knot-polynomial data of a crossing to a uniform operator
without discarding the information a matrix product needs.

The smallest case makes the compression visible. Two unknotted
strands — the vacuum--vacuum pair — carry no knotting at all, yet
their crossing does not reduce to the identity: the Hecke relation
still fires, and the pair is assigned the simplest non-identity
transfer matrix in the catalogue. That a genuinely empty
configuration already produces a non-trivial matrix is the sign that
the transfer matrix records the crossing itself, not merely the
knots being crossed.

This section builds the catalogue crossing type by crossing type. It
begins with the trivial matrices — unknot pairs and the identity —
passes to the nuclear proton--neutron matrices that govern every
nucleon interaction, then to the electromagnetic matrices for
photons, electrons, and positrons, and on to the higher-generation
pairs; it closes by sorting the entire list into a short
classification, so that the many named matrices collapse to a handful
of distinct forms.
<!-- FILE_END: tm-knot-pairs-intro.md -->

<!-- FILE_START: tm-knot-pairs.md -->
A transfer matrix records how a single crossing between two knotted
strands acts on the Hecke chain; each knot pair contributes a
$2 \times 2$ block determined by its crossing coefficients $c$ and
$d$.  The catalogue matters because every nuclear and electromagnetic
crossing in the paper reduces to one of just three classes
(Section 5), so the long list below — trivial and degenerate cases
included — is exhaustive rather than diverse.

This section lists **every** transfer matrix for each knot pair.  All
matrices are $2 \times 2$ over $\mathbb{Z}[q^{\pm 1/2}]$.

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

See [Table 1](#tbl:tm-knot-pairs-table1-data).

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

See [Table 2](#tbl:tm-knot-pairs-table2-data).

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

See [Table 3](#tbl:tm-knot-pairs-table3-data).

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

Knots: $K_1 = \varnothing$, $K_2 = \varnothing$ (two empty knots / photons).

Same as unknot--unknot (both have $J = 1$):

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

Knots: $K_1 = \varnothing$, $K_2 = T_{2,3}^{\sigma}$.

Since $J_{\varnothing}(q) = 1$: $c = 1$, $d = 0$.

$$
  \boxed{
    T_{\gamma e^+}(q) =  T_{pp}(q) = 
    \begin{pmatrix}
      q - q^{-1} & 1 \\
      1 & 0
    \end{pmatrix}
  }
$$

The empty knot (photon) is invisible to the transfer matrix
regardless of the partner's chirality — exactly as for the
unknot (neutrino), since both satisfy $J = 1$.

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

**The unknot is universally invisible.**  The same applies to
the photon (empty knot $\varnothing$, $J_{\varnothing} = 1$),
which acts as the identity on the Hecke chain for every
partner $K$.

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

See [Table 4](#tbl:tm-knot-pairs-table4-data).

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
<!-- FILE_END: tm-knot-pairs.md -->

