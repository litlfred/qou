---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-006-31-naive-axiomatic-approach-to-higher-hochschild
section_title: "Naive axiomatic approach to higher Hochschild homology"
section_number: 3.1
pages: 10-15
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.987
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:NaiveHH label="S:NaiveHH"}

We first recall the standard construction of chain complexes computing higher Hochschild homology (also called Hochschild homology over spaces) following [@P; @GTZ]. The higher Hochschild complex is a functor $CH: sSet \times CDGA \to CDGA$. This functor is defined as follows: the tensor products $A\otimes B$ of two CDGAs has an natural structure of CDGA(in other words, $CDGA$ has a symmetric monoidal structure canonically induced by the underlying tensor product of chain complexes). Furthermore, the multiplication $A\otimes A\to A$ is an algebra homomorphism since $A$ is commutative. It follows that a $CDGA$ can be thought of a strict symmetric monoidal functor from the category of finite sets with disjoint union to the category of chain complexes (whose value on a finite set $J$ is given by $A^{\otimes J}$), which can be extended to the category of all sets by taking colimits. Given a simplicial set $X_{\scriptstyle\bullet}$, thought of as a functor $\Delta^{op} \to sSet$, compose these two functors to obtain a simplicial complex $X_{\scriptstyle\bullet}\mapsto A^{\otimes X_{\scriptstyle\bullet}}$. The total complex (that is the geometric realization $\big|A^{\otimes X_{\scriptstyle\bullet}}\big|$) of this simplicial complex is, by definition, $CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A,A)$. In more details, we get the following explicit definitions.

::: definition
[]{#D:Hoch label="D:Hoch"} First let $Y_{\scriptstyle\bullet}:\Delta^{op}\to \mathcal Sets_*$ be a finite pointed simplicial set, and for $k\geq 0$, we set $y_k:=Y_k -\{*\}$ to be the complement of the base point in $Y_k$. Furthermore, let $(A=\bigoplus_{i\in \mathbb Z} A^i, d, {\scriptstyle\bullet})$ be a differential graded, associative, commutative algebra, and $(M=\bigoplus_{i\in \mathbb Z}M^i,d_M)$ a differential graded module over $A$ (viewed as a symmetric bimodule). Then, the **Hochschild chain complex of $A$ with values in $M$ over $Y_{\scriptstyle\bullet}$** is defined as[^1] $CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,M):=\bigoplus_{n\in \mathbb Z} CH^n_{Y_{\scriptstyle\bullet}}(A,M)$, where $$CH^n_{Y_{\scriptstyle\bullet}}(A,M):=\bigoplus_{k\geq 0} (M\otimes A^{\otimes y_k})^{n+k}$$ is given by a sum of elements of total degree $n+k$. In order to define a differential $D$ on $CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$, we define morphisms $d_i:Y_k\to Y_{k-1}$, for $i=0,\dots,k$ as follows. First note that for any map $f:Y_k\to Y_l$ of pointed sets, and for $m\otimes a_1\otimes \dots\otimes a_{y_k}\in M\otimes A^{\otimes y_k}$, we denote by $f_*:M\otimes A^{\otimes y_k}\to M\otimes A^{\otimes y_l}$, $$\label{f_*}
 f_*(m\otimes a_1\otimes \dots\otimes a_{y_k})=(-1)^{\epsilon} n\otimes b_1\otimes \dots\otimes b_{y_l},$$ where $b_{j}=\prod_{i\in f^{-1}(j)} a_i$ (or $b_j=1$ if $f^{-1}(j)=\emptyset$) for $j=0,\dots,y_{l}$, and $n=m{\scriptstyle\bullet}\prod_{i\in f^{-1}(\text{basepoint}), i\neq \text{basepoint}}a_i$. The sign $\epsilon$ in equation [\[f\_\*\]](#f_*){reference-type="eqref" reference="f_*"} is determined by the usual Koszul sign rule of $(-1)^{|x|{\scriptstyle\bullet}|y|}$ whenever $x$ moves across $y$. In particular, there are induced boundaries $(d_i)_*:CH^k_{Y_{\scriptstyle\bullet}}(A,M)\to CH^{k-1}_{Y_{\scriptstyle\bullet}}(A,M)$ and degeneracies $(s_j)_*:CH^k_{Y_{\scriptstyle\bullet}}(A,M)\to CH^{k+1}_{Y_{\scriptstyle\bullet}}(A,M)$, which we denote by abuse of notation again by $d_i$ and $s_j$. Using these, the differential $D:CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,A)\to CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,A)$ is defined by letting $D(a_0\otimes a_1\otimes \dots\otimes a_{y_k})$ be equal to $$\sum_{i=0}^{y_k} (-1)^{k+\epsilon_i} a_0\otimes \dots\otimes d(a_i)\otimes \dots\otimes a_{y_k}+\sum_{i=0}^k (-1)^i d_i (a_0\otimes \dots\otimes a_{y_k}),$$ where $\epsilon_i$ is again given by the Koszul sign rule, *i.e.*, $(-1)^{\epsilon_i}=(-1)^{|a_0|+\cdots+|a_{i-1}|}$. The simplicial conditions on $d_i$ imply that $D^2=0$.

If $Y_{\scriptstyle\bullet}:\Delta^{op}\to \mathcal Sets$ is a finite (not necessarily pointed) simplicial set, we may still define $CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A):=\bigoplus_{n\in \mathbb Z} CH^n_{Y_{\scriptstyle\bullet}}(A,A)$ via the same formula as above, $CH^n_{Y_{\scriptstyle\bullet}}(A,A):=\bigoplus_{k\geq 0} (A\otimes A^{\otimes y_k})_{n+k}$. Formula [\[f\_\*\]](#f_*){reference-type="eqref" reference="f_*"} again induces boundaries $d_i$ and degeneracies $s_i$, which produce a differential $D$ of square zero on $CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,A)$ as above.

If $Y_{\scriptstyle\bullet}$ is any simplicial set we define $$CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M):=\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{\small \begin{array}{l}K_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}, \\ K_{\scriptstyle\bullet}\mbox{ finite} \end{array}} CH_{K_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$$ as the colimit over all finite simplicial sets. If $Y_{\scriptstyle\bullet}$ is finite, then this definition agrees with the previous ones thanks to the Yoneda lemma.
:::

::: remark
Note that due to our grading convention, if $A$ is non graded, or concentrated in degree 0, then $HH_{\scriptstyle\bullet}^{Y_{{\scriptstyle\bullet}}}(A,A)$ is concentrated in non positive degrees. In particular, our grading is opposite of the one in [@L].
:::

Note that the equation [\[f\_\*\]](#f_*){reference-type="eqref" reference="f_*"} also makes sense for any map of simplicial pointed sets $f:X_k\to Y_k$. Since $A$ is graded commutative and $M$ symmetric, $(f\circ g)_* =f_*\circ g_*$, hence $Y_{\scriptstyle\bullet}\mapsto CH^{\scriptstyle\bullet}_{Y_{\scriptstyle\bullet}}(A,M)$ is a functor from the category of finite pointed simplicial sets to the category of simplicial $k$-vector spaces, see [@P]. If $M=A$, $CH^{\scriptstyle\bullet}_{Y_{\scriptstyle\bullet}}(A)$ is a functor from the category of finite simplicial sets to the category of simplicial $k$-algebras.

Now note that any map $g:A\to B$ of CDGAs and any maps of modules $\rho:M\to N$ over $g:A\to B$, *i.e.* $\rho(am)=g(a)\rho(m)$, induces a map $CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(g,\rho): CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)\to CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B,N)$ of simplicial vector spaces.

The chain complex $\left(CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A), D\right)$ inherits a structure of (differential graded) algebra. This is a formal consequence of the fact that $CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ is a simplicial commutative algebra. Indeed, given two simplicial vector spaces $V_{\scriptstyle\bullet}$ and $W_{\scriptstyle\bullet}$, one defines a simplicial structure on the simplicial space $(V\times W)_k:=V_k\otimes W_k$ using the boundaries $d^V_i\otimes d^W_i$ and degeneracies $s^V_i\otimes s^W_i$. The *shuffle product* is (the collection of) maps $sh:V_p\otimes W_q\to (V\times W)_{p+q}$ defined by $$sh(v\otimes w)=\sum_{(\mu,\nu)} sgn(\mu,\nu) (s_{\nu_q}\dots s_{\nu_1}(v)\otimes s_{\mu_p}\dots s_{\mu_1}(w)),$$ where $(\mu,\nu)$ denotes a $(p,q)$-shuffle, *i.e.* a permutation of $\{0,\dots,p+q-1\}$ mapping $0\leq j\leq p-1$ to $\mu_{j+1}$ and $p\leq j\leq p+q-1$ to $\nu_{j-p+1}$, such that $\mu_1<\dots<\mu_p$ and $\nu_1<\dots<\nu_q$.

Since $CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,M)$ is a simplicial vector space, we obtain an induced shuffle map $sh:CH_{Y_p}^{{\scriptstyle\bullet}}(A,M)\otimes CH^{{\scriptstyle\bullet}}_{Y_q}(B,N) \to CH^{{\scriptstyle\bullet}}_{Y_{p+q}}(A\otimes B, M\otimes N)$ for any CDGAs $A,B$ and modules $M,N$. Now, since $A$ is a CDGA, the multiplication $\mu:A\otimes A\to A$ is an algebra map, and the map $\nu:M\otimes A\to M$ a map of $A$-modules. Composing these maps with the shuffle products we obtain the multiplication $$sh_{Y_{\scriptstyle\bullet}}:CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,M)\otimes CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A)\stackrel {sh} \to CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A\otimes A,M\otimes A)\stackrel {CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(\mu,\nu)} \longrightarrow  CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,M).$$

::: proposition
[]{#P:shuffleinvariance label="P:shuffleinvariance"} The multiplication $sh_{Y_{\scriptstyle\bullet}}$ makes $CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A)$ a differential graded commutative algebra and $CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$ a DG-module over $CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A)$, which are natural in $A$ and $M$.
:::

::: proof
*Proof.* The proof of the algebra structure is given in [@GTZ Proposition 2.4.2] and the proof of the module structure is the same. ◻
:::

Note that $CH_{\mathop{pt}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ is the (chain complex associated to the) constant simplicial CDGA $A$. In particular there is a canonical quasi-isomorphism $\eta: A=CH_{\mathop{pt}_0}^{{\scriptstyle\bullet}}(A)\to CH_{\mathop{pt}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ splitting the augmentation map $CH_{\mathop{pt}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\to CH_{\mathop{pt}_0}^{{\scriptstyle\bullet}}(A)$. It follows from Proposition [\[P:shuffleinvariance\]](#P:shuffleinvariance){reference-type="ref" reference="P:shuffleinvariance"} above that if $X_{\scriptstyle\bullet}$ is a pointed simplicial set, the canonical map $\mathop{pt}_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ induces a natural $A$-module structure on $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$ (and an $A$-algebra structure on $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$). In other words, $CH_{X_{\scriptstyle\bullet}}^{\scriptstyle\bullet}(A,M)$ is naturally an $A$-module.

Summing up the previous discussion and proposition we obtain:

::: corollary
[]{#C:Hfunctor label="C:Hfunctor"} The rule $(Y_{\scriptstyle\bullet}, A)\mapsto (CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A),D,sh_{Y_{\scriptstyle\bullet}})$ is a functor $CH:sSet\times CDGA\to CDGA$. Similarly, the rule $(Y_{\scriptstyle\bullet}, M)\mapsto (CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,M),D,sh_{Y_{\scriptstyle\bullet}})$ is a functor $CH:sSet_* \times A\textit{-}Mod \to A\textit{-}Mod$.
:::

::: definition
[]{#D:HH label="D:HH"} The Hochschild homology of a CDGA $A$ over a simplicial set $X_{\scriptstyle\bullet}$ is the cohomology[^2] $HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)=H^\bullet(CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A),D)$ of the CDGA $(CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A),D, sh)$ as a commutative graded algebra.

Further if $X_\bullet$ is pointed and $M$ is an $A$-module, the Hochschild homology of $A$ with value in $M$ over $X_{\scriptstyle\bullet}$ is the homology $HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)=H^*(CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M),D)$ as a graded module over $HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$.
:::

Now let $X$ be a *topological space*, we define the Hochschild homology of a $CDGA$ $A$ over $X$ to be $HH^{\scriptstyle\bullet}_{S_{\scriptstyle\bullet}(X)}(A)$ where $$S_{\scriptstyle\bullet}(X)=\mathop{Map}(\Delta^\bullet, X)$$ is the singular simplicial set of $X$. If $X$ is pointed, then $S_{\scriptstyle\bullet}(X)$ is a pointed simplicial set and we define the Hochschild homology of a $CDGA$ $A$ with value in an $A$-module $M$ over $X$ to be $HH^{\scriptstyle\bullet}_{S_{\scriptstyle\bullet}(X)}(A,M)$.

The Hochschild chain functor satisfies the following properties which allows to build *explicitly and easily* these chain complexes out of other simplicial sets and do computations (for instance, see [@P; @G; @GTZ]).

::: proposition
[]{#P:tensor label="P:tensor"}Let $A,B$ be two CDGAs. For any $X_{\scriptstyle\bullet}\in sSet$, there is a canonical isomorphism $$CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A\otimes B) \cong CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A)\otimes CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(B)$$ of CDGAs. Further for any simplicial set $Y_{\scriptstyle\bullet}$, one has a natural isomorphism $$CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}\coprod Y_{\scriptstyle\bullet}}(A) \cong CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A)\otimes CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A)$$ of CDGAs and a natural isomorphism of modules $$CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}\coprod Y_{\scriptstyle\bullet}}(A,M) \cong CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A,M)\otimes CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A)$$ if $X_{\scriptstyle\bullet}$ is a pointed simplicial set.
:::

::: proof
*Proof.* It follows from the canonical isomorphisms $(A\otimes B)^{\otimes n}\cong A^{\otimes n} \otimes B^{\otimes n}$ and $A^{\otimes n+m}\cong A^{\otimes n}\otimes A^{\otimes m}$. ◻
:::

Recall that, by functoriality, if $f:Y_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ is a map of simplicial sets, then for any CDGA $A$, we have a map of algebra $f_*:CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\to CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ which exhibits the Hochschild complex of $A$ over $X_{\scriptstyle\bullet}$ as a module over the Hochschild complex of $A$ over $Y_{\scriptstyle\bullet}$. Let $Z{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$, $Z_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ be two maps of simplicial sets and let $W_{\scriptstyle\bullet}$ be a pushout $W_{\scriptstyle\bullet}\cong X_{\scriptstyle\bullet}\coprod_{Z_{\scriptstyle\bullet}} Y_{\scriptstyle\bullet}$.

::: proposition
[]{#P:pushout label="P:pushout"} There is a natural map of simplicial modules [^3] $$CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)\otimes_{CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,A)} CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,A) \to CH_{W_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$$ which is a map of algebras if $M=A$ (with its natural module structure). If $Z_{\scriptstyle\bullet}$ injects into either $Z_{\scriptstyle\bullet}\stackrel {f_{\scriptstyle\bullet}}\to X_{\scriptstyle\bullet}$ or $Z_{\scriptstyle\bullet}\stackrel{g_{\scriptstyle\bullet}}\to Y_{\scriptstyle\bullet}$, then this map is in fact an isomorphism of $CH_{W_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$-modules.
:::

::: proof
*Proof.* The proof [@GTZ Lemma 2.1.6] given in the case $M=A$ applies to any module $M$. ◻
:::

::: corollary
[]{#C:Homologyfunctor label="C:Homologyfunctor"} The rule $(X_{\scriptstyle\bullet},A)\mapsto HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ is a functor $HH:sSet\times CDGA\to CGA$ which satisfies the following axioms

1.  **bimonoidal:** Hochschild homology is monoidal with respect to the monoidal structures given by the disjoint union of simplicial sets and tensor products of algebras. In other words, there are natural isomorphisms: $$HH_{X_{\scriptstyle\bullet}\times Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\cong HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}\!(A) \otimes HH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A), \; HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A\otimes B) \cong HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A) \otimes HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B).$$

2.  **homotopy invariance :** if $f:X_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ and $g:A\to B$ are (weak) homotopy equivalences, then $HH(f,g):HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\to HH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B)$ is an isomorphism.

3.  **point** There is a natural isomorphism $HH_{pt}^{{\scriptstyle\bullet}}(A)\cong A$

A similar statement holds with the category of topological spaces instead of simplicial sets, and with the pointed analogs of these categories (as in Corollary [\[C:Hfunctor\]](#C:Hfunctor){reference-type="ref" reference="C:Hfunctor"}).
:::

::: proof
*Proof.* This follows from Proposition [\[P:pushout\]](#P:pushout){reference-type="ref" reference="P:pushout"}, Proposition [\[P:tensor\]](#P:tensor){reference-type="ref" reference="P:tensor"}, Corollary [\[C:Hfunctor\]](#C:Hfunctor){reference-type="ref" reference="C:Hfunctor"} and Proposition [\[P:homologyinvariance\]](#P:homologyinvariance){reference-type="ref" reference="P:homologyinvariance"} below. ◻
:::

The axioms listed in the above proposition are *not* enough to uniquely determine Hochschild homology as a functor. Indeed, we are missing an analog of the Excision/Mayer-Vietoris axioms in the classical Eilenberg-Steenrod axioms for singular homology. The analog of this axiom is similar to the *locality axiom* of a Topological Field Theory. In view of Proposition [\[P:pushout\]](#P:pushout){reference-type="ref" reference="P:pushout"}, we wish to compute the Hochschild homology over an union of two open sets as the tensor product of the Hochschild homology of each open tensored over the Hochschild homology over their intersection. This forces us to take *derived* tensor products. Thus a better framework for an axiomatic description of Hochschild chains is given by considering derived categories or $(\infty,1)$-categories. We deal with this *locality* axiom in Section [\[S:inftyfunctor\]](#S:inftyfunctor){reference-type="ref" reference="S:inftyfunctor"} below. This axiom translates into an Eilenberg-Moore spectral sequence for Hochschild homology, see Corollary [\[C:HlocalitySpecSeq\]](#C:HlocalitySpecSeq){reference-type="ref" reference="C:HlocalitySpecSeq"}.

A crucial property of Hochschild chains which allows to pass to homotopy categories, is the fact, proved by Pirashvili [@P], that the higher Hochschild chain complex is invariant along *quasi-isomorphisms* in both arguments.

::: proposition
[]{#P:homologyinvariance label="P:homologyinvariance"}\[Homotopy and homology invariance\] If $f: X_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ is a map of simplicial sets inducing an isomorphism in homology $H_{\scriptstyle\bullet}(X)\stackrel{\simeq}\to H_{\scriptstyle\bullet}(Y)$ , then the map $CH_{X_{\scriptstyle\bullet}}^{\scriptstyle\bullet}(A, M) \to CH_{Y_{\scriptstyle\bullet}}^{\scriptstyle\bullet}(A, M)$ is a quasi-isomorphism.

Further if $h:A\to B$ is a quasi-isomorphism of CDGAs, then the induced map $h_{\scriptstyle\bullet}: CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\to CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B)$ is a quasi-isomorphism of CDGAs.

If $Z_{\scriptstyle\bullet}$ is a pointed simplicial set and $M$ is a $B$-module, the induced map $h_{\scriptstyle\bullet}: CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)\to CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B,M)$ is a quasi-isomorphism of $CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$-modules and if $\alpha: M\to N$ is a map of $B$-modules, the induced map $\alpha_{\scriptstyle\bullet}: CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B,M)\to CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B,N)$ is a quasi-isomorphism of $CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B)$-modules.
:::

::: proof
*Proof.* This is essentially due to Pirashvili [@P]. Indeed, let $\Gamma$ be the category of finite sets, then the Hochschild chain complex $CH_{X_{\scriptstyle\bullet}}^{\scriptstyle\bullet}(A)$ is isomorphic to the tensor product $$k_{X_{\scriptstyle\bullet}} \otimes_{\Gamma} \mathcal{L}(A)$$ of the left $\Gamma$-module $\mathcal{L}(A)$ and the simplicial right $\Gamma$-module $k_{X_{\scriptstyle\bullet}}$. Here the left $\Gamma$-module $\mathcal{L}(A)$ is defined by $n\mapsto A^{\otimes n+1}$ and formula [\[f\_\*\]](#f_*){reference-type="eqref" reference="f_*"}. The right $\Gamma$-module $k_{X_{\scriptstyle\bullet}}$ is defined by $n\mapsto \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{K_{\scriptstyle\bullet}\mbox{ finite}} k\big[Hom_{\Gamma}\big([n], K_{\scriptstyle\bullet}\big)]$ where $[n]$ is the finite set $\{0,\dots,n\}$, see [@P]. A quasi-isomorphism of CDGAs induces a quasi-isomorphism of left $\Gamma$-module and similarly for a quasi-isomorphism of simplicial sets. Since each right $\Gamma$-module $k_{X_m}$ ($m\in \mathbb N$) is a projective right $\Gamma$-module (see [@P]), the tensor product $k_{X_{\scriptstyle\bullet}} \otimes_{\Gamma} \mathcal{L}(A)$ is quasi-isomorphic to the derived tensor product $k_{X_{\scriptstyle\bullet}} \otimes^{\mathbb{L}}_{\Gamma} \mathcal{L}(A)$. It follows that this complex is invariant along quasi-isomorphisms in both arguments ($X_{\scriptstyle\bullet}$ and $A$). The proof in the case of pointed simplicial sets and modules is the same with the category $\Gamma$ replaced by the category of pointed finite sets. ◻
:::

[^1]: We recall that we are using a cohomological type grading for our differential graded modules, see Convention (7) on page , hence the upper index $n$. Note that, nowhere in this paper will we consider Hochschild cochains.

[^2]: Recall that we are using a cohomological type grading for our differential graded modules, see Convention (7) on page .

[^3]: The tensor product in Proposition [\[P:pushout\]](#P:pushout){reference-type="ref" reference="P:pushout"} is the tensor product of (simplicial) modules over the simplicial differential graded commutative algebra $CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,A)$. Passing to the Hochschild chain complexes, it induces a natural map of CDGAs and modules and yield a quasi-isomorphism if $Z_{\scriptstyle\bullet}$ injects into either $X_{\scriptstyle\bullet}$ or $Y_{\scriptstyle\bullet}$, see [@GTZ Corollary 2.4.3].
