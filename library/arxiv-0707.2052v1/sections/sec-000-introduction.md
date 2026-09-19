---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
The purpose of the present paper is to introduce the Mukai pai ring on the
Hochschild homology of smooth, proper spaces. This pairing is the natural
analogue, in the context of Hochschild theory, of the Poinca r´ e pairing on the
singular cohomology of smooth manifolds.
Our approach is categorical. We start with a geometric categ ory, whose
objects will be called spaces. For a space X we deﬁne its Hochschild homology
which is a graded vector space HH•(X) equipped with the non-degenerate
Mukai pairing. We show that this structure satisﬁes a number of properties ,
the most important of which are functoriality and adjointness.
The advantage of the categorical approach is that the techni ques we de-
velop apply in a wide variety of geometric situations, as lon g as an analogue
of Serre duality is satisﬁed. Examples of categories for whi ch our results ap-
ply include compact complex manifolds, proper smooth algeb raic varieties,
proper Deligne-Mumford stacks for which Serre duality hold s, representa-
tions of a ﬁxed ﬁnite group, and compact “twisted spaces” in t he sense of [3].
We expect the same construction to work for categories of Lan dau-Ginzburg
models [16], but at the moment it is not known whether Serre du ality holds
for these.
∗Mathematics Department, University of Wisconsin–Madison , 480 Lincoln Drive,
Madison, WI 53706–1388, USA, e-mail: andreic@math.wisc.edu
†Department of Pure Mathematics, University of Sheﬃeld, Hic ks Building, Hounsﬁeld
Road, Sheﬃeld, S3 7RH, UK, e-mail: S.Willerton@sheffield.ac.uk
1
The Hochschild structure
In order to deﬁne the Hochschild structure of a space we need n otation for
certain special kernels which will play a fundamental role i n what follows.
For a space X, denote by IdX and Σ− 1
X the objects of D(X × X) given by
IdX := ∆∗OX and Σ− 1
X := ∆∗ω− 1
X [− dim X],
where ∆ : X→ X × X is the diagonal map, and ω− 1
X is the anti-canonical line
bundle of X. When regarded as kernels, these objects induce the identit y
functor and the inverse of the Serre functor on D(X), respectively. We shall
see in the sequel that IdX can be regarded as the identity 1-morphism of X
in a certain 2-category V ar.
The Hochschild structure of the space X then consists of the following
data:
• the graded ring HH•(X), the Hochschild cohomology ring of X, whose
i-th graded piece is deﬁned as
HHi(X) := Homi
D(X×X)(IdX, IdX);
• the graded left HH•(X)-module HH•(X), the Hochschild homology mod-
ule of X, deﬁned as
HHi(X) := Hom− i
D(X×X)(Σ− 1
X , IdX);
• a non-degenerate graded pairing ⟨− , − ⟩M on HH•(X), the generalized
Mukai pairing.
The above deﬁnitions of Hochschild homology and cohomology agree
with the usual ones for quasi-projective schemes (see [5]). The pairing is
named after Mukai, who was the ﬁrst to introduce a pairing sat isfying the
main properties below, on the total cohomology of complex K3 surfaces [15].
Properties of the Mukai pairing
The actual deﬁnition of the Mukai pairing is quite complicat ed and is given
in Section 5. We can, however, extricate the fundamental pro perties of
Hochschild homology and of the Mukai pairing.
Functoriality: Integral kernels induce, in a functorial way, linear maps on
Hochschild homology. Explicitly, to any integral kernel Φ ∈ D(X × Y) we
associate, in Section 4.3, a linear map of graded vector spac es
Φ∗ : HH•(X)→ HH•(Y),
and this association is functorial with respect to composit ion of integral
kernels (Theorem 6).
2
Adjointness: For any adjoint pair of integral kernels Ψ ⊣ Φ, the induced maps
on homology are themselves adjoint with respect to the Mukai pairing:
⟨Ψ∗v, w ⟩M = ⟨v, Φ ∗w⟩M
for v ∈ HH•(Y), w ∈ HH•(X) (Theorem 8).
The following are then consequences of the above basic prope rties:
Chern character: In all geometric situations there is a naturally deﬁned ob-
ject 1 ∈ HH0(pt). An element E in D(X) can be thought of as the kernel
of an integral transform pt→ X, and using functoriality of homology we
deﬁne a Chern character map
ch : K0(X)→ HH0(X), ch(E ) = E∗(1).
For a smooth proper variety the Hochschild-Kostant-Rosenb erg isomor-
phism identiﬁes HH0(X) and ⨁
p Hp,p(X); our deﬁnition of the Chern char-
acter matches the usual one under this identiﬁcation [5].
Semi-Hirzebruch-Riemann-Roch Theorem: For E , F ∈ D(X) we have
⟨ch(E ), ch(F )⟩M = χ(E , F ) =
∑
i
(− 1)i dim Exti
X(E , F ).
Cardy Condition: The Hochschild structure appears naturally in the con-
text of open-closed topological quantum ﬁeld theories (TQF Ts). The
Riemann-Roch theorem above is a particular case of a standar d constraint
in these theories, the Cardy Condition. We brieﬂy discuss op en-closed
TQFTs, and we argue that the natural statement of the Cardy Co ndi-
tion in the B-model open-closed TQFT is always satisﬁed, eve n for spaces
which are not Calabi-Yau (Theorem 16).
The 2-categorical perspective
In order to describe the functoriality of Hochschild homolo gy it is useful to
take a macroscopic point of view using a 2-category called V ar. One way to
think of this 2-category is as something half-way between th e usual category
consisting of spaces and maps, and C at, the 2-category of (derived) cate-
gories, functors and natural transformations. The 2-categ ory V ar has spaces
as its objects, has objects of the derived category D(X × Y) — considered
as integral kernels — as its 1-morphisms from X to Y, and has morphisms
in the derived category as its 2-morphisms.
One consequence of thinking of spaces in this 2-category is t hat whereas
in the usual category of spaces and maps two spaces are equiva lent if they
are isomorphic, in V ar two spaces are equivalent precisely when they are
Fourier-Mukai partners. This is the correct notion of equiv alence in many
circumstances, thus making V ar an appropriate context in which to work.
3
This point of view is analogous to the situation in Morita the ory in which
the appropriate place to work is not the category of algebras and algebra
morphisms, but rather the 2-category of algebras, bimodule s and bimodule
morphisms. In this 2-category two algebras are equivalent p recisely when
they are Morita equivalent, which again is the pertinent not ion of equivalence
in many situations.
Many facts about integral transforms can be stated very eleg antly as
facts about the 2-category V ar. For example, the fact that every integral
transform between derived categories has both a left and rig ht adjoint is
an immediate consequence of the more precise fact — proved ex actly the
same way — that every integral kernel has both a left and right adjoint in
V ar. Here the deﬁnition of an adjoint pair of 1-morphisms in a 2-c ategory is
obtained from one of the standard deﬁnitions of an adjoint pa ir of functors
by everywhere replacing the word ‘functor’ by the word ‘1-mo rphism’ and
the words ‘natural transformation’ by the word ‘2-morphism ’.
The Hochschild cohomology of a space X has a very natural description in
terms of the 2-category V ar: it is the “second homotopy group of V ar based
at X”, which means that it is 2-HomV ar(IdX, IdX), the set of 2-morphisms
from the identity 1-morphism at X to itself. Unpacking this deﬁnition for
V ar one obtains precisely Ext•
X×X(O∆ , O∆ ), one of the standard deﬁnitions
of Hochschild cohomology. By analogy with homotopy groups, given a ker-
nel Φ : X→ Y, i.e., a “path” in V ar, one might expect an induced map
HH•(X)→ HH•(Y) obtained by “conjugating with Φ”. However, this does
not work, as the analogue of the “inverse path to Φ” needed is a simultane-
ous left and right adjoint of Φ, and such a thing does not exist in general
as the left and right adjoints of Φ diﬀer by the Serre kernels of X and Y.
The Hochschild homology HH•(X) of a space X can be given a similar
natural deﬁnition in terms of V ar — it is 2-HomV ar(Σ− 1
X , IdX) the set of 2-
morphisms from the inverse Serre kernel of X to the identity 1-morphism at
X. In this case, the idea of “conjugating by a kernel Φ : X→ Y” does work
as the Serre kernel in the deﬁnition exactly compensates the discrepancy
between the left and right adjoints of Φ.
The functoriality of Hochschild homology can be expressed b y saying
that HH• is a functor into the category of vector spaces from the Groth en-
dieck category of the 2-category V ar (i.e., the analogue of the Grothendieck
group of a 1-category) whose objects are spaces and whose mor phisms are
isomorphism classes of kernels. One aspect of this which we do not examine
here is related to the fact that this Grothendieck category i s actually a
monoidal category with certain kinds of duals for objects an d morphisms,
and that Hochschild homology is a monoidal functor. The Muka i pairing is
then a manifestation of the fact that spaces are self-dual in this Grothendieck
category. Details will have to appear elsewhere.
There is an alternative categorical approach to deﬁning Hoc hschild ho-
mology and cohomology. This approach uses the notion of enha nced tri-
angulated categories of Bondal and Kapranov [1], which are t riangulated
4
categories arising as homotopy categories of diﬀerential- graded (dg) cate-
gories. In [18], To¨ en argued that the Hochschild cohomolog y HH•(X) of a
space X can be regarded as the cohomology of the dg-algebra of dg-nat ural
transformations of the identity functor on the dg-enhancem ent of D(X). It
seems reasonable to expect that a similar construction can b e used to de-
ﬁne the Hochschild homology HH•(X) as dg-natural transformations from
the inverse of the Serre functor to the identity. However, si nce the theory
of Serre functors for dg-categories is not yet fully develop ed, we chose to
use the language of the 2-category V ar, where all our results can be made
precise.
String diagram notation
As 2-categories are fundamental to the functoriality, and t hey are fundamen-
tally 2-dimensional creatures, we adopt a 2-dimensional no tation. The most
apt notation in this situation appears to be that of string diagrams , which
generalizes the standard notation used for monoidal catego ries in quantum
topology. String diagrams are Poincar´ e dual to the usual ar row diagrams
for 2-categories. The reader unfamiliar with these ideas sh ould be aware
that the pictures scattered through this paper form rigorou s notation and
are not just mnemonics.
Note
This paper supersedes the unpublished paper [4], in which it was stated
that hopefully the correct categorical context could be fou nd for the results
therein. This paper is supposed to provide the appropriate c ontext.
Synopsis
The paper is structured as follows. The ﬁrst section is devot ed to the study
of integral transforms and of the 2-category V ar. In the next section we
review the Serre functor and Serre trace on the derived categ ory, and we use
these in Section 3 to study adjoint kernels in V ar. In Section 4 we introduce
the maps between Hochschild homology groups associated to a kernel, and
we examine their functorial properties. The Mukai pairing i s deﬁned in
Section 5, where we also prove its compatibility with adjoin t functors. In
Section 6 we deﬁne the Chern character and we prove the Semi-H irzebruch-
Riemann-Roch theorem. We conclude with Section 7 where we re view open-
closed TQFTs, and we discuss the Cardy Condition. An appendi x contains
some of the more technical proofs.
Notation
Throughout this paper k will denote an algebraically closed ﬁeld of charac-
teristic zero and D(X) will denote the bounded derived category of coherent
5
sheaves on X. Categories will be denoted by bold letters, such as C, and the
names of 2-categories will have a script initial letter, suc h as V ar.
The base category of spaces
We ﬁx for the remainder of the paper a geometric category, who se objects
we shall call spaces. It is beyond the purpose of this paper to list the axioms
that this category needs to satisfy, but the following categ ories can be used:
• smooth projective schemes over k;
• smooth proper Deligne-Mumford stacks over k;
• smooth projective schemes over k, with an action of a ﬁxed ﬁnite group
G, along with G-equivariant morphisms;
• twisted spaces in the sense of [3], i.e., smooth projective s chemes over
k, enriched with a sheaf of Azumaya algebras.
For any space X as above, the category of coherent sheaves on X makes
sense, and the standard functors (push-forward, pull-back , sheaf-hom, etc.)
are deﬁned and satisfy the usual compatibility relations.
Acknowledgments
We have greatly beneﬁted from conversations with Jonathan B lock, Tom
Bridgeland, Andrew Kresch, Aaron Lauda, Eyal Markman, Mirc ea Mustat ¸˘ a,
Tony Pantev, Justin Roberts, Justin Sawon, and Sarah Wither spoon. Many
of the ideas in this work were inspired by an eﬀort to decipher the lit-
tle known but excellent work [10] of Nikita Markarian. Greg M oore and
Tom Bridgeland suggested the connection between the Semi-H irzebruch-
Riemann-Roch theorem and the Cardy Condition in physics.
AC’s initial work on this project was supported by an NSF post -doctoral
fellowship, and by travel grants and hospitality from the Un iversity of Penn-
sylvania, the University of Salamanca, Spain, and the Newto n Institute in
Cambridge, England. AC’s current work is supported by the Na tional Sci-
ence Foundation under Grant No. DMS-0556042. SW has been sup ported
by a WUN travel bursary and a Royal Society Conference grant.
