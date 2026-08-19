---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-002-3-2-categories-and-2-connections
section_title: "2-Categories and 2-Connections"
section_number: 3
pages: 11-14
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
Now we want to climb up one dimension, and talk about ‘2-connections’. A
connection tells us how particles transform as they move along path s. A 2-
connection will also tell us how strings transform as they sweep out surfaces. To
make this idea precise, we need to take everything we said in the prev ious section
and boost the dimension by one. Instead of categories, we need ‘2- categories’.
Instead of groups, we need ‘2-groups’. Instead of the path grou poid, we need
the ‘path 2-groupoid’. And instead of functors, we need ‘2-functo rs’. When
we understand all these things, the analogue of Theorem 1 will look s trikingly
similar to the original version:
Theorem. For any Lie 2-group G and any smooth manifold M , there is a
one-to-one correspondence between:
1. 2-connections on the trivial principal G-2-bundle over M ,
2. pairs consisting of a smooth g-valued 1-form A and a smooth h-valued
2-form B on M , such that
t
(B) = dA + A ∧ A
where we use t: h → g, the diﬀerential of the map t: H → G, to convert B
into a g-valued 2-form, and
3. smooth 2-functors
hol: P2(M ) → G
where P2(M ) is the path 2-groupoid of M .
What does this say? In brief: there is a way to extract from a Lie 2-g roup
G a pair of Lie groups G and H. Suppose we have a 1-form A taking values in
the Lie algebra of G, and a 2-form B valued in the Lie algebra of H. Suppose
furthermore that these forms obey the equation above. Then we can use them
to consistently deﬁne parallel transport, or ‘holonomies’, for path s and surfaces.
They thus deﬁne a ‘2-connection’.
That is the idea. But to make it precise, we need 2-categories.
11
3.1 2-Categories
Sets have elements. Categories have elements, usually called ‘objec ts’, but also
morphisms between these. In an ‘ n-category’, we go further and include 2-
morphisms between morphisms, 3-morphisms between 2-morphisms ,... and so
on up to the nth level. We are beginning to see n-categories provide an algebraic
language for n-dimensional structures in physics [12]. Higher gauge theory is
just one place where this is happening.
Anyone learning n-categories needs to start with 2-categories [63]. A 2-
category consists of:
• a collection of objects,
• for any pair of objects x and y, a set of morphisms f : x → y:
y• • x
f
/d117/d117
• for any pair of morphisms f, g: x → y, a set of 2-morphisms α: f ⇒ g:
y• • x
g
/d103/d103
f
/d119/d119 α/d11/d19
We call f the source of α and g the target of α.
Morphisms can be composed just as in a category:
z• • y
f
/d119/d119 •x
g
/d119/d119 = z• • x
f g
/d119/d119
while 2-morphisms can be composed in two distinct ways, vertically:
y• • x
f
/d0/d0 f ′
/d111/d111
f ′′
/d96/d96
α
/d11/d19
α′
/d11/d19
= y• • x
f
/d120/d120
f ′′
/d102/d102 α′·α
/d11/d19
and horizontally:
z• y•
f1
/d118/d118
f ′
1
/d104/d104 α1
/d11/d19 •x
f2
/d119/d119
f ′
2
/d103/d103 α2
/d11/d19 = z• • x
f1f2
/d120/d120
f ′
1f ′
2
/d102/d102 α1◦α2
/d11/d19
Finally, these laws must hold:
12
• Composition of morphisms is associative, and every object x has a mor-
phism
x• • x
1x
/d117/d117
serving as an identity for composition, just as in an ordinary catego ry.
• Vertical composition is associative, and every morphism f has a 2-morphism
y• • x
f
/d103/d103
f
/d119/d119
1f/d11/d19
serving as an identity for vertical composition.
• Horizontal composition is associative, and the 2-morphism
x• • x
1x
/d104/d104
1x
/d118/d118
11x/d11/d19
serves as an identity for horizontal composition.
• Vertical and horizontal composition of 2-morphisms obey the interchange
law:
(α′
1 · α1) ◦ (α′
2 · α2) = ( α′
1 ◦ α′
2) · (α1 ◦ α2)
so that diagrams of the form
x• y•
f1
/d124/d124
f ′
1/d111/d111
f ′′
1
/d98/d98
α1
/d11/d19
α′
1/d11/d19
•z
f2
/d124/d124 f ′
2/d111/d111
f ′′
2
/d99/d99
α2
/d11/d19
α′
2/d11/d19
deﬁne unambiguous 2-morphisms.
The interchange law is the truly new thing here. A category is all abou t
attaching 1-dimensional arrows end to end, and we need the assoc iative law to
do that unambiguously. In a 2-category, we visualize the 2-morphis ms as little
pieces of 2-dimensional surface:
• •/d102/d102/d120/d120
/d11/d19
We can attach these together in two ways: vertically and horizonta lly. For
the result to be unambiguous, we need not only associative laws but a lso the
interchange law. In what follows we will see this law turning up all over t he
place.
13
