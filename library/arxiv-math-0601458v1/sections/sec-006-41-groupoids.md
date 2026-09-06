---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-006-41-groupoids
section_title: "Groupoids"
section_number: 4.1
pages: 14-30
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
with here:
Deﬁnition 8. A groupoid is a category in which all morphisms are invertible.
A group is a special example of a groupoid, with only one object - then the
elemnts of the group correspond to morphisms of the groupoid. An other special
case of a groupoid is a groupoid which has only one (identity) morphism per object
- such a groupoid is just equivalent to the set of its objects. General groupoids
are diﬀerent from either extreme case, since they can have many o bjects and many
morphisms. However, the idea that a set may have a cardinality leads us to try to
extend this idea to more general groupoids.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 15
4.1.1. Groupoid Cardinality. There indeed is a notion of cardinality for any groupoid,
which in general can give any positive real number (though it may also be diver-
gent). The notion of cardinality is closely related to the idea of “deca tegoriﬁcation”.
This is a process which takes a category and gives the set of isomorp hism classes
of objects. Similarly, there is a notion of cardinality which takes a set and gives
a number, one which takes a structure type and gives a formal pow er series, and
one which takes a monoidal category and gives a monoid (a category with extra
structure producing a set with extra structure).
Deﬁnition 9. The groupoid cardinality of a groupoid G is
(19) |G| =
∑
[x]∈G
1
| Aut(x)|
whereG is the set of isomorphism classes of objects of G. We call a groupoid tame
if this sum converges.
That is, each isomorphism class of objects of G contributes a term inversely
proportional to the size of the automorphism group of a typical ele ment. Note
that groupoid cardinalities of ﬁnite groupoids are just positive ratio nal numbers -
a ﬁnite sum of reciprocals of the sizes of ﬁnite groups. However, sin ce a general
groupoid may be inﬁnite, its cardinality may be an inﬁnite sum. Thus, gr oupoid
cardinalities can be any nonnegative real number (including inﬁnity). It is worth
noting that, as with sets, this idea of cardinality agrees with two nat ural operations
we can perform on groupoids. These are the disjoint union (sum) an d product, in
the following sense:
Theorem 4. IfG andG′ are tame groupoids, then so are G +G′ andG×G ′, and
we have |G +G′| =|G| +|G′| and|G×G ′| =|G|×|G ′|. If G andG′ are equivalent,
|G| =|G′|.
Proof. The groupoid G +G′ is the category whose set of objects is the disjoint
union of the sets of objects of G andG′, and since all morphisms are internal to
these groupoids, so is the set of isomorphism classes of objects. S o the fact that
|G +G′| =|G| +|G′| follows directly from the deﬁnition.
The groupoidG×G ′ has objects which are ordered pairs of objects from G andG′,
and morphisms likewise ordered pairs of morphisms, which are iso prec isely when
both elements of the pair are iso. So the isomorphism classes of obje cts are again
ordered pairs of isomorphism classes of objects from G andG′. The automorphism
group of any object ( g,g ′)∈G×G ′ is the direct product Aut( g)× Aut(g′), so
|G×G ′| =
∑
[(g,g′)]∈G×G ′
1
| Aut(g,g ′)|(20)
=
∑
[g]∈G
∑
[g′]∈G′
1
| Aut(g)× Aut(g′)|
=

∑
[g]∈G
1
| Aut(g)|

×

 ∑
[g′]∈G′
1
| Aut(g′)|


= |G|×|G ′|
16 JEFFREY MORTON
To see that cardinality is preserved under equivalence, just note t hat there is a 1-1
correspondence between isomorphism classes of their objects, a nd equivalent objects
have isomorphic automorphism groups, since an equivalence is a full, f aithful, and
essentially surjective functor.
□
This allows us to begin to elide the distinction between groupoids and th eir cardi-
nalities, passing back and forth as convenient (part of the intent o f categoriﬁcation,
just as when we conﬂate /C6 and FinSet0).
We can make an analogy with sets here: in a set seen as a category wit h only
identity morphisms, an element of the set is exactly the same as an iso morphism
class of objects, so we might think of these classes as “elements” o f a groupoid G.
In this case, the cardinality function (decategoriﬁcation) which we have described
gives us potentially fractional values for each “element” of a group oidG, so we can
think of a groupoid as a way of getting a “fractional” set - at least fr om the point of
view of this cardinality function. So we can think of a groupoid as an en tity whose
cardinality is a nonnegative extended real number (given by a possib ly inﬁnite
sum of positive rationals), and so if a structure type is an entity who se cardinality
is a formal power series with natural number coeﬃcients, it should n ot be too
surprising that we can view this structure type as a function which t akes a groupoid
and produces another groupoid, just as a power series can be eva luated at a real
number and yields another real number. Moreover, although grou poid cardinalities
can diverge, creating a problem of well-deﬁnedness, by passing to t he categoriﬁed
setting, we can eliminate this problem, and deal directly with the grou poids instead.
The way we do this is to deﬁne
(21) F (Z0) =
∑
n∈ /C6
(Fn×Z n
0 )//Sn
where the sum is interpreted as a coproduct, Fn is the groupoid whose object set
is the nth coeﬃcient of F (as a set of structures) and whose morphisms are as
above (the groupoid of F -structured ﬁnite sets is a direct sum of groupoids Fn, of
structures whose underlying sets have size n). In this deﬁnition, Z n
0 is a product of
n copies of Z0, and Sn is the permutation group on n elements. The quotient which
appears inside the sum (coproduct) is a weak quotient of the group oid Fn×Z n
0
by the group Sn. This requires some explanation. First we will describe groupoid-
coloured sets, then we will describe the construction of a weak quo tient.
4.1.2. Groupoid-Coloured Sets. For any groupoidZ0, we can speak of “Z0-coloured”
sets. It is easier to understand what these are if we think of sets a s groupoids
themselves. In particular, given a set S, we can think of it as a groupoid whose
objects are the elements of S, and the only morphisms present are the identity
morphisms (which must exist by deﬁnition). This is clearly a groupoid. T hen a
map from a set into a groupoid is just a functor. So:
Deﬁnition 10. A Z0-coloured set is a set S equipped with a colouring map
c : S → Z0. Maps of Z0-coloured sets in hom((S,c ), (S′,c ′)) are bijections
σ : S→ S′ together with, for each x∈ S, a morphism fx∈ hom(c(x),c ′(σ(x)).
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 17
That is,
(22) S
σ /d47/d47
c
/d15/d15
S′
c′
/d15/d15
Z0 {fx}
/d43/d51Z0
We can think of these as sets having each element x∈S “coloured” by an object
ofZ0, namely its image under the map f , which is a functor between two groupoids.
The general form of such a thing is shown in (23), and an illustration o f a coloured
set is shown in ﬁgure 2.
(23) Z0 •···•f
/d111/d111
g 1 g 2 g 3 g 4 g 5
Figure 2. A Z0-Coloured Set
Morphisms of Z0-coloured sets can be seen as bijections α of the underlying
sets where “strands” of the bijections are labelled by morphisms of Z0 between the
Z0-objects colouring the elements of S and S′ they connect, as shown in ﬁgure 3,
where all the gi and g′
i are inG, and fi∈ hom(gi,g ′
i).
(24) Z0
{fi}
/d11/d19
•···•c
/d111/d111
α
/d15/d15Z0 •···•
c′
/d111/d111
f4
f5
f3
f1f2
g 1 g 2 g 3 g 4 g 5
g’2 g’4 g’5 g’1 g’3
Figure 3. A Morphism of G-Coloured Sets
Theorem 5. The collection of Z0-coloured ﬁnite sets forms the object set of a cat-
egoryZ0-Set whose morphisms are as described. Moreover, Z0-Set is a groupoid.
18 JEFFREY MORTON
Proof. The morphisms described can be composed in the obvious way - compo sing
bijections of the sets, and labelling strands of the result with the co mposites of the
Z0-morphisms labelling each strand:
(25) S
σ /d47/d47
c
/d15/d15
σ;σ′
/d40/d40
S′ σ′
/d47/d47
c′
/d15/d15
S′′
c′′
/d15/d15
Z0
{fx} /d43/d51
{fx;f ′
x′ }
/d50/d58Z0
{f ′
x} /d43/d51Z0
This notion of composition is well deﬁned since if the strand σ(x) = x′ is labelled
byf∈ hom(x,x ′) and σ′(x′) = x′′ byf ′∈ hom(x′,x ′′), the strand in the composite
σ′σ(x) = x′′ can be labelled by f ′f since these are composable. This composition
rule inherits all the usual properties (e.g. associativity) from bijec tions in Set and
morphisms in Z0.
The identity morphism from a Z0-coloured set to itself is clearly the morphism
with identity bijection whose strands are labelled by identity morphism s on the
labels - again, properties of the identity are inherited from Set and Z0. So in fact
Z0-Set is a category.
Moreover all morphisms of this kind are invertible, since both bijectio ns σ and
all morphisms from Z0 labelling strands are invertible (i.e. Z0-Set inherits the
property of being a groupoid from the fact that both Z0 and Set are. □
In short,Z0-Set is a groupoid of sets labelled by objects of Z0 in a way compatible
with the groupoid structure of Z0.
Remark 1. In the special case where Z0 is a trivial groupoid with only identity
morphisms, (which can be seen as a set) the deﬁnition of a morphism r educes to
bijections compatible with the colourings, that is σ : S → S′ gives a morphism
between the Z0-coloured sets c :S→Z0 and c′ :S′→Z0 providedφ◦c′ =c), i.e.
that:
(26) S
c
/d15/d15
σ /d47/d47S′
c′
/d126/d126/d125/d125/d125/d125/d125/d125/d125/d125
Z0
commutes.
This is an example of an “over category”, also known as a “slice” cate gory. See
appendix B for more comments on this.
Having constructed a groupoid Z0-Set from Z0, it makes sense to ask about its
cardinality. However, this is a special case of what we really wish to do : given a stuﬀ
type Φ, ﬁnd the cardinality of Φ-stuﬀed, Z0-coloured ﬁnite sets. In particular, if Φ
is the stuﬀ type (in fact, structure type) “being a ﬁnite set”, the n this is exactly
the cardinality of Z0-Set. To describe the general case, we need to understand
the weak quotient of groupoids by groups, which will account for th e eﬀect of the
permutations σ in the above construction.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 19
4.1.3. Weak Quotients of Groupoids by Groups. We want to deﬁne the weak quo-
tient of any groupoidG by a group G which acts on it, giving a groupoid G/G. This
will be particularly nice in the special case where G is just a trivial groupoid - i.e.
a set S, seen as a category - and in this case we can also speak of the quotie nt of a
set by a group, which will be a groupoid S/G.
Deﬁnition 11. A strict action of a group G on a category C is a map A which
for every g∈ G gives a functor A(g) : C→ C such that A(gh) = A(g)A(h) and
A(1) = Id C . If there is such a strict action, then the strict quotient of C by G is
a categoryC/G together with a quotient functor j :C→C/G such that j◦A(g) = j
for all g∈G.
Clearly, in the special case where G is a groupoid, so is G//G, since all morphisms
are generated, by composition, from invertible morphisms. Moreov er, when C is a
trivial groupoid - i.e., a set - the deﬁnition of a strict action of G on C is identical
to the usual deﬁnition of a group action on a set, but when there ar e nontrivial
morphisms, it carries more information because A(g) must be functorial. A strict
quotient agrees with the usual intuition of how a quotient should wor k on objects, in
that if there is a group element taking an object x∈C toy∈C, then j(x) = j(y):
the objects of C/G are just equivalence classes of objects in C which are equivalent
if they lie in the same orbit under the action A. Also, the fact that A and j are
functorial means that morphisms of C are taken to morphisms of C/G compatibly
with composition.
This strict action, and strict quotient, require too much to be very useful. More
generally, it is not necessary that j◦A(g) actually be equal to j, so long as they
are isomorphic in a reasonable way.
Deﬁnition 12. A weak quotient of a category C by a group G, acting on C by
an action A (as above), is a groupoid C//G whose objects are objects of C. Its
morphisms are generated by composition from morphisms in C with morphisms of
the form A(h,g ) : g→ g′, whenever A(h)(g) = g′, where g,g ′∈ C, h∈ G. Any
relations which hold in C hold in C//G, together with relations: A(h′,g ′)◦A(h,g ) =
A(h′h,g ) wheneverA(h)g =g′; and A(h)f◦A(h,g ′′) = A(h,g )◦f for all f :g′′→g
(the action A is functorial).
Notice that all the morphisms added by the group action are invertib le, since
h ∈ G is invertible. Now we illustrate the weak quotent C//G showing a few
representative morphisms:
(27) •g
A(h,g)
/d60/d60•g′′
f/d123/d123
A(h)f ◦A(h,g′′)=A(h,g)◦f
/d41/d41
A(h,g′′)
/d61/d61•
A(h)f
/d55/d55• •g′
Remark 2. It is possible to describe a weak quotient by means of a (weak) uni-
versal property. It will be a groupoid C//G together with a quotient functor
j : C → C//G such that there is a natural isomorphism τ (g) : j◦ A(g)
∼
−→j
for all g∈G. We require that the natural isomporphism satisfy the coherence con-
dition τ (gh) = τ (g)◦τ (h), and that the weak quotient should be “weakly initial”
20 JEFFREY MORTON
among all groupoids with these properties. We will not describe this in detail here,
however, since we have a concrete construction.
Once we have this concept of the weak quotient of a groupoid by a gr oup, we
naturally want to ﬁnd its groupoid cardinality; this will generally be sma ller than
|G| since we have added new isomorphisms, hence potentially increased | Aut(x)|
for some objects x. In fact, we have a better result:
Theorem 6. The cardinality of the weak quotient of a groupoid G by a group G
satisﬁes
(28) |G//G| =|G|
|G|
Proof. We have by deﬁnition that
(29) |G//G| =

 ∑
[g]∈G/ /G
1
| Aut(g)|·| Stab(g)|


where Stab(g) is the stabilizer subgroup of a representative g inG. This is since
the isomorphism classes in G//G are given by considering the isomorphism classes
inG and identifying any which are related by the action of G. For each of these
isomorphism classes, the automorphism group consists of transfo rmations taking
one equivalent object to another. Any given object [ g] in such a class will have as
automorphism group the product of the automorphism of a corres ponding object in
G with its stabilizer subgroup Stab([g]) inG. So each isomorphism class contributes
a term 1
| Aut(g)|·| Stab(g)| .
On the other hand,
(30) |G|
|G| = 1
|G|
∑
g∈G
1
| Aut(g)|
Here the isomorphism classes are in G: for each isomorphism class in G//G, there
will be|G|/| Stab(g)| isomorphism classes in G, since each object g∈G is acted on
by each element of G and taken to one of these classes. So in fact this is the same
as|G//G|. □
Remark 3. It is worth noting what happens in the special case where G is just a
discrete groupoid (i.e. a set, whose groupoid cardinality is just its se t cardinality).
If the group action happens to be free, this result just says that the number of
orbits is the cardinality of the set divided by the size of the group - bu t the result
holds even when the action is not free, as in this picture illustrating a Z2 action on
a 3-element set, giving a groupoid with cardinality 3
2 :
(31) • /d2/d2 /d28/d28
id
/d68/d68 •
id
/d68/d68
/d26/d26 /d4/d4 •
id
/d68/d68
4.2. Stuﬀ Types as a Generalization of Structure Types. We are now ready
to describe stuﬀ types and some of their properties.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 21
4.2.1. Stuﬀ Types. We have already described structure types as functors
F : FinSet0→ Set
and also as special functors (in particular, faithful ones)
˜F : X→ FinSet0
where X is the groupoid of F -structures on ﬁnite sets, and the functor ˜F takes
each to its underlying set. Faithfulness means that we do not have t wo distinct
morphisms in X with the same image in FinSet0 - that is, that a map between
structures is completely determined by its eﬀects on the underlying set. So we
say that we have “forgotten structure” - since there may be mor phisms in FinSet0
which do not correspond to any in X (because they do not “preserve F -structure”).
In section 4.4, we describe in more detail what is meant by saying that a functor
forgets properties, structure, and stuﬀ . For the moment, we extend the notion of
structure types, and describe property types, structure typ es, and stuﬀ types, all of
which are functors from some groupoid X to FinSet0 which forget the given sort
of information.
Deﬁnition 13. A stuﬀ type is a functor Φ : X→ FinSet0, where X is a groupoid.
If Φ is faithful but perhaps not full or essentially surjective ( forgets structure) we
say it is a structure type ; if it is full and faithful, but perhaps not essentially
surjective (forgets properties) it is a property type; if it is an equivalence (forgets
nothing), it is a vacuous property type .
We think of these functors as giving the “underlying sets” of the st uﬀ type
in question. We can think of a stuﬀ type Φ : X→ FinSet0 as a “groupoid over
FinSet0”, so that any object of the groupoid X has an underlying set in FinSet0,
and by analogy with the terminology “ F -structured ﬁnite set”, we will describe it
as a “Φ-stuﬀed ﬁnite set”. This should suggest the idea that a stuﬀ type gives us
a collection of objects which correspond to ﬁnite sets S, but which possibly have
extra information associated with them (the “stuﬀ” forgotten by Φ).
Returning to our connection with the quantum harmonic oscillator, if we view
stuﬀ types this way, and think of the dual entity, Φ ∗ : FinSet0→ Set, taking
each ﬁnite set n to the set of ways of putting “Φ-stuﬀ” on it - in this context, this
represents the set of ways for a state with energy n to occur in X, the groupoid
associated with the state (which, however, we just denote Φ).
We can see how this connection develops in two steps. First, we repla ce a function
ψ : /C6 → /BV function ψ : /C6 → Set: that is, a structure type described as a map
giving, for any ﬁnite set, the set of all Ψ-structures on it. The cat egory of sets takes
the role of the complex numbers (in the ﬁrst stage), which we under stand in the
following way. The complex values ψn, which in quantum mechanics represent the
“amplitude” for the particular pure state with energy n to occur are replaced in
this ﬁrst stage by sets of Ψ-structures on a particular ﬁnite set S of size n. We can
think of these as “the set of ways for possibility n to occur”. (In section 6 we will
see how amplitudes arise).
The net step is to replace the natural numbers /C6 by the groupoid FinSet0,
so that stuﬀ types get a richer structure - in particular, we can de scribe them as
functors, since FinSet0 is a groupoid rather than merely a set. Now we can think
of these in several ways, including as bundles over the groupoid FinSet0. In this
setting, a “point” in the type Φ is an object of X together with its underlying set
22 JEFFREY MORTON
- the base point in the bundle. We we can also think of the “point” as a ﬁ nite
set with extra “Ψ-stuﬀ”, which we depict as a label x attached to Ψ( x). This is
illustrated in ﬁgure 4.
xΨ
Figure 4. Example Object of a Stuﬀ Type Ψ
If Ψ is a structure type, this label can be seen as some structure p ut on the set
Ψ(x), but in general this will not be the case - the label could, for examp le, be
other sets in a tuple of which Ψ( x) is one part (this is example 12). To be general,
we will not specify what this label contains, and simply say that it cont ains “stuﬀ”.
A morphism f in X is iso, since X is a groupoid: this gives a bijection Ψ( f ) of
underlying sets in FinSet0. Together, this data is a morphism in Ψ, show generally
in (32) and illustrated by the example in ﬁgure 5.
(32) •···•
Ψ( f ) ≀
/d15/d15
/d63/d62/d61/d60 /d56/d57/d58/d59x
f ≀
/d15/d15
Ψ
/d111/d111
•···• /d71/d70/d69/d68/d64/d65/d66/d67x′
Ψ
/d111/d111
Ψ x’
Ψ x
Ψ(f) f
Figure 5. Morphism In the Groupoid of Stuﬀ Type Ψ
Example 6. We’ve seen that the structure type “being a ﬁnite set” can be repr e-
sented as EZ, since there is exactly one way to put this structure on any ﬁnite se t
S (in fact, it is the “vacuous property type”). We might ask if there is a structure
type “EEZ
” - shorthand for “being a ﬁnite set of ﬁnite sets”. But, in fact, th is is
impossible. Certainly, this will not have cardinality e ez
, since there are an inﬁnite
number of ways of putting this structure on a given ﬁnite set S - that is, taking
a ﬁnite set of (disjoint) ﬁnite sets such that their union is S. In particular, any
number of copies of the empty set may be in an “ EEZ
-structure” on S. A worse
problem is that there are distinct morphisms of such structure, diﬀ ering only in
their eﬀect on these empty sets, which correspond to the same mo rphism on the
underlying set S. So these empty sets constitute extra “stuﬀ”, and this EEZ
must
be a stuﬀ type which is not a structure type.
This example, EEZ
, highlights two points which we should address about stuﬀ
types. First, it is a special case of something we would like to be able to do more
generally, namely given two types F and G, to ﬁnd a type F◦G which is in some
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 23
reasonable sense the composite of F and G. In this example, both F and G are
the vacuuous property type EZ , yet even in this elementary case, their composite
already needs to be a stuﬀ type. The second issue is cardinality: our concept of
composition should include the fact that when we take cardinalities, w e should have
that|F◦G| =|F|◦|G|. This does not work with the cardinality operation we have
developed for structure types - at least when we try to generalize it naively. The
stuﬀ type we are optimistically calling F◦G =EEZ
is well deﬁned, for any ﬁnite
set S, but the set of these structures has inﬁnite cardinality, so the co rresponding
generating function is not e ez
. So we need a new concept of cardinality for stuﬀ
types, which should be consistent with the old deﬁnition in the special case where
they are structure types. We will deal with this issue ﬁrst.
4.2.2. Cardinality of Stuﬀ Types. We have said that a stuﬀ type is a groupoid over
FinSet0. By analogy with the situation for structure types, then, we can d eﬁne
a notion of cardinality for stuﬀ types. For structure types, we ha d a notion of
cardinality for which
(33) |F| =
∑
n∈FinSet0
|Fn|
n! zn
Here, as before, FinSet0 is the set of isomorphism classes of FinSet0 (that is,
/C6 ), and |Fn| is the cardinality of the set of F -structures on n - where this is now
the usual cardinality function on sets. The use of a common notatio n for both
cardinality operators emphasizes that any notion of cardinality |·| is in some sense
a decategoriﬁcation operation. For simplicity, we will replace FinSet0 with /C6 , but
we should remember that it derives from the original groupoid FinSet0.
In the same way, we can deﬁne the cardinality of a stuﬀ type:
Deﬁnition 14. Given a stuﬀ type Φ : X→ FinSet0, we deﬁne its cardinality by
(34) |Φ| =
∑
n∈ /C6
|Φ n|zn
where|Φ n| is the groupoid cardinality of the preimage of n under Φ .
Remark 4. Note that this really only makes sense if we are working with a “skele-
tal” version of FinSet0, so that the preimage of a set of size n is well deﬁned. This
is a category which is equivalent as a category to the standard vers ion of FinSet0
from set theory - that is, there are functors between them whos e composites are
naturally isomorphic to the identities. However, the skeletal versio n of FinSet0
has only one object per isomorphism class - that is, per ﬁnite cardina l number. We
will assume FinSet0 is skeletal whenever convenient.
Remark 5. Deﬁnition (14) is consistent with the deﬁnition of structure types,
since if we think of a structure type as a groupoid over FinSet0, its morphisms all
arise from permutations of the underlying sets, and so the groupo id cardinality of
the preimage of n is precisely|Φ n|/n!, since the groupoid is equivalent to the weak
quotient Φ n//Sn. Just as structure types had cardinalities which were power series
whose nth coeﬃcients were integers divided by n!, stuﬀ types have cardinalities
which are power series with nonnegative real coeﬃcients.
An example shows that stuﬀ types signiﬁcantly generalize structur e types, at
least as concerns the kinds of generating functions (power series ) which can appear
as their cardinalities:
24 JEFFREY MORTON
Example 7. The stuﬀ type “being the ﬁrst of a k-tuple of equal-sized ﬁnite sets”,
for any value k > 1, is a stuﬀ type which is not a structure type. This can be
represented as a functor Φ : X→ FinSet0, where X is the groupoid whose objects
are k-tuples of ﬁnite sets of the same size, and whose morphisms are k-tuples of
bijections. The components of X are Xn, which are the groupoids of k-tuples of
n-element sets. The cardinality of Φ is
|Φ| =
∑
n∈ /C6
|Xn|zn(35)
=
∑
n∈ /C6
|1//Sn|kzn
=
∑
n∈ /C6
( 1
n!
) k
zn
This cardinality cannot appear as that of any structure type, sinc e the coeﬃcients
ofzn in such power series must be of the form an
n! foran∈ /C6 , which is not the case
here unless k = 1.
4.3. Stuﬀ Types As Power Series. Once we have the mechanics of groupoids,
stuﬀ types, and their cardinalities, it becomes possible to extend th e analogy with
formal power series which began structure types. Although for t he purposes of
quantum mechanics, we are mainly interested in the Hilbert space structure of for-
mal power series, it is worth pointing out that more of the algebraic a nd arithmetical
properties of power series can also be recovered. In particular, w e will next see that
the cardinality maps for stuﬀ types and groupoids lets us ﬁnd analog s of the eval-
uation of a power series at a real number - and, by extension, the c omposition of
two power series. These could not, in general, be done with just str ucture types.
In section 5 we return to features specially relevant to quantum me chanics.
4.3.1. Evaluation of Stuﬀ Types. One useful fact about stuﬀ types is that we can
deﬁne a sensible notion of evaluation, which brings us back to the fac t that we
had two ways of looking at power series as functions: either by the e valuation map
z ↦→f (z) or by the map picking out coeﬃcients in the power series expansion,
n↦→fn. Structure types have given us a good categoriﬁed way of looking a t the
latter, but with stuﬀ types we will be able to do the former as well. This also
lets us talk sensibly about the composition of types, just as we might talk about
composition of functions. Since this is one motivation for passing fro m structure
types to stuﬀ types, let’s consider an example of an algebraic opera tion with power
series which can’t be extended to the setting of structure types in a way which is
compatible with the correspondence between structure types an d power series:
This example of a stuﬀ type suggests the way we speak of evaluating stuﬀ types
at groupoids - by “colouring” elements of a set with objects of the g roupoid. That
is:
Deﬁnition 15. Given a groupoid Z0 and a stuﬀ type Φ : X → FinSet0, the
evaluation of Φ at Z0. is the groupoid Φ(Z0) of Φ -stuﬀed, Z0-coloured ﬁnite
sets, whose objects are pairs (φ,z 0)∈ Φ n×Z n
0 , where φ is a way of equipping an
n-element set with Φ -stuﬀ, and z0 is a map f :n→Z0 equipping each element of n
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 25
with an object of Z0. The morphisms of Φ(Z0) are bijections of the underlying n-
element sets with strands labelled by morphisms in Z0 between the objects labelling
corresponding elements.
Notice that there is an action of Sn on the objects of Φ( Z0)n - the ways of putting
Φ-stuﬀ on a set of size n, together with a Z0-colouring of this set - which comes
immediately from the action of Sn on the underlying set.
In the case where Φ is a structure type F , the groupoid F (Z0)n is just a weak
quotient (Fn×Z n
0 )//Sn. That is, its objects consist of pairs: F -structures which
can be put on an n-element set, together with colourings of an n-element set by
Z0 objects. These have an action of the permutation group on the un derlying set
(two such objects are isomorphic by reindexing the sets in in the F -structure and
the colouring in the same way). So then the groupoid cardinality of F (Z0) is
(36) |
∞∑
n=0
(Fn×Z n
0 )//Sn| =
∞∑
n=0
|Fn||Z0|n
n! =|F|(|Z0|)
where the ﬁrst “sum” is a categorical coproduct. This formula is co nsistent with
the formula for the generating function of a structure type which we’ve seen before
in equation (2). The analogous fact is true for any stuﬀ type, thou gh recall that in
that case we will not explicitly refer to the action of Sn on the groupoid. However,
just as above, we have
(37) |Φ(Z0)| =|Φ|(|Z0|)
Example 8. Take a groupoid G, and say X is the groupoid of G-coloured ﬁnite
sets, and consider this groupoid as the stuﬀ type
Φ : X→ FinSet0
where Φ is the forgetful functor which takes a G-coloured ﬁnite set to its underlying
set. An object in Xn (the preimage of n in X) consists of n objects from G, and
morphisms of Xn are n-tuples of morphisms in G composed with permutations of
the n elements. Thus, Xn ≃ Gn
0/Sn, the weak quotient by the action we have
described. Taking its cardinality, we ﬁnd that
|Φ| =
∑
n∈ /C6
|Xn|zn(38)
=
∑
n∈ /C6
|Gn//Sn|zn
=
∑
n∈ /C6
|G|n
n! zn
= e |G|z
This follows since groupoid cardinalities are compatible with both power s and weak
quotients.
Both the parallel with the generating function e |G|z and the notion that F is
the type of “G-coloured ﬁnite sets” suggests that it makes sense F should be seen
as EG×Z - that is, composition of the type E□ (“ﬁnite sets of”) with G× Z (the
product type whose objects are one-element sets together with objects of G - i.e.
G-coloured one-element sets).
26 JEFFREY MORTON
Some interesting special cases of this example: when G is a groupoid which is
just a set k with only identity morphisms, we have a structure type of “k-coloured
ﬁnite sets”; G is a group G seen as a one-object groupoid, we have a notion of
(1//G)-coloured sets.
Furthermore, the calculation above gives us the cardinality of the g roupoid X
ofG-colored ﬁnite sets itself (i.e. not as a stuﬀ type) to be simply e |G| (since no
powers of z appear, but the calculation is otherwise the same). So we can see th is
groupoid as the evaluation of E□ atG.
4.3.2. Composition of Stuﬀ Types. At last we can return to the question of how
to compose stuﬀ types. We have seen how to evaluate stuﬀ types a t groupoids -
given a groupoid Z0, evaluating the stuﬀ type Φ at it gives Φ( Z0), the groupoid
of “Φ-stuﬀed Z0-coloured ﬁnite sets”. Since evaluating a stuﬀ type at a groupoid
(whose cardinality is a real number) yields another groupoid (whose cardinality is
again a real number), we should be able to repeat this process as ma ny times as
we like. In principle, for instance, we should be able to describe Ψ ◦ Φ(Z0) as “Ψ-
stuﬀed, Φ( Z0)-coloured ﬁnite sets” - a set with G-stuﬀ, whose elements are labelled
by ﬁnite sets with F -stuﬀ and elements labelled with objects of Z0.
Since a stuﬀ type Φ is itself a groupoid over ﬁnite sets, Φ : X→ FinSet0,
and we have a way of evaluating a stuﬀ type at a groupoid, we get a no tion of
composition for stuﬀ-types. We have seen in section 4.1.2 that ther e is a groupoid of
Z0-coloured ﬁnite sets, whose morphisms are bijections of sets with s trands labelled
by morphisms in Z0. We saw in (8) that its cardinality is e |Z0|.
We should think of this as an illustration of the above where F is the structure
type, in which we had the stuﬀ type “being a ﬁnite set” composed with the type
Z0×Z -Z0-coloured one-element sets, but we can generalize this to any stuﬀ typesF
andG, to obtain stuﬀ types F◦G =F (G) and in such a way that |F◦G| =|F|◦|G|.
a 2 a 3a 1
A
b 1 b 2
B
c 1 c 2 c 3
C F X
Figure 6. An Object in a Composite Stuﬀ Type
We can describe what we get here as a type which, evaluated at Z0, gives “ F -
stuﬀed G(Z0)-labelled ﬁnite sets”. This has objects (as shown in ﬁgure 6) which
consist of ﬁnite sets equipped with F -stuﬀ (say F : X→ S). The elements of F
are labelled by objects of G(Z0): that is, the labels themselves consist of ﬁnite sets
labelled with G-stuﬀ, denoted by capital letters in the ﬁgure, whose elements ar e
themselves labelled in turn by objects from Z0, denoted by lower-case letters.
Morphisms in the groupoid of F -stuﬀed G(Z0)-coloured ﬁnite sets (illustrated
in ﬁgure 7) consist of maps between the objects of F ’s groupoid of stuﬀ, which
project down to morphisms of the underlying G(Z0)-coloured sets. This has its top
level as a bijection of the underlying sets. The strands of the top- level bijection are
labelled by morphisms of the groupoid of G(Z0)-coloured ﬁnite sets. These include
morphisms of the objects associated to the G-stuﬀed Z0-coloured sets (the dotted
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 27
1h 2h
3h
c 1 c 2 c 3
C
c’1 c’3 c’2
C’
b 1 b 2
B
1g
2g
b’1 b’2
B’
f1 f3f2
a’3 a’1a’2
A’
a 2 a 3a 1
A
XF
X’F
Figure 7. A Morphism in a Composite Stuﬀ Type
lines), which are associated to bijections of the Z0-coloured sets - with strands
labelled by morphisms of Z0.
Clearly, we could in principle continue this sort of construction recur sively, to
deﬁne the composite of any number of stuﬀ types.
4.4. F orgetful F unctors: Properties, Structure, and Stuﬀ. Here we take a
detour through some ideas from category theory which apply direc tly to stuﬀ types.
The ﬁrst is a classiﬁcation of functors by degrees of forgetfulnes s, which is the source
of the term “stuﬀ” in “stuﬀ type”. In fact, we want to explain the t erms “structure”
and “stuﬀ” which appear before the word “type” in our terminology . We began
by trying to categorify a certain rigs, replacing it by a 2-rig of funct ors - and now
we look at a classiﬁcation of functors to see how we generalized this p rocess. In
particular, we are interested in functors which are, respectively: faithful; full and
faithful; or full and faithful and essentially surjective:
Deﬁnition 16. A functor F :C →D is essentially surjective if the images
of objects in C cover all objects of D in the sense that for any d∈ Ob(D), there
is some c∈ Cwith F (c)∼= d. It is full if for any c,c ′ ∈ C, the map between
the sets of morphisms, F : Hom C(c,c ′) → HomD(F (c),F (c′)), is surjective (in
the set-theoretic sense). The functor F is faithful if for morphisms in its image,
F (f ),F (f ′)∈ HomD(F (c),F (c′)), we have F (f ) = F (f ′)⇒f =f ′ in HomC(c,c ′).
Each of these can be seen as a form of surjectivity. The notion of e ssential surjec-
tivity is a version of onto for categories at the level of objects. Fullness means that
a functor is “ onto for morphisms”; faithfulness is “ onto for equations between mor-
phisms” in the sense that any equation between morphisms in Hom D(F (c),F (c′))
comes from some equation between the preimage morphisms in Hom C(c,c ′).
We have a classiﬁcation of functors, then, by which of these it satis ﬁes (which
we will attempt to explain next):
28 JEFFREY MORTON
F unctor F orgets
essentially surjective, full, faithful “nothing”
full, faithful “properties”
faithful “structure”
all “stuﬀ”
When we move to the setting of n-categories, we have not only objects and mor-
phisms, and the possibility that morphisms may be equal, but also 2-mo rphisms
between morphisms (so that they may be 2-isomorphic, rather tha n merely equal, or
indeed might have non-iso 2-morphisms between them), and 3-morp hisms between
2-morphisms, and so on. Important to notice is that essential sur jectivity involves
a weakening (a functor is essentially surjective if it is surjective ont o isomorphism
classes, but not necessarily objects). This is because we should no t distinguish
between equivalent categories, and since every category is equiva lent to a skeletal
category with only one object in each equivalence class. We will, in fact , want simi-
larly weakened versions of full , faithful, and their higher-dimensional counterparts,
when we use n-categories.
For now, though, we will explain the second column of this table, and s ee how it
applies to structure types. The intuition begins with the commonplac e fact that a
map between sets is an isomorphism if it is both injective and surjectiv e. For func-
tors between categories, essential surjectivity is the natural a nalog of surjectivity,
but full functors are the natural analogs of injective maps. A map is inject ive if no
two distinct objects have the same image - that is, any equation of o bjects in the
image comes from an equation in the domain. A functor is full if every m orphism
between objects in the image comes from a morphism in the domain, so injectivity
of set maps is a special case, considering a set as a category with on ly identity
morphisms. In this trivial sort of category, every functor is faith ful.
So a bijection between sets is a full, faithful, essentially surjective f unctor, and if
such a functor exists, we should treat the sets as “the same” - th e functor has lost
no important information (of which there is very little, for a set), wh ich is reﬂected
in the fact that it is invertible. If we have more general categories, with nontrivial
morphisms, then in much the same way, we have that a functor F :C→ D, is an
equivalence ofC andD (i.e. there is a functor F −1 which is an inverse to F up to
natural isomorphism) if F is full, faithful, and essentially surjective. Similar results
are true for higher-dimensional categories ( n-categories, for any n), while functors
which fail to have these properties are in various senses “forgetf ul” - not being
equivalences, they must forget information about the source cat egory. This gives
a “periodic table” of grades of “stuﬀ” forgotten by functors whic h fail to be onto
for objects, morphisms, 2-morphisms (between morphisms), 3-m orphisms (between
2-morphisms), and so on. We restrict our attention to the case n = 1, but note
that the pattern we will develop continues for higher n.
We see that these classes of functor can be used to talk about clas ses of “type”:
structure types and stuﬀ types are functors from groupoids int o the groupoid
FinSet0 - in fact, they are functors which forget “structure” and “stuﬀ ” respec-
tively.
4.4.1. Examples of Forgetful Functors. Some examples illustrate the classes of func-
tors we have described. So for instance, if a functor F :C→D is not essentially
surjective, but is full and faithful, we have a subcategory of C inD, namely the
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 29
image of F , which is equivalent to C, but which does not exhaust the isomorphism
classes ofD:
Example 9. The functor
I : AbGrp→ Grp
embeds the category of abelian groups and their homomorphisms int o the category
of all groups and homomorphisms. This functor has “forgotten a p roperty”, namely
the property of being Abelian. The category Grp does not discriminate between
objects with and without this property, whereas AbGrp is distinguished by the
fact that it does.
If a functor fails to be essentially surjective and fails to be full, we can have not
only the sort of situation above, but the target category can hav e morphisms which
do not correspond to those in the source:
Example 10. The functor
I : OrdFinSet0→ FinSet0
takes any element in the groupoid OrdFinSet0 of totally ordered ﬁnite sets (whose
morphisms are order-preserving bijections) into FinSet0 - taking ordered sets and
order-preserving maps to the underlying sets and set-maps. This fails to be full
since there can be bijections between the underlying sets of two or dered sets which
fail to preserve order. This functor “forgets structure” - nam ely, that structure
which must be preserved by morphisms in OrdFinSet0, the total ordering on its
objects.
Both of these examples are faithful functors, in the sense that e ach morphism in
the source category is sent to a distinct morphism in the target. Th ere are functors
which lack this property as well:
Example 11. Consider the functor:
P1 : V ect2→ V ect
The objects and morphisms in V ect2 are ordered pairs of those in V ect, namely
vector spaces and linear transformations between them, while the functorP1 is just
projection onto the ﬁrst component of these pairs. Clearly, this is not faithful, since
there are many pairs morphisms in V ect2 with the same ﬁrst component. What
this functor has “forgotten” is, for each object, an entire vect or space, and all the
information about morphisms associated to these. More than simply forgetting
about properties shared by all objects, or structure which must be preserved by
morphisms, we say this functor forgets “stuﬀ” - parts of object s, in this case.
Example 12. Our previous example of a completely forgetful functor involved
the category of vector spaces, but similarly, there is an obvious cla ss of stuﬀ types
associated to the groupoid FinSet0
n, whose objects and morphisms are n-tuples
of ﬁnite sets and bijections:
Pj : FinSet0
n→ FinSet0
where Pj is the projection onto the jth coordinate. The set in this entry is the
“underlying set”, and the “stuﬀ” being forgotten consists of all t he other sets in
the tuple. This stuﬀ type is a completely forgetful functor.
30 JEFFREY MORTON
