---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-003-outline-of-strategy
section_title: "Outline of Strategy"
section_number: null
pages: 22-26
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Definition 3.1.1.LetMbe a compact oriented connected 3 manifold with boundary
X− andX + of codimension 1. Aprime Morse datumis a pairf:M→Rand an
ordered tupleb= (b 0<b 1<···<b m)∈R m+1 such that
1.X − =f−1(b0) andX + =f−1(bm) are the sets of minimum resp maximum off.
2.b i are regular values offsuch that any connected componentC⊂f −1(bi−1,bi)
is diffeomorphic toD 3,S 2×I,S 3\int(⊔ 3D3), orp\int(D 3⊔D 3) wherepis an
oriented irreducible 3-manifold.
Cis called anelementary bordismifCis diffeomorphic toD 3 orS 3\int(⊔ 3D3).Cis
called aprime bordismifCis diffeomorphic top\int(D 3⊔D 3) forp̸ ∼=S2×S 1 oriented
irreducible.CiscylindricalifCis diffeomorphic toS 2×I. Note elementary bordisms
admit Morse datum with only one critical point (the standard Morse function), while
a cylindrical one admits datum with no critical point. Any Morse datum on a prime
bordism must necessarily have more than one critical point.
We frequently suppressbwhen discussing the prime Morse datumf,bif it is clear
from context which prime decomposition it induces.
Definition 3.1.2.Theprime decompositionof a bordismMcompact oriented con-
nected 3 manifold with boundaryX −,X + is a decomposition
M=M 1∪X1M2∪X2···∪ Xm−1Mm.
such thatM i is diffeomorphic to a disjoint union ofD 3,S 2×I,S 3\int(⊔ 3D3), or
p\int(D 3⊔D 3) forp̸ ∼= S2×S 1 oriented irreducible. Additionally we require that
M1∩∂M=X + andM m∩∂M=X −.
Definition 3.1.3.(Prime composition) of a morphism [M] in Cob(3) S2 is a collection
of morphisms [M 1],[M 2],...,[M m] such that
1. each[Mi] is a tensor product of 1,tr,id,m,m ∨, and [p\int(D 3⊔D 3)] forp
oriented irreducible 3-manifold.
22
2. the collection composes to [M] = [M 1]◦[M 2]···◦[M m].
Claim 3.1.4.1. Any prime Morse datumf,bonMinduces a prime decomposition
ofM. each factor isM m−i+1 =f−1(bi−1,bi).
2. Any prime decomposition of a bordismMinduces a prime composition of [M]
such thatM i∈[M i].
3. Any prime decomposition ofMcomes from some prime Morse datum – once
fixed some “standard” Morse functions for eachM i, and glue them together into
a Morse function onM.
4. Any prime composition of a morphism comes from a prime decomposition of a
representative.
General strategies on showing a certain relation is trueSuppose we have
two composition sequences, say one sequence composes to [M] and the other to [M ′],
and we want to show that they are equal. There are two strategies: one at the level of
prime decompositions, one at the level of Morse data.
At the level of prime decompositions, one can show that two chosen representatives
M,M′ of [M] and [M ′] have prime decompositions inducing the corresponding com-
positions, and thatMandM ′ are diffeomorphic. This is convenient when it is easy
to argue thatM ∼= M′. One can alternatively show that that the same manifold has
two prime decompositions, but it is harder– this amounts to explicitly identifying the
gluing surfaces on a fixed manifoldM.
At the level of Morse data, one can start with two Morse functions (or rather, prime
Morse data)f 0,f 1 :M→Ron the same manifold, and show thatf 0,f 1 indeed induce
the appropriate Morse decompositions. This process necessarily factors through the
alternative method at the level of prime decomposition, but is strictly easier, as it gives
explicitly the gluing surfaces which are regular surfaces of the Morse data. Note that if
we want a non-trivial relation,f 0,f 1 must induce non-isomorphic /diffeomorphic prime
decompositions, thus inducing different prime compositions.
The classification of relations take the opposite approach.To classify all
possible relations between generating bordisms is to show that for any two prime com-
positions of the same bordism class [M], one can always turn one composition into
the other using a set of known relations. This means that there exists a sequence of
prime compositions (Ci) such thatC i−1 andC i are the same everywhere except for one
instance of a known relation. Since the two compositions result in the same bordism
class, we may choose the same representativeM. Hence at the level of prime decompo-
sitions, one needs to show that there exists a sequence (Di) of prime decompositions of
Minducing the composition sequence (C i) such thatD i,D i−1 are the same except for
one application of a known decomposition diffeomorphism. At the level of Morse data,
we need a sequence of Morse datum (f i,bi) which induce the prime decompositions
(Di)
Let’s review what this means in Cob(2). LetMbe a compact oriented bordism
andf 0,f 1 :M→Rprime data which induce compositionsC 0,C 1. To show that com-
mutative Frobenius relations are sufficient, one must show that there exists a sequence
(f0,...,f i,...,f 1) such thatf i−1 andf i induces decompositions that are identical ex-
cept related by a diffeomorphism of a certain kind, which in turn induces compositions
that are identical except related by a commutative Frobenius relation. By noticing
23
that Cerf theory provides a path fromf 0 tof 1 which is excellent Morse for all but
finitely many singularities, and that the types of singularities can be shown to induce
commutative Frobenius relations, one chooses a path and let the sequence of Morse
functions be chosen, one for each excellent Morse segment, along which with suitable
choices ofb i the decomposition is unique up to diffeomorphism. One summarizes by
saying “the singularities along the Cerf path exhibit the relations necessary to equate
compositionC 0 toC 1.”
The situation in Cob(3) S2 is markedly different due to the additional prime mor-
phisms, especially at the level of Morse data. First, external prime relations, such
as legs and waist relations, are induced by Morse functions connected by a Cerf path
with multiple singularities. Second, there is no longer a bijection between non-trivial
singularities and commutative Frobenius relations. For example, the 0-1 birth death
does not induce any relations among commutative Frobenius generators.
To show that commutative Frobenius relations between theC={1,m}andF=
{tr,m∨}generators are true, we use the local form of a birth-death singularity to deduce
the straight forward decompositions, hence compositions; we analyse the topological
constraints on the exchanges of critical values and deduce the corresponding decom-
positions, which induce the compositions. To show that these relations are sufficient
among CF generators, we prove in proposition 3.5.2 and proposition 3.5.3 that any
two Morse data inducing CF-generated compositions are connected by a path whose
singularities split the path into segments, each of which is related to its neighbours by
inducing a specific relation among the decompositions. To do so, we invoke the equiv-
alence between the types of singularities and the induced decomposition relations, and
show that only specific types of singularities are present on this path. This culminates
in corollary 3.5.4, which states that there are no more relations between CF generators.
Then we have to deal with the prime bordisms, which have no counterparts in
Cob(2). There are some obvious composition relations coming from prime decompo-
sitions, which can be induced by Morse data closely related to each other. One such
example isprime commutativityintroduced in 4.2.1, which saysp ××
1 ◦p××
2 =p××
2 ◦p××
1 .
If (f,b= 0) is a prime Morse datum inducing a prime decomposition inducing the com-
position on the left hand side, then “flipping the picture upside down,” post-composing
with the mapR→Rsendingx7→−xand keepingb= 0 fixed will induce the compo-
sition on the right hand side. See figure 4.3.
Even though this relation has very simple geometric interpretations, the singularity
types of a path between their Morse functions may be very complicated. Therefore
we conclude that prime relations such as prime commutativity arenotclassified by
singularity types– rather, they are collections of singularities along Cerf paths. This
makes the classification at the Cerf-theoretic level challenging, but we are able to
circumvent it through geometric arguments.
After a brief digression regarding (the lack of)internal relations, we prove thatlegs
and waist relations4.2.3 exist by proving that the prime decompositions, which induces
the compositions under consideration, are decompositions of diffeomorphic manifolds.
At the level of Morse data, the legs relations are trivial, but the story for the waist
relations is similar to that of prime commutativity– paths between the pairs of Morse
functions, which induce the waist relations, will have multiple singularities where the
function fails to be excellent Morse. Therefore two Morse data inducing a waist relation
is connected by a path with more than one singularity.
24
The proof that commutative Frobenius relations, prime relations, and legs and
waist relations together are sufficient can also be viewed at both the level of prime
decompositions and at the level of Morse data. At the level of prime decompositions,
one first show that there are “standard” form prime decompositions which allows one to
isolate the prime morphisms Then we show that the parts generated by CF generators
can be brought from one decomposition to the other using proposition 3.5.3. We may
hold the Morse functions over the prime part constant, and glue with the corresponding
path to get the total path.
We first outline the strategy for this section. Since bothG 1 andG 2 shareCandF
generators, we first prove that these generators satisfy the usual commutative Frobenius
relations like their counterparts in Cob(2), and most importantly that these relations
are necessary and sufficient among morphisms generated byCandF.
More precisely, this means that the graph with

⊔nS2	∼= Z≥0 vertices andC∪F
(and tensor products) as directed edges, together with commutative Frobenius relations
form a presentation A.1.8 of a subcategory of Cob(3) S2. This category is denoted
Cob(3)S2,CF and defined as
Definition 3.1.5.(Cob(3) S2,CF ) LetC={m,1},F={m ∨,tr}be defined as in
2.0.6. Consider the subcategory of Cob(3) S2 whose morphisms are those which admit
a composition in terms ofC∪Fgenerators and their tensor products. Call this category
Cob(3)S2,CF .
Next, we show thatPgenerators inG 2 satisfyprime commutativityin . The more
interesting question is whether the commutative Frobenius generators interact with
the new prime generators in some non-trivial way. We first address that there are
no “internal” commutative Frobenius relations inside a prime generator, and then we
show that there are only a handful of “external” relations each forPand just one for
L. These external relations are called “co/legs and co/waist relations” forPand “legs
relations” forL. Theorem 4.3.1 shows thatG 2, with commutative Frobenius relations,
prime commutativity, co/legs and co/waist relations, form a presentation of Cob(3)S2.
In particular, these relations are sufficient. On the other hand, theorem 4.3.2 shows
thatG 1, with commutative Frobenius relations alone, form a presentation of Cob(3)S2.
The fact that commutative Frobenius relations alone are sufficient for theG 1 pre-
sentation raises the question of whether the same could happen toG 2. This turns out
to be mostly the case, except for the co/legs relations. We present a series of proposi-
tions which shows that prime commutativity and co/waist relations are implied by the
co/legs relations and commutative Frobenius relations, culminating in theorem 4.4.13,
which shows thatG 2, with commutative Frobenius relations and legs relations, form a
presentation of Cob(3)S2. In particular, these relations are necessary.
From a higher perspective, what we aim to achieve in this section is to develop the
Cerf theory of 3 manifolds equipped with a notion of “good” Morse function, but instead
of achieving this goal through the more common Jet-stratification analysis/algebraic
approach, we exploit the isomorphism 3.3.6 between Cob(2) and Cob(3) S2 and prove
purely geometrically that the relations outlined in the previous paragraphsarethe Cerf
theory we promised.
25
