This appendix is **self-contained**.  Every transfer matrix in the
paper is listed here in explicit closed form, with all notation
defined locally.  No prior reading is required.

## Symbols

See [Table 1](#tbl:tm-notation-table1-data).

## Knot dictionary

Every transfer matrix is labelled by a **pair of knots** $(K_1, K_2)$
meeting at a crossing.  The knots relevant to this paper are:

See [Table 2](#tbl:tm-notation-table2-data).

## Particle assignments

See [Table 3](#tbl:tm-notation-table3-data).

## Nucleons

See [Table 4](#tbl:tm-notation-table4-data).

## Mechanism of transfer-matrix use

Given a nucleus with $A = Z + N$ nucleons, the braid word has
$A - 1$ generators $\sigma_0, \ldots, \sigma_{A-2}$.  At each
generator $\sigma_i$, the transfer matrices of all crossings
are composed as operators acting by left-multiplication,
with crossings applied from right to left in the braid word:

$$
  M_i(q) =  \prod_{j=A-1}^{i+1} T_{K_j, K_i}(q)
$$

where the product is taken in decreasing order of $j$.

The **Markov-traced volume** at generator $\sigma_i$ is:

$$
  \hat{V}_i(q) =  z(q) \cdot (M_i)_{11} + (M_i)_{21}
$$

The **nuclear Skein polynomial** is:

$$
  P_{\mathcal{N}}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

This requires exactly $\binom{A}{2}$ transfer matrix
multiplications (one per nucleon pair).
