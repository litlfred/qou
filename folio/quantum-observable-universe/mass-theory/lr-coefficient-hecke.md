*Let $\mu \vdash n_1$, $\nu \vdash n_2$, and $\lambda \vdash n_1 + n_2$ be partitions. The **Littlewood-Richardson coefficient** $c^\lambda_{\mu\nu}$ is the multiplicity of the irreducible Iwahori-Hecke module $V_\lambda$ in the restriction:*

$$
  V_\lambda \;\downarrow_{\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q)} \;=\; \bigoplus_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}} c^\lambda_{\mu\nu} \cdot (V_\mu \boxtimes V_\nu)
$$

*Equivalently, $c^\lambda_{\mu\nu} = |\mathrm{LR}(\lambda/\mu, \nu)|$ counts the Littlewood-Richardson skew tableaux of shape $\lambda/\mu$ and content $\nu$ whose reverse-reading word is Yamanouchi (every prefix has $\#i \geq \#(i{+}1)$).*

*The coefficient $c^\lambda_{\mu\nu}$ is a non-negative integer. It is zero if $\mu \not\subseteq \lambda$ or $|\lambda| - |\mu| \neq |\nu|$.*

The LR coefficient gives the multiplicity of $V_\lambda$ in the outer tensor product $V_\mu \boxtimes V_\nu$ pulled back through the standard inclusion $\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q) \hookrightarrow \mathbf{H}_{n_1 + n_2}(q)$. This constitutes the Hecke-deformed counterpart of the classical Littlewood-Richardson rule for symmetric groups.

The operator-valued Wenzl 1988 sub-lemma 2.1 ([Crystal R-matrix Sub-lemma 2.1 (operator-valued)](crystal-r-matrix-sub-lemma.md)) sums per $(\mu, \nu)$ block with multiplicity $c^\lambda_{\mu\nu}$:

$$
  \chi^\lambda(W_{\mathrm{inner}} \cdot I \cdot \beta_{\mathrm{block}}) = \sum_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}} c^\lambda_{\mu\nu} \cdot \mathrm{Tr}\bigl(A^\lambda_{\mu\nu}(I) \cdot (\rho_\mu(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_{\mathrm{block}}))\bigr)
$$

The LR coefficient $c^\lambda_{\mu\nu}$ provides the integer multiplicity consumed by the operator-valued combiner. The operator $A^\lambda_{\mu\nu}(I)$ acts on the $c^\lambda_{\mu\nu}$-dimensional multiplicity space.

The canonical formalism computes $c^\lambda_{\mu\nu}$ by direct LR-tableau enumeration with Yamanouchi pruning. The canonical $A=2,3,4$ atomic decompositions rely on precomputed tables. The skew-SYT primitive $f^{\lambda/\mu}$ counts all standard Young tableaux of skew shape and weights all chains. The LR coefficient $c^\lambda_{\mu\nu}$ counts only the Yamanouchi-valid semistandard Young tableaux of content $\nu$.
