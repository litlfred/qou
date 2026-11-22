---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-008-32-representations-vs-corepresentations-as-tenso
section_title: "Representations vs. Corepresentations as Tensor $*$-Categories"
section_number: 3.2
pages: 14-17
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.983
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
We now proceed to establish the correspondence between representations of an aqg $(A,\Delta)$ and corepresentations of $(\hat{A},\hat{\Delta})$, restricting ourselves to finite dimensional Hilbert spaces. For homomorphisms $\pi: A\rightarrow\mathrm{End}K$ there are two different notions of non-degeneracy which, fortunately, are equivalent for $K$ finite dimensional.

::: lem
[]{#l-non-deg label="l-non-deg"} Let $A$ be an algebra and $K$ a finite dimensional vector space. For a homomorphism $\pi: A\rightarrow\mathrm{End}\,K$ the conditions $\pi(A)\mathrm{End}\,K=\mathrm{End}\,K$ and $\pi(A)K=K$ are equivalent.
:::

*Proof. *For $K$ finite dimensional we clearly have $(\mathrm{End}\,K)K=K$. Assuming $\pi(A)\mathrm{End}K=\mathrm{End}K$ we compute $$\pi(A)K=\pi(A)((\mathrm{End}K)K)=(\pi(A)\mathrm{End}K)K=(\mathrm{End}K)K=K.$$ Conversely, assume $\pi(A)K=K$. With the isomorphism $\alpha: K\otimes K^*\rightarrow\mathrm{End}\,K$ determined by $\alpha(x\otimes\phi)(z)=x\phi(z)$ for $x,z\in K, \phi\in K^*$ we have $(s\alpha(x\otimes\phi))(z)=sx\phi(z)=\alpha(sx\otimes\phi)(z)$ and therefore $$\pi(A)\mathrm{End}\,K=\pi(A)\alpha(K\otimes K^*)=\alpha((\pi(A)K)\otimes K^*)
   =\alpha(K\otimes K^*)=\mathrm{End}\,K,$$ as desired.

::: defin
[]{#d-repf label="d-repf"} Let $(A,\Delta)$ be an aqg. Let $\mathrm{Rep}_f (A,\Delta)$ denote the class of (algebraically) non-degenerate $*$-representations of $A$ on finite dimensional Hilbert spaces including the zero representation $0$. Let $\pi_1, \pi_2\in \mathrm{Rep}_f (A,\Delta)$. Then $\pi_i\in\mathrm{Hom}(A,B(K_i ))$, so we define $\pi_1\times\pi_2 \in\mathrm{Hom}(A,B(K_1 )\otimes B(K_2 ))
=\mathrm{Hom}(A,B(K_1\otimes K_2 ))\subset\mathrm{Rep}_f (A,\Delta)$ according to Definition [\[d-tensor\]](#d-tensor){reference-type="ref" reference="d-tensor"}.
:::

We regard $\mathrm{Rep}_f (A,\Delta)$ as a tensor $*$-category with representations as objects and intertwiners as arrows. (Recall that a zero representation $0$ is not regarded as an irreducible object.) The tensor product is the one given in the definition above. Clearly, $\mathrm{Rep}_f (A,\Delta)$ is a tensor $*$-category with the counit $\varepsilon$ as the irreducible unit. Of course, the $*$-operation in the category is the usual Hilbert space adjoint of operators.

::: defin
[]{#d-corepf label="d-corepf"} We say $V$ is a finite dimensional unitary corepresentation of an aqg $(A,\Delta)$ on a Hilbert space $K$ if $K$ is finite dimensional and $V$ is a unitary corepresentation of $(A,\Delta)$ on the unital $*$-algebra $B(K)$ of linear operators on $K$. Let $\mathrm{Corep}_f (A,\Delta)$ denote the class of all such unitary corepresentations including the zero corepresentation $0$. Let $V, V'\in \mathrm{Corep}_f (A,\Delta)$. Then we define the unitary corepresentation $V\times V'$ of $(A,\Delta)$ on $B(K)\otimes B(K')=B(K\otimes K' )$ according to Definition [\[d-tensor\]](#d-tensor){reference-type="ref" reference="d-tensor"}. Clearly, we have $V\times V'\in \mathrm{Corep}_f (A,\Delta)$.
:::

We regard $\mathrm{Corep}_f (A,\Delta)$ as a tensor $*$-category with corepresentations as objects and intertwiners as arrows. Recall that $T\in B(K,K' )$ is an intertwiner between two corepresentations $V,V'\in \mathrm{Corep}_f (A,\Delta)$ iff $T(\omega\otimes\iota )V =(\omega\otimes\iota )V' T$, for all $\omega\in\hat{A}$. The tensor product is the one given in the definition above. Clearly, $\mathrm{Corep}_f (A,\Delta)$ is a tensor $*$-category with the unit $1\otimes 1$ as the irreducible unit. Again, the $*$-operation in the category is the usual Hilbert space adjoint of operators.

The two tensor categories are related in the following way.

::: thm
[]{#t-dualcor label="t-dualcor"} Let notation be as above. The correspondence $$P: \ \mathrm{Corep}_f (A,\Delta) \rightarrow\mathrm{Rep}_f (\hat{A},\hat{\Delta} ), \quad V \mapsto \pi_V$$ provided by Proposition [\[p-functP\]](#p-functP){reference-type="ref" reference="p-functP"} together with the identity map on morphisms gives rise to an isomorphism of tensor $*$-categories.
:::

*Proof. *The proof is immediate from Theorem [\[t-bij\]](#t-bij){reference-type="ref" reference="t-bij"}.

::: rema
A similar result can be obtained for the infinite dimensional case. One needs then to talk about $*$-representations which are non-degenerate in the $C^*$-algebra sense, so $\pi\in \mathrm{Rep}(A,\Delta)$ iff the exists a (possibly infinite dimensional) Hilbert space $K$ and a $*$-homomorphism $\pi :A\rightarrow B(K)$ such that the vector space $\pi (A)K$ is dense in $K$. The tensor $*$-category $\mathrm{Corep}(A_r, \Delta_r )$ of unitary corepresentations on Hilbert spaces consists of Hilbert spaces $K$ and unitaries $V\in M(A_r\otimes B_0 (K))$ such that $(\Delta_r\otimes\iota )V =V_{13}V_{23}$. For the exact correspondence thus established, see [@BMT].
:::

We will look at another way of obtaining a tensor $*$-category $\mathrm{Rep}_f (A^o_s, \hat{\Delta})$ from a compact aqg $(A,\Delta)$ which is equivalent to $\mathrm{Corep}_f (A,\Delta)$. This can sometimes come in very handy, especially when dealing with representations of quantized universal enveloping Lie algebras $U_q ({\mathfrak g})$.

First recall that $(A,\Delta)$ is a Hopf $*$-algebra with counit $\varepsilon$, coinverse $S$ and unit $I$, so the vector space $A'$ of all linear functionals on $A$ is a unital $*$-algebra with unit $\varepsilon$, product $\omega\eta =(\omega\otimes\eta)\Delta\in A'$ and $*$-operation $\omega^*\in A'$ given by $\omega^* (a)=\overline{\omega (S(a)^* )}$, for all $a\in A$. Define a linear map $\hat{\Delta}
:A'\rightarrow (A\otimes A)'$ by $\hat{\Delta}(\omega )(a\otimes b)=\omega (ab)$, for all $\omega\in A'$ and $a,b\in A$. Consider the subspace $A^o$ of $A'$ given by $$A^o =\{\omega\in A'\ |\ \hat{\Delta}(\omega )\in A'\otimes A'\},$$ where we understand the embedding $A'\otimes A'\subset (A\otimes A)'$. Then $(A^o, \hat{\Delta} )$ is called the *maximal dual* Hopf $*$-algebra of $(A,\Delta)$. Note that for $\hat{f}\in M(\hat{A})$ as in Theorem [\[t-disc2\]](#t-disc2){reference-type="ref" reference="t-disc2"}, we have $\hat{f}\in A^o$ and $\hat{\Delta}(\hat{f })=\hat{f}\otimes\hat{f}$. Regard $A^o$ as a locally convex topological vector space with pointwise convergence, so $\omega_{\lambda}\rightarrow\omega$ in $A^o$ if $\omega_{\lambda}(a)\rightarrow\omega (a)$, for all $a\in A$. The continuous unital $*$-representations of $(A^o, \hat{\Delta} )$ on finite dimensional Hilbert spaces clearly form a tensor $*$-category with conjugates given by the same formulas as for $\mathrm{Rep}_f (\hat{A},\hat{\Delta})$. Note that in general, the maximal dual Hopf $*$-algebra can be very small!

::: thm
Let $(A,\Delta)$ be a compact aqg and let $(A^o_s, \hat{\Delta})$ be a sub Hopf $*$-algebra of the maximal dual Hopf $*$-algebra of $(A,\Delta)$ which separates the elements of $A$. (Thus $A^o_s$ is a unital $*$-subalgebra of $A^o$ and $\hat{\Delta}$ is given by restriction). Consider the tensor $*$-category $\mathrm{Rep}_f (A^o_s, \hat{\Delta})$ of continuous unital $*$-representations of $(A^o_s, \hat{\Delta} )$ on finite dimensional Hilbert spaces with arrows, $*$-operation and tensor product defined in the obvious way. Then the assignment $$N: \ \mathrm{Corep}_f (A,\Delta)\rightarrow\mathrm{Rep}_f (A^o_s, \hat{\Delta}), \quad V\mapsto \pi_V \ \mbox{with} \ 
   \pi_V (\omega )=(\omega\otimes\iota )V, \ \forall\omega\in A^o_s,$$ together with the identity map on arrows, is an equivalence of tensor $*$-categories.
:::

*Proof. * The only part which requires a proof is that any $\pi\in \mathrm{Rep}_f (A^o_s, \hat{\Delta})$ is of the form $\pi_{V_{\pi}}$ for some $V_{\pi}\in \mathrm{Corep}_f (A,\Delta)$. Thus let $\pi :A^o_s\rightarrow B(K)$ be a continuous unital $*$-representation of $A^o_s$ on a finite dimensional Hilbert space $K$. We will provide a $V_{\pi}\in A\otimes B(K)$ such that $\pi_{V_{\pi}}=\pi$. Using the fact that $A^o_s$ separates the elements of $A$, it is then clear that $V_{\pi}$ will be unitary, that $(\Delta\otimes\iota )V_{\pi} =(V_{\pi})_{13}(V_{\pi})_{23}$ and that the $*$-preserving tensor functor $N$ is an equivalence.

Now pick an orthonormal basis $(e_i )$ for $K$ and consider the system $m_{ij}$ of matrix units for $B(K)$ defined as $m_{ij}(e_k )=\delta_{jk}e_i$, for all $i,j,k$. Consider, for fixed $i$ and $j$, the linear functional on $A^o_s$ given by $\omega\mapsto (\pi (\omega )e_j, e_i )$ for all $\omega\in A^o_s$. Since $\pi$ is continuous w.r.t pointwise topology on $A^o_s$, it follows from [@ped Proposition 2.4.4], that there exists a unique $a_{ij}\in A$ such that $\omega (a_{ij})=(\pi (\omega )e_j, e_i )$, for all $\omega\in A^o_s$. Define now $V_{\pi}\in A\otimes B(K)$ by $V_{\pi}=\sum_{ij} a_{ij}\otimes m_{ij}$. By construction $\pi_{V_{\pi}}=\pi$ and we are done.

::: rema
It is known that for the usual quantized compact aqg $(A_q, \Delta)$, the associated quantized universal enveloping Lie algebras $U_q ({\mathfrak g} )$ are Hopf $*$-algebras with $A^o_s =U_q ({\mathfrak g} )$ which separate the elements of $A_q$ [@schm Sect. 7.1.5]. Thus the tensor $*$-category of continuous unital $*$-representations of $(U_q ({\mathfrak g} ),\hat{\Delta})$ on finite dimensional Hilbert spaces is equivalent to $\mathrm{Corep}_f (A_q, \Delta)$. Also $\hat{f}\in U_q ({\mathfrak g})$, so the intrinsic dimension can be read off conveniently for such representations [@RT]. We return to this issue in the next subsection.
:::

We now recast our results in the language of modules and comodules.

::: prop
Any non-degenerate $*$-representation $\pi$ of a discrete aqg $(A,\Delta)$ on a finite dimensional Hilbert space $K$ gives rise to an $A$-module $K$. Namely, define a linear map $\alpha_\pi: A\otimes K\rightarrow K$ by $\alpha_\pi (a\otimes \xi )=\pi (a)\xi$, for all $a\in A$ and $\xi\in K$. Then the following properties hold:

1.  $\alpha_{\pi}(m\otimes\iota )=\alpha_{\pi}(\iota\otimes\alpha_{\pi} )$.

2.  $\alpha_{\pi} (A\otimes K)=K$.

3.  $(\alpha_{\pi}(a^*\otimes\xi ),\eta )=(\xi, \alpha_{\pi}(a\otimes \eta)) \ \ 
    \forall a\in A\ \ \forall \xi, \eta\in K$.

Denote by $\mathrm{Mod}_f (A,\Delta)$ the tensor $*$-category of linear maps $\alpha :A\otimes K\rightarrow K$ satisfying properties 1-3 above, with arrows $t:\alpha\rightarrow\alpha '$ being linear maps $t:K\rightarrow K'$ satisfying $\alpha' =t\alpha$ and tensor product $\alpha\times\alpha ':A\otimes K\otimes K'\rightarrow K\otimes K'$ uniquely determined by $$(\alpha\times\alpha ')(\iota\otimes\alpha\otimes\alpha )(a\otimes b\otimes\xi\otimes c\otimes\xi')
   =\sum_k \alpha (a_k \otimes\xi )\otimes \alpha' (b_k\otimes \xi '),$$ for all $a,b\in A$, $\xi\in K$ and $\xi'\in K'$ and where $\sum_k a_k\otimes b_k =\Delta(a)(b\otimes c)$. Then the assignment $\pi\mapsto\alpha_{\pi}$ is a monoidal $*$-preserving equivalence of $\mathrm{Rep}_f (A,\Delta)$ and $\mathrm{Mod}_f (A,\Delta)$.
:::

*Proof. * Straightforward, once one shows that $\alpha\times\alpha '$ is well-defined. This is most easily done by considering the corresponding well-defined tensor product $\pi\times\pi'$ of the associated non-degenerate $*$-representations, i.e, of $\pi$ and $\pi'$ such that $\alpha =\alpha_{\pi}$ and $\alpha'=\alpha_{\pi'}$, and then noting that $\alpha\times\alpha '=\alpha_{\pi\times\pi'}$.

::: prop
Any unitary corepresentation $V$ of a compact aqg $(A,\Delta)$ on a finite dimensional Hilbert space $K$ gives rise to an $A$-comodule $K$. Namely, define a linear map $\beta_V :K\rightarrow A\otimes K$ by $\beta_V (\xi )=\sum_k a_k\otimes x_k\xi$, for all $\xi\in K$ and where $V=\sum_k a_k\otimes x_k\in A\otimes B(K)$. Then the following properties hold:

1.  $(\Delta^{op}\otimes\iota )\beta_V =(\iota\otimes\beta_V )\beta_V$.

2.  $(S\otimes(\cdot,\eta))\beta_V (\xi )=(*\otimes (\xi,\cdot ))\beta_V (\eta )\ \ \ \ \forall \xi, \eta\in K$,

where $\varepsilon$ and $S$ are the counit and coinverse of $(A,\Delta)$, respectively. Let $\mathrm{Comod}_f (A,\Delta^{op})$ denote the tensor $*$-category of linear maps $\beta :K\rightarrow A\otimes K$ satisfying properties 1-2 above, with arrows $t:\beta\rightarrow\beta'$ being linear maps $t:K\rightarrow K'$ satisfying $\beta' t=(\iota\otimes t)\beta$ and tensor product $\beta\times\beta ':K\otimes K'\rightarrow A\otimes K\otimes K'$ given by $$(\beta\times\beta ')(\xi\otimes \xi')
=\beta (\xi )_{12}\beta'(\xi ')_{13},$$ for all $\xi\in K$ and $\xi'\in K'$. Then the assignment $V\mapsto\beta_V$ is a monoidal $*$-preserving equivalence of $\mathrm{Corep}_f (A,\Delta)$ and $\mathrm{Comod}_f (A,\Delta^{op})$.
:::

*Proof. * Straightforward. How to produce a unitary corepresentation $V\in A\otimes B(K)$ of $(A,\Delta)$ from a prescribed comodule $\beta :K\rightarrow A\otimes K$ of $(A,\Delta^{op})$ perhaps calls for some explanation. Pick an orthonormal basis $(e_k )$ for $K$ and consider the system $(m_{ij})$ of matrix units of $B(K)$ given by $m_{ij}(e_k )=\delta_{jk}\ e_i$ for all $i,j,k$. Define $V\in A\otimes B(K)$ by $V=\sum_{ij} a_{ij}\otimes m_{ij}$, where the elements $a_{ij}\in A$ are given by $$a_{ij}=(\iota\otimes (\cdot,e_i ))\beta (e_j ),$$ for all $i,j$. It is now easily checked that $\beta_V =\beta$.

We thus get the following restatement of Theorem [\[t-dualcor\]](#t-dualcor){reference-type="ref" reference="t-dualcor"}.

::: thm
[]{#t-dual-comod label="t-dual-comod"} Let $(A,\Delta)$ be a discrete aqg. Then $\mathrm{Mod}_f (A,\Delta)$ and $\mathrm{Comod}_f (\hat{A},\hat{\Delta}^{op})$ are equivalent as semisimple tensor $*$-categories.
:::
