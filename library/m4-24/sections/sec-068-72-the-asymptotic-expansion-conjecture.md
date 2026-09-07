---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-068-72-the-asymptotic-expansion-conjecture
section_title: "The asymptotic expansion conjecture"
section_number: 7.2
pages: 102-109
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
The perturbative expansion of the Chern-Simons path integral (36) is given by
the semi-classical approximation and its higher loop perturbations. Roughly
speaking, the semi-classical approximation is obtained from the path integral
by ignoring the contribution from the third order term of the Chern-Simons
functional, and the higher loop perturbation contributions are the corrections
to this semi-classical contribution.
To the best of our knowledge, there is today, no complete perturbative treatment
of the Chern-Simons quantum 
eld theory available, even from a mathematical
physics point of view. In the following few paragraphs we shall try to outline
the main activities seen so far in this direction.
The the 
rst formula for the semi-classical approximation of the Chern-Simons
path integral was given by Witten in [403], describing it as a sum of contribu-
tions, one for each gauge equivalence classes of ﬂat connection, involving the
Chern-Simons value, the Reidemeister torsion and a certain spectral ﬂow for
each such gauge equivalence class. To test this prediction, Freed and Gompf
[127] made for certain Seifert 
bered manifolds some computer studies of the
large k behavior of ZSU (2)
k (M) and based on these calculations and further dis-
cussion of the semi-classical approximation of the path integral, they proposed
the following formula for the semi-classical approximation ( r =k +2 )
ZSU (2)
k (M) 
r!1
e−3p−1(1+b1(M))=4

X
[A]
e2p−1rCS(A)r(h1
A−h0
A)=2e−2p−1(IA=4+h0
A=8)
M (A)1=2;
The 
rst version of Section 7.2 was written by T. Ohtsuki, following seminar talks given
by J.E. Andersen. Based on it, J.E. Andersen wrote this section.
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 475
where the sum is over the gauge equivalence classes of ﬂat connections A.L e t
us explain the quantities involved in this expression and in which cases one can
make sense of this expression as it stands.
For any ﬂat connection A, we have the cohomology groups Hi(M;dA)o ft h e
covariant derivative complex dA :Ω ?(M;g)! Ω?+1(M;g)g i v e nb ydAf =
df +[A;f ], and hi
A is the dimension of Hi(M;dA). Further associated to this
complex we have the Reidemeister torsion 
M (A)2⊗i
(
detHi(M;dA)
(−1)i
=
detH0(M;dA)⊗
(
detH1(M;dA)
2
(by Poincare duality). If one now as-
sumes that all the gauge equivalence classes of ﬂat connections A are isolated,
in fact Freed and Gompf assumed H1(M;dA) = 0, so that the above sum is

nite and such that the square root of the Reidemeister torsion 
M (A)1=2 is
a well-de
ned number (once a volume on H0(M;dA) has been 
xed, but for
irreducible connections H0(M;dA)=0 ) .
The quantity IA2Z=8Z denotes the spectral ﬂow of the operator

?dAt −dAt?
dAt? 0

on Ω 1(M;g)⊗Ω 3(M;g), where At is a path of connections running from the
trivial connection toA. T h e ya l s ol o o k e da ts o m ee x a m p l e sw h e r eH1(M;dA)6=
0 and checked the overall growth predicted by the above formula.
Following this Je
rey [184] proposed the following more general interpretation
of the square root of Reidemeister torsion in the cases where the connections
are not isolated: Assume that the moduli space of ﬂat connections M on M is
smooth and that the tangent space at each equivalence class of ﬂat connection
A equalsH1(M;dA). Since H0(M;dA) g the invariant inner product we have
chosen on g induces a volume element on H0(M;dA). In total this means that
the square root of the Reidemeister torsion induces a measure on the moduli
space when we pair it with the induced volume element on H0(M;dA) divided
by the order of the center of G and one arrives at (r =k +h
_
)
ZG
k (M) 
r!1
e−p−1(dim G)(1+b1(M))=4

Z
[A]2M
e2p−1rCS(A)r(h1
A−h0
A)=2e−2p−1(IA=4+(h0
A+h1
A)=8)
M (A)1=2:
For some mapping tori of genus 1 surfaces and lens spaces, Je
rey veri
ed
this form of the semi-classical approximation. Garoufalidis [134] independently
proved the semi-classical approximation for lens spaces and studied in various
examples the growth rate predicted by these approximations. Rozansky [352]
Geometry &TopologyMonographs, Volume 4 (2002)
476 T. Ohtsuki (Editor)
proposed a further re
ned version of the above semi-classical approximation,
and o
ered calculations for a very large class of Seifert 
bered manifolds as
evidence. He proposed to divide the volume element on H0(M;dA)b yt h e
volume of the stabilizer of A, and to use the resulting quantity paired with the
square root of the Reidemeister torsion as the measure on M (generalizing the
division by the order of the center above). This gave a natural explanation of
factors not accounted for in both the work of Freed and Gompf and the work of
Je
rey. He also proposed corrections to the formula for the growth rate of the
invariant (i.e. the power of r in the above), in cases where not all directions in
H1(M;dA) are tangent to paths of ﬂat connections (see [352] and [353]).
Axelrod and Singer [21, 22] (see also [226]) considered the higher loop contri-
butions in the perturbation expansion and proposed the following:
ZG
k (M) 
k!1
Z
[A]2M
 semi-classical
approximation

exp
0
@
1X
l=1
clk−l
(2l)!(3l)!
X
e(Γ)=−l
ZΓ(M;A )
jAut(Γ)j
1
A
(39)
for some scalar c, where the right sum runs over connected trivalent graphs Γ
whose Euler number is equal to−l,a n djAut(Γ)j denotes the order of the group
of automorphisms of Γ. Further, in the case where A is acyclic or whenA2M
is contained in a smooth component, Axelrod and Singer was able to construct
ZΓ(M;A ) as a topological invariant of ( M;A ); roughly speaking, it is given as
follows in the acyclic case. We identify the set of connection around A with
Ω 1(M; g). The second order part of the Chern-Simons functional gives a bilinear
form on Ω 1(M; g)⊗2 , and it determines a 2-form L2 Ω 2(MM; g⊗g)a n di t s
\inverse". Further, the third order part of the Chern-Simons functional gives a
trilinear form T on Ω 1(M; g)⊗3 .W e o b t a i nZΓ (M;A ) by contracting L⊗(3l) by
T⊗(2l) \along the trivalent graph Γ" (roughly regarding L as in Ω 1(M; g)⊗2 );
we determine the action of T⊗(2l) on L⊗(3l)2 Ω 1(M; g)⊗(6l) by putting copies
of L on 3l edges of Γ and putting copies of T on 2l vertices of Γ. For a precise
(mathematical) construction (and its topological invariance) of ZΓ (M;A ), see
[21, 22].
From the mathematical viewpoint we regard ZG
k (M)a s
ZG
k (M)=

G
k+h_ (M)

G
k+h_ (S1S2)
for the quantum G invariant 
G
r (M). Then, the asymptotic expansion of
ZG
k (M) is predicted by the semi-classical approximation and its higher loop
corrections stemming from a perturbative expansion of the Chern-Simons path
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 477
integral, explained above in some cases. This leads us to the following somewhat
vague conjecture.
Conjecture 7.6 (The perturbative expansion conjecture) The asymptotic
expansion of ZG
k (M) of a closed oriented 3-manifold M is given by
ZG
k (M) 
k!1
e−p−1(dim G)(1+b1(M))=4

Z
[A]2M
e2p−1rCS(A)r(h1
A−h0
A)=2e−2p−1(IA=4+(h0
A+h1
A)=8)
M (A)1=2
 exp
0
@
1X
l=1
clk−l
(2l)!(3l)!
X
e(Γ)=−l
ZΓ (M;A )
jAut(Γ)j
1
A;
putting r =k +h
_
, where the right hand side can be given in the mathemat-
ical viewpoint in certain cases, as mentioned above, but which needs further
interpretation in general.
Remark The semi-classical approximation stated above (the upper two lines
in the above formula), has been con
rmed for lens spaces (
rst partially [127])
and then by [184, 134], for certain mapping tori of di
eomorphisms of a torus
[184], and for all 
nite order mapping tori of automorphisms of any closed
orientable surface of genus at least 2 [6]. For a large class of Seifert 
bered
manifolds [353] and [354] o
ered calculations which provided evidence that the
phases in the semi-classical approximation is given by the Chern-Simons invari-
ants and the measure is given by the square root of the Reidemeister torsion
as explained above. Also, expressions for the higher loop corrections was of-
fered. Later the necessary analytic estimates was provided in [168] so as to
con
rm this. See also the discussion below. For now, there are no examples of
hyperbolic manifolds, where parts of the above conjecture has been con
rmed.
For other versions of Conjecture 7.6, see [220, Problem 3.108], [136].
The formula in Conjecture 7.6 might not give an exact description of the asymp-
totic behavior of ZG
k (M) even in the semi-classical part, neither is it in all cases
well-de
ned. Moreover, it might be dicult at present to calculate the concrete
value of the higher loop corrections in the asymptotic expansion of Conjecture
7.6 for given M , A, and Γ. Nor do we have de
nitions for these terms, which
has been proven to be well de
ned topological invariants in all cases.
The following conjecture o
ers a kind of reverse viewpoint on Conjecture 7.6,
avoiding such ambiguities and diculties.
Geometry &TopologyMonographs, Volume 4 (2002)
478 T. Ohtsuki (Editor)
Conjecture 7.7 (The asymptotic expansion conjecture, J.E. Andersen [6])
Letfc0 =0 ;c 1; ;cmg be the set of values of the Chern-Simons functional
of ﬂat G connections on a closed oriented 3-manifold M .T h e r e e x i s tdj 2Q,
~Ij 2Q=Z, vj 2R+ ,a n dae
j 2C for j =0 ; 1; ;m and e =1 ; 2; 3; such
that (r =k +h
_
)
ZG
k (M) 
r!1
mX
j=0
e2p−1rcjrdjep−1~Ij=4vj
(
1+
1X
e=1
ae
jr−e
;
that is, for all E =0; 1; 2;::: , there exists a constant cE such that

ZG
k (M)−
mX
j=0
e2p−1rcjrdjep−1~Ij=4vj
(
1+
EX
e=1
ae
jr−e

cErd−E−1
for all r =2; 3; 4; . Here, d = maxfd0; ;dmg.
Remark (J.E. Andersen) If such an expansion in the above conjecture exists,
then cj , dj , ~Ij , vj ,a n d ae
j are uniquely determined by ZG
k+2(M)f o r k =
0; 1; 2; 3; 4; .
Problem 7.8 (J.E. Andersen) If such an expansion exists, understand how
it is related to the expansion of Ohtsuki and the expansion of Habiro.
It will of course be important to establish, that an expansion of this type ex-
ists, however, of far greater importance will be to give independent topological
meaning to the many resulting new invariants, e.g. to prove that the phases are
the Chern-Simons values cj . From the discussion above on the semi-classical
approximation we derive the following conjecture:
Conjecture 7.9 (Topological interpretations of the dj ’s) Let Mj be the
union of components of the moduli space of ﬂat connections M which has
Chern-Simons value cj .T h e n
dj = 1
2 max
A2Mj
(h1
A−h0
A);
where max here means the maximum value that (h1
A−h0
A) assumes on a Zariski
open subset of Mj .
Note that this conjecture might be rather optimistic, and may only hold in the
non-degenerate cases. However, we do not know of any cases where it fails (see
[136]).
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 479
Remark (J.E. Andersen) The special max proposed in Conjecture 7.9 is
certainly needed, as shown by the example of the mapping torus of the di
eo-
morphism−Id of a torus. The quantum SU (2) invariant of this manifold is
easily seen to be r−1, since−Id is represented trivially for all levels, however,
there are ﬂat SU (2) connections for which ( h1
A−h0
A)> 2.
The Conjecture 7.9 implies the following growth rate.
Conjecture 7.10 (The growth rate conjecture) Let d =m a xfd0;:::;d ng:
ThenjZG
r (M)j =O(rd):
It is well known that the quantum invariants only grows like r to some power.
The power is bounded from above by some simple function (depending on G)
of the Heegaard genus of the manifold.
Remark (J.E. Andersen)
(1) Suppose that M is a closed 3-manifold satisfying that 
G
r (M)= 
G
r (S3)
for all r. If the growth rate conjecture 7.10 is true for the group G, then there
is no non-central representation of 1(M)t o G.
(2) Kronheimer and Mrowka have proposed a program using Seiberg-Witten
theory and Floer homology to establish that any 3-manifold M obtained from
S3 by +1 surgery along a non-trivial knot K has a non-trivial (and therefore
non-abelian) representation of 1(M)t o SU (2). Suppose that this is the case
and the growth rate conjecture 7.10 is true. Then, JK;c = JU;c for all c =
1; 2; if and only if K is the trivial knot U ,w h e r eJK;c denotes the colored
Jones polynomial of a knot K with a color c.
At this time we do not know of a topological interpretation of the values of ~Ij
and vj which makes sense in all cases. Let us simply just propose the following
Conjecture 7.11 There is a construct of the right measure, say 
M (A)1=2
for A2Mi , from the square root of the Reidemeister torsion generalizing the
non-degenerate case explained above and such that
ep−1~Ij=4vj =
Z
A2Mi
ep−1(−2IA+h0
A+h1
A)=4
M (A)1=2:
Conjectures 7.7 and 7.9 together with Conjecture 7.11 were 
rst proved for
mapping tori of all 
nite order di
eomorphisms of all surfaces of genus at least
two in [6]. Recently, Conjecture 7.7 was proved for all Seifert 
bered spaces in
[168] by supplementing the calculations in [353] and [354] with the need analytic
estimates.
Geometry &TopologyMonographs, Volume 4 (2002)
480 T. Ohtsuki (Editor)
Example Let us illustrate the asymptotic behavior of the quantum SU (2)
invariant of the lens space L(5; 1) of type (5 ; 1). For simplicity, we let r be
an odd prime. Since 
SU (2)
3
(
L(5; 1)

= 1, putting  =e x p ( 2p−1=r), we have
that

SU (2)
r
(
L(5; 1)

=
SO(3)
r
(
L(5; 1)

=
5
r

−35? 10?
−−10?
2?
−−2? ;
wherek? denotes the inverse ofk inZ=rZ.S i n c e
SU (2)
r (S1S2)= pr
2= sin(
r ),
we have that
ZSU (2)
r−2
(
L(5; 1)

= 
SU (2)
r
(
L(5; 1)


SU (2)
r
(
S1S2 =
r
2
r sin
r
5
r

−35? 10?
−−10?
2?
−−2? :
(40)
On the other hand, as in [184], the semi-classical approximation is given as
follows. The lens space L(5; 1) has three ﬂat connections An (n=0,1,2); each
An is determined by the representation of 1
(
L(5; 1)
=Z=5Z to SU (2) which
takes a generator of Z=5Z to
 
e2p−1n=5 0
0 e−2p−1n=5
!
. As in [184], we have
that CS(An)= n2=5, h0
An =1 , h1
An =0 , 
M (An)1=2 = 4
p
2p
5 sin2 2n
5 ,a n d
In(mod 4) = 1 if n< 5=2, and −1i f n> 5=2. Hence,
ZSU (2)
r−2
(
L(5; 1)


r!1
2
r
−2
5r
X
n=0;1;2
e2p−1rn2=5 sin2 2n
5 ; (41)
noting that the notatin of lens spaces in [184] is equal to the notation of their
mirror images in [221, 134].
The sequence of 
SU (2)
r
(
L(5; 1)

for odd primes r splits into four subsequences
according to r 1;3 mod 10, and each subsequence can be approximated
by a function of a polynomial order. Let us describe the subsequence, say, with
r−1 mod 10, as follows. Since 10 ? =(r +1 )=10, we calculate (40) as
ZSU (2)
r−2
(
L(5; 1)

=
r
2
r sin
re−6p−1=5rep−1=5r−!−1e−p−1=5r
ep−1=r−e−p−1=r

r!1
1−!−1
p−2 r−1=2;
putting ! =e x p ( 2p−1=5). On the other hand, the right hand side of (41) is
calculated as
2
r
−2
5r

e−2p−1=5 sin2 2
5 +e2p−1=5 sin2 4
5

= !−1p−2r−1=2;
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 481
noting that
p
5=1+2 ! +2!−1 (Gaussian sum). Therefore, it was veri
ed
that the semi-classical approximation is correct for this subsequence.
This is related to the perturbative invariant

SO(3)(
L(5; 1)

=q−3=5q1=10−q−1=10
q1=2−q−1=2 2Q[[q−1]]
as follows. We regard it as a holomorphic function of q in a suitable domain.
The asymptotic behavior of 
SO(3)
r
(
L(5; 1)

, say, for the above mentioned sub-
sequence, can be presented by using this holomorphic function aroundq1=5 =!.
Example It is known, see [243, 247], that

SO(3)
r
(
(2; 3; 5)

= 1
1−
r−1X
n=0
n(1−n+1)(1−n+2) (1−2n+1)
for Poincare homology 3-sphere (2 ; 3; 5), where we put  =e x p ( 2p−1=r).
It is an exercise to compute the asymptotic behaviour of ZSU (2)
r−2
(
(2; 3; 5)

as r !1 related to Conjecture 7.7, and to formulate a relation with the
perturbative invariant given by

SO(3)(
(2; 3; 5)

= 1
1−q
1X
n=0
qn(1−qn+1)(1−qn+2) (1−q2n+1):
