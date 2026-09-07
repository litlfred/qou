---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-004-4-kv-2-vector-spaces-and-finite-groupoids
section_title: "KV 2-Vector Spaces and Finite Groupoids"
section_number: 4
pages: 15-16
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
We have now seen that we can get a 2-vector space as a category o f functions
from some ﬁnite set S into V ect, and this may have extra structure if S does.
However, this is somewhat unnatural, since V ectis a category and S a mere set.
It seems more natural to consider functor categories into V ectfrom some category
C. These are examples of the generalized 2-vector spaces describe d by Elgueta
[8]. Then the above way of looking at a KV 2-vector space can be redu ced to the
situation when C is a discrete category with a ﬁnite set of objects. However, there
are interesting cases where C is not of this form, and the result is still a KV vector
space. A relevant class of examples, as we shall show, come from sp ecial kinds of
groupoids.
4.1. F ree 2-V ector Space on a Finite Groupoid. Since we want our 2-vector
spaces to have ﬁnitely many generators, we need a condition on the sorts of groupoids
we are talking about here. Of course, since often one works with to pological
groupoids which may be uncountable, the kind of ﬁniteness condition we will have
to apply seems restrictive. A full treatment of, for example, Lie gr oupoids, would
require much more consideration of inﬁnite dimensional 2-vector sp aces (and in-
deed 2-Hilbert spaces). In the meantime, we can only consider grou poids which are
essentially ﬁnite.
We ﬁrst show that essentially ﬁnite groupoids are among the special categories
C we want to consider:
Lemma 4.1.1. If X is an essentially ﬁnite groupoid, Rep(X) = [ X, V ect] is a
2-vector space
Proof. The groupoid X is equivalent its skeleton, X, which contains a single object
in each isomorphism class. Since X is essentially ﬁnite, this is a ﬁnite set of objects,
and each object has a ﬁnite group of endomorphisms. So
(38) X≃
∐
x∈X
Aut(x)
where the groups Aut(x) are seen as one-object groupoids.
Then
[X, V ect]≃
∏
x∈X
[Aut(x), V ect](39)
=
∏
x∈X
Rep(Aut(x))(40)
This inherits the biproducts from the categories Rep(Aut(x)). An irreducible
representation of an essentially ﬁnite groupoid amounts to a choice of isomorphism
class of objects [ x], and an irreducible representation of the group Aut(x). By
Schur’s Lemma, these are indeed simple objects, since irreducible re presentations
of a group are simple.
16 JEFFREY C. MORTON
□
We notice that we are speaking here of groupoids, and any groupoid X is equiv-
alent to its opposite category Xop, by an equivalence that leaves objects intact
and replaces each morphism by its inverse. So there is no real diﬀere nce between
[X, V ect], the category of V ect-valued functors from X, and [ Xop, V ect], the cate-
gory of V ect-valued presheaves (or just “ V ect-presheaves”) on X. (We also should
note that, since our groupoids are discrete, there is no distinction here between
sheaves and presheaves).
Figure 3 is an illustration of an object in [ X, V ect].
Figure 3. A V ect-valued Presheaf on X
We will use the terminology of “presheaves” for objects of [ X, V ect] for the
sake of highlighting the connection between these results and the u sual facts about
presheaves of sets in topos theory - which again raises questions a bout topologically
interesting groupoids. This will be addressed in later work, but for n ow we consider
the algebraic aspect of the 2-linearization construction by itself.
