---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-001-2-categories-and-connections
section_title: "Categories and Connections"
section_number: 2
pages: 3-11
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
A category consists of objects, which we draw as dots:
• x
and morphisms between objects, which we draw as arrows between dots:
x•
f
/d39/d39
•y
You should think of objects as ‘things’ and morphisms as ‘processes ’. The main
thing you can do in a category is take a morphism from x to y and a morphism
from y to z:
x•
f
/d39/d39 •y
g
/d39/d39 •z
and ‘compose’ them to get a morphism from x to z:
x•
gf
/d36/d36 •z
The most famous example is the category Set, which has sets as obj ects and
functions as morphisms. Most of us know how to compose functions , and we
have a pretty good intuition of how this works. So, it can be helpful t o think
of morphisms as being like functions. But as we shall soon see, there are some
very important categories where the morphisms are not functions.
Let us give the formal deﬁnition. A category consists of:
• A collection of objects, and
• for any pair of objects x, y, a set of morphisms f : x → y. Given a
morphism f : x → y, we call x its source and y its target.
• Given two morphisms f : x → y and g: y → z, there is a composite
morphism gf : x → z. Composition satisﬁes the associative law :
(hg)f = h(gf ).
• For any object x, there is an identity morphism 1x: x → x. These identity
morphisms satisfy the left and right unit laws :
1yf = f = f 1x
for any morphism f : x → y.
3
The hardest thing about category theory is getting your arrows t o point the
right way. It is standard in mathematics to use f g to denote the result of doing
ﬁrst g and then f . In pictures, this backwards convention can be annoying. But
rather than trying to ﬁght it, let us give in and draw a morphism f : x → y as
an arrow from right to left:
y• • x
f
/d119/d119
Then composition looks a bit better:
z• • y
f
/d119/d119 •x
g
/d119/d119 = z• • x
f g
/d119/d119
An important example of a category is the ‘path groupoid’ of a space X.
We give the precise deﬁnition below, but the basic idea is to take the dia grams
we have been drawing seriously! The objects are points in X, and morphisms
are paths:
y• • x
γ
/d2/d2
We also get examples from groups. A group is the same as a category with one
object where all the morphisms are invertible. The morphisms of this category
are the elements of the group. The object is there just to provide them with a
source and target. We compose the morphisms using the multiplicatio n in the
group.
In both these examples, a morphism f : x → y is not a function from x to y.
And these two examples have something else in common: they are impo rtant in
gauge theory! We can use a path groupoid to describe the possible m otions of
a particle through spacetime. We can use a group to describe the sy mmetries
of a particle. And when we combine these two examples, we get the co ncept of
connection—the basic ﬁeld in any gauge theory.
How do we combine these examples? We do it using a map between cate-
gories. A map between categories is called a ‘functor’. A functor fro m a path
groupoid to a group will send every object of the path groupoid to t he same
object of our group. After all, a group, regarded as a category, has only one
object. But this functor will also send any morphism in our path grou poid to
a group element. In other words, it will assign a group element to eac h path in
our space. This group element describes how a particle transforms as it moves
along that path.
But this is precisely what a connection does! A connection lets us com pute
for any path a group element describing parallel transport along th at path.
So, the language of categories and functors quickly leads us to the concept of
connection—but with an emphasis on parallel transport.
4
The following theorem makes these ideas precise. Let us ﬁrst state the
theorem, then deﬁne the terms involved, and then give some idea of how it is
proved:
Theorem 1. For any Lie group G and any smooth manifold M , there is a
one-to-one correspondence between:
1. connections on the trivial principal G-bundle over M ,
2. g-valued 1-forms on M , where g is the Lie algebra of G, and
3. smooth functors
hol: P1(M ) → G
where P1(M ) is the path groupoid of M .
We assume you are familiar with the ﬁrst two items. Our goal is to expla in the
third. We must start by explaining the path groupoid.
Suppose M is a manifold. Then the path groupoid P1(M ) is roughly a
category in which objects are points of M and a morphism from x to y is a path
from x to y. We compose paths by gluing them end to end. So, given a path δ
from x to y, and a path γ from y to z:
z• y•
γ
/d2/d2
x•
δ
/d2/d2
we would like γδ to be the path from x to z built from γ and δ.
However, we need to be careful about the details to make sure tha t the
composite path γδ is well-deﬁned, and that composition is associative! Since we
are studying paths in a smooth manifold, we want them to be smooth. But the
path γδ may not be smooth: there could be a ‘kink’ at the point y.
There are diﬀerent ways to get around this problem. One is to work w ith
piecewise smooth paths. But here is another approach: say that a path
γ: [0, 1] → M
is lazy if it is smooth and also constant in a neighborhood of t = 0 and t = 1.
The idea is that a lazy hiker takes a rest before starting a hike, and a lso after
completing it. Suppose γ and δ are smooth paths and γ starts where δ ends.
Then we deﬁne their composite
γδ: [0, 1] → M
in the usual way:
(γδ)(t) =
{ δ(2t) if 0 ≤ t ≤ 1
2
γ(2t − 1) if 1
2 ≤ t ≤ 1
5
In other words, γδ spends the ﬁrst half of its time moving along δ, and the
second half moving along γ. In general the path γδ may not be smooth at
t = 1
2 . However, if γ and δ are lazy, then their composite is smooth—and it,
too, is lazy!
So, lazy paths are closed under composition. Unfortunately, comp osition of
lazy paths is not associative. The paths ( αβ)γ and α(βγ ) diﬀer by a smooth
reparametrization, but they are not equal. To solve this problem, w e can take
certain equivalence classes of lazy paths as morphisms in the path groupoid.
We might try ‘homotopy classes’ of paths. Remember, a homotopy is a way
of interpolating between paths:
y• • x
δ
/d103/d103
γ
/d119/d119
Σ/d11/d19
More precisely, a homotopy from the path γ: [0, 1] → M to the path δ: [0, 1] →
M is a smooth map
Σ: [0 , 1]2 → M
such that Σ(0 , t) = γ(t) and Σ(1 , t) = δ(t). We say two paths are homotopic,
or lie in the same homotopy class , if there is a homotopy between them.
There is a well-deﬁned category where the morphisms are homotopy classes
of lazy paths. Unfortunately this is not right for gauge theory, sin ce for most
connections, parallel transport along homotopic paths gives diﬀer ent results. In
fact, parallel transport gives the same result for all homotopic pa ths if and only
if the connection is ﬂat.
So, unless we are willing to settle for ﬂat connections, we need a more delicate
equivalence relation between paths. Here the concept of ‘thin’ hom otopy comes
to our rescue. A homotopy is thin if it sweeps out a surface that has zero area.
In other words, it is a homotopy Σ such that the rank of the diﬀeren tial dΣ is
less than 2 at every point. If two paths diﬀer by a smooth reparame trization,
they are thinly homotopic. But there are other examples, too. For example,
suppose we have a path γ: x → y, and let γ−1: y → x be the reverse path,
deﬁned as follows:
γ−1(t) = γ(1 − t).
Then the composite path γ−1γ, which goes from x to itself:
y• • x/d28/d28
γ−1
γ
/d2/d2
is thinly homotopic to the constant path that sits at x. The reason is that we
can shrink γ−1γ down to the constant path without sweeping out any area.
We deﬁne the path groupoid P1(M ) to be the category where:
• Objects are points of M .
6
• Morphisms are thin homotopy classes of lazy paths in M .
• If we write [γ] to denote the thin homotopy class of the path γ, composition
is deﬁned by
[γ][δ] = [ γδ].
• For any point x ∈ M , the identity 1 x is the thin homotopy class of the
constant path at x.
With these rules, it is easy to check that P1(M ) is a category. The most
important point is that since the composite paths ( αβ)γ and α(βγ ) diﬀer by a
smooth reparametrization, they are thinly homotopic. This gives th e associative
law when we work with thin homotopy classes.
But as its name suggests, P1(M ) is better than a mere category. It is a
groupoid: that is, a category where every morphism γ: x → y has an inverse
γ−1: y → x satisfying
γ−1γ = 1 x and γγ −1 = 1 y
In P1(M ), the inverse is deﬁned using the concept of a reverse path:
[γ]−1 = [γ−1].
The rules for an inverse only hold in P1(M ) after we take thin homotopy classes.
After all, the composites γγ −1 and γ−1γ are not constant paths, but they are
thinly homotopic to constant paths. But henceforth, we will relax a nd write
simply γ for the morphism in the path groupoid corresponding to a path γ,
instead of [ γ].
As the name suggests, groupoids are a bit like groups. Indeed, a group is
secretly the same as a groupoid with one object! In other words, s uppose we
have group G. Then there is a category where:
• There is only one object, •.
• Morphisms from • to • are elements of G.
• Composition of morphisms is multiplication in the group G.
• The identity morphism 1 • is the identity element of G.
This category is a groupoid, since every group element has an invers e. Con-
versely, any groupoid with one object gives a group. Henceforth w e will freely
switch back and forth between thinking of a group in the traditional way, and
thinking of it as a one-object groupoid.
How can we use groupoids to describe connections? It should not be sur-
prising that we can do this, now that we have our path groupoid P1(M ) and
our one-object groupoid G in hand. A connection gives a map from P1(M ) to
G, which says how to transform a particle when we move it along a path. More
precisely: if G is a Lie group, any connection on the trivial G-bundle over M
7
yields a map, called the parallel transport map or holonomy, that assigns an
element of G to each path:
hol: • •
γ
/d118/d118 ↦→ hol(γ) ∈ G
In physics notation, the holonomy is deﬁned as the path-ordered e xponential of
some g-valued 1-form A, where g is the Lie algebra of G:
hol(γ) = P exp
( ∫
γ
A
)
∈ G.
The holonomy map satisﬁes certain rules, most of which are summariz ed in
the word ‘functor’. What is a functor? It is a map between categorie s that
preserves all the structure in sight!
More precisely: given categories C and D, a functor F : C → D consists of:
• a map F sending objects in C to objects in D, and
• another map, also called F , sending morphisms in C to morphisms in D,
such that:
• given a morphism f : x → y in C, we have F (f ): F (x) → F (y),
• F preserves composition:
F (f g) = F (f )F (g)
when either side is well-deﬁned, and
• F preserves identities:
F (1x) = 1 F (x)
for every object x of C.
The last property actually follows from the rest. The second to last —preserving
composition—is the most important property of functors. As a tes t of your
understanding, check that if C and D are just groups (that is, one-object
groupoids) then a functor F : C → D is just a homomorphism.
Let us see what this deﬁnition says about a functor
hol: P1(M ) → G
where G is some Lie group. This functor hol must send all the points of M to
the one object of G. More interestingly, it must send thin homotopy classes of
paths in M to elements of G:
hol: • •
γ
/d118/d118 ↦→ hol(γ) ∈ G
8
It must preserve composition:
hol(γδ) = hol( γ) hol(δ)
and identities:
hol(1x) = 1 ∈ G.
While they may be stated in unfamiliar language, these are actually well-
known properties of connections! First, the holonomy of a connec tion along a
path
hol(γ) = P exp
( ∫
γ
A
)
∈ G
only depends on the thin homotopy class of γ. To see this, compute the variation
of hol( γ) as we vary the path γ, and show the variation is zero if the homotopy
is thin. Second, to compute the group element for a composite of pa ths, we just
multiply the group elements for each one:
P exp
( ∫
γδ
A
)
= P exp
( ∫
γ
A
)
P exp
( ∫
δ
A
)
And third, the path-ordered exponential along a constant path is just the iden-
tity:
P exp
( ∫
1x
A
)
= 1 ∈ G.
All this information is neatly captured by saying hol is a functor. And
Theorem 1 says this is almost all there is to being a connection. The on ly
additional condition required is that hol be smooth. This means, roughly, that
hol(γ) depends smoothly on the path γ—more on that later. But if we drop this
condition, we can generalize the concept of connection, and deﬁne a generalized
connection on a smooth manifold M to be a functor hol: P1(M ) → G.
Generalized connections have long played an important role in loop qua n-
tum gravity, ﬁrst in the context of real-analytic manifolds [3], and lat er for
smooth manifolds [17, 65]. The reason is that if M is any manifold and G
is a connected compact Lie group, there is a natural measure on th e space of
generalized connections. This means that you can deﬁne a Hilbert sp ace of
complex-valued square-integrable functions on the space of gene ralized connec-
tions. In loop quantum gravity these are used to describe quantum states before
any constraints have been imposed. The switch from connections t o generalized
connections is crucial here—and the lack of smoothness gives loop q uantum
gravity its ‘discrete’ ﬂavor.
But suppose we are interested in ordinary connections. Then we re ally want
hol(γ) to depend smoothly on the path γ. How can we make this precise?
One way is to use the theory of ‘smooth groupoids’ [16]. Any Lie grou p
is a smooth groupoid, and so is the path groupoid of any smooth manif old.
We can deﬁne smooth functors between smooth groupoids, and th en smooth
functors hol: P1(M ) → G are in one-to-one correspondence with connections on
9
the trivial principal G-bundle over M . We can go even further: there are more
general maps between smooth groupoids, and maps hol: P1(M ) → G of this
more general sort correspond to connections on not necessarily trivial principal
G-bundles over M . For details, see the work of Bartels [25], Schreiber and
Waldorf [87].
But if this sounds like too much work, we can take the following shortc ut.
Suppose we have a smooth function F : [0, 1]n × [0, 1] → M , which we think of
as a parametrized family of paths. And suppose that for each ﬁxed value of the
parameter s ∈ [0, 1]n, the path γs given by
γs(t) = F (s, t)
is lazy. Then our functor hol: P1(M ) → G gives a function
[0, 1]n → G
s ↦→ hol(γs).
If this function is smooth whenever F has the above properties, then the functor
hol: P1(M ) → G is smooth.
Starting from this deﬁnition one can prove the following lemma, which lie s
at the heart of Theorem 1:
Lemma. There is a one-to-one correspondence between smooth functo rs
hol: P1(M ) → G and Lie(G)-valued 1-forms A on M .
The idea is that given a Lie( G)-valued 1-form A on M , we can deﬁne a
holonomy for any smooth path as follows:
hol(γ) = P exp
( ∫
γ
A
)
,
and then check that this deﬁnes a smooth functor hol: P1(M ) → G. Conversely,
suppose we have a smooth functor hol of this sort. Then we can de ﬁne hol( γ)
for smooth paths γ that are not lazy, using the fact that every smooth path is
thinly homotopic to a lazy one. We can even do this for paths γ: [0, s] → M
where s ⁄= 1, since any such path can be reparametrized to give a path of the
usual sort. Given a smooth path
γ: [0, 1] → M
we can truncate it to obtain a path γs that goes along γ until time s:
γs: [0, s] → M.
By what we have said, hol( γs) is well-deﬁned. Using the fact that hol: P1(M ) →
G is a smooth functor, one can check that hol( γs) varies smoothly with s. So,
we can diﬀerentiate it and deﬁne a Lie( G)-valued 1-form A as follows:
A(v) = d
ds hol(γs)
⏐
⏐
s=0
10
where v is any tangent vector at a point x ∈ M , and γ is any smooth path with
γ(0) = x, γ ′(0) = v.
Of course, we need to check that A is well-deﬁned and smooth. We also need to
check that if we start with a smooth functor hol, construct a 1-fo rm A in this
way, and then turn A back into a smooth functor, we wind up back where we
started.
