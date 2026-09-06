---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-005-42-the-ambidextrous-adjunction
section_title: "The Ambidextrous Adjunction"
section_number: 4.2
pages: 16-18
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
gous to a standard result for set-valued presheaves (see, e.g. M acLane and Moerdijk
[14], Theorem 1.9.2). This is that functors between groupoids induce 2-linear maps
between the 2-vector spaces of V ect-presheaves on them. For Set-presheaves, there
will be a left and a right adjoint to this functor. For V ect-presheaves, these coin-
cide, as we have seen in Theorem 3.2.4 (an inspection of the proof sho ws that this
is essentially because a ﬁnite dimensional vector space V is naturally isomorphic
to its double dual V ††, while the analogous statement is false for sets). Thus, one
says that the “pushforward” map is an ambidextrous adjoint for the pullback. For
much more on ambidextrous adjunctions and their relation to TQFTs , see Lauda
[11]). This is one important motivation for the present work. We summ arize the
statement as follows.
Proposition 4.2.1. If X and Y are essentially ﬁnite groupoids, a functor f :
Y→ X gives two 2-linear maps between KV 2-vector spaces:
(41) f ∗ : [X, V ect]→[Y, V ect]
2-VECTOR SPACES AND GROUPOIDS 17
called “pullback along f ” and
(42) f∗ : [Y, V ect]→[X, V ect]
the (two-sided) adjoint to f ∗, called “pushforward along f ”
Proof. For any functor F : X→ V ect,
(43) f ∗(F ) = F◦ f
which is a functor from Y to V ect, the pullback of F along f .
To see that this is a 2-linear map, we recall that it is enough to show it is C-linear,
since then biproducts will automatically be preserved. But a linear co mbination of
maps in some hom-category in [ X, V ect] is taken by f ∗ to the corresponding linear
combination in the hom-category in [ Y, V ect], where maps are now between vector
spaces thought of over y∈ Y.
So indeed there is a 2-linear map f ∗. But then by Theorem 3.2.4, there is a
two-sided adjoint of f ∗, denoted f∗. □
Figure 4. A Functor F : Y→ X Between Groupoids
In Figure 4, we see the essential information contained in a functor of groupoids.
Any groupoid is equivalent to a skeletal one (that is, one with just on e object in
each isomorphism class), so we illustrate this case. A skeletal group oid can be seen
as a set of objects, each labelled by a group. A functor between gr oupoids is a
set map, where each “strand” of the set map (i.e. each pair ( yi, xj ) of source and
image under the map) is labelled by a homomorphism fi. This takes the group Gi
of automorphisms of the source yi to the group Hj of automorphisms of the target
xj.
It will be useful to have another, more explicit, way to describe the “pushfor-
ward” map than the matrix-dependent view of Theorem 3.2.4. Fortu nately, there
is a more intrinsic way to describe the 2-linear map f∗, the adjoint of f ∗.
Deﬁnition 4.2.2. For a given x∈ X, the comma category (f ↓ x) has objects
which are objects y∈ Y equipped with maps f (y)→ x in X, and morphisms which
18 JEFFREY C. MORTON
are morphisms a : y→ y′ whose images make the triangles
(44) f (y)
/d15/d15
f (a) /d47/d47 f (y′)
/d123/d123/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
x
in X commute. Given a V ect-presheaf G on Y, deﬁne f∗(G)(x) = colim G(f↓ x)—
a colimit in V ect.
The pushforward of a morphism b : x→ x′ in X, f∗(G)(b) : f∗(G)(x)→ f∗(G)(x′)
is the induced morphism.
The comma category is the appropriate categorical equivalent of a preimage—
rather than requiring f (y) = x, one accepts that they may be isomorphic, in dif-
ferent ways. So this colimit is a categoriﬁed equivalent of taking a sum over a
preimage. The result is the Kan extension of G along f .
Consider the eﬀect of f∗ on a 2-vector G : Y→ V ect by describing f∗G :
X→ V ect. If F : X→ V ect is as above, there should be a canonical isomor-
phism between [ G, f ∗(F )] (a hom-set in [ Y, V ect]) and [ p∗(G), F ] (a hom-set in
[X, V ect]).
The hom-set [ G, f ∗(F )] is found by ﬁrst taking the pullback of F along f . This
gives a presheaf on Y, namely F (f (−)). The hom-set is then the set of natural
transformations α : G→ f ∗F . Given an object y in Y, α picks a linear map
αy : F (f (y))→ G(y) subject to the naturality condition.
Now, we have seen that, given f : Y→ X, this f∗ : [ Y, V ect]→ [X, V ect]
is a 2-linear map, and an ambidextrous adjoint for f ∗. We would like to describe
