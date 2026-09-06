---
doc_id: arxiv-math-0004133v1
doc_title: "From Finite Sets to Feynman Diagrams"
section_id: sec-003-x-note-that-π-1x-is-far-more-informative-than-π
section_title: "Note that Π 1(X) is far more informative than Π 0(X), because it records"
section_number: X
pages: 5-7
source_pdf: 0004133v1.pdf
source_sha256: 687de8249639c7f2
doc_brief: "From Finite Sets to Feynman Diagrams — ‘Categoriﬁcation’ is the process of replacing equations by isomor- phisms."
---
not just whether one can get from here to there, but also a bit a bout the
path taken. In fact, one can make quite precise the sense in wh ich Π 1 is a
stronger invariant than Π 0. We say X is a homotopy n-type if it is locally
well-behaved (e.g. a CW complex) and any continuous map f : Sk → X is
5
contractible to a point when k > n . If X is a homotopy 0-type, we can
classify it up to homotopy equivalence using Π 0(X). This is not true if X is
a homotopy 1-type. However, if X is a homotopy 1-type, we can classify it
up to homotopy equivalence using Π 1(X).
There is a suggestive pattern here. To see how it continues, w e need
to categorify the notion of category itself! This gives the c oncept of a ‘2-
category’ or ‘bicategory’ [10, 20]. We will not give the full deﬁnitions here, but
the basic idea is that a 2-category has objects, morphisms be tween objects,
and also 2-morphisms between morphisms, like this:
/0
/0
/1
/1
/0/0
/0/0
/1/1
/1/1
Just as a category allows us to distinguish between equality and isomorphism
for objects, a 2-category allows us to make this distinction for morphisms.
From any space X we can form a 2-category Π 2(X) whose objects are
points of X, whose 1-morphisms are paths in X, and whose 2-morphisms are
homotopy classes of ‘paths of paths’. In fact this 2-categor y is a 2-groupoid,
meaning that every 2-morphism is invertible and every morph ism is invertible
up to a 2-morphism. We call Π 2(X) the fundamental 2-groupoid of X. If X
is a homotopy 2-type, we can classify it up to homotopy equiva lence using
Π 2(X). Moreover, if we decategorify Π 2(X) by treating homotopic paths as
equal, we get back Π 1(X).
Going still further, Grothendieck [14] proposed that if we t ake the notion
of ‘set’ and categorify it n times, we should obtain a notion of n-category:
a structure with objects, morphisms between objects, 2-mor phisms between
morphisms and so on up to n-morphisms. Any space X should give us an
n-category Π n(X) whose objects are the points of X, whose morphisms are
paths in X, whose 2-morphisms are paths of paths, and so on... with the
n-morphisms being homotopy classes of n-fold paths. In this n-category all
the j-morphisms are equivalences, meaning that for j = n that they are
invertible, while for j < n they are invertible up to equivalence. We call
an n-category with this property an n-groupoid. Given any decent deﬁnition
of n-categories, n-groupoids should be essentially the same as homotopy n-
types.
6
In short, by iterated categoriﬁcation, the whole of homotop y theory should
spring forth naturally from pure algebra! This dream is well on its way to
being realized, but it still holds many challenges for mathe matics. Various
deﬁnitions of n-category have been proposed [5, 9, 23, 28], and for some
of these the notion of fundamental n-groupoid has already been explored.
However, nobody has yet shown that these diﬀerent deﬁnition s are equiva-
lent. Finding a clear treatment of n-categories is a major task for the century
to come.
