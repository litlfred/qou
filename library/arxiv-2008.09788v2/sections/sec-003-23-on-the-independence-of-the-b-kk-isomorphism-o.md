---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETR Y"
section_id: sec-003-23-on-the-independence-of-the-b-kk-isomorphism-o
section_title: "On the independence of the B-KK isomorphism of infinite prime and Plotkin conjecture for symplectomorphisms"
section_number: 2.3
pages: 13-23
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
Plotkin conjecture for symplectomorphisms.
2.3.1. Plotkin’s problem for symplectomorphism and the Kontsevic h conjec-
ture. Observe that the study of automorphisms of the group of polyn omial symplecto-
morphisms, as well as automorphisms of the Weyl algebra (Plo tkin’s problem) is extremely
important in course of the Kontsevich conjecture, as well as the Jacobian conjecture.
14 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
2.3.2. Ultraﬁlters and inﬁnite primes. Let U ⊂ 2N be an arbitrary non-principal
ultraﬁlter on the set of all positive numbers (in this note N will almost always be regarded
as the index set). Let P be the set of all prime numbers, and let PN denote the set of all
sequences p = ( pm)m∈N of prime numbers. We refer to a generic set A ∈ U as an index
subset in situations involving the restriction p|A : A → P. We will call a sequence p of
prime numbers U-stationary if there is an index subset A ∈ U such that its image p(A)
consists of one point.
A sequence p : N → P is bounded if the image p(N) is a ﬁnite set. Thanks to the
ultraﬁlter ﬁnite intersection property, bounded sequence s are necessarily U-stationary.
Any non-principal ultraﬁlter U generates a congruence
∼U ⊆ PN × PN
in the following way. Two sequences p1 and p2 are U-congruent iﬀ there is an index subset
A ∈ U such that for all m ∈ A the following equality holds:
p1
m = p2
m.
The corresponding quotient
∗P ≡ PN/ ∼U
contains as a proper subset the set of all primes P (naturally identiﬁed with classes of U-
stationary sequences), as well as classes of unbounded sequ ences. The latter are referred to
as nonstandard, or inﬁnitely large, primes. We will use both names and normally denote
such elements by [ p], mirroring the convention for equivalence classes. The te rminology is
justiﬁed, as the set of nonstandard primes is in one-to-one c orrespondence with the set of
prime elements in the ring ∗Z of nonstandard integers in the sense of Robinson [96].
Indeed, one may utilize the following construction, which w as thoroughly studied 1
in [49]. Consider the ring Zω = ∏
m∈N Z - the product of countably many copies of
Z indexed by N. The minimal prime ideals of Zω are in bijection with the set of all
ultraﬁlters on N (perhaps it is opportune to remind that the latter is precise ly the Stone-
Cech compactiﬁcation β N of N as a discrete space). Explicitly, if for every a = (am) ∈ Zω
one deﬁnes the support complement as
θ(a) = {m ∈ N | am = 0}
and for an arbitrary ultraﬁlter U ∈ 2N sets
(U) = {a ∈ Zω | θ(a) ∈ U} ,
then one obtains a minimal prime ideal of Zω . It is easily shown that every minimal prime
ideal is of such a form. Of course, the index set N may be replaced by any set I, after
which one easily gets the description of minimal primes of ZI (since those correspond to
ultraﬁlters, there are exactly 2 2|I|
of them if I is inﬁnite and |I| when I is a ﬁnite set).
Note that in the case of ﬁnite index set all ultraﬁlters are pr incipal, and the corresponding
(U) are of the form Z × · · · × (0) × · · · × Z - a textbook example.
Similarly, one may replace each copy of Z by an arbitrary integral domain and repeat
the construction above. If for instance all the rings in the p roduct happen to be ﬁelds,
then, since the product of any number of ﬁelds is von Neumann r egular, the ideal ( U) will
also be maximal.
The ring of nonstandard integers may be viewed as a quotient ( an ultrapower)
Zω / (U) = ∗Z.
The class of U-congruent sequences [ p] corresponds to an element (also an equivalence
class) in ∗Z, which may as well as [ p] be represented by a prime number sequence p = (pm),
only in the latter case some but not too many of the primes pm may be replaced by
arbitrary integers. For all intents and purposes, this diﬀe rence is insigniﬁcant.
1also cf. [14]
SOME LOGICAL ASPECTS 15
Also, observe that [ p] indeed generates a maximal prime ideal in ∗Z: if one for (any)
p ∈ [p] deﬁnes an ideal in Zω as
(p, U) = {a ∈ Zω | {m | am ∈ pmZ} ∈ U} ,
then, taking the quotient Zω / (p, U) in two diﬀerent ways, one arrives at an isomorphism
∗Z/ ([p]) ≃
(∏
m
Zpm
)
/ (U),
and the right-hand side is a ﬁeld by the preceding remark. For a ﬁxed non-principal U
and an inﬁnite prime [ p], we will call the quotient
Z[p] ≡ ∗Z/ ([p])
the nonstandard residue ﬁeld of [ p]. Under our assumptions this ﬁeld has characteristic
zero.
2.3.3. Algebraic closure of nonstandard residue ﬁeld. We have seen that the objects
[p] - the inﬁnite prime - behaves similarly to the usual prime nu mber in the sense that a
version of a residue ﬁeld corresponding to this object may be constructed. Note that the
standard residue ﬁelds are contained as a degenerate case in this construction, namely if
we drop the condition of unboundedness and instead consider U-stationary sequences, we
will arrive at a residue ﬁeld isomorphic to Zp, with p being the image of the stationary
sequence in the chosen class. The ﬁelds of the form Z[p] are a realization of what is known
as pseudoﬁnite ﬁeld, cf. [7].
The nonstandard case is surely more interesting. While the a lgebraic closure of a
standard residue ﬁeld is countable, the nonstandard one its elf has the cardinality of the
continuum. Its algebraic closure is also of that cardinalit y and has characteristic zero,
which implies that it is isomorphic to the ﬁeld of complex num bers. We proceed by
demonstrating these facts.
Proposition 2.31. For any inﬁnite prime [p] the residue ﬁeld Z[p] has the cardinality of
the continuum 2.
Proof. It suﬃces to show there is a surjection
h∗ : Z[p] → P,
where P = {0, 1}ω is the Cantor set given as the set of all countable strings of b its
with the 2-adic metric
d2(x, y ) = 1 /k, k = min{m | xm ⁄= ym}.
The map h∗ is constructed as follows. If Z ⊂ P is the subset of all strings with ﬁnite
number of ones in them, and
e : Z+ → Z, e
(∑
k<m
fk2k
)
= (f1, . . . , f m−1, 0, . . . )
is the bijection that sends a nonnegative integer to its bina ry decomposition, then for a
class representative a = ( am) ∈ [a] ∈ Z[p] set h∗(a) to be the (unique) ultralimit of the
sequence of points {xm = e(am)}. The correctness of this map rests on the property of
the Cantor set being Hausdorﬀ quasi-compact. Surjectivity is then established directly:
consider an arbitrary x ∈ P. For each m ∈ N the set
Pm = {e(0), e (1), . . . , e (pm − 1)}
2There is a general statement on cardinality of ultraproduct due to Frayne, Morel, and Scott [20].
We believe the proof of this particular instance may serve as a neat example of what we are dealing
with in the present paper.
16 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
consists of pm distinct points. Let xm be the nearest to x point from this set with respect
to the 2-adic metric. The sequence ( pm) is unbounded, so that for every m ∈ N the index
subset
Am = {k ∈ N | pk > 2m}
belongs to the ultraﬁlter U. It is easily seen that for every k ∈ Am one has:
d2(x, x k) < 1/m
But that eﬀectively means that the sequence ( xm) has the ultralimit x, after which am =
e−1(xm) yields the desired preimage. □
As an immediate corollary of this proposition and the well-k nown Steinitz theorem,
one has
Theorem 2.32. The algebraic closure
Z[p] of Z[p] is isomorphic to the ﬁeld of complex
numbers.
We now ﬁx the notation for the aforementioned isomorphisms i n order to employ it in
the next section.
For any nonstandard prime [ p] ∈ ∗P ﬁx an isomorphism α [p] : C → Z[p] coming from the
preceding theorem. Denote by Θ [p] : Z[p] → Z[p] the nonstandard Frobenius automorphism
- that is, a well-deﬁned ﬁeld automorphism that sends a seque nce of elements to a sequence
of their pm-th powers:
(xm) ↦→(xpm
m ).
The automorphism Θ [p] is identical on Z[p]; conjugated by α [p], it yields a wild auto-
morphism of complex numbers, as by assumption no ﬁnite power of it (as always, in the
sense of index subsets A ∈ U ) is the identity homomorphism.
2.3.4. Extension of the W eyl algebra. The n-th Weyl algebra An, C ≃ An, Z[p]
can be
realized as a proper subalgebra of the following ultraprodu ct of algebras
An(U, [p]) =
(∏
m∈N
An, Fpm
)
/ U.
Here for any m the ﬁeld Fpm = Zpm is the algebraic closure of the residue ﬁeld Zpm .
This larger algebra contains elements of the form ( ζIm )m∈N with unbounded |Im| - some-
thing which is not present in An, Z[p]
, hence the proper embedding. Note that for the exact
same reason (with degrees |Im| of diﬀerential operators having been replaced by degrees
of minimal polynomials of algebraic elements) the inclusio n
Z[p] ⊆
(∏
m∈N
Fpm
)
/ U
is also proper.
It turns out that, unlike its standard counterpart An, C, the algebra An(U, [p]) has a
huge center described in this proposition:
Proposition 2.33. The center of the ultraproduct of Weyl algebras over the sequ ence of
algebraically closed ﬁelds {Fpm } coincides with the ultraproduct of centers of An, Fpm :
C(An(U, [p])) =
(∏
m
C(An, Fpm )
)
/ U.
SOME LOGICAL ASPECTS 17
The proof is elementary and is left to the reader. As in positi ve characteristic the
center C(An, Fp ) is given by the polynomial algebra
Fp[xp
1, . . . , x p
n, y p
1 , . . . , y p
n] ≃ Fp[ξ1, . . . , ξ 2n],
there is an injective C-algebra homomorphism
C[ξ1, . . . ξ 2n] →
(∏
m
Fpm [ξ(m)
1 , . . . ξ (m)
2n ]
)
/ U
from the algebra of regular functions on A2n
C to the center of An(U, [p]), evaluated on
the generators in a straightforward way:
ξi ↦→[(ξ(m)
i )m∈N].
Just as before, this injection is proper.
Furthermore, the image of this monomorphism (the set which w e will simply refer to
as the polynomial algebra) may be endowed with the canonical Poisson bracket. Recall
that in positive characteristic case for any a, b ∈ Zp[ξ1, . . . , ξ 2n] one can deﬁne
{a, b } = −π
([a0, b 0]
p
)
.
Here π : An, Z → An, Zp is the modulo p reduction of the Weyl algebra, and a0, b 0 are
arbitrary lifts of a, b with respect to π . The operation is well deﬁned, takes values in the
center and satisﬁes the Leibnitz rule and the Jacobi identit y. On the generators one has
{ξi, ξ j} = ω ij.
The Poisson bracket is trivially extended to the entire cent er Fp[ξ1, . . . , ξ 2n] and then to
the ultraproduct of centers. Observe that the Poisson brack et of two elements of bounded
degree is again of bounded degree, hence one has the bracket o n the polynomial algebra.
2.3.5. Endomorphisms and symplectomorphisms. The point of this construction
lies in the fact that thus deﬁned Poisson structure on the (in jective image of) polynomial
algebra is preserved under all endomorphisms of An(U, [p]) of bounded degree. Every
endomorphism of the standard Weyl algebra is speciﬁed by an a rray of coeﬃcients ( ai,I )
(which form the images of the generators in the standard basi s); these coeﬃcients are al-
gebraically dependent, but with only a ﬁnite number of bound ed-order constraints. Hence
the endomorphism of the standard Weyl algebra can be extende d to the larger algebra
An(U, [p]). The restriction of any such obtained endomorphism on the polynomial algebra
C[ξ1, . . . , ξ 2n] preserves the Poisson structure. In this setup the automor phisms of the
Weyl algebra correspond to symplectomorphisms of A2n
C .
Example. If xi and yi are standard generators, then one may perform a linear sym-
plectic change of variables:
f (xi) =
n∑
j=1
aijxj +
n∑
j=1
ai,n +j yj, i = 1, . . . , n,
f (di) =
n∑
j=1
ai+n,j xj +
n∑
j=1
ai+n,n +jyj , a ij ∈ C.
In this case the corresponding polynomial automorphism f c of
C[ξ1, . . . , ξ 2n] ≃ C[x[p]
1 , . . . , x [p]
n , y [p]
1 , . . . , y [p]
n ]
acts on the generators ξ as
f c(ξi) =
2n∑
j=1
(aij)[p]ξj,
18 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
where the notation ( aij)[p] means taking the base ﬁeld automorphism that is conjugate to
the nonstandard Frobenius via the Steinitz isomorphism.
Let γ : C → C be an arbitrary automorphism of the ﬁeld of complex numbers. Then,
given an automorphism f of the Weyl algebra An, C with coordinates ( ai,I ), one can build
another algebra automorphism using the map γ. Namely, the coeﬃcients γ(ai,I ) deﬁne a
new automorphism γ∗(f ) of the Weyl algebra, which is of the same degree as the origin al
one. In other words, every automorphism of the base ﬁeld indu ces a map γ∗ : An, C → An, C
which preserves the structure of the ind-object. It obvious ly is a group homomorphism.
Now, if Pn, C denotes the commutative polynomial algebra with Poisson br acket, we may
deﬁne an ind-group homomorphism ϕ : Aut( An, C) → Aut(PnC) as follows. Previously
we had a morphism f ↦→f c, however as the example has shown it explicitly depends
on the choice of the inﬁnite prime [ p]. We may eliminate this dependence by pushing
the whole domain Aut( An, C) forward with a speciﬁc base ﬁeld automorphism γ, namely
γ = Θ −1
[p] - the ﬁeld automorphism which is Steinitz-conjugate with th e inverse nonstandard
Frobenius, and only then constructing the symplectomorphi sm f c
Θ as the restriction to the
(nonstandard) center. For the subgroup of tame automorphis ms such as linear changes of
variables this procedure has a simple meaning: just take the [p]-th root of all coeﬃcients
(ai,I ) ﬁrst. We thus obtain a group homomorphism which preserves t he ﬁltration by
degree and is in fact well-behaved with respect to the Zarisk i topology on Aut (indeed,
the ﬁltration Aut N ⊂ AutN+1 is given by Zariski-closed embeddings). Formally, we have
a proposition:
Proposition 2.34. There is a system of morphisms
ϕ [p],N : Aut ≤N (An, C) → Aut≤N (Pn, C).
such that the following diagram commutes for all N ≤ N ′:
Aut≤N (An, C) Aut ≤N (Pn, C)
Aut≤N ′
(An, C) Aut ≤N ′
(Pn, C)
ϕ [p],N
µ N N′ ν N N′
ϕ [p],N′
The corresponding direct limit of this system is given by ϕ [p], which maps a Weyl algebra
automorphism f to a symplectomorphism f c
Θ .
The Belov – Kontsevich conjecture then states:
Conjecture 2.35. ϕ [p] is a group isomorphism.
Injectivity may be established right away.
Theorem 2.36. ϕ [p] is an injective homomorphism.
(See [37] for the fairly elementary proof).
2.3.6. On the loops related to inﬁnite primes. Let us at ﬁrst assume that the Belov
– Kontsevich conjecture holds, with ϕ [p] furnishing the isomorphism between the auto-
morphism groups. This would be the case if all automorphisms in Aut( An, C) were tame,
which is unknown at the moment for n > 1.
The main result of the paper is as follows:
Theorem 2.37. If one assumes that ϕ [p],N is surjective for any inﬁnite prime [p], then
Φ N is quasiﬁnitedimensional and its eigenvalues are roots of u nity.
SOME LOGICAL ASPECTS 19
Let [ p] and [ p′] be two distinct classes of U-congruent prime number sequences - that
is, two distinct inﬁnite primes. We then have the following d iagram:
Aut(An, C) Aut( Pn, C)
Aut(An, C) Aut( Pn, C)
ϕ [p]
isom isom
ϕ [p′]
with all arrows being isomorphisms. Vertical isomorphisms answer to diﬀerent presenta-
tions of C as Z[p] and Z[p′]. The corresponding automorphism C → Z[p] is denoted by α [p]
for any [ p].
The fact that all the arrows in the diagram are isomorphisms a llows one instead to
consider a loop of the form
Φ : Aut( An, C) → Aut(An, C).
Furthermore, as it was noted in the previous section, the mor phism Φ belongs to
Aut(Aut(An, C)).
We need to prove that Φ is a trivial automorphism. The ﬁrst obs ervation is as follows.
Proposition 2.38. The map Φ is a morphism of algebraic varieties.
Proof. Basically, this is a property of ϕ [p] (or rather its unshifted version, fp ↦→f c
p ). More
precisely, it suﬃces to show that, given an automorphism fp of the Weyl algebra in positive
characteristic p with coordinates ( ai,I ), its restriction to the center (a symplectomorphism)
f c
p has coordinates which are polynomials in ( ap
i,I ).
The switch to positive characteristic and back is performed for a ﬁxed f ∈ Aut(An, C)
on an index subset Af ∈ U .
Let f be an automorphism of An, C and let N = deg f be its degree. The automorphism
f is given by its coordinates ai,I ∈ C, i = 1 , . . . , 2n, I = {i1, . . . , i 2n}, obtained from the
decomposition of algebra generators ζi in the standard basis of the free module:
f (ζi) =
∑
i,I
ai,I ζI , ζ I = ζi1
1 · · · ζi2n
2n .
Let ( ai,I,p ) denote the class α [p](ai,I ), p = ( pm), and let {Rk(ai,I | i, I ) = 0 }k=1,...,M
be a ﬁnite set of algebraic constraints for coeﬃcients ai,I . Let us denote by A1, . . . , A M
the index subsets from the ultraﬁlter U, such that Ak is precisely the subset, on whose
indices the constraint Rk is valid for ( ai,I,p ). Take Af = A1 ∩ . . . ∩ AM ∈ U and for
pm, m ∈ Af , deﬁne an automorphism fpm of the Weyl algebra in positive characteristic
An, Fpm by setting
fpm (ζi) =
∑
i,I
ai,I,p m ζI .
All of the constraints are valid on Af , so that f corresponds to a class [ fp] modulo ultraﬁlter
U of automorphisms in positive characteristic. The degree of every fpm (m ∈ Af ) is
obviously less than or equal to N = deg f .
Now consider f ∈ Aut≤N (An, C) with the index subset Af over which its deﬁning
constraints are valid. The automorphisms fpm = fp : An, Fp → An, Fp deﬁned for m ∈
Af ∈ U provide arrays of coordinates ai,I,p . Let us ﬁx any valid pm = p denote by Fpk
a ﬁnite subﬁeld of Fp which contains the respective coordinates ai,I,p (one may take k to
be equal to the maximum degree of all minimal polynomials of e lements ai,I,p which are
algebraic over Zp).
Let a1, . . . , a s be the transcendence basis of the set of coordinates ai,I,p and let t1, . . . , t s
denote s independent (commuting) variables. Consider the ﬁeld of ra tional functions:
20 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
Fpk (t1, . . . , t s).
The vector space
DerZp (Fpk (t1, . . . , t s), Fpk (t1, . . . , t s))
of all Zp-linear derivations of the ﬁeld Fpk (t1, . . . , t s) is ﬁnite-dimensional with
Zp-dimension equal to ks; a basis of this vector space is given by elements
{eaDtb | a = 1, . . . , k, b = 1, . . . , s }
where ea are basis vectors of the Zp-vector space Fpk , and Dtb is the partial derivative
with respect to the variable tb.
Set a1, . . . , a s = t1, . . . , t s (i.e. consider an s-parametric family of automorphisms),
so that the rest of the coeﬃcients ai,I,p are algebraic functions of s variables t1, . . . , t s.
We need to show that the coordinates of the corresponding sym plectomorphism f c
p are
annihilated by all derivations eaDtb .
Let δ denote a derivation of the Weyl algebra induced by an arbitra ry basis derivation
eaDtb of the ﬁeld. For a given i, let us introduce the short-hand notation
a = fp(ζi), b = δ(a).
We need to prove that
δ(f c(ξi)) = δ(fp(ζp
i )) = 0 .
In our notation δ(fp(ζp
i )) = δ(ap), so by Leibnitz rule we have:
δ(fp(ζp
i )) = bap−1 + abap−2 + · · · + ap−1b.
Let ad x : An, Fp → An, Fp denote a Zp-derivation of the Weyl algebra corresponding to
the adjoint action (all Weyl algebra derivations are inner! ):
adx(y) = [ x, y ].
We will call an element x ∈ An, Fp locally ad-nilpotent if for any y ∈ An, Fp there is an
integer D = D(y) such that
adD
x (y) = 0 .
All algebra generators ζi are locally ad-nilpotent. Indeed, one could take D(y) = deg y + 1
for every ζi.
If f is an automorphism of the Weyl algebra, then f (ζi) is also a locally ad-nilpotent
element for all i = 1 , . . . , 2n. That means that for any i = 1 , . . . , 2n there is an integer
D ≥ N + 1 such that
adD
fp(ζi)(δ(fp(ζi))) = ad D
a (b) = 0 .
Now, for p ≥ D + 1 the previous expression may be rewritten as
0 = ad p−1
a (b) =
p−1∑
l=0
(−1)l
(
p − 1
l
)
albap−1−l ≡
p−1∑
l=0
albap−1−l (mod p),
and this is exactly what we wanted.
We have thus demonstrated that for an arbitrary automorphis m fp of the Weyl algebra
in characteristic p the coordinates of the corresponding symplectomorphism f c
p are poly-
nomial in p-th powers of the coordinates of fp, provided that p is greater than deg fp + 1.
As the sequence (deg fpm ) is bounded from above by N for all m ∈ Af , we see that there
is an index subset A∗
f ∈ U such that the coordinates of the symplectomorphism f c
pm for
m ∈ A∗
f are polynomial in pm-th powers of ai,I,p m . This implies that f c in characteristic
zero is given by coeﬃcients polynomial in α [p](ai,I )[p] as desired.
SOME LOGICAL ASPECTS 21
It follows, after shifting by the inverse nonstandard Frobe nius, that Φ is an endomor-
phism of the algebraic variety Aut( An, C). □
The automorphism Φ acting on elements f ∈ Aut(An, C), takes the set of coordinates
(ai,I ) and returns a set ( Gi,I (ak,K )) of the same size. All functions Gi,I are algebraic
by the above proposition. It is convenient to introduce a par tial order on the set of
coordinates. We say that ai,I ′ is higher than ai,I (for the same generator i) if |I| < |I ′|
and we leave pairs with i ⁄= j or with |I| = |I ′| unconnected. We deﬁne the dominant
elements ai,I (or rather, dominant places ( i, I )) to be the maximal elements with respect
to this partial order, and subdominant elements to be the ele ments covered by maximal
ones (in other words, for ﬁxed i, subdominant places are the ones with |I| = |Imax| − 1).
The next observation follows from the fact that the morphism s in question are algebra
automorphisms.
Lemma 2.39. Functions Gi,I corresponding to dominant places (i, I ) are identities:
Gi,I (ak,K ) = ai,I .
Proof. Indeed, it follows from the commutation relations that for a ny i = 1 , . . . , 2n and
fp, p = pm, m ∈ Af ∈ U , the highest-order term in f c
p (ξi) = fp(ζp
i ) = fp(ζi)p has the
coeﬃcient ap
i,I,p . The shift by the inverse Frobenius then acts as the p-th root on the
dominant place, so that we deduce that the latter is independ ent of the choice of [ p]. □
Let us now ﬁx N ≥ 1 and consider
Φ N : Aut ≤N An, C → Aut≤N An, C
– the restriction of Φ to the subvariety Aut ≤N An, C, which is well deﬁned by the above
lemma. The morphism corresponds to an endomorphism of the ri ng of functions
Φ ∗
N : O(Aut≤N An, C) → O (Aut≤N An, C)
Let us take a closer look at the behavior of Φ N (and of Φ ∗
N , which is essentially the
same up to an inversion), speciﬁcally at how Φ N aﬀects one-dimensional subvarieties of au-
tomorphisms. Let XN be the set of all algebraic curves of automorphisms in Aut ≤N An, C;
by virtue of Lemma 3.3 we may without loss of generality consi der the subset of all curves
with ﬁxed dominant places – we denote such a subset by X ′
N , and, for that same matter,
the subsets X (k)
N of curves with ﬁxed places of the form ( i, I ′), which are away from a
dominant place by a path of length at most ( k − 1). In particular one has X ′
N = X (1)
N .
The morphism Φ N yields a map
˜Φ N : XN → X N
and its restrictions
˜Φ (k)
N : X (k)
N → X N .
Our immediate goal is to prove that for all attainable k we have
˜Φ (k)
N : X (k)
N → X (k)
N ,
i.e. the map Φ N preserves the terms corresponding to non-trivial diﬀerent ial monomials.
In spite of minor abuse of language, we will call the highest n on-constant terms of a
curve in X (k)
N dominant, although they cease to be so when that same curve is regarded
as an element of XN .
Let A ∈ X N be an algebraic curve in general position. Coordinate-wise A answers to a
set ( ai,I (τ)) of coeﬃcients parameterized by an indeterminate. By Lemm a 3.3, Φ N leaves
the (coeﬃcients corresponding to) dominant places of this c urve unchanged, so we may
well set A ∈ X (1)
N . In fact, it is easily seen that the subdominant terms are not aﬀected
by Φ N either, thanks to the commutation relations that deﬁne the W eyl algebra: for
every p participating in the ultraproduct decomposition, after on e raises to the p-th power
22 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
one should perform a reordering within the monomials – a proc edure which degrades the
cardinality |I| by an even number. Therefore, nothing contributes to the ima ge of any
subdominant term other than that subdominant term itself, w hich therefore is ﬁxed under
Φ N . We are then to consider the image
˜Φ (2)
N (A) ∈ X (2)
N .
Again, given a positive characteristic p within the ultraproduct decomposition, suppose
the curve A (or rather its component answering to the chosen element p) has a number
of poles attained on dominant 3 terms. Let us pick among these poles the one of the
highest order k, and let ( i0, I 0) be its place. By deﬁnition of an automorphism of Weyl
algebra as a set of coeﬃcients, the number i0 does not actually carry any meaningful
data, so that we are left with a pair ( k, |I0|). As we can see, this pair is maximal from two
diﬀerent viewpoints; in fact, the pair represents a vertex o f a Newton polygon taken over
the appropriate ﬁeld, with the discrete valuation given by |I|. The coordinate function
ai0,I 0 corresponding to this pole admits a decomposition
ai0,I 0 = a−k
tk + · · · ,
with t a local parameter. Acting upon this curve by the morphism Φ N amounts to two
steps: ﬁrst, we raise everything to the p-th power and then assemble the components
within the ultraproduct decomposition, then we take the pre image, which is essentially
the same as taking the p′-root, with respect to a diﬀerent ultraproduct decompositi on.
The order of the maximal pole is then multiplied by an integer during the ﬁrst step and
divided by the same integer during the second one. By maximality, there are no other
terms that might contribute to the resulting place in ˜Φ (2)
N (A). It therefore does not change
under Φ N .
We may process the rest of the dominant (with respect to X (2)
N ) terms similarly: indeed,
it suﬃces to pick a diﬀerent curve in general position. We the n move down to X (k)
N with
higher k and argue similarly.
After we have exhausted the possibilities with non-constan t terms, we arrive at the
conclusion that all that Φ N does is permute the irreducible components of Aut ≤N An, C.
That in turn implies the existence of a positive integer l such that
Φ l
N = Id.
In fact, the preceding argument gives us more than just the ob servation that Φ N is
unipotent. Let Φ ∗
N,M denote the linear map of ﬁnite-dimensional vector spaces ob tained
by restricting Φ ∗
N to regular functions of total degree less than or equal to M . Then the
following proposition holds.
Proposition 2.40. If λ is an eigenvalue of Φ ∗
N,M , then λ k = 1 for some integer k.
Proof. Indeed, should there exist λ 0 ⁄= 1, we may ﬁnd an exceptional curve whose sin-
gularity changes under Φ N , note that coeﬃcients are products of normalization coordi -
nates. □
2.3.7. Discussion. The investigation of decomposition of polynomial algebra- related ob-
jects into ultraproducts over the prime numbers P leads to a problem of independence of
the choice of inﬁnite prime. In the case of the Tsuchimoto – Be lov – Kontsevich homo-
morphism the answer turns out to be aﬃrmative, although ther e are other constructions,
which are of algebraic or even polynomial nature but for whic h the independence fails.
The reason for such arbitrary behavior has a lot to do with gro wth functions (in which
3With respect to X (2)
N , i.e. the highest terms that actually change - see above wher e we specify this
convention.
SOME LOGICAL ASPECTS 23
case the situation is similar to the one described in[55], an d in fact in[105], where one
has a non-injective endomorphism fp : An, Fp → An, Fp , whose degree grows with p, which
disallows for the construction of a naive counterexample to the Dixmier Conjecture in the
ultralimit). It is, in our view, worthwhile to study such beh avior in greater detail.
