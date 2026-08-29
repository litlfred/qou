---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-003-finite-semisimple-bimodule-categories-over-pivot
section_title: "Finite semisimple (bi)module categories over pivotal fusion categories"
section_number: null
pages: 9-9
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
We focus onfinite semisimple (C,D)-bimodule categories overfusion categoriesC,D and on (C,D)-bimodule
functors and natural transformations between them. In this case all categoriesFun(C,D)(M,N ) are finite
C-linear abelian categories [EGNO, Prop. 7.11.6] and semisimple, see [ENO05, Th. 2.16] by Etingof et al.
Moreover, the 2-category Bimod(C,D) of finite semisimple (C,D)-bimodule categories (C,D)-bimodule
functors and (C,D)-bimodule natural transformations is equipped with duals. Any(C,D)-bimodule functor
F :M→N between finite semisimple(C,D)-bimodule categories has a left adjointFl :N→M and a right
adjointFr :N→M , and these adjoints are also(C,D)-bimodule functors. The left and right duals ofF are
given by its left and right adjoint and the units and counits of the adjunction.
This follows, because module functors between finite semisimple module categories are always exact, as finite
semisimple module categories are exact and module functors between exact module categories are exact
[EGNO, Prop. 7.6.9]. Any finite abelianC-linear category is equivalent to the category of modules over some
finite-dimensional semisimple C-algebra [EGNO, Def. 1.8.5]. Any right exactC-linear functor between such
categories is⊗-representable [EGNO, Prop. 1.8.10] and hence has a left adjoint, namely the corresponding
Hom-functor. Analogously, left exactness implies the existence of a right adjoint.
It follows that categoryEndC(M) is a finite multifusion category. It is a fusion category if and only ifM is
indecomposable, that is, not the direct sum of non-trivial module categories, see [EGNO, Sec. 7.3.6] and the
remark after [EGNO, Def. 7.2.12]. The categoryM is an EndC(M)-module category with the action functor
that applies endofunctors and natural transformations to objects and morphisms inM.
We also require that the fusion categoriesC andD are pivotal. This has implications for the opposite bimodule
category from Example 1.6. A(D,C)-bimodule structure onMop can be defined analogously to Example
1.6 for any fusion categoryM. However, the categoryM## is in general not equivalent to the bimodule
categoryM, and one needs to distinguish the(D,C)-bimodule category structures onMop that are induced
by left and right duals, see the results by Douglas et al. in [DSS20, Sec. 2.4]. As shown in [S15], the pivotal
structures ofC andD relate their left and right duals and eliminate this ambiguity. This justifies the name
opposite bimodule category.
Proposition 1.12. [S15, DSS20]
LetC,D be pivotal fusion categories andM,N finite semisimple (C,D)-bimodule categories.
1. There are equivalences Ω : M## → Mof (C,D)-bimodule categories withF Ω = Ω F ## for all
(C,D)-bimodule functorsF :M→N .
2. There are equivalences of(C,D)-bimodule categoriesM#→ FunC(M,C) andM#→ FunDrev(M,D).
Proof. Claim 1. is shown in [S15]. As a functorΩ = idM, and its coherence isomorphisms are given by the
pivots ω :∗∗⇒ id as sc,m = ωc▷ 1m : c∗∗▷m→ c▷m and tm,d = 1m◁ω−1
d : m◁d→ m◁d∗∗. The
identityF Ω = ΩF ## follows directly from the definition ofF # in Example 1.10, 7. and formula(20) for the
coherence data of a composite bimodule functor.
Claim 2. is essentially [DSS20, Prop. 2.4.9] for module categories over pivotal fusion categories. It follows
by combining [DSS20, Prop. 2.4.9] with 1. The (D,C)-bimodule structure on FunC(M,C) is given by
(d▷F )(m) =F (m◁d) and (F◁c)(m) =F (m)⊗c and the one onFunDrev(M,D) by (d▷F )(m) =d⊗F (m)
and (F◁c)(m) =F (c▷m) for allc∈ ObC, m∈ ObM and d∈ ObD. The equivalences are given by the left
adjoints of the functors−▷m :C→M and m◁− :D→M from Example 1.10, 5. and 6.
