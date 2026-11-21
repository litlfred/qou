---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-001-generators
section_title: "Generators"
section_number: null
pages: 13-22
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
There are two approaches to presenting the content.
One could either employ the
full power of abstraction, in terms of presentations of categories outlined in Appendix
A.1, or appeal to intuition carried over from presentations of groups. We will try to
accomplish both. The readers are encouraged to refresh their memories on the rigorous
setup of quotient categories, generators and relations, and presentations of categories,
found in the form of an expository note in the appendix.
The category we wish to find a presentation for is the subcategory of Cob(3) spanned
by spherical objects.
Definition 2.0.1. (Cob(3)S2) Consider the symmetric monoidal category Cob(3). It
has a subcategory whose objects are disjoint unions of S2. Call this category Cob(3)S2
and note that it inherits the symmetric monoidal structure.
Note that some authors include all possible codimension 1 closed oriented manifolds
when defining Cob(n). Even though we have demanded that our categories Cob(3)S2
to have objects strictly the unit sphere, we did not lose any generality, because in the
other convention, we have
Proposition 2.0.2. Let X, Y be diffeomorphic objects of Cob(n) and f : X →Y a
diffeomorphism. Then Z(X) ∼= Z(Y ).
Proof. Consider the mapping cylinder Mf : X →Y and the reverse M′
f : Y →X.
Unwrap the definition and it’s easy to see that M′
f ◦Mf = X × I, and so is the other
direction. Hence Mf is an isomorphism.
We say a set G generates morphisms of (C, ⊗) if every morphism in C is a composi-
tion of elements of G and all monoidal products of G. Note that we will also include,
implicitly, the associated identities, left and right unitors, associators, and braiding.
We say a set of equalities R among (compositions of monoidal products of) elements
of G is sufficient if every equality of morphisms in C is induced by equalities in R. If
G generates morphisms and R is sufficient, then we say (G | R) is a presentation of C.
We want a presentation of Cob(3)S2, both generators and relations. As we will
see, there are two sets of generators, named G1 and G2, giving rise to two different
presentations. The G1 presentation is associated with the letter “L” due to the distinct
upside-down “L”-shaped branches in figure 2.2. After passing through TFTs it would
give rise to L-monoids and L-algebras. The G2 presentation is associated with the
letter “P” for “Prime” due to a lack of imagination.
Passing through TFTs gives
rise to P-monoids and P-algebras. As G1 and G2 both generate Cob(3)S2, we shall
foreshadow that there is an equivalence between P-monoids and L-monoids, as well as
between P-algebras and L-algebras.
The following notations will be used throughout the paper:
Notations 2.0.3. Let M be a manifold. Denote by M◦and int(M) the interior of M.
Let n ≥1 be a positive integer, then we frequently write ⊔nM for short to denote the
disjoint union of n-many copies of M, instead of ⊔n
i=1M.
Consider the following diffeomorphism classes of oriented bordisms of two-spheres:
Notations 2.0.4. Define the following morphisms of Cob(3)S2 :
idS2 =

S2 × I

m =

S3 \ int(⊔3D3)

: S2 ⊔S2 →S2
1 =

D3
: ∅→S2
m∨=

S3 \ int(⊔3D3)

: S2 →S2 ⊔S2
tr =

D3
: S2 →∅
Comment 2.0.5. This set of bordisms can be neatly organized as follows: recall that
the three-sphere is homeomorphic to the gluing of two three-balls along their common
boundary (the north and south hemisphere glued along the equator). If we elect in-
coming/outgoing time direction to run from south to north, then the 1 (namely unit)
map can be viewed as the southern hemisphere, and tr (namely trace) as the northern.
Either one could be viewed as S3 \ int(D3) and distinguished by incoming/outgoing
time reversal. The identity map could be viewed as S3 \ int(D3 ⊔D3). So we have
identified S3 minus one, two, and three D3. In addition, S3 itself can be obtained by
the hemisphere decomposition tr ◦1, and since composing two multiplications together
increases the incoming boundary components by 1, S3 minus n ≥3-many D3 interiors
can be obtained by composing n −2 multiplication maps. 1
Notations 2.0.6. For suggestive reasons, we let
C = {m, 1} ,
F =

m∨, tr
	
.
Furthermore, consider the following three sets indexed by oriented prime 3-manifolds:
P ′ =

p \ int(D3 ⊔D3)

: S2 →S2 | p prime
	
L′ =

p \ int(D3)

: ∅→S2 | p prime
	
L∨′ =

p \ int(D3)

: S2 →∅| p prime
	
whose elements we simply refer to as p×× and p×, p×∨. Note that L∨′ is the incom-
ing/outgoing reversal of L′, but there is no P ∨′ as the time reversal of any such bordism
is itself.
1One can also think of this as the operadic composition law of the (framed) little 3-disk operad.
Proposition 2.0.7. The homs of Cob(3)S2 have two generating sets:
G′
1 = C ∪F ∪L′ ∪L∨′ ∪orientation reversal
G′
2 = C ∪F ∪P ′ ∪orientation reversal
More precisely, let F(Gra1) and F(Gra2) be the free categories of the graphs Gra1 and
Gra2, which have

⊔iS2 | i ∈Z≥0
	 ∼= Z≥0 as vertices and directed edges generated by
G′
1 and G′
2 and all tensor products. Then the tautological functors F(Gra1) →Cob(3)S2
and F(Gra2) →Cob(3)S2 are full and bijective on objects.
Proof. Let [M] : ⊔nincS2 →⊔noutS2 be a morphism from ninc-many two-spheres to
nout-many two-spheres. Since the braiding βS2,S2 permutes the boundary spheres, we
can, without loss of generality, assume that within incoming or outgoing boundary
components the spheres are not labelled. [Koc03]
Therefore we need to show that given an oriented bordism of unlabelled spheres
[M], we can find a composition in terms of G′
1 and G′
2 generators and their tensor
products. Let M be a representative of [M], we will show that M is diffeomorphic to
gluings of manifolds which are representatives of G′
1 and G′
2 generators.
Consider the closed oriented manifold
c
M ∼=
 ninc+nout
G
i=1
D3 [
∂M
M
obtained from filling in the bounding spheres. One can show that the gluing is well de-
fined up to diffeomorphism [Hir76]. By the Kneser-Milnor theorem, c
M is diffeomorphic
to a finite connected sum of oriented prime 3-manifolds P1, . . . , Pm,
c
M ∼= P1#P2# . . . #Pm.
Therefore M itself is diffeomorphic to the same finite connected sum minus the interior
of the boundary balls
M ∼= (P1#P2# . . . #Pm) \ int
 ninc+nout
G
i=1
D3
.
Unlike a generic Morse decomposition whose gluing surfaces are constrained by their
values, the attaching balls for each connect sum operation can be freely chosen. De-
pending on the choices of the attaching balls, we will have two different decompositions
of M as gluings. To make the expression more symmetric, consider adding two trivial
connect sum factors
M ∼= S3# (P1#P2# . . . #Pm) #S3 \ int
 ninc+nout
G
i=1
D3
and choose2 that the incoming and outgoing balls be cut from these two factors
M ∼=

S3 \ int
 nout
G
i=1
D3
#(P1#P2# . . . #Pm)#

S3 \ int
 nout
G
j=1
D3
.
2This is not a constraint but a choice made to make apparent how subsequent choices end up being
generated by G′
1 and G′
2, much like the use of the “standard form” of surfaces commonly used in the
classification of 2d TFT, see for eg [Kock].
1. (The choice leading to G′
2)
For each prime factor Pj there are two chosen embedding of three-balls
ej
1,2 : D3 →Pj,
j = 1, . . . , m,
where ej
2 forms the connect sum with ej+1
1
of Pj+1 unless j = m, when em
2 forms
the connect sum with an embedded three ball in S3 \ int(⊔nincD3). We choose
e1
1 to form the connect sum with an embedded three-ball in S3 \ int(⊔noutD3).
Noting that
M#N ∼= (M \ int(D3)) ∪∂D3 (N \ int(D3)),
where the boundary of the embedded three balls being identified can be thought
of as the boundary being glued over, we may rewrite the connect sum as
M ∼=

S3 \ int
 nout
G
i=1
D3
# (P1#P2# . . . #Pm) #

S3 \ int
 ninc
G
j=1
D3
∼=

S3 \ int
 nout+1
G
i=1
D3
∪S2

P1 \ int(D3 ⊔D3)

∪S2 . . .
· · · ∪S2

Pm \ int(D3 ⊔D3)

∪S2

S3 \ int
 nint+1
G
D3
.
Under the natural choice of ej
1 bounding the outgoing sphere and ej
2 bounding
the incoming sphere, this composition induces
h
M
i
=
h
S3 \ int(⊔noutD3)
i
◦
h
P1 \ int(D3 ⊔D3)
i
◦. . .
· · · ◦
h
Pm \ int(D3 ⊔D3)
i
◦
h
S3 \ int(⊔nincD3)
i
=
h
S3 \ int(⊔noutD3)
i
◦P ××
1
◦· · · ◦P ××
m
◦
h
S3 \ int(⊔nincD3)
i
and by comment 2.0.5 the morphisms [S3 \ int(⊔nD3)] can be obtained as a
composition of commutative Frobenius generators. See figure 2.1 for a sketch of
this composition.
2. (The choice leading to G′
1)
For each Pj there is one chosen embedding of three balls
ej : D3 →Pj
for j = 1, . . . , m. Take an additional S3 factor and choose m + 2 embeddings
ej, e0, em+1, j = 1, . . . , m. Let ej form the connect sum with ej, let e0 form the
connect sum with an embedded three ball in S3 \ ⊔noutD3 and let em+1 form the
connect sum with an embedded three ball in S3 \ ⊔nincD3. Noting that
M#N ∼= (M \ int(D3)) ∪∂D3 (N \ int(D3))
Pm
· · ·
P1
Figure 2.1: A sketch of how G2 generates a generic bordism [M] where M ’s prime factors are
P1, . . . , Pm. Note that this picture is “sideways” as we usually associate the “time” direction
as going up. In this case, time goes from left to right.
where the boundary of the embedded three balls being identified can be thought
of as the boundary being glued over, we may rewrite the connect sum as
M ∼=

S3 \ int
 nout
G
i=1
D3
# (P1#P2# . . . #Pm) #

S3 \ int
 ninc
G
j=1
D3
∼=
 
S3 \ int
 nout+1
G
i=1
D3
⊔

S3 \ int
 ninc+1
G
i′=1
D3! [
S2⊔S2
 
S3 \ int
 m+2
G
i′′=1
D3!
[
⊔mS2


m
G
j=1
 Pj \ int(D3)



Besides the obvious choice for e0 to bound an outgoing sphere and em+1 to bound
an incoming sphere, there is no canonical choice of incoming vs outgoing for the
boundaries of ej and ej for j = 1, . . . , m.
One choice is for all ej to bound
outgoing boundaries and ej incoming. Then the S3 which all the prime factors are
connected with becomes S3 \int(⊔m+2D3) with m+1 many incoming boundaries
and 1 outgoing. This choice induces the following composition of [M]:
h
M
i
=
h
S3 \ int(⊔nout+1D3)
i
◦
h
S3 \ int(⊔m+2D3)
i
◦
 m
O
j=1
h
Pj \ int(D3)
i
⊗
h
S3 \ int(⊔ninc+1D3)
i
=
h
S3 \ int(⊔nout+1D3)
i
◦
h
S3 \ int(⊔m+2D3)
i
◦
 m
O
j=1
P ×
j ⊗
h
S3 \ int(⊔ninc+1D3)
i
where P ×
j
= [Pj \ int(D3)] : ∅→S2.
By comment 2.0.5, the corresponding
morphism [S3 \ int(⊔nD3)] can be obtained as a composition of commutative
Frobenius generators.
If we had chosen ej to bound incoming and ej to bound outgoing, then we would
instead induce the following composition of [M]:
h
M
i
=
 m
O
j=1
h
Pj \ int(D3)
i
⊗
h
S3 \ int(⊔nout+1D3)
i
◦
h
S3 \ int(⊔m+2D3)
i
◦
h
S3 \ int(⊔ninc+1D3)
i
=
 m
O
j=1
P ×∨
j
⊗
h
S3 \ int(⊔nout+1D3)
i
◦
h
S3 \ int(⊔m+2D3)
i
◦
h
S3 \ int(⊔ninc+1D3)
i
where now P ×∨
j
= [Pj \ D3] : S2 →∅.
If we had chosen ej to bound a mixture of incoming and outgoing boundaries,
the induced composition of [M] would be a mixture
h
M
i
=

O
ej
incoming
P ×∨
j
⊗
h
S3 \ int(⊔nout+1D3)
i
◦
h
S3 \ int(⊔m+2D3)
i
◦

O
ej
outgoing
P ×
j ⊗
h
S3 \ int(⊔ninc+1D3)
i
See figure 2.2 for an illustration of a composition in the case all ej are incoming.
Remark 2.0.8. Neither G′
1 nor G′
2 is minimal– S2 × S1 is prime, but it has a standard
Morse function which factors through the projection onto the S1 factor:
S2 × S1 proj
−→S1 height
−→R
whose critical points are of index 0, 2, 1, 3 in increasing critical values, and whose regular
surfaces are either empty or a disjoint union of S2. This is depicted (in a slightly wonky
manner) in figure 3.5-(a). Therefore there is a Morse gluing resembling the toric pants
decomposition one dimension down, inducing the equality
h
S2 × S1i
∼= tr ◦m ◦m∨◦1.
In particular, the element [S2×S1\int(D3⊔D3)] ∈P ⊂G′
2 is equal to the composition
m◦m∨, and the elements
h
S2×S1\int(D3)
i
∈L, L∨⊂G′
1 is equal to the compositions
m ◦m∨◦1 and tr ◦m ◦m∨respectively.
Remark 2.0.9. The L∨′ generators are redundant – let P ×∨= [P \ int(D3)] ∈L∨′ be a
morphism S2 →∅. Consider P × = [P \ D3] ∈L′ a morphism ∅→S2. Since
P \ int(D3) ∼=
 P#S3
\ int(D3) ∼=

P \ int(D3)

∪S2

S3 \ int(
3G
i=1
D3)

∪S2 D3
. . .
P1
P2
Pm
Figure 2.2: A sketch of how G1 generates a generic bordism [M] where M ’s prime factors are
P1, . . . Pm. This particular [M] has 3 incoming S2 components and 4 outgoing components.
This figure depicts the case where all the bounding balls ej are incoming, namely all the
prime factors are in the form of P ×
i : ∅→S2.
we learn that
P ×∨= tr ◦m ◦(P × ⊗idS2) ◦λ−1
S2
where λS2 : ∅⊔S2 →S2 is the left unitor. This relation is reflected in the sketch if
figure 2.3.
Notations 2.0.10. Given the two remarks 2.0.8 and 2.0.9, we shall remove S2 × S1
from the prime generators and delete the redundant set L∨′. Recalling that S2 × S1 is
the only reducible oriented prime 3-manifold, we define
P =
n
p×× =
h
p \ int(D3 ⊔D3)
i
: S2 →S2 | p oriented irreducible
o
L =
n
p× =
h
p \ int(D3)
i
: ∅→S2 | p oriented irreducible
o
Proposition 2.0.11. The following sets generate morphisms of Cob(3)S2 and are both
minimal:
G1 = C ∪F ∪L ∪orientation reversal
G2 = C ∪F ∪P ∪orientation reversal
This proposition will be revisited as 3.3.7 and the proof will be presented there.
Remark 2.0.12. Another distinction between S2×S1 and other primes, in the setting of
our restricted bordism category Cob(3)S2, is the special role it plays when compositing
P ×
P ×∨
∼=
Figure 2.3: Redundancy of L∨′ generators.
bordisms together: let [M] : ⊔aS2 →⊔bS2 and [N] : ⊔bS2 →⊔cS2 be two bordisms,
and let
c
M ∼= (⊔aD3) ∪⊔aS2 M ∪⊔bS2 (⊔bD3)
be the closed manifold obtained by filling the incoming and outgoing boundaries of
M.
One can show that the choice of gluing result in a well defined manifold up
to diffeomorphism. Define b
N analogously. Then there are prime decompositions of
c
M ∼= M1#M2# . . . #Mm and b
N ∼= N1# . . . #Nn, where each factor Mi, Nj is prime.
Taking the composition along the common boundary ⊔bS2, and filling in the remaining
boundaries, the resulting manifold gains connected sum factors of S2 ×S1. To see this,
refer to the figure 2.1 where M has been put into a normal form. Consider doing the
same for N. The pairing of the outgoing component of M and the incoming components
of N gives rise to the new connect sum factors of S2 × S1, much like increasing genus
in one dimension down:
\
N ◦M ∼= (N1# . . . #Nn)#

#b−1(S2 × S1)

#(M1# . . . #Mm).
In fact, as we shall see by theorem 3.3.6, the morphisms in a subcategory of Cob(3)S2
are all #g(S2×S1) minus some (interiors of) disks, and g the number of S2×S1-factors
is equivalent to the genus of some surfaces as a morphism in Cob(2).
Comment 2.0.13. For now, the choice of using G1 or G2 is a matter of taste, as there
is a clear bijection between the generators and that one can switch between p×× =
[p \ int(D3 ⊔D3)] ∈P and p× = [p \ int(D3)] ∈L by relations
h
p \ int(D3)
i
=
h
p \ int(D3 ⊔D3)
i
◦1
h
p \ int(D3 ⊔D3)
i
= m ◦(
h
p \ int(D3)
i
⊗idS2) ◦λ−1
S2
where λS2 : ∅⊔S2 →S2 is the left unitor. The first relation geometrically fills in a
ball. The latter creates a new boundary component through m. In fact, there is an
alternative construction
h
p \ int(D3 ⊔D3)
i
= m ◦(idS2 ⊗
h
p \ int(D3)
i
) ◦ρ−1
S2
where ρS2 : S2 ⊔∅→S2 is the right unitor. The equivalence of the two constructions is
the first example of a prime relation. This particular one is explored in proposition 4.2.7
and shown to be implied by the more fundamental commutative Frobenius relations in
proposition 4.2.9.
The bijection between G1 and G2 generators is depicted in 2.4.
P ×
P ××
P ××
∼=
P ×
P ×
∼=
∼=
(a)
(b)
Figure 2.4: Bijection between G1 and G2 generators. Figure (a) shows that all prime units
P × can be recovered by filling in the incoming ball of the prime endomorphism P ××. Figure
(b) shows that all prime endomorphisms can be recovered from the prime units by post-
composing with the 3-dimensional pair of pants. Note that there are two possible orderings
of the legs. This is known as the “legs relations” for L ⊂G1 generators.
Chapter 3
