---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 3-13
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Motivations
One of the greatest scientific achievements in the 20th century is the development
of quantum field theories, which model the interaction of elementary particles with
great precision through quantum fields. Quantum fields are , roughly speaking, classes
of functions ϕ : M →C where M is a manifold representing the underlying space-
time. Unfortunately, developing a mathematically rigorous definition of quantum field
theories has proven extremely challenging, leaving one of the most foundational subjects
of modern physics on unstable soil.
Topological field theories are toy models of quantum field theories. In some sense,
they are the most constrained version of quantum field theories. Generally speaking,
the more constrained an object is, the easier it is to study– for example, it is much
easier to study finite dimensional inner product spaces over R than to study modules
over a not necessarily commutative ring R. However, just because it is easier doesn’t
mean it is useless. A student likely learns about bases for a vector spaces first, and
then carries that rather helpful intuition to the study of modules. So the hope is that
by understanding topological field theories, the highly constrained version of quantum
field theories, one may gain a glimpse at the full mathematical complexity of quantum
field theory.
It turns out that topological field theories can be rigorously formulated in math-
ematics, and the structures one discovers are already extremely interesting, intricate,
and ingenious. This paper explores one aspect of the structures of topological field
theories of dimension ≥3.
Mathematically, the vanilla definition of a topological field theory is
Definition 1.0.1. An n-dimensional topological field theory is a symmetric monoidal
functor:
Z : Cob(n) →Vectk .
where Cob(n) is the category of closed oriented n-manifolds and cobordisms modulo
orientation and boundary preserving diffeomorphisms, Vectk is the category of (insert
your favorite adjectives here such as topological) k-vector spaces.
Historically, this definition was given by [Ati88], possibly inspired by [Seg88]’s at-
tempt to define a conformal field theory and [Wit82] on the relation between Morse
theory and supersymmetry.
Unpacking the definition, a topological field theory is a nice assignment Z which
assigns to a closed oriented (n −1)-manifold X a vector space Z(X), and to a bordism
M from X to Y a linear map Z(M) : Z(X) →Z(Y ). In particular, Z(∅) = k where ∅
is the empty (n −1)-dimensional closed oriented manifold. Therefore Z sends a closed
oriented n manifold M, which is thought of as a cobordism between the empty set and
itself, to a linear map Z(M) : k →k, which can be identified with its image of 1. So
Z(M) is just a number.
This definition closely aligns with physics: Z(X) is supposed to be the (Hilbert)
space of states HX on X, and the linear map Z(M) : Z(X) →Z(X) is supposed to be
time evolution on HX. In the case X is empty, the number Z(M) is supposed to be
the partition function Z of the theory on spacetimes M. Some excellent expositions
by [CR18] and [Fre09] goes into the physics side in greater detail.
The vanilla definition has since then been enhanced. The modern mathematical
perspective is
Definition 1.0.2. A fully-extended n-dimensional topological field theory is a sym-
metric monoidal functor of (∞, n)-categories
Z : Bordn →C.
The (∞, n) category Bordn has objects 0-dimensional manifolds, 1-morphisms are
cobordisms between 0-dimensional manifolds, 2-morphisms are cobordisms between
cobordisms, etc. The n-morphisms can be interpreted as an n-dimensional manifold
with corners. The (n + 1)-morphisms are diffeomorphisms between two n-manifold
with corners, and the (n + 2)-morphisms are isotopies between diffeomorphisms, etc.
This construction was proposed by [Lur08] and later corrected by [CS19] and appeared
as the thesis of [Sch14].
Notice two features about this modern definition: one does not mod out the diffeo-
morphisms in the cobordisms and instead store these information in (n+1)-morphisms
and higher; the vanilla 1-categorical definition sits inside the (n −1)-morphisms and
the n-morphisms, and can be recovered once one passes to the homotopy category.
Physically, an extended topological field theory allows one to encode more infor-
mation than just the space of states and the partition function. For example, a 2-
dimensional fully extended topological field theory also associates to a zero-dimensional
manifold (aka a point) some additional data, usually a category. For the topological
B-model on a complex manifold Y , this is the category Db Coh(Y ). For the topological
A model with symplectic K¨ahler target X, this is the category Fuk(X). Homological
mirror symmetry is equivalent to the equivalence between the topological A model as
a 2-dimensional fully extended TFT ZA and the topological B model ZB. For physical
interpretations of these higher structures in general, see [Kap10], [CR18] and [Fre09].
Topological field theories have also proven to be more than just highly constrained
toy models, especially in the field of mathematics. Much of the attention came from
the Geometric Langlands correspondence, which can be reinterpreted as a conjectural
equivalence of two topological field theories by [KW07; Wit10]. There is a conjectured
equivalence for relative Langlands as well [BSV24]. Therefore much of the modern
formal interests in topological field theories have come from the mathematical side.
Some of the most interesting results and insights have come from attempts to clas-
sify topological field theories. Historically the most famous theorem is perhaps the
equivalence between 2-dimensional topological field theories (up to equivalence) and
commutative Frobenius algebras (up to isomorphism):
Theorem 1.0.3. The 2-dimensional oriented bordism category Cob(2) is the free sym-
metric monoidal category with a single commutative Frobenius algebra object. In par-
ticular the category of oriented 2-dimensional topological field theories is equivalent to
the category of commutative Frobenius algebras.
This theorem was widely known and formal proofs appeared in numerous papers
such as [Dij89], [Abr96], and J. [Koc03].
The category Cob(2) has objects closed
oriented 1-dimensional manifolds (namely, a disjoint union of oriented circles), and
morphisms are cobordisms between the disjoint unions of circles modulo diffeomor-
phisms. The single commutative Frobenius algebra object refers to the circle S1. By a
commutative Frobenius algebra we mean a k-vector space A together with the following
data
Multiplication m : A ⊗A →A
Unit 1 : k →A
Co-multiplication m∨: A →A ⊗A
Trace/co-unit tr : A →k
satisfying:
1. The multiplication m is associative and commutative.
2. The unit 1 is the unit map with respect to the multiplication m.
3. The co-multiplication m∨is co-associative and co-commutative.
4. The co-unit tr is the co-unit map with respect to the co-multiplication m∨.
5. The Frobenius condition: (m ⊗id) ◦(id ⊗m∨) = m∨◦m.
In Cob(2) , these maps are given by the morphisms in figure 1.1.
m
1
m∨
tr
Figure 1.1: The commutative Frobenius generators of Cob(2).
Physically, this means that the space of states associated to a circle of any 2-
dimensional topological field theory must be a commutative Frobenius algebra. Un-
surprisingly, being a commutative Frobenius algebra is a strong condition which forces
many desirable properties, the most notable of which is finite dimensionality.
Other classification theorems exist in dimensions > 2 as well, putting TFTs in very
rigid mathematical structures. In dimension 3, [Bar+14; Bar+15] showed that there
is an equivalence between (1 + 1 + 1)-dimensional TFT and modular tensor categories.
[Juh18] gave generator and relations for the cobordism category Cob(n) for any n, in
particular for n = 3 it is shown that there is an equivalence between the category of
3-dimensional oriented TFTs and the category of J-algebras. [Lur08] sketched a proof
of the cobordism hypothesis of [BD95] that an n-dimensional fully extended framed
TFT is determined by its value on the framed point.
However none of these classification theorems provides the answer to the most naive
question one might ask upon learning theorem 1.0.3:
If the circle is a commutative Frobenius object in Cob(2), what kind
of algebraic structure does the sphere have in Cob(3) ?
In this thesis, we provide the answer
The sphere has the commutative Frobenius structure as well as new
“prime” structures.
By prime structures here we mean structures labelled by diffeomorphism classes
of oriented irreducible prime 3-manifolds.
Physically, this means that the space of
states for a 3-dimensional topological field theory is not only a commutative Frobenius
algebra but it also has additional structures labelled by these prime 3-manifolds.
Overview of Contents
The result of this thesis can be summarized as the slogan: in Cob(3), the category of
oriented closed 2-manifolds and their bordisms, the object S2 has the usual structures
of a commutative Frobenius object, as well as additional new maps p×× : S2 →S2
and p× : ∅→S2, where p is a connected closed irreducible oriented 3-manifold. Be-
sides the commutative Frobenius relations, the only other necessary relations are the
“legs relations” m ◦(p×× ⊗idS2) = m ◦(idS2 ⊗p××). In particular, there are no more
structures on S2– every other algebraic structure is generated by commutative Frobe-
nius structures and {p××} which satisfy the legs relations, or commutative Frobenius
structures and {p×}.
We shall explain what this means in the remainder of the Introduction.
The classification of 2-dimensional topological field theories Z : Cob(2) →Vectk
requires that one show S1 has the structures of commutative Frobenius objects in
Cob(2) . This means that one needs to show that the maps (m, 1, m∨, tr) exist, and
that they satisfy the usual commutative Frobenius conditions. This part is easy. The
difficult part is showing that these maps and the commutative Frobenius conditions
are sufficient and necessary. In the language of category theory, one needs to construct
a presentation of the bordism category Cob(2). By a presentation we mean genera-
tors and relations. The generators being (m, 1, m∨, tr), and the relations being the
commutative Frobenius relations. One inevitably has to dig into the Morse theory of
2-dimensional manifolds to show, among other things, that two different ways of glu-
ing the generators into the same cobordism [M] must be related by only commutative
Frobenius relations. This is most naturally proven using Cerf theory: the two different
gluings correspond to Morse functions f0, f1 : M →R, and [Cer70] showed that there is
a path of functions ft from f0 to f1 such that along this path the function ft only fails
to be “excellent Morse” at finitely many times. In particular, before and after those
singularities, the Morse functions induce a commutative Frobenius type of relations.
We will essentially take a similar approach to understand the algebraic structures
of S2. In order to do so, we need to consider all possible bordisms between disjoint
unions of S2. These span a subcategory Cob(3)S2 of Cob(3), defined as
Definition 1.0.4. Consider the symmetric monoidal category Cob(3). It has a sub-
category whose objects are disjoint unions of S2. Call this category Cob(3)S2 and note
that it inherits the symmetric monoidal structure.
In particular, the morphisms in Cob(3)S2 all have spherical boundaries. For exam-
ple, here’s a list of morphisms that will play a central role in defining the presentations
of Cob(3)S2:
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
p×× = [p \ int(D3 ⊔D3)] : S2 →S2
p× = [p \ int(D3)] : ∅→S2
where p is any diffeomorphism class of connected closed oriented irreducible 3-manifold.
Note that the only 3-manifold which is prime but reducible is S2 ×S1. So,equivalently,
p is any diffeomorphism class of connected closed oriented prime 3-manifold which is
not S2 × S1. See figure 1.2 for a sketch of these morphisms.
p××
p×
Figure 1.2: A list of generating morphisms.
From left to right: idS2, multiplication m,
unit 1, comultiplication m∨, trace tr, prime endomorphism p××, prime unit p×, one for
each connected oriented irreducible prime 3-manifold p. All but the last kind make up the
generating set G2. All but the second to last kind make up the generating set G1.
Our aim is to construct presentations of Cob(3)S2. It turns out that Cob(3)S2 has
two sets of generators:
G1 = C ∪F ∪L ∪orientation reversal
G2 = C ∪F ∪P ∪orientation reversal
where C = {1, m} , F = {tr, m∨} , P = {p××}p∈I , L = {p×}p∈I. Here I denotes the
set {connected closed irreducible 3-manifold} /orientation-preserving diffeomorphisms
.
The presentation using G1 generators is usually associated with the letter “L” be-
cause of the distinct L-shaped prime factor attachments in figure 2.2. The presentation
using G2 generators is usually associated with the letter “P” for “prime” due to a lack
of imagination.
The G2 presentation is given by the usual commutative Frobenius relations, as well
as the “legs relations” suggestively sketched in figure 1.3
m ◦(p×× ⊗idS2) = m ◦(idS2 ⊗p××).
P ××
P ××
∼=
Figure 1.3: The “legs relations” for the G2 presentation of Cob(3)S2.
The legs relations are not trivially implied by commutativity because our boundaries
are ordered. To see this, consider passing through a TFT Z, then both sides of the
legs relations are maps from Z(S2) ⊗Z(S2) to Z(S2). The left hand side sends the
element a ⊗b to Z(p××)(a) · b, while the right hand side sends it to a · Z(p××)(b).
We prove in theorem 4.4.13 that
Theorem 1.0.5. Cob(3)S2 has a presentation with G2 generators under commutative
Frobenius relations and legs relations. These relations are necessary.
The G1 presentation is given by the usual commutative Frobenius relations only.
We prove in theorem 4.3.2 that
Theorem 1.0.6. Cob(3)S2 has a presentation with G1 generators and commutative
Frobenius relations.
What is perhaps surprising about the theorems is that the relations are extremely
simple, even though the topology of 3-manifolds are significantly more complicated
than the topology of 2-manifolds. In Cob(2) , a morphism is a 2-manifold with bound-
aries. The classification of 2-manifolds shows that up to diffeomorphisms the manifold
is classified by its genus. The classification of 3-manifolds is more complicated but
standard– the theorem of Kneser-Milnor prime decomposition will play a repeated
central role in our proof:
Theorem 1.0.7. (Kneser-Milnor Prime Decomposition Theorem)
Let M be a compact, connected and orientable 3-manifold. Then there is a decom-
position
M = P1#P2# . . . #Pm.
where each Pi is prime. This decomposition is unique up to insertion or deletion of
S3’s.
A connected 3-manifold X is prime if X = P#Q implies either P = S3 or Q = S3.
The # denotes the connect sum operation– one deletes a 3-ball from both P and Q
and then glues them together along the sphere boundary. Meaning that one can always
view M = M1#M2 as M ∼= (M1 \ int(D3)) ∪S2 (M2 \ int(D3)).
Notice that we can use the prime decomposition theorem to “chop up” a bordism
M : ⊔nincS2 →⊔noutS2 into prime factors. This is the idea behind the generators G1
and G2, which correspond to two different choices of chopping.
To show that G1 and G2 with appropriate relations are presentations of the category
Cob(3)S2, we first consider the non-prime part–if one forgets about the prime factors
in P ⊂G2 and L ⊂G1 for a moment and only considers the CF generators, then we
are working with the category Cob(3)S2,CF whose objects are disjoint unions of spheres
like before, but whose morphisms are bordisms that are generated by CF generators.
We prove in theorem 3.3.6 that
Theorem 1.0.8. There is a canonical isomorphism S : Cob(2) ∼
→Cob(3)S2,CF
The isomorphism S sends n-copies of S1 to n-copies of S2, and sends the multi-
plication map of S1 to the multiplication map of S2. Same goes for unit, trace, and
co-multiplication. On more complicated bordisms, S sends a genus g bordism to a bor-
dism with g-many S2 × S1 connect sum factors. This theorem essentially shows that
the commutative Frobenius part of Cob(S2) is completely determined by Cob(2). In
particular, the commutative Frobenius relations of G1 and G2 generators are necessary.
The Cerf theory we build through geometry can be roughly summarized as follows:
every composition in Cob(3)S2 is induced by some decomposition, which is induced by
some Morse data. Two different compositions of the same morphism are induced by
two different Morse data on the same underlying manifold. Let’s denote the two Morse
functions as f0, f1 : M →R. We show that there exists a sequence of relations which
can put a composition into a “normal form” using only prime relations.
A prime relation is a pair of Morse functions which can and will be connected by a
path of functions with more than 1 singularities where the function fails to be excellent
Morse, unlike commutative Frobenius relations, each of which is a single specific type
of singularity.
Call the Morse functions inducing these normal-form compositions f′
0, f′
1. We then
show the resulting normal-form compositions are related by commutative Frobenius
relations only. This means that one can construct a path from f0 to f1 consisting of 3
distinct segments:
1. Segment 1: from f0 to f′
0, which induces the change from the starting composition
to the normal-form composition.
Since we will use only prime relations, the
Morse functions inducing the individual intermediate compositions are separated
by more than one singularity.
2. Segment 2: from f′
0 to f′
1, which has only commutative Frobenius type singulari-
ties.
3. Segment 3: from f′
1 to f1. This is the reverse of segment 1 but for the other
composition.
A generic figure depicting this process can be found in 1.4.
f0
f ′
0
f ′
1
f1
Figure 1.4: A path from f0 to f1 using 3 prime relations, then 2 commutative Frobenius
relations, then 2 prime relations. Note that each black dot is a Morse data which induces
some composition. The prime relations is a pair of Morse data separated by more than 1
singularities, while a commutative Frobenius relation is always given by a single specific kind
of singularity.
Passing through a TFT, the two presentations of Cob(3)S2 give rise to two kinds of
structures called P-algebras and L-algebras. Since they are both induced by Cob(3)S2,
it is unsurprising when we show in lemma 5.1.2 that there is a bijection between P-
algebras and L-algebras. So it makes sense to refer to them as a single kind of structure:
Definition 1.0.9. Let A be a commutative Frobenius algebra over k. Then A is an
L-algebra (equiv. P-algebra) if there are elements 1p ∈A (equiv. endomorphisms ep :
A →A that acts by multiplication by 1p) for every diffeomorphism class of connected
oriented irreducible 3-manifold p.
The remarkable feature of L and P algebras is their simplicity. We are supposed to
think of such an algebra as Z(S2) for some 3d TFT Z : Cob(3) →Vectk. Even though
the bordisms of S2 are very complicated, geometry forces G1 and G2 presentations to
be extremely simple, which in turn forces the prime structures of L and P algebras to
be also extremely simple.
Relative to existing literature on 3-dimensional TFTs, our results sit somewhat
“diagonally.”
[Juh18] showed that there is a bijection between the category of 3-
dimensional TFTs and the category of J-algebras. The J-algebra associated to a TFT
Z is a g ≥0 graded algebra ⊕gAg, with maps that encode geometric operations such
as the attachment of 1 and 2 handles. Z(S2) is the genus 0 part A0 of the J-algebra
assigned to Z. However J-algebras do not answer the question we are addressing in
this paper.
For example, a J-algebra A = ⊕gAg carries with it a “1-handle map”
A0 →A1, which corresponds to the Morse bordism of attaching a 1-handle to a two-
sphere, increasing the genus by 1. What we need to classify is all possible maps from
A0 to A0, or to A0 ⊗A0, or to A0 ⊗A0 ⊗A0, etc, which factors through products
of A0’s exclusively. The domain of these maps can also have multiple factors of A0.
From a physics point of view, while it is useful to understand maps from the space of
local operators/states A0 to whatever Ag>0 means in the particular contexts, it is more
surprising to learn that the space of local operators/states of a 3-dimensional TFT is
a finite dimensional commutative Frobenius algebra. Our work on the presentations
of Cob(3)S2 and on L/P algebras says that the degree 0 part of a J-algebra carries
additional simple structures labelled by connected oriented irreducible 3-manifolds.
In the context of modern (∞, n)-perspectives of fully-extended topological field
theories, it is less clear what kind of structure must replace our L/P algebras besides
tautology. For example, while S1 is a commutative Frobenius object in Cob(2), S1 is an
E2-algebra in Bordfr
2
the (∞, 2)-category of framed bordisms. This only captures the
operadic structure of S1, rather than the whole PROP (products and permutations).
The full PROP is, tautologically, the subcategory of Bordfr
2 spanned by disjoint unions
of S1. It is widely known that Sn−1 is at least an En-algebra in Bordfr
n , but obviously
there is more operadic structure in dimension n ≥3.
We propose an ∞-operad L⊗in definition 5.3.11 and 5.3.13 which we conjecture
to be isomorphic to the connected part of the full ∞-endomorphism operad of S2. An
n-ary operation is, roughly speaking, a bordism from n-many S2 to a single S2, where
the bordism is itself a connected 3-manifold. This is achieved by first specifying a
collection of irreducible manifolds Pi, then specifying how to glue them together into a
single bordism using some connect-sum configuration data. Adding to the plausibility,
the E3 operad sits nicely inside L⊗as a suboperad. The construction is inspired by the
unfinished draft of [Hat08], which just recently was completed by [BBS26] in almost
all cases except, unfortunately, for bordisms with spherical boundaries.
Organization Roadmap
In Chapter 2, we introduce the generators G1 and G2 of Cob(3)S2 and show in propo-
sition 2.0.7 that they generate all the morphisms.
Chapter 3 and chapter 4 are dedicated to showing that commutative Frobenius
relations are necessary and sufficient for the G1 presentation, and additionally the legs
relations are necessary for the G2 presentation. To achieve this, we first outline the
basic strategy in section 3.1.
We then first address the commutative Frobenius relations between the shared CF
generators of G1 and G2 in chapter 3. This is done in stages: we first show existence
in proposition 3.2.2 in section 3.2 by analyzing the generic Cerf theory arguments. We
then show in theorem 3.3.6 in section 3.3 that there is an isomorphism between Cob(2)
and Cob(3)S2,CF . We then setup some machinery in section 3.4 so we can prove in
section 3.5 that 3.5.4 CF generators satisfy no more relations.
We then address the new relations that arise from the prime-labelled generators
in chapter 4.
This is also done in stages: first we show that CF generators exists
exclusively outside prime factors, a phenomena we call “no internal relations.” This is
the topic of section 4.1. We then immediately introduce the prime relations in section
4.2: prime commutativity 4.2.1, legs and waist relations for G2 4.2.3, and legs relations
for G1 4.2.7. In section 4.3 we prove in theorem 4.3.1 and 4.3.2 that these relations are
sufficient to give presentations of Cob(3)S2. However, some relations are not necessary.
We show in section 4.4 that, besides the commutative Frobenius relations, only the
legs relations for G2 are necessary– all other relations are implied by commutative
Frobenius relations and the legs relations. This is explained in propositions 4.4.6 to
4.4.10. Therefore we prove in theorem 4.4.13 that commutative Frobenius relations
and legs relations are necessary and sufficient to form a presentation of Cob(3).
Chapter 5 is dedicated to the consequences of realizing Cob(3)S2 as presentations
after passing through 3-dimensional topological field theories. In section 5.1 we de-
fine the notion of an L algebra, or equivalently a P algebra, in definition 5.1.8. We
also explain some immediate consequences and properties afforded by L algebras. We
examine in section 5.2 the relations between L algebras and J-algebras which classify
2 + 1-dimensional TFTs. We show that the degree 0 part of every J- algebra is an
L-algebra in theorem 5.2.3, and provide a specific recipe in proposition 5.2.8 to recover
all the prime endomorphisms and prime units using Heegaard splitting. Lastly in sec-
tion 5.3, we define an ∞-operad L⊗in definition 5.3.11 and 5.3.13, which has E⊗
3 as a
suboperad. We conjecture in 5.3.32 and 5.3.33 that L⊗is isomorphic to the connected
part of the ∞-endomorphism operad of S2 in Bordfr
3
or BordSO
3 .
Chapter 2
