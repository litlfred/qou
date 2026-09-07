---
doc_id: arxiv-math-0409393v1
doc_title: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS Jacques Sauloy"
section_id: sec-000-1-introduction-and-general-conventions
section_title: "Introduction and general conventions"
section_number: 1
pages: 1-15
source_pdf: 0409393v1.pdf
source_sha256: 2107d961f6065539
doc_brief: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS Jacques Sauloy — — The local analytic classiﬁcation of irregular linear q-diﬀerence equa- tions has recently"
---
2. Local analytic classiﬁcation. . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . 6
3. Algebraic summation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . 15
4. The q-Gevrey ﬁltration on the Stokes sheaf. . . . . . . . . . . . . . . . . . . . . . 22
References. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . 25
2 J. SAULOY
1. Introduction and general conventions
1.1. Introduction. — This paper deals with Birkhoﬀ’s program of 1941 ([ 3], see
also [ 2]) towards the local analytic classiﬁcation of q-diﬀerence equations and some
extensions stated by J.-P. Ramis in 1990 ([ 14]).
A full treatment of the Birkhoﬀ program including the case of irregu lar q-diﬀerence
equations is being given in [ 15]. The method used there closely follows the an-
alytic procedure developed in the last decades by B. Malgrange, Y. S ibuya, J.-P.
Ramis,. . . for the “classical” case, i.e., the case of diﬀerential equat ions: adequate
asymptotics, q-Stokes phenomenon, q-Stokes sheaves and theorems of Malgrange-
Sibuya type; explicit cocycles are built using a discrete summation process due to C.
Zhang ([27]) where the Jackson q-integral and theta functions are introduced in place
of the Laplace integral and exponential kernels.
To get an idea of the classical theory for linear diﬀerential equation s one should look
at the survey [ 25] by V. S. Varadarajan, especially section 6, and to get some feeling
of how the change of landscape from diﬀerential equations to q-diﬀerence equations
operates, at the survey [ 7] by L. Di Vizio, J.-P. Ramis, J. Sauloy and C. Zhang.
The aim of this paper is to show how the harder analytic tools can, to s ome extent,
be replaced by much simpler algebraic arguments. The problem under consideration
being a transcendental one we necessarily keep using analytic argu ments but in their
most basic, “19th century style”, features only. In particular, w e avoid here using the
discrete summation process.
Again our motivation is strongly pushed ahead by the classical model of which
we recall three main steps: the d´ evissage Gevreyintroduced by J.-P. Ramis ([ 12])
occured to be the fundamental tool for understanding the Stok es phenomenon. The
underlying algebra was clariﬁed by P. Deligne in [ 6], then put at work by D. G.
Babbitt and V. S. Varadarajan in [ 1] (see also [ 25]) for moduli theoretic purposes.
On the same basis, eﬀective methods, a natural summation and galo isian properties
were thoroughly explored by M. Loday-Richaud in [ 9].
Some speciﬁcities of our problem are due, on one hand, to the fact t hat the
sheaves to be considered are quite similar to holomorphic vector bun dles over an
elliptic curve, whence the beneﬁt of GAGA theorems, and, on anoth er hand, to the
existence for q-diﬀerence operators of an analytic factorisation without equivale nt for
diﬀerential operators. Such a factorisation originates in Birkhoﬀ ( [3]), where it was
rather stated in terms of a triangular form of the system. It has b een revived by C.
Zhang ([ 26], [ 10]) in terms of factorisation and we will use it in its linear guise, as a
ﬁltration of q-diﬀerence modules ([ 22]).
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS3
In this paper, following the classical theory recalled above, we build a q-Gevrey
ﬁltration on the q-Stokes sheaf, thereby providing a q-analog of the Gevrey devissage
in the classical case. This q-devissage jointly with a natural summation argument
allows us to prove the q-analog of a Malgrange-Sibuya theorem (theorem 3 of [ 25])
in quite a direct and easy way; in particular, we avoid here the Newland er-Nirenberg
structural theorem used in [ 15]. Our ﬁltration is, in some way, easier to get than the
classical one : indeed, due to the forementionned canonical ﬁltrat ion of q-diﬀerence
modules, our systems admit a natural triangularisation which is indep endent of the
choice of a Stokes direction and of the domination order of exponen tials (here replaced
by theta functions). Also, our ﬁltration has a much nicer structur e than the classical
Gevrey ﬁltration since the so-called elementary sheaves of the clas sical theory are here
replaced by holomorphic vector bundles endowed with a very simple st ructure over
an elliptic curve (they are tensor products of ﬂat bundles by line bun dles).
On the side of what this paper does not contain, there is neither a st udy of con-
ﬂuency when q goes to 1, nor any application to Galois theory. As for the former,
we hope to extend the results in [ 20] to the irregular case, but this seems a diﬃcult
matter. Only partial results by C. Zhang are presently available, on signiﬁcant exam-
ples. As for the latter, it is easier to obtain as a consequence of the present results
that, under natural restrictions, “canonical Stokes operator s are Galoisian” like in [ 9].
However, to give this statement its full meaning, we have to genera lize the results of
[21] and to associate vector bundles to arbitrary equations. This is a q uite diﬀerent
mood that we will develop in a forthcoming paper ([ 23]; meanwhile, a survey is given
in [ 24]). Here, we give some hints in remarks 3.11 and 4.5.
Also, let us point out that there has been little eﬀort made towards s ystematisation
and generalisation. The intent is to get as eﬃciently as possible to the striking speciﬁc
features of q-diﬀerence theory. For instance, most of the results about morp hisms be-
tween q-diﬀerence modules can be obtained by seing these morphisms as mer omorphic
solutions of other modules (internal Hom) and they can therefore be seen as result-
ing from more general statements. These facts, evenso quite of ten sorites, deserve
to be written. In the same way, the many regularity properties of t he homological
equation X(qz)A(z) − B(z)X(z) = Y (z) should retain some particular attention and
be clariﬁed in the language of functional analysis. They are implicitly or explicitly
present in many places in the work of C. Zhang. Last, the q-Gevrey ﬁltration should
be translated in terms of factorisation of Stokes operators, like in [9].
Let us now describe the organization of the paper.
Notations and conventions are given in subsection 1.2.
4 J. SAULOY
Section 2 deals with the recent developments of the theory of q-diﬀerence equa-
tions and some improvements. In subsection 2.1, we recall the local classiﬁcation
of fuchsian systems by means of ﬂat vector bundles as it can be fou nd in [ 21] and
its easy extension to the so-called “tamely irregular” q-diﬀerence modules. We then
describe the ﬁltration by the slopes ([ 22]). In subsections 2.2, we summarize results
from [ 15] about the local analytic classiﬁcation of irregular q-diﬀerence systems,
based on the Stokes sheaf. The lemma 2.7 provides a needed improve ment about
Gevrey decay; proposition 2.8 and corollary 2.10 an improvement abo ut polynomial
normal forms.
In chapter 3, we ﬁrst build our main tool, the algebraic summation pro cess (the-
orem 3.7). Its application to the local classiﬁcation is then developed in subsection
3.2. We state there and partially prove the second main result of this paper (theorem
3.18): a q-analog of the Malgrange-Sibuya theorem for the local analytic clas siﬁcation
of linear diﬀerential equations.
Section 4 is devoted to studying the q-Gevrey ﬁltration of the Stokes sheaf and
proving the theorem 3.18. In subsection 4.1, we show how conditions of ﬂatness
(otherwise said, of q-Gevrey decay) of solutions near 0 translate algebraically and
how to provide the devissage for the Stokes sheaf of a “tamely irre gular” module. In
subsection 4.2 we draw some cohomological consequences and we ﬁn ish the proof of
the theorem 3.18. Finally, in subsection 4.3, we sketch the Stokes sh eaf of a general
module.
The symbol □ indicates the end of a proof or the absence of proof if considered
straightforward. Theorems, propositions and lemmas considered as “prerequisites”
and coming from the quoted references are not followed by the sym bol□ .
Acknowledgements. — The present work (1) is directly related with the paper
[15], written in collaboration with Jean-Pierre Ramis and with Changgui Zh ang. It
has been a great pleasure to talk with them, confronting very diﬀer ent points of view
and sharing a common excitement.
The epigraph at the beginning of this paper is intended to convey the happiness
of wandering and daydreaming in Jean-Pierre Ramis’ garden; and th e overwhelming
surprise of all its bifurcations. Like in Borges’ story, pathes fork and then unite, the
(1)This paper has been submitted (and accepted) for publicatio n in the proceedings of the Interna-
tional Conference in Honor of Jean-Pierre Ramis, held in Tou louse, september 22-26 2004.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS5
same landscapes are viewed from many points with renewed pleasure . This strong
feeling of the unity of mathematics without any uniformity is typical o f Jean-Pierre.
1.2. Notations and general conventions. — We ﬁx once for all a complex
number q ∈ C such that |q| > 1. We then deﬁne the automorphism σq on various
rings, ﬁelds or spaces of functions by putting σqf (z) = f (qz). This holds in particular
for the ﬁeld C(z) of complex rational functions, the ring C{z} of convergent power
series and its ﬁeld of fractions C({z}), the ring C[[z]] of formal power series and
its ﬁeld of fractions C((z)), the ring O(C∗, 0) of holomorphic germs and the ﬁeld
M(C∗, 0) of meromorphic germs in the punctured neighborhood of 0, the r ing O(C∗)
of holomorphic functions and the ﬁeld M(C∗) of meromorphic functions on C∗; this
also holds for all modules or spaces of vectors or matrices over the se rings and ﬁelds.
For any such ring (resp. ﬁeld) R, the σq-invariants elements make up the subring
(resp. subﬁeld) Rσ q of constants. For instance, the ﬁeld of constants of M(C∗, 0) or
that of M(C∗) can be identiﬁed with a ﬁeld of elliptic functions, the ﬁeld M(Eq) of
meromorphic functions over the complex torus (or elliptic curve) Eq = C∗/qZ. We
shall use heavily the theta function of Jacobi deﬁned by the followin g equality:
θq(z) =
∑
n∈Z
q−n(n+1)/ 2zn.
This function is holomorphic in C∗ with simple zeroes, all located on the discrete
q-spiral [ −1; q], where we write [ a; q] = aqZ , (a ∈ C∗). It satisﬁes the functional
equation: σqθq = zθq. We shall also use its multiplicative translates θq,c (z) = θq(z/c)
(for c ∈ C∗); the function θq,c is holomorphic in C∗ with simple zeroes, all located
on the discrete q-spiral [ −c; q] and satisﬁes the functional equation: σqθq,c = z
c θq,c .
As is customary for congruence classes, we shall write a = a (mod qZ) for the
image of a ∈ C∗ in the elliptic curve Eq. This notation extends to a subset A of C∗,
so that A does not denote its topological closure. Then, for a divisor D =∑ ni[αi]
over Eq (i.e., the ni ∈ Z, the αi ∈ Eq), we shall write evEq (D) =∑ niαi ∈ Eq for its
evaluation, computed with the group law on Eq.
Let K denote any one of the forementioned ﬁelds of functions. Then, we write
Dq,K = K
⟨
σ, σ−1⟩
for the ¨Ore algebra of non commutative Laurent polynomials char-
acterized by the relation σ.f = σq(f ).σ. We now deﬁne the category of q-diﬀerence
modules in three clearly equivalent ways:
Dif f M od(K, σq) = {(E, Φ) / E a K-vector space of ﬁnite rank , Φ : E → E a σq-linear map }
= {(K n, Φ A) / A ∈ GLn(K), Φ A(X) = A−1σqX}
= ﬁnite length left Dq,K -modules.
6 J. SAULOY
This is a C-linear abelian rigid tensor category, hence a tannakian category. For
basic facts and terminology about these, see [ 21], [ 11], [ 5], [ 4]. Last, we note that all
objects in Dif f M od(K, σq) have the form Dq,K /Dq,K P .
2. Local analytic classiﬁcation
2.1. Devissage of irregular equation ( [21],[22]). —
Fuchsian and tamely irregular modules . — For a q-diﬀerence module M over any of
the ﬁelds C(z), C({z}), C((z)), it is possible to deﬁne its Newton polygon at 0, or,
equivalently, the slopes of M , which we write in descending order : µ1 > · · · > µ k ∈ Q,
and their multiplicities r1, . . . , rk ∈ N∗. The module M is said to be pure of slope
µ1 if k = 1 and fuchsian if it is pure of slope 0. The latter condition is equivalent to
M having the shape M = ( K n, Φ A) with A(0) ∈ GLn(C). There are also criteria of
growth (or decay) of solutions near 0, see further below, in sectio n 2.2, the subsection
about ﬂatness conditions.
Call E the category Dif f M od(C(z), σq) of rational equations. Fuchsian modules
at 0 and ∞ over C(z) make up a tannakian subcategory Ef of E. In order to study
them, one “localizes” these categories by extending the class of mo rphisms, precisely,
by allowing morphisms deﬁned over C({z}). This gives “thickened” categories E (0)
and E (0)
f . A classical lemma says that any fuchsian system is locally equivalent t o one
with constant coeﬃcients. This suggests the introduction of the f ull subcategory P (0)
f
of E (0)
f made up of “ﬂat” objects, that is, the ( C(z)n, Φ A) with A ∈ GLn(C). Thus,
the inclusion of P (0)
f into E (0)
f is actually an isomorphism of tannakian categories.
To any A ∈ GLn(C) one associates the holomorphic vector bundle FA over Eq
obtained by quotienting C∗ × Cn by the equivalence relation ∼A generated by the
relations ( z, X ) ∼A (qz, AX ). This deﬁnes a functor from P (0)
f to the category
F ibp(Eq) of ﬂat holomorphic vector bundles over Eq. This is an equivalence of
tannakian categories. Note that the classical lemma alluded above e qually holds for
any fuchsian q-diﬀerence module over C({z}) or over C((z)), which implies that this
local classiﬁcation applies to Dif f M od(C({z}), σq) and Dif f M od(C((z)), σq) as
well. The galoisian aspects of this local correspondance and its globa l counterpart
are detailed in [ 21].
A pure module of integral slope µ over K = C({z}) or C((z)) has the shape
(K n, Φ z−µ A) with A ∈ GLn(C). For such a module, the above construction of a
vector bundle extends trivially, yielding the tensor product of a ﬂat bundle by a line
bundle. We shall call pure such a bundle.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS7
Direct sums of pure modules play a special role in [ 22], [ 15] and in the present
paper. We shall call them tamely irregular, in an intended analogy with tamely
ramiﬁed extensions in algebraic number theory: for us, they are irr egular objects
without wild monodromy, as follows from [ 15]. The category of tamely irregular
modules with integral slopes over C({z}) can, for the same reasons as above, be
seen either as a subcategory of Dif f M od(C({z}), σq) or of E (0). We write it E (0)
mi, 1
(2). It is generated (as a tannakian category) by the fuchsian module s and by the
pure module ( C({z}), z−1σq) of slope 1. We can thus associate to any such module
a direct sum of pure modules, thereby deﬁning a functor from E (0)
mi, 1 to the category
F ib(Eq) of holomorphic vector bundles over Eq. This functor is easily seen to be
compatible with all linear operations (it is a functor of tannakian cate gories).
Filtration by the slopes . — The following is proved in [ 22]:
Theorem 2.1. — Let the letter K stand for the ﬁeld C({z}) (convergent case) or
the ﬁeld C((z)) (formal case). In any case, any object M of Dif f M od(K, σq) admits
a unique ﬁltration (F ≥µ (M ))µ ∈Q by subobjects such that each F (µ )(M ) = F ≥µ (M)
F >µ (M) is
pure of slope µ. The F (µ ) are endofunctors of Dif f M od(K, σq) and gr = ⨁ F (µ )
is a faithful exact C-linear ⊗-compatible functor and a retraction of the inclusion of
E (0)
mi into E (0). In the formal case, gr is isomorphic to the identity functor.
From now on, we only consider the full subcategory E (0)
1 of modules with
integral slopes. The notation E (0)
1 will be justiﬁed a posteriori by the fact that all its
objects are locally equivalent to objects of E (existence of a normal polynomial form).
This is an abelian tensor subcategory of E (0) and the functor gr retracts E (0)
1 to E (0)
mi, 1.
We also introduce notational conventions which will be used all along t his paper for
a module M in E (0)
1 and its associated graded module M0 = gr(M ), an object of E (0)
mi, 1.
The module M may be given the shape M = (C({z})n, Φ A), with:
(2.1.1) A = AU =
def


z−µ 1A1 . . . . . . . . . . . .
. . . . . . . . . U i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . z −µ k Ak


,
where µ1 > · · · > µ k are integers, ri ∈ N∗, Ai ∈ GLri(C) ( i = 1, . . . , k) and
U = (Ui,j )1≤i<j≤k ∈
∏
1≤i<j≤k
Matri,r j (C({z})).
(2)The subscript “mi” stands for “moder´ ement irr´ egulier”, t he subscript 1 for restricting to slopes
with denominator 1.
8 J. SAULOY
The associated graded module is then a direct sum M0 = P1 ⊕ · · · ⊕ Pk, where, for
1 ≤ i < j ≤ k, the module Pi is pure of rank ri and slope µi and can be put into the
form Pi = ( C({z})ri, Φ z−µ i Ai ). Therefore, one has M0 = ( C({z})n, Φ A0), where the
matrix A0 is block-diagonal:
(2.1.2) A0 =


z−µ 1A1 . . . . . . . . . . . .
. . . . . . . . . 0 . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . z −µ k Ak


.
The set of analytic isoformal classes . — This section comes from [ 15]. The deﬁni-
tions here should be compared to those in [ 25], p. 29 or [ 1].
In Dif f M od(C((z)), σq), the canonical ﬁltration of a module M is split; more pre-
cisely, the associated graded module gr(M ) is the unique formal classifyer of M . The
isoformal analytic classiﬁcation is therefore the same as the isogra ded classiﬁcation,
whence the following deﬁnitions.
Deﬁnition 2.2 . — Let P1, . . . , Pk be pure modules with ranks r1, . . . , rk and with
integral slopes µ1 > · · · > µ k. The module M0 = P1⊕· · ·⊕Pk has rank n = r1+· · ·+rk.
We shall write F (M0) for the set of equivalence classes of pairs (M, g) of a module
M and an isomorphismism g : gr(M ) → M0, where (M, g) is said to be equivalent
to (M ′, g′) if there exists a morphism u : M → M ′ such that g = g′ ◦ gr(u) (u is
automatically an isomorphism).
We write G for the algebraic subgroup of GLn made up of matrices of the form:
(2.2.1) F =


Ir1 . . . . . . . . . . . .
. . . . . . . . . F i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . I rk


.
Its Lie algebra g consists in matrices of the form:
(2.2.2) f =


0r1 . . . . . . . . . . . .
. . . . . . . . . f i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . 0rk


.
For F in G, we shall write F [A] = ( σqF ) AF −1 for the result of the gauge transfor-
mation F on the matrix A.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS9
We shall identify Pi with ( C({z})ri, Φ z−µ i Ai), where Ai ∈ GLri(C). The datum
of a pair ( M, g) then amounts to that of a matrix A in the form 2.1.1. Two such
matrices A, A′ are equivalent iﬀ there exists a matrix F ∈ G(C({z})) such that
F [A] = A′.
Write GA0(C((z))) = {F ∈ G(C((z))) / F [A0] ∈ GLn(C({z}))}. The sub-
group G(C({z})) of G(C((z))) operates at left on the latter (by translation) and
GA0 (C((z))) is stable for that operation. The theory in the previous section entails:
∀(Ui,j )1≤i<j≤k ∈
∏
1≤i<j≤k
Matri,r j (C({z})) , ∃! ˆF ∈ G(C((z))) : ˆF [A0] = AU .
This ˆF will be written ˆF (U ). Its existence can also be proved by direct computa-
tion, solving by iteration the ﬁxpoint equation of the z-adically contracting operator:
F ↦→(AU )−1
(
σq ˆF
)
A0. It follows that the unique formal gauge transformation of
G(C((z))) taking AU to AV is ˆF (U, V ) = ˆF (V ) ˆF (U )−1. Besides, AU is equiva-
lent to AV in the above sense if and only if ˆF (U, V ) ∈ G(C({z})), or, equivalently,
ˆF (V ) ∈ G(C({z})) ˆF (U ). This translates into the following lemma.
Proposition 2.3 . — Sending AU to ˆF (U ) induces a one-to-one correspondance be-
tween F (M0) and the left quotient G(C({z}))\GA0 (C((z))).
One thus recognizes in isoformal classiﬁcation a classical problem of summation of
divergent power series. In order to illustrate the possible strateg ies, we shall end this
section by examining a speciﬁc example. We shall try, as far as possib le, to mimic
the methods and the terminology of the “classical” theory (Stokes operators for linear
diﬀerential equations and summation in sectors along directions).
Example 2.4 . — The module Mu = ( C({z})2, Φ Au ) corresponding to the matrix
Au =
( 1 u
0 z
)
is formally isomorphic to its associated graded module M0. More
precisely, there exists a formal gauge transformation F such that F [A0] = Au, that
is,F (qz)A0(z) = Au(z)F (z). If one moreover requires F to be compatible with the
graduation, that is, to have the form F =
( 1 f
0 1
)
, then there is unicity of the formal
series f , which must satisfy the functional equation:
f (z) = −u(z) + zf (qz).
We call ˆfu this unique formal solution (it can be computed by iterating the above
ﬁxpoint equation) and ˆFu the corresponding formal gauge transformation. One checks
that two such matrices Au and Av are analytically equivalent if and only if the formal
power series ˆfu−v = ˆfu − ˆfv is convergent. In this case (two slopes), the problem is
additive.
10 J. SAULOY
For u = 1, the unique solution is
ˆf1 = −
∑
n≥0
qn(n−1)/ 2zn,
the so-called Tschakaloﬀ series (up to the sign). It is diver gent and may be seen as a
natural q-analog of the Euler series. Thus, A1 is not equivalent to A0.
In general, we apply the formal q-Borel-Ramis transform of level 1, deﬁned by
Bq, 1
∑
n
anzn =
∑
n
q−n(n−1)/ 2anξn.
It sends convergent series to series with an inﬁnite radius o f convergence. Our func-
tional equation is transformed into:
(1 − ξ)Bq, 1f (ξ) = −Bq, 1u(ξ).
The existence of a convergent solution f has only one obstruction, the number
ν = Bq, 1u(1). This number can therefore be considered as the unique analy tic
invariant of Mu within the formal class of M0. It can also be considered as giving
a normal form, since Aν is the unique matrix in the analytic class of Au such that
ν ∈ C. It is a particular case of normal polynomial form (see furth er below).
The functional equation can also be solved by a variant of the method of “varying
constants”. We look for the solution in the form g = θq,λ f . For convenience, we also
write v = θq,λ u, which is an element of O(C∗, 0). We compare their Laurent series
coeﬃcientwise and get:
∀n ∈ Z , (1 − λqn)gn = vn.
If λ ⁄∈ [1; q] (prohibited direction of summation), there is a unique solu tion
g ∈ O(C∗, 0) (it does converge where it should), thus a unique solution f ∈ M(C∗, 0)
such that θq,λ f has no poles in C∗. We then get a unique solution fλ,u with (at most)
simple poles over [−λ; q]: it is the summation of ˆfu in the direction λ ∈ Eq and its
“sector” of validity is (the germ at 0) of C∗ \ [−λ; q], the preimage by the canonical
projection C∗ → Eq of the Zariski open set Eq \ {−λ}.
There is another way of looking at this summation process, wi th a deeper analytical
meaning. We can consider Bq, 1f (ξ) as a meromorphic function φ over the ξ-plane
and apply to it some q-analog of the Laplace transform. In our case, putting
Lλ
q, 1φ(z) =
∑
ξ∈[λ ;q]
φ(ξ)
θq(z/ξ ) ,
gives again fλ,u . This discrete summation process is due to Changgui Zhang see ( [27],
also see [7]) and it is heavily used in [15]. In this work, we rather use the ﬁrst more
algebraic and more naive method.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS11
2.2. Classiﬁcation through the Stokes sheaf ( [15],[16]). —
The Stokes sheaf and its Lie algebra . — First, we recall the relevant deﬁnitions about
asymptotic expansions. The semigroup Σ = q−N operates on C∗ with quotient Eq (its
horizon); in the classical setting, one would rather have an operation of th e semigroup
Σ = e]−∞, 0] with horizon the circle S1 of directions. We consider as sectors the germs
at 0 of invariant open subsets of C∗. We introduce two sheaves of diﬀerential algebras
over C∗ by putting, for any sector U :
B(U ) = {f ∈ O(U ) / f is bounded on every invariant relatively compact subset of U }
A′(U ) = {f ∈ O(U ) / ∃ ˆf ∈ C[[z]] : ∀n ∈ N , z −n
(
f − Sn−1 ˆf
)
∈ B (U )},
where, as usual, Sn−1 ˆf stands for the truncation. For any sector U , we write U∞ =
U/Σ for its horizon (an open subset of Eq). We now deﬁne a sheaf of diﬀerential
algebras over Eq by putting:
A(V ) = lim
→
A′(U ),
the direct limit being taken for the system of those open subsets U such that their
horizon is U∞ = V . There is a natural morphism from A to the constant sheaf with
ﬁbre C{z} over Eq and it is an epimorphism ( q-analog of Borel-Ritt lemma). We call
A0 its kernel, the sheaf of inﬁnitely ﬂat functions. For instance, it is ea sy to see that
a solution of fuchsian equation divided by a product of theta functio ns is ﬂat within
its domain (more on this in the next subsection).
We then write Λ I = In + M atn(A0) for the subsheaf of groups of GLn(A) made
up of matrices inﬁnitely tangent to the identity and we put Λ G
I = Λ I ∩ G(A). This
is a sheaf of matrices of the form 2.2.1 with all the Fi,j ﬂat. Last, for a module
M = (C({z})n, Φ A), we consider the subsheaf Λ I (M ) of Λ G
I whose sections F satisfy
the equality: F [A] = A (automorphisms of M inﬁnitely tangent to identity). This is
the Stokes sheaf of the module M .
Note for further use that Λ I(M ) is a sheaf of unipotent groups so that one can
deﬁne algebraically the sheaf λI (M ) of their Lie algebras: we put λI = M atn(A0),
λg
I = λI ∩ g(A) (see 2.2.2) and take as sections of λI (M ) those sections of λg
I such
that (σqf ) A = Af . Obviously, f is a section of λI (M ) if and only if In + f is a section
of Λ I (M ), or, equivalently, exp(f ) is a section of Λ I(M ). Indeed, the triangular form
and the functional equations are easily checked, and the ﬂatness properties stem from
the well known fact that, for nilpotent matrices, f and exp(f ) − In are polynomials
in each other, without constant terms.
The q-analogs of Malgrange-Sibuya theorems . — One showed in [ 15] the following
q-analogs of classical theorems by Malgrange-Sibuya:
12 J. SAULOY
Theorem 2.5. — There are natural bijective mappings:
G(C{z})/downslopeGA0(C[[z]]) → G(C({z}))/downslopeGA0 (C((z))) → H 1(Eq, Λ G
I ).
Actually, the following more general theoren is proven in loc. cit. , dealing with
an arbitrary algebraic subgroup G of GLn. Its proof relies on some heavy analysis
(Newlander-Nirenberg theorem).
Theorem 2.6. — Let M0 be as above. There are natural bijective mappings:
F (M0) → G(C{z})/downslopeGA0 (C[[z]]) → G(C({z}))/downslopeGA0 (C((z))) → H 1(Eq, Λ G
I ),
where Λ G
I = Λ I ∩ G(A).
The former theorem is deduced from the latter together with the e xistence of
asymptotic solutions. One can explicitly build, by discrete resummatio n, privileged
cocycles associated to a class in F (M0) and to “Stokes directions”. In the next
chapter, I shall exhibit an algebraic variant of this construction. M orally, it is possible
because the sheaf Λ I (M0) is almost a vector bundle over the elliptic curve Eq.
Flatness conditions . — Details about the contents of this section can be found in
[17] and [ 15]; see also the older references [ 13] and [ 14].
The above notion of ﬂatness can be reﬁned, introducing q-Gevrey levels. These
may be characterized either in terms of growth (or decay) of func tions near 0, or in
terms of growth of coeﬃcients of power series. We shall use here t he following simple
terminology and facts.
We start from a proper germ of q−N invariant subset U of ( C∗, 0). Then any
solution of a fuchsian system that is holomorphic on U has polynomial growth at 0
(see for instance [ 21]); this is for instance true for a quotient of theta functions. We
say that f ∈ O (U ) has level of ﬂatness ≥ t (where t is an integer) if, for one (hence
any) theta function θ = θq,λ , the function f |θ|t has polynomial growth near 0. We
easily get the following implications.
Lemma 2.7 . — (i) For t > 0, t-ﬂatness implies ﬂatness in the sense of asymptotics.
(ii) Solutions of pure systems of slope µ are µ-ﬂat.
(iii) If a solution of a pure system of slope µ is t-ﬂat with t > 0, then it is 0.
□
Normal polynomial forms . — The computations will follow the same pattern as
in [ 15], [ 16]. However, we shall need a slightly more general version afterward s
(proposition 2.8).
We start with a computation with two slopes. Take integers µ > µ ′, square invert-
ible matrices A ∈ GLr(C) and A′ ∈ GLr′(C). Just for this section, call V(r, r′, µ, µ′)
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS13
the subspace of Mr,r ′(C({z})) spanned by matrices all of whose coeﬃcients belong
to ∑
µ ′≤k<µ
Czk.
For U ∈ M r,r ′(C({z})), write BU =
( z−µ A U
0 z−µ ′
A′
)
. Then, for any such U ,
there exists a unique pair ( F, V ) with F ∈ M r,r ′(C({z})) and V ∈ V (r, r′, µ, µ′) such
that the matrix
( Ir F
0 Ir′
)
deﬁnes an isomorphism from BU to BV . This amounts to
solving:
(2.7.1) ( σqF ) (z−µ ′
A′) − (z−µ A)F = V − U.
Successive reductions boil the problem down to example 2.4. We shall write
Red(µ, A, µ′, A′, U) for the pair ( F, V ).
Now, we come back to our usual notations 2.1.1 and 2.1.2. We consider the
matrix AU associated to U = ( Ui,j ) ∈ ∏
1≤i<j≤k
Mri,r j (C({z})). Then, there is a
unique pair ( F , V ) with F = ( Fi,j ) ∈ ∏
1≤i<j≤k
Mri,r j (C({z})) and V = ( Vi,j ) ∈
∏
1≤i<j≤k
V(ri, rj, µi, µj) such that the associated gauge transformation F ∈ G(C({z}))
deﬁnes an isomorphism from AU to AV . The pair ( F , V ) can be computed by solving
iteratively a system of equations of the type 2.7.1 for 1 ≤ i < j ≤ k. This is done by
inductively with the help of the formula:
(Fi,j , Vi,j ) = Red

µi, Ai, µj, Aj, Ui,j +
∑
i<l<j
(σqFi,l ) Ul,j −
∑
i<l<j
Vi,l Fl,j

 .
What we get is, in essence, the canonical form of Birkhoﬀ and Guent her. Standing
alone, this statement conﬁrms our earlier contention in section 2.1, to the eﬀect that
all objects of E (0)
1 are locally equivalent to objects of E.
Now, we shall have use for an extension of these results allowing for coeﬃcients in
O(C∗, 0) (instead of C({z})).
Proposition 2.8 . — Let AU be as above, but with U = (Ui,j ) ∈ ∏
1≤i<j≤k
Mri,r j (O(C∗, 0)).
Then, there exists a unique pair (F , V ) with F = ( Fi,j ) ∈ ∏
1≤i<j≤k
Mri,r j (O(C∗, 0))
and V = ( Vi,j ) ∈ ∏
1≤i<j≤k
V(ri, rj, µi, µj) such that the associated gauge transforma-
tion F ∈ G(O(C∗, 0)) deﬁnes an isomorphism from AU to AV .
Proof. - The same induction as before can be used, and the proof boils down t o
the following lemma.
14 J. SAULOY
Lemma 2.9 . — Let µ > µ ′ in Z, A ∈ GLr(C),A′ ∈ GLr′(C) and U ∈
Mr,r ′(O(C∗, 0)). There exists a unique pair (F, V ) with F ∈ M r,r ′(O(C∗, 0))
and V ∈ V (r, r′, µ, µ′) satisfying 2.7.1.
Proof. - The same reductions as in loc. cit. entail that we may as well as-
sume from the beginning that µ = 0 and µ′ = −1. The equation as written has
unknown F and right hand side V − U in a space of rectangular matrices. Call s
the rank of this space and call B the matrix of its automorphism F ↦→AF A′−1
relative to some basis. Multiplying both sides of 2.7.1 by A′−1 at right, we get an
equivalent equation of the shape z σ qX − BX = Y − Y (0), for which we want to
show that, for arbitrary B ∈ GLs(C) and Y ∈ O (C∗, 0)s, there is a unique solution
(X, Y (0)) ∈ O(C∗, 0)s × Cs. Note that, replacing X =∑
n∈Z Xnzn, Y =∑
n∈Z Ynzn
and Y (0) respectively by ∑
n∈Z BnXnzn,∑
n∈Z Bn−1Ynzn and B−1Y (0), we do not
change the conditions on X, Y , Y (0), and we are led to study a similar problem
with B = Is. The latter problem can be tackled componentwise: we are to show
that, for any u ∈ O (C∗, 0)s, there is a unique pair ( f, ν) ∈ O (C∗, 0) × C such that
zσqf − f = u − ν (compare to example 2.4).
We apply the q-Borel-Ramis transform of level 1. This clearly sends O(C∗, 0) to
O(C∗): indeed, for any A > 0, Anq−n(n−1)/ 2 tends to 0 when n → ±∞ . From
the computations in example 2.4, we deduce that we have to take ν = Bq, 1u(1) =∑
n∈Z q−n(n−1)/ 2un; we must then prove the existence and unicity of f . Replacing
u by u − ν, we may assume that Bq, 1u(1) = 0. We write f ′
n = q−n(n−1)/ 2fn and
u′
n = q−n(n−1)/ 2un the coeﬃcients of the q-Borel-Ramis transforms Bq, 1f and Bq, 1u.
We know that ∑ +∞
−∞ u′
k = 0 and require that ∀n ∈ Z, f ′
n−1 − f ′
n = u′
n. The only
possibility allowing f ′
n → 0 for n → ±∞ is given by the two equivalent deﬁnitions:
f ′
n =
def
+∞∑
k=n+1
u′
k
=
def
−
n∑
k=−∞
u′
k.
For n → +∞, we thus take (using the ﬁrst deﬁnition of f ′
n):
fn = qn(n−1)/ 2
+∞∑
k=n+1
uk
qk(k−1)/ 2 .
By assumption on u, there exists A > 0 and C > 0 such that, ∀n ≥ 0, |un| ≤ CAn.
Then:
|fn| ≤ CAn+1
|q|n
(
1 + A
|q|n+1 + A2
|q|(n+1)+(n+2) + · · ·
)
,
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS15
whence |fn| = O
((
A
|q|
) n)
when n → +∞.
On the side of negative powers, putting, for convenience, gn = f−n and vk = u−k
and, using the second deﬁnition for f ′
n, we see that
gn = qn(n+1)/ 2
+∞∑
k=n
vk
qk(k+1)/ 2 .
By assumption on u, we have, for any B > 0, |vk| = O( Bk) when k → +∞ and a
similar computation as before then yields that, for any B > 0, |gn| = O( Bn) when
n → +∞, allowing one to conclude that f ∈ O(C∗, 0) as desired. □
We shall actually need only the following consequence of the proposit ion.
Corollary 2.10 . — Let A = AU in the canonical form 2.1.1, with U = ( Ui,j ) ∈∏
1≤i<j≤k
Mri,r j (O(C∗, 0)). Then, there exists F ∈ G(O(C∗, 0)) such that AV = F [AU ]
has the same form, but with V = (Vi,j ) ∈ ∏
1≤i<j≤k
Mri,r j (C({z})).
□
Obviously the same properties hold if one replaces O(C∗, 0) by O(C∗).
