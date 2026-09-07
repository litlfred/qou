---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-25
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
‘Groupoidiﬁcation’ is an attempt to expose the combinatorial under pinnings of
linear algebra—the hard bones of set theory underlying the ﬂexibility of the
continuum. One of the main lessons of modern algebra is to avoid choo sing
bases for vector spaces until you need them. As Hermann Weyl wr ote, “The
introduction of a coordinate system to geometry is an act of violenc e”. But
1
vector spaces often come equipped with a natural basis—and when this happens,
there is no harm in taking advantage of it. The most obvious example is when
our vector space has been deﬁned to consist of formal linear comb inations of
the elements of some set. Then this set is our basis. But surprisingly often,
the elements of this set are isomorphism classes of objects in some groupoid .
This is when groupoidiﬁcation can be useful. It lets us work directly wit h the
groupoid, using tools analogous to those of linear algebra, without b ringing in
the real numbers (or any other ground ﬁeld).
For example, let E be the groupoid of ﬁnite sets and bijections. An isomor-
phism class of ﬁnite sets is just a natural number, so the set of isom orphism
classes of objects in E can be identiﬁed with N. Indeed, this is why natural
numbers were invented in the ﬁrst place: to count ﬁnite sets. The r eal vector
space with N as basis is usually identiﬁed with the polynomial algebra R[z],
since that has basis z0,z 1,z 2,.... Alternatively, we can work with inﬁnite for-
mal linear combinations of natural numbers, which form the algebra of formal
power series, R[[z]]. So, the vector space of formal power series is a kind of
stand-in for the groupoid of ﬁnite sets.
Indeed, formal power series have long been used as ‘generating fu nctions’
in combinatorics [46]. Given any combinatorial structure we can put o n ﬁnite
sets, its generating function is the formal power series whose nth coeﬃcient says
how many ways we can put this structure on an n-element set. Andr´ e Joyal
formalized the idea of ‘a structure we can put on ﬁnite sets’ in terms of esp` eces
de structures , or ‘structure types’ [6, 22, 23]. Later his work was generalized to
‘stuﬀ types’ [4], which are a key example of groupoidiﬁcation.
Heuristically, a stuﬀ type is a way of equipping ﬁnite sets with a speciﬁc type
of extra stuﬀ—for example a 2-coloring, or a linear ordering, or an a dditional
ﬁnite set. Stuﬀ types have generating functions, which are forma l power series.
Combinatorially interesting operations on stuﬀ types correspond t o interesting
operations on their generating functions: addition, multiplication, d iﬀerentia-
tion, and so on. Joyal’s great idea amounts to this: work directly with stuﬀ types
as much as possible, and put oﬀ taking their generating funct ions. As we shall
see, this is an example of groupoidiﬁcation.
To see how this works, we should be more precise. A stuﬀ type is a groupoid
over the groupoid of ﬁnite sets: that is, a groupoid Ψ equipped with a functor
v : Ψ → E. The reason for the funny name is that we can think of Ψ as a
groupoid of ﬁnite sets ‘equipped with extra stuﬀ’. The functor v is then the
‘forgetful functor’ that forgets this extra stuﬀ and gives the u nderlying set.
The generating function of a stuﬀ type v : Ψ →E is the formal power series
Ψ
~
(z) =
∞∑
n=0
|v−1(n)|zn. (1)
Here v−1(n) is the ‘full inverse image’ of any n-element set, say n ∈ E. We
deﬁne this term later, but the idea is straightforward: v−1(n) is the groupoid
of n-element sets equipped with the given type of stuﬀ. The nth coeﬃcient of
the generating function measures the size of this groupoid.
2
But how? Here we need the concept of groupoid cardinality. It seems this
concept ﬁrst appeared in algebraic geometry [5, 28]. We rediscover ed it by
pondering the meaning of division [4]. Addition of natural numbers com es from
disjoint union of ﬁnite sets, since
|S +T | = |S| + |T |.
Multiplication comes from cartesian product:
|S ×T | = |S| × |T |.
But what about division?
If a group G acts on a set S, we can ‘divide’ the set by the group and form
the quotient S/G. If S and G are ﬁnite and G acts freely on S, S/G really
deserves the name ‘quotient’, since then
|S/G| = |S|/|G|.
Indeed, this fact captures some of our naive intuitions about divisio n. For
example, why is 6 /2 = 3? We can take a 6-element set S with a free action of
the group G = Z/2 and construct the set of orbits S/G:
Since we are ‘folding the 6-element set in half’, we get |S/G| = 3.
The trouble starts when the action of G on S fails to be free. Let’s try the
same trick starting with a 5-element set:
We don’t obtain a set with 2 1
2 elements! The reason is that the point in the
middle gets mapped to itself. To get the desired cardinality 2 1
2 , we would need
a way to count this point as ‘folded in half’.
To do this, we should ﬁrst replace the ordinary quotient S/G by the ‘action
groupoid’ or weak quotient S//G. This is the groupoid where objects are
elements of S, and a morphism from s ∈S to s′ ∈S is an element g ∈G with
gs =s′. Composition of morphisms works in the obvious way. Next, we should
deﬁne the ‘cardinality’ of a groupoid as follows. For each isomorphism class of
objects, pick a representative x and compute the reciprocal of the number of
3
automorphisms of this object; then sum the result over isomorphis m classes. In
other words, deﬁne the cardinality of a groupoid X to be
|X| =
∑
isomorphism classes of objects [x]
1
|Aut(x)| . (2)
With these deﬁnitions, our problematic example gives a groupoid S//G with
cardinality 2 1
2 , since the point in the middle of the picture gets counted as ‘half
a point’. In fact,
|S//G| = |S|/|G|
wheneverG is a ﬁnite group acting on a ﬁnite set S.
The concept of groupoid cardinality gives an elegant deﬁnition of the generat-
ing function of a stuﬀ type—Equation 1—which matches the usual ‘ex ponential
generating function’ from combinatorics. For the details of how th is works, see
Example 11.
Even better, we can vastly generalize the notion of generating fun ction, by
replacing E with an arbitrary groupoid. For any groupoid X we get a vector
space: namely RX , the space of functions ψ : X → R, where X is the set of
isomorphism classes of objects in X. Any suﬃciently nice groupoid over X
gives a vector in this vector space.
The question then arises: what about linear operators? Here it is go od to
take a lesson from Heisenberg’s matrix mechanics. In his early work o n quantum
mechanics, Heisenberg did not know about matrices. He reinvented them based
on this idea: a matrix S can describe a quantum process by letting the matrix
entry Sj
i ∈ C stand for the ‘amplitude’ for a system to undergo a transition
from its ith state to its jth state.
The meaning of complex amplitudes was somewhat mysterious—and ind eed
it remains so, much as we have become accustomed to it. However, t he mystery
evaporates if we have a matrix whose entries are natural numbers . Then the
matrix entrySj
i ∈ N simply counts the number of ways for the system to undergo
a transition from its ith state to its jth state.
Indeed, let X be a set whose elements are possible ‘initial states’ for some
system, and let Y be a set whose elements are possible ‘ﬁnal states’. Suppose
S is a set equipped with maps to X and Y :
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
Mathematically, we call this setup a span of sets. Physically, we can t hink of S
as a set of possible ‘events’. Points in S sitting over i ∈ X and j ∈ Y form a
subset
Sj
i = {s : q(s) = j, p(s) = i}.
We can think of this as the set of ways for the system to undergo a transition
from its ith state to its jth state. Indeed, we can picture S more vividly as a
4
matrix of sets:
q p
XY
S
If all the sets Sj
i are ﬁnite, we get a matrix of natural numbers |Sj
i |.
Of course, matrices of natural numbers only allow us to do a limited po rtion
of linear algebra. We can go further if we consider, not spans of set s, but spans
of groupoids. We can picture one of these roughly as follows:
q p
XY
S
If a span of groupoids is suﬃciently nice—our technical term will be ‘ta me’—we
can convert it into a linear operator from RX to RY . Viewed as a matrix, this
operator will have nonnegative real matrix entries. So, we have no t succeeded
in ‘groupoidifying’ full-ﬂedged quantum mechanics, where the matric es can be
complex. Still, we have made some progress.
As a sign of this, it turns out that any groupoid X gives not just a vector
space RX , but a real Hilbert space L2(X). If X = E, the complexiﬁcation of
this Hilbert space is the Hilbert space of the quantum harmonic oscillat or. The
quantum harmonic oscillator is the simplest system where we can see t he usual
tools of quantum ﬁeld theory at work: for example, Feynman diagra ms. It turns
out that large portions of the theory of Feynman diagrams can be d one with
spans of groupoids replacing operators [4]. The combinatorics of th ese diagrams
then becomes vivid, stripped bare of the trappings of analysis. We s ketch how
5
this works in Section 4.1. A more detailed treatment can be found in th e work
of Jeﬀrey Morton [33].
To get complex numbers into the game, Morton generalizes groupoid s to
‘groupoids over U(1)’: that is, groupoids X equipped with functors v : X →
U(1), where U(1) is the groupoid with unit complex numbers as objec ts and only
identity morphisms. The cardinality of a groupoid over U(1) can be co mplex.
Other generalizations of groupoid cardinality are also interesting. F or exam-
ple, Leinster has generalized it to categories [29]. The cardinality of a category
can be negative! More recently, Weinstein has generalized the conc ept of car-
dinality to Lie groupoids [45]. Getting a useful generalization of group oids for
which the cardinality is naturally complex, without putting in the comple x num-
bers ‘by hand’, remains an elusive goal. However, the work of Fiore an d Leinster
suggests that it is possible [13].
In the last few years James Dolan, Todd Trimble and the authors hav e
applied groupoidiﬁcation to better understand the process of ‘ q-deformation’
[2]. Many important algebraic structures can be systematically defo rmed in
a way that depends on a parameter q, with q = 1 being the ‘default’ case
of no deformation at all. A beautiful story has begun to emerge in wh ich q-
deformation arises naturally from replacing the groupoid of pointed ﬁnite sets by
the groupoid of ﬁnite-dimensional vector spaces over the ﬁeld with q elements,
Fq, where q is a prime power. We hope to write up this material and develop it
further in the years to come. This paper is just a ﬁrst installment.
For example, any Dynkin diagram with n dots gives rise to a ﬁnite group of
linear transformations of Rn which is generated by reﬂections, one for each dot
of the Dynkin diagram, which satisfy some relations, one for each ed ge. These
groups are called ‘Coxeter groups’ [20]. The simplest example is the sy mmetry
group of the regular n-simplex, which arises from a Dynkin diagram with n dots
in a row, like this:
• • •
This group is generated by n reﬂections sd, one for each dot d. These generators
obey the Yang–Baxter equation:
sdsd′sd =sd′sdsd′
when the dots d andd′ are connected by an edge, and they commute otherwise.
Indeed the symmetry group of the regular n-simplex is just the symmetric group
Sn+1, which acts as permutations of the vertices, and the generator sd is the
transposition that switches the dth and (d + 1)st vertices.
Coxeter groups are a rich and fascinating subject, and part of th eir charm
comes from the fact that the group algebra of any Coxeter group admits a q-
deformation, called a ‘Hecke algebra’, which has many of the propert ies of the
original group (as expressed through its group algebra). The Hec ke algebra again
has one generator for each dot of the Dynkin diagram, now called σd. These
generators obey the same relation for each edge that we had in the original
Coxeter group. The only diﬀerence is that while the Coxeter group g enerators
6
are reﬂections, and thus satisfy s2
d = 1, the Hecke algebra generators obey a
q-deformed version of this equation:
σ2
d = (q − 1)σd +q.
Where do Hecke algebras come from? They arise in a number of ways,
but one enlightening description involves the theory of ‘buildings’, whe re each
Dynkin diagram corresponds to a type of geometry [10, 15]. For ex ample, the
Dynkin diagram shown above (with n dots) corresponds to the geometry of
projective n-space. Projective n-space makes sense over any ﬁeld, and when
q is a prime power, the Hecke algebra arises in the study of n-dimensional
projective space over the ﬁeld Fq. We shall explain this in detail in the case of
the projective plane. But the n-simplex can be thought of as a ‘ q → 1 limit’ of
ann-dimensional projective space over Fq. The idea is that the vertices, edges,
triangles, and so on of the n-simplex play the role of points, lines, planes, and
so on in a degenerate sort of projective space. In this limiting case, the Hecke
algebra reduces to the group algebra of the symmetric group. As it turns out,
this fact can be understood more clearly when we groupoidify the Hecke algebra.
We shall sketch the idea in this paper, and give more details in the next paper
of this series. In the meantime, see [18].
Any Dynkin diagram also gives a geometry over the ﬁeld C, and the symme-
tries of this geometry form a simple Lie group. The symmetry transf ormations
close to the identity are described by the Lie algebra g of this group—or equally
well, by the universal enveloping algebra U g, which is a Hopf algebra. This
universal enveloping algebra admits a q-deformation, a Hopf algebra Uqg known
as a ‘quantum group’. There has been a lot of work attempting to cat egorify
quantum groups, from the early ideas of Crane and Frenkel [11], to the work of
Khovanov, Lauda and Rouqier [26, 27, 37], and beyond.
Here we sketch how to groupoidify, not the whole quantum group, b ut only
its ‘positive part’U +
q g. When q = 1, this positive part is just the universal en-
veloping algebra of a chosen maximal nilpotent subalgebra of g. The advantage
of restricting attention to the positive part is that U +
q g has a basis in which the
formula for the product involves only nonnegative real numbers—and any such
number is the cardinality of some groupoid.
The strategy for groupoidifying U +
q g is implicit in Ringel’s work on Hall alge-
bras [34]. Suppose we have a ‘simply-laced’ Dynkin diagram, meaning on e where
two generators of the Coxeter group obey the Yang-Baxter equ ation whenever
the corresponding dots are connected by an edge. If we pick a dire ction for each
edge of this Dynkin diagram, we obtain a directed graph. This in turn f reely
generates a category, say Q. The objects in this category are the dots of the
Dynkin diagram, while the morphisms are paths built from directed edg es.
For any prime power q, there is a category Rep( Q) whose objects are ‘rep-
resentations’ ofQ: that is, functors
R : Q → FinVectq,
where FinVectq is the category of ﬁnite-dimensional vector spaces over Fq. The
morphisms in Rep( Q) are natural transformations. Thanks to the work of
7
Ringel, one can see that the underlying groupoid of Rep( Q)—which has only
natural isomorphisms as morphisms—groupoidiﬁes the vector space U +
q g. Even
better, we can groupoidify the product in U +
q g. The same sort of construction
with the category of pointed ﬁnite sets replacing FinVect q lets us handle the
q = 1 case [43]. So yet again, q-deformation is related to the passage from
pointed ﬁnite sets to ﬁnite-dimensional vector spaces over ﬁnite ﬁ elds.
The plan of the paper is as follows. In Section 2, we present some bas ic
facts about ‘degroupoidiﬁcation’. We describe a process that asso ciates to any
groupoid X the vector space RX consisting of real-valued functions on the set
of isomorphism classes of objects of X, and associates to any ‘tame’ span of
groupoids a linear operator. In Section 3, we describe a slightly diﬀer ent pro-
cess, which associates to X the vector space R[X] consisting of formal linear
combinations of isomorphism classes of objects of X. Then we turn to some
applications. Section 4.1 describes how to groupoidify the theory of Feynman
diagrams, Section 4.2 describes how to groupoidify the theory of He cke alge-
bras, and Section 4.3 describes how to groupoidify Hall algebras. In Section 5
we prove that degroupoidifying a tame span gives a well-deﬁned linear operator.
We also give an explicit criterion for when a span of groupoids is tame, a nd an
explicit formula for the operator coming from a tame span. Section 6 proves
many other results stated earlier in the paper. Appendix A provides some basic
deﬁnitions and useful lemmas regarding groupoids and spans of gro upoids. The
goal is to make it easy for readers to try their own hand at groupoid iﬁcation.
2 Degroupoidiﬁcation
In this section we describe a systematic process for turning group oids into vector
spaces and tame spans into linear operators. This process, ‘degro upoidiﬁcation’,
is in fact a kind of functor. ‘Groupoidiﬁcation’ is the attempt to undo this func-
tor. To ‘groupoidify’ a piece of linear algebra means to take some str ucture built
from vector spaces and linear operators and try to ﬁnd interestin g groupoids and
spans that degroupoidify to give this structure. So, to understa nd groupoidiﬁ-
cation, we need to master degroupoidiﬁcation.
We begin by describing how to turn a groupoid into a vector space. In what
follows, all our groupoids will be essentially small . This means that they have
a set of isomorphism classes of objects, not a proper class. We also assu me our
groupoids are locally ﬁnite : given any pair of objects, the set of morphisms
from one object to the other is ﬁnite.
Deﬁnition 1. Given a groupoid X, let X be the set of isomorphism classes of
objects of X.
Deﬁnition 2. Given a groupoid X, let the degroupoidiﬁcation of X be the
vector space
RX = {Ψ : X → R}.
A nice example is the groupoid of ﬁnite sets and bijections:
8
Example 3. LetE be the groupoid of ﬁnite sets and bijections. Then E ∼= N,
so
RE ∼= {ψ : N → R} ∼= R[[z]],
where the formal power series associated to a function ψ : N → R is given by:
∑
n∈N
ψ(n)zn.
A suﬃciently nice groupoid over a groupoid X will give a vector in RX . To
construct this, we use the concept of groupoid cardinality:
Deﬁnition 4. The cardinality of a groupoid X is
|X| =
∑
[x]∈X
1
|Aut(x)|
where |Aut(x)| is the cardinality of the automorphism group of an object x in
X. If this sum diverges, we say |X| = ∞.
The cardinality of a groupoid X is a well-deﬁned nonnegative rational num-
ber whenever X and all the automorphism groups of objects in X are ﬁnite.
More generally, we say:
Deﬁnition 5. A groupoid X is tame if it is essentially small, locally ﬁnite,
and |X|< ∞.
We show in Lemma 62 that given equivalent groupoids X and Y , |X| = |Y |.
We give a useful alternative formula for groupoid cardinality in Lemma 33.
The reason we use R rather than Q as our ground ﬁeld is that there are
interesting groupoids whose cardinalities are irrational numbers. T he following
example is fundamental:
Example 6. The groupoid of ﬁnite sets E has cardinality
|E| =
∑
n∈N
1
|Sn| =
∑
n∈N
1
n! = e.
With the concept of groupoid cardinality in hand, we now describe how to
obtain a vector in RX from a suﬃciently nice groupoid over X.
Deﬁnition 7. Given a groupoid X, a groupoid over X is a groupoid Ψ
equipped with a functor v : Ψ →X.
Deﬁnition 8. Given a groupoid over X, say v : Ψ →X, and an object x ∈X,
we deﬁne the full inverse image of x, denoted v−1(x), to be the groupoid
where:
• an object is an object a ∈ Ψ such that v(a) ∼=x;
• a morphism f : a →a′ is any morphism in Ψ froma to a′.
9
Deﬁnition 9. A groupoid over X, say v : Ψ → X, is tame if the groupoid
v−1(x) is tame for all x ∈X.
We sometimes loosely say that Ψ is a tame groupoid over X. When we do this,
we are referring to a functor v : Ψ →X that is tame in the above sense. We do
not mean that Ψ is tame as a groupoid.
Deﬁnition 10. Given a tame groupoid over X, say v : Ψ →X, there is a vector
Ψ
~
∈ RX deﬁned by:
Ψ
~
([x]) = |v−1(x)|.
As discussed in Section 1, the theory of generating functions gives many exam-
ples of this construction. Here is one:
Example 11. Let Ψ be the groupoid of 2-colored ﬁnite sets. An object of Ψ is
a ‘2-colored ﬁnite set’: that is a ﬁnite set S equipped with a function c :S → 2,
where 2 = {0, 1}. A morphism of Ψ is a function between 2-colored ﬁnite sets
preserving the 2-coloring: that is, a commutative diagram of this so rt:
S
c /d33/d33/d68/d68/d68/d68/d68/d68/d68/d68
f /d47/d47S′
c′
/d124/d124/d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121
{0, 1}
There is a forgetful functor v : Ψ →E sending any 2-colored ﬁnite set c : S → 2
to its underlying set S. It is a fun exercise to check that for any n-element set,
sayn for short, the groupoid v−1(n) is equivalent to the weak quotient 2 n//Sn,
where 2 n is the set of functions c : n → 2 and the permutation group Sn acts
on this set in the obvious way. It follows that
Ψ
~
(n) = |v−1(n)| = |2n//Sn| = 2 n/n!
so the corresponding power series is
Ψ
~
=
∑
n∈N
2n
n!zn =e2z ∈ R[[z]].
We call this the generating function of v : Ψ →E, and indeed it is the usual
generating function for 2-colored sets. Note that the n! in the denominator, often
regarded as a convention, arises naturally from the use of groupo id cardinality.
Both addition and scalar multiplication of vectors have groupoidiﬁed a na-
logues. We can add two groupoids Φ, Ψ over X by taking their coproduct, i.e.,
the disjoint union of Φ and Ψ with the obvious map to X:
Φ + Ψ
/d15/d15
X
We then have:
10
Proposition. Given tame groupoids Φ and Ψ over X,
Φ + Ψ
~
= Φ
~
+ Ψ
~
.
Proof. This will appear later as part of Lemma 31, which also considers inﬁnite
sums.
We can also multiply a groupoid over X by a ‘scalar’—that is, a ﬁxed
groupoid. Given a groupoid over X, say v : Φ → X, and a groupoid Λ, the
cartesian product Λ × Ψ becomes a groupoid over X as follows:
Λ × Ψ
vπ 2
/d15/d15
X
where π2 : Λ × Ψ → Ψ is projection onto the second factor. We then have:
Proposition. Given a groupoid Λ and a groupoid Ψ overX, the groupoid Λ ×Ψ
over X satisﬁes
Λ × Ψ
~
= |Λ |Ψ
~
.
Proof. This is proved as Proposition 39.
We have seen how degroupoidiﬁcation turns a groupoid X into a vector space
RX . Degroupoidiﬁcation also turns any suﬃciently nice span of groupoid s into
a linear operator.
Deﬁnition 12. Given groupoids X and Y , a span fromX to Y is a diagram
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
whereS is groupoid and p : S →X and q : S →Y are functors.
To turn a span of groupoids into a linear operator, we need a constr uction
called the ‘weak pullback’. This construction will let us apply a span from X
to Y to a groupoid over X to obtain a groupoid over Y . Then, since a tame
groupoid over X gives a vector in RX , while a tame groupoid over Y gives a
vector in RY , a suﬃciently nice span from X to Y will give a map from RX to
RY . Moreover, this map will be linear.
As a warmup for understanding weak pullbacks for groupoids, we re call ordi-
nary pullbacks for sets, also called ‘ﬁbered products’. The data for constructing
such a pullback is a pair of sets equipped with functions to the same se t:
T
q
/d32/d32/d64/d64/d64/d64/d64/d64/d64 S
p
/d127/d127/d126/d126 /d126/d126 /d126/d126 /d126
X
11
The pullback is the set
P = {(s,t ) ∈S ×T |p(s) = q(t)}
together with the obvious projections πS : P →S andπT :P →T . The pullback
makes this diamond commute:
P
π T
/d126/d126/d126 /d126/d126 /d126/d126 /d126/d126 π S
/d31/d31/d64/d64/d64/d64/d64/d64/d64
T
q
/d32/d32/d64/d64/d64/d64/d64/d64/d64 S
p
/d127/d127/d126/d126 /d126/d126 /d126/d126 /d126
X
and indeed it is the ‘universal solution’ to the problem of ﬁnding such a com-
mutative diamond [30].
To generalize the pullback to groupoids, we need to weaken one cond ition.
The data for constructing a weak pullback is a pair of groupoids equip ped with
functors to the same groupoid:
T
q
/d32/d32/d64/d64/d64/d64/d64/d64/d64 S
p
/d127/d127/d126/d126 /d126/d126 /d126/d126 /d126
X
But now we replace the equation in the deﬁnition of pullback by a speciﬁed
isomorphism. So, we deﬁne the weak pullback P to be the groupoid where an
object is a triple ( s,t,α ) consisting of an object s ∈S, an object t ∈T , and an
isomorphism α : p(s) →q(t) in X. A morphism in P from (s,t,α ) to (s′,t ′,α ′)
consists of a morphism f :s →s′ inS and a morphism g :t →t′ inT such that
the following square commutes:
p(s)
p(f )
/d15/d15
α /d47/d47q(t)
q(g)
/d15/d15
p(s′)
α ′
/d47/d47q(t′)
Note that any set can be regarded as a discrete groupoid: one with only identity
morphisms. For discrete groupoids, the weak pullback reduces to t he ordinary
pullback for sets. Using the weak pullback, we can apply a span from X to Y
to a groupoid over X and get a groupoid over Y . Given a span of groupoids:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
12
and a groupoid over X:
Ψ
v
/d126/d126/d126/d126 /d126 /d126/d126 /d126 /d126
X
we can take the weak pullback, which we call SΨ:
SΨ
π S
/d126/d126/d124/d124/d124/d124/d124/d124/d124/d124 π Ψ
/d33/d33/d66/d66/d66/d66/d66/d66/d66/d66
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d32/d32/d66/d66/d66/d66/d66/d66/d66/d66 Ψ
v
/d125/d125/d124/d124/d124/d124/d124/d124/d124/d124
Y X
and think of SΨ as a groupoid over Y :
SΨ
qπ S
/d125/d125/d124/d124/d124/d124/d124/d124/d124/d124
Y
This process will determine a linear operator from RX to RY if the span S is
suﬃciently nice:
Deﬁnition 13. A span
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
is tame if v : Ψ →X being tame implies that qπS :SΨ →Y is tame.
Theorem. Given a tame span:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
there exists a unique linear operator
S
~
: RX → RY
such that
S
~
Ψ
~
=SΨ
~
whenever Ψ is a tame groupoid over X.
13
Proof. This is Theorem 34.
Theorem 36 provides an explicit criterion for when a span is tame. This
theorem also gives an explicit formula for the the operator corresp onding to a
tame span S fromX toY . If X andY are ﬁnite, then RX has a basis given by
the isomorphism classes [ x] in X, and similarly for RY . With respect to these
bases, the matrix entries of S
~
are given as follows:
S
~
[y][x] =
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)| (3)
where |Aut(x)| is the set cardinality of the automorphism group of x ∈X, and
similarly for |Aut(s)|. Even when X andY are not ﬁnite, we have the following
formula for S
~
applied to ψ ∈ RX :
(S
~
ψ)([y]) =
∑
[x]∈X
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)| ψ([x]). (4)
As with vectors, there are groupoidiﬁed analogues of addition and s calar
multiplication for operators. Given two spans from X to Y :
S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64 T
qT
/d127/d127/d126/d126/d126/d126/d126/d126/d126 pT
/d32/d32/d64/d64/d64/d64/d64/d64/d64
Y X Y X
we can add them as follows. By the universal property of the copro duct we
obtain from the right legs of the above spans a functor from the dis joint union
S +T toX. Similarly, from the left legs of the above spans, we obtain a functor
from S +T to Y . Thus, we obtain a span
S +T
/d124/d124/d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120
/d34/d34/d70/d70/d70/d70/d70/d70/d70/d70
Y X
This addition of spans is compatible with degroupoidiﬁcation:
Proposition. If S and T are tame spans from X to Y , then so is S +T , and
S +T
~
=S
~
+T
~
.
Proof. This is proved as Proposition 37.
We can also multiply a span by a ‘scalar’: that is, a ﬁxed groupoid. Given
a groupoid Λ and a span
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
14
we can multiply them to obtain a span
Λ ×S
qπ 2
/d124/d124/d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 pπ 2
/d34/d34/d70/d70/d70/d70/d70/d70/d70/d70
Y X
Again, we have compatibility with degroupoidiﬁcation:
Proposition. Given a tame groupoid Λ and a tame span
S
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
then Λ ×S is tame and
Λ ×S
~
= |Λ |S
~
.
Proof. This is proved as Proposition 40.
Next we turn to the all-important process of composing spans. This is the
groupoidiﬁed analogue of matrix multiplication. Suppose we have a spa n from
X to Y and a span from Y to Z:
T
qT
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pT
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Z Y X
Then we say these spans are composable. In this case we can form a weak
pullback in the middle:
TS
π T
/d126/d126/d124/d124/d124/d124/d124/d124/d124/d124 π S
/d32/d32/d66/d66/d66/d66/d66/d66/d66/d66
T
qT
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pT
/d32/d32/d66/d66/d66/d66/d66/d66/d66/d66 S
qS
/d126/d126/d124/d124/d124/d124/d124/d124/d124/d124 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Z Y X
which gives a span from X to Z:
TS
qT π T
/d125/d125/d124/d124/d124/d124/d124/d124/d124/d124 pS π S
/d33/d33/d67/d67/d67/d67/d67/d67/d67/d67
Z X
called the composite TS .
15
When all the groupoids involved are discrete, the spans S and T are just
matrices of sets, as explained in Section 1. We urge the reader to ch eck that
in this case, the process of composing spans is really just matrix mult iplication,
with cartesian product of sets taking the place of multiplication of nu mbers,
and disjoint union of sets taking the place of addition:
(TS )k
j =
∐
j∈Y
T k
j ×Sj
i.
So, composing spans of groupoids is a generalization of matrix multiplic ation,
with weak pullback playing the role of summing over the repeated index j in
the formula above.
So, it should not be surprising that degroupoidiﬁcation sends a comp osite
of tame spans to the composite of their corresponding operators :
Proposition. If S and T are composable tame spans:
T
qT
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pT
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Z Y X
then the composite span
TS
qT π T
/d125/d125/d124/d124/d124/d124/d124/d124/d124/d124 pS π S
/d33/d33/d67/d67/d67/d67/d67/d67/d67/d67
Z X
is also tame, and
TS
~
=T
~
S
~
.
Proof. This is proved as Lemma 44.
Besides addition and scalar multiplication, there is an extra operation for
groupoids over a groupoid X, which is the reason groupoidiﬁcation is connected
to quantum mechanics. Namely, we can take their inner product:
Deﬁnition 14. Given groupoids Φ and Ψ overX, we deﬁne the inner product
⟨Φ, Ψ ⟩ to be this weak pullback:
⟨Φ, Ψ ⟩
/d124/d124/d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121
/d34/d34/d69/d69/d69/d69/d69/d69/d69/d69
Φ
/d35/d35/d70/d70/d70/d70/d70/d70/d70/d70/d70 Ψ
/d123/d123/d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120
X
16
Deﬁnition 15. A groupoid Ψ over X is called square-integrable if ⟨Ψ, Ψ ⟩ is
tame. We deﬁne L2(X) to be the subspace of RX consisting of ﬁnite real linear
combinations of vectors Ψ
~
where Ψ is square-integrable.
Note that L2(X) is all of RX when X is ﬁnite. The inner product of
groupoids over X makesL2(X) into a real Hilbert space:
Theorem. Given a groupoid X, there is a unique inner product ⟨·, ·⟩ on the
vector space L2(X) such that
⟨Φ
~
, Ψ
~
⟩ = |⟨Φ, Ψ ⟩|
whenever Φ and Ψ are square-integrable groupoids over X. With this inner
productL2(X) is a real Hilbert space.
Proof. This is proven later as Theorem 45.
We can always complexify L2(X) and obtain a complex Hilbert space. We
work with real coeﬃcients simply to admit that groupoidiﬁcation as de scribed
here does not make essential use of the complex numbers. Morton ’s generaliza-
tion involving groupoids over U(1) is one way to address this issue [33 ].
The inner product of groupoids over X has the properties one would expect:
Proposition. Given a groupoid Λ and square-integrable groupoids Φ , Ψ , and
Ψ ′ over X, we have the following equivalences of groupoids:
1.
⟨Φ, Ψ ⟩ ≃ ⟨Ψ, Φ ⟩.
2.
⟨Φ, Ψ + Ψ ′⟩ ≃ ⟨Φ, Ψ ⟩ + ⟨Φ, Ψ ′⟩.
3.
⟨Φ, Λ × Ψ ⟩ ≃ Λ × ⟨Φ, Ψ ⟩.
Proof. Here equivalence of groupoids is deﬁned in the usual way—see Deﬁnit ion
56. This result is proved below as Proposition 49.
Just as we can deﬁne the adjoint of an operator between Hilbert sp aces, we
can deﬁne the adjoint of a span of groupoids:
Deﬁnition 16. Given a span of groupoids from X to Y :
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
17
its adjoint S† is the following span of groupoids from Y to X:
S
p
/d127/d127/d126 /d126/d126 /d126 /d126/d126 /d126 q
/d31/d31/d63/d63/d63/d63/d63/d63/d63
X Y
We warn the reader that the adjoint of a tame span may not be tame , due
to an asymmetry in the criterion for tameness, Theorem 36. But of course a
span of ﬁnite groupoids is tame, and so is its adjoint. Moreover, we h ave:
Proposition. Given a span
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
and a pair v : Ψ →X,w : Φ →Y of groupoids over X andY , respectively, there
is an equivalence of groupoids
⟨Φ,S Ψ ⟩ ≃ ⟨S†Φ, Ψ ⟩.
Proof. This is proven as Proposition 46.
We say what it means for spans to be ‘equivalent’ in Deﬁnition 61. Equivalent
tame spans give the same linear operator: S ≃ T implies S
~
= T
~
. Spans of
groupoids obey many of the basic laws of linear algebra—up to equivale nce.
For example, we have these familiar properties of adjoints:
Proposition. Given spans
T
qT
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pT
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Z Y Y X
and a groupoid Λ , we have the following equivalences of spans:
1. (TS )† ≃S†T †
2. (S +T )† ≃S† +T †
3. (ΛS)† ≃ ΛS†
Proof. These will follow easily after we show addition and composition of spans
and scalar multiplication are well deﬁned.
In fact, degroupoidiﬁcation is a functor
~
: Span → Vect
where Vect is the category of real vector spaces and linear opera tors, and Span
is a category with
18
• groupoids as objects,
• equivalence classes of tame spans as morphisms,
where composition comes from the method of composing spans we ha ve just
described. We prove this fact in Theorem 41. A deeper approach, w hich we
shall explain elsewhere, is to think of Span as a weak 2-category (i.e., bicategory)
with:
• groupoids as objects,
• tame spans as morphisms,
• isomorphism classes of maps of spans as 2-morphisms
Then degroupoidiﬁcation becomes a functor between weak 2-cate gories:
~
: Span → Vect
where Vect is viewed as a weak 2-category with only identity 2-morph isms. So,
groupoidiﬁcation is not merely a way of replacing linear algebraic struc tures
involving the real numbers with purely combinatorial structures. I t is also a
form of ‘categoriﬁcation’ [3], where we take structures deﬁned in t he category
Vect and ﬁnd analogues that live in the weak 2-category Span.
We could go even further and think of Span as a weak 3-category wit h
• groupoids as objects,
• tame spans as morphisms,
• maps of spans as 2-morphisms,
• maps of maps of spans as 3-morphisms.
However, we have not yet found a use for this further structure .
Lastly we would like to say a few words about tensors and traces. We can
deﬁne the tensor product of groupoids X andY to be their cartesian product
X ×Y , and the tensor product of spans
S
q
/d127/d127/d127/d127/d127 /d127/d127/d127/d127 p
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63 S′
q′
/d126/d126/d125/d125/d125/d125/d125/d125/d125/d125 p′
/d32/d32/d66/d66/d66/d66/d66/d66/d66/d66
Y X Y ′ X ′
to be the span
S ×S′
Y ×Y ′ X ×X ′
q×q′
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
p×p′
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63
19
Deﬁning the tensor product of maps of spans in a similar way, we conj ecture
that Span actually becomes a symmetric monoidal weak 2-category[32]. If this
is true, then degroupoidiﬁcation should be a ‘lax symmetric monoidal f unctor’,
thanks to the natural map
RX ⊗ RY → RX×Y .
The word ‘lax’ refers to the fact that this map is not an isomorphism o f vector
spaces unless either X or Y has ﬁnitely many isomorphism classes of objects.
In the next section we present an alternative approach to degrou poidiﬁcation
that avoids this problem. The idea is simple: instead of working with the vector
space RX consisting of all functions on X, we work with the vector space R[X]
havingX as its basis. Then we have
R[X] ⊗ R[Y ] ∼= R[X ×Y ].
In fact both approaches to groupoidiﬁcation have their own advan tages, and
they are closely related, since
RX ∼= R[X]∗.
Regardless of these nuances, the important thing about the ‘mono idal’ aspect
of degroupoidiﬁcation is that it lets us mimic all the usual manipulations for
tensors with groupoids replacing vector spaces. Physicists call a lin ear map
S : V1 ⊗ · · · ⊗Vm →W1 ⊗ · · · ⊗Wn
a tensor, and denote it by an expression
Sj1···jn
i1···im
with one subscript for each ‘input’ vector space V1,...,V m, and one super-
script for each ‘output’ vector space W1,...,W n. In the traditional approach
to tensors, these indices label bases of the vector spaces in ques tion. Then the
expressionSj1···jn
i1···im stands for an array of numbers: the components of the tensor
S with respect to the chosen bases. This lets us describe various ope rations on
tensors by multiplying such expressions and summing over indices tha t appear
repeatedly, once as a superscript and once as a subscript. In the more modern
‘string diagram’ approach, these indices are simply names of input an d output
wires for a black box labelled S:
i1 i2 i3 i4
j1 j2 j3
S
20
Here we are following physics conventions, where inputs are at the b ottom and
outputs are at the top. In this approach, when an index appears o nce as a
superscript and once as a subscript, it means we attach an output wire of one
black box to an input of another.
The most famous example is matrix multiplication:
(TS )k
i =T k
jSj
i.
Here is the corresponding string diagram:
k
j
i
T
S
Another famous example is the trace of a linear operator S : V → V , which is
the sum of its diagonal entries:
tr(S) = Si
i
As a string diagram, this looks like:
i
i
S
Here the sum is only guaranteed to converge if V is ﬁnite-dimensional, and in-
deed the full collection of tensor operations is deﬁned only for ﬁnite -dimensional
vector spaces.
All these ideas work just as well with spans of groupoids
S
Y1 × · · · ×Yn X1 × · · · ×Xm
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
p
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63
21
taking the place of tensors. The idea is that weak pullback takes the place of
summation over repeated indices . Even better, there is no need to impose any
ﬁniteness or tameness conditions until we degroupoidify.
We have already seen the simplest example: composition of spans via w eak
pullback is a generalization of matrix multiplication. For a trickier one, e mpha-
sized by Urs Schreiber [39], consider the trace of a span:
S
q
/d127/d127/d126 /d126/d126 /d126/d126 /d126/d126 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X X
Here it is a bit hard to see which weak pullback to do! We can get around this
problem using an alternate formula for the trace of a linear map S :V →V :
tr(S) = gjkSj
igik (5)
Heregjk is the tensor corresponding to an arbitrary inner product g : V ⊗V → R.
In the ﬁnite-dimensional case, any such inner product determines an isomor-
phismV ∼=V ∗, so we can interpret the adjoint of g as a linear map ˜g : R →V ⊗V ,
and the tensor for this is customarily written as g with superscripts: gik. Equa-
tion 5 says that the operator
R
˜g
− →V ⊗V
S⊗1
− →V ⊗V
g
− →R
is multiplication by tr( S). We can draw g as a ‘cup’ and ˜g as a ‘cap’, giving
this string diagram:
k
k
j
i
S
Now let us see how to implement this formula for the trace at the grou poid-
iﬁed level, to deﬁne the trace of a span of groupoids. Any groupoid X automat-
ically comes equipped with a span
X
1 X ×X
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
∆
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63
22
where ∆ is the diagonal map and the left-hand arrow is the unique fun ctor
to the terminal groupoid —that is, the groupoid 1 with one object and one
morphism. We can check that at least when X is ﬁnite, degroupoidifying this
span gives an operator
g : RX ⊗ RX → R
φ ⊗ψ ↦→ ⟨φ,ψ ⟩
corresponding to the already described inner product on RX . Similarly, the
span
X
X ×X 1
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
∆
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63
degroupoidiﬁes to give the operator
˜g : R → RX ⊗ RX.
So, to implement Equation 5 at the level of groupoids and deﬁne the t race of
this span:
S
q
/d127/d127/d126 /d126/d126 /d126/d126 /d126/d126 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X X
we should take the composite of these three spans:
S ×X
X ×X X ×X
q×1
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
p×1
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63X
1
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
∆
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63 X
1
∆
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63
The result is a span from 1 to 1, whose apex is a groupoid we deﬁne to b e the
trace tr(S). We leave it as an exercise to check the following basic properties
of the trace:
Proposition. Given a span of groupoids
S
q
/d127/d127/d126 /d126/d126 /d126/d126 /d126/d126 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X X
its trace tr(S) is equivalent to the groupoid for which:
• an object is a pair (s,α ) consisting of an object s ∈ S and a morphism
α : p(s) →q(s);
23
• a morphism from (s,α ) to (s′,α ′) is a morphism f : s →s′ such that
p(s)
p(f )
/d15/d15
α /d47/d47q(s)
q(f )
/d15/d15
p(s′)
α ′
/d47/d47q(s′)
commutes.
Proposition. Given a span of groupoids
S
q
/d127/d127/d126 /d126/d126 /d126/d126 /d126/d126 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X X
whereX is ﬁnite, we have
|tr(S)| = tr(S
~
).
Proposition. Given spans of groupoids
S
qS
/d127/d127/d126 /d126/d126 /d126/d126 /d126/d126 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64 T
qT
/d126/d126/d126 /d126/d126/d126 /d126/d126 /d126 pT
/d32/d32/d64/d64/d64/d64/d64/d64/d64
X X X X
and a groupoid Λ , we have the following equivalences of groupoids:
1. tr(S +T ) ≃ tr(S) + tr(T )
2. tr(Λ ×S) ≃ Λ × tr(S)
Proposition. Given spans of groupoids
T
qT
/d126/d126/d126 /d126/d126 /d126/d126 /d126/d126 pT
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X Y Y X
we have an equivalence of groupoids
tr(ST ) ≃ tr(TS ).
We could go even further generalizing ideas from vector spaces and linear
operators to groupoids and spans, but at this point the reader is p robably hungry
for some concrete applications. For these, proceed directly to Se ction 4. Section
3 can be skipped on ﬁrst reading, since we need it only for the applicat ion to
Hall algebras in Section 4.3.
24
