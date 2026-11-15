---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-009-4-factorization-algebras-and-derived-hochschild
section_title: "Factorization algebras and derived Hochschild functor over spaces"
section_number: 4
pages: 25-28
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.978
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:factor-alg label="S:factor-alg"} The main goal of this section is to prove that Hochschild chains are a special kind of *factorization algebras* in the sense of [@CG] (allowing to compute it using covers or CW-decomposition).

## The Hochschild $(\infty,1)$-functor in $\Top$

The Quillen equivalence between the model categories of simplicial sets and topological spaces induces an equivalence $\hTop \stackrel{S_\infty}\longrightarrow sSet_\infty$ of $(\infty,1)$-categories (Example [\[E:hsset\]](#E:hsset){reference-type="ref" reference="E:hsset"}). Here $S_\infty$ is the $(\infty,1)$-functor lifting the singular set functor $X\mapsto S_{\scriptstyle\bullet}(X)=\mathop{Map}(\Delta^\bullet, X)$. Recall that to any space $X$ we naturally associate the CDGA $CH^{\scriptstyle\bullet}_X(A) = CH^{\scriptstyle\bullet}_{S_\bullet(X)}(A)$, the Hochschild chains of $A$ over $X$. The canonical adjunction map $X_{\scriptstyle\bullet}\to S_{\scriptstyle\bullet}(|X_{\scriptstyle\bullet}|)$ yields a natural quasi-isomorphism $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\to CH_{|X_{\scriptstyle\bullet}|}^{{\scriptstyle\bullet}}(A)$ of CDGAs by Proposition [\[P:homologyinvariance\]](#P:homologyinvariance){reference-type="ref" reference="P:homologyinvariance"}.

From the above equivalence $\hTop \stackrel{\sim}\longrightarrow sSet_\infty$ (or alternatively by changing $sSet_\infty$ to $\hTop$ in all the proofs in Section [\[S:inftyfunctor\]](#S:inftyfunctor){reference-type="ref" reference="S:inftyfunctor"} and [\[SS:modules\]](#SS:modules){reference-type="ref" reference="SS:modules"}), we deduce the following topological counterpart to the results of Section [\[S:inftyfunctor\]](#S:inftyfunctor){reference-type="ref" reference="S:inftyfunctor"} and Section [\[SS:modules\]](#SS:modules){reference-type="ref" reference="SS:modules"}.

::: proposition
[]{#P:Topderived label="P:Topderived"}

-   The Hochschild chain over spaces functor $(X,A)\mapsto CH_X^{\scriptstyle\bullet}(A)$ lifts as an $(\infty,1)$-bifunctor $CH: \hTop\times CDGA_\infty\to CDGA_\infty$ fitting into the commutative diagram $${\small \xymatrix{ sSet_\infty\times CDGA_\infty\ar[rr]^{CH} & & CDGA_\infty\\
    \hTop\times CDGA_\infty\ar[u]^{S_\infty}_{\simeq} \ar[rru]_{CH} && }}$$ that satisfies all the axioms of Theorem [\[T:derivedfunctor\]](#T:derivedfunctor){reference-type="ref" reference="T:derivedfunctor"} (with $\hTop$ instead of $sSet_\infty$).

-   Further, up to natural equivalences of $(\infty,1)$-bifunctors, it is the only bifunctor $\hTop\times CDGA_\infty\to CDGA_\infty$ satisfying the axioms of Theorem [\[T:deriveduniqueness\]](#T:deriveduniqueness){reference-type="ref" reference="T:deriveduniqueness"} (with $\hTop$ instead of $sSet_\infty$).

-   Replacing $sSet_\infty$ by $\hTop$ and ${sSet_\infty}_*$ by ${\hTop}_*$, the analogs of Corollary [\[C:HlocalitySpecSeq\]](#C:HlocalitySpecSeq){reference-type="ref" reference="C:HlocalitySpecSeq"}, Proposition [\[P:product\]](#P:product){reference-type="ref" reference="P:product"}, Corollary [\[C:hocolim\]](#C:hocolim){reference-type="ref" reference="C:hocolim"}, Theorem [\[T:Mderivedfunctor\]](#T:Mderivedfunctor){reference-type="ref" reference="T:Mderivedfunctor"} and Corollary [\[C:MlocalitySpecSeq\]](#C:MlocalitySpecSeq){reference-type="ref" reference="C:MlocalitySpecSeq"} hold.
:::

The fact that Hochschild chains are computed by taking colimits over finite simplicial sets has the following translation for topological spaces.

::: proposition
Let $X$ be (weakly homotopic to) a $CW$-complex, $A$ a CDGA and $M$ an $A$-module. There are natural equivalences $$\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} K\to X\\ K\mbox{ compact}\end{array}}\!\! \!\!\!\!\! \Big(CH_{K}^{{\scriptstyle\bullet}}(A) \Big)\stackrel{\simeq} \longrightarrow CH_{X}^{{\scriptstyle\bullet}}(A) \;\; \text{ and } \;\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} K\to X\\ K\mbox{ compact}\end{array}}\!\!\!\!\!\!\! \Big( CH_{K}^{{\scriptstyle\bullet}}(A,M) \Big)\stackrel{\simeq} \longrightarrow CH_{X}^{{\scriptstyle\bullet}}(A,M)$$ in $CDGA_\infty$ and $CH_{X}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$ respectively.
:::

::: proof
*Proof.* Since $CH_{X}^{{\scriptstyle\bullet}}(A,M)\cong M\mathop{\otimes}^{\mathop{L}}_{A} CH_{X}^{{\scriptstyle\bullet}}(A)$ in $CH_{X}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$, we only need to prove that the first map is an equivalence.

We first assume $X$ to be a $CW$-complex of finite dimension $n$. Let $X_\bullet$ be a simplicial set model of $X$ with no non-degenerate simplices in dimension $m>n$. Then, given a finite simplicial set $K_{\scriptstyle\bullet}$, any map $f: K_\bullet \to X_\bullet$ factors through a finite simplicial set $\tilde{K}_\bullet$ with no non-degenerate simplices in dimension $m>n$. Thus, the realization $|\tilde{K}_\bullet|$ is compact. Conversely, if $\tilde{K}$ is a compact subset of the $CW$-complex $X$, it has a simplicial model $K_\bullet$ with finitely many non-degenerate simplices. Further, any map $K\to X$ has a compact image, since $X$ is Hausdorff, and thus factors through a compact subset of $X$. We get a zigzag $$\begin{gathered}
 \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} K\to X \\ K\mbox{ compact}\end{array}} CH^{\scriptstyle\bullet}_{K}(A) \stackrel{\simeq}\longleftarrow \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} \tilde{K}\subset X  \\ \tilde{K}\mbox{ compact}\end{array}} CH^{\scriptstyle\bullet}_{\tilde{K}} (A) \stackrel{\simeq}\longrightarrow \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize  \tilde{K}_\bullet \in \mbox{ FNDS}(X_\bullet) } CH^{\scriptstyle\bullet}_{\tilde{K}_\bullet}(A) \\
 \stackrel{\simeq}\longrightarrow \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} K\bullet \to X_\bullet \\ {K}_\bullet \mbox{ finite} \end{array}  } CH^{\scriptstyle\bullet}_{{K}_\bullet}(A)
 \stackrel{\simeq}\longrightarrow CH^{\scriptstyle\bullet}_{X_\bullet}(A)   \stackrel{\simeq}\longrightarrow  CH^{\scriptstyle\bullet}_{X}(A)
\end{gathered}$$ where the first and third arrows are equivalences since they are induced by cofinal functors. Here $FNDS(X_\bullet)$ is the set of simplicial subsets of $X_\bullet$ with finitely many non-degenerate simplices. That the other arrows in the zigzag are equivalences follows from Proposition [\[P:Topderived\]](#P:Topderived){reference-type="ref" reference="P:Topderived"} and thus the result is proved for finite dimensional $CW$-complexes.

We now reduce the general case to the finite dimensional one. Let $X_{\scriptstyle\bullet}$ be a simplicial set model of $X$. The geometric realization $|sk_n X_{\scriptstyle\bullet}|$ of $sk_nX_{\scriptstyle\bullet}$ is a finite dimensional $CW$-complex, and, if $K$ is compact, any map $f: K\to X$ factors as the composition $K\to |sk_n X_{\scriptstyle\bullet}| \hookrightarrow X$ for some $n$. Hence the natural map $$\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n} \Big(\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} \tilde{K}\to |sk_n X_{\scriptstyle\bullet}| \\ \tilde{K}\mbox{ compact}\end{array}} CH^{\scriptstyle\bullet}_{K}(A)\Big)  \quad\longrightarrow \quad  \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{ \scriptsize \begin{array}{l} K\to X \\ K\mbox{ compact}\end{array}} CH^{\scriptstyle\bullet}_{K}(A)$$ is a natural equivalence in $CDGA_\infty$. The result now follows from the finite dimensional case, the natural equivalence $\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n} CH_{sk_n X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A) \; \stackrel{\sim} \to CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ (see Remark [\[R:limskn\]](#R:limskn){reference-type="ref" reference="R:limskn"}), and Proposition [\[P:Topderived\]](#P:Topderived){reference-type="ref" reference="P:Topderived"}.i). ◻
:::

Specifying Corollary [\[C:hocolim\]](#C:hocolim){reference-type="ref" reference="C:hocolim"} to the case of topological spaces that are obtained by attaching cells, we get the following lemma.

::: lemma
[]{#L:CHhandling label="L:CHhandling"} Let $X_0$ be (weakly homotopic to) a $CW$-complex and $X$ be (weakly homotopic to) a $CW$-complex obtained from $X_0$ by attaching a countable family $(C_n)_{n\in \mathbb N}$ of cells. We let $X_n$ be the result of attaching the first $n$ cells. For any CDGA $A$, one has a natural equivalence $$\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n\in \mathbb N} CH_{X_n}^{{\scriptstyle\bullet}}(A) \stackrel{\simeq}\longrightarrow CH_{X}^{{\scriptstyle\bullet}}(A)$$ in $CDGA_\infty$, as well as $\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n\in \mathbb N} CH_{X_n}^{{\scriptstyle\bullet}}(A,M) \stackrel{\simeq}\longrightarrow CH_{X}^{{\scriptstyle\bullet}}(A)$ in $CH_{X}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$.
:::

::: proof
*Proof.* Since $CH_{X}^{{\scriptstyle\bullet}}(A,M)\cong M\mathop{\otimes}^{\mathop{L}}_{A} CH_{X}^{{\scriptstyle\bullet}}(A)$ as $CH_{X}^{{\scriptstyle\bullet}}(A)$-modules, we only need to consider the case of $CH_{X}^{{\scriptstyle\bullet}}(A)$. Further, the cells $C_i$ are homeomorphic to euclidean balls and the attaching maps have domain given by their boundaries. Thus we may assume that each $X_n$ is obtained from a simplicial set model $(X_0)_\bullet$ of $X_0$ by adding finitely many non-degenerates simplices. Thus we get a sequence of cofibrations of simplicial sets (*i.e.* degree wise injective maps) $(X_0)_\bullet \hookrightarrow (X_1)_\bullet \cdots \hookrightarrow (X_n)_\bullet \cdots \hookrightarrow X_\bullet=\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n\in \mathbb N} (X_n)_\bullet$ which are (homotopy) models for the sequence of maps $X_0\to X_1\to \cdots \to X$. By definition of Hochschild chains, there is a canonical equivalence $\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{\scriptsize \begin{array}{l} K_\bullet\to X_\bullet\\
K_\bullet\mbox{ finite}\end{array}} \!\!CH_{K_\bullet}^{{\scriptstyle\bullet}}(A) \cong CH_{X_\bullet}^{{\scriptstyle\bullet}}(A)$ of CDGAs. The maps $(X_n)_\bullet \to X_\bullet$ assemble to give a map of colimits $$\label{eq:CHhandling}
 \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n\in \mathbb N} \Big( \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{\scriptsize \begin{array}{l} K_\bullet\to (X_n)_\bullet\\
K_\bullet\mbox{ finite}\end{array}} \!\!CH_{K_\bullet}^{{\scriptstyle\bullet}}(A)\Big) \longrightarrow \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{\scriptsize \begin{array}{l} K_\bullet\to X_\bullet\\
K_\bullet\mbox{ finite}\end{array}} \!\!CH_{K_\bullet}^{{\scriptstyle\bullet}}(A) .$$ Given a finite set $K_i$ and a map $f_i: K_i\to X_i$, the image $f_i(K_i)$ lies in some $(X_n)_i$ since $X_\bullet=\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{n\in \mathbb N} (X_n)_\bullet$ and $f_i(K_i)$ is finite. This proves that the family $K_\bullet \to (X_n)_\bullet$ of maps from a pointed set into some $(X_n)_\bullet$ is cofinal and thus the map [\[eq:CHhandling\]](#eq:CHhandling){reference-type="eqref" reference="eq:CHhandling"} is an equivalence in $CDGA_\infty$. ◻
:::

::: remark
It is possible to enhance the result of Lemma [\[L:CHhandling\]](#L:CHhandling){reference-type="ref" reference="L:CHhandling"} in the following way. One can take any space $X_\emptyset$ and a space $X$ obtained by attaching a family $(C_i)_{i\in I}$ of other spaces to it. Then, essentially the same argument as the one in Lemma [\[L:CHhandling\]](#L:CHhandling){reference-type="ref" reference="L:CHhandling"} shows that $CH^{\scriptstyle\bullet}_{X}(A)$ is the colimit $\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits CH^{\scriptstyle\bullet}_{X_F}(A)$ over all possible subspaces $X_F\subset X$ obtained by attaching finitely many $C_i$'s.
:::

Let us conclude this section by giving an analog of Leray acyclic cover theorem/Mayer Vietoris principle for Hochschild chains.

Let $X$ be a topological space and $\mathcal{U} =(U_i)_{i\in I}$ be a *good cover* for $X$, *i.e.* a cover such that the $U_i$ and all of their nonempty finite intersections are contractible. We denote $N_{\scriptstyle\bullet}(I)$ the nerve of the cover, that is $N_0(I)=I$, $N_1(I)$ is the set of pairs of indices $i_0,i_1$ such that $U_{i_0}\cap U_{i_1} \neq \emptyset$ and so on.

::: corollary
Let $X$ be a topological space and $\mathcal{U} =(U_i)_{i\in I}$ be a *good cover* for $X$ such that the inclusions $U_i\cap U_j \to U_i$ are cofibrations. Then there is a natural equivalence $$CH^{\scriptstyle\bullet}_{X}(A)\stackrel{\simeq}\longrightarrow  A^{\otimes I} \mathop{\otimes}\limits_{A^{\otimes N_1(I)}}^{\mathbb{L}} A^{\otimes I}$$ in $CDGA_\infty$. Here the left and right module structure are induced by the two canonical projections $N_1(I)\to N_0(I)=I$ given by $(i,j)\mapsto i$, $(i,j)\mapsto j$.
:::

::: proof
*Proof.* Since each $U_i$ is contractible, the natural map $CH_{U_i}^{{\scriptstyle\bullet}}(A) \to CH_{pt}^{{\scriptstyle\bullet}}(A)\cong A$ is an equivalence by Theorem [\[T:derivedfunctor\]](#T:derivedfunctor){reference-type="ref" reference="T:derivedfunctor"} and similarly (when $U_i\cap U_j$ is not empty) for the natural map $CH_{U_i\cap U_j}^{{\scriptstyle\bullet}}(A)\to A$ because $\mathcal{U}$ is a good cover. Since $X$ is the coequalizer $\coprod_{N_1(I)} U_i\cap U_j \rightrightarrows \coprod_{I} U_i \rightarrow X$, the result follows from the coproduct axiom (2) and the gluing axiom (3) in Theorem [\[T:derivedfunctor\]](#T:derivedfunctor){reference-type="ref" reference="T:derivedfunctor"} (or Proposition [\[P:Topderived\]](#P:Topderived){reference-type="ref" reference="P:Topderived"}). ◻
:::
