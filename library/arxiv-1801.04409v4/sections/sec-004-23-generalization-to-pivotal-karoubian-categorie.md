---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-004-23-generalization-to-pivotal-karoubian-categorie
section_title: "Generalization to pivotal Karoubian categories"
section_number: 2.3
pages: 5-8
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.861
latex_coverage_ratio: 0.977
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
The above results generalize to pivotal tensor categories ([@EGNO], Subsection 4.7) such that $\dim^L X=0$ if and only if $\dim^R X=0$ for any indecomposable object $X\in \mathcal{C}$ (an example of such a category which is not spherical is the category of representations of the Taft Hopf algebra). Namely, in such a category, for any endomorphism $h: X\to X$ of an indecomposable object $X$, one has $\text{Tr}^L(h)=0$ if and only if $\text{Tr}^R(h)=0$. Thus, if $f: X\to Y$ is a morphism between arbitrary objects of $\mathcal{C}$, then the condition that for any $g:Y\to X$, one has $\text{Tr}^L(f\circ g)=0$ is equivalent to the condition that for any $g:Y\to X$, one has $\text{Tr}^R(f\circ g)=0$. One then defines $f$ to be negligible if any of these two equivalent conditions is satisfied. Then Lemma [\[charneg\]](#charneg){reference-type="ref" reference="charneg"}, Lemma [\[tensid\]](#tensid){reference-type="ref" reference="tensid"} and Proposition [\[semisi\]](#semisi){reference-type="ref" reference="semisi"} generalize verbatim, with analogous proofs.

Moreover, the above results also extend to the case when $\mathcal{C}$ is a Karoubian rigid monoidal category in which the trace of a nilpotent endomorphism is zero, a necessary condition for $\mathcal{C}$ to be embeddable into an abelian tensor category.[^1] For instance, the well-known construction of the fusion categories attached to a simple Lie algebra $\mathfrak{g}$ (in characteristic zero or $p$ bigger than the Coxeter number), [@EGNO], Subsection 8.18.2, starts with the category of tilting modules for the corresponding (quantum) group (which is Karoubian), and takes a quotient by the tensor ideal of negligible morphisms. Note that in this special case negligible morphisms happen to be those that factor through negligible objects (i.e., direct sums of simple objects of dimension $0$); this is not the case in general (e.g., for $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(\Bbb Z/p)$).

To summarize, we have the following result. Let $\mathcal{C}$ be a pivotal category, let $\dim^L(X):=\text{Tr}^L({\rm Id}_X)$, $\dim^R(X):=\text{Tr}^R({\rm Id}_X)$ for $X\in \mathcal{C}$, and call a morphism $f: X\to Y$ negligible if for any $g: Y\to X$ one has $\text{Tr}^L(f\circ g)=0$.

::: theorem
[]{#karpiv label="karpiv"} Let $\mathcal{C}$ be a ${\bold k}-$linear Karoubian rigid monoidal category such that all morphisms spaces are finite dimensional.[^2] Assume that $\mathcal{C}$ is equipped with a pivotal structure such that

\(1\) the left trace $\text{Tr}^L$ of any nilpotent endomorphism is zero;

\(2\) $\dim^L X=0$ if and only if $\dim^R X=0$ for an indecomposable $X\in \mathcal{C}$.

Then negligible morphisms are characterized as in Lemma [\[charneg\]](#charneg){reference-type="ref" reference="charneg"} and form a tensor ideal ${\mathcal N}(\mathcal{C})$. Moreover, $\mathcal{C}/\mathcal{N}(\mathcal{C})$ is a semisimple tensor category, whose simple objects are the indecomposable objects of $\mathcal{C}$ of nonzero dimension.
:::

::: proof
*Proof.* First of all, (1) implies that the right trace of any nilpotent endomorphism in $\mathcal{C}$ is zero, since $\text{Tr}^L(f)=\text{Tr}^R(f^*)$, see [@EGNO], Proposition 4.7.3.

Hence, for an endomorphism $h: X\to X$, $\text{Tr}^L(h)=0$ if and only if $\text{Tr}^R(h)=0$. Indeed, by decomposing $X$ into generalized eigenobjects of $h$, we may assume that $h=\lambda{\rm Id}+h_0$, where $h_0$ is nilpotent. Then $\text{Tr}^L(h)=\lambda \dim^L X$ and $\text{Tr}^R(h)=\lambda \dim^R X$ (as $\text{Tr}^L(h_0)=\text{Tr}^R(h_0)=0$), so our claim follows from (2).

The rest of the proof is parallel to the spherical abelian case. ◻
:::

::: example
[]{#ex1 label="ex1"} 1. If $\mathcal{C}$ is semisimple, then $\overline{\mathcal{C}}\cong\mathcal{C}$. Moreover, in this case for any tensor category $\mathcal{D}$ one has $\overline{\mathcal{C}\boxtimes \mathcal{D}}\cong\mathcal{C}\boxtimes \overline{\mathcal{D}}$.

2\. If ${\rm char}(\bold k)=p>0$ and $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits_{\bold k} (\Bbb Z/p)$ then $\overline{\mathcal{C}}$ is the Verlinde category ${\rm Ver}_p$ introduced by Gelfand-Kazhdan and Georgiev-Mathieu, see [@O] and references therein.

3\. Let ${\rm char}(\mathbf{k})=0$ and $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits GL(n|1)$, $n\ge 1$. Then $\overline{\mathcal{C}}=\mathop{\mathrm{Rep}}\nolimits(GL(n-1)\times GL(1)\times GL(1))\boxtimes {\rm Supervec}$, where ${\rm Supervec}$ is the category of supervector spaces, see [@H], Theorem 4.13.

4\. Let $G=({\mathbb Z}/2{\mathbb Z})^2$ and ${\rm char}(\mathbf{k})=2$. Then it is well known that indecomposable representations of $G$ over $\mathbf{k}$ of non-zero mod $2$ (i.e. odd) dimension are precisely $\Omega^n({\bf 1}), n\in {\mathbb Z}$, where $\Omega$ is the Heller shift operator, see e.g. [@B1 Theorem 4.3.3]. Also one deduces from [@B1 Corollary 3.1.6] that $$\Omega^n({\bf 1})\otimes \Omega^m({\bf 1})\simeq \Omega^{n+m}({\bf 1})\oplus \mbox{a projective module}.$$ Thus $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(G)}=\mathrm{Vec}_{\mathbb Z} =\mathop{\mathrm{Rep}}\nolimits GL(1)$.
:::

::: remark
1\. It is clear that if $\mathcal{C}$ is symmetric or braided, then so is $\overline{\mathcal{C}}$ and the functor $\bold S$.

2\. If $\mathcal{C}$ is finite then $\overline{\mathcal{C}}$ may be infinite (see Example [\[ex1\]](#ex1){reference-type="ref" reference="ex1"}(4)), and can, in fact, be unmanageably large, since the problem of classifying indecomposable objects in finite abelian categories is often wild (in fact, this is already so for $\mathop{\mathrm{Rep}}\nolimits_{\bold k}(\Bbb Z/p)^2$, where ${\rm char}(\bold k)=p>2$).
:::

::: remark
[]{#remhopf label="remhopf"} 1. Let $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits H$, where $H$ is a finite dimensional Hopf algebra over a field $\bold k$ of characteristic zero. Then condition (2) of Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"} (that $\dim^L X=0$ if and only if $\dim^R X=0$) holds for any pivotal structure. Indeed, we may assume that $\mathbf{k}=\Bbb C$. A pivotal structure on $\mathop{\mathrm{Rep}}\nolimits H$ is given by a grouplike element $g\in H$ such that $gxg^{-1}=S^2(x)$ for $x\in H$, and $\dim^L X=\text{Tr}_X(g)$, $\dim^RX=\text{Tr}_X(g^{-1})$. But $g$ has finite order, so the eigenvalues of $g$ are roots of unity, hence $\dim^R X=\overline{\dim^L X}$, as desired. We expect that the same holds for any finite tensor category over a field of characteristic zero.

However, the above condition can be violated for categories of finite dimensional modules or comodules over an infinite dimensional Hopf algebra. For example, let $\mathcal{C}$ be the category of finite dimensional representations of $U_q(\mathfrak{b})$, $q\in \Bbb C^\times$, where $\mathfrak{b}\subset \mathfrak{sl}_3$ is a Borel subalgebra. Recall that a pivotal structure on $\mathcal{C}$ is defined by the element $K=q^{2\rho}$. Let $X$ be the $U_q(\mathfrak{b})$ subrepresentation of the adjoint representation of $U_q(\mathfrak{sl}_3)$ (with highest weight $\alpha_1+\alpha_2$) spanned by the vectors whose weights are positive roots. Then $\dim^L X=2q^2+q^4$ and $\dim^R X=2q^{-2}+q^{-4}$. So if $q^2=-2$ then $\dim^L X=0$ but $\dim^R X=-3/4\ne 0$.

The same happens in characteristic $p$, even for a finite dimensional Hopf algebra. Namely, we can take the same example. Note that $q^2=-2$ is then a root of unity (or some order dividing $p-1$), so one may replace $U_q(\mathfrak b)$ with the corresponding small quantum group $\mathfrak{u}_q(\mathfrak{b})$.

2\. Condition (1) of Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"} holds true if $\mathcal{C}$ is an abelian tensor category, since the quantum trace is additive on exact sequences, see e.g. [@EGNO Proposition 4.7.5]. Moreover, assume that there exists a pivotal tensor functor $\mathcal{C}\to \mathcal{D}$, where the category $\mathcal{D}$ satisfies condition (1) of Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"} (e.g., $\mathcal{D}$ is abelian). Then obviously the category $\mathcal{C}$ also satisfies condition (1) of Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}. This observation was used by U. Jannsen to prove that the category of numerical motives is semisimple, see [@Ja]. Moreover, the assumption on finite dimensionality of morphism spaces in $\mathcal{C}$ in Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"} can be dropped if there exists a pivotal monoidal functor $F:\mathcal{C}\to \mathcal{D}'$, where all morphism spaces in $\mathcal{D}'$ are finite dimensional, since the tensor ideal of morphisms sent by $F$ to zero consists of negligible morphisms, which implies finite dimensionality of morphism spaces in $\mathcal{C}/\mathcal{N}(\mathcal{C})$.

Here is an example of such a situation. Take any collection of morphisms in a symmetric tensor category $\mathcal{D}$, compute some of relations between them, and define $\mathcal{C}$ to be the Karoubian envelope of the universal symmetric monoidal category generated by morphisms satisfying these relations. Then we have an obvious symmetric monoidal functor $\mathcal{C}\to \mathcal{D}$, hence the semisimplification of $\mathcal{C}$ is a semisimple symmetric tensor category.
:::

[^1]: Note that this condition is not necessarily satisfied: e.g. if ${\rm char}(\mathbf{k})=p$, $t\in \mathbf{k}$, and $\underline{\mathop{\mathrm{Rep}}\nolimits}_\mathbf{k}(S_t)$ is the Karoubian Deligne category of representations of $S_t$ ([@EGNO], Subsection 9.12) then this property holds only if $t\in \Bbb F_p\subset \mathbf{k}$; namely, if $\sigma$ is the cyclic permutation on $X^{\otimes p}$, where $X$ is the tautological object, then $(1-\sigma)^p=0$ but $\text{Tr}(1-\sigma)=t^p-t$.

[^2]: Note that any Karoubian linear category with finite dimensional morphism spaces satisfies the Krull-Schmidt theorem, which says that any object has a unique decomposition into a direct sum of indecomposables (up to a non-unique isomorphism); for this reason, such categories are sometimes called Krull-Schmidt categories.
