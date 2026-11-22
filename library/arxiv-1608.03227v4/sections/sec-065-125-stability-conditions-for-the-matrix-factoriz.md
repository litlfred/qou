---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-065-125-stability-conditions-for-the-matrix-factoriz
section_title: "Stability conditions for the matrix factorizations."
section_number: 12.5
pages: 69-71
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
We denote by $$\SymbolPrint{V^0}\subset V=\CC^n$$ the subset of vectors with a non-zero last coordinate. Let us define $\SymbolPrint{\calX_{\ell,fr}}$ as the subvariety of $\calX_\ell\times V$ consisting of collections $(X,g_1,Y_1,,\dots,g_\ell,Y_\ell,u)$ such that $$\CC \langle \Ad_{g_i}^{-1}(X),Y_i\rangle g^{-1}_i(u)=V,\quad g^{-1}(u)\in V^0,\quad i=1,\dots,\ell-1,$$

The map that forgets framing $\SymbolPrint{\forg }:\calX_{\ell,fr}\to \calX_\ell$ is defined as restriction of the projection $\calX_\ell\times V\rightarrow \calX_\ell$ on the open subset $\calX_{\ell,fr}\subset\calX_\ell\times V$. It is dominant over the open that we call the stable locus $\calX_{\ell,st}$. There a unique $G\times B^\ell$-equivariant structure on $\calX_{\ell,fr,i}$ that makes map $\forg$ $G\times B^\ell$-equivariant.

The framed space comes equipped with the natural convolution algebra structure: $$\calF\SymbolPrint{\star} \calG:=\pi_{13*}(\CE_{\frn^{(2)}}(\pi_{12}^*(\calF)\otimes\pi_{23}^*(\calG))^{T^{(2)}}),$$ where $\pi_{ij}:\calX_{3,fr}\to \calX_{2,fr}$ are the natural projection maps. There is a natural pull back map $$\SymbolPrint{\forg}: \MF_{B^2}(\calX_2,W)\to \MF_{B^2}(\calX_{2,fr},W)$$ and the key to what follows in the next sections is the Lemma below:

::: lemma
[]{#lem: for homom label="lem: for homom"} The pull-back map $\forg^*$ is the homomorpism of the convolution algebras.
:::

::: proof
*Proof.* Let us denote by $\calC$ the matrix factorization $$\pi_{12}^*(\calF)\otimes\pi_{23}^*(\calG)\in\MF_{B^2}(\calX_{3,fr},\pi_{13}^*(W)).$$ Then what we need to show is that for any Zarisky open set $U\subset \calX_{2,fr}$ the matrix factorizations of $\CC[U]$-modules $\forg^*(\CE_{\frn^{(2)}}(\calC)^{T^{(2)}})$ and $\CE_{\frn^{(2)}}(\forg^*(\calC))^{T^{(2)}})$ are homotopic.

It is more convenient to restate the above homotopic relation in a slightly more geometric terms. Let us denote by $\calX_{3,fr,1}$ the subvariety of $\calX_3\times V$ that is defined by the stability condition: $$\CC\langle \Ad_{g_1}^{-1}(X), Y_1\rangle g_1^{-1}(u)=V,\quad g_1^{-1}(u)\in V^0$$ Both spaces $\calX_{3,fr,1}$ and $\calX_{3,fr}$ project onto $\calX_{2,fr}$ and to distinguish these projections we denote the projection from the first space by $\pi_{13}$ and from the second by $\pi_{13}^{fr}$. Thus the statement of the lemma is equivalent to the homotopy equivalence of the $\CC[U]$ matrix factorizations $$\label{eq: framed homotopy}
     \CE_{\frn^{(2)}}(\calC|_{\pi_{13}^{-1}(U)})^{T^{(2)}}\sim \CE_{\frn^{(2)}}(\calC|_{\pi^{fr,-1}_{13}(U)})^{T^{(2)}}.$$

From the previous discussion of the equations for the support of $\calC_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_l}^{\epsilon_l}}$ we see that $$\calX_3^{crit}\times V \cap\calX_{3,fr,1}=\calX_3^{crit}\times V \cap \calX_{3,fr}.$$ Finally since $Z=\calX_{3,fr,1}\setminus\calX_{3,fr}$ is the closed subvariety the equation ([\[eq: framed homotopy\]](#eq: framed homotopy){reference-type="ref" reference="eq: framed homotopy"}) follows from the general lemma that follows the proof: we use $X=\calX_{3,fr,1}$ and $Z'=\calX_3^{crit}\times V$ in the lemma. ◻
:::

Typically the stable locus is a open subset of some more natural bigger space and we are interesting in comparing the matrix factorizations on the big space with the ones on the stable locus. The lemma below shows that the category does not change as we pass to the stable locus as long the unstable locus does not intersect the critical locus of the potential. The lemma is shown in more general case and we do not refer to a stability a condition.

::: lemma
Suppose $X$ is a quasi-affine variety and $\calF=(M,D)\in \MFs(X,W)$, $W\in \CC[X]$. The elements of $\CC[X]$ act on $\MFs(X,W)$ by multiplication. Let us assume that the elements of the ideal $I=(f_1,\dots,f_m)\subset \CC[X]$ act by zero homotopies on $\calF$ and $Z'\subset X$ is the zero locus of $I$. Let $Z\subset X$ be a subvariety defined by $J=(g_1,\dots,g_n)$ such that $Z\cap Z'=\emptyset$. Then $\calF$ is homotopic to $\calF|_{X\setminus Z}$ as matrix factorization over $\CC[X]$.
:::

::: proof
*Proof.* Let us the convention $X_f$ for the open Zarisky subset of $X$ which is a complement of the zero locus of $f$. By the conditions of the lemma the open sets $X_{f_i}$ and $X_{g_i}$ form a Cech cover of $X$ and we denote by the $\check{C}_{f,g}(\calF)$ the Cech resolution of $\calF$. The terms of the complex $\check{C}_{f,g}(\calF)$ are the matrix factorizations $\calF|_{X_{S,T}}$ where $S\subset \{ 1,\dots, m\}$ and $T\subset \{ 1,\dots, n\}$ and $X_{S,T}$ is the complement to the zero locus of $\prod_{s\in S}f_s\prod_{t\in T} g_t$.

By the conditions of the lemma the matrix factorization $\calF|_{X_{S,T}}$ is contractible if $S\ne \emptyset$. Thus after performing all the contractions we are left with $\check{C}_{g}(\calF)$ which is exactly $\calF|_{X\setminus Z}$ and the lemma follows. ◻
:::

## Taking the $B^\ell$ quotient

Let us define the closure map: $\cl: \calX_{\ell-1}\rightarrow \calX_\ell$ by $$\SymbolPrint{\cl}(X,g_1,Y_1,\dots,g_{\ell-1},Y_{\ell-1}):=(X,g_1,Y_1,\dots,g_{\ell-1},Y_{\ell-1},g_1,Y_1).$$ This map is $G\times B^{\ell-1}$-equivariant with $B^{\ell-1}$-action on $\calX_{\ell-1}$ induced by the group homomorphism $\mathrm{id}_{2,\dots,\ell-1}\times \Delta_{1,\ell}$.

We use the same notation for the maps of the framed and stable spaces. Let us notice that the preimage of the map $\cl$ applied to $\calX_{\ell+1,fr}$ is the cyclicly framed space $\SymbolPrint{\calX_{\ell,fc}}$ that consists of points $(X,g_1,Y_1,\dots,g_\ell,Y_\ell,v)$ satisfying : $$\CC\langle\Ad_{g_i}^{-1}(X),Y_i\rangle g^{-1}(u)=V,\quad  g^{-1}(u)\in V^0, i=1,\dots,\ell.$$ The intersection with the zero-locus of $\mathcal{I}^{crit}_\ell$ we denote by $\calX_{\ell,fc}^{crit}$.

Respectively, we have the pull back map: $$\cl^*:\MF_{B^{\ell-1}}(\calX_{\ell,fr},W)\to \MF_{B^{\ell-1}}(\calX_{\ell-1,fc},0),$$ and let us denote by $C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_\ell^{\epsilon_\ell}}$ the pull-back $\cl^*(\calC_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_\ell^{\epsilon_\ell}})$. We use the same nation for $\cl^*(\calC_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_\ell^{\epsilon_\ell}})\in \MF_{B^{\ell-1}}(\calX_{\ell-1},0)$, usually it is clear from the context which category of matrix factorizations we work with.

Let us denote by $\SymbolPrint{\MFcrit_{B^\ell}}(\calX_{\ell,fc},0)\subset  \MF_{B^\ell}(\calX_{\ell,fc},0)$, $\MFcrit_{B^\ell}(\calX_{\ell},0)\subset  \MF_{B^\ell}(\calX_{\ell},0)$ the subcategory consisting of matrix factorizations with the property that the ideal $\calI^{crit}_\ell$ acts by zero homotopy. The element $C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{\ell+1}^{\epsilon_{\ell+1}}}$ is an element of the subcategory $\MFcrit_{B^\ell}(\calX_{\ell,fc},0)$.

Given an element $C\in \MFcrit_{B^\ell}(\calX_{\ell},0)$ the homology $$\cohog{*}{\CE_{\frn^\ell}(C)}:=\cohog{even}{\CE_{\frn^\ell}(C)}
\oplus\cohog{odd}{\CE_{\frn^\ell}(C)}$$ is a module over the ring of $\frn^\ell$ invariants $R_\ell^{\frn^\ell}$ where $R_\ell:=\CC[\calX_{\ell}^{crit}]$. Let us fix a notation for the affine scheme $\calX^{crit}_{\ell}/U^\ell:=\Spec(R_{\ell}^{\frn^\ell})$. We use notation $\mathcal{H}_U(\calX_{\ell},C)$ for $\cohog{*}{\CE_{\frn^\ell}(C)}$ considered as $R_\ell^{\frn^\ell}$-module.

There is an natural map $\forg: \calX^{crit}_{\ell,fc}\rightarrow\calX^{crit}_{\ell}$ and by applying the respective pull-back map we obtain $$\SymbolPrint{\mathcal{H}_U}(\calX_{\ell,fc},C):=\forg^*(\mathcal{H}_U(\calX_\ell, C))\in \MFs_{T^{\ell}}(\calX_{\ell,fc}/U^{\ell},0).$$

The complex of sheaves $\calH_U(\calX_{\ell,fc},C)$ is $T^\ell\times \hat{G}$-equivariant complex of sheaves on $\calX^{crit}_{\ell,fr}/U^\ell$ and we define $\SymbolPrint{\calH_B}(\calX_{\ell,fc},C)$ as a complex of sheaves of $T^\ell$-invariant sections of $\calH_U(\calX_{\ell,fc},C)$. Thus $\calH_B(\calX_{\ell,fc},C)$ is a complex of quasi-coherent sheaves on the quotient $\calX_{\ell,fc}/B^\ell$.

The complex of sheaves $\calH_{B}(\calX_{\ell,fc},C)$ is $\hat{G}$-equivariant hence the complex sheaves $\calH_{B}(\calX_{\ell,fc},C)^{\hat{G}}$ of $\hat{G}$-invariant sections of $\calH_{B}(\calX_{\ell,fc},C)$ is a complex of quasi coherent sheaves on $\St_\ell$.
