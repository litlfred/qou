---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
Deﬁne the ‘center’ Z0(X) of a set X to be the monoid of all functions f : X → X (with
composition as product and the identity map as unit.) Then th e usual center Z1 ≡ Z of
the monoid Z0(X) is trivial: Z1(Z0(X)) = {idX}. The cardinality of Z0(X) is given by
#Z0(X) = # X #X. The aim of the present work is to prove 1-categorical analog ues of
these trivial set theoretic (= 0-categorical) observation s. (I owe the above deﬁnition of
Z0(X) to J. Baez.)
Given an arbitrary monoidal category (or tensor category) C its center Z(C) is a braided
monoidal category which was deﬁned independently by Drinfe l’d (unpublished), Majid [36]
and Joyal and Street [20]. (See Section 3 for the deﬁnition.) In order to avoid confusion
with another notion of center, we will write Z1(C) throughout. In the present work, as in
[36, 20], we will assume C to be strict, but this is exclusively for notational conveni ence.
The deﬁnition of the center Z1 and all results in this paper extend immediately to the
non-strict case. The other assumptions which we must make on C are more restrictive, but
we are still left with a class of categories which appears in c ontexts like low dimensional
topology and subfactor theory. We assume C to be linear over a ground ﬁeld which is
algebraically closed. Furthermore, C is semisimple with simple tensor unit and spherical
[6]. (A semisimple category is spherical iﬀ it is pivotal [6] (=sovereign) and every simple
object has the same dimension as its dual, cf. [38, Lemma 2.8] .) See [6] or [38, Section 2]
for the precise deﬁnitions.
Definition 1.1 Let C be a semisimple spherical tensor category with simple unit a nd let
Γ be the set of isomorphism classes of simple objects. If Γ is ﬁnite we deﬁne
dim C =
∑
i∈Γ
d(Xi)2,
otherwise we write dim C = ∞.
If C is ﬁnite dimensional and braided then the Gauss sums of C are given by
∆ ±(C) =
∑
i∈Γ
ω(Xi)±1d(Xi)2,
where θ(X) = ω(X)idX is the twist of the simple object X which is deﬁned by the spherical
structure [56].
We can now state our Main Theorem:
Theorem 1.2 Let F be an algebraically closed ﬁeld and C a spherical F-linear tensor
category with End (1) ∼= F. We assume that C is semisimple with ﬁnitely many simple
objects and dim C ⁄= 0 . Then also the center Z1(C) has all these properties and is a
modular category [53]. Furthermore, the dimension and the G auss sums are given by
dim Z1(C) = (dim C)2,
∆ +(Z1(C)) = ∆ −(Z1(C)) = dim C.
2
Deﬁning the center Z2(C) of a braided tensor category C to be the full subcategory whose
objects are those X which satisfy
c(X, Y ) = c(Y, X)−1 ∀Y ∈ Obj C,
one easily sees that Z2(C) is stable w.r.t. isomorphisms (thus replete), direct sums , re-
tractions, tensor products and duals, the inherited braidi ng obviously being symmetric.
One can show that a braided category satisfying the properti es in the theorem (i.e. a
premodular category [8]) is modular iﬀ the center Z2(C) is trivial, in the sense that all
objects of Z2(C) are multiples of the tensor unit. (This was done in [48] for ∗-categories
and in [7] for spherical categories with dim C ⁄= 0, see also Corollary 7.11 below.) Thus
Z2(Z1(C)) is trivial for all C as in the Main Theorem, which is the promised analogue of
the 0-categorical observation Z1(Z0(X)) = {1}.
The Main Theorem can be generalized slightly: If C is as before except for F not being
algebraically closed then there is a ﬁnite extension F′ ⊃ F such that Z1(C ⊗FF′) is modular.
Concerning the prospects of further generalizations the au thor is not optimistic. There is
little hope of proving semisimplicity of Z1(C) without assuming dim C ⁄= 0. (Furthermore,
it is known [53] that the dimension of a modular category must be non-zero.) In the
non-semisimple case one might hope to prove that the center o f a spherical noetherian
category satisﬁes the non-degeneracy condition on the the b raiding introduced in [33].
But the methods of this paper will most likely not apply.
The results of the present work can be considered as generali zations of known results
concerning Hopf algebras and we brieﬂy comment on this in ord er to put our results into
their context. We recall that the quantum double of a Hopf alg ebra was introduced,
among many other things, in Drinfel’d’s seminal work [11]. I n the following discussion
all Hopf algebras are ﬁnite dimensional over some ﬁeld F. The quantum double D(H)
of a Hopf algebra H is a certain Hopf algebra which contains H and the dual ˆH as
Hopf subalgebras and it is generated as an algebra by these. W e refrain from repeating
the well known deﬁnition and refer to [22] for a nice treatmen t. We only remark that
D(H) ∼= H ⊗F ˆH as a vector space, thus
dimF D(H) = (dim F H)2.
Furthermore, D(H) is quasitriangular, i.e. there is an invertible R ∈ D(H) ⊗ D(H) such
that σ ◦ ∆ = R∆( ·)R−1 where σ is the ﬂip automorphism of the tensor product. The
constructions of the quantum double of a Hopf algebra and of t he center of a monoidal
category are linked by the equivalence
D(H)-mod
⊗
≃br Z1(H-mod)
of braided monoidal categories, where H-mod and D(H)-mod are the categories of ﬁnite
dimensional left H- and D(H)-modules, respectively, the braiding of D(H)-mod being
provided by the R-matrix. Again, see [22, Chapter XIII.4] fo r a detailed account.
Now, the R-matrix of a quantum double D(H) is non-degenerate in a certain sense,
D(H) being ‘factorizable’ [49]. If H is semisimple and cosemisimple then D(H) is semisim-
ple [47]. It then turns out to be also modular and the category D(H)-mod of ﬁnite dimen-
sional left D(H)-modules is modular in the sense of Turaev [53]. (This was pr oved in [13]
3
for algebras over algebraically closed ﬁelds of characteri stic zero, but the latter condition
can be dropped. In the appendix we give a general proof.) Furt hermore, one clearly has
dim Z1(H-mod) = dim D(H)-mod = dim D(H) = (dim H)2 = (dim H-mod)2, (1.1)
where dim C is the dimension of the monoidal category C as deﬁned above.
It is now clear that our Main Theorem can be considered as an ex tension of the above
results to tensor categories which are not necessarily repr esentation categories of Hopf
algebras. Here one remark on the notation is in order. In [23] Kassel and Turaev intro-
duced a modiﬁed version of the construction of the center Z1(C) and called it the quantum
double D(C), see also [52]. Their category is the categorical version o f a construction of
Reshetikhin (which adjoins a certain square root θ to a quasitriangular Hopf algebra H in
order to turn it into a ribbon algebra H(θ)) applied to a quantum double, cf. [23, Theorem
5.4.1]. In the context of [23] the starting point was that eve n if C is rigid this need not
be true for Z1(C), whereas the category D(C) is rigid. As we will see, spherical categories
(tensor categories with nice two sided duals) are better beh aved in the sense that their
centers Z1 are again spherical. In addition, whereas Z1(C) is modular for the categories
satisfying the conditions of our Main Theorem, this is never true for D(C)! This is why
we stick to the original deﬁnition Z1(C). Apart from writing Z1(C) instead of Z(C), we
do not attempt to change the established symbols, but we use t he expression ‘quantum
double’ as a synonym for Z1(C) rather than D(C).
Unfortunately, the work on Hopf algebras mentioned above pr ovides no clues on how to
prove Theorem 1.2. This is where subfactor theory enters the present story. Starting from
an inclusion N ⊂ M of hyperﬁnite type II 1 factors of ﬁnite index and depth, Ocneanu
[43] deﬁned an ‘asymptotic subfactor’ B ⊂ A:
B = M ∨ (M∞ ∩ M ′) ⊂ M∞ = A.
(Here N ⊂ M ⊂ M1 ⊂ M2 ⊂ . . . is the Jones tower associated with N ⊂ M and
M∞ = ∨iMi.) In [45] he argued that a certain monoidal category associa ted with B ⊂ A is
braided, concluding that the asymptotic subfactor is an ‘an alogue’ of Drinfel’d’s quantum
double of a Hopf algebra. In fact, Ocneanu does not use catego ry language and does
not refer to the quantum double (center) of monoidal categor ies. In [15] Evans and
Kawahigashi published proofs for most of Ocneanu’s announc ements. In the paper [30],
which otherwise has little to do with the asymptotic subfact or, Longo and Rehren then
constructed a subfactor B ⊂ A from an inﬁnite factor M and a – in our language – ﬁnite
dimensional full monoidal subcategory C of End( M ) and conjectured that it is related
to Ocneanu’s construction. This conjecture was made precis e and proven in [37]. The
author’s involvement in the present story began when in 1998 he received a copy of a
short preprint [18] by M. Izumi. In the meantime a full accoun t of Izumi’s results has
appeared in [19]. In [18, 19] Izumi gives an in-depth analysi s of the LR-subfactor, in
particular its B − B sectors. Seeing [18] the present author was struck by the fac t that
its main theorem implicitly contained the deﬁnition of the c enter of a monoidal category.
In fact properly formulated, Izumi’s results provide a prec ise and completely general form
of Ocneanu’s ‘analogy’ between the asymptotic subfactor (o r the LR-subfactor) and the
quantum double, albeit the categorical one instead of the on e for Hopf algebras. In Section
8.3 we will rephrase Izumi’s results in categorical languag e to make this evident. Yet, this
is not the main purpose of the present work.
4
In [45] it has been argued that the braided monoidal category associated with B ⊂ A is
modular and a complete proof has been provided in [19], where it was also shown that the
dimension of the category in question is given by (dim C)2. As in our discussion of the Hopf
algebra quantum double, it is again natural to ask whether a p urely categorical version of
these results can be proven. Here we have to face the problem t hat ﬁnite-index subfactors
have a lot of ‘in-built’ categorical structure which is not a priori available in a purely
categorical setting. (In particular, most of [19] strongly relies on this structure.) Yet
this problem can be overcome once one realizes that the more a lgebraic part of subfactor
theory can be cast into the language of 2-categories. This is the content of [38], which
in a sense can be considered a continuation of [31], though in a somewhat more general
setting.
The paper is organized as follows. In Section 2 we ﬁrst recall some of the less standard
deﬁnitions from [38]. We then summarize the main results of [ 38] on Frobenius algebras in
tensor categories, related 2-categories and the notion of w eak monoidal Morita equivalence
of tensor categories. This section can by no means replace [3 8]. Our study of the quantum
double Z1(C) begins in Section 3, where we show that it preserves the clos edness w.r.t.
direct sums and subobjects and sphericity. Most importantl y and least trivially, we prove
the semisimplicity of Z1(C). These results do not yet rely on the machinery of [38]. In
Section 4 we prove the weak monoidal Morita equivalence Z1(C) ≈ C ⊗ F Cop, which in
particular implies that the double construction squares th e dimension of the category.
Section 5 is devoted to the proof of modularity of Z1(C), equivalent to triviality of the
category Z2(Z1(C)). As an important ﬁrst step we analyze the structure of the s imple
objects of the double, providing an explanation for Ocneanu ’s ‘tube algebra’. The next
two sections consider the case of categories with a positive ∗-structure ( C ∗-categories
or unitary categories) and the special case where C is already braided. In Section 8 we
consider applications to the invariants of 3-manifolds, pr oving a conjecture of Gelfand and
Kazhdan and speculating about a far stronger result. Finall y, we establish the link with
subfactor theory, relying heavily on Izumi’s work, improvi ng on it only slightly.
