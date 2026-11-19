This appendix is self-contained: every transfer matrix appears in explicit closed form, with notation defined locally.

Symbols are collected in [Table 1](#tbl:tm-notation-table1-data). Every transfer matrix is labelled by a pair of knots $(K_1, K_2)$ meeting at a crossing. The relevant knots and their labels are listed in [Table 2](#tbl:tm-notation-table2-data). Particle assignments for each knot type are in [Table 3](#tbl:tm-notation-table3-data). Knot assignments for the proton and neutron are given in [Table 4](#tbl:tm-notation-table4-data).

The per-crossing transfer matrices are composed across a nucleus to produce a single scalar, its nuclear Skein polynomial $P_{\mathcal{N}}(q)$.

Given a nucleus with $A = Z + N$ nucleons, the braid word has $A - 1$ generators $\sigma_0, \ldots, \sigma_{A-2}$. At each generator $\sigma_i$, the transfer matrices of all crossings are composed as operators acting by left-multiplication, applied from right to left in the braid word:

$$
  M_i(q) = \prod_{j=A-1}^{i+1} T_{K_j, K_i}(q)
$$

The product is taken in decreasing order of $j$. The Markov-traced volume at generator $\sigma_i$ is

$$
  \hat{V}_i(q) = z(q) \cdot (M_i)_{11} + (M_i)_{21}
$$

where $z(q) = q^3/(q^2+1) = q^2/[2]_q$ is the canonical **Convention D** Markov-trace loop value for $\sigma_i$ stabilisation (distinct from $1/(q^{1/2}+q^{-1/2})$, which weights the Temperley–Lieb generator $e_i = q - \sigma_i$ rather than $\sigma_i$, and at which the illustrative decimals in the worked tables below were evaluated). Every symbolic $\hat V_i(q)$ and $P_{\mathcal{N}}(q)$ in this appendix carries $z(q) = q^3/(q^2+1)$:

$$
  P_{\mathcal{N}}(q) = \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

This requires exactly $\binom{A}{2}$ transfer matrix multiplications.
