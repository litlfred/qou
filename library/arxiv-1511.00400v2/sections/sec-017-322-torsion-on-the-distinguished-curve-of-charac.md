---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-017-322-torsion-on-the-distinguished-curve-of-charac
section_title: "Torsion on the distinguished curve of characters"
section_number: 3.2.2
pages: 20-22
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.988
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
We say that a character $\chi\in X(M^3)$ is trivial if it takes values in $\{\pm 2\}$, i.e. it is a lift or the trivial character in $\mathrm{PSL}_2(\mathbb{C})$.

An irreducible character is the character of a unique conjugacy class of representations. A reducible character can correspond to more conjugacy classes, but if the character is non-trivial, then either all representations with this character are acyclic, either none of them is (Lemma [\[lemma:acyclicorbit\]](#lemma:acyclicorbit){reference-type="ref" reference="lemma:acyclicorbit"}).

::: definition
Define the torsion function on $X_0(M^3)$ minus the trivial character: $$\label{eqn:torsionfunct2}
\mathbb{T}_M(\chi_\rho)=\left\{
\begin{array}{ll}
\operatorname{tor}(M^3,\rho) & \textrm{if }\rho\textrm{ is acyclic;} \\
0 &  \textrm{if } \chi_\rho \textrm{ is non-trivial and } \rho \textrm{ 
non-acyclic,}
\end{array}
\right.$$ where $\chi_\rho$ denotes the character of $\rho$.
:::

::: prop
[]{#prop:rational label="prop:rational"} For a hyperbolic oriented manifold with one cusp, the torsion defines a rational function on $X_0(M^3)$, $\mathbb{T}_M\in \mathbb{C}(X_0(M^3))$, which is regular away from the trivial character.

In particular, if the trivial character is not contained in $X_0(M^3)$ (e.g. if $b_1(M^3)=1$), then $\mathbb{T}_M\in \mathbb{C}[X_0(M^3)]$, i.e. it is holomorphic (with no poles) $$\mathbb{T}_M \colon X_0(M^3)\to \mathbb{C}.$$
:::

::: remark
We prove that the trivial representation cannot be approached by irreducible ones when $b_1(M^3)=1$ in Appendix [\[sec:notapprox\]](#sec:notapprox){reference-type="ref" reference="sec:notapprox"}. This is always the case when $M^3$ is a knot exterior.
:::

::: proof
*Proof.* The dimension of each cohomology group is upper semi-continuous on the representation (see [@Heusener-Porti2011 Lemma 3.2], this is a particular case of the semi-continuity theorem [@Hartshorne1977 Ch. III, Theorem 12.8]). With Lemma [\[lemma:acyclicorbit\]](#lemma:acyclicorbit){reference-type="ref" reference="lemma:acyclicorbit"}, we can conclude that acyclicity holds true in a dense open Zariski domain $U\subset  X_0(M^3)$, after removing the trivial character if required. The fact that the function $\mathbb{T}_M$ is algebraic on this domain is clear, as this is defined from polynomials on the entries of $\rho$. Invariance by conjugation is one of the properties of the torsion. Thus it remains to deal with the points where it is not acyclic. Recall that by Lemma [\[lemma:acyclicorbit\]](#lemma:acyclicorbit){reference-type="ref" reference="lemma:acyclicorbit"} a representation with nontrivial character is acyclic if and only all representations with the same character are.

First notice that $H^0(M^3;\rho)$ is trivial when the character $\chi_\rho$ is non-trivial, because this cohomology group is naturally isomorphic to the space of invariants $\mathbb{C}^{\rho(\pi_1 M^3)}$. More precisely, $\mathbb{C}^{\rho(\pi_1 M^3)}$ is non-trivial only when all elements in $\rho(\pi_1 M^3)$ have $1$ as eigenvalue, which means that their trace is $2$, i.e. $\chi_\rho$ is trivial. Thus by duality $H_0(M^3;\rho)=  0$ when $\chi_\rho$ is non-trivial.

Now fix a representation $\rho_1$ which is not acyclic and non-trivial. Non-acyclicity implies that $H_1(M^3;\rho_1)\neq 0$ and $H_2(M^3;\rho_1)\neq 0$, as $H_0(M^3;\rho_1) = 0$, the homotopical dimension of $M^3$ is $2$, and $\chi(M^3)=0$. Notice that $M^3$ has the simple homotopy type of a 2-complex (see [@Nicolaescu Page 54] for instance), that can be used to compute the torsion. Using the notation of Section [\[sec:comb\]](#sec:comb){reference-type="ref" reference="sec:comb"}, fix a basis $\{v_1,v_2\}$ for $\mathbb{C}^2$ and lifts of cells $\tilde e^i_j$ of a triangulation of $M^3$. Then define a family of basis $c_i(\rho)$ by varying the representation in $v_k\otimes_\rho \tilde e^i_j$. Now choose $\tilde b_1(\rho)=c_2(\rho)$ and $\tilde b_0(\rho)$, a linear combination of $c_1(\rho)$ with constant coefficients (though $c_1(\rho)$ changes with $\rho$), so that $\partial(\tilde b_0(\rho_1))=c_0(\rho_1)$. The function $$\label{eqn:ratiotau2}
\rho\mapsto [\partial \tilde b_1(\rho)\sqcup \tilde b_0(\rho),c_1(\rho) ]/[\partial \tilde b_0( \rho),c_0(\rho)]$$ is well defined in the set where its denominator does not vanish. This is a Zariski open set that contains $\rho_1$. On this set $\partial \tilde b_1(\rho)=\partial c_2(\rho)$ has maximal rank iff $\rho$ is acyclic, thus the function [\[eqn:ratiotau2\]](#eqn:ratiotau2){reference-type="eqref" reference="eqn:ratiotau2"} vanishes when $\rho$ is not acyclic, and when $\rho$ is acyclic [\[eqn:ratiotau2\]](#eqn:ratiotau2){reference-type="eqref" reference="eqn:ratiotau2"} is the torsion. ◻
:::

::: example
[]{#ex:fig8sl2 label="ex:fig8sl2"} For the figure eight knot, in [@Kitano94b] Kitano computes it: $$\mathbb{T}_M(\rho)=2-2\operatorname{tr}(\rho(m))=2-2\chi_\rho(m)\, ,$$ where $m$ denotes the meridian of the knot. Notice that here the function only depends on $\operatorname{tr}(\rho(m))$, namely the evaluation of the character at $m$, and one does not need to describe the variety of characters. In general, as $\operatorname{tr}(\rho(m))$ is a non-constant function on the curve $X_0(M^3)$, $\mathbb{T}_M(\rho)$ and $\chi_\rho(m)= \operatorname{tr}(\rho(m))$ are related by a polynomial equation; compare with [@DuboisG16].
:::
