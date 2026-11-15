---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 9-15
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
The geometry of a smooth complex projective curve C with Jacobian
variety Jac(C) is governed, after the choice of a base point on the curve, by
the Abel-Jacobi morphism. In particular, the latter deﬁnes for each n ∈N
a morphism Cn = C ×···×C −→Jac(C) whose ﬁbres correspond to linear
series of divisors on the curve, and the loci where the ﬁbre dimension jumps
are the subvarieties W r
n ⊆Jac(C) of special divisors that have been studied
extensively in classical Brill-Noether theory [6].
For smooth complex projective varieties Y of higher dimension one still
has the Albanese morphism
fn :
Y n = Y ×···×Y −→X = Alb(Y),
but here the situation is much harder to describe in general. For example, the
image f1(Y) ,→X can have any dimension between zero and dim(X), and
there is no obvious substitute for Brill-Noether theory in general. In some
sense, the ﬁrst three chapters of this thesis provide a possible framework for
such a substitute. More speciﬁcally, the properties of fn we are interested
in (such as the loci on X where the ﬁbre dimension jumps) can be studied
via the higher direct images
Rifn∗(CY n)
for
i ≥0,
which are constructible sheaves in the sense that there exists a stratiﬁcation
of X into ﬁnitely many locally closed subvarieties over which they restrict
to locally constant sheaves. In general the geometry of these higher direct
image sheaves is rather involved, as we will see in a particular example in
chapter 5. However, we propose a simple description of such direct images
in terms of the representation theory of a reductive algebraic group that can
be attached to Y via the Tannakian formalism [33].
The basis for this Tannakian description will be a vanishing theorem for
constructible sheaves on abelian varieties which can be seen as an analog
of the Artin-Grothendieck afﬁne vanishing theorem [7, exp. XIV, cor. 3.2]
and contains as a special case the generic vanishing theorems of Green and
Lazarsfeld [47]. For any character χ : π1(X,0) −→C∗of the fundamental
group, let us denote by Lχ the corresponding local system on X. Then in
chapters 1 and 2 which are based on joint work with R. Weissauer [68],
1
2
Introduction
we show that for any constructible sheaf F on X and a sufﬁciently general
character χ one has
Hi(X,F ⊗C Lχ) = 0
for all
i > dim(Supp(F)).
An independent proof of this result has also been given by C. Schnell [94],
using the Fourier-Mukai transform for holonomic D-modules. Our proof
is of a different ﬂavour and is closely intertwined with the deﬁnition of the
Tannakian categories we are interested in. It is based on an abstract quotient
construction for semisimple tensor categories — we only use D-modules
at a single place in section 1.4 where we classify all perverse sheaves of
Euler characteristic zero (which will be precisely the objects which become
isomorphic to zero under the above quotient construction). At present we
do not know whether this classiﬁcation extends to algebraically closed base
ﬁelds of positive characteristic p > 0, but otherwise all our arguments also
work for l-adic constructible sheaves on abelian varieties over the algebraic
closure of a ﬁnite ﬁeld Fp for prime numbers l̸ = p.
Our Tannakian results are best formulated in the framework of perverse
sheaves which has its historic roots in the theory of D-modules [57] and
in the sheaf-theoretic construction of intersection cohomology for singular
varieties [10]. Let us for convenience brieﬂy recall some basic deﬁnitions
and notations from loc. cit. For any complex algebraic variety Z, we will
denote by Db
c (Z,C) the derived category of bounded C-sheaf complexes
whose cohomology sheaves are constructible for some stratiﬁcation of Z
into Zariski-locally closed subsets. This is a triangulated category, and one
can deﬁne the full abelian subcategory
Perv(Z,C) ⊂Db
c (Z,C)
of perverse sheaves to be the core of the middle perverse t-structure. More
explicitly, a sheaf complex K is said to be semi-perverse if its cohomology
sheaves H −i(K) satisfy the support estimate dim(SuppH −i(K)) ≤i for
all i ∈Z, and it is a perverse sheaf iff both K and its Verdier dual D(K) are
semi-perverse. For example, the perverse intersection cohomology sheaf is
by deﬁnition the intermediate extension
δZ = j!∗(CU[dim(Z)]) ∈Perv(Z,C)
where j : U ,→Z denotes the inclusion of a smooth open dense subset. This
perverse sheaf is self-dual with respect to Verdier duality, and it does not
depend on the choice of the smooth open dense subset. Thus for smooth
varieties Z the perverse intersection cohomology sheaf δZ coincides with
the constant sheaf up to a degree shift. If Z is a closed subvariety of X with
embedding i : Z ,→X, then the direct image i∗: Perv(Z,C) ,→Perv(X,C)
is a fully faithful functor, and in this case we will by abuse of notation also
write δZ for the perverse sheaf i∗(δZ) ∈Perv(X,C).
3
In the context of perverse sheaves, our above vanishing theorem can be
reformulated as the statement that for any perverse sheaf P ∈Perv(X,C)
and a general character χ : π1(X,0) −→C∗the hypercohomology groups
satisfy the property
Hi(X,P⊗C Lχ) = 0
for all
i̸ = 0,
as we will explain in more detail in chapter 1. Our methods also allow
to determine the precise locus S (P) of characters χ for which the above
vanishing property fails. In section 1.5 we will see that this locus is a ﬁnite
union of translates of algebraic subtori of the character torus
Π(X) = Hom(π1(X,0),C∗),
and that for perverse sheaves P ∈Perv(X,C) of geometric origin in the
sense of [10, sect. 6.2.4] the occuring translations can be taken to be torsion
points. Again this has been shown independently by C. Schnell in [94] with
a different argument. The two approaches seem to be complementary in
some sense — for example, whereas in the framework of loc. cit. the proof
of the statement about torsion points requires a deep result of C. Simpson,
the methods to be explained below allow to reduce it to a statement over a
ﬁnite ﬁeld which can be checked directly by looking at the eigenvalues of
the Frobenius operator, see lemma 1.11.
We now come back to the Albanese morphism fn : Y n −→X = Alb(Y)
of a smooth complex projective variety Y of arbitrary dimension. The group
law a : X ×X −→X of the Albanese variety deﬁnes a convolution product
on the bounded derived category Db
c (X,C) by the formula
K ∗M = Ra∗(K ⊠M)
for
K, M ∈Db
c (X,C),
and in these terms the direct image of the constant sheaf can be written (up
to a degree shift) as the n-fold convolution
Rfn∗(δY n) = R f1∗(δY)∗···∗Rf1∗(δY)
|
{z
}
n times
.
Our goal is to interpret this convolution as a tensor product in the category
of representations of some reductive algebraic group. To motivate this, let
us take a look at the case where Y = C is a curve. Then f1 : C ,→X is the
Abel-Jacobi embedding, and we are interested in the convolution powers of
the perverse sheaf δC ∈Perv(X,C). Although in general these convolution
powers are not perverse, it turns out that the failure of perversity only comes
from locally constant sheaves: In view of Gabber’s decomposition theorem
we can write
(δC)∗n = δn ⊕τn
where τn denotes the maximal direct summand all of whose cohomology
sheaves are locally constant on X, and then by [106, th. 7] the remaining
4
Introduction
direct summand δn is a perverse sheaf. Let us say that a perverse sheaf is
a Brill-Noether sheaf if it is a subquotient of δn for some n ∈N. Then for
a suitable normalization of the Abel-Jacobi morphism, it has been shown
in theorem 14 of loc. cit. that the category of all Brill-Noether sheaves is
equivalent to the category of algebraic representations of the group
G(δC) =
(
Sp2g−2(C)
if C is hyperelliptic,
Sl2g−2(C)
otherwise,
and that the tensor product of representations is induced by the convolution
product of perverse sheaves. This Tannakian description reduces classical
geometric problems to simple computations in representation theory. For
example, if g denotes the genus of C, then the perverse sheaf δΘ attached
to the theta divisor Θ = Wg−1 ⊂X corresponds via the above equivalence
to the g −1st fundamental representation of G(δC). Using this one may
decompose the convolution δΘ ∗δΘ into its irreducible constituents, which
leads to a new proof of Torelli’s theorem [111].
Alongside our proof of the vanishing theorem and still based on [68], in
chapter 2 we generalize the Tannakian constructions from above to the case
of semisimple sheaf complexes on arbitrary complex abelian varieties X. In
particular, we show that every convolution of semisimple perverse sheaves
is a direct sum of a semisimple perverse sheaf and a further sheaf complex
which is negligible in a suitable sense (for example, on a simple abelian
variety a complex is negligible iff all its cohomology sheaves are locally
constant). To any semisimple perverse sheaf P ∈Perv(X,C) we then attach
a reductive algebraic group G(P) whose representation theory governs the
decomposition of the convolution powers P∗n = P∗···∗P up to negligible
direct summands, see corollary 2.14.
We remark that for algebraic tori in place of abelian varieties, similar
results have been obtained by Gabber and Loeser in [41]. However, in their
case the essential problem is to deﬁne the correct notion of convolution in
the non-proper case, and once this has been done, the required properties
follow from Artin’s vanishing theorem for afﬁne morphisms. By way of
contrast, in the case of abelian varieties the main point of the construction
is to ﬁnd a proper analog of Artin’s theorem, which will be precisely the
vanishing theorem that we stated earlier.
The Tannaka groups G(P) attached to perverse sheaves P ∈Perv(X,C)
as above form an interesting family of new invariants which contain much
information about the geometry and the moduli of the underlying abelian
variety. So far the most efﬁcient method to determine such Tannaka groups
has been to study degenerations of the abelian variety (an example for this
can be found in chapter 4). Even if one is only interested in semisimple
5
perverse sheaves on abelian varieties, such degenerations naturally lead to
non-semisimple perverse sheaves on semiabelian varieties. In chapter 3 we
extend our Tannakian constructions to this more general case, combining
the results of Gabber and Loeser for tori with our vanishing theorem for
abelian varieties. We also give a Tannakian description for the functor of
nearby cycles for a family of abelian varieties which degenerates into a
semiabelian variety. Even though in the non-proper case the functor of
nearby cycles does not preserve the Euler characteristic, we will show that
the degenerate Tannaka group is a subgroup of the generic one whenever
one can possibly expect this to hold (see theorem 3.15).
In the remaining chapters we study in more detail the case where P = δΘ
is the perverse intersection cohomology sheaf associated with a symmetric
theta divisor of a principally polarized abelian variety X. In chapter 4 we
use a degeneration argument to show that for a general principally polarized
abelian variety (ppav) of dimension g one has
G(δΘ) =
(
SOg!(C)
if g is odd,
Spg!(C)
if g is even,
and that δΘ corresponds to the standard representation of this group, a result
that was conjectured in [67]. As an application we deduce that for g = 4 the
invariant G(δΘ) solves the Schottky problem in the sense that it detects the
locus of Jacobian varieties inside the moduli space A4 of ppav’s.
Once we know the Tannaka group G(δΘ), we can use representation
theory to decompose arbitrary convolution powers of the perverse sheaf δΘ
into their simple constituents. This produces a plethora of interesting simple
perverse sheaves which describe the Hodge theory of various subvarieties
of X. For example, consider the translate Θx = Θ+x of the theta divisor by
a point x ∈X(C). The geometry of the intersections
Yx = Θ∩Θx
is closely connected with the moduli of the underlying ppav and has been
studied classically in relation with Torelli’s theorem [25], with the Schottky
problem [27] and with the Prym map [61]. The involution σ = −idX acts
on these intersections, and if the theta divisor is smooth, then for a general
point x ∈X(C) the quotient variety
Y +
x
= Yx/σ
will be smooth as well. We will see in chapter 5 that for varying x, the
variable part of the cohomology H•(Y +
x ,Q) can be identiﬁed naturally with
the stalk cohomology of the alternating resp. symmetric convolution square
of the perverse sheaf δΘ, depending on whether the dimension g = dim(X)
is even or odd. For a general ppav the Tannakian result of chapter 4 implies
6
Introduction
that this alternating resp. symmetric convolution square is irreducible up to
a skyscraper sheaf and negligible terms.
So for x varying in a Zariski-open dense subset of X(C), the variable
part of the cohomology of Y +
x deﬁnes a variation of Hodge structures whose
underlying local system is irreducible. The main topic of chapter 5 is a study
of this variation in the case where g = 4. In this case we are dealing with
a family of smooth surfaces of general type with a surprisingly explicit and
beautiful geometry. On the level of integral cohomology, we will determine
the N´eron-Severi lattices
H2(Yx,Z)
and
H2(Y +
x ,Z)
of the respective surfaces and deduce that the local system underlying the
considered variation of Hodge structures essentially has the monodromy
group W(E6), see theorem 5.1. We will also see that the appearance of this
Weyl group in the present context is closely related to the ubiquitous 27
lines on a cubic surface — the link is provided by the Prym-embedded
curves on Yx which have been studied by E. Izadi in [61] and appear here as
glue vectors for the above N´eron-Severi lattices.
In view of this example, it remains an intriguing question to ask for the
general relationship between the Tannaka group G(P) attached to a perverse
sheaf P ∈Perv(X,C) and the monodromy groups deﬁned by the simple
perverse sheaves in the corresponding Tannakian category. At present this
relationship remains mysterious even for Brill-Noether sheaves on Jacobian
varieties. As a ﬁrst step in this direction, we conclude this dissertation with
a recursive formula for the generic rank of Brill-Noether sheaves — in the
hope that this formula may be given a representation-theoretic and more
conceptual interpretation at some future time.
