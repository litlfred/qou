---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-015-54-the-non--case
section_title: "The Non-$*$ Case"
section_number: 5.4
pages: 36-37
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.99
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
Our starting point in this paper is a tensor $*$-category with direct sums, subobjects, conjugates and irreducible unit. From it we (re)construct a multiplier Hopf $*$-algebra with positive left invariant functional. Such algebras were called algebraic quantum groups (aqg) by Van Daele, who now prefers to speak of 'multiplier Hopf $*$-algebras with integrals'. We stick to 'algebraic quantum groups' mainly for the sake of definiteness and brevity. When $A$ is no longer a $*$-algebra and the invariant functional is required to be faithful rather than positive ($\varphi(ab)=0$ for all $a\in A$ implies $b=0$) we arrive at the notion of a regular multiplier Hopf algebras with left invariant functional. Essentially the entire theory works just as well in this setting, provided one adopts a modified notion of dual. We say a tensor category is rigid if every object $X$ comes with a chosen left dual $\overline{X}$ and morphisms $e_X: \overline{X}\otimes X\rightarrow{\bf 1}$ and $d_X: {\bf 1}\rightarrow X\otimes\overline{X}$ satisfying the triangular equations instead of the conjugate equations. In a semisimple category, left duals are automatically two-sided duals since dual morphisms $e'_X: {\bf 1}\rightarrow\overline{X}\otimes X$ and $d'_X: X\otimes\overline{X}\rightarrow{\bf 1}$ exist. Adopting the standard definition of semisimple categories as abelian categories with all exact sequences splitting, one can prove the following:

::: thm
[]{#t-nonstar label="t-nonstar"} Let ${\mathbb F}$ be an algebraically closed field (of arbitrary characteristic). Let ${\cal C}$ be a ${\mathbb F}$-linear semisimple rigid tensor category with $\mathrm{End}\,{\bf 1}\cong{\mathbb F}$ and let $E:{\cal C}\rightarrow\mathrm{Vect}_{\mathbb F}$ be a faithful tensor functor. Then there is a discrete regular multiplier Hopf algebra $(A,\Delta)$ with faithful left invariant functional $\varphi$ and an equivalence $F: {\cal C}\rightarrow\mathrm{Rep}(A,\Delta)$ such that $K\circ F=E$.
:::

The proof proceeds exactly as for $*$-categories, ignoring all references to the $*$-preserving property of $E$ and the $*$-involution of $A$. Again, existence, uniqueness and faithfulness of the invariant functional are proven using results due to Van Daele. Only the construction of the coinverse requires careful examination since the notion of dual is different.

We close with some remarks on the two different notions of discreteness applying to multiplier Hopf algebras. In analogy to the $*$-case, a regular multiplier Hopf algebra $(A,\Delta)$ with left invariant functional is called *discrete* if $A$ is a direct sum of finite dimensional matrix algebras over ${\mathbb F}$. In the non-$*$ case Proposition [\[p-disc\]](#p-disc){reference-type="ref" reference="p-disc"} fails, and $(A,\Delta)$ is said to be of *discrete type* iff there exists $0\ne h\in A$ such that $ah=\varepsilon(a) h$ for all $a\in A$. As in the $*$-case, $(A,\Delta)$ is of *compact type* or, equivalently, *compact* if $A$ has a unit. It is well known [@VD] that $(A,\Delta)$ is of discrete type iff $(\hat{A},\hat{\Delta})$ is of compact type.

Every discrete multiplier Hopf algebra has a copy of ${\mathbb F}$ as a direct summand, corresponding to the one-dimensional representation $\varepsilon$. The unit $I_0$ of this algebra has the property $aI_0=I_0a=\varepsilon(a)I_0$, thus a discrete multiplier Hopf algebra is of discrete type. The following characterizes discrete multiplier Hopf algebras, generalizing a well known result for finite dimensional Hopf algebras (which automatically possess integrals).

::: prop
[]{#p-disc2 label="p-disc2"} Let $(A,\Delta)$ and $(\hat{A},\hat{\Delta})$ be mutually dual regular multiplier Hopf algebras with faithful left invariant functionals. Then the following are equivalent:

1.  $(A,\Delta)$ is discrete.

2.  $(A,\Delta)$ is of discrete type and $h$ can be chosen to be idempotent.

3.  $(\hat{A},\hat{\Delta})$ is of compact type and $\hat{\varphi}(1)\ne 0$.
:::

*Proof. *The implication 1.$\Rightarrow$<!-- -->2. has been discussed before. Assuming 2., we have $h=hh=\varepsilon(h)h$, thus $\varepsilon(h)=1$. Conversely, if $\varepsilon(h)\ne 0$ then $h/\varepsilon(h)$ satisfies 2. Now, 2. implies that $(\hat{A},\hat{\Delta})$ is compact, and compactness implies the existence of $0\ne h\in A$ satisfying $xh=\varepsilon(x)h$ for all $x\in A$. By definition of the dual $(\hat{A},\hat{\Delta})$ and assuming the normalization $\varphi(h)=1$, we have $\hat{\varphi}(1)=\varepsilon(h)$, yielding the equivalence 2.$\Leftrightarrow$<!-- -->3. Now assume 3. holds. Then $(\hat{A},\hat{\Delta})$ is a Hopf algebra with left invariant functional $\hat{\varphi}$ satisfying $\hat{\varphi}(1)\ne 0$. By classical results, cf., e.g., [@swe 14.0.3] or [@abe Theorem 3.3.2], it follows that $(\hat{A},\hat{\Delta})$ is cosemisimple. This means that the ${\mathbb F}$-coalgebra $(\hat{A},\hat{\Delta},\hat{\varepsilon})$ is a direct sum of finite dimensional coalgebras. Since ${\mathbb F}$ is algebraically closed, every finite dimensional ${\mathbb F}$-coalgebra is a matrix coalgebra, i.e. it has a basis $\{a_{ij}, 1\le i,j\le n\}$ such that $\Delta(a_{ij})=\sum_l a_{il}\otimes a_{lj}$. Since $A=\{ \hat{\varphi}(\cdot a),\ a\in \hat{A}\}\subset\hat{A}^*$ and $\hat{\varphi}$ is faithful, $A$ has a basis $\{ b^\alpha_{ij}=\hat{\varphi}(\cdot a^\alpha_{ij}), \ \alpha\in I, 1\le i,j\le n_\alpha\in{\mathbb N}\}$. These elements multiply according to $b^\alpha_{ij}b^{\alpha'}_{i'j'}=\delta_{\alpha\alpha'}\delta_{ji'}b^\alpha_{ij'}$, thus $$A=\bigoplus_{\alpha\in I} M_{n_\alpha}({\mathbb F}),$$ as desired.

::: rema
1\. In the $*$-case, $\hat{\varphi}$ is positive and $1>0$, thus discrete type implies discreteness.

2\. We indicate how Proposition [\[p-disc2\]](#p-disc2){reference-type="ref" reference="p-disc2"} can be used to prove Theorem [\[t-nonstar\]](#t-nonstar){reference-type="ref" reference="t-nonstar"}. Given a semisimple tensor category ${\cal C}$ with embedding functor $E$, by [@ulb] there exists a Hopf algebra $H$ such that ${\cal C}\simeq\mathrm{Comod}\,H$. By [@swe 14.0.3], semisimplicity of ${\cal C}$ implies the existence of a left invariant functional $\hat{\varphi}$ on $H$, satisfying $\hat{\varphi}(1)\ne 0$. Thus $(H,\hat{\Delta})$ is a compact multiplier Hopf algebra with left invariant functional. Its dual $(A,\Delta)$ then is a discrete multiplier Hopf algebra with left invariant functional, and by Theorem [\[t-dualcor\]](#t-dualcor){reference-type="ref" reference="t-dualcor"} we have ${\cal C}\simeq\mathrm{Rep}_f(A,\Delta)$. However, the direct proof of Theorem [\[t-nonstar\]](#t-nonstar){reference-type="ref" reference="t-nonstar"} analogous to the proof of Theorem [\[t-main-equiv\]](#t-main-equiv){reference-type="ref" reference="t-main-equiv"} is more direct and instructive.
:::
