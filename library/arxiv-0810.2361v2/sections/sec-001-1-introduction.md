---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
In this paper, I will describe an extension of the groupoidiﬁcation program of
Baez and Dolan [2]. Groupoidiﬁcation refers to the program of treat ing parts
of linear algebra as arising from spans of groupoids (categories who se morphisms
are all invertible) by a process of “degroupoidiﬁcation”, which prod uces complex
vector spaces associated to groupoids, and linear maps associate d to spans. The
extension described here shows a connection of the setting of gro upoids and spans
with 2-vector spaces and 2-linear maps, a categorical analog of line ar algebra. (We
will assume that all groupoids are essentially ﬁnite - that is, equivalen t to ﬁnite
groupoids - although there is work in progress on how to extend the se results to
inﬁnite groupoids, and in particular Lie groupoids.)
A simple example of the groupoidiﬁcation program can be seen in terms of
spans of ﬁnite sets (i.e. ﬁnite trivial groupoids). In that program, groupoids give
corresponding vector spaces and spans of groupoids give corres ponding linear maps.
In particular, the special case of trivial groupoids (equivalently, s ets) gives a useful
illustration. Given a ﬁnite set S, there is a ﬁnite dimensional vector space L(S)
consisting of all complex linear combinations of elements of S. Now, consider a
span in FinSet: that is, a diagram of the form:
(1) X
s
/d126/d126/d126 /d126 /d126 /d126 /d126 /d126 /d126 t
/d32/d32/d64/d64/d64/d64/d64/d64/d64
Y Z
To the span, there is a corresponding to a linear map L(X) : L(Y ) → L(Z),
represented by a matrix T whose ( i, j)-component is|(s, t)−1(yi, zj)
So the set in Figure 1 gives rise to the linear transformation:
y1↦→z1
y2↦→z1 + z2(2)
y3↦→z2
1
2 JEFFREY C. MORTON
Figure 1. A Span of Sets
This makes sense for spans of ﬁnite sets. Similarly, we will be consider ing an
analogous construction for spans of essentially ﬁnite groupoids.
There is a physical motivation here in quantum mechanics. If Y is the (discrete)
set of classical (pure) states of a system, then L(Y ) = C[Y ], the space of linear
combinations of states in Y , is the Hilbert space of the corresponding quantum
mechanical system. (More generally, if Y is a measure space, one takes L2(Y )). In
the span, we think of X as a set of “processes” x, each with a designated “source”
or starting state s(x)∈ Y and “target” or ending state t(x)∈ Z. Then the linear
transformation described by the matrix T can be seen in the following way, which
we shall generalize later on:
Given a linear combination of elements of Y (that is, a function f : Y → C),
transport f to X by “pulling back” along s. That is, s∗f (x) = f (s(x)). Then
“push forward” to Z by taking the sum over all elements of X mapping down to a
chosen one in Z:
(3) t∗s∗f (z) =
∑
t(x)=z
s∗f (x)
This precisely gives matrix multiplication by the matrix described above , and can
clearly also be seen as a “sum over histories”: the value of t∗s∗f (z) is a sum, over
all histories x ending at z, of the value of f at the source s(x). This illustrates
a contrast between classical and quantum processes. Classically, states succeed
each other by exactly one process. In the quantum picture, every possible process
contributes to evolution of a state. In particular, there is an inter pretation of
quantum processes in terms of “matrix mechanics”, which takes a s um (in the form
of matrix multiplication) over all histories joining ﬁxed start and end s tates. This
is exactly what is shown in our example.
It is not too diﬃcult to check that the linearization of spans of sets g ets along
with composition, so that the composite of spans (by pullback, giving a set of
composite paths) agrees with composition of linear maps. That is, that the process
is functorial. This fact makes it possible to think of categorifying this process, in
order to explicitly include symmetries of both states and histories as fundamental
concepts. A categoriﬁed version of this process should be a 2-fun ctor.
One way to generalize spans of sets, which is seen in [2], uses groupoid s (cate-
gories whose morphisms are all invertible) instead of sets. One reas on to consider
this is that it often happens that the conﬁguration space can natu rally be thought
of not as a set but as a groupoid. This happens particularly when the re are sym-
metry operations acting on the set of conﬁgurations, and we explic itly represent
2-VECTOR SPACES AND GROUPOIDS 3
such symmetries as morphisms of the groupoid. The existence of a g roup action on
the set would be one example. In such a categoriﬁed picture, X has objects which
represent states of a system, and morphisms denoting symmetries of states. Then L
gives vector spaces which are linear combinations of isomorphism classes of objects
of the groupoids. The components of the linear maps uses groupoid cardinality
instead of set cardinality:
L(X)[yi],[zk] =
∑
x∈(s,t)−1(yi,zk)
#(Aut(yi))
#(Aut(x))(4)
=| ˆ(yi, zk)|· #(Aut(yi))
where ˆ(yi, zk) is the essential preimage of yi and zk, and its cardinality is the
groupoid cardinality described by Baez and Dolan [4] (the other card inality is the
order of the group). This uses a weighting of contributions from int ermediate
elements depending on the size of their symmetry group. The group oid cardinality
of a ﬁnite groupoid X is:
(5) |X| =
∑
[x]∈X
1
# Aut(x)
where the cardinality in the sum denotes the order of the group.
Here, however, we want to do something a little diﬀerent: this proce ss is still a
functor, and we wanted a 2-functor. Since we want to think of X as a category,
rather than look at functions from the objects of X into C, we should look at
functors from X into some category which plays the role of C. In particular, this
category will be V ect, whose objects are vector spaces over C, and whose morphisms
are linear maps. When categorifying, therefore, we will want to ﬁnd an analogous
2-functor, which requires specifying more data.
Then there will be a “free 2-vector space” Λ( X) of all functors from X into
V ect. We think of the objects as “2-linear combinations” of classical sta tes, each
with an internal state space which carries a representation of the symmetry group
of that state. For most physically realistic systems, X would be an inﬁnite set
with a measure, and in fact a symplectic manifold. In general, to deal with L2
spaces involves some issues in analysis, such as the measure on X. Then instead of
L(X) we consider L2(X). A similar caveat should apply in the categoriﬁed setting.
Restricting to the situation of a ﬁnite groupoid helps to more clearly illu strate some
of the purely category-theoretic aspects of the “free 2-vecto r space” construction.
We do expect that for well-behaved smooth groupoids, for example , similar results
to those considered in this paper will hold, involving inﬁnite dimensional 2-vector
spaces one could denote 2 L2(X). But this will be addressed in a companion paper.
Finally, we remark that this construction is used in the construction of an Ex-
tended Topological Quantum Field Theory (ETQFT) in the author’s Ph .D. thesis
[15], where the groupoids in question are topological invariants of ma nifolds. By
analogy, it could be used to give “extended quantum theories” in oth er settings
where spans of groupoids appear.
Another view of a related process involves the 2-functor into addit ive categories
(which, in the C-linear case, are the KV 2-vector spaces) from a 2-category Bim,
whose objects are rings, morphisms in hom Bim(R, S) are ( R, S)-bimodules, and
whose 2-morphisms are bimodule homomorphisms. This is a dual pictur e to that of
4 JEFFREY C. MORTON
spans. Indeed, the type of “pull-push” construction given here is ubiquitous (as its
appearance in linear algebra suggests), due to the universal prop erties of categories
of spans (see [7]). Similar notions also appear in the theory of Mackey functors (see
[16]), and in the study of “correspondences” in noncommutative ge ometry, algebraic
geometry, and elsewhere.
In this paper, we will begin by describing the source and target cate gories,
Span(FinGpd) in section 2, and 2V ectin section 3. In particular, to categorify
the functor L, we need a 2-category to correspond to V ect, and this will be the
2-category of all Kapranov-Voevodsky 2-vector spaces. A KV 2 -vector space is an
abelian category with some extra structure, just as a vector spa ce is a special type
of abelian group. In section 3 we give some background and collect so me fundamen-
tal results about them which are widely known, but whose proofs ar e seldom given.
For example, we show that 2-vector spaces, understood as a sem isimple C-linear
additive category, are all equivalent to V ectk for some nonnegative integer k.
In section 4, we give the object level of our construction for a 2-f unctor Λ, which,
to (essentially ﬁnite) groupoids assigns KV 2-vector spaces. Analo gously with sets,
we obtain 2-linear maps for spans of groupoids. In fact, just as wit h sets, this is
a consequence of an even simpler correspondence. Namely, there is the “pullback”
and “push-forward” of a function mentioned in the description of t he linear map
from a span of sets as a sum over histories (the sum occurs in the “push-forward”
operation, and corresponds to the sum in matrix multiplication). The groupoid
situation is more complicated than that for sets, however, becaus e of the existence
of automorphisms of the objects, and the condition that maps bet ween groupoids
are functors. This means, in particular, that for each object x in a groupoid, the
functor determines a homomorphism from the automorphism group of x to that of
its image. The push-forward operation can be interpreted as a Kan extension and
has both an object and a morphism level.
Section 5 describes how these results deﬁne 2-linear maps associat ed to spans
of groupoids. It begins with a brief discussion of the bicategory who se objects are
groupoids, whose morphisms are spans of groupoids, and whose 2- morphisms are
span maps. This is followed by an explicit construction of the morphism level of the
2-functor Λ : Span( FinGpd)→ 2V ectand shows that it preserves composition of
spans in the weak sense: that is, up to a speciﬁed isomorphism. (Tec hnical details
of this proof are reserved for appendix A). Finally, using Frobenius reciprocity, it
describes a simple explicit matrix representation for the 2-functor constructed.
Section 6 then continues by describing how this representation wor ks at the level
of 2-morphisms. This is analogous to the 1-morphism level, in that it co nsists of a
“pullback and pushforward” process. This is most easily described in terms of the
linear maps between corresponding vector spaces which appear in t he matrix rep-
resentation of the 2-linear maps associated to a pair of spans from A to B. We give
this construction and show it preserves both vertical and horizon tal composition of
2-morphisms in the appropriate ways.
The results shown in sections 5 and 6 do much of the work involved in sh owing
that our representation is really a 2-functor. The remainder of th is proof is given
in section 7.
Now we begin to describe the 2-linearization process by collecting som e key facts
about the bicategory of 2-vector spaces, including a canonical co nstruction of one
for each (essentially ﬁnite) groupoid.
2-VECTOR SPACES AND GROUPOIDS 5
2. The Bicategory Span(FinGpd)
The main purpose of this paper is to describe a weak 2-functor
(6) Λ : Span( FinGpd)→ 2V ect
In this section, we will describe the source bicategory, Span( FinGpd).
First, the objects of Span( FinGpd).
Deﬁnition 2.0.1. An essentially ﬁnite groupoid is one which is equivalent to a
ﬁnite groupoid. A ﬁnitely generated groupoid is one with a ﬁnite set of objects,
and all of whose morphisms are generated under composition b y a ﬁnite set of
morphisms. An essentially ﬁnitely generated groupoid is one which is equivalent
to a ﬁnitely generated one.
Note that, in particular, essentially ﬁnitely generated groupoids mu st be essen-
tially ﬁnite, since every object has an identity morphism. We will use th e term
“essentially ﬁnite” to mean both of these conditions. Next we descr ibe the mor-
phisms of Span( FinGpd).
In any category C, a span is a diagram of the form:
(7) X
s/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125
t /d32/d32/d65/d65/d65/d65/d65/d65/d65/d65
A1 A2
In particular, we want to reproduce the “linearization” associated to spans of sets
which we discussed in the introduction. The idea is that given a span of groupoids,
as in Figure 2 (which suppresses the homomorphisms labelling the stra nds in the
span, but should be compared with Figure 1), there will be a “transf er” 2-linear
map from the KV 2-vector space associated to the source of the s pan, to that
associated to the target.
Figure 2. A Span of Groupoids
6 JEFFREY C. MORTON
If C has pullbacks, we can deﬁne composition of spans using them:
(8) X ′◦ X
S
/d123/d123/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
T
/d35/d35/d72/d72/d72/d72/d72/d72/d72/d72/d72
X
s
/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125
t
/d35/d35/d71/d71/d71/d71/d71/d71/d71/d71/d71 X ′
s′
/d123/d123/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
t′
/d33/d33/d66/d66/d66/d66/d66/d66/d66/d66
A1 A2 A3
where we deﬁne X ′◦ X to be the object, unique up to isomorphism, which makes
the central square a pullback square. That is, it is a terminal occup ant of this
niche. If C is, in addition, a concrete category, the pullback is a subobject of t he
product X× X ′.
(9) X ′◦ X = X×A2 X ′ =
⋃
a∈A2
t−1(a)× (s′)−1(a)
the ﬁbred product of X ′ and X over A2. (Indeed, if C is Cartesian, any span can
be factored through a product.)
Now, for any category C with pullbacks, there is a category Span( C) whose
objects are the objects of C, and whose morphisms are isomorphism classes spans
in C composed by pullback. Here we are taking spans up to isomorphisms α :
X1→ X2 which are commuting diagrams of the form:
(10) X1
s1
/d125/d125/d124 /d124 /d124 /d124 /d124 /d124 /d124 /d124
α
/d15/d15
t1
/d33/d33/d66/d66/d66/d66/d66/d66/d66/d66
A1 X2s2
/d111/d111
t2
/d47/d47 A2
However, we will do something slightly diﬀerent. We will be interested in spans
of groupoids. Since groupoids naturally form a 2-category, we sho uld weaken the
notion of composition, and give an appropriate notion of 2-morphism , for a bicat-
egory Span( FinGpd).
Given any 2-category C with weak pullbacks, one can again form a bicategory
Span(C) with the same objects as C and with spans for morphisms. T composite
of spans A1
s
← X
t
→ A2 and A2
s′
← X ′ t′
→ A3 is an object X ′◦ X together with a
2-morphism α making this diagram commute, and terminal for such choices:
(11) X ′◦ X
S
/d123/d123/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
T
/d35/d35/d72/d72/d72/d72/d72/d72/d72/d72/d72
s◦S
/d11/d11
t′◦T
/d19/d19
X
s
/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125
t /d35/d35/d71/d71/d71/d71/d71/d71/d71/d71/d71
α
∼
/d43/d51X ′
s′
/d123/d123/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
t′
/d33/d33/d66/d66/d66/d66/d66/d66/d66/d66
A1 A2 A3
A 2-morphism in Span( C) will be an isomorphism class of spans of span maps .
That is, consider a span of 2-morphisms in the usual Span( C). This is a diagram
2-VECTOR SPACES AND GROUPOIDS 7
of the form:
(12) X1
s1
/d125/d125/d124 /d124 /d124 /d124 /d124 /d124 /d124 /d124
t1 /d33/d33/d66/d66/d66/d66/d66/d66/d66/d66
A1 Y/d111/d111 /d47/d47
t
/d15/d15
s
/d79/d79
A2
X2
s2
/d97/d97/d66 /d66 /d66 /d66 /d66 /d66 /d66 /d66
t2
/d61/d61/d124/d124/d124/d124/d124/d124/d124/d124
In principle we need only require this diagram commute weakly: that is, there
are isomorphisms ζs : s1◦ s→ s2◦ t and ζt : t1◦ s→ t2◦ t. For the most part, since
the construction we mean to give is invariant under equivalence of gr oupoids, and
taking the Ai to be skeletal makes this strict, we will assume strict commutativity ,
though we shall indicate where the argument must be changed to ac commodate the
weak case.
We are considering such diagrams only up to isomorphism : that is, the inner
span X1← Y→ X2 in the 2-morphism 12 is only considered up to an isomorphism
of spans in the sense of 10.
The reason for considering these is as follows. First, taking a categ ory C and
passing to Span( C) amounts to formally adjoining duals for morphisms in C. The
dual of any span is the span which has the same maps, considered in t he reverse
orientation, exchanging the role of source and target object. Wh en we apply Λ,
these duals will in fact become adjoints, as we shall see.
Now, we are interested in the case C = FinGpd, so the diagram for the com-
posite of spans between groupoids contains a weak pullback square : composition
is only preserved up to isomorphism. In particular, the objects are now groupoids,
which are themselves categories with objects and morphisms. Since it makes sense
to speak of two objects of a groupoid being isomorphic, the weakes t meaningful
condition is that objects of groupoids X and X ′ should need only project to iso-
morphic objects on A2. But there are potentially diﬀerent isomorphisms between
those objects. So the weak pullback is a larger groupoid than a stric t pullback,
since its objects come with a speciﬁed isomorphism between the two r estrictions.
That this is a weak pullback square of functors between groupoids m eans that
this diagram commutes up to the natural isomorphism α : t◦ S−→ s′◦ T . (The fact
that α is iso is what makes this a weak pullback rather than a lax pullback, where
α is only a natural transformation.) This is an example of a comma category (the
concept, though not the name, was introduced by Lawvere in his do ctoral thesis
[12]). We recall some background about this construction in Append ix A.1.
Now, the process of ﬁnding higher morphisms by taking spans of spa n maps
could obviously be continued: each new level of span naturally gives m aps of spans
as morphisms. We could repeat the process of adjoining duals by pas sing to spans
of such span maps, and so on recursively as far as we wish. For our p urposes here,
however, we will stop at 2-morphisms for two reasons. First, we wa nt to describe a
representation into 2V ect, which is a 2-category. This in turn is since the objects
of FinGpd are themselves categories, and our 2-functor Λ will represent th em as
categories - so a 2-category is the natural setting for them.
Collecting the deﬁnition together, we then have the following.
Deﬁnition 2.0.2. The bicategory Span(FinGpd) has:
8 JEFFREY C. MORTON
• Objects: Essentially ﬁnite groupoids
• Morphisms: Spans of groupoids, composed by weak pullback
• 2-Morphisms: Isomorphism classes of spans of span maps, composed by
weak pullback both horizontally and vertically
Having deﬁned Span( FinGpd), the source bicategory of the 2-functor Λ we aim
to describe here, we next describe its target, 2V ect.
