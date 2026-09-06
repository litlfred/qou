---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-003-21--category-basics
section_title: "-category basics"
section_number: 2.1
pages: 14-18
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
encodes the notion of a category whose morphisms form topologica l spaces and whose compositions
and associativity properties are deﬁned up to coherent homotopie s. The theory of ∞-categories
has many alternative formulations (see [Ber] for a comparison betw een the diﬀerent versions). We
will follow the conventions of [L1], which is based on Joyal’s quasi-categ ories [Jo]. Namely, an ∞-
category is a simplicial set satisfying a weak version of the Kan condit ion guaranteeing the ﬁllability
of certain horns. The underlying vertices play the role of the set of objects while the ﬁllable horns
correspond to sequences of composable morphisms. The book [L1 ] presents a detailed study of
∞-categories, developing analogues of many of the common notions o f category theory (an overview
of the ∞-categorical language, including limits and colimits, appears in [L1, Cha pter 1.2]). An
important distinction between ∞-categories and the more traditional settings of model categorie s
or homotopy categories is that coherent homotopies are naturally built into the deﬁnitions. Thus
for example, all functors are derived and the natural notions of lim its and colimits correspond to
homotopy limits and colimits. We will make essential use of the theory o f adjoint functors, monads
and Lurie’s extension [L2, 6.2.2] of the Barr-Beck theorem to the se tting of∞-categories.
Most of the ∞-categories that we will encounter are presentable [L1, 5.5] in the s ense that they
are closed under all small colimits (as well as limits, by [L1, Proposition 5 .5.2.4]), and generated
under suitable colimits by a small category. Examples include ∞-categories of spaces and of modules
over a ring. Presentable ∞-categories form an∞-categoryPr whose morphisms are left adjoints, or
equivalently by the adjoint functor theorem [L1, 5.2], functors tha t preserve all colimits [L1, 5.5.3].
An∞-category is stable [L2, 1.1,1.2] if it has a zero object, is closed under ﬁnite limits and
colimits, and pushouts and pullbacks coincide. Stable ∞-categories are an analogue of the additive
setting of homological algebra: the homotopy category of a stable ∞-category has the canonical
structure of a triangulated category [L2, 1.1.2]. We will denote by St⊂P r the full∞-subcategory
of stable presentable ∞-categories as studied in [L2, 1.4.5].
2.1.1. Ind-categories and compact generators. Recall that an object c of an∞-categoryC is compact
if the functor Hom C(c,−) preserves (small) colimits (see [L1, 5.3.4] for a detailed discussion).
Given a functor f :C→D between∞-categories, we will say
• f is continuous if it preserves all (small) colimits, and
• f is quasi-proper if it takes compact objects to compact objects.
We brieﬂy recall the properties of ind-categories from [L1, Section 5.3.5]. Given a small ∞-
categoryC which admits ﬁnite colimits, we may freely adjoin to C all small ﬁltered colimits. The
result is a new ∞-category IndC, called the ind-category of C, which is presentable (and so in
particular, admits all small colimits). By [L2, 1.1.3], if C is stable then so is Ind C. In general, Ind C
can be identiﬁed with the category of those presheaves on C taking ﬁnite colimits to ﬁnite limits
(and so in particular, it comes with an embedding C⊂ IndC).
Let us denote by st the∞-category of small stable ∞-categories that are idempotent-complete
[L1, 4.4.5] (see [BFN, 4.1] for a discussion). For C∈ st, we can recover C from its ind-category IndC
14
as the full ∞-categoryC≃ (IndC)cpt of compact objects of Ind C (see [L1, Lemma 5.4.2.4] or [L1,
5.3.4.17], and also Neeman [N1]).
This hints at the intimate relation between ind-categories and the cla ssical notion of compact
generation (see [L2, 1.4.5] and [L1, 5.5.7] for more details). A stable ∞-categoryC is said to be
compactly generated if it admits ﬁltered colimits and there is a small ∞-categoryC◦ of compact
objects ci∈C whose right orthogonal vanishes: if m∈C satisﬁes Hom C(ci,m )≃ 0, for all i, then
m≃ 0.
Note that an ind-category Ind C is automatically compactly generated (with compact objects the
objects of C). In fact, any compactly generated stable presentable ∞-categoryC can be identiﬁed
with the ind-category Ind Ccpt of its subcategory Ccpt⊂C of compact objects. This is a version of
a theorem of Schwede and Shipley [SSh] characterizing module categ ories for A∞-algebras (see [L2,
7.1.2] for the ∞-categorical version, and [Ke] for the diﬀerential graded versio n). More generally,
the functor Ind : st→St identiﬁes st with the subcategory of St consisting of compactly generated
∞-categories, and with morphisms quasi-proper continuous functo rs; a quasi-inverse is given by
C↦→C cpt.
2.1.2. Opposite categories and restricted opposites. We denote by C♦ the opposite category of an
∞-categoryC (reserving the superscript op for the opposite monoidal structure on algebras; see
Section 2.2 below). We will typically consider opposite categories for s mall categories only. For
C = IndCcpt a compactly generated ∞-category, we will work with the modiﬁed notion of the
restricted opposite category deﬁned by
C′ = Ind(C♦
cpt).
The terminology is motivated by that of the restricted dual of vect or spaces equipped with an extra
structure such as a grading.
Example 2.1. For the∞-category VectC of C-vector spaces, Vect C,cpt consists of perfect complexes
of C-vector spaces. Duality gives an identiﬁcation Vect C,cpt≃ Vect♦
C,cpt, which extends by continuity
to an equivalence Vect C≃ Vect′
C. Note that the plain opposite category Vect ♦
C is the ∞-category
of pro-ﬁnite dimensional vector spaces, which is quite diﬀerent fro m Vect′
C.
2.1.3. Adjoint and quasi-proper functors. We record here a couple of other useful statements.
Lemma 2.2. Let F :C ←→D : G denote an adjoint pair of functors of ∞-categories. If G is
continuous, then F is quasi-proper. Conversely, if C is compactly generated and F is quasi-proper,
then G is continuous.
Proof. See [DrG2, Proposition 1.2.4]. □
We will only need the following in the stable setting though it holds more g enerally.
Lemma 2.3. Let f :C←→D : g denote an adjoint pair of exact functors between small stabl e
∞-categories. Then the induced functors Indf : IndC←→ IndD : Indg are also adjoint.
Proof. The assertion follows immediately from the universal property [L1, Proposition 5.3.5.10] of
the Ind construction: for C a small stable ∞-category andD∈ St a presentable stable ∞-category,
there is an equivalence of ∞-categories
Ind : Fun ex(C,D) ∼ /d47/d47 FunL(IndC,D)
between the categories of continuous functors (equivalently, lef t adjoints) from Ind C toD and
functors fromC toD that preserve ﬁnite colimits. □
15
2.1.4. Reversing diagrams. The adjoint functor theorem has a very useful corollary that ena bles us
to calculate suitable colimits of∞-categories by turning them into (much simpler) limits. Recall that
given a small colimit-preserving (respectively, small limit-preserving accessible) functor F :C→D
between stable presentable∞-categories, the adjoint functor theorem provides a right (resp ectively,
left) adjoint. In other words, the opposite of the ∞-category St of stable presentable ∞-categories
with morphisms colimit-preserving functors is the∞-categoryStR of stable presentable∞-categories
with morphisms accessible limit-preserving functors (see ([L1, Coro llary 5.5.3.4] in the unstable
setting). Moreover, small limits of stable presentable ∞-categories are independent of context: the
forgetful functors
St /d47/d47 Cat∞ StR/d111/d111
to the ∞-category Cat ∞ of all ∞-categories preserve limits. Thus the limit of a diagram in St
consisting of limit-preserving functors can be calculated as the limit o f the same diagram regarded
inStR. In turn, the limit of a diagram in StR can be calculated as the colimit of the corresponding
diagram in St formed by the left adjoints.
2.2. Monoidal∞-categories and duals. A monoidal ∞-category as deﬁned in [L2, 4.1.1] is an
∞-category equipped with a homotopy coherent associative unital p roduct. Its homotopy category
is an ordinary monoidal category. An algebra object A in a monoidal ∞-category as deﬁned in [L2,
4.1.2] is an object equipped with a homotopy coherent multiplication. L eft and right module objects
over an algebra object are deﬁned similarly [L2, 4.2.2], with right module s identiﬁed with left
modules over the opposite algebra object Aop in the opposite monoidal ∞-category. There is a
relative tensor product ·⊗ A· of left and right modules given by the two-sided bar construction [L2 ,
4.3.4]. Monoidal ∞-categories, algebra objects in a monoidal ∞-category, and module objects over
an algebra object themselves form ∞-categories, some of whose properties (in particular, behavior
of limits and colimits) are worked out in [L2, 4.2].
The deﬁnition of a symmetric monoidal ∞-category is given in [L2, 2.0.0.7] modeled on the Segal
machine for inﬁnite loop spaces. Its homotopy category is an ordina ry symmetric monoidal category.
There is the notion of commutative algebra object A in a symmetric monoidal ∞-category such
thatA-modules form a symmetric monoidal ∞-category with respect to relative tensor product [L2,
4.4.2]. Given two associative algebra objects A,B , their monoidal product A⊗B carries a natural
associative algebra structure. Furthermore, any associative alg ebra object A is a left (as well as a
right) module object over the associative algebra A⊗Aop via left and right multiplication.
The∞-categoryPr of presentable ∞-categories and continuous functors carries a symmetric
monoidal structure introduced in [L2, 6.3.1]. The tensor product C⊗D of presentable C,D is a
recipient of a universal functor from the Cartesian product C×D which is “bilinear” (commutes
with colimits in each variable separately). In fact, the tensor produ ct lifts to a symmetric monoidal
structure in which the unit object is the ∞-category of spaces [L2, 6.3.1]. Furthermore, the sym-
metric monoidal structure is closed in the sense that Pr admits an internal hom functor compatible
with the tensor structure [L1, Remark 5.5.3.9], [L2, Remark 6.3.1.17]. T he internal hom assigns to
presentable∞-categoriesC andD the∞-category of colimit-preserving functors Fun(C,D) which is
presentable by [L1, Proposition 5.5.3.8].
The symmetric monoidal structure on the ∞-categoryPr of presentable ∞-categories restricts
to one on the full ∞-subcategory St⊂P r of stable presentable ∞-categories [L2, 6.3.2], [L2, 6.3.2].
The unit is the stable category, modules over the sphere spectrum . By [BFN, Proposition 4.4], the
functor Ind : st→St is in a natural way a symmetric monoidal functor
Ind(C1⊗C 2)≃ Ind(C1)⊗ Ind(C2)
for the natural symmetric monoidal structures on both sides.
A basic example of a symmetric monoidal stable ∞-category is Vect C, which underlies the dg
category of chain complexes of C-vector spaces. The rest of this paper takes place in the setting o f
the symmetric monoidal ∞-category
StC = Mod VectC(St)
16
of C-linear stable presentable ∞-categories, deﬁned as modules for Vect C in stable categories. The
category StC provides a model for the theory of diﬀerential graded categories over C (see [Co]
for the identiﬁcation of the corresponding homotopy theories). A s the category of modules over a
commutative algebra object (namely Vect C),StC inherits a symmetric monoidal structure itself with
unit VectC. All of the foundations and formal results for stable ∞-categories naturally translate to
the C-linear setting by base change to the commutative algebra Vect C.
2.2.1. Dualizability. Let A denote a monoidal ∞-category with monoidal product ⋆ and monoidal
unit 1 A. A key property for objects of A is dualizability (see [L2, Section 4.2.5]).
Deﬁnition 2.4. An object a∈ A of a monoidal ∞-category is left dualizable (respectively, right
dualizable) if there is an object ∨a (respectively,a∨) together with morphisms
coev : 1 A /d47/d47 ∨a⋆a ev :a⋆ ∨a /d47/d47 1A
so that the obvious compositions
a /d47/d47a⋆ ∨a⋆a /d47/d47a ∨a /d47/d47 ∨a⋆a⋆ ∨a /d47/d47 ∨a
are equivalent to the corresponding identity maps (respect ively,
coev : 1 A /d47/d47a⋆a ∨ ev :a∨⋆a /d47/d47 1A
satisfying analogous composition identities).
Note that the left dual of a∨ is again a, and the right dual of ∨a is again a, i.e., left and right
dualities are inverses of each other. For a symmetric monoidal ∞-categoryA, we will take advantage
of the natural identiﬁcation between the notions of left and right d uals and speak simply of the dual
a′.
One can reinterpret the notion of dualizable object in terms of adjo int functors: a∈ A is left
dualizable (respectively, right dualizable) if the functor ⋆a admits the left adjoint⋆∨a, or equivalently
the functor a⋆ admits the right adjoint ∨a⋆ (respectively, if the functor ⋆a admits the right adjoint
⋆a∨, or equivalently the functor a⋆ admits the left adjoint a∨⋆). Let us record this in the following
form for easy reference.
Lemma 2.5. For a right (respectively, left) dualizable object a in a monoidal ∞-categoryA we have
functorial identiﬁcations
HomA(a∨⋆b,c )≃ HomA(b,a⋆c ) Hom A(b⋆a,c )≃ HomA(b,c⋆a ∨)
which are monoidal in a.
Likewise, for an A-module category M and objects m,n∈M , we have a functorial identiﬁcation
HomM (a∨⋆m,n )≃ HomM (m,a⋆n )
where we write ⋆ for the A-action on M .
2.2.2. Dualizability of stable ∞-categories. We work with stable presentable C-linear categories StC
(or dg categories), though everything works in the general sett ing St over the sphere. As discussed
above, the ∞-category StC is naturally symmetric monoidal with unit the ∞-category Vect C of
chain complexes.
Proposition 2.6. SupposeC∈ St is compactly generated so that C = IndCcpt. Then C is dualizable
in St with dual the restricted opposite C′ = Ind(C♦
cpt).
Proof. See [G, Proposition 2.3.1]. □
17
2.2.3. Dualizability of modules. We will also require a slightly generalized notion of dualizablity,
which applies in the (non-monoidal) setting of modules over an associa tive algebra. Let A∈Alg(S)
denote an associative algebra in a symmetric monoidal ∞-categoryS with unit 1 S, and let C =
A⊗Aop -mod denote the ∞-category of A-bimodules in S.
Deﬁnition 2.7. An A-module M is said to be A-dualizable (respectively,S-dualizable) if there is
an Aop-module ∨M (respectivelyM ∨) together with morphisms
evL :M⊗S ∨M /d47/d47A inC coevL : 1 S /d47/d47 ∨M⊗AM inS
(respectively,
evR :M ∨⊗AM /d47/d47 1S inS coevR :A /d47/d47M⊗SM ∨ inC)
satisfying the usual identities.
Remark 2.8. The notion of dualizability for A-modules is perhaps more naturally seen as usual
dualizability for bimodules for algebra objects A andB (in the case B = 1 S), under the convolution
product on bimodules.
Recall (see [L3]) that by considering monoidal categories as 2-cate gories with a single object,
we can understand duality for objects in a monoidal category as a s pecial case of the notion of
adjoints in a 2-category. The above notion of duality for A-modules (or bimodules) has a similar
interpretation. Namely, we consider an A-module M∈C as a bimodule for A and the unit 1 S, and
thus as a morphism A→ 1S in the Morita (∞, 2)-categoryAlg(1)(S) of algebra objects in S. In this
interpretation, M is A- (respectively,S-) dualizable precisely when M admits a left (respectively,
right) adjoint.
We record here the following elementary compatibility of our previous deﬁnitions.
Lemma 2.9. AnA-moduleM∈ ModA(S) isS-dualizable if and only if the underlying object M∈S
is dualizable. In this case, the S-dual M ∨∈ ModAop(S) has underlying object the dual M ′∈S ,
compatibly with evaluation and coevaluation maps.
Proof. Suppose M isS-dualizable withS-dual M ∨. Then we can extend its evaluation morphism
ev :M⊗SM ∨ /d47/d47M⊗AM ∨ evR
/d47/d47 1S
where the ﬁrst map is the natural quotient, and its coevaluation mo rphism
coev : 1 S /d47/d47A coevR
/d47/d47M ∨⊗S M
where the ﬁrst map is the unit of the algebra A. It is straightforward to check that these exhibit
M ∨ as the plain dual of M .
Conversely, supposeM is dualizable with dual M ′. There is a canonical identiﬁcation of algebras
EndS(M ′)≃ EndS(M )op,
and so M ′ inherits a natural Aop-module structure. By construction, the evaluation ev descends to
provide the evaluation evR. Likewise, by adjunction, the coevaluation coev extends to provide the
A-bilinear coevaluation coevR. □
