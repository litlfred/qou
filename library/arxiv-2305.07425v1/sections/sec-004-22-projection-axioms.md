---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-004-22-projection-axioms
section_title: "Projection axioms"
section_number: 2.2
pages: 5-6
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
machinery developed in [BBF15] to obtain actions on quasi-t rees. In this section, we review
this machinery.
Deﬁnition 2.7. Let Y be a collection of geodesic spaces equipped with projection maps
{πY : Y \ {Y } → Y }Y ∈Y.
Let dY (X,Z ) = diam(πY (X) ∪πY (Z)) for X ⁄=Y ⁄=Z ∈ Y. The pair ( Y, {πY }Y ∈Y) satisﬁes
the projection axioms for a projection constant ξ ≥ 0 if
(1) diam(πY (X)) ≤ξ wheneverX ⁄=Y ;
(2) if X,Y,Z are distinct and dY (X,Z )>ξ , then dX (Y,Z ) ≤ξ; and
(3) for X ⁄=Z, the set {Y ∈ Y | dY (X,Z )>ξ } is ﬁnite.
For a ﬁxed K >0 and a pair ( Y,π Y ) satisfying the projection axioms for some constant ξ,
Bestvina, Bromberg, and Fujiwara construct a quasi-tree of spaces CK(Y) in [BBF15]. If Y
admits an action of the group G so that πgY (gX ) = gπY (X) for any g ∈ G and X,Y ∈ Y,
thenG acts by isometries on CK(Y); see Section 4.4 in [BBF15]. Moreover, they show that if
K >4ξ and Y is a collection of metric spaces uniformly quasi-isometric to R, then CK(Y) is
an unbounded quasi-tree [BBF15, Theorem 4.14].
The following is a useful example to keep in mind throughout t he paper and is discussed
in detail in the introduction of [BBF15].
Example 2.8. Let G be a discrete group of isometries of H2 and g1,...,g k ∈ G a ﬁnite
collection of loxodromic elements with axes γ1,...,γ k, respectively. Let Y be the set of all
G–translates of γ1,...,γ k, and given Y ∈ Y, deﬁne πY to be closest point projection in H2.
Since all translates of each γi are convex, this is a well-deﬁned 1–Lipschitz map, and it fol lows
from hyperbolicity that the projection of one translate of a n axis onto another has uniformly
bounded diameter. In [BBF15] it is veriﬁed that the pair ( Y,π Y ) satisﬁes the projection
axioms for some constant ξ.
Given a pair ( Y, {πY }Y ∈Y) satisfying the projection axioms and three domains X,Y,Z ∈ Y,
there is a notion of distance between a point of X and a point of Z from the point of view
of Y , which we now describe. Let x ∈ X and z ∈ Z. If X,Y,Z are all distinct, then deﬁne
dY (x,z ) :=dY (X,Z ). If Y =X andY ⁄=Z, then deﬁne dY (x,z ) := diam({x}∪πY (z)), where
the diameter is measured in Y . Finally, if X =Y =Z, then let dY (x,z ) be the distance in Y
betweenx andz. The spaces Y ∈ Y naturally embed into CK(Y), so the distance dCK (Y)(x,z )
is also deﬁned.
We have the following upper bound on distance in CK (Y). Set [ t]K = t if t ≥ K and
[t]K = 0 if t<K .
Proposition 2.9 ([BBF15, Lemma 4.4]) . Let (Y,π Y ∈Y) satisfy the projection axioms with
constantξ. For any K suﬃciently large,
dCK (Y)(x,z ) ≤ 6K + 4
∑
Y ∈Y
[dY (x,z )]K.
This distance formula was originally stated with a modiﬁed d istance function. In [BBF15]
the distance deﬁned above was denoted dπ
Y , and the modiﬁed distance was denoted dY . How-
ever, since dY (x,z ) ≤ dπ
Y (x,z ) for all point x,z , the inequality holds with the distance dπ
Y ,
as well. As we will not need the modiﬁed distance function in t his paper, we use the simpler
notation dY for dπ
Y and choose to state the proposition with this distance.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 6
