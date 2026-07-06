The canonical trace decomposes as a sum of generator volumes, one for each braid generator $\sigma_i$ in $B_A$. A transfer matrix product computes each generator's volume. These terms organize as a jet expansion in the nucleon count. Each jet order corresponds to a color degree.

**Proposition.**
Let $\mathcal{N}(Z, N)$ be the nuclear braid word in $H_A(q)$ ([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)). At each generator $\sigma_i$ ($i = 0, \ldots, A-2$), nucleon $i$ crosses with nucleons $j = i+1, \ldots, A-1$. These $k_i = A - i - 1$ crossings act on $\sigma_i$ and reduce via the Hecke relation to a linear combination:

$$
  \prod_{j=i+1}^{A-1} C_{ij}(\sigma_i)
  = 
  a_i  \sigma_i + b_i
$$

where each crossing factor $C_{ij}(\sigma_i) = c_j \sigma_i + d_j$ has coefficients determined by the pair type:

$$
  (c_j, d_j) = 
  \begin{cases}
    (1, 0) & \text{if } i, j \text{ both protons (}\sigma\text{)} \\[3pt]
    (1, -(q - q^{-1})) & \text{if } i, j \text{ both neutrons (}\sigma^{-1}\text{)} \\[3pt]
    (1, -\tfrac{1}{2}(q - q^{-1}))
      & \text{if mixed (}\tfrac{1}{2}(\sigma + \sigma^{-1})\text{)}
  \end{cases}
$$

The coefficients $(a_i, b_i)$ satisfy a recurrence. We start from $(a_0, b_0) = (0, 1)$ (the identity), multiply $(a_k \sigma + b_k)(c_j \sigma + d_j)$, and apply $T^2 = (q - q^{-1})T + 1$:

$$
  a_{k+1} = a_k c_j (q - q^{-1}) + a_k d_j + b_k c_j,
  \qquad
  b_{k+1} = a_k c_j + b_k d_j.
$$

This defines a $2 \times 2$ transfer matrix $T_j$ at each crossing.

## Jet expansion in the nucleon count

The transfer matrix product at generator $\sigma_i$:

$$
  M_i =  \prod_{j=i+1}^{A-1} T_j
$$

is a product of $k_i = A - i - 1$ matrices. This product admits a jet expansion. This is a Taylor series in the number of crossings, where each order corresponds to a color degree:

$$
  M_i =  \mathbb{1}
  +  \underbrace{\sum_{j} T_j^{(1)}}_{\text{1-jet: pair interactions}}
  +  \underbrace{\sum_{j < k} T_j^{(1)} T_k^{(1)}}_{\text{2-jet: triple correlations}}
  +  \cdots
  +  \underbrace{\prod_{j} T_j^{(1)}}_{\text{$k_i$-jet: full product}}
$$

where $T_j = \mathbb{1} + T_j^{(1)}$, with $T_j^{(1)}$ measuring the deviation from the identity.

The color degree at generator $\sigma_i$ equals $k_i = A - i - 1$.

| Jet order $r$ | Color degree | Physical content | Multiplicity |
|:---:|:---:|---|:---:|
| $0$ | $0$ | Free nucleon (identity) | $1$ |
| $1$ | $1$ | Pair interactions ($i$-$j$ crossings) | $k_i$ |
| $2$ | $2$ | Triple correlations ($i$-$j$-$k$) | $\binom{k_i}{2}$ |
| $r$ | $r$ | $(r+1)$-body correlations | $\binom{k_i}{r}$ |
| $k_i$ | $k_i$ | Full product (exact) | $1$ |

The total number of terms across all jets and all generators is:

$$
  \sum_{i=0}^{A-2} \sum_{r=0}^{k_i} \binom{k_i}{r}
  = 
  \sum_{i=0}^{A-2} 2^{k_i}
$$

This sum scales exponentially. However, the transfer matrix product computes the algebraic trace in exactly $k_i$ steps (one per crossing). The total step count across all generators is:

$$
  \sum_{i=0}^{A-2} k_i
  = 
  \sum_{i=0}^{A-2} (A - i - 1)
  = 
  \frac{A(A-1)}{2}
  = 
  \binom{A}{2}
$$

The transfer matrix product requires exactly $\binom{A}{2}$ algebraic steps. This matches the number of nucleon pairs.

## Beta decay as the 1-jet variation

Single beta decay ($\beta^{\pm}$) changes one nucleon type. The trace variation $\delta E$ represents the first jet (first variation) of the volume functional in the nucleon-type variable $\tau_p \in \{\mathfrak{p}, \mathfrak{n}\}$:

$$
  \delta E =  \sum_{i=0}^{p} (V_i^{\mathrm{dau}} - V_i^{\mathrm{par}})
$$

We sum only over generators affected by the converting nucleon at position $p$. Generators $i > p$ remain unaffected and cancel exactly. This yields the 1-jet of $E$ in the fibre direction: a single crossing change at one nucleon.

## Double beta decay as the 2-jet variation

Double beta decay ($2\beta$) changes two nucleons simultaneously. If nucleons at positions $p_1$ and $p_2$ (with $p_1 < p_2$) both convert $\mathfrak{n} \to \mathfrak{p}$, the trace variation includes a cross-term:

$$
  \delta^2 E
  = 
  \underbrace{\delta E_{p_1} + \delta E_{p_2}}_{\text{sum of single variations}}
  + 
  \underbrace{\Delta_{p_1 p_2}}_{\text{2-jet cross-term}}
$$

The cross-term $\Delta_{p_1 p_2}$ arises because at generators $\sigma_i$ with $i \leq p_1$, both converting nucleons' crossings change. The transfer matrix at these generators encounters two modified crossing factors. The product $T_{p_1}^{(1)} T_{p_2}^{(1)}$ contributes a new term that cannot be reduced to the sum of individual variations.

For generator $\sigma_i$ with $i \leq p_1$, the transfer matrix product changes at positions $j = p_1$ and $j = p_2$. We write $T_j = T_j^{(\mathrm{par})} + \delta T_j$:

$$
  M_i^{(2\beta)}
  = 
  M_i^{(\mathrm{par})}
  + 
  \underbrace{\delta T_{p_1} \cdot (\text{rest})
    + (\text{rest}) \cdot \delta T_{p_2}}_{\text{1-jet terms (linear)}}
  + 
  \underbrace{\delta T_{p_1} \cdot (\text{between}) \cdot \delta T_{p_2}}_{\text{2-jet cross-term}}
$$

The 2-jet cross-term encodes the correlation between the two converting nucleons. All nucleons between positions $p_1$ and $p_2$ mediate this correlation. This term provides the nuclear matrix element $M^{(2\nu)}$ of double beta decay.

For neutrinoless double beta decay ($0\nu\beta\beta$), the 2-jet cross-term adopts a different structure. The two $L_0^{-}$ smoothings remain coupled. The two emitted electrons share a single neutrino propagator. In the braid framework, this corresponds to a single unknot $T_{1,0}$ threading both crossing changes.

## The jet bundle structure

The generator volumes $\{V_i\}_{i=0}^{A-2}$ form a section of a jet bundle over the nuclear configuration space. The base is the space of nucleon-type assignments $\tau : \{0, \ldots, A-1\} \to \{\mathfrak{p}, \mathfrak{n}\}$. The fibre at each assignment is the vector of generator volumes $(V_0, \ldots, V_{A-2})$.

| Object | Jet bundle interpretation |
|--------|-------------------------|
| Nucleon-type assignment $\tau$ | Point in the base |
| Generator volumes $(V_0, \ldots, V_{A-2})$ | Section of the fibre |
| Single beta decay $\delta\tau_{p}$ | 1-jet (first derivative) |
| Double beta decay $\delta\tau_{p_1} \delta\tau_{p_2}$ | 2-jet (second derivative) |
| $r$-fold decay | $r$-jet ($r$-th derivative) |
| Full transfer matrix product | $\infty$-jet (exact) |

The color degree of the $r$-jet at generator $\sigma_i$ equals $\min(r, k_i)$. The number of crossings at that generator bounds this degree.

## Generator volume profile

The Markov-traced volume at generator $\sigma_i$ is:

$$
  \hat{V}_i =  z \cdot a_i + b_i
$$

where $z = 1/(q^{1/2} + q^{-1/2})$ provides the Markov parameter.
The canonical trace decomposes as:

$$
  \tfrac{1}{2}\ln\bigl(\mathrm{tr}(\mathcal{N}) \cdot \overline{\mathrm{tr}(\mathcal{N})}\bigr) =
  \tfrac{1}{2}\sum_{i=0}^{A-2} \ln\bigl(\hat{V}_i \cdot \overline{\hat{V}_i}\bigr)
$$

Exactly $k_i$ transfer matrix steps determine each term $\tfrac{1}{2}\ln(\hat{V}_i \cdot \overline{\hat{V}_i})$.

## The volume of the ideal

The Gröbner--Shirshov ideal $I$ at generator $\sigma_i$ absorbs the difference between the unreduced weight and the reduced weight. The ideal volume at generator $i$ is:

$$
  V_i^I =  k_i - V_i
$$

where $k_i = A - i - 1$ counts the number of crossings. This represents the trace contribution removed by the Hecke relation (the resolved crossings). The total ideal volume $V^I = \sum_i V_i^I = \binom{A}{2} - E$ measures the portion of the naive crossing count absorbed by double-crossing resolutions.

## Connection to the Reeb decomposition

The color degree at each generator corresponds to the vertical degree $\deg\alpha_V$ of the Reeb flow:

- Generator $\sigma_0$: color degree $A - 1$ (sees all other nucleons). This forms the lowest Reeb stratum.
- Generator $\sigma_{A-2}$: color degree $1$ (sees one nucleon). This forms the highest Reeb stratum.

The jet expansion at each generator gives the Taylor series of the transfer matrix product along the Reeb flow direction. Each additional crossing adds one color degree. This corresponds to one more nucleon entering the interaction region.

The generator volume decomposition provides the discrete analogue of the jet bundle of the canonical action $\mathfrak{S}_q$ over the nuclear configuration space. The 1-jet captures single beta decay changes. The 2-jet captures double beta decay changes. The full $\infty$-jet recovers the exact algebraic trace. The same $\binom{A}{2}$ transfer matrix steps compute all of these.
