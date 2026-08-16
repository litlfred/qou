---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 9-12
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
The geometry of a smooth complex projective curveC with Jacobian
varietyJac(C) is governed, after the choice of a base point on the curve, by
the Abel-Jacobi morphism. In particular, the latter deﬁnes for eachn∈ N
a morphismCn =C×···× C−→Jac(C) whose ﬁbres correspond to linear
series of divisors on the curve, and the loci where the ﬁbre dimension jumps
are the subvarietiesWrn⊆ Jac(C) of special divisors that have been studied
extensively in classical Brill-Noether theory [6].
For smooth complex projective varietiesY of higher dimension one still
has the Albanese morphism
fn : Yn = Y×···× Y−→X = Alb(Y),
but here the situation is much harder to describe in general. For example, the
image f1(Y) ↪→ X can have any dimension between zero and dim(X), and
there is no obvious substitute for Brill-Noether theory in general. In some
sense, the ﬁrst three chapters of this thesis provide a possible framework for
such a substitute. More speciﬁcally, the properties offn we are interested
in (such as the loci onX where the ﬁbre dimension jumps) can be studied
via the higher direct images
Rifn∗(CYn) for i≥ 0,
which are constructible sheaves in the sense that there exists a stratiﬁcation
of X into ﬁnitely many locally closed subvarieties over which they restrict
to locally constant sheaves. In general the geometry of these higher direct
image sheaves is rather involved, as we will see in a particular example in
chapter 5. However, we propose a simple description of such direct images
in terms of the representation theory of a reductive algebraic group that can
be attached toY via the Tannakian formalism [33].
The basis for this Tannakian description will be a vanishing theorem for
constructible sheaves on abelian varieties which can be seen as an analog
of the Artin-Grothendieck afﬁne vanishing theorem [7, exp. XIV , cor. 3.2]
and contains as a special case the generic vanishing theorems of Green and
Lazarsfeld [47]. For any characterχ : π1(X,0)−→C∗ of the fundamental
group, let us denote byLχ the corresponding local system onX. Then in
chapters 1 and 2 which are based on joint work with R. Weissauer [68],
1
2 Introduction
we show that for any constructible sheafF on X and a sufﬁciently general
characterχ one has
Hi(X,F⊗CLχ) = 0 for all i > dim(Supp(F)).
An independent proof of this result has also been given by C. Schnell [94],
using the Fourier-Mukai transform for holonomicD-modules. Our proof
is of a different ﬂavour and is closely intertwined with the deﬁnition of the
Tannakian categories we are interested in. It is based on an abstract quotient
construction for semisimple tensor categories — we only useD-modules
at a single place in section 1.4 where we classify all perverse sheaves of
Euler characteristic zero (which will be precisely the objects which become
isomorphic to zero under the above quotient construction). At present we
do not know whether this classiﬁcation extends to algebraically closed base
ﬁelds of positive characteristicp > 0, but otherwise all our arguments also
work forl-adic constructible sheaves on abelian varieties over the algebraic
closure of a ﬁnite ﬁeldFp for prime numbersl⁄= p.
Our Tannakian results are best formulated in the framework of perverse
sheaves which has its historic roots in the theory ofD-modules [57] and
in the sheaf-theoretic construction of intersection cohomology for singular
varieties [10]. Let us for convenience brieﬂy recall some basic deﬁnitions
and notations from loc. cit. For any complex algebraic varietyZ, we will
denote by Dbc (Z,C) the derived category of boundedC-sheaf complexes
whose cohomology sheaves are constructible for some stratiﬁcation ofZ
into Zariski-locally closed subsets. This is a triangulated category, and one
can deﬁne the full abelian subcategory
Perv(Z,C)⊂ Db
c (Z,C)
of perverse sheaves to be the core of the middle perverset-structure. More
explicitly, a sheaf complexK is said to be semi-perverse if its cohomology
sheavesH−i(K) satisfy the support estimate dim(SuppH−i(K))≤ i for
all i∈ Z, and it is a perverse sheaf iff bothK and its Verdier dualD(K) are
semi-perverse. For example, the perverse intersection cohomology sheaf is
by deﬁnition the intermediate extension
δZ = j!∗(CU[dim(Z)])∈ Perv(Z,C)
where j :U ↪→Z denotes the inclusion of a smooth open dense subset. This
perverse sheaf is self-dual with respect to Verdier duality, and it does not
depend on the choice of the smooth open dense subset. Thus for smooth
varietiesZ the perverse intersection cohomology sheafδZ coincides with
the constant sheaf up to a degree shift. IfZ is a closed subvariety ofX with
embeddingi : Z ↪→ X, then the direct imagei∗ : Perv(Z,C) ↪→ Perv(X,C)
is a fully faithful functor, and in this case we will by abuse of notation also
writeδZ for the perverse sheafi∗(δZ)∈ Perv(X,C).
3
In the context of perverse sheaves, our above vanishing theorem can be
reformulated as the statement that for any perverse sheafP∈ Perv(X,C)
and a general characterχ : π1(X,0)−→C∗ the hypercohomology groups
satisfy the property
Hi(X,P⊗CLχ) = 0 for all i⁄= 0,
as we will explain in more detail in chapter 1. Our methods also allow
to determine the precise locusS (P) of charactersχ for which the above
vanishing property fails. In section 1.5 we will see that this locus is a ﬁnite
union of translates of algebraic subtori of the character torus
Π(X) = Hom(π1(X,0),C∗),
and that for perverse sheavesP∈ Perv(X,C) of geometric origin in the
sense of [10, sect. 6.2.4] the occuring translations can be taken to be torsion
points. Again this has been shown independently by C. Schnell in [94] with
a different argument. The two approaches seem to be complementary in
some sense — for example, whereas in the framework of loc. cit. the proof
of the statement about torsion points requires a deep result of C. Simpson,
the methods to be explained below allow to reduce it to a statement over a
ﬁnite ﬁeld which can be checked directly by looking at the eigenvalues of
the Frobenius operator, see lemma 1.11.
We now come back to the Albanese morphismfn : Yn−→X = Alb(Y)
of a smooth complex projective varietyY of arbitrary dimension. The group
lawa : X×X−→X of the Albanese variety deﬁnes a convolution product
on the bounded derived categoryDbc (X,C) by the formula
K∗M = Ra∗(K⊠M) for K, M∈ Db
c (X,C),
and in these terms the direct image of the constant sheaf can be written (up
to a degree shift) as then-fold convolution
R fn∗(δYn) = R f1∗(δY)∗···∗ R f1∗(δY)| {z }
n times
.
Our goal is to interpret this convolution as a tensor product in the category
of representations of some reductive algebraic group. To motivate this, let
us take a look at the case whereY =C is a curve. Thenf1 : C ↪→ X is the
Abel-Jacobi embedding, and we are interested in the convolution powers of
the perverse sheafδC∈ Perv(X,C). Although in general these convolution
powers are not perverse, it turns out that the failure of perversity only comes
from locally constant sheaves: In view of Gabber’s decomposition theorem
we can write
(δC)∗n = δn⊕ τn
where τn denotes the maximal direct summand all of whose cohomology
sheaves are locally constant onX, and then by [106, th. 7] the remaining
