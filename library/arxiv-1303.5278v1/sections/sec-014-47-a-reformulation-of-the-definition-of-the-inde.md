---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-014-47-a-reformulation-of-the-definition-of-the-inde
section_title: "A reformulation of the definition of the index"
section_number: 4.7
pages: 24-26
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.899
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
It is sometimes convenient to work with a slight variation on the tetrahedral index function [\[eq.ID\]](#eq.ID){reference-type="eqref" reference="eq.ID"}. Whenever $a-b, b-c \in \mathbb{Z}$ we define $$\label{eq.JDdef}
J_{\Delta}(a,b,c)= (-q^{\frac{1}{2}})^{-b} I_{\Delta}(b-c,a-b)
= (-q^{\frac{1}{2}})^{-c} I_{\Delta}(c-a,b-c) = (-q^{\frac{1}{2}})^{-a} I_{\Delta}(a-b,c-a).$$ Note that the above expressions are equal by the triality identity ([\[eq.Z3\]](#eq.Z3){reference-type="ref" reference="eq.Z3"}) for $I_{\Delta}$, and by using the duality identity ([\[eq.Z2\]](#eq.Z2){reference-type="ref" reference="eq.Z2"}), it follows that $J_{\Delta}$ is invariant under *all permutations* of its arguments. Further, we have $$\label{eq.JD_add_tet_sol}J_{\Delta}(a+s,b+s,c+s) = (-q^{\frac{1}{2}})^{-s} J_{\Delta}(a,b,c) \text{ for all } s \in \mathbb{R}.$$ We also note that the quadratic identity [\[eq.IDquadratic\]](#eq.IDquadratic){reference-type="eqref" reference="eq.IDquadratic"} can be rewritten in the form $$\label{eq.JD_quad_id}
\sum_{a\in\mathbb{Z}} J_{\Delta}(a,b,c) J_{\Delta}(a+x,b,c) \,q^a= \delta_{x,0}.$$ This follows since $$\begin{aligned}
LHS &= \sum_{a\in\mathbb{Z}} (-q^{1/2})^{-b} I_{\Delta}(b-c,a-b)\, (-q^{1/2})^{-b} I_{\Delta}(b-c,a-b+x) \, q^a \\
&= \sum_{e\in \mathbb{Z}} I_{\Delta}(m,e) I_{\Delta}(m,e+x) \,q^e = \delta_{x,0}
\end{aligned}$$ by ([\[eq.IDquadratic\]](#eq.IDquadratic){reference-type="ref" reference="eq.IDquadratic"}) with $m=b-c$ and $e = a - b$.\
Now suppose that $M$ is a 3-manifold whose boundary $\partial M$ consists of $r \ge 1$ tori. Let $\overline{\mathbf A}$, $\overline{\mathbf B}$ and $\overline{\mathbf C}$ be the matrices of angle structure equation coefficients as in Definition [\[matrix equations\]](#matrix equations){reference-type="ref" reference="matrix equations"}, and let $\bar{\boldsymbol{a}}_j, \bar{\boldsymbol{b}}_j, \bar{\boldsymbol{c}}_j$ for $j=1,\dots N$ denote the columns of $\overline{\mathbf A}$, $\overline{\mathbf B}$ and $\overline{\mathbf C}$ respectively. For each $\boldsymbol{k}\in \mathbb{Z}^N$ and oriented multi-curve $\varpi$ in $\partial M$ representing a homology class $[\varpi]  \in H_1(\partial M,\mathbb{Z})$, let $$\bar a_j(\boldsymbol{k},\varpi)=\boldsymbol{k}\cdot \bar\boldsymbol{a}_j + \bar a_{\varpi,j},~~
\bar b_j(\boldsymbol{k},\varpi)=\boldsymbol{k}\cdot \bar\boldsymbol{b}_j + \bar b_{\varpi,j},~~
\bar c_j(\boldsymbol{k},\varpi)=\boldsymbol{k}\cdot \bar\boldsymbol{c}_j + \bar c_{\varpi,j},$$ and $$a_j(\boldsymbol{k},\varpi) =\bar a_j(\boldsymbol{k},\varpi)- \bar b_j(\boldsymbol{k},\varpi),~
b_j(\boldsymbol{k},\varpi)=\bar c_j(\boldsymbol{k},\varpi)-\bar b_j(\boldsymbol{k},\varpi) .$$

Then the definition [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"} of the index of the triangulation $\mathcal{T}$ of a manifold $M$ can be written $$I_{\mathcal{T}}(\varpi)(q)=\sum_{\boldsymbol{k}\in \mathbb Z^{N-r}\subset \mathbb{Z}^N}
(-q^{\frac{1}{2}})^{\boldsymbol{k}\cdot \boldsymbol{\nu}+ \nu_{\varpi}} 
\prod_{j=1}^N I_{\Delta}(-b_j(\boldsymbol{k},\varpi), a_j(\boldsymbol{k},\varpi) ) \, ,$$ where the sum is over $\boldsymbol{k}$ in any coordinate plane $\mathbb{Z}^{N-r} \subset \mathbb{Z}^N$ corresponding to a set $\mathcal B$ of $N-r$ basic edges as given by Theorem [\[pick_edges\]](#pick_edges){reference-type="ref" reference="pick_edges"}.

Let $\boldsymbol{k}=(k_1, \ldots, k_N)$, $\boldsymbol{\nu}=(\nu_1, \ldots, \nu_N)$ and let $\bar b_{ij}$ be the $(i,j)$ entry of $\overline{\mathbf B}$. Then we have $$\boldsymbol{k}\cdot \boldsymbol{\nu}= \sum_i k_i \nu_i = \sum_i 2 k_i - \sum_{i,j} k_i \bar b_{ij}
= \sum_i 2 k_i - \sum_j \boldsymbol{k}\cdot \bar \boldsymbol{b}_j$$ and $\nu_\varpi = - \sum \bar b_{\varpi,j}$, so $$\boldsymbol{k}\cdot \boldsymbol{\nu}+ \nu_\varpi =  \sum_i 2 k_i - \sum_j \bar b_j(k,\varpi).$$ Hence, grouping together the contributions from tetrahedron $j$, we have $$\begin{aligned}
I_{\mathcal{T}}(\varpi)(q) &= \sum_{\boldsymbol{k}\in \mathbb{Z}^{N-r}} 
 q^{\sum_i k_i}   \prod_j  (-q^{\frac{1}{2}})^{- \bar b_j (k,\varpi)} 
I_{\Delta}(\bar b_j(\boldsymbol{k},\varpi)-\bar c_j(\boldsymbol{k},\varpi) , \bar a_j(\boldsymbol{k},\varpi) -\bar b_j(\boldsymbol{k},\varpi)) \notag\\
& = \sum_{\boldsymbol{k}\in \mathbb{Z}^{N-r}} 
 q^{\sum_i k_i}   \prod_j 
J_{\Delta}(\bar a_j(\boldsymbol{k},\varpi), \bar b_j(\boldsymbol{k},\varpi) , \bar c_j(\boldsymbol{k},\varpi)),
\label{JD_index_eq}
\end{aligned}$$ where $\mathbb{Z}^{N-r} \subset \mathbb{Z}^N$ corresponds to a set $\mathcal B$ of $N-r$ basic edges as given by Theorem [\[pick_edges\]](#pick_edges){reference-type="ref" reference="pick_edges"}.

In particular, this expression shows that the index does not depend on the quad-choice used in the original definition.

::: rmk
[]{#basis_indept label="basis_indept"} Next we show that the definition of index in [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"} does not depend on the choice of integer basis for the integer row space $\Lambda \subset \mathbb{R}^{2N}$ of the Neumann-Zagier matrix $(\mathbf A \mid \mathbf B)$.

Each $x \in \Lambda$ can be written in the form $$\label{lambda_rep}
x = \sum_i k_i E_i$$ where $E_i$ is the $i$th row of $(\mathbf A \mid \mathbf B)$ and $\boldsymbol{k}=(k_1, \ldots, k_N) \in \mathbb{Z}^N$. We claim that the expression $$\label{term_in_sum}
J(x,\varpi) = q^{\sum_i k_i}   \prod_j  J_{\Delta}(\bar a_j(\boldsymbol{k},\varpi), \bar b_j(\boldsymbol{k},\varpi) , \bar c_j(\boldsymbol{k},\varpi))$$ is well-defined, depending only on $x \in \Lambda$ and not on the choice of $\boldsymbol{k}$ in [\[lambda_rep\]](#lambda_rep){reference-type="eqref" reference="lambda_rep"}.

To see this, consider the linear map $\psi : \mathbb{R}^N \to \mathbb{R}^{2N}$ defined by $\psi(k_1, \ldots,k_N) = \sum_i k_i E_i$ and let $\langle C \rangle \subset \mathbb{R}^N$ be the real subspace generated by the cusp relation vectors $(c_{h1}, \ldots, c_{hN})$ where the cusp index $h$ varies over $\{1, \ldots, r \}$. Then $\psi(\langle C \rangle) = 0$ by the cusp relations [\[cusp_relations\]](#cusp_relations){reference-type="eqref" reference="cusp_relations"}, and the work of Neumann and Zagier ([@NZ; @Neumann-combi]) also shows that $\dim \rm{Im}\, \psi =N-r$ and $\dim \langle C \rangle=r$ where $r$ is the number of cusps. Hence $\langle C \rangle = \ker \psi$.

So if $x = \sum_i k_i E_i = \sum_i k'_i E_i$ where $\boldsymbol{k}'=(k'_1, \ldots, k'_N) \in \mathbb{R}^N$ then $\boldsymbol{k}'=\boldsymbol{k}+ \boldsymbol{c}$ where $\boldsymbol{c} \in \langle C \rangle$. We claim that replacing $\boldsymbol{k}$ by $\boldsymbol{k}'$ does not change the expression [\[term_in_sum\]](#term_in_sum){reference-type="eqref" reference="term_in_sum"}. To see this, suppose we replace $\boldsymbol{k}$ by $\boldsymbol{k}'$ where $k'_i= k_i + s  c_{hi}$ for $i=1, \ldots, N$ and $s \in \mathbb{R}$. Then the term $q^{\sum_i k_i}$ in [\[term_in_sum\]](#term_in_sum){reference-type="eqref" reference="term_in_sum"} is multiplied by $q^{s n_h}$ where $n_h$ is the number of vertices in the triangulation of cusp $h$, while $\bar a_j(\boldsymbol{k},\varpi), \bar b_j(\boldsymbol{k},\varpi) , \bar c_j(\boldsymbol{k},\varpi)$ are increased by $s$ for each triangle of tetrahedron $j$ lying in the cusp $h$. By ([\[eq.JD_add_tet_sol\]](#eq.JD_add_tet_sol){reference-type="ref" reference="eq.JD_add_tet_sol"}), this changes $\prod_j J_{\Delta}(\bar a_j(\boldsymbol{k},\varpi), \bar b_j(\boldsymbol{k},\varpi) , \bar c_j(\boldsymbol{k},\varpi))$ by a factor $(-q^{1/2})^{-2s n_h}$ since there are $2n_h$ triangles on cusp $h$. Hence the right hand side of [\[term_in_sum\]](#term_in_sum){reference-type="eqref" reference="term_in_sum"} does not change.

We conclude that the expression for index in [\[JD_index_eq\]](#JD_index_eq){reference-type="eqref" reference="JD_index_eq"} can be rewritten in the form $$I_\mathcal{T}(\varpi) = \sum_{x \in \Lambda} J(x,\varpi)$$ and so does not depend on a choice of basis for $\Lambda$. Further, we can evaluate $I_\mathcal{T}(\varpi)$ by choosing an integer basis for $\Lambda$ corresponding to a set of basic edges as given by Theorem [\[pick_edges\]](#pick_edges){reference-type="ref" reference="pick_edges"}, and we recover the definition of index in [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"}.

It also follows that we can write the index in the form $$I_\mathcal{T}(\varpi) = \sum_{\boldsymbol{k}\in S} q^{\sum_i k_i}   \prod_j 
J_{\Delta}(\bar a_j(\boldsymbol{k},\varpi), \bar b_j(\boldsymbol{k},\varpi) , \bar c_j(\boldsymbol{k},\varpi)),$$ where $S \subset \mathbb{Z}^N$ is any complete set of coset representatives for $(\mathbb{Z}^N + \langle C \rangle)/\langle C \rangle \subset \mathbb{R}^N /\langle C \rangle$.
:::
