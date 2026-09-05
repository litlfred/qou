---
doc_id: arxiv-0707.3799v3
doc_title: "EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION"
section_id: sec-012-26-roman-bezrukavnikov-and-michael-finkelberg
section_title: "ROMAN BEZRUKAVNIKOV AND MICHAEL FINKELBERG"
section_number: 26
pages: 26-28
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
doc_brief: "EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION — 16 sections: ROMAN BEZRUKAVNIKOV AND MICHAEL FI; ROMAN BEZRUKAVNIKOV AND MICHAEL FI; ROMAN BEZRUKAVNIKOV AND MICHAEL FI"
---
ThusKis an Ind-object in the category of Harish-Chandra bimodules; moreover, it is
an algebra Ind-object in this monoidal category.
Proposition 4.We have a canonical isomorphism of algebra Ind-objects:F(D) ∼= K.
To prove Proposition we need another auxiliary
Lemma 14.We have a canonical isomorphismD◦S ∼= S◦C ˇG◦D, whereD,C ˇG
denote, respectively, Verdier duality and the functor induced by the canonical outer
automorphism of ˇGinterchanging conjugacy classes ofgandg −1,g∈ ˇG(the Chevalley
involution).
Proof: Recall that a monoidal categoryCis rigid if for any objectV∈Cthere
exists another objectV ∗∈Cand morphismsι:1→V⊗V ∗ andτ:V ∗⊗V→1
satisfying a certain compatibility constraint, see [14]. GivenV, an objectV ∗ together
with morphismsι,τis unique up to a unique isomorphism if it exists. Thus for a
rigid categoryCwe have a canonical (up to a canonical isomorphism) functorC7→C op
sendingVtoV ∗. It is immediate to check that monoidal categoriesPerv GO⋊Gm(Gr)
andHC fr
ℏ are rigid categories with duality functors given byC G◦DandDrespectively,
where the functorC G is induced by the Chevalley involution ofG. The equivalence
between the two categories intertwines the canonically defined dualities. Also, it is
well-known thatS◦C ˇG∼= CG◦Scanonically. The Lemma follows.□
Proof of Proposition 4.The Ind-objectDrepresents the functor
F7→H •
GO⋊Gm(D(F)). In view of Lemma 14 and Proposition 3(c) we see
that the Ind-objectF(D) represents the functorM7→κ ℏ(D(M)) on the category
of free asymptotic Harish-Chandra modules. It is straighforward to see from the
definitions that the Ind-objectKrepresents the same functor. The isomorphism
of functors yields an isomorphism of Harish-Chandra bimodules. Since the
isomorphism of functors is compatible with the monoidal structure, the isomorphism
of Harish-Chandra bimodules is compatible with the algebra structure.□
Proof of Theorem 3.By Propositions 3 and 4 we have an isomorphism of algebras
H GO⋊Gm
• (Gr) =H•
GO⋊Gm(D)∼=κℏ(K).
The latter is by definition the algebra of the quantum Toda lattice.□
6.5.Formality from purity.In this section we combine the above Ext computation
with a standard argument which allows one to derive formality of the RHom algebra
from purity of the Ext spaces. The result is a description of the derived Satake category,
including the version equivariant with respect to the loop rotation.
Except for some technical details, this section does not contain original contributions
of the authors.We have learned the geometric (respectively, algebraic) ideas exposed
here from V. Ginzburg (respectively, L. Positselski) around 1998.
In order to be able to use Frobenius weights we extend the basic setting, and consider
GO, Gr etc. over ¯Fq, and the categories of equivariantl-adic sheaves on Gr.
Consider the following general situation. LetRbe a finitely localized ring of integers
of a number fieldE, and letF q be a finite field quotient ofR. LetX R be a flat scheme
overRacted upon by a smooth affine group schemeG R, such that the set of orbits
EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION 27
is finite. We denote by (X ¯Fq,G ¯Fq) (resp. (X ¯E,G ¯E)) the base change of (X R,GR) to
a geometric point ofRoverF q (resp. over the generic point). We choose a primel
invertible inR. LetD G¯Fq
(X¯Fq) (resp.D G ¯E(X ¯E)) stand for the bounded equivariant
constructible derived category of ´ etaleQl-sheaves onX ¯Fq (resp.X ¯E) (see e.g. [6], 7.4).
We choose an isomorphism Ql≃k(under a technical assumption thatkhas the same
cardinality as Ql), and an embedding ¯E ,→C, and we denote by (X C,G C) the base
change of (X ¯E,G ¯E) toC. LetD GC(XC) (resp.D top
GC
(XC, Ql), Dtop
GC
(XC)) stand for the
bounded equivariant constructible derived category of ´ etale Ql-sheaves onX C (resp.
bounded equivariant constructible derived category of sheaves withQl-coefficients, resp.
k-coefficients,in the classical topologyofX C).
Proposition 5.There exists a localizationR (r) ofRsuch that for any pointR (r) ↠F q,
we have the following chain of natural equivalences:
DG¯Fq
(X¯Fq) α→D G ¯E(X ¯E)
β
→D GC(XC)
γ
→D top
GC
(XC, Ql) δ→D top
GC
(XC)
Sketch of proof.The argument is taken from [5], 6.1. The first equivalenceαis con-
structed in [5], 6.1.9 (existence of good models). To justify the finiteness assumptions
ofloc. cit.we note that the set of isomorphism classes ofG-equivariant irreducible per-
verse sheaves onXis finite. Since the equivariant derived categories are not considered
inloc. cit.we note that according to [6], 7.4, to compare the equivariant Exts between
equivariant irreducible perverse sheaves onXit suffices to compare the usual Exts
between the lifts of these sheaves toX×G n (see the canonical spectral sequence (312)
ofloc. cit.). These are calculated by the K¨ unneth formula.
The second equivalenceβis just the base change from ¯EtoC. The third equivalence
γis the classical M. Artin’s comparison theorem of ´ etale and classical cohomology,
see [5], 6.1.2(B′′). Finally,δis induced by our isomorphism Ql≃k.□
From now on we will restrict our attention to the equivariant derived categories in
our new setting, that is, over ¯Fq.
LetXbe an algebraic variety over a finiteF q, and letD(X ¯Fq) stand for the bounded
constructiblel-adic derived category ofX ¯Fq. LetFbe a pure weight zero object of
thel-adic derived category ofXof geometric origin. The space Ext i(F¯Fq,F ¯Fq) =L Exti
j(F¯Fq,F ¯Fq) carries a canonical grading by Frobenius weights; here the subindex
denotes base change to ¯Fq, and Ext i
j is the component of weightj. Recall that by
Deligne Theorem [13] Exti
j = 0 forj <i.
LetEbe a graded algebra andϕ:E→Ext •(F¯Fq,F ¯Fq)op be a homomorphism sending
a graded componentE i toExt i
i(F¯Fq,F ¯Fq).
We will consider the graded algebraEas a dg-algebra with zero differential.
Proposition 6.There exists a canonical functorΦ X :D perf (E)→D(X ¯Fq)sending
the free module toF ¯Fq and inducing the mapϕon Ext groups.
Sketch of proof.The complexF ¯Fq is semi-simple, i.e. is isomorphic to⊕IC i[di],
where ICi is an irreducible perverse sheaf andd i ∈Z. By Beilinson’s Theorem [4]
