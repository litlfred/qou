---
doc_id: arxiv-2508.03145v1
doc_title: "Θ -Categories and Tannakian duality"
section_id: sec-005-tannakian--categories-and-tannakian-gerbes
section_title: "Tannakian -categories and Tannakian gerbes"
section_number: null
pages: 21-23
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.949
doc_brief: "Θ -Categories and Tannakian duality — We introduce a notion of Θ-categories, which is a refinement of the notion of symmetric monoidal ∞-categories."
---
For the sake of simplicity we will only deal with the neutral case in the present work.

::: df
A *neutralized $k$-linear Tannakian $\Theta$-category* is a map of $k$-linear $\Theta$-categories $$\omega\colon  T^\Theta \longrightarrow \widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(k)\simeq \mathsf{QCoh}^{\mathrm{LSym}}(k)$$ satisfying the following conditions.

1.  The underlying presentable symmetric monoidal $\infty$-category $T$ is \"rigid\": it is compactly generated and compact objects in $T$ coincide with dualizable objects.

2.  The underlying $\infty$-functor $\omega \colon T \to \widehat{\mathsf{Perf}}(k) \simeq \mathsf{QCoh}(k)$ is conservative.

3.  Let $\mathsf{QCoh}(k)^{\leq 0}\subset \mathsf{QCoh}(k)$ denote the full sub-$\infty$-category of connective objects. The full sub-$\infty$-category $\omega^{-1}(\mathsf{QCoh}(k)^{\leq 0}) \subset T$ then defines the connective part of a bounded (on compact objects) $t$-structure on $T$ for which $\omega$ becomes $t$-exact.

Let us write $k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta/k := \big(k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta\big)\big/\mathsf{QCoh}^{\mathrm{LSym}}(k)$ for the $(2,\infty)$-category of $k$-linear $\Theta$-categories over $\mathsf{QCoh}^{\mathrm{LSym}}(k)$ and $$k\text{-}\mathcal{T}an_*^\Theta \subseteq k/ \infty\text{-}\mathbf{Cat}_{pr}^\Theta/ k$$ for the full sub-$(2,\infty)$-category on the neutralized $k$-linear Tannakian $\Theta$-categories. Here the \"$*$\" refers to the neutralized assumption. As $\omega$ is conservative, the $(2,\infty)$-category $k\text{-}\mathcal{T}an_*^\Theta$ is in fact a $(1,\infty)$-category.
:::

::: df
A *pointed* (or *neutralized*) *Tannakian gerbe* over $k$ is a pointed stack $F \in \ast/\mathbf{St}_k$ satisfying the following conditions.

1.  The natural morphism of fpqc-sheaves $* \to \pi_0(F)$ is an isomorphism.

2.  The stack $F$ is *pointed Q-local*: for any morphism of pointed and connected stacks $u \colon G_1 \to G_2$ whose induced $\infty$-functor $u^* \colon \mathsf{QCoh}(G_2) \to \mathsf{QCoh}(G_1)$ is an equivalence, the induced morphism in mapping spaces $$u^* \colon \mathbf{Map}_{\mathbf{St}_k}(G_2,F) \to \mathbf{Map}_{\mathbf{St}_k}(G_1,F)$$ is an equivalence.

3.  There exists a coconnective $k$-linear $\mathrm{LSym}$-algebra $B$ and an equivalence $$\mathbf{Spec}\, B \simeq \Omega_*F$$ (see [@chaff] for the notion of spectrum of coconnective $\mathrm{LSym}$-algebras and the theory of affine stacks). Moreover, $B$ is of positive Tor-dimension (also called connectively flat): if $E$ is a coconnective object in $\mathsf{QCoh}(k)$, then $E \otimes_k B$ remains coconnective.

4.  The $k$-linear $\Theta$-functor $\omega\colon \widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F) \to \widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(k)$, obtained by pull-back along the base point $* \to F$, makes $\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F)$ into a Tannakian $\Theta$-category.

We will write $k\text{-}\mathcal{G}erb_* \subset */\mathbf{St}_k$ for the full sub-$\infty$-category on the pointed Tannakian gerbes over $k$.
:::

Let $T^\Theta$ be a $k$-linear $\Theta$-category. For a commutative $k$-algebra $A$, we set $$\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)(A):=\mathbf{Map}_{k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T,\mathsf{QCoh}^{\mathrm{LSym}}(A)).$$ Since $\mathsf{QCoh}^{\mathrm{LSym}}$ defines an fpqc-stack of $k$-linear $\Theta$-categories, varying $A$ inside the category of commutative $k$-algebras yields an fpqc-stack $\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)$, called the *stack of $\Theta$-fiber functors on $T^\Theta$*. This is part of an adjunction $$\xymatrix{
\mathsf{Fib}^{\mathrm{LSym}}\colon k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta\ar@<1ex>[r] &  \mathbf{St}^{op}_k : \mathsf{QCoh}^{\mathrm{LSym}}.\ar@<1ex>[l]
}$$ Indeed, since $\mathsf{QCoh}^{\mathrm{LSym}}$ satisfies fpqc descent, there is a natural equivalence for $F \in \mathbf{St}_k$ and $T^\Theta \in k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta$ $$\mathbf{Map}_{k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T^\Theta,\mathsf{QCoh}^{\mathrm{LSym}}(F)) \simeq 
\mathbf{Map}_{\mathbf{St}_k}(F,\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)).$$ In particular, we have adjunction morphisms $$\beta_{T^\Theta} \colon T^\Theta \to \mathsf{QCoh}^{\mathrm{LSym}}\big(\mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)\big) \qquad
F \to \mathsf{Fib}^{\mathrm{LSym}}\big(\mathsf{QCoh}^{\mathrm{LSym}}(F)\big).$$ The second morphism, composed with the canonical morphism $\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F) \to \mathsf{QCoh}^{\mathrm{LSym}}(F)$, induces a morphism $$\alpha_F \colon F \to \mathsf{Fib}^{\mathrm{LSym}}\big(\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F)\big).$$

This extends naturally to the neutralized, or pointed, situation as follows. Let us write $\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta) \subset \mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)$ for the full sub-stack consisting of all fiber functors locally equivalent to $\omega \colon T^{\Theta} \to \mathsf{QCoh}^{\mathrm{LSym}}(k)$. This full sub-stack can also be written $$\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta) \simeq B\underline{aut}^{\Theta}(\omega) \subset \mathsf{Fib}^{\mathrm{LSym}}(T^\Theta)$$ where $\underline{aut}^{\Theta}(\omega)$ is the stack of $\Theta$-auto-equivalences of $\omega$. The stack $\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta)$ is connected (by definition) and canonically pointed at $\omega$. Note that any $\Theta$-endomorphism of $\omega$ is also a self-equivalence, as a consequence of the rigidity condition (T1).

Similarly, if $x \colon * \to F$ is a pointed connected stack, we can identify $\mathsf{QCoh}^{\mathrm{LSym}}(F)$ with an object in $k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta/k$ using its canonical fiber functor at the basepoint $x^* \colon \mathsf{QCoh}^{\mathrm{LSym}}(F) \to \mathsf{QCoh}^{\mathrm{LSym}}(k)$. This yields a similar adjunction $$\xymatrix{
\mathsf{Fib}_\ast^{\mathrm{LSym}}\colon k/\infty\text{-}\mathbf{Cat}_{pr}^\Theta/k\ar@<1ex>[r] &  (\ast/\mathbf{St}^{cn}_k)^{op} : \mathsf{QCoh}^{\mathrm{LSym}}\ar@<1ex>[l]
}$$ where $\ast/\mathbf{St}^{cn}_k$ denotes the $\infty$-category of pointed connected stacks. Using the unit and counit of this adjunction, together with natural morphism $\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}} \to \mathsf{QCoh}^{\mathrm{LSym}}(F)$, we obtain two canonical morphisms $$\beta_{T^\Theta} \colon T^\Theta \to \mathsf{QCoh}^{\mathrm{LSym}}(\mathsf{Fib}_*^{\mathrm{LSym}}(T^\Theta))
 \qquad\quad \alpha_F \colon F \to \mathsf{Fib}_*^{\mathrm{LSym}}(\widehat{\mathsf{Perf}}{}^{\mathrm{LSym}}(F))$$

The Tannakian duality investigated in the next chapter ensures that $\beta$ and $\alpha$ are somehow equivalences when $T^\Theta$ is Tannakian and $F$ is a Tannakian gerbe. We will only have partial answers, but we refer to Remarks [\[r1\]](#r1){reference-type="ref" reference="r1"} and [\[r2\]](#r2){reference-type="ref" reference="r2"} for some indications of how better results can be obtained.
