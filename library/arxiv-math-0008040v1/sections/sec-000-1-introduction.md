---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 1.0
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
Let $U=U_q({\mathbf{g}})$ be the quantum group associated to a semisimple Lie algebra $\mathbf{g}$ of rank $n$. The negative part $U^-$ of $U$ has a canonical basis $\mathbf{B}$ with favourable properties (see Kashiwara [@kash2] and Lusztig [@lusztig6 §14.4.6]). For example, via action on highest weight vectors it gives rise to bases for all the finite-dimensional irreducible highest weight $U$-modules.

Let $W$ be the Weyl group of ${\mathbf{g}}$, with Coxeter generators $s_1,s_2,\ldots ,s_n$, and let $w_0$ be the element of maximal length in $W$. Let ${\mathbf{i}}$ be a reduced expression for $w_0$, i.e. $w_0=s_{i_1}s_{i_2}
\cdots s_{i_k}$ is reduced. Lusztig obtains a parametrization of the canonical basis $\mathbf{B}$ for each such reduced expression $\mathbf{i}$, via a correspondence between a basis of PBW-type associated to $\mathbf{i}$ and the canonical basis. This gives a bijection $\varphi_{\mathbf{i}}:\B\rightarrow \N^k,$ where $\N=\{0,1,2,\ldots \}$.

Kashiwara, in his approach to the canonical basis (which he calls the global crystal basis), defines certain root operators $\TF_i$ on the canonical basis (see [@kash2 §3.5]) which lead to a parametrization of the canonical basis for each reduced expression $\mathbf{i}$ by a certain subset $Y_{\mathbf{i}}$ of $\N^k$. This gives a bijection $\psi_{\mathbf{i}}:\B\rightarrow
Y_{\mathbf{i}}$. The subset $Y_{\mathbf{i}}$ is called the string cone.

There is no simple way to express the elements of $\B$ in terms of the natural generators $F_1,F_2,\ldots ,F_n$ of $U^-$. This has been done for all of $\mathbf{B}$ only in types $A_1,A_2,A_3$ and $B_2$ (see [@lusztig2 §3.4], [@lusztig7 §13], [@xi2] and [@xi3]) and appears to become arbitrarily complicated in general.

A monomial $F_{i_1}^{(a_1)}F_{i_2}^{(a_2)}\cdots F_{i_k}^{(a_k)}$, where $F_i^{(a)}=F_i^a/[a]!$, is said to be *tight* if it belongs to ${\B}$. Lusztig [@lusztig7] described a method which in low rank cases leads to the construction of tight monomials. He defined, for each reduced expression $\mathbf{i}$ of $w_0$, a certain cone $C_{\mathbf{i}}$ in $\N^k$ which we shall call the Lusztig cone. Let $$M_{\mathbf{i}}=\{F_{i_1}^{(a_1)}F_{i_2}^{(a_2)}\cdots F_{i_k}^{(a_k)}
\,:\,\mathbf{a}\in C_{\mathbf{i}}\}$$ be the set of monomials obtained from elements of $C_{\mathbf{i}}$. Lusztig showed that, in types $A_1,A_2$ and $A_3$, $M_{\mathbf{i}}\subseteq \B$. The author [@me7] has extended this to type $A_4$. However, counter-examples of Xi [@xi4] and Reineke [@reineke2] show that this fails for higher rank.

Instead, one can consider monomials in Kashiwara's operators $\TF_i$. Define, for a reduced expression $\mathbf{i}$ for $w_0$, $$\B_{\mathbf{i}}=\{b\in \B\,:\,b\equiv \TF_{i_1}^{a_1}\TF_{i_2}^{a_2}\cdots
\TF_{i_k}^{a_k}\cdot 1,\ \mathbf{a}\in C_{\mathbf{i}}\}.$$ It has been shown by Premat [@premat1] that $C_{\mathbf{i}}\subseteq Y_{\mathbf{i}}$, so we have $\B_{\mathbf{i}}=\psi_{\mathbf{i}}^{-1}(C_{\mathbf{i}})$. Then it is known that $\B_{\mathbf{i}}=M_{\mathbf{i}}$ in types $A_1,A_2,A_3$ (using Lusztig's work [@lusztig7] and direct calculation); it will be seen in [@me10] that this is also true in type $A_4$. This breaks down in higher ranks because of the above counter-examples. Thus $B_{\mathbf{i}}$ can be regarded as a generalisation of $M_{\mathbf{i}}$ for higher ranks, and it is likely that canonical basis elements in $B_{\mathbf{i}}$ will have a common form.

Furthermore, the cones $C_{\mathbf{i}}$ play a role with respect to various reparametrization functions of the canonical basis. Let $\mathbf{i},\mathbf{j}$ be reduced expressions for $w_0$. There is a reparametrization function, $R_{\mathbf{i}}^{\mathbf{j}}=
\varphi_{\mathbf{j}}\varphi_{\mathbf{i}}^{-1}:\mathbb{N}^k\rightarrow \mathbb{N}^k$ (see [@lusztig2 §2]); a reparametrization function $T_{\mathbf{i}}^{\mathbf{j}}=\psi_{\mathbf{j}}\psi_{\mathbf{i}}^{-1}:
Y_{\mathbf{i}} \rightarrow Y_{\mathbf{j}}$ (see [@bz1 §§2.6, 2.7] and also the remark at the end of Section 2 of [@nz1]). We also define a reparametrization function $S_{\mathbf{i}}^{\mathbf{j}}=\varphi_{\mathbf{j}}\psi_{\mathbf{i}}^{-1}:
Y_{\mathbf{i}} \rightarrow {\mathbf{N}}^k$ linking the approaches of Lusztig and Kashiwara. The functions $R_{\mathbf{i}}^{\mathbf{j}}$ and $T_{\mathbf{i}}^{\mathbf{j}}$ are known to be piecewise-linear, and it follows that $S_{\mathbf{i}}^{\mathbf{j}}$ is also piecewise-linear. These functions are very difficult to understand; they have recently been described by Zelevinsky in [@bz3], but their regions of linearity are only known in types $A_1$--$A_5$, $B_2$, $C_3$, $D_4$ and $G_2$ (see [@carter3] and references therein).

Suppose now that $\mathbf{g}$ is of type $A_n$. In [@me8], it was shown that $C_{\mathbf{i}}$ could be expressed as the set of nonnegative integral combinations of a certain set of $k$ spanning vectors, $v_j(\mathbf{i})$, $j=1,\ldots ,n$, $v_P(\mathbf{i})$, $P$ a partial quiver of type $A_n$ associated to $\mathbf{i}$ (as described in [@me8]). A partial quiver of type $A_n$ is a quiver of type $A_n$ with some directed edges replaced by undirected edges in such a way that the subgraph of directed edges is connected.

If an element $\mathbf{a}=(a_1,a_2,\ldots ,a_k)\in C_{\mathbf{i}}$ is written $\mathbf{a}=(a_{\alpha})_{\alpha\in \Phi^+}$, where $\Phi^+$ is the set of positive roots of $\mathbf{g}$ and $a_{\alpha}=a_j$ where $\alpha$ is the $j$th root in the ordering on $\Phi^+$ induced by $\mathbf{i}$, then the $v_j(\mathbf{i})$ and the $v_P(\mathbf{i})$ do not depend on $\mathbf{i}$ and are described in [@me8]. These vectors have also been studied by Bédard [@bedard2] in terms of the representation theory of quivers. Here we show that if $\mathbf{a}=(a_1,a_2,\ldots ,a_k)$ is one of these vectors then the corresponding monomial of Kashiwara's operators $\TF_{i_1}^{a_1}
\TF_{i_2}^{a_2}\cdots \TF_{i_k}^{a_k}\cdot 1$ can be described using a remarkable rectangle combinatorics.

For $j=1,2,\ldots ,n$ and $P$ a partial quiver associated to $\mathbf{i}$, let $b_j(\mathbf{i})=\psi_{\mathbf{i}}^{-1}(v_j(\mathbf{i}))$ and $b_P(\mathbf{i})=\psi_{\mathbf{i}}^{-1}(v_P(\mathbf{i}))$ be the corresponding canonical basis elements. We will show that these elements are independent of the reduced expression $\mathbf{i}$. Thus the canonical basis elements arising in this way for at least one reduced expression $\mathbf{i}$ can be labelled $b_j$, $j=1,2,\ldots ,n$, $b_P$, $P$ a partial quiver of type $A_n$.

The following conjecture, which will be shown in type $A_4$ in [@me10], suggests that these elements are important in understanding the canonical basis. For a reduced expression $\mathbf{j}$ for $w_0$, let $c_j(\mathbf{j})=\phi_{\mathbf{j}}(b_j)$ and let $c_P(\mathbf{j})=
\phi_{\mathbf{j}}(b_P)$ be the parametrizations of these canonical basis elements arising from Lusztig's approach.

::: conjecture
(Carter and Marsh)\
Let $\mathbf{i}$ be a reduced expression for $w_0$ and let $\mathbf{k}=
(1,3,5,\ldots 2,4,6,\ldots )$ and $\mathbf{k'}=(2,4,6,\ldots ,1,3,5,\ldots )$, the opposite reduced expressions for $w_0$ arising in [@lusztig2]. Then the vectors $c_j(\mathbf{k})$, $j=1,2,\ldots ,n$, $c_P(\mathbf{k})$, $P$ a partial quiver associated with $\mathbf{i}$ as above form a simplicial region of linearity $X_{\mathbf{i}}$ of Lusztig's piecewise-linear function $R_{\mathbf{k}}^{\mathbf{k'}}$. Furthermore, all such simplicial regions arise in this way, and the map $\mathbf{i}\mapsto X_{\mathbf{i}}$ from the graph of commutation classes of reduced expressions for $w_0$ (with edges given by the long braid relation) to the graph of simplicial regions of linearity of $R$ (with edges given by adjacency) is a graph isomorphism.
:::

In this paper we shall use the above rectangle combinatorics to calculate the vectors $c_j(\mathbf{j})$, $c_P(\mathbf{j})$ for the reduced expression $\mathbf{j}=(n,n-1,n,n-2,n-1,n,\ldots ,1,2,\ldots ,n)$ for $w_0$. This will be used in a future paper of Carter in order to calculate the vectors $c_j(\mathbf{k})$, $c_P(\mathbf{k})$, and thus the conjectural simplicial regions of linearity of $R_{\mathbf{k}}^{\mathbf{k'}}$. It is also possible that the above conjecture is true for *any* pair of opposite reduced expressions $\mathbf{k},\mathbf{k'}$ for $w_0$; in particular for $\mathbf{j}$ and its opposite $\mathbf{j'}$, i.e. that the vectors $c_j(\mathbf{j})$ and $c_P^{\mathbf{j}}$ span simplicial regions of linearity of $R_{\mathbf{j}}^{\mathbf{j'}}$.
