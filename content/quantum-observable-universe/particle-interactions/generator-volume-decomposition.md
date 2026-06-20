*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The nuclear binding energy decomposes as a **sum of generator
volumes** — one for each braid generator $\sigma_i$ in $B_A$.
Each generator's volume is computed by a transfer matrix product
whose terms organize as a **jet expansion in the nucleon count**,
with each jet order corresponding to a color degree.

**Proposition.**
Let $\mathcal{N}(Z, N)$ be the nuclear braid word in $H_A(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).
At each generator $\sigma_i$ ($i = 0, \ldots, A-2$), nucleon
$i$ has crossings with nucleons $j = i+1, \ldots, A-1$.  These
$k_i = A - i - 1$ crossings all act on $\sigma_i$ and reduce
via the Hecke relation to a linear combination:

$$
  \prod_{j=i+1}^{A-1} C_{ij}(\sigma_i)
  = 
  a_i  \sigma_i + b_i
$$

where each crossing factor is $C_{ij}(\sigma_i) = c_j \sigma_i + d_j$ with coefficients depending on the pair type:

$$
  (c_j, d_j) = 
  \begin{cases}
    (1, 0) & \text{if } i, j \text{ both protons (}\sigma\text{)} \\[3pt]
    (1, -(q - q^{-1})) & \text{if } i, j \text{ both neutrons (}\sigma^{-1}\text{)} \\[3pt]
    (1, -\tfrac{1}{2}(q - q^{-1}))
      & \text{if mixed (}\tfrac{1}{2}(\sigma + \sigma^{-1})\text{)}
  \end{cases}
$$

The coefficients $(a_i, b_i)$ satisfy the recurrence: starting
from $(a_0, b_0) = (0, 1)$ (identity), multiplying
$(a_k \sigma + b_k)(c_j \sigma + d_j)$ and applying
$T^2 = (q - q^{-1})T + 1$:

$$
  a_{k+1} = a_k c_j (q - q^{-1}) + a_k d_j + b_k c_j,
  \qquad
  b_{k+1} = a_k c_j + b_k d_j.
$$

This is a $2 \times 2$ **transfer matrix** $T_j$ at each crossing.

## Jet expansion in the nucleon count

The transfer matrix product at generator $\sigma_i$:

$$
  M_i =  \prod_{j=i+1}^{A-1} T_j
$$

is a product of $k_i = A - i - 1$ matrices.  This product
admits a **jet expansion** — a Taylor series in the number of
crossings, where each order corresponds to a color degree:

$$
  M_i =  \mathbb{1}
  +  \underbrace{\sum_{j} T_j^{(1)}}_{\text{1-jet: pair interactions}}
  +  \underbrace{\sum_{j < k} T_j^{(1)} T_k^{(1)}}_{\text{2-jet: triple correlations}}
  +  \cdots
  +  \underbrace{\prod_{j} T_j^{(1)}}_{\text{$k_i$-jet: full product}}
$$

where $T_j = \mathbb{1} + T_j^{(1)}$ and $T_j^{(1)}$ is the
deviation from the identity.

**The color degree at generator $\sigma_i$ is exactly $k_i = A - i - 1$.**

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

which is exponential.  But the **transfer matrix product computes
the exact answer** (the $k_i$-jet) in exactly $k_i$ steps — one
per crossing.  The total across all generators:

$$
  \sum_{i=0}^{A-2} k_i
  = 
  \sum_{i=0}^{A-2} (A - i - 1)
  = 
  \frac{A(A-1)}{2}
  = 
  \binom{A}{2}
$$

This is **exact** — not an approximation.  No terms are dropped.
Every jet order is included.  The transfer matrix product
computes $\binom{A}{2}$ steps, and this number has physical
meaning: it is the number of nucleon pairs in the nucleus.

## Beta decay as the 1-jet variation

Single beta decay ($\beta^{\pm}$) changes one nucleon type.
The energy variation $\delta E$ is the **first jet** (first
variation) of the energy functional in the nucleon-type
variable $\tau_p \in \{\mathfrak{p}, \mathfrak{n}\}$:

$$
  \delta E =  \sum_{i=0}^{p} (V_i^{\mathrm{dau}} - V_i^{\mathrm{par}})
$$

summing only over generators affected by the converting
nucleon at position $p$.  Generators $i > p$ are unaffected
and cancel exactly.

This is the **1-jet** of $E$ in the fibre direction: a single
crossing change at one nucleon.

## Double beta decay as the 2-jet variation

**Double beta decay** ($2\beta$) changes two nucleons
simultaneously.  If nucleons at positions $p_1$ and $p_2$
(with $p_1 < p_2$) both convert $\mathfrak{n} \to \mathfrak{p}$,
the energy variation has a **cross-term**:

$$
  \delta^2 E
  = 
  \underbrace{\delta E_{p_1} + \delta E_{p_2}}_{\text{sum of single variations}}
  + 
  \underbrace{\Delta_{p_1 p_2}}_{\text{2-jet cross-term}}
$$

The cross-term $\Delta_{p_1 p_2}$ arises because at generators
$\sigma_i$ with $i \leq p_1$, BOTH converting nucleons' crossings
change.  The transfer matrix at these generators sees TWO modified
crossing factors, and the product $T_{p_1}^{(1)} T_{p_2}^{(1)}$
contributes a genuinely new term that is not the sum of individual
variations.

Explicitly: for generator $\sigma_i$ with $i \leq p_1$, the
transfer matrix product changes at positions $j = p_1$ and
$j = p_2$.  Writing $T_j = T_j^{(\mathrm{par})} + \delta T_j$:

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

The 2-jet cross-term is **not** negligible — it encodes the
correlation between the two converting nucleons mediated by
all nucleons between positions $p_1$ and $p_2$.  This is the
**nuclear matrix element $M^{(2\nu)}$** of double beta decay.

For **neutrinoless double beta decay** ($0\nu\beta\beta$), the
2-jet cross-term has a different structure: the two $L_0^{-}$
smoothings are **not independent** (the two emitted electrons
share a single neutrino propagator, which in the braid framework
corresponds to a single unknot $T_{1,0}$ threading both crossing
changes).

## The jet bundle structure

The generator volumes $\{V_i\}_{i=0}^{A-2}$ form a section of
a **jet bundle** over the nuclear configuration space.  The base
is the space of nucleon-type assignments
$\tau : \{0, \ldots, A-1\} \to \{\mathfrak{p}, \mathfrak{n}\}$,
and the fibre at each assignment is the vector of generator
volumes $(V_0, \ldots, V_{A-2})$.

| Object | Jet bundle interpretation |
|--------|-------------------------|
| Nucleon-type assignment $\tau$ | Point in the base |
| Generator volumes $(V_0, \ldots, V_{A-2})$ | Section of the fibre |
| Single beta decay $\delta\tau_{p}$ | 1-jet (first derivative) |
| Double beta decay $\delta\tau_{p_1} \delta\tau_{p_2}$ | 2-jet (second derivative) |
| $r$-fold decay | $r$-jet ($r$-th derivative) |
| Full transfer matrix product | $\infty$-jet (exact) |

The color degree of the $r$-jet at generator $\sigma_i$ is
$\min(r, k_i)$, bounded by the number of crossings at that
generator.

## Generator volume profile

The Markov-traced volume at generator $\sigma_i$ is:

$$
  \hat{V}_i =  z \cdot a_i + b_i
$$

where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter.
The nuclear energy decomposes as:

$$
  \tfrac{1}{2}\ln\bigl(\mathrm{tr}(\mathcal{N}) \cdot \overline{\mathrm{tr}(\mathcal{N})}\bigr) =
  \tfrac{1}{2}\sum_{i=0}^{A-2} \ln\bigl(\hat{V}_i \cdot \overline{\hat{V}_i}\bigr)
$$

Each term $\tfrac{1}{2}\ln(\hat{V}_i \cdot \overline{\hat{V}_i})$ is determined by exactly $k_i$
transfer matrix steps.

## The volume of the ideal

The Gröbner--Shirshov ideal $I$ at generator $\sigma_i$ absorbs the
difference between the unreduced weight and the reduced weight.
The **ideal volume** at generator $i$ is:

$$
  V_i^I =  k_i - V_i
$$

where $k_i = A - i - 1$ is the number of crossings.  This is
the energy removed by the Hecke relation — the "resolved"
crossings.  The total ideal volume
$V^I = \sum_i V_i^I = \binom{A}{2} - E$ measures how much of
the naive crossing count is absorbed by double-crossing
resolutions.

## Computational verification

| Nucleus | $A$ | $\binom{A}{2}$ | $E(\mathrm{parent})$ | $E(\mathrm{daughter})$ | $\Delta E$ |
|---------|-----|:-:|---------------------|----------------------|-----------|
| ${}^{2}\mathrm{H}$ | 2 | 1 | $1.174$ | $1.000$ | $-0.174$ |
| ${}^{3}\mathrm{H}$ | 3 | 3 | $2.728$ | $2.466$ | $-0.263$ |
| ${}^{4}\mathrm{He}$ | 4 | 6 | $4.136$ | $3.794$ | $-0.342$ |
| ${}^{6}\mathrm{Li}$ | 6 | 15 | $8.054$ | $7.567$ | $-0.486$ |
| ${}^{14}\mathrm{C}$ | 14 | 91 | $47.171$ | $43.810$ | $-3.361$ |
| ${}^{60}\mathrm{Co}$ | 60 | 1770 | $38{,}863$ | $35{,}813$ | $-3{,}050$ |
| ${}^{210}\mathrm{Bi}$ | 210 | 21945 | $8.25 \times 10^{13}$ | $7.62 \times 10^{13}$ | $-6.24 \times 10^{12}$ |

All $\Delta E$ are negative — the daughter has lower energy.
The computation requires exactly $\binom{A}{2}$ transfer matrix
multiplications (including ${}^{210}\mathrm{Bi}$: 21,945 steps,
instant).

## Generator volume profile: ${}^{14}\mathrm{C}$ vs ${}^{14}\mathrm{N}$

Generators $\sigma_7$ through $\sigma_{12}$ have **identical
volumes** in both nuclei — only generators $\sigma_0$ through
$\sigma_6$ differ (the 1-jet support of the single beta decay).

| Generator | $k_i$ | $V_i({}^{14}\mathrm{C})$ | $V_i({}^{14}\mathrm{N})$ | $\Delta V_i$ |
|:---------:|:---:|:-----------------------:|:-----------------------:|:------------:|
| $\sigma_0$ | 13 | $5.970$ | $5.616$ | $-0.354$ |
| $\sigma_1$ | 12 | $5.485$ | $5.150$ | $-0.335$ |
| $\sigma_2$ | 11 | $4.823$ | $4.540$ | $-0.283$ |
| $\sigma_3$ | 10 | $4.476$ | $4.201$ | $-0.275$ |
| $\sigma_4$ | 9 | $3.887$ | $3.661$ | $-0.226$ |
| $\sigma_5$ | 8 | $3.664$ | $3.436$ | $-0.228$ |
| $\sigma_6$ | 7 | $4.603$ | $2.943$ | $-\mathbf{1.660}$ |
| $\sigma_7$--$\sigma_{12}$ | 6--1 | identical | identical | $0$ |

Generator $\sigma_6$ — the converting neutron's own generator —
has the **largest volume change** ($-1.660$, nearly half the total
$\Delta E$).  Its color degree is $k_6 = 7$: it sees 7 crossings
with downstream nucleons, ALL of which change type when the
neutron converts to a proton.  This is the highest color degree
at the converting position.

## Connection to the Reeb decomposition

The color degree at each generator corresponds to the
**vertical degree** $\deg\alpha_V$ of the Reeb flow:

- Generator $\sigma_0$: color degree $A - 1$ (sees all
  other nucleons) — the "lowest" Reeb stratum
- Generator $\sigma_{A-2}$: color degree $1$ (sees one
  nucleon) — the "highest" Reeb stratum

The jet expansion at each generator is the **Taylor series
of the transfer matrix product along the Reeb flow direction**.
Each additional crossing adds one color degree, corresponding
to one more nucleon entering the interaction region.

This means the generator volume decomposition is the **discrete
analogue of the jet bundle of the canonical action** $\mathfrak{S}_q$
over the nuclear configuration space.  The 1-jet gives single
beta decay; the 2-jet gives double beta decay; the full
$\infty$-jet gives the exact energy — all computed by the same
$\binom{A}{2}$ transfer matrix steps.
