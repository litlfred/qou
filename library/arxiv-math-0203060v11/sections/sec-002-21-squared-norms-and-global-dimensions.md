---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-002-21-squared-norms-and-global-dimensions
section_title: "Squared norms and global dimensions"
section_number: 2.1
pages: 4-5
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.987
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let us introduce the notion of the global dimension of a fusion category. First of all, we have the following known result (see e.g., [@O]).

::: proposition
[]{#doubledual label="doubledual"} In a fusion category, any simple object $V$ is isomorphic to its double dual $V^{**}$.
:::

To prove this, it suffices to note that for any simple object $V$, the right dual $V^*$ is the unique simple object $X$ for which $V\otimes X$ contains the neutral object, while the left dual $^*V$ is the unique simple object $X$ for which $V\otimes X$ projects to the neutral object; so $^*V=V^*$ by semisimplicity of the category, and hence $V=V^{**}$ for any simple $V$.

Next, recall ([@BaKi], p.39) that if $V\in {\mathcal C}$, and $g:V\to V^{**}$ is a morphism, then one can define its "quantum trace" $\text{Tr}_V(g)\in k$ by the formula $$\text{Tr}_V(g)={\rm ev}_{V^*} \circ (g\otimes 1_{V^*})\circ {\rm coev}_V,$$ where $\mathbf 1$ is the unit object of ${\mathcal C}$, ${\rm coev}_V: \mathbf 1\to V\otimes V^*$ and ${\rm ev}_V: V^*\otimes V\to \mathbf 1$ are the coevaluation and evaluation maps (see [@BaKi]). It is easy to show (and well known, see e.g. [@BaKi]) that for any simple object $V$ and a nonzero morphism $a: V\to V^{**}$ one has $\text{Tr}_V(a)\ne 0$. Indeed, otherwise there is a sequence of nonzero maps $\mathbf 1\to V\otimes V^*\to \mathbf 1$ with zero composition, which would imply that the multiplicity of $\mathbf 1$ in $V\otimes V^*$ is at least 2 -- a contradiction.

Now, following [@Mu1], for every simple object $V$ of a fusion category ${\mathcal C}$, define the *squared norm* $|V|^2\in k^\times$ of $V$ as follows. Fix an isomorphism $a: V\to V^{**}$ (which exists by Proposition [\[doubledual\]](#doubledual){reference-type="ref" reference="doubledual"}), and let $|V|^2=\text{Tr}_V(a)\text{Tr}_{V^*}((a^{-1})^*)$. It is clearly independent on the choice of $a$ (since $a$ is uniquely determined up to a scaling), and nonzero by the explanation in the previous paragraph. For example, for the neutral object $\mathbf 1$ we have $|\mathbf 1|^2=1$.

::: definition
[@Mu1] The *global dimension* of a fusion category ${\mathcal C}$ is the sum of squared norms of its simple objects. It is denoted by $\dim({\mathcal C})$.
:::

One of our main results is

::: theorem
[]{#posi label="posi"} If $k={\mathbb{C}}$ then $|V|^2>0$ for all simple objects $V\in {\mathcal C}$; therefore $\dim({\mathcal C})\ge 1$, and is $>1$ for any nontrivial ${\mathcal C}$. In particular, for any fusion category ${\mathcal C}$ one has $\dim({\mathcal C})\ne 0$.
:::

::: remark
Note that the second statement immediately follows from the first one, since ${\mathcal C}$ is always defined over a finitely generated subfield $k'$ of $k$, which can be embedded into ${\mathbb{C}}$.
:::

The proof of Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"}, which relies on Theorem [\[fourstars\]](#fourstars){reference-type="ref" reference="fourstars"} below, is given in Section 3. Theorem [\[fourstars\]](#fourstars){reference-type="ref" reference="fourstars"} is proved in Section 4.

::: remark
In the course of proof of Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"} we show that for any simple object $V$, the number $|V|^2$ is an eigenvalue of an integer matrix. In particular, if $k={\mathbb{C}}$ then $|V|^2$ is an algebraic integer. Thus, for $k={\mathbb{C}}$ Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"} actually implies that $|V|^2$ is a "totally positive" algebraic integer, i.e. all its conjugates are real and positive (since one can twist a fusion category by an automorphism of ${\mathbb{C}}$ and get a new fusion category). Similarly, $\dim({\mathcal C})$ is "totally" $\ge 1$, i.e. all its conjugates are $\ge 1$.
:::

One of the main tools in the proof of Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"} is

::: theorem
[]{#fourstars label="fourstars"} In any fusion category, the identity functor is isomorphic to the functor \*\*\*\* as a tensor functor.
:::

For the category of representations of a Hopf algebra, this result follows from Radford's formula for $S^4$ [@R1]. In general, it follows from the analog of Radford's formula for weak Hopf algebras, which was proved by the second author in [@N] (see Section 4).

::: definition
A pivotal structure on a fusion category ${\mathcal C}$ is an isomorphism of tensor functors $i:\text{Id}\to **$. A fusion category equipped with a pivotal structure is said to be a pivotal fusion category.
:::

We conjecture a stronger form of Theorem [\[fourstars\]](#fourstars){reference-type="ref" reference="fourstars"}:

::: conjecture
Any fusion category admits a pivotal structure.
:::

For example, this is true for the representation category of a semisimple Hopf algebra over $k$, since in this case by the Larson-Radford theorem [@LR2], the squared antipode is $1$ and hence $\text{Id}=**$. Furthermore, in Section 8 we will show that the conjecture is true for the representation category of a semisimple quasi-Hopf algebra.
