---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-001-generators
section_title: "Generators"
section_number: null
pages: 13-21
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
There are two approaches to presenting the content. One could either employ the
full power of abstraction, in terms of presentations of categories outlined in Appendix
A.1, or appeal to intuition carried over from presentations of groups. We will try to
accomplish both. The readers are encouraged to refresh their memories on the rigorous
setup of quotient categories, generators and relations, and presentations of categories,
found in the form of an expository note in the appendix.
The category we wish to find a presentation for is the subcategory of Cob(3) spanned
by spherical objects.
Definition 2.0.1.(Cob(3) S2) Consider the symmetric monoidal category Cob(3). It
has a subcategory whose objects are disjoint unions ofS 2. Call this category Cob(3)S2
and note that it inherits the symmetric monoidal structure.
Note that some authors include all possible codimension 1 closed oriented manifolds
when defining Cob(n). Even though we have demanded that our categories Cob(3) S2
to have objects strictly the unit sphere, we did not lose any generality, because in the
other convention, we have
Proposition 2.0.2.LetX,Ybe diffeomorphic objects ofCob(n)andf:X→Ya
diffeomorphism. ThenZ(X) ∼=Z(Y).
Proof.Consider the mapping cylinderM f :X→Yand the reverseM ′
f :Y→X.
Unwrap the definition and it’s easy to see thatM ′
f◦Mf =X×I, and so is the other
direction. HenceM f is an isomorphism.
We say a setGgenerates morphisms of (C,⊗) if every morphism inCis a composi-
tion of elements ofGand all monoidal products ofG. Note that we will also include,
implicitly, the associated identities, left and right unitors, associators, and braiding.
We say a set of equalitiesRamong (compositions of monoidal products of) elements
ofGis sufficient if every equality of morphisms inCis induced by equalities inR. If
Ggenerates morphisms andRis sufficient, then we say (G|R) is a presentation ofC.
We want a presentation of Cob(3) S2, both generators and relations. As we will
see, there are two sets of generators, namedG 1 andG 2, giving rise to two different
presentations. TheG 1 presentation is associated with the letter “L” due to the distinct
upside-down “L”-shaped branches in figure 2.2. After passing through TFTs it would
give rise toL-monoids andL-algebras. TheG 2 presentation is associated with the
13
letter “P” for “Prime” due to a lack of imagination. Passing through TFTs gives
rise toP-monoids andP-algebras. AsG 1 andG 2 both generate Cob(3) S2, we shall
foreshadow that there is an equivalence betweenP-monoids andL-monoids, as well as
betweenP-algebras andL-algebras.
The following notations will be used throughout the paper:
Notations 2.0.3.LetMbe a manifold. Denote byM ◦ and int(M) the interior ofM.
Letn≥1 be a positive integer, then we frequently write⊔ nMfor short to denote the
disjoint union ofn-many copies ofM, instead of⊔ n
i=1M.
Consider the following diffeomorphism classes of oriented bordisms of two-spheres:
Notations 2.0.4.Define the following morphisms of Cob(3) S2 :
idS2 =

S2×I

m=

S3\int(⊔ 3D3)

:S 2⊔S 2→S 2
1 =

D3
:∅→S 2
m∨ =

S3\int(⊔ 3D3)

:S 2→S 2⊔S 2
tr =

D3
:S 2→∅
Comment2.0.5.This set of bordisms can be neatly organized as follows: recall that
the three-sphere is homeomorphic to the gluing of two three-balls along their common
boundary (the north and south hemisphere glued along the equator). If we elect in-
coming/outgoing time direction to run from south to north, then the 1 (namely unit)
map can be viewed as the southern hemisphere, and tr (namely trace) as the northern.
Either one could be viewed asS 3\int(D 3) and distinguished by incoming/outgoing
time reversal. The identity map could be viewed asS 3\int(D 3⊔D 3). So we have
identifiedS 3 minus one, two, and threeD 3. In addition,S 3 itself can be obtained by
the hemisphere decomposition tr◦1, and since composing two multiplications together
increases the incoming boundary components by 1,S 3 minusn≥3-manyD 3 interiors
can be obtained by composingn−2 multiplication maps. 1
Notations 2.0.6.For suggestive reasons, we let
C={m,1}, F=

m∨,tr
	
.
Furthermore, consider the following three sets indexed by oriented prime 3-manifolds:
P′ =

p\int(D 3⊔D 3)

:S 2→S 2|pprime
	
L′ =

p\int(D 3)

:∅→S 2|pprime
	
L∨′
=

p\int(D 3)

:S 2→∅|pprime
	
whose elements we simply refer to asp ×× andp ×,p×∨. Note thatL ∨′
is the incom-
ing/outgoing reversal ofL′, but there is noP∨′
as the time reversal of any such bordism
is itself.
1One can also think of this as the operadic composition law of the (framed) little 3-disk operad.
14
Proposition 2.0.7.The homs ofCob(3) S2 have two generating sets:
G′
1 =C∪F∪L ′∪L∨′
∪orientation reversal
G′
2 =C∪F∪P ′∪orientation reversal
More precisely, letF(Gra 1)andF(Gra 2)be the free categories of the graphs Gra 1 and
Gra2, which have

⊔iS2|i∈Z ≥0
	∼= Z≥0 as vertices and directed edges generated by
G′
1 andG′
2 and all tensor products. Then the tautological functorsF(Gra 1)→Cob(3) S2
andF(Gra 2)→Cob(3) S2 are full and bijective on objects.
Proof.Let [M] :⊔ nincS2→⊔ noutS2 be a morphism fromn inc-many two-spheres to
nout-many two-spheres. Since the braidingβ S2,S2 permutes the boundary spheres, we
can, without loss of generality, assume that within incoming or outgoing boundary
components the spheres are not labelled. [Koc03]
Therefore we need to show that given an oriented bordism of unlabelled spheres
[M], we can find a composition in terms ofG ′
1 andG ′
2 generators and their tensor
products. LetMbe a representative of [M], we will show thatMis diffeomorphic to
gluings of manifolds which are representatives ofG ′
1 andG′
2 generators.
Consider the closed oriented manifold
cM∼=
ninc+noutG
i=1
D3
[
∂M
M
obtained from filling in the bounding spheres. One can show that the gluing is well de-
fined up to diffeomorphism [Hir76]. By the Kneser-Milnor theorem, cMis diffeomorphic
to a finite connected sum of oriented prime 3-manifoldsP 1,...,P m,
cM∼=P1#P2#...#P m.
ThereforeMitself is diffeomorphic to the same finite connected sum minus the interior
of the boundary balls
M∼= (P1#P2#...#P m)\int
ninc+noutG
i=1
D3

.
Unlike a generic Morse decomposition whose gluing surfaces are constrained by their
values, the attaching balls for each connect sum operation can be freely chosen. De-
pending on the choices of the attaching balls, we will have two different decompositions
ofMas gluings. To make the expression more symmetric, consider adding two trivial
connect sum factors
M∼=S3# (P1#P2#...#P m) #S3\int
ninc+noutG
i=1
D3

and choose2 that the incoming and outgoing balls be cut from these two factors
M∼=

S3\int
noutG
i=1
D3

#(P1#P2#...#P m)#

S3\int
noutG
j=1
D3

.
2This is not a constraint but a choice made to make apparent how subsequent choices end up being
generated byG ′
1 andG ′
2, much like the use of the “standard form” of surfaces commonly used in the
classification of 2d TFT, see for eg [Kock].
15
1. (The choice leading toG ′
2)
For each prime factorP j there are two chosen embedding of three-balls
ej
1,2 :D 3→P j, j= 1,...,m,
wheree j
2 forms the connect sum withe j+1
1 ofP j+1 unlessj=m, whene m
2 forms
the connect sum with an embedded three ball inS 3\int(⊔nincD3). We choose
e1
1 to form the connect sum with an embedded three-ball inS 3\int(⊔noutD3).
Noting that
M#N∼= (M\int(D 3))∪∂D3 (N\int(D 3)),
where the boundary of the embedded three balls being identified can be thought
of as the boundary being glued over, we may rewrite the connect sum as
M∼=

S3\int
noutG
i=1
D3

# (P1#P2#...#P m) #

S3\int
nincG
j=1
D3

∼=

S3\int
nout+1G
i=1
D3

∪S2

P1\int(D 3⊔D 3)

∪S2...
···∪ S2

Pm\int(D 3⊔D 3)

∪S2

S3\int
nint+1G
D3

.
Under the natural choice ofe j
1 bounding the outgoing sphere ande j
2 bounding
the incoming sphere, this composition induces
h
M
i
=
h
S3\int(⊔noutD3)
i
◦
h
P1\int(D 3⊔D 3)
i
◦...
···◦
h
Pm\int(D 3⊔D 3)
i
◦
h
S3\int(⊔nincD3)
i
=
h
S3\int(⊔noutD3)
i
◦P××
1 ◦···◦P ××
m ◦
h
S3\int(⊔nincD3)
i
and by comment 2.0.5 the morphisms [S 3\int(⊔ nD3)] can be obtained as a
composition of commutative Frobenius generators. See figure 2.1 for a sketch of
this composition.
2. (The choice leading toG ′
1)
For eachP j there is one chosen embedding of three balls
ej :D 3→P j
forj= 1,...,m. Take an additionalS 3 factor and choosem+ 2 embeddings
ej,e 0,em+1,j= 1,...,m. Lete j form the connect sum withe j, lete 0 form the
connect sum with an embedded three ball inS 3\⊔noutD3 and lete m+1 form the
connect sum with an embedded three ball inS 3\⊔nincD3. Noting that
M#N∼= (M\int(D 3))∪∂D3 (N\int(D 3))
16
Pm ···P 1
Figure 2.1: A sketch of howG 2 generates a generic bordism [M] whereM’s prime factors are
P1,...,P m. Note that this picture is “sideways” as we usually associate the “time” direction
as going up. In this case, time goes from left to right.
where the boundary of the embedded three balls being identified can be thought
of as the boundary being glued over, we may rewrite the connect sum as
M∼=

S3\int
noutG
i=1
D3

# (P1#P2#...#P m) #

S3\int
nincG
j=1
D3

∼=
 
S3\int
nout+1G
i=1
D3

⊔

S3\int
ninc+1G
i′=1
D3
! [
S2⊔S2
 
S3\int
m+2G
i′′=1
D3
!
[
⊔mS2


mG
j=1
 
Pj\int(D 3)



Besides the obvious choice fore 0 to bound an outgoing sphere ande m+1 to bound
an incoming sphere, there is no canonical choice of incoming vs outgoing for the
boundaries ofe j ande j forj= 1,...,m. One choice is for alle j to bound
outgoing boundaries andej incoming. Then theS 3 which all the prime factors are
connected with becomesS 3\int(⊔m+2D3) withm+1 many incoming boundaries
and 1 outgoing. This choice induces the following composition of [M]:
h
M
i
=
h
S3\int(⊔nout+1D3)
i
◦
h
S3\int(⊔m+2D3)
i
◦
 mO
j=1
h
Pj\int(D 3)
i
⊗
h
S3\int(⊔ninc+1D3)
i
=
h
S3\int(⊔nout+1D3)
i
◦
h
S3\int(⊔m+2D3)
i
◦
 mO
j=1
P×
j ⊗
h
S3\int(⊔ninc+1D3)
i
17
whereP ×
j = [Pj\int(D 3)] :∅ →S 2. By comment 2.0.5, the corresponding
morphism [S 3\int(⊔ nD3)] can be obtained as a composition of commutative
Frobenius generators.
If we had chosene j to bound incoming ande j to bound outgoing, then we would
instead induce the following composition of [M]:
h
M
i
=
 mO
j=1
h
Pj\int(D 3)
i
⊗
h
S3\int(⊔nout+1D3)
i
◦
h
S3\int(⊔m+2D3)
i
◦
h
S3\int(⊔ninc+1D3)
i
=
 mO
j=1
P×∨
j ⊗
h
S3\int(⊔nout+1D3)
i
◦
h
S3\int(⊔m+2D3)
i
◦
h
S3\int(⊔ninc+1D3)
i
where nowP ×∨
j = [Pj\D 3] :S 2→∅.
If we had chosene j to bound a mixture of incoming and outgoing boundaries,
the induced composition of [M] would be a mixture
h
M
i
=
 O
ej
incoming
P×∨
j ⊗
h
S3\int(⊔nout+1D3)
i
◦
h
S3\int(⊔m+2D3)
i
◦
 O
ej
outgoing
P×
j ⊗
h
S3\int(⊔ninc+1D3)
i
See figure 2.2 for an illustration of a composition in the case alle j are incoming.
Remark2.0.8.NeitherG ′
1 norG′
2 isminimal–S 2×S 1 is prime, but it has a standard
Morse function which factors through the projection onto theS 1 factor:
S2×S 1 proj
−→S 1 height
−→R
whose critical points are of index 0,2,1,3 in increasing critical values, and whose regular
surfaces are either empty or a disjoint union ofS 2. This is depicted (in a slightly wonky
manner) in figure 3.5-(a). Therefore there is a Morse gluing resembling the toric pants
decomposition one dimension down, inducing the equality
h
S2×S 1
i
∼=tr◦m◦m ∨◦1.
In particular, the element [S2×S 1\int(D3⊔D 3)]∈P⊂G ′
2 is equal to the composition
m◦m∨, and the elements
h
S2×S 1\int(D3)
i
∈L,L ∨⊂G′
1 is equal to the compositions
m◦m ∨◦1 andtr◦m◦m ∨ respectively.
Remark2.0.9.TheL ∨′
generators are redundant – letP ×∨ = [P\int(D 3)]∈L ∨′
be a
morphismS 2→∅. ConsiderP × = [P\D 3]∈L ′ a morphism∅→S 2. Since
P\int(D 3)∼=
 
P#S 3
\int(D 3)∼=

P\int(D 3)

∪S2

S3\int(
3G
i=1
D3)

∪S2D3
18
...P1 P2 Pm
Figure 2.2: A sketch of howG 1 generates a generic bordism [M] whereM’s prime factors are
P1,...P m. This particular [M] has 3 incomingS 2 components and 4 outgoing components.
This figure depicts the case where all the bounding ballse j are incoming, namely all the
prime factors are in the form ofP ×
i :∅→S 2.
we learn that
P×∨ =tr◦m◦(P ×⊗idS2)◦λ −1
S2
whereλ S2 :∅⊔S 2→S 2 is the left unitor. This relation is reflected in the sketch if
figure 2.3.
Notations 2.0.10.Given the two remarks 2.0.8 and 2.0.9, we shall removeS 2×S 1
from the prime generators and delete the redundant setL ∨′
. Recalling thatS 2×S 1 is
the only reducible oriented prime 3-manifold, we define
P=
n
p×× =
h
p\int(D 3⊔D 3)
i
:S 2→S 2|poriented irreducible
o
L=
n
p× =
h
p\int(D 3)
i
:∅→S 2|poriented irreducible
o
Proposition 2.0.11.The following sets generate morphisms ofCob(3) S2 and are both
minimal:
G1 =C∪F∪L∪orientation reversal
G2 =C∪F∪P∪orientation reversal
This proposition will be revisited as 3.3.7 and the proof will be presented there.
Remark2.0.12.Another distinction betweenS 2×S 1 and other primes, in the setting of
our restricted bordism category Cob(3)S2, is the special role it plays when compositing
19
P×
P×∨ ∼=
Figure 2.3: Redundancy ofL ∨′ generators.
bordisms together: let [M] :⊔ aS2→⊔ bS2 and [N] :⊔ bS2→⊔ cS2 be two bordisms,
and let
cM∼= (⊔aD3)∪⊔aS2M∪⊔bS2 (⊔bD3)
be the closed manifold obtained by filling the incoming and outgoing boundaries of
M. One can show that the choice of gluing result in a well defined manifold up
to diffeomorphism. Define bNanalogously. Then there are prime decompositions of
cM∼= M1#M2#...#M m and bN∼= N1#...#N n, where each factorM i,Nj is prime.
Taking the composition along the common boundary⊔bS2, and filling in the remaining
boundaries, the resulting manifold gains connected sum factors ofS 2×S 1. To see this,
refer to the figure 2.1 whereMhas been put into a normal form. Consider doing the
same forN. The pairing of the outgoing component ofMand the incoming components
ofNgives rise to the new connect sum factors ofS 2×S 1, much like increasing genus
in one dimension down:
\N◦M ∼= (N1#...#N n)#

#b−1(S2×S 1)

#(M1#...#M m).
In fact, as we shall see by theorem 3.3.6, the morphisms in a subcategory of Cob(3) S2
are all #g(S2×S 1) minus some (interiors of) disks, andgthe number ofS 2×S 1-factors
is equivalent to the genus of some surfaces as a morphism in Cob(2).
Comment2.0.13.For now, the choice of usingG 1 orG 2 is a matter of taste, as there
is a clear bijection between the generators and that one can switch betweenp ×× =
[p\int(D 3⊔D 3)]∈Pandp × = [p\int(D 3)]∈Lby relations
h
p\int(D 3)
i
=
h
p\int(D 3⊔D 3)
i
◦1
h
p\int(D 3⊔D 3)
i
=m◦(
h
p\int(D 3)
i
⊗idS2)◦λ −1
S2
whereλ S2 :∅⊔S 2→S 2 is the left unitor. The first relation geometrically fills in a
ball. The latter creates a new boundary component throughm. In fact, there is an
alternative construction
h
p\int(D 3⊔D 3)
i
=m◦(id S2⊗
h
p\int(D 3)
i
)◦ρ −1
S2
20
whereρ S2 :S 2⊔∅→S 2 is the right unitor. The equivalence of the two constructions is
the first example of aprime relation. This particular one is explored in proposition 4.2.7
