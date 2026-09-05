---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-007-5-stuff-types-and-quantum-mechanics
section_title: "Stuff Types And Quantum Mechanics"
section_number: 5
pages: 30-56
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
Now we will return to our original motivation - seeing stuﬀ types as a c ategori-
ﬁcation of states of the quantum harmonic oscillator. We have alrea dy seen how
stuﬀ types can take the role of formal power series, at least up to the level of linear
structure. The space of formal power series should be the Hilbert space of states
of the quantum oscillator: so composition of stuﬀ types, which we ha ve explored,
will not enter into this picture, though the linear structure will. If st uﬀ types are
categoriﬁed power series, and the 2-category StuﬀTypes is a categoriﬁed Fock
space some of the basic structure for a Hilbert space 2. One diﬃculty is that we do
not have additive inverses, and another is that we lack an inner prod uct (which any
Hilbert space must have, and which we need to calculate probabilities in a quantum
system).
Interestingly, while the additive inverses are rather tricky to deﬁn e, and will have
to wait until section 6 when we deﬁne M -stuﬀ types, the inner product does not
even need to be deﬁned as a special construction, or imposed as ex tra structure: a
canonical one arises directly from the categoriﬁed framework as a (in part because
by describing stuﬀ types as functors into Set, we are in eﬀect choosing an ordered
basis for this categoriﬁed equivalent of a Hilbert space). What is mor e, a Hilbert
space should have an algebra of linear operators - endofunctions - which acts on it.
We need to see what the equivalents of operators on stuﬀ types ar e before we can
use them to categorify the oscillator. We will see that these are dire ctly related to
the inner product.
5.1. Inner Product of Stuﬀ Types. The ﬁrst feature of a Hilbert space we need
to recover is its inner product.
5.1.1. Inner Product as Pullback. When we were discussing the Hilbert space of
states of the quantum harmonic oscillator, we described the inner p roduct on this
Hilbert space, which gave us, on the basis of pure states zk, the form ⟨zn,z m⟩ =
δn,mn!. We would like to give this a combinatorial, or categoriﬁed, interpreta tion
in terms of our categoriﬁed states - stuﬀ types. The inner produc t for stuﬀ types
(now thought of as categoriﬁed states) will turn out to satisfy th e property that
|⟨Φ, Ψ⟩| =⟨|Φ|,|Ψ|⟩ just as we saw for composition of types.
Previously we described the categoriﬁcation of formal power serie s in two steps
- ﬁrst replacing the complex numbers by some groupoid X, then replacing the
natural numbers by FinSet0. We follow the same two-step process to describe the
categoriﬁed inner product.
Now, in a quantum mechanical setting, the space of states of a sys tem is a
space of L2 functions over some conﬁguration space. In the case of the harm onic
oscillator, the conﬁguration space is just a set of energy levels, eq uivalent to /C6 , and
so the space of states can be seen as ℓ2, the space of square-summable sequences
(of complex numbers).
In the categoriﬁed space of states, a natural way to get an inner product is
to extend the deﬁnition ⟨ψ,φ⟩ =∑
n∈ /C6
ψnφn in the case of complex numbers to
become
(39) ⟨ψ,φ⟩ =
∑
n∈ /C6
ψn×φn
2A treatment of the construction of Hilbert spaces from struc ture types appears in [9].
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 31
where the sum is now a coproduct in Set (i.e. a disjoint union) and the multiplica-
tion is the categorical (Cartesian) product. This way of looking at t he inner product
gives a set, and the equivalent condition to square-summability is the ﬁniteness of
this set. The cardinality operator gives us a notion of square-summ ability in the
decategoriﬁed setting: we can dispense with this condition in the cat egoriﬁed set-
ting, just as we can treat structure types with inﬁnite sets as coe ﬃcients. In the
case where the set we get is ﬁnite, it should be clear that when we tak e cardinalities,
we just get that the cardinality |⟨ψ,φ⟩| is just ⟨|ψ|,|φ|⟩. So this is naturally seen
as an inner product in the sense that when we take cardinalities, we g et a number
which will be the inner product of the vectors in the space of power s eries which
are the cardinalities of the two types. In the ﬁnite case these are j ust polynomials:
this is as yet not very interesting since we are dealing with sets, whos e cardinalities
are just integers. We will address this when we pass to the case of a groupoid over
FinSet0.
To see how this will work, note that, just as structure types and s tuﬀ types
themselves, we can treat the inner product as a “bundle over /C6 ”, with projection
maps taking the individual elements of this disjoint union of products down to /C6
by the obvious projection taking an element of ψn×φn ton (which is well deﬁned,
since all elements of the inner product are of this form). So if we thin k of the
two states ψ,φ as corresponding to two bundles F : S→ /C6 and G : S′→ /C6 for
S,S ′∈ Set we have, as we’ve seen:
(40) ⟨F,G⟩ =
∑
n∈ /C6
ψn×φn =
∑
n∈ /C6
F −1(n)×G−1(n)
This can be understood in categorical terms as the ﬁbered produc t of the two
bundles, also written as X×
/C6
Y where the projection maps F,G of the bundles
are understood. Another way to say this is to describe it as a pullback of the two
projections X
F
→ /C6
G
←Y , which is to say an object which is initial among objects of
the form X
Px
←O
Py
→Y making the square
(41) O
Px /d47/d47
Py
/d15/d15
X
F
/d15/d15
Y G
/d47/d47
/C6
commute. (That is, given any other such object O′ with maps into X and Y, there
is a unique map from O to O′ making the combined diagram commute.)
5.1.2. The Categoriﬁed Case: Inner Product As Weak Pullback. The next level of
categoriﬁcation of this description will give us a deﬁnition of the inner product
of two stuﬀ types as a groupoid - namely the pullback of the two func tors from
groupoids X and Y into FinSet0. The inner product on this space is the same
one we described when talking about the harmonic oscillator (equatio n 13). To get
this more fully categoriﬁed inner product - now an inner product of s tuﬀ types -
we should replace /C6 , the “base space” by FinSet0, which is the free symmetric
monoidal category on one generator, just as /C6 is the free commutative monoid on
one generator.
So suppose we have two stuﬀ types, namely functors Ψ : X → FinSet0 and
Φ : Y→ FinSet0, for some groupoids X, Y∈ Gpd. We want to do the equivalent
32 JEFFREY MORTON
of taking the pullback of these two functors:
X
Ψ
→ FinSet0
Φ
← Y
Since these are not just functions between sets, but functors b etween categories, the
pullback is in the 2-category Cat, or indeed in Gpd. So deﬁning a pullback becomes
slightly more complicated - in fact, we can and should weaken the requ irement that
the pullback square
(42) ⟨Ψ, Φ⟩
PX
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
PY
/d123/d123/d118/d118/d118/d118/d118/d118/d118/d118/d118
Y
Φ /d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72 X
Ψ/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118
FinSet0
commutes exactly, and allow it to commute only up to a 2-isomorphism b etween the
two composite projections, so that what we want is the weak pullback (an example
of a “pseudo-limit” in a 2-category; see [15]) :
(43) ⟨Ψ, Φ⟩
PX
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
PY
/d123/d123/d118/d118/d118/d118/d118/d118/d118/d118/d118
Y
Φ /d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72 X
Ψ/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118α
∼/d107/d115
FinSet0
This is like the ﬁbrewise product over /C6 which we described above, and we
can also denote this by X×FinSet0 Y, emphasizing the groupoids rather than the
functors. Let’s understand this weak pullback better by seeing wh at this groupoid
actually looks like internally, and then seeing that the groupoid cardin ality of this
inner product of stuﬀ types corresponds to the inner product of two states|Ψ| and
|Φ|.
Deﬁnition 17. The groupoid⟨Ψ, Φ⟩ = X×FinSet0 Y has objects which are pairs
(x,y )∈ X× Y equipped with an isomorphism α(x,y) : Ψ( x) ˜→Φ(y). A morphism in
⟨Ψ, Φ⟩ is a morphism in X× Y, say (f,g ) : (x,y )→ (x′,y ′), such that
(44) Ψ( x)
Ψ( f ) /d47/d47
αx,y
/d15/d15
Ψ(x′)
αx′ ,y′
/d15/d15
Φ(y)
Φ( g)
/d47/d47 Φ(y′)
commutes. That is, αx′,y′◦ Ψ(f ) = Φ( g)◦αx,y.
The isomorphism α is from the deﬁnition of weak pullback; in a strict pullback,
α(x,y) would always be the identity - that is, we would require that Ψ( x) = Φ( y).
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 33
Now, what does this all mean? The isomorphism α is a bijection of underlying
sets - so an object of ⟨Ψ, Φ⟩ is a pair of objects ( x,y ), (Ψ- and Φ-stuﬀ respectively
on their underlying sets), together with a bijection between the un derlying sets, as
shown generall in (45) and illustrated in ﬁgure 8.
(45) •···•
αx,y ≀
/d15/d15
/d63/d62/d61/d60 /d56/d57/d58/d59x
Ψ
/d111/d111
•···• /d63/d62/d61/d60 /d56/d57/d58/d59y
Φ
/d111/d111
Ψ x
yΦ
αx,y
Figure 8. Object of an Inner Product (Pullback) Groupoid
A morphism between two such objects includes morphisms of the for m (32)
between the objects of Ψ and Φ; this gives bijections between the u nderlying sets
which must be compatible with those which are part of the ⟨Ψ, Φ⟩ objects (of the
form (45)) themselves. The general result is illustrated in (46) and an example
appears in ﬁgure 9.
(46) /d63/d62/d61/d60 /d56/d57/d58/d59x
Ψ
/d124/d124/d121/d121/d121/d121/d121/d121/d121/d121/d121/d121
f
∼
/d47/d47/d71/d70/d69/d68/d64/d65/d66/d67x′
Ψ
/d124/d124/d120/d120/d120/d120/d120/d120/d120/d120/d120
•···•
αx,y ≀
/d15/d15
Ψ( f )
∼
/d47/d47•···•
αx′,y′≀
/d15/d15
/d63/d62/d61/d60 /d56/d57/d58/d59y
Φ
/d124/d124/d121/d121/d121/d121/d121/d121/d121/d121/d121/d121
g
∼
/d47/d47/d71/d70/d69/d68/d64/d65/d66/d67y′
Φ
/d124/d124/d121/d121/d121/d121/d121/d121/d121/d121/d121/d121
•···•
Φ( g)
∼
/d47/d47•···•
So the naturality square (44) means that the inner square of set b ijections in
(46) commutes: in other words, that we have given a way to identify all these
underlying sets. We can see this in the ﬁgure as the fact that followin g strands
of the set bijections (of 3-element sets) around the square reve als that there are
exactly three complete squares of strands.
5.1.3. Stuﬀ Type and Fock Space Inner Products Related. The key example of the
inner product which makes clear the connection with the inner produ ct on Fock
space developed in section 3.1.2 is the inner product of stuﬀ types Z n andZ m, which
34 JEFFREY MORTON
Ψ x
yΦ x’Ψ
y’Φ
αx,y
αx’,y’
f
g
Φ (g)
Ψ(f)
Figure 9. A Morphism in an Inner Product (Pullback) Groupoid
also happen to be structure types. The stuﬀ type (in fact, struc ture type) Z n is the
type of total orders on an n-element set , or “being a totally ordered n-element set”.
An object of the inner product groupoid ⟨Z n,Z m⟩ is thus a pair ( x,y ) which are
n- and m-element totally-ordered sets respectively, equipped with an isomo rphism
between the underlying sets. We may think of these as the sets n ={0,...,n − 1}
and m ={0,...,m − 1}, and the isomorphism is just any bijection α between
these. If n⁄= m, there are no such objects since there are no such bijections. If
n =m, then there are n! such bijections, given by the permutations of {1,...,n }.
The morphisms of⟨Z n,Z m⟩ are just the identity morphisms on these objects, since
the only morphisms in the groupoid of totally ordered sets are order -preserving
bijections - that is, objects have no nontrivial automorphisms. Th us, we get:
(47) ⟨Z n,Z m⟩ =n!δn,m
where n! is the groupoid with n! objects (one per permutation of n) and only
identity morphisms, and δn,m is analogous to the usual Kronecker delta, being a
groupoid with no objects if n⁄=m and with one object and one morphism if n =m.
Thus,
(48) |⟨Z n,Z m⟩| =⟨|Z n|,|Z m|⟩
so that the inner product we found on Fock space is natural in this s etting. This
also illustrates the reason for the factor n! which shows up in the nth term in the
expansion of a structure type, or the power series which is its gene rating func-
tion. This n! is the cardinality of the group Sn, the group of permutations of the
underlying n-element set.
5.2. Stuﬀ Operators. So far we have described stuﬀ types, and implied that they,
as extensions of structure types, are a useful way of categorif ying functions - in the
setting where these functions are seen as states of a certain qua ntum system. The
inner product deﬁned in section 5.1 gives these some of the structu re of a Hilbert
space, and also makes a connection to Feynman diagrams for energ y quanta of a
harmonic oscillator. We want to describe more of the structure of t he 2-rig of stuﬀ
types - in particular its linear structure, demanding a deﬁnition for t he equivalent
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 35
of a linear operator. We call such a thing a stuﬀ operator . There will be a category
of these, called StuﬀOps , with higher-dimensional algebraic structure similar to
that of the algebra of linear operators on a Hilbert space, with an ac tion on the
category StuﬀTypes .
We need to describe this action: a stuﬀ operator T , given a stuﬀ type Ψ : X→
FinSet0, ought to produce another stuﬀ type T (Ψ) : T (X)→ FinSet0, using
natural category-theoretic operations, in a way that reﬂects t he fact that T is the
categoriﬁed equivalent of a linear operator on a Hilbert space of sta tes. One way
to motivate our approach to constructing this is to remember that for a Hilbert
spaceH, a linear operator T can be thought of as an element of the tensor product
H⊗H ∗ of H with its dual, and given a basis of H, T can be represented as a
matrix (a two-index tensor). To put this into the same framework a s the stuﬀ type
Ψ, recall that this can be seen as a vector in a space of states 3, and the equivalent
of resolving it in a basis arises by taking the preimages of elements of FinSet0
as the components in the basis. In this setting, applying T to a vector v (using
the H ∗ in the description in terms of H⊗H ∗) amounts to applying covectors in
any decomposition of T to v, which (since H∼= H ∗) amounts to taking the inner
product of v with a vector in H. Since we have already seen a natural deﬁnition of
inner product for stuﬀ types, we will use a similar construction.
A stuﬀ type Ψ : X→ FinSet0 can be variously seen as the projection map
of a groupoid-bundle on ﬁnite sets, and also as a way of picking out an index for
some component of a vector in a categoriﬁed equivalent of a Hilbert s pace. A stuﬀ
operator should have two such maps, since it is to correspond to a linear operator.
We should think of this as “resolving T in the same basis”.
The analogy with matrices suggests that T acts on stuﬀ types in the same way
as the inner product, just as matrices act on vectors (resolved in a basis) by way of
the inner product in each index. So indeed, T Ψ is deﬁned as a weak pullback:
Deﬁnition 18. A stuﬀ operator is a groupoid T with two projection maps into
FinSet0:
(49) T
p1
/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118 p2
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
FinSet0 FinSet0
We have seen the internal picture of objects of Ψ in ﬁgure 4, so we n ext look at
a similar description for T . An object t∈ T is somewhat similar to an object of
Ψ, but this object has not just one underlying set, but two possibly distinct ones,
which we call p1(t) and p2(t), which in general need not have the same cardinality.
We can think of this as two sets sharing a common label, which we may th ink of as
a “process” connecting p1(t) with p2(t), where the label t contains stuﬀ associated
to this transition, shown generally in (50) and illustrated in ﬁgure 10.
(50) •···• /d63/d62/d61/d60 /d56/d57/d58/d59tp1
/d111/d111
p2
/d47/d47◦···◦
3Strictly speaking, the “ground ﬁeld” here is not /BV but rather the setting for cardinalities
of groupoids, /CA
+, so we do not yet have a vector space. When we introduce M -stuﬀ and get
cardinalities in something like /BV , we will really have a vectorspace.
36 JEFFREY MORTON
t
Figure 10. Object in the Groupoid of Stuﬀ Operator T
We are not yet at the point of recovering Feynman diagrams, but we can already
see an object which contains some sort of label for a process conn ecting an n-
element set of “quanta” (in the convention we have already applied t o the harmonic
oscillator) to an m-element set of “quanta”. First we should see how these act like
linear operators.
We can deﬁne an algebraic structure of stuﬀ operators, when we r ecall how the
the categorical product and coproduct work for groupoids X and Y in Gpd. The
coproduct X + Y is just the direct sum of groupoids, whose objects and morphisms
are all objects and morphisms of either X or Y (in a way which distinguishes
where they came from). Their categorical product of has object s and morphisms
both consisting of ordered pairs of those from X and Y. We have seen that these
operations are compatible with groupoid cardinalities.
Deﬁnition 19. Given two stuﬀ operators T , T ′ with projection operators p1, p2
and p′
1, p′
2, respectively, the sum has groupoid T +T ′ whose projection functors
pi +p′
i act like pi or p′
i as appropriate. The product of T by a groupoid G, GT
has objects is the product groupoid G×T (with projection operators acting on the
T component).
These naturally have the properties that ( T +T ′)Ψ ∼=T Ψ + T ′Ψ and ( GT )Ψ ∼=
G(T Ψ) in the sense of the sum and “scalar product” of stuﬀ types, and thus the
corresponding facts hold “on the nose” (i.e. as equations) for car dinalities. On
the other hand, if we think of the stuﬀ operators as the categoriﬁ ed equivalent of
inﬁnite matrices (with projection operators the equivalent of index ing), we can think
of these as the sum and scalar product for matrices, deﬁning the lin ear structure
of the algebra of operators. We leave the proof of this to the inter ested reader.
More interesting is its internal multiplication, and the action on our ca tegoriﬁed
Hilbert space, the 2-category StuﬀTypes .
Deﬁnition 20. There is also an action of T on a stuﬀ type Ψ giving a stuﬀ
typeT Ψ given by a weak pullback:
(51) T Ψ
PT
/d122/d122/d117/d117/d117/d117/d117/d117/d117/d117/d117
PX
/d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73
PT ;p1
/d9/d9
T
p1
/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118
p2
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72/d107/d115
α
∼
X
Ψ/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118
FinSet0 FinSet0
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 37
and a composite of T and T ′ given similarly:
(52) TT ′
PT
/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118 P ′
T
/d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73
PT ;p1
/d9/d9
P ′
T ;p′
2
/d21/d21
T
p1
/d123/d123/d118/d118/d118/d118/d118/d118/d118/d118/d118
p2
/d35/d35/d72/d72/d72/d72/d72/d72/d72/d72/d72/d107/d115
α
∼
T ′
p′
1/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118
p′
2 /d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73
FinSet0 FinSet0 FinSet0
Here, we note that ( TT ′)Ψ ∼= T (T ′Ψ), which can be seen by considering the
isomorphisms α of the weak pullbacks in the diagrams for these two constructs.
Now, the groupoid T Ψ resulting from the action of T naturally becomes a stuﬀ
type (a groupoid over FinSet0) by composition of the projections PT ;p2 = p2◦
PT , where PT is the projection onto T from T Ψ, which is the pullback of the
functor Ψ from X onto FinSet0 along the projection P fromT to the same copy of
FinSet0. To understand this construction better, we should see what the objects
and morphisms of the groupoid T Ψ are like internally.
The stuﬀ type T Ψ is a weak pullback of T and Ψ, over the copy of FinSet0 which
is the target of Ψ : X→ FinSet0, and also of p2 :T→ FinSet0. Its objects will be
pairs of objects x∈ X and t∈T together with isomorphisms αx,t : Ψ( x)→p2(t).
These are isomorphisms of the underlying sets, so in particular they only exist if
these sets have the same cardinality. Thus, an object of T Ψ looks like an object of
T connected by a bijection of underlying sets to an object of Ψ (using the “right-
hand” underlying set of T ). The general form is shown in (53) and an example is
illustrated in ﬁgure 11.
(53) •···• /d63/d62/d61/d60 /d56/d57/d58/d59tp1
/d111/d111
p2
/d47/d47◦···◦
◦···◦
αx,t
/d79/d79
/d63/d62/d61/d60 /d56/d57/d58/d59x
Ψ
/d111/d111
p2
p1
t
xΨ
Figure 11. Object of Stuﬀ Type T Ψ
Since this is to be an object of T Ψ, we should see it as a stuﬀ type it its own
right, over the copy of FinSet0 mapped to under the projection p1 from T . That
38 JEFFREY MORTON
is, everything in this picture - the t object, x object, and the speciﬁc bijection αx,t
between the appropriate underlying sets - can be regarded as “ T Ψ-stuﬀ” attached
to the underlying set p1(t).
Now as for the composite of T and T ′, similar reasoning holds except that we
have another stuﬀ operator T ′ in place of Ψ, so the general form of an object of
TT ′ is as shown in (54), and an example is illustrated in ﬁgure 12.
(54) •···• /d63/d62/d61/d60 /d56/d57/d58/d59tp1
/d111/d111
p2
/d47/d47◦···◦
◦···◦
αt,t′
/d79/d79
/d63/d62/d61/d60 /d56/d57/d58/d59t′
p′
1
/d111/d111 p′
2 /d47/d47⋄···⋄
1p
2p
t
p’
1
t’
2
p’
Figure 12. Object of Stuﬀ Type TT ′
The construction we have described for stuﬀ operators is an exam ple of a “span”:
in particular, as morphisms from FinSet0 to itself. The composition we have de-
scribed above, as well as being analogous to matrix multiplication of line ar opera-
tors, satisﬁes the axioms for composition of morphisms. But in fact we have seen
that these operators also have an action on the category StuﬀTypes , derived from
the fact that it is a category over FinSet0. In fact, we can interpret stuﬀ opera-
tors as endofunctors of StuﬀTypes , just as linear operators are endofunctions of
a vector space. We describe this in more detail in appendix B.1.
5.3. F eynman Diagrams and Stuﬀ Operators. From a quantum mechanical
point of view, we are often interested in ﬁnding inner products such as⟨Φ,T Ψ⟩, and
ﬁnding these inner products can be done by means of Feynman diagr ams. That is,
in QM, the “transition amplitude” between states Φ and T Ψ is a sum of amplitudes
associated to Feynman diagrams, each showing one possible way of g etting from
state Φ to state Ψ by process T . We will show how this idea can be recovered in
the categoriﬁed setting, and in fact is given by exactly the algebraic ideas we have
deﬁned. In general, the groupoid ⟨Φ,T Ψ⟩ has objects as shown in ﬁgure 13
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 39
1p
2p
t
Ψ x 2
Φ X 1
αx1,t
αt,x2
Figure 13. Object of Groupoid ⟨Ψ,T Φ⟩
We will see that we can think of these as Feynman diagrams, and ﬁndin g the
sum over their amplitudes is exactly the process of taking the group oid cardinality
of this inner product of stuﬀ types - that is, a sum over Feynman dia grams of some
“amplitudes”. At the moment, these amplitudes are all positive reals , rather than
complex numbers as is usual in quantum mechanics. When we discuss M -stuﬀ
types in section 6, and in particular the case M =U (1) in section 6.2, we will see
how this can be resolved by introducing the quantum mechanical not ion of phase.
Since we are motivated here by the use of the algebra of stuﬀ types as a cat-
egoriﬁcation of the Weyl algebra, we examine the stuﬀ operators A and A∗, the
annihilation and creation operators. The annihilation operator A can be realized
in this form, with T = FinSet0 with two projection functors to FinSet0, one of
which is the identity, the other of which is the functor whose action o n objects is
to take a set S and produce S +{⋆}:
(55) FinSet0
1
←−FinSet0
+{⋆}
−→ FinSet0
To see that this reduces to our previous deﬁnition for A (deﬁnition 7) on stuﬀ
types which happen to be structure types, ﬁrst recall that it said an AF -structure
on a set S is an F -structure on the set S∪{⋆}. If our stuﬀ type Ψ happens to be
a structure type F whose groupoid is just a set of F -structured ﬁnite sets, then we
have:
(56) AS
P1
/d120/d120/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113
P2
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72/d72
AF =P1
/d5/d5
FinSet0
1/d120/d120/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113
+{⋆} /d38/d38/d77/d77/d77/d77/d77/d77/d77/d77/d77/d77 /d107/d115
α
/d43/d51S
F/d123/d123/d119/d119/d119/d119/d119/d119/d119/d119/d119/d119
FinSet0 FinSet0
Tracing the map in the new type AF fromAS to FinSet0, we note that we can
pass through S so that AF =P2;α, in which case we see that since α must make
the lower triangle commmute so that α; +{⋆} = F we get that the preimage of a
given ﬁnite set S under AF must correspond to the preimage of S +{⋆} under F .
40 JEFFREY MORTON
So indeed, putting an AF -structure on S amounts to putting an F -structure on
S +{⋆}.
Similar reasoning shows that A∗, the adjoint of A, can be realized in the same
way, with groupoid T ∗ = FinSet0 but with the projections reversed:
(57) FinSet0
+{⋆}
←− FinSet0
1
−→FinSet0
Moreover, this acts like A∗, so that in the event that Ψ = F is a structure type, a
A∗F -structure on a ﬁnite set S amounts to choosing an element of S and putting
an F structure on what remains.
From the parallel with Fock space, one operator we should want to d eﬁne is the
ﬁeld operator A +A∗. As a stuﬀ operator, this behaves as one might expect: the
groupoid in the stuﬀ operator is just the groupoid sum T +T ∗ (i.e. two copies
of FinSet0), and the projections just act as the projections on T and T ∗ when
applied to objects and morphisms from each of the two copies. So, t he objects of
the groupoid Φ, following the pattern we illustrated in (50), look like eit her objects
of A or of A∗, as shown in ﬁgure 14.
A* Aor
Figure 14. Example Objects in the Categoriﬁed Field Operator
In our categoriﬁed setting, this is written nearly the same way,
⟨
Z n, Φ kZ m⟩
, but
we now have an interpretation of the inner product as a groupoid ov er FinSet0,
obtained by a pullback - and indeed, of the stuﬀ operator Φ k as a composite of stuﬀ
operators, etc. Now, this Φ k has objects which are chains of objects of the form in
ﬁgure 14, composed as in ﬁgure 12. We can draw these in various way s (diﬀerent
drawing styles form objects in equivalent categories), but for com pactness, we will
draw these in a style which omits the “internal” bijections of the comp osite type,
and also the bijections from the A and A∗ objects of Φ to FinSet0. Thus, each
internal ﬁnite set would have previously been drawn three times, wit h bijections
between them. This compact style is illustrated in ﬁgure 15, which sho ws an object
of Φ 4. This one shows an object made from one annihilation and three crea tion
operators, in that order. All other permutations of four Φ-obje cts are possible also.
For the sake of further compactness (and another drawing style depicting an
equivalent category), note that what we really have here is an oper ation in which k
quanta of energy either appear or disappear, and do so in a deﬁnite order. We could
really draw this with just a single “interaction” vertex, incident with k strands (all
other strands passing straight through the diagram, matching up a quantum in the
top with a quantum in the bottom). These incidences would have to be labelled
with a total ordering, so that the object shown in ﬁgure 15 would be drawn as in
ﬁgure 16.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 41
B
A
C
D
Figure 15. Example Object From Φ 4
A
CD
B
Figure 16. Example Object From Φ 4 (Alternate Style)
There is an action of the permutation group Sk on these objects, changing the
order in which we encounter objects from A and A∗ as we pass through Φ k. That
is, for every object we get whose diagram has one order labelling the incidences,
we will get objects with all other possible orders exactly once throu gh the action
of the permutation group Sk, also known as k!. So if we want to omit this labelling
for clarity in the drawings, we can do so as long as we remember that t his means
we are really drawing objects of the weak quotient Φ k//Sk (weak quotients are
deﬁned in deﬁnition 12). The objects of this weak quotient are isomo rphism classes
of diagrams under permutations of labellings. These permutations g ive the natural
isomorphisms in the deﬁnition of weak quotient by taking any labelled dia gram to
the same diagram with permuted labels. In this new category, the ca rdinality of
the groupoid is thus scaled by 1
k! . We also need to keep in mind that an unlabelled
diagram really stands in for possibly several diﬀerent inequivalent lab ellings of the
incidences by distinct orderings.
All this is really a notational convenience: really, to calculate transit ion ampli-
tude between states ψ and φ for which we have a description as stuﬀ types Ψ and
Φ, when we put the system through some process t which we describe as a stuﬀ
operator T , we only need to ﬁnd the groupoid cardinality |⟨Ψ,T Φ⟩|. Simplifying
diagrams and ﬁnding convenient conventions for labelling them is really a way for
42 JEFFREY MORTON
getting a calculational convenience out of diagrams like ﬁgure 17, wh ich shows an
object from the groupoid Φ 4//S4.
Figure 17. Example Object in Φ 4//S4
Now, diagrams like this give vertices with k incidences. Taking polynomials in
the operators which give such diagrams gives operators which can b e interpreted in
terms of diagrams having several such vertices. Such a diagram is s hown in ﬁgure
18 - note that here we continue the practice of omitting to draw the internal ﬁnite
sets in the composite stuﬀ operator.
Ψ2
x2
Ψ1
x1
Figure 18. An Object in
⟨
Ψ 2, (Φ 3//S3)6Ψ 1
⟩
Given two stuﬀ types Ψ 1 : X1→ FinSet0 and Ψ 2 : X2→ FinSet0, we can take
the inner product ⟨Ψ 1, Φ nΨ 2⟩. This applies this operator to Ψ 2 to give compound
objects involving objects of Φ n and of X2. Taking the inner product with Ψ 1 gives
objects as illustrated in ﬁgure 18. The groupoid cardinality of this inn er product
amounts to a sum over all such diagrams, each with a weight related t o the size of
the symmetry group of the diagram.
Example 13. We can use the above to show the categorical meaning of the usual
calculation of the expectation value of a power of the ﬁeld operator . In particular,
suppose we want to calculate
⟨
1, φ6
6! 1
⟩
, the vacuum expectation value of the 6th
power of the (normalized) ﬁeld operator.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 43
To do this, we want to take a sum over objects which are equivalent t o ways
of matching two empty sets with diagrams like ﬁgure 17, containing on e vertex of
valence 6. We begin with the case where incidences are labelled (as in ﬁg ure 16).
Since the source and target sets are empty, all edges must form lo ops touching the
vertex at both ends. The number of such diagrams is (
( 6
2
)( 4
2
)( 2
2
)
)/3! = 15 (choosing
the endpoints of three edges, without order). These give the obj ects of a groupoid
one of which is shown in ﬁgure 19.
C
DE
F
A B
Figure 19. Example Object in
⟨
1, Φ 6//S61
⟩
The isomorphisms of this groupoid are given by permutations of the la bels.
Since this permutation group is S6 with 720 elements, the groupoid cardinality
should be 15
720 = 1
48 . The automorphism group of any such diagram is of size
48: there are 6 ways to map the set of loops to themselves, each wit h the same
orientation, or reversed orientation. Equivalently, we can think of the objects of
the groupoid as diagrams like this, but without labels. In this case, th ere is only
one such diagram, with the automorphism group as just described. So we have⟨
1, φ6
6! 1
⟩
=|
⟨
1, Φ 5//S61
⟩
| = 1
48 .
Now, the transition amplitude between two states in a quantum harm onic os-
cillator which undergoes an interaction described by a given operato r in the Weyl
algebra can be calculated, in part using a sum over Feynman diagrams . We have
now seen how, in this categoriﬁed setting, we can ﬁnd a direct combin atorial inter-
pretation for this fact.
Unfortunately, some features of the diagrams used in quantum me chanics are
missing from this interpretation. In particular, we do not have any w ay to express
the notion of “phase”, or operators involving propagators withou t interactions. In
quantum mechanics, states exist in superpositions - linear combinat ions - having
complex coeﬃcients. Non-interacting propagation in time involves th e rotation of
those coeﬃcients by a phase - that is, a unit complex number. Thus, both /BV
and the group U (1) of phases are important. We will see in section 6 how to
incorporate this into our combinatorial picture. As we shall see, th is involves an
explicit decomposition of complex numbers into amplitudes and phases .
6. M -Stuff Types And Quantum Mechanics
We have described various entities under the heading types, namely stuﬀ, struc-
ture, and property types, and hinted at the possibility that this se quence of classiﬁ-
cations will continue as we move into the setting of increasingly higher -dimensional
categories. For physical purposes, though, we are still missing so me essential prop-
erties which we would like a categoriﬁed version of quantum mechanics to have. In
particular, all of our cardinalities, and hence coeﬃcients of our typ es, lie in rigs,
44 JEFFREY MORTON
rather than rings - they can be added and multiplied, but not subtra cted and di-
vided. It is possible to handle this in the abstract setting of structu re types by
deﬁning virtual structure types as equivalence classes of formal diﬀerences of struc-
ture types (and similarly for stuﬀ types) to make subtraction poss ible (see [3]). For
quantum mechanics, however, the coeﬃcients of the power series which represent
states are complex numbers, and the physical signiﬁcance of phase is of paramount
importance, so we will still need something more. So for our purpose s, it makes
more sense to treat the question in a diﬀerent way.
6.1. M -Stuﬀ Types. Now we will see an analog of a stuﬀ type which can carry
a phase - or more generally, a weighting of some kind. To reproduce s ome of the
features of quantum mechanics which don’t appear in the picture of stuﬀ types as
“categoriﬁed states”, we should consider what is missing. First, st ates of a quantum
system should form a Hilbert space, and in particular a vector space . Since we
already have something like an inner product, what is missing is the abilit y to take
linear combinations of states. For this, they need to have a notion o f scalar product
and of addition. If we allow the categoriﬁed states to carry a weight , this weight
can play the role of a scalar multiple, but these weights need to form a monoid,
which we think of as multiplicative.
This is the motivation for deﬁning a notion of “ M -Stuﬀ Types” for some monoid
M , and in particular M =U (1), the group of phases. This is the case which is most
interesting for quantum mechanics. We’ll do this in general, since the construction
does not require M =U (1).
6.1.1. M -Sets. Before we can talk about M -Stuﬀ Types, we should start with a
more basic deﬁnition:
Deﬁnition 21. If M is a monoid, MSet is the category of “sets over M ”4, or
“M -sets”. Its objects are pairs (S,f ), for S∈ Set and f : S→ M . Morphisms
between two M -sets f1 : S1→M and f2 : S2→M are maps g :S1→ S2 in Set
giving commuting triangles:
(58) S1
f1
/d15/d15
g /d47/d47S2
f2/d126/d126/d125/d125/d125/d125/d125/d125/d125/d125
M
By abuse of notation, we will sometimes call the object just S or just f if the
meaning is clear by context. A similar deﬁnition can be made for MFinSet or
MFinSet0, where the sets S lie in FinSet or FinSet0.
Note that for each set S of cardinality n, the set of all M -sets with “overlying
set”S is just M S, equivalent to M n. The morphisms which make this into an over
category provide some extra structure, however.
We also note that this deﬁnition is similar to that for a Z0-coloured set for a
groupoid Z0 - in fact, the image one should have of an M -coloured set is just
the same as ﬁgure 2. One diﬀerence is that in this case, the picture w e have for
morphisms is diﬀerent from that for Z0-coloured sets: for M -Sets, morphisms are
just set maps which are compatible with the labelling. We could, of cour se, deﬁne
4See appendix B for comments about such “over categories”. Th e usual deﬁnition applies
here by treating M as a set of elements, though we get some extra structure from t he monoidal
operation on M .
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 45
a weak over category of sets “weakly over M ”, as we did with groupoid-coloured
sets, for which strands of morphisms are also labelled by elements of M , but as we
shall see, this is not what we want to do. One result of this is that we lo se some of
the desirable features of the category of sets, while retaining oth ers. For example,
we have the following:
Theorem 7. MSet is a category with all colimits (in particular, it has coprod ucts).
Proof. First, consider any diagram in MSet, and take the underlying diagram in
Set. Since Set is a cocomplete category, every diagram, and in particular this one,
has a colimit S. The diagram in MSet has a colimit provided we can construct
a map from S to M which is compatible with the set-maps from the objects of
the diagram in MSet. For any given element in S, every element taken to it by
one of the maps in Set must have the same image in M under the map for the
corresponding object in MSet, since if there is more than one, they must be taken
to some common element by maps in the diagram. Thus, we can consist ently deﬁne
f (s) for any element in the colimit to be equal to the value for any preimag e, and
so all the maps in Set are compatible with the function into M , and the colimit in
Set becomes a colimit in MSet. □
Coproducts in MSet can be interpreted as direct sums of M -sets - and this
makes it possible to deﬁne a cardinality for M -sets. We note that since M has
only one monoidal operation, we could consider two interesting kinds of cardinality,
depending on whether we want this operation to look like addition or mu ltiplication.
For our purposes, it is better to think of M as a multiplicative monoid, since we
will later want to take M =U (1), thought of as a subgroup of /BV . So we would like
to have a notion of cardinality which gets along with multiplication in an an alogous
way. We should deﬁne a notion of cardinality which reduces to set car dinality when
we think of M as multiplicative. Then we will ﬁnd a “tensor product” compatible
with this notion of cardinality.
Deﬁnition 22. The cardinality of an M -setS
f
→M is an element of /C6 ⊗M given
by
(59) |S| =
∑
s∈S
f (s)
where the sum is taken in /C6 .
This cardinality operator is a kind of decategoriﬁcation: it takes a se tS labelled
with values in M , and gives a formal sum of values in M , each taken the number
of times it appears in S. Note that this is again not compatible with the cartesian
product in MSet, by the same argument as for the additive cardinality. Instead,
we should take the following product:
Deﬁnition 23. The tensor product of two M -sets S
f
→M and S′ f ′
→M is an
M -setS⊗S′ has underlying set S×S′ (the cartesian product of underlying sets in
Set). The map (f⊗f ′) : S×S′→M is given by (f⊗f ′)(s,s ′) = f (s)·f ′(s′).
Theorem 8. The tensor product of M -sets satisﬁes |S⊗S′| =|S|×| S′|. When
M is commutative, the tensor product is symmetric.
46 JEFFREY MORTON
Proof.
|S⊗S′| =
∑
(s,s′)∈S×S′
f (s)f ′(s′)(60)
=
( ∑
s∈S
f (s)
)( ∑
s′∈S′
f (s′)
)
= |S|×| S′|
WhenM is commutative, there is an obvious isomorphism between S×S′ andS′×S
taking (s,s ′) to (s′,s ); the labelling is unchanged, since f (s)f ′(s′) = f ′(s′)f (s). □
These constructions for sets can be extended to groupoids, whe re cardinalities
start to look like complex numbers.
6.1.2. M -Groupoids. We would like to extend these results aboutM -sets to a notion
ofM -groupoids and their cardinalities which is compatible with cardinalities o fM -
sets and of ordinary groupoids in the suitable special cases. One wa y to see the
correct approach to M -groupoids is to take advantage our existing idea of M -sets
and a connection we already know between sets and groupoids. This is the concept
of a groupoid-coloured set. We deﬁne groupoid-coloured M -sets by analogy with
these. Recall from 4.1.2 that a set can be seen as groupoid whose ob jects are the
elements of the set, and with only identity morphisms 5. Then we have:
Deﬁnition 24. Given a groupoidZ0, a Z0-colouredM -set is an M -setS equipped
with a colouring map c : S → Z0. Maps of Z0-coloured M -sets are M -
set bijections σ : S → S′ together with, for each x ∈ S), a morphism fx ∈
hom(c(x),c ′(σ(x)). That is,
(61) S
σ /d47/d47
c
/d15/d15
S′
c′
/d15/d15
Z0 {fx}
/d43/d51Z0
This is essentially the same deﬁnition as appeared in 4.1.2, but we note t hat now
σ is a bijection of M -sets - that is, it is a set bijection which is compatible with
the M -labelling. But notice that groupoid-coloured M -sets are just sets with two
maps, one into a groupoid, and one into a monoid:
(62) S
c
/d126/d126/d126/d126/d126/d126/d126/d126/d126/d126 f
/d31/d31/d64/d64/d64/d64/d64/d64/d64/d64
Z0 M
Since the elements of this Z0-coloured M -set are just elements of S labelled by
both an object of Z0 and an element of M , we would like to be able to think of this
as a set labelled by objects of an “ M -groupoid”, which would look like objects of
the groupoid Z0 labelled by element of M . A consideration of what morphisms of
Z0-coloured M -sets must be reveals how to deﬁne this:
5Since we are already thinking of sets as special kinds of cate gories here, this raises the question
of what happens if we categorify M . W e return to this in section 7.1.2.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 47
Deﬁnition 25. Given a monoid M , an M -groupoid is a groupoidG with a functor
f fromG into the set M regarded as a groupoid. The cardinality of an M -groupoid
GM is an element of /CA
+⊗M , where /CA
+ and M are thought of as multiplicative
monoids. The cardinality of GM is given by the formal sum:
(63) |GM| =
∑
[x]∈GM
f (x)
| Aut(x)|
Remark 6. Note that /CA
+⊗M consists of all formal /CA
+-linear sums of formal
productsr⊗m forr∈ /CA
+ andm∈M , subject to the distributive law ( r+r′)⊗m =
r⊗m +r′⊗m. It becomes a rig with the obvious multiplication ( r⊗m)(r′⊗m′) =
(rr′⊗mm′).
Since we are thinking of M as a groupoid with only identity morphisms, functo-
riality of f means that for any a and b inG and g∈ hom(a,b ), we have f◦g =f .
That is, the following diagram commutes:
(64) a
g /d47/d47
f
/d15/d15
b
f/d127/d127/d126/d126/d126/d126/d126/d126/d126/d126
M
We see also that f (x) is well deﬁned for elements of any given isomorphism, since
any two objects with an isomorphism between them will be sent under f to the same
element of M . It should be clear that in the case where the “overlying” groupoid
of an M -groupoid happens to be a set (i.e. groupoid with only trivial morphism s),
this reduces to the deﬁnition of an M -set and its cardinality. In the case where M
is the trivial groupoid, this cardinality reduces to the usual groupo id cardinality.
Given two M -groupoids, we deﬁne their product as with M -sets:
Deﬁnition 26. The tensor product of two M -groupoids X
f
→M and X ′ f ′
→M
is an M -groupoid X⊗X ′ which has underlying groupoid X×X ′ (the cartesian
product of underlying groupoids in Gpd). The map (f⊗f ′) : X×X ′→M is given
by (f⊗f ′)(x,x ′) = f (x)·f ′(x′).
As with M -sets, this product gets along with M -groupoid cardinalities. The
proof is essentially the same, except that cardinalities involve facto rs of | Aut(x)|.
This depends on the fact that the automorphism group of an objec t (x,x ′) inX×X ′
is just the product of the automorphism groups of x and x′.
6.1.3. M -Stuﬀ Types and their Cardinalities. We begin with a deﬁnition:
Deﬁnition 27. AnM -stuﬀ type is anM -groupoid X
f
→M equipped with a functor
Ψ : X→ FinSet0, where X∈ Gpd.
Typically, we will just think of X as an object of MGpd and blur the details,
but this deﬁnition is what we always mean. So as with stuﬀ types, we ma y think of
M -stuﬀ types as functors from M -sets of “Ψ-stuﬀed ﬁnite sets” to their underlying
ﬁnite sets. In the case where Ψ is faithful we can say it is an M -structure type.
Note that we are still thinking of X as lying over FinSet0, not MFinSet0 - we
will return to this shortly.
Since stuﬀ types (and M -stuﬀ types) can be multiplied by groupoids, whose
cardinalities lie in /CA
+, this action by M gives another version of multiplication.
48 JEFFREY MORTON
This will be particularly interesting when we consider M =U (1) in section 6.2, but
ﬁrst we should deﬁne the cardinality of an M -stuﬀ type:
Deﬁnition 28. The cardinality of an M -stuﬀ type Ψ : X→ FinSet0 is
(65) |Ψ| =
∑
n∈FinSet0
|Ψ n|zn
where|Ψ n| is now the M -groupoid cardinality of the preimage of n under Ψ .
(As with a stuﬀ type, this deﬁnition requires us to take FinSet0 to be skeletal
to be well deﬁned - or else to consider only the essential preimage . We will do the
former.) This cardinality is an element of ( /CA
+⊗M )[ [z] ]: a formal power series in
z whose coeﬃcients are formal combinations of pairs of groupoid car dinalities and
elements of M .
Theorem 9. There are natural left and right actions of the monoid M on the
M -stuﬀ type Ψ . If M is abelian, these are the same action, which satisﬁes
(66) |mΨ|(z) = m|Ψ|(z)
Proof. We deﬁne the map ( m, Ψ) ↦→mΨ, where mΨ : mX→ FinSet0 acts as
follows. If x∈ X is an object of X whose weight is f (x), then the corresponding
element mx in mX has weight m·f (x). Then mΨ(mx) = Ψ( x). This is a left
action on stuﬀ types because it is a left action on M -groupoids together with a
compatible map to FinSet0. The right action of M is deﬁned similarly.
If M is abelian, a left and right action are the same, and the result follows b y
direct calculation. □
6.1.4. M -Stuﬀ Type Inner Product and M -Stuﬀ Operators. Once we deﬁned M -
sets and hence M -groupoids, it was possible to deﬁne M -stuﬀ types simply by
substituting these for groupoids in the original deﬁnition of stuﬀ ty pes. The only
properties of FinSet0 which were used in the original construction of stuﬀ types and
operators was that it should be a groupoid: groupoids X with one or two functors
into it were stuﬀ types and operators respectively. Morphisms bet ween the objects
of a stuﬀ type were morphisms in X together with compatible bijections of sets
(recall ﬁgure 5), but this depended only on the fact that these we re isomorphisms
in the groupoid FinSet0. So, in the same way, a morphism in the groupoid of an
M -stuﬀ type consists of a morphism in its M -groupoid, together with a compatible
bijection of underlying sets, as illustrated in ﬁgure 20. Notice that t he objects x
andx′ are labelled by the same element, m1∈M , since f is an isomorphism in X.
Ψ(f)
Ψ x m1
f
Ψ
1mx’
Figure 20. A Morphism in the Groupoid of an M -Stuﬀ Type
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 49
Now, the inner product of stuﬀ types Ψ : X→ FinSet0 and Φ : Y→ FinSet0
was deﬁned to be a weak pullback, as described in (43). The same deﬁ nition will
apply if we let these be M -stuﬀ types, allowing X and Y to be M -groupoids.
So we have a weak pullback of Ψ along Φ, which gives a groupoid ⟨Ψ, Φ⟩, and
can deﬁne canonical projection maps to X and Y. The groupoid is the ﬁbrewise
product X×FinSet0 Y, where we must use the tensor product of M -groupoids rather
than the cartesian product of groupoids to assign elements of M to its objects.
Deﬁnition 29. The given two M -stuﬀ-types Ψ : X→ FinSet0, and Φ : Y→
FinSet0, the M -groupoid⟨Ψ, Φ⟩ = X⊗FinSet0 Y is the weak pullback of Ψ and
Φ over FinSet0. It has objects which are pairs (x,y )∈ X⊗ Y equipped with an
isomorphism α(x,y) : Ψ( x) ˜→Φ(y). A morphism in ⟨Ψ, Φ⟩ is a morphism in X⊗ Y,
say (f,g ) : (x,y )→ (x′,y ′), such that
(67) Ψ( x)
Ψ( f ) /d47/d47
αx,y
/d15/d15
Ψ(x′)
αx′ ,y′
/d15/d15
Φ(y)
Φ( g)
/d47/d47 Φ(y′)
commutes. That is, αx′,y′◦ Ψ(f ) = Φ( g)◦αx,y.
An object in the inner product groupoid looks like ﬁgure 21, where mi are
elements of M . This ﬁgure is analogous to the previous inner product (ﬁgure 8).
Note that, in contrast to the case in ﬁgure 20, the objects x∈ X and y ∈ Y
are not in the same groupoid, hence not related by any morphism, so there is no
requirement that m1 andm2 should be equal. The object illustrated is labelled be
the element m1·m2∈M (as highlighted).
αx,y
Φ y m2
Ψ x m1
Figure 21. An Object In the Inner Product of two M -Stuﬀ Types
Similar changes apply to the other constructions deﬁned using the w eak pullback,
so that we have nearly identical categorical diagrams deﬁnining mor phisms in the
inner product, as well as the action of an M -stuﬀ operator on an M -stuﬀ type and
the composition of two M -stuﬀ operators, as in deﬁnition 20. The sole change at
this level is the replacement of groupoids with M -groupoids, and thus in ﬁgures
11 and 12, we have labels in M on every groupoid object, preserved under every
isomorphism.
50 JEFFREY MORTON
Deﬁnition 30. AnM -stuﬀ operator is an M -groupoidT with two functors from
the underlying groupoid of T into FinSet0:
(68) T
p1
/d122/d122/d118/d118/d118/d118/d118/d118/d118/d118/d118 p2
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
FinSet0 FinSet0
It acts on an M -stuﬀ type to give another M -stuﬀ type by weak pullback over one
copy of FinSet0.
Just as with the former constructions, we have:
Theorem 10. If Ψ and Φ are two M -stuﬀ types, then |⟨Ψ, Φ⟩| =⟨|Ψ|,|Φ|⟩.
Proof. At the level of the underlying sets and groupoids, every product o ver a ﬁnite
set in the (skeletal version of) FinSet0 in the ﬁbrewise product looks just the same
as for regular stuﬀ types. Each of these products is a product of M -groupoids,
which are compatible with cardinality. So the result holds. □
6.2. Quantum Mechanics: M =U (1). As remarked earlier, the notion of a phase
is crucial in quantum mechanics. Stuﬀ types, and in particular stuﬀ o perators and
the inner product of stuﬀ types, proved in the last section to have a close connection
to entities which resemble Feynman diagrams, but the only notion of c ardinality we
had for these was groupoid cardinality, which yields positive real valu es. We would
like to be able to do more, since in quantum mechanics, these diagrams should have
not a real cardinality, but a complex amplitude, which has both a magn itude and
a phase. This leads us to the idea of U (1)-stuﬀ types, since U (1) is the group of
phases, corresponding to the unit circle in /BV .
6.2.1. U (1)-Stuﬀ Types. From here on, we take M =U (1) - an abelian monoid, and
in fact an abelian group - we know that U (1)-stuﬀ types exist, and that they have
cardinalities in ( /CA
+⊗U (1))[ [z] ], which has the obvious homomorphism into /BV [ [z] ].
As we have seen, the cardinalities of M -sets for an abelian monoid M lie in M ,
which we can think of ; cardinalities for M -groupoids lie in /CA
+⊗M ; cardinalities
for M -stuﬀ types lie in ( /CA
+⊗M )[ [z] ]. When M = U (1), this gives /CA
+⊗U (1),
which has a homomorphism onto /BV
(69) h : /CA
+⊗U (1)→ /BV
We should note that this description of /BV in terms of /CA
+⊗U (1) explicitly
separates complex numbers into a magnitude and a phase, and while it has a mul-
tiplication resembling that for /BV , but it fails to capture the addition, which is
formal. However, the homomorphism h just imposes the relations which deﬁne
complex addition. The derived rig homomorphism h : ( /CA
+⊗U (1))[ [z] ]→ /BV [ [z] ]
behaves similarly. This homomorphism loses information, just as the p rocess of
taking cardinalities does, so in fact, when M = U (1), we can deﬁne a new cardi-
nality operator:
Deﬁnition 31. If X is a U (1)-groupoid and Ψ : X→ FinSet0 a U (1)-stuﬀ type,
the complex cardinality of Ψ is h applied to the usual M -stuﬀ-type cardinality:
(70) |Ψ|
/BV
=h
( ∑
S∈ /C6
|Ψ n|zn
)
=
∑
S∈ /C6
h|Ψ n|zn
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 51
where|Ψ n| is the usual M -stuﬀ cardinality, h is the above homomorphism, and
addition is in /BV .
The complex cardinality is a map which takes a U (1)-stuﬀ type and yields a
power series in /BV [ [z] ], namely Fock space. When dealing with U (1)-stuﬀ types, we
will write|Ψ|
/BV
as|Ψ|, unless otherwise noted.
Remark 7. Note that a type which consists of two states over U (1)-sets of the same
set cardinality but opposite phase will have a cardinality in ( /CA
+⊗U (1))[ [z] ] which
contains a formal linear combination which is in the kernel ofh. This is the critical
fact that when we represent states in Fock space, there can be interference between
states with opposite phases. In particular, the amplitude for a (ca tegoriﬁed) state
containing only those two objects will be zero.
6.2.2. Conjugation and The Inner Product. There is a property of U (1)-stuﬀ types
which is not generally shared by M -stuﬀ types for arbitrary M , resulting from
the fact that it is an Abelian group. This follows from the fact that th ere is a
nontrivial monoid isomorphism between U (1) and itself, taking each element of
U (1) to its multiplicative inverse. There will be such an isomorphism when everM
is an Abelian group. Viewing U (1) as the unit complex numbers, however, allows
us to see this as complex conjugation, which is how we will think of it. Th us, there
is an operation special to U (1)-stuﬀ types:
Deﬁnition 32. If X is a groupoid with U (1) labellingf : X→U (1), its conjugate
groupoid is the U (1) groupoid whose groupoid is labelling is f , given by f (x) = f (x).
When we write X for the U (1)-groupoid, we write the conjugate as X. If Ψ : X→
FinSet0 is a U (1)-stuﬀ type, its conjugate Ψ is the type which acts like Ψ on the
objects of the underlying groupoid of X.
This allows us to deﬁne a variant of the inner product which has the co njugate-
linearity of the usual complex inner product on Fock space. To distin guish this
from the (bilinear) inner product ⟨Ψ, Φ⟩, and call it ⟨Ψ|Φ⟩, also a more familiar
notation to physicists:
Deﬁnition 33. The Fock space inner product is given by
(71) ⟨Ψ|Φ⟩ =
⟨
Ψ, Φ
⟩
Theorem 11. The Fock space inner product, for U (1)-stuﬀ types Ψ and Φ satisﬁes
|⟨Ψ|Φ⟩| =⟨|Ψ|||Φ|⟩, giving the usual conjugate-linear inner product on /BV [ [z] ].
Proof.
|⟨Ψ|Φ⟩| =
∑
n∈ /C6
|⟨Ψ|Φ⟩n|(72)
=
∑
n∈ /C6
|Ψ n|·| Φ n|
= ⟨|Ψ||| Φ|⟩
□
So for U (1)-stuﬀ types, we might want to deﬁne a new inner product given in
terms of the usual M -stuﬀ type inner product as ⟨Ψ|Φ⟩. We will discuss brieﬂy in
section 7.1.1 how to interpret this seemingly arbitrary innovation.
52 JEFFREY MORTON
It is worth noting here that the inner product between two states of a U (1)-stuﬀ
type may be zero. Of course, this can happen with stuﬀ types in any case: for
instance, if Ψ is the stuﬀ type for which there is one object in X over every even-
cardinality set, with automorphism group the same as that of the se t, and no others;
and Φ is similar, but has objects over odd-cardinality sets. These ha ve cardinalities
(generating functions) cosh(z) and sinh(z) respectively. They are examples of what
we called “property types” in section 4.4 - namely, these types can b e interpreted
as the properties “being an even set” and “being an odd set”. Thes e two stuﬀ types
are orthogonal in the sense that their inner product is zero. Here , the interpretation
is that there are no sets having both properties, and so the stuﬀ-type inner product
is the empty groupoid.
However, the situation with U (1)-types is more subtle: we may have a nonempty
inner product groupoid whose U (1)-groupoid cardinality happens to be zero. This
arises because we may now have negative (and indeed complex) cont ributions to the
sum giving this cardinality. This is related to the quantum mechanical p henomenon
of “destructive interference” between states. In our formalism , this interference
occurs when we apply the homomorphism h : /CA
+⊗U (1)→ /BV and its derived
variants.
We interpret the cardinality of the groupoid inner product as the us ual inner
product in quantum-mechanics. This is the amplitude for ﬁnding our s ystem in a
given state Φ after setting it up in a state Ψ, so this says this amplitud e (and hence
the probability) is zero.
So the transition amplitudes between some of the “pure” (decateg oriﬁed) states
of which ψ and φ are superpositions may be nonzero, but the phases with which
they appear may allow the transition between ψ and φ to have zero amplitude.
Thus, introducing phases allows destructive interference which ma kes otherwise
feasible transitions impossible. We will see in the next section that this issue of
phase is closely related to the concept of time evolution in quantum mechanics, and
the propagator.
In particular, in the harmonic oscillator, the phase of a state chang es over time,
with a frequency proportional to the energy of that state. This is the eﬀect of the
free propagator for a system, and it is an operator. So we must describe U (1)-stuﬀ
operators next, and this propagator in particular.
6.2.3. U (1)-Stuﬀ Operators and Time. We have already noted that M -stuﬀ oper-
ators act on M -stuﬀ types just like ordinary stuﬀ operators acting on stuﬀ type s,
except that the groupoids are now replaced by M -groupoids. The groupoid T Ψ for
anM -stuﬀ operator T and type Ψ then consists of pairs of objects t∈T andx∈ X
together with a bijection of their underlying sets. As with the produ ct groupoid,
this object is labelled by an element in M given by the product of the labels on t
and x. This is well deﬁned when M is Abelian, as in the case when M =U (1).
One class of U (1)-stuﬀ operators which is particularly relevant to quantum me-
chanics is that of the time evolution operators. These are operators which, when
applied to an M -stuﬀ type Ψ, produce an M -stuﬀ type Ψ ′ for which the M -labels
on the elements of the underlying sets have labels multiplied by a ﬁxed p hase in
U (1). An example of an object in such an operator, designated θ, is shown in ﬁgure
22. Here, we are showing the operator ET , “time evolution by T ”. We show an
object which will evolve a state with three quanta of energy. Here, eiT is the change
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 53
of phase corresponding to time evolution of a one-energy-quantu m state by T . A
state with three energy quanta changes phase by e 3iT .
1
p
2
p
3iTet
Figure 22. An Object in The U (1)-Stuﬀ Operator ET
Any object in ET has two projections - each to an underlying set of the same size.
This corresponds to the fact that in unperturbed time evolution no interactions are
occurring which would change the energy level of the system. An ob ject t in the
groupoid of ET , lying over sets with k quanta of energy. There will be just one
such object in ET for each ﬁnite set. It is labelled by the phase by which a state
withk quanta will change in time T . The operator ET acts on any U (1)-stuﬀ type
(categoriﬁed state) to give state to which this has evolved after a timeT . An object
of the resulting stuﬀ type is shown in ﬁgure 23.
1
p
2
p
θ3t
x,tα
Ψ x 1θ
Figure 23. An Object in The U (1)-Stuﬀ Type ET Ψ
The object in the groupoid of ET Ψ is the entire ensemble associated to the ﬁnite
setp2(t). It includes the object t∈ET itself, as well as x∈ X, their underlying sets
and the bijection αx,t between them, and also their associated labels e 3iθ and e iθ1.
This is an object in a product U (1)-groupoid: U (1)Gpd is a weak 2-category with
(weak) products, of which this is an example. This object in the prod uct groupoid
ET× X is labelled by the product of the labels on t and x, namely e iθ1 e3iθ.
Suppose the U (1)-stuﬀ type in question happens to just be Z k - the categoriﬁed
state with just k quanta of energy and no phase angle, or the property type “being
an k-element ﬁnite set labelled by 1 ∈ U (1)”. Then we get ET (Z k)∼= (eiθZ)k,
and the same fact holds as an equation for the complex cardinalities. So the U (1)-
cardinality of a k-elementU (1)-set changes by e ikθ in time T , since each quantum
picks up a phase rotation of e iθ in time T . In particular, the phase of an object in
54 JEFFREY MORTON
a categoriﬁed state changes with a frequency proportional to its energy (the size of
the underlying set).
Choosing time units so that θ =T , we get a phase change of e iT k on a state of
energy k. We can write this as ET = e iT N, where N is the number operator. To
prove this equality at the categoriﬁed level (using a categoriﬁcatio n of the expo-
nential such as we have already discussed) would require a fully cate goriﬁed version
of the complex numbers. However, for now we can observe that th is will be true
at the level of cardinalities, and take it as a deﬁnition. This arises phy sically from
the Hamiltonian formulation of quantum mechanics. We will not enter in to this in
detail, but note that the free Hamiltonian is just H0 =N , the number operator in
the exponent of the propagator, which measures the energy of a state.
Since e iT N has exactly one object for each cardinality, the product groupoid
eiT NΨ is equivalent to the groupoid whose objects are the same as those of X,
but whose U (1)-labellings have been multiplied by phases e iT k, for an object with
underlying set k. This is the groupoid of the state Ψ, time-evolved by T . Note
that time-evolution by −T will be given by a similar operator E−T = e −iT N: all
the object-labels are the inverses of those of ET . We will return to this point in
section 7.1.1.
In any case, using these propagators, and the U (1) version of inner product
groupoids whose objects resemble Feynman diagram for interactio ns, we recover
a combinatorial interpretation for many of the standard feature s of the quantum
mechanics of the harmonic oscillator.
6.2.4. Feynman Diagrams And Perturbation. Having found a categoriﬁcation of
the quantum harmonic oscillator, we know that transition amplitudes such as⟨
ψ,p ( φn
n! )ψ′
⟩
as a sum over Feynman diagrams. In physically realistic settings,
this sort of amplitude often arises when we consider the time-evolut ion of an os-
cillator which is perturbed. The free oscillator evolves in time according to the
operator ET = e −iT N described above. The perturbed oscillator, on the other
hand, describes a situation where the energy of the oscillator is mod iﬁed by an-
other term: it only approximately matches the description of the fr ee oscillator we
have been using. Physically, this represents a potential in which the oscillator is
moving. This means that the energy of the oscillator is changed by th e addition
of an extra term, V , which is some function of position, which we think of as a
potential energy, in addition to the energy in the oscillator proper.
In this case, time evolution can be calculated using the new energy, H =H0 +V .
IfV is a function of position, then since the position is proportional to a + a∗ =φ,
we have V = f (φ), for some function f . We will consider the case where f = p
is some polynomial (though naturally any analytic function can be app roximated
this way to some degree, so we can obtain successive approximation s by taking a
sequence of pk converging to f ). Since the energy for the free oscillator is already
quadratic in position, we assume that f has minimum degree at least 3. In this case,
at the decategoriﬁed level, the amplitudes for time evolution by time t associated
to the Hamiltonian H =N +V , are:
(73)
⟨
Z k|e−iT HZ l⟩
=
∞∑
n=0
∫
0≤t1≤···≤tn≤T
⟨
Z k|e−i(T −tn)NV e−i(tn−tn−1)NV ...V e−it1NZ l
⟩
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 55
To avoid considering questions of convergence, we think of this pur ely as a statement
about power series in T . It would take us too far aﬁeld to derive this standard
quantum-mechanical fact in full detail, though background can be found in [4], and
one derivation of this equation in our setting can be found in [2]. Howev er, we will
point out here that it follows from the fact that the evolution of a st ate is governed
by the Schr¨ odinger equation, which amounts to:
(74) ∂tψ =−i(eitH0V e−itH0 )
Integrating this equation over time, we get
(75) ψ(t) =−i
∫ t
0
(eitH0V e−itH0 )ψ(t0)dt0 +ψ(0)
and by repeated substitution of this expression for ψ(t) into the integral, we get the
sum of integrals which appear in the expression above. Taking the inn er product
with this operator, we ﬁnally get the whole expression.
Ideally, we would like to derive this equation entirely at the categoriﬁe d level.
However this would require a more complete understanding of the ca tegoriﬁed ver-
sion of the complex numbers than we have constructed here. To re cover time
evolution by a phase from an expression of the form e itH0 , we would need to see
that the result is indeed a phase in U (1).
However, knowing that the equation holds at the decategoriﬁed lev el allows us
to give a simple interpretation for the formula.
Theorem 12. The transition amplitude
⟨
zk|e−iT Hzl⟩
for the perturbed harmonic
oscillator with potential V = f (φ) is given by a sum over all Feynman diagrams
given as composites of those associated with V , from a state with k quanta to one
with l quanta. The sum is of an integral over all labellings of the ed ges of the
diagrams such that the total phase along all paths is e−iT .
Proof. This transition amplitude is the U (1)-groupoid cardinality of the inner prod-
uct
⟨
Z k|EiT HZ l⟩
, and given by 73. Consider the operator in that equation,
O = e −i(T −tn)NV e−i(tn−tn−1)NV ...V e−it1N
We know that the terms e −i(ti−ti−1)N are just free propagators, which contribute
a phase of e −i() for each quantum of energy. We can think of these operators as
having objects given by any number of “strands”, one for each qu antum, and each
strand labelled by a phase e −i(ti−ti−1), the total number giving the total phase
change associated to that energy.
Now consider the U (1)-stuﬀ operators V . Each of these operators has a groupoid
whose objects are naturally identiﬁed with Feynman diagrams of the sort associated
with V . These do not aﬀect phases.
Composing the operators together, we get all possible composites of Feynman
diagrams of the type associated to V , connected by diagrams whose eﬀect is to label
strands by phases associated to the time intervals between intera ctions. To ﬁnd the
total phase associated to such a composite, we multiply all phases. This is clearly
equivalent to multiplying the phases on any labelled edges which are join ed by the
composition to get a phase on the resulting edge, then multiplying the product of
all edges thus produced.
56 JEFFREY MORTON
The transition amplitude we want to recover is:
∞∑
n=0
∫
0≤t1≤···≤tn≤T
⟨
Z k|OZ l⟩
The sum taken over all n simply means that we are taking a groupoid containing all
possiblen-fold composites of this form. The integral over all n-part partitions of the
interval [0,T ] means each such diagram contributes a phase found by integratin g
over all possible ways of dividing the interval into free and interactio n parts. This
contribution is weighted by the size of the symmetry group, since th e inner product
inside the integral is just a U (1)-groupoid cardinality.
This proves the statement. □
This recovers the usual Feynman rules for calculating transition am plitudes in
the oscillator.
