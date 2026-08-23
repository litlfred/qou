---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-007-25-translation-functors
section_title: "Translation functors"
section_number: 2.5
pages: 14-27
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
all i ∈ Z≥0 and ν will stay in ¯A0). Recall that there is a unique simple Uq-module Lq(ν) ∼= Tq(ν).
Denote by pλ : T → Tλ the projection onto the block Tλ functor. Similarly for µ.
Deﬁnition 2.32. (Onto and out of the wall) Given λ and µ, we deﬁne two functors via
T µ
λ : Tλ → Tµ, M ↦→pµ(M ⊗Q(q) Tq(ν)), T λ
µ : Tµ → Tλ, M ↦→pλ(M ⊗Q(q) Tq(ν)).
We call them translation onto the µ-wall T µ
λ and translation out of the µ-wall T λ
µ . ▲
Deﬁnition 2.33. (Through the wall) Deﬁne Θ λ
s = T λ
−1 ◦ T −1
λ and Θ λ
t = T λ
l−1 ◦ T l−1
λ . We call them
translation through the wall functors. ▲
If it is clear which λ we are using we, abusing notation, denote them by Θ s, Θ t.
Proposition 2.34. For all i ∈ Z≥0 we have the following.
(a) The functors T µ
λ and T λ
µ are well-deﬁned (their deﬁnition gives Uq-tilting modules in the
right blocks), adjoints (left and right) and exact. Thus,Θ λ
s and Θ λ
t are exact and self-adjoint.
(b) We have (recalling that Lq(µi) ∼
= Tq(µi))
T µ
λ (Tq(λi)) ∼=
{
Tq(µi−1) ⊕ Tq(µi+1), if µi > λ i,
Tq(µi) ⊕ Tq(µi), if µi < λ i, T λ
µ (Tq(µi)) ∼=
{
Tq(λi+1), if µi > λ i,
Tq(λi), if µi < λ i.
(c) The dead-end relations Θ λ
s (Tq(λ0)) ∼= 0, Θ λ
s (Tq(λ1)) ∼
= Tq(λ2), and Θ λ
t (Tq(λ0)) ∼
= Tq(λ1).
Moreover, we have
Θ λ
s or t(Tq(λi)) ∼
=
{
Tq(λi−1) ⊕ Tq(λi+1), if i > 1 is odd for s and even for t,
Tq(λi) ⊕ Tq(λi), if i > 0 is odd for t and even for s.
Here we set Tq(−1) = Tq(λ−1) = Tq(µ−1) = 0 . □
Note that biadjoint functors have in addition some other nice properties, see e.g. [32, Section 2].
Moreover, in the case µ = −1 we have µi > λ i iff i is odd whereas in the case µ = l − 1 we have
µi > λ i iff i is even as a look at (6) should convince the reader.
14
Proof. (a). The functors are well-deﬁned by (c) of Proposition 2.16 and p art (b) of Lemma 2.18,
i.e. tensor products of tiltings are tiltings. The other sta tements can be veriﬁed as in the case of
category O, i.e. we can adopt [24, Sections 7.1 and 7.2] without difﬁculties.
(b). Use Propositions 2.7 and 2.20, Corollary 2.8 and Theorem 2.23.
(c). This is just a direct application of the ﬁner list of statements given in (b). ■
We use the convention that Θ λ
k−tst denotes an alternating composition of length k of translation
through the wall functors starting with Θ λ
t . Likewise for Θ λ
k−sts. Using (c) of Proposition 2.34, we
get the following.
Corollary 2.35. (Combinatorics of the translation through the wall functors) We have:
(a) Θ λ
s ◦ Θ λ
s ∼= Θ λ
s ⊕ Θ λ
s and Θ λ
t ◦ Θ λ
t ∼= Θ λ
t ⊕ Θ λ
t as functors.
(b) We have for i ∈ Z≥0 even respectively odd, that (with k ≥ 0 terms Θ λ
t or s) there exist
multiplicities mj ∈ Z≥0 (that can be zero) such that
Θ λ
k−tstTq(λi) = (Θ λ
s or t ◦ . . . Θ λ
t ◦ Θ λ
s ◦ Θ λ
t )Tq(λi) ∼= Tq(λi+k) ⊕
⨁
j<i+k
Tq(λj)⊕mj ,
Θ λ
k−tstTq(λi) = (Θ λ
s or t ◦ . . . Θ λ
t ◦ Θ λ
s ◦ Θ λ
t )Tq(λi) ∼= Tq(λi−1+k)⊕2 ⊕
⨁
j<i−1+k
Tq(λj)⊕mj .
Similarly for i ∈ Z≥0 odd respectively even and Θ λ
k−sts. □
Proof. Clear from Proposition 2.34. ■
Deﬁne the following functors:
T µ,i
λ = pi ◦ T µ
λ , T λ,i
µ (Tq(µj)) =
{
δi,jTq(λi), if µ = −1, i even,
δi,jTq(λi), if µ = l − 1, i odd,
Θ λ,i
s or t =
{
pi ◦ Θ λ
s , if i is even,
pi ◦ Θ λ
t , if i is odd.
Here pi denotes the projection to the Tq(i)-part.
Deﬁnition 2.36. Given a Uq-tilting module T , denote by FT any functor FT ∼
= · ⊗ Q(q) T . A
functor F : T → T is called projective if it is a direct summand of functors of the form FT .
We denote by pEnd(T) the category of projective endofunctors F : T → T whose morphisms
HompEnd(T)(F , F ′) are natural transformations η : F → F ′. Moreover, we denote by pEnd(Tλ)
the category of projective endofunctors F : Tλ → Tλ that can be obtained via compositions and
countable direct sums of functors of the form Θ λ,i
s or t. Similarly for walls µ. Here we count the
empty sum as the identity functor. ▲
It follows from Lemma 2.37 below that these are actually categories. Moreover, by construction,
the translation through the wall functors Θ λ
s or Θ λ
t are objects in pEnd(Tλ), since
(8) Θ λ
s =
⨁
i∈Z≥1
Θ λ,2i
s , Θ λ
t =
⨁
i∈Z≥0
Θ λ,2i+1
s ,
as follows by Proposition 2.34. Similarly,
(9) T µ
λ =
⨁
i∈Z≥0
T µ,i
λ , T λ
µ =
{ ⨁
i∈Z≥0
T λ,2i
µ , if µ = −1,⨁
i∈Z≥0
T λ,2i+1
µ , if µ = l − 1.
15
Lemma 2.37. pEnd(T), pEnd(Tλ), pEnd(Tµ) are additive categories of exact functors. □
Proof. That pEnd(T) is closed under composition follows from part (b) of Lemma 2. 18, and the
identity functor is projective because of id ∼= · ⊗Q(q) Tq(0). Hence, pEnd(T) is a category. That
pEnd(T) is preserved under ﬁnite direct sums (showing that the categ ory is additive) follows
from part (a) of Lemma 2.18. The statement for the λ and µ versions follow by construction. Last,
that functors in pEnd(T) are exact follows because tensoring over a ﬁeld always respe cts exact
sequences. Likewise for the λ and µ versions which come from projections of such functors. ■
The following lemma is true in more generality (see for examp le [6, Chapter 4, Section 6]),
but we restrict to our case here. Recall that a functor betwee n additive categories F : C → D
is called indecomposable if any decomposition F ∼
= F1 ⊕ F 2 implies that F1 ∼= 0 or F2 ∼= 0.
Moreover, we call a category inﬁnite Krull-Schmidt if each object can be uniquely decomposed
(up to permutation) into a countably inﬁnite direct sum of indecomposable objects.
Lemma 2.38. A functor F ∼= · ⊗Q(q) T is indecomposable iff T is an indecomposable Uq-module.
Thus, pEnd(T) is Krull-Schmidt. In contrast, the λ and µ versions are inﬁnite Krull-Schmidt. □
Proof. Assume that T decomposes into T1 ⊕ T2. Then F ∼= (· ⊗Q(q) T1) ⊕ (· ⊗Q(q) T2). On the other
hand, by Yoneda and the tensor-hom adjunction, the T representing F is uniquely determined up
to isomorphism. Thus, a decomposition of F induces a decomposition ofT . This implies, by using
part (a) of Lemma 2.18, that pEnd(T) is Krull-Schmidt.
The statement for the λ and µ versions follow again by construction. ■
Proposition 2.39. The functors T µ,i
λ , T λ,i
µ and Θ λ,i
s or t are all indecomposable.
Proof. Any non-trivial decomposition Θ λ,i
s or t = F1 ⊕ F2 gives rise to a non-trivial idempotent
η ∈ pEnd(Θ λ,i
s or t). By using Proposition 2.34 together with Corollary 2.31 we s ee that such a
natural transformation can not exist (most of the Uq-intertwiners are nilpotent). Let us illustrate
this in an explicit calculation for Θ λ,i
t with i ⁄= 0. Applying Θ λ,i
t on the sequence
(10) Tq(i − 1)
ui−1 /d47/d47
Tq(i)
di
/d111/d111
ui /d47/d47 Tq(i + 1 )
di+1
/d111/d111
gives us (with bottom and top row given by applying Θ λ,i
t to (10))
Tq(i)

0
1


/d47/d47
/d79/d79
ηTq (i− 1)
/d15/d15
Tq(i) ⊕ Tq(i)
(
1 0
)
/d47/d47
(
1 0
)/d111/d111 /d79/d79
ηTq (i)
/d15/d15
Tq(i)
0
1


/d111/d111
/d79/d79
ηTq (i+1)
/d15/d15
Tq(i)

0
1


/d47/d47
Tq(i) ⊕ Tq(i)
(
1 0
)
/d47/d47
(
1 0
)/d111/d111 Tq(i).
0
1


/d111/d111
(11)
Here we used Proposition 2.34 to calculateΘ λ,i
t (Tq(i)), while the images of theUq-intertwiners can
be calculated as in Example 3.15. Note that η above is assumed to be a natural transformation, i.e.
all squares in (11) commute. Now, under the assumption that η is an idempotent, we have ηTq(i−1)
16
equals 0 or 1 because of Corollary 2.31. In the ﬁrst case we obtain that all others components
of η are zero as well, while in the second case we obtain that all ot hers components of η are
the identity as well (both follow via direct computation usi ng Corollary 2.31, the assumption that
all components of η are idempotents and the commutativity of all squares in (11) ). The same
arguments and calculations show the claim for the functors Θ λ,i
s and T µ,i
λ (except that our job is
even easier for the latter since all involved tiltings are si mple). The claim for the functor T λ,i
µ is
left to the reader. This shows the statement. ■
Remark 2.40. The category pEnd(Tλ) is the Karoubi envelope (in the sense of Deﬁnition 4.2) of
the category pEndΘ (Tλ) generated (via direct sums and compositions) by the translation through
the wall functors Θ λ
s or t. This follows from (8) and Proposition 2.39. We call pEnd(Tλ) the cate-
gory of projective endofunctors although it would be historical more accurate to call pEndΘ (Tλ)
the category of projective endofunctors. This convention i s due to the fact that, in contrast to the
case of category O (see e.g. [9]), our buildings blocks are the various Θ λ,i
s or t and not the functors
Θ λ
s or t themselves. ▲
3. T HE KHOVANOV-SEIDEL QUIVER ALGEBRA AND GRADINGS
In the present section 6 we identify the quiver for the blocks Tλ. We show how the quiver
description can be used to deﬁne a grading on T. We obtain a grading on pEnd(T) as well.
Additionally, we show how the translation functors ofTλ can be used to get a categoriﬁcation of
the action of the braid group on the (split) Grothendieck group of Tλ which realizes the Burau rep-
resentation on the (split) Grothendieck group. Moreover, w e show how the category of projective
endofunctors on Tλ can be used to categorify (parts of) the Temperley-LiebQ(v)-algebras (where
the grading decategoriﬁes to the indeterminate v).
By an algebra we always mean an associative, but not necessarily unital Q(q)-algebra.
3.1. The quiver algebras Qm and Q∞. Let m ∈ Z≥0. We consider the following quiver
(12) •m dm
/d47/d47
•m−1
um−1/d111/d111
dm−1
/d47/d47 •m−2
um−2/d111/d111
dm−2
/d47/d47 · · ·
um−3/d111/d111
d3
/d47/d47 •
2
u2/d111/d111
d2
/d47/d47 •
1
u1/d111/d111
d1
/d47/d47 •
0
u0/d111/d111
having m + 1 vertices 0, 1, . . . ,m and 2m arrows called up and down:
ui : i → i + 1 , i = 0, . . . , m− 1, d i : i → i − 1, i = 1, . . . , m.
The path algebra Pm of the quiver from (12) is deﬁned to be theQ(q)-algebra whose underlying
Q(q)-module is the Q(q)-vector space spanned by all ﬁnite paths with multiplicatio n given by
composition of paths if possible and zero otherwise.
Recall that a Z-graded Q(q)-algebra A (or simply graded) is a Q(q)-algebra A = ⊕i∈ZAi such
that AiAj ⊂ Ai+j for all i, j ∈ Z. The path algebra Pm is a graded Q(q)-algebra7, that is
Pm =
⨁
k∈Z≥0
P k
m, with P k
m = {All paths in Pm of length k},
since we clearly have P k
m ◦ P k′
m ⊂ P k+k′
m . We write l(·) for the grading on Pm (the “length”).
6We use right modules in this section and read from right to left: we think o f the paths in the quiver as applying
morphisms/functors. The reason for this will become clear in Subsection 3.4.
7Note that Khovanov and Seidel use free Z-modules instead of Q(q)-vector spaces. In order to avoid too many
different overlapping notations, we only use the Q(q)-vector space version, but it is not a big problem to work overZ.
17
Deﬁnition 3.1. (Khovanov-Seidel’sm-quiver algebra) Let Qm denote the quotient algebra ob-
tained from the path algebra Pm for the quiver from (12) by the deﬁning relations
ui ◦ ui−1 = 0 = di ◦ di+1, i = 1, . . . , m− 1, d i+1 ◦ ui = ui−1 ◦ di, i = 1, . . . , m− 1,
d1 ◦ u0 = 0.
The latter is called thedead-end relation. Given two paths p, p′ ∈ Qm we write p′p instead of p′ ◦ p.
The algebra Qm inherits the grading l(·) from Pm since all the relations are homogeneous. We call
Qm for short KS m-quiver algebra. ▲
We denote, by abuse of notation, the path of length0 that starts and ends at i also by i. Note that
the i are projectors or idempotents, because ii = i, pi = p if p starts in i and 0 else and ip = p if p
ends in i and 0 else. Moreover, they form a complete set of pairwise orthogonal idempotents, that
is 1 = 0 + 1 + · · · + m and ij = δ(i, j), where 1 ∈ Qm is the unit. Note that 0 ⁄= 0, 1 ⁄= 1 and the
i’s are not central form > 0, since e.g. 0 = iui ⁄= uii = ui for i = 0, . . . , m− 1.
Moreover, we denote for i = 1 , . . . , m by εi = ui−1di the loop that starts at i and goes via di
to i − 1 and then back via ui−1. Note that the relations imply that εi = di+1ui (if possible, i.e.
if i + 1 ≤ m). Thus, the Q(q)-algebra Qm has a basis given by i (for i = 0 , . . . , m) and ui (for
i = 0, . . . , m− 1) and di, εi (for i = 1, . . . , m) with l(i) = 0 , l(ui) = l(di) = 1 and l(εi) = 2 .
We call an algebra homomorphism f : A → B between graded algebras A and B a homomor-
phism of graded algebras, if f (Ak) ⊂ Bk for all k ∈ Z. We have the following.
Lemma 3.2. There is a sequence of (non-unital!) inclusions of graded algebras
Q0
/d31 /d127 ι0 /d47 Q1
/d31 /d127 ι1 /d47 Q2
/d31 /d127 ι2 /d47 . . . ,
where ιm : Qm → Qm+1 is deﬁned by i, ui, di, εi ↦→i, ui, di, εi for all suitable indices i. □
Proof. This follows because Pm includes into Pm+1 and the set of relations for Qm is included in
the ones for Qm+1. That these morphisms respect the grading and are injective is immediate. ■
This motivates the following deﬁnition.
Deﬁnition 3.3. (Khovanov-Seidel’s∞-quiver algebra) Deﬁne Q∞ to be the inductive limit of
the sequence of inclusions of graded algebras from Lemma 3.2 , that is Q∞ = lim− →Qm. We call it
for short KS ∞-quiver algebra. ▲
Note that Q∞ is a graded Q(q)-vector space of countable dimension. Moreover, Q∞ is an
algebra with a complete set of pairwise orthogonal idempote nts {i | i ∈ Z≥0}, but Q∞ is a
non-unital algebra, since the unit would have to be an inﬁnite sum of the i’s. Such an algebra is
sometimes called idempotented.
Example 3.4. Q0 consists just of Q(q)-multiples of 0. The algebra Qm>0 can be visualized as
•m
εm
/d5/d5
dm
/d47/d47 · · ·
um−1/d111/d111
di+1
/d47/d47 •
i
εi
/d5/d5ui/d111/d111
di
/d47/d47 · · ·
ui−1/d111/d111
d3
/d47/d47 •
2
ε2
/d5/d5u2/d111/d111
d2
/d47/d47 •
1
ε1
/d5/d5u1/d111/d111
d1
/d47/d47 •
0
u0/d111/d111
The KS ∞-quiver algebra Q∞ can be visualized as
· · ·
di+1
/d47/d47 •
i
εi
/d5/d5ui/d111/d111
di
/d47/d47 · · ·
ui−1/d111/d111
d3
/d47/d47 •
2
ε2
/d5/d5u2/d111/d111
d2
/d47/d47 •
1
ε1
/d5/d5u1/d111/d111
d1
/d47/d47 •
0
u0/d111/d111
18
We point out that Q∞ only has one asymmetry coming from the dead-end relation. Moreover, Q∞
is graded by the path length l(·) due to the fact that Q∞ does not contain inﬁnite paths. ▲
In order to be able to also consider the semisimple blocks T−1 and Tl−1 of our category T,
we also introduce another quotient of the path algebra Pm, denoted by Qtriv
m , (and take a limit as
above). Since the corresponding module categories should b e semisimple, the quotient Qtriv
m is
rather trivial and we call it KS trivial m-quiver algebra.
Deﬁnition 3.5. (Khovanov-Seidel’s trivial m-quiver algebra) Let Qtriv
m denote the quotient al-
gebra obtained from the path algebra Pm for the quiver from (12) by the deﬁning relations
ui = 0 = di+1, i = 0, . . . , m− 1.
The algebra Qtriv
m inherits the grading l(·) from Pm, but this grading is trivial. Qtriv
m consists
only of orthogonal idempotents i for i = 0 , . . . , m. These idempotents form a set of pairwise
non-isomorphic, central, orthogonal idempotents which sh ows that Qtriv
m is a semisimple algebra.
Moreover, the algebra Qtriv
m is clearly isomorphic to Q(q) × · · · × Q(q) (with m + 1 factors).
As before we deﬁne Khovanov-Seidel’s trivial∞-quiver algebra via Qtriv
∞ = lim− →Qtriv
m . We note
that this can be visualized as
· · · •
i
· · · •
2
•
1
•
0
where we take the inductive limit as above. ▲
For convenience we set um = d0 = ε0 = 0 for all Qm and d0 = ε0 = 0 for Q∞ in the following.
3.2. Combinatorics of the graded, right Qm- and Q∞-modules. Recall that, if A denotes some
graded Q(q)-algebra, then a (right) A-module M is called Z-graded (or simply graded), if
M =
⨁
k∈Z
M k and M k · Ak′
⊂ M k+k′
.
An A-module homomorphism between graded modules f : M → N is called degree preserving,
if f (M k) ⊂ N k for all k ∈ Z and homogeneous (of degreed ∈ Z) if f (M k) ⊂ N k+d for all k ∈ Z.
We denote by Modgr-A the category of graded, ﬁnitely generated A-modules whose morphisms
from M to M ′ are given by
(13) HomModgr-A(M, M ′) =
⨁
s∈Z
HomA(M, M ′⟨s⟩)0,
where the zero should mean degree preserving morphisms and ⟨s⟩ denotes a shift as below. Thus,
all morphisms in Modgr-A are ﬁnite direct sums of homogeneous morphisms.
The endofunctor ·⟨s⟩: Modgr-A → Modgr-A, called shift8 by s ∈ Z sends the k − s-th degree
part of a module to the k-th of the shift M⟨s⟩, that is, M⟨s⟩k = M k−s.
We use similar notions for left modules (we denote such categ ories by e.g. A-Modgr) or pro-
jective modules (we denote such categories by e.g. pModgr-A). We only work in categories of
(graded) ﬁnitely generated (projective) modules.
Qm acts on itself from the right by pre-composition and from the left by post-composition of
paths. This makes a difference: let us denote by Pi the left ideal of Qm generated by i. Similar, iP
denotes the right ideal generated by i. We have as Q(q)-vector spaces
Pi = Q(q)i ⊕ Q(q)ui ⊕ Q(q)di ⊕ Q(q)εi, iP = Q(q)i ⊕ Q(q)ui−1 ⊕ Q(q)di+1 ⊕ Q(q)εi,
8In our convention a positive number shifts the degree up.
19
with homogeneous components of degree 0, 1, 1, 2 (from left to right).
The Pi and the iP are graded Qm-modules (left and right respectively) that can be visualized as
Pi = · · · •
i
εi
/d5/d5ui/d111/d111
di
/d47/d47 · · · , iP = · · ·
di+1
/d47/d47 •
i
εi
/d5/d5
· · ·.
ui−1/d111/d111
Thus, the Pi’s and theiP ’s are projective, since we have (as left, respectively right, Qm-modules)
Qm =
m⨁
i=0
Pi, Q m =
m⨁
i=0
iP.
Moreover, they are all indecomposable because they are the p rojective covers of the simple left,
respectively right, Qm-modules Li and iL obtained from Pi and iP by killing ui, di and εi respec-
tively ui−1, di+1 and εi. Furthermore, it is easy to see that all indecomposable left , respectively
right, Qm-modules are of the form Pi⟨s⟩, respectively iP ⟨s⟩, for some s ∈ Z: this follows directly
from the fact that Qm is ﬁnite-dimensional. Thus, all indecomposable projectiv e Qm-modules are
direct summands of Qm considered as a (left or right) Qm-module.
Example 3.6. One easily checks that the same is true for the corresponding notions for Q∞ and
that one gets a decomposition into iP ’s as follows (we have indicated the neighbouringiP ’s using
alternating colors and we for simplicity assume that the i below is odd)
· · ·
di+1
/d47/d47 •
i
εi
/d5/d5ui/d111/d111
di
/d47/d47 · · ·
ui−1/d111/d111
d3
/d47/d47 •
2
ε2
/d5/d5u2/d111/d111
d2
/d47/d47 •
1
ε1
/d5/d5u1/d111/d111
d1
/d47/d47 •
0
u0/d111/d111
We encourage the reader to draw the decomposition intoPi’s. Again, all ﬁnitely generated, graded
projective, indecomposable right Q∞-modules are, up to a shift, of the form iP . Same for the left
modules and the Pi’s. This can be deduced directly, but is true in more generality for idempotented
algebras, see for example [34, Proposition 5.3.1]. ▲
Similarly for Qtriv
m and Qtriv
∞ which decompose into the corresponding (left and right) mod ules
denoted by P triv
i and iP triv.
3.3. Endofunctors on pModgr-Qm and pModgr-Q∞. Set9 Bi = Pi ⊗Q(q) iP ⟨−1⟩for all indices
i = 1, . . . , m. Note that the Bi’s are gradedQm-bimodules with the tensor product p ⊗ p′ of degree
l(p ⊗ p′) = l(p) + l(p′) for p of degree l(p) and p′ of degree l(p′). We deﬁne functors
Ui : pModgr-Qm → pModgr-Qm, Ui = · ⊗Qm Bi for i = 1, . . . , m.
Note that we have
(14) i′P ⊗Qm Pi ∼=
{
Q(q)i ⊕ Q(q)εi, if |i − i′| = 0, Q(q)ui, if i′ − i = 1,
Q(q)di, if i − i′ = 1, 0, if |i − i′| > 1.
This can be easily seen by considering (here i = i′ as an example)
· · ·
di+1
/d47/d47
•
i
εi
/d5/d5
· · ·
ui−1/d111/d111 ⊗Qm · · · •
i
εi
/d5/d5ui/d111/d111
di
/d47/d47 · · · ,
9Note that we use a different convention than Khovanov and Seidel for the gradings by shifting iP down by one.
20
where we have illustrated the overlapping pieces of iP and Pi. This clearly implies
(15) Ui(i′P ) ∼=





iP ⟨−1⟩ ⊕ iP ⟨+1⟩, if |i − i′| = 0,
iP, if |i − i′| = 1,
0, if |i − i′| > 1.
We note that we can seei′P ⊗Qm Pi as a graded, rightQtriv
m -module where the action ofi kills every-
thing that does not start in i. Note that, in this notation, Q(q)i, Qui, Q(q)di and Q(q)εi are all one
dimensional Qtriv
m -modules concentrated in degrees 0, 1, 1 and 2 respectively. Hence, as graded,
right Qtriv
m -modules, Q(q)ui ∼= Q(q)i⟨+1⟩, Q(q)di ∼
= Q(q)i⟨+1⟩ and Q(q)εi ∼
= Q(q)i⟨+2⟩.
Corollary 3.7. The functors Ui : pModgr-Qm → pModgr-Qm satisfy the following.
(a) Ui ◦ Ui ∼= Ui⟨−1⟩ ⊕ Ui⟨+1⟩ for i = 1, . . . , m.
(b) Let i′ = i ± 1 such that i, i′ ∈ {1, . . . , m}. Then Ui ◦ Ui′ ◦ Ui ∼= Ui.
(c) Ui ◦ Ui′ ∼= 0, if |i − i′| > 1. □
Proof. This follows directly from (15). ■
Finally we set
Ueven =
⨁
1≤i,2i≤m
U2i, Uodd =
⨁
0≤i,2i+1≤m
U2i+1.
By Corollary 3.7 we see that
(16) Ueven ◦ Ueven ∼= Ueven⟨−1⟩ ⊕ Ueven⟨+1⟩, Uodd ◦ Uodd ∼= Uodd⟨−1⟩ ⊕ Uodd⟨+1⟩.
It is clear that we can easily adapt the deﬁnition of the Ui’s to the Q∞ case. We denote these
functors by U ∞
i for all i ∈ Z>0. These functors satisfy completely similar relations as before.
We also deﬁne U ∞
even and U ∞
odd completely analogously by taking the direct sum over alli ∈ Z>0.
The reader is still invited to check that these two satisfy similar relations as in (16).
We also reﬁne the deﬁnitions of the functors Ui by factoring through the category of graded
(right) Qtriv
m -modules which we denote by Modgr-Qtriv
m . To be precise, we deﬁne U t
i and U i
t via
U t
i : Modgr-Qm → Modgr-Qtriv
m , U t
i = · ⊗Qm Pi
U i
t : Modgr-Qtriv
m → Modgr-Qm, U i
t = · ⊗Q(q) iP ⟨−1⟩.
It is immediate that Ui = U i
t ◦ U t
i . We deﬁne even and odd versions of these reﬁnements as before
where we use U t
even and U even
t as notations (similar for the odd versions).
The following lemma can be seen, by Remark 3.16 below, as an analog of [57, Theorem 8.4].
Lemma 3.8. As graded functors: U t
i ⟨+1⟩is the right adjoint ofU i
t , U t
i is the left adjoint ofU i
t ⟨−1⟩.
Similar for the even/odd versions. The functors Ui, Ueven and Uodd are all graded self adjoint. □
Proof. This is a case-by-case check. We use that, as graded Q(q)-vector spaces, we have
(17) HompModgr-Qm(iP, i′P ) ∼=
{
Q(q)i ⊕ Q(q)εi, if |i − i′| = 0, Q(q)ui, if i′ − i = 1,
Q(q)di, if i − i′ = 1, 0, if |i − i′| > 1.
The isomorphism is given by mapping a path p on the right-hand side to the homomorphism
iP → i′P given by left multiplication (post-composition) with p. Note that this is a homogeneous
morphism of degree l(p).
21
We only prove thatU t
i ⟨+1⟩is the right adjoint of U i
t and leave the rest to the reader. To this end,
we have to show that there are isomorphisms of graded vector spaces
HompModgr-Qm(U i
t (Q(q)i), i′P ) ∼= HompModgr-Qtriv
m (Q(q)i, U t
i ⟨+1⟩(i′P )),
where we can restrict to check only for objects as above by add itivity. Note that we have three
cases depending on i − i′, since the case |i − i′| > 1 is clear.
i = i′. The left-hand side is HompModgr-Qm(iP ⟨−1⟩, iP ) ∼= Q(q)i⟨+1⟩ ⊕ Q(q)εi⟨+1⟩, which
follows from (17). Moreover, by (14) and the shift by +1, we get the same for the right side.
i′ = i + 1. The left-hand side gives HompModgr-Qm(iP ⟨−1⟩, i+1P ) ∼= Q(q)ui⟨+1⟩. This fol-
lows again by (17). The right-hand side gives, by (14) and the shift by +1, the same result.
i′ = i − 1. Similarly to the case i′ = i + 1.
Thus, we have an adjoint pair (U i
t , U t
i ⟨+1⟩). The other statements follow analogously. ■
The same holds, mutatis mutandis, for the inﬁnity versions as well.
3.4. Q∞ and the tilting category T. Recall that the category Tλ denotes the λ-block of T for λ
in the fundamental alcove A0, see Subsection 2.4. We ﬁx any such λ and denote everything using
the simpliﬁed notation without the λ’s. In particular, recall our notation from Deﬁnition 2.25 f or
the tilting generators Tq(∞ ) and Tq(≤ m). We denote by Tλ(≤ m) the full subcategory of Tλ
consisting of objects whose indecomposable summands are all from the set {Tq(λ0), . . . , Tq(λm)}
for some ﬁxed m ∈ Z≥0. We also use completely similar notations for the walls µ by indicating
this case with a superscript t.
Proposition 3.9. We have
EndUq (Tq(≤ m)) ∼= Qm and EndUq (Tq(≤ m)t) ∼= Qtriv
m ,
which are isomorphisms of Q(q)-algebras. □
Proof. We are going to construct these isomorphisms explicitly. Moreover, if we simply writei for
Tq(i), then we can visualize EndUq(Tq(≤ m)) using Proposition 2.30 for all m > 0 as
•m
εm
/d5/d5
dm
/d47/d47 · · ·
um−1/d111/d111
di+1
/d47/d47 •
i
εi
/d5/d5ui/d111/d111
di
/d47/d47 · · ·
ui−1/d111/d111
d3
/d47/d47 •
2
ε2
/d5/d5u2/d111/d111
d2
/d47/d47 •
1
ε1
/d5/d5u1/d111/d111
d1
/d47/d47 •
0
u0/d111/d111
Thus, we consider the (by Proposition 2.30 well-deﬁned) Q(q)-algebra homomorphism
φ : Qm → EndUq (Tq(≤ m)), ui ↦→ui, di ↦→di, εi ↦→εi
for all suitable indices i. Using Corollary 2.31 we see that this is an isomorphism. The case m = 0
and the “trivial case” cases are immediate which proves the statement. ■
The morphisms of EndUq (Tq(∞ )) are “matrices” f = ∏
i,i′∈Z≥0
fi′i with fi′i : Tq(i) → Tq(i′)
and each row consists only of ﬁnitely many non-zero entries ( this follows from Corollary 2.31).
Now Endfs
Uq (Tq(∞ )) should be the (non-unital) subalgebra ofEndUq (Tq(∞ )) of all matrices with
only ﬁnitely many non-zero rows, i.e.
Endfs
Uq (Tq(∞ )) ∼=
∞⨁
i,i′=0
HomUq(Tq(i), Tq(i′)).
Similarly, of course, in the “trivial” case.
22
Proposition 3.10. We have
Endfs
Uq (Tq(∞ )) ∼=
∞⨁
i,i′=0
HomUq(Tq(i), Tq(i′)) ∼= Q∞,
Endfs
Uq(Tq(∞ )t) ∼=
∞⨁
i,i′=0
HomUq(Tq(i)t, Tq(i′)t) ∼= Qtriv
∞ ,
which are isomorphisms of Q(q)-algebras. □
Proof. We only show the ﬁrst isomorphism since the other is clear. By using Corollary 2.31 and
the deﬁnition of Endfs
Uq(Tq(∞ )) from above we see that, for each f ∈ Endfs
Uq (Tq(∞ )), there
exists some m ∈ Z≥0 such that fi′i = 0 for i, i′ > m . Those matrices describe elements in
EndUq (Tq(≤ m)) by “forgetting” the parts for i, i′ > m. Thus, we have
Endfs
Uq(Tq(∞ )) ∼
= lim
− →EndUq (Tq(≤ m)).
By Proposition 3.9 we see that this implies
Endfs
Uq (Tq(∞ )) ∼= lim
− →Qm ∼
= Q∞.
This ﬁnishes the proof. ■
We are now able to relate Tλ(≤ m) to pMod-Qm and thus, Tλ to pMod-Q∞. We deﬁne
Tm : Tλ(≤ m) → Mod-Qm, Tm(M) = Hom Uq(Tq(≤ m), M),
T∞ : Tλ → Mod-Q∞, T∞(M) = Hom fs
Uq (Tq(∞ ), M) ∼=
∞⨁
i=0
HomUq (Tq(i), M),
for M in either Ob(T(≤ m)) or Ob(Tλ) respectively where the isomorphism follows from Propo-
sition 3.10. Similarly for the walls µ where we indicate the functors Tt
m and Tt
∞ (and everything
else) with superscripts t. We note that the hom-spaces above are right Qm-modules (or Q∞, Qtriv
m
or Qtriv
∞ -modules) by pre-composition.
Note that Θ s, Θ t ∈ Ob(End(Tλ)) from Deﬁnition 2.33 clearly descent to Tλ(≤ m) for all
m ∈ Z≥0. We denote these restrictions, by abuse of notation, also by Θ s, Θ t. Furthermore, recall
the notation Θ i
s or t for i ∈ Z>0 which are deﬁned via (pi projects to the Tq(i)-part)
Θ i
s or t =
{
pi ◦ Θ s, if i is even ,
pi ◦ Θ t, if i is odd .
We use the same conventions and notations in the ﬁnite case by killing everything above m.
Similarly: the functors T µ
λ and T λ
µ from Deﬁnition 2.32 also descent to the ﬁnite case where we
again denote them by the same symbols.
We consider the right side for the tilting embedding theorem (ﬁnite and inﬁnite) as ungraded
modules/functors. Moreover pMod always denotes categories of projective modules.
Theorem 3.11. (Tilting embedding theorem - ﬁnite version) We have the following.
(a) The functor Tm is fully faithful.
(b) The functor Tm sends objects M ∈ Ob(Tλ(≤ m)) to projective Qm-modules and is an
equivalence between Tλ(≤ m) and pMod-Qm.
23
(c) We have the following commuting diagram.
Tλ(≤ m)
Tm /d47/d47
Θ i
s or t
/d15/d15
pMod-Qm
Ui
/d15/d15
Tλ(≤ m) Tm
/d47/d47 pMod-Qm.
(d) We have the following commuting diagrams.
Tλ(≤ m)
Tm /d47/d47
Θ s
/d15/d15
pMod-Qm
Ueven
/d15/d15
Tλ(≤ m) Tm
/d47/d47 pMod-Qm
and
Tλ(≤ m)
Tm /d47/d47
Θ t
/d15/d15
pMod-Qm
Uodd
/d15/d15
Tλ(≤ m) Tm
/d47/d47 pMod-Qm.
(e) The same as in (a)+(b) works for the walls µ as well by using Tt
m.
(f) We have the following commuting diagrams.
Tλ(≤ m)
Tm /d47/d47
T −1
λ
/d15/d15
pMod-Qm
U t
even
/d15/d15
T−1(≤ m)
Tt
m
/d47/d47
pMod-Qtriv
m
and
Tλ(≤ m)
Tm /d47/d47
T l−1
λ
/d15/d15
pMod-Qm
U t
odd
/d15/d15
Tl−1(≤ m)
Tt
m
/d47/d47
pMod-Qtriv
m .
(g) We have the following commuting diagrams.
T−1(≤ m)
Tt
m /d47/d47
T λ
−1
/d15/d15
pMod-Qtriv
m
U even
t
/d15/d15
Tλ(≤ m) Tm
/d47/d47 pMod-Qm
and
Tl−1(≤ m)
Tt
m /d47/d47T λ
l−1
/d15/d15
pMod-Qtriv
m
U odd
t
/d15/d15
Tλ(≤ m) Tm
/d47/d47 pMod-Qm. □
Proof. We are careless with the indices in the proof and hope that thi s does not cause confusion.
All appearing indices should be such that everything below 0 or above m is deﬁned to be zero.
(a). By Proposition 2.20 part (c) and Lemma 2.18 part (a) it is enou gh to verify the statement
for M = Tq(i) for i = 0 , . . . , m. Moreover, by using Corollary 2.31 together with the discus sion
in Subsection 3.2, we get isomorphisms Tm(Tq(i)) = Hom Uq(Tq(≤ m), Tq(i)) ∼= iP . Thus, Tm
is fully faithful.
(b). From (a) by using the discussion in Subsection 3.2.
(c). This follows by combining Tm(Tq(i)) = Hom Uq (Tq(≤ m), Tq(i)) ∼= iP with (15) and part
(c) of Proposition 2.34.
(d). This follows directly from (c) and the deﬁnition of Ueven and Uodd.
(e). The “trivial” cases are clear.
(f). We do the left case here. Note that Tm(Tq(i)) ∼= iP . Thus, using (14), we see that
U even
t Tt
m sends Tq(i) to Q(q)i ⊕ Q(q)εi for even i and Q(q)ui−1 ⊕ Q(q)di+1 for odd i. This,
by the discussion in Subsection 3.3, is isomorphic as right Qtriv
m -modules to Q(q)i ⊕ Q(q)i and
Q(q)i − 1 ⊕ Q(q)i + 1 respectively. In addition, T −1
λ sends Tq(i) to Tq(µi) ⊕ Tq(µi) (for i even)
or to Tq(µi−1) ⊕ Tq(µi+1) (for i odd). These are then sent to Q(q)i ⊕ Q(q)i (for i even) respectively
Q(q)i − 1 ⊕ Q(q)i + 1 (for i odd).
(g): Analogously to (f). ■
24
Theorem 3.12. (Tilting embedding theorem - inﬁnite version) We have the following.
(a) The functor T∞ is fully faithful.
(b) The functor T∞ sends objects M ∈ Ob(T) to projective Q∞-modules and is an equiva-
lence between Tλ and pMod-Q∞.
(c) We have the following commuting diagram.
Tλ
T∞ /d47/d47
Θ i
s or t
/d15/d15
pMod-Q∞
U ∞
i
/d15/d15
Tλ T∞
/d47/d47 pMod-Q∞.
(d) We have the following commuting diagrams.
Tλ
T∞ /d47/d47
Θ s
/d15/d15
pMod-Q∞
U ∞
even
/d15/d15
Tλ T∞
/d47/d47 pMod-Q∞
and
Tλ
T∞ /d47/d47
Θ t
/d15/d15
pMod-Q∞
U ∞
odd
/d15/d15
Tλ T∞
/d47/d47 pMod-Q∞.
(e) The same as in (a)+(b) works for the walls µ as well by using Tt
∞.
(f) We have the following commuting diagrams.
Tλ(∞ )
T∞ /d47/d47
T −1
λ
/d15/d15
pMod-Q∞
U t
even
/d15/d15
T−1(∞ )
Tt
∞
/d47/d47
pMod-Qtriv
∞
and
Tλ(∞ )
T∞ /d47/d47
T l−1
λ
/d15/d15
pMod-Q∞
U t
odd
/d15/d15
Tl−1(∞ )
Tt
∞
/d47/d47
pMod-Qtriv
∞ .
(g) We have the following commuting diagrams.
T−1(∞ )
Tt
∞ /d47/d47
T λ
−1
/d15/d15
pMod-Qtriv
∞
U even
t
/d15/d15
Tλ(∞ ) T∞
/d47/d47 pMod-Q∞
and
Tl−1(∞ )
Tt
∞ /d47/d47T λ
l−1
/d15/d15
pMod-Qtriv
∞
U odd
t
/d15/d15
Tλ(∞ ) T∞
/d47/d47 pMod-Q∞. □
Proof. The proofs of (a)-(g) is similar to the proofs given in Theore m 3.11 by using arguments as
in Proposition 3.10. We leave it to the reader. ■
Remark 3.13. We encourage the reader to work out the translations onto and out of the wall
commuting diagrams similar to part (c) of the theorems above. ▲
We note the following corollary for completeness.
Corollary 3.14. For all λ, λ′ ∈ A 0 we have Tλ ∼= Tλ′. Thus,
T(≤ m) ∼=
l−2⨁
i=0
pMod-Qm ⊕
1⨁
i=0
pMod-Qtriv
m , T ∼
=
l−2⨁
i=0
pMod-Q∞ ⊕
1⨁
i=0
pMod-Qtriv
∞ ,
with semisimple categories pMod-Qtriv
m and pMod-Qtriv
∞ . □
25
Proof. This follows from Lemma 2.26 and Theorems 3.11 and 3.12 becau se the right-hand sides
are always the same independent of λ ∈ A 0. ■
Example 3.15. (How to compute the images of the translation functors on Uq-morphisms)
Combining the commuting diagrams of the Theorems 3.11 and 3. 12 we obtain an explicit way to
compute Θ s and Θ t not just on the Tq(i)’s (as we already know by part (c) of Proposition 2.34),
but also on the Uq-intertwiners in HomUq(Tq(i), Tq(i′)).
This follows by using (17) together with Θ s ↭ Ueven and Θ t ↭ Uodd. For example, given
u0 : Tq(0) → Tq(1), we can compute Θ t(u0) as follows. First note that T∞Θ t(Tq(0)) ∼= 1P and
T∞Θ t(Tq(1)) ∼= 1P ⊕ 1P by (15) and Theorem 3.12. By using (17) we see
Θ t(u0) =
(
0
id
)
: Tq(1) → Tq(1) ⊕ Tq(1).
We see that this is actually
Θ t(u0) =
(
0
id
)
: Tq(1) → Tq(1)⟨−1⟩ ⊕ Tq(1)⟨+1⟩,
by using the results we are going to explain in Subsection 3.5 . Indeed, the grading is very helpful
to calculate the images of the Uq-interwiners, e.g. Θ t(u0) can only be zero on the ﬁrst component,
since we will show that there will not be suitable Uq-intertwiners lowering the degree. ▲
Remark 3.16. Let g = slm+1 and p = p1 be a maximal parabolic subalgebra for S1 × Sm−1 (for
a deﬁnition see for example [24, Chapter 9]). Denote by Op the corresponding parabolic category
O (for a deﬁnition and some properties see e.g. [24, Section 9. 3]). Moreover, denote by Op
0 the
principle block. As Khovanov and Seidel show in [36, Proposi tion 2.9] there is an equivalence of
categories Op
0 ∼
= Mod-Qm. Thus, by Theorems 3.11 and 3.12, we see that Tλ governs Op
0 for
all m. Similarly for the projective endofunctors: as explained i n [36, below Proposition 2.9], the
functors Ui correspond to the translation through the i-th wall (note that, under the equivalence
above, the slm+1 has Weyl group generators s1, . . . , sm and therefore translation functors indexed
by i = 1 , . . . , m). Moreover, U t
i corresponds to the translation onto and U i
t corresponds to the
translation out off the wall functors. Hence, by Theorems 3.11 and 3.12, we can say that these are
governed by the combinatorics of T µ
λ , T λ
µ and Θ λ
s or t from our tilting case.
Another point is, as Khovanov and Seidel explain after [36, Proposition 2.9], that the path length
grading gives rise to a Koszul grading in the sense of [7] on the Qm’s, see also [58, Example 1.1].
The same holds for Q∞. This can either be seen “by hand” or by using a more general th eory for
(quotients of) not necessary ﬁnite quiver algebras that can be found for example in [45]. ▲
Remark 3.17. Khovanov and Seidel’s quiver is also related to Khovanov’s arc algebra H m (for
m even) that he introduced in [31] to give an algebraic interpr etation of Khovanov homology.
The arc algebra categoriﬁes the invariant tensors of V ⊗m where V is the two dimensional vector
representation of Uv. In addition, together with Chen he extended in [16] this cat egoriﬁcation
to the full tensor product V ⊗m by deﬁning a certain subquotient ∏
k Ak,m−k (this quotient can be
seen as the quasi-hereditary cover ofH m). All of these have a topological interpretation as algebras
consisting of cobordisms, see e.g. [16, Section 2], and they are graded by the Euler characteristic
of these cobordisms. As explained in [16, Section 3], the A1,m−1-part of this subquotient is graded
isomorphic to Qm. Thus, we see that T governs A1,m−1 for all m. Moreover, this gives a hint for a
generalization of our work: we think that analogs of the Theorems 3.11 and 3.12 can be proven for
certain subquotients of the sln generalizations of H m studied in e.g. [43], [44], [59] or [60]. ▲
26
