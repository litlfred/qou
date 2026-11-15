---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-002-3-symmetries-of-integer-linear-programs
section_title: "Symmetries of Integer Linear Programs"
section_number: 3
pages: 7-9
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.973
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:ILP label="sec:ILP"} We now turn to our main focus. Associated with $\operatorname{LP}(A,b,c)$ is the integer linear program $$\label{eq:ILP}
  \begin{array}{ll}
    \max & c^tx\\
    \textrm{s.t.} & Ax \le b \, , \ x \in {\mathbb{Z}}^n  \, ,
  \end{array}$$ which we denote as $\operatorname{ILP}(A,b,c)$. Throughout we make the same assumptions as above: the linear program $\operatorname{LP}(A,b,c)$ is feasible, the matrix $A$ does not have any zero rows, and the inequalities bijectively correspond to the hyperplane arrangement ${\mathscr{H}}(A,b)$; see Remark [\[rem:scale\]](#rem:scale){reference-type="ref" reference="rem:scale"}.

::: definition
A *symmetry* of the integer linear program $\operatorname{ILP}(A,b,c)$ is an automorphism of $\operatorname{LP}(A,b,c)$ which acts on the signed standard basis $\{\pm e_1,\pm e_2,\dots,\pm e_n\}$ of ${\mathbb{R}}^n$ as a signed permutation.
:::

The symmetries of the integer linear program [\[eq:ILP\]](#eq:ILP){reference-type="eqref" reference="eq:ILP"} form a group $\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,c))$ which is a subgroup of the group ${\operatorname{O}}_n{\mathbb{Z}}$, the group of all $0/1/{-}1$-matrices with exactly one non-zero entry per row and column. We have ${\operatorname{O}}_n{\mathbb{Z}}={\operatorname{O}}_n{\mathbb{R}}\cap{\operatorname{GL}}_n{\mathbb{Z}}$, and ${\operatorname{O}}_n{\mathbb{Z}}$ is isomorphic to the Coxeter group of type $B_n$, the group of automorphisms of the regular $n$-dimensional cube and its polar, the regular $n$-dimensional cross polytope. As a consequence, the group of symmetries of an integer linear program is finite, even if $\operatorname{Aut}(\operatorname{LP}(A,b,c))$ is infinite.

The motivation for our definition is Lie-theoretical: let $\Gamma$ be any finite subgroup of ${\operatorname{GL}}_n{\mathbb{Z}}$. Then $\Gamma$ is a compact subgroup of ${\operatorname{GL}}_n{\mathbb{R}}$, hence it is contained in (a conjugate copy of) the maximal compact subgroup ${\operatorname{O}}_n{\mathbb{R}}$. It follows that, up to conjugation in ${\operatorname{GL}}_n{\mathbb{R}}$, the group $\Gamma$ is a subgroup of ${\operatorname{O}}_n{\mathbb{Z}}$.

As an abstract group ${\operatorname{O}}_n{\mathbb{Z}}$ is isomorphic to the wreath product $${\mathbb{Z}}_2\wr\mathop{\mathrm{Sym}}(n) \ = \ ({\mathbb{Z}}_2)^n \rtimes \mathop{\mathrm{Sym}}(n) \, ,$$ where ${\mathbb{Z}}_2$ is the cyclic group of order two and $\mathop{\mathrm{Sym}}(n)$ is the symmetric group of degree $n$; the group $\mathop{\mathrm{Sym}}(n)$ acts on the direct product $({\mathbb{Z}}_2)^n$ by permuting the factors. Each element of ${\operatorname{O}}_n{\mathbb{Z}}$ can be written as a product of a sign vector and a permutation. Since a permutation is a product of disjoint cycles, each signed permutation is a product of signed cycles which are disjoint. In terms of notation we write the signs between the indices within a cycle. This is to say, $(1{+}2{-}4{+}3{-})$ denotes the signed permutation matrix $$\begin{pmatrix}
  0 & 0 & -1& 0\\
  1 & 0 & 0 & 0\\
  0 & 0 & 0 & 1\\
  0 & -1 & 0 & 0
\end{pmatrix}$$ which is to be multiplied to column vectors from the left.

::: remark
In the optimization literature the authors often restrict their attention to symmetries permuting the standard basis vectors; for instance, see Margot [@Margot10] and the references listed there. However, our more general analysis below shows that taking signed permutations into account does not cause any extra effort. Moreover, if the polyhedron $P(A,b)$ is full-dimensional and bounded the group of automorphisms of the linear relaxation is already finite by Lemma [\[lem:Aut_finite\]](#lem:Aut_finite){reference-type="ref" reference="lem:Aut_finite"}. Then $\operatorname{Aut}(\operatorname{LP}(A,b,c))\cap{\operatorname{GL}}_n{\mathbb{Z}}$ is already contained in ${\operatorname{O}}_n{\mathbb{Z}}$ by the Lie-theoretical argument given above. Hence, at least in this case, considering groups of signed permutations is a natural choice.
:::

Before we will inspect groups of symmetries of integer linear programs we need to collect a few basic results on the action of the group ${\operatorname{O}}_n{\mathbb{Z}}$ on the entire space ${\mathbb{R}}^n$. Throughout let $\Gamma$ be a subgroup of ${\operatorname{O}}_n{\mathbb{Z}}$. Then $\Gamma$ acts on the standard basis $$S \ = \ \{\pm e_1,\pm e_2,\dots,\pm e_n\} \, .$$ In the sequel we will always consider this particular action of $\Gamma$. There are two kinds of orbits to distinguish: the *bipolar* orbits contain at least one pair $\pm
e_i$, while the *unipolar* orbits do not. Since $\Gamma$ is a linear group, a signed permutation $\sigma\in\Gamma$ with $\sigma e_i=\epsilon e_j$ and $\epsilon\in \{\pm 1\}$ maps $-e_i$ to $-\epsilon e_j$. Hence, a bipolar orbit only consists of pairs, that is, $-O=O$. On the other hand, for each unipolar orbit $O$ the set $-O=\{-e_i\,|\,e_i\in O\}$ forms another orbit, and $\Gamma$ acts equivalently on $O$ and $-O$.

::: proposition
[]{#prop:fix label="prop:fix"} For the fixed space of $\Gamma$ we have $$\operatorname{Fix}_\Gamma({\mathbb{R}}^n) \ = \ \mathop{\mathrm{lin}}\left\{\beta(O)\vphantom{\text{$O$ orbit of $\Gamma$}}\,\right.\left|\,\vphantom{\beta(O)}\text{$O$ orbit of $\Gamma$}\right\} \ = \
  \mathop{\mathrm{lin}}\left\{\beta(O)\vphantom{\text{$O$ unipolar orbit of $\Gamma$}}\,\right.\left|\,\vphantom{\beta(O)}\text{$O$ unipolar orbit of $\Gamma$}\right\} \, .$$
:::

::: proof
*Proof.* The first equality is a consequence of Lemma [\[lem:fix_spanned_by_betaO\]](#lem:fix_spanned_by_betaO){reference-type="ref" reference="lem:fix_spanned_by_betaO"}. The second equality holds as $\beta(O)=0$ for any bipolar orbit $O$. ◻
:::

::: remark
The points in $S$ are the vertices of the regular $n$-dimensional cross polytope. If $O\subset S$ is a unipolar $\Gamma$-orbit, then $\beta(O)$ is the barycenter of the non-trivial face of the cross polytope which is spanned by the vertices in $O$. In view of cone polarity the action of $\Gamma$ on $S$ is dual to the induced action on the vertices of the regular cube $[-1,1]$. That is, the two corresponding representations of $\Gamma$, on ${\mathbb{R}}^n$ and its dual space, form a contra-gradient pair.
:::

We call the action of $\Gamma$ on the set of signed standard basis vectors *semi-transitive* if there are precisely two opposite orbits of length $n$. Moreover, we call the action *sub-transitive* if there is no proper coordinate subspace which is invariant under $\Gamma$. Clearly, a semi-transitive action is necessarily sub-transitive. The converse does not hold, but we have the following characterization.

::: proposition
[]{#prop:semi-trs label="prop:semi-trs"} Suppose that $\Gamma$ acts sub-transitively. Then either $\Gamma$ acts semi-transitively with orbits $O$ and $-O$ such that the fixed space $$\operatorname{Fix}_\Gamma({\mathbb{R}}^n) \ = \ \mathop{\mathrm{lin}}(\beta_O) \ = \ \mathop{\mathrm{lin}}(\beta_{-O})$$ is one-dimensional, or $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)=0$.
:::

::: proof
*Proof.* If $\Gamma$ has a bipolar orbit $O$, then $O$ equals the entire set $S$ of signed standard basis vectors because $\Gamma$ acts sub-transitively. In this case the fixed space reduces to the origin. If, however, each orbit is unipolar, we have exactly one pair $(O,-O)$ of opposite orbits, again due to sub-transitivity. Now the claim follows from Proposition [\[prop:fix\]](#prop:fix){reference-type="ref" reference="prop:fix"}. ◻
:::

::: corollary
[]{#cor:conjugate label="cor:conjugate"} If $\Gamma$ acts semi-transitively, then $\Gamma$ is conjugate to a subgroup of $\mathop{\mathrm{Sym}}(n)$ in ${\operatorname{O}}_n{\mathbb{Z}}$.
:::

::: proof
*Proof.* Let $O$ and $-O$ be the two orbits of $\Gamma$, both of which have length $n$. Pick a transformation $\epsilon\in{\operatorname{O}}_n{\mathbb{Z}}$ which maps $O$ to the standard basis $\{e_1,e_2,\dots,e_n\}$. Now for each $\gamma\in\Gamma$ the conjugate transformation $\epsilon\gamma\epsilon^{-1}$ leaves the sets $\{e_1,e_2,\dots,e_n\}$ and $\{-e_1,-e_2,\dots,-e_n\}$ invariant. We conclude that $\epsilon\Gamma\epsilon^{-1}$ is a subgroup of $\mathop{\mathrm{Sym}}(n)$. ◻
:::

We now interprete the results above for integer linear programming. Consider an integer linear program $\operatorname{ILP}(A,b,c)$ such that the set $P(A,b)$ of feasible points of the linear relaxation is full-dimensional. Let $\Gamma\le\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,c))$ be a group of automorphisms. We have $\Gamma\le{\operatorname{O}}_n{\mathbb{Z}}$. The action of $\Gamma$ on the set $\{\pm
e_1,\pm e_2,\dots,\pm e_n\}$ can be decomposed into orbits. In this way the most relevant case occurs when $\Gamma$ acts sub-transitively. From Lemma [\[lem:Aut_finite\]](#lem:Aut_finite){reference-type="ref" reference="lem:Aut_finite"} we know that $c$ is contained in the fixed space $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)$, and then Proposition [\[prop:semi-trs\]](#prop:semi-trs){reference-type="ref" reference="prop:semi-trs"} says $c\ne 0$ enforces the action of $\Gamma$ to be semi-transitive. Finally, by Corollary [\[cor:conjugate\]](#cor:conjugate){reference-type="ref" reference="cor:conjugate"} we can conjugate $\Gamma$ into a subgroup of $\mathop{\mathrm{Sym}}(n)$ acting on the standard basis $\{e_1,e_2,\dots,e_n\}$. This is the situation that we will be dealing with in our algorithms below.
