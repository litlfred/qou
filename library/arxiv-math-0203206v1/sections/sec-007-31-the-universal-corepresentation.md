---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-007-31-the-universal-corepresentation
section_title: "The Universal Corepresentation"
section_number: 3.1
pages: 12-14
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.971
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
Throughout this section $(A,\Delta)$ stands for an arbitrary aqg and $B$ denotes a $*$-algebra. We recall the universal corepresentation $U$ of $(A,\Delta)$ and discuss its various properties [@ku-e].

::: defin
A corepresentation of $(A,\Delta)$ on $B$ is an element $V\in M(A\otimes B)$ such that $(\Delta\otimes \iota )V=V_{13}V_{23}$.
:::

::: prop
Suppose $V$ is a corepresentation of $(A,\Delta)$ on $B$. Then the following are equivalent:

1.  $V$ is invertible in $M(A\otimes B)$ with $V^{-1}=(S\otimes\iota )V$.

2.  $(\varepsilon\otimes\iota )V=1$.

3.  $V(A\otimes B)=A\otimes B =(A\otimes B)V$.

A corepresentation $V$ satisfying these equivalent conditions is said to be non-degenerate.
:::

::: defin
A unitary corepresentation $V$ of $(A,\Delta)$ on $B$ is a corepresentation on $B$ which is a unitary element of $M(A\otimes B)$.
:::

The following result is fundamental for corepresentations of aqg. We regard elements of $A\otimes\hat{A}$ as endomorphisms of $A$.

::: thm
[]{#t-univ-corep label="t-univ-corep"} There exists a unique element $U\in M(A\otimes\hat{A})$ such that $$[U(x\otimes\omega )](y)=(\iota\otimes\omega )(\Delta(y)(x\otimes 1))$$ $$[(x\otimes\omega )U](y)=(\omega\otimes\iota )((1\otimes x)\Delta(y))$$ for all $x,y\in A$ and $\omega\in\hat{A}$. Moreover, we have the following properties for $U$:

1.  $U$ is unitary in $M(A\otimes\hat{A})$.

2.  $(\Delta\otimes\iota )U=U_{13}U_{23}$.

3.  $(\iota\otimes\hat{\Delta})U=U_{12}U_{13}$.

4.  $(\omega\otimes\iota )U=\omega$ for all $\omega\in\hat{A}$.

5.  $(\iota\otimes a)U=a$ for all $a\in A$, where $a$ acts on $\hat{A}$ by the identification $A=\hat{A} \hspace{-.55ex}\hat{\rule{0ex}{2.0ex}}\hspace{.55ex}$.
:::

Note that claims 1 and 2 say that $U$ is a unitary corepresentation of $(A,\Delta)$ on $\hat{A}$, whereas claims 1 and 3 say that $\sigma(U)$ is a unitary corepresentation of $(\hat{A},\hat{\Delta})$ on $A$. Below we will explain why $U$ is called the universal corepresentation of $(A,\Delta)$. It follows that $\sigma (U)$ is the universal corepresentation of $(\hat{A},\hat{\Delta})$.

Let $\mathrm{Hom}(A,B)$ denote the set of $*$-homomorphisms from $A$ to $M(B)$ satisfying $\theta (A)B=B$.

::: prop
[]{#p-functP label="p-functP"} Let $V\in M(A\otimes B)$ and consider the linear map $$\pi_V:\ \hat{A}\rightarrow M(B), \quad \omega \mapsto (\omega\otimes\iota) V.$$ Then the following equivalences hold:

1.  $V$ is a corepresentation (of $(A,\Delta)$ on $B$) iff $\pi_V$ is multiplicative.

2.  $V$ is a non-degenerate corepresentation iff $\pi_V$ is multiplicative and non-degenerate.

3.  $V$ is a unitary corepresentation iff $\pi_V\in\mathrm{Hom}(\hat{A},B)$.
:::

The universality of $U$ can now be formulated as follows.

::: thm
[]{#t-univ-corr label="t-univ-corr"} For any unitary corepresentation $V$ of $(A,\Delta)$ on $B$ and any $\theta\in\mathrm{Hom}(\hat{A},B)$, we have:

1.  $(\iota\otimes \pi_V )U=V$.

2.  $\pi_{(\iota\otimes\theta )U}=\theta$.
:::

The result remains valid for the non-degenerate situation without $*$-operation.

::: defin
[]{#d-tensor label="d-tensor"} Let $B'$ be non-degenerate $*$-algebra. For $\theta\in\mathrm{Hom}(A,B)$ and $\theta '\in \mathrm{Hom}(A,B')$ we define $\theta\times\theta'\in \mathrm{Hom}(A,B\otimes B' )$ by $\theta\times\theta' =(\theta\otimes\theta' )\Delta$. If $V$ and $V'$ are unitary corepresentations of $(A,\Delta)$ on $B$ and $B'$, respectively, we define a unitary corepresentation $V\times V'$ of $(A,\Delta)$ on $B\otimes B'$ by $V\times V' =V_{12}V'_{13}$.
:::

::: thm
[]{#t-bij label="t-bij"} The map sending unitary corepresentations $V$ of $(A,\Delta)$ on $B$ to $\pi_V\in\mathrm{Hom}(\hat{A},B)$, is a bijection. Let $V'$ be a unitary corepresentation of $(A,\Delta)$ on $B'$. Then $\pi_{V\times V'} =\pi_V\times\pi_{V'}$. For the universal corepresentation $U$ of $(A,\Delta)$ on $\hat{A}$ we have $\pi_U =\iota\in\mathrm{Hom}(\hat{A},\hat{A})$, and finally for the trivial unitary corepresentation $1\otimes 1\in A\otimes B({\mathbb C} )$ of $(A,\Delta)$ we have $\pi_{1\otimes 1}=\hat{\varepsilon}$, where $\hat{\varepsilon}$ is the counit of $(\hat{A},\hat{\Delta})$.
:::

*Proof. *The only part which is not immediate from the results above, is the identity $\pi_{V\times V'} =\pi_V\times\pi_{V'}$. To show this, first note that $$V\times V'=V_{12}V'_{13}=[(\iota\otimes\pi_V )U]_{12}[(\iota\otimes\pi_{V'} )U]_{13}  
=(\iota\otimes\pi_V\otimes\pi_{V'})(U_{12}U_{13})$$ $$=(\iota\otimes\pi_V\otimes\pi_{V'})(\iota\otimes\hat{\Delta})U
=(\iota\otimes(\pi_V\otimes\pi_{V'})\hat{\Delta})U
=(\iota\otimes\pi_{V}\times\pi_{V'})U.$$ Thus we may conclude that $$\pi_{V\times V'}(\omega )=(\omega\otimes\iota\otimes\iota )(V\times V' )
=(\omega\otimes\iota\otimes\iota )(\iota\otimes\pi_{V}\times\pi_{V'})U
=(\pi_{V}\times\pi_{V'})(\omega\otimes\iota )U =(\pi_{V}\times\pi_{V'})(\omega ),$$ for all $\omega\in\hat{A}$.

::: rema
[]{#r-cat label="r-cat"} The correspondence established in Theorem [\[t-bij\]](#t-bij){reference-type="ref" reference="t-bij"} is in fact a functor if we define arrows for representations and corepresentations on $*$-algebras in the following way. For any objects $\pi\in\mathrm{Hom}(A,B)$ and $\pi'\in \mathrm{Hom}(A,B')$ define an arrow $f:\pi\rightarrow\pi'$ to be $f\in \mathrm{Hom}(B,B')$ such that $f\pi =\pi'$. Similarly, if $V$ and $V'$ are unitary corepresentations of $(A,\Delta)$ on $B$ and $B'$, respectively, we define an arrow $f:V\rightarrow V'$ between these objects to be $f\in \mathrm{Hom}(B,B')$ such that $V' =(\iota\otimes f)V$. Then the correspondence $V\mapsto\pi_V$ in Theorem [\[t-bij\]](#t-bij){reference-type="ref" reference="t-bij"} is an equivalence of tensor categories (they are not $*$-categories).
:::

::: rema
[]{#r-actcoact label="r-actcoact"} We remark on the tensor categories of actions and coactions of an aqg $(A,\Delta)$ on $*$-algebras.

By an action $\gamma$ of $(A,\Delta)$ on a $*$-algebra $B$, we mean a surjective linear map $\gamma :A\otimes B\rightarrow B$ such that $\gamma (m\otimes\iota )=\gamma (\iota\otimes\gamma )$. An arrow $f:\gamma\rightarrow \gamma'$ is an element $f\in\mathrm{Hom}(B,B')$ such that $f\gamma=\gamma' f$. We do not define tensor products in the general case.

Given $\pi\in\mathrm{Hom}(A,B)$, we define the action $\gamma_{\pi}$ of $(A,\Delta)$ on $B$ by $\gamma_{\pi}(a\otimes b)=\pi (a)b$, for all $a\in A$ and $b\in B$. Using non-degeneracy of $f$, we see that for any $f\in \mathrm{Hom}(B,B')$, we have $f:\pi\rightarrow\pi'$ iff $f:\gamma_{\pi}\rightarrow\gamma_{\pi'}$. Thus $\pi\mapsto\gamma_{\pi}$ is an equivalence of the tensor category of non-degenerate $*$-representations of $(A,\Delta)$ on $*$-algebras to the tensor category of actions of $(A,\Delta)$ on $*$-algebras contained in the image of the functor and with tensor product $\gamma_{\pi}\times \gamma_{\pi '}$ simply defined to be the action $\gamma_{\pi\times\pi'}$. We have not incorporated the $*$-preserving property of $\pi$ in $\gamma_{\pi}$ and the axioms for actions.

A coaction $\delta$ of $(A,\Delta)$ on a $*$-algebra $B$ is a $\delta\in\mathrm{Hom}(B,A\otimes B)$ such that $(\iota\otimes\delta)\delta =(\Delta\otimes\iota)\delta$ and $(\varepsilon\otimes\iota)\delta=\iota$. Such coactions form a tensor category, an arrow $f:\delta\rightarrow\delta '$ being an element $f\in\mathrm{Hom}(B,B')$ such that $(\iota\otimes f)\delta =\delta 'f$ and the tensor product $\delta\times\delta '$ being the comodule of $(A,\Delta)$ on $B\otimes B'$ given by $(\delta\times\delta ')(b\otimes b')=\delta (b)_{12}\delta' (b')_{13}$, for all $b\in B$ and $b'\in B'$.

Let $V$ be a unitary corepresentation of $(A,\Delta)$ on $B$. Then the linear map $\delta_V :B\rightarrow M(A\otimes B)$ given by $\delta_V (b)=V (1\otimes b)V^*$ for all $b\in B$, is indeed a coaction of $(A,\Delta^{op})$ on $B$. Non-degeneracy of $\delta_V$ follows from $V(A\otimes B)=A\otimes B$, and the formula $(\iota\otimes\delta_V)\delta_V =(\Delta^{op}\otimes\iota)\delta_V$ follows from the calculation $$\begin{aligned}
 \lefteqn{  (\iota\otimes\delta_V )\delta_V (b)
   =(\iota\otimes\delta_V )V(1\otimes\delta_V (b))((\iota\otimes\delta_V )V)^*
   =V_{23}V_{13}V_{23}^* (1\otimes V(1\otimes b)V^* )(V_{23}V_{13}V_{23}^* )^* } \\
  && =V_{23}V_{13}(1\otimes 1\otimes b)V_{13}^* V_{23}^*
=(\Delta^{op}\otimes \iota )V(1\otimes 1\otimes b)((\Delta^{op}\otimes\iota )V)^*
=(\Delta^{op}\otimes\iota )(V(1\otimes b)V^* ) \\
 &&=(\Delta^{op}\otimes\iota )\delta_V (b)
\end{aligned}$$ for all $b\in B$. Note that any arrow $f:V\rightarrow V'$ will be an arrow $f:\delta_V\rightarrow \delta_{V'}$, but the converse is not true (consider $B'$ commutative). So we have a tensor functor $V\mapsto\delta_V$ from the tensor category of unitary corepresentations of $(A,\Delta)$ on $*$-algebras to the tensor category of coactions of $(A,\Delta^{op})$ on $*$-algebras, which in general, is not an equivalence.
:::
