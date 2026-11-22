---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-014-51-factorization-homology-with-coefficients-in-c
section_title: "Factorization homology with coefficients in commutative algebras"
section_number: 5.1
pages: 28-31
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.973
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
We begin by examining commutative algebras in $\mathcal V$, otherwise known as $\mathcal E_\infty$-algebras in $\mathcal V$. Note first that a commutative algebra in $\mathcal V$ is equivalent to a symmetric monoidal functor ${\sf Fin}\rightarrow\mathcal V$ from finite sets with disjoint union. So restriction along the connected components functor $[-]: \mathop{\mathrm{{\mathcal D}\sf isk}}^B_n\rightarrow\mathop{\mathrm{{\mathcal D}\sf isk}}_n \xrightarrow{[-]} {\sf Fin}$ defines a forgetful functor $${\sf fgt}\colon \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)\longrightarrow \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n}(\mathcal V)~.$$ We have the following consequence of $\otimes$-excision, where $\mathcal V$ is a symmetric monoidal $\infty$-category which is $\otimes$-presentable. To phrase this result we utilize that the $\infty$-category $\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)$ is tensored over spaces: $$\mathop{\mathrm{\mathsf{Spaces}}}\times \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V) \xrightarrow{\otimes} \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)~,\qquad (X,A)\mapsto \mathop{\mathrm{\sf colim}}\bigl(X\to \ast \xrightarrow{\{A\}} \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)\bigr)~.$$

::: prop
[]{#tensor label="tensor"} The following diagram among $\infty$-categories commutes: $$\xymatrix{
\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_n \times \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V) \ar[r]^-{U\times {\sf id}}\ar[d]^-{{\sf id}\times {\rm fgt}} 
& 
\mathop{\mathrm{\sf Spaces}}\times \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)\ar[r]^-\otimes&\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)\ar[d]
\\
\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_n \times\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n}(\mathcal V)\ar[rr]_\int &&\mathcal V
}$$ where $U$ is the underlying space functor and the right downward arrow is the standard forgetful functor. In particular, there is a natural equivalence $$\int_M A~\simeq~ M\otimes A$$ between the factorization homology of $M$ with coefficients in $A$ and the tensor of the commutative algebra $A$ with the underlying space of $M$.
:::

::: proof
*Proof.* The functor $-\otimes A\colon \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B \to \mathcal V$ carries each contractible manifold to the underlying object of the commutative algebra $A$. For $(A_i)_{i\in I}$ a finite sequence of commutative algebras in $\mathcal V$, the $I$-fold coproduct in $\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\mathsf{Com}}}}(\mathcal V)$ is the pointwise tensor product $\underset{i\in I} \bigotimes A_i$ (see Proposition 3.2.4.7 of [@dag]). It follows that this functor $-\otimes A$ is symmetric monoidal. From the defining expression of factorization homology as a colimit, there results a natural transformation $$\int_- A \longrightarrow -\otimes A$$ between symmetric monoidal functors $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B\to \mathcal V$, which evaluates as an equivalence on objects of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B$. Lemma [\[excision\]](#excision){reference-type="ref" reference="excision"} grants that the domain of this natural transformation satisfies $\otimes$-excision. Because a collar-gluing $M'\underset{M_0\times \mathbb R}\bigcup M'' \cong M$ determines a pushout of underlying spaces $M'\underset{M_0}\coprod M'' \simeq M$, the codomain of this natural transformation too satisfies $\otimes$-excision. That the natural transformation evaluates on each $B$-framed $n$-manifold $M$ as an equivalence then follows by induction on a handle decomposition on $M$. ◻
:::

In other words, the factorization homology $\int_M A$ has a natural structure of a commutative algebra when $A$ is commutative, and this commutative algebra has a universal property: for each commutative algebra $C$ in $\mathcal V$ there is a natural equivalence from the space of commutative algebra maps $$\mathop{\mathrm{\sf Map}}_{\mathop{\mathrm{\mathsf{Com}}}}\bigl(\int_MA,C\bigr)~\simeq ~\mathop{\mathrm{\sf Map}}_{\mathop{\mathrm{\mathsf{Com}}}}(A,C)^M~,$$ to the space of maps from $M$ to the space of commutative algebra maps. By formal properties of left adjoints and tensors, this has the immediate corollary.

::: cor
For each symmetric monoidal $\infty$-category $\mathcal V$ which is $\otimes$-presentable, there is a natural equivalence in $\mathcal V$: $$\int_M \mathop{\mathrm{\sf Sym}}(V) ~\simeq ~\mathop{\mathrm{\sf Sym}}(M\otimes V)~.$$
:::

In particular, if $\mathcal V$ is the $\infty$-category of chain complexes with tensor product, then there is an equivalence $\int_M\mathop{\mathrm{\sf Sym}}(V) \simeq \mathop{\mathrm{\sf Sym}}(\mathsf C_\ast(M,V))$ for each chain complex $V$. We now push the above result slightly further for the two special classes of commutative algebras arising from the cohomology of spaces and the cohomology of Lie algebras. The study of the latter has benefitted greatly from conversations with Kevin Costello and Dennis Gaitsgory, and a full development of these ideas will amount to a forthcoming work.

::: prop
[]{#prop.5.3 label="prop.5.3"} Let $M$ be an $n$-manifold, and let $X$ be a nilpotent $n$-connective space of finite type over $R$ such that $\pi_nX$ is finite. There is a natural equivalence of chain complexes $$\int_M \mathsf C^\ast(X, R)~ \simeq~ \mathsf C^\ast(X^M,R)$$ between the factorization homology of $M$ with coefficient in the $R$-cohomology of $X$ and the $R$-cohomology of the space of maps from $M$ to $X$.
:::

::: proof
*Proof.* The two sides are evidently equivalent in the case where $M$ is homeomorphic to $\mathbb R^n$, so to establish the result it suffices, as usual, to check by induction over a handle decomposition of $M$. Given a handle decomposition $N\underset{S^{k}\times\mathbb R^{n-k}}\bigcup\mathbb R^n\cong M$, we have a homotopy pullback diagram of spaces $$\label{nilpotent-square}
\xymatrix{
X^M\ar[r]\ar[d]&\ar[d] X^{\mathbb R^n}\\
X^{N}\ar[r]&X^{S^{k}\times\mathbb R^{n-k}}\\}$$ which gives rise to a natural map in $R$-homology $$\mathsf C_\ast(X^{M},R)\longrightarrow \mathsf C_\ast(X^{N},R)\underset{\mathsf C_\ast(X^{S^k\times\mathbb R^{n-k}},R)}\bigotimes\mathsf C_\ast(X^{\mathbb R^n},R)$$ from the homology of the mapping spaces to the cotensor product of the comodules $\mathsf C_\ast(X^{N},R)$ and $\mathsf C_\ast(X^{\mathbb R^n},R)$ over the coalgebra $\mathsf C_\ast(X^{S^k\times\mathbb R^{n-k}},R)$. This map is an equivalence exactly if the homological Eilenberg--Moore, or Rothenberg--Steenrod, spectral sequence for this homotopy Cartesian diagram converges. By Dwyer [@dwyer], the convergence of this Eilenberg--Moore spectral sequence is assured if the base $X^{S^k\times\mathbb R^{n-k}}$ is connected and the action $$\pi_1 \bigl(X^{S^k\times\mathbb R^{n-k}}, f\bigr)
\circlearrowright
\pi_\ast\bigl({\sf fiber}_f(X^{\mathbb R^n}\rightarrow X^{S^k\times\mathbb R^{n-k}})\bigr)$$ is nilpotent for a choice of basepoint $f \in X^{S^k\times\mathbb R^{n-k}}$. Since $X$ is $n$-connective, for $k<n$ any map $f:  S^k \rightarrow X$ is nullhomotopic, and therefore the base $X^{S^k\times\mathbb R^{n-k}} \simeq X^{S^k}$ is connected. We can thus take $f$ to be the constant map valued at the basepoint of $X$, and so identify ${\sf fiber}_f(X^{\mathbb R^n}\rightarrow X^{S^k\times\mathbb R^{n-k}}) \simeq \Omega^{k+1}X$. We now show the action of $\pi_1 \bigl(X^{S^k}\bigr)$ on $\pi_\ast \Omega^{k+1} X$ is nilpotent. Consider the fiber sequence $\Omega^{k+1} X \to X^{S^k} \xrightarrow{{\sf ev}_\ast} X$. This fibration admits a section, given by the constant maps. Consequently, there is an identification as a semi-direct product: $$\pi_1\bigl(X^{S^k}\bigr)
\cong
\pi_1X \ltimes\pi_1\Omega^k X
\cong
\pi_1X \ltimes\pi_0 \Omega^{k+1} X
~.$$ Through this identification, the action of $\pi_1 \bigl(X^{S^k}\bigr)$ on $\pi_\ast \Omega^{k+1} X$ is the unique action that extends the standard actions of $\pi_1X$ and of $\pi_0 \Omega^{k+1}X$ on $\pi_\ast \Omega^{k+1}X$. By assumption, the action of $\pi_1X$ on $\pi_{\ast+k+1}X \cong \pi_\ast \Omega^{k+1} X$ is nilpotent. In the case that $k=0$, the same assumption grants that the action of $\pi_0 \Omega^{k+1} X$ on $\pi_\ast \Omega^{k+1}X$ is nilpotent. In the case that $k>0$, the action of $\pi_0 \Omega^{k+1} X$ on $\pi_\ast \Omega^{k+1}X$ is automatically nilpotent due to commutativity. Nilpotence of the action of $\pi_1 \bigl(X^{S^k}\bigr)$ on $\pi_\ast \Omega^{k+1} X$ follows. Consequently, the natural map in $R$-homology above is an equivalence.

The remainder of this argument is checking that we have imposed sufficient finiteness conditions to ensure the convergence in cohomology as well as homology. Dualizing, we obtain an equivalence $$\Bigl(\mathsf C_\ast(X^{N},R)\underset{\mathsf C_\ast(X^{S^k\times\mathbb R^{n-k}},R)}\bigotimes\mathsf C_\ast(X^{\mathbb R^n},R)\Bigr)^\vee \overset{\sim}\longrightarrow \mathsf C^\ast(X^{M},R)~.$$ Since $\pi_nX$ is finite, the mapping space $X^K$ has finitely many components for any $n$-dimensional finite CW complex $K$. Because the source spaces, $M$, $N$, $S^k\times\mathbb R^{n-k}$, and $\mathbb R^n$, all have have the homotopy types of finite $n$-dimensional CW complexes, we obtain that all these mapping spaces have finitely many components. Since they are additionally finite CW complexes and $X$ is finite type, the homology groups of the mapping spaces $\mathsf H_i(X^K,R)$ are finite rank over $R$, and therefore $\mathsf C_*(X^K,R)$ is its own double dual: the map $\mathsf C_*(X^K,R)\rightarrow\mathsf C^*(X^K,R)^\vee$ is an equivalence. Likewise, there is an equivalence between the dual of the tensor product and the cotensor product $$\Bigl( \mathsf C^\ast(X^{N},R)\underset{\mathsf C^\ast(X^{S^k\times\mathbb R^{n-k}},R)}\bigotimes\mathsf C^\ast(X^{\mathbb R^n},R)\Bigr)^\vee \simeq \mathsf C_\ast(X^{N},R)\underset{\mathsf C_\ast(X^{S^k\times\mathbb R^{n-k}},R)}\bigotimes\mathsf C_\ast(X^{\mathbb R^n},R)\simeq \mathsf C_\ast(X^M,R)$$ -- this can be seen by commuting duality with the colimit to obtain a limit of a cosimplicial object, then comparing termwise. Continuing, one then concludes the equivalence $$\mathsf C^\ast(X^M,R) \simeq \mathsf C^\ast(X^N,R)\underset{\mathsf C^\ast(X^{S^k\times\mathbb R^{n-k}},R)}\bigotimes \mathsf C^\ast(X^{\mathbb R^n},R)~,$$ thereby finishing the proof. ◻
:::

::: remark
See [@gtz1] for a closely related approach to the study of mapping spaces, in which one approaches the cohomology of a mapping space as a Hochschild homology-type invariant of the cohomology of the target.
:::
