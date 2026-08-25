---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-020-131-the-tree
section_title: "The tree"
section_number: 1.3.1
pages: 30-31
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
Let K be an extension ofk, we deﬁne ak-discrete valuation as a surjective map
v : K→ Z∪{∞} such that
— v(0) = +∞
— v(x +y)≥ min(v(x),v (y))
— v(xy) =v(x) +v(y)
—∀z∈k,v (z) = 0 and k is maximal for this property.
WecallOv ={x∈ K :v(x)≥ 0}the valuation ring,andwepick t∈O v anelementof
valuation 1, that we call auniformizing parameter. The group of invertible elements
O∗
v is the group of elements whose valuation is zero,(t) is the unique maximal ideal
ofOv,Ov/(t)≃k is theresidual ﬁeld. Remark that every ideal is of the form(tn),
for somen∈ N. The main exemple to have in mind here is the valuation ringC[[t]]
of formal series int, with the valuationv : C((t))∗→ Z,P ↦→ ordt(P ) given by the
vanishing order att = 0. The uniformizing element ist and the residual ﬁeld isC.
A lattice L in a two dimensionalK-vector spaceV is a freeOv-module of rank two
that spansV as a vector space. The groupK∗ acts on the set of lattices inV by
homothety . We denote byT the set of equivalence classes, that isL∼L′ iﬀ there
exists x∈ K∗ such thatL′ =xL.
We are going to deﬁne an integer-valued distance onT. We ﬁx a latticeL together
with a basis ofL, say{e,f}. For any class[L′]∈T one can express a basis ofL′∈ [L′]
as{ae +bf,ce +df} with a,b,c,d ∈ K; and up to homothety, we can pick in fact
a,b,c,d ∈O v, that isL′⊂ L. Assumea has minimal valuation among{a,b,c,d },
then the matrix(a b
c d) can be transformed into
(
a 0
0 d−bc
a
)
by SL2(Ov) right and left
multiplication that preserves the standard latticeO2
v. HenceL′≃aOv⊕(d−bc
a )Ov≃
tnOv⊕tmOv for somen,m∈ N. We deﬁned([L], [L′]) =|n−m|, and one can check
29
that it deﬁnes a distance that does depend only on[L] and [L′].
This distance turnsT into a graph whose vertices are classes of lattices[L] such
that vertices at distance 1 are linked by an edge. This graph is connected since
any two vertices admit representativesL,L′ such that L = Ov⊕O v and L′ =
Ov⊕td([L],[L′])Ov, hence a path joiningL toL′ can be constructed asLk =Ov⊕tkOv
with k = 0,...,d ([L], [L′]). In fact it can be shown thatT is a tree, see [SB77].
