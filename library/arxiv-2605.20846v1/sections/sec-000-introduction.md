---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-13
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
2 Generators 13
3 Commutative Frobenius Relations 22
3.1 Outline of Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 Existence and Spherical Morse Functions . . . . . . . . . . . . . . . . . 26
3.3 Spherical Morse Functions . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.4 Local Models of Excellent Morse Failures . . . . . . . . . . . . . . . . . 38
3.5 Sufficiency of Commutative Frobenius Relations Among CF Generators 41
4 Prime Relations 46
4.1 No Internal Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.2 External Prime Relations . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.3 Sufficiency of External Relations . . . . . . . . . . . . . . . . . . . . . . 54
4.4 Necessity of Legs Relations . . . . . . . . . . . . . . . . . . . . . . . . . 60
5 Passing through TFTs 70
5.1 P and L Monoids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
5.2 Relations to J-Algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.3 The∞-operadL ⊗ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
A Appendix: Definitions and Common Results 90
A.1 Presentations of a Category . . . . . . . . . . . . . . . . . . . . . . . . . 90
A.2 Towards∞. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
2
Chapter 1
Introduction
Motivations
One of the greatest scientific achievements in the 20th century is the development
of quantum field theories, which model the interaction of elementary particles with
great precision throughquantum fields. Quantum fields are , roughly speaking, classes
of functionsϕ:M→CwhereMis a manifold representing the underlying space-
time. Unfortunately, developing a mathematically rigorous definition of quantum field
theories has proven extremely challenging, leaving one of the most foundational subjects
of modern physics on unstable soil.
Topological field theoriesare toy models of quantum field theories. In some sense,
they are the most constrained version of quantum field theories. Generally speaking,
the more constrained an object is, the easier it is to study– for example, it is much
easier to study finite dimensional inner product spaces overRthan to study modules
over a not necessarily commutative ringR. However, just because it is easier doesn’t
mean it is useless. A student likely learns about bases for a vector spaces first, and
then carries that rather helpful intuition to the study of modules. So the hope is that
by understanding topological field theories, the highly constrained version of quantum
field theories, one may gain a glimpse at the full mathematical complexity of quantum
field theory.
It turns out that topological field theories can be rigorously formulated in math-
ematics, and the structures one discovers are already extremely interesting, intricate,
and ingenious. This paper explores one aspect of the structures of topological field
theories of dimension≥3.
Mathematically, the vanilla definition of a topological field theory is
Definition 1.0.1.Ann-dimensional topological field theory is a symmetric monoidal
functor:
Z: Cob(n)→Vect k.
where Cob(n) is the category of closed orientedn-manifolds and cobordisms modulo
orientation and boundary preserving diffeomorphisms, Vectk is the category of (insert
your favorite adjectives here such as topological)k-vector spaces.
Historically, this definition was given by [Ati88], possibly inspired by [Seg88]’s at-
tempt to define a conformal field theory and [Wit82] on the relation between Morse
theory and supersymmetry.
3
Unpacking the definition, a topological field theory is a nice assignmentZwhich
assigns to a closed oriented (n−1)-manifoldXa vector spaceZ(X), and to a bordism
MfromXtoYa linear mapZ(M) :Z(X)→Z(Y). In particular,Z(∅) =kwhere∅
is the empty (n−1)-dimensional closed oriented manifold. ThereforeZsends a closed
orientednmanifoldM, which is thought of as a cobordism between the empty set and
itself, to a linear mapZ(M) :k→k, which can be identified with its image of 1. So
Z(M) is just a number.
This definition closely aligns with physics:Z(X) is supposed to be the (Hilbert)
space of statesH X onX, and the linear mapZ(M) :Z(X)→Z(X) is supposed to be
time evolution onH X. In the caseXis empty, the numberZ(M) is supposed to be
the partition functionZof the theory on spacetimesM. Some excellent expositions
by [CR18] and [Fre09] goes into the physics side in greater detail.
The vanilla definition has since then been enhanced. The modern mathematical
perspective is
Definition 1.0.2.A fully-extendedn-dimensional topological field theory is a sym-
metric monoidal functor of (∞,n)-categories
Z: Bord n→C.
The (∞,n) category Bord n has objects 0-dimensional manifolds, 1-morphisms are
cobordisms between 0-dimensional manifolds, 2-morphisms are cobordisms between
cobordisms, etc. Then-morphisms can be interpreted as ann-dimensional manifold
with corners. The (n+ 1)-morphisms are diffeomorphisms between twon-manifold
with corners, and the (n+ 2)-morphisms are isotopies between diffeomorphisms, etc.
This construction was proposed by [Lur08] and later corrected by [CS19] and appeared
as the thesis of [Sch14].
Notice two features about this modern definition: one does not mod out the diffeo-
morphisms in the cobordisms and instead store these information in (n+1)-morphisms
and higher; the vanilla 1-categorical definition sits inside the (n−1)-morphisms and
then-morphisms, and can be recovered once one passes to the homotopy category.
Physically, an extended topological field theory allows one to encode more infor-
mation than just the space of states and the partition function. For example, a 2-
dimensional fully extended topological field theory also associates to a zero-dimensional
manifold (aka a point) some additional data, usually a category. For the topological
B-model on a complex manifoldY, this is the categoryD b Coh(Y). For the topological
Amodel with symplectic K¨ ahler targetX, this is the category Fuk(X). Homological
mirror symmetry is equivalent to the equivalence between the topologicalAmodel as
a 2-dimensional fully extended TFTZ A and the topologicalBmodelZ B. For physical
interpretations of these higher structures in general, see [Kap10], [CR18] and [Fre09].
Topological field theories have also proven to be more than just highly constrained
toy models, especially in the field of mathematics. Much of the attention came from
the Geometric Langlands correspondence, which can be reinterpreted as a conjectural
equivalence of two topological field theories by [KW07; Wit10]. There is a conjectured
equivalence for relative Langlands as well [BSV24]. Therefore much of the modern
formal interests in topological field theories have come from the mathematical side.
Some of the most interesting results and insights have come from attempts to clas-
sify topological field theories. Historically the most famous theorem is perhaps the
4
equivalence between 2-dimensional topological field theories (up to equivalence) and
commutative Frobenius algebras (up to isomorphism):
Theorem 1.0.3.The 2-dimensional oriented bordism categoryCob(2)is the free sym-
metric monoidal category with a single commutative Frobenius algebra object. In par-
ticular the category of oriented 2-dimensional topological field theories is equivalent to
the category of commutative Frobenius algebras.
This theorem was widely known and formal proofs appeared in numerous papers
such as [Dij89], [Abr96], and J. [Koc03]. The category Cob(2) has objects closed
oriented 1-dimensional manifolds (namely, a disjoint union of oriented circles), and
morphisms are cobordisms between the disjoint unions of circles modulo diffeomor-
phisms. The single commutative Frobenius algebra object refers to the circleS 1. By a
commutative Frobenius algebra we mean ak-vector spaceAtogether with the following
data
Multiplicationm:A⊗A→A
Unit 1 :k→A
Co-multiplicationm∨ :A→A⊗A
Trace/co-unittr:A→k
satisfying:
1. The multiplicationmis associative and commutative.
2. The unit 1 is the unit map with respect to the multiplicationm.
3. The co-multiplicationm ∨ is co-associative and co-commutative.
4. The co-unittris the co-unit map with respect to the co-multiplicationm ∨.
5. The Frobenius condition: (m⊗id)◦(id⊗m ∨) =m∨◦m.
In Cob(2) , these maps are given by the morphisms in figure 1.1.
m 1 m∨ tr
Figure 1.1: The commutative Frobenius generators of Cob(2).
Physically, this means that the space of states associated to a circle of any 2-
dimensional topological field theory must be a commutative Frobenius algebra. Un-
surprisingly, being a commutative Frobenius algebra is a strong condition which forces
many desirable properties, the most notable of which is finite dimensionality.
5
Other classification theorems exist in dimensions>2 as well, putting TFTs in very
rigid mathematical structures. In dimension 3, [Bar+14; Bar+15] showed that there
is an equivalence between (1 + 1 + 1)-dimensional TFT and modular tensor categories.
[Juh18] gave generator and relations for the cobordism category Cob(n) for anyn, in
particular forn= 3 it is shown that there is an equivalence between the category of
3-dimensional oriented TFTs and the category ofJ-algebras. [Lur08] sketched a proof
of thecobordism hypothesisof [BD95] that ann-dimensional fully extended framed
TFT is determined by its value on the framed point.
However none of these classification theorems provides the answer to the most naive
question one might ask upon learning theorem 1.0.3:
If the circle is a commutative Frobenius object inCob(2),what kind
of algebraic structure does the sphere have inCob(3)?
In this thesis, we provide the answer
The sphere has the commutative Frobenius structure as well as new
“prime” structures.
By prime structures here we mean structures labelled by diffeomorphism classes
of oriented irreducible prime 3-manifolds. Physically, this means that the space of
states for a 3-dimensional topological field theory is not only a commutative Frobenius
algebra but it also has additional structures labelled by these prime 3-manifolds.
Overview of Contents
The result of this thesis can be summarized as theslogan: in Cob(3), the category of
oriented closed 2-manifolds and their bordisms, the objectS 2 has the usual structures
of a commutative Frobenius object, as well asadditional new mapsp ×× :S 2→S 2
andp× :∅→S 2, wherepis a connected closed irreducible oriented 3-manifold. Be-
sides the commutative Frobenius relations, the only other necessary relations are the
“legs relations”m◦(p ××⊗idS2) =m◦(id S2⊗p××). In particular, there areno more
structuresonS 2– every other algebraic structure is generated by commutative Frobe-
nius structures and{p ××}which satisfy the legs relations, or commutative Frobenius
structures and{p ×}.
We shall explain what this means in the remainder of the Introduction.
The classification of 2-dimensional topological field theoriesZ: Cob(2)→Vect k
requires that one showS 1 has the structures of commutative Frobenius objects in
Cob(2) . This means that one needs to show that the maps (m,1,m ∨,tr) exist, and
that they satisfy the usual commutative Frobenius conditions. This part is easy. The
difficult part is showing that these maps and the commutative Frobenius conditions
aresufficient and necessary. In the language of category theory, one needs to construct
apresentationof the bordism category Cob(2). By apresentationwe mean genera-
tors and relations. The generators being (m,1,m ∨,tr), and the relations being the
commutative Frobenius relations. One inevitably has to dig into the Morse theory of
2-dimensional manifolds to show, among other things, that two different ways of glu-
ing the generators into the same cobordism [M] must be related by only commutative
Frobenius relations. This is most naturally proven using Cerf theory: the two different
gluings correspond to Morse functionsf 0,f 1 :M→R, and [Cer70] showed that there is
a path of functionsf t fromf 0 tof 1 such that along this path the functionf t only fails
6
to be “excellent Morse” at finitely many times. In particular, before and after those
singularities, the Morse functions induce a commutative Frobenius type of relations.
We will essentially take a similar approach to understand the algebraic structures
ofS 2. In order to do so, we need to consider all possible bordisms between disjoint
unions ofS 2. These span a subcategory Cob(3) S2 of Cob(3), defined as
Definition 1.0.4.Consider the symmetric monoidal category Cob(3). It has a sub-
category whose objects are disjoint unions ofS 2. Call this category Cob(3)S2 and note
that it inherits the symmetric monoidal structure.
In particular, the morphisms in Cob(3)S2 all have spherical boundaries. For exam-
ple, here’s a list of morphisms that will play a central role in defining the presentations
of Cob(3)S2:
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
p×× = [p\int(D 3⊔D 3)] :S 2→S 2
p× = [p\int(D 3)] :∅→S 2
wherepis any diffeomorphism class of connected closed oriented irreducible 3-manifold.
Note that the only 3-manifold which is prime but reducible isS 2×S 1. So,equivalently,
pis any diffeomorphism class of connected closed oriented prime 3-manifold which is
notS 2×S 1. See figure 1.2 for a sketch of these morphisms.
p××
 p×
Figure 1.2: A list of generating morphisms. From left to right:id S2, multiplicationm,
unit 1, comultiplicationm ∨, tracetr, prime endomorphismp ××, prime unitp ×, one for
each connected oriented irreducible prime 3-manifoldp. All but the last kind make up the
generating setG 2. All but the second to last kind make up the generating setG 1.
Our aim is to construct presentations of Cob(3) S2. It turns out that Cob(3) S2 has
two sets of generators:
G1 =C∪F∪L∪orientation reversal
G2 =C∪F∪P∪orientation reversal
whereC={1,m},F={tr,m ∨},P={p ××}p∈I,L={p ×}p∈I. HereIdenotes the
set{connected closed irreducible 3-manifold}/orientation-preserving diffeomorphisms
.
7
The presentation usingG 1 generators is usually associated with the letter “L” be-
cause of the distinct L-shaped prime factor attachments in figure 2.2. The presentation
usingG 2 generators is usually associated with the letter “P” for “prime” due to a lack
of imagination.
TheG 2 presentation is given by the usual commutative Frobenius relations, as well
as the “legs relations” suggestively sketched in figure 1.3
m◦(p ××⊗idS2) =m◦(id S2⊗p××).
P×× P××
∼=
Figure 1.3: The “legs relations” for theG 2 presentation of Cob(3)S2.
The legs relations are not trivially implied by commutativity because our boundaries
are ordered. To see this, consider passing through a TFTZ, then both sides of the
legs relations are maps fromZ(S 2)⊗Z(S 2) toZ(S 2). The left hand side sends the
elementa⊗btoZ(p ××)(a)·b, while the right hand side sends it toa·Z(p ××)(b).
We prove in theorem 4.4.13 that
Theorem 1.0.5.Cob(3) S2 has a presentation withG 2 generators under commutative
Frobenius relations and legs relations. These relations are necessary.
TheG 1 presentation is given by the usual commutative Frobenius relations only.
We prove in theorem 4.3.2 that
Theorem 1.0.6.Cob(3) S2 has a presentation withG 1 generators and commutative
Frobenius relations.
What is perhaps surprising about the theorems is that the relations are extremely
simple, even though the topology of 3-manifolds are significantly more complicated
than the topology of 2-manifolds. In Cob(2) , a morphism is a 2-manifold with bound-
aries. The classification of 2-manifolds shows that up to diffeomorphisms the manifold
is classified by its genus. The classification of 3-manifolds is more complicated but
standard– the theorem of Kneser-Milnor prime decomposition will play a repeated
central role in our proof:
Theorem 1.0.7.(Kneser-Milnor Prime Decomposition Theorem)
8
LetMbe a compact, connected and orientable 3-manifold. Then there is a decom-
position
M=P 1#P2#...#P m.
where eachP i is prime. This decomposition is unique up to insertion or deletion of
S3’s.
A connected 3-manifoldXisprimeifX=P#Qimplies eitherP=S 3 orQ=S 3.
The # denotes theconnect sumoperation– one deletes a 3-ball from bothPandQ
and then glues them together along the sphere boundary. Meaning that one can always
viewM=M 1#M2 asM ∼= (M1\int(D 3))∪S2 (M2\int(D 3)).
Notice that we can use the prime decomposition theorem to “chop up” a bordism
M:⊔ nincS2→⊔ noutS2 into prime factors. This is the idea behind the generatorsG 1
andG 2, which correspond to two different choices of chopping.
To show thatG1 andG 2 with appropriate relations are presentations of the category
Cob(3)S2, we first consider the non-prime part–if one forgets about the prime factors
inP⊂G 2 andL⊂G 1 for a moment and only considers the CF generators, then we
are working with the category Cob(3)S2,CF whose objects are disjoint unions of spheres
like before, but whose morphisms are bordisms that are generated by CF generators.
We prove in theorem 3.3.6 that
Theorem 1.0.8.There is a canonical isomorphismS: Cob(2) ∼→Cob(3) S2,CF
The isomorphismSsendsn-copies ofS 1 ton-copies ofS 2, and sends the multi-
plication map ofS 1 to the multiplication map ofS 2. Same goes for unit, trace, and
co-multiplication. On more complicated bordisms,Ssends a genusgbordism to a bor-
dism withg-manyS 2×S 1 connect sum factors. This theorem essentially shows that
the commutative Frobenius part of Cob(S 2) is completely determined by Cob(2). In
particular, the commutative Frobenius relations ofG 1 andG 2 generators are necessary.
The Cerf theory we build through geometry can be roughly summarized as follows:
every composition in Cob(3)S2 is induced by some decomposition, which is induced by
some Morse data. Two different compositions of the same morphism are induced by
two different Morse data on the same underlying manifold. Let’s denote the two Morse
functions asf 0,f 1 :M→R. We show that there exists a sequence of relations which
can put a composition into a “normal form” using onlyprime relations.
A prime relation is a pair of Morse functions which can and will be connected by a
path of functions with more than 1 singularities where the function fails to be excellent
Morse, unlike commutative Frobenius relations, each of which is a single specific type
of singularity.
Call the Morse functions inducing these normal-form compositionsf ′
0,f′
1. We then
show the resulting normal-form compositions are related by commutative Frobenius
relations only. This means that one can construct a path fromf 0 tof 1 consisting of 3
distinct segments:
1. Segment 1: fromf 0 tof′
0, which induces the change from the starting composition
to the normal-form composition. Since we will use only prime relations, the
Morse functions inducing the individual intermediate compositions are separated
by more than one singularity.
2. Segment 2: fromf ′
0 tof ′
1, which has only commutative Frobenius type singulari-
ties.
9
3. Segment 3: fromf ′
1 tof 1. This is the reverse of segment 1 but for the other
composition.
A generic figure depicting this process can be found in 1.4.
f0
f′
0
f′
1
f1
Figure 1.4: A path fromf 0 tof 1 using 3 prime relations, then 2 commutative Frobenius
relations, then 2 prime relations. Note that each black dot is a Morse data which induces
some composition. The prime relations is a pair of Morse data separated by more than 1
singularities, while a commutative Frobenius relation is always given by a single specific kind
of singularity.
Passing through a TFT, the two presentations of Cob(3)S2 give rise to two kinds of
structures called P-algebras and L-algebras. Since they are both induced by Cob(3) S2,
it is unsurprising when we show in lemma 5.1.2 that there is a bijection between P-
algebras and L-algebras. So it makes sense to refer to them as a single kind of structure:
Definition 1.0.9.LetAbe a commutative Frobenius algebra overk. ThenAis an
L-algebra (equiv.P-algebra) if there are elements 1 p∈A(equiv. endomorphismse p :
A→Athat acts by multiplication by 1 p) for every diffeomorphism class of connected
oriented irreducible 3-manifoldp.
The remarkable feature ofLandPalgebras is their simplicity. We are supposed to
think of such an algebra asZ(S 2) for some 3d TFTZ: Cob(3)→Vect k. Even though
the bordisms ofS 2 are very complicated, geometry forcesG 1 andG 2 presentations to
be extremely simple, which in turn forces the prime structures ofLandPalgebras to
be also extremely simple.
Relative to existing literature on 3-dimensional TFTs, our results sit somewhat
“diagonally.” [Juh18] showed that there is a bijection between the category of 3-
dimensional TFTs and the category ofJ-algebras. TheJ-algebra associated to a TFT
Zis ag≥0 graded algebra⊕ gAg, with maps that encode geometric operations such
as the attachment of 1 and 2 handles.Z(S 2) is the genus 0 partA 0 of theJ-algebra
assigned toZ. However J-algebras do not answer the question we are addressing in
this paper. For example, a J-algebraA=⊕ gAg carries with it a “1-handle map”
A0→A 1, which corresponds to the Morse bordism of attaching a 1-handle to a two-
sphere, increasing the genus by 1. What we need to classify is all possible maps from
A0 toA 0, or toA 0⊗A 0, or toA 0⊗A 0⊗A 0, etc, which factors through products
ofA 0’s exclusively. The domain of these maps can also have multiple factors ofA 0.
From a physics point of view, while it is useful to understand maps from the space of
local operators/statesA 0 to whateverAg>0 means in the particular contexts, it is more
surprising to learn that the space of local operators/states of a 3-dimensional TFT is
a finite dimensional commutative Frobenius algebra. Our work on the presentations
10
of Cob(3)S2 and onL/Palgebras says that the degree 0 part of aJ-algebra carries
additional simple structures labelled by connected oriented irreducible 3-manifolds.
In the context of modern (∞,n)-perspectives of fully-extended topological field
theories, it is less clear what kind of structure must replace ourL/Palgebras besides
tautology. For example, whileS 1 is a commutative Frobenius object in Cob(2),S 1 is an
E2-algebra in Bordfr
2 the (∞,2)-category of framed bordisms. This only captures the
operadic structure ofS 1, rather than the whole PROP (products and permutations).
The full PROP is, tautologically, the subcategory of Bordfr
2 spanned by disjoint unions
ofS 1. It is widely known thatS n−1 is at least anE n-algebra in Bordfr
n , but obviously
there is more operadic structure in dimensionn≥3.
We propose an∞-operadL ⊗ in definition 5.3.11 and 5.3.13 which we conjecture
to be isomorphic to the connected part of the full∞-endomorphism operad ofS 2. An
n-ary operation is, roughly speaking, a bordism fromn-manyS 2 to a singleS 2, where
the bordism is itself a connected 3-manifold. This is achieved by first specifying a
collection of irreducible manifoldsP i, then specifying how to glue them together into a
single bordism using some connect-sum configuration data. Adding to the plausibility,
theE 3 operad sits nicely insideL⊗ as a suboperad. The construction is inspired by the
unfinished draft of [Hat08], which just recently was completed by [BBS26] in almost
all cases except, unfortunately, for bordisms with spherical boundaries.
Organization Roadmap
In Chapter 2, we introduce the generatorsG 1 andG 2 of Cob(3)S2 and show in propo-
sition 2.0.7 that they generate all the morphisms.
Chapter 3 and chapter 4 are dedicated to showing that commutative Frobenius
relations are necessary and sufficient for theG 1 presentation, and additionally the legs
relations are necessary for theG 2 presentation. To achieve this, we first outline the
basic strategy in section 3.1.
We then first address the commutative Frobenius relations between the shared CF
generators ofG 1 andG 2 in chapter 3. This is done in stages: we first show existence
in proposition 3.2.2 in section 3.2 by analyzing the generic Cerf theory arguments. We
then show in theorem 3.3.6 in section 3.3 that there is an isomorphism between Cob(2)
and Cob(3)S2,CF . We then setup some machinery in section 3.4 so we can prove in
section 3.5 that 3.5.4 CF generators satisfy no more relations.
We then address the new relations that arise from the prime-labelled generators
in chapter 4. This is also done in stages: first we show that CF generators exists
exclusively outside prime factors, a phenomena we call “no internal relations.” This is
the topic of section 4.1. We then immediately introduce the prime relations in section
4.2: prime commutativity 4.2.1, legs and waist relations forG 2 4.2.3, and legs relations
forG 1 4.2.7. In section 4.3 we prove in theorem 4.3.1 and 4.3.2 that these relations are
sufficient to give presentations of Cob(3)S2. However, some relations are not necessary.
We show in section 4.4 that, besides the commutative Frobenius relations, only the
legs relations forG 2 are necessary– all other relations are implied by commutative
Frobenius relations and the legs relations. This is explained in propositions 4.4.6 to
4.4.10. Therefore we prove in theorem 4.4.13 that commutative Frobenius relations
and legs relations are necessary and sufficient to form a presentation of Cob(3).
Chapter 5 is dedicated to the consequences of realizing Cob(3) S2 as presentations
after passing through 3-dimensional topological field theories. In section 5.1 we de-
11
fine the notion of anLalgebra, or equivalently aPalgebra, in definition 5.1.8. We
also explain some immediate consequences and properties afforded byLalgebras. We
examine in section 5.2 the relations betweenLalgebras andJ-algebras which classify
2 + 1-dimensional TFTs. We show that the degree 0 part of everyJ- algebra is an
L-algebra in theorem 5.2.3, and provide a specific recipe in proposition 5.2.8 to recover
all the prime endomorphisms and prime units using Heegaard splitting. Lastly in sec-
tion 5.3, we define an∞-operadL ⊗ in definition 5.3.11 and 5.3.13, which hasE ⊗
3 as a
suboperad. We conjecture in 5.3.32 and 5.3.33 thatL ⊗ is isomorphic to the connected
part of the∞-endomorphism operad ofS 2 in Bordfr
3 or BordSO
3 .
12
Chapter 2
