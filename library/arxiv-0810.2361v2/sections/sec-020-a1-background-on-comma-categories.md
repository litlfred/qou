---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-020-a1-background-on-comma-categories
section_title: "A.1. Background on Comma Categories"
section_number: null
pages: 41-43
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
comma categories, which play a role in our construction of our 2-functor Λ in
the composition of spans of groupoids, via weak pullback.
Deﬁnition A.1.1. Given a diagram of categories A
F→C
G
←B. Then an object in
the comma category (F ↓G) consists of a triple (a, f, b), where a ∈A and b ∈B
are objects, and f : F(a) →G(b) is a morphism in C. A morphism in (F ↓G) from
(a1, f1, b1) to (a2, f2, b2) consists of a pair of morphisms (h, k) ∈A × B making the
42
JEFFREY C. MORTON
square
(179)
F(a1)
f1
/
F (h)

G(b2)
G(k)

F(a2)
f2
/ G(b2)
commute.
Remark A.1.2. Note that in a weak pullback, the morphisms f would be required
to be an isomorphism, but when we are talking about a weak pullback of groupoids,
these conditions are the same.
The comma category has projection functors which complete the (weak) pullback
square for the two projections:
(180)
(F ↓G)
PA
{wwwwwwwww
PB
#G
G
G
G
G
G
G
G
G
A
F
$H
H
H
H
H
H
H
H
H
H
α
∼
+3 B
G
{vvvvvvvvvv
C
such that (F ↓G) is a universal object (in Cat) with maps into A and B making
the resulting square commute up to a natural isomorphism α. This satisﬁes the
universal condition that, given any other category D with maps to A and B, there
is an equivalence between [D, C] and the comma category (P ∗
A, P ∗
B) (where PS∗and
PT ∗are the functors from D to B which factor through PS and PT respectively).
This is the weak form of the universal property of a pullback.
So suppose we restrict to the case of a weak pullback of groupoids.
This is
equivalent to the situation where A, B and C are skeletal - that is, each is just
a disjoint union of groups. Then the set of objects of (F ↓G) is a disjoint union
over all the morphisms of C (which are all of the form g : x →x for some object
x) of all the pairs of objects a ∈A and b ∈B with g : F(a) →G(b). In particular,
since we assume C is skeletal, this means F(a) = G(b), though there will be an
instance of this pair in (F ↓G) for each g in the group of morphisms on this object
F(a) = G(b).
So as the set of objects in (F ↓G) we have a disjoint union of products of sets—
for each c ∈C, we get |Aut(c)| copies of F −1(c) × G−1(c). The set of morphisms
is just the collection of commuting squares as in (179) above.
Note that if we choose a particular c and g : c →c, and choose objects a, b with
F(a) = c, G(b) = c, and if H = Aut(a), K = Aut(b) and M = Aut(c), then the
group of automorphisms of (a, g, b) ∈(F ↓G) is isomorphic to the ﬁbred product
H ×M K. In particular, it is a subgroup of the product group H × K consisting
of only those pairs (h, k) with F(h)g = gG(k), or just F(h) = gG(k)g−1. We can
call it H ×M K, keeping in mind that this ﬁbred product depends on g. Clearly,
the group of automorphisms of two isomorphic objects in (F ↓G) are isomorphic
groups.
Now, as we saw when discussing comma squares, the objects of the weak pullback
X′ ◦X consist of pairs of objects, x ∈X, and x′ ∈X′, together with a morphism in
2-VECTOR SPACES AND GROUPOIDS
43
A2, g : t(x) →s′(x′). The morphisms from (x1, g1, x′1) to (x2, g2, x′2) in the weak
pullback are pairs of morphisms, (h, k) ∈X × X′, making the square
(181)
t(x1)
g1 /
t(h)

s′(x′2)
s′(k)

t(x2)
g2 / s′(x′2)
commute.
We may assume that the groupoids we begin with are skeletal—if not, we replace
the groupoid with its skeleton, so the objects are just isomorphism classes of the
original objects. Then recall from Section 5.1 that in this weak pullback the set of
objects in X′ ◦X is a disjoint union of products of sets - for each a ∈A2, we get
|Aut(a)| copies of t−1(a) × (s′)−1(a).
