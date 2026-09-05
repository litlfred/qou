---
doc_id: arxiv-math-0004133v1
doc_title: "From Finite Sets to Feynman Diagrams"
section_id: sec-002-2-equality-and-isomorphism
section_title: "Equality and Isomorphism"
section_number: 2
pages: 3-5
source_pdf: 0004133v1.pdf
source_sha256: 687de8249639c7f2
doc_brief: "From Finite Sets to Feynman Diagrams — ‘Categoriﬁcation’ is the process of replacing equations by isomor- phisms."
---
One of the most fundamental notions in mathematics is that of equality.
For the most part we take it for granted: we say an equation exp resses the
identity of a thing and itself. But the curious thing is that a n equation is
only interesting or useful to the extent that the two sides ar e diﬀerent! The
one equation that truly expresses identity,
x = x,
is precisely the one that is completely boring and useless. I nteresting equa-
tions do not merely express the identity of a thing and itself ; instead, they
hint at the existence of a reversible transformation that ta kes us from the
quantity on one side to the quantity on the other.
To make this more precise, we need the concept of a category. A set has
elements, and two elements are either equal or not — it’s a yes -or-no business.
A category is a subtler structure: it has objects but also mor phisms between
objects, which we can compose in an associative way. Every ob ject x has an
identity morphism
1x: x → x
which serves as a left and right unit for composition; this mo rphism de-
scribes the process of going from x to x by doing nothing at all. But more
interestingly, we say a morphism
f : x → y
is an isomorphism if there is a morphism g: y → x with f g = 1 y, gf =
1x. An isomorphism describes a reversible transformation goi ng from x to
y. Isomorphism is not a yes-or-no business, because two objec ts can be
isomorphic in more than one way. Indeed, the notion of ‘symme try’ arises
3
precisely from the fact that an object can be isomorphic to it self in many
ways: for any object x, the set of isomorphisms f : x → x forms a group called
its symmetry group or automorphism group , aut( x).
Now, given a category C, we may ‘decategorify’ it by forgetting about
the morphisms and pretending that isomorphic objects are eq ual. We are
left with a set (or class) whose elements are isomorphism cla sses of objects
of C. This process is dangerous, because it destroys useful info rmation. It
amounts to forgetting which road we took from x to y, and just remembering
that we got there. Sometimes this is actually useful, but mos t of the time
people do it unconsciously, out of mathematical naivete. We write equations,
when we really should specify isomorphisms. ‘Categoriﬁcat ion’ is the attempt
to undo this mistake. Like any attempt to restore lost inform ation, it not
a completely systematic process. Its importance is that it b rings to light
previously hidden mathematical structures, and clariﬁes t hings that would
otherwise remain mysterious. It seems strange and complica ted at ﬁrst, but
ultimately the goal is to make things simpler.
We like to illustrate this with the parable of the shepherd. L ong ago,
when shepherds wanted to see if two herds of sheep were isomor phic, they
would look for a speciﬁc isomorphism. In other words, they wo uld line up
both herds and try to match each sheep in one herd with a sheep i n the
other. But one day, a shepherd invented decategoriﬁcation. She realized one
could take each herd and ‘count’ it, setting up an isomorphis m between it
and a set of ‘numbers’, which were nonsense words like ‘one, t wo, three, . . . ’
specially designed for this purpose. By comparing the resul ting numbers, she
could show that two herds were isomorphic without explicitl y establishing
an isomorphism! In short, the set N of natural numbers was created by
decategorifying FinSet, the category whose objects are ﬁni te sets and whose
morphisms are functions between these.
Starting with the natural numbers, the shepherds then inven ted the basic
operations of arithmetic by decategorifying important ope rations on ﬁnite
sets: disjoint union, Cartesian product, and so on. We descr ibe this in detail
in the next section. Later, their descendants found it usefu l to extend N
to larger number systems with better formal properties: the integers, the
rationals, the real and complex numbers, and so on. These mak e it easier to
prove a vast range of theorems, even theorems that are just ab out natural
numbers. But in the process, the original connection to the c ategory of ﬁnite
sets was obscured.
4
Now we are in the position of having an enormous body of mathem atics,
large parts of which are secretly the decategoriﬁed residues of deeper truths,
without knowing exactly which parts these are. For example, any equation
involving natural numbers may be the decategoriﬁcation of a n isomorphism
between ﬁnite sets. In combinatorics, when people ﬁnd an iso morphism ex-
plaining such an equation, they say they have found a ‘biject ive proof’ of it.
But decategoriﬁcation lurks in many other places as well, an d wherever we
ﬁnd it, we have the opportunity to understand things more dee ply by go-
ing back and categorifying: working with objects directly, rather than their
isomorphism classes.
For example, the ‘representation ring’ of a group is a decategoriﬁed version
of its category of representations, with characters servin g as stand-ins for the
representations themselves. The ‘Burnside ring’ of a group is a decategoriﬁed
version of its category of actions on ﬁnite sets. The ‘K-theo ry’ of a topological
space is a decategoriﬁed version of the category of vector bu ndles over this
space. And the ‘Picard group’ of a variety is obtained by deca tegorifying the
category of line bundles over this variety. In all mathemati cs involving these
ideas and their many generalizations, there is room for cate goriﬁcation.
Actually, in the ﬁrst three examples above, decategoriﬁcat ion has been fol-
lowed by the process of adjoining formal additive inverses, just as we obtained
the integers by ﬁrst decategorifying FinSet and then adjoin ing the negative
numbers. Apart from ignorance of categories, the desire for additive inverses
may be the main reason mathematicians indulge in decategori ﬁcation. This
makes it very important to understand additive inverses in t he categoriﬁed
context. We touch upon this issue in the next section.
When one digs more deeply into categoriﬁcation, one quickly hits upon
homotopy theory. The reason is as follows. Starting with a to pological space
X, we can form a category Π 1(X) whose objects are the points of X and
whose morphisms f : x → y are homotopy classes of paths from x to y. This
category is a groupoid, meaning that all its morphisms are isomorphisms
[12, 29]. We call it the fundamental groupoid of X.
If we decategorify Π 1(X), we obtain the set Π 0(X) of path components of
