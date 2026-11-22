---
doc_id: arxiv-2508.03145v1
doc_title: "Θ -Categories and Tannakian duality"
section_id: sec-006-the-tannakian-duality-theorem
section_title: "The Tannakian duality theorem"
section_number: null
pages: 23-29
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.972
doc_brief: "Θ -Categories and Tannakian duality — We introduce a notion of Θ-categories, which is a refinement of the notion of symmetric monoidal ∞-categories."
---
We start by investigating the morphism $\beta$.

::: thm
[]{#t1 label="t1"} Let $T^\Theta$ be a neutralized Tannakian $\Theta$-category over $k$. Then the following hold.

1.  The unit morphism of $\Theta$-categories $\beta_{T^\Theta}\colon T^\Theta \to \mathsf{QCoh}^{\mathrm{LSym}}(\mathsf{Fib}^{\mathrm{LSym}}_*(T^\Theta))$ induces an equivalence of symmetric monoidal $\infty$-categories $$T \simeq \widehat{\mathsf{Perf}}(\mathsf{Fib}^{\mathrm{LSym}}_*(T^\Theta)).$$

2.  The stack $\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)$ is a pointed Tannakian gerbe.
:::

The proof of Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} relies on the following property of the fiber functor of a neutralized Tannakian $\Theta$-category.

::: lem
[]{#l-2-2 label="l-2-2"} Let $T^\Theta$ be a neutralized Tannakian $\Theta$-category over $k$. Then there is an equivalence of $\Theta$-categories under $T^{\Theta}$ $$\xymatrix{
& T^{\Theta}\ar[ld]_-{\omega}\ar[rd]^-{\hspace{5pt}\omega_*(\mathbf{1})\otimes -}\\
\mathsf{QCoh}(k)\ar[rr]^-{\omega_*}_-\sim & & \omega_*(\mathbf{1})\text{-}\mathsf{Mod}(T^{\Theta}).
}$$
:::

::: proof
*Proof.* It suffices to verify that $\omega \colon T^\Theta \to \mathsf{QCoh}^{\mathrm{LSym}}(k)$ satisfies the conditions of Proposition [\[p1-3\]](#p1-3){reference-type="ref" reference="p1-3"}. As dualizable objects are preserved by symmetric monoidal $\infty$-functors, $\omega$ preserves compact objects by condition (T1). Since $T$ is stable by Lemma [\[l-2-1\]](#l-2-1){reference-type="ref" reference="l-2-1"}, this implies that its right adjoint $\omega_* \colon \mathsf{QCoh}(k) \to T$ preserves colimits, so in particular geometric realizations. Condition $(2)$ of Proposition [\[p1-3\]](#p1-3){reference-type="ref" reference="p1-3"} is obvious when $x$ is a dualizable object, because we have for any $z \in T$ $$\begin{aligned}
\mathbf{Map}_{T}(z,x \otimes \omega_*(y)) &\simeq \mathbf{Map}_{T}(z\otimes x^\vee,\omega_*(y)) \simeq 
\mathbf{Map}_T(\omega(z) \otimes \omega(x)^\vee,y)\\
&\simeq\mathbf{Map}_T(\omega(z),\omega(x)\otimes y) \simeq \mathbf{Map}_T(z,\omega_*(\omega(x)\otimes y)).
\end{aligned}$$ The general case follows by writing $x$ as a colimit of compact and thus dualizable objects. ◻
:::

::: proof
*Proof of Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"}.* Let us start by describing the stack $\mathsf{Fib}^{\mathrm{LSym}}_*(T^\theta)\simeq B\underline{aut}^\Theta(\omega)$ in more detail. Let us write $$B := \omega_*(\mathbf{1})\in \Theta\text{-}\mathsf{CAlg}(T^{\Theta})$$ and let $B^*\colon \Delta_+^{op}\to \Theta\text{-}\mathsf{CAlg}(T^{\Theta})$ be the augmented cosimplicial diagram given by the co-nerve of the map $\mathbf{1}\to B$ (so $B^{-1}=\mathbf{1}$ and $B^0=B$). We obtain an augmented cosimplicial diagram of $\Theta$-categories $$B^*\text{-}\mathsf{Mod}(T^{\Theta}) \in T^{\Theta}/\infty\text{-}\mathbf{Cat}_{pr}^\Theta$$ By Proposition [\[p1-2\]](#p1-2){reference-type="ref" reference="p1-2"}, the co-Segal maps exhibit each $B^n\text{-}\mathsf{Mod}(T^{\Theta})$ as the $(n+1)$-fold coproduct of $B\text{-}\mathsf{Mod}(T^{\Theta})$ in $T^{\Theta}/\infty\text{-}\mathbf{Cat}_{pr}^\Theta$. It follows that the simplicial diagram of stacks of $\Theta$-fiber functors $$G_*:=\mathsf{Fib}^{\mathrm{LSym}}(B^*\text{-}\mathsf{Mod}(T^{\Theta}))$$ is equivalent to the nerve of the map $\mathsf{Fib}^{\mathrm{LSym}}(B\text{-}\mathsf{Mod}(T^{\Theta}))\to \mathsf{Fib}^{\mathrm{LSym}}(T^{\Theta})$. By Lemma [\[l-2-2\]](#l-2-2){reference-type="ref" reference="l-2-2"}, this is equivalent to the nerve of the basepoint $x\colon \ast\to \mathsf{Fib}^{\mathrm{LSym}}(T^{\Theta})$ corresponding to $\omega$. Consequently, we obtain an equivalence of group stacks $$\underline{aut}^\Theta(\omega)\simeq \mathsf{Fib}^{\mathrm{LSym}}\big(B^{\otimes 2}\text{-}\mathsf{Mod}(T^{\Theta})\big)=: G$$ where the group structure on $G$ is encoded by the simplicial diagram $G_*$ (in particular, $G_n\simeq G^{\times n}$ via the Segal maps). The stack $G$ can be identified more explicitly as follows.

::: lem
[]{#l-2-3 label="l-2-3"} Let $T^\Theta$ be a neutralized Tannakian $\Theta$-category over $k$. Then the stack of $\Theta$-self-automorphisms of its fiber functor $\omega$ is an affine stack, given by $$\underline{aut}^\Theta(\omega) \simeq \mathbf{Spec}\, \omega(B).$$ In addition, the $\mathrm{LSym}$-algebra $\omega(B)$ has positive tor-dimension.
:::

::: proof
*Proof of Lemma [\[l-2-3\]](#l-2-3){reference-type="ref" reference="l-2-3"}.* Let $\omega_*(\mathbf{1})\otimes B\to\omega_*(\omega(B))$ be the natural map of $\mathrm{LSym}$-algebras adjoint to the map $\omega(\omega_*(\mathbf{1}))\otimes \omega(B)\to \mathbf{1}\otimes \omega(B)$. This is an equivalence by the projection formula. Lemma [\[l-2-2\]](#l-2-2){reference-type="ref" reference="l-2-2"} therefore gives an equivalence $$B^{\otimes 2}\text{-}\mathsf{Mod}(T^{\Theta})\simeq \omega(B)\text{-}\mathsf{Mod}(\mathsf{QCoh}(k)).$$ We now note that the stack of $\Theta$-fiber functors of $\omega(B)\text{-}\mathsf{Mod}(\mathsf{QCoh}(k))$ is equivalent to $\mathbf{Spec}\, \omega(B)$ by Proposition [\[p1-2\]](#p1-2){reference-type="ref" reference="p1-2"}.

To see that $\omega(B)$ has positive tor-dimension, let $E$ be a coconnective complex of $k$-modules. Then the projection formula shows that $$E \otimes \omega(B)\simeq \omega(\omega_*(E))$$ remains coconnective, since $\omega$ is t-exact and $\omega_*$ is (hence) left t-exact. ◻
:::

All in all, we see that $\mathsf{Fib}_*^{\mathrm{LSym}}(T^{\Theta})\simeq BG$ where $G=\mathbf{Spec}\, \omega(B)$ is the group stack whose group structure is encoded by the simplicial diagram $G_*$.\
Let us now prove (1). The unit map fits into a natural transformation of augmented cosimplicial $\Theta$-categories $$\xymatrix@C=1.5pc{
T^\Theta\ar[r]\ar[d]_-{\beta_{T^\Theta}} & 
B\text{-}\mathsf{Mod}(T^{\Theta})\ar@<3pt>[r]\ar@<-3pt>[r]\ar[d]^-{\beta_0} &
B^{\otimes 2}\text{-}\mathsf{Mod}(T^{\Theta})\ar[r]\ar@<6pt>[r]\ar@<-6pt>[r]\ar[d]^-{\beta_1}  &
\dots\\
\mathsf{QCoh}^{\mathrm{LSym}}(BG)\ar[r] &
 \mathsf{QCoh}^{\mathrm{LSym}}(k) \ar@<1ex>[r]\ar@<-1ex>[r] &
 \mathsf{QCoh}^{\mathrm{LSym}}(G) \ar[r]\ar@<6pt>[r]\ar@<-6pt>[r] &
  \dots
}$$ The bottom row is a limit diagram by definition. For the top row, note that $B$ has positive tor-dimension because (by Lemma [\[l-2-3\]](#l-2-3){reference-type="ref" reference="l-2-3"}) $\omega(B)$ has positive tor-dimension and $\omega$ is $t$-exact and conservative. In addition, $B\otimes -\colon T\to B\text{-}\mathsf{Mod}(T)$ is conservative, since it is equivalent to $\omega$ by Lemma [\[l-2-2\]](#l-2-2){reference-type="ref" reference="l-2-2"}. An abstract version of flat descent, for which we refer to Proposition [\[pa\]](#pa){reference-type="ref" reference="pa"}, therefore shows that the top row restricts to an equivalence on eventually coconnective objects $$T^{>-\infty} \simeq \lim_{n\in \Delta}\big(B^*\text{-}\mathsf{Mod}(T^{>-\infty})\big).$$

Since dualizable objects in $T$ are bounded for the $t$-structure, we therefore obtain a diagram of symmetric monoidal $\infty$-categories of dualizable objects $$\xymatrix@C=1.5pc{
T^{rig}\ar[r]\ar[d]_-{\beta_{T^\Theta}} & B\text{-}\mathsf{Mod}(T)^{rig}\ar@<3pt>[r]\ar@<-3pt>[r]\ar[d]^-{\beta_0} & B^{\otimes 2}\text{-}\mathsf{Mod}(T)^{rig}\ar[r]\ar@<6pt>[r]\ar@<-6pt>[r]\ar[d]^-{\beta_1} & \dots\\
\mathsf{Perf}(BG)\ar[r] & \mathsf{Perf}(k) \ar@<1ex>[r]\ar@<-1ex>[r] & \mathsf{Perf}(G) \ar[r]\ar@<6pt>[r]\ar@<-6pt>[r] & \dots
}$$ in which both the top and bottom row are limit diagrams.

For each $n\geq 0$, the functor $\beta_n\colon B^{\otimes 1+n}\text{-}\mathsf{Mod}(T)\longrightarrow \mathsf{QCoh}(G^{\times n})$ can be identified as follows. By the same projection formula argument as in the proof of Lemma [\[l-2-3\]](#l-2-3){reference-type="ref" reference="l-2-3"}, there is a symmetric monoidal equivalence $$B^{\otimes 1+n}\text{-}\mathsf{Mod}(T)\simeq \omega(B)^{\otimes n}\text{-}\mathsf{Mod}.$$ By construction, this equivalence identifies $\beta_n$ with the canonical symmetric monoidal left adjoint $\infty$-functor $$\mathcal{O}\otimes_{\omega(B)^{\otimes n}} -\colon \omega(B)^{\otimes n}\text{-}\mathsf{Mod}\longrightarrow \mathsf{QCoh}(G^{\times n}) \simeq \mathsf{QCoh}(\mathbf{Spec}\, \omega(B)^{\otimes n})$$ coming from the canonical equivalence, as an $E_\infty$-algebra, between $\omega(B)^{\otimes n}$ and the endomorphisms of the unit $\mathcal{O}\in \mathsf{QCoh}(\mathbf{Spec}\, \omega(B)^{\otimes n})$. Using that the right adjoint to the above functor takes global sections, one readily sees that the restriction to dualizable objects $\omega(B)^{\otimes n}\text{-}\mathsf{Mod}^{rig} \to \mathsf{Perf}(G^{\times n})$ is fully faithful.

We conclude that each $\beta_n\colon B^{\otimes n}\text{-}\mathsf{Mod}(T)^{rig}\to \mathsf{QCoh}(G^{\times n})$ is fully faithful. In addition, $\beta_0$ is evidently an equivalence. It follows that the induced functor on limits $$\beta_{T^\Theta} \colon T^{rig}\xrightarrow{\simeq} \mathsf{Perf}(BG)$$ is an equivalence as well. Since $T$ is rigid by (T1), it then follows that $\beta_{T^\Theta}$ induces a symmetric monoidal $\infty$-categories $T\simeq \widehat{\mathsf{Perf}}(BG)$, proving (1).

We now turn to point (2). Condition (G1) for being a Tannakian gerbe is satisfied because $\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)$ is pointed and connected by definition. Condition (G3) holds by Lemma [\[l-2-3\]](#l-2-3){reference-type="ref" reference="l-2-3"} and condition (G4) holds by point (1). It remains to prove that (G2) is also satisfied. For any other stack $G$, the inclusion $\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta) \subset \mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)$ induces a full embedding on mapping spaces $$\mathbf{Map}_{\mathbf{St}_k}(G,\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)) \subset \mathbf{Map}_{\mathbf{St}_k}(G,\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)).$$ If $G$ is furthermore pointed and connected this inclusion fits into a cartesian square $$\xymatrix{
\mathbf{Map}_{\mathbf{St}_k}(G,\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)) \ar[r] \ar[d] &  \mathbf{Map}_{\mathbf{St}_k}(G,\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)) \ar[d] \\
B\underline{aut}^{\Theta}(\omega)(k) \ar[r] &
\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)(k),
}$$ where bottom horizontal morphism is the inclusion of the connected component containing the global point $\omega \in \mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)(k)$. By the definition of the stack $\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)$, the mapping space on the top right corner identifies canonically $$\mathbf{Map}_{\mathbf{St}_k}(G,\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)) \simeq \mathbf{Map}_{k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T^\Theta,\mathsf{QCoh}^{\mathrm{LSym}}(G)).$$ As a result, we see that if $f \colon G_1 \to G_2$ is a morphism between pointed and connected stacks, such that $f^* \colon \mathsf{QCoh}(G_2) \to \mathsf{QCoh}(G_1)$ is an equivalence, then the induced morphism on mapping spaces $$f^* \colon \mathbf{Map}_{\mathbf{St}_k}(G_2,\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)) \longrightarrow 
\mathbf{Map}_{\mathbf{St}_k}(G_1,\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta))$$ is an equivalence as required, showing that $\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)$ is always pointed $Q$-local. ◻
:::

The following corollary gathers the important conclusion of the Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"}, which states the existence of Tannakian duals for Tannakian $\Theta$-categories.

::: cor
[]{#ct1 label="ct1"} Let $T^\Theta$ be a neutralized Tannakian $\Theta$-category over $k$. Then there exists an affine group stack $G=\mathbf{Spec}\, C$, with $C$ a $k$-linear $LSym$-algebra of positive tor-dimension, and an equivalence of symmetric monoidal $\infty$-categories $$\beta : T \simeq \widehat{\mathsf{Perf}}(BG).$$
:::

::: rmk
[]{#r1 label="r1"} The reader will notice that in the proof of Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} we have a commutative diagram of symmetric monoidal $\infty$-categories $$\xymatrix{
T \ar[dr] \ar[r]^-{\simeq}& \widehat{\mathsf{Perf}}(\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)) \ar[d] \\
 & \mathsf{QCoh}(\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta))
}$$ where the top horizontal $\infty$-functor is an equivalence. Moreover, each of the two other $\infty$-functors possesses a natural lift to a morphism of $\Theta$-categories. However, we have not been able to prove that the equivalence $T\simeq \widehat{\mathsf{Perf}}(\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta))$ can be enhanced to an equivalence of $\Theta$-categories. This is due to our choice of definition of $\Theta$-category, which is probably not optimal (see also Remark [\[r2\]](#r2){reference-type="ref" reference="r2"}).
:::

The next corollary investigates the other direction of Tannakian duality, and the morphism $\alpha$. We recall that we have introduced the notion of $Q$-local stacks in the definition of Tannakian gerbes (condition (G2)). It has a refined version called $P$-local, which already naturally appears in the setting of schematic homotopy theory of [@chaff]. A pointed and connected stack $F$ is said to be *pointed $P$-local* if for any morphism of pointed and connected stacks $u \colon G_1 \to G_2$ such that $u^* : \mathsf{Perf}(G_2) \to \mathsf{Perf}(G_1)$ is an equivalence, the induced morphism $$u^* \colon \mathbf{Map}_{\mathbf{St}_k}(G_2,F) \to  \mathbf{Map}_{\mathbf{St}_k}(G_1,F)$$ is also an equivalence. As perfect complexes are the rigid objects in quasi-coherent complexes, being pointed $Q$-local implies being pointed $P$-local. However, the converse does not hold.

::: cor
[]{#ct2 label="ct2"} Let $F$ be a pointed Tannakian gerbe. Then, the adjunction morphism $$\alpha_F \colon F \to \mathsf{Fib}_*^{\mathrm{LSym}}(\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F))$$ induces an equivalence of $\Theta$-categories $$\alpha_F^* \colon \widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(\mathsf{Fib}_*^{\mathrm{LSym}}(\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F))) \simeq \widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F).$$ In particular, if the stack $F$ is pointed $P$-local, then $\alpha_F$ is a retract. If the stacks $F$ and $\mathsf{Fib}_*^{\mathrm{LSym}}(\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F))$ are both pointed $P$-local, then it is an equivalence of stacks.
:::

::: proof
*Proof.* By our Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} applied to $\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F)$, the $\infty$-functor induces by pull-back along $\alpha_F$ is an equivalence on Ind-perfect complexes $$\alpha_F^* \colon \widehat{\mathsf{Perf}}(\mathsf{Fib}_*^{\mathrm{LSym}}(\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F))) \simeq \widehat{\mathsf{Perf}}(F).$$ As the forgetful $\infty$-functor $\infty\text{-}\mathbf{Cat}_{pr}^\Theta\to \infty\text{-}\mathbf{Cat}^{\otimes}_{pr}$ is conservative, the corollary follows. ◻
:::

::: rmk
[]{#r2 label="r2"} As a final comment, we see that the results on Tannakian duality are imperfect and do not induce a nice equivalence between Tannakian $\Theta$-categories and Tannakian gerbes. One reason for this has been identified in Remark [\[r1\]](#r1){reference-type="ref" reference="r1"}: the equivalence of symmetric monoidal $\infty$-categories of Corollary [\[ct2\]](#ct2){reference-type="ref" reference="ct2"} has not been shown to lift to an equivalence of $\Theta$-categories. We think it is probably not possible to improve this using the present approach to $\Theta$-categories. The technical complication comes here from the use of presentable, and thus non-small $\infty$-categories everywhere, whereas the natural approach would be to write everything in terms of $\infty$-categories of perfect complexes as opposed to quasi-coherent sheaves or ind-perfect complexes. The problem with working with small $\infty$-categories of perfect complexes is of course that the monads involved, as the LSym monad does not preserve perfect complexes globally.

One possible approach is to consider the LSym monads as graded monads, as done in $\S 2.1$ for the construction of the $\Theta$-structure in ind-perfect complexes. Alternatively, and perhaps more satisfactorily, one can develop a theory of $\Theta$-categories in terms of symmetric monoidal $\infty$-categories equipped with additional symmetric power operations. Since the derived symmetric powers $\mathrm{LSym}^n$ preserve perfect complexes, such a theory would also allow to view $\mathsf{Perf}(X)$ as a $\Theta$-category. We believe that such an approach, allowing for $\Theta$-categories to be small $\infty$-categories could reduce the imperfection of Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"}. This will be investigated elsewhere.
:::
