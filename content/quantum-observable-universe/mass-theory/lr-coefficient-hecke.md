*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c).
Underlying combinatorial content stays generic to any commutative ring.*

**Proposition.**
*For partitions $\mu \vdash n_1$, $\nu \vdash n_2$, and $\lambda \vdash n_1 + n_2$,
the **Littlewood-Richardson coefficient** $c^\lambda_{\mu\nu}$ is the
multiplicity of the irreducible Iwahori-Hecke module $V_\lambda$ in the
restriction*

$$
  V_\lambda \;\downarrow_{\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q)}
  \;=\; \bigoplus_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}}
        c^\lambda_{\mu\nu} \cdot (V_\mu \boxtimes V_\nu)
$$

*Equivalently, $c^\lambda_{\mu\nu} = |\mathrm{LR}(\lambda/\mu, \nu)|$
is the number of Littlewood-Richardson skew tableaux of shape $\lambda/\mu$
and content $\nu$ whose reverse-reading word is Yamanouchi
(every prefix has $\#i \geq \#(i{+}1)$).*

*The coefficient is a non-negative integer:
$c^\lambda_{\mu\nu} \in \mathbb{Z}_{\geq 0}$, with $c^\lambda_{\mu\nu} = 0$
if $\mu \not\subseteq \lambda$ (as Young diagrams) or
$|\lambda| - |\mu| \neq |\nu|$.*

## Categorical interpretation

The LR coefficient is the multiplicity of $V_\lambda$ in the
**outer tensor product** $V_\mu \boxtimes V_\nu$ pulled back through
the standard inclusion
$\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q) \hookrightarrow \mathbf{H}_{n_1 + n_2}(q)$
(omitting the inter-block generator $\sigma_{n_1}$).
This is the Hecke-deformed counterpart of the classical
Littlewood-Richardson rule for symmetric groups
(\cite{ariki1996} §6, \cite{ram1991}).

## Role in the operator-valued Wenzl branching

The Wenzl 1988 sub-lemma 2.1 (operator-valued form, per
[`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md))
sums **per $(\mu, \nu)$ block** with multiplicity $c^\lambda_{\mu\nu}$:

$$
  \chi^\lambda(W_{\mathrm{inner}} \cdot I \cdot \beta_{\mathrm{block}})
    = \sum_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}}
      c^\lambda_{\mu\nu} \cdot
      \mathrm{Tr}\bigl(A^\lambda_{\mu\nu}(I) \cdot
                       (\rho_\mu(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_{\mathrm{block}}))\bigr)
$$

The LR coefficient $c^\lambda_{\mu\nu}$ is therefore the
**integer multiplicity** that the operator-valued combiner consumes;
the operator $A^\lambda_{\mu\nu}(I)$ acts on the
$c^\lambda_{\mu\nu}$-dimensional multiplicity space.

## Computational realisation

The script
[`computations/substrate/lr_coefficients.py`](../../computations/substrate/lr_coefficients.py)
computes $c^\lambda_{\mu\nu}$ via direct LR-tableau enumeration with
Yamanouchi pruning. Precomputed tables exist for the canonical
A=2/3/4 atomic decompositions
(`LR_TABLE_3_3_TO_6`, `LR_TABLE_3_6_TO_9`, `LR_TABLE_6_6_TO_12`).
The skew-SYT primitive
[`pyhecke.skew_syt.skew_syt_count`](../../tools/pyhecke/python/pyhecke/skew_syt.py)
(PR [#1515](https://github.com/litlfred/qou/pull/1515)) is a
related-but-distinct quantity ($f^{\lambda/\mu} = $ # SYT of skew
shape, weights all chains; $c^\lambda_{\mu\nu}$ counts only the
Yamanouchi-valid SSYT of content $\nu$).
