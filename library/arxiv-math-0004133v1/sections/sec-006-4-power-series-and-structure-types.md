---
doc_id: arxiv-math-0004133v1
doc_title: "From Finite Sets to Feynman Diagrams"
section_id: sec-006-4-power-series-and-structure-types
section_title: "Power Series and Structure Types"
section_number: 4
pages: 17-22
source_pdf: 0004133v1.pdf
source_sha256: 687de8249639c7f2
doc_brief: "From Finite Sets to Feynman Diagrams — ‘Categoriﬁcation’ is the process of replacing equations by isomor- phisms."
---
In combinatorics, a standard problem is to count the number o f structures
of a given type that can be put on a ﬁnite set. For example, the n umber of
ways to linearly order an n-element set is n!, while the number of ways to
partition it into disjoint nonempty subsets is some more com plicated function
of n. Such counting problems can often be solved with almost magi cal ease
using formal power series [11, 25, 30].
The idea is simple. Let F be any type of structure that we can put on
ﬁnite sets, and let Fn be the set of all structures of this type that can be
put on your favorite n-element set (which we will simply call ‘ n’). Deﬁne the
generating function of F to be the formal power series
|F |(x) =
∞∑
n=0
|Fn|
n! xn.
Using this deﬁnition, operations on structure types corres pond to operations
on their generating functions.
For example, suppose we have two structure types F and G. Then we
can make up a new structure type F + G by saying that a structure of type
F + G on a ﬁnite set is the same as a structure of type F or a structure of
type G on this set. We count the structures of these two types as disj oint,
so number of ways to put a structure of type F + G on the n-element set is
|(F + G)n| = |Fn| + |Gn|.
We thus have the following relation between generating func tions:
|F + G| = |F | + |G|.
Similarly, we can make up a structure type F G as follows: to put a
structure of type F G on a ﬁnite set, we ﬁrst choose a way to chop this set
into two disjoint parts, and then put a structure of type F on the ﬁrst part
and a structure of type G on the second part. The number of ways to do
this for the n-element set is
|(F G)n| =
n∑
m=0
( n
m
)
|Fm| |Gn−m|,
17
so a little calculation shows that
|F G| = |F ||G|.
Simple structure types have simple power series as their gen erating func-
tions. For example, consider the impossible structure : by deﬁnition, there
are no ways to put this structure on any set. If we use use 0 to st and for the
impossible structure, we have
|0| = 0.
For that matter, consider the structure of being the empty set . There is one
way to put this struture on a set with 0 elements, and no ways to put it on a
set with n elements when n > 0, so the generating function of this stucture
type is just the power series 1. If we call this structure type ‘1’, we thus have
|1| = 1.
More generally, the structure of being an n-element set has the generating
function xn/n !. It follows that the vacuous structure — the structure of
‘being a ﬁnite set’ — has the generating function
ex = 1 + x + x2
2! + x3
3! + · · ·
Let us use these ideas to count something. Let B denote the structure
type of binary rooted trees [11]. For example, here is a way to put a structure
of type B on the set {1, . . . , 7}:
2
1
4
3
5
7
6
We can recursively deﬁne B as follows. First, there is exactly one way to put
a structure of type B on the empty set. Second, to put a structure of type
18
B on nonempty ﬁnite set S, we pick an element r ∈ S called the root, chop
the set S − {r} into two parts L and R called the left and right subtrees , and
put a structure of type B on L and on R. Translating this deﬁnition into an
equation using the method described above, we have
B = 1 + xB2.
In short: a binary rooted tree is either the empty set or a one- element set
together with two binary rooted trees! Thanks to the way thin gs are set up,
this equation gives rise to an identical-looking equation f or the generating
function |B|:
|B| = 1 + x|B|2.
Now comes the miracle. We can solve this equation for |B|:
|B|(x) = 1 − √1 − 4x
2x ,
and doing a Taylor expansion we get:
|B|(x) = 1 + x + 2x2 + 5x3 + 14x4 + 42x5 + · · ·
The coeﬃcients of this series are called the Catalan numbers , cn:
|B|(x) =
∞∑
n=0
cnxn
A little messing around with the binomial theorem shows that
cn = 1
n + 1
( 2n
n
)
,
so the number of ways to put a binary rooted tree structure on t he n-element
set is
|Bn| = n!cn = (2n)!
(n + 1)! .
What is really going on here? Joyal clariﬁed the subject imme nsely by
giving a precise deﬁnition of the ‘structure types’ we have a lready been using
here in an informal way. A structure type is a functor F : FinSet0 → FinSet.
For the reader who is not comfortable with functors, we can sp ell out exactly
19
what this means. First, a structure type assigns to any ﬁnite set S a set FS,
which we think of as the set of all structures of type F on S. Second, it
assigns to any bijection f : S → T a map Ff : FS → FT . These maps describe
how structures of type F transform under bijections. Third, we require that
Ff g = Ff Fg whenever f and g are composable.
Structure types form a category where the morphisms are ‘nat ural trans-
formations’ between functors — any decent book on category t heory will
explain what these are [22], but it doesn’t much matter here. The category
of structure types, which we call FinSet {x}, is a kind of categoriﬁed version
of the rig of formal power series
N{x} = {
∞∑
n=0
an
n! xn : an ∈ N}.
We have already seen how any structure type F determines a formal power
series |F | ∈ N{x}. In fact, the category FinSet {x} is a symmetric rig category
with the addition and multiplication operations already me ntioned. As a
result, its decategoriﬁcation is a commutative ring. This c ommutative ring
is not N{x}, since the isomorphism class of a structure type F contains more
information than the numbers |Fn|. However, there is a homomorphism from
the decategoriﬁcation of FinSet {x} onto N{x}.
In fact, one can make the analogy between power series and str ucture
types very precise [5]. But instead of doing this here, let us give an illustration
of just how far the analogy goes. Suppose F is a structure type and X is a
ﬁnite set. Deﬁne the groupoid F (X) as follows:
F (X) =
∞∑
n=0
(Fn × X n)/ /n ! .
Here n! stands for the group of permutations of the set n. This group acts
on Fn thanks to the deﬁnition of structure type, and it also acts on X n in
an obvious way, so we can form the weak quotient ( Fn × X n)/ /n !, which is a
groupoid. Taking the coproduct of all these groupoids, we ge t F (X). This is
the categoriﬁed version of evaluating a power series at a num ber. But unlike
the case of ordinary power series, there is no issue of conver gence!
The issue of convergence arises only when we decategorify. S ince groupoid
cardinality gets along nicely with coproducts and weak quot ients, we have
20
the formula
|F (X)| = |F |(|X|)
whenever both sides make sense. The left-hand side makes sen se when the
groupoid F (X) is tame. The right-hand side makes sense when the power
series |F |(x) converges at x = |X|. These two conditions are actually equiv-
alent.
This formula is good for calculating groupoid cardinalitie s. The groupoid
F (1) is particularly interesting because it is equivalent to the groupoid of
F -structured ﬁnite sets . The objects of this groupoid are ﬁnite sets equipped
with a structure of type F , and the morphisms are structure-preserving bi-
jections. When this groupoid is tame, its cardinality is |F |(1). For example,
if F is the vacuous structure, its generating function is |F |(x) = ex, and F (1)
is the groupoid of ﬁnite sets. Thus the cardinality of this gr oupoid is e, as
we have already seen. For a more interesting example, take a s tructure of
type P on a ﬁnite set to be a partition into disjoint nonempty subset s. Then
|P |(x) = eex−1,
so the cardinality of the groupoid of ﬁnite sets equipped wit h a partition is
ee−1. On the other hand, the groupoid of binary rooted trees is not tame,
because the power series |B|(x) diverges at x = 1. By analytic continuation
using the formula
|B|(x) = 1 − √1 − 4x
2x
one might assign this groupoid a cardinality of 1
2 −
√
3
2 i, ignoring the issue
of branch cuts. These ‘analytically continued cardinaliti es’ have interesting
properties, but it is far from clear what they mean!
Finally, let us mention some interesting generalizations o f structure types.
As we have seen, any structure type F determines a groupoid F (1), the
groupoid of F -structured ﬁnite sets. There is a functor U: F (1) → FinSet0
sending each F -structured ﬁnite set to its underlying set. It turns out tha t
this functor contains all the information in the structure t ype. Given suitable
ﬁniteness conditions, everything we have said about struct ure types actually
works for any groupoid G equipped with a functor U: G → FinSet0. Since
the objects of G can be thought of as ﬁnite sets together with extra ‘stuﬀ’,
we call a groupoid equipped with a functor to FinSet a stuﬀ type . For a good
21
example of a stuﬀ type that is not a structure type, take G to be the groupoid
whose objects are ordered n-tuples of ﬁnite sets and whose morphisms are
ordered n-tuples of bijections, and let U be the projection onto one entry. As
we shall see in the next section, stuﬀ types are important for understanding
the combinatorics of Feynman diagrams.
In fact, we can categorify the concept of ‘stuﬀ type’ inﬁnite ly many times!
If we do, we ultimately reach the notion of a space equipped wi th a contin-
uous function to the classifying space B(FinSet0). This notion allows for
a fascinating interplay between Feynman diagrams and homot opy theory.
Unfortunately, for the details the reader will have to turn e lsewhere [7].
