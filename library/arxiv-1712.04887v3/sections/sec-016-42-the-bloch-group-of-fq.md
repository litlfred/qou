---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-016-42-the-bloch-group-of-fq
section_title: "The Bloch group of Fq"
section_number: 4.2
pages: 23-25
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.939
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#section:hh label="section:hh"}

In order to make our maps explicit, we must relate the Chern class map to the Bloch group. Let $p > 2$ and $q > 2$ be odd primes such that $q \equiv -1 \;\text{\rm mod}\;n$, where $n=p^m$. For a finite field $\mathbf F_q$, the group $\mathbf F^{\times}_q$ is cyclic, so $\bigwedge^2 \mathbf F^{\times}_q$ is a 2-torsion group. Hence the Bloch group $B(\mathbf F_q)$ coincides with the pre-Bloch group after tensoring with $\mathbf F_p$, where the pre-Bloch group is defined as the quotient of the free abelian group on $\mathbf{P}^1(\mathbf F_q)$ by the $5$-term relation ([\[5term\]](#5term){reference-type="ref" reference="5term"}). By [@Hutch], the Bloch group $B(\mathbf F_q)$ is a cyclic group of order $q+1$ up to $2$-torsion. Moreover, following [@Hutch], one may relate $B(\mathbf F_q)$ to the cohomology of $\mathrm{SL}_2(\mathbf F_q)$ in degree three, as we now discuss.

There is an isomorphism $$H_3(\mathrm{SL}_2(\mathbf F_q),\mathbf Z) \otimes \mathbf Z/n\mathbf Z\; \simeq\; \mathbf Z/n\mathbf Z.$$ Let us describe this isomorphism more carefully. By a computation of Quillen, we know that $H_3(\mathrm{SL}_2(\mathbf F_q),\mathbf Z)$ is cyclic of order $q^2 - 1$. It follows that the $p$-part of this group comes from the $p$-Sylow subgroup. If one chooses an isomorphism $$\mathbf F_{q^2} \simeq (\mathbf F_q)^2$$ of abelian groups, one gets a well defined map: $$\mathbf F^{\times}_{q^2} \;=\; C \;=\; \mathrm{Aut}_{\mathbf F_q}(\mathbf F_{q^2}) \rightarrow \mathrm{GL}_2(\mathbf F_q)$$ which is well defined up to conjugation. There is, correspondingly, a map $C^1 \rightarrow \mathrm{SL}_2(\mathbf F_q)$, where $$C^1 \;=\; \text{Ker}\bigl(N: \mathbf F^{\times}_{q^2} \rightarrow \mathbf F^{\times}_q \bigr)\,.$$ We refer to both $C$ and $C^1$ as the non-split Cartan subgroup. By Quillen's computation, we deduce that there is a canonical map: $$C^1 \;=\; H_3(C^1,\mathbf Z) \rightarrow H_3(\mathrm{SL}_2(\mathbf F_q),\mathbf Z)$$ which is an isomorphism after tensoring with $\mathbf Z/n\mathbf Z$. There is a canonical isomorphism $C^1[n] = \mu$, where $\mu$ denotes the $n$th roots of unity. Hence to give an element of order $p$ in $H_3(\mathrm{SL}_2(\mathbf F_q),\mathbf Z)$ up to conjugation is equivalent to giving a primitive $n$th root of unity $\zeta\in C^1 \subset C = \mathbf F^{\times}_{q^2}$. From [@Hutch], there is a canonical map: $$H_3(\mathrm{SL}_2(\mathbf F_q),\mathbf Z) \rightarrow B(\mathbf F_q)\,,$$ at least away from $2$-power torsion, which is an isomorphism after tensoring with $\mathbf Z/n\mathbf Z$. Given a root of unity $\zeta$, let $t$ denote the corresponding element of $\mathrm{SL}_2(\mathbf F_q)$. The corresponding element of $B(\mathbf F_q)$ is given (see [@Hutch]) by: $$\sum_{k \;\text{\rm mod}\;n} \left[ \frac{t(\infty) - t^{k+1}(\infty)}{
t(\infty) - t^{k+2}(\infty)} \right]\,.$$ This construction yields the same element for $\zeta$ and $\zeta^{-1}$. We may represent $t$ by its conjugacy class in $\mathrm{GL}_2(\mathbf F_q)$, which has determinant one and trace $\zeta+ \zeta^{-1} \in \mathbf F_q$. The choice of $\zeta$ up to (multiplicative) sign is given by this trace. Note that the congruence condition on $q$ ensures that the Chebyshev polynomial with roots $\zeta+ \zeta^{-1}$ has distinct roots which split completely over $\mathbf F_q$. Explicitly, we may choose $$t \;=\; 
\left(\begin{matrix} 0 & 1 \\ -1 & \zeta+ \zeta^{-1} \end{matrix} \right) = 
A \left(\begin{matrix} \zeta^{-1} & 0  \\ 0 & \zeta\end{matrix} \right) A^{-1},
\qquad 
A  \;=\; \left(\begin{matrix} \zeta& \zeta^{-1} \\ 1 & 1 \end{matrix} \right).$$ Let $F_k$ be the Chebyshev polynomials, so $\displaystyle{F_k(2 \cos \phi) = \frac{\sin k\phi}{\sin \phi}}$. Then $$t^k(\infty)  \;=\; \frac{F_{k-1}(\zeta+ \zeta^{-1})}{F_k(\zeta+ \zeta^{-1})}\,,$$ and an elementary computation then shows that the corresponding element in $B(\mathbf F_q) \otimes \mathbf Z_p$ is given by $$\label{finitefield}
\sum_{{k \;\text{\rm mod}\;n}} \left[1 -  \frac{1}{F_{k}(\zeta+ \zeta^{-1})^2} \right]  
{
=  \sum_{k \;\text{\rm mod}\;n} \left[  1 - \left(\frac{\zeta-\zeta^{-1}}{\zeta^{k}-\zeta^{-k}}\right)^2 \right],}$$

## The local Chern class map $c_\zeta$ {#sub.reduction}

In this section, $q$ will denote a prime with $q \equiv -1 \;\text{\rm mod}\;p^{m}$ which splits completely in $F$. Let $\mathfrak{q}$ be a prime above $q$. There is a natural map $B(F) \rightarrow B(\mathcal{O}_F/\mathfrak{q}) = B(\mathbf F_q)$.

The reduction map sends $[x]$ to $[\overline{x}]$ under the natural reduction map $\mathbf P^1(F) \rightarrow \mathbf P^1(\mathbf F_q)$.

::: lemma
[]{#lemma:commute label="lemma:commute"} Let $p > 2$. There is a commutative diagram as follows: $$\begin{diagram}
B(F)/nB(F) & \rTo & \bigoplus B(\mathbf F_q) \otimes \mathbf Z/n\mathbf Z& &  \\
\dEquals & & \dLine_{\simeq} & &  \\
K_3(F)/nK_3(F) & \rTo & \bigoplus K_3(\mathbf F_q) \otimes \mathbf Z/n\mathbf Z& 
\rEquals^{\bigoplus c_{\zeta,\mathfrak{q}}} &  
\bigoplus \mathbf F^{\times}_{q^2}/\mathbf F^{\times n}_{q^2}\,,
\end{diagram}$$ where the product runs over all primes $\mathfrak{q}$ of norm $q  \equiv -1 \;\text{\rm mod}\;n$ which split completely in $F$, or alternatively all but finitely many such primes.
:::

::: proof
*Proof.* The isomorphism of the left vertical map is a theorem of Suslin [@Suslintwo Theorem 5.2] (taking into account Lemma [\[suslincomparison\]](#suslincomparison){reference-type="ref" reference="suslincomparison"}), and the isomorphism of the right vertical map follows from [@Hutch]. The fact that the diagram commutes is a consequence of the fact that both constructions are compatible (and can be seen in group cohomology). ◻
:::

Recall that an element $x$ of an abelian group $G$ is $p$-saturated if $x\not\in [p]G$, where $[p]:G \rightarrow G$ is the multiplication by $p$ map.

::: corollary
There is an algorithm to prove that a set of generators of $B(F)$ is $p$-saturated for $p > 2$.
:::

::: proof
*Proof.* Computing $B(\mathbf F_q)$ is clearly algorithmically possible. Moreover, we can *a priori* compute $B(F) \otimes \mathbf Z_p$ as an abstract $\mathbf Z_p$-module. Hence it suffices to find sufficiently many distinct primes $\mathfrak{q}$ such that the image of a given set of generators has the same order as $B(F)/nB(F)$. ◻
:::

In light of the commutative diagram of Lemma [\[lemma:commute\]](#lemma:commute){reference-type="ref" reference="lemma:commute"}, we also use $c_\zeta$ to denote the Chern class map on $B(F)/nB(F)$.

## The local $R_\zeta$ map

Suppose that $q \equiv -1 \;\text{\rm mod}\;p$. It follows that the field $\mathbf F_{q}$ does not contain $\zeta_p$, and so Proposition [\[prop.Pdef\]](#prop.Pdef){reference-type="ref" reference="prop.Pdef"} applies to give maps $P_{\zeta}$ and $R_{\zeta}$ which are well defined over this field. In particular, since $(p,q-1) = 1$, all elements of $\mathbf F_{q}$ are $p$-th powers, and hence the Kummer extension $H$ is given by $H = F_n$ and $R_{\zeta}$ and $P_{\zeta}$ coincide.
