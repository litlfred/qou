---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-031-2-bundles
section_title: "2-Bundles"
section_number: null
pages: 37-39
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.937
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#2bundles label="2bundles"}

Let ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module. Let the associated differential crossed module be ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$. Fix a smooth manifold $M$ and a smooth principal $G$-bundle $\pi\colon P \to M$.

A natural weakening of the notion of a categorical connection $(\w,m)$ in $P$ is to consider $m$ to be only locally defined on $P$, but so that $\d(m_i)=\W$, for any $i$. Here $m_i \in \A^2(P_i,\le)$, where $P_i=\pi^{-1}(U_i)$ and $\{U_i\}$ is an open cover of $P$. This can be done by using the general theory of 2-bundles [@BS], or non-abelian gerbes [@BrMe], which correspond to 2-bundles with structure crossed modules of the form $G=\rm{Aut}(E)$ of example [\[q\]](#q){reference-type="ref" reference="q"}.

To this end, let $\{U_i\}$ be an open cover of $M$. We can suppose that, for any $i_1,\ldots ,i_n$, the $n$-fold intersection $U_{i_1,\ldots ,i_n}\doteq U_{i_1} \cap \ldots \cap U_{i_n}$ is contractible. A $\Gc$-2-bundle can be described by using smooth maps $g_{ij}\colon U_{ij} \to G$ and $h_{ijk}\colon U_{ijk} \to E.$ These have to satisfy the cocycle conditions: $\d(h_{ijk}^{-1})g_{ij}g_{jk}=g_{ik}$ and $h_{ijk}h_{ikl}=\left (g_{ij}\tr h_{jkl}\right)h_{ijl}$ for any $i,j,k,l$. Therefore a $\Gc$-2-bundle does not necessarily define a $G$-principal bundle, unless $\d(h_{ijk})=1$ for each $i,j,k$. If this condition is satisfied, a $\Gc$-2-bundle will be called a *special $\Gc$-2-bundle.*

The main purpose of this article was the construction of categorical holonomies, in other words of smooth categorical group maps $\Pc_2(M,*) \to \C(\Gc)$, or, equivalently of smooth crossed module maps $\Pi_2^{2,1}(M,*)\to \Gc$; see [\[thinfund\]](#thinfund){reference-type="ref" reference="thinfund"} for this notation. From the point of view of 2-dimensional holonomy, $\Gc$-2-bundles are natural objects; see [@BS]. However, our notion of categorical holonomy requires the existence of a smooth group morphism $\pi^1_1(M,*) \to G$, and therefore of a principal $G$-bundle with connection; see [@CP]. This makes it natural to work with special $\Gc$-2-bundles.

A special $\Gc$-2-bundle with connection can be specified by the following data: (Here $A=\ker (\d) \subset E$, and $\la$ is its Lie algebra; note that $A$ is central in $E$).

1.  A principal $G$-bundle $\pi\colon P \to M$ with a connection $\w$.

2.  An open cover $\{U_i\}$ of $M$ such that for any $i_1,\ldots ,i_n$ the $n$-fold intersection $U_{i_1,\ldots ,i_n}$ is contractible. Let $P_{i_1,\ldots ,i_n}=\pi^{-1}(U_{i_1,\ldots ,i_n})$.

3.  $G$-equivariant $A$-valued functions $e_{ijk}\colon P_{ijk} \to A$. These are required to satisfy: $e_{ijk}e_{ikl}= e_{jkl} e_{ijl}$.

4.  $G$-equivariant horizontal 2-forms $m_i\in  \A^2(P_i,\le)$. These are required to satisfy $\d(m_i)=\W$, the curvature 2-form of $\w$.

5.  $G$-equivariant horizontal 1-forms $\eta_{ij} \in \A^1(P_{ij},\la)$. These are required to satisfy: $$m_i-m_j=D \eta_{ij} \quad \textrm{ and }\quad  \left(De_{ijk}^{-1}\right) e_{ijk}=\eta_{ij}+\eta_{jk}-\eta_{ik},$$ where $D$ denotes the exterior covariant derivative with respect to $\w$, in other words, by using lemma [\[ext\]](#ext){reference-type="ref" reference="ext"}, $$m_i-m_j=d \eta_{ij} +\w \wedge^\tr \eta_{ij} \quad \textrm{ and }\quad  \left(d e_{ijk}^{-1}+\w \wedge^\tr e_{ijk}^{-1}\right) e_{ijk}=\eta_{ij}+\eta_{jk}-\eta_{ik}.$$

One passes from this setting to the setting in [@BS] by choosing local sections $f_i$ of $P_i$, and defining the functions $g_{ij}\colon U_{ij} \to G$ in the usual way: $f_ig_{ij}=f_j.$ Next define $h_{ijk}=f_i^*(e_{ijk})$, $A_i=f_i^*(\w)$, $B_i=f_i^*(m_i)$ and $a_{ij}=f_i^*(\eta_{ij})$. Then this data defines the local differential forms of Baez and Schreiber [@BS], satisfying equations corresponding to our special $\Gc$-2-bundles with connection, in particular with the transition functions $g_{ij}$ satisfying the usual cocycle condition for a principal $G$-bundle. Note that the Baez-Schreiber local differential forms can be seen as a generalisation to arbitrary $\Gc$ of the local description of non-abelian gerbes, with $G=\rm{Aut}(E)$, of Breen and Messing [@BrMe].

Special $\Gc$-2-bundles with connection define group morphisms $\pi_1^1(M,*) \to G$. However, the definition of the categorical holonomy on a 2-track $[\G]\in \P_2(M,*)$ is tricky if one is to deal with the fact that $m$ is not globally defined. This can be done (and will appear in a future work), however, it will only be, a priori, defined up to multiplication by central elements of $E$, and thus it should not define holonomies $\Pc_2(M,*) \to \C(\Gc)$, unless we restrict to elements of $\pi_2^2(M,*)$, as in [@MP]. For instance, it is easy to see that given two categorical $\Gc$-connections $(\w,m)$ and $(\w,m')$ in $P$ then given a $2$-path $\G\in \Pc_2(M,*)$ we have $${e_\G'=\exp  
\Big (
\int_{0}^{1} \eta 
\left (\t{\frac{d}{d t}\g_1(t)} \right)
_{{\mathcal{H}}_\w(\g_1,t,u) }  dt 
 \Big)\exp  
\Big (-
\int_{0}^{1} \eta 
\left (\t{\frac{d}{d t}\g_2(t)} \right)
_{{\mathcal{H}}_\w(\g_2,t,u) }  dt 
 \Big) e_\G}$$ where $m-m'=D \eta=d \eta+\w \wedge^\tr \eta$, moreover $\eta\in \A^1(P,\la)$ is $G$-equivariant and horizontal. We have put $\g_1=\d_u(\G)$ and $\g_2=\d_d(\G)$. Also $e_\G$ and $e_\G'$ denote 2-dimensional holonomy with respect to $(\w,m)$ and $(\w,m')$, respectively.

For this reason we feel that it is likely that the construction in this article, with a globally defined $m$, will describe all categorical holonomies $\Pc_2(M,*) \to \C(\Gc)$, especially if we consider a generalised unbased setting. We will investigate this issue in a future publication.
