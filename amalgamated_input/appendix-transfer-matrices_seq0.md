<!-- FILE_START: tm-notation-intro.md -->
The transfer matrices that carry the paper's nuclear computations are
scattered across several chapters, each introducing its own symbols
where they first arise.  This appendix gathers those conventions in one
place so that any transfer matrix can be looked up in explicit closed
form without hunting back through the derivations that produced it.  The
recurring symbols the reader will meet below are the substrate parameter
$q$, the braid/Hecke generators $\sigma_i$, the transfer matrices
$T_{K_1,K_2}$ themselves, and the Markov parameter $z(q)$ used to close
each crossing into a scalar.

Concretely, every transfer matrix here is fixed by a single labelling
convention: it is indexed by the **pair of knots** $(K_1, K_2)$ that
meet at a crossing, so the symbol $T_{K_1,K_2}(q)$ names the matrix
before any general scheme is stated.

The tables that follow set out these conventions in order — first the
symbol glossary, then the knot dictionary, the particle assignments, and
the nucleon labels — after which the mechanism relating them is given.
<!-- FILE_END: tm-notation-intro.md -->

<!-- FILE_START: tm-notation.md -->
This appendix is **self-contained**: every transfer matrix in the
paper appears here in explicit closed form, with all notation
defined locally.

## Symbols

The symbols used throughout this appendix, with their meanings, are
collected in [Table 1](#tbl:tm-notation-table1-data).

## Knot dictionary

Every transfer matrix is labelled by a **pair of knots** $(K_1, K_2)$
meeting at a crossing.  The knots relevant to this paper, and the
labels by which they are referenced below, are listed in
[Table 2](#tbl:tm-notation-table2-data).

## Particle assignments

The particle carried by each knot type is recorded in
[Table 3](#tbl:tm-notation-table3-data).

## Nucleons

The knot assignments for the proton and neutron are given in
[Table 4](#tbl:tm-notation-table4-data).

## Mechanism of transfer-matrix use

The per-crossing transfer matrices are composed across an entire
nucleus to produce a single scalar, its **nuclear Skein polynomial**
$P_{\mathcal{N}}(q)$; the recipe below spells out that composition.

Given a nucleus with $A = Z + N$ nucleons, the braid word has
$A - 1$ generators $\sigma_0, \ldots, \sigma_{A-2}$.  At each
generator $\sigma_i$, the transfer matrices of all crossings
are composed as operators acting by left-multiplication,
with crossings applied from right to left in the braid word:

$$
  M_i(q) =  \prod_{j=A-1}^{i+1} T_{K_j, K_i}(q)
$$

where the product is taken in decreasing order of $j$.

The **Markov-traced volume** at generator $\sigma_i$ is (with
$z(q) = 1/(q^{1/2} + q^{-1/2})$ the Markov-trace loop value):

$$
  \hat{V}_i(q) =  z(q) \cdot (M_i)_{11} + (M_i)_{21}
$$

The **nuclear Skein polynomial** is:

$$
  P_{\mathcal{N}}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

This requires exactly $\binom{A}{2}$ transfer matrix
multiplications (one per nucleon pair).
<!-- FILE_END: tm-notation.md -->

