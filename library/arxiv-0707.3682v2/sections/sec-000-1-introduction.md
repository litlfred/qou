---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-9
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
The Beilinson conjectures about special values of L-functions [2] are a far reach-
ing generalization of the class number formula for the Dedekind zeta function. For
every algebraic variety X over the rationals it predicts the leading term of the
Taylor expansions of L(Hi(X),s ) at certain points, up to a rational multiple, in
terms of arithmetic information associated with X, namely, its algebraic K-groups
Kj(X) [43]. More generally, these conjectures can also be formulated fo r motives.
There have been several important steps taken towards veriﬁca tion of these con-
jectures in various cases, although, strictly speaking they have o nly been veriﬁed
completely in the case where X is the spectrum of a number ﬁeld, where they follow
from famous theorems of Borel [10, 11].
To motivate what follows, let us brieﬂy recall the conjecture that in terests us
the most (for an introduction see [23, 46]). One associates with X two cohomology
groups. The ﬁrst one is the Deligne cohomology Hi
D(X/R, R(n)), which is an R-
vector space. The second is “integral” motivic cohomology Hi
M (X/Z, Q(n)), which
may be deﬁned as a certain subspace of K2n−i(X) ⊗Z Q. There is a regulator map
deﬁned by Beilinson,
(1.1) Hi
M (X/Z, Q(n)) →Hi
D(X/R, R(n)).
If 2n > i+ 1 then det Hi
D(X/R, R(n)) has a rational structure coming from the
relations between Hi
D(XR, R(n)) and the de Rham and singular cohomology groups
of X [46, p.30].
The ﬁrst part of the conjecture is that the map in (1.1) induces an is omorphism
between the lefthand side tensored with R and the righthand side, and consequently
2000 Mathematics Subject Classiﬁcation. Primary: 19F27; secondary: 11G55, 11R42, 11R70.
Key words and phrases. Beilinson conjecture, Borel’s theorem, number ﬁeld, Artin motive,
syntomic regulator, p-adic L-function.
1
2 AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRAN C ¸ OIS ROBLOT
provides a second rational structure on det Hi
D(X/R, R(n)). The second part of the
conjecture states that, assuming a suitable functional equation for L(Hi−1(X),s ),
these two rational structures diﬀer from each other by the leadin g term in the
Taylor expansion of L(Hi−1(X),s ) at s =i −n. Because of the expected functional
equation one can reformulate the conjecture in terms of L(Hi−1(X),n ) (see [2,
Corollary 3.6.2] or [31, 4.12]).
As mentioned before, this conjecture has only been veriﬁed in the c ase of number
ﬁelds, due to diﬃculties in the computation of motivic cohomology. Wha t has been
veriﬁed in several other cases is a form of the conjecture in which o ne assumes
the ﬁrst part. For this one ﬁnds dim RHi
D(X/R, R(n)) elements of Hi
M (X/Z, Q(n)),
checks that their images under (1.1) are independent, hence shou ld form a basis of
Hi
M (X/Z, Q(n)) according to the ﬁrst part of the conjecture, and veriﬁes the second
part using these elements.
The idea that there should be a p-adic analogue of Beilinson’s conjectures has
been around since the late 80’s. Such a conjecture was formulated and proved by
Gros in [29, 30] in the case of Artin motives associated with Dirichlet ch aracters.
In the weak sense mentioned before, it was proved for certain CM e lliptic curves
in [17] (where the relation with the syntomic regulator is proved in [4] a nd fur-
ther elucidated in [7]), and for elliptic modular forms it follows from Kato ’s work
(see [47]).
The book [42] contains a very general conjecture about the exist ence and proper-
ties of p-adicL-functions, from which one can derive a p-adic Beilinson conjecture.
Rather than explain this in full detail we shall give a sketch of this con jecture
similar to the sketch above of the Beilinson conjecture.
For thep-adic Beilinson conjectures one has to replace Deligne cohomology wit h
syntomic cohomology [30, 41, 3], the Beilinson regulator with the synt omic regula-
tor, and L-functions with p-adic L-functions.
Syntomic cohomology Hi
syn(Y,n ) is deﬁned for a smooth scheme Y of ﬁnite type
over a complete discrete valuation ring of mixed characteristic (0 ,p ) with perfect
residue ﬁeld. For the Q-varietyX we obtain, for all but ﬁnitely many primes, a
map
(1.2) Hi
M (X/Z, Q(n)) →Hi
syn(Y,n )
where Y is a smooth model for X over Zp. This cohomology group is a Qp-vector
space.
The theory of p-adic L-functions starts with Kubota and Leopoldt’s p-adic ζ-
function [35], ζp(s), which is deﬁned by interpolating special values of complex
valued DirichletL-functions. This principle has been extended to ζ- andL-functions
in various situations, resulting in corresponding p-adic functions for totally real
number ﬁelds [1, 15, 22], CM ﬁelds [32, 33] and modular forms [37]. (Giv en the
occasion, let us note that the approach of Deligne and Ribet using mo dular forms
was initiated by Serre [48].)
Thep-adic Beilinson conjecture therefore has many similarities with its com plex
counterpart. However, there is a very important diﬀerence. In g eneral, when 2n>
i+1, there is no hope that (1.2) induces an isomorphism after tensor ing the lefthand
side with Qp. To see this, consider a number ﬁeld k with ring of algebraic integers
Ok. By Borel’s theorem (see Theorem 2.2) we have, in accordance with B eilinson’s
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 3
conjectures,
dimQH 1
M (Spec(k)/Z, Q(n)) =
{ r2 when n ≥ 2 is even
r1 +r2 when n ≥ 2 is odd
with r1 (resp. 2r2) the number of real (resp. complex) embeddings of k. Thus,
motivic cohomology “knows” about the number of real and complex e mbeddings
of k, as does, by its deﬁnition, Deligne cohomology, which in this case beco mes
H 1
D(Spec(k)/R, R(n)) ∼
= {(xσ)σ:k→C in R(n − 1)r1+2r2 such that
xσ = xσ}. But
syntomic cohomology, which depends only on the completion of k at p, does not.
In this case, we obtain H 1
syn(Spec(Ok ⊗Z Zp),n ) ∼
= Qr1+2r2
p .
The solution to this problem suggested in [42] is to make the p-adic L-function
depend on a subspace of syntomic cohomology which is complementar y to the
image of the regulator. While this might seem artiﬁcial, there are othe r reasons for
choosing this solution. In most cases one chooses a particular subs pace and obtains
a special case of the conjecture.
In the important special case of a totally real number ﬁeld, or more generally an
Artin motive over Q, associated with a Galois representation whose kernel is totally
real (let us call these totally real Artin motives), no such subspac e is required when
n ≥ 2 is odd (see Proposition 3.12). The same holds for Artin motives wher e the
conjugacy class of complex conjugation acts as multiplication by −1 and n ≥ 2 is
even (we may think of those as the “negative part” of CM Artin motiv es).
Ifχ denotes the character associated with either representation, t hen the Beilin-
son conjecture relates the regulator of K2n−1 with the Artin L-function of χ at n.
For the p-adic L-functions one has to consider χ ⊗ω1−n
p with ωp the Teichm¨ uller
character for the prime number p. Then the ﬁxed ﬁeld of the kernel of the rep-
resentation underlying χ ⊗ω1−n
p is totally real, and it is perhaps no coincidence
that in precisely this case the existence of a p-adicL-function that is not identicaly
zero has been established, by [1, 15, 22] for the case of ﬁelds and b y [28] for Artin
motives.
The goal of the present work is to describe in detail the conjectur es for the cases
of totally real ﬁelds, totally real Artin motives, as well as the “nega tive part” of
CM Artin motives, and describe the (conjectural) relation between the classical and
p-adic conjectures. We test everything numerically in several case s, and also deduce
most of the conjectures for Abelian Artin motives from work by Cole man [16].
There have been several developments that allow us to carry out t his numerical
veriﬁcation. In [19] de Jeu proved part of Zagier’s conjecture co ncerning a more
explicit description of the K-theory (tensored with Q) of number ﬁelds (see Sec-
tion 4). While this conjecture is not known to give the K-theory of su ch ﬁelds
in all cases, it does in practice. Thus it provides a way of computing th em, and
Paul Buckingham wrote a computer implementation for this. In [5] B esser and
de Jeu computed the syntomic regulator for (essentially) the part of the K-theory
of a number ﬁeld described by Zagier’s conjecture and showed that it is given by
applying the p-adic polylogarithm. Those p-adic polylogarithms were invented by
Coleman [16] using his theory of p-adic integration but are not so easy to compute.
In [6] Besser and de Jeu devised an algorithm for this computation. T aken together,
these developments allow us to compute (1.1) and (1.2) for number ﬁ elds. Finally,
building on earlier work in [45], Roblot has dealt with the computational a spects
4 AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRAN C ¸ OIS ROBLOT
of computing p-adic L-functions for Abelian characters over Q or a real quadratic
ﬁeld [44].
This paper is organized as follows. In Section 2 we recall Borel’s theor em as
well as various facts about L-functions and p-adic L-functions, and formulate a
conjectural p-adic analogue of Borel’s theorem. In Section 3 we introduce Artin
motives with coeﬃcients in a number ﬁeld E in terms of representations of the Ga-
lois group, determine when the Q-dimension of the left-hand side of (1.2) equals the
Qp-dimension of the right-hand side (corresponding to equality in Prop osition 3.12),
deﬁne both classical and p-adicL-functions with coeﬃcients in E, and formulate the
motivic Beilinson conjecture with coeﬃcients in E, Conjecture 3.18, a small part of
which is the same as a conjecture by Gross. In Section 4 we describe the set-up for
ﬁnding elements in the K-groups of number ﬁelds using Zagier’s conjecture, and
the classical and p-adic regulators on them. We also prove most of Conjecture 3.18
for Abelian Artin motives over Q (Proposition 4.17 and Remark 4.18). In Section 5
we discuss a few computational aspects of implementing Zagier’s con jecture and
describe the Artin motives that we consider later for the numerical examples, and
in the process prove Gross’s conjecture for Artin motives obtaine d from S3 and
D8-extensions of Q. Then in Section 6 we sketch how the p-adic L-functions can
be computed in certain cases, and make the required Brauer induct ion explicit for
the Artin motives we want to consider. Finally, the last section is devo ted to the
results of the numerical calculations for examples.
Amnon Besser, Paul Buckingham and Rob de Jeu would like to thank th e EC
network Arithmetic Algebraic Geometry for travel support. Rob d e Jeu would like
to thank the Tata Institute of Fundamental Research for a prod uctive stay during
which this paper was worked on, and the Nuﬃeld Foundation for a gra nt under
the Undergraduate Research Bursary programme (NUF-URB03) that enabled Paul
Buckingham to develop a computer program for ﬁnding the necessa ry elements in
K-theory. Amnon Besser would like to thank the Institute for Advan ced Study
in Princeton for a stay during which part of the paper was worked on , and the
Bell companies Fellowship and the James D. Wolfensohn fund for ﬁnan cial support
while at the institute. Finally, the authors would like to thank Alfred We iss for
very useful explanations about p-adic L-functions, and, in particular, for bringing
to their attention the paper [28].
Notation
Throughout the paper, for an Abelian group A we let AQ denoteA ⊗Z Q. If B is a
subgroup of C andn an integer then we let B(n) = (2πi)nB ⊆ C We normalize the
absolute value | · |p on the ﬁeld of p-adic numbers Qp in such a way that |p|p =p−1,
and use the same notation for its extensions to an algebraic closure
Qp and Cp = ˆQp.
2. The p-adic Beilinson conjecture for totally real fields
Let k be a number ﬁeld with r1 real embeddings, 2 r2 complex embeddings,
ring of algebraic integers Ok, and discriminant Dk. As is well-known, O∗
k is a
ﬁnitely generated Abelian group of rank r = r1 + r2 − 1, and its regulator R
satisﬁes w
√
|Dk| Ress=1ζk(s) = 2 r1(2π)r2 |Cl(Ok)|R, with Cl( Ok) the class group
of Ok, and w the number of roots of unity in k. Because K0(Ok) ∼
= Cl(Ok) ⊕ Z
and K1(Ok) ∼
= O∗
k, so |Cl(Ok)| = |K0(Ok)tor| and w = |K1(Ok)tor|, this can be
interpreted as a statement about the K-theory of Ok, and it is from this point
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 5
of view that it can be generalized to ζk(n) for n ≥ 2. Namely, in [43], Quillen
proved that Km(Ok) is a ﬁnitely generated Abelian group for all m. Borel in [10]
computed its rank when m ≥ 2. For m even this rank is zero, but for odd m it is
r1 +r2 orr2, and in [11] he showed that a suitably deﬁned regulator of K2n−1(Ok)
is related to ζk(n). Since K2n−1(Ok)
∼
→ K2n−1(k) when n ≥ 2 we can rephrase
his results for K2n−1(Ok) in terms of K2n−1(k). Also, we replace Borel’s regulator
map regB :K2n−1(C) → R(n − 1) (n ≥ 2) with Beilinson’s regulator map reg ∞ (see
[46, § 4]), which is half the Borel map regulator by [12, Theorem 10.9]. Becau se
k ⊗Q C ∼
= ⊕σ:k→CC, and n> dim Spec(k ⊗ C), we obtain by [46, p.9]
(2.1)
H 1
D(Spec(k ⊗ C)/R, R(n)) ∼
=H 0(Spec(k ⊗ C)/R, R(n − 1))
∼
=
(⨁
σ:k→C
R(n − 1)
) +
,
which consists of those ( xσ)σ with x
σ =xσ. Finally, for any embedding σ :k → C
we let σ∗ :K2n−1(k) →K2n−1(C) be the induced map.
Theorem 2.2. (Borel) Letk be a number ﬁeld of degree d, with r1 real embeddings
and 2r2 complex embeddings, and let n ≥ 2. Then the rank mn of K2n−1(k) equals
r2 if n is even and r1 +r2 if n is odd. Moreover, the map
(2.3)
K2n−1(k) →
⨁
σ:k→C
R(n − 1)
α ↦→(reg∞ ◦σ∗(α))σ
embeds K2n−1(k)/torsion as a lattice in (⊕σR(n − 1))+ ∼
= Rmn , and the volume
Vn(k) of a fundamental domain of this lattice satisﬁes
(2.4) ζk(n)
√
|Dk| =qπn(d−mn)Vn(k)
for some q in Q∗.
Remark 2.5. In Theorem 2.2 mn = 0 precisely when k is totally real and n ≥ 2
is odd. In this case the given relation holds (with Vn(k) = 1) by the Siegel-Klingen
theorem [40, Chapter VII, Corollary 9.9].
This theorem is equivalent with Beilinson’s conjecture for k. In order to deal
with this in detail (see Remarks 2.20 and 3.24) and in order to introduc e p-adic
L-functions we recall some facts about Artin L-functions [40, Chapter VII, § 10-12].
Let k be a number ﬁeld, d = [k : Q], and let χ be a C-valued Artin character of
Gal(k/k). For a prime number ℓ we deﬁne
Eulℓ(s,χ,k ) =
∏
l|ℓ
Eull(s,χ,k )
where Eul l(s,χ,k ) is the reciprocal of the Euler factor for l and the product is over
primes l of k lying above ℓ. Then for s ∈ C with Re(s)> 1 we can write the Artin
L-function of χ as
L(s,χ,k ) =
∏
ℓ
Eulℓ(s,χ,k )−1.
For an inﬁnite place v of k we let
Lv(s,χ,k ) =
{ LC(s)χ(1) when v is complex,
LR(s)n+
LR(s + 1)n−
when v is real,
6 AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRAN C ¸ OIS ROBLOT
whereLR(s) = π−s/2Γ(s/2), LC(s) = 2(2π)−sΓ(s) and n± = d
2χ(1) ±∑
v
1
2χ(Frw),
with the sum taken over the real places v of k and Frw the generator of the image
of Gal( C/R) in Gal(k/k) corresponding to any extension w :k → C of v. Then
Λ(s,χ,k ) = L(s,χ,k )
∏
v|∞
Lv(s,χ,k )
extends to a meromorphic function, satisfying the functional equ ation (cf. [40, p.
541])
Λ(s,χ,k ) = W (χ)C(χ,k )1/2C(χ,k )−sΛ(1 −s,χ,k )
withW (χ) a constant of absolute value 1 and C(χ,k ) = |Dk|χ(1)Nmk/Q(f(χ,k )) for
f(χ,k ) the Artin conductor of χ. Therefore
(2.6)
L(1 −s,χ,k ) = W (χ)C(χ,k )s− 1
2 (2(2π)−sΓ(s))dχ(1)
× (cos(πs/2))n+
(sin(πs/2))n−
L(s,χ,k ).
Following [28, pp. 80–81] we shall now describe a p-adic L-function Lp(s,χ,k )
when k is a totally real number ﬁeld, p a prime and χ : Gal(k/k) → Qp a suitable
Artin character. We begin with the case of 1-dimensional Artin char acters.
If σ : Qp → C is any isomorphism then σ ◦χ is a complex Artin character, so
we have the Artin L-function L(s,σ ◦χ,k ). We may also view χ as a character of
a suitable ray class group, so by [40, Corollary 9.9 and page 509] all L(m,σ ◦χ,k )
for m ∈ Z≤0 are in Q(σ ◦χ) and the values
(2.7) L∗(m,χ,k ) = σ−1(L(m,σ ◦χ,k ))
are independent of the choice of σ.
In the same way, we deﬁne
(2.8) Eul ∗
ℓ (m,χ,k ) = σ−1(Eulℓ(m,σ ◦χ,k )),
which is clearly independent of the choice of σ. To construct the p-adicL-function
one ﬁnds a p-adic analytic or meromorphic function on an open ball around 0 that
interpolates the values L∗(m,χ,k ). For 1-dimensional χ with the ﬁxed ﬁeld kχ of
its kernel totally real this was achieved independently by Deligne and Ribet [22],
Barsky [1], and Cassou-Nogu` es [14, 15]. We shall sketch a proof of the following
theorem and Remark 2.13 below in Section 6. (When kχ is not totally real the
p-adicL-function is identically zero since the values interpolated are all zero by the
functional equation of the L-function.)
Theorem 2.9. Forp prime, let B in Cp be the open ball with centre 0 and radius
qp−1/(p−1) where q = p if p >2 and q = 4 if p = 2 . If k is a totally real number
ﬁeld and χ : Gal(
k/k) → Qp a 1-dimensional Artin character, then there exists a
unique Cp-valued function Lp(s,χ,k ) on B satisfying the following properties:
(1) Lp(s,χ,k ) is analytic if χ is non-trivial and meromorphic with at most a
simple pole at s = 1 if χ is trival;
(2) if m is a negative integer such that m ≡ 1 moduloϕ(q) then
Lp(m,χ,k ) = Eul ∗
p(m,χ,k )L∗(m,χ,k ).
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 7
If χ : Gal(k/k) → Qp is any Artin character then by Brauer’s induction theo-
rem [40, (10.3)] there exist 1-dimensional Artin characters χ1,...,χ t on subgroups
G1,...,G t of Gal(k/k) of ﬁnite index, and integers a1,...,a t, such that
(2.10) χ =
t∑
i=1
aiIndGal(k/k)
Gi (χi).
If kχ is totally real then we can assume that the same holds for the ﬁxed ﬁ elds ki
of the Gi, and we deﬁne the p-adic L-function of χ by
(2.11) Lp(s,χ,k ) =
t∏
i=1
Lp(s,χi,ki)ai,
which is a meromorphic function on B (see Section 6). For any negative integer m ≡
1 modulo ϕ(q) the value Lp(m,χ,k ) is deﬁned and equals Eul ∗
p(m,χ,k )L∗(m,χ,k )
by well-known properties of Artin L-functions (see [40, Prop. 10.4(iv)]), showing
the function is independent of how we express χ as a sum of induced 1-dimensional
characters.
Remark 2.12. In [28], Greenberg proves that the Main Conjecture of Iwasawa
theory implies the p-adic Artin conjecture, that is, that the p-adicL-function of an
Artin character χ is analytic on the open ball B if it does not contain the trivial
character, and has at most a simple pole at s = 1 otherwise. It therefore follows
from the proof of the Main Conjecture by Mazur and Wiles [38] for p odd that
Lp(n,χ,k ) for p ⁄= 2 is deﬁned for all integers n ⁄= 1. In particular, the values of
thep-adicL-functions in Conjecture 2.17 below exist by Theorem 2.9, and those in
Conjecture 3.18 exist when p ⁄= 2 but have to be assumed to exist when p = 2.
Remark 2.13. Let Wp ⊂ Z∗
p be the subgroup of ( p − 1)-th roots of unity if p is
odd and let W2 = {±1}. The Teichm¨ uller character on Gal(
k/k) is deﬁned as the
composition
(2.14) ωp : Gal(
k/k) → Gal(Q/Q) → Gal(Q(µq)/Q)
∼
→ (Z/qZ)∗ ∼
→Wp,
where the last map sends an element of ( Z/qZ)∗ to the unique element of Wp
to which it is congruent modulo q. For an Artin character χ : Gal(k/k) → Qp
and an integer l, χωl
p is also an Artin character. If m ≤ 0 satisﬁes l +m ≡ 1
moduloϕ(q) and either χ is 1-dimensional or kχ is totally real then Lp(m,χωl
p,k ) =
Eul∗
p(m,χ,k )L∗(m,χ,k ).
The p-adic Beilinson conjecture is going to predict the special values of p-adic
L-functions in terms of a p-adic regulator. The required regulator is the syntomic
regulator [3, Theorem 7.5]. Let F be a complete discretely valued ﬁeld of charac-
teristic 0 with perfect residue ﬁeld of characteristic p and let X be a scheme that is
smooth and of ﬁnite type over the valuation ring OF . Then the above mentioned
paper associates to X its rigid syntomic cohomologies Hi
syn(X,n ), as well as syn-
tomic regulators (i.e., Chern characters) reg p : K2n−i(X) → Hi
syn(X,n ). In this
work, unlike in [3], we shall need to change the base ﬁeld F . We therefore prefer
to denote the syntomic cohomology by Hi
syn(X/OF,n ). For the formulation of the
conjecture the following basic fact is required.
Lemma 2.15. We have H 1
syn(Spec(OF )/OF,n ) ∼
= F , for all n > 0 and conse-
quently we have a syntomic regulator regp : K2n−1(OF ) → F . Furthermore, the
8 AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRAN C ¸ OIS ROBLOT
map regp commutes in the obvious way with ﬁnite extensions of ﬁelds an d with
automorphisms of such ﬁelds, provided that their residue ﬁe lds are algebraic over
the prime ﬁeld.
Proof. The ﬁrst claim follows from part 3 of [3, Proposition 8.6]. For the secon d
claim we note that by part 4 of the same proposition we have in this cas e an
isomorphism between syntomic and modiﬁed syntomic cohomology (th e latter only
exists under the additional assumption on the residue ﬁeld). The co mpatibility
with ﬁnite base changes now follows from the same result for modiﬁed syntomic
cohomology in [3, Proposition 8.8]. The same holds for automorphisms, although
not explicitly stated in the above reference, since the relevant bas e change results,
e.g., Proposition 8.6.4, hold for this type of base change as well. □
As a consequence of the lemma we can also, by abuse of notation, de ﬁne for any
complete discretely valued subﬁeld F ⊂
Qp the regulator reg p :K2n−1(OF ) →F .
In [5], two of the authors of the present work showed how one can s ometimes
compute the map reg p by using p-adic polylogarithms.
We now restrict our attention to a totally real number ﬁeld k with [k : Q] = d.
Our goal will be to formulate a conjecture that is the p-adic analogue of Theorem 2.2
for K2n−1(k) with n ≥ 2. Since this K-group is torsion when n is even but has
rank d when n is odd, we only consider odd n ≥ 2.
In preparation for the more general construction that will follow in Section 3 let
us ﬁrst reformulate Theorem 2.2 in this special case. Let a1,...,a d form a Z-basis
of Ok and let σ∞
1 ,...,σ ∞
d be the embeddings of k into C. Then we deﬁne D1/2,∞
k =
det(σ∞
i (aj)), a real root of the discriminant of k. Similarly, if α1,...,α d form a
Z-basis of K2n−1(k)/torsion then we let Rn,∞(k) = det(reg ∞ ◦σ∞
i∗ (αj)). Then
D1/2,∞
k and Rn,∞(k) are well-deﬁned up to sign, and the relation in Theorem 2.2
in this case is equivalent with
(2.16) ζk(n)D1/2,∞
k =q(n,k )Rn,∞(k)
with q(n,k ) in Q∗.
Now let F ⊂
Qp be the topological closure of the Galois closure of k embedded
in Qp in any way. If σp
1,...,σ p
d are the embeddings of k into F then D1/2,p
k =
det(σp
i (aj)) is a root in F of the discriminant of k. For σ : k → F an embedding
we denote the induced map K2n−1(k) → K2n−1(F ) by σ∗. Then we deﬁne a p-
adic regulator in F byRn,p(k) = det(regp ◦σp
i∗(αj)). Both D1/2,p
k and Rn,p(k) are
well-deﬁned up to sign.
Remark 2.13 suggests that the role of ζk(n) in a p-adic analogue of Theorem 2.2
should be played by Lp(n,ω 1−n
p ,k )/Eulp(n,k ) where ζk(s) = ∏
l Eull(s,k )−1 for
Re(s)> 1, so we can hope that
Lp(n,ω 1−n
p ,k )D1/2,p
k =qp(n,k ) Eulp(n,k )Rn,p(k)
for some qp(n,k ) in Q∗.
More precisely, because Rn,∞(k)/D1/2,∞
k andRn,p(k)/D1/2,p
k are invariant under
reordering the σ∞
i or σp
i , and transform in the same way if we change the bases of
Ok and K2n−1(k)/torsion, we can make the following conjecture.
Conjecture 2.17. Fork a totally real number ﬁeld, p prime, and n ≥ 2 odd, we
have, with notation as above:
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 9
(1) in F the equality
Lp(n,ω 1−n
p ,k )D1/2,p
k =qp(n,k ) Eulp(n,k )Rn,p(k)
holds for some qp(n,k ) in Q∗;
(2) in fact, qp(n,k ) = q(n,k );
(3) Lp(n,ω 1−n
p ,k ) and Rn,p(k) are non-zero.
As mentioned in the introduction, this, and the corresponding part s of Con-
jecture 3.18 below, can be deduced (with some eﬀort) from a much m ore general
conjecture of Perrin-Riou [42, 4.2.2].
Remark 2.18. The conjecture is similar to the result that the residue of ζp(s,k ) at
s = 1 is related to the Leopoldt regulator of O∗
k through exactly the same formula as
for the residue of ζ(s,k ) and the Dirichlet regulator [18], with part(4) corresponding
to the Leopoldt conjecture. However, we have not tried to deter mine if Colmez’s
normalization of the sign for the regulator is the same as here, espe cially given the
sign error in the proof of Lemma 4.3 in loc. cit. (see Section 6).
Remark 2.19. We can use a basis of a subgroup of ﬁnite index of K2n−1(k)/torsion
in the deﬁnition of Rn,∞(k) and Rn,p(k), or even a Q-basis of K2n−1(k)Q, without
aﬀecting the rationality of q(n,k ),qp(n,k ) or their equality. Similarly we can replace
the Z-basis of Ok with a Q-basis of k in the deﬁnitions of D1/2,∞
k and D1/2,p
k .
Remark 2.20. As is well-known, for k and n as in Conjecture 2.17, by (2.6)
ζk(s) at s = 1 −n has a zero of order d and the ﬁrst non-zero coeﬃcient in its
Taylor expansion,ζ♯
k(1 −n), equals (2πi)d(1−n)((n − 1)!/2)dDn−1/2
k ζk(n). If we take
D1/2,∞
k =D1/2
k in (2.16) then we obtain
ζ♯
k(1 −n) = ((n − 1)!/2)dq(n,k )Dn−1
k ~Rn,∞(k)
for Beilinson’s renormalized regulator ~Rn,∞(k) = (2πi)d(1−n)Rn,∞(k). In computer
calculations ((n − 1)!/2)dq(n,k )Dn−1
k often has only relatively small prime factors,
so the larger prime factors in q(n,k ) correspond to D1−n
k . This phenomenon also
occurs in the calculations for Conjecture 3.18 below (see Remark 7.8 ).
Remark 2.21. (1) The thought that Lp(n,ω 1−n
p ,k ) is non-zero for n ≥ 2 and odd
when k is a totally real Abelian extension of Q is mentioned by C. Soul´ e in [50,
3.4].
(2) F. Calegari [13] (see also [8]) proved that, for p = 2 and 3, ζp(3), which in
those cases equals Lp(3,ω −2
p , Q), is irrational. (More results along these lines are
described in Remark 3.20(3).)
(3) Parts (1) and (2) of Conjecture 2.17 hold when k is a totally real Abelian
number ﬁeld, and in fact the corresponding parts of a much strong er conjecture
that we shall describe in Section 3 hold for cyclotomic ﬁelds (see Prop osition 4.17).
(4) We numerically veriﬁed part (3) of Conjecture 2.17, and its more reﬁned
version Conjecture 3.18(4) below, in certain cases; see Remark 4.1 9 and Section 7.
