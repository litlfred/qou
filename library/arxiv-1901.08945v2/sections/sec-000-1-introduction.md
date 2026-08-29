---
doc_id: arxiv-1901.08945v2
doc_title: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
doc_brief: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group decomposes accordi ng to the char- acters of"
---
2. Torsion pairs and decompositions of derived categories 5
3. Gerbes 13
4. Twisted sheaves 16
5. The derived category of a gerbe 20
6. Semi-orthogonal decompositions for Brauer–Severi schemes 24
References 27
1. Introduction
The concept of a twisted sheaf goes back to Giraud and his formal treatment
of the Brauer group in terms of gerbes [Gir71, Section V.4]. During the last two
decades, twisted sheaves and their derived categories have gaine d a renewed interest,
starting with the thesis of C˘ ald˘ araru [C˘ al00], who studied moduli problems for semi-
stable sheaves on varieties, and the work by de Jong [ dJ04] and Lieblich [ Lie04,
Lie15] on the period–index problem for the Brauer group. For a survey o n later
developments, we refer to Lieblich [ Lie17, Section 4].
Although twisted sheaves have a rather elementary description in t erms of 2-
cocycles (cf. Remark 4.6), they are most naturally viewed as sheaves on gerbes
banded by diagonalizable groups (see Deﬁnition 4.4). Our ﬁrst result is the following
theorem on the decomposition of the derived category associated to such a gerbe,
generalizing a result by Lieblich [ Lie04, Section 2.2.4].
Theorem A (see Theorem 5.4). Let S be an algebraic stack and π : X → S a
gerbe banded by a diagonalizable group ∆ with character group A. Then taking the
2010 Mathematics Subject Classiﬁcation. Primary 14F05; Secondary 14A20.
Key words and phrases. Semi-orthogonal decomposition, Derived category, Gerbe, Brauer–
Severi variety, Algebraic stack.
1
2 DANIEL BERGH AND OLAF M. SCHN ¨URER
coproduct deﬁnes an equivalence
(1.1)
∏
χ ∈A
Dqc,χ (X)
∼
− →Dqc(X), (Fχ )χ ∈A ↦→
⨁
χ ∈A
Fχ,
of triangulated categories, where Dqc,χ (X) denotes the full subcategory of Dqc(X)
of objects with χ-homogeneous quasi-coherent cohomology (see Deﬁnition 4.2).
In the underived setting, a splitting similar as in the theorem above (s ee Theo-
rem 4.7) is a consequence of the well-known fact that quasi-coherent rep resentations
of ∆ split into subrepresentations corresponding to the characte rs of the group ∆.
The result by Lieblich is the decomposition in Theorem A in the special case
when S is a quasi-compact, separated scheme. He proves and uses the fa ct that in
this setting the obvious functor
(1.2) D(Qcoh( X)) → Dqc(X)
is an equivalence of categories [ Lie04, Proposition 2.2.4.6]. Note that, if the base S
is a scheme, the functor ( 1.2) only fails to be an equivalence in truly pathological
situations. However, as shown by Hall–Neeman–Rydh [ HNR18, Theorem 1.3], the
functor (1.2) fails to be an equivalence for large classes of algebraic stacks, inclu ding
the basic case when X is the classifying stack B GL n of the general linear group
(see Remark 5.10). In particular, this kind of argument cannot be used to obtain
the splitting of the derived category of one of the most fundament al examples of
gerbes banded by Gm — namely the gerbe of trivializations B GLn → B PGLn for
the universal Brauer–Severi scheme (see Remark 6.1).
In order to prove Theorem A, we study the more general problem whether suit-
able torsion pairs in abelian categories induce semi-orthogonal deco mpositions on
the level of derived categories. We achieve the following theorem of independent
interest.
Theorem B (see Theorem 2.7 and Theorem 2.22). Let B be a weak Serre subcat-
egory of an abelian category A. Let T and F be abelian subcategories of B forming
a torsion pair (T, F ) in B. Assume that
Extn
A(T,F ) = 0
for all objects T ∈ T , F ∈ F and all integers n. Then
Db
B(A) = ⟨Db
F (A), Db
T (A)⟩
is a semi-orthogonal decomposition. Furthermore, if the in clusion DB(A) ⊂ D(A)
satisﬁes some technical conditions on homotopy limits and c olimits formulated pre-
cisely in the statement of Theorem 2.22, then
DB(A) = ⟨DF (A), DT (A)⟩
is a semi-orthogonal decomposition.
The theory of gerbes, hinging on the theory of stacks, used to ha ve a reputa-
tion of being inaccessible, and Giraud’s book on non-abelian cohomolog y [ Gir71]
introducing them is notorious for being a hard read, even among exp erts. How-
ever, in recent years the theory of algebraic stacks has become a main stream part
of algebraic geometry, much owing to the excellent text books by La umon–Moret-
Bailly [LMB00] and Olsson [ Ols16], and to the Stacks Project [ SP19]. Moreover, as
explained in the thesis by Lieblich [ Lie04], only a small part of Giraud’s theory is
actually needed to develop a satisfactory theory of twisted sheav es. We illustrate
the eﬀectiveness of the language of gerbes by giving a short, simple and conceptually
appealing proof of the following theorem, which generalizes a result b y Bernardara
[Ber09, Theorem 4.1].
DECOMPOSITIONS 3
Theorem C (see Theorem 6.2 and Corollary 6.5). Let S be an algebraic stack
and π : P → S a Brauer–Severi scheme of relative dimension n over S. Let β ∈
H2(Sfppf, Gm) denote the Brauer class of π. Then, for any a ∈ Z, the category
Dqc(P ) admits a semi-orthogonal decomposition
(1.3) D qc(P ) = ⟨Da,..., Da+n⟩
into right admissible subcategories Di, where the category Di is equivalent to the cat-
egory Dqc,β i(S) of βi-twisted complexes on S (see Deﬁnition 5.1 and Remark 6.3).
Similarly, we have corresponding decompositions for the ca tegory of perfect com-
plexes, the category of locally bounded pseudo-coherent complexes and the singularity
category. In particular, we also have such a decomposition f or Db
coh(P ) when S is
Noetherian.
Bernardara’s result is the semi-orthogonal decomposition ( 1.3) in the case when
S is a Noetherian, separated scheme with the property that any pair of points
in S is contained in an open aﬃne subscheme (cf. Remark 6.6). Apart from our
Theorem A, the main ingredient in our proof of Theorem C is a classical result by
Orlov regarding a semi-orthogonal decomposition of the derived ca tegory of a pro-
jectivized vector bundle [ Orl92, Theorem 2.6], which we previously have generalized
to algebraic stacks using the technique of conservative descent [BS17, Theorem 6.7,
Corollary 6.8].
While ﬁnishing the manuscript, we were informed by Brown and Moulinos of a
result [ BM19, Theorem 3.1] which is similar to our Theorem C.
Outline. In Section 2, we work mostly in the general setting of derived categories
of abelian categories. This section contains the proof of Theorem B. In Section 3
and Section 4, we recall and collect some basic facts on gerbes, bandings and twis ted
sheaves which are scattered in the literature. We expect most of t hese results to
be well known to experts. In Section 5, we turn our attention to derived categories
of gerbes and twisted sheaves. We generalize some of the fundame ntal results by
C˘ ald˘ araru and Lieblich [C˘ al00, Lie04] to the case when we work over an algebraic
stack. Most notably we prove Theorem A. Finally, in the last section, we give a
brief summary on Giraud’s treatment of the Brauer group [ Gir71, Section V.4], and
use the theory to prove Theorem C.
Acknowledgments. The ﬁrst named author was partially supported by the Dan-
ish National Research Foundation through the Niels Bohr Professo rship of Lars
Hesselholt, by the Max Planck Institute for Mathematics in Bonn, an d by the DFG
through SFB/TR 45. The second named author was partially suppor ted by the
DFG through a postdoctoral fellowship and through SFB/TR 45.
Notation and conventions. If A is an abelian category, we write D( A) for its un-
bounded derived category. We write D ≤n(A) and D ≥n(A) for its full subcategories
of objects whose cohomology is concentrated in the indicated degr ees, where n ∈ Z.
The (intelligent) truncation functors on D( A) are denoted τ≤n andτ≥n. If E andF
are objects of D( A), we sometimes abbreviate Ext n
A(E,F ) := Hom D(A)(E, ΣnF ).
By a diagonalizable group we mean a diagonalizable group scheme over Spec Z
that is isomorphic to the spectrum of the group ring of a ﬁnitely gene rated abelian
group.
We use the deﬁnitions of algebraic space and algebraic stack given in t he stacks
project [ SP19, Tag 025Y, Tag 026O]. In particular, we do not impose any separat-
edness conditions. The algebraic stacks form a 2-category where each 2-morphism
is invertible. We will follow the common practice to often suppress 2-c ategorical
4 DANIEL BERGH AND OLAF M. SCHN ¨URER
details. For instance, we will usually simply write morphism of stacks ins tead of 1-
morphism of stacks, subcategory of the category of stacks inst ead of 2-subcategory
etc.
For the theory of quasi-coherent modules and derived categories in the context of
algebraic stacks, we basically follow the approach of Laumon–Moret -Bailly [LMB00,
Sections 12 and 13], which we now brieﬂy recapitulate. Let X be an algebraic stack.
We denote the topos of sheaves on the big fppf site over X byXfppf and the topos
of sheaves on the lisse–´ etalesite over X by Xlis-´ et. For τ ∈ { fppf, lis-´ et}, we let
Mod(Xτ, OX ) denote category of OX -modules in Xτ , and Qcoh( Xτ, OX ) the full
subcategory of quasi-coherent modules (see [ SP19, Tag 03DL]).
Remark 1.1. The categories Qcoh( Xτ, OX ) and Mod( Xτ, OX ) are Grothendieck
abelian categories [ SP19, Tag 0781]. In particular, since the inclusion functor
Qcoh(Xτ, OX )֒→Mod(Xτ, OX ) is colimit preserving, it admits a right adjoint.
This right adjoint is called the quasi-coherator.
The construction ( −)τ functorially associates an adjoint pair
(1.4) f ∗ :Yτ ⇄Xτ :f∗
of functors to any morphism f : X → Y of algebraic stacks. Moreover, the func-
tor f ∗ preserves ﬁnite products. In particular, the adjunction ( 1.4) induces an
adjunction
(1.5) f ∗ : Mod(Yτ, OY ) ⇄ Mod(Xτ, OX ) :f∗.
Moreover, the pull-back functor f ∗ preserves quasi-coherence. The functor
(1.6) f∗ : Qcoh(Xτ, OX ) → Qcoh(Yτ, OY )
is deﬁned as the right adjoint of the restriction of f ∗ to quasi-coherent sheaves.
The existence of such a right adjoint is guaranteed by the quasi-co herator (see Re-
mark 1.1).
Remark 1.2. If τ = lis-´ et, then the functor ( 1.6) is the restriction of the push-
forward for sheaves of modules provided thatf is quasi-compact and quasi-separated,
but not in general. If τ = fppf, then ( 1.6) seldom is the restriction of the push-
forward for sheaves of modules.
The category Mod( Xτ, OX ) has a closed symmetric monoidal structure with
operations given by the usual tensor product and the sheaf hom f unctor. The tensor
operation preserves quasi-coherence and is preserved by pull-ba cks. In particular,
we get an induced symmetric monoidal structure on Qcoh( Xτ, OX ).
Remark 1.3. The symmetric monoidal structure on Qcoh( Xτ, OX ) induced by the
tensor product is also closed. This follows from the existence of the quasi-coherator
(see Remark 1.1). For τ = lis-´ et, the internal hom functor coincides with the sheaf
hom functor provided that the ﬁrst argument is of ﬁnite presenta tion, but not in
general.
There is an obvious restriction functor Xfppf →Xlis-´ et, which is compatible with
push-forward. This induces a monoidal equivalence
(1.7) Qcoh( Xfppf, OX )
∼
− →Qcoh(Xlis-´ et, OX ),
functorial in X (see [ SP19, Tag 07B1]).
We denote the derived category D(Mod(Xlis-´ et, OX )) simply by D(X). The cate-
gory Dqc(X) is deﬁned as the full subcategory of D( X) consisting of complexes with
quasi-coherent cohomology sheaves. The derived tensor produc t on D(X) preserves
objects in D qc(X), giving the latter category a symmetric monoidal structure, whic h
is closed.
DECOMPOSITIONS 5
Remark 1.4. The internal hom functor on D qc(X) is the restriction of the derived
sheaf hom functor provided that the ﬁrst argument is perfect, b ut not in general
(see [ HR17, Section 1.2]).
Given an arbitrary morphism f : X →Y of algebraic stacks, we have an adjoint
pair of functors
(1.8) f ∗ : D qc(Y ) → Dqc(X), f ∗ : D qc(Y ) → Dqc(X),
and the formation of such pairs is functorial.
Remark 1.5. The functor f ∗ in ( 1.8) coincides with the derived pull-back between
the ambient categories provided that f is smooth. For general f , the construction
of f ∗ is somewhat technical owing to the fact that the adjunction ( 1.4), for τ =
lis-´ et, does not form a morphism of topoi, as was ﬁrst noted by Beh rend [ Beh03,
Warning 5.3.12]. The construction is worked out by Olsson [ Ols07] in the bounded
case and by Laszlo–Olsson [ LO08, Example 2.2.5] in the unbounded case. We refer
to [ HR17, Section 1] for a concise summary on this.
Remark 1.6. The push-forward f∗ in (1.8) coincides with the derived push-forward
provided that f is concentrated [HR17, Deﬁnition 2.4, Theorem 2.6(2)], but not in
general.
Remark 1.7. It is also possible to construct D qc(X) using the topos Xfppf . This ap-
proach is taken in the stacks project [ SP19, Tag 07B6]. For τ = fppf the adjunction
(1.4) does give a morphism of topoi, making the construction of the pull-b ack in
(1.8) easier. On the other hand the inclusion Qcoh( Xfppf, OX ) ⊂ Mod(Xfppf, OX )
is not exact [ SP19, Tag 06WU], making the actual construction of D qc(X) quite
technical. We will not use this point of view in the present article.
Notation 1.8. We conclude this section by summarizing our notational conven-
tions regarding sheaves on stacks. In the discussion below, we let τ ∈ {fppf, lis-´ et}.
(a) We simply write Qcoh( X) for any of the categories Qcoh( Xτ, OX ) when
no distinction is necessary. This is motivated by the functorial equiv a-
lence ( 1.7).
(b) The monoidal operations on the categories
Qcoh(Xτ, OX ), Mod(Xτ, OX ), D(X), Dqc(X)
are always denoted − ⊗ − and Hom(−, −), respectively. In particular, we
omit any derived decorations. The precise category we are working on will
always be inferable from context. Note that in the cases Qcoh( Xτ, OX )
and D qc(X) the functor Hom does not always coincide with Hom on the
ambient category (cf. Remark 1.3 and Remark 1.4).
(c) The pull-backs and push-forwards along a morphism f : X →Y are always
denoted by f ∗ and f∗, respectively. Which of the categories
(−)τ, Mod((−)τ, O(−)), Qcoh((−)τ, O(−)),
D(−), Dqc(−),
we are working with will always be inferable from context. In particula r,
we do not use any derived decorations or any particular decoration s for
push-forward of quasi-coherent sheaves (cf. Remark 1.2 and Remark 1.6).
