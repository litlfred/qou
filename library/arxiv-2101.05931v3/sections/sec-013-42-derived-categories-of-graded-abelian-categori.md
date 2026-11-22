---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-013-42-derived-categories-of-graded-abelian-categori
section_title: "Derived categories of graded abelian categories"
section_number: 4.2
pages: 11-12
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.909
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
We now specialise to the case of derived categories.  We recall that if $\cA$ is an abelian category, then the bounded derived category $D^b(\cA)$ has a standard t-structure $(D^b(\cA)^{\leq0},D^b(\cA)^{\geq0})$ whose heart is $\cA$.  

Given a $\cB \subset \cA$ a Serre subcategory, we let $D_\cB^b(\cA) \subset D^b(\cA)$ denote the thick subcategory consisting of complexes with cohomology supported in $\cB$. The category $D_\cB^b(\cA)$ inherits a natural t-structure from the standard t-structure on $D^b(\cA)$: $D_\cB^b(\cA)^{\leq0}=D_\cB^b(\cA) \cap D^b(\cA)^{\leq0}$ and $D_\cB^b(\cA)^{\geq0}=D_\cB^b(\cA) \cap D^b(\cA)^{\geq0}$.  The heart of the t-structure on 
$D_\cB^b(\cA)$ is $\cB$.  Moreover, if $\cC \subset \cB$ is another Serre subcategory then 
the $t$-structure on $D_\cB^b(\cA)$ is compatible with $D_\cC^b(\cA)$.  In particular, the quotient  $D_\cB^b(\cA)/D_\cC^b(\cA)$ inherits a natural t-structure whose heart is $\cB/\cC$.

For the remainder of this section let $\cA,\cA'$ be graded abelian categories.  In the setting of derived categories of graded abelian categories, a perverse equivalence can be packaged as follows.  We can encode a perversity triple $(\mathcal{A}_\bullet, \mathcal{A}'_\bullet, p)$ using filtrations on the abelian categories: $\cA_\bullet$ and $\cA'_\bullet$ are filtrations by shift-invariant Serre subcategories:
\begin{align*}
	0 = \mathcal{A}_{-1} \subset \mathcal{A}_0 \subset \mathcal{A}_1 \subset \hdots \subset \mathcal{A}_r=\mathcal{A}, \quad
	0 = \mathcal{A}'_{-1} \subset \mathcal{A}'_0 \subset \mathcal{A}'_1 \subset \hdots \subset \mathcal{A}'_r=\mathcal{A}'.
	\end{align*}
Then a graded equivalence $\sF:D^b(\mathcal{A}) \to D^b(\mathcal{A}')$ is a perverse with respect to $(\mathcal{A}_\bullet, \mathcal{A}'_\bullet, p)$ if conditions (1) and (2) of Definition \ref{def:PE} hold for $\cT_i=D^b_{\mathcal{A}_i}(\mathcal{A})$ and $\cT_i'=D^b_{\mathcal{A}'_i}(\mathcal{A}')$









 As above, a graded perverse equivalence $\sF:D^b(\mathcal{A}) \to D^b(\mathcal{A}')$ induces a bijection $\varphi_\sF:\Irr(\cA)\to\Irr(\cA')$.  
 
The following standard lemma will be useful in the proof of our main result.  

\begin{Lemma}\label{lem:trianginv}
Let $\cA,\cA'$ be abelian categories, and $\cB,\cB'$ Serre subcategories.  Let $a\leq b$ be integers, and $\sF_i:\cA \to \cA'$ be exact functors for $a \leq i \leq b$.  Suppose these functors  fit into a  complex $\sF=(\sF_a \to \sF_{a+1} \to \cdots \to \sF_{b} )$, defining a functor 
$$
\sF:D^b(\cA) \to D^b(\cA').
$$
If $\sF_i(\cB)\subset \cB'$ for all $a \leq i \leq b$, then $\sF(D_\cB^b(\cA))\subseteq D_{\cB'}^b(\cA')$.
\end{Lemma}
