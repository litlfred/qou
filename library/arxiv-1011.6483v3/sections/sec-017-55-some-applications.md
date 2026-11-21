---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-017-55-some-applications
section_title: "Some applications"
section_number: 5.5
pages: 55-59
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.98
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#SS:applications label="SS:applications"}

### Another construction of topological chiral homology for framed manifolds

Let $M$ be an $m$-dimensional manifold which is $n$-framed. Given an $E_n$-algebra $A$, we can define the topological chiral homology $\int_M A$ of $M$ with values in $A$. By Proposition [\[P:TCHisFact\]](#P:TCHisFact){reference-type="ref" reference="P:TCHisFact"} and Theorem [\[T:HF=TCH\]](#T:HF=TCH){reference-type="ref" reference="T:HF=TCH"}, $\int_M A$ is the factorization homology of a factorization algebra on $M\times D^{n-m}$. We explain how to construct this factorization algebra directly.

Since $M$ is $n$-framed, there is a bundle isomorphism $\varphi: T(M\times D^{n-m}) \stackrel{\simeq}\longrightarrow \underline{\mathbb R^n}$ where $\underline{\mathbb R^n}$ is a trivial bundle over $M\times D^{n-m}$. Choosing a Riemannian metric on $M\times D^{n-m}$, we have, using the spray associated to the exponential map, canonical diffeomorphisms of (a basis of) open neighborhoods of any $x\in M\times D^{n-m}$ to open sets in the tangent space $T(M\times D^{n-m})_x$ of $M\times D^{n-m}$ at $x$. Composing with the map $\varphi$ induced by the framing, we get diffeomorphisms $U\mapsto \psi(U_x)\in Op(\mathbb R^n)$ where $U$ is a (geodesically convex) open neighborhood of $x$.

Let $\mathcal{U}$ be the cover of $M\times D^{n-m}$ obtained by considering the $U$ above such that $\phi_x(U_x)\in \mathcal{B}\mathit{all}(\mathbb R^n)$ is an euclidean ball. The cover $\mathcal{U}$ is a factorizing basis of open subsets of $M\times D^{n-m}$.

To any $U\in \mathcal{U}$, we associate $\mathcal{A}(U)=A$, a (fixed) $E_n$-algebra. We wish to extend $\mathcal{A}$ into a factorization algebra. Since $A$ is an $E_n$-algebra, it defines a locally constant factorization algebra on $\mathbb R^n$ (see [@Co; @L-VI] and Proposition [\[P:Fac=En\]](#P:Fac=En){reference-type="ref" reference="P:Fac=En"}), which we, by abuse of notation, again denote by $A$. For any pairwise disjoint $U_1, \cdots, U_n \in \mathcal{U}$, and $V \in \mathcal{U}$ such that $U_i \subset V$ ($i=1\cdots n$), we define the structure maps $\mu_{U_1,\dots, U_n, V}$ (see Section [\[S:Factorization\]](#S:Factorization){reference-type="ref" reference="S:Factorization"}) by the following commutative diagram: $$\xymatrix{ \mathcal{A}({U_1})  \otimes \cdots \otimes \mathcal{A}({U_n}) \ar[d]_{\simeq} \ar[rr]^{\qquad \quad \mu_{U_1,\dots, U_n,V}}  & & \mathcal{A}({V})  \ar[d]^{\simeq}\\ A(\psi(U_1))\otimes \cdots \otimes A(\psi(U_n)) \ar[rr]_{} & & A(\psi(V))}$$ where the lower arrow is given by the $E_n$-algebra structure of $A$. This yields a $\mathcal{U}$-factorization algebra (in the sense of [@CG] and § [\[S:Factorization\]](#S:Factorization){reference-type="ref" reference="S:Factorization"}) since $A$ is a factorization algebra on $\mathbb R^n$ and $M\times D^{n-m}$ is framed. By [@CG Section 3], we can now extend $\mathcal{A}$ to a factorization algebra on $M\times D^{n-m}$.

::: corollary
[]{#C:FactforframedTCH label="C:FactforframedTCH"} There is an equivalence of $E_{n-m}$-algebras $$\int_M A \; \cong \; HF(M,\mathcal{A}).$$
:::

::: proof
*Proof.* For any ball $U$, we have a natural equivalence $\int_U A \cong A \cong \mathcal{A}(U)$. Now the result follows from Theorem [\[T:HF=TCH\]](#T:HF=TCH){reference-type="ref" reference="T:HF=TCH"} (and its proof) after taking global sections. ◻
:::

Note that topological chiral homology $\mathcal{TC}_M(A)$ is independent of the Riemannian metric, hence the factorization algebra $\mathcal{A}\in \mathop{Fac}_{M\times D^{n-m}}^{lc}(k\textit{-}Mod_\infty)$ on $M$ thus obtained is also independent of the Riemannian metric.

### Interpretation of topological chiral and higher Hochschild in terms of mapping spaces

As we have already noticed, higher Hochschild chains behave much like mapping spaces (and thus so do $\int_M A$ for CDGAs $A$). Indeed,

::: corollary
Let $A=\Omega^\ast N$ be the de Rham forms on a $d$-connected manifold (with its usual differential). Then for any manifold $M$ of dimension $m\leq d$, there is a natural quasi-isomorphism $\int_M A \cong \Omega^\ast (N^M)$, the space of (Chen) de Rham forms of the mapping space $N^M= \mathop{Map} (M,N)$.
:::

In other words, topological chiral homology of $M$ with value in $\Omega^\ast N$ calculates the mapping space $N^M$ (if $N$ is sufficiently connected).

::: proof
*Proof.* By Theorem [\[T:TCH=CH\]](#T:TCH=CH){reference-type="ref" reference="T:TCH=CH"}, we are left to a similar statement for $CH_{M}(\Omega^\ast N)$. Since $M$ is $m$-dimensional it has a simplicial model with no non-degenerate simplices in dimensions above $m$. Now the result follows from [@GTZ Proposition 2.5.3 and Proposition 2.4.6]. ◻
:::

::: remark
By [@GTZ Section 2.4], there is a canonical map $\int_M \Omega^\ast N \to \Omega^\ast (N^M)$. Further, it is possible to replace $N$ by any nilpotent space (by mimicking the proof of [@GTZ Propositions 2.5.3 and 2.4.6]) and $\Omega^\ast N$ by a Sullivan model of $N$.
:::

We now give a (derived/homotopical) algebraic geometry statement. Recall that $k$ denotes a field of characteristic zero and let $\mathbf{dSt}_k$ be the (model) category of *derived stacks* over $k$ described in details in [@ToVe Section 2.2] (which is a derived enhancement of the category of stacks over $k$). This category admits internal Hom's that we denote by $\mathbb{R}\mathop{Map}(\mathfrak{X},\mathfrak{Y})$ following [@ToVe; @ToVe2]. To any simplicial set $X_{\scriptstyle\bullet}$, we associate the constant simplicial presheaf $k\textit{-}Alg \to sSet$ defined by $R\mapsto X_{\scriptstyle\bullet}$ and we denote $\mathfrak{X}$ the associated stack. For a (derived) stack $\mathfrak{Y}$, we denote $\mathcal{O}_{\mathfrak{Y}}$ its functions [@ToVe] (*i.e.*, $\mathcal{O}_{\mathfrak{Y}}:=\mathbb{R}\underline{Hom}(\mathfrak{Y},\mathbb{A}^1)$).

::: corollary
[]{#C:mappingstack label="C:mappingstack"} Let $\mathfrak{R}=\mathbb{R}\mathop{Spec}(R)$ be an affine derived stack (for instance an affine stack) [@ToVe]. Then the Hochschild chains over $X_{\scriptstyle\bullet}$ with coefficient in $R$ represent the mapping stack $\mathbb{R}\mathop{Map}(\mathfrak{X}, \mathfrak{R})$. That is, $$\mathcal{O}_{\mathbb{R}\mathop{Map}(\mathfrak{X},\mathfrak{R})}\; \cong \; CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(R).$$
:::

::: proof
*Proof.* The bifunctor $(\mathfrak{X},\mathbb{R}\mathop{Spec}(R))\mapsto \mathbb{R}\mathop{Map}(\mathfrak{X}, \mathbb{R}\mathop{Spec}(R))$ is contravariant in $\mathfrak{X}$ and $R \in CDGA^{\leq 0}$. Thus, $\mathcal{O}_{\mathbb{R}\mathop{Map}(\mathfrak{X},\mathfrak{R})}$ defines a covariant bifunctor. Since $\mathbb{R}\mathop{Map}(-,\mathfrak{R})$ sends (homotopy) limits to (homotopy) colimits, it follows from Theorem [\[T:deriveduniqueness\]](#T:deriveduniqueness){reference-type="ref" reference="T:deriveduniqueness"} (also see Remark [\[R:cdga-\]](#R:cdga-){reference-type="ref" reference="R:cdga-"}) that $\mathcal{O}_{\mathbb{R}\mathop{Map}(\mathfrak{X},\mathfrak{R})}$ is equivalent to $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(R)$. ◻
:::

::: example
Let $B_{\scriptstyle\bullet}\mathbb{Z}$ be the nerve of $\mathbb{Z}$ and $\mathfrak{B}\mathbb{Z}$ its associated stack. Recall that there is an homotopy equivalence $S^1\to |B_{\scriptstyle\bullet}\mathbb{Z}|$ (actually induced by a simplicial set map, see [@L]). From Corollary [\[C:mappingstack\]](#C:mappingstack){reference-type="ref" reference="C:mappingstack"} we recover that the derived loop stack $L\mathfrak{R}:=\mathbb{R}\mathop{Map}(\mathfrak{B}\mathbb{Z},\mathfrak{R})$ is represented by $CH_{B_{\scriptstyle\bullet}\mathbb{Z}}^{{\scriptstyle\bullet}}(R) \stackrel{\simeq}\longleftarrow CH_{S^1_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(R)$ the standard Hochschild chain complex of $R$ as was proved in [@ToVe2]. Similarly, the derived torus mapping stack $\mathbb{R}\mathop{Map}(\mathfrak{B}\mathbb{Z}\times \mathfrak{B}\mathbb{Z},\mathfrak{R})$ is represented by $CH_{S^1\times S^1}^{\scriptstyle\bullet}(R)$ and the secondary cyclic homology in the sense of [@ToVe2] is represented by the homotopy fixed points $CH_{S^1\times S^1}^{\scriptstyle\bullet}(R)^{h (S^1\times S^1)}$ with respect to the induced action of the simplicial group $B_{\scriptstyle\bullet}\mathbb{Z}\times B_{\scriptstyle\bullet}\mathbb{Z}$ on the derived mapping space.
:::

::: remark
Sheafifying (or rather stackifying) the higher Hochschild derived functor, it seems possible to extend Corollary [\[C:mappingstack\]](#C:mappingstack){reference-type="ref" reference="C:mappingstack"} to general derived schemes.
:::

### Topological chiral Homology and homology spheres

Topological chiral homology of CDGAs is a homology invariant, and thus, in particular, a homotopy invariant. Indeed, we have the following corollary.

::: corollary
Let $f:M \to N$ be smooth map between two manifolds inducing isomorphisms on homology and $A$ be a CDGA, then $\int_M A\cong \int_N  A$.
:::

::: proof
*Proof.* This follows from Theorem [\[T:TCH=CH\]](#T:TCH=CH){reference-type="ref" reference="T:TCH=CH"} and the quasi-isomorphism invariance of $CH_{(-)}^{{\scriptstyle\bullet}}(A)$ (Proposition [\[P:homologyinvariance\]](#P:homologyinvariance){reference-type="ref" reference="P:homologyinvariance"}). ◻
:::

::: example
The composition $S^3 \to SO(3) \to SO(3)/I$, where $I$ is the icosahedral group, induces an isomorphism on homology. To see this note that the fundamental group of $SO(3)/I$ is the binary icosahedral group $\tilde{I}$ which is a perfect group and therefore $H_1(SO(3)/I)=0$. The result $SO(3)/I$ is the Poincaré homology sphere and has thus the same topological chiral homology with value in any CDGA as $S^3$.
:::

::: remark
Note that we study topological chiral homology in the framework of chain complexes, *i.e.* we have fixed the $(\infty,1)$-category of chain complexes as our ''ground'' monoidal $(\infty,1)$-category. If one works in some other framework (such as topological spaces), one can expect to have more refined invariants.
:::

::: remark
Note that $S^1$ has two diffeomorphic $1$-framings (specified by a choice of orientation). This accounts for the fact that classically there is only one Hochschild complex for associative algebras. There are countably many $2$-framings for the circle, one for each integer, giving rise to equivalent topological chiral homologies when the integrand is a CDGA. It would therefore be meaningful to look for an explicit $E_2$-algebra that distinguishes these framings from one another, if such exists. Similarly, it would be interesting to find an explicit $E_3$-algebra that distinguishes the two $3$-framings of $S^1$.
:::

### Fubini formula for topological chiral homology

The exponential law for Hochschild chains (Proposition [\[P:product\]](#P:product){reference-type="ref" reference="P:product"}) has an analogue for topological chiral homology.

::: corollary
[]{#C:FubiniTCH label="C:FubiniTCH"} Let $M$, $N$ be manifolds and $\mathcal{A}$ be an $\mathbb{E}_d[M\times N]$-algebra. Then, $\int_N\mathcal{A}$ has a canonical lift as an $\mathbb{E}_d[M]$-algebra and further, there is an equivalence of $E_d$-algebras $$\int_{M\times N} \mathcal{A} \; \cong \; \int_M\Big(\int_N \mathcal{A}\Big).$$
:::

::: proof
*Proof.* Replacing $M$ by $M\times \mathbb{R}^d$ and using Lemma [\[L:EnFact\]](#L:EnFact){reference-type="ref" reference="L:EnFact"}, it is enough to prove the result for $d=0$. Since the homology of a factorization algebra on $X$ is given by the pushforward along the canonical map $p:X\to pt$, by Theorem [\[T:HF=TCH\]](#T:HF=TCH){reference-type="ref" reference="T:HF=TCH"}, one has $$\label{eq:FubiniTCH}\int_{M\times N}\mathcal{A}
 \cong p_*\big( \mathcal{TC}_{M\times N}(\mathcal{A})\big) 
\cong p_*\big(\pi_*\big(\mathcal{TC}_{M\times N}(\mathcal{A}) \big)\big)$$ where $\pi:M\times N\to M$ is the canonical projection. Since $\mathcal{TC}_{M\times N}(\mathcal{A})$ is locally constant, $\pi_*\big(\mathcal{TC}_{M\times N}(\mathcal{A})$ is also locally constant whose value on an open ball $D\subset M$ is given by $\pi_*\big(\mathcal{TC}_{M\times N}(\mathcal{A})(U) \cong \mathcal{TC}_{M\times N}(\mathcal{A})(U\times N)
\cong \int_N \mathcal{A}$. This defines the canonical $\mathbb{E}_d[M]$-algebra structure on $\int_N \mathcal{A}$ and the result now follows from the equivalence [\[eq:FubiniTCH\]](#eq:FubiniTCH){reference-type="eqref" reference="eq:FubiniTCH"}. ◻
:::

::: example
Let $M$, $N$ be $m+k$-framed and $n+\ell$-framed manifolds of respective dimension $m$, $n$ and $A$ be an ${E}_{n+k+m+\ell}$-algebra. Then, the product $M\times N$ is canonically $m+n+k+\ell$-framed and $A$ is an $\mathbb{E}_{k+\ell}$-algebra. Then, Corollary [\[C:FubiniTCH\]](#C:FubiniTCH){reference-type="ref" reference="C:FubiniTCH"} yields an equivalence of $E_{k+\ell}$-algebras: $$\int_{M\times N} A \; \cong \; \int_{M} \Big(\int_{N} A\Big).$$ In particular, if $A$ is a CDGA, then Corollary [\[C:FubiniTCH\]](#C:FubiniTCH){reference-type="ref" reference="C:FubiniTCH"} reduces to the exponential law for Hochschild chains (Proposition [\[P:product\]](#P:product){reference-type="ref" reference="P:product"}) under the equivalence between topological chiral homology and derived Hochschild chains (Theorem [\[T:TCH=CH\]](#T:TCH=CH){reference-type="ref" reference="T:TCH=CH"}).
:::
